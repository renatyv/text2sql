# Additional Metadata

## Clarified Semantics

- `name` is the shared dataset key across every table; `problem.name` is a PK (necessarily unique). All other tables hold multiple rows per `name`.
- `version` is a dataset-feature-engineering/pipeline version (1..8). It is not exhaustive per dataset: high versions (7,8) have few rows and some datasets only appear at low versions.
- `step` (1..3) is the stacking staging index; `model`, `model_score`, `model_importance`, and `feature_importance` all carry `step`. In `model`, each (name,version) generally has all three steps (101 rows each step), while `feature_importance` has step 3 far less often (405 of 233-... of 1241 per step1/2).
- `Stack` is a special reserved meta-model present only in `model_score` (it is the stacked-ensemble score) and is **absent** from `model_importance`.
- `L1_model` in `model` records whether the level-1 (base) learner family is `tree` or `regression`; `solution_ext` is literally a view reducing `model` to distinct (name, version, L1_model).
- Model-id suffixes are meaningful: ids end in `E`, `C`, `R`, `Q`, `M` etc. denoting variant families (e.g. RFCG/RFRA vs RFRP/DTRP) reused across both classification and regression families; `L1_model` disambiguates base family.
- `model_importance.model` stores per-model importance only for base models. Joining to `model_score` on (name,version,step,model) matches 2566 of 2872 model_score rows; `KNCD` is the observed non-matching base model id.
- `eda` is per (name, version, feature) with per-feature flags `drop_user`, `drop_correlation`, `target` and `type` (`num`/`cat`); `range` is a BLOB, 306 rows have NULL `type`/`range` (likely a Phase/pipeline where type not yet determined).
- `solution` has exactly one row per (name, version) (101 unique combos) describing a configuration: `nb_model`, `nb_feature`, `score`, `test_size`, `resampling`. It is configuration-level, not per-step.
- `problem` holds external dataset metadata (Kaggle `path`), task `type` (classification/regression) and the `target` column name.

## Potential Join Strategies

- **problem ↔ every table on `name`** (1:1 per dataset from `problem`): enrich any dataset metric with `problem.type` (classification vs regression) and `problem.target` (label column). Useful as a filter/partition, especially since `eda` also flags `target` rows.
- **eda ↔ feature_importance on (name, version)** (+ optionally feature name): pair per-feature flags (`drop_user`, `drop_correlation`, `type`) with per-step `feature_importance.importance`; note `feature_importance` has only 3 steps and its own distinct feature list (294 dist) vs eda (335), so not all features resolve.
- **model_score ↔ model on (name, version, step)**: brings `L1_model` (tree vs regression) to each base model score; joins `model` where each (name,version) has all 3 steps (101/step).
- **model_score ↔ model_importance on (name, version, step, model)**: pair each base model's test_score with its stacking `importance`, filtering out `Stack`. Caveat: model_importance does not hold Stack, and ≥1 base model (KNCD) is absent from model_importance.
- **model_score ↔ model_importance (self, model='Stack' vs rest)**: derive the strength of stacking by comparing `Stack.test_score` to the max non-Stack test_score per (name, version, step) — this is exactly what the `stack_ok` view computes (`strong` when >, `soft` when `=`). Ambiguity: a tie yields `soft`; both only exist when a `Stack` row also has a `test_score`.
- **solution ↔ model_score on (name, version)**: compare configured `solution.nb_model`/`nb_feature`/`score` to the actual number/identities of models and to realized per-step test scores; `solution` has one row per (name,version) so collapses the 3 per-step model rows.
- **solution ↔ problem on `name`**: relates the reported solution `score` to dataset `type`/`target`, useful since score interpretation differs by classification vs regression.
- **stack_ok ↔ stack_ok_score**: `stack_ok_score` pivots `stack_ok` Stack test_scores across step 1/2/3 into score_1/2/3 columns, which 1:1 aligns with `stack_ok` rows that cover all 3 steps (64 rows vs 139 total; the rest lack all-step coverage).