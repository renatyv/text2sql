---
generator: db-snooper
version: 0.0.34
generated_at_utc: 2026-08-24T21:23:56.548646Z
dialect: sqlite
database: /var/folders/9j/b9bx_drd53sc6zbpsqyrjy4h0000gn/T/dbsnoop-4l6qfvi8/modern_data.sqlite
schema: main
---

# "companies_dates"  (rows=1085)

columns:
"company_id" int: 1074 distinct, 0..1073
"date_joined" text: iso-date, 639 distinct
"year_founded" int: 35 distinct, 1919..2021, avg=2012.88, median=2014

indexes: none

samples:
| column | latest | sample | sample |
|---|---|---|---|
| company_id | 1073 | 345 | 591 |
| date_joined | 2020-09-16T00:00:00.000 | 2021-04-14T00:00:00.000 | 2021-09-16T00:00:00.000 |
| year_founded | 2014 | 2015 | 2016 |

# "companies_funding"  (rows=1085)

columns:
"company_id" int: 1074 distinct, 0..1073
"valuation" int: 30 distinct, 1000000000..180000000000, avg=3.4e+09, median=2e+09
"funding" int: 538 distinct, 0..14000000000, avg=5.5e+08, median=3.6e+08
"select_investors" text: 1058 distinct, nulls=1

indexes: none

samples:
| column | latest | sample | sample |
|---|---|---|---|
| company_id | 1073 | 947 | 92 |
| valuation | 1000000000 | 1000000000 | 7000000000 |
| funding | 620000000 | 0 | 844000000 |
| select_investors | "Novator Partners, True, Causeway Media Partners" | "Berkshire Partners, Norwest Venture Partners" | "Bessemer Venture Partners, Qualcomm Ventures, Kleiner Perkins Caufield & Byers" |

# "companies_industries"  (rows=1085)

columns:
"company_id" int: 1074 distinct, 0..1073
"industry" text: "Fintech"=230, "Internet software & services"=208, "E-commerce & direct-to-consumer"=113, "Artificial intelligence"=84, "Health"=74, "Other"=58, ""Supply chain, logistics, & delivery""=57, "Cybersecurity"=50, "Data management & analytics"=41, "Mobile & telecommunications"=38, "Hardware"=34, "Auto & transportation"=31, "Edtech"=28, "Consumer & retail"=25, "Travel"=14

indexes: none

samples:
| column | latest | sample | sample |
|---|---|---|---|
| company_id | 1073 | 285 | 835 |
| industry | E-commerce & direct-to-consumer | Auto & transportation | Mobile & telecommunications |

# "income_trees"  (rows=220)

columns:
"zipcode" int: 216 distinct, 10001..11697, avg=10763.8, median=11002
"Estimate_Total" int: 185 distinct, 0..43456, avg=14736.1, median=13775.5
"Margin_of_Error_Total" int: 153 distinct, 11..1181, avg=347.055, median=353
"Estimate_Median_income" int: 184 distinct, 0..193510, avg=54439.9, median=53427
"Margin_of_Error_Median_income" int: 180 distinct, 0..41091, avg=4334.21, median=3228.5
"Estimate_Mean_income" int: 185 distinct, 0..441278, avg=79260.9, median=72082
"Margin_of_Error_Mean_income" int: 182 distinct, 0..56347, avg=5755.62, median=3569

indexes: none

samples:
| column | latest | sample | sample |
|---|---|---|---|
| zipcode | 11697 | 10013 | 10169 |
| Estimate_Total | 1520 | 11558 | 0 |
| Margin_of_Error_Total | 139 | 507 | 11 |
| Estimate_Median_income | 93333 | 96667 | 0 |
| Margin_of_Error_Median_income | 21346 | 17159 | 0 |
| Estimate_Mean_income | 109500 | 242875 | 0 |
| Margin_of_Error_Mean_income | 11505 | 27704 | 0 |

# "pizza_clean_customer_orders"  (rows=14)

