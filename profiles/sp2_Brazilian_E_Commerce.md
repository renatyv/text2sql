---
generator: db-snooper
version: 0.0.33
generated_at_utc: 2026-08-21T12:31:57.738438Z
dialect: sqlite
database: /var/folders/9j/b9bx_drd53sc6zbpsqyrjy4h0000gn/T/dbsnoop-oa8npo7b/Brazilian_E_Commerce.sqlite
schema: main
---

# "olist_customers"  (rows=99441)

columns:
"customer_id" text: unique identifier
"customer_unique_id" text: 96096 distinct
"customer_zip_code_prefix" bigint: 14994 distinct, 1003..99990, avg=35137.5, median=24416
"customer_city" text: 4119 distinct
"customer_state" text: 27 distinct

indexes: none

samples:
| column | latest | sample | sample |
|---|---|---|---|
| customer_id | ffffe8b65bbe3087b653a978c870db99 | 6c94244091c0ea6ecf242283e1455871 | 226152ac481f0b29cd416d4028f64224 |
| customer_unique_id | 736e6bfa0510aa5b878881a226a5fd89 | 6e7932d65c10afc9c622770cdf6e9d1c | d38867091f1bf3531ce67c7f4b93b39b |
| customer_zip_code_prefix | 6172 | 99955 | 62680 |
| customer_city | osasco | vila langaro | paracuru |
| customer_state | SP | RS | CE |

# "olist_geolocation"  (rows=≈1000163)

columns:
"geolocation_zip_code_prefix" bigint
"geolocation_lat" float
"geolocation_lng" float
"geolocation_city" text
"geolocation_state" text

indexes: none


# "olist_order_items"  (rows=112650)

columns:
"order_id" text: profile metrics skipped
"order_item_id" bigint: 1..21
"product_id" text: profile metrics skipped
"seller_id" text: profile metrics skipped
"shipping_limit_date" text: iso-date
"price" float: 0.85..6735, avg=120.654
"freight_value" float: 0..409.68, avg=19.9903

indexes: none

samples:
| column | latest | sample | sample |
|---|---|---|---|
| order_id | fffe41c64501cc87c801fd61db3f6244 | 4082a09e70f0dcced54c17ec25ac2a50 | 741c75a2bee4e666de0415b10cd0cad7 |
| order_item_id | 1 | 1 | 1 |
| product_id | 350688d9dc1e75ff97be326363655e01 | e59dd207c69d86e890febadc796d1078 | 98c2f7da94217786e372e7d85462c354 |
| seller_id | f7ccf836d21b2fb1de37564105216cc1 | 1c68394e931a64f90ea236c5ea590300 | 2199e7fe213c16213bf5d6a7eadc9a5d |
| shipping_limit_date | 2018-06-12 17:10:13 | 2018-02-19 15:56:06 | 2018-06-12 22:30:49 |
| price | 43 | 144.41 | 76 |
| freight_value | 12.79 | 17.45 | 14.62 |

# "olist_order_payments"  (rows=103886)

columns:
"order_id" text: profile metrics skipped
"payment_sequential" bigint: 1..29, avg=1.09268
"payment_type" text: profile metrics skipped
"payment_installments" bigint: 0..24, avg=2.85335
"payment_value" float: 0..13664.1, avg=154.1

indexes: none

samples:
| column | latest | sample | sample |
|---|---|---|---|
| order_id | fffe41c64501cc87c801fd61db3f6244 | b15acd827ae5109303845f18ff8d4662 | 08c94cca559ddccd243fc551e088b856 |
| payment_sequential | 1 | 1 | 1 |
| payment_type | credit_card | credit_card | credit_card |
| payment_installments | 1 | 1 | 4 |
| payment_value | 55.79 | 61 | 40.06 |

# "olist_order_reviews"  (rows=99224)

columns:
"review_id" text: 98410 distinct
"order_id" text: 98673 distinct
"review_score" bigint: 5=57328, 4=19142, 1=11424, 3=8179, 2=3151, 1..5
"review_comment_title" text: 4527 distinct, nulls=87656
"review_comment_message" text: 36159 distinct, nulls=58247
"review_creation_date" text: iso-date, 636 distinct
"review_answer_timestamp" text: iso-date, 98248 distinct

indexes: none

samples:
| column | latest | sample | sample |
|---|---|---|---|
| review_id | fffefe7a48d22f7b32046421062219d1 | 0da5fbb616b9667780903ae573227e95 | 2166f23eeb75757d6ba352963584a2c3 |
| order_id | 1061bc32577c6b8beb107bf1b5a65175 | 9db4c3ce35bd9bdf6b8eb62c68eb4415 | fe784ed3dfc728fd4de44fa9918fe1eb |
| review_score | 5 | 1 | 5 |
| review_comment_title | null | null | null |
| review_comment_message | null | null | null |
| review_creation_date | 2017-10-28 00:00:00 | 2018-06-27 00:00:00 | 2018-08-07 00:00:00 |
| review_answer_timestamp | 2017-10-30 21:43:56 | 2018-06-27 21:29:35 | 2018-08-10 15:35:52 |

# "olist_orders"  (rows=99441)

