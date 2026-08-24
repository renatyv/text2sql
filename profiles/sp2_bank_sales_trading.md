---
generator: db-snooper
version: 0.0.34
generated_at_utc: 2026-08-24T21:58:28.801127Z
dialect: sqlite
database: /var/folders/9j/b9bx_drd53sc6zbpsqyrjy4h0000gn/T/dbsnoop-n4g8fkl1/bank_sales_trading.sqlite
schema: main
---

# "bitcoin_members"  (rows=14)

columns:
"member_id" text: unique identifier
"first_name" text: "Abe"=1, "Alex"=1, "Ayush"=1, "Ben"=1, "Charlie"=1, "Danny"=1, "Enoch"=1, "Leah"=1, "Nandita"=1, "Pavan"=1, "Rowan"=1, "Sonia"=1, "Vikram"=1, "Vipul"=1
"region" text: "United States"=7, "Australia"=4, "Africa"=1, "Asia"=1, "India"=1

indexes: none

samples:
| column | latest | sample | sample |
|---|---|---|---|
| member_id | eccbc8 | d3d944 | e4da3b |
| first_name | Charlie | Enoch | Rowan |
| region | United States | Africa | United States |

# "bitcoin_prices"  (rows=3404)

columns:
"ticker" text: "BTC"=1702, "ETH"=1702
"market_date" text: 1702 distinct
"price" float: 3362 distinct, 8.2..63540.9, avg=6645.43, median=1961.73
"open" float: 3347 distinct, 8.17..63544.2, avg=6630.64, median=1948.01
"high" float: 3351 distinct, 8.5..64778, avg=6836.06, median=2036.43
"low" float: 3358 distinct, 8.03..62067.5, avg=6403.45, median=1871.95
"volume" text: 2811 distinct
"change" text: 1496 distinct

indexes: none

samples:
| column | latest | sample | sample |
|---|---|---|---|
| ticker | ETH | ETH | BTC |
| market_date | 31-12-2020 | 16-03-2017 | 21-08-2017 |
| price | 735.94 | 45.07 | 4005.1 |
| open | 751.92 | 34.8 | 4066.6 |
| high | 755.13 | 46.21 | 4097.3 |
| low | 724.67 | 34.8 | 3966.9 |
| volume | 1.04M | 3.06M | 90.65K |
| change | -2.11% | 29.51% | -1.51% |

# "bitcoin_transactions"  (rows=22918)

columns:
"txn_id" int: unique identifier, 1..22918
"member_id" text: "c4ca42"=2161, "a87ff6"=1947, "aab323"=1909, "c81e72"=1833, "c20ad4"=1724, "45c48c"=1697, "6512bd"=1688, "c9f0f8"=1572, "d3d944"=1526, "e4da3b"=1448, "8f14e4"=1405, "c51ce4"=1400, "167909"=1341, "eccbc8"=1267
"ticker" text: "BTC"=12484, "ETH"=10434
"txn_date" text: 1700 distinct
"txn_type" text: "BUY"=18881, "SELL"=4037
"quantity" float: 22891 distinct, 0.000711769..50, avg=5.06366, median=5.03259
"percentage_fee" float: 31 distinct, 0..0.3, avg=0.255142, median=0.3
"txn_time" text: iso-date, 22891 distinct

indexes: none

samples:
| column | latest | sample | sample |
|---|---|---|---|
| txn_id | 22918 | 10524 | 12961 |
| member_id | d3d944 | c4ca42 | e4da3b |
| ticker | BTC | BTC | ETH |
| txn_date | 27-08-2021 | 27-02-2019 | 31-08-2019 |
| txn_type | BUY | BUY | SELL |
| quantity | 7.22216 | 7.1647 | 4.99077 |
| percentage_fee | 0.01 | 0.3 | 0.08 |
| txn_time | 2021-08-27T22:26:10.258Z | 2019-02-27T19:00:45.070Z | 2019-08-31T16:08:56.319Z |

# "cleaned_weekly_sales"  (rows=17117)

