# Additional Metadata

## Clarified Semantics

- Distinguished-customer model: `olist_customers.customer_id` is unique per order, while `customer_unique_id` identifies the person; a given customer can appear in multiple order rows, so count customers via `customer_unique_id`.
- `olist_order_items`: `(order_id, order_item_id)` is a unique composite key; all 21 possible `order_item_id` values occur, but for some orders the item numbers are not contiguous (gaps).
- All 32,951 `product_id`s present in `olist_products`/`olist_products_dataset` appear in `olist_order_items`, so item↔product joins are essentially lossless.
- `olist_order_reviews` is many-to-one on orders: 99224 rows but only 98,673 distinct `order_id`, and `review_id` (98,410 distinct) repeats, so a single order can carry multiple review rows; `review_score` is on a 1–5 scale.
- `olist_order_payments` holds one row per payment stripe; many orders have multiple payments (`payment_sequential` 1..29), summing `payment_value` per `order_id` reconstructs each order total.
- `olist_orders` has 99,441 rows but only 98,666 orders have items and 99,440 have payments, so joins from orders to items lose a small set (~775) of orderless/inventory-less orders.
- `olist_geolocation` ~1,000,163 rows are essentially all within Brazil's lat/lng box; there are multiple lat/lng coordinates per zip prefix and one zip can map to several city/state spellings.
- `product_category_name_translation` (71 rows) has fewer categories than `olist_products` (73), so some Portuguese category names have no English equivalent.

## Potential Join Strategies

- **Translations**: `olist_products.product_category_name = product_category_name_translation.product_category_name` — 1:1; beware ~2 untranslated categories and nulls (610 product rows) on both sides.
- **Orders ↔ payments**: `olist_orders.order_id = olist_order_payments.order_id` — 1:many, nearly full coverage; to get per-order total, aggregate payments before joining to avoid row multiplication.
- **Orders ↔ items**: `olist_orders.order_id = olist_order_items.order_id` — 1:many; a few orders have no items, filter with INNER join if items are required.
- **Items ↔ products/translations**: `olist_order_items.product_id = olist_products.product_id` then category translation; 1:1 at each hop, keeps granularity but each sell of same product appears per order row.
- **Items ↔ sellers**: `olist_order_items.seller_id = olist_sellers.seller_id` — repeatable many products per seller.
- **Regional pairing (customers ↔ sellers via geography)**: both expose `*_zip_code_prefix`, `*_city`, `*_state`. Match on `state` is clean (27 vs 23 values, ~SP dominated) or on `zip_code_prefix` for finer grain; city-name equivalence is unreliable due to spelling/case differences.
- **Geo‑lookup**: `olist_customers.zip = olist_geolocation.geolocation_zip_code_prefix` (same prefix axis) to recover lat/lng and validate region; caveat: prefix is duplicated with multiple coordinates and mixed city/state variants, so use for aggregation, not unique mapping, and optionally dedup for avglat/lng.
- **Review vs delivery timing**: joins `olist_order_reviews.review_creation_date` ↔ `olist_orders.order_delivered_customer_date`/`order_estimated_delivery_date` treat both as ISO datetime strings; delivery-date cols are null for non-`delivered`/`shipped` statuses, so pairs only those orders to avoid spurious gaps.