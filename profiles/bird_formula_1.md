---
generator: db-snooper
version: 0.0.34
generated_at_utc: 2026-08-24T21:21:17.405221Z
dialect: sqlite
database: /var/folders/9j/b9bx_drd53sc6zbpsqyrjy4h0000gn/T/dbsnoop-xnsadlmr/formula_1.sqlite
schema: main
---

## Relationships

- "circuits"."circuitId" ← "races"."circuitId"
- "constructors"."constructorId" ← "constructorResults"."constructorId", "constructorStandings"."constructorId", "qualifying"."constructorId", "results"."constructorId"
- "drivers"."driverId" ← "driverStandings"."driverId", "lapTimes"."driverId", "pitStops"."driverId", "qualifying"."driverId", "results"."driverId"
- "races"."raceId" ← "constructorResults"."raceId", "constructorStandings"."raceId", "driverStandings"."raceId", "lapTimes"."raceId", "pitStops"."raceId", "qualifying"."raceId", "results"."raceId"
- "seasons"."year" ← "races"."year"
- "status"."statusId" ← "results"."statusId"

# "circuits"  (rows=72)

columns:
"circuitId" int PK: unique identifier, 2..73, avg=37.5, median=37.5
"circuitRef" text NOTNULL: all distinct
"name" text NOTNULL: all distinct
"location" text: 69 distinct
"country" text: 32 distinct
"lat" float: 71 distinct, -34.9272..57.2653, avg=34.8685, median=41.3783
"lng" float: 71 distinct, -118.189..138.927, avg=-0.26669, median=3.54722
"alt" int: all NULL
"url" text NOTNULL: all distinct

indexes: none

samples:
| column | latest | sample | sample |
|---|---|---|---|
| circuitId | 73 | 30 | 12 |
| circuitRef | BAK | kyalami | valencia |
| name | Baku City Circuit | Kyalami | Valencia Street Circuit |
| location | Baku | Midrand | Valencia |
| country | Azerbaijan | South Africa | Spain |
| lat | 40.3725 | -25.9894 | 39.4589 |
| lng | 49.8533 | 28.0767 | -0.331667 |
| alt | null | null | null |
| url | http://en.wikipedia.org/wiki/Baku_City_Circuit | http://en.wikipedia.org/wiki/Kyalami | http://en.wikipedia.org/wiki/Valencia_Street_Circuit |

# "constructorResults"  (rows=11082)

columns:
"constructorResultsId" int PK: unique identifier, 1..15579, avg=7319.37, median=5541.5
"raceId" int NOTNULL FK: 907 distinct, 1..982, avg=453.535, median=438
"constructorId" int NOTNULL FK: 172 distinct, 1..210, avg=41.2624, median=24
"points" float: 45 distinct, 0..66, avg=3.15525, median=0
"status" text: "D"=17, nulls=11065

indexes: none

samples:
| column | latest | sample | sample |
|---|---|---|---|
| constructorResultsId | 15579 | 12977 | 11113 |
| raceId | 982 | 565 | 694 |
| constructorId | 6 | 56 | 167 |
| points | 0 | 1 | 0 |
| status | null | null | null |

# "constructorStandings"  (rows=11836)

columns:
"constructorStandingsId" int PK: unique identifier, 1..26872, avg=15141.5, median=11496.5
"raceId" int NOTNULL FK: 906 distinct, 1..982, avg=466.488, median=461
"constructorId" int NOTNULL FK: 156 distinct, 1..210, avg=45.6973, median=25
"points" float NOTNULL: 436 distinct, 0..765, avg=26.3847, median=6
"position" int: 22 distinct, 1..22, avg=7.45091, median=7
"positionText" text: digits, 23 distinct
"wins" int NOTNULL: 20 distinct, 0..19, avg=0.638729, median=0

indexes: none

samples:
| column | latest | sample | sample |
|---|---|---|---|
| constructorStandingsId | 26872 | 24591 | 24379 |
| raceId | 982 | 846 | 348 |
| constructorId | 210 | 6 | 131 |
| points | 37 | 93 | 132 |
| position | 8 | 3 | 4 |
| positionText | 8 | 3 | 4 |
| wins | 0 | 0 | 0 |

# "constructors"  (rows=208)

columns:
"constructorId" int PK: unique identifier, 1..210, avg=105.514, median=105.5
"constructorRef" text NOTNULL: all distinct
"name" text NOTNULL: all distinct
"nationality" text: 24 distinct
"url" text NOTNULL: 171 distinct

indexes: none

samples:
| column | latest | sample | sample |
|---|---|---|---|
| constructorId | 210 | 199 | 197 |
| constructorRef | haas | march-alfa_romeo | brm-ford |
| name | Haas F1 Team | March-Alfa Romeo | BRM-Ford |
| nationality | American | British | British |
| url | http://en.wikipedia.org/wiki/Haas_F1_Team | http://en.wikipedia.org/wiki/March_Engineering | http://en.wikipedia.org/wiki/BRM |

# "driverStandings"  (rows=31578)

