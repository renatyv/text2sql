---
generator: db-snooper
version: 0.0.26
generated_at_utc: 2026-08-16T07:19:17.012416Z
dialect: sqlite
database: /Users/renatyuldashev/Documents/ai-sql/custom-bench/data/bird_mini_dev/databases/dev_databases/financial/financial.sqlite
schema: main
---

## Relationships

- account.account_id ← disp.account_id, loan.account_id, order.account_id, trans.account_id
- client.client_id ← disp.client_id
- disp.disp_id ← card.disp_id
- district.district_id ← account.district_id, client.district_id

# account

```sql
CREATE TABLE account
(
    account_id  INTEGER default 0 not null
        primary key,
    district_id INTEGER default 0 not null,
    frequency   TEXT   not null,
    date        DATE          not null,
    foreign key (district_id) references district (district_id)
);
```

## Rows

- total=4500

| column | latest | sample | sample |
|---|---|---|---|
| account_id | 11382 | 3083 | 1165 |
| district_id | 74 | 66 | 44 |
| frequency | POPLATEK MESICNE | POPLATEK MESICNE | POPLATEK MESICNE |
| date | 1995-08-20 | 1997-03-18 | 1997-03-23 |

## Columns

- account_id: unique identifier, int 1..11382
- district_id: 77 distinct, int 1..77
- frequency: "POPLATEK MESICNE"=4167, "POPLATEK TYDNE"=240, "POPLATEK PO OBRATU"=93
- date: 1535 distinct


# card

```sql
CREATE TABLE card
(
    card_id INTEGER default 0 not null
        primary key,
    disp_id INTEGER           not null,
    type    TEXT    not null,
    issued  DATE          not null,
    foreign key (disp_id) references disp (disp_id)
);
```

## Rows

- total=892

| column | latest | sample | sample |
|---|---|---|---|
| card_id | 1247 | 434 | 69 |
| disp_id | 13660 | 2739 | 438 |
| type | classic | classic | classic |
| issued | 1995-06-13 | 1997-12-30 | 1997-05-17 |

## Columns

- card_id: unique identifier, int 1..1247
- disp_id: unique identifier, int 9..13660
- type: "classic"=659, "junior"=145, "gold"=88
- issued: 607 distinct


# client

```sql
CREATE TABLE client
(
    client_id   INTEGER        not null
        primary key,
    gender      TEXT not null,
    birth_date  DATE       not null,
    district_id INTEGER        not null,
    foreign key (district_id) references district (district_id)
);
```

## Rows

- total=5369

| column | latest | sample | sample |
|---|---|---|---|
| client_id | 13998 | 135 | 1910 |
| gender | F | F | M |
| birth_date | 1953-08-12 | 1938-09-10 | 1946-11-08 |
| district_id | 74 | 6 | 67 |

## Columns

- client_id: unique identifier, int 1..13998
- gender: "M"=2724, "F"=2645
- birth_date: 4738 distinct
- district_id: 77 distinct, int 1..77


# disp

```sql
CREATE TABLE disp
(
    disp_id    INTEGER        not null
        primary key,
    client_id  INTEGER        not null,
    account_id INTEGER        not null,
    type      TEXT not null,
    foreign key (account_id) references account (account_id),
    foreign key (client_id) references client (client_id)
);
```

## Rows

- total=5369

| column | latest | sample | sample |
|---|---|---|---|
| disp_id | 13690 | 2257 | 1106 |
| client_id | 13998 | 2257 | 1106 |
| account_id | 11382 | 1861 | 917 |
| type | OWNER | OWNER | DISPONENT |

## Columns

- disp_id: unique identifier, int 1..13690
- client_id: unique identifier, int 1..13998
- account_id: 4500 distinct, int 1..11382
- type: "OWNER"=4500, "DISPONENT"=869


# district

```sql
CREATE TABLE district
(
    district_id INTEGER default 0 not null
        primary key,
    A2          TEXT   not null,
    A3          TEXT   not null,
    A4          TEXT       not null,
    A5          TEXT           not null,
    A6          TEXT           not null,
    A7          TEXT           not null,
    A8          INTEGER        not null,
    A9          INTEGER           not null,
    A10         REAL not null,
    A11         INTEGER           not null,
    A12         REAL null,
    A13         REAL not null,
    A14         INTEGER           not null,
    A15         INTEGER        null,
    A16         INTEGER          not null
);
```

## Rows

- total=77

| column | latest | sample | sample |
|---|---|---|---|
| district_id | 77 | 29 | 37 |
| A2 | Vsetin | Rokycany | Litomerice |
| A3 | north Moravia | west Bohemia | north Bohemia |
| A4 | 148545 | 45714 | 114006 |
| A5 | 8 | 52 | 71 |
| A6 | 35 | 10 | 26 |
| A7 | 12 | 5 | 6 |
| A8 | 3 | 1 | 2 |
| A9 | 4 | 6 | 9 |
| A10 | 53.5 | 55.6 | 62.3 |
| A11 | 8909 | 8843 | 9065 |
| A12 | 4 | 2.8 | 4.4 |
| A13 | 5.56 | 3.6 | 5.39 |
| A14 | 113 | 113 | 123 |
| A15 | 3460 | 818 | 4147 |
| A16 | 3590 | 888 | 4166 |

## Columns

