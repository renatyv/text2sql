---
generator: db-snooper
version: 0.0.26
generated_at_utc: 2026-08-16T08:09:20.750265Z
dialect: sqlite
database: /var/folders/9j/b9bx_drd53sc6zbpsqyrjy4h0000gn/T/dbsnoop-qdnymb79/electronic_sales.sqlite
schema: main
---

# customers

```sql
CREATE TABLE "customers" (
"index" INTEGER,
  "customer_id" TEXT,
  "customer_unique_id" TEXT,
  "customer_zip_code_prefix" INTEGER,
  "customer_city" TEXT,
  "customer_state" TEXT
);
```

## Indexes

- CREATE INDEX "ix_customers_index"ON "customers" ("index")

## Rows

- total=99441

| column | latest | sample | sample |
|---|---|---|---|
| index | 99440 | 86423 | 26938 |
| customer_id | 274fa6071e5e17fe303b9748641082c8 | 3985d677d82341e381758018d936ef49 | 5f750fcde3b475b60c61b731cd78dba6 |
| customer_unique_id | 84732c5050c01db9b23e19ba39899398 | c297bb9230dc3152522d0c2b4caa7a1a | 64ecd6ed6e3f52a5d7499a0ce66b15f1 |
| customer_zip_code_prefix | 6703 | 8773 | 27640 |
| customer_city | cotia | mogi das cruzes | barao de juparana |
| customer_state | SP | SP | RJ |

## Columns

- index: all distinct, int 0..99440
  - stats: average=49720, median=49720
- customer_id: unique identifier
- customer_unique_id: 96096 distinct
- customer_zip_code_prefix: 14994 distinct, int 1003..99990
  - stats: average=35137.5, median=24416
- customer_city: 4119 distinct
- customer_state: 27 distinct


# geolocation

```sql
CREATE TABLE "geolocation" (
"index" INTEGER,
  "geolocation_zip_code_prefix" INTEGER,
  "geolocation_lat" REAL,
  "geolocation_lng" REAL,
  "geolocation_city" TEXT,
  "geolocation_state" TEXT
);
```

## Indexes

- CREATE INDEX "ix_geolocation_index"ON "geolocation" ("index")

## Rows

- total≈1000163 (estimated from db stats; row/column profiling skipped)


# order_items

```sql
CREATE TABLE "order_items" (
"index" INTEGER,
  "order_id" TEXT,
  "order_item_id" INTEGER,
  "product_id" TEXT,
  "seller_id" TEXT,
  "shipping_limit_date" TEXT,
  "price" REAL,
  "freight_value" REAL
);
```

## Indexes

- CREATE INDEX "ix_order_items_index"ON "order_items" ("index")

## Rows

- total=112650

| column | latest | sample | sample |
|---|---|---|---|
| index | 112649 | 77800 | 8142 |
| order_id | fffe41c64501cc87c801fd61db3f6244 | b11277967c91e971b81a787a51849320 | 127db093fee728a76262a027b66556aa |
| order_item_id | 1 | 1 | 1 |
| product_id | 350688d9dc1e75ff97be326363655e01 | e4ef515e041ce5062868aacf106df8b3 | a9516a079e37a9c9c36b9b78b10169e8 |
| seller_id | f7ccf836d21b2fb1de37564105216cc1 | ca3bd7cd9f149df75950150d010fe4a2 | 7c67e1448b00f6e969d365cea6b010ab |
| shipping_limit_date | 2018-06-12 17:10:13 | 2017-03-17 02:23:28 | 2017-05-31 16:42:20 |
| price | 43 | 98.3 | 124.99 |
| freight_value | 12.79 | 41.92 | 18.59 |

## Columns

- index: all distinct, int 0..112649
  - stats: average=56324.5
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
"index" INTEGER,
  "order_id" TEXT,
  "payment_sequential" INTEGER,
  "payment_type" TEXT,
  "payment_installments" INTEGER,
  "payment_value" REAL
);
```

## Indexes

- CREATE INDEX "ix_order_payments_index"ON "order_payments" ("index")

## Rows

- total=103886

| column | latest | sample | sample |
|---|---|---|---|
| index | 103885 | 842 | 100595 |
| order_id | 28bbae6599b09d39ca406b747b6632b1 | 88222a046146c4aab763e90b35ab4799 | e5b496243933ca726952157c6d6bb648 |
| payment_sequential | 1 | 1 | 1 |
| payment_type | boleto | credit_card | credit_card |
| payment_installments | 1 | 1 | 5 |
| payment_value | 191.58 | 10.39 | 138.9 |

## Columns

- index: all distinct, int 0..103885
  - stats: average=51942.5
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
"index" INTEGER,
  "review_id" TEXT,
  "order_id" TEXT,
  "review_score" INTEGER,
  "review_comment_title" TEXT,
  "review_comment_message" TEXT,
  "review_creation_date" TEXT,
  "review_answer_timestamp" TEXT
);
```

## Indexes

- CREATE INDEX "ix_order_reviews_index"ON "order_reviews" ("index")

## Rows

- total=99224

