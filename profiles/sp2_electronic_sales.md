---
generator: db-snooper
version: 0.0.33
generated_at_utc: 2026-08-21T12:34:14.844141Z
dialect: sqlite
database: /var/folders/9j/b9bx_drd53sc6zbpsqyrjy4h0000gn/T/dbsnoop-_cmh6jjy/electronic_sales.sqlite
schema: main
---

# "customers"  (rows=99441)

columns:
"index" int: all distinct, 0..99440, avg=49720, median=49720
"customer_id" text: unique identifier
"customer_unique_id" text: 96096 distinct
"customer_zip_code_prefix" int: 14994 distinct, 1003..99990, avg=35137.5, median=24416
"customer_city" text: 4119 distinct
"customer_state" text: 27 distinct

indexes: "index"

samples:
| column | latest | sample | sample |
|---|---|---|---|
| index | 99440 | 91198 | 3586 |
| customer_id | 274fa6071e5e17fe303b9748641082c8 | 1de54ffbfb658eec45cfc9bd9bfb2917 | 143fdaaf1a8b9e8905183ee2714d3647 |
| customer_unique_id | 84732c5050c01db9b23e19ba39899398 | e5500e25b05cdc41ad05df9cb17ac25d | 66cf8110aa095f9456d89b7ca697d3a5 |
| customer_zip_code_prefix | 6703 | 79604 | 82410 |
| customer_city | cotia | tres lagoas | curitiba |
| customer_state | SP | MS | PR |

# "geolocation"  (rows=≈1000163)

columns:
"index" int
"geolocation_zip_code_prefix" int
"geolocation_lat" float
"geolocation_lng" float
"geolocation_city" text
"geolocation_state" text

indexes: "index"


# "order_items"  (rows=112650)

columns:
"index" int: all distinct, 0..112649, avg=56324.5
"order_id" text: profile metrics skipped
"order_item_id" int: 1..21
"product_id" text: profile metrics skipped
"seller_id" text: profile metrics skipped
"shipping_limit_date" text: iso-date
"price" float: 0.85..6735, avg=120.654
"freight_value" float: 0..409.68, avg=19.9903

indexes: "index"

samples:
| column | latest | sample | sample |
|---|---|---|---|
| index | 112649 | 14901 | 20488 |
| order_id | fffe41c64501cc87c801fd61db3f6244 | 21f09bf30ca7f813ec079b4774e485ea | 2ef78d4b9e33e5bb08a6ccff0771df05 |
| order_item_id | 1 | 1 | 1 |
| product_id | 350688d9dc1e75ff97be326363655e01 | f62cbf4416c9ef8e1b4e8d5279891f24 | 5237739bb5fee495dbd337755a138660 |
| seller_id | f7ccf836d21b2fb1de37564105216cc1 | 8b321bb669392f5163d04c59e235e066 | 966cb4760537b1404caedd472cc610a5 |
| shipping_limit_date | 2018-06-12 17:10:13 | 2018-01-15 07:24:04 | 2018-06-11 12:55:33 |
| price | 43 | 13.65 | 809 |
| freight_value | 12.79 | 7.78 | 22.37 |

# "order_payments"  (rows=103886)

columns:
"index" int: all distinct, 0..103885, avg=51942.5
"order_id" text: profile metrics skipped
"payment_sequential" int: 1..29, avg=1.09268
"payment_type" text: profile metrics skipped
"payment_installments" int: 0..24, avg=2.85335
"payment_value" float: 0..13664.1, avg=154.1

indexes: "index"

samples:
| column | latest | sample | sample |
|---|---|---|---|
| index | 103885 | 102477 | 9593 |
| order_id | 28bbae6599b09d39ca406b747b6632b1 | 4c6e24a5fceacbcf444cdb5141ec1688 | 897fab0704eda65c69520010b02a3fee |
| payment_sequential | 1 | 1 | 1 |
| payment_type | boleto | boleto | credit_card |
| payment_installments | 1 | 1 | 1 |
| payment_value | 191.58 | 75.5 | 52.05 |

# "order_reviews"  (rows=99224)

columns:
"index" int: all distinct, 0..99223, avg=49611.5, median=49611.5
"review_id" text: 98410 distinct
"order_id" text: 98673 distinct
"review_score" int: 5=57328, 4=19142, 1=11424, 3=8179, 2=3151, 1..5
"review_comment_title" text: 4527 distinct, nulls=87656
"review_comment_message" text: 36159 distinct, nulls=58247
"review_creation_date" text: iso-date, 636 distinct
"review_answer_timestamp" text: iso-date, 98248 distinct

indexes: "index"

samples:
| column | latest | sample | sample |
|---|---|---|---|
| index | 99223 | 18681 | 17615 |
| review_id | efe49f1d6f951dd88b51e6ccd4cc548f | 4e6978c0a53b3b1e5be5ecc79e39e544 | d6de7b5b09aec7945e550724ca520b37 |
| order_id | 90531360ecb1eec2a1fbb265a0db0508 | c770a2c821be1649e3bff529f0e97b7d | 3e555879d29880ec5bc189b44a6d77fa |
| review_score | 1 | 5 | 5 |
| review_comment_title | null | null | null |
| review_comment_message | meu produto chegou e ja tenho que devolver, pois está com defeito , não segurar carga | null | null |
| review_creation_date | 2017-07-03 00:00:00 | 2017-08-02 00:00:00 | 2017-03-14 00:00:00 |
| review_answer_timestamp | 2017-07-03 21:01:49 | 2017-08-03 00:09:47 | 2017-03-15 07:26:45 |

