#!/usr/bin/env python3
"""Orchestrate the db-snooper profile × metadata experiment.

Implements three phases:
  phase0  — sanity: 1 question × all arms, headless, end-to-end scored
  pilot   — neutron n=20 (default), all arms
  main    — full per-dataset sampling, all arms

Examples
--------
  # Phase-0 sanity (default): 1 neutron question, all arms
  python run_experiment.py --dataset neutron --phase phase0

  # Phase-1 pilot
  python run_experiment.py --dataset neutron --phase pilot --arm all

  # Any subset of arms, with a different sample size per database
  python run_experiment.py --phase main --samples neutron=100 nova=80 dw=50 \
      --arms raw profile metadata

  # Dry-run cost projection from existing pilot data
  python run_experiment.py --dataset neutron --phase pilot --estimate-cost

  # Rescore (no model calls) after tweaking the scorer
  python run_experiment.py --dataset neutron --phase pilot --score-only
"""
from __future__ import annotations

import argparse
import hashlib
import json
import random
import sys
import threading
import time
from concurrent.futures import ThreadPoolExecutor, as_completed
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

from harness import config, manifest as manifest_mod, metrics, network, parse_sql, prompts, runner_container, runner_pi, runner_zeroshot, scorer

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


# Whether agentic arms run in a container (default) or on the host (--no-container).
# Set in run() so the thread-pool worker below picks it up without a signature change.
_USE_CONTAINER = True


def _q_target(q: dict, db_label: str) -> tuple[str, str, str]:
    """Resolve a question's (engine, db, profile_key).

    BEAVER: one MySQL schema per dataset. BIRD / Spider 2.0: the question's
    `db` is an .sqlite file path and `profile` the per-database profile key.
    """
    spec = config.dataset_spec(db_label)
    engine = q.get("engine") or spec["engine"]
    db = q.get("db") or config.mysql_db_for(db_label) or db_label
    profile_key = q.get("profile") or db
    return engine, db, profile_key


def _run_one(q: dict, arm: str, db_label: str, max_turns: int, idx: int,
             status_callback=None) -> dict:
    sandbox = config.SANDBOX_ROOT / f"{db_label}_{arm}_{idx}_{q['id']}"
    engine, db, profile_key = _q_target(q, db_label)
    if config.arm_spec(arm)["tools"]:
        if _USE_CONTAINER:
            rec = runner_container.run(
                db_label, q["question"], arm, max_turns, sandbox, status_callback,
                engine=engine, db=db, evidence=q.get("evidence"),
                profile_key=profile_key,
            )
        else:
            rec = runner_pi.run(
                db_label, q["question"], arm, max_turns, sandbox,
                engine=engine, db=db, evidence=q.get("evidence"),
                profile_key=profile_key,
            )
    else:
        rec = runner_zeroshot.run(
            db_label, q["question"], arm, sandbox,
            engine=engine, db=db, evidence=q.get("evidence"),
            profile_key=profile_key,
        )
    return rec


def _score(rec: dict, q: dict, engine: str, db: str, mode: str = "beaver") -> dict:
    eval_meta = None
    if mode == "spider2":
        eval_meta = {
            "gold_csvs": q.get("gold_csvs") or [],
            "condition_cols": q.get("condition_cols"),
            "ignore_order": bool(q.get("ignore_order", False)),
        }
    s = scorer.score_prediction(rec.get("pred_sql"), q.get("sql"), db,
                                engine=engine, mode=mode, eval_meta=eval_meta)
    rec.update(s)
    # denormalize for the record / subgroup metrics
    rec["id"] = q["id"]
    for field in ("category", "detailed_category", "contains_domain_knowledge",
                  "difficulty", "db_id"):
        if q.get(field) is not None:
            rec[field] = q[field]
    return rec


