---
generator: db-snooper
version: 0.0.26
generated_at_utc: 2026-08-16T08:08:43.581586Z
dialect: sqlite
database: /var/folders/9j/b9bx_drd53sc6zbpsqyrjy4h0000gn/T/dbsnoop-qsbsjlrv/bank_sales_trading.sqlite
schema: main
---

# bitcoin_members

```sql
CREATE TABLE "bitcoin_members" (
"member_id" TEXT,
  "first_name" TEXT,
  "region" TEXT
);
```

## Rows

- total=14

| column | latest | sample | sample |
|---|---|---|---|
| member_id | eccbc8 | c20ad4 | c4ca42 |
| first_name | Charlie | Leah | Danny |
| region | United States | Asia | Australia |

## Columns

- member_id: unique identifier
- first_name: "Abe"=1, "Alex"=1, "Ayush"=1, "Ben"=1, "Charlie"=1, "Danny"=1, "Enoch"=1, "Leah"=1, "Nandita"=1, "Pavan"=1, "Rowan"=1, "Sonia"=1, "Vikram"=1, "Vipul"=1
- region: "United States"=7, "Australia"=4, "Africa"=1, "Asia"=1, "India"=1


# bitcoin_prices

```sql
CREATE TABLE "bitcoin_prices" (
"ticker" TEXT,
  "market_date" TEXT,
  "price" REAL,
  "open" REAL,
  "high" REAL,
  "low" REAL,
  "volume" TEXT,
  "change" TEXT
);
```

## Rows

- total=3404

| column | latest | sample | sample |
|---|---|---|---|
| ticker | ETH | BTC | BTC |
| market_date | 31-12-2020 | 24-11-2020 | 03-04-2020 |
| price | 735.94 | 19152.6 | 6735.9 |
| open | 751.92 | 18394.6 | 6799.9 |
| high | 755.13 | 19416.6 | 7026.3 |
| low | 724.67 | 18074.8 | 6623.6 |
| volume | 1.04M | 180.79K | 1.35M |
| change | -2.11% | 4.21% | -0.95% |

## Columns

- ticker: "BTC"=1702, "ETH"=1702
- market_date: 1702 distinct
- price: 3362 distinct, num 8.2..63540.9
  - stats: average=6645.43, median=1961.73
- open: 3347 distinct, num 8.17..63544.2
  - stats: average=6630.64, median=1948.01
- high: 3351 distinct, num 8.5..64778
  - stats: average=6836.06, median=2036.43
- low: 3358 distinct, num 8.03..62067.5
  - stats: average=6403.45, median=1871.95
- volume: 2811 distinct
- change: 1496 distinct


# bitcoin_transactions

```sql
CREATE TABLE "bitcoin_transactions" (
"txn_id" INTEGER,
  "member_id" TEXT,
  "ticker" TEXT,
  "txn_date" TEXT,
  "txn_type" TEXT,
  "quantity" REAL,
  "percentage_fee" REAL,
  "txn_time" TEXT
);
```

## Rows

- total=22918

| column | latest | sample | sample |
|---|---|---|---|
| txn_id | 22918 | 7594 | 5279 |
| member_id | d3d944 | c9f0f8 | 6512bd |
| ticker | BTC | BTC | ETH |
| txn_date | 27-08-2021 | 18-07-2018 | 26-01-2018 |
| txn_type | BUY | BUY | BUY |
| quantity | 7.22216 | 7.9482 | 7.60621 |
| percentage_fee | 0.01 | 0.3 | 0.3 |
| txn_time | 2021-08-27T22:26:10.258Z | 2018-07-18T01:51:49.866Z | 2018-01-26T18:25:00.506Z |

## Columns

- txn_id: unique identifier, int 1..22918
- member_id: "c4ca42"=2161, "a87ff6"=1947, "aab323"=1909, "c81e72"=1833, "c20ad4"=1724, "45c48c"=1697, "6512bd"=1688, "c9f0f8"=1572, "d3d944"=1526, "e4da3b"=1448, "8f14e4"=1405, "c51ce4"=1400, "167909"=1341, "eccbc8"=1267
- ticker: "BTC"=12484, "ETH"=10434
- txn_date: 1700 distinct
- txn_type: "BUY"=18881, "SELL"=4037
- quantity: 22891 distinct, num 0.000711769..50
  - stats: average=5.06366, median=5.03259
