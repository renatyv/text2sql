Agentic text-to-SQL experiment: does a pre-generated [db-snooper](https://github.com/renatyv/db-snooper)
profile of the target DB improve a coding agent's **execution accuracy** on
[BEAVER](https://huggingface.co/datasets/BeaverBench/beaver), vs. raw DB access?

Also runs BIRD Mini-Dev (`--dataset bird_mini_dev`) and Spider 2.0-lite SQLite
subset (`--dataset sp2_lite_sqlite`): these execute natively on the original
.sqlite files under `data/bird_mini_dev/` and `data/sp2_lite_sqlite/` — they are
NOT loaded into MySQL. One-time setup: `make load-bird` / `make load-spider2`,
then `make generate-profiles DB=...`; run with `make benchmark-bird` /
`make benchmark-spider2`. Scoring follows each benchmark's official semantics
(`harness/scorer.py`, `harness/spider2_eval.py`).

Project is managed by `uv`

The (BEAVER) databases are loaded to MySQL running in docker on localhost port 3307, user and password in the .env file. Use `--skip-ssl`
