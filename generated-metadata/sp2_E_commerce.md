# Additional Metadata

## Clarified Semantics

- `geolocation` is a geographic reference table keyed by `geolocation_zip_code_prefix` (not unique: ~19k distinct prefixes in ~1M rows, many rows repeat a prefix). `customer_zip_code_prefix`/`seller_zip_code_prefix` map into it to obtain lat/lng/city/state; the city/state values in geolocation are the source for the customer/seller city/state columns.
- `customers` has a many-to-one structure: each `customer_id` (row) is unique, but `customer_unique_id` is shared by ~6,342 rows, so one logical customer can hold multiple order accounts/orders.
- `order_items.order_item_id` is a per-order line number; an order can span 1..21 line items (one order_id → many product/seller rows).
- `order_payments.payment_sequential` is the sequence of payments made for a single order (1..29); multi-payment orders appear as multiple rows per order_id. Note split payment types: credit_card, boleto, voucher, debit_card, not_defined.
- `order_reviews.review_id` is not unique and `order_id` has repeats: a given order can receive multiple review rows.
- `orders.order_status` distribution is short-tailed: mostly "delivered" (~96k) with shipped/canceled/unavailable small counts; `order_delivered_customer_date` is NULL for non-delivered orders.
- `leads_closed.seller_id` is populated for all 842 closed leads and corresponds to a seller that converted; these same sellers also appear in `sellers` and `order_items`.
- `leads_qualified.mql_id` is the marketing-qualified lead id; only a subset of qualified leads appear in `leads_closed` (closed/won).
- `products.product_name_lenght`, `product_description_lenght`, `product_photos_qty` are stored as floats but are integer counts. `product_category_name` can be translated via `product_category_name_translation` (Portuguese → English).
- `sellers` provides the seller hub; sellers are geo-located via `seller_zip_code_prefix` only (no city/state signature beyond that).

## Potential Join Strategies

- **Order → customer geography**: join `orders.customer_id = customers.customer_id`, then `customers.customer_zip_code_prefix = geolocation.geolocation_zip_code_prefix` to attach lat/lng/city/state. Caveat: geolocation has many duplicate rows per prefix, so dedupe (pick one row per prefix) before joining to avoid fan-out.
- **Order ↔ items ↔ products/sellers** (e-commerce core): `orders.order_id = order_items.order_id`, then `order_items.product_id = products.product_id` and `order_items.seller_id = sellers.seller_id`. Caveat: order_items fans out per line, so aggregate before comparing order-level totals.
- **Payment vs item pricing**: `order_payments.order_id = order_items.order_id` (both fan out). Sum `price + freight_value` across order_items per order and compare to summed `payment_value`; flag order-level mismatches only after aggregation to avoid row multiplication.
- **Reviews per order**: `order_reviews.order_id = orders.order_id` (one-to-many; dedupe by `review_id`/order to get first review). Review score can be pivoted against order status or delivery dates.
- **Category translation**: `products.product_category_name = product_category_name_translation.product_category_name` to get English category labels; translate before grouping by category.
- **Lead funnel (mql)**: `leads_qualified.mql_id = leads_closed.mql_id` links contact/origin (`leads_qualified.origin`, date) to conversion outcome (won_date, business_type, segment). Caveat: only a fraction of the 8,000 qualified leads appear among the 842 closed leads, so outer join preserves attribution; use a left join from qualified to closed.
- **Closed leads → sellers**: `leads_closed.seller_id = sellers.seller_id` to enrich converted leads with seller hub geo (`sellers.seller_state`); can then bridge to `order_items.seller_id` to measure realised sales for won leads. Caveat: cardinality is tiny on the lead side, so prefer per-seller aggregates on the order side.
- **Customer ↔ seller geo proximity**: `customers.customer_zip_code_prefix = sellers.seller_zip_code_prefix` (customer↔seller link), optionally resolved to lat/lng through geolocation to compute distance. Caveat: one prefix maps to many sellers and many customers, producing a large cross-product; filter by `customer_state`/`seller_state` first.