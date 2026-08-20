---
generator: db-snooper
version: 0.0.31
generated_at_utc: 2026-08-20T17:29:02.235918Z
dialect: sqlite
database: /var/folders/9j/b9bx_drd53sc6zbpsqyrjy4h0000gn/T/dbsnoop-ewjjn5br/electronic_sales.sqlite
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
fk: none

samples:
| column | latest | sample | sample |
|---|---|---|---|
| index | 99440 | 96535 | 46170 |
| customer_id | 274fa6071e5e17fe303b9748641082c8 | eb33bee09a3f5351b344d6c73cd74c52 | c2e1d65c47178eac5bd515e6653959e8 |
| customer_unique_id | 84732c5050c01db9b23e19ba39899398 | 39e441e925537ef195f789be824ffc07 | d1dae3a5d39b1261850728549a01667a |
| customer_zip_code_prefix | 6703 | 4052 | 9370 |
| customer_city | cotia | sao paulo | maua |
| customer_state | SP | SP | SP |

# "geolocation"  (rows=≈1000163)

columns:
"index" int
"geolocation_zip_code_prefix" int
"geolocation_lat" float
"geolocation_lng" float
"geolocation_city" text
"geolocation_state" text

indexes: "index"
fk: none


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
fk: none

samples:
| column | latest | sample | sample |
|---|---|---|---|
| index | 112649 | 84364 | 109056 |
| order_id | fffe41c64501cc87c801fd61db3f6244 | bfb074fa3d43b5b13e7a67203ebdedf5 | f7dca277a6bb273200598f0e36319d94 |
| order_item_id | 1 | 1 | 1 |
| product_id | 350688d9dc1e75ff97be326363655e01 | 50692766f5927d896a4b516389e92b4a | ad30079acfcea22be08f603414dbc0fe |
| seller_id | f7ccf836d21b2fb1de37564105216cc1 | f80edd2c5aaa505cc4b0a3b219abf4b8 | 2078fe5066350e7d220c0ad3a3bbc6c1 |
| shipping_limit_date | 2018-06-12 17:10:13 | 2017-05-18 10:25:08 | 2018-04-04 03:15:23 |
| price | 43 | 129.9 | 29.9 |
| freight_value | 12.79 | 43.32 | 38.14 |

# "order_payments"  (rows=103886)

columns:
"index" int: all distinct, 0..103885, avg=51942.5
"order_id" text: profile metrics skipped
"payment_sequential" int: 1..29, avg=1.09268
"payment_type" text: profile metrics skipped
"payment_installments" int: 0..24, avg=2.85335
"payment_value" float: 0..13664.1, avg=154.1

indexes: "index"
fk: none

samples:
| column | latest | sample | sample |
|---|---|---|---|
| index | 103885 | 34139 | 47042 |
| order_id | 28bbae6599b09d39ca406b747b6632b1 | 045b9114be21f880246ba6d749f577af | 520e9b73b66dd639c67ced184953ca2d |
| payment_sequential | 1 | 1 | 1 |
| payment_type | boleto | credit_card | boleto |
| payment_installments | 1 | 6 | 1 |
| payment_value | 191.58 | 61.29 | 358.89 |

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
fk: none

samples:
| column | latest | sample | sample |
|---|---|---|---|
| index | 99223 | 68454 | 13653 |
| review_id | efe49f1d6f951dd88b51e6ccd4cc548f | 1502d84801ecd79eabe6b83db96ec218 | 3e100e137e189c05d6ef08f3750ad229 |
| order_id | 90531360ecb1eec2a1fbb265a0db0508 | 4790bc3402a232e073d643e12035d859 | f88efcb15bb4da564e09c5ef905ae3cb |
| review_score | 1 | 5 | 5 |
| review_comment_title | null | null | null |
| review_comment_message | meu produto chegou e ja tenho que devolver, pois está com defeito , não segurar carga | null | null |
| review_creation_date | 2017-07-03 00:00:00 | 2017-04-04 00:00:00 | 2017-11-02 00:00:00 |
| review_answer_timestamp | 2017-07-03 21:01:49 | 2017-04-05 11:06:09 | 2017-11-04 18:14:23 |

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
fk: none

samples:
| column | latest | sample | sample |
|---|---|---|---|
| index | 99440 | 16726 | 68010 |
| order_id | 66dea50a8b16d9b4dee7af250b4be1a5 | e7b01e38e214dfdeaa5c9c98f911a7e4 | e55a581d6b3fcf41394ef2afb9a4205e |
| customer_id | edb027a75a1449115f6b43211ae02a24 | 03959f8a4aa2ffd6c471d797b3e95055 | 4962e73408e74b80e37b78b3a7a5126c |
| order_status | delivered | delivered | delivered |
| order_purchase_timestamp | 2018-03-08 20:57:30 | 2018-02-07 07:24:08 | 2017-12-03 18:39:00 |
| order_approved_at | 2018-03-09 11:20:28 | 2018-02-07 07:35:29 | 2017-12-03 18:53:39 |
| order_delivered_carrier_date | 2018-03-09 22:11:59 | 2018-02-07 19:56:01 | 2017-12-04 18:13:41 |
| order_delivered_customer_date | 2018-03-16 13:08:30 | 2018-02-20 00:33:39 | 2017-12-19 00:28:24 |
| order_estimated_delivery_date | 2018-04-03 00:00:00 | 2018-03-13 00:00:00 | 2018-01-02 00:00:00 |

# "product_category_name_translation"  (rows=71)

columns:
"index" int: all distinct, 0..70, avg=35, median=35
"product_category_name" text: all distinct
"product_category_name_english" text: all distinct

indexes: "index"
fk: none

samples:
| column | latest | sample | sample |
|---|---|---|---|
| index | 70 | 52 | 35 |
| product_category_name | seguros_e_servicos | sinalizacao_e_seguranca | casa_conforto |
| product_category_name_english | security_and_services | signaling_and_security | home_confort |

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
fk: none

samples:
| column | latest | sample | sample |
|---|---|---|---|
| index | 32950 | 2541 | 10294 |
| product_id | 106392145fca363410d287a815be6de4 | 9d8a0e115e802d845b4ce1eb794d1260 | 3b53b6b3ce85cb52f521117e354480db |
| product_category_name | cama_mesa_banho | esporte_lazer | relogios_presentes |
| product_name_lenght | 58 | 30 | 42 |
| product_description_lenght | 309 | 2299 | 712 |
| product_photos_qty | 1 | 1 | 1 |
| product_weight_g | 2083 | 150 | 350 |
| product_length_cm | 12 | 20 | 16 |
| product_height_cm | 2 | 10 | 12 |
| product_width_cm | 7 | 15 | 11 |

# "sellers"  (rows=3095)

columns:
"index" int: all distinct, 0..3094, avg=1547, median=1547
"seller_id" text: unique identifier
"seller_zip_code_prefix" int: 2246 distinct, 1001..99730, avg=32291.1, median=14940
"seller_city" text: 611 distinct
"seller_state" text: 23 distinct

indexes: "index"
fk: none

samples:
| column | latest | sample | sample |
|---|---|---|---|
| index | 3094 | 1947 | 16 |
| seller_id | 9e25199f6ef7e7c347120ff175652c3b | 1f7fd2a6fcd5a6fa5d8a4dabc72aaae0 | 166e8f1381e09651983c38b1f6f91c11 |
| seller_zip_code_prefix | 12051 | 95800 | 88780 |
| seller_city | taubate | venancio aires | imbituba |
| seller_state | SP | RS | SC |
