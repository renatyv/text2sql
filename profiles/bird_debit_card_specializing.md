---
generator: db-snooper
version: 0.0.26
generated_at_utc: 2026-08-16T07:18:45.209296Z
dialect: sqlite
database: /Users/renatyuldashev/Documents/ai-sql/custom-bench/data/bird_mini_dev/databases/dev_databases/debit_card_specializing/debit_card_specializing.sqlite
schema: main
---

## Relationships

- customers.CustomerID ← yearmonth.CustomerID

# customers

```sql
CREATE TABLE customers
(
    CustomerID INTEGER UNIQUE     not null
        primary key,
    Segment    TEXT null,
    Currency   TEXT null
);
```

## Rows

- total=32461

| column | latest | sample | sample |
|---|---|---|---|
| CustomerID | 53314 | 18686 | 43717 |
| Segment | SME | SME | SME |
| Currency | CZK | CZK | CZK |

## Columns

- CustomerID: unique identifier, int 3..53314
  - stats: average=27888.2, median=28608
- Segment: "SME"=26763, "LAM"=3658, "KAM"=2040
- Currency: "CZK"=30459, "EUR"=2002


# gasstations

```sql
CREATE TABLE gasstations
(
    GasStationID INTEGER    UNIQUE   not null
        primary key,
    ChainID      INTEGER          null,
    Country      TEXT null,
    Segment      TEXT null
);
```

## Rows

- total=5716

| column | latest | sample | sample |
|---|---|---|---|
| GasStationID | 5772 | 1949 | 5719 |
| ChainID | 16 | 3 | 248 |
| Country | CZE | CZE | SVK |
| Segment | Other | Other | Other |

## Columns

- GasStationID: unique identifier, int 44..5772
  - stats: average=2905.28, median=2903.5
- ChainID: 233 distinct, int 1..290
  - stats: average=27.528, median=6
- Country: "CZE"=4836, "SVK"=880
- Segment: "Other"=2392, "Premium"=1428, "Noname"=1005, "Value for money"=597, "Discount"=294


# products

```sql
CREATE TABLE products
(
    ProductID   INTEGER   UNIQUE      not null
        primary key,
    Description TEXT null
);
```

## Rows

- total=591

| column | latest | sample | sample |
|---|---|---|---|
| ProductID | 630 | 323 | 551 |
| Description | CCS Carnet Pronájem HW (Manual) | Eurosuper 96 | Garage commission |

## Columns

- ProductID: unique identifier, int 1..630
  - stats: average=298.306, median=296
- Description: 529 distinct


# transactions_1k

```sql
CREATE TABLE "transactions_1k"
(
    TransactionID INTEGER
        primary key autoincrement,
    Date          DATE,
    Time          TEXT,
    CustomerID    INTEGER,
    CardID        INTEGER,
    GasStationID  INTEGER,
    ProductID     INTEGER,
    Amount        INTEGER,
    Price         REAL
);
```

## Rows

- total=1000

| column | latest | sample | sample |
|---|---|---|---|
| TransactionID | 1000 | 682 | 700 |
| Date | 2012-08-25 | 2012-08-25 | 2012-08-25 |
| Time | 12:45:00 | 15:31:00 | 04:10:00 |
| CustomerID | 25986 | 24700 | 48793 |
| CardID | 655214 | 607212 | 707950 |
| GasStationID | 3899 | 3475 | 5368 |
| ProductID | 2 | 5 | 2 |
| Amount | 38 | 1 | 28 |
| Price | 870.93 | 20.75 | 652.98 |

## Columns

- TransactionID: unique identifier, int 1..1000
  - stats: average=500.5, median=500.5
- Date: 2012-08-24=492, 2012-08-25=425, 2012-08-26=73, 2012-08-23=10
- Time: 599 distinct
- CustomerID: 517 distinct, int 96..49838
  - stats: average=21975.4, median=19182
- CardID: 902 distinct, int 26228..775970
  - stats: average=560900, median=597140
- GasStationID: 437 distinct, int 48..5481
  - stats: average=2290.53, median=2440
- ProductID: 28 distinct, int 2..352
  - stats: average=26.878, median=2
- Amount: 83 distinct, int 0..264
  - stats: average=19.678, median=19
- Price: 930 distinct, num 1.76..5762.49
  - stats: average=425.576, median=354.035


# yearmonth

```sql
CREATE TABLE "yearmonth"
(
    CustomerID  INTEGER not null
        references customers
            on update cascade on delete cascade
        references customers,
    Date        TEXT    not null,
    Consumption REAL,
    primary key (Date, CustomerID)
);
```

## Rows

- total=383282

| column | latest | sample | sample |
|---|---|---|---|
| CustomerID | 52353 | 31762 | 27859 |
| Date | 201311 | 201307 | 201309 |
| Consumption | 1566.24 | 5909.61 | 116971 |

## Columns

- CustomerID: 30566 distinct, int 5..52353
  - stats: average=25793
- Date: 21 distinct
- Consumption: num -582093..2.05219e+06
  - stats: average=8911.14
