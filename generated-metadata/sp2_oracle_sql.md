# Additional Metadata

## Clarified Semantics

- `customer_favorites.favorite_list` is a denormalized comma-separated string of product IDs (not a FK-joined set).
- `customer_reviews.review_list` is a comma-separated string of `product_id:GRADE` entries (grades A/B/C). Not normalized.
- `customer_order_products_obj.product_coll` is a JSON-array-like concatenated string of `{"product_id","product_name"}` objects, one per orderline (denormalized); it can contain repeated products.
- `orders.delivery` is entirely NULL in the DB → represents not-yet-delivered orders; don't rely on it as a filter.
- `picking_log.activity` has three distinct states (values A/D/P). `picking_log.location_id` and `pickline_no` are nullable → not every log row maps to a picking_line row.
- `picking_log.pickline_no` is the composite-FK counterpart of `picking_line.line_no`.
- `monthly_budget` covers only 2 products over 2018–2019; `monthly_sales` covers all 10 products over 2016–2018 (overlapping only in 2018).
- `product_minimums` also covers only the same 2 budget products; `qty_minimum` and `qty_purchase` set reorder thresholds.
- `monthly_orders` (view) derives order line quantities per product per month from `orders`/`orderlines`; granularity (product, month).
- `web_demographics` column prefix convention: leading `m_`/`f_` = gender, middle `_tw_`/`_fb_` = channel, suffix `_cnt` = counts, `_qty` = quantities. `gender_dim` and `channels_dim` are lookup tables decoding these prefixes.
- `web_devices`, `web_demographics`, `server_heartbeat`, `ticker`/`stock` are standalone/keyed-by-day or keyed-by-symbol tables with no link to the ecommerce tables.
- `product_alcohol.sales_volume` (330/500) corresponds to packaging bottle sizes but is not an explicit FK link.
- Tables with no meaningful rows or failed DDL: `emp_hire_periods_with_name` (view-definition error, skipped), and empty tables `conway_gen_zero`, `favorite_coll_type`, `id_name_coll_entries`, `id_name_coll_type`, `id_name_type`.

## Potential Join Strategies

- Purchases → Inventory: join `inventory.purchase_id = purchases.id` (1 purchase → many inventory rows when a purchase splits across locations). Caveat: only a subset of purchases (62 of 180) appear in inventory, so isolate misses with a left join.
- Orders → orderlines → products: central consumer-demand path via `orderlines.order_id`/`orderlines.product_id`.
- Orders → picking_line (`picking_line.order_id = orders.id`) → picking_list (`picking_list.id = picking_line.picklist_id`) → employees/picker (`picker_emp_id`) to attribute order fulfillment to a picker.
- picking_log ↔ picking_line: composite join on `(picklist_id, pickline_no)` = `(picklist_id, line_no)`; expected 1:1 per line but nullable log rows make it a left join.
- employees self-join on `employees.supervisor_id = employees.id` builds the org hierarchy; `emp_hire_periods` gives 1 employee → many tenure/title periods, so joining to current title is ambiguous without a start/end window.
- products is the central hub: `products.id` links `orderlines`, `purchases`, `inventory`, `monthly_sales`, `product_alcohol`, `product_minimums`, `monthly_budget`; `products.group_id → product_groups.id`.
- Inventory ↔ Purchases ↔ Product aggregation: `inventory_totals` (per-product stock) can be compared to purchases and sales via product_id; caveat `monthly_budget` only exists for 2 products.
- Customers → favorites/reviews: `customer_favorites.customer_id` and `customer_reviews.customer_id` are 1:1 (PK) but only a subset of customers have rows → use left join.
- `packaging_relations` self-join: `packaging_id` (container) → `contains_id` (contained) with `qty` = count per container; allows recursive nesting (pallet → box → bottle).
- `brewery_products` view exposes (brewery, product) pairs that have purchases; join to `purchases` for quantities/costs per brewery-product.
- `web_pages (app_id, page_no)` composite PK joins `web_counter_hist` and `web_page_visits`; `web_page_counter_hist` view pre-decorates with `friendly_url`.
- Web analytics combine day-keyed standalone tables (web_devices, web_demographics) with each other by `day`, and with `web_counter_hist.day`/`web_page_visits.visit_time` date.
- `stock.symbol` ↔ `ticker.symbol` is a trivial 1-key join (single ticker symbol).