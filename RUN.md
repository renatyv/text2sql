# Runbook — db-snooper profile experiment (agentic text-to-SQL on BEAVER)

Implements [`AGENT_PROFILE_EXPERIMENT_PLAN.md`](AGENT_PROFILE_EXPERIMENT_PLAN.md).
Three arms, pi-only runner, paired comparison:

| Arm | Context |
|---|---|
| **A — baseline** | NL question + MySQL + `sql_exec` tool. No schema hints. |
| **B — profile** | Same as A + frozen db-snooper `<db>.md` in the initial prompt. |
| **C — zero-shot + profile** | Profile + question, **no DB / no tools / no agent loop** — one LLM call. |

## Prerequisites

1. **pi** on PATH (`pi --version`). Installed globally via npm.
2. **MySQL** with the BEAVER DBs on `127.0.0.1:3307`, user/pass `beaver`/`beaver`
   (already loaded; verify: `mysql -h127.0.0.1 -P3307 -ubeaver -pbeaver -e "SHOW DATABASES"`).
3. **Profiles** in `profiles/{neutron,nova,dw}.md` (present).
4. **Question data** in `data/<db>/{dev,dev_sampled}.json` (present for neutron/dw;
   build more with `python data/build_local.py --datasets nova dw_real`).
5. Python deps: `pymysql` (in `.venv`). `mysql` CLI on PATH (used by `sql_exec`).

## One-time setup: OpenRouter + DeepSeek V4 Flash

The locked model is `deepseek/deepseek-v4-flash-0731` via OpenRouter.

```bash
export OPENROUTER_API_KEY=sk-or-...        # from https://openrouter.ai/keys
python harness/setup_openrouter.py         # confirms ctx=1,048,576, registers provider+model in pi
```

This also satisfies the plan's Phase-0 task *“Confirm DeepSeek-flash context limit
from OpenRouter `/models`”* — context (1,048,576) ≫ the 320K token guard.

> **Smoke test without an OpenRouter key:** the harness is model-agnostic via
> `PI_PROVIDER`/`PI_MODEL`. To exercise the pipeline on any provider pi already
> has credentials for, e.g. `export PI_PROVIDER=zai-coding-cn PI_MODEL=glm-5.2`
> (arm C then uses a single `pi -p --no-tools` call instead of a direct
> OpenRouter request).

## Phases

```bash
# Phase 0 — sanity: 1 neutron question × {A,B,C}, headless, scored end-to-end.
export BEAVER_MYSQL_PWD=beaver
python run_experiment.py --dataset neutron --phase phase0 --arm all

# Phase 1 — pilot: neutron n=20 (stratified by category × domain-knowledge).
python run_experiment.py --dataset neutron --phase pilot  --arm all

# Phase-1 go/no-go: project Phase-2 cost from the pilot before scaling.
python run_experiment.py --dataset neutron --phase pilot  --estimate-cost

# Phase 2 — main study (full per-dataset sampling; dw ~500 by default).
python run_experiment.py --dataset neutron --phase main
python run_experiment.py --dataset nova    --phase main
python run_experiment.py --dataset dw      --phase main --num-samples 500
python run_experiment.py --dataset dw_real --phase main
```

Common flags: `--num-samples N` (override sample size), `--limit M` (cap
questions), `--max-turns N` (default pilot=6, main=10), `--force` (re-run cached),
`--score-only` (rescore existing records, no model calls), `--arm {A,B,C,all}`.

## Outputs

```
runs/      manifest__<db>__<phase>__<n>.json   # frozen question list + seed (identical across arms)
results/   <db>__<phase>__<n>/
             armA.jsonl  armB.jsonl  armC.jsonl  # one record/question (pred_sql, usage, score, …)
             summary.json                          # accuracy, CIs, McNemar, subgroups, error taxonomy
```

`summary.json` reports per-arm accuracy + Wilson 95% CI, `% valid runnable SQL`,
mean turns / DB-queries, tokens in/out, latency, cost, subgroup accuracy by
`category` and `contains_domain_knowledge`, an error taxonomy, and the pairwise
**Δ + 95% CI** for **B−A**, **B−C**, **C−A** with exact McNemar p-values.

## Anti-cheat / leakage controls (validity)

Per plan §“Anti-cheat”:

- **Isolation:** each question runs in a fresh sandbox cwd
  (`$BEAVER_SANDBOX_ROOT/<db>_<arm>_<i>_<id>`, default `/tmp/beaver-sbx`).
  The prompt (question + profile) is piped via **stdin**, never a repo file.
- **Tooling:** `--no-builtin-tools --tools sql_exec` ⇒ the agent can only run
  read-only SQL. Web/fetch/search/read/bash are all off. `sql_exec` rejects any
  DML/DDL (the benchmark DB is never mutated).
- **Context:** `--no-extensions --no-skills --no-context-files --no-themes
  --offline` ⇒ no global skills/AGENTS.md/themes load and pi makes no startup
  network call beyond the LLM endpoint.
- **No leakage:** the agent sees only the NL question (+ profile in B/C). Gold
  `sql`/`tables`/`join_keys`/`column_mapping`/`domain_knowledge`/`sub_questions`
  are never passed (see `harness/prompts.py`).
- **Strongest mode (recommended for the real run):** run the orchestrator inside
  a throwaway **Docker/OrbStack** container that mounts only `results/` rw and
  the DB on `3307`, with outbound firewalled to OpenRouter + MySQL only.

## Caps (identical across cells)

| Cap | Value |
|---|---|
| MySQL query timeout | 20 s |
| Max agent turns | pilot 6 / main 10 (enforced in the `sql_exec` extension via `turn_end` + `ctx.abort()`) |
| Token runaway guard | 320 000 tokens/question |
| Exploration rows per `sql_exec` | 100 |

## Methodology notes

- **Execution accuracy** (Spider/BEAVER-style): gold and predicted SQL are both
  executed on the live DB; result sets compared as ordered tuples when the gold
  has `ORDER BY`, else as unordered multisets, with float tolerance (`1e-6` rel).
- **Candidate recovery:** if the agent is cut off by the turn cap before emitting
  a fenced `​```sql` block, the last SELECT it executed via `sql_exec` is used.
- Rescorable: tweak `harness/scorer.py` and re-run `--score-only`.
