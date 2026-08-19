---
generator: db-snooper
version: 0.0.26
generated_at_utc: 2026-08-16T08:08:38.881792Z
dialect: sqlite
database: /var/folders/9j/b9bx_drd53sc6zbpsqyrjy4h0000gn/T/dbsnoop-u95d2rk_/E_commerce.sqlite
schema: main
---

# customers

```sql
CREATE TABLE "customers" (
"customer_id" TEXT,
  "customer_unique_id" TEXT,
  "customer_zip_code_prefix" INTEGER,
  "customer_city" TEXT,
  "customer_state" TEXT
);
```

## Rows

- total=99441

| column | latest | sample | sample |
|---|---|---|---|
| customer_id | ffffe8b65bbe3087b653a978c870db99 | c808210ff5bbf25415730cefb3ca0113 | 693150edb86213500719059c108a7ca4 |
| customer_unique_id | 736e6bfa0510aa5b878881a226a5fd89 | 1288febe2567b6c947c5f7755a2856a0 | bdf10f125e125adbd467cbca77d80ab4 |
| customer_zip_code_prefix | 6172 | 80330 | 47800 |
| customer_city | osasco | curitiba | barreiras |
| customer_state | SP | PR | BA |

## Columns

- customer_id: unique identifier
- customer_unique_id: 96096 distinct
- customer_zip_code_prefix: 14994 distinct, int 1003..99990
  - stats: average=35137.5, median=24416
- customer_city: 4119 distinct
- customer_state: 27 distinct


# geolocation

```sql
CREATE TABLE "geolocation" (
"geolocation_zip_code_prefix" INTEGER,
  "geolocation_lat" REAL,
  "geolocation_lng" REAL,
  "geolocation_city" TEXT,
  "geolocation_state" TEXT
);
```

## Rows

- total≈1000163 (estimated from db stats; row/column profiling skipped)


# leads_closed

```sql
CREATE TABLE "leads_closed" (
"mql_id" TEXT,
  "seller_id" TEXT,
  "sdr_id" TEXT,
  "sr_id" TEXT,
  "won_date" TEXT,
  "business_segment" TEXT,
  "lead_type" TEXT,
  "lead_behaviour_profile" TEXT,
  "has_company" INTEGER,
  "has_gtin" INTEGER,
  "average_stock" TEXT,
  "business_type" TEXT,
  "declared_product_catalog_size" REAL,
  "declared_monthly_revenue" REAL
);
```

## Rows

- total=842

| column | latest | sample | sample |
|---|---|---|---|
| mql_id | fff8db9478d2fd72df65a67ee6b62f67 | f5772c97a8e2bcf909674d8701480d55 | d2e8ac40dc18011d5ecd890846f36ec1 |
| seller_id | bdae679a9b282249bc23b9b69dae9a99 | 63c6951772f3f4fc4e40ffd24207fd19 | 503ad3c3811010c6ba4577f411724b13 |
| sdr_id | 4b339f9567d060bcea4f5136b9f5949e | 4b339f9567d060bcea4f5136b9f5949e | 9d12ef1a7eca3ec58c545c678af7869c |
| sr_id | 6565aa9ce3178a5caf6171827af3a9ba | 060c0a26f19f4d66b42e0d8796688490 | 4ef15afb4b2723d8f3d81e51ec7afefe |
| won_date | 2018-01-24 15:19:49 | 2018-03-09 13:45:50 | 2018-04-27 03:00:00 |
| business_segment | construction_tools_house_garden | phone_mobile | food_drink |
| lead_type | online_medium | online_big | offline |
| lead_behaviour_profile | null | cat | eagle |
| has_company | null | null | null |
| has_gtin | null | null | null |
| average_stock | null | null | null |
| business_type | reseller | reseller | reseller |
| declared_product_catalog_size | null | null | null |
| declared_monthly_revenue | 0 | 0 | 0 |

## Columns

