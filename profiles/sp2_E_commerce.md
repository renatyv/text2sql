---
generator: db-snooper
version: 0.0.33
generated_at_utc: 2026-08-21T12:33:17.446501Z
dialect: sqlite
database: /var/folders/9j/b9bx_drd53sc6zbpsqyrjy4h0000gn/T/dbsnoop-wgq9dsl7/E_commerce.sqlite
schema: main
---

# "customers"  (rows=99441)

columns:
"customer_id" text: unique identifier
"customer_unique_id" text: 96096 distinct
"customer_zip_code_prefix" int: 14994 distinct, 1003..99990, avg=35137.5, median=24416
"customer_city" text: 4119 distinct
"customer_state" text: 27 distinct

indexes: none

samples:
| column | latest | sample | sample |
|---|---|---|---|
| customer_id | ffffe8b65bbe3087b653a978c870db99 | 066e5acdd1a429b05b4bcb0c8f8273d3 | b77ee5671feb9b6efce84cc804842024 |
| customer_unique_id | 736e6bfa0510aa5b878881a226a5fd89 | 36cb06fed5371d8e5ae0074141da1ae2 | 5c64fc047d4115cc4be24c9c0c9503c2 |
| customer_zip_code_prefix | 6172 | 71215 | 73088 |
| customer_city | osasco | brasilia | brasilia |
| customer_state | SP | DF | DF |

# "geolocation"  (rows=≈1000163)

columns:
"geolocation_zip_code_prefix" int
"geolocation_lat" float
"geolocation_lng" float
"geolocation_city" text
"geolocation_state" text

indexes: none


# "leads_closed"  (rows=842)

columns:
"mql_id" text: unique identifier
"seller_id" text: unique identifier
"sdr_id" text: 32 distinct
"sr_id" text: 22 distinct
"won_date" text: iso-date, 824 distinct
"business_segment" text: 33 distinct, nulls=1
"lead_type" text: "online_medium"=332, "online_big"=126, "industry"=123, "offline"=104, "online_small"=77, "online_beginner"=57, "online_top"=14, "other"=3, nulls=6
"lead_behaviour_profile" text: "cat"=407, "eagle"=123, "wolf"=95, "shark"=24, "cat, wolf"=8, "eagle, cat"=3, "eagle, wolf"=3, "shark, cat"=1, "shark, wolf"=1, nulls=177
"has_company" int: 1=58, 0=5, nulls=779
"has_gtin" int: 1=54, 0=10, nulls=778
"average_stock" text: "5-20"=22, "50-200"=15, "1-5"=10, "20-50"=8, "200+"=7, "unknown"=4, nulls=776
"business_type" text: "reseller"=587, "manufacturer"=242, "other"=3, nulls=10
"declared_product_catalog_size" float: 33 distinct, nulls=773, 1..2000, avg=233.029, median=100
"declared_monthly_revenue" float: 27 distinct, 0..5e+07, avg=73377.7, median=0

indexes: none

samples:
| column | latest | sample | sample |
|---|---|---|---|
| mql_id | fff8db9478d2fd72df65a67ee6b62f67 | 5985e72b3752e4749926885db1b45be4 | ba7fb7aa93b1203a1f5e19b0857870e3 |
| seller_id | bdae679a9b282249bc23b9b69dae9a99 | 044668ccd5316b12a7cf0d54a156e3e9 | bec568278124768c474ee90971ca94d1 |
| sdr_id | 4b339f9567d060bcea4f5136b9f5949e | 56bf83c4bb35763a51c2baab501b4c67 | 4b339f9567d060bcea4f5136b9f5949e |
| sr_id | 6565aa9ce3178a5caf6171827af3a9ba | 4ef15afb4b2723d8f3d81e51ec7afefe | 2695de1affa7750089c0455f8ce27021 |
| won_date | 2018-01-24 15:19:49 | 2018-01-31 21:00:13 | 2018-06-05 13:34:52 |
| business_segment | construction_tools_house_garden | food_drink | home_decor |
| lead_type | online_medium | offline | online_beginner |
| lead_behaviour_profile | null | null | cat |
| has_company | null | null | null |
| has_gtin | null | null | null |
| average_stock | null | null | null |
| business_type | reseller | reseller | reseller |
| declared_product_catalog_size | null | null | null |
| declared_monthly_revenue | 0 | 0 | 0 |

