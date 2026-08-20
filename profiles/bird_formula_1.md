---
generator: db-snooper
version: 0.0.31
generated_at_utc: 2026-08-20T17:26:38.295665Z
dialect: sqlite
database: /var/folders/9j/b9bx_drd53sc6zbpsqyrjy4h0000gn/T/dbsnoop-w08da0gy/formula_1.sqlite
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
fk: none

samples:
| column | latest | sample | sample |
|---|---|---|---|
| circuitId | 73 | 40 | 9 |
| circuitRef | BAK | zolder | silverstone |
| name | Baku City Circuit | Zolder | Silverstone Circuit |
| location | Baku | Heusden-Zolder | Silverstone |
| country | Azerbaijan | Belgium | UK |
| lat | 40.3725 | 50.9894 | 52.0786 |
| lng | 49.8533 | 5.25694 | -1.01694 |
| alt | null | null | null |
| url | http://en.wikipedia.org/wiki/Baku_City_Circuit | http://en.wikipedia.org/wiki/Zolder | http://en.wikipedia.org/wiki/Silverstone_Circuit |

# "constructorResults"  (rows=11082)

columns:
"constructorResultsId" int PK: unique identifier, 1..15579, avg=7319.37, median=5541.5
"raceId" int NOTNULL FK: 907 distinct, 1..982, avg=453.535, median=438
"constructorId" int NOTNULL FK: 172 distinct, 1..210, avg=41.2624, median=24
"points" float: 45 distinct, 0..66, avg=3.15525, median=0
"status" text: "D"=17, nulls=11065

indexes: none
fk: "constructorId"→"constructors"."constructorId", "raceId"→"races"."raceId"

samples:
| column | latest | sample | sample |
|---|---|---|---|
| constructorResultsId | 15579 | 14267 | 14077 |
| raceId | 982 | 852 | 351 |
| constructorId | 6 | 15 | 205 |
| points | 0 | 0 | 0 |
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
fk: "raceId"→"races"."raceId", "constructorId"→"constructors"."constructorId"

samples:
| column | latest | sample | sample |
|---|---|---|---|
| constructorStandingsId | 26872 | 20852 | 21643 |
| raceId | 982 | 686 | 653 |
| constructorId | 210 | 90 | 187 |
| points | 37 | 0 | 31 |
| position | 8 | 18 | 5 |
| positionText | 8 | 18 | 5 |
| wins | 0 | 0 | 0 |

# "constructors"  (rows=208)

columns:
"constructorId" int PK: unique identifier, 1..210, avg=105.514, median=105.5
"constructorRef" text NOTNULL: all distinct
"name" text NOTNULL: all distinct
"nationality" text: 24 distinct
"url" text NOTNULL: 171 distinct

indexes: none
fk: none

samples:
| column | latest | sample | sample |
|---|---|---|---|
| constructorId | 210 | 71 | 44 |
| constructorRef | haas | apollon | eurobrun |
| name | Haas F1 Team | Apollon | Euro Brun |
| nationality | American | Swiss | Italian |
| url | http://en.wikipedia.org/wiki/Haas_F1_Team | http://en.wikipedia.org/wiki/Apollon_(Formula_One) | http://en.wikipedia.org/wiki/Euro_Brun |

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
fk: "driverId"→"drivers"."driverId", "raceId"→"races"."raceId"

samples:
| column | latest | sample | sample |
|---|---|---|---|
| driverStandingsId | 68460 | 9605 | 18910 |
| raceId | 982 | 284 | 370 |
| driverId | 814 | 112 | 114 |
| points | 0 | 2 | 0 |
| position | 23 | 15 | 40 |
| positionText | 23 | 15 | 40 |
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
fk: none

samples:
| column | latest | sample | sample |
|---|---|---|---|
| driverId | 841 | 740 | 275 |
| driverRef | giovinazzi | comotti | lombardi |
| number | 36 | null | null |
| code | GIO | null | null |
| forename | Antonio | Franco | Lella |
| surname | Giovinazzi | Comotti | Lombardi |
| dob | 1993-12-14 | 1906-07-24 | 1941-03-26 |
| nationality | Italian | Italian | Italian |
| url | http://en.wikipedia.org/wiki/Antonio_Giovinazzi | http://en.wikipedia.org/wiki/Franco_Comotti | http://en.wikipedia.org/wiki/Lella_Lombardi |

# "lapTimes"  (rows=≈400524)

columns:
"raceId" int PK FK
"driverId" int PK FK
"lap" int PK
"position" int
"time" text
"milliseconds" int