def _protocol_fingerprint(q: dict, arm: str, db: str, max_turns: int) -> str:
    engine, target_db, profile_key = _q_target(q, db)
    system, user = prompts.agent_prompts(
        db, q["question"], arm, max_turns, engine=engine, db=target_db,
        evidence=q.get("evidence"), profile_key=profile_key,
    )
    model_registry_hash = None
    if _USE_CONTAINER and config.CONTAINER_AGENT == "pi":
        model_registry_hash = hashlib.sha256(config.openrouter_models_path().read_bytes()).hexdigest()
    payload = {
        "version": config.PROTOCOL_VERSION,
        "runner": f"container:{config.CONTAINER_AGENT}" if _USE_CONTAINER else "host:pi",
        "model": config.CONTAINER_AGENT_MODEL if _USE_CONTAINER else config.DEFAULT_MODEL_ID,
        "model_registry_hash": model_registry_hash,
        "thinking": config.PI_THINKING,
        "pi_version": config.PI_AGENT_VERSION,
        "max_turns": max_turns,
        "wall_clock": config.PI_WALL_CLOCK,
        "system_prompt": system,
        "user_prompt": user,
    }
    return hashlib.sha256(json.dumps(payload, sort_keys=True).encode()).hexdigest()


def _run_one_and_score(q: dict, arm: str, db_label: str,
                       max_turns: int, idx: int,
                       status_callback=None) -> tuple[dict, float]:
    """Worker: run one question + score it, never raising.

    Moved out of the loop body so it can be submitted to a ThreadPoolExecutor:
    a single question failing (subprocess crash, scorer error, ...) is captured
    here as an error record instead of poisoning the pool. Returns (rec, elapsed_s)
    so the wall time is measured around the actual work, not after `as_completed`
    reorders completions.
    """
    t0 = time.time()
    fingerprint = _protocol_fingerprint(q, arm, db_label, max_turns)
    engine, db, _profile_key = _q_target(q, db_label)
    mode = config.dataset_spec(db_label)["scoring"]
    try:
        for attempt in range(2):
            rec = _run_one(q, arm, db_label, max_turns, idx, status_callback)
            if not rec.get("retryable_error"):
                break
            if attempt == 0:
                time.sleep(random.uniform(5, 15))
        if not rec.get("infrastructure_error"):
            rec = _score(rec, q, engine, db, mode)
        rec["harness_attempts"] = attempt + 1
        rec["id"] = q["id"]
        rec["protocol_fingerprint"] = fingerprint
    except Exception as e:  # never let one question kill the run
        rec = {"id": q["id"], "arm": arm, "error": f"{type(e).__name__}: {e}",
               "infrastructure_error": True, "correct": False, "valid_sql": False}
    return rec, time.time() - t0


def _is_infrastructure_failure(rec: dict) -> bool:
    if rec.get("budget_exhausted"):
        return False
    return bool(
        rec.get("infrastructure_error")
        or (rec.get("turns") == 0
            and not (rec.get("usage") or {}).get("totalTokens")
            and not rec.get("model")
            and not rec.get("pred_sql"))
    )


def _load_existing(path: Path, fingerprints: dict[str, str] | None = None) -> dict[str, dict]:
    return {r["id"]: r for r in metrics.read_jsonl(path)
            if "id" in r and not _is_infrastructure_failure(r)
            and (fingerprints is None
                 or r.get("protocol_fingerprint") == fingerprints.get(r["id"]))}


