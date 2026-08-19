---
generator: db-snooper
version: 0.0.26
generated_at_utc: 2026-08-16T08:07:39.897983Z
dialect: sqlite
database: /var/folders/9j/b9bx_drd53sc6zbpsqyrjy4h0000gn/T/dbsnoop-qd4z6rli/Brazilian_E_Commerce.sqlite
schema: main
---

# olist_customers

```sql
CREATE TABLE olist_customers (
	customer_id TEXT, 
	customer_unique_id TEXT, 
	customer_zip_code_prefix BIGINT, 
	customer_city TEXT, 
	customer_state TEXT
);
```

## Rows

- total=99441

| column | latest | sample | sample |
|---|---|---|---|
| customer_id | ffffe8b65bbe3087b653a978c870db99 | 9194b81f653a21ddac05211e071c9d7f | aab60551b0c17b5dd31690b0d1bf3911 |
| customer_unique_id | 736e6bfa0510aa5b878881a226a5fd89 | 6505382a6c43c538aba29d966f31e175 | 42572eaafadc787ce69afad9af65a7b7 |
| customer_zip_code_prefix | 6172 | 13273 | 8160 |
| customer_city | osasco | valinhos | sao paulo |
| customer_state | SP | SP | SP |

## Columns

- customer_id: unique identifier
- customer_unique_id: 96096 distinct
- customer_zip_code_prefix: 14994 distinct, int 1003..99990
  - stats: average=35137.5, median=24416
- customer_city: 4119 distinct
- customer_state: 27 distinct


# olist_geolocation

```sql
CREATE TABLE olist_geolocation (
	geolocation_zip_code_prefix BIGINT, 
	geolocation_lat FLOAT, 
	geolocation_lng FLOAT, 
	geolocation_city TEXT, 
	geolocation_state TEXT
);
```

## Rows

- total≈1000163 (estimated from db stats; row/column profiling skipped)


# olist_order_items

```sql
CREATE TABLE olist_order_items (
	order_id TEXT, 
	order_item_id BIGINT, 
	product_id TEXT, 
	seller_id TEXT, 
	shipping_limit_date TEXT, 
	price FLOAT, 
	freight_value FLOAT
);
```

## Rows

- total=112650

| column | latest | sample | sample |
|---|---|---|---|
| order_id | fffe41c64501cc87c801fd61db3f6244 | d4acee3ee57cea5cac8b23fadcabbeda | 864bd5ba759c631c93986c49f5c42168 |
| order_item_id | 1 | 1 | 1 |
| product_id | 350688d9dc1e75ff97be326363655e01 | 2ebf71f199b0f3f3331af7d426ad714c | 65735dc44187883022fa8d0d78c807bc |
| seller_id | f7ccf836d21b2fb1de37564105216cc1 | 4c18691b6037662be2df78a765d98ab5 | 43f8c9950d11ecd03a0304a49e010da6 |
| shipping_limit_date | 2018-06-12 17:10:13 | 2018-04-02 12:47:29 | 2017-08-03 15:32:52 |
| price | 43 | 39.95 | 155.99 |
| freight_value | 12.79 | 14.44 | 17.53 |

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


# olist_order_payments

```sql
CREATE TABLE olist_order_payments (
	order_id TEXT, 
	payment_sequential BIGINT, 
	payment_type TEXT, 
	payment_installments BIGINT, 
	payment_value FLOAT
);
```

## Rows

- total=103886

| column | latest | sample | sample |
|---|---|---|---|
| order_id | fffe41c64501cc87c801fd61db3f6244 | 18b3b5404f523379b23e3eed42639acc | f409e6b1a36ed880f8c2280446f9e6bb |
| payment_sequential | 1 | 1 | 1 |
| payment_type | credit_card | credit_card | credit_card |
| payment_installments | 1 | 2 | 8 |
| payment_value | 55.79 | 291.07 | 621.83 |

## Columns

- order_id: profile metrics skipped
- payment_sequential: int 1..29
  - stats: average=1.09268