columns:
"week_date_formatted" text: 72 distinct
"week_date" text: iso-date, 72 distinct
"region" text: "AFRICA"=2448, "ASIA"=2448, "CANADA"=2448, "OCEANIA"=2448, "USA"=2448, "SOUTH AMERICA"=2441, "EUROPE"=2436
"platform" text: "Retail"=8568, "Shopify"=8549
"segment" text: "unknown"=3024, "C1"=2016, "C2"=2016, "C3"=2016, "F1"=2016, "F2"=2016, "F3"=2009, "C4"=2004
"customer_type" text: "Existing"=8064, "New"=8045, "Guest"=1008
"transactions" int: 9307 distinct, 1..2578158, avg=63554.3, median=1657
"sales" int: 16559 distinct, 0..69763805, avg=2.4e+06, median=196458
"week_number" int: 24 distinct, 13..36, avg=24.4996, median=25
"month_number" int: 7=3330, 4=3327, 6=3093, 8=3089, 5=2853, 3=951, 9=474, 3..9
"calendar_year" int: 2020=5711, 2019=5708, 2018=5698, 2018..2020
"age_band" text: "Retirees"=6029, "Middle Aged"=4032, "Young Adults"=4032, "unknown"=3024
"demographic" text: "Couples"=8052, "Families"=6041, "unknown"=3024
"avg_transaction" float: 9539 distinct, 0..880.33, avg=110.955, median=67.18

indexes: none

samples:
| column | latest | sample | sample |
|---|---|---|---|
| week_date_formatted | 2020-8-31 | 2019-6-3 | 2019-6-24 |
| week_date | 2020-08-31 | 2019-06-03 | 2019-06-24 |
| region | USA | SOUTH AMERICA | EUROPE |
| platform | Shopify | Retail | Retail |
| segment | unknown | C3 | F1 |
| customer_type | New | New | New |
| transactions | 154 | 775 | 939 |
| sales | 25762 | 30023 | 38925 |
| week_number | 36 | 23 | 26 |
| month_number | 8 | 6 | 6 |
| calendar_year | 2020 | 2019 | 2019 |
| age_band | unknown | Retirees | Young Adults |
| demographic | unknown | Couples | Families |
| avg_transaction | 167.29 | 38.74 | 41.45 |

# "customer_nodes"  (rows=3500)

columns:
"customer_id" int: 500 distinct, 1..500
"region_id" int: 1=770, 2=735, 3=714, 4=665, 5=616, 1..5
"node_id" int: 1=728, 5=707, 4=704, 3=699, 2=662, 1..5
"start_date" text: iso-date, 161 distinct
"end_date" text: iso-date, 160 distinct

indexes: none

samples:
| column | latest | sample | sample |
|---|---|---|---|
| customer_id | 500 | 400 | 466 |
| region_id | 2 | 4 | 1 |
| node_id | 5 | 5 | 4 |
| start_date | 2020-03-13 | 2020-03-12 | 2020-02-09 |
| end_date | 2020-03-18 | 2020-03-28 | 2020-03-02 |

# "customer_regions"  (rows=5)

columns:
"region_id" int
"region_name" text

indexes: none

all rows:
| column | row 1 | row 2 | row 3 | row 4 | row 5 |
|---|---|---|---|---|---|
| region_id | 1 | 2 | 3 | 4 | 5 |
| region_name | Australia | America | Africa | Asia | Europe |

# "customer_transactions"  (rows=5868)

columns:
"customer_id" int: 500 distinct, 1..500
"txn_date" text: iso-date, 119 distinct
"txn_type" text: "deposit"=2671, "purchase"=1617, "withdrawal"=1580
"txn_amount" int: 999 distinct, 0..1000, avg=504.211, median=503

indexes: none

samples:
| column | latest | sample | sample |
|---|---|---|---|
| customer_id | 500 | 344 | 457 |
| txn_date | 2020-03-25 | 2020-02-29 | 2020-02-12 |
| txn_type | deposit | deposit | deposit |
| txn_amount | 825 | 90 | 300 |

# "interest_map"  (rows=1209)

columns:
"id" int: unique identifier, 1..51678
"interest_name" text: 1208 distinct
"interest_summary" text: 1188 distinct, nulls=20
"created_at" text: iso-date, 302 distinct
"last_modified" text: iso-date, 256 distinct

indexes: none

samples:
| column | latest | sample | sample |
|---|---|---|---|
| id | 51678 | 22424 | 85 |
| interest_name | Plumbers | Cosplay Enthusiasts | Online Movie Downloaders |
| interest_summary | Professionals reading industry news and researching products and services for plumbers. | People researching cosplay events and activities and purchasing costumes. | Consumers downloading feature length movies and TV shows. |
| created_at | 2019-05-06 22:00:00 | 2018-06-21 14:15:06 | 2016-05-26 14:57:59 |
| last_modified | 2019-05-07 18:50:04 | 2018-06-21 14:15:06 | 2018-05-23 11:30:13 |

# "interest_metrics"  (rows=14273)

