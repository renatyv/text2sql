---
generator: db-snooper
version: 0.0.34
generated_at_utc: 2026-08-24T21:59:20.292647Z
dialect: sqlite
database: /var/folders/9j/b9bx_drd53sc6zbpsqyrjy4h0000gn/T/dbsnoop-2fxcu_zd/electronic_sales.sqlite
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
| index | 99440 | 29727 | 32977 |
| customer_id | 274fa6071e5e17fe303b9748641082c8 | a55e8e19f8787d1c56a55001da76ccd0 | ea26c56ff6442484745579ed30526f01 |
| customer_unique_id | 84732c5050c01db9b23e19ba39899398 | 859b1c60b32236f6e71137547894935d | 8dfbc9064378d19ac99a21ac353072d7 |
| customer_zip_code_prefix | 6703 | 85660 | 24240 |
| customer_city | cotia | dois vizinhos | niteroi |
| customer_state | SP | PR | RJ |

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
| index | 112649 | 80452 | 63993 |
| order_id | fffe41c64501cc87c801fd61db3f6244 | b7085490200f5a1f838eb937d05b4b4a | 922acd93e452539fe6833fd485296ffe |
| order_item_id | 1 | 2 | 1 |
| product_id | 350688d9dc1e75ff97be326363655e01 | 0152f69b6cf919bcdaf117aa8c43e5a2 | 389d119b48cf3043d311335e499d9c6b |
| seller_id | f7ccf836d21b2fb1de37564105216cc1 | d2374cbcbb3ca4ab1086534108cc3ab7 | 1f50f920176fa81dab994f9023523100 |
| shipping_limit_date | 2018-06-12 17:10:13 | 2017-04-26 09:15:16 | 2018-02-14 07:50:29 |
| price | 43 | 13.9 | 49.9 |
| freight_value | 12.79 | 13.54 | 17.6 |

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
| index | 103885 | 16187 | 28532 |
| order_id | 28bbae6599b09d39ca406b747b6632b1 | f70a0aff17df5a6cdd9a7196128bd354 | 7f7b3e8f848e23fbcd3d2e096d12ef94 |
| payment_sequential | 1 | 1 | 1 |
| payment_type | boleto | boleto | credit_card |
| payment_installments | 1 | 1 | 7 |
| payment_value | 191.58 | 313.19 | 73.49 |

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
| index | 99223 | 57267 | 13775 |
| review_id | efe49f1d6f951dd88b51e6ccd4cc548f | 12b537151a5e71612763d55a3d9e326a | df55ce5fdc0c4d061eb3952ebda8b3ff |
| order_id | 90531360ecb1eec2a1fbb265a0db0508 | eb6c151662d92e0f9c6b1c3f30122348 | 5ff78652a040431e007c9349249d3503 |
| review_score | 1 | 5 | 5 |
| review_comment_title | null | null | null |
| review_comment_message | meu produto chegou e ja tenho que devolver, pois está com defeito , não segurar carga | null | null |
| review_creation_date | 2017-07-03 00:00:00 | 2018-01-09 00:00:00 | 2018-05-01 00:00:00 |
| review_answer_timestamp | 2017-07-03 21:01:49 | 2018-01-09 19:05:44 | 2018-05-03 23:16:35 |

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
| index | 99440 | 18962 | 30949 |
| order_id | 66dea50a8b16d9b4dee7af250b4be1a5 | 8abd0f2c3a61336c2ee97b2785175332 | 741f2c4e19ea249883b7eab05a4061f6 |
| customer_id | edb027a75a1449115f6b43211ae02a24 | b26210baf58f3919747468874d88c53f | ac8e2c478cb1b8bd0ebf1915f0d789e4 |
| order_status | delivered | canceled | delivered |
| order_purchase_timestamp | 2018-03-08 20:57:30 | 2018-04-19 13:18:07 | 2017-04-26 20:47:50 |
| order_approved_at | 2018-03-09 11:20:28 | 2018-04-19 14:31:24 | 2017-04-26 21:02:32 |
| order_delivered_carrier_date | 2018-03-09 22:11:59 | null | 2017-05-03 14:48:17 |
| order_delivered_customer_date | 2018-03-16 13:08:30 | null | 2017-05-10 09:49:55 |
| order_estimated_delivery_date | 2018-04-03 00:00:00 | 2018-05-08 00:00:00 | 2017-05-31 00:00:00 |

# "product_category_name_translation"  (rows=71)

columns:
"index" int: all distinct, 0..70, avg=35, median=35
"product_category_name" text: all distinct
"product_category_name_english" text: all distinct

indexes: "index"

samples:
| column | latest | sample | sample |
|---|---|---|---|
| index | 70 | 32 | 34 |
| product_category_name | seguros_e_servicos | eletronicos | artigos_de_festas |
| product_category_name_english | security_and_services | electronics | party_supplies |

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
| index | 32950 | 28683 | 30783 |
| product_id | 106392145fca363410d287a815be6de4 | cf262d646b27e22488de0494b5d08da0 | 1ba74b19c790ee59fb57fa2befa6e885 |
| product_category_name | cama_mesa_banho | utilidades_domesticas | fashion_bolsas_e_acessorios |
| product_name_lenght | 58 | 63 | 53 |
| product_description_lenght | 309 | 807 | 297 |
| product_photos_qty | 1 | 13 | 1 |
| product_weight_g | 2083 | 1900 | 150 |
| product_length_cm | 12 | 27 | 21 |
| product_height_cm | 2 | 23 | 9 |
| product_width_cm | 7 | 35 | 14 |

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
| index | 3094 | 619 | 748 |
| seller_id | 9e25199f6ef7e7c347120ff175652c3b | 054694fa03fe82cec4b7551487331d74 | 3faf68a3b0af94b10bac70d86077be49 |
| seller_zip_code_prefix | 12051 | 15840 | 13825 |
| seller_city | taubate | itajobi | holambra |
| seller_state | SP | SP | SP |
