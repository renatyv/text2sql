---
generator: db-snooper
version: 0.0.31
generated_at_utc: 2026-08-20T17:28:05.682982Z
dialect: sqlite
database: /var/folders/9j/b9bx_drd53sc6zbpsqyrjy4h0000gn/T/dbsnoop-uoig43s4/E_commerce.sqlite
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
fk: none

samples:
| column | latest | sample | sample |
|---|---|---|---|
| customer_id | ffffe8b65bbe3087b653a978c870db99 | 51d9009f107df3256dcb608b5cb40a7c | 5582a1c42a6723f0fdbb6dccb54693ae |
| customer_unique_id | 736e6bfa0510aa5b878881a226a5fd89 | 0922f37485310929b1b94e8f0c984ca5 | 38b70b993e11d6fb460d550ec9891153 |
| customer_zip_code_prefix | 6172 | 86037 | 21230 |
| customer_city | osasco | londrina | rio de janeiro |
| customer_state | SP | PR | RJ |

# "geolocation"  (rows=≈1000163)

columns:
"geolocation_zip_code_prefix" int
"geolocation_lat" float
"geolocation_lng" float
"geolocation_city" text
"geolocation_state" text

indexes: none
fk: none


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
fk: none

samples:
| column | latest | sample | sample |
|---|---|---|---|
| mql_id | fff8db9478d2fd72df65a67ee6b62f67 | ac68bc93ecc07d7daec8ce924ca09b0c | 2852475bf1d02022e4eb5269c452259a |
| seller_id | bdae679a9b282249bc23b9b69dae9a99 | 6025c79c035c3d772133b8b8238463b2 | 1a47a5831effd926ad6bee7ab8beb86c |
| sdr_id | 4b339f9567d060bcea4f5136b9f5949e | b90f87164b5f8c2cfa5c8572834dbe3f | 370c9f455f93a9a96cbe9bea48e70033 |
| sr_id | 6565aa9ce3178a5caf6171827af3a9ba | 56bf83c4bb35763a51c2baab501b4c67 | 495d4e95a8cf8bbf8b432b612a2aa328 |
| won_date | 2018-01-24 15:19:49 | 2018-05-10 19:07:39 | 2018-06-29 17:54:16 |
| business_segment | construction_tools_house_garden | car_accessories | home_decor |
| lead_type | online_medium | online_medium | online_medium |
| lead_behaviour_profile | null | wolf | wolf |
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
fk: none

samples:
| column | latest | sample | sample |
|---|---|---|---|
| mql_id | fffffe98d0963d27015c198262d97221 | 387ba2ba73ce1e4c81fb09175bf2a1f3 | 923b4926a703db2f6355a326bf10656e |
| first_contact_date | 2018-01-25 | 2018-02-01 | 2018-01-27 |
| landing_page_id | 88740e65d5d6b056e0cda098e1ea6313 | 83bfeb1d106df88a2cde0965999161f0 | f017be4dbf86243af5c1ebed0cff36a2 |
| origin | social | organic_search | direct_traffic |

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
fk: none

samples:
| column | latest | sample | sample |
|---|---|---|---|
| order_id | fffe41c64501cc87c801fd61db3f6244 | 58346246ea802a21cb34124ed2326770 | 80501e8921c07f421d238fdf268c5ce4 |
| order_item_id | 1 | 4 | 1 |
| product_id | 350688d9dc1e75ff97be326363655e01 | ee0c1cf2fbeae95205b4aa506f1469f0 | 913580fde3e72c3b3e4ce0b79963bee6 |
| seller_id | f7ccf836d21b2fb1de37564105216cc1 | cc419e0650a3c5ba77189a1882b7556a | b76dba6c951ab00dc4edf0a1aa88037e |
| shipping_limit_date | 2018-06-12 17:10:13 | 2018-07-13 17:25:53 | 2017-02-19 22:30:52 |
| price | 43 | 44.99 | 10.99 |
| freight_value | 12.79 | 7.58 | 16.05 |

# "order_payments"  (rows=103886)

columns:
"order_id" text: profile metrics skipped
"payment_sequential" int: 1..29, avg=1.09268
"payment_type" text: profile metrics skipped
"payment_installments" int: 0..24, avg=2.85335
"payment_value" float: 0..13664.1, avg=154.1

indexes: none
fk: none