columns:
"_month" float: 8=1916, 7=1593, 3=1136, 2=1121, 4=1099, 12=995, 1=973, 11=928, 5=857, 10=857, 6=824, 9=780, nulls=1194, 1..12
"_year" float: 2019=8023, 2018=5056, nulls=1194
"month_year" text: "08-2019"=1149, "03-2019"=1136, "02-2019"=1121, "04-2019"=1099, "12-2018"=995, "01-2019"=973, "11-2018"=928, "07-2019"=864, "05-2019"=857, "10-2018"=857, "06-2019"=824, "09-2018"=780, "08-2018"=767, "07-2018"=729, nulls=1194
"interest_id" float: 1202 distinct, nulls=1193, 1..51678
"composition" float: 884 distinct, 1.51..21.2, avg=3.3376, median=2.86
"index_value" float: 345 distinct, 0.44..6.19, avg=1.53515, median=1.45
"ranking" int: 998 distinct, 1..1194, avg=484.332, median=470
"percentile_ranking" float: 2301 distinct, 0..99.92, avg=50.3404, median=50.46

indexes: none

samples:
| column | latest | sample | sample |
|---|---|---|---|
| _month | 12 | 8 | 5 |
| _year | 2018 | 2019 | 2019 |
| month_year | 12-2018 | 08-2019 | 05-2019 |
| interest_id | 42239 | 19595 | 6221 |
| composition | 1.74 | 2.11 | 1.65 |
| index_value | 1.39 | 0.98 | 1.22 |
| ranking | 523 | 1120 | 754 |
| percentile_ranking | 47.44 | 2.52 | 12.02 |

# "shopping_cart_campaign_identifier"  (rows=3)

columns:
"campaign_id" int
"products" text
"campaign_name" text
"start_date" text
"end_date" text

indexes: none

all rows:
| column | row 1 | row 2 | row 3 |
|---|---|---|---|
| campaign_id | 1 | 2 | 3 |
| products | 1-3 | 4-5 | 6-8 |
| campaign_name | BOGOF - Fishing For Compliments | 25% Off - Living The Lux Life | Half Off - Treat Your Shellf(ish) |
| start_date | 2020-01-01 | 2020-01-15 | 2020-02-01 |
| end_date | 2020-01-14 | 2020-01-28 | 2020-03-31 |

# "shopping_cart_event_identifier"  (rows=5)

columns:
"event_type" int
"event_name" text

indexes: none

all rows:
| column | row 1 | row 2 | row 3 | row 4 | row 5 |
|---|---|---|---|---|---|
| event_type | 1 | 2 | 3 | 4 | 5 |
| event_name | Page View | Add to Cart | Purchase | Ad Impression | Ad Click |

# "shopping_cart_events"  (rows=32734)

columns:
"visit_id" text: 3564 distinct
"cookie_id" text: 1782 distinct
"page_id" int: 2=4752, 9=2515, 10=2513, 11=2511, 6=2509, 3=2497, 4=2479, 8=2457, 5=2446, 7=2393, 12=2103, 1=1782, 13=1777, 1..13
"event_type" int: 1=20928, 2=8451, 3=1777, 4=876, 5=702, 1..5
"sequence_number" int: 23 distinct, 1..23, avg=7.11606, median=6
"event_time" text: iso-date, all distinct

indexes: none

samples:
| column | latest | sample | sample |
|---|---|---|---|
| visit_id | ffeed3 | a10c2c | 0d8e27 |
| cookie_id | beed13 | 81e6ff | 8c3236 |
| page_id | 2 | 12 | 8 |
| event_type | 1 | 1 | 1 |
| sequence_number | 1 | 17 | 10 |
| event_time | 2020-02-15 22:00:09.764174 | 2020-02-22 13:39:39.340224 | 2020-03-16 17:47:29.717291 |

# "shopping_cart_page_hierarchy"  (rows=13)

columns:
"page_id" int: unique identifier, 1..13
"page_name" text: "Abalone"=1, "All Products"=1, "Black Truffle"=1, "Checkout"=1, "Confirmation"=1, "Crab"=1, "Home Page"=1, "Kingfish"=1, "Lobster"=1, "Oyster"=1, "Russian Caviar"=1, "Salmon"=1, "Tuna"=1
"product_category" text: "Shellfish"=4, "Fish"=3, "Luxury"=2, nulls=4
"product_id" float: 1=1, 2=1, 3=1, 4=1, 5=1, 6=1, 7=1, 8=1, 9=1, nulls=4, 1..9

indexes: none

samples:
| column | latest | sample | sample |
|---|---|---|---|
| page_id | 13 | 3 | 10 |
| page_name | Confirmation | Salmon | Crab |
| product_category | null | Fish | Shellfish |
| product_id | null | 1 | 8 |

