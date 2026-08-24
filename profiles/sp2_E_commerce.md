---
generator: db-snooper
version: 0.0.34
generated_at_utc: 2026-08-24T21:58:22.859128Z
dialect: sqlite
database: /var/folders/9j/b9bx_drd53sc6zbpsqyrjy4h0000gn/T/dbsnoop-ro9dgqm9/E_commerce.sqlite
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
| customer_id | ffffe8b65bbe3087b653a978c870db99 | d41c394310a182cb056aac9346787d35 | 6cb94c8d3c096c20feafe2abf1ed78d3 |
| customer_unique_id | 736e6bfa0510aa5b878881a226a5fd89 | 8ccefd0fe3c240e494ee7326a9feca1d | 3daa1c97a3155484f70c88b19c90dfb5 |
| customer_zip_code_prefix | 6172 | 35680 | 61890 |
| customer_city | osasco | itauna | guaiuba |
| customer_state | SP | MG | CE |

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
| mql_id | fff8db9478d2fd72df65a67ee6b62f67 | d90b1c32b55f731e8a2072bfad782fdd | 85ac6feb584b665e85664974c546cfec |
| seller_id | bdae679a9b282249bc23b9b69dae9a99 | d8d9567d0bfb0bc7eb845a205ba42657 | 74636e24f01da9268b0ed88dacd8513e |
| sdr_id | 4b339f9567d060bcea4f5136b9f5949e | 4b339f9567d060bcea4f5136b9f5949e | 56bf83c4bb35763a51c2baab501b4c67 |
| sr_id | 6565aa9ce3178a5caf6171827af3a9ba | d3d1e91a157ea7f90548eef82f1955e3 | 9ae085775a198122c5586fa830ff7f2b |
| won_date | 2018-01-24 15:19:49 | 2018-02-09 13:41:10 | 2018-02-28 16:19:57 |
| business_segment | construction_tools_house_garden | books | toys |
| lead_type | online_medium | online_medium | online_medium |
| lead_behaviour_profile | null | wolf | cat |
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
| mql_id | fffffe98d0963d27015c198262d97221 | 49bf72bb66a00f922b002b7fcac4804f | 2e95ade370c3871fda51e03448bf1b20 |
| first_contact_date | 2018-01-25 | 2018-02-21 | 2018-02-01 |
| landing_page_id | 88740e65d5d6b056e0cda098e1ea6313 | 2228a43ac0bc372e25f9569e69fc9015 | 40dec9f3d5259a3d2dbcdab2114fae47 |
| origin | social | paid_search | paid_search |

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
| order_id | fffe41c64501cc87c801fd61db3f6244 | ef26a1bd5203cf613f8150597210abdc | 827efe7f5818a815652ea13b2dda5d7e |
| order_item_id | 1 | 1 | 1 |
| product_id | 350688d9dc1e75ff97be326363655e01 | ebe4b53f756dfcecfc539faf8ec0df9f | 04b48e86a968cfe620da1cab5c7556ae |
| seller_id | f7ccf836d21b2fb1de37564105216cc1 | 7178f9f4dd81dcef02f62acdf8151e01 | 15b3b1b81484422eb41df68ac87f1f50 |
| shipping_limit_date | 2018-06-12 17:10:13 | 2017-08-02 23:45:06 | 2017-11-30 02:12:58 |
| price | 43 | 199 | 43.35 |
| freight_value | 12.79 | 16.14 | 12.69 |

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
| order_id | fffe41c64501cc87c801fd61db3f6244 | 1bb86f8d6d2967cbf88b8a487d536e43 | 2bad3a7085e17ad44f9117d127de525f |
| payment_sequential | 1 | 1 | 1 |
| payment_type | credit_card | credit_card | credit_card |
| payment_installments | 1 | 1 | 1 |
| payment_value | 55.79 | 81.75 | 61.83 |

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
| review_id | fffefe7a48d22f7b32046421062219d1 | 24c49c99bb61d6912887795f94e680de | 662d2c533d56243557c12699eff9d5a3 |
| order_id | 1061bc32577c6b8beb107bf1b5a65175 | 371dcdd114490b436dff8fac7d52a928 | aa20064eef8808d62ed9ac5286ec0796 |
| review_score | 5 | 4 | 5 |
| review_comment_title | null | null | null |
| review_comment_message | null | null | null |
| review_creation_date | 2017-10-28 00:00:00 | 2018-07-12 00:00:00 | 2017-04-14 00:00:00 |
| review_answer_timestamp | 2017-10-30 21:43:56 | 2018-07-13 18:53:26 | 2017-04-16 19:41:32 |

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
| order_id | fffe41c64501cc87c801fd61db3f6244 | f380a3a29b8b454d07e134ad890c93b3 | d6e3732aea036f7d71b44db75163e2f4 |
| customer_id | 96d649da0cc4ff33bb408b199d4c7dcf | 5fa2daff047604045729c55aac7b6c3b | 0e030dda2e8d63beb191f52346ac0fbe |
| order_status | delivered | delivered | delivered |
| order_purchase_timestamp | 2018-06-09 17:00:18 | 2017-06-22 22:30:56 | 2018-07-03 09:45:53 |
| order_approved_at | 2018-06-09 17:10:13 | 2017-06-22 22:43:17 | 2018-07-05 16:27:57 |
| order_delivered_carrier_date | 2018-06-11 14:11:00 | 2017-06-23 12:35:59 | 2018-07-04 14:03:00 |
| order_delivered_customer_date | 2018-06-14 17:56:26 | 2017-06-27 18:17:51 | 2018-07-05 15:21:52 |
| order_estimated_delivery_date | 2018-06-28 00:00:00 | 2017-07-12 00:00:00 | 2018-07-20 00:00:00 |

# "product_category_name_translation"  (rows=71)

columns:
"product_category_name" text: all distinct
"product_category_name_english" text: all distinct

indexes: none

samples:
| column | latest | sample | sample |
|---|---|---|---|
| product_category_name | utilidades_domesticas | fashion_roupa_masculina | papelaria |
| product_category_name_english | housewares | fashion_male_clothing | stationery |

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
| product_id | fffe9eeff12fcbd74a2f2b007dde0c58 | 0d9e040b938001c020cc395f7ee87ce7 | 6d8d9c9af735eae354cb0b43a9cbebfa |
| product_category_name | brinquedos | automotivo | fashion_bolsas_e_acessorios |
| product_name_lenght | 57 | 52 | 63 |
| product_description_lenght | 1536 | 126 | 655 |
| product_photos_qty | 3 | 1 | 4 |
| product_weight_g | 3900 | 100 | 300 |
| product_length_cm | 43 | 16 | 16 |
| product_height_cm | 16 | 10 | 9 |
| product_width_cm | 11 | 16 | 20 |

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
| seller_id | ffff564a4f9085cd26170f4732393726 | c03121937e54a93fcc1825c3098bbb6e | 76c47a299e4a8fe992316a85865acbe9 |
| seller_zip_code_prefix | 13070 | 82800 | 14075 |
| seller_city | campinas | curitiba | ribeirao preto |
| seller_state | SP | PR | SP |
