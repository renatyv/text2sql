---
generator: db-snooper
version: 0.0.31
generated_at_utc: 2026-08-20T17:28:11.556511Z
dialect: sqlite
database: /var/folders/9j/b9bx_drd53sc6zbpsqyrjy4h0000gn/T/dbsnoop-00pauh5q/bank_sales_trading.sqlite
schema: main
---

# "bitcoin_members"  (rows=14)

columns:
"member_id" text: unique identifier
"first_name" text: "Abe"=1, "Alex"=1, "Ayush"=1, "Ben"=1, "Charlie"=1, "Danny"=1, "Enoch"=1, "Leah"=1, "Nandita"=1, "Pavan"=1, "Rowan"=1, "Sonia"=1, "Vikram"=1, "Vipul"=1
"region" text: "United States"=7, "Australia"=4, "Africa"=1, "Asia"=1, "India"=1

indexes: none
fk: none

samples:
| column | latest | sample | sample |
|---|---|---|---|
| member_id | eccbc8 | 8f14e4 | e4da3b |
| first_name | Charlie | Alex | Rowan |
| region | United States | United States | United States |

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
fk: none

samples:
| column | latest | sample | sample |
|---|---|---|---|
| ticker | ETH | ETH | ETH |
| market_date | 31-12-2020 | 25-04-2017 | 16-04-2020 |
| price | 735.94 | 53.9 | 172.31 |
| open | 751.92 | 53.54 | 152.9 |
| high | 755.13 | 54.21 | 174.28 |
| low | 724.67 | 53.25 | 148.91 |
| volume | 1.04M | 97.44K | 32.99M |
| change | -2.11% | 0.67% | 12.69% |

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
fk: none

samples:
| column | latest | sample | sample |
|---|---|---|---|
| txn_id | 22918 | 18524 | 11548 |
| member_id | d3d944 | 6512bd | d3d944 |
| ticker | BTC | BTC | ETH |
| txn_date | 27-08-2021 | 05-10-2020 | 15-05-2019 |
| txn_type | BUY | BUY | BUY |
| quantity | 7.22216 | 9.56706 | 0.928699 |
| percentage_fee | 0.01 | 0.3 | 0.06 |
| txn_time | 2021-08-27T22:26:10.258Z | 2020-10-05T08:38:36.030Z | 2019-05-15T21:10:33.339Z |

# "cleaned_weekly_sales"  (rows=17117)

columns:
"week_date_formatted" text: 72 distinct
"week_date" text: iso-date, 72 distinct
"region" text: "AFRICA"=2448, "ASIA"=2448, "CANADA"=2448, "OCEANIA"=2448, "USA"=2448, "SOUTH AMERICA"=2441, "EUROPE"=2436
"platform" text: "Retail"=8568, "Shopify"=8549
"segment" text: "unknown"=3024, "C1"=2016, "C2"=2016, "C3"=2016, "F1"=2016, "F2"=2016, "F3"=2009, "C4"=2004
"customer_type" text: "Existing"=8064, "New"=8045, "Guest"=1008
"transactions" int: 9307 distinct, 1..2578158, avg=63554.3, median=1657
"sales" int: 16559 distinct, 0..69763805, avg=2.3803e+06, median=196458
"week_number" int: 24 distinct, 13..36, avg=24.4996, median=25
"month_number" int: 7=3330, 4=3327, 6=3093, 8=3089, 5=2853, 3=951, 9=474, 3..9
"calendar_year" int: 2020=5711, 2019=5708, 2018=5698, 2018..2020
"age_band" text: "Retirees"=6029, "Middle Aged"=4032, "Young Adults"=4032, "unknown"=3024
"demographic" text: "Couples"=8052, "Families"=6041, "unknown"=3024
"avg_transaction" float: 9539 distinct, 0..880.33, avg=110.955, median=67.18

indexes: none
fk: none

samples:
| column | latest | sample | sample |
|---|---|---|---|
| week_date_formatted | 2020-8-31 | 2020-5-11 | 2018-6-25 |
| week_date | 2020-08-31 | 2020-05-11 | 2018-06-25 |
| region | USA | USA | CANADA |
| platform | Shopify | Retail | Shopify |
| segment | unknown | F2 | C1 |
| customer_type | New | Existing | New |
| transactions | 154 | 98067 | 56 |
| sales | 25762 | 5720394 | 7479 |
| week_number | 36 | 20 | 26 |
| month_number | 8 | 5 | 6 |
| calendar_year | 2020 | 2020 | 2018 |
| age_band | unknown | Middle Aged | Young Adults |
| demographic | unknown | Families | Couples |
| avg_transaction | 167.29 | 58.33 | 133.55 |

