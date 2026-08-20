# Schema Links

- version: 0.0.5
- dialect: sqlite
- database: file:/Users/renatyuldashev/Documents/ai-sql/custom-bench/data/sp2_lite_sqlite/databases/Brazilian_E_Commerce.sqlite
- schema: main

## Declared PK/FK Links

No declared PK/FK links found.

## Inferred Links

### products
- inferred: olist_products.product_description_lenght, olist_products.product_height_cm, olist_products.product_length_cm, olist_products.product_name_lenght, olist_products.product_photos_qty, olist_products.product_width_cm, olist_products_dataset.product_description_lenght, olist_products_dataset.product_height_cm, olist_products_dataset.product_length_cm, olist_products_dataset.product_name_lenght, olist_products_dataset.product_photos_qty, olist_products_dataset.product_width_cm

### olist
- inferred: olist_customers.customer_city, olist_sellers.seller_city

### order
- inferred: olist_order_reviews.review_creation_date, olist_orders.order_estimated_delivery_date

### products
- inferred: olist_products.product_id, olist_products_dataset.product_id

### state
- inferred: olist_customers.customer_state, olist_sellers.seller_state

### zip
- inferred: olist_customers.customer_zip_code_prefix, olist_sellers.seller_zip_code_prefix