# "leads_qualified"  (rows=8000)

columns:
"mql_id" text: unique identifier
"first_contact_date" text: iso-date, 336 distinct
"landing_page_id" text: 495 distinct
"origin" text: "organic_search"=2296, "paid_search"=1586, "social"=1350, "unknown"=1099, "direct_traffic"=499, "email"=493, "referral"=284, "other"=150, "display"=118, "other_publicities"=65, nulls=60

indexes: none

samples:
| column | latest | sample | sample |
|---|---|---|---|
| mql_id | fffffe98d0963d27015c198262d97221 | debcfcbcdbc48a17e199bca9d040a4d2 | 3e864b47b8a2d0bbc43aca4c5da5ddbe |
| first_contact_date | 2018-01-25 | 2018-05-12 | 2018-03-20 |
| landing_page_id | 88740e65d5d6b056e0cda098e1ea6313 | 40dec9f3d5259a3d2dbcdab2114fae47 | b76ef37428e6799c421989521c0e5077 |
| origin | social | paid_search | unknown |

# "order_items"  (rows=112650)

columns:
"order_id" text: profile metrics skipped
"order_item_id" int: 1..21
"product_id" text: profile metrics skipped
"seller_id" text: profile metrics skipped
"shipping_limit_date" text: iso-date
"price" float: 0.85..6735, avg=120.654
"freight_value" float: 0..409.68, avg=19.9903

indexes: none

samples:
| column | latest | sample | sample |
|---|---|---|---|
| order_id | fffe41c64501cc87c801fd61db3f6244 | 73ab3121732a6b5bd3e8ad44c1d81c57 | ef2ecde1a76f9bcc15c632e7970aca8d |
| order_item_id | 1 | 1 | 1 |
| product_id | 350688d9dc1e75ff97be326363655e01 | fd1abebad3478dd37080b399656dbb7d | d48bacc1dcd9c86bf1ed4ed2a303336c |
| seller_id | f7ccf836d21b2fb1de37564105216cc1 | e4f121bf6ef8b9a1d4d3e65dd0473fab | 406822777a0b9eb5c50e442dd4cd3ec5 |
| shipping_limit_date | 2018-06-12 17:10:13 | 2018-04-05 21:30:21 | 2018-07-11 18:45:13 |
| price | 43 | 30 | 49 |
| freight_value | 12.79 | 18.23 | 14.65 |

# "order_payments"  (rows=103886)

columns:
"order_id" text: profile metrics skipped
"payment_sequential" int: 1..29, avg=1.09268
"payment_type" text: profile metrics skipped
"payment_installments" int: 0..24, avg=2.85335
"payment_value" float: 0..13664.1, avg=154.1

indexes: none

samples:
| column | latest | sample | sample |
|---|---|---|---|
| order_id | fffe41c64501cc87c801fd61db3f6244 | f3144b968537c3068bdd820f07160523 | 1f440e230578d73badf5afd8bb78c632 |
| payment_sequential | 1 | 1 | 1 |
| payment_type | credit_card | credit_card | credit_card |
| payment_installments | 1 | 1 | 8 |
| payment_value | 55.79 | 74.16 | 327.58 |

# "order_reviews"  (rows=99224)

columns:
"review_id" text: 98410 distinct
"order_id" text: 98673 distinct
"review_score" int: 5=57328, 4=19142, 1=11424, 3=8179, 2=3151, 1..5
"review_comment_title" text: 4527 distinct, nulls=87656
"review_comment_message" text: 36159 distinct, nulls=58247
"review_creation_date" text: iso-date, 636 distinct
"review_answer_timestamp" text: iso-date, 98248 distinct