columns:
"order_id" int: 4=3, 3=2, 10=2, 1=1, 2=1, 5=1, 6=1, 7=1, 8=1, 9=1, 1..10
"customer_id" int: 103=4, 101=3, 102=3, 104=3, 105=1, 101..105
"pizza_id" int: 1=10, 2=4
"exclusions" text: "4"=4, "2,6"=1, nulls=9
"extras" text: "1"=2, "1,4"=1, "1,5"=1, nulls=10
"order_time" text: "2021-01-04 13:23:46"=3, "2021-01-02 23:51:23"=2, "2021-01-11 18:34:49"=2, "2021-01-01 18:05:02"=1, "2021-01-01 19:00:52"=1, "2021-01-08 21:00:29"=1, "2021-01-08 21:03:13"=1, "2021-01-08 21:20:29"=1, "2021-01-09 23:54:33"=1, "2021-01-10 11:22:59"=1

indexes: none

samples:
| column | latest | sample | sample |
|---|---|---|---|
| order_id | 10 | 10 | 3 |
| customer_id | 104 | 104 | 102 |
| pizza_id | 1 | 1 | 2 |
| exclusions | 2,6 | null | null |
| extras | 1,4 | null | null |
| order_time | 2021-01-11 18:34:49 | 2021-01-11 18:34:49 | 2021-01-02 23:51:23 |

# "pizza_clean_runner_orders"  (rows=10)

columns:
"order_id" int
"runner_id" int
"pickup_time" text
"distance" float
"duration" float
"cancellation" text

indexes: none

all rows:
| column | row 1 | row 2 | row 3 | row 4 | row 5 | row 6 | row 7 | row 8 | row 9 | row 10 |
|---|---|---|---|---|---|---|---|---|---|---|
| order_id | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9 | 10 |
| runner_id | 1 | 1 | 1 | 2 | 3 | 3 | 2 | 2 | 2 | 1 |
| pickup_time | 2021-01-01 18:15:34 | 2021-01-01 19:10:54 | 2021-01-03 00:12:37 | 2021-01-04 13:53:03 | 2021-01-08 21:10:57 | null | 2021-01-08 21:30:45 | 2021-01-10 00:15:02 | null | 2021-01-11 18:50:20 |
| distance | 20 | 20 | 13.4 | 23.4 | 10 | 0 | 25 | 23.4 | 0 | 10 |
| duration | 32 | 27 | 20 | 40 | 15 | 0 | 25 | 15 | 0 | 10 |
| cancellation | null | null | null | null | null | Restaurant Cancellation | null | null | Customer Cancellation | null |

# "pizza_customer_orders"  (rows=14)

columns:
"order_id" int: 4=3, 3=2, 10=2, 1=1, 2=1, 5=1, 6=1, 7=1, 8=1, 9=1, 1..10
"customer_id" int: 103=4, 101=3, 102=3, 104=3, 105=1, 101..105
"pizza_id" int: 1=10, 2=4
"exclusions" text: "4"=4, "2,6"=1, nulls=9
"extras" text: "1"=2, "1,4"=1, "1,5"=1, nulls=10
"order_time" text: "2021-01-04 13:23:46"=3, "2021-01-02 23:51:23"=2, "2021-01-11 18:34:49"=2, "2021-01-01 18:05:02"=1, "2021-01-01 19:00:52"=1, "2021-01-08 21:00:29"=1, "2021-01-08 21:03:13"=1, "2021-01-08 21:20:29"=1, "2021-01-09 23:54:33"=1, "2021-01-10 11:22:59"=1

indexes: none

samples:
| column | latest | sample | sample |
|---|---|---|---|
| order_id | 10 | 8 | 3 |
| customer_id | 104 | 102 | 102 |
| pizza_id | 1 | 1 | 1 |
| exclusions | 2,6 | null | null |
| extras | 1,4 | null | null |
| order_time | 2021-01-11 18:34:49 | 2021-01-09 23:54:33 | 2021-01-02 23:51:23 |

# "pizza_get_exclusions"  (rows=4)

columns:
"row_id" int
"order_id" int
"exclusions" int
"total_exclusions" int

indexes: none

all rows:
| column | row 1 | row 2 | row 3 | row 4 |
|---|---|---|---|---|
| row_id | 1 | 1 | 1 | 2 |
| order_id | 4 | 9 | 10 | 10 |
| exclusions | 4 | 4 | 2 | 6 |
| total_exclusions | 3 | 1 | 2 | 2 |

# "pizza_get_extras"  (rows=6)

columns:
"row_id" int
"order_id" int
"extras" int
"extras_count" int

indexes: none

