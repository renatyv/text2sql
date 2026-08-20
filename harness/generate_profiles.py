#!/usr/bin/env python3
"""Run db-snooper to (re)generate profiles.

MySQL datasets profile their single schema; SQLite benchmarks (BIRD /
Spider 2.0) profile each original .sqlite file. db-snooper writes every
SQLite profile as `main.md` (the schema name), so each run targets a temp
dir and the result is renamed to the question profile key
(profiles/bird_<db_id>.md, profiles/sp2_<db>.md).

The benchmark .sqlite files are never ANALYZEd or otherwise mutated: each
one is copied to the temp dir and the copy is ANALYZEd before profiling, so
sqlite_stat1 exists and db-snooper can classify large tables from catalog
stats instead of running unbounded per-column scans over them (its query
timeout does not bind SQLite). Tables at/above --large-table-threshold rows
are profiled from stats only; existing profiles are skipped unless --force."""
from __future__ import annotations

import argparse
import json
import shutil
import sqlite3
import subprocess
import tempfile
from pathlib import Path

from . import config

# below this: full dump/sampling; at/above: catalog-stats only (see docstring)
LARGE_TABLE_THRESHOLD = 200_000


def _sqlite_profile_pairs(db_label: str) -> list[tuple[Path, str]]:
    dev = config.DATA_DIR / db_label / "dev.json"
    questions = json.loads(dev.read_text(encoding="utf-8"))
    return sorted({(config.sqlite_db_path(q["db"]), q["profile"]) for q in questions})


def run_sqlite(db_path: Path, profile_key: str, force: bool = False) -> Path | None:
    target = config.profile_path_for(profile_key)
    if target.is_file() and not force:
        return None
    with tempfile.TemporaryDirectory(prefix="dbsnoop-") as temp:
        analyzed = Path(temp) / db_path.name
        shutil.copyfile(db_path, analyzed)
        conn = sqlite3.connect(analyzed)
        try:
            conn.execute("ANALYZE")
            conn.commit()
        finally:
            conn.close()
        subprocess.run(
            ["db-snooper", "profile", "--db-type", "sqlite",
             "--database", str(analyzed),
             "--large-table-threshold", str(LARGE_TABLE_THRESHOLD),
             "--output", temp],
            check=True,
        )
        produced = Path(temp) / "main.md"
        if not produced.is_file():
            raise RuntimeError(f"db-snooper produced no profile for {db_path}")
        target.parent.mkdir(exist_ok=True)
        target.write_text(produced.read_text(encoding="utf-8"), encoding="utf-8")
    return target


def run_mysql(db_label: str) -> Path:
    subprocess.run(
        ["db-snooper", "profile", "--db-type", "mysql",
         "--database", config.mysql_db_for(db_label),
         "--host", config.MYSQL_HOST, "--port", str(config.MYSQL_PORT),
         "--user", config.MYSQL_USER, "--password", config.MYSQL_PWD,
         "--output", str(config.PROFILES_DIR)],
        check=True,
    )
    return config.profile_path(db_label)


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--database", choices=list(config.DATASETS), default="neutron")
    parser.add_argument("--force", action="store_true",
                        help="SQLite benchmarks: regenerate existing profiles too")
    args = parser.parse_args(argv)
    if config.engine_for(args.database) == "sqlite":
        for db_path, profile_key in _sqlite_profile_pairs(args.database):
            target = run_sqlite(db_path, profile_key, force=args.force)
            print(f"[profiles] {db_path.name} -> "
                  f"{target if target else config.profile_path_for(profile_key) + ' (exists, skipped)'}")
        return 0
    print(f"[profiles] {config.mysql_db_for(args.database)} -> {run_mysql(args.database)}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