- payment_type: profile metrics skipped
- payment_installments: int 0..24
  - stats: average=2.85335
- payment_value: num 0..13664.1
  - stats: average=154.1


# olist_order_reviews

```sql
CREATE TABLE olist_order_reviews (
	review_id TEXT, 
	order_id TEXT, 
	review_score BIGINT, 
	review_comment_title TEXT, 
	review_comment_message TEXT, 
	review_creation_date TEXT, 
	review_answer_timestamp TEXT
);
```

## Rows

- total=99224

| column | latest | sample | sample |
|---|---|---|---|
| review_id | fffefe7a48d22f7b32046421062219d1 | 27e23e9a4217bbbf2e98610d19b2ea59 | 5263da9fe14004e89c90a5e4f64649f0 |
| order_id | 1061bc32577c6b8beb107bf1b5a65175 | 64f0da9068715955d37b40377363ecc7 | d69c7c969d600368c5f533b188e402eb |
| review_score | 5 | 2 | 1 |
| review_comment_title | null | null | STATUS DE ENTREGUE |
| review_comment_message | null | O produto comprado não tem a mesma qualidade de outros perfumes da mesma marca que comprei anteriormente. | Porém não recebi e muito menos membros da minha família recebeu o produto.  |
| review_creation_date | 2017-10-28 00:00:00 | 2017-10-13 00:00:00 | 2018-05-29 00:00:00 |
| review_answer_timestamp | 2017-10-30 21:43:56 | 2017-11-22 16:20:24 | 2018-05-29 21:41:58 |

## Columns

- review_id: 98410 distinct
- order_id: 98673 distinct
- review_score: 5=57328, 4=19142, 1=11424, 3=8179, 2=3151, int 1..5
- review_comment_title: 4527 distinct, nulls=87656
- review_comment_message: 36159 distinct, nulls=58247
- review_creation_date: 636 distinct
- review_answer_timestamp: 98248 distinct


# olist_orders

```sql
CREATE TABLE olist_orders (
	order_id TEXT, 
	customer_id TEXT, 
	order_status TEXT, 
	order_purchase_timestamp TEXT, 
	order_approved_at TEXT, 
	order_delivered_carrier_date TEXT, 
	order_delivered_customer_date TEXT, 
	order_estimated_delivery_date TEXT
);
```

## Rows

- total=99441

| column | latest | sample | sample |
|---|---|---|---|
| order_id | fffe41c64501cc87c801fd61db3f6244 | e734700453d78cc2958b64b3b5613bcd | d515df6c2f06c05d78204a42d3a0bd11 |
| customer_id | 96d649da0cc4ff33bb408b199d4c7dcf | 44a36762b3b2f6bc16c48380685d3d6e | 50474ea7574ee03f95852dcba23a5639 |
| order_status | delivered | delivered | delivered |
| order_purchase_timestamp | 2018-06-09 17:00:18 | 2017-03-08 15:10:18 | 2018-08-19 19:09:43 |
| order_approved_at | 2018-06-09 17:10:13 | 2017-03-08 15:10:18 | 2018-08-20 12:55:27 |
| order_delivered_carrier_date | 2018-06-11 14:11:00 | 2017-03-21 09:52:21 | 2018-08-23 14:01:00 |
| order_delivered_customer_date | 2018-06-14 17:56:26 | 2017-03-28 15:12:15 | 2018-08-29 22:21:19 |
| order_estimated_delivery_date | 2018-06-28 00:00:00 | 2017-04-19 00:00:00 | 2018-09-10 00:00:00 |

## Columns

- order_id: unique identifier
- customer_id: unique identifier
- order_status: "delivered"=96478, "shipped"=1107, "canceled"=625, "unavailable"=609, "invoiced"=314, "processing"=301, "created"=5, "approved"=2
- order_purchase_timestamp: 98875 distinct
- order_approved_at: 90733 distinct, nulls=160
- order_delivered_carrier_date: 81018 distinct, nulls=1783
- order_delivered_customer_date: 95664 distinct, nulls=2965
- order_estimated_delivery_date: 459 distinct


