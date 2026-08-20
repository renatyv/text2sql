# Additional Metadata

## Clarified Semantics

- `access_log` is noisy/corrupt: its `stamp` column mixes timestamps (`2016-01-*`, only 11 of 30 rows) with path-like strings (`/detail`, `/search`, `/top`), and its `action` column mixes `view` with random opaque tokens (`1CwlSX`, `6SN6DD`, ...). Do not rely on timestamp or path semantics for this table.
- `mst_categories.id` is **not unique**: id 6 is shared by both `cooking` and `food`. `id` cannot identify a single category; `name` is the meaningful key.
- `product_sales.category_name` is free text (`book`, `cd`, `dvd`). Only `book` and `dvd` appear in `mst_categories.name` — there is no `cd` category there, so the join on category name is only partial.
- `mst_products_20161201` and `mst_products_20170101` are two dated point-in-time snapshots of the same product master, not complementary tables. Compare them to observe product churn (e.g., `B001` present only in the 2016 snapshot; `D002`, `DAD` only in 2017).
- `invalid_action_log` mirrors `action_log`'s shape but contains no rows matching `action_log` by `(session, stamp)`; its sessions (`0CVKaz`, `1QceiB`) are absent from `action_log`. Treat it as a separate set of invalid/incomplete events (many null `stamp`/`products`/`amount`), not as a filtered subset of `action_log`.
- Session identifiers are not shared across the log tables (`action_log`, `activity_log`, `access_log`, `action_log_with_ip`, `form_log`, `read_log`); joining these on `session` will generally match nothing.
- `app1_mst_users` / `app2_mst_users` are small (2 rows each) per-app user masters keyed on the same `U001`/`U002` that appear in `mst_users`; each holds app-specific contact info.
- `purchase_log.amount` (100–800) and `action_log` "purchase" `amount` (1000/2000) are on different scales and different periods (2017 vs 2016) and are unrelated.

## Potential Join Strategies

- **User dimension join**: join any log's `user_id` to `mst_users.user_id` (authoritative 320-row master) for `sex`/`birth_date`/`register_date`/`register_device`/`withdraw_date`. Caveat: log tables use only a small subset (`U001`–`U012`) of the 30 distinct `mst_users` ids; also note duplicate user_id X tables can fan out per log row.
- **User master split (per-app)** : `mst_users.user_id` = `app1_mst_users.user_id` (gives `email`) and = `app2_mst_users.user_id` (gives `phone`). Each app master has exactly those 2 users, so only those ids pick up contact details.
- **Product dimension from logs**: `action_log.products` and `dup_action_log.products` are comma-separated lists of `product_id` (e.g. `D001,D002`) — must be split per token before joining to `mst_products_*.product_id`. Prefer `mst_products_20170101` as snapshot since it covers both `D001` and `D002`; the 2016 snapshot lacks `D002` (src span limited to `A001/A002/B001/B002/C001/D001`).
- **Category name join (partial)**: `product_sales.category_name = mst_categories.name` matches only the `book` and `dvd` rows, not `cd`; a full outer or filter-by-known-names avoids losing `cd`.

- **category identity**: since `mst_categories.id` is duplicated, join on `name` (unique) rather than `id`; do not use `id` for counting categories.