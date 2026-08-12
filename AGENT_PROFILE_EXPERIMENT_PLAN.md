# Plan: Agentic text-to-SQL with vs. without db-snooper profiles

## 1. Goal & hypothesis

**Goal.** Does a pre-generated [db-snooper](https://github.com/renatyv/db-snooper) profile of the target DB improve a coding agent's
text-to-SQL **execution accuracy** on BEAVER, vs. raw DB access.

**Hypothesis.** A pre-loaded schema+data profile raises accuracy **and** lowers cost (fewer DB
round-trips, turns, tokens) within a fixed agent budget.

**New method.** Unlike original BEAVER, this is **agentic**:
the agent probes the DB and writes SQL itself. Comparison = *agent exploration* vs. *agent
exploration helped by a profile*.

---

## Experimental design

| Arm | Context |
|---|---|
| **A — baseline** | NL question + MySQL connection + SQL-exec tool. No schema hints. |
| **B — profile** | Same as A, plus a **frozen db-snooper `<db>.md` profile** in the initial prompt. |
| **C — zero-shot + profile** | NL question + the **same frozen `<db>.md` profile**, but **no DB connection / SQL-exec tool** and **no agent loop** — a single LLM call produces SQL directly. Non-agentic control that isolates the profile's standalone value vs. agentic exploration (B). |

Never pass gold `tables` / `join_keys` / `column_mapping` / `domain_knowledge` /
`sub_questions` to the agent — those are the answer. Agent sees only NL question + DB (+ profile
in B).

---

## Datasets & sampling

The Beaver benchmark databases are already loaded to MySQL running in docker on port 3307. User `beaver` password `beaver`.
Profiles are already generated in `prpfiles/`

| Dataset | DB | Size | Use |
|---|---|---|---|
| neutron | neutron | 1017 | main, full |
| nova | nova | 1053 | main, full |
| dw | dw | 5787 | sample ~500 (biggest DB → tests profile-size effects) |
| dw_real | dw | 121 | run **fully** as sanity check (reuses dw profile) |

- **Pilot:** reuse `data/<db>/dev_sampled.json` (n=100, seed 77) to line up with current runs.
- Stratify by `category` and `contains_domain_knowledge` for balanced difficulty + subgroup reports.
- Freeze question list + seed into a run manifest so both arms see identical questions.
- **CLI:** `--num-samples N` selects how many questions per dataset at runtime (full dataset when
  omitted); pairs with `--dataset {neutron,nova,dw,dw_real}`. Overrides the per-dataset defaults above.

---

## Metrics

**Primary:** execution accuracy (%) per arm per dataset; pairwise **Δ** with 95% CI — **B − A** (does the profile help the agent?), **B − C** (does agentic exploration beat profile-alone?), **C − A** (does the profile alone beat un-aided exploration?) — **and cost**
(turns, DB queries, tokens in/out, latency, actual $ spent) per arm per dataset.

**Secondary:** #DB queries/question, #agent turns, LLM tokens in/out, latency; % questions yielding
*valid runnable* SQL; profile token cost (`<db>.md` size) — a real deployment consideration.

**Subgroup:** accuracy by `category` / `detailed_category`, split by `contains_domain_knowledge`
(hypothesis: profile helps most on domain-knowledge + complex-join questions).

**Error taxonomy (sampled):** wrong table / wrong join / wrong agg / syntax / timeout.

---

## Phasing (cost-aware — agents are expensive)

- **Phase 0 — setup & sanity:** generate+commit profiles, log token sizes, confirm MySQL reachable;
  get **1 neutron question** producing valid SQL headlessly in **all three** arms A, B & C.
  *Exit:* scored sql for all arms, end-to-end.
- **Phase 1 — pilot signal:** neutron n=20, default temp, paired. *Before* go/no-go, **estimate
  Phase 2 cost** (≈ total questions × arms × runner × avg tokens/question × $/token) and confirm the
  budget.
- **Phase 2 — main study:** neutron+nova full, dw ~500, dw_real full; default temp; collect all
  secondary metrics.
- **Phase 3 — analysis & writeup:** Δ + 95% CI, McNemar, subgroups, error taxonomy; include **C
  (zero-shot + profile)** to separate profile-alone from agentic+profile; side-by-side with
  **fewshot setting-0** (all ETE); cost/accuracy tradeoff chart.

---

## Locked decisions

1. **Runner:** **pi only** (opencode deferred). 3 cells = pi × {A, B, **C**}, where **C =
   `zero-shot with profile`** (single LLM call, no tools / no agent loop). Compare **paired within
   the runner** (Δ + CI per arm pair).
2. **Model:** `deepseek/deepseek-v4-flash-0731` via OpenRouter; reasoning = **model default**
   (no effort override), identical across all cells. Verify from a transcript that the runner
   doesn't silently force an effort level.
3. **Profile variant:** **injected `.md`** (arms B & C).
4. **Caps (identical across cells):** max **10 turns** (pilot 6),
   ~**320K total tokens/question** guard (runaway only), **20s MySQL query timeout**. Confirm
   DeepSeek-flash context limit from OpenRouter `/models` in Phase 0.
5. **Scale:** neutron **full (1,017)**, nova **full (1,053)**, dw **stratified ~500**, dw_real
   **full (121, directional)**. ≈2,600 questions × 3 arms × 1 runner. Pilot n=20 first.

## Anti-cheat / leakage controls (validity-critical)

The repo holds the answers (`beaver-query/*.parquet`, `data/<db>/dev*.json` with gold
`sql`/`tables`/`join_keys`/`domain_knowledge`, `eval/` gold refs); dataset is public on HF.

1. **Sandbox:** run each question in a fresh, minimal dir holding only the prompt (question
   **inline**, not a file), the profile (arms B & C), DB connection details (A & B only — C is
   zero-shot with no tools), and a write-only
   output path. **Never point the agent at the repo.** Best: throwaway **Docker/OrbStack** container
   mounting only the output dir rw.
2. **Network:** **disable web/fetch/search tools** in both runners; **block outbound**
   — allow only OpenRouter + mysql running in docker with all dbs pre-loaded
