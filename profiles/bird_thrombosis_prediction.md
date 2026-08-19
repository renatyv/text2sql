---
generator: db-snooper
version: 0.0.26
generated_at_utc: 2026-08-16T07:19:20.255488Z
dialect: sqlite
database: /Users/renatyuldashev/Documents/ai-sql/custom-bench/data/bird_mini_dev/databases/dev_databases/thrombosis_prediction/thrombosis_prediction.sqlite
schema: main
---

## Relationships

- Patient.ID ← Examination.ID, Laboratory.ID

# Examination

```sql
CREATE TABLE Examination
(
    ID                 INTEGER          null,
    `Examination Date` DATE         null,
    `aCL IgG`          REAL        null,
    `aCL IgM`          REAL        null,
    ANA                INTEGER          null,
    `ANA Pattern`      TEXT null,
    `aCL IgA`          INTEGER          null,
    Diagnosis          TEXT null,
    KCT                TEXT null,
    RVVT              TEXT null,
    LAC                TEXT null,
    Symptoms           TEXT null,
    Thrombosis         INTEGER          null,
    foreign key (ID) references Patient (ID)
            on update cascade on delete cascade
);
```

## Rows

- total=106

| column | latest | sample | sample |
|---|---|---|---|
| ID | 5779550 | null | 163109 |
| Examination Date | 1998-03-31 | 1998-01-16 | 1997-07-01 |
| aCL IgG | 0 | 0 | 6.1 |
| aCL IgM | 2.5 | 2 | 9.5 |
| ANA | 4 | 16 | 4096 |
| ANA Pattern | S | P | S |
| aCL IgA | 0 | 0 | 9 |
| Diagnosis | SLE susp | null | null |
| KCT | null | null | - |
| RVVT | null | null | + |
| LAC | null | null | + |
| Symptoms | null | null | CNS lupus |
| Thrombosis | 0 | 0 | 2 |

## Columns

- ID: 69 distinct, nulls=36, int 14872..5779550
  - stats: average=3.21898e+06, median=3.7128e+06
- Examination Date: 94 distinct, nulls=4
- aCL IgG: 33 distinct, num 0..2150.3
  - stats: average=33.3887, median=0.8
- aCL IgM: 49 distinct, num 0..200
  - stats: average=4.94906, median=2
- ANA: 0=20, 16=17, 64=14, 4=11, 256=11, 1024=7, 4096=7, nulls=19, int 0..4096
- ANA Pattern: "S"=31, "P"=19, "P,S"=12, "D,P,S"=1, "S,D"=1, "S,P"=1, nulls=41
- aCL IgA: 21 distinct, int 0..223
  - stats: average=7.89623, median=0
- Diagnosis: 44 distinct, nulls=24
- KCT: "-"=15, "+"=6, nulls=85
- RVVT: "-"=14, "+"=7, nulls=85
- LAC: "-"=16, "+"=9, nulls=81
- Symptoms: "Apo"=2, "CNS lupus"=2, "AMI"=1, "CNS susp"=1, "CVA, epilepsy"=1, "DVT"=1, "PH"=1, "brain infarction"=1, "thrombocytopenia"=1, "thrombophlebitis"=1, nulls=94
- Thrombosis: 0=94, 1=8, 2=3, 3=1, int 0..3


# Laboratory

```sql
CREATE TABLE Laboratory
(
    ID        INTEGER  default 0            not null,
    Date      DATE default '0000-00-00' not null,
    GOT       INTEGER                       null,
    GPT       INTEGER                        null,
    LDH       INTEGER                        null,
    ALP       INTEGER                        null,
    TP        REAL             null,
    ALB       REAL             null,
    UA        REAL             null,
    UN        INTEGER                       null,
    CRE       REAL             null,
    `T-BIL`   REAL             null,
    `T-CHO`   INTEGER                       null,
    TG        INTEGER                       null,
    CPK       INTEGER                       null,
    GLU       INTEGER                       null,
    WBC       REAL             null,
    RBC       REAL             null,
    HGB       REAL             null,
    HCT       REAL             null,
    PLT       INTEGER                       null,
    PT        REAL             null,
    APTT      INTEGER                       null,
    FG        REAL             null,
    PIC       INTEGER                       null,
    TAT       INTEGER                       null,
    TAT2      INTEGER                       null,
    `U-PRO`   TEXT              null,
    IGG       INTEGER                       null,
    IGA       INTEGER                       null,
    IGM       INTEGER                       null,
    CRP       TEXT              null,
    RA        TEXT              null,
    RF        TEXT              null,
    C3        INTEGER                       null,
    C4        INTEGER                       null,
    RNP       TEXT              null,
    SM        TEXT              null,
    SC170     TEXT              null,
    SSA       TEXT              null,
    SSB       TEXT              null,
    CENTROMEA TEXT              null,
    DNA       TEXT              null,
    `DNA-II`  INTEGER                       null,
    primary key (ID, Date),
        foreign key (ID) references Patient (ID)
            on update cascade on delete cascade
);
```