- mql_id: unique identifier
- seller_id: unique identifier
- sdr_id: 32 distinct
- sr_id: 22 distinct
- won_date: 824 distinct
- business_segment: 33 distinct, nulls=1
- lead_type: "online_medium"=332, "online_big"=126, "industry"=123, "offline"=104, "online_small"=77, "online_beginner"=57, "online_top"=14, "other"=3, nulls=6
- lead_behaviour_profile: "cat"=407, "eagle"=123, "wolf"=95, "shark"=24, "cat, wolf"=8, "eagle, cat"=3, "eagle, wolf"=3, "shark, cat"=1, "shark, wolf"=1, nulls=177
- has_company: 1=58, 0=5, nulls=779
- has_gtin: 1=54, 0=10, nulls=778
- average_stock: "5-20"=22, "50-200"=15, "1-5"=10, "20-50"=8, "200+"=7, "unknown"=4, nulls=776
- business_type: "reseller"=587, "manufacturer"=242, "other"=3, nulls=10
- declared_product_catalog_size: 33 distinct, nulls=773, num 1..2000
  - stats: average=233.029, median=100
- declared_monthly_revenue: 27 distinct, num 0..5e+07
  - stats: average=73377.7, median=0


# leads_qualified

```sql
CREATE TABLE "leads_qualified" (
"mql_id" TEXT,
  "first_contact_date" TEXT,
  "landing_page_id" TEXT,
  "origin" TEXT
);
```

## Rows

- total=8000

| column | latest | sample | sample |
|---|---|---|---|
| mql_id | fffffe98d0963d27015c198262d97221 | 2a5f614fbd6b69fd6695ae213d63eef0 | c31de872e4b768853e4180258bb2ab00 |
| first_contact_date | 2018-01-25 | 2017-07-12 | 2018-02-01 |
| landing_page_id | 88740e65d5d6b056e0cda098e1ea6313 | 31aa231b755f09653f48e41c110c8860 | f017be4dbf86243af5c1ebed0cff36a2 |
| origin | social | organic_search | organic_search |

## Columns

- mql_id: unique identifier
- first_contact_date: 336 distinct
- landing_page_id: 495 distinct
- origin: "organic_search"=2296, "paid_search"=1586, "social"=1350, "unknown"=1099, "direct_traffic"=499, "email"=493, "referral"=284, "other"=150, "display"=118, "other_publicities"=65, nulls=60


# order_items

```sql
CREATE TABLE "order_items" (
"order_id" TEXT,
  "order_item_id" INTEGER,
  "product_id" TEXT,
  "seller_id" TEXT,
  "shipping_limit_date" TEXT,
  "price" REAL,
  "freight_value" REAL
);
```

## Rows

- total=112650

| column | latest | sample | sample |
|---|---|---|---|
| order_id | fffe41c64501cc87c801fd61db3f6244 | 2259c28617dcf9c2ed34e78bb3dfb562 | da095f1f4d7e0e3111772d51a08ad079 |
| order_item_id | 1 | 1 | 1 |
| product_id | 350688d9dc1e75ff97be326363655e01 | abaefce0c17047c6829ff4078f2005d0 | 781afe929e3016a667f5f439afd55fce |
| seller_id | f7ccf836d21b2fb1de37564105216cc1 | 669ae81880e08f269a64487cfb287169 | 08633c14ef2db992c11f840f04fad4cd |
| shipping_limit_date | 2018-06-12 17:10:13 | 2017-12-21 00:12:12 | 2018-05-24 17:14:45 |
| price | 43 | 24.99 | 109.9 |
| freight_value | 12.79 | 19.14 | 9.12 |

## Columns

- order_id: profile metrics skipped
- order_item_id: int 1..21
- product_id: profile metrics skipped
- seller_id: profile metrics skipped
- shipping_limit_date: profile metrics skipped
- price: num 0.85..6735
  - stats: average=120.654
- freight_value: num 0..409.68
  - stats: average=19.9903


# order_payments

```sql
CREATE TABLE "order_payments" (
"order_id" TEXT,
  "payment_sequential" INTEGER,
  "payment_type" TEXT,
  "payment_installments" INTEGER,
  "payment_value" REAL
);
```

## Rows

