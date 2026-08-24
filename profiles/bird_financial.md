---
generator: db-snooper
version: 0.0.34
generated_at_utc: 2026-08-24T21:56:13.497740Z
dialect: sqlite
database: /var/folders/9j/b9bx_drd53sc6zbpsqyrjy4h0000gn/T/dbsnoop-ns5a5hmt/financial.sqlite
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
| account_id | 11382 | 1586 | 2161 |
| district_id | 74 | 1 | 15 |
| frequency | POPLATEK MESICNE | POPLATEK MESICNE | POPLATEK TYDNE |
| date | 1995-08-20 | 1996-10-03 | 1993-12-30 |

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
| card_id | 1247 | 577 | 291 |
| disp_id | 13660 | 3687 | 1836 |
| type | classic | classic | classic |
| issued | 1995-06-13 | 1994-02-15 | 1998-09-29 |

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
| client_id | 13998 | 908 | 5117 |
| gender | F | F | M |
| birth_date | 1953-08-12 | 1961-03-07 | 1975-03-21 |
| district_id | 74 | 51 | 52 |

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
| disp_id | 13690 | 9679 | 11547 |
| client_id | 13998 | 9987 | 11855 |
| account_id | 11382 | 8085 | 9631 |
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
| district_id | 77 | 70 | 52 |
| A2 | Vsetin | Karvina | Usti nad Orlici |
| A3 | north Moravia | north Moravia | east Bohemia |
| A4 | 148545 | 285387 | 139012 |
| A5 | 8 | 0 | 59 |
| A6 | 35 | 2 | 41 |
| A7 | 12 | 8 | 8 |
| A8 | 3 | 5 | 3 |
| A9 | 4 | 7 | 10 |
| A10 | 53.5 | 89.9 | 61.9 |
| A11 | 8909 | 10177 | 8363 |
| A12 | 4 | 6.6 | 2.5 |
| A13 | 5.56 | 7.75 | 3.49 |
| A14 | 113 | 81 | 108 |
| A15 | 3460 | 9878 | 2564 |
| A16 | 3590 | 10108 | 2799 |

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
| loan_id | 7308 | 5313 | 7138 |
| account_id | 11362 | 1776 | 10440 |
| date | 1996-12-27 | 1998-05-27 | 1995-07-03 |
| amount | 129408 | 43200 | 60000 |
| duration | 24 | 24 | 60 |
| payments | 5392 | 1800 | 1000 |
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
| order_id | 46338 | 33296 | 31849 |
| account_id | 11362 | 2644 | 1668 |
| bank_to | MN | IJ | IJ |
| account_to | 61540514 | 61139798 | 84733837 |
| amount | 5392 | 124 | 3275 |
| k_symbol | UVER | SIPO | SIPO |

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