## Rows

- total=13908

| column | latest | sample | sample |
|---|---|---|---|
| ID | 5452747 | 1086485 | 1614305 |
| Date | 1998-11-17 | 1981-08-03 | 1983-12-05 |
| GOT | 20 | null | 46 |
| GPT | 16 | null | 37 |
| LDH | 211 | null | 209 |
| ALP | 241 | null | 103 |
| TP | 8.1 | null | 8.1 |
| ALB | 4.5 | null | 4.8 |
| UA | 4.3 | null | 3.3 |
| UN | 14 | null | 10 |
| CRE | 0.5 | null | 0.9 |
| T-BIL | 0.3 | null | 0.4 |
| T-CHO | 247 | null | 244 |
| TG | null | null | null |
| CPK | null | null | 414 |
| GLU | 127 | null | null |
| WBC | 12 | 4.7 | 4.6 |
| RBC | 4.5 | 4.1 | 4.7 |
| HGB | 14 | 12.2 | 9.4 |
| HCT | 41.7 | 37.4 | 31 |
| PLT | 327 | null | null |
| PT | null | null | null |
| APTT | null | null | null |
| FG | null | null | null |
| PIC | null | null | null |
| TAT | null | null | null |
| TAT2 | null | null | null |
| U-PRO | - | TR | null |
| IGG | 1210 | null | null |
| IGA | 345 | null | null |
| IGM | 88 | null | null |
| CRP | null | - | <0.002 |
| RA | - | - | null |
| RF | null | <40 | null |
| C3 | null | null | null |
| C4 | null | null | null |
| RNP | null | null | null |
| SM | null | null | null |
| SC170 | null | null | null |
| SSA | null | null | null |
| SSB | null | null | null |
| CENTROMEA | null | null | null |
| DNA | null | null | null |
| DNA-II | null | null | null |

## Columns

- ID: 302 distinct, int 27654..5452747
  - stats: average=3.16549e+06, median=3.21599e+06
  - top_values: 2933261=226, 3182521=200, 444499=183, 2315140=166, 4884792=165, 2343945=147, 5122312=135, 4790235=130, 2370675=129, 2395148=126
- Date: 3723 distinct
  - top_values: 1985-11-11=26, 1985-09-09=25, 1984-10-01=22, 1985-05-13=21, 1984-12-17=20, 1985-04-22=20, 1985-12-09=20, 1981-05-11=19, 1985-05-20=19, 1984-01-09=18
- GOT: 218 distinct, nulls=2630, int 3..21480
  - stats: average=28.8021, median=20
- GPT: 302 distinct, nulls=2634, int 1..4780
  - stats: average=30.4459, median=18
- LDH: 917 distinct, nulls=2603, int 25..67080
  - stats: average=322.266, median=295
- ALP: 532 distinct, nulls=2757, int 11..1308
  - stats: average=122.448, median=101
- TP: 62 distinct, nulls=2790, num 0..9.9
  - stats: average=7.12418, median=7.1
- ALB: 39 distinct, nulls=2840, num 1..5.8
  - stats: average=4.14287, median=4.2
- UA: 132 distinct, nulls=2805, num 0.4..17.3
  - stats: average=4.39502, median=4.3
- UN: 108 distinct, nulls=2670, int 0..152
  - stats: average=15.4022, median=14
- CRE: 65 distinct, nulls=2655, num 0.1..17.1
  - stats: average=0.791309, median=0.7
- T-BIL: 40 distinct, nulls=4287, num 0.1..7.9
  - stats: average=0.533209, median=0.5
- T-CHO: 325 distinct, nulls=3244, int 37..568
  - stats: average=203.058, median=198
- TG: 392 distinct, nulls=7471, int 1..867
  - stats: average=125.229, median=108
- CPK: 463 distinct, nulls=8892, int 0..10835
  - stats: average=100.403, median=35.5
- GLU: 208 distinct, nulls=12203, int 62..499
  - stats: average=115.745, median=102
- WBC: 217 distinct, nulls=1827, num 0.9..35.2
  - stats: average=7.56596, median=7
- RBC: 56 distinct, nulls=1827, num 0.4..6.6
  - stats: average=4.3184, median=4.3
- HGB: 138 distinct, nulls=1827, num 1.3..18.9
  - stats: average=12.423, median=12.5
- HCT: 363 distinct, nulls=1827, num 3..56
  - stats: average=37.9283, median=38.1
- PLT: 657 distinct, nulls=2621, int 5..5844
  - stats: average=263.011, median=248
- PT: 104 distinct, nulls=13287, num 10.1..27
  - stats: average=13.2717, median=12.4
- APTT: 27 distinct, nulls=13857, int 57..146
  - stats: average=97.3333, median=95
- FG: 279 distinct, nulls=13453, num 23.8..106.5
  - stats: average=43.2855, median=39
- PIC: 63 distinct, nulls=13832, int 114..700
  - stats: average=322.342, median=267
- TAT: 82 distinct, nulls=13766, int 63..183
  - stats: average=121.387, median=118
- TAT2: 60 distinct, nulls=13789, int 59..155
  - stats: average=116.395, median=118
- U-PRO: "-"=4579, "0"=2748, "TR"=866, "30"=398, "1"=319, "2"=313, "3"=148, "100"=138, "300"=57, "-15"=37, "4"=21, "+1(30)"=18, ">=1000"=11, ">=300"=6, "%%"=4, "+2(100)"=4, nulls=4241
- IGG: 1516 distinct, nulls=11228, int 3..6510
  - stats: average=1800.41, median=1666
- IGA: 682 distinct, nulls=11228, int 1..1765
  - stats: average=368.798, median=343
- IGM: 487 distinct, nulls=11230, int 0..1573
  - stats: average=190.225, median=152
- CRP: 211 distinct, nulls=2453
- RA: "-"=1684, "+"=658, "2+"=323, "+-"=189, "7-"=1, nulls=11053
- RF: 903 distinct, nulls=10571
- C3: 151 distinct, nulls=8447, int 15..196
  - stats: average=70.7028, median=69
- C4: 62 distinct, nulls=8447, int 3..80
  - stats: average=22.2679, median=21
- RNP: "0"=72, "negative"=22, "4"=14, "1"=10, "16"=10, "64"=8, "256"=6, "15"=1, nulls=13765
- SM: "0"=102, "negative"=20, "1"=4, "2"=1, "8"=1, nulls=13780
- SC170: "0"=12, "negative"=12, "4"=2, "1"=1, "16"=1, nulls=13880
- SSA: "0"=41, "negative"=27, "16"=11, "64"=8, "1"=5, "4"=5, "256"=2, nulls=13809
- SSB: "0"=58, "negative"=30, "32"=2, "1"=1, "2"=1, "8"=1, nulls=13815
- CENTROMEA: "0"=11, "negative"=4, nulls=13893
- DNA: 66 distinct, nulls=13839
- DNA-II: all NULL


# Patient

```sql
CREATE TABLE Patient
(
    ID           INTEGER default 0 not null
        primary key,
    SEX          TEXT  null,
    Birthday     DATE          null,
    Description  DATE          null,
    `First Date` DATE          null,
    Admission    TEXT  null,
    Diagnosis    TEXT  null
);
```

## Rows

- total=1238

| column | latest | sample | sample |
|---|---|---|---|
| ID | 5845877 | 5437753 | 4988540 |
| SEX | F | F | M |
| Birthday | 1951-12-13 | 1980-01-20 | 1931-07-10 |
| Description | 1998-09-02 | null | 1994-02-14 |
| First Date | 1998-08-28 | 1996-01-25 | 1993-06-28 |
| Admission | + | + | - |
| Diagnosis | Weber-Christian, PM | SLE | RA |

## Columns

- ID: unique identifier, int 2110..5845877
  - stats: average=3.96171e+06, median=4.53395e+06
- SEX: "F"=1023, "M"=202, ""=13
- Birthday: 1193 distinct, nulls=1
- Description: 97 distinct, nulls=216
- First Date: 797 distinct, nulls=251
- Admission: "-"=713, "+"=488, ""=34, "+("=3
- Diagnosis: 220 distinct