- district_id: unique identifier, int 1..77
- A2: all distinct
- A3: "south Moravia"=14, "central Bohemia"=12, "east Bohemia"=11, "north Moravia"=11, "north Bohemia"=10, "west Bohemia"=10, "south Bohemia"=8, "Prague"=1
- A4: all distinct
- A5: 53 distinct
- A6: 36 distinct
- A7: "4"=12, "6"=11, "7"=10, "5"=9, "10"=5, "3"=5, "8"=5, "0"=4, "1"=3, "2"=3, "12"=2, "13"=2, "18"=2, "11"=1, "14"=1, "20"=1, "9"=1
- A8: 1=34, 2=23, 3=12, 0=4, 4=3, 5=1, int 0..5
- A9: 6=14, 4=12, 7=11, 5=10, 8=7, 9=7, 10=7, 1=4, 3=2, 11=2, 2=1, int 1..11
- A10: 70 distinct, num 33.9..100
  - stats: average=63.0351, median=59.8
- A11: 76 distinct, int 8110..12541
  - stats: average=9031.68, median=8814
- A12: 41 distinct, nulls=1, num 0.2..7.3
  - stats: average=3.07237, median=2.8
- A13: 73 distinct, num 0.43..9.4
  - stats: average=3.78701, median=3.6
- A14: 44 distinct, int 81..167
  - stats: average=116.13, median=113
- A15: 75 distinct, nulls=1, int 818..85677
  - stats: average=4850.32, median=2932
- A16: 76 distinct, int 888..99107
  - stats: average=5030.83, median=3040


# loan

```sql
CREATE TABLE loan
(
    loan_id    INTEGER default 0 not null
        primary key,
    account_id INTEGER           not null,
    date       DATE          not null,
    amount     INTEGER           not null,
    duration   INTEGER           not null,
    payments   REAL not null,
    status     TEXT    not null,
    foreign key (account_id) references account (account_id)
);
```

## Rows

- total=682

| column | latest | sample | sample |
|---|---|---|---|
| loan_id | 7308 | 5772 | 6185 |
| account_id | 11362 | 3906 | 5774 |
| date | 1996-12-27 | 1998-03-08 | 1995-11-28 |
| amount | 129408 | 334620 | 31176 |
| duration | 24 | 60 | 24 |
| payments | 5392 | 5577 | 1299 |
| status | A | C | A |

## Columns

- loan_id: unique identifier, int 4959..7308
- account_id: unique identifier, int 2..11362
- date: 559 distinct
- amount: 645 distinct, int 4980..590820
  - stats: average=151410, median=116928
- duration: 60=145, 24=138, 48=138, 12=131, 36=130, int 12..60
- payments: 577 distinct, num 304..9910
  - stats: average=4190.66, median=3934
- status: "C"=403, "A"=203, "D"=45, "B"=31


# order

```sql
CREATE TABLE `order`
(
    order_id   INTEGER default 0 not null
        primary key,
    account_id INTEGER           not null,
    bank_to    TEXT    not null,
    account_to INTEGER           not null,
    amount     REAL not null,
    k_symbol   TEXT    not null,
    foreign key (account_id) references account (account_id)
);
```

## Rows

- total=6471

| column | latest | sample | sample |
|---|---|---|---|
| order_id | 46338 | 33162 | 33192 |
| account_id | 11362 | 2542 | 2557 |
| bank_to | MN | AB | YZ |
| account_to | 61540514 | 12512219 | 31457412 |
| amount | 5392 | 2637 | 2806 |
| k_symbol | UVER |  | SIPO |

## Columns

- order_id: unique identifier, int 29401..46338
- account_id: 3758 distinct, int 1..11362
- bank_to: "QR"=531, "YZ"=521, "AB"=519, "WX"=515, "ST"=511, "KL"=500, "UV"=499, "IJ"=496, "GH"=487, "OP"=485, "EF"=483, "MN"=466, "CD"=458
- account_to: 6446 distinct, int 399..99994199
  - stats: average=4.9399e+07, median=4.97561e+07
- amount: 4412 distinct, num 1..14882
  - stats: average=3280.64, median=2596
- k_symbol: "SIPO"=3502, ""=1379, "UVER"=717, "POJISTNE"=532, "LEASING"=341


# trans

```sql
CREATE TABLE trans
(
    trans_id   INTEGER default 0    not null
        primary key,
    account_id INTEGER default 0    not null,
    date       DATE             not null,
    type       TEXT       not null,
    operation  TEXT      null,
    amount     INTEGER              not null,
    balance    INTEGER             not null,
    k_symbol   TEXT      null,
    bank       TEXT       null,
    account    INTEGER          null,
    foreign key (account_id) references account (account_id)
);
```

## Rows

- total=1056320

| column | latest | sample | sample |
|---|---|---|---|
| trans_id | 3682987 | 688384 | 1164269 |
| account_id | 10451 | 2351 | 3986 |
| date | 1998-12-31 | 1998-06-09 | 1998-05-16 |
| type | PRIJEM | PRIJEM | PRIJEM |
| operation | null | VKLAD | VKLAD |
| amount | 42 | 29252 | 3800 |
| balance | 13695 | 73885 | 34637 |
| k_symbol | UROK | null | null |
| bank | null | null | null |
| account | null | null | null |

## Columns

- trans_id: unique identifier, int 1..3682987
- account_id: int 1..11382
- date: profile metrics skipped
- type: profile metrics skipped
- operation: nulls=183114
- amount: int 0..87400
- balance: int -41126..209637
- k_symbol: nulls=481881
- bank: nulls=782812
- account: nulls=760931, int 0..99994199
