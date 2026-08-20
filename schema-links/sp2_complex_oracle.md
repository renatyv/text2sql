# Schema Links

- version: 0.0.5
- dialect: sqlite
- database: file:/Users/renatyuldashev/Documents/ai-sql/custom-bench/data/sp2_lite_sqlite/databases/complex_oracle.sqlite
- schema: main

## Declared PK/FK Links

costs.channel_id -> channels.channel_id
costs.prod_id -> products.prod_id
costs.promo_id -> promotions.promo_id
costs.time_id -> times.time_id
customers.country_id -> countries.country_id
sales.channel_id -> channels.channel_id
sales.cust_id -> customers.cust_id
sales.prod_id -> products.prod_id
sales.promo_id -> promotions.promo_id
sales.time_id -> times.time_id

## Inferred Links

### month
- inferred: currency.month, times.calendar_month_number, times.day_number_in_month, times.fiscal_month_number

### year
- inferred: currency.year, times.calendar_year, times.fiscal_year