| column | latest | sample | sample |
|---|---|---|---|
| index | 99223 | 51040 | 77122 |
| review_id | efe49f1d6f951dd88b51e6ccd4cc548f | 38cabd8408d8e48b75b94e0f1aa9f1c2 | 41cf8fdf7074755935805dc52565e5c6 |
| order_id | 90531360ecb1eec2a1fbb265a0db0508 | 5b7687ff6fc51511eec02492c8169ff6 | 4452080876f5de5c69e66d6d8b9e10cc |
| review_score | 1 | 5 | 5 |
| review_comment_title | null | null | null |
| review_comment_message | meu produto chegou e ja tenho que devolver, pois está com defeito , não segurar carga | Mto rápido  | Muito Bom |
| review_creation_date | 2017-07-03 00:00:00 | 2018-03-23 00:00:00 | 2017-09-19 00:00:00 |
| review_answer_timestamp | 2017-07-03 21:01:49 | 2018-03-25 20:26:06 | 2017-09-20 15:57:49 |

## Columns

- index: all distinct, int 0..99223
  - stats: average=49611.5, median=49611.5
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
"index" INTEGER,
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

## Indexes

- CREATE INDEX "ix_orders_index"ON "orders" ("index")

## Rows

- total=99441

| column | latest | sample | sample |
|---|---|---|---|
| index | 99440 | 72979 | 20597 |
| order_id | 66dea50a8b16d9b4dee7af250b4be1a5 | bd948f34444b602f314108a393c1f49e | 55c784ded75d252ba646536f7e8506b5 |
| customer_id | edb027a75a1449115f6b43211ae02a24 | baa600e4d9d98a86bd334869aeb7cf49 | 4ba06f0d95d8065031a5696bc5770ac3 |
| order_status | delivered | delivered | delivered |
| order_purchase_timestamp | 2018-03-08 20:57:30 | 2017-07-12 16:37:28 | 2017-12-25 15:48:56 |
| order_approved_at | 2018-03-09 11:20:28 | 2017-07-12 16:45:14 | 2017-12-25 16:08:48 |
| order_delivered_carrier_date | 2018-03-09 22:11:59 | 2017-07-17 14:30:10 | 2017-12-27 18:54:39 |
| order_delivered_customer_date | 2018-03-16 13:08:30 | 2017-07-25 19:12:30 | 2018-01-16 14:49:48 |
| order_estimated_delivery_date | 2018-04-03 00:00:00 | 2017-08-03 00:00:00 | 2018-01-24 00:00:00 |

## Columns

- index: all distinct, int 0..99440
  - stats: average=49720, median=49720
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
"index" INTEGER,
  "product_category_name" TEXT,
  "product_category_name_english" TEXT
);
```

## Indexes

- CREATE INDEX "ix_product_category_name_translation_index"ON "product_category_name_translation" ("index")

## Rows

- total=71

| column | latest | sample | sample |
|---|---|---|---|
| index | 70 | 61 | 46 |
| product_category_name | seguros_e_servicos | musica | artes |
| product_category_name_english | security_and_services | music | art |

## Columns

- index: all distinct, int 0..70
  - stats: average=35, median=35
- product_category_name: all distinct
- product_category_name_english: all distinct


# products

```sql
CREATE TABLE "products" (
"index" INTEGER,
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

## Indexes

- CREATE INDEX "ix_products_index"ON "products" ("index")

## Rows

- total=32951

| column | latest | sample | sample |
|---|---|---|---|
| index | 32950 | 30972 | 30622 |
| product_id | 106392145fca363410d287a815be6de4 | 58f036d3b8f12d9378518f902fb4e226 | 6e8230f255f558ee8dfc9bcbe56b9434 |
| product_category_name | cama_mesa_banho | artes | livros_interesse_geral |
| product_name_lenght | 58 | 58 | 32 |
| product_description_lenght | 309 | 374 | 1311 |
| product_photos_qty | 1 | 3 | 2 |
| product_weight_g | 2083 | 1650 | 875 |
| product_length_cm | 12 | 41 | 20 |
| product_height_cm | 2 | 10 | 10 |
| product_width_cm | 7 | 13 | 30 |

## Columns

- index: all distinct, int 0..32950
  - stats: average=16475, median=16475
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
"index" INTEGER,
  "seller_id" TEXT,
  "seller_zip_code_prefix" INTEGER,
  "seller_city" TEXT,
  "seller_state" TEXT
);
```

## Indexes

- CREATE INDEX "ix_sellers_index"ON "sellers" ("index")

## Rows

- total=3095

| column | latest | sample | sample |
|---|---|---|---|
| index | 3094 | 1789 | 1031 |
| seller_id | 9e25199f6ef7e7c347120ff175652c3b | e82de6494d91d3c4c54450f59b227a94 | 0bb27263628258b8111a0262769fa9db |
| seller_zip_code_prefix | 12051 | 14940 | 3077 |
| seller_city | taubate | ibitinga | sao paulo |
| seller_state | SP | SP | SP |

## Columns

- index: all distinct, int 0..3094
  - stats: average=1547, median=1547
- seller_id: unique identifier
- seller_zip_code_prefix: 2246 distinct, int 1001..99730
  - stats: average=32291.1, median=14940
- seller_city: 611 distinct
- seller_state: 23 distinct
