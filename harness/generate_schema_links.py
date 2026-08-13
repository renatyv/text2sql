#!/usr/bin/env python3
"""Generate conservative, reproducible schema-link hints from MySQL metadata."""
from __future__ import annotations

import argparse
import os
import subprocess
from collections import defaultdict

from . import config


def _mysql(database: str, sql: str) -> list[tuple[str, ...]]:
    env = dict(os.environ, MYSQL_PWD=config.MYSQL_PWD)
    result = subprocess.run(
        ["mysql", "--skip-ssl", "--protocol=TCP", "-N", "-B", "-h", config.MYSQL_HOST,
         "-P", str(config.MYSQL_PORT), "-u", config.MYSQL_USER, database, "-e", sql],
        capture_output=True, text=True, check=True, env=env,
    )
    return [tuple(line.split("\t")) for line in result.stdout.splitlines() if line]


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
    by_name: dict[str, list[str]] = defaultdict(list)
    for table, column in columns:
        if column not in {"id", "created_at", "updated_at", "deleted_at"}:
            by_name[column].append(f"{table}.{column}")

    lines = ["# Schema Links", "", "- generator: local information_schema", "- dialect: mysql",
             f"- database: {database}", "", "## Declared Links", ""]
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


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--database", choices=list(config.DATASETS), default="neutron")
    args = parser.parse_args(argv)
    config.SCHEMA_LINKS_DIR.mkdir(exist_ok=True)
    config.schema_links_path(args.database).write_text(
        generate(config.mysql_db_for(args.database)), encoding="utf-8"
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