- percentage_fee: 31 distinct, num 0..0.3
  - stats: average=0.255142, median=0.3
- txn_time: 22891 distinct


# cleaned_weekly_sales

```sql
CREATE TABLE "cleaned_weekly_sales" (
"week_date_formatted" TEXT,
  "week_date" TEXT,
  "region" TEXT,
  "platform" TEXT,
  "segment" TEXT,
  "customer_type" TEXT,
  "transactions" INTEGER,
  "sales" INTEGER,
  "week_number" INTEGER,
  "month_number" INTEGER,
  "calendar_year" INTEGER,
  "age_band" TEXT,
  "demographic" TEXT,
  "avg_transaction" REAL
);
```

## Rows

- total=17117

| column | latest | sample | sample |
|---|---|---|---|
| week_date_formatted | 2020-8-31 | 2019-4-29 | 2018-7-23 |
| week_date | 2020-08-31 | 2019-04-29 | 2018-07-23 |
| region | USA | CANADA | SOUTH AMERICA |
| platform | Shopify | Shopify | Retail |
| segment | unknown | F1 | C2 |
| customer_type | New | Existing | Existing |
| transactions | 154 | 560 | 551 |
| sales | 25762 | 103000 | 21339 |
| week_number | 36 | 18 | 30 |
| month_number | 8 | 4 | 7 |
| calendar_year | 2020 | 2019 | 2018 |
| age_band | unknown | Young Adults | Middle Aged |
| demographic | unknown | Families | Couples |
| avg_transaction | 167.29 | 183.93 | 38.73 |

## Columns

- week_date_formatted: 72 distinct
- week_date: 72 distinct
- region: "AFRICA"=2448, "ASIA"=2448, "CANADA"=2448, "OCEANIA"=2448, "USA"=2448, "SOUTH AMERICA"=2441, "EUROPE"=2436
- platform: "Retail"=8568, "Shopify"=8549
- segment: "unknown"=3024, "C1"=2016, "C2"=2016, "C3"=2016, "F1"=2016, "F2"=2016, "F3"=2009, "C4"=2004
- customer_type: "Existing"=8064, "New"=8045, "Guest"=1008
- transactions: 9307 distinct, int 1..2578158
  - stats: average=63554.3, median=1657
- sales: 16559 distinct, int 0..69763805
  - stats: average=2.3803e+06, median=196458
- week_number: 24 distinct, int 13..36
  - stats: average=24.4996, median=25
- month_number: 7=3330, 4=3327, 6=3093, 8=3089, 5=2853, 3=951, 9=474, int 3..9
- calendar_year: 2020=5711, 2019=5708, 2018=5698, int 2018..2020
- age_band: "Retirees"=6029, "Middle Aged"=4032, "Young Adults"=4032, "unknown"=3024
- demographic: "Couples"=8052, "Families"=6041, "unknown"=3024
- avg_transaction: 9539 distinct, num 0..880.33
  - stats: average=110.955, median=67.18


# customer_nodes

```sql
CREATE TABLE "customer_nodes" (
"customer_id" INTEGER,
  "region_id" INTEGER,
  "node_id" INTEGER,
  "start_date" TEXT,
  "end_date" TEXT
);
```

## Rows

- total=3500

| column | latest | sample | sample |
|---|---|---|---|
| customer_id | 500 | 358 | 19 |
| region_id | 2 | 3 | 2 |
| node_id | 5 | 3 | 3 |
| start_date | 2020-03-13 | 2020-01-15 | 2020-03-27 |
| end_date | 2020-03-18 | 2020-01-22 | 9999-12-31 |

## Columns

- customer_id: 500 distinct, int 1..500
- region_id: 1=770, 2=735, 3=714, 4=665, 5=616, int 1..5
- node_id: 1=728, 5=707, 4=704, 3=699, 2=662, int 1..5
- start_date: 161 distinct
- end_date: 160 distinct


# customer_regions

## All rows

| column | row 1 | row 2 | row 3 | row 4 | row 5 |
|---|---|---|---|---|---|
| region_id | 1 | 2 | 3 | 4 | 5 |
| region_name | Australia | America | Africa | Asia | Europe |


# customer_transactions

