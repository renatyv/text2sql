#!/usr/bin/env python3
"""Build the BIRD Mini-Dev (SQLite) dataset for the harness.

Unpacks the official mini_dev zip (bird-bench/mini_dev) and normalizes the
500-question SQLite split into the harness's data/<label>/dev.json
convention. The .sqlite files are used AS-IS — nothing is loaded into
MySQL — so the benchmark's native dialect, data and gold SQL are preserved
end-to-end (agent SQL, gold SQL and scoring all run on the original files).

Layout produced:
  data/bird_mini_dev/
    dev.json                    # normalized questions (internal schema)
    databases/dev_databases/<db_id>/sqlite/<db_id>.sqlite

Usage:
  uv run python data/build_bird_mini_dev.py [--zip minidev.zip] [--force]

The zip is downloaded from the official mirror when --zip is not given.
Re-run with --force to rebuild from scratch.
"""
from __future__ import annotations

import argparse
import json
import shutil
import sqlite3
import sys
import urllib.request
import zipfile
from collections import Counter
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(REPO_ROOT))

from harness import config  # noqa: E402

DATASET = "bird_mini_dev"
MINI_DEV_URL = "https://bird-bench.oss-cn-beijing.aliyuncs.com/minidev.zip"
QUESTIONS_MEMBER = "mini_dev_sqlite.json"


def _download(dest: Path) -> Path:
    print(f"[bird] downloading {MINI_DEV_URL} -> {dest} (large, be patient)")
    with urllib.request.urlopen(MINI_DEV_URL, timeout=60) as resp, open(dest, "wb") as f:
        shutil.copyfileobj(resp, f)
    return dest


def _extract(zip_path: Path, out_dir: Path) -> tuple[Path, list[Path]]:
    """Extract mini_dev_sqlite.json + every dev database .sqlite file.

    The zip nests everything under mini_dev_data/ (possibly with varying
    prefixes); members are matched by suffix and re-rooted into out_dir.
    Returns (questions_json_path, sqlite_files).
    """
    questions_path: Path | None = None
    db_files: list[Path] = []
    with zipfile.ZipFile(zip_path) as zf:
        members = zf.namelist()
        for member in members:
            parts = Path(member).parts
            if member.endswith(QUESTIONS_MEMBER):
                target = out_dir / QUESTIONS_MEMBER
                zf.extract(member, out_dir.parent)
                extracted = out_dir.parent / member
                target.parent.mkdir(parents=True, exist_ok=True)
                if extracted != target:
                    shutil.move(str(extracted), target)
                questions_path = target
            elif "dev_databases" in parts and member.endswith(".sqlite"):
                # .../<db_id>/sqlite/<db_id>.sqlite -> databases/dev_databases/...
                idx = parts.index("dev_databases")
                rel = Path(*parts[idx:])
                target = out_dir / "databases" / rel
                target.parent.mkdir(parents=True, exist_ok=True)
                with zf.open(member) as src, open(target, "wb") as dst:
                    shutil.copyfileobj(src, dst)
                db_files.append(target)
    if questions_path is None:
        raise SystemExit(f"[bird] {QUESTIONS_MEMBER} not found in {zip_path}")
    return questions_path, db_files


def _verify_sqlite(path: Path) -> int:
    """Open read-only and count tables; raises on a corrupt file."""
    conn = sqlite3.connect(f"file:{path}?mode=ro", uri=True)
    try:
        rows = conn.execute(
            "SELECT COUNT(*) FROM sqlite_master WHERE type='table'"
        ).fetchone()
        return int(rows[0])
    finally:
        conn.close()


def build(zip_path: Path, force: bool = False) -> None:
    out_dir = config.DATA_DIR / DATASET
    dev_json = out_dir / "dev.json"
    if dev_json.exists() and not force:
        print(f"[bird] {dev_json} exists (use --force to rebuild)")
        return

    if not zip_path.exists():
        zip_path = _download(zip_path)

    if out_dir.exists():
        shutil.rmtree(out_dir)
    out_dir.mkdir(parents=True)

    print(f"[bird] extracting from {zip_path} ...")
    questions_path, db_files = _extract(zip_path, out_dir)
    print(f"[bird] extracted {len(db_files)} sqlite databases")

    # Map db_id -> file by the sqlite filename stem (BIRD convention:
    # dev_databases/<db_id>/sqlite/<db_id>.sqlite).
    db_by_id = {f.stem: f for f in db_files}

    raw = json.loads(questions_path.read_text(encoding="utf-8"))
    questions = []
    skipped: list[str] = []
    for entry in raw:
        db_id = entry["db_id"]
        db_file = db_by_id.get(db_id)
        if db_file is None:
            skipped.append(f"{entry.get('question_id')}: no sqlite file for {db_id}")
            continue
        questions.append({
            "id": f"bird_{entry['question_id']}",
            "question": entry["question"],
            "evidence": entry.get("evidence") or "",
            "difficulty": entry.get("difficulty"),
            "sql": entry["SQL"],
            "db": str(db_file.relative_to(REPO_ROOT)),
            "db_id": db_id,
            "engine": "sqlite",
            "profile": f"bird_{db_id}",
        })

    if skipped:
        print(f"[bird] WARNING skipped {len(skipped)} questions:")
        for line in skipped[:10]:
            print(f"  - {line}")

    dev_json.write_text(json.dumps(questions, indent=2, ensure_ascii=False),
                        encoding="utf-8")

    # ---- sanity report -----------------------------------------------------
    tables = {f.stem: _verify_sqlite(f) for f in sorted(db_files)}
    sizes = {f.stem: f.stat().st_size for f in db_files}
    print(f"[bird] {len(questions)} questions across {len(db_by_id)} databases")
    print(f"[bird] difficulty: {dict(Counter(q['difficulty'] for q in questions))}")
    for db_id in sorted(tables):
        print(f"  - {db_id}: {tables[db_id]} tables, {sizes[db_id] / 1e6:.1f} MB")
    print(f"[bird] wrote {dev_json}")
    # the extracted mini_dev_sqlite.json stays next to the data for provenance


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__,
                                     formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument("--zip", type=Path,
                        default=Path.home() / ".cache/custom-bench/minidev.zip",
                        help=f"path to the official minidev.zip (downloaded from {MINI_DEV_URL} if missing)")
    parser.add_argument("--force", action="store_true", help="rebuild even if dev.json exists")
    args = parser.parse_args(argv)
    build(args.zip, args.force)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
