# Additional Metadata

## Clarified Semantics

- **bitcoin_prices.market_date** is stored as text in `DD-MM-YYYY` format (e.g. `29-08-2021`); same human-readable format is used for **bitcoin_transactions.txn_date**, whereas `txn_time` uses ISO-8601 (`YYYY-MM-DDTHH:MM:SS.sssZ`).
- **bitcoin_prices** is the daily OHLCV series; price/open/high/low are USD floats, `volume` and `change` are stored as text (strings such as `1.04M`, `-2.11%`), so numeric aggregation must parse these.
- **bitcoin_transactions**: only `BUY` and `SELL` types; `percentage_fee` is 0–0.3 (mostly 0.3). `txn_date` is the DD-MM-YYYY date, `txn_time` gives full timestamp.
- **bitcoin_members.region** values use mixed case/full names ("United States", "Australia"...) while sales/region tables use uppercase codes ("USA", "EUROPE"...) — no direct join on this string.
- **weekly_sales** vs **cleaned_weekly_sales**: cleaned version is weekly_sales plus derived columns (`week_date_formatted`, `week_number`, `month_number`, `calendar_year`, `age_band`, `demographic`, `avg_transaction`) and `segment` NULLs replaced by literal `"unknown"`.
- **customer_nodes** is an interval/as-of table: a customer can have many rows, each with a `start_date`/`end_date` window and a `region_id`/`node_id` holding at that time.
- **customer_regions** maps `region_id` 1..5 to names (Australia, America, Africa, Asia, Europe) — note "America" not "USA".
- **interest_metrics** contains rows where `_month`, `_year`, `month_year`, and `interest_id` are all NULL (~1194 rows ≈ the `interest_map` null-summary rows); these rows still carry composition/index/ranking values.
- **interest_map.id** is the (sparse) key for **interest_metrics.interest_id**.
- **shopping_cart_event_identifier.event_type** maps codes to names: 1=Page View, 2=Add to Cart, 3=Purchase, 4=Ad Impression, 5=Ad Click (profile lists them in a scrambled order).
- **shopping_cart_page_hierarchy.product_id** is NULL for non-product pages (Home Page, All Products, Checkout, Confirmation); product pages correspond to product_id 1..9.
- **shopping_cart_campaign_identifier.products** is a textual range ("1-3", "4-5", "6-8") referencing `product_id` ranges in page_hierarchy, not page_id.
- **veg_* tables** cover fresh vegetables (RMB/kg prices, kg quantities); `veg_txn_df` has no PK/index and is large (~878K rows) with `sale/return` flag and `discount(%)`.
- **veg_cat** groups items by `category_code`/`category_name`; **veg_loss_rate_df** provides `loss_rate_%` per item; **veg_whsle_df** gives wholesale daily prices. `item_code` (a large 64-bit integer) is the shared item key.

## Potential Join Strategies

- **bitcoin_members ↔ bitcoin_transactions**: join on `member_id`. One member has many transactions (14 members across 22,918 txns), so member-side is the one side; filter on `member_id`/`region` in the member table to restrict txns.
- **btc_prices ↔ bitcoin_transactions**: join `bitcoin_prices.market_date` = `bitcoin_transactions.txn_date` AND `bitcoin_prices.ticker` = `bitcoin_transactions.ticker` (both use DD-MM-YYYY in text, so string equality works). Both span 2017–2021; prices are per-day per-ticker, txns per-day — group txns by `(ticker, txn_date)` first to avoid fan-out.
- **customer_nodes ↔ customer_regions**: join `customer_nodes.region_id` = `customer_regions.region_id`. Region is a per-customer time-dependent attribute — do not join on customer alone; a customer can have multiple active intervals.
- **customer_transactions ↔ customer_nodes / customer_regions**: join on `customer_id`; apply date-window predicates (`txn_date` BETWEEN `start_date` AND `end_date`) to assign each transaction to the region/node in effect at that time.
- **bitcoin_transactions.txn_id ↔ customer_transactions.txn_amount** (inferred link): weak/heterogeneous linkage — different id spaces (range 1..22918 vs amounts 0..1000); not a reliable foreign key. Prefer customer-scoped joins instead.
- **shopping_cart_events ↔ shopping_cart_users**: join on `cookie_id` to resolve users; users have multiple cookies per user_id (1782 cookies → 500 users).
- **shopping_cart_events ↔ shopping_cart_page_hierarchy**: join on `page_id` to get product/category; for purchase analysis, `event_type` 3 (Purchase) with page_id 13 (Confirmation) has no product — attribute product via the earlier Add-to-Cart/Page View events in the same `visit_id`.
- **shopping_cart events ↔ campaigns**: campaign `products` ranges ("1-3","4-5","6-8") map to `product_id` in page_hierarchy and `start_date`/`end_date`; join on product overlap + event_time within campaign window.
- **cleaned_weekly_sales ↔ weekly_sales**: deduplicate/never double-count; join on `week_date`+`region`+`platform`+`segment`+`customer_type` (or compare on `transactions`/`sales`). cleaned is a derived super-set of weekly_sales.
- **interest_map ↔ interest_metrics**: join `interest_map.id` = `interest_metrics.interest_id`; exclude rows where `interest_id` is NULL. Note `id` is sparse (up to 51678 across ~1208 rows).
- **cleaned_weekly_sales ↔ interest_metrics**: `calendar_year` ≈ `_year` (2018–2020 vs 2018–2019) with no month-name alignment (month_number vs _month/month_year); usable only for coarse time alignment, not an identity join.
- **veg_* tables**: join `veg_cat`/`veg_loss_rate_df`/`veg_whsle_df` on `item_code` (also `item_name`); `veg_txn_df` joins on `item_code` = same key. Use it for item semantics; filter out the ~4 null-product rows / loss-rate zero rows as needed.