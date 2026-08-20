# Schema Links

- version: 0.0.5
- dialect: sqlite
- database: file:/Users/renatyuldashev/Documents/ai-sql/custom-bench/data/sp2_lite_sqlite/databases/bank_sales_trading.sqlite
- schema: main

## Declared PK/FK Links

No declared PK/FK links found.

## Inferred Links

### date
- inferred: customer_nodes.end_date, customer_nodes.start_date, customer_transactions.txn_date, shopping_cart_users.start_date

### number
- inferred: cleaned_weekly_sales.month_number, interest_metrics._month, shopping_cart_events.sequence_number

### customer
- inferred: customer_nodes.customer_id, customer_transactions.customer_id

### date
- inferred: bitcoin_prices.market_date, bitcoin_transactions.txn_date

### member
- inferred: bitcoin_members.member_id, bitcoin_transactions.member_id

### region
- inferred: customer_nodes.region_id, customer_regions.region_id

### shopping
- inferred: shopping_cart_events.cookie_id, shopping_cart_users.cookie_id

### shopping
- inferred: shopping_cart_events.page_id, shopping_cart_page_hierarchy.page_id

### txn
- inferred: bitcoin_transactions.txn_id, customer_transactions.txn_amount

### year
- inferred: cleaned_weekly_sales.calendar_year, interest_metrics._year