samples:
| column | latest | sample | sample |
|---|---|---|---|
| order_id | fffe41c64501cc87c801fd61db3f6244 | 90bd52654dd4d9b5601a908e69f98659 | df31c03f22f15e6460a9eeb4de4968ac |
| payment_sequential | 1 | 1 | 1 |
| payment_type | credit_card | credit_card | credit_card |
| payment_installments | 1 | 10 | 4 |
| payment_value | 55.79 | 182.96 | 134.58 |

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
fk: none

samples:
| column | latest | sample | sample |
|---|---|---|---|
| review_id | fffefe7a48d22f7b32046421062219d1 | ede62474f1618961be12678f362dca4a | 5b27644eb6a7c79082b61b97d6488cca |
| order_id | 1061bc32577c6b8beb107bf1b5a65175 | b0f4af5c1b06e24fef510703bfe9f0a6 | cb71bd92e29c501f67b650fa19bee739 |
| review_score | 5 | 5 | 5 |
| review_comment_title | null | null | null |
| review_comment_message | null | Otimo comprar por este site as mercadorias chegam antes do prazo determinado. | null |
| review_creation_date | 2017-10-28 00:00:00 | 2017-11-11 00:00:00 | 2018-04-28 00:00:00 |
| review_answer_timestamp | 2017-10-30 21:43:56 | 2017-11-15 09:54:14 | 2018-04-29 04:29:49 |

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
fk: none

samples:
| column | latest | sample | sample |
|---|---|---|---|
| order_id | fffe41c64501cc87c801fd61db3f6244 | 312bfb221da51864b9fc4b361542ee5b | 475e0dfe76ac445fc716ef9eca7a00bd |
| customer_id | 96d649da0cc4ff33bb408b199d4c7dcf | 4ad01985d5063053b72dbd0191762f81 | f8de827b79379e8ba3b7f0c8c363b085 |
| order_status | delivered | delivered | delivered |
| order_purchase_timestamp | 2018-06-09 17:00:18 | 2018-06-04 19:33:54 | 2017-11-30 22:04:12 |
| order_approved_at | 2018-06-09 17:10:13 | 2018-06-04 19:53:21 | 2017-12-01 10:31:15 |
| order_delivered_carrier_date | 2018-06-11 14:11:00 | 2018-06-06 14:47:00 | 2017-12-04 12:59:36 |
| order_delivered_customer_date | 2018-06-14 17:56:26 | 2018-06-08 22:46:49 | 2017-12-06 18:30:10 |
| order_estimated_delivery_date | 2018-06-28 00:00:00 | 2018-06-28 00:00:00 | 2017-12-18 00:00:00 |

# "product_category_name_translation"  (rows=71)

columns:
"product_category_name" text: all distinct
"product_category_name_english" text: all distinct

indexes: none
fk: none

samples:
| column | latest | sample | sample |
|---|---|---|---|
| product_category_name | utilidades_domesticas | flores | livros_importados |
| product_category_name_english | housewares | flowers | books_imported |

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
fk: none

samples:
| column | latest | sample | sample |
|---|---|---|---|
| product_id | fffe9eeff12fcbd74a2f2b007dde0c58 | 90f83991bae254d0fd02bdddaa20b340 | 267a48e9a306231f94d36b274782ca5d |
| product_category_name | brinquedos | moveis_decoracao | automotivo |
| product_name_lenght | 57 | 59 | 52 |
| product_description_lenght | 1536 | 241 | 381 |
| product_photos_qty | 3 | 1 | 2 |
| product_weight_g | 3900 | 1400 | 4259 |
| product_length_cm | 43 | 40 | 24 |
| product_height_cm | 16 | 10 | 22 |
| product_width_cm | 11 | 34 | 32 |

# "sellers"  (rows=3095)

columns:
"seller_id" text: unique identifier
"seller_zip_code_prefix" int: 2246 distinct, 1001..99730, avg=32291.1, median=14940
"seller_city" text: 611 distinct
"seller_state" text: 23 distinct

indexes: none
fk: none

samples:
| column | latest | sample | sample |
|---|---|---|---|
| seller_id | ffff564a4f9085cd26170f4732393726 | 73a63f72308aa20a46f4b1632018f196 | 21c62b998a043ebe31161d38f84929fc |
| seller_zip_code_prefix | 13070 | 82510 | 60110 |
| seller_city | campinas | curitiba | fortaleza |
| seller_state | SP | PR | CE |