all rows:
| column | row 1 | row 2 | row 3 | row 4 | row 5 | row 6 |
|---|---|---|---|---|---|---|
| row_id | 1 | 1 | 1 | 1 | 2 | 2 |
| order_id | 5 | 7 | 9 | 10 | 9 | 10 |
| extras | 1 | 1 | 1 | 1 | 5 | 4 |
| extras_count | 1 | 1 | 2 | 2 | 2 | 2 |

# "pizza_names"  (rows=2)

columns:
"pizza_id" int
"pizza_name" text

indexes: none

all rows:
| column | row 1 | row 2 |
|---|---|---|
| pizza_id | 1 | 2 |
| pizza_name | Meatlovers | Vegetarian |

# "pizza_recipes"  (rows=2)

columns:
"pizza_id" int
"toppings" text

indexes: none

all rows:
| column | row 1 | row 2 |
|---|---|---|
| pizza_id | 1 | 2 |
| toppings | 1, 2, 3, 4, 5, 6, 8, 10 | 4, 6, 7, 9, 11, 12 |

# "pizza_runner_orders"  (rows=10)

columns:
"order_id" int
"runner_id" int
"pickup_time" text
"distance" text
"duration" text
"cancellation" text

indexes: none

all rows:
| column | row 1 | row 2 | row 3 | row 4 | row 5 | row 6 | row 7 | row 8 | row 9 | row 10 |
|---|---|---|---|---|---|---|---|---|---|---|
| order_id | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9 | 10 |
| runner_id | 1 | 1 | 1 | 2 | 3 | 3 | 2 | 2 | 2 | 1 |
| pickup_time | 2021-01-01 18:15:34 | 2021-01-01 19:10:54 | 2021-01-03 00:12:37 | 2021-01-04 13:53:03 | 2021-01-08 21:10:57 | null | 2021-01-08 21:30:45 | 2021-01-10 00:15:02 | null | 2021-01-11 18:50:20 |
| distance | 20km | 20km | 13.4km | 23.4 | 10 | null | 25km | 23.4 km | null | 10km |
| duration | 32 minutes | 27 minutes | 20 mins | 40 | 15 | null | 25mins | 15 minute | null | 10minutes |
| cancellation | null | null | null | null | null | Restaurant Cancellation | null | null | Customer Cancellation | null |

# "pizza_runners"  (rows=4)

columns:
"runner_id" int
"registration_date" text

indexes: none

all rows:
| column | row 1 | row 2 | row 3 | row 4 |
|---|---|---|---|---|
| runner_id | 1 | 2 | 3 | 4 |
| registration_date | 2021-01-01 | 2021-01-03 | 2021-01-08 | 2021-01-15 |

# "pizza_toppings"  (rows=12)

columns:
"topping_id" int: unique identifier, 1..12
"topping_name" text: "BBQ Sauce"=1, "Bacon"=1, "Beef"=1, "Cheese"=1, "Chicken"=1, "Mushrooms"=1, "Onions"=1, "Pepperoni"=1, "Peppers"=1, "Salami"=1, "Tomato Sauce"=1, "Tomatoes"=1

indexes: none

samples:
| column | latest | sample | sample |
|---|---|---|---|
| topping_id | 12 | 9 | 10 |
| topping_name | Tomato Sauce | Peppers | Salami |

# "statistics"  (rows=1010)

columns:
"date" text: iso-date, 285 distinct
"state" text: "MA"=287, "FL"=256, "CO"=253, "NC"=214
"total_cases" int: 932 distinct, 1..836370, avg=132505, median=62120.5
"total_deaths" int: 835 distinct, 0..17179, avg=3939, median=1975

indexes: none

samples:
| column | latest | sample | sample |
|---|---|---|---|
| date | 2020-11-11 00:00:00 | 2020-03-16 00:00:00 | 2020-09-17 00:00:00 |
| state | MA | MA | FL |
| total_cases | 182367 | 197 | 666507 |
| total_deaths | 10202 | 0 | 13086 |

# "trees"  (rows=≈690626)

columns:
"idx" int
"tree_id" int
"tree_dbh" int
"stump_diam" int
"status" text
"health" text
"spc_latin" text
"spc_common" text
"address" text
"zipcode" int
"borocode" int
"boroname" text
"nta_name" text
"state" text
"latitude" float
"longitude" float

indexes: none


# "word_list"  (rows=≈373804)

columns:
"words" text

indexes: none
