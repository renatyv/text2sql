#!/usr/bin/env python3
"""Build the Spider 2.0-lite (SQLite subset) dataset for the harness.

Filters the official spider2-lite task list to the 135 SQLite (`local*`)
instances, stages their original .sqlite databases and the official gold
CSVs, and normalizes everything into data/sp2_lite_sqlite/dev.json. Nothing
is loaded into MySQL — agents, gold SQL (where released) and scoring all run
on the original SQLite files, and scoring uses the official gold-CSV fuzzy
comparison (ported in harness/spider2_eval.py).

Inputs (see README for the exact commands):
  --repo     a checkout/sparse-clone of https://github.com/xlang-ai/Spider2
             (needs spider2-lite/spider2-lite.jsonl, evaluation_suite/gold/,
             resource/documents/)
  --dbs-zip  the official "local database" archive (30 .sqlite files), from
             the spider2-lite README's Google Drive link; or --dbs-dir with
             the files already extracted

Layout produced:
  data/sp2_lite_sqlite/
    dev.json                       # normalized questions (internal schema)
    databases/<db>.sqlite          # original SQLite databases
    gold/<instance>.csv[_a|_b|..]  # official gold result CSVs
    gold_sql/<instance>.sql        # released gold SQL (partial, 24 tasks)
"""
from __future__ import annotations

import argparse
import json
import shutil
import sqlite3
import sys
import zipfile
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(REPO_ROOT))

from harness import config  # noqa: E402

DATASET = "sp2_lite_sqlite"


def _stage_databases(zip_path: Path | None, dbs_dir: Path | None, out_dir: Path,
                     needed: set[str]) -> dict[str, Path]:
    """Copy the needed .sqlite files into data/<dataset>/databases/.

    Returns a lower-cased db-name -> staged-file map (Spider2 naming is
    inconsistent about case: 'sqlite-sakila' vs 'SQLITE_SAKILA')."""
    dest_root = out_dir / "databases"
    dest_root.mkdir(parents=True, exist_ok=True)
    staged: dict[str, Path] = {}

    def stage(name: str, source) -> Path:
        target = dest_root / f"{name}.sqlite"
        if not target.exists():
            with source() as src, open(target, "wb") as dst:
                shutil.copyfileobj(src, dst)
        staged[name.lower()] = target
        return target

    if zip_path is not None:
        with zipfile.ZipFile(zip_path) as zf:
            members = {Path(m).stem.lower(): m for m in zf.namelist()
                       if m.endswith(".sqlite")}
            for db in sorted(needed):
                member = members.get(db.lower())
                if member is None:
                    continue
                stage(Path(member).stem, lambda m=member: zf.open(m))
    else:
        wanted = {d.lower() for d in needed}
        for f in sorted(dbs_dir.glob("*.sqlite")):
            if f.stem.lower() in wanted:
                stage(f.stem, lambda p=f: open(p, "rb"))
    return staged


def _verify_sqlite(path: Path) -> int:
    conn = sqlite3.connect(f"file:{path}?mode=ro", uri=True)
    try:
        return int(conn.execute(
            "SELECT COUNT(*) FROM sqlite_master WHERE type='table'").fetchone()[0])
    finally:
        conn.close()


