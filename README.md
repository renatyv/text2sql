# profiling-test

Does a pre-generated [db-snooper](https://github.com/renatyv/db-snooper) profile improve an agent's execution accuracy on [BEAVER](https://huggingface.co/datasets/BeaverBench/beaver), compared with raw database access?

**Short answer: no.** Across 100 questions per database per arm, the profile moved execution accuracy by approximately nothing (every pairwise McNemar test p = 1.0) while multiplying pooled input tokens by ~6. Metadata alone — a quarter of the tokens — did just as well.

## Results

Execution accuracy, 100 questions per database per arm, identical prompts, tools, model, and budgets:

| Database | Raw | + Profile | + Metadata |
|---|---|---|---|
| neutron | 13% | 13% | 13% |
| nova | 9% | 8% | 11% |
| dw | 5% | 4% | 3% |

The profile arm also dropped from ~4.6 to ~2.2 turns and from 7.8 to 1.3 database queries per question — the agent read the profile, stopped exploring, and was wrong sooner. Open `results-viz.html` in a browser for the full per-run breakdown (turns, tokens, cost, failure modes).

The agentic arms run in a fresh, unprivileged Docker/OrbStack container for every question. Pi uses the purpose-built `sql_exec` tool; the optional Claude Code, OpenCode, and Codex runners use their built-in tools with the container's MySQL/Python utilities. The database account enforces SELECT-only access.

## Experiment arms

- `raw` — agent + MySQL CLI.
- `profile` — raw access + frozen db-snooper profile.
- `metadata` — raw access + aggregated metadata.
- `profile_metadata` — raw access + both artifacts.

All four arms use the same agent, prompt instructions, error-avoidance checklist, tools, model, and caps; only the supplied context differs. The default model and caps live in [`harness/config.py`](harness/config.py). The fixed evaluation budget is ten turns and 600 seconds per question. Exhausting either budget counts as an incorrect answer; only transient provider/API failures are retried.

## Isolation model

Each agent question gets `docker run --rm` on the internal `beaver-sandbox` network. It has an empty `/workspace`, runs as the non-root `node` user, has no Docker socket or repo mount, and is deleted after the run. A wall-clock timeout explicitly force-removes the container as well.

The only permitted connections are:

- MySQL at `beaver-mysql:3306`, using a separate account that is reset at experiment startup to `SELECT` on `neutron`, `nova`, and `dw` only.
- `https://openrouter.ai`, via `beaver-egress-proxy`. The proxy is the only container with internet access and accepts `CONNECT` only for the exact allow-listed hostname.

The host's loader/scorer credentials and coding-agent configuration are never mounted into an agent. The runner mounts only its own read-only agent configuration and pins the selected model. This prevents filesystem state from one question reaching the next and prevents arbitrary internet access. It cannot prevent the required OpenRouter model call itself from seeing the prompt and tool outputs.

## Setup

Prerequisites: OrbStack or Docker, the existing `beaver-mysql` container exposing MySQL on host port 3307, and `uv`.

```bash
cp .env.example .env   # then fill in your OPENROUTER_API_KEY
uv sync
uv run --group data python data/download_hf.py   # only if data/ is missing (re-creates the seed-77 samples)
docker build -t beaver-agent -f Dockerfile.agent .
docker build -t beaver-egress-proxy -f Dockerfile.proxy harness/egress
uv run python run_experiment.py --dataset neutron --phase phase0 --arms raw profile metadata profile_metadata
```

At startup the runner creates the two networks, attaches MySQL to the internal one, starts the proxy, and provisions `beaver_agent`. The privileged host MySQL credentials still come from `.env` (`BEAVER_MYSQL_*` or `MYSQL_*`). Do not set `BEAVER_AGENT_MYSQL_PWD` unless a stable debugging password is necessary; otherwise a new random password is used for each experiment process.

Useful runs:

```bash
uv run python run_experiment.py --dataset neutron --phase pilot
uv run python run_experiment.py --phase main --samples neutron=20 nova=20 dw=20 --arms raw profile metadata --workers 8 --max-turns 10
uv run python run_experiment.py --dataset neutron --phase pilot --estimate-cost
uv run python run_experiment.py --dataset neutron --phase pilot --score-only
```

`--no-container` is a legacy debugging path. It runs pi on the host with `sql_exec.ts`; it does not provide the container isolation described above.

Completed records are reused only when their protocol fingerprint matches the current prompts, artifacts, model, runner, reasoning effort, and budgets. Prompt or budget changes therefore cannot silently mix incompatible results. While pi runs, the progress bar shows the latest completed agent turn and database-query count.

## Switch coding agents

The default is pi. Set `BEAVER_AGENT` before a run; all choices retain the same fresh container, SELECT-only MySQL account, and OpenRouter-only proxy.

```bash
BEAVER_AGENT=claude uv run python run_experiment.py --dataset neutron --phase phase0
BEAVER_AGENT=opencode uv run python run_experiment.py --dataset neutron --phase phase0
BEAVER_AGENT=codex uv run python run_experiment.py --dataset neutron --phase phase0
```

Choose any OpenRouter model with `--model`; its slug is passed through unchanged (an optional `openrouter/` prefix is accepted). Reasoning effort defaults to `medium` and can be changed with `--effort`. For example:

```bash
uv run python run_experiment.py --dataset neutron --phase phase0 --model openai/gpt-5.6-luna-pro --effort medium
```

`BEAVER_AGENT_MODEL` remains available for scripted runs. Unknown custom models report zero projected cost until their rates are added to `harness/openrouter_models.json`. Claude Code is configured with OpenRouter's Anthropic-compatible endpoint; Codex and OpenCode use its OpenAI-compatible endpoint. Pi and Claude have a CLI turn cap; Codex and OpenCode retain the prompt budget and the same 10-minute container wall-clock cap. Non-pi runs record execution accuracy, but their CLI telemetry is deliberately reported as unavailable rather than a false zero; use pi when you need turns, database-query counts, token, or cost projections.

## Verify the boundary

After a run, the sandbox should be internal and contain only the proxy and MySQL. The egress network should contain only the proxy.

```bash
docker network inspect beaver-sandbox
docker network inspect beaver-net
docker run --rm --network beaver-sandbox --entrypoint sh beaver-agent -lc \
  'curl --noproxy "*" --connect-timeout 5 -I https://example.com || true; \
   curl -x http://beaver-egress-proxy:8888 -I https://example.com || true'
```

The direct request must fail because the network has no internet route; the proxied request must fail with `CONNECT tunnel failed, response 403`. A request to `https://openrouter.ai` through that proxy is the one allowed external route.

## Layout

```text
harness/
  runner_container.py      default ephemeral-container runner
  network.py               network + SELECT-only MySQL account setup
  egress/egress-proxy.js   exact-host HTTPS CONNECT allow-list
  turn_guard.ts            hard agent turn cap
  prompts.py               arm-specific prompts
  scorer.py                execution-accuracy scorer
  runner_zeroshot.py       no-tools OpenRouter arm
Dockerfile.agent           coding-agent CLIs + analytics tools image
Dockerfile.proxy           egress proxy image
profiles/                  db-snooper profiles
data/                      BEAVER splits (regenerable via data/download_hf.py)
results/                   per-run records and summaries (ignored)
```

## Data

`data/` holds the BEAVER splits used by the harness: the full question set (`dev.json`), the seed-77 sample actually run (`dev_sampled.json`), and the official table metadata (`dev_tables.json`). Everything is regenerable from Hugging Face with `uv run --group data python data/download_hf.py --sample 100`, or offline from local parquet dumps with `data/build_local.py`.

## License

[MIT](LICENSE)