```sql
CREATE TABLE "customer_transactions" (
"customer_id" INTEGER,
  "txn_date" TEXT,
  "txn_type" TEXT,
  "txn_amount" INTEGER
);
```

## Rows

- total=5868

| column | latest | sample | sample |
|---|---|---|---|
| customer_id | 500 | 372 | 453 |
| txn_date | 2020-03-25 | 2020-03-15 | 2020-02-04 |
| txn_type | deposit | purchase | deposit |
| txn_amount | 825 | 44 | 171 |

## Columns

- customer_id: 500 distinct, int 1..500
- txn_date: 119 distinct
- txn_type: "deposit"=2671, "purchase"=1617, "withdrawal"=1580
- txn_amount: 999 distinct, int 0..1000
  - stats: average=504.211, median=503


# interest_map

```sql
CREATE TABLE "interest_map" (
"id" INTEGER,
  "interest_name" TEXT,
  "interest_summary" TEXT,
  "created_at" TEXT,
  "last_modified" TEXT
);
```

## Rows

- total=1209

| column | latest | sample | sample |
|---|---|---|---|
| id | 51678 | 14 | 12277 |
| interest_name | Plumbers | NFL Fans | Market Intelligence Researchers |
| interest_summary | Professionals reading industry news and researching products and services for plumbers. | People reading articles and websites about football and the NFL. | Professionals reading industry news focused on market intelligence. |
| created_at | 2019-05-06 22:00:00 | 2016-05-26 14:57:59 | 2017-12-04 17:10:02 |
| last_modified | 2019-05-07 18:50:04 | 2018-05-23 11:30:13 | 2017-12-18 10:57:27 |

## Columns

- id: unique identifier, int 1..51678
- interest_name: 1208 distinct
- interest_summary: 1188 distinct, nulls=20
- created_at: 302 distinct
- last_modified: 256 distinct


# interest_metrics

```sql
CREATE TABLE "interest_metrics" (
"_month" REAL,
  "_year" REAL,
  "month_year" TEXT,
  "interest_id" REAL,
  "composition" REAL,
  "index_value" REAL,
  "ranking" INTEGER,
  "percentile_ranking" REAL
);
```

## Rows

- total=14273

| column | latest | sample | sample |
|---|---|---|---|
| _month | 12 | null | 8 |
| _year | 2018 | null | 2019 |
| month_year | 12-2018 | null | 08-2019 |
| interest_id | 42239 | null | 6181 |
| composition | 1.74 | 2.56 | 2.34 |
| index_value | 1.39 | 1.73 | 1.28 |
| ranking | 523 | 646 | 998 |
| percentile_ranking | 47.44 | 45.9 | 13.14 |

## Columns

- _month: 8=1916, 7=1593, 3=1136, 2=1121, 4=1099, 12=995, 1=973, 11=928, 5=857, 10=857, 6=824, 9=780, nulls=1194, num 1..12
- _year: 2019=8023, 2018=5056, nulls=1194
- month_year: "08-2019"=1149, "03-2019"=1136, "02-2019"=1121, "04-2019"=1099, "12-2018"=995, "01-2019"=973, "11-2018"=928, "07-2019"=864, "05-2019"=857, "10-2018"=857, "06-2019"=824, "09-2018"=780, "08-2018"=767, "07-2018"=729, nulls=1194
- interest_id: 1202 distinct, nulls=1193, num 1..51678
- composition: 884 distinct, num 1.51..21.2
  - stats: average=3.3376, median=2.86
- index_value: 345 distinct, num 0.44..6.19
  - stats: average=1.53515, median=1.45
- ranking: 998 distinct, int 1..1194
  - stats: average=484.332, median=470
- percentile_ranking: 2301 distinct, num 0..99.92
  - stats: average=50.3404, median=50.46


# shopping_cart_campaign_identifier

## All rows

| column | row 1 | row 2 | row 3 |
|---|---|---|---|
| campaign_id | 1 | 2 | 3 |
| products | 1-3 | 4-5 | 6-8 |
| campaign_name | BOGOF - Fishing For Compliments | 25% Off - Living The Lux Life | Half Off - Treat Your Shellf(ish) |
| start_date | 2020-01-01 | 2020-01-15 | 2020-02-01 |
| end_date | 2020-01-14 | 2020-01-28 | 2020-03-31 |


# shopping_cart_event_identifier

## All rows

