"""Execution accuracy scorer (Spider/BEAVER-style ETE).

Runs the gold and predicted SQL on the live MySQL DB and compares result sets.
"""
from __future__ import annotations

import re
from collections import Counter
from decimal import Decimal
from datetime import date, datetime

from . import config, mysql_io


def score_prediction(pred_sql: str | None, gold_sql: str, database: str) -> dict:
    """Return a scoring record for one question.

    Fields:
      correct          : bool — execution accuracy (primary metric)
      valid_sql        : bool — pred produced a runnable result set
      pred_error       : str|None
      gold_error       : str|None  (when gold itself fails, scoring is unreliable)
      timed_out        : bool
      pred_rows        : int
      gold_rows        : int
      ordered          : bool — whether ordered comparison was used
      query_shape      : str  — structural class of the *gold* query (window/
                                rollup/set_op/cte/simple); a question property,
                                identical across arms, used for stratification.
      error_class      : str  — diagnostic label (see _classify_error)
      cardinality_ratio: float|None — pred_rows / gold_rows
      cardinality_direction : "over"|"under"|"exact"|None
      struct_diff      : list[str] — structural signals detected (pred vs gold)
      gold_sql         : str  — the gold SQL as executed (for debugging/rescoring)
      pred_sql         : str|None — the SQL that was scored
    """
    rec: dict = {
        "correct": False, "valid_sql": False, "pred_error": None, "gold_error": None,
        "timed_out": False, "pred_rows": None, "gold_rows": None, "ordered": False,
        "gold_sql": gold_sql, "pred_sql": pred_sql,
        "query_shape": classify_query_shape(gold_sql),
    }

    gold = mysql_io.execute(gold_sql, database)
    if gold.timed_out:
        rec["gold_error"] = "gold query timed out"
        return rec
    if gold.error:
        rec["gold_error"] = gold.error
        return rec
    rec["gold_rows"] = len(gold.rows or [])

    if not pred_sql:
        rec["pred_error"] = "no SQL extracted"
        _add_cardinality_diagnostics(rec)
        rec["error_class"] = "not_runnable"
        return rec

    pred = mysql_io.execute(pred_sql, database)
    if pred.timed_out:
        rec["timed_out"] = True
        rec["pred_error"] = "predicted query timed out"
        _add_cardinality_diagnostics(rec)
        rec["error_class"] = "timeout"
        return rec
    if pred.error:
        rec["pred_error"] = pred.error
        _add_cardinality_diagnostics(rec)
        err = (rec["pred_error"] or "").lower()
        if "syntax" in err or "you have an error" in err or "near " in err:
            rec["error_class"] = "syntax"
        elif "unknown column" in err or "unknown table" in err or "doesn't exist" in err:
            rec["error_class"] = "wrong_table_or_column"
        else:
            rec["error_class"] = "not_runnable"
        return rec
    rec["valid_sql"] = True
    rec["pred_rows"] = len(pred.rows or [])

    ordered = _has_order_by(gold_sql)
    rec["ordered"] = ordered
    rec["correct"] = _compare(gold.rows, pred.rows, ordered)
    _add_cardinality_diagnostics(rec)
    rec["error_class"] = "correct" if rec["correct"] else _classify_error(rec, pred_sql, gold_sql)
    return rec


def _add_cardinality_diagnostics(rec: dict) -> None:
    """Attach cardinality ratio and direction to a scoring record."""
    g, p = rec.get("gold_rows"), rec.get("pred_rows")
    rec["cardinality_ratio"] = round(p / g, 4) if (g and p and g > 0) else None
    if g is None or p is None:
        rec["cardinality_direction"] = None
    elif p > g:
        rec["cardinality_direction"] = "over"
    elif p < g:
        rec["cardinality_direction"] = "under"
    else:
        rec["cardinality_direction"] = "exact"


def _classify_error(rec: dict, pred_sql: str, gold_sql: str) -> str:
    """Diagnostic error taxonomy for runnable-but-wrong predictions.

    ``error_class`` only reports an observable execution outcome. SQL-shape
    differences are useful diagnostics, but cannot establish the cause: an
    equivalent rewrite may use no GROUP BY or different aggregates. Those
    non-causal signals are kept in ``struct_diff``.
    """
    rec["struct_diff"] = _struct_diff(pred_sql, gold_sql)
    if rec.get("pred_rows") == 0:
        return "empty_result"
    if rec.get("pred_rows") != rec.get("gold_rows"):
        return "wrong_cardinality"
    return "wrong_result"


