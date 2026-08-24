---
generator: db-snooper
version: 0.0.34
generated_at_utc: 2026-08-24T21:23:50.886748Z
dialect: sqlite
database: /var/folders/9j/b9bx_drd53sc6zbpsqyrjy4h0000gn/T/dbsnoop-8l8euo9e/electronic_sales.sqlite
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
| index | 99440 | 68484 | 40582 |
| customer_id | 274fa6071e5e17fe303b9748641082c8 | 4f1f2b13805c2ab2ce70a6cad8001b18 | 9ccdd15c9060a6ea0d5f0abbb7324022 |
| customer_unique_id | 84732c5050c01db9b23e19ba39899398 | 34fbd9c42eb9702b4b8c6624b228ef11 | d6203ca017ec577b71f0f49429a38203 |
| customer_zip_code_prefix | 6703 | 4218 | 8900 |
| customer_city | cotia | sao paulo | guararema |
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
| index | 112649 | 57126 | 93610 |
| order_id | fffe41c64501cc87c801fd61db3f6244 | 8203c6a0f836ad28ea9043e6db95cb71 | d42c0ebb65d63fd42b509a1573c281aa |
| order_item_id | 1 | 1 | 1 |
| product_id | 350688d9dc1e75ff97be326363655e01 | 3790861742b5e1e8c72bc179fbeba4be | d0b9d3d449a97f582b325f11b512bfd2 |
| seller_id | f7ccf836d21b2fb1de37564105216cc1 | 066a6914e1ebf3ea95a216c73a986b91 | da6a60cc8cc724fe51be021ff8be779c |
| shipping_limit_date | 2018-06-12 17:10:13 | 2018-07-26 17:25:15 | 2018-07-18 22:45:15 |
| price | 43 | 24.9 | 115.89 |
| freight_value | 12.79 | 18.27 | 23.61 |

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
| index | 103885 | 18131 | 78888 |
| order_id | 28bbae6599b09d39ca406b747b6632b1 | 52fb2336bbf199586136afbe9822086c | 0ee3384432be1cfa2a044251ca3ea3a4 |
| payment_sequential | 1 | 1 | 1 |
| payment_type | boleto | credit_card | credit_card |
| payment_installments | 1 | 10 | 3 |
| payment_value | 191.58 | 157.21 | 58.74 |

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
| index | 99223 | 32196 | 35980 |
| review_id | efe49f1d6f951dd88b51e6ccd4cc548f | a339be8981f438caccabc132af417f93 | 5c0b7e34ed85ec659bb064902d878e7a |
| order_id | 90531360ecb1eec2a1fbb265a0db0508 | 12321543ad6f89cc74cde9ae42d12e3e | 0005f50442cb953dcd1d21e1fb923495 |
| review_score | 1 | 5 | 4 |
| review_comment_title | null | null | null |
| review_comment_message | meu produto chegou e ja tenho que devolver, pois está com defeito , não segurar carga | null | null |
| review_creation_date | 2017-07-03 00:00:00 | 2017-09-20 00:00:00 | 2018-07-05 00:00:00 |
| review_answer_timestamp | 2017-07-03 21:01:49 | 2017-09-20 21:45:33 | 2018-07-05 23:17:04 |

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
| index | 99440 | 7261 | 77191 |
| order_id | 66dea50a8b16d9b4dee7af250b4be1a5 | 606f74161b904d7a1bd3ac18746368a6 | 75af1e1795850c2407c73221960b3d1f |
| customer_id | edb027a75a1449115f6b43211ae02a24 | e190b8172936245229e18611c7f908bf | 8c13b0382b29fe9c46551ddc325a857a |
| order_status | delivered | delivered | delivered |
| order_purchase_timestamp | 2018-03-08 20:57:30 | 2017-08-16 23:23:48 | 2018-06-20 22:58:49 |
| order_approved_at | 2018-03-09 11:20:28 | 2017-08-17 01:05:34 | 2018-06-22 02:59:06 |
| order_delivered_carrier_date | 2018-03-09 22:11:59 | 2017-08-17 21:11:22 | 2018-06-22 12:59:00 |
| order_delivered_customer_date | 2018-03-16 13:08:30 | 2017-08-25 22:09:48 | 2018-06-28 19:56:38 |
| order_estimated_delivery_date | 2018-04-03 00:00:00 | 2017-09-08 00:00:00 | 2018-07-12 00:00:00 |

# "product_category_name_translation"  (rows=71)

columns:
"index" int: all distinct, 0..70, avg=35, median=35
"product_category_name" text: all distinct
"product_category_name_english" text: all distinct

indexes: "index"

samples:
| column | latest | sample | sample |
|---|---|---|---|
| index | 70 | 42 | 39 |
| product_category_name | seguros_e_servicos | moveis_sala | livros_tecnicos |
| product_category_name_english | security_and_services | furniture_living_room | books_technical |

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
| index | 32950 | 9201 | 19850 |
| product_id | 106392145fca363410d287a815be6de4 | dce4459168283eed926d7af76ba39e02 | 58db79da5975332e9006ec0fca77226f |
| product_category_name | cama_mesa_banho | telefonia | automotivo |
| product_name_lenght | 58 | 50 | 58 |
| product_description_lenght | 309 | 165 | 974 |
| product_photos_qty | 1 | 3 | 6 |
| product_weight_g | 2083 | 150 | 800 |
| product_length_cm | 12 | 18 | 35 |
| product_height_cm | 2 | 6 | 20 |
| product_width_cm | 7 | 11 | 20 |

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
| index | 3094 | 1353 | 241 |
| seller_id | 9e25199f6ef7e7c347120ff175652c3b | ea3ebea5317b0efbc663ecc8ce5e9bc2 | 830379336fad8c6f3b15a4a3ddb5c66e |
| seller_zip_code_prefix | 12051 | 88036 | 2518 |
| seller_city | taubate | florianopolis | sao paulo |
| seller_state | SP | SC | SP |
