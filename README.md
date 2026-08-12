# profiling-test

Agentic text-to-SQL experiment: does a pre-generated [db-snooper](https://github.com/renatyv/db-snooper)
profile of the target DB improve a coding agent's **execution accuracy** on
[BEAVER](https://huggingface.co/datasets/BeaverBench/beaver), vs. raw DB access?

Three arms, **pi-only** runner, paired comparison:

- **A — baseline:** NL question + MySQL + a `sql_exec` tool (agent explores the schema itself).
- **B — profile:** same as A + a frozen `<db>.md` profile in the initial prompt.
- **C — zero-shot + profile:** profile + question, **no DB / no tools / no agent loop** — one LLM call.

See [`AGENT_PROFILE_EXPERIMENT_PLAN.md`](AGENT_PROFILE_EXPERIMENT_PLAN.md) for the
full design and [`RUN.md`](RUN.md) for how to run it.

## Quick start

```bash
export OPENROUTER_API_KEY=sk-or-...
python harness/setup_openrouter.py          # register provider+model, confirm ctx window
export BEAVER_MYSQL_PWD=beaver
python run_experiment.py --dataset neutron --phase phase0 --arm all   # sanity (1 q × 3 arms)
python run_experiment.py --dataset neutron --phase pilot              # n=20, all arms
python run_experiment.py --dataset neutron --phase pilot --estimate-cost   # go/no-go gate
```

## Layout

```
harness/
  config.py              arms, datasets, caps, model defaults
  prompts.py             per-arm prompt construction (A/B share system; C is zero-shot)
  manifest.py            freeze question list (seed 77, stratified by category×domain-knowledge)
  pi_extension/sql_exec.ts   read-only MySQL tool + turn-cap enforcement, loaded via `pi -e`
  mysql_io.py  scorer.py  parse_sql.py   execution-accuracy scorer (Spider/BEAVER-style ETE)
  runner_pi.py           arms A & B (pi headless, json stream → SQL + usage)
  runner_zeroshot.py     arm C (direct OpenRouter call; pi --no-tools fallback)
  metrics.py             accuracy, Wilson CI, McNemar, subgroups, error taxonomy, cost projection
  setup_openrouter.py    one-time provider/model registration + Phase-0 context check
  openrouter_models.json provider+model fragment for pi (~/.pi/agent/models.json)
run_experiment.py        CLI orchestrator (--dataset/--arm/--phase/--num-samples/…)
profiles/  data/         db-snooper profiles; BEAVER dev splits
runs/      results/      frozen manifests; per-question records + summary.json
```
