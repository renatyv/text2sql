#!/usr/bin/env python3
"""Generate conservative, reproducible schema-link hints from DB metadata.

MySQL datasets introspect information_schema (one file per schema); SQLite
datasets (BIRD / Spider 2.0) introspect the original .sqlite files via PRAGMAs,
one schema-links file per database, keyed by the question profile key."""
from __future__ import annotations

import argparse
import json
import os
import sqlite3
import subprocess
from collections import defaultdict
from pathlib import Path

from . import config


def _mysql(database: str, sql: str) -> list[tuple[str, ...]]:
    env = dict(os.environ, MYSQL_PWD=config.MYSQL_PWD)
    result = subprocess.run(
        ["mysql", "--skip-ssl", "--protocol=TCP", "-N", "-B", "-h", config.MYSQL_HOST,
         "-P", str(config.MYSQL_PORT), "-u", config.MYSQL_USER, database, "-e", sql],
        capture_output=True, text=True, check=True, env=env,
    )
    return [tuple(line.split("\t")) for line in result.stdout.splitlines() if line]


def _render(database: str, dialect: str, foreign_keys: list[tuple[str, str, str, str]],
            columns: list[tuple[str, str]]) -> str:
    by_name: dict[str, list[str]] = defaultdict(list)
    for table, column in columns:
        if column not in {"id", "created_at", "updated_at", "deleted_at"}:
            by_name[column].append(f"{table}.{column}")

    lines = ["# Schema Links", "", "- generator: local introspection",
             f"- dialect: {dialect}", f"- database: {database}", "",
             "## Declared Links", ""]
    if foreign_keys:
        for table, column, ref_table, ref_column in foreign_keys:
            lines.append(f"- `{table}.{column}` → `{ref_table}.{ref_column}`")
    else:
        lines.append("- No declared foreign keys.")
    lines += ["", "## Same-name Candidates", ""]
    for name, refs in by_name.items():
        if len(refs) > 1:
            lines.append(f"- `{name}`: " + ", ".join(f"`{ref}`" for ref in refs))
    return "\n".join(lines) + "\n"


def generate(database: str) -> str:
    foreign_keys = _mysql(database, """
        SELECT table_name, column_name, referenced_table_name, referenced_column_name
        FROM information_schema.key_column_usage
        WHERE table_schema = DATABASE() AND referenced_table_name IS NOT NULL
        ORDER BY referenced_table_name, referenced_column_name, table_name, column_name
    """)
    columns = _mysql(database, """
        SELECT table_name, column_name
        FROM information_schema.columns
        WHERE table_schema = DATABASE()
        ORDER BY column_name, table_name
    """)
    return _render(database, "mysql", foreign_keys, columns)


def _sqlite_introspect(db_path: Path) -> tuple[list[tuple[str, str, str, str]], list[tuple[str, str]]]:
    conn = sqlite3.connect(f"file:{db_path}?mode=ro", uri=True)
    try:
        tables = [r[0] for r in conn.execute(
            "SELECT name FROM sqlite_master WHERE type='table' AND name NOT LIKE 'sqlite_%' "
            "ORDER BY name")]
        foreign_keys: list[tuple[str, str, str, str]] = []
        columns: list[tuple[str, str]] = []
        for table in tables:
            quoted = table.replace('"', '""')
            columns += [(table, row[1]) for row in conn.execute(f'PRAGMA table_info("{quoted}")')]
            for row in conn.execute(f'PRAGMA foreign_key_list("{quoted}")'):
                # (id, seq, ref_table, from, to, ...) reshaped to the MySQL tuple order
                foreign_keys.append((table, row[3], row[2], row[4] or "rowid"))
        return sorted(foreign_keys), sorted(columns, key=lambda tc: (tc[1], tc[0]))
    finally:
        conn.close()


def generate_sqlite_dataset(db_label: str) -> list[Path]:
    """One schema-links file per database used by the dataset's questions."""
    dev = config.DATA_DIR / db_label / "dev.json"
    questions = json.loads(dev.read_text(encoding="utf-8"))
    profile_keys = {q["db"]: q["profile"] for q in questions}
    written = []
    for db_rel, key in sorted(profile_keys.items()):
        db_path = config.sqlite_db_path(db_rel)
        foreign_keys, columns = _sqlite_introspect(db_path)
        target = config.schema_links_path_for(key)
        target.write_text(_render(db_path.stem, "sqlite", foreign_keys, columns),
                          encoding="utf-8")
        written.append(target)
    return written


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--database", choices=list(config.DATASETS), default="neutron")
    args = parser.parse_args(argv)
    config.SCHEMA_LINKS_DIR.mkdir(exist_ok=True)
    if config.engine_for(args.database) == "sqlite":
        for path in generate_sqlite_dataset(args.database):
            print(f"[schema-links] wrote {path}")
        return 0
    config.schema_links_path(args.database).write_text(
        generate(config.mysql_db_for(args.database)), encoding="utf-8"
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