| column | row 1 | row 2 | row 3 | row 4 | row 5 |
|---|---|---|---|---|---|
| event_type | 1 | 2 | 3 | 4 | 5 |
| event_name | Page View | Add to Cart | Purchase | Ad Impression | Ad Click |


# shopping_cart_events

```sql
CREATE TABLE "shopping_cart_events" (
"visit_id" TEXT,
  "cookie_id" TEXT,
  "page_id" INTEGER,
  "event_type" INTEGER,
  "sequence_number" INTEGER,
  "event_time" TEXT
);
```

## Rows

- total=32734

| column | latest | sample | sample |
|---|---|---|---|
| visit_id | ffeed3 | 83972a | 9f6ccc |
| cookie_id | beed13 | 4c0e26 | 9872ed |
| page_id | 2 | 12 | 8 |
| event_type | 1 | 1 | 2 |
| sequence_number | 1 | 11 | 8 |
| event_time | 2020-02-15 22:00:09.764174 | 2020-03-18 20:07:11.569516 | 2020-02-20 16:25:34.664023 |

## Columns

- visit_id: 3564 distinct
- cookie_id: 1782 distinct
- page_id: 2=4752, 9=2515, 10=2513, 11=2511, 6=2509, 3=2497, 4=2479, 8=2457, 5=2446, 7=2393, 12=2103, 1=1782, 13=1777, int 1..13
- event_type: 1=20928, 2=8451, 3=1777, 4=876, 5=702, int 1..5
- sequence_number: 23 distinct, int 1..23
  - stats: average=7.11606, median=6
- event_time: all distinct


# shopping_cart_page_hierarchy

```sql
CREATE TABLE "shopping_cart_page_hierarchy" (
"page_id" INTEGER,
  "page_name" TEXT,
  "product_category" TEXT,
  "product_id" REAL
);
```

## Rows

- total=13

| column | latest | sample | sample |
|---|---|---|---|
| page_id | 13 | 11 | 6 |
| page_name | Confirmation | Oyster | Russian Caviar |
| product_category | null | Shellfish | Luxury |
| product_id | null | 9 | 4 |

## Columns

- page_id: unique identifier, int 1..13
- page_name: "Abalone"=1, "All Products"=1, "Black Truffle"=1, "Checkout"=1, "Confirmation"=1, "Crab"=1, "Home Page"=1, "Kingfish"=1, "Lobster"=1, "Oyster"=1, "Russian Caviar"=1, "Salmon"=1, "Tuna"=1
- product_category: "Shellfish"=4, "Fish"=3, "Luxury"=2, nulls=4
- product_id: 1=1, 2=1, 3=1, 4=1, 5=1, 6=1, 7=1, 8=1, 9=1, nulls=4, num 1..9


# shopping_cart_users

```sql
CREATE TABLE "shopping_cart_users" (
"user_id" INTEGER,
  "cookie_id" TEXT,
  "start_date" TEXT
);
```

## Rows

- total=1782

| column | latest | sample | sample |
|---|---|---|---|
| user_id | 500 | 325 | 352 |
| cookie_id | f1ab70 | 89f0fd | dcb6c8 |
| start_date | 2020-02-28 | 2020-01-29 | 2020-01-13 |

## Columns

- user_id: 500 distinct, int 1..500
- cookie_id: unique identifier
- start_date: 131 distinct


# veg_cat

```sql
CREATE TABLE "veg_cat" (
"index" INTEGER,
  "item_code" INTEGER,
  "item_name" TEXT,
  "category_code" INTEGER,
  "category_name" TEXT
);
```

## Rows

- total=251

| column | latest | sample | sample |
|---|---|---|---|
| index | 250 | 102 | 59 |
| item_code | 106973990980123 | 102900011009970 | 102900011030103 |
| item_name | Hfyg Haixian Mushroom (Bunch) | Qinggengsanhua | Garden Chrysanthemum (Bag) |
| category_code | 1011010801 | 1011010201 | 1011010101 |
| category_name | Edible Mushroom | Cabbage | Flower/Leaf Vegetables |

## Columns

- index: all distinct, int 0..250
  - stats: average=125, median=125
- item_code: all distinct, int 102900005115168..106973990980123
  - stats: average=1.03191e+14, median=1.029e+14