def _struct_diff(pred_sql: str, gold_sql: str) -> list[str]:
    """Return non-causal textual differences between pred and gold SQL."""
    signals: list[str] = []
    if _has_clause(gold_sql, r"GROUP\s+BY") and not _has_clause(pred_sql, r"GROUP\s+BY"):
        signals.append("missing_group_by")
    if _has_clause(gold_sql, r"ORDER\s+BY") and not _has_clause(pred_sql, r"ORDER\s+BY"):
        signals.append("missing_order_by")
    if _has_clause(gold_sql, r"LIMIT\b") and not _has_clause(pred_sql, r"LIMIT\b"):
        signals.append("missing_limit")
    if _aggregates_used(gold_sql) and _aggregates_used(pred_sql) != _aggregates_used(gold_sql):
        signals.append("different_aggregates")
    return signals


# ---------------------------------------------------------------------------
# SQL structural helpers (lightweight, dependency-free)
# ---------------------------------------------------------------------------
# All operate on SQL with string/identifier literals stripped so keywords
# embedded in data (e.g. a tenant id containing "order") don't trip detection.
def _strip_literals(sql: str) -> str:
    """Remove string and quoted-identifier literals so keyword detection is robust."""
    s = re.sub(r"'[^']*'", "''", sql, flags=re.DOTALL)
    s = re.sub(r'"[^"]*"', '""', s, flags=re.DOTALL)
    s = re.sub(r"`[^`]*`", "``", s, flags=re.DOTALL)
    return s


def _has_clause(sql: str, clause: str) -> bool:
    """True if SQL contains the given keyword/phrase (word-boundary, case-insensitive)."""
    return bool(re.search(rf"\b{clause}\b", _strip_literals(sql), re.IGNORECASE))


_AGG_RE = re.compile(r"\b(COUNT|SUM|AVG|MIN|MAX|STDDEV|STDDEV_POP|STDDEV_SAMP|VAR_POP|VAR_SAMP|GROUP_CONCAT)\s*\(", re.IGNORECASE)


def _aggregates_used(sql: str) -> set[str]:
    return {m.group(1).upper() for m in _AGG_RE.finditer(_strip_literals(sql))}


def _has_order_by(sql: str) -> bool:
    return _has_clause(sql, r"ORDER\s+BY")


# Strongest-first: a window query that also uses a CTE is classified by its
# hardest feature (window), since that's the dominant difficulty driver.
_SHAPE_RULES: tuple[tuple[str, str], ...] = (
    ("window", r"\bOVER\s*\("),                 # window functions — hardest, most common here
    ("rollup", r"\bWITH\s+ROLLUP\b"),
    ("set_op", r"\b(?:UNION|INTERSECT|EXCEPT)\b"),
    ("cte", r"\bWITH\s+\w+\s+AS\s*\("),         # non-recursive CTE
)


def classify_query_shape(sql: str) -> str:
    """Coarse structural class of a query, derived from its SQL.

    A property of the *question* (computed from gold), used to partition the
    benchmark by difficulty. Ordered strongest-first so the hardest feature
    wins (e.g. a CTE containing a window function is `window`, not `cte`).
    """
    s = _strip_literals(sql)
    for label, pat in _SHAPE_RULES:
        if re.search(pat, s, re.IGNORECASE):
            return label
    return "simple"


# ---------------------------------------------------------------------------
# comparison helpers
# ---------------------------------------------------------------------------


def _normalize_cell(v):
    if v is None:
        return None
    if isinstance(v, bool):
        return int(v)
    if isinstance(v, Decimal):
        return float(v)
    if isinstance(v, (datetime, date)):
        return v.isoformat()
    if isinstance(v, (bytes, bytearray)):
        try:
            return v.decode("utf-8")
        except Exception:
            return v.decode("latin-1", errors="replace")
    return v


def _rows_equal(a: tuple, b: tuple) -> bool:
    if len(a) != len(b):
        return False
    for x, y in zip(a, b):
        x, y = _normalize_cell(x), _normalize_cell(y)
        if isinstance(x, (int, float)) and isinstance(y, (int, float)):
            if abs(x - y) > 1e-6 * max(1.0, abs(x), abs(y)):
                return False
        elif x != y:
            return False
    return True


def _compare(gold: list[tuple] | None, pred: list[tuple] | None, ordered: bool) -> bool:
    gold = gold or []
    pred = pred or []
    if len(gold) != len(pred):
        return False
    if ordered:
        return all(_rows_equal(g, p) for g, p in zip(gold, pred))
    # multiset comparison: O(n^2) worst case, but n is small per question.
    pending = list(pred)
    for g in gold:
        for i, p in enumerate(pending):
            if _rows_equal(g, p):
                pending.pop(i)
                break
        else:
            return False
    return not pending


# quick self-test: python -m harness.scorer
if __name__ == "__main__":
    db = config.mysql_db_for("neutron")
    # sanity: a query vs itself
    q = "SELECT COUNT(*) FROM neutron.SUBNETS;"
    print("self-consistency:", score_prediction(q, q, db))
    # mismatched count
    print("wrong count:", score_prediction("SELECT 1;", "SELECT COUNT(*) FROM neutron.SUBNETS;", db))
