---
generator: db-snooper
version: 0.0.26
generated_at_utc: 2026-08-16T07:19:18.149763Z
dialect: sqlite
database: /Users/renatyuldashev/Documents/ai-sql/custom-bench/data/bird_mini_dev/databases/dev_databases/formula_1/formula_1.sqlite
schema: main
---

## Relationships

- circuits.circuitId ← races.circuitId
- constructors.constructorId ← constructorResults.constructorId, constructorStandings.constructorId, qualifying.constructorId, results.constructorId
- drivers.driverId ← driverStandings.driverId, lapTimes.driverId, pitStops.driverId, qualifying.driverId, results.driverId
- races.raceId ← constructorResults.raceId, constructorStandings.raceId, driverStandings.raceId, lapTimes.raceId, pitStops.raceId, qualifying.raceId, results.raceId
- seasons.year ← races.year
- status.statusId ← results.statusId

# circuits

```sql
CREATE TABLE circuits
(
    circuitId  INTEGER
        primary key autoincrement,
    circuitRef TEXT default '' not null,
    name       TEXT default '' not null,
    location   TEXT,
    country    TEXT,
    lat        REAL,
    lng        REAL,
    alt        INTEGER,
    url        TEXT default '' not null
        unique
);
```

## Rows

- total=72

| column | latest | sample | sample |
|---|---|---|---|
| circuitId | 73 | 17 | 22 |
| circuitRef | BAK | shanghai | suzuka |
| name | Baku City Circuit | Shanghai International Circuit | Suzuka Circuit |
| location | Baku | Shanghai | Suzuka |
| country | Azerbaijan | China | Japan |
| lat | 40.3725 | 31.3389 | 34.8431 |
| lng | 49.8533 | 121.22 | 136.541 |
| alt | null | null | null |
| url | http://en.wikipedia.org/wiki/Baku_City_Circuit | http://en.wikipedia.org/wiki/Shanghai_International_Circuit | http://en.wikipedia.org/wiki/Suzuka_Circuit |

## Columns

- circuitId: unique identifier, int 2..73
  - stats: average=37.5, median=37.5
- circuitRef: all distinct
- name: all distinct
- location: 69 distinct
- country: 32 distinct
- lat: 71 distinct, num -34.9272..57.2653
  - stats: average=34.8685, median=41.3783
- lng: 71 distinct, num -118.189..138.927
  - stats: average=-0.26669, median=3.54722
- alt: all NULL
- url: all distinct


# constructorResults

```sql
CREATE TABLE constructorResults
(
    constructorResultsId INTEGER
        primary key autoincrement,
    raceId               INTEGER default 0 not null,
    constructorId        INTEGER default 0 not null,
    points               REAL,
    status               TEXT,
    foreign key (raceId) references races(raceId),
    foreign key (constructorId) references constructors(constructorId)

);
```

## Rows

- total=11082

| column | latest | sample | sample |
|---|---|---|---|
| constructorResultsId | 15579 | 2732 | 1083 |
| raceId | 982 | 268 | 122 |
| constructorId | 6 | 33 | 17 |
| points | 0 | 0 | 2 |
| status | null | null | null |

## Columns

- constructorResultsId: unique identifier, int 1..15579
  - stats: average=7319.37, median=5541.5
- raceId: 907 distinct, int 1..982
  - stats: average=453.535, median=438
- constructorId: 172 distinct, int 1..210
  - stats: average=41.2624, median=24
- points: 45 distinct, num 0..66
  - stats: average=3.15525, median=0
- status: "D"=17, nulls=11065


# constructorStandings

```sql
CREATE TABLE constructorStandings
(
    constructorStandingsId INTEGER
        primary key autoincrement,
    raceId                 INTEGER default 0 not null,
    constructorId          INTEGER default 0 not null,
    points                 REAL   default 0 not null,
    position               INTEGER,
    positionText           TEXT,
    wins                   INTEGER default 0 not null,
    foreign key (raceId) references races(raceId),
    foreign key (constructorId) references constructors(constructorId)
);
```