indexes: none

samples:
| column | latest | sample | sample |
|---|---|---|---|
| review_id | fffefe7a48d22f7b32046421062219d1 | 503f504e7d0ab093fdb903838c4b5e98 | 75538694db1f1734454b7c3a86da3d22 |
| order_id | 1061bc32577c6b8beb107bf1b5a65175 | f6ed6898419c893a57cd88e7dbbdb2c7 | 4892ff734d87bb926bd317ebafca95d1 |
| review_score | 5 | 1 | 5 |
| review_comment_title | null | null | null |
| review_comment_message | null | Não recebi o produto favor me informe quando chegará  | Produto ótimo e entregue beem antes do prazo . |
| review_creation_date | 2017-10-28 00:00:00 | 2018-03-22 00:00:00 | 2017-06-07 00:00:00 |
| review_answer_timestamp | 2017-10-30 21:43:56 | 2018-04-04 13:23:59 | 2017-06-08 17:02:10 |

# "orders"  (rows=99441)

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
| order_id | fffe41c64501cc87c801fd61db3f6244 | f24bbebc2c8ba687b65f1be751dd8982 | dca954560c94725cbb8402714b1dc7bd |
| customer_id | 96d649da0cc4ff33bb408b199d4c7dcf | 541884ec125bd7f617b86a0f92b8e3b7 | af189c7154bf7cd83ae87e7c7c43a6b9 |
| order_status | delivered | delivered | delivered |
| order_purchase_timestamp | 2018-06-09 17:00:18 | 2018-02-20 18:27:39 | 2018-01-09 21:59:13 |
| order_approved_at | 2018-06-09 17:10:13 | 2018-02-21 18:31:57 | 2018-01-10 10:32:14 |
| order_delivered_carrier_date | 2018-06-11 14:11:00 | 2018-02-24 00:51:34 | 2018-01-11 22:56:00 |
| order_delivered_customer_date | 2018-06-14 17:56:26 | 2018-04-19 16:49:31 | 2018-01-22 18:58:25 |
| order_estimated_delivery_date | 2018-06-28 00:00:00 | 2018-03-14 00:00:00 | 2018-01-26 00:00:00 |

# "product_category_name_translation"  (rows=71)

columns:
"product_category_name" text: all distinct
"product_category_name_english" text: all distinct

indexes: none

samples:
| column | latest | sample | sample |
|---|---|---|---|
| product_category_name | utilidades_domesticas | cds_dvds_musicais | utilidades_domesticas |
| product_category_name_english | housewares | cds_dvds_musicals | housewares |

# "products"  (rows=32951)

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
| product_id | fffe9eeff12fcbd74a2f2b007dde0c58 | 43a24e051b37c8e88accdfdeecddb71b | eb551aa4ed7eb5e2839d5b7d2896bece |
| product_category_name | brinquedos | informatica_acessorios | telefonia |
| product_name_lenght | 57 | 33 | 51 |
| product_description_lenght | 1536 | 253 | 350 |
| product_photos_qty | 3 | 1 | 1 |
| product_weight_g | 3900 | 1000 | 100 |
| product_length_cm | 43 | 37 | 19 |
| product_height_cm | 16 | 19 | 3 |
| product_width_cm | 11 | 19 | 11 |

# "sellers"  (rows=3095)

columns:
"seller_id" text: unique identifier
"seller_zip_code_prefix" int: 2246 distinct, 1001..99730, avg=32291.1, median=14940
"seller_city" text: 611 distinct
"seller_state" text: 23 distinct

indexes: none

samples:
| column | latest | sample | sample |
|---|---|---|---|
| seller_id | ffff564a4f9085cd26170f4732393726 | 99cd94252748d2bdde08e17858233602 | 749e7cdabbaf72f16677859e27874ba5 |
| seller_zip_code_prefix | 13070 | 12401 | 7122 |
| seller_city | campinas | sao paulo | guarulhos |
| seller_state | SP | SP | SP |