columns:
"order_id" text: unique identifier
"customer_id" text: unique identifier
"order_status" text: "delivered"=96478, "shipped"=1107, "canceled"=625, "unavailable"=609, "invoiced"=314, "processing"=301, "created"=5, "approved"=2
"order_purchase_timestamp" text: iso-date, 98875 distinct
"order_approved_at" text: iso-date, 90733 distinct, nulls=160
"order_delivered_carrier_date" text: iso-date, 81018 distinct, nulls=1783
"order_delivered_customer_date" text: iso-date, 95664 distinct, nulls=2965
"order_estimated_delivery_date" text: iso-date, 459 distinct

indexes: none

samples:
| column | latest | sample | sample |
|---|---|---|---|
| order_id | fffe41c64501cc87c801fd61db3f6244 | 59471e5f3a931a6b88ced311417896b4 | 89a7e32e1ea0948b881497e7ae8bbfa2 |
| customer_id | 96d649da0cc4ff33bb408b199d4c7dcf | 29930c7777c92ade51cb983da38b64b7 | 390d6b4ec75d23f0b453e3b7374db5df |
| order_status | delivered | delivered | delivered |
| order_purchase_timestamp | 2018-06-09 17:00:18 | 2018-02-19 22:54:38 | 2018-03-28 10:38:12 |
| order_approved_at | 2018-06-09 17:10:13 | 2018-02-20 00:06:48 | 2018-03-28 10:50:29 |
| order_delivered_carrier_date | 2018-06-11 14:11:00 | 2018-02-22 00:58:57 | 2018-03-29 20:06:54 |
| order_delivered_customer_date | 2018-06-14 17:56:26 | 2018-03-15 23:33:21 | 2018-04-12 15:30:54 |
| order_estimated_delivery_date | 2018-06-28 00:00:00 | 2018-03-19 00:00:00 | 2018-04-19 00:00:00 |

# "olist_products"  (rows=32951)

columns:
"product_id" text: unique identifier
"product_category_name" text: 73 distinct, nulls=610
"product_name_lenght" float: 66 distinct, nulls=610, 5..76, avg=48.4769, median=51
"product_description_lenght" float: 2960 distinct, nulls=610, 4..3992, avg=771.495, median=595
"product_photos_qty" float: 1=16489, 2=6263, 3=3860, 4=2428, 5=1484, 6=968, 7=343, 8=192, 9=105, 10=95, 11=46, 12=35, 13=9, 15=8, 17=7, 14=5, 18=2, 19=1, 20=1, nulls=610, 1..20
"product_weight_g" float: 2204 distinct, nulls=2, 0..40425, avg=2276.47, median=700
"product_length_cm" float: 99 distinct, nulls=2, 7..105, avg=30.8151, median=25
"product_height_cm" float: 102 distinct, nulls=2, 2..105, avg=16.9377, median=13
"product_width_cm" float: 95 distinct, nulls=2, 6..118, avg=23.1967, median=20

indexes: none

samples:
| column | latest | sample | sample |
|---|---|---|---|
| product_id | fffe9eeff12fcbd74a2f2b007dde0c58 | 4da918a160c19da9bfdf9945d18006ec | 5e14c2beea650eac6b94bc9d446cd71a |
| product_category_name | brinquedos | instrumentos_musicais | eletronicos |
| product_name_lenght | 57 | 56 | 46 |
| product_description_lenght | 1536 | 1262 | 272 |
| product_photos_qty | 3 | 2 | 1 |
| product_weight_g | 3900 | 5600 | 175 |
| product_length_cm | 43 | 30 | 22 |
| product_height_cm | 16 | 62 | 12 |
| product_width_cm | 11 | 45 | 16 |

# "olist_products_dataset"  (rows=32951)

columns:
"index" bigint: all distinct, 0..32950, avg=16475, median=16475
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
| index | 32950 | 4145 | 3691 |
| product_id | 106392145fca363410d287a815be6de4 | 8c0794180bc059d1af097905d7352cfa | 79e42c4fa2bde6e0c828d23c4fb7df35 |
| product_category_name | cama_mesa_banho | livros_tecnicos | instrumentos_musicais |
| product_name_lenght | 58 | 25 | 57 |
| product_description_lenght | 309 | 1002 | 962 |
| product_photos_qty | 1 | 1 | 4 |
| product_weight_g | 2083 | 2000 | 900 |
| product_length_cm | 12 | 30 | 42 |
| product_height_cm | 2 | 4 | 8 |
| product_width_cm | 7 | 23 | 40 |

# "olist_sellers"  (rows=3095)

columns:
"seller_id" text: unique identifier
"seller_zip_code_prefix" bigint: 2246 distinct, 1001..99730, avg=32291.1, median=14940
"seller_city" text: 611 distinct
"seller_state" text: 23 distinct

indexes: none

samples:
| column | latest | sample | sample |
|---|---|---|---|
| seller_id | ffff564a4f9085cd26170f4732393726 | 3d0cd21d41671c46f82cd11176bf7277 | 066a6914e1ebf3ea95a216c73a986b91 |
| seller_zip_code_prefix | 13070 | 89217 | 85863 |
| seller_city | campinas | joinville | foz do iguacu |
| seller_state | SP | SC | PR |

# "product_category_name_translation"  (rows=71)

columns:
"product_category_name" text: all distinct
"product_category_name_english" text: all distinct

indexes: none

samples:
| column | latest | sample | sample |
|---|---|---|---|
| product_category_name | utilidades_domesticas | bebes | eletrodomesticos |
| product_category_name_english | housewares | baby | home_appliances |
