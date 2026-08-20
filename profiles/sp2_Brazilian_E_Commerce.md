---
generator: db-snooper
version: 0.0.31
generated_at_utc: 2026-08-20T17:26:48.493779Z
dialect: sqlite
database: /var/folders/9j/b9bx_drd53sc6zbpsqyrjy4h0000gn/T/dbsnoop-twx8043o/Brazilian_E_Commerce.sqlite
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
fk: none

samples:
| column | latest | sample | sample |
|---|---|---|---|
| customer_id | ffffe8b65bbe3087b653a978c870db99 | cb177a0cad6d0debf72041b70b6ca9f5 | ff48f1a9014cdfc6f9cbfc1d0ac2b525 |
| customer_unique_id | 736e6bfa0510aa5b878881a226a5fd89 | 0d20fac912fcef6baa10ef72530ee3c4 | a48a1b0b5708e03743e9564390772ed0 |
| customer_zip_code_prefix | 6172 | 30120 | 5017 |
| customer_city | osasco | belo horizonte | sao paulo |
| customer_state | SP | MG | SP |

# "olist_geolocation"  (rows=≈1000163)

columns:
"geolocation_zip_code_prefix" bigint
"geolocation_lat" float
"geolocation_lng" float
"geolocation_city" text
"geolocation_state" text

indexes: none
fk: none


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
fk: none

samples:
| column | latest | sample | sample |
|---|---|---|---|
| order_id | fffe41c64501cc87c801fd61db3f6244 | 56ff65d43900d5ae69573bbf9369c417 | 64d68b5e88c8e4cda34a9d46314132a1 |
| order_item_id | 1 | 2 | 1 |
| product_id | 350688d9dc1e75ff97be326363655e01 | 1600dcf1cea8c0c83702e07b577ab231 | dad27486af34282fef3bef995d0fda7b |
| seller_id | f7ccf836d21b2fb1de37564105216cc1 | 6560211a19b47992c3666cc44a7e94c0 | 7a67c85e85bb2ce8582c35f2203ad736 |
| shipping_limit_date | 2018-06-12 17:10:13 | 2017-11-06 18:33:04 | 2017-10-13 17:14:20 |
| price | 43 | 44 | 199.99 |
| freight_value | 12.79 | 14.1 | 18.65 |

# "olist_order_payments"  (rows=103886)

columns:
"order_id" text: profile metrics skipped
"payment_sequential" bigint: 1..29, avg=1.09268
"payment_type" text: profile metrics skipped
"payment_installments" bigint: 0..24, avg=2.85335
"payment_value" float: 0..13664.1, avg=154.1

indexes: none
fk: none

samples:
| column | latest | sample | sample |
|---|---|---|---|
| order_id | fffe41c64501cc87c801fd61db3f6244 | 25ec17a7457f797d4a253f3f492d4686 | 2be14bfbd7aa00107ece493cbbcc29f0 |
| payment_sequential | 1 | 1 | 1 |
| payment_type | credit_card | boleto | credit_card |
| payment_installments | 1 | 1 | 3 |
| payment_value | 55.79 | 26.89 | 176.16 |

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
fk: none

samples:
| column | latest | sample | sample |
|---|---|---|---|
| review_id | fffefe7a48d22f7b32046421062219d1 | 9fd59cd04b42f600df9f25e54082a8d1 | b8f79fe5aae72e2bbb3874760f6d5881 |
| order_id | 1061bc32577c6b8beb107bf1b5a65175 | 3c314f50bc654f3c4e317b055681dff9 | f5bdbbff47c740c2cca90305841220a8 |
| review_score | 5 | 1 | 5 |
| review_comment_title | null | null | null |
| review_comment_message | null | Nada de chegar o meu pedido. | null |
| review_creation_date | 2017-10-28 00:00:00 | 2017-04-21 00:00:00 | 2018-02-21 00:00:00 |
| review_answer_timestamp | 2017-10-30 21:43:56 | 2017-04-23 05:37:03 | 2018-02-22 09:20:58 |

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
fk: none

