---
generator: db-snooper
version: 0.0.26
generated_at_utc: 2026-08-16T08:09:25.529763Z
dialect: sqlite
database: /var/folders/9j/b9bx_drd53sc6zbpsqyrjy4h0000gn/T/dbsnoop-jiakt3mu/modern_data.sqlite
schema: main
---

# companies_dates

```sql
CREATE TABLE "companies_dates" (
"company_id" INTEGER,
  "date_joined" TEXT,
  "year_founded" INTEGER
);
```

## Rows

- total=1085

| column | latest | sample | sample |
|---|---|---|---|
| company_id | 1073 | 151 | 339 |
| date_joined | 2020-09-16T00:00:00.000 | 2021-06-10T00:00:00.000 | 2021-04-07T00:00:00.000 |
| year_founded | 2014 | 2020 | 2017 |

## Columns

- company_id: 1074 distinct, int 0..1073
- date_joined: 639 distinct
- year_founded: 35 distinct, int 1919..2021
  - stats: average=2012.88, median=2014


# companies_funding

```sql
CREATE TABLE "companies_funding" (
"company_id" INTEGER,
  "valuation" INTEGER,
  "funding" INTEGER,
  "select_investors" TEXT
);
```

## Rows

- total=1085

| column | latest | sample | sample |
|---|---|---|---|
| company_id | 1073 | 801 | 808 |
| valuation | 1000000000 | 1000000000 | 1000000000 |
| funding | 620000000 | 323000000 | 458000000 |
| select_investors | "Novator Partners, True, Causeway Media Partners" | "General Catalyst, Bling Capital, Felicis Ventures" | "Intact Ventures, Munich Re Ventures, General Atlantic" |

## Columns

- company_id: 1074 distinct, int 0..1073
- valuation: 30 distinct, int 1000000000..180000000000
  - stats: average=3.44332e+09, median=2e+09
- funding: 538 distinct, int 0..14000000000
  - stats: average=5.50842e+08, median=3.65e+08
- select_investors: 1058 distinct, nulls=1


# companies_industries

```sql
CREATE TABLE "companies_industries" (
"company_id" INTEGER,
  "industry" TEXT
);
```

## Rows

- total=1085

| column | latest | sample | sample |
|---|---|---|---|
| company_id | 1073 | 449 | 1009 |
| industry | E-commerce & direct-to-consumer | Fintech | Other |

## Columns

- company_id: 1074 distinct, int 0..1073
- industry: "Fintech"=230, "Internet software & services"=208, "E-commerce & direct-to-consumer"=113, "Artificial intelligence"=84, "Health"=74, "Other"=58, ""Supply chain, logistics, & delivery""=57, "Cybersecurity"=50, "Data management & analytics"=41, "Mobile & telecommunications"=38, "Hardware"=34, "Auto & transportation"=31, "Edtech"=28, "Consumer & retail"=25, "Travel"=14


# income_trees

```sql
CREATE TABLE "income_trees" (
"zipcode" INTEGER,
  "Estimate_Total" INTEGER,
  "Margin_of_Error_Total" INTEGER,
  "Estimate_Median_income" INTEGER,
  "Margin_of_Error_Median_income" INTEGER,
  "Estimate_Mean_income" INTEGER,
  "Margin_of_Error_Mean_income" INTEGER
);
```

## Rows

- total=220

| column | latest | sample | sample |
|---|---|---|---|
| zipcode | 11697 | 11237 | 11366 |
| Estimate_Total | 1520 | 16582 | 4191 |
| Margin_of_Error_Total | 139 | 363 | 229 |
| Estimate_Median_income | 93333 | 44950 | 72486 |
| Margin_of_Error_Median_income | 21346 | 2489 | 6760 |
| Estimate_Mean_income | 109500 | 62004 | 93774 |
| Margin_of_Error_Mean_income | 11505 | 3688 | 6425 |

## Columns

- zipcode: 216 distinct, int 10001..11697
  - stats: average=10763.8, median=11002
- Estimate_Total: 185 distinct, int 0..43456
  - stats: average=14736.1, median=13775.5
- Margin_of_Error_Total: 153 distinct, int 11..1181
  - stats: average=347.055, median=353
- Estimate_Median_income: 184 distinct, int 0..193510
  - stats: average=54439.9, median=53427
- Margin_of_Error_Median_income: 180 distinct, int 0..41091
  - stats: average=4334.21, median=3228.5
- Estimate_Mean_income: 185 distinct, int 0..441278
  - stats: average=79260.9, median=72082
- Margin_of_Error_Mean_income: 182 distinct, int 0..56347
  - stats: average=5755.62, median=3569


# pizza_clean_customer_orders