# "customer_nodes"  (rows=3500)

columns:
"customer_id" int: 500 distinct, 1..500
"region_id" int: 1=770, 2=735, 3=714, 4=665, 5=616, 1..5
"node_id" int: 1=728, 5=707, 4=704, 3=699, 2=662, 1..5
"start_date" text: iso-date, 161 distinct
"end_date" text: iso-date, 160 distinct

indexes: none
fk: none

samples:
| column | latest | sample | sample |
|---|---|---|---|
| customer_id | 500 | 342 | 146 |
| region_id | 2 | 1 | 1 |
| node_id | 5 | 5 | 4 |
| start_date | 2020-03-13 | 2020-01-27 | 2020-01-25 |
| end_date | 2020-03-18 | 2020-02-12 | 2020-02-18 |

# "customer_regions"  (rows=5)

columns:
"region_id" int: unique identifier, 1..5
"region_name" text: "Africa"=1, "America"=1, "Asia"=1, "Australia"=1, "Europe"=1

indexes: none
fk: none

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
fk: none

samples:
| column | latest | sample | sample |
|---|---|---|---|
| customer_id | 500 | 327 | 6 |
| txn_date | 2020-03-25 | 2020-03-22 | 2020-02-24 |
| txn_type | deposit | purchase | deposit |
| txn_amount | 825 | 562 | 240 |

# "interest_map"  (rows=1209)

columns:
"id" int: unique identifier, 1..51678
"interest_name" text: 1208 distinct
"interest_summary" text: 1188 distinct, nulls=20
"created_at" text: iso-date, 302 distinct
"last_modified" text: iso-date, 256 distinct

indexes: none
fk: none

samples:
| column | latest | sample | sample |
|---|---|---|---|
| id | 51678 | 35953 | 17271 |
| interest_name | Plumbers | Kitchen and Bath Professionals | Car Collector Enthusiasts |
| interest_summary | Professionals reading industry news and researching products and services for plumbers. | Professionals reading industry news and researching products and services for kitchen and bathroom construction and design. | People reading news on the collector car market.  |
| created_at | 2019-05-06 22:00:00 | 2018-09-06 16:55:03 | 2018-02-27 14:15:03 |
| last_modified | 2019-05-07 18:50:04 | 2018-09-06 16:55:03 | 2018-05-23 16:19:12 |

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
fk: none

samples:
| column | latest | sample | sample |
|---|---|---|---|
| _month | 12 | 6 | null |
| _year | 2018 | 2019 | null |
| month_year | 12-2018 | 06-2019 | null |
| interest_id | 42239 | 44383 | null |
| composition | 1.74 | 1.79 | 4.07 |
| index_value | 1.39 | 1.48 | 1.7 |
| ranking | 523 | 711 | 677 |
| percentile_ranking | 47.44 | 13.71 | 43.3 |

# "shopping_cart_campaign_identifier"  (rows=3)

columns:
"campaign_id" int: unique identifier, 1..3
"products" text: "1-3"=1, "4-5"=1, "6-8"=1
"campaign_name" text: "25% Off - Living The Lux Life"=1, "BOGOF - Fishing For Compliments"=1, "Half Off - Treat Your Shellf(ish)"=1
"start_date" text: "2020-01-01"=1, "2020-01-15"=1, "2020-02-01"=1
"end_date" text: "2020-01-14"=1, "2020-01-28"=1, "2020-03-31"=1

indexes: none
fk: none

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
"event_type" int: 1=1, 2=1, 3=1, 4=1, 5=1, 1..5
"event_name" text: "Ad Click"=1, "Ad Impression"=1, "Add to Cart"=1, "Page View"=1, "Purchase"=1

indexes: none
fk: none

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
fk: none

samples:
| column | latest | sample | sample |
|---|---|---|---|
| visit_id | ffeed3 | 6b2867 | 198e9a |
| cookie_id | beed13 | dbe2d6 | 67c175 |
| page_id | 2 | 2 | 6 |
| event_type | 1 | 1 | 1 |
| sequence_number | 1 | 1 | 6 |
| event_time | 2020-02-15 22:00:09.764174 | 2020-02-24 17:08:20.339934 | 2020-03-13 00:44:17.571736 |

# "shopping_cart_page_hierarchy"  (rows=13)

columns:
"page_id" int: unique identifier, 1..13
"page_name" text: "Abalone"=1, "All Products"=1, "Black Truffle"=1, "Checkout"=1, "Confirmation"=1, "Crab"=1, "Home Page"=1, "Kingfish"=1, "Lobster"=1, "Oyster"=1, "Russian Caviar"=1, "Salmon"=1, "Tuna"=1
"product_category" text: "Shellfish"=4, "Fish"=3, "Luxury"=2, nulls=4
"product_id" float: 1=1, 2=1, 3=1, 4=1, 5=1, 6=1, 7=1, 8=1, 9=1, nulls=4, 1..9

