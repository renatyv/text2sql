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
    """
    rec: dict = {
        "correct": False, "valid_sql": False, "pred_error": None, "gold_error": None,
        "timed_out": False, "pred_rows": None, "gold_rows": None, "ordered": False,
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
        return rec

    pred = mysql_io.execute(pred_sql, database)
    if pred.timed_out:
        rec["timed_out"] = True
        rec["pred_error"] = "predicted query timed out"
        return rec
    if pred.error:
        rec["pred_error"] = pred.error
        return rec
    rec["valid_sql"] = True
    rec["pred_rows"] = len(pred.rows or [])

    ordered = _has_order_by(gold_sql)
    rec["ordered"] = ordered
    rec["correct"] = _compare(gold.rows, pred.rows, ordered)
    rec["error_class"] = "correct" if rec["correct"] else _classify_error(rec, gold_sql)
    return rec


def _classify_error(rec: dict, gold_sql: str) -> str:
    """Coarse error taxonomy (plan §Metrics): sampled manually later, but a
    cheap heuristic label helps triage."""
    if rec.get("timed_out"):
        return "timeout"
    err = (rec.get("pred_error") or "").lower()
    if not rec.get("valid_sql"):
        if "syntax" in err or "you have an error" in err or "near " in err:
            return "syntax"
        if "unknown column" in err or "unknown table" in err or "doesn't exist" in err:
            return "wrong_table_or_column"
        return "not_runnable"
    # runnable but wrong result
    if rec.get("pred_rows") == 0:
        return "empty_result"
    if (rec.get("gold_rows") or 0) > 0 and (rec.get("pred_rows") or 0) != rec.get("gold_rows"):
        return "wrong_cardinality"
    return "wrong_result"


# ---------------------------------------------------------------------------
# comparison helpers
# ---------------------------------------------------------------------------
def _has_order_by(sql: str) -> bool:
    # Strip string literals so the word "order" inside them doesn't trip us.
    stripped = re.sub(r"'[^']*'", "''", sql, flags=re.DOTALL)
    stripped = re.sub(r'"[^"]*"', '""', stripped, flags=re.DOTALL)
    return bool(re.search(r"\bORDER\s+BY\b", stripped, re.IGNORECASE))


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