```sql
CREATE TABLE "pizza_clean_customer_orders" (
"order_id" INTEGER,
  "customer_id" INTEGER,
  "pizza_id" INTEGER,
  "exclusions" TEXT,
  "extras" TEXT,
  "order_time" TEXT
);
```

## Rows

- total=14

| column | latest | sample | sample |
|---|---|---|---|
| order_id | 10 | 2 | 10 |
| customer_id | 104 | 101 | 104 |
| pizza_id | 1 | 1 | 1 |
| exclusions | 2,6 | null | null |
| extras | 1,4 | null | null |
| order_time | 2021-01-11 18:34:49 | 2021-01-01 19:00:52 | 2021-01-11 18:34:49 |

## Columns

- order_id: 4=3, 3=2, 10=2, 1=1, 2=1, 5=1, 6=1, 7=1, 8=1, 9=1, int 1..10
- customer_id: 103=4, 101=3, 102=3, 104=3, 105=1, int 101..105
- pizza_id: 1=10, 2=4
- exclusions: "4"=4, "2,6"=1, nulls=9
- extras: "1"=2, "1,4"=1, "1,5"=1, nulls=10
- order_time: "2021-01-04 13:23:46"=3, "2021-01-02 23:51:23"=2, "2021-01-11 18:34:49"=2, "2021-01-01 18:05:02"=1, "2021-01-01 19:00:52"=1, "2021-01-08 21:00:29"=1, "2021-01-08 21:03:13"=1, "2021-01-08 21:20:29"=1, "2021-01-09 23:54:33"=1, "2021-01-10 11:22:59"=1


# pizza_clean_runner_orders

## All rows

| column | row 1 | row 2 | row 3 | row 4 | row 5 | row 6 | row 7 | row 8 | row 9 | row 10 |
|---|---|---|---|---|---|---|---|---|---|---|
| order_id | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9 | 10 |
| runner_id | 1 | 1 | 1 | 2 | 3 | 3 | 2 | 2 | 2 | 1 |
| pickup_time | 2021-01-01 18:15:34 | 2021-01-01 19:10:54 | 2021-01-03 00:12:37 | 2021-01-04 13:53:03 | 2021-01-08 21:10:57 | null | 2021-01-08 21:30:45 | 2021-01-10 00:15:02 | null | 2021-01-11 18:50:20 |
| distance | 20 | 20 | 13.4 | 23.4 | 10 | 0 | 25 | 23.4 | 0 | 10 |
| duration | 32 | 27 | 20 | 40 | 15 | 0 | 25 | 15 | 0 | 10 |
| cancellation | null | null | null | null | null | Restaurant Cancellation | null | null | Customer Cancellation | null |


# pizza_customer_orders

```sql
CREATE TABLE "pizza_customer_orders" (
"order_id" INTEGER,
  "customer_id" INTEGER,
  "pizza_id" INTEGER,
  "exclusions" TEXT,
  "extras" TEXT,
  "order_time" TEXT
);
```

## Rows

- total=14

| column | latest | sample | sample |
|---|---|---|---|
| order_id | 10 | 7 | 4 |
| customer_id | 104 | 105 | 103 |
| pizza_id | 1 | 2 | 2 |
| exclusions | 2,6 | null | 4 |
| extras | 1,4 | 1 | null |
| order_time | 2021-01-11 18:34:49 | 2021-01-08 21:20:29 | 2021-01-04 13:23:46 |

## Columns

- order_id: 4=3, 3=2, 10=2, 1=1, 2=1, 5=1, 6=1, 7=1, 8=1, 9=1, int 1..10
- customer_id: 103=4, 101=3, 102=3, 104=3, 105=1, int 101..105
- pizza_id: 1=10, 2=4
- exclusions: "4"=4, "2,6"=1, nulls=9
- extras: "1"=2, "1,4"=1, "1,5"=1, nulls=10
- order_time: "2021-01-04 13:23:46"=3, "2021-01-02 23:51:23"=2, "2021-01-11 18:34:49"=2, "2021-01-01 18:05:02"=1, "2021-01-01 19:00:52"=1, "2021-01-08 21:00:29"=1, "2021-01-08 21:03:13"=1, "2021-01-08 21:20:29"=1, "2021-01-09 23:54:33"=1, "2021-01-10 11:22:59"=1


# pizza_get_exclusions

## All rows

| column | row 1 | row 2 | row 3 | row 4 |
|---|---|---|---|---|
| row_id | 1 | 1 | 1 | 2 |
| order_id | 4 | 9 | 10 | 10 |
| exclusions | 4 | 4 | 2 | 6 |
| total_exclusions | 3 | 1 | 2 | 2 |