columns:
"driverStandingsId" int PK: unique identifier, 1..68460, avg=39409.4, median=47373.5
"raceId" int NOTNULL FK: 970 distinct, 1..982, avg=535.826, median=564
"driverId" int NOTNULL FK: 833 distinct, 1..841, avg=278.727, median=204
"points" float NOTNULL: 337 distinct, 0..397, avg=10.3378, median=0
"position" int: 108 distinct, 1..108, avg=20.6076, median=17
"positionText" text: digits, 109 distinct
"wins" int NOTNULL: 0=27946, 1=1898, 2=744, 3=382, 4=223, 5=145, 6=116, 7=50, 8=25, 9=21, 10=13, 11=7, 12=5, 13=3, 0..13

indexes: none

samples:
| column | latest | sample | sample |
|---|---|---|---|
| driverStandingsId | 68460 | 57934 | 3321 |
| raceId | 982 | 549 | 169 |
| driverId | 814 | 256 | 55 |
| points | 0 | 0 | 0 |
| position | 23 | 29 | 22 |
| positionText | 23 | 29 | 22 |
| wins | 0 | 0 | 0 |

# "drivers"  (rows=840)

columns:
"driverId" int PK: unique identifier, 1..841, avg=420.538, median=420.5
"driverRef" text NOTNULL: all distinct
"number" int: all distinct, nulls=804, 2..99, avg=30.8333, median=21.5
"code" text: 80 distinct, nulls=757
"forename" text NOTNULL: 465 distinct
"surname" text NOTNULL: 784 distinct
"dob" date: 821 distinct, nulls=1
"nationality" text: 41 distinct
"url" text NOTNULL: all distinct

indexes: none

samples:
| column | latest | sample | sample |
|---|---|---|---|
| driverId | 841 | 392 | 329 |
| driverRef | giovinazzi | fisher | beuttler |
| number | 36 | null | null |
| code | GIO | null | null |
| forename | Antonio | Mike | Mike |
| surname | Giovinazzi | Fisher | Beuttler |
| dob | 1993-12-14 | 1943-03-13 | 1940-04-13 |
| nationality | Italian | American | British |
| url | http://en.wikipedia.org/wiki/Antonio_Giovinazzi | http://en.wikipedia.org/wiki/Mike_Fisher_(driver) | http://en.wikipedia.org/wiki/Mike_Beuttler |

# "lapTimes"  (rows=≈400524)

columns:
"raceId" int PK FK
"driverId" int PK FK
"lap" int PK
"position" int
"time" text
"milliseconds" int

indexes: none


# "pitStops"  (rows=5815)

columns:
"raceId" int PK FK: 124 distinct, 842..982, avg=906.012, median=901, 936=96, 851=88, 844=82, 970=82, 982=82, 884=79, 914=79, 845=77, 861=76, 956=76
"driverId" int PK FK: 54 distinct, 1..841, avg=424.956, median=155, 13=293, 1=273, 20=268, 4=260, 817=257, 815=252, 18=245, 3=240, 807=215, 8=209
"stop" int PK: 1=2552, 2=2005, 3=932, 4=250, 5=63, 6=13, 1..6
"lap" int NOTNULL: 73 distinct, 1..74, avg=25.1001, median=25
"time" text NOTNULL: 4650 distinct
"duration" text: 4580 distinct
"milliseconds" int: 4580 distinct, 12897..2011266, avg=46307.8, median=23356

indexes: none

samples:
| column | latest | sample | sample |
|---|---|---|---|
| raceId | 982 | 955 | 898 |
| driverId | 840 | 830 | 818 |
| stop | 4 | 2 | 1 |
| lap | 26 | 20 | 27 |
| time | 21:05:07 | 17:41:33 | 13:54:22 |
| duration | 29.412 | 22.497 | 24.381 |
| milliseconds | 29412 | 22497 | 24381 |

# "qualifying"  (rows=6967)

columns:
"qualifyId" int PK: unique identifier, 23..7419, avg=3719.18, median=3703
"raceId" int NOTNULL FK: 319 distinct, 2..982, avg=443.562, median=258
"driverId" int NOTNULL FK: 151 distinct, 1..841, avg=198.587, median=30
"constructorId" int NOTNULL FK: 41 distinct, 1..210, avg=34.8665, median=9
"number" int NOTNULL: 48 distinct, 0..99, avg=15.1672, median=12
"position" int: 28 distinct, 1..28, avg=11.5019, median=11
"q1" text: 6283 distinct, nulls=109
"q2" text: 3222 distinct, nulls=3577
"q3" text: 1959 distinct, nulls=4935

indexes: none

samples:
| column | latest | sample | sample |
|---|---|---|---|
| qualifyId | 7419 | 1144 | 1078 |
| raceId | 982 | 77 | 68 |
| driverId | 828 | 4 | 30 |
| constructorId | 15 | 4 | 6 |
| number | 9 | 5 | 5 |
| position | 20 | 6 | 6 |
| q1 | 1:45.570 | 1:31.056 | 1:47.366 |
| q2 | null | null | 1:45.660 |
| q3 | null | null | 1:45.775 |

# "races"  (rows=954)

