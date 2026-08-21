"""SQLite helpers for the scorer and loaders (BIRD / Spider 2.0 run natively
on their original .sqlite files — nothing is loaded into MySQL).

Mirrors mysql_io.execute(): fresh read-only connection per call, tuple rows,
wall-clock watchdog so one runaway query cannot stall a run.
"""
from __future__ import annotations

import sqlite3
import threading
from pathlib import Path

from . import config
from .mysql_io import QueryResult  # shared result shape


def connect(db_path: str | Path):
    """Open the database read-only (URI mode; the file is never writable)."""
    path = Path(db_path)
    return sqlite3.connect(f"file:{path}?mode=ro", uri=True, timeout=5)


def execute(sql: str, db_path: str | Path, timeout: float | None = None) -> QueryResult:
    """Execute SQL and return tuple rows, bounded by a wall-clock thread."""
    timeout = timeout or config.MYSQL_QUERY_TIMEOUT
    result: QueryResult = QueryResult(None, None, False)

    def _run():
        try:
            conn = connect(db_path)
            try:
                cur = conn.cursor()
                cur.execute("PRAGMA query_only = ON")
                cur.execute(sql)
                result.columns = len(cur.description or ())
                result.rows = [tuple(r) for r in cur.fetchall()]
            finally:
                conn.close()
        except sqlite3.OperationalError as e:
            msg = str(e)
            if "interrupted" in msg.lower():
                result.timed_out = True
            else:
                result.error = msg
        except Exception as e:  # syntax errors, missing tables, etc.
            result.error = f"{type(e).__name__}: {e}"

    t = threading.Thread(target=_run, daemon=True)
    t.start()
    t.join(timeout + 5)  # grace beyond the budget, mirroring mysql_io
    if t.is_alive():
        result.timed_out = True
        result.rows = None
    return result