indexes: none
fk: none

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
fk: none

samples:
| column | latest | sample | sample |
|---|---|---|---|
| user_id | 500 | 147 | 260 |
| cookie_id | f1ab70 | 8d5e95 | a4f236 |
| start_date | 2020-02-28 | 2020-02-05 | 2020-01-08 |

# "veg_cat"  (rows=251)

columns:
"index" int: all distinct, 0..250, avg=125, median=125
"item_code" int: all distinct, 102900005115168..106973990980123, avg=1.03191e+14, median=1.029e+14
"item_name" text: 247 distinct
"category_code" int: 1011010101=100, 1011010801=72, 1011010504=45, 1011010402=19, 1011010501=10, 1011010201=5, 1011010101..1011010801
"category_name" text: "Flower/Leaf Vegetables"=100, "Edible Mushroom"=72, "Capsicum"=45, "Aquatic Tuberous Vegetables"=19, "Solanum"=10, "Cabbage"=5

indexes: none
fk: none

samples:
| column | latest | sample | sample |
|---|---|---|---|
| index | 250 | 8 | 58 |
| item_code | 106973990980123 | 102900005115816 | 102900011030097 |
| item_name | Hfyg Haixian Mushroom (Bunch) | Nanguajian | Yunnan Leaf Lettuce (Bag) |
| category_code | 1011010801 | 1011010101 | 1011010101 |
| category_name | Edible Mushroom | Flower/Leaf Vegetables | Flower/Leaf Vegetables |

# "veg_loss_rate_df"  (rows=251)

columns:
"index" int: all distinct, 0..250, avg=125, median=125
"item_code" int: all distinct, 102900005115168..106973990980123, avg=1.03191e+14, median=1.029e+14
"item_name" text: 247 distinct
"loss_rate_%" float: 126 distinct, 0..29.25, avg=9.42669, median=9.43

indexes: none
fk: none

samples:
| column | latest | sample | sample |
|---|---|---|---|
| index | 250 | 235 | 206 |
| item_code | 106973990980123 | 106931885000035 | 102900011034354 |
| item_name | Hfyg Haixian Mushroom (Bunch) | Embroidered Aureus | Xianzongye (Bag) (1) |
| loss_rate_% | 0.12 | 11.13 | 0 |

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
fk: none


# "veg_whsle_df"  (rows=55982)

columns:
"index" int: all distinct, 0..55981, avg=27990.5, median=27990.5
"whsle_date" text: iso-date, 1091 distinct
"item_code" int: 251 distinct, 102900005115168..106973990980123, avg=1.03045e+14, median=1.029e+14
"whsle_px_rmb-kg" float: 2380 distinct, 0.01..141, avg=5.96262, median=4.63

indexes: none
fk: none

samples:
| column | latest | sample | sample |
|---|---|---|---|
| index | 55981 | 27029 | 14945 |
| whsle_date | 2023-06-30 00:00:00 | 2022-01-07 00:00:00 | 2021-05-26 00:00:00 |
| item_code | 106971533450003 | 102900005116219 | 102900011009444 |
| whsle_px_rmb-kg | 1.95 | 13.28 | 4.48 |

# "weekly_sales"  (rows=17117)

columns:
"week_date" text: 72 distinct
"region" text: "AFRICA"=2448, "ASIA"=2448, "CANADA"=2448, "OCEANIA"=2448, "USA"=2448, "SOUTH AMERICA"=2441, "EUROPE"=2436
"platform" text: "Retail"=8568, "Shopify"=8549
"segment" text: "C1"=2016, "C2"=2016, "C3"=2016, "F1"=2016, "F2"=2016, "F3"=2009, "C4"=2004, nulls=3024
"customer_type" text: "Existing"=8064, "New"=8045, "Guest"=1008
"transactions" int: 9307 distinct, 1..2578158, avg=63554.3, median=1657
"sales" int: 16559 distinct, 0..69763805, avg=2.3803e+06, median=196458

indexes: none
fk: none

samples:
| column | latest | sample | sample |
|---|---|---|---|
| week_date | 9/7/18 | 22/7/19 | 31/8/20 |
| region | USA | EUROPE | EUROPE |
| platform | Shopify | Shopify | Shopify |
| segment | F3 | C2 | F1 |
| customer_type | New | Existing | Existing |
| transactions | 50 | 142 | 138 |
| sales | 8314 | 32462 | 30015 |