def _run_dataset(args) -> int:
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
    spec = config.dataset_spec(args.dataset)
    engine = man.get("engine") or spec["engine"]
    db = man.get("mysql_db") or config.mysql_db_for(args.dataset)
    db_desc = db if engine == "mysql" else f"{engine} · {len({q['db'] for q in questions})} database files"
    run_id = _run_id(args.dataset, args.phase, num_samples)
    rdir = _results_dir(run_id)

    arms = args.arms or (list(config.ARMS) if args.arm in (None, "all") else [args.arm])
    max_turns = args.max_turns or PHASE_DEFAULT_TURNS[args.phase]
    # Container vs. host runner for agentic arms.
    global _USE_CONTAINER
    _USE_CONTAINER = not getattr(args, "no_container", False)
    fingerprints = {
        arm: {q["id"]: _protocol_fingerprint(q, arm, args.dataset, max_turns)
              for q in questions}
        for arm in arms
    }

    runner_name = f"container:{config.CONTAINER_AGENT}" if _USE_CONTAINER else "host(pi)"
    print(f"=== run {run_id} | arms={arms} | questions={len(questions)} | "
          f"max_turns={max_turns} | db={db_desc} | workers={args.workers} "
          f"| runner={runner_name} ===")
    model = config.CONTAINER_AGENT_MODEL if _USE_CONTAINER else config.DEFAULT_MODEL_ID
    print(f"agent model: openrouter/{model}")

    # Setup also resets this process's random, SELECT-only agent account. Run
    # it even when the network already exists; otherwise a later process would
    # have credentials that do not match the account provisioned by an earlier
    # process. Zero-shot and host-pi runs do not need this boundary. SQLite
    # benchmarks need no grants at all (read-only file mounts), but the proxy
    # bring-up still applies.
    has_container_agent = any(config.arm_spec(arm)["tools"] for arm in arms)
    if _USE_CONTAINER and has_container_agent and not (args.score_only or args.estimate_cost):
        print("=== preparing agent network and SELECT-only database account ===")
        network.setup(set(man.get("mysql_dbs") or []))

    # ---- score-only / estimate-cost short-circuit --------------------------
    if args.score_only or args.estimate_cost:
        by_id = {q["id"]: q for q in questions}
        by_arm: dict[str, list[dict]] = {}
        progress = _progress()
        with progress:
            for arm in arms:
                recs = list(_load_existing(
                    rdir / f"arm{arm}.jsonl", None if args.score_only else fingerprints[arm]
                ).values())
                if args.score_only:
                    desc = f"rescore arm {arm}"
                    task = progress.add_task(desc, total=len(recs))
                    for r in recs:
                        q = by_id.get(r.get("id"), {})
                        if q:
                            r["pred_sql"] = parse_sql.extract_sql(r.get("raw_text", "")) or r.get("pred_sql")
                            q_engine, q_db, _key = _q_target(q, args.dataset)
                            _score(r, q, q_engine, q_db, spec["scoring"])
                        progress.advance(task)
                    metrics.write_jsonl(rdir / f"arm{arm}.jsonl", recs)
                by_arm[arm] = recs
        if args.estimate_cost:
            print(json.dumps(metrics.project_cost(by_arm, config.PHASE2_SAMPLE_SIZES.get(args.dataset, 0)), indent=2))
            return 0
        _summarize(by_arm, rdir, spec["subgroups"])
        return 0

    # ---- main loop ---------------------------------------------------------
    summaries: dict[str, list[dict]] = {}
    infrastructure_failures = 0
    progress = _progress()
    n_total = len(questions)
    with progress:
        for arm in arms:
            path = rdir / f"arm{arm}.jsonl"
            done = _load_existing(path, fingerprints[arm])
            records: list[dict] = list(done.values())
            write_lock = threading.Lock()  # guards `records` + write_jsonl on main thread
            desc = f"arm {arm} · {config.ARM_DESCRIPTIONS[arm]}"
            task = progress.add_task(desc, total=n_total)

            # Partition: cached questions are accounted for up front on the main
            # thread; the rest are dispatched to the pool.
            to_run: list[tuple[int, dict]] = []
            for i, q in enumerate(questions, 1):
                if q["id"] in done and not args.force:
                    progress.console.print(f"  [{i}/{n_total}] {q['id']}: cached")
                    progress.advance(task)
                else:
                    to_run.append((i, q))

            if not to_run:
                summaries[arm] = [r for r in records if not r.get("infrastructure_error")]
                continue

            workers = max(1, args.workers)
            with ThreadPoolExecutor(max_workers=workers) as pool:
                def live_status(qid: str, turn: int, dbq: int) -> None:
                    progress.update(
                        task,
                        description=(f"arm {arm} · {config.ARM_DESCRIPTIONS[arm]} · "
                                     f"{qid} turn {turn}/{max_turns} dbq={dbq}"),
                    )

                future_to_q = {
                    pool.submit(
                        _run_one_and_score, q, arm, args.dataset, max_turns, i,
                        lambda turn, dbq, qid=q["id"]: live_status(qid, turn, dbq),
                    ): (i, q)
                    for i, q in to_run
                }
                for fut in as_completed(future_to_q):
                    i, q = future_to_q[fut]
                    rec, elapsed = fut.result()  # _run_one + _score (or error rec) — never raises
                    # Only the main thread mutates `records` / writes the file,
                    # so no concurrent access happens here; the lock is retained
                    # for safety if writes ever move off-thread.
                    with write_lock:
                        records = [r for r in records if r.get("id") != q["id"]] + [rec]
                        metrics.write_jsonl(path, records)
                    tag = _status_tag(rec)
                    line = (f"  [{i}/{n_total}] {q['id']}: {tag}  "
                            f"turns={rec.get('turns')} dbq={rec.get('db_queries')} "
                            f"tok={rec.get('usage', {}).get('totalTokens', 0)} "
                            f"({elapsed:.1f}s)")
                    if not rec.get("correct"):
                        err = rec.get("error") or rec.get("pred_error")
                        if err:
                            line += f"  [red]err={err}[/red]"
                    progress.console.print(line)
                    progress.advance(task)
            failures = [r for r in records if r.get("infrastructure_error")]
            infrastructure_failures += len(failures)
            summaries[arm] = [r for r in records if not r.get("infrastructure_error")]

    _summarize(summaries, rdir, spec["subgroups"])
    if infrastructure_failures:
        print(f"ERROR: {infrastructure_failures} infrastructure failures were excluded; "
              "rerun the same command to retry them.")
        return 1
    return 0


