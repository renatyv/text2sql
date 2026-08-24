---
generator: db-snooper
version: 0.0.34
generated_at_utc: 2026-08-24T21:57:03.153096Z
dialect: sqlite
database: /var/folders/9j/b9bx_drd53sc6zbpsqyrjy4h0000gn/T/dbsnoop-2n4r5edi/Brazilian_E_Commerce.sqlite
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
| customer_id | ffffe8b65bbe3087b653a978c870db99 | daf15f1b940cc6a72ba558f093dc00dd | 23786cea8b640b4add6ebb373091a6ac |
| customer_unique_id | 736e6bfa0510aa5b878881a226a5fd89 | 37bc3d463e2a0024012a7fa587597a3c | 585f61c2e4b273283550c434cf1d0640 |
| customer_zip_code_prefix | 6172 | 88598 | 29780 |
| customer_city | osasco | celso ramos | sao gabriel da palha |
| customer_state | SP | SC | ES |

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
| order_id | fffe41c64501cc87c801fd61db3f6244 | 7aea47643f83c856db4ceee0830f39da | 996259172fd54f591a1046dbffa906d3 |
| order_item_id | 1 | 1 | 1 |
| product_id | 350688d9dc1e75ff97be326363655e01 | 8173ca41cdb176462f9ae79821a48404 | ca5c923962558430573f83661dbe36d6 |
| seller_id | f7ccf836d21b2fb1de37564105216cc1 | d566c37fa119d5e66c4e9052e83ee4ea | 66922902710d126a0e7d26b0e3805106 |
| shipping_limit_date | 2018-06-12 17:10:13 | 2018-05-11 11:55:23 | 2018-04-05 23:08:47 |
| price | 43 | 35.9 | 105 |
| freight_value | 12.79 | 18.23 | 15.53 |

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
| order_id | fffe41c64501cc87c801fd61db3f6244 | cb7cdbc81a72944010981bb56fe37f54 | 22cee08cd372f903b380852fdf75a1eb |
| payment_sequential | 1 | 1 | 1 |
| payment_type | credit_card | credit_card | credit_card |
| payment_installments | 1 | 1 | 6 |
| payment_value | 55.79 | 52.38 | 91.89 |

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
| review_id | fffefe7a48d22f7b32046421062219d1 | 0b1e61925512ff464d29d630d394cc85 | 31a662fa3857e4779f0527f61a40c426 |
| order_id | 1061bc32577c6b8beb107bf1b5a65175 | cb1ef5be56747ab6c5ef7271ecf4e12c | a1ecf6ff2702a73805ca6ffa3771ab05 |
| review_score | 5 | 5 | 5 |
| review_comment_title | null | null | null |
| review_comment_message | null | muito bom | null |
| review_creation_date | 2017-10-28 00:00:00 | 2017-11-24 00:00:00 | 2017-04-06 00:00:00 |
| review_answer_timestamp | 2017-10-30 21:43:56 | 2017-11-27 14:59:44 | 2017-04-06 21:36:31 |

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
| order_id | fffe41c64501cc87c801fd61db3f6244 | a8b53c7a7288e0478af915b26764b54b | 0019c29108428acffd089c36103c9440 |
| customer_id | 96d649da0cc4ff33bb408b199d4c7dcf | 77acf6c07ec68312b7a4ad8016d3c731 | 5f6bbac628ae418db4e0f92932f899c1 |
| order_status | delivered | delivered | delivered |
| order_purchase_timestamp | 2018-06-09 17:00:18 | 2018-03-22 11:52:57 | 2018-03-06 06:40:28 |
| order_approved_at | 2018-06-09 17:10:13 | 2018-03-23 11:50:22 | 2018-03-06 06:50:26 |
| order_delivered_carrier_date | 2018-06-11 14:11:00 | 2018-03-27 15:16:38 | 2018-03-07 01:20:05 |
| order_delivered_customer_date | 2018-06-14 17:56:26 | 2018-04-03 18:58:58 | 2018-03-16 22:34:53 |
| order_estimated_delivery_date | 2018-06-28 00:00:00 | 2018-05-02 00:00:00 | 2018-04-11 00:00:00 |

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
| product_id | fffe9eeff12fcbd74a2f2b007dde0c58 | 6a73bd4563b3f205e24c101f9a3c0d14 | 28b5fef7b6d63771e9784bc68c783793 |
| product_category_name | brinquedos | cama_mesa_banho | eletrodomesticos |
| product_name_lenght | 57 | 46 | 60 |
| product_description_lenght | 1536 | 116 | 564 |
| product_photos_qty | 3 | 1 | 1 |
| product_weight_g | 3900 | 350 | 1500 |
| product_length_cm | 43 | 40 | 65 |
| product_height_cm | 16 | 4 | 8 |
| product_width_cm | 11 | 30 | 38 |

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
| index | 32950 | 7534 | 6929 |
| product_id | 106392145fca363410d287a815be6de4 | f7f7214af35d79cb0baa6038fdc65e2c | a6a86219152d22366ffe68794aa1c219 |
| product_category_name | cama_mesa_banho | utilidades_domesticas | telefonia |
| product_name_lenght | 58 | 47 | 50 |
| product_description_lenght | 309 | 485 | 500 |
| product_photos_qty | 1 | 5 | 1 |
| product_weight_g | 2083 | 1700 | 88 |
| product_length_cm | 12 | 32 | 19 |
| product_height_cm | 2 | 14 | 4 |
| product_width_cm | 7 | 28 | 11 |

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
| seller_id | ffff564a4f9085cd26170f4732393726 | f67efa3f0b6761102a7f8c6b7b571f5d | 52f976b17ea7f2f087f56dcc419328f6 |
| seller_zip_code_prefix | 13070 | 82300 | 86820 |
| seller_city | campinas | curitiba | california |
| seller_state | SP | PR | PR |

# "product_category_name_translation"  (rows=71)

columns:
"product_category_name" text: all distinct
"product_category_name_english" text: all distinct

indexes: none

samples:
| column | latest | sample | sample |
|---|---|---|---|
| product_category_name | utilidades_domesticas | fashion_roupa_infanto_juvenil | livros_interesse_geral |
| product_category_name_english | housewares | fashion_childrens_clothes | books_general_interest |