# "orders"  (rows=99441)

columns:
"index" int: all distinct, 0..99440, avg=49720, median=49720
"order_id" text: unique identifier
"customer_id" text: unique identifier
"order_status" text: "delivered"=96478, "shipped"=1107, "canceled"=625, "unavailable"=609, "invoiced"=314, "processing"=301, "created"=5, "approved"=2
"order_purchase_timestamp" text: iso-date, 98875 distinct
"order_approved_at" text: iso-date, 90733 distinct, nulls=160
"order_delivered_carrier_date" text: iso-date, 81018 distinct, nulls=1783
"order_delivered_customer_date" text: iso-date, 95664 distinct, nulls=2965
"order_estimated_delivery_date" text: iso-date, 459 distinct

indexes: "index"

samples:
| column | latest | sample | sample |
|---|---|---|---|
| index | 99440 | 77876 | 92837 |
| order_id | 66dea50a8b16d9b4dee7af250b4be1a5 | 30a8343ec44216954bf765295fc0c65f | 387d785f482aa3f1844fa843a72d97de |
| customer_id | edb027a75a1449115f6b43211ae02a24 | 87d61d8c11c89fe50ae234f4acec63c7 | 5f5b81ce642e4f5b3dc6685cf9478a39 |
| order_status | delivered | delivered | delivered |
| order_purchase_timestamp | 2018-03-08 20:57:30 | 2017-10-24 09:18:20 | 2017-06-08 20:28:21 |
| order_approved_at | 2018-03-09 11:20:28 | 2017-10-24 09:28:16 | 2017-06-10 03:03:46 |
| order_delivered_carrier_date | 2018-03-09 22:11:59 | 2017-10-26 16:59:01 | 2017-06-16 18:26:28 |
| order_delivered_customer_date | 2018-03-16 13:08:30 | 2017-11-03 19:53:50 | 2017-06-19 20:55:49 |
| order_estimated_delivery_date | 2018-04-03 00:00:00 | 2017-11-17 00:00:00 | 2017-06-30 00:00:00 |

# "product_category_name_translation"  (rows=71)

columns:
"index" int: all distinct, 0..70, avg=35, median=35
"product_category_name" text: all distinct
"product_category_name_english" text: all distinct

indexes: "index"

samples:
| column | latest | sample | sample |
|---|---|---|---|
| index | 70 | 4 | 27 |
| product_category_name | seguros_e_servicos | moveis_decoracao | construcao_ferramentas_jardim |
| product_category_name_english | security_and_services | furniture_decor | costruction_tools_garden |

# "products"  (rows=32951)

columns:
"index" int: all distinct, 0..32950, avg=16475, median=16475
"product_id" text: unique identifier
"product_category_name" text: 73 distinct, nulls=610
"product_name_lenght" float: 66 distinct, nulls=610, 5..76, avg=48.4769, median=51
"product_description_lenght" float: 2960 distinct, nulls=610, 4..3992, avg=771.495, median=595
"product_photos_qty" float: 1=16489, 2=6263, 3=3860, 4=2428, 5=1484, 6=968, 7=343, 8=192, 9=105, 10=95, 11=46, 12=35, 13=9, 15=8, 17=7, 14=5, 18=2, 19=1, 20=1, nulls=610, 1..20
"product_weight_g" float: 2204 distinct, nulls=2, 0..40425, avg=2276.47, median=700
"product_length_cm" float: 99 distinct, nulls=2, 7..105, avg=30.8151, median=25
"product_height_cm" float: 102 distinct, nulls=2, 2..105, avg=16.9377, median=13
"product_width_cm" float: 95 distinct, nulls=2, 6..118, avg=23.1967, median=20

indexes: "index"

samples:
| column | latest | sample | sample |
|---|---|---|---|
| index | 32950 | 10563 | 18370 |
| product_id | 106392145fca363410d287a815be6de4 | 6814dd9a0fcc3213534377d08d8a24fa | ba9801d3385d4a4f778fb1cbd1318ad5 |
| product_category_name | cama_mesa_banho | cama_mesa_banho | esporte_lazer |
| product_name_lenght | 58 | 47 | 28 |
| product_description_lenght | 309 | 372 | 227 |
| product_photos_qty | 1 | 1 | 1 |
| product_weight_g | 2083 | 1450 | 300 |
| product_length_cm | 12 | 34 | 32 |
| product_height_cm | 2 | 12 | 11 |
| product_width_cm | 7 | 40 | 17 |

# "sellers"  (rows=3095)

columns:
"index" int: all distinct, 0..3094, avg=1547, median=1547
"seller_id" text: unique identifier
"seller_zip_code_prefix" int: 2246 distinct, 1001..99730, avg=32291.1, median=14940
"seller_city" text: 611 distinct
"seller_state" text: 23 distinct

indexes: "index"

samples:
| column | latest | sample | sample |
|---|---|---|---|
| index | 3094 | 1859 | 336 |
| seller_id | 9e25199f6ef7e7c347120ff175652c3b | f08a5b9dd6767129688d001acafc21e5 | ec80e49e69745ab6c14f984bf2149423 |
| seller_zip_code_prefix | 12051 | 90230 | 13480 |
| seller_city | taubate | porto alegre | limeira |
| seller_state | SP | RS | SP |