def _parse_samples(values: list[str]) -> list[tuple[str, int]]:
    parsed = []
    seen = set()
    for value in values:
        db, sep, raw_n = value.partition("=")
        if not sep or db not in config.DATASETS:
            raise argparse.ArgumentTypeError(
                f"invalid sample {value!r}; use DB=N with DB in {list(config.DATASETS)}"
            )
        try:
            n = int(raw_n)
        except ValueError:
            n = 0
        if n < 1 or db in seen:
            raise argparse.ArgumentTypeError(f"invalid or duplicate sample {value!r}")
        parsed.append((db, n))
        seen.add(db)
    return parsed


def run(args) -> int:
    samples = _parse_samples(args.samples) if args.samples else [(args.dataset, args.num_samples)]
    status = 0
    for dataset, num_samples in samples:
        dataset_args = argparse.Namespace(**vars(args))
        dataset_args.dataset = dataset
        dataset_args.num_samples = num_samples
        status = max(status, _run_dataset(dataset_args))
    return status


def _summarize(by_arm: dict[str, list[dict]], rdir: Path,
               subgroup_fields: list[str] | None = None) -> None:
    print("\n=== summary ===")
    # Subgroup annotations are per benchmark: BEAVER reports category ×
    # domain-knowledge, BIRD difficulty, Spider 2.0 the source database.
    subgroup_fields = subgroup_fields or ["category", "contains_domain_knowledge", "query_shape"]
    summary: dict[str, dict] = {}
    for arm, recs in by_arm.items():
        agg = metrics.aggregate(recs)
        for field in subgroup_fields:
            agg[f"by_{field}"] = metrics.subgroup_accuracy(recs, field)
        agg["error_taxonomy"] = metrics.value_counts(recs, "error_class")
        summary[arm] = agg
        telemetry = "unavailable" if not agg.get("operational_metrics_available", True) else f"${agg.get('cost_usd')}"
        print(f"arm {arm}: n={agg.get('n')} acc={agg.get('accuracy')} "
              f"(CI {agg.get('accuracy_ci95')}) valid={agg.get('valid_sql_pct')} "
              f"mean_turns={agg.get('mean_turns')} mean_dbq={agg.get('mean_db_queries')} "
              f"tok_in/out={agg.get('tokens_in')}/{agg.get('tokens_out')} "
              f"cost={telemetry}")

    # Pair only IDs completed in both arms; infrastructure failures must never
    # become false answers in a statistical comparison.
    pairwise: dict[str, dict] = {}
    for sub, minu in config.PAIRWISE:
        if sub in by_arm and minu in by_arm:
            a = {r["id"]: bool(r.get("correct")) for r in by_arm[sub]}
            b = {r["id"]: bool(r.get("correct")) for r in by_arm[minu]}
            ids = sorted(a.keys() & b.keys())
            pairwise[f"{minu}-{sub}"] = metrics.paired_diff_ci(
                [a[i] for i in ids], [b[i] for i in ids]
            )
    if pairwise:
        summary["pairwise"] = pairwise
        for name, p in pairwise.items():
            print(f"  Δ {name}: {p['delta']:+.3f}  (95% CI {p['ci_low']:+.3f}..{p['ci_high']:+.3f}, "
                  f"discordant b/c={p['b']}/{p['c']}, p={p['p_value_exact']})")

    (rdir / "summary.json").write_text(json.dumps(summary, indent=2, ensure_ascii=False), encoding="utf-8")
    print(f"\nwrote {rdir/'summary.json'}")