## Rows

- total=11836

| column | latest | sample | sample |
|---|---|---|---|
| constructorStandingsId | 26872 | 7664 | 24305 |
| raceId | 982 | 323 | 342 |
| constructorId | 210 | 3 | 1 |
| points | 37 | 15 | 129 |
| position | 8 | 2 | 3 |
| positionText | 8 | 2 | 3 |
| wins | 0 | 1 | 2 |

## Columns

- constructorStandingsId: unique identifier, int 1..26872
  - stats: average=15141.5, median=11496.5
- raceId: 906 distinct, int 1..982
  - stats: average=466.488, median=461
- constructorId: 156 distinct, int 1..210
  - stats: average=45.6973, median=25
- points: 436 distinct, num 0..765
  - stats: average=26.3847, median=6
- position: 22 distinct, int 1..22
  - stats: average=7.45091, median=7
- positionText: 23 distinct
- wins: 20 distinct, int 0..19
  - stats: average=0.638729, median=0


# constructors

```sql
CREATE TABLE constructors
(
    constructorId  INTEGER
        primary key autoincrement,
    constructorRef TEXT default '' not null,
    name           TEXT default '' not null
        unique,
    nationality    TEXT,
    url            TEXT default '' not null
);
```

## Rows

- total=208

| column | latest | sample | sample |
|---|---|---|---|
| constructorId | 210 | 57 | 178 |
| constructorRef | haas | ensign | cooper-alfa_romeo |
| name | Haas F1 Team | Ensign | Cooper-Alfa Romeo |
| nationality | American | British | British |
| url | http://en.wikipedia.org/wiki/Haas_F1_Team | http://en.wikipedia.org/wiki/Ensign_%28racing_team%29 | http://en.wikipedia.org/wiki/Cooper_Car_Company |

## Columns

- constructorId: unique identifier, int 1..210
  - stats: average=105.514, median=105.5
- constructorRef: all distinct
- name: all distinct
- nationality: 24 distinct
- url: 171 distinct


# driverStandings

```sql
CREATE TABLE driverStandings
(
    driverStandingsId INTEGER
        primary key autoincrement,
    raceId            INTEGER default 0 not null,
    driverId          INTEGER default 0 not null,
    points            REAL   default 0 not null,
    position          INTEGER,
    positionText      TEXT,
    wins              INTEGER default 0 not null,
    foreign key (raceId) references races(raceId),
    foreign key (driverId) references drivers(driverId)
);
```

## Rows

- total=31578

| column | latest | sample | sample |
|---|---|---|---|
| driverStandingsId | 68460 | 58273 | 20317 |
| raceId | 982 | 556 | 416 |
| driverId | 814 | 259 | 117 |
| points | 0 | 0 | 53 |
| position | 23 | 36 | 3 |
| positionText | 23 | 36 | 3 |
| wins | 0 | 0 | 3 |

## Columns

- driverStandingsId: unique identifier, int 1..68460
  - stats: average=39409.4, median=47373.5
- raceId: 970 distinct, int 1..982
  - stats: average=535.826, median=564
- driverId: 833 distinct, int 1..841
  - stats: average=278.727, median=204
- points: 337 distinct, num 0..397
  - stats: average=10.3378, median=0
- position: 108 distinct, int 1..108
  - stats: average=20.6076, median=17
- positionText: 109 distinct
- wins: 0=27946, 1=1898, 2=744, 3=382, 4=223, 5=145, 6=116, 7=50, 8=25, 9=21, 10=13, 11=7, 12=5, 13=3, int 0..13


# drivers

```sql
CREATE TABLE drivers
(
    driverId    INTEGER
        primary key autoincrement,
    driverRef   TEXT default '' not null,
    number      INTEGER,
    code        TEXT,
    forename    TEXT default '' not null,
    surname     TEXT default '' not null,
    dob         DATE,
    nationality TEXT,
    url         TEXT default '' not null
        unique
);
```

## Rows

- total=840