- total=103886

| column | latest | sample | sample |
|---|---|---|---|
| order_id | fffe41c64501cc87c801fd61db3f6244 | 4a202f407d179ddfd8b58bba11a48809 | 4fd1eaa23a51a767193af5013ae6dbff |
| payment_sequential | 1 | 1 | 1 |
| payment_type | credit_card | credit_card | boleto |
| payment_installments | 1 | 2 | 1 |
| payment_value | 55.79 | 138.87 | 64.77 |

## Columns

- order_id: profile metrics skipped
- payment_sequential: int 1..29
  - stats: average=1.09268
- payment_type: profile metrics skipped
- payment_installments: int 0..24
  - stats: average=2.85335
- payment_value: num 0..13664.1
  - stats: average=154.1


# order_reviews

```sql
CREATE TABLE "order_reviews" (
"review_id" TEXT,
  "order_id" TEXT,
  "review_score" INTEGER,
  "review_comment_title" TEXT,
  "review_comment_message" TEXT,
  "review_creation_date" TEXT,
  "review_answer_timestamp" TEXT
);
```

## Rows

- total=99224

| column | latest | sample | sample |
|---|---|---|---|
| review_id | fffefe7a48d22f7b32046421062219d1 | ca44a6c225b903a90fad8244bab09e37 | e561213bb9a006c744517ed52091307e |
| order_id | 1061bc32577c6b8beb107bf1b5a65175 | 4128f35defa24e9fb110452626b9b824 | ce6ff4543efa5c36ab4ee967236674db |
| review_score | 5 | 5 | 3 |
| review_comment_title | null | null | null |
| review_comment_message | null | null | null |
| review_creation_date | 2017-10-28 00:00:00 | 2018-06-05 00:00:00 | 2017-09-22 00:00:00 |
| review_answer_timestamp | 2017-10-30 21:43:56 | 2018-06-07 21:02:44 | 2017-09-24 21:44:28 |

## Columns

- review_id: 98410 distinct
- order_id: 98673 distinct
- review_score: 5=57328, 4=19142, 1=11424, 3=8179, 2=3151, int 1..5
- review_comment_title: 4527 distinct, nulls=87656
- review_comment_message: 36159 distinct, nulls=58247
- review_creation_date: 636 distinct
- review_answer_timestamp: 98248 distinct


# orders

```sql
CREATE TABLE "orders" (
"order_id" TEXT,
  "customer_id" TEXT,
  "order_status" TEXT,
  "order_purchase_timestamp" TEXT,
  "order_approved_at" TEXT,
  "order_delivered_carrier_date" TEXT,
  "order_delivered_customer_date" TEXT,
  "order_estimated_delivery_date" TEXT
);
```

## Rows

- total=99441

| column | latest | sample | sample |
|---|---|---|---|
| order_id | fffe41c64501cc87c801fd61db3f6244 | 65efd756608003e865eb8d80f66a3ebb | 4185d8c314ae4ed44a3b41814c04cec4 |
| customer_id | 96d649da0cc4ff33bb408b199d4c7dcf | b91d240f382eadc3b867e8a28a56f7ba | 9ea89970b67c49baca8fe32d6f30ba7c |
| order_status | delivered | delivered | delivered |
| order_purchase_timestamp | 2018-06-09 17:00:18 | 2017-03-07 23:19:46 | 2017-08-27 14:29:01 |
| order_approved_at | 2018-06-09 17:10:13 | 2017-03-07 23:34:02 | 2017-08-27 14:45:08 |
| order_delivered_carrier_date | 2018-06-11 14:11:00 | 2017-03-10 10:06:50 | 2017-08-28 18:51:31 |
| order_delivered_customer_date | 2018-06-14 17:56:26 | 2017-03-16 12:22:14 | 2017-09-04 21:26:43 |
| order_estimated_delivery_date | 2018-06-28 00:00:00 | 2017-03-30 00:00:00 | 2017-09-19 00:00:00 |

## Columns