# "shopping_cart_users"  (rows=1782)

columns:
"user_id" int: 500 distinct, 1..500
"cookie_id" text: unique identifier
"start_date" text: iso-date, 131 distinct

indexes: none

samples:
| column | latest | sample | sample |
|---|---|---|---|
| user_id | 500 | 313 | 249 |
| cookie_id | f1ab70 | 061fca | 077e29 |
| start_date | 2020-02-28 | 2020-03-05 | 2020-01-28 |

# "veg_cat"  (rows=251)

columns:
"index" int: all distinct, 0..250, avg=125, median=125
"item_code" int: all distinct, 102900005115168..106973990980123
"item_name" text: 247 distinct
"category_code" int: 1011010101=100, 1011010801=72, 1011010504=45, 1011010402=19, 1011010501=10, 1011010201=5, 1011010101..1011010801
"category_name" text: "Flower/Leaf Vegetables"=100, "Edible Mushroom"=72, "Capsicum"=45, "Aquatic Tuberous Vegetables"=19, "Solanum"=10, "Cabbage"=5

indexes: none

samples:
| column | latest | sample | sample |
|---|---|---|---|
| index | 250 | 168 | 207 |
| item_code | 106973990980123 | 102900011032244 | 102900011026793 |
| item_name | Hfyg Haixian Mushroom (Bunch) | Red Hot Peppers (Bag) | Apricot Bao Mushroom (250 G) |
| category_code | 1011010801 | 1011010504 | 1011010801 |
| category_name | Edible Mushroom | Capsicum | Edible Mushroom |

# "veg_loss_rate_df"  (rows=251)

columns:
"index" int: all distinct, 0..250, avg=125, median=125
"item_code" int: all distinct, 102900005115168..106973990980123
"item_name" text: 247 distinct
"loss_rate_%" float: 126 distinct, 0..29.25, avg=9.42669, median=9.43

indexes: none

samples:
| column | latest | sample | sample |
|---|---|---|---|
| index | 250 | 232 | 227 |
| item_code | 106973990980123 | 102900051010790 | 102900051004294 |
| item_name | Hfyg Haixian Mushroom (Bunch) | Purple Beicai | Green Line Pepper |
| loss_rate_% | 0.12 | 19.58 | 7.8 |

# "veg_txn_df"  (rows=≈878503)

columns:
"index" int
"txn_date" text
"txn_time" text
"item_code" int
"qty_sold(kg)" float
"unit_selling_px_rmb/kg" float
"sale/return" text
"discount(%)" int
"day_of_week" text

indexes: none


# "veg_whsle_df"  (rows=55982)

columns:
"index" int: all distinct, 0..55981, avg=27990.5, median=27990.5
"whsle_date" text: iso-date, 1091 distinct
"item_code" int: 251 distinct, 102900005115168..106973990980123
"whsle_px_rmb-kg" float: 2380 distinct, 0.01..141, avg=5.96262, median=4.63

indexes: none

samples:
| column | latest | sample | sample |
|---|---|---|---|
| index | 55981 | 29300 | 7029 |
| whsle_date | 2023-06-30 00:00:00 | 2022-02-14 00:00:00 | 2020-12-12 00:00:00 |
| item_code | 106971533450003 | 102900005116530 | 102900005116530 |
| whsle_px_rmb-kg | 1.95 | 11.35 | 12 |

# "weekly_sales"  (rows=17117)

columns:
"week_date" text: 72 distinct
"region" text: "AFRICA"=2448, "ASIA"=2448, "CANADA"=2448, "OCEANIA"=2448, "USA"=2448, "SOUTH AMERICA"=2441, "EUROPE"=2436
"platform" text: "Retail"=8568, "Shopify"=8549
"segment" text: "C1"=2016, "C2"=2016, "C3"=2016, "F1"=2016, "F2"=2016, "F3"=2009, "C4"=2004, nulls=3024
"customer_type" text: "Existing"=8064, "New"=8045, "Guest"=1008
"transactions" int: 9307 distinct, 1..2578158, avg=63554.3, median=1657
"sales" int: 16559 distinct, 0..69763805, avg=2.4e+06, median=196458

indexes: none

samples:
| column | latest | sample | sample |
|---|---|---|---|
| week_date | 9/7/18 | 25/5/20 | 8/4/19 |
| region | USA | SOUTH AMERICA | CANADA |
| platform | Shopify | Retail | Retail |
| segment | F3 | C1 | C4 |
| customer_type | New | Existing | New |
| transactions | 50 | 2841 | 11386 |
| sales | 8314 | 78053 | 445194 |