| column | latest | sample | sample |
|---|---|---|---|
| driverId | 841 | 147 | 134 |
| driverRef | giovinazzi | barilla | bertaggia |
| number | 36 | null | null |
| code | GIO | null | null |
| forename | Antonio | Paolo | Enrico |
| surname | Giovinazzi | Barilla | Bertaggia |
| dob | 1993-12-14 | 1961-04-20 | 1964-09-19 |
| nationality | Italian | Italian | Italian |
| url | http://en.wikipedia.org/wiki/Antonio_Giovinazzi | http://en.wikipedia.org/wiki/Paolo_Barilla | http://en.wikipedia.org/wiki/Enrico_Bertaggia |

## Columns

- driverId: unique identifier, int 1..841
  - stats: average=420.538, median=420.5
- driverRef: all distinct
- number: all distinct, nulls=804, int 2..99
  - stats: average=30.8333, median=21.5
- code: 80 distinct, nulls=757
- forename: 465 distinct
- surname: 784 distinct
- dob: 821 distinct, nulls=1
- nationality: 41 distinct
- url: all distinct


# lapTimes

```sql
CREATE TABLE lapTimes
(
    raceId       INTEGER not null,
    driverId     INTEGER not null,
    lap          INTEGER not null,
    position     INTEGER,
    time         TEXT,
    milliseconds INTEGER,
    primary key (raceId, driverId, lap),
    foreign key (raceId) references races(raceId),
    foreign key (driverId) references drivers(driverId)
);
```

## Rows

- total=400524

| column | latest | sample | sample |
|---|---|---|---|
| raceId | 982 | 9 | 933 |
| driverId | 840 | 16 | 154 |
| lap | 58 | 16 | 20 |
| position | 8 | 6 | 11 |
| time | 1:48.699 | 1:37.506 | 1:13.645 |
| milliseconds | 108699 | 97506 | 73645 |

## Columns

- raceId: 367 distinct, int 2..982
  - stats: average=415.835
- driverId: 121 distinct, int 1..841
  - stats: average=181.131
- lap: 78 distinct, int 1..78
  - stats: average=29.9691
- position: int 1..24
  - stats: average=9.69788
- time: profile metrics skipped
- milliseconds: int 67411..7507547
  - stats: average=95708.6


# pitStops

```sql
CREATE TABLE pitStops
(
    raceId       INTEGER not null,
    driverId     INTEGER not null,
    stop         INTEGER not null,
    lap          INTEGER not null,
    time         TEXT    not null,
    duration     TEXT,
    milliseconds INTEGER,
    primary key (raceId, driverId, stop),
    foreign key (raceId) references races(raceId),
    foreign key (driverId) references drivers(driverId)
);
```

## Rows

- total=5815

| column | latest | sample | sample |
|---|---|---|---|
| raceId | 982 | 943 | 848 |
| driverId | 840 | 20 | 30 |
| stop | 4 | 1 | 1 |
| lap | 26 | 1 | 14 |
| time | 21:05:07 | 13:04:58 | 14:28:40 |
| duration | 29.412 | 28.070 | 21.201 |
| milliseconds | 29412 | 28070 | 21201 |

## Columns

- raceId: 124 distinct, int 842..982
  - stats: average=906.012, median=901
  - top_values: 936=96, 851=88, 844=82, 970=82, 982=82, 884=79, 914=79, 845=77, 861=76, 956=76
- driverId: 54 distinct, int 1..841
  - stats: average=424.956, median=155
  - top_values: 13=293, 1=273, 20=268, 4=260, 817=257, 815=252, 18=245, 3=240, 807=215, 8=209
- stop: 1=2552, 2=2005, 3=932, 4=250, 5=63, 6=13, int 1..6
- lap: 73 distinct, int 1..74
  - stats: average=25.1001, median=25
- time: 4650 distinct
- duration: 4580 distinct
- milliseconds: 4580 distinct, int 12897..2011266
  - stats: average=46307.8, median=23356


# qualifying

