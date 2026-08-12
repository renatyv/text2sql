#!/usr/bin/env python3
"""Orchestrate the db-snooper profiling experiment (AG vs. AG+profile vs. zero-shot).

Implements the phases in AGENT_PROFILE_EXPERIMENT_PLAN.md:
  phase0  — sanity: 1 question × {A,B,C}, headless, end-to-end scored
  pilot   — neutron n=20 (default), all arms
  main    — full per-dataset sampling, all arms

Examples
--------
  # Phase-0 sanity (default): 1 neutron question, all 3 arms
  python run_experiment.py --dataset neutron --phase phase0

  # Phase-1 pilot
  python run_experiment.py --dataset neutron --phase pilot --arm all

  # Dry-run cost projection from existing pilot data
  python run_experiment.py --dataset neutron --phase pilot --estimate-cost

  # Rescore (no model calls) after tweaking the scorer
  python run_experiment.py --dataset neutron --phase pilot --score-only
"""
from __future__ import annotations

import argparse
import json
import sys
import time
from pathlib import Path

from rich.progress import (
    BarColumn,
    MofNCompleteColumn,
    Progress,
    SpinnerColumn,
    TaskProgressColumn,
    TextColumn,
    TimeElapsedColumn,
)

from harness import config, manifest as manifest_mod, metrics, runner_pi, runner_zeroshot, scorer

PHASE_DEFAULT_N = {"phase0": 1, "pilot": config.PILOT_N}
PHASE_DEFAULT_TURNS = {"phase0": config.MAX_TURNS_PILOT,
                       "pilot": config.MAX_TURNS_PILOT,
                       "main": config.MAX_TURNS_MAIN}


def _progress() -> Progress:
    """A shared rich.Progress layout for both loops.

    `transient=True` clears each arm's bar when it finishes so the screen isn't
    cluttered with one stale bar per arm; the per-question result line and the
    final summary are printed via `progress.console.print`, which is not cleared.
    """
    return Progress(
        SpinnerColumn(),
        TextColumn("[bold blue]{task.description}"),
        BarColumn(),
        MofNCompleteColumn(),
        TaskProgressColumn(),
        "•",
        TimeElapsedColumn(),
        transient=True,
    )


def _status_tag(rec: dict) -> str:
    """One-glyph correctness marker, colour-coded for the result line."""
    if rec.get("correct"):
        return "[green]✓[/green]"
    if rec.get("valid_sql"):
        return "[yellow]sql[/yellow]"
    return "[red]✗[/red]"


def _run_id(dataset: str, phase: str, num_samples: int | None) -> str:
    n_tag = "full" if num_samples is None else f"n{num_samples}"
    return f"{dataset}__{phase}__{n_tag}"


def _results_dir(run_id: str) -> Path:
    d = config.RESULTS_DIR / run_id
    d.mkdir(parents=True, exist_ok=True)
    return d


def _run_one(q: dict, arm: str, db_label: str, max_turns: int, idx: int) -> dict:
    sandbox = config.SANDBOX_ROOT / f"{db_label}_{arm}_{idx}_{q['id']}"
    if arm in ("A", "B"):
        rec = runner_pi.run(db_label, q["question"], arm, max_turns, sandbox)
    else:
        rec = runner_zeroshot.run(db_label, q["question"], sandbox)
    return rec


def _score(rec: dict, q: dict, db: str) -> dict:
    s = scorer.score_prediction(rec.get("pred_sql"), q["sql"], db)
    rec.update(s)
    # denormalize for the record
    rec["id"] = q["id"]
    rec["category"] = q.get("category")
    rec["detailed_category"] = q.get("detailed_category")
    rec["contains_domain_knowledge"] = q.get("contains_domain_knowledge")
    return rec


def _load_existing(path: Path) -> dict[str, dict]:
    return {r["id"]: r for r in metrics.read_jsonl(path) if "id" in r}


