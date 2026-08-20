#!/usr/bin/env python3
"""Generate schema-link reports with schema-linker.

MySQL datasets are linked one schema at a time. SQLite datasets (BIRD / Spider
2.0) are linked from their original read-only .sqlite files, one report per
question profile key.
"""
from __future__ import annotations

import argparse
import json
from pathlib import Path

from schema_linker import SchemaLinkOptions, link_schema
from schema_linker.progress import ProgressBar
from sqlalchemy import URL, create_engine
from sqlalchemy.engine import Engine

from . import config


def _link(engine: Engine) -> str:
    progress_bar = ProgressBar("Linking", 0)

    def show_progress(current: int, total: int, item: str) -> None:
        nonlocal progress_bar
        if progress_bar.total != total:
            progress_bar.finish()
            progress_bar = ProgressBar("Linking", total)
            progress_bar.start(item)
            return
        progress_bar.update(current, item)

    try:
        report = link_schema(
            engine, SchemaLinkOptions(show_declared_links=True), progress=show_progress
        )
        progress_bar.finish("Schema linking complete")
        return report
    except Exception:
        progress_bar.finish()
        raise
    finally:
        engine.dispose()


def _link_sqlite(db_path: Path) -> str:
    return _link(create_engine(URL.create(
        "sqlite+pysqlite", database=f"file:{db_path.resolve()}",
        query={"mode": "ro", "uri": "true"},
    )))


def generate(database: str) -> str:
    return _link(create_engine(URL.create(
        "mysql+pymysql", username=config.MYSQL_USER, password=config.MYSQL_PWD,
        host=config.MYSQL_HOST, port=config.MYSQL_PORT, database=database,
    )))


def generate_sqlite_dataset(db_label: str) -> list[Path]:
    """Write one schema-links report per database used by the dataset."""
    dev = config.DATA_DIR / db_label / "dev.json"
    questions = json.loads(dev.read_text(encoding="utf-8"))
    profile_keys = {q["db"]: q["profile"] for q in questions}
    written = []
    for db_rel, key in sorted(profile_keys.items()):
        target = config.schema_links_path_for(key)
        target.write_text(_link_sqlite(config.sqlite_db_path(db_rel)), encoding="utf-8")
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
