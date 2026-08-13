# profiling-test

Agentic text-to-SQL experiment: does a pre-generated [db-snooper](https://github.com/renatyv/db-snooper)
profile of the target DB improve a coding agent's **execution accuracy** on
[BEAVER](https://huggingface.co/datasets/BeaverBench/beaver), vs. raw DB access?

Four arms over three dimensions (sql_exec tool / db-snooper profile / error-avoidance
checklist), **pi-only** runner, paired comparison:

- **`pi_no_profile_no_checklist`** — pi agent + `sql_exec`, no profile, no checklist.
- **`pi_no_profile_checklist`** — same as above + the error-avoidance checklist.
- **`pi_profile_checklist`** — pi agent + `sql_exec` + a frozen `<db>.md` profile + checklist.
- **`zeroshot_profile_checklist`** — profile + checklist, **no DB / no tools / no agent loop** — one LLM call.

Each pair of arms differs along exactly one dimension, so every pairwise Δ
isolates a single manipulation (checklist effect, profile effect, agentic-vs-zero-shot).

See [`AGENT_PROFILE_EXPERIMENT_PLAN.md`](AGENT_PROFILE_EXPERIMENT_PLAN.md) for the
full design and [`RUN.md`](RUN.md) for how to run it.

## Quick start

```bash
export OPENROUTER_API_KEY=sk-or-...
python harness/setup_openrouter.py          # register provider+model, confirm ctx window
export BEAVER_MYSQL_PWD=beaver
python run_experiment.py --dataset neutron --phase phase0 --arm all   # sanity (1 q × all arms)
python run_experiment.py --dataset neutron --phase pilot              # n=20, all arms
python run_experiment.py --dataset neutron --phase pilot --estimate-cost   # go/no-go gate
```

## Layout

```
harness/
  config.py              arms (tools/profile/checklist matrix), datasets, caps, model defaults
  prompts.py             per-arm prompt construction (agentic arms share system text; zero-shot is single-call)
  manifest.py            freeze question list (seed 77, stratified by category×domain-knowledge)
  pi_extension/sql_exec.ts   read-only MySQL tool + turn-cap enforcement, loaded via `pi -e`
  mysql_io.py  scorer.py  parse_sql.py   execution-accuracy scorer (Spider/BEAVER-style ETE)
  runner_pi.py           agentic arms (pi headless, json stream → SQL + usage)
  runner_zeroshot.py     zero-shot arm (direct OpenRouter call; pi --no-tools fallback)
  metrics.py             accuracy, Wilson CI, McNemar, subgroups, error taxonomy, cost projection
  setup_openrouter.py    one-time provider/model registration + Phase-0 context check
  openrouter_models.json provider+model fragment for pi (~/.pi/agent/models.json)
run_experiment.py        CLI orchestrator (--dataset/--arm/--phase/--num-samples/…)
profiles/  data/         db-snooper profiles; BEAVER dev splits
runs/      results/      frozen manifests; per-question records + summary.json
```


## How `rich` profile was computed

Prompt:
```
`profiles/neutron.md`, `schema-links/neutron.md`
 
1. Explore the `neutron` database at localhost port 3307 login `beaver` password `beaver`.
2. Copy the the original DB profile into `rich-profile/neutron.md`
3. For each table and column where the meaning was not already clear before exploration, inject a brief comment
4. Use schema-links file to derive non-obvious potential join strategies. Inject them into the enriched profile.

Never select all rows. Always have LIMIT 10 or 100 in the worst case
```