# pizza_get_extras

## All rows

| column | row 1 | row 2 | row 3 | row 4 | row 5 | row 6 |
|---|---|---|---|---|---|---|
| row_id | 1 | 1 | 1 | 1 | 2 | 2 |
| order_id | 5 | 7 | 9 | 10 | 9 | 10 |
| extras | 1 | 1 | 1 | 1 | 5 | 4 |
| extras_count | 1 | 1 | 2 | 2 | 2 | 2 |


# pizza_names

## All rows

| column | row 1 | row 2 |
|---|---|---|
| pizza_id | 1 | 2 |
| pizza_name | Meatlovers | Vegetarian |


# pizza_recipes

## All rows

| column | row 1 | row 2 |
|---|---|---|
| pizza_id | 1 | 2 |
| toppings | 1, 2, 3, 4, 5, 6, 8, 10 | 4, 6, 7, 9, 11, 12 |


# pizza_runner_orders

## All rows

| column | row 1 | row 2 | row 3 | row 4 | row 5 | row 6 | row 7 | row 8 | row 9 | row 10 |
|---|---|---|---|---|---|---|---|---|---|---|
| order_id | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9 | 10 |
| runner_id | 1 | 1 | 1 | 2 | 3 | 3 | 2 | 2 | 2 | 1 |
| pickup_time | 2021-01-01 18:15:34 | 2021-01-01 19:10:54 | 2021-01-03 00:12:37 | 2021-01-04 13:53:03 | 2021-01-08 21:10:57 | null | 2021-01-08 21:30:45 | 2021-01-10 00:15:02 | null | 2021-01-11 18:50:20 |
| distance | 20km | 20km | 13.4km | 23.4 | 10 | null | 25km | 23.4 km | null | 10km |
| duration | 32 minutes | 27 minutes | 20 mins | 40 | 15 | null | 25mins | 15 minute | null | 10minutes |
| cancellation | null | null | null | null | null | Restaurant Cancellation | null | null | Customer Cancellation | null |


# pizza_runners

## All rows

| column | row 1 | row 2 | row 3 | row 4 |
|---|---|---|---|---|
| runner_id | 1 | 2 | 3 | 4 |
| registration_date | 2021-01-01 | 2021-01-03 | 2021-01-08 | 2021-01-15 |


# pizza_toppings

```sql
CREATE TABLE "pizza_toppings" (
"topping_id" INTEGER,
  "topping_name" TEXT
);
```

## Rows

- total=12

| column | latest | sample | sample |
|---|---|---|---|
| topping_id | 12 | 3 | 5 |
| topping_name | Tomato Sauce | Beef | Chicken |

## Columns

- topping_id: unique identifier, int 1..12
- topping_name: "BBQ Sauce"=1, "Bacon"=1, "Beef"=1, "Cheese"=1, "Chicken"=1, "Mushrooms"=1, "Onions"=1, "Pepperoni"=1, "Peppers"=1, "Salami"=1, "Tomato Sauce"=1, "Tomatoes"=1


# statistics

```sql
CREATE TABLE "statistics" (
"date" TEXT,
  "state" TEXT,
  "total_cases" INTEGER,
  "total_deaths" INTEGER
);
```

## Rows

- total=1010

| column | latest | sample | sample |
|---|---|---|---|
| date | 2020-11-11 00:00:00 | 2020-06-16 00:00:00 | 2020-10-08 00:00:00 |
| state | MA | MA | MA |
| total_cases | 182367 | 105885 | 144173 |
| total_deaths | 10202 | 7665 | 9558 |

## Columns

- date: 285 distinct
- state: "MA"=287, "FL"=256, "CO"=253, "NC"=214
- total_cases: 932 distinct, int 1..836370
  - stats: average=132505, median=62120.5
- total_deaths: 835 distinct, int 0..17179
  - stats: average=3939, median=1975


# trees

```sql
CREATE TABLE "trees" (
"idx" INTEGER,
  "tree_id" INTEGER,
  "tree_dbh" INTEGER,
  "stump_diam" INTEGER,
  "status" TEXT,
  "health" TEXT,
  "spc_latin" TEXT,
  "spc_common" TEXT,
  "address" TEXT,
  "zipcode" INTEGER,
  "borocode" INTEGER,
  "boroname" TEXT,
  "nta_name" TEXT,
  "state" TEXT,
  "latitude" REAL,
  "longitude" REAL
);
```

## Rows

- total≈690626 (estimated from db stats; row/column profiling skipped)


# word_list

```sql
CREATE TABLE "word_list" (
"words" TEXT
);
```

## Rows

- total≈373804 (estimated from db stats; row/column profiling skipped)
