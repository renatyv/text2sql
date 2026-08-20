---
generator: db-snooper
version: 0.0.31
generated_at_utc: 2026-08-20T17:26:38.121896Z
dialect: sqlite
database: /var/folders/9j/b9bx_drd53sc6zbpsqyrjy4h0000gn/T/dbsnoop-u904z_2i/financial.sqlite
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
fk: "district_id"→"district"."district_id"

samples:
| column | latest | sample | sample |
|---|---|---|---|
| account_id | 11382 | 3517 | 2670 |
| district_id | 74 | 26 | 13 |
| frequency | POPLATEK MESICNE | POPLATEK MESICNE | POPLATEK MESICNE |
| date | 1995-08-20 | 1996-11-22 | 1993-01-27 |

# "card"  (rows=892)

columns:
"card_id" int PK: unique identifier, 1..1247
"disp_id" int NOTNULL FK: unique identifier, 9..13660
"type" text NOTNULL: "classic"=659, "junior"=145, "gold"=88
"issued" date NOTNULL: 607 distinct

indexes: none
fk: "disp_id"→"disp"."disp_id"

samples:
| column | latest | sample | sample |
|---|---|---|---|
| card_id | 1247 | 204 | 361 |
| disp_id | 13660 | 1239 | 2312 |
| type | classic | junior | classic |
| issued | 1995-06-13 | 1996-05-30 | 1998-09-23 |

# "client"  (rows=5369)

columns:
"client_id" int PK: unique identifier, 1..13998
"gender" text NOTNULL: "M"=2724, "F"=2645
"birth_date" date NOTNULL: 4738 distinct
"district_id" int NOTNULL FK: 77 distinct, 1..77

indexes: none
fk: "district_id"→"district"."district_id"

samples:
| column | latest | sample | sample |
|---|---|---|---|
| client_id | 13998 | 1137 | 4004 |
| gender | F | F | F |
| birth_date | 1953-08-12 | 1977-03-05 | 1957-08-12 |
| district_id | 74 | 1 | 30 |

# "disp"  (rows=5369)

columns:
"disp_id" int PK: unique identifier, 1..13690
"client_id" int NOTNULL FK: unique identifier, 1..13998
"account_id" int NOTNULL FK: 4500 distinct, 1..11382
"type" text NOTNULL: "OWNER"=4500, "DISPONENT"=869

indexes: none
fk: "account_id"→"account"."account_id", "client_id"→"client"."client_id"

samples:
| column | latest | sample | sample |
|---|---|---|---|
| disp_id | 13690 | 12020 | 9 |
| client_id | 13998 | 12328 | 9 |
| account_id | 11382 | 10022 | 7 |
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
fk: none

samples:
| column | latest | sample | sample |
|---|---|---|---|
| district_id | 77 | 13 | 76 |
| A2 | Vsetin | Rakovnik | Sumperk |
| A3 | north Moravia | central Bohemia | north Moravia |
| A4 | 148545 | 53921 | 127369 |
| A5 | 8 | 61 | 31 |
| A6 | 35 | 22 | 32 |
| A7 | 12 | 1 | 13 |
| A8 | 3 | 1 | 2 |
| A9 | 4 | 2 | 7 |
| A10 | 53.5 | 41.3 | 51.2 |
| A11 | 8909 | 8598 | 8369 |
| A12 | 4 | 2.7 | 4.7 |
| A13 | 5.56 | 3.26 | 5.88 |
| A14 | 113 | 123 | 107 |
| A15 | 3460 | 1597 | 3736 |
| A16 | 3590 | 1875 | 2807 |

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
fk: "account_id"→"account"."account_id"

samples:
| column | latest | sample | sample |
|---|---|---|---|
| loan_id | 7308 | 7189 | 6235 |
| account_id | 11362 | 10728 | 6062 |
| date | 1996-12-27 | 1996-03-21 | 1998-04-19 |
| amount | 129408 | 154656 | 321360 |
| duration | 24 | 48 | 60 |
| payments | 5392 | 3222 | 5356 |
| status | A | C | C |

# "order"  (rows=6471)

columns:
"order_id" int PK: unique identifier, 29401..46338
"account_id" int NOTNULL FK: 3758 distinct, 1..11362
"bank_to" text NOTNULL: "QR"=531, "YZ"=521, "AB"=519, "WX"=515, "ST"=511, "KL"=500, "UV"=499, "IJ"=496, "GH"=487, "OP"=485, "EF"=483, "MN"=466, "CD"=458
"account_to" int NOTNULL: 6446 distinct, 399..99994199, avg=4.9399e+07, median=4.97561e+07
"amount" float NOTNULL: 4412 distinct, 1..14882, avg=3280.64, median=2596
"k_symbol" text NOTNULL: "SIPO"=3502, ""=1379, "UVER"=717, "POJISTNE"=532, "LEASING"=341

indexes: none
fk: "account_id"→"account"."account_id"

samples:
| column | latest | sample | sample |
|---|---|---|---|
| order_id | 46338 | 29545 | 40816 |
| account_id | 11362 | 90 | 7713 |
| bank_to | MN | YZ | ST |
| account_to | 61540514 | 2028567 | 45360702 |
| amount | 5392 | 361 | 8418 |
| k_symbol | UVER |  | SIPO |

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
fk: "account_id"→"account"."account_id"
