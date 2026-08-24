---
generator: db-snooper
version: 0.0.34
generated_at_utc: 2026-08-24T21:59:19.761851Z
dialect: sqlite
database: /var/folders/9j/b9bx_drd53sc6zbpsqyrjy4h0000gn/T/dbsnoop-1wvfrevn/delivery_center.sqlite
schema: main
---

# "channels"  (rows=40)

columns:
"channel_id" int PK: unique identifier, 1..49
"channel_name" varchar50: all distinct
"channel_type" varchar50: "MARKETPLACE"=26, "OWN CHANNEL"=14

indexes: none

samples:
| column | latest | sample | sample |
|---|---|---|---|
| channel_id | 49 | 20 | 41 |
| channel_name | RIBA PLACE | MUNICH PLACE | PANCEPS PLACE |
| channel_type | OWN CHANNEL | MARKETPLACE | MARKETPLACE |

# "deliveries"  (rows=≈378843)

columns:
"delivery_id" int PK
"delivery_order_id" int
"driver_id" int
"delivery_distance_meters" numeric
"delivery_status" varchar50

indexes: none


# "drivers"  (rows=4824)

columns:
"driver_id" int PK: unique identifier, 133..66494
"driver_modal" varchar50: "MOTOBOY"=3222, "BIKER"=1602
"driver_type" varchar50: "FREELANCE"=3939, "LOGISTIC OPERATOR"=885

indexes: none

samples:
| column | latest | sample | sample |
|---|---|---|---|
| driver_id | 66494 | 50630 | 55187 |
| driver_modal | MOTOBOY | MOTOBOY | MOTOBOY |
| driver_type | FREELANCE | FREELANCE | LOGISTIC OPERATOR |

# "hubs"  (rows=32)

columns:
"hub_id" int PK: unique identifier, 2..91
"hub_name" varchar50: all distinct
"hub_city" varchar50: "SÃO PAULO"=15, "RIO DE JANEIRO"=9, "CURITIBA"=4, "PORTO ALEGRE"=4
"hub_state" char2: "SP"=15, "RJ"=9, "PR"=4, "RS"=4
"hub_latitude" numeric: all distinct, -30.085743..-22.88582, avg=-24.4207, median=-23.5557
"hub_longitude" numeric: all distinct, -51.245997..-43.182181, avg=-46.5115, median=-46.6303

indexes: none

samples:
| column | latest | sample | sample |
|---|---|---|---|
| hub_id | 91 | 37 | 86 |
| hub_name | GAROA SHOPPING | RIVER SHOPPING | R SHOPPING |
| hub_city | SÃO PAULO | SÃO PAULO | SÃO PAULO |
| hub_state | SP | SP | SP |
| hub_latitude | -23.5251 | -23.5071 | -23.5415 |
| hub_longitude | -46.5468 | -46.7182 | -46.5766 |

# "orders"  (rows=≈368999)

columns:
"order_id" int PK
"store_id" int
"channel_id" int
"payment_order_id" int
"delivery_order_id" int
"order_status" varchar50
"order_amount" numeric
"order_delivery_fee" numeric
"order_delivery_cost" numeric
"order_created_hour" int
"order_created_minute" int
"order_created_day" int
"order_created_month" int
"order_created_year" int
"order_moment_created" datetime
"order_moment_accepted" datetime
"order_moment_ready" datetime
"order_moment_collected" datetime
"order_moment_in_expedition" datetime
"order_moment_delivering" datetime
"order_moment_delivered" datetime
"order_moment_finished" datetime
"order_metric_collected_time" numeric
"order_metric_paused_time" numeric
"order_metric_production_time" numeric
"order_metric_walking_time" numeric
"order_metric_expediton_speed_time" numeric
"order_metric_transit_time" numeric
"order_metric_cycle_time" numeric

indexes: none


# "payments"  (rows=≈400834)

columns:
"payment_id" int PK
"payment_order_id" int
"payment_amount" numeric
"payment_fee" numeric
"payment_method" varchar50
"payment_status" varchar50

indexes: none


# "stores"  (rows=951)

columns:
"store_id" int PK: unique identifier, 3..4679
"hub_id" int: 32 distinct, 2..91
"store_name" varchar50: 480 distinct
"store_segment" varchar50: "GOOD"=567, "FOOD"=384
"store_plan_price" numeric: 29=252, 29.9=177, 49=173, 49.9=159, 0=62, 1=7, 0.01=3, 19.9=1, 29.29=1, 39=1, nulls=115, 0..49.9
"store_latitude" numeric: 92 distinct, nulls=16, -30.085743..-19.875356, avg=-23.8864, median=-23.5611
"store_longitude" numeric: 87 distinct, nulls=16, -51.245997..-43.176536, avg=-46.0429, median=-46.6185

indexes: none

samples:
| column | latest | sample | sample |
|---|---|---|---|
| store_id | 4679 | 2604 | 911 |
| hub_id | 85 | 21 | 28 |
| store_name | PIGUE PIPACO  | GIPUMZIGUM  | RCOUMILES  |
| store_segment | FOOD | GOOD | FOOD |
| store_plan_price | 49.9 | null | 0 |
| store_latitude | -23.5134 | -23.5504 | -23.5958 |
| store_longitude | -46.6185 | -46.7213 | -46.686 |