def main(argv=None) -> int:
    p = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    p.add_argument("--dataset", default="neutron", choices=list(config.DATASETS),
                   help="single-database mode (default: neutron)")
    p.add_argument("--samples", nargs="+", metavar="DB=N",
                   help="multi-database mode; e.g. neutron=100 nova=80 dw=50")
    arm_group = p.add_mutually_exclusive_group()
    arm_group.add_argument("--arms", nargs="+", choices=list(config.ARMS),
                           help="one or more arms (default: all four)")
    arm_group.add_argument("--arm", choices=list(config.ARMS) + ["all"],
                           help="legacy single-arm form")
    p.add_argument("--phase", default="phase0", choices=["phase0", "pilot", "main"])
    p.add_argument("--num-samples", type=int, default=None,
                   help="questions per dataset (default: phase-dependent; omit = full)")
    p.add_argument("--limit", type=int, default=None, help="cap questions (quick tests)")
    p.add_argument("--max-turns", type=int, default=None)
    p.add_argument("--model", metavar="OPENROUTER_MODEL",
                   help="OpenRouter model slug for every arm; e.g. openai/gpt-5.6-luna-pro")
    p.add_argument("--effort", choices=["off", "minimal", "low", "medium", "high", "xhigh", "max"],
                   default=config.PI_THINKING,
                   help="reasoning effort for every arm (default: %(default)s)")
    p.add_argument("--workers", type=int, default=4,
                   help="parallel questions per arm (thread pool). Bounded by "
                        "OpenRouter/DeepSeek rate limits; raise with care.")
    p.add_argument("--force", action="store_true", help="re-run cached questions")
    p.add_argument("--no-container", action="store_true",
                   help="run agentic arms with the host `pi` binary (legacy sql_exec.ts "
                        "path) instead of the isolated Docker container. For debugging "
                        "and comparability with pre-container runs.")
    p.add_argument("--score-only", action="store_true", help="rescore existing records")
    p.add_argument("--estimate-cost", action="store_true", help="project Phase-2 cost from pilot")
    args = p.parse_args(argv)
    try:
        config.PI_THINKING = args.effort
        if args.model:
            config.set_openrouter_model(args.model)
        return run(args)
    except (argparse.ArgumentTypeError, ValueError) as e:
        p.error(str(e))


if __name__ == "__main__":
    sys.exit(main())