def build(repo: Path, dbs_zip: Path | None, dbs_dir: Path | None, force: bool) -> None:
    out_dir = config.DATA_DIR / DATASET
    dev_json = out_dir / "dev.json"
    if dev_json.exists() and not force:
        print(f"[sp2] {dev_json} exists (use --force to rebuild)")
        return

    lite_jsonl = repo / "spider2-lite" / "spider2-lite.jsonl"
    eval_jsonl = (repo / "spider2-lite" / "evaluation_suite" / "gold"
                  / "spider2lite_eval.jsonl")
    exec_result = repo / "spider2-lite" / "evaluation_suite" / "gold" / "exec_result"
    gold_sql_dir = repo / "spider2-lite" / "evaluation_suite" / "gold" / "sql"
    documents = repo / "spider2-lite" / "resource" / "documents"
    for required in (lite_jsonl, eval_jsonl, exec_result):
        if not required.exists():
            raise SystemExit(f"[sp2] missing {required} — pass --repo with a "
                             "(sparse) clone of xlang-ai/Spider2")

    tasks = [json.loads(l) for l in lite_jsonl.read_text(encoding="utf-8").splitlines() if l.strip()]
    local = [t for t in tasks if t["instance_id"].startswith("local")]
    standards = {}
    for line in eval_jsonl.read_text(encoding="utf-8").splitlines():
        if line.strip():
            item = json.loads(line)
            standards[item["instance_id"]] = item

    if out_dir.exists():
        shutil.rmtree(out_dir)
    out_dir.mkdir(parents=True)
    gold_dir = out_dir / "gold"
    gold_dir.mkdir()
    (out_dir / "gold_sql").mkdir()

    # ---- stage databases (only those the local tasks use) -------------------
    needed = {t["db"] for t in local}
    staged = _stage_databases(dbs_zip, dbs_dir, out_dir, needed)
    missing_dbs = {d for d in needed if d.lower() not in staged}
    if missing_dbs:
        raise SystemExit(f"[sp2] databases not found in archive: {sorted(missing_dbs)}")

    questions = []
    skipped: list[str] = []
    for task in local:
        iid = task["instance_id"]
        db_file = staged[task["db"].lower()]
        std = standards.get(iid, {})

        # gold CSVs: <id>.csv (single) or <id>_a.csv, <id>_b.csv, ... (any-of)
        csvs = sorted(exec_result.glob(f"{iid}.csv")) or sorted(exec_result.glob(f"{iid}_*.csv"))
        if not csvs:
            skipped.append(f"{iid}: no gold CSVs")
            continue
        gold_csvs = []
        for src in csvs:
            dst = gold_dir / src.name
            shutil.copy2(src, dst)
            gold_csvs.append(str(dst.relative_to(REPO_ROOT)))

        # released gold SQL (partial — 24 of 135 local tasks)
        sql = None
        sql_src = gold_sql_dir / f"{iid}.sql"
        if sql_src.exists():
            sql = sql_src.read_text(encoding="utf-8").strip()
            (out_dir / "gold_sql" / sql_src.name).write_text(sql, encoding="utf-8")

        evidence = ""
        doc = task.get("external_knowledge")
        if doc:
            doc_path = documents / doc
            if doc_path.exists():
                evidence = doc_path.read_text(encoding="utf-8").strip()
            else:
                print(f"[sp2] WARNING {iid}: external knowledge doc missing: {doc_path}")

        questions.append({
            "id": iid,
            "question": task["question"],
            "evidence": evidence,
            "sql": sql,
            "db": str(db_file.relative_to(REPO_ROOT)),
            "db_id": task["db"],
            "engine": "sqlite",
            "profile": f"sp2_{db_file.stem}",
            "gold_csvs": gold_csvs,
            "condition_cols": std.get("condition_cols"),
            "ignore_order": bool(std.get("ignore_order", False)),
        })

    dev_json.write_text(json.dumps(questions, indent=2, ensure_ascii=False),
                        encoding="utf-8")

    # ---- sanity report -------------------------------------------------------
    if skipped:
        print(f"[sp2] skipped {len(skipped)} tasks:")
        for line in skipped:
            print(f"  - {line}")
    print(f"[sp2] {len(questions)} tasks across {len(staged)} databases")
    print(f"[sp2] gold SQL available for {sum(1 for q in questions if q['sql'])} tasks")
    print(f"[sp2] external knowledge docs inlined for "
          f"{sum(1 for q in questions if q['evidence'])} tasks")
    for name in sorted(staged):
        p = staged[name]
        print(f"  - {p.stem}: {_verify_sqlite(p)} tables, {p.stat().st_size / 1e6:.1f} MB")
    print(f"[sp2] wrote {dev_json}")


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__,
                                     formatter_class=argparse.RawDescriptionHelpFormatter)
    source = parser.add_mutually_exclusive_group(required=True)
    source.add_argument("--dbs-zip", type=Path,
                        help="official spider2-lite local database archive (.zip)")
    source.add_argument("--dbs-dir", type=Path,
                        help="directory with the .sqlite files already extracted")
    parser.add_argument("--repo", type=Path,
                        default=Path.home() / ".cache/custom-bench/Spider2",
                        help="(sparse) clone of xlang-ai/Spider2")
    parser.add_argument("--force", action="store_true", help="rebuild even if dev.json exists")
    args = parser.parse_args(argv)
    build(args.repo, args.dbs_zip, args.dbs_dir, args.force)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
