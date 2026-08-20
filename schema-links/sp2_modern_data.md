# Schema Links

- version: 0.0.5
- dialect: sqlite
- database: file:/Users/renatyuldashev/Documents/ai-sql/custom-bench/data/sp2_lite_sqlite/databases/modern_data.sqlite
- schema: main

## Declared PK/FK Links

No declared PK/FK links found.

## Inferred Links

### pizza
- inferred: pizza_clean_customer_orders.order_id, pizza_clean_runner_orders.order_id, pizza_customer_orders.order_id, pizza_get_exclusions.order_id, pizza_get_extras.order_id, pizza_runner_orders.order_id

### company
- inferred: companies_dates.company_id, companies_funding.company_id, companies_industries.company_id

### runner
- inferred: pizza_clean_runner_orders.runner_id, pizza_runner_orders.runner_id, pizza_runners.runner_id

### total
- inferred: pizza_get_exclusions.total_exclusions, statistics.total_cases, statistics.total_deaths

### pizza
- inferred: pizza_clean_customer_orders.customer_id, pizza_customer_orders.customer_id
