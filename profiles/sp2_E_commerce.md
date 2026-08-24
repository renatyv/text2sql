---
generator: db-snooper
version: 0.0.34
generated_at_utc: 2026-08-24T21:22:51.399781Z
dialect: sqlite
database: /var/folders/9j/b9bx_drd53sc6zbpsqyrjy4h0000gn/T/dbsnoop-593w9orh/E_commerce.sqlite
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
| customer_id | ffffe8b65bbe3087b653a978c870db99 | e34c642add1c46f0904e95997afac775 | 038043a62bca294b36eefac078e69729 |
| customer_unique_id | 736e6bfa0510aa5b878881a226a5fd89 | ce1fd4ae53af3460683ee1e6dff3e028 | 27177c850559ea0ec7bc49e36d30a45c |
| customer_zip_code_prefix | 6172 | 74820 | 84300 |
| customer_city | osasco | goiania | tibagi |
| customer_state | SP | GO | PR |

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
| mql_id | fff8db9478d2fd72df65a67ee6b62f67 | a7a8f7739ddc1abdd3bf7d4f9d8a911f | cd39b2fcf60d4580dbe25b82be3fd1ab |
| seller_id | bdae679a9b282249bc23b9b69dae9a99 | ec8463980a4e0ea9f8517aea1ed0c419 | 72bb43f9683adea77d240b7985e2dfa2 |
| sdr_id | 4b339f9567d060bcea4f5136b9f5949e | 4b339f9567d060bcea4f5136b9f5949e | 4b339f9567d060bcea4f5136b9f5949e |
| sr_id | 6565aa9ce3178a5caf6171827af3a9ba | 9e4d1098a3b0f5da39b0bc48f9876645 | 495d4e95a8cf8bbf8b432b612a2aa328 |
| won_date | 2018-01-24 15:19:49 | 2018-04-09 18:58:34 | 2018-03-27 03:00:00 |
| business_segment | construction_tools_house_garden | home_decor | pet |
| lead_type | online_medium | online_medium | online_medium |
| lead_behaviour_profile | null | shark | wolf |
| has_company | null | null | null |
| has_gtin | null | null | null |
| average_stock | null | null | null |
| business_type | reseller | manufacturer | reseller |
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
| mql_id | fffffe98d0963d27015c198262d97221 | 54ed85e7af8edc78637654cb4a89040e | 47cd9b242ad7a8e2ebc41a4ea69d2ca9 |
| first_contact_date | 2018-01-25 | 2017-09-09 | 2018-05-28 |
| landing_page_id | 88740e65d5d6b056e0cda098e1ea6313 | 007f9098284a86ee80ddeb25d53e0af8 | b76ef37428e6799c421989521c0e5077 |
| origin | social | paid_search | social |

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
| order_id | fffe41c64501cc87c801fd61db3f6244 | 2922d9dd6672241cb658a40bf507e4b1 | 9f076b87261e6c9894139da7d41eb02d |
| order_item_id | 1 | 1 | 4 |
| product_id | 350688d9dc1e75ff97be326363655e01 | bfc275f6de912665e4dcd8da32f43c10 | 7a82832901d5f4cd314a4e102c47bd2b |
| seller_id | f7ccf836d21b2fb1de37564105216cc1 | 71271995e85f5b8530be99ed54a91b89 | 9de4643a8dbde634fe55621059d92273 |
| shipping_limit_date | 2018-06-12 17:10:13 | 2018-07-17 10:06:23 | 2017-05-11 19:45:09 |
| price | 43 | 97 | 37.99 |
| freight_value | 12.79 | 14.98 | 15.1 |

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
| order_id | fffe41c64501cc87c801fd61db3f6244 | 4f3e39331cc2ae23851f526e268a8880 | 1182df110fbf0a14dfb08dd06c560836 |
| payment_sequential | 1 | 1 | 1 |
| payment_type | credit_card | credit_card | credit_card |
| payment_installments | 1 | 3 | 1 |
| payment_value | 55.79 | 123.2 | 49.84 |

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
| review_id | fffefe7a48d22f7b32046421062219d1 | c1b71fac499523deefebaf45957320d9 | 3c0a75a2772c0644eadf7fb35e34f635 |
| order_id | 1061bc32577c6b8beb107bf1b5a65175 | 91fb016286a84fa7006aa6033499914b | 8f4855298c9242f63d934ee48d41253f |
| review_score | 5 | 5 | 5 |
| review_comment_title | null | excelente | null |
| review_comment_message | null | null | Amo comprar nas lojas lannister. parabéns estou satisfeita obrigada por tudo bjks ficam com Deus 💋💋💕💕💞???? |
| review_creation_date | 2017-10-28 00:00:00 | 2018-08-23 00:00:00 | 2018-04-14 00:00:00 |
| review_answer_timestamp | 2017-10-30 21:43:56 | 2018-08-24 22:56:25 | 2018-04-17 00:02:11 |

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
| order_id | fffe41c64501cc87c801fd61db3f6244 | 4294e241abc5a583ac06ee97d557745f | 1ecb44533ccf6974a67e7d36d913b027 |
| customer_id | 96d649da0cc4ff33bb408b199d4c7dcf | 87a887e1089dce0c7fed596e76039b27 | 9e10bfe5eb4c55263654f22bfb0af9b7 |
| order_status | delivered | delivered | delivered |
| order_purchase_timestamp | 2018-06-09 17:00:18 | 2018-03-04 16:29:24 | 2017-08-07 09:56:09 |
| order_approved_at | 2018-06-09 17:10:13 | 2018-03-04 16:48:33 | 2017-08-07 10:05:26 |
| order_delivered_carrier_date | 2018-06-11 14:11:00 | 2018-03-08 21:09:35 | 2017-08-09 15:30:23 |
| order_delivered_customer_date | 2018-06-14 17:56:26 | 2018-03-20 21:58:29 | 2017-08-25 17:31:19 |
| order_estimated_delivery_date | 2018-06-28 00:00:00 | 2018-04-02 00:00:00 | 2017-08-29 00:00:00 |

# "product_category_name_translation"  (rows=71)

columns:
"product_category_name" text: all distinct
"product_category_name_english" text: all distinct

indexes: none

samples:
| column | latest | sample | sample |
|---|---|---|---|
| product_category_name | utilidades_domesticas | instrumentos_musicais | beleza_saude |
| product_category_name_english | housewares | musical_instruments | health_beauty |

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
| product_id | fffe9eeff12fcbd74a2f2b007dde0c58 | 880f4cc8f0bd44fe5afa9fc978a216e1 | 3948f284081821f4e27ba8c23d4cbc9a |
| product_category_name | brinquedos | cine_foto | brinquedos |
| product_name_lenght | 57 | 52 | 26 |
| product_description_lenght | 1536 | 578 | 344 |
| product_photos_qty | 3 | 1 | 1 |
| product_weight_g | 3900 | 100 | 1825 |
| product_length_cm | 43 | 16 | 33 |
| product_height_cm | 16 | 5 | 19 |
| product_width_cm | 11 | 12 | 45 |

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
| seller_id | ffff564a4f9085cd26170f4732393726 | a08692680c77d30a0b4280da5df01c5a | dfc5fb7259bb2b599ca565e6e9448f0f |
| seller_zip_code_prefix | 13070 | 4719 | 9780 |
| seller_city | campinas | sao paulo | sao bernardo do campo |
| seller_state | SP | SP | SP |