- item_name: 247 distinct
- category_code: 1011010101=100, 1011010801=72, 1011010504=45, 1011010402=19, 1011010501=10, 1011010201=5, int 1011010101..1011010801
- category_name: "Flower/Leaf Vegetables"=100, "Edible Mushroom"=72, "Capsicum"=45, "Aquatic Tuberous Vegetables"=19, "Solanum"=10, "Cabbage"=5


# veg_loss_rate_df

```sql
CREATE TABLE "veg_loss_rate_df" (
"index" INTEGER,
  "item_code" INTEGER,
  "item_name" TEXT,
  "loss_rate_%" REAL
);
```

## Rows

- total=251

| column | latest | sample | sample |
|---|---|---|---|
| index | 250 | 9 | 13 |
| item_code | 106973990980123 | 102900005115816 | 102900005115878 |
| item_name | Hfyg Haixian Mushroom (Bunch) | Nanguajian | Garden Chrysanthemum |
| loss_rate_% | 0.12 | 13.46 | 6.27 |

## Columns

- index: all distinct, int 0..250
  - stats: average=125, median=125
- item_code: all distinct, int 102900005115168..106973990980123
  - stats: average=1.03191e+14, median=1.029e+14
- item_name: 247 distinct
- loss_rate_%: 126 distinct, num 0..29.25
  - stats: average=9.42669, median=9.43


# veg_txn_df

```sql
CREATE TABLE "veg_txn_df" (
"index" INTEGER,
  "txn_date" TEXT,
  "txn_time" TEXT,
  "item_code" INTEGER,
  "qty_sold(kg)" REAL,
  "unit_selling_px_rmb/kg" REAL,
  "sale/return" TEXT,
  "discount(%)" INTEGER,
  "day_of_week" TEXT
);
```

## Rows

- total≈878503 (estimated from db stats; row/column profiling skipped)


# veg_whsle_df

```sql
CREATE TABLE "veg_whsle_df" (
"index" INTEGER,
  "whsle_date" TEXT,
  "item_code" INTEGER,
  "whsle_px_rmb-kg" REAL
);
```

## Rows

- total=55982

| column | latest | sample | sample |
|---|---|---|---|
| index | 55981 | 38093 | 17967 |
| whsle_date | 2023-06-30 00:00:00 | 2022-07-10 00:00:00 | 2021-07-26 00:00:00 |
| item_code | 106971533450003 | 102900005116530 | 102900005115984 |
| whsle_px_rmb-kg | 1.95 | 13.6 | 3.28 |

## Columns

- index: all distinct, int 0..55981
  - stats: average=27990.5, median=27990.5
- whsle_date: 1091 distinct
- item_code: 251 distinct, int 102900005115168..106973990980123
  - stats: average=1.03045e+14, median=1.029e+14
- whsle_px_rmb-kg: 2380 distinct, num 0.01..141
  - stats: average=5.96262, median=4.63


# weekly_sales

```sql
CREATE TABLE "weekly_sales" (
"week_date" TEXT,
  "region" TEXT,
  "platform" TEXT,
  "segment" TEXT,
  "customer_type" TEXT,
  "transactions" INTEGER,
  "sales" INTEGER
);
```

## Rows

- total=17117

| column | latest | sample | sample |
|---|---|---|---|
| week_date | 9/7/18 | 30/3/20 | 26/3/18 |
| region | USA | ASIA | USA |
| platform | Shopify | Retail | Retail |
| segment | F3 | F1 | C1 |
| customer_type | New | New | Existing |
| transactions | 50 | 28970 | 47218 |
| sales | 8314 | 944706 | 2219869 |

## Columns

- week_date: 72 distinct
- region: "AFRICA"=2448, "ASIA"=2448, "CANADA"=2448, "OCEANIA"=2448, "USA"=2448, "SOUTH AMERICA"=2441, "EUROPE"=2436
- platform: "Retail"=8568, "Shopify"=8549
- segment: "C1"=2016, "C2"=2016, "C3"=2016, "F1"=2016, "F2"=2016, "F3"=2009, "C4"=2004, nulls=3024
- customer_type: "Existing"=8064, "New"=8045, "Guest"=1008
- transactions: 9307 distinct, int 1..2578158
  - stats: average=63554.3, median=1657
- sales: 16559 distinct, int 0..69763805
  - stats: average=2.3803e+06, median=196458
