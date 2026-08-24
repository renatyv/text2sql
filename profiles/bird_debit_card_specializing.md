---
generator: db-snooper
version: 0.0.34
generated_at_utc: 2026-08-24T21:20:34.609403Z
dialect: sqlite
database: /var/folders/9j/b9bx_drd53sc6zbpsqyrjy4h0000gn/T/dbsnoop-zmf8sx1_/debit_card_specializing.sqlite
schema: main
---

## Relationships

- "customers"."CustomerID" ← "yearmonth"."CustomerID"

# "customers"  (rows=32461)

columns:
"CustomerID" int PK UNIQ: unique identifier, 3..53314, avg=27888.2, median=28608
"Segment" text: "SME"=26763, "LAM"=3658, "KAM"=2040
"Currency" text: "CZK"=30459, "EUR"=2002

indexes: none

samples:
| column | latest | sample | sample |
|---|---|---|---|
| CustomerID | 53314 | 52055 | 32164 |
| Segment | SME | SME | LAM |
| Currency | CZK | CZK | CZK |

# "gasstations"  (rows=5716)

columns:
"GasStationID" int PK UNIQ: unique identifier, 44..5772, avg=2905.28, median=2903.5
"ChainID" int: 233 distinct, 1..290, avg=27.528, median=6
"Country" text: "CZE"=4836, "SVK"=880
"Segment" text: "Other"=2392, "Premium"=1428, "Noname"=1005, "Value for money"=597, "Discount"=294

indexes: none

samples:
| column | latest | sample | sample |
|---|---|---|---|
| GasStationID | 5772 | 1858 | 936 |
| ChainID | 16 | 3 | 33 |
| Country | CZE | CZE | CZE |
| Segment | Other | Other | Premium |

# "products"  (rows=591)

columns:
"ProductID" int PK UNIQ: unique identifier, 1..630, avg=298.306, median=296
"Description" text: 529 distinct

indexes: none

samples:
| column | latest | sample | sample |
|---|---|---|---|
| ProductID | 630 | 450 | 29 |
| Description | CCS Carnet Pronájem HW (Manual) | Vydání karty  | Ekol.paliva |

# "transactions_1k"  (rows=1000)

columns:
"TransactionID" int PK: unique identifier, 1..1000, avg=500.5, median=500.5
"Date" date: "2012-08-24"=492, "2012-08-25"=425, "2012-08-26"=73, "2012-08-23"=10
"Time" text: 599 distinct
"CustomerID" int: 517 distinct, 96..49838, avg=21975.4, median=19182
"CardID" int: 902 distinct, 26228..775970, avg=560900, median=597140
"GasStationID" int: 437 distinct, 48..5481, avg=2290.53, median=2440
"ProductID" int: 28 distinct, 2..352, avg=26.878, median=2
"Amount" int: 83 distinct, 0..264, avg=19.678, median=19
"Price" float: 930 distinct, 1.76..5762.49, avg=425.576, median=354.035

indexes: none

samples:
| column | latest | sample | sample |
|---|---|---|---|
| TransactionID | 1000 | 823 | 15 |
| Date | 2012-08-25 | 2012-08-25 | 2012-08-24 |
| Time | 12:45:00 | 13:25:00 | 09:36:00 |
| CustomerID | 25986 | 22994 | 14728 |
| CardID | 655214 | 654107 | 570199 |
| GasStationID | 3899 | 1248 | 967 |
| ProductID | 2 | 15 | 7 |
| Amount | 38 | 0 | 0 |
| Price | 870.93 | 38.69 | 60.48 |

# "yearmonth"  (rows=≈383282)

columns:
"CustomerID" int PK FK
"Date" text PK
"Consumption" float

indexes: none
