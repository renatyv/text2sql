"""Faithful port of the official Spider 2.0-lite evaluation for
SQL-result-vs-gold-CSV scoring (evaluation_suite/evaluate.py::
compare_pandas_table / compare_multi_pandas_table), without pandas.

Semantics preserved from the official evaluator:
  * comparison is COLUMN-wise: every gold column (vector of cell values) must
    match some predicted column — extra predicted columns are allowed;
  * `condition_cols` restricts which gold CSV column indices must match;
  * numeric cells compare with math.isclose(abs_tol=1e-2); everything else
    compares exactly (case-sensitive, no stripping);
  * missing cells (NaN in pandas) normalize to 0 before comparison;
  * `ignore_order` sorts both vectors first (official sort key kept verbatim);
  * multiple gold CSVs are an any-of match, with per-gold condition_cols;
  * a gold CSV with zero rows scores 1 vacuously (official quirk).

Both sides emulate the official CSV round-trip (df.to_csv -> pd.read_csv):
values are stringified, then whole columns are coerced to numbers only when
every non-empty cell parses — mirroring pandas' per-column dtype inference.
"""
from __future__ import annotations

import csv
import math
from functools import lru_cache
from pathlib import Path

TOLERANCE = 1e-2


def _isna(v) -> bool:
    return v is None or (isinstance(v, float) and math.isnan(v))


def _coerce_column(values: list[str | None]) -> list:
    """pd.read_csv-like column inference: numeric only if the whole column
    parses; empty cells become None (NaN upstream)."""
    non_empty = [v for v in values if v not in (None, "")]
    if not non_empty:
        return [None] * len(values)
    try:
        return [None if v in (None, "") else float(v) for v in values]
    except (TypeError, ValueError):
        return [None if v in (None, "") else v for v in values]


@lru_cache(maxsize=None)
def load_gold_csv(path: str) -> list[list]:
    """Gold CSV as a list of columns with pandas-like per-column typing."""
    with open(path, newline="", encoding="utf-8") as f:
        rows = list(csv.reader(f))
    if not rows:
        return []
    header, body = rows[0], rows[1:]
    columns = [[row[i] if i < len(row) else "" for row in body]
               for i in range(len(header))]
    return [_coerce_column(col) for col in columns]


def _stringify_cell(v) -> str:
    """df.to_csv stringification of a SQL result cell."""
    if v is None:
        return ""
    if isinstance(v, float):
        return repr(v)  # to_csv writes 1.0 as "1.0", 1.5 as "1.5"
    return str(v)


def pred_columns(rows: list[tuple]) -> list[list]:
    """Predicted SQL rows as columns, after emulating the CSV round-trip.

    A SELECT always yields at least one column, and the official evaluator's
    pandas round-trip keeps the header — so zero rows still produce one empty
    column vector (this is what makes a 0-row prediction match a header-only
    gold CSV)."""
    if not rows:
        return [[]]
    ncols = max(len(r) for r in rows)
    columns = []
    for i in range(ncols):
        cells = [_stringify_cell(row[i] if i < len(row) else None) for row in rows]
        columns.append(_coerce_column(cells))
    return columns


def _normalize(v):
    """Official normalize(): NaN -> 0 before vector comparison."""
    return 0 if _isna(v) else v


def _sort_key(x):
    # official sort key, verbatim
    return (x is None, str(x), isinstance(x, (int, float)))


def _vectors_match(v1: list, v2: list, ignore_order: bool = False,
                   tol: float = TOLERANCE) -> bool:
    v1 = [_normalize(x) for x in v1]
    v2 = [_normalize(x) for x in v2]
    if ignore_order:
        v1 = sorted(v1, key=_sort_key)
        v2 = sorted(v2, key=_sort_key)
    if len(v1) != len(v2):
        return False
    for a, b in zip(v1, v2):
        if _isna(a) and _isna(b):
            continue
        if isinstance(a, (int, float)) and isinstance(b, (int, float)):
            if not math.isclose(float(a), float(b), abs_tol=tol):
                return False
        elif a != b:
            return False
    return True


def _compare(pred_cols: list[list], gold_cols: list[list],
             condition_cols, ignore_order: bool) -> int:
    if condition_cols:
        if not isinstance(condition_cols, (list, tuple)):
            condition_cols = [condition_cols]
        try:
            gold_cols = [gold_cols[i] for i in condition_cols]
        except (IndexError, TypeError):
            return 0
    for gold_vector in gold_cols:
        if not any(_vectors_match(gold_vector, p, ignore_order)
                   for p in pred_cols):
            return 0
    return 1


def _conditions_by_gold(count: int, condition_cols) -> list:
    if count == 1:
        return [condition_cols]
    if condition_cols in (None, [], [[]], [None]):
        return [[] for _ in range(count)]
    if (not isinstance(condition_cols, (list, tuple))
            or not all(isinstance(c, list) for c in condition_cols)):
        return [condition_cols for _ in range(count)]
    return list(condition_cols)


def _unmatched(pred_cols: list[list], gold_cols: list[list], condition_cols,
               ignore_order: bool) -> list[list]:
    if condition_cols:
        if not isinstance(condition_cols, (list, tuple)):
            condition_cols = [condition_cols]
        try:
            gold_cols = [gold_cols[i] for i in condition_cols]
        except (IndexError, TypeError):
            return gold_cols
    return [gold for gold in gold_cols
            if not any(_vectors_match(gold, pred, ignore_order) for pred in pred_cols)]


def score_pred_details(pred_rows: list[tuple], gold_csv_paths: list[str | Path],
                       condition_cols=None, ignore_order: bool = False) -> dict:
    """Score plus diagnostics for the matching (or closest) gold variant."""
    paths = [str(p) for p in gold_csv_paths]
    if not paths:
        return {"correct": 0, "selected_index": None, "condition_cols": condition_cols,
                "unmatched_gold_columns": []}
    pred_cols = pred_columns(pred_rows)
    variants = []
    for index, (path, cols) in enumerate(zip(paths, _conditions_by_gold(len(paths), condition_cols))):
        gold_cols = load_gold_csv(path)
        variants.append({
            "correct": _compare(pred_cols, gold_cols, cols, ignore_order),
            "selected_index": index,
            "condition_cols": cols,
            "unmatched_gold_columns": _unmatched(pred_cols, gold_cols, cols, ignore_order),
        })
    return next((v for v in variants if v["correct"]),
                min(variants, key=lambda v: len(v["unmatched_gold_columns"])))


def score_pred(pred_rows: list[tuple], gold_csv_paths: list[str | Path],
               condition_cols=None, ignore_order: bool = False) -> int:
    """Score predicted rows against one-or-more gold CSVs (any-of)."""
    return score_pred_details(pred_rows, gold_csv_paths, condition_cols,
                              ignore_order)["correct"]
