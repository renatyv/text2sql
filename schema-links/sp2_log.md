# Schema Links

- version: 0.0.5
- dialect: sqlite
- database: file:/Users/renatyuldashev/Documents/ai-sql/custom-bench/data/sp2_lite_sqlite/databases/log.sqlite
- schema: main

## Declared PK/FK Links

No declared PK/FK links found.

## Inferred Links

### user
- inferred: access_log.user_id, action_log.user_id, action_log_with_ip.user_id, app1_mst_users.user_id, app2_mst_users.user_id, dup_action_log.user_id, invalid_action_log.user_id, mst_users.user_id, mst_users_with_card_number.user_id, purchase_log.user_id

### products
- inferred: dup_action_log.products, mst_products_20161201.product_id, mst_products_20170101.product_id
