# Schema Links

- version: 0.0.5
- dialect: sqlite
- database: file:/Users/renatyuldashev/Documents/ai-sql/custom-bench/data/sp2_lite_sqlite/databases/E_commerce.sqlite
- schema: main

## Declared PK/FK Links

No declared PK/FK links found.

## Inferred Links

### city
- inferred: customers.customer_city, sellers.seller_city

### mql
- inferred: leads_closed.mql_id, leads_qualified.mql_id

### order
- inferred: order_reviews.review_creation_date, orders.order_estimated_delivery_date

### product
- inferred: leads_closed.declared_product_catalog_size, products.product_description_lenght

### state
- inferred: customers.customer_state, sellers.seller_state

### zip
- inferred: customers.customer_zip_code_prefix, sellers.seller_zip_code_prefix