```sql
CREATE TABLE qualifying
(
    qualifyId     INTEGER
        primary key autoincrement,
    raceId        INTEGER default 0 not null,
    driverId      INTEGER default 0 not null,
    constructorId INTEGER default 0 not null,
    number        INTEGER default 0 not null,
    position      INTEGER,
    q1            TEXT,
    q2            TEXT,
    q3            TEXT,
    foreign key (raceId) references races(raceId),
    foreign key (driverId) references drivers(driverId),
    foreign key (constructorId) references constructors(constructorId)
);
```

## Rows

- total=6967

| column | latest | sample | sample |
|---|---|---|---|
| qualifyId | 7419 | 2610 | 1972 |
| raceId | 982 | 257 | 214 |
| driverId | 828 | 77 | 57 |
| constructorId | 15 | 6 | 1 |
| number | 9 | 28 | 9 |
| position | 20 | 17 | 10 |
| q1 | 1:45.570 | 1:18.855 | 1:15.339 |
| q2 | null | null | null |
| q3 | null | null | null |

## Columns

- qualifyId: unique identifier, int 23..7419
  - stats: average=3719.18, median=3703
- raceId: 319 distinct, int 2..982
  - stats: average=443.562, median=258
- driverId: 151 distinct, int 1..841
  - stats: average=198.587, median=30
- constructorId: 41 distinct, int 1..210
  - stats: average=34.8665, median=9
- number: 48 distinct, int 0..99
  - stats: average=15.1672, median=12
- position: 28 distinct, int 1..28
  - stats: average=11.5019, median=11
- q1: 6283 distinct, nulls=109
- q2: 3222 distinct, nulls=3577
- q3: 1959 distinct, nulls=4935


# races

```sql
CREATE TABLE races
(
    raceId    INTEGER
        primary key autoincrement,
    year      INTEGER default 0            not null,
    round     INTEGER default 0            not null,
    circuitId INTEGER default 0            not null,
    name      TEXT    default ''           not null,
    date      DATE    default '0000-00-00' not null,
    time      TEXT,
    url       TEXT unique,
    foreign key (year) references seasons(year),
    foreign key (circuitId) references circuits(circuitId)
);
```

## Rows

- total=954

| column | latest | sample | sample |
|---|---|---|---|
| raceId | 988 | 445 | 536 |
| year | 2017 | 1984 | 1978 |
| round | 20 | 10 | 10 |
| circuitId | 24 | 38 | 38 |
| name | Abu Dhabi Grand Prix | British Grand Prix | British Grand Prix |
| date | 2017-11-26 | 1984-07-22 | 1978-07-16 |
| time | 17:00:00 | null | null |
| url | https://en.wikipedia.org/wiki/2017_Abu_Dhabi_Grand_Prix | http://en.wikipedia.org/wiki/1984_British_Grand_Prix | http://en.wikipedia.org/wiki/1978_British_Grand_Prix |

## Columns

- raceId: unique identifier, int 2..988
  - stats: average=491.922, median=492.5
- year: 68 distinct, int 1950..2017
  - stats: average=1987.95, median=1989
- round: 21 distinct, int 1..21
  - stats: average=8.33648, median=8
- circuitId: 71 distinct, int 2..73
  - stats: average=22.1719, median=18
- name: 42 distinct
- date: all distinct
- time: "12:00:00"=107, "14:00:00"=26, "06:00:00"=13, "07:00:00"=11, "13:00:00"=11, "16:00:00"=11, "15:00:00"=8, "19:00:00"=8, "17:00:00"=6, "18:00:00"=6, "05:00:00"=5, "08:00:00"=5, "11:00:00"=4, "09:30:00"=3, "04:30:00"=2, "11:30:00"=2, "14:30:00"=2, "09:00:00"=1, "20:00:00"=1, nulls=722
- url: unique identifier


# results