def run(args) -> int:
    if args.dataset not in config.DATASETS:
        print(f"unknown dataset '{args.dataset}'; choose from {list(config.DATASETS)}")
        return 2

    num_samples = args.num_samples
    if num_samples is None and args.phase in PHASE_DEFAULT_N:
        num_samples = PHASE_DEFAULT_N[args.phase]

    man = manifest_mod.load_manifest(manifest_mod.build_manifest(args.dataset, args.phase, num_samples))
    questions = man["questions"]
    if args.limit:
        questions = questions[: args.limit]
    db = man["mysql_db"]
    run_id = _run_id(args.dataset, args.phase, num_samples)
    rdir = _results_dir(run_id)

    arms = list(config.ARMS) if args.arm == "all" else [args.arm]
    max_turns = args.max_turns or PHASE_DEFAULT_TURNS[args.phase]

    print(f"=== run {run_id} | arms={arms} | questions={len(questions)} | "
          f"max_turns={max_turns} | db={db} ===")
    print(f"model: {config.DEFAULT_PROVIDER}/{config.DEFAULT_MODEL_ID}")

    # ---- score-only / estimate-cost short-circuit --------------------------
    if args.score_only or args.estimate_cost:
        gold = {q["id"]: q["sql"] for q in questions}
        by_arm: dict[str, list[dict]] = {}
        progress = _progress()
        with progress:
            for arm in arms:
                recs = list(_load_existing(rdir / f"arm{arm}.jsonl").values())
                if args.score_only:
                    desc = f"rescore arm {arm}"
                    task = progress.add_task(desc, total=len(recs))
                    for r in recs:
                        q = {"id": r.get("id"), "sql": gold.get(r.get("id"), ""),
                              "category": r.get("category"),
                              "detailed_category": r.get("detailed_category"),
                              "contains_domain_knowledge": r.get("contains_domain_knowledge")}
                        _score(r, q, db)
                        progress.advance(task)
                    metrics.write_jsonl(rdir / f"arm{arm}.jsonl", recs)
                by_arm[arm] = recs
        if args.estimate_cost:
            print(json.dumps(metrics.project_cost(by_arm, config.PHASE2_SAMPLE_SIZES.get(args.dataset, 0)), indent=2))
            return 0
        _summarize(by_arm, rdir)
        return 0

    # ---- main loop ---------------------------------------------------------
    summaries: dict[str, list[dict]] = {}
    progress = _progress()
    with progress:
        for arm in arms:
            path = rdir / f"arm{arm}.jsonl"
            done = _load_existing(path)
            records: list[dict] = list(done.values())
            desc = f"arm {arm} · {config.ARM_DESCRIPTIONS[arm]}"
            task = progress.add_task(desc, total=len(questions))
            for i, q in enumerate(questions, 1):
                if q["id"] in done and not args.force:
                    progress.console.print(f"  [{i}/{len(questions)}] {q['id']}: cached")
                    progress.advance(task)
                    continue
                t0 = time.time()
                try:
                    rec = _run_one(q, arm, args.dataset, max_turns, i)
                    rec = _score(rec, q, db)
                except Exception as e:  # never let one question kill the run
                    rec = {"id": q["id"], "arm": arm, "error": f"{type(e).__name__}: {e}",
                           "correct": False, "valid_sql": False}
                records = [r for r in records if r.get("id") != q["id"]] + [rec]
                metrics.write_jsonl(path, records)
                tag = _status_tag(rec)
                line = (f"  [{i}/{len(questions)}] {q['id']}: {tag}  "
                        f"turns={rec.get('turns')} dbq={rec.get('db_queries')} "
                        f"tok={rec.get('usage', {}).get('totalTokens', 0)} "
                        f"({time.time() - t0:.1f}s)")
                if not rec.get("correct"):
                    err = rec.get("pred_error") or rec.get("error")
                    if err:
                        line += f"  [red]err={err}[/red]"
                progress.console.print(line)
                progress.advance(task)
            summaries[arm] = records
        summaries[arm] = records

    _summarize(summaries, rdir)
    return 0


def _summarize(by_arm: dict[str, list[dict]], rdir: Path) -> None:
    print("\n=== summary ===")
    summary: dict[str, dict] = {}
    for arm, recs in by_arm.items():
        agg = metrics.aggregate(recs)
        agg["by_category"] = metrics.subgroup_accuracy(recs, "category")
        agg["by_contains_domain_knowledge"] = metrics.subgroup_accuracy(recs, "contains_domain_knowledge")
        agg["error_taxonomy"] = metrics.value_counts(recs, "error_class")
        summary[arm] = agg
        print(f"arm {arm}: n={agg.get('n')} acc={agg.get('accuracy')} "
              f"(CI {agg.get('accuracy_ci95')}) valid={agg.get('valid_sql_pct')} "
              f"mean_turns={agg.get('mean_turns')} mean_dbq={agg.get('mean_db_queries')} "
              f"tok_in/out={agg.get('tokens_in')}/{agg.get('tokens_out')} "
              f"cost=${agg.get('cost_usd')}")

    # pairwise comparisons (require identical question sets)
    def _correct_vec(arm):
        # ordered by id to align paired comparisons
        m = {r["id"]: bool(r.get("correct")) for r in by_arm.get(arm, [])}
        ids = sorted(set().union(*( {r["id"] for r in v} for v in by_arm.values())))
        return [m.get(i, False) for i in ids], ids

    pairs = [("B", "A"), ("B", "C"), ("C", "A")]
    if "A" in by_arm and "B" in by_arm and "C" in by_arm:
        vA, ids = _correct_vec("A")
        vB, _ = _correct_vec("B")
        vC, _ = _correct_vec("C")
        summary["pairwise"] = {
            "B-A": metrics.paired_diff_ci(vA, vB),
            "B-C": metrics.paired_diff_ci(vC, vB),
            "C-A": metrics.paired_diff_ci(vA, vC),
        }
        for name, p in summary["pairwise"].items():
            print(f"  Δ {name}: {p['delta']:+.3f}  (95% CI {p['ci_low']:+.3f}..{p['ci_high']:+.3f}, "
                  f"discordant b/c={p['b']}/{p['c']}, p={p['p_value_exact']})")

    (rdir / "summary.json").write_text(json.dumps(summary, indent=2, ensure_ascii=False), encoding="utf-8")
    print(f"\nwrote {rdir/'summary.json'}")


def main(argv=None) -> int:
    p = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    p.add_argument("--dataset", default="neutron", choices=list(config.DATASETS))
    p.add_argument("--arm", default="all", choices=list(config.ARMS) + ["all"])
    p.add_argument("--phase", default="phase0", choices=["phase0", "pilot", "main"])
    p.add_argument("--num-samples", type=int, default=None,
                   help="questions per dataset (default: phase-dependent; omit = full)")
    p.add_argument("--limit", type=int, default=None, help="cap questions (quick tests)")
    p.add_argument("--max-turns", type=int, default=None)
    p.add_argument("--force", action="store_true", help="re-run cached questions")
    p.add_argument("--score-only", action="store_true", help="rescore existing records")
    p.add_argument("--estimate-cost", action="store_true", help="project Phase-2 cost from pilot")
    return run(p.parse_args(argv))


if __name__ == "__main__":
    sys.exit(main())