samples:
| column | latest | sample | sample |
|---|---|---|---|
| order_id | fffe41c64501cc87c801fd61db3f6244 | e031b115c17b49bdf313c9150d4cfdb0 | 3147cb8f96cb619b380fd37e3da08c93 |
| customer_id | 96d649da0cc4ff33bb408b199d4c7dcf | 4b7e3d0d6bbbfcf977e12746495b9e30 | 43537c82236df07bc096a68639cc3c25 |
| order_status | delivered | delivered | delivered |
| order_purchase_timestamp | 2018-06-09 17:00:18 | 2018-03-19 14:26:20 | 2018-01-06 20:02:44 |
| order_approved_at | 2018-06-09 17:10:13 | 2018-03-19 14:35:52 | 2018-01-06 20:13:19 |
| order_delivered_carrier_date | 2018-06-11 14:11:00 | 2018-03-20 17:08:49 | 2018-01-09 20:18:21 |
| order_delivered_customer_date | 2018-06-14 17:56:26 | 2018-04-13 20:32:20 | 2018-01-15 17:27:55 |
| order_estimated_delivery_date | 2018-06-28 00:00:00 | 2018-04-09 00:00:00 | 2018-02-05 00:00:00 |

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
fk: none

samples:
| column | latest | sample | sample |
|---|---|---|---|
| product_id | fffe9eeff12fcbd74a2f2b007dde0c58 | 83ed3cc53055fe51099569075b77ceca | 3831462c36ead78cff9e8fb704dbb879 |
| product_category_name | brinquedos | eletronicos | papelaria |
| product_name_lenght | 57 | 55 | 60 |
| product_description_lenght | 1536 | 600 | 313 |
| product_photos_qty | 3 | 1 | 6 |
| product_weight_g | 3900 | 817 | 7200 |
| product_length_cm | 43 | 35 | 60 |
| product_height_cm | 16 | 8 | 20 |
| product_width_cm | 11 | 34 | 29 |

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
fk: none

samples:
| column | latest | sample | sample |
|---|---|---|---|
| index | 32950 | 18973 | 26524 |
| product_id | 106392145fca363410d287a815be6de4 | 4272f4544f17efd4fa4ccdc76912feab | 3e08b2e39d6d62bba485dfd958639662 |
| product_category_name | cama_mesa_banho | ferramentas_jardim | eletronicos |
| product_name_lenght | 58 | 27 | 36 |
| product_description_lenght | 309 | 961 | 167 |
| product_photos_qty | 1 | 4 | 1 |
| product_weight_g | 2083 | 1042 | 2350 |
| product_length_cm | 12 | 20 | 26 |
| product_height_cm | 2 | 24 | 26 |
| product_width_cm | 7 | 20 | 16 |

# "olist_sellers"  (rows=3095)

columns:
"seller_id" text: unique identifier
"seller_zip_code_prefix" bigint: 2246 distinct, 1001..99730, avg=32291.1, median=14940
"seller_city" text: 611 distinct
"seller_state" text: 23 distinct

indexes: none
fk: none

samples:
| column | latest | sample | sample |
|---|---|---|---|
| seller_id | ffff564a4f9085cd26170f4732393726 | 4c8b8048e33af2bf94f2eb547746a916 | b3f19518fcec265b2e97af287725f981 |
| seller_zip_code_prefix | 13070 | 14940 | 15170 |
| seller_city | campinas | ibitinga | tanabi |
| seller_state | SP | SP | SP |

# "product_category_name_translation"  (rows=71)

columns:
"product_category_name" text: all distinct
"product_category_name_english" text: all distinct

indexes: none
fk: none

samples:
| column | latest | sample | sample |
|---|---|---|---|
| product_category_name | utilidades_domesticas | moveis_cozinha_area_de_servico_jantar_e_jardim | telefonia |
| product_category_name_english | housewares | kitchen_dining_laundry_garden_furniture | telephony |