indexes: none
fk: "raceId"→"races"."raceId", "driverId"→"drivers"."driverId"


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
fk: "driverId"→"drivers"."driverId", "raceId"→"races"."raceId"

samples:
| column | latest | sample | sample |
|---|---|---|---|
| raceId | 982 | 843 | 862 |
| driverId | 840 | 153 | 818 |
| stop | 4 | 1 | 2 |
| lap | 26 | 9 | 28 |
| time | 21:05:07 | 15:19:36 | 15:53:07 |
| duration | 29.412 | 22.419 | 23.623 |
| milliseconds | 29412 | 22419 | 23623 |

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
fk: "driverId"→"drivers"."driverId", "raceId"→"races"."raceId", "constructorId"→"constructors"."constructorId"

samples:
| column | latest | sample | sample |
|---|---|---|---|
| qualifyId | 7419 | 4000 | 2055 |
| raceId | 982 | 119 | 225 |
| driverId | 828 | 53 | 57 |
| constructorId | 15 | 18 | 1 |
| number | 9 | 18 | 7 |
| position | 20 | 20 | 7 |
| q1 | 1:45.570 | 1:19.174 | 1:19.607 |
| q2 | null | null | null |
| q3 | null | null | null |

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
fk: "circuitId"→"circuits"."circuitId", "year"→"seasons"."year"

samples:
| column | latest | sample | sample |
|---|---|---|---|
| raceId | 988 | 664 | 721 |
| year | 2017 | 1969 | 1963 |
| round | 20 | 9 | 3 |
| circuitId | 24 | 48 | 39 |
| name | Abu Dhabi Grand Prix | Canadian Grand Prix | Dutch Grand Prix |
| date | 2017-11-26 | 1969-09-20 | 1963-06-23 |
| time | 17:00:00 | null | null |
| url | https://en.wikipedia.org/wiki/2017_Abu_Dhabi_Grand_Prix | http://en.wikipedia.org/wiki/1969_Canadian_Grand_Prix | http://en.wikipedia.org/wiki/1963_Dutch_Grand_Prix |

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
"milliseconds" int: 5751 distinct, nulls=17391, 1474899..15090540, avg=6.32918e+06, median=5.89006e+06
"fastestLap" int: 77 distinct, nulls=18185, 2..78, avg=41.1584, median=44
"rank" int: 25 distinct, nulls=18057, 0..24, avg=10.6613, median=11
"fastestLapTime" text: 4709 distinct, nulls=18185
"fastestLapSpeed" text: numeric, 4794 distinct, nulls=18185
"statusId" int NOTNULL FK: 131 distinct, 1..136, avg=18.4415, median=11

indexes: none
fk: "driverId"→"drivers"."driverId", "constructorId"→"constructors"."constructorId", "raceId"→"races"."raceId", "statusId"→"status"."statusId"

samples:
| column | latest | sample | sample |
|---|---|---|---|
| resultId | 23661 | 3126 | 18867 |
| raceId | 982 | 166 | 783 |
| driverId | 8 | 65 | 476 |
| constructorId | 6 | 19 | 6 |
| number | 7 | 8 | 36 |
| grid | 4 | 11 | 8 |
| position | null | null | 3 |
| positionText | R | R | 3 |
| positionOrder | 20 | 21 | 3 |
| points | 0 | 0 | 4 |
| laps | 0 | 20 | 85 |
| time | null | null | null |
| milliseconds | null | null | null |
| fastestLap | null | null | null |
| rank | 0 | null | null |
| fastestLapTime | null | null | null |
| fastestLapSpeed | null | null | null |
| statusId | 3 | 6 | 12 |

# "seasons"  (rows=68)

columns:
"year" int PK: unique identifier, 1950..2017, avg=1983.5, median=1983.5
"url" text NOTNULL: all distinct

indexes: none
fk: none

samples:
| column | latest | sample | sample |
|---|---|---|---|
| year | 2017 | 1950 | 2001 |
| url | https://en.wikipedia.org/wiki/2017_Formula_One_season | http://en.wikipedia.org/wiki/1950_Formula_One_season | http://en.wikipedia.org/wiki/2001_Formula_One_season |

# "status"  (rows=134)

columns:
"statusId" int PK: unique identifier, 1..136, avg=68.709, median=69.5
"status" text NOTNULL: all distinct

indexes: none
fk: none

samples:
| column | latest | sample | sample |
|---|---|---|---|
| statusId | 136 | 79 | 93 |
| status | Seat | Drivetrain | Safety belt |