columns:
"raceId" int PK: unique identifier, 2..988, avg=491.922, median=492.5
"year" int NOTNULL FK: 68 distinct, 1950..2017, avg=1987.95, median=1989
"round" int NOTNULL: 21 distinct, 1..21, avg=8.33648, median=8
"circuitId" int NOTNULL FK: 71 distinct, 2..73, avg=22.1719, median=18
"name" text NOTNULL: 42 distinct
"date" date NOTNULL: all distinct
"time" text: "12:00:00"=107, "14:00:00"=26, "06:00:00"=13, "07:00:00"=11, "13:00:00"=11, "16:00:00"=11, "15:00:00"=8, "19:00:00"=8, "17:00:00"=6, "18:00:00"=6, "05:00:00"=5, "08:00:00"=5, "11:00:00"=4, "09:30:00"=3, "04:30:00"=2, "11:30:00"=2, "14:30:00"=2, "09:00:00"=1, "20:00:00"=1, nulls=722
"url" text UNIQ: unique identifier

indexes: none

samples:
| column | latest | sample | sample |
|---|---|---|---|
| raceId | 988 | 622 | 57 |
| year | 2017 | 1972 | 2006 |
| round | 20 | 3 | 5 |
| circuitId | 24 | 45 | 20 |
| name | Abu Dhabi Grand Prix | Spanish Grand Prix | European Grand Prix |
| date | 2017-11-26 | 1972-05-01 | 2006-05-07 |
| time | 17:00:00 | null | 14:00:00 |
| url | https://en.wikipedia.org/wiki/2017_Abu_Dhabi_Grand_Prix | http://en.wikipedia.org/wiki/1972_Spanish_Grand_Prix | http://en.wikipedia.org/wiki/2006_European_Grand_Prix |

# "results"  (rows=23179)

columns:
"resultId" int PK: unique identifier, 23..23661, avg=11873.6, median=11892
"raceId" int NOTNULL FK: 948 distinct, 2..982, avg=486.903, median=479
"driverId" int NOTNULL FK: 839 distinct, 1..841, avg=225.852, median=156
"constructorId" int NOTNULL FK: 207 distinct, 1..210, avg=46.6559, median=25
"number" int: 128 distinct, nulls=6, 0..208, avg=16.977, median=15
"grid" int NOTNULL: 35 distinct, 0..34, avg=11.2768, median=11
"position" int: 33 distinct, nulls=10326, 1..33, avg=7.78869, median=7
"positionText" text NOTNULL: 39 distinct
"positionOrder" int NOTNULL: 39 distinct, 1..39, avg=13.1293, median=13
"points" float NOTNULL: 33 distinct, 0..50, avg=1.56208, median=0
"laps" int NOTNULL: 172 distinct, 0..200, avg=45.312, median=52
"time" text: 5588 distinct, nulls=17390
"milliseconds" int: 5751 distinct, nulls=17391, 1474899..15090540, avg=6.3e+06, median=5.9e+06
"fastestLap" int: 77 distinct, nulls=18185, 2..78, avg=41.1584, median=44
"rank" int: 25 distinct, nulls=18057, 0..24, avg=10.6613, median=11
"fastestLapTime" text: 4709 distinct, nulls=18185
"fastestLapSpeed" text: numeric, 4794 distinct, nulls=18185
"statusId" int NOTNULL FK: 131 distinct, 1..136, avg=18.4415, median=11

indexes: none

samples:
| column | latest | sample | sample |
|---|---|---|---|
| resultId | 23661 | 14718 | 1215 |
| raceId | 982 | 597 | 74 |
| driverId | 8 | 224 | 40 |
| constructorId | 6 | 1 | 18 |
| number | 7 | 5 | 20 |
| grid | 4 | 3 | 19 |
| position | null | 3 | null |
| positionText | R | 3 | R |
| positionOrder | 20 | 3 | 17 |
| points | 0 | 4 | 0 |
| laps | 0 | 75 | 8 |
| time | null | +30.27 | null |
| milliseconds | null | 6210620 | null |
| fastestLap | null | null | 5 |
| rank | 0 | null | 20 |
| fastestLapTime | null | null | 1:28.334 |
| fastestLapSpeed | null | null | 201.041 |
| statusId | 3 | 1 | 8 |

# "seasons"  (rows=68)

columns:
"year" int PK: unique identifier, 1950..2017, avg=1983.5, median=1983.5
"url" text NOTNULL: all distinct

indexes: none

samples:
| column | latest | sample | sample |
|---|---|---|---|
| year | 2017 | 1953 | 1970 |
| url | https://en.wikipedia.org/wiki/2017_Formula_One_season | http://en.wikipedia.org/wiki/1953_Formula_One_season | http://en.wikipedia.org/wiki/1970_Formula_One_season |

# "status"  (rows=134)

columns:
"statusId" int PK: unique identifier, 1..136, avg=68.709, median=69.5
"status" text NOTNULL: all distinct

indexes: none

samples:
| column | latest | sample | sample |
|---|---|---|---|
| statusId | 136 | 125 | 67 |
| status | Seat | +46 Laps | Wheel bearing |
