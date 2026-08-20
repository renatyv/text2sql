# Additional Metadata

## Clarified Semantics

- No declared foreign keys exist; `orders` is the central hub. `orders.delivery_order_id` and `orders.payment_order_id` act as logical FKs to `deliveries`/`payments` despite the naming mismatch.
- `orders.delivery_order_id` and `orders.payment_order_id` are each unique (1 value per order, same cardinality as `order_id`), so they can be used as order-level keys for joining.
- Status vocabularies differ and are not shared across tables:
  - `orders.order_status`: FINISHED / CANCELED.
  - `deliveries.delivery_status`: DELIVERED / CANCELLED / DELIVERING (only a few in-progress).
  - `payments.payment_status`: PAID / CHARGEBACK / AWAITING (rare).
  - Do not conflate FINISHED (orders) with DELIVERED (deliveries) — they are separate lifecycles.
- Some orders have no delivery row: ~10,345 orders have a `delivery_order_id` absent from `deliveries`. Similarly ~18,665 orders have a `payment_order_id` absent from `payments`. Use outer joins when completeness matters.
- `deliveries` may hold multiple rows per `delivery_order_id` (distinct values 358,654 vs 378,843 rows) → retries/attempts.
- `payments` likewise holds multiple rows per `payment_order_id` (350,334 distinct vs 400,834 rows) → multiple payment statuses per order.
- `orders` denormalizes time into both `order_moment_*` datetimes and `order_created_hour/minute/day/month/year` plus `order_metric_*` durations; metric columns are cumulative time measures (transit, walking, production, etc.).
- `store_segment` values are GOOD / FOOD; `store_plan_price` is effectively an enum (29, 29.9, 49, 49.9, 0, etc.) and is nullable.
- `hubs.hub_city` and `hubs.hub_state` are consistent (e.g., SÃO PAULO/SP); `hub_name` and `store_name` are cosmetic, not keys.

## Potential Join Strategies

- `orders.delivery_order_id = deliveries.delivery_order_id` — join orders to delivery facts. Caveat: fan-out because `deliveries` can have several rows per order id; filter `delivery_status` (e.g., DELIVERED) to pick the meaningful row. Also ~10k orders produce no match.
- `orders.store_id = stores.store_id`, then `stores.hub_id = hubs.hub_id` — chain orders→store→hub to group orders by hub/city/state. `stores.hub_id` has 32 distinct values; `stores.store_id` is 1:1 into `stores`.
- `orders.channel_id = channels.channel_id` — attach channel type (MARKETPLACE vs OWN CHANNEL) as an order dimension; `orders` only references 39 of the 40 channels.
- `orders.payment_order_id = payments.payment_order_id` — join order to payment record. Caveat: fan-out (multiple payment rows per order); filter or aggregate by `payment_status` to avoid double counting amounts.
- `deliveries.driver_id = drivers.driver_id` — attach driver modal/type (MOTOBOY/BIKER, FREELANCE/LOGISTIC OPERATOR) to delivery-level records, joined after the order→delivery link.
- For cost/fee analysis, join `orders` to `deliveries` and reference `order_delivery_fee` vs `order_delivery_cost` on the same order row alongside delivery distance (`delivery_distance_meters`).