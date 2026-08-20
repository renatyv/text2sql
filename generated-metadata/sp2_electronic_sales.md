# Additional Metadata

## Clarified Semantics
- `customers.customer_id` is a per-order customer row id, while `customer_unique_id` groups repeat purchases by the same person; one unique id can map to multiple `customer_id`s. `index` is just an ordinal row counter (0..rows-1), not meaningful.
- `order_payments.payment_sequential` is the installment-split sequence for one order; one order may have many payment rows. `payment_installments` counts installments, `payment_value` is per-payment-row amount (sum over rows = order total).
- `order_reviews` is many-to-one on `orders`: multiple reviewed rows per order is possible (`review_id` has 98410 distinct vs 98673 distinct order_id). `review_creation_date` is a date (time truncated to 00:00:00); `review_answer_timestamp` carries time.
- `orders.order_delivered_customer_date` and `order_delivered_carrier_date` have nulls for non-delivered/failed statuses (`canceled`, `unavailable`); delivery-time computations should filter on `order_status='delivered'`.
- `order_estimated_delivery_date` has only 459 distinct dates; hundreds of orders share the same estimate date.
- `products` dimension fields (`product_name_lenght`, `description_lenght`, `photos_qty`, sizes, weight) are nullable, and `product_category_name` has ~610 nulls; category translation is only meaningful for non-null categories.
- `geolocation` is coarse-grained (zip-code prefix level), not per customer/seller; multiple coordinates can exist per zip prefix while `customer_*_prefix`/`seller_*_prefix` use the same prefix code, so location joins are many-to-many and approximate.
- `payment_type` values include both direct (`boleto`, `credit_card`) and declined statuses; treat it as label text.
- `orders.order_approved_at`, delivery timestamps, and `order_purchase_timestamp` are ISO timestamps; `order_estimated_delivery_date` and review creation dates are dates.

## Potential Join Strategies
- `orders` → `order_items` on `orders.order_id = order_items.order_id`: 1-to-many (order_items holds up to 21 `order_item_id`). Only 98666 of 99441 orders appear in order_items, so item-free orders (e.g. canceled/unavailable) are dropped in an inner join; filter status first if analyzing delivered orders.
- `orders` → `order_payments` on `order_id`: 1-to-many, payments often >=1 rows per order. Compare summed `payment_value` per order against item-level `SUM(price)+SUM(freight_value)` to verify totals.
- `orders` → `order_reviews` on `order_id`: 1-to-many (some orders have multiple reviews); dedupe if a single score per order is needed.
- `order_items` → `products` on `product_id`: both have 32951 distinct ids, effectively the FK; join loses no products but `product_category_name` has nulls.
- `order_items` → `sellers` on `seller_id`: all 3095 sellers present in order_items; each item row maps to one seller, so join is many-to-1 from items.
- `products` → `product_category_name_translation` on `product_category_name`: small lookup (71 rows), 1-to-1; null categories won't match.
- `customers` → `orders` on `customer_id`: 1-to-many (one order each `customer_id`, multiple orders per `customer_unique_id`). To aggregate per unique customer, group orders by `customer_id` joined to `customer_unique_id`.
- `customers` ↔ `geolocation` on `customer_zip_code_prefix = geolocation_zip_code_prefix`, and `sellers` ↔ `geolocation` on `seller_zip_code_prefix = geolocation_zip_code_prefix`: prefix-level only, many-to-many, geometry approximate; use for state/city confirmation rather than exact addresses.
- Cross-customer/seller `state` and `city` links (schema-links city/state): join `customers.customer_state`=`sellers.seller_state` and `customer_city`=`seller_city` for delivery/fulfillment-region analysis; city names are lowercase text and may not be uniformly normalized across the two tables.