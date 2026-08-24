---
generator: db-snooper
version: 0.0.34
generated_at_utc: 2026-08-24T21:56:14.997378Z
dialect: sqlite
database: /var/folders/9j/b9bx_drd53sc6zbpsqyrjy4h0000gn/T/dbsnoop-ij2xuh0a/thrombosis_prediction.sqlite
schema: main
---

## Relationships

- "Patient"."ID" ← "Examination"."ID", "Laboratory"."ID"

# "Examination"  (rows=106)

columns:
"ID" int FK: 69 distinct, nulls=36, 14872..5779550
"Examination Date" date: 94 distinct, nulls=4
"aCL IgG" float: 33 distinct, 0..2150.3, avg=33.3887, median=0.8
"aCL IgM" float: 49 distinct, 0..200, avg=4.94906, median=2
"ANA" int: 0=20, 16=17, 64=14, 4=11, 256=11, 1024=7, 4096=7, nulls=19, 0..4096
"ANA Pattern" text: "S"=31, "P"=19, "P,S"=12, "D,P,S"=1, "S,D"=1, "S,P"=1, nulls=41
"aCL IgA" int: 21 distinct, 0..223, avg=7.89623, median=0
"Diagnosis" text: 44 distinct, nulls=24
"KCT" text: "-"=15, "+"=6, nulls=85
"RVVT" text: "-"=14, "+"=7, nulls=85
"LAC" text: "-"=16, "+"=9, nulls=81
"Symptoms" text: "Apo"=2, "CNS lupus"=2, "AMI"=1, "CNS susp"=1, "CVA, epilepsy"=1, "DVT"=1, "PH"=1, "brain infarction"=1, "thrombocytopenia"=1, "thrombophlebitis"=1, nulls=94
"Thrombosis" int: 0=94, 1=8, 2=3, 3=1, 0..3

indexes: none

samples:
| column | latest | sample | sample |
|---|---|---|---|
| ID | 5779550 | 1787610 | 4860570 |
| Examination Date | 1998-03-31 | 1997-06-17 | 1996-11-18 |
| aCL IgG | 0 | 1.1 | 0 |
| aCL IgM | 2.5 | 3.2 | 1.1 |
| ANA | 4 | 64 | 4 |
| ANA Pattern | S | S | P |
| aCL IgA | 0 | 6 | 0 |
| Diagnosis | SLE susp | PSS, MCTD | SjS |
| KCT | null | null | null |
| RVVT | null | null | null |
| LAC | null | null | null |
| Symptoms | null | null | null |
| Thrombosis | 0 | 0 | 0 |

# "Laboratory"  (rows=13908)

columns:
"ID" int PK FK: 302 distinct, 27654..5452747, 2933261=226, 3182521=200, 444499=183, 2315140=166, 4884792=165, 2343945=147, 5122312=135, 4790235=130, 2370675=129, 2395148=126
"Date" date PK: 3723 distinct, "1985-11-11"=26, "1985-09-09"=25, "1984-10-01"=22, "1985-05-13"=21, "1984-12-17"=20, "1985-04-22"=20, "1985-12-09"=20, "1981-05-11"=19, "1985-05-20"=19, "1984-01-09"=18
"GOT" int: 218 distinct, nulls=2630, 3..21480, avg=28.8021, median=20
"GPT" int: 302 distinct, nulls=2634, 1..4780, avg=30.4459, median=18
"LDH" int: 917 distinct, nulls=2603, 25..67080, avg=322.266, median=295
"ALP" int: 532 distinct, nulls=2757, 11..1308, avg=122.448, median=101
"TP" float: 62 distinct, nulls=2790, 0..9.9, avg=7.12418, median=7.1
"ALB" float: 39 distinct, nulls=2840, 1..5.8, avg=4.14287, median=4.2
"UA" float: 132 distinct, nulls=2805, 0.4..17.3, avg=4.39502, median=4.3
"UN" int: 108 distinct, nulls=2670, 0..152, avg=15.4022, median=14
"CRE" float: 65 distinct, nulls=2655, 0.1..17.1, avg=0.791309, median=0.7
"T-BIL" float: 40 distinct, nulls=4287, 0.1..7.9, avg=0.533209, median=0.5
"T-CHO" int: 325 distinct, nulls=3244, 37..568, avg=203.058, median=198
"TG" int: 392 distinct, nulls=7471, 1..867, avg=125.229, median=108
"CPK" int: 463 distinct, nulls=8892, 0..10835, avg=100.403, median=35.5
"GLU" int: 208 distinct, nulls=12203, 62..499, avg=115.745, median=102
"WBC" float: 217 distinct, nulls=1827, 0.9..35.2, avg=7.56596, median=7
"RBC" float: 56 distinct, nulls=1827, 0.4..6.6, avg=4.3184, median=4.3
"HGB" float: 138 distinct, nulls=1827, 1.3..18.9, avg=12.423, median=12.5
"HCT" float: 363 distinct, nulls=1827, 3..56, avg=37.9283, median=38.1
"PLT" int: 657 distinct, nulls=2621, 5..5844, avg=263.011, median=248
"PT" float: 104 distinct, nulls=13287, 10.1..27, avg=13.2717, median=12.4
"APTT" int: 27 distinct, nulls=13857, 57..146, avg=97.3333, median=95
"FG" float: 279 distinct, nulls=13453, 23.8..106.5, avg=43.2855, median=39
"PIC" int: 63 distinct, nulls=13832, 114..700, avg=322.342, median=267
"TAT" int: 82 distinct, nulls=13766, 63..183, avg=121.387, median=118
"TAT2" int: 60 distinct, nulls=13789, 59..155, avg=116.395, median=118
"U-PRO" text: "-"=4579, "0"=2748, "TR"=866, "30"=398, "1"=319, "2"=313, "3"=148, "100"=138, "300"=57, "-15"=37, "4"=21, "+1(30)"=18, ">=1000"=11, ">=300"=6, "%%"=4, "+2(100)"=4, nulls=4241
"IGG" int: 1516 distinct, nulls=11228, 3..6510, avg=1800.41, median=1666
"IGA" int: 682 distinct, nulls=11228, 1..1765, avg=368.798, median=343
"IGM" int: 487 distinct, nulls=11230, 0..1573, avg=190.225, median=152
"CRP" text: 211 distinct, nulls=2453
"RA" text: "-"=1684, "+"=658, "2+"=323, "+-"=189, "7-"=1, nulls=11053
"RF" text: 903 distinct, nulls=10571
"C3" int: 151 distinct, nulls=8447, 15..196, avg=70.7028, median=69
"C4" int: 62 distinct, nulls=8447, 3..80, avg=22.2679, median=21
"RNP" text: "0"=72, "negative"=22, "4"=14, "1"=10, "16"=10, "64"=8, "256"=6, "15"=1, nulls=13765
"SM" text: "0"=102, "negative"=20, "1"=4, "2"=1, "8"=1, nulls=13780
"SC170" text: "0"=12, "negative"=12, "4"=2, "1"=1, "16"=1, nulls=13880
"SSA" text: "0"=41, "negative"=27, "16"=11, "64"=8, "1"=5, "4"=5, "256"=2, nulls=13809
"SSB" text: "0"=58, "negative"=30, "32"=2, "1"=1, "2"=1, "8"=1, nulls=13815
"CENTROMEA" text: "0"=11, "negative"=4, nulls=13893
"DNA" text: numeric, 66 distinct, nulls=13839
"DNA-II" int: all NULL