# olist_products

```sql
CREATE TABLE olist_products (
	product_id TEXT, 
	product_category_name TEXT, 
	product_name_lenght FLOAT, 
	product_description_lenght FLOAT, 
	product_photos_qty FLOAT, 
	product_weight_g FLOAT, 
	product_length_cm FLOAT, 
	product_height_cm FLOAT, 
	product_width_cm FLOAT
);
```

## Rows

- total=32951

| column | latest | sample | sample |
|---|---|---|---|
| product_id | fffe9eeff12fcbd74a2f2b007dde0c58 | fdac82e439dafa5f87a9547581532380 | e5188da1834c44869e7f0b1b2c0b4c14 |
| product_category_name | brinquedos | automotivo | informatica_acessorios |
| product_name_lenght | 57 | 60 | 49 |
| product_description_lenght | 1536 | 1541 | 937 |
| product_photos_qty | 3 | 1 | 1 |
| product_weight_g | 3900 | 1000 | 3100 |
| product_length_cm | 43 | 26 | 43 |
| product_height_cm | 16 | 40 | 35 |
| product_width_cm | 11 | 20 | 35 |

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


# olist_products_dataset

```sql
CREATE TABLE olist_products_dataset (
	"index" BIGINT, 
	product_id TEXT, 
	product_category_name TEXT, 
	product_name_lenght FLOAT, 
	product_description_lenght FLOAT, 
	product_photos_qty FLOAT, 
	product_weight_g FLOAT, 
	product_length_cm FLOAT, 
	product_height_cm FLOAT, 
	product_width_cm FLOAT
);
```

## Indexes

- ("index")

## Rows

- total=32951

| column | latest | sample | sample |
|---|---|---|---|
| index | 32950 | 18020 | 21211 |
| product_id | 106392145fca363410d287a815be6de4 | 8316da766ebc954ed00fe9bcf1413254 | 3faadd91c89ff779e6cd1fd09a46ee39 |
| product_category_name | cama_mesa_banho | automotivo | beleza_saude |
| product_name_lenght | 58 | 58 | 60 |
| product_description_lenght | 309 | 523 | 419 |
| product_photos_qty | 1 | 6 | 1 |
| product_weight_g | 2083 | 100 | 350 |
| product_length_cm | 12 | 24 | 32 |
| product_height_cm | 2 | 2 | 4 |
| product_width_cm | 7 | 17 | 11 |

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


# olist_sellers

```sql
CREATE TABLE olist_sellers (
	seller_id TEXT, 
	seller_zip_code_prefix BIGINT, 
	seller_city TEXT, 
	seller_state TEXT
);
```

## Rows

- total=3095

| column | latest | sample | sample |
|---|---|---|---|
| seller_id | ffff564a4f9085cd26170f4732393726 | 609e1a9a6c2539919b8205cf7c4e6ff0 | 6bd69102ab48df500790a8cecfc285c2 |
| seller_zip_code_prefix | 13070 | 88359 | 4293 |
| seller_city | campinas | brusque | sao paulo |
| seller_state | SP | SC | SP |

## Columns

- seller_id: unique identifier
- seller_zip_code_prefix: 2246 distinct, int 1001..99730
  - stats: average=32291.1, median=14940
- seller_city: 611 distinct
- seller_state: 23 distinct


# product_category_name_translation

```sql
CREATE TABLE product_category_name_translation (
	product_category_name TEXT, 
	product_category_name_english TEXT
);
```

## Rows

- total=71

| column | latest | sample | sample |
|---|---|---|---|
| product_category_name | utilidades_domesticas | fashion_roupa_feminina | beleza_saude |
| product_category_name_english | housewares | fashio_female_clothing | health_beauty |

## Columns

- product_category_name: all distinct
- product_category_name_english: all distinct
