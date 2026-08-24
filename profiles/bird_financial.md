---
generator: db-snooper
version: 0.0.34
generated_at_utc: 2026-08-24T21:21:17.230828Z
dialect: sqlite
database: /var/folders/9j/b9bx_drd53sc6zbpsqyrjy4h0000gn/T/dbsnoop-wm5yngwy/financial.sqlite
schema: main
---

## Relationships

- "account"."account_id" ← "disp"."account_id", "loan"."account_id", "order"."account_id", "trans"."account_id"
- "client"."client_id" ← "disp"."client_id"
- "disp"."disp_id" ← "card"."disp_id"
- "district"."district_id" ← "account"."district_id", "client"."district_id"

# "account"  (rows=4500)

columns:
"account_id" int PK: unique identifier, 1..11382
"district_id" int NOTNULL FK: 77 distinct, 1..77
"frequency" text NOTNULL: "POPLATEK MESICNE"=4167, "POPLATEK TYDNE"=240, "POPLATEK PO OBRATU"=93
"date" date NOTNULL: 1535 distinct

indexes: none

samples:
| column | latest | sample | sample |
|---|---|---|---|
| account_id | 11382 | 2468 | 758 |
| district_id | 74 | 4 | 51 |
| frequency | POPLATEK MESICNE | POPLATEK MESICNE | POPLATEK MESICNE |
| date | 1995-08-20 | 1996-07-13 | 1997-12-19 |

# "card"  (rows=892)

columns:
"card_id" int PK: unique identifier, 1..1247
"disp_id" int NOTNULL FK: unique identifier, 9..13660
"type" text NOTNULL: "classic"=659, "junior"=145, "gold"=88
"issued" date NOTNULL: 607 distinct

indexes: none

samples:
| column | latest | sample | sample |
|---|---|---|---|
| card_id | 1247 | 468 | 1137 |
| disp_id | 13660 | 3023 | 11771 |
| type | classic | classic | gold |
| issued | 1995-06-13 | 1995-01-30 | 1998-12-01 |

# "client"  (rows=5369)

columns:
"client_id" int PK: unique identifier, 1..13998
"gender" text NOTNULL: "M"=2724, "F"=2645
"birth_date" date NOTNULL: 4738 distinct
"district_id" int NOTNULL FK: 77 distinct, 1..77

indexes: none

samples:
| column | latest | sample | sample |
|---|---|---|---|
| client_id | 13998 | 536 | 1364 |
| gender | F | M | M |
| birth_date | 1953-08-12 | 1939-08-25 | 1933-12-28 |
| district_id | 74 | 47 | 1 |

# "disp"  (rows=5369)

columns:
"disp_id" int PK: unique identifier, 1..13690
"client_id" int NOTNULL FK: unique identifier, 1..13998
"account_id" int NOTNULL FK: 4500 distinct, 1..11382
"type" text NOTNULL: "OWNER"=4500, "DISPONENT"=869

indexes: none

samples:
| column | latest | sample | sample |
|---|---|---|---|
| disp_id | 13690 | 3172 | 6481 |
| client_id | 13998 | 3172 | 6481 |
| account_id | 11382 | 2628 | 5369 |
| type | OWNER | OWNER | OWNER |

# "district"  (rows=77)

columns:
"district_id" int PK: unique identifier, 1..77
"A2" text NOTNULL: all distinct
"A3" text NOTNULL: "south Moravia"=14, "central Bohemia"=12, "east Bohemia"=11, "north Moravia"=11, "north Bohemia"=10, "west Bohemia"=10, "south Bohemia"=8, "Prague"=1
"A4" text NOTNULL: digits, all distinct
"A5" text NOTNULL: digits, 53 distinct
"A6" text NOTNULL: digits, 36 distinct
"A7" text NOTNULL: "4"=12, "6"=11, "7"=10, "5"=9, "10"=5, "3"=5, "8"=5, "0"=4, "1"=3, "2"=3, "12"=2, "13"=2, "18"=2, "11"=1, "14"=1, "20"=1, "9"=1
"A8" int NOTNULL: 1=34, 2=23, 3=12, 0=4, 4=3, 5=1, 0..5
"A9" int NOTNULL: 6=14, 4=12, 7=11, 5=10, 8=7, 9=7, 10=7, 1=4, 3=2, 11=2, 2=1, 1..11
"A10" float NOTNULL: 70 distinct, 33.9..100, avg=63.0351, median=59.8
"A11" int NOTNULL: 76 distinct, 8110..12541, avg=9031.68, median=8814
"A12" float: 41 distinct, nulls=1, 0.2..7.3, avg=3.07237, median=2.8
"A13" float NOTNULL: 73 distinct, 0.43..9.4, avg=3.78701, median=3.6
"A14" int NOTNULL: 44 distinct, 81..167, avg=116.13, median=113
"A15" int: 75 distinct, nulls=1, 818..85677, avg=4850.32, median=2932
"A16" int NOTNULL: 76 distinct, 888..99107, avg=5030.83, median=3040

