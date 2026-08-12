"""Extract the final SQL statement from model/agent output."""
from __future__ import annotations

import re

_FENCE_RE = re.compile(r"```(?:sql|SQL|mysql|MySQL)?\s*\n(.*?)```", re.DOTALL)
# A "FINAL" tag optionally wraps the intended answer block.
_FINAL_RE = re.compile(r"FINAL[:\s]*```", re.IGNORECASE)


def extract_sql(text: str) -> str | None:
    """Pull the single best SQL candidate out of free-form model output.

    Strategy (first hit wins):
      1. The last ```sql``` fenced block appearing after a FINAL marker, if any.
      2. The last fenced block overall.
      3. The longest ;-terminated statement in raw text.

    Returns None when nothing plausible is found.
    """
    if not text:
        return None

    # 1. FINAL-tagged fenced block.
    final_match = _FINAL_RE.search(text)
    if final_match:
        tail = text[final_match.start():]
        blocks = [m.group(1) for m in _FENCE_RE.finditer(tail)]
        if blocks:
            return _clean(blocks[-1])

    # 2. Any fenced block (prefer the last one — usually the final answer).
    blocks = [m.group(1) for m in _FENCE_RE.finditer(text)]
    if blocks:
        return _clean(blocks[-1])

    # 3. Raw text: take the longest ;-terminated statement.
    stmts = [s.strip() for s in text.split(";") if s.strip()]
    stmts = [s for s in stmts if _looks_like_sql(s)]
    if stmts:
        return _clean(max(stmts, key=len))

    return None


def _looks_like_sql(s: str) -> bool:
    head = s.lstrip()[:12].upper()
    return any(head.startswith(k) for k in ("SELECT", "WITH", "(")) or head.startswith("(SELECT")


def _clean(sql: str) -> str:
    sql = sql.strip()
    # Strip leading commentary / labels the model sometimes adds.
    sql = re.sub(r"^\s*--[^\n]*\n", "", sql)
    return sql.strip().rstrip(";").strip() + ";"


_READ_ONLY_PREFIXES = ("SELECT", "WITH", "(")


def last_select(sqls: list[str]) -> str | None:
    """Return the last read-only (SELECT/WITH) statement from a list.

    Used to recover an answer candidate from the agent's executed sql_exec calls
    when the final assistant text carries no fenced SQL (e.g. turn-cap abort).
    """
    for s in reversed(sqls or []):
        head = s.lstrip()[:12].upper()
        if any(head.startswith(p) for p in _READ_ONLY_PREFIXES) or head.startswith("(SELECT"):
            return _clean(s)
    return None