```sql
CREATE TABLE results
(
    resultId        INTEGER
        primary key autoincrement,
    raceId          INTEGER default 0  not null,
    driverId        INTEGER default 0  not null,
    constructorId   INTEGER default 0  not null,
    number          INTEGER,
    grid            INTEGER default 0  not null,
    position        INTEGER,
    positionText    TEXT    default '' not null,
    positionOrder   INTEGER default 0  not null,
    points          REAL   default 0  not null,
    laps            INTEGER default 0  not null,
    time            TEXT,
    milliseconds    INTEGER,
    fastestLap      INTEGER,
    rank            INTEGER default 0,
    fastestLapTime  TEXT,
    fastestLapSpeed TEXT,
    statusId        INTEGER default 0  not null,
    foreign key (raceId) references races(raceId),
    foreign key (driverId) references drivers(driverId),
    foreign key (constructorId) references constructors(constructorId),
    foreign key (statusId) references status(statusId)
);
```

## Rows

- total=23179

| column | latest | sample | sample |
|---|---|---|---|
| resultId | 23661 | 12577 | 3366 |
| raceId | 982 | 519 | 177 |
| driverId | 8 | 152 | 37 |
| constructorId | 6 | 51 | 21 |
| number | 7 | 35 | 14 |
| grid | 4 | 17 | 18 |
| position | null | 17 | null |
| positionText | R | 17 | R |
| positionOrder | 20 | 17 | 19 |
| points | 0 | 0 | 0 |
| laps | 0 | 75 | 5 |
| time | null | null | null |
| milliseconds | null | null | null |
| fastestLap | null | null | null |
| rank | 0 | null | null |
| fastestLapTime | null | null | null |
| fastestLapSpeed | null | null | null |
| statusId | 3 | 15 | 20 |

## Columns

- resultId: unique identifier, int 23..23661
  - stats: average=11873.6, median=11892
- raceId: 948 distinct, int 2..982
  - stats: average=486.903, median=479
- driverId: 839 distinct, int 1..841
  - stats: average=225.852, median=156
- constructorId: 207 distinct, int 1..210
  - stats: average=46.6559, median=25
- number: 128 distinct, nulls=6, int 0..208
  - stats: average=16.977, median=15
- grid: 35 distinct, int 0..34
  - stats: average=11.2768, median=11
- position: 33 distinct, nulls=10326, int 1..33
  - stats: average=7.78869, median=7
- positionText: 39 distinct
- positionOrder: 39 distinct, int 1..39
  - stats: average=13.1293, median=13
- points: 33 distinct, num 0..50
  - stats: average=1.56208, median=0
- laps: 172 distinct, int 0..200
  - stats: average=45.312, median=52
- time: 5588 distinct, nulls=17390
- milliseconds: 5751 distinct, nulls=17391, int 1474899..15090540
  - stats: average=6.32918e+06, median=5.89006e+06
- fastestLap: 77 distinct, nulls=18185, int 2..78
  - stats: average=41.1584, median=44
- rank: 25 distinct, nulls=18057, int 0..24
  - stats: average=10.6613, median=11
- fastestLapTime: 4709 distinct, nulls=18185
- fastestLapSpeed: 4794 distinct, nulls=18185
- statusId: 131 distinct, int 1..136
  - stats: average=18.4415, median=11


# seasons

```sql
CREATE TABLE seasons
(
    year INTEGER default 0  not null
        primary key,
    url  TEXT    default '' not null
        unique
);
```

## Rows

- total=68

| column | latest | sample | sample |
|---|---|---|---|
| year | 2017 | 1987 | 2009 |
| url | https://en.wikipedia.org/wiki/2017_Formula_One_season | http://en.wikipedia.org/wiki/1987_Formula_One_season | http://en.wikipedia.org/wiki/2009_Formula_One_season |

## Columns

- year: unique identifier, int 1950..2017
  - stats: average=1983.5, median=1983.5
- url: all distinct


# status

```sql
CREATE TABLE status
(
    statusId INTEGER
        primary key autoincrement,
    status   TEXT default '' not null
);
```

## Rows

- total=134

| column | latest | sample | sample |
|---|---|---|---|
| statusId | 136 | 45 | 51 |
| status | Seat | +11 Laps | Oil pressure |

## Columns

- statusId: unique identifier, int 1..136
  - stats: average=68.709, median=69.5
- status: all distinct