indexes: none

samples:
| column | latest | sample | sample |
|---|---|---|---|
| district_id | 77 | 34 | 51 |
| A2 | Vsetin | Chomutov | Trutnov |
| A3 | north Moravia | north Bohemia | east Bohemia |
| A4 | 148545 | 125236 | 121947 |
| A5 | 8 | 28 | 37 |
| A6 | 35 | 11 | 28 |
| A7 | 12 | 1 | 7 |
| A8 | 3 | 4 | 3 |
| A9 | 4 | 5 | 11 |
| A10 | 53.5 | 87.7 | 70.5 |
| A11 | 8909 | 9675 | 8541 |
| A12 | 4 | 6.4 | 2.5 |
| A13 | 5.56 | 7.68 | 2.97 |
| A14 | 113 | 100 | 131 |
| A15 | 3460 | 5323 | 3496 |
| A16 | 3590 | 5190 | 3839 |

# "loan"  (rows=682)

columns:
"loan_id" int PK: unique identifier, 4959..7308
"account_id" int NOTNULL FK: unique identifier, 2..11362
"date" date NOTNULL: 559 distinct
"amount" int NOTNULL: 645 distinct, 4980..590820, avg=151410, median=116928
"duration" int NOTNULL: 60=145, 24=138, 48=138, 12=131, 36=130, 12..60
"payments" float NOTNULL: 577 distinct, 304..9910, avg=4190.66, median=3934
"status" text NOTNULL: "C"=403, "A"=203, "D"=45, "B"=31

indexes: none

samples:
| column | latest | sample | sample |
|---|---|---|---|
| loan_id | 7308 | 6992 | 6868 |
| account_id | 11362 | 9790 | 9208 |
| date | 1996-12-27 | 1996-07-27 | 1998-10-12 |
| amount | 129408 | 133968 | 82128 |
| duration | 24 | 48 | 24 |
| payments | 5392 | 2791 | 3422 |
| status | A | C | C |

# "order"  (rows=6471)

columns:
"order_id" int PK: unique identifier, 29401..46338
"account_id" int NOTNULL FK: 3758 distinct, 1..11362
"bank_to" text NOTNULL: "QR"=531, "YZ"=521, "AB"=519, "WX"=515, "ST"=511, "KL"=500, "UV"=499, "IJ"=496, "GH"=487, "OP"=485, "EF"=483, "MN"=466, "CD"=458
"account_to" int NOTNULL: 6446 distinct, 399..99994199, avg=4.9e+07, median=5e+07
"amount" float NOTNULL: 4412 distinct, 1..14882, avg=3280.64, median=2596
"k_symbol" text NOTNULL: "SIPO"=3502, ""=1379, "UVER"=717, "POJISTNE"=532, "LEASING"=341

indexes: none

samples:
| column | latest | sample | sample |
|---|---|---|---|
| order_id | 46338 | 39352 | 34939 |
| account_id | 11362 | 6715 | 3755 |
| bank_to | MN | GH | YZ |
| account_to | 61540514 | 85509657 | 53685873 |
| amount | 5392 | 2298.2 | 13500 |
| k_symbol | UVER | UVER | SIPO |

# "trans"  (rows=≈1056320)

columns:
"trans_id" int PK
"account_id" int NOTNULL FK
"date" date NOTNULL
"type" text NOTNULL
"operation" text
"amount" int NOTNULL
"balance" int NOTNULL
"k_symbol" text
"bank" text
"account" int

indexes: none