- order_id: unique identifier
- customer_id: unique identifier
- order_status: "delivered"=96478, "shipped"=1107, "canceled"=625, "unavailable"=609, "invoiced"=314, "processing"=301, "created"=5, "approved"=2
- order_purchase_timestamp: 98875 distinct
- order_approved_at: 90733 distinct, nulls=160
- order_delivered_carrier_date: 81018 distinct, nulls=1783
- order_delivered_customer_date: 95664 distinct, nulls=2965
- order_estimated_delivery_date: 459 distinct


# product_category_name_translation

```sql
CREATE TABLE "product_category_name_translation" (
"product_category_name" TEXT,
  "product_category_name_english" TEXT
);
```

## Rows

- total=71

| column | latest | sample | sample |
|---|---|---|---|
| product_category_name | utilidades_domesticas | construcao_ferramentas_iluminacao | moveis_colchao_e_estofado |
| product_category_name_english | housewares | construction_tools_lights | furniture_mattress_and_upholstery |

## Columns

- product_category_name: all distinct
- product_category_name_english: all distinct


# products

```sql
CREATE TABLE "products" (
"product_id" TEXT,
  "product_category_name" TEXT,
  "product_name_lenght" REAL,
  "product_description_lenght" REAL,
  "product_photos_qty" REAL,
  "product_weight_g" REAL,
  "product_length_cm" REAL,
  "product_height_cm" REAL,
  "product_width_cm" REAL
);
```

## Rows

- total=32951

| column | latest | sample | sample |
|---|---|---|---|
| product_id | fffe9eeff12fcbd74a2f2b007dde0c58 | 4fb3a6cb6e0aa78466566ab0ec0666c6 | f706789a48ef8564b44640d0180b1aa7 |
| product_category_name | brinquedos | cama_mesa_banho | cama_mesa_banho |
| product_name_lenght | 57 | 56 | 39 |
| product_description_lenght | 1536 | 230 | 292 |
| product_photos_qty | 3 | 1 | 1 |
| product_weight_g | 3900 | 2000 | 1300 |
| product_length_cm | 43 | 40 | 41 |
| product_height_cm | 16 | 7 | 7 |
| product_width_cm | 11 | 30 | 41 |

## Columns

- product_id: unique identifier
- product_category_name: 73 distinct, nulls=610
- product_name_lenght: 66 distinct, nulls=610, num 5..76
  - stats: average=48.4769, median=51
- product_description_lenght: 2960 distinct, nulls=610, num 4..3992
  - stats: average=771.495, median=595
- product_photos_qty: 1=16489, 2=6263, 3=3860, 4=2428, 5=1484, 6=968, 7=343, 8=192, 9=105, 10=95, 11=46, 12=35, 13=9, 15=8, 17=7, 14=5, 18=2, 19=1, 20=1, nulls=610, num 1..20
- product_weight_g: 2204 distinct, nulls=2, num 0..40425
  - stats: average=2276.47, median=700
- product_length_cm: 99 distinct, nulls=2, num 7..105
  - stats: average=30.8151, median=25
- product_height_cm: 102 distinct, nulls=2, num 2..105
  - stats: average=16.9377, median=13
- product_width_cm: 95 distinct, nulls=2, num 6..118
  - stats: average=23.1967, median=20


# sellers

```sql
CREATE TABLE "sellers" (
"seller_id" TEXT,
  "seller_zip_code_prefix" INTEGER,
  "seller_city" TEXT,
  "seller_state" TEXT
);
```

## Rows

- total=3095

| column | latest | sample | sample |
|---|---|---|---|
| seller_id | ffff564a4f9085cd26170f4732393726 | 8d79c8a04e42d722a75097ce5cbcf2ef | 5bba18b40e8c973b0f32e748004775b0 |
| seller_zip_code_prefix | 13070 | 61658 | 15840 |
| seller_city | campinas | caucaia | itajobi |
| seller_state | SP | CE | SP |

## Columns

- seller_id: unique identifier
- seller_zip_code_prefix: 2246 distinct, int 1001..99730
  - stats: average=32291.1, median=14940
- seller_city: 611 distinct
- seller_state: 23 distinct