indexes: none

samples:
| column | latest | sample | sample |
|---|---|---|---|
| ID | 5452747 | 4632519 | 1180510 |
| Date | 1998-11-17 | 1996-03-22 | 1997-08-04 |
| GOT | 20 | 13 | 15 |
| GPT | 16 | 6 | 12 |
| LDH | 211 | 379 | 407 |
| ALP | 241 | 116 | 98 |
| TP | 8.1 | 6.8 | 7.1 |
| ALB | 4.5 | 3.9 | 3.9 |
| UA | 4.3 | 5 | 3.9 |
| UN | 14 | 14 | 10 |
| CRE | 0.5 | 1.2 | 0.3 |
| T-BIL | 0.3 | 0.3 | 2.5 |
| T-CHO | 247 | 201 | null |
| TG | null | 74 | null |
| CPK | null | null | null |
| GLU | 127 | null | null |
| WBC | 12 | 9.8 | 3.7 |
| RBC | 4.5 | 3.5 | 3.6 |
| HGB | 14 | 9.8 | 11.2 |
| HCT | 41.7 | 30.8 | 33.3 |
| PLT | 327 | 275 | 229 |
| PT | null | null | null |
| APTT | null | null | null |
| FG | null | null | null |
| PIC | null | null | null |
| TAT | null | null | null |
| TAT2 | null | null | null |
| U-PRO | - | - | - |
| IGG | 1210 | 1583 | null |
| IGA | 345 | 446 | null |
| IGM | 88 | 100 | null |
| CRP | null | 0.3 | <0.3 |
| RA | - | null | null |
| RF | null | 158.2 | null |
| C3 | null | 72 | 46 |
| C4 | null | 27 | 12 |
| RNP | null | null | null |
| SM | null | null | null |
| SC170 | null | null | null |
| SSA | null | null | null |
| SSB | null | null | null |
| CENTROMEA | null | null | null |
| DNA | null | null | null |
| DNA-II | null | null | null |

# "Patient"  (rows=1238)

columns:
"ID" int PK: unique identifier, 2110..5845877
"SEX" text: "F"=1023, "M"=202, ""=13
"Birthday" date: 1193 distinct, nulls=1
"Description" date: 97 distinct, nulls=216
"First Date" date: 797 distinct, nulls=251
"Admission" text: "-"=713, "+"=488, ""=34, "+("=3
"Diagnosis" text: 220 distinct

indexes: none

samples:
| column | latest | sample | sample |
|---|---|---|---|
| ID | 5845877 | 5307308 | 2988883 |
| SEX | F | F | F |
| Birthday | 1951-12-13 | 1957-10-14 | 1940-01-01 |
| Description | 1998-09-02 | 1996-12-05 | 1997-03-27 |
| First Date | 1998-08-28 | 1995-04-11 | null |
| Admission | + | - | - |
| Diagnosis | Weber-Christian, PM | RA | RA, SJS |
