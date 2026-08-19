---
generator: db-snooper
version: 0.0.26
generated_at_utc: 2026-08-16T08:09:23.541657Z
dialect: sqlite
database: /var/folders/9j/b9bx_drd53sc6zbpsqyrjy4h0000gn/T/dbsnoop-h21kjunm/f1.sqlite
schema: main
---

# circuits

```sql
CREATE TABLE "circuits" (
  "circuit_id" INT(11) NOT NULL,
  "circuit_ref" VARCHAR(255) NOT NULL DEFAULT '',
  "name" VARCHAR(255) NOT NULL DEFAULT '',
  "location" VARCHAR(255) DEFAULT NULL,
  "country" VARCHAR(255) DEFAULT NULL,
  "lat" FLOAT DEFAULT NULL,
  "lng" FLOAT DEFAULT NULL,
  "alt" INT(11) DEFAULT NULL,
  "url" VARCHAR(255) NOT NULL DEFAULT '',
  PRIMARY KEY ("circuit_id")
);
```

## Rows

- total=77

| column | latest | sample | sample |
|---|---|---|---|
| circuit_id | 80 | 44 | 15 |
| circuit_ref | vegas | las_vegas | marina_bay |
| name | Las Vegas Strip Street Circuit | Las Vegas Street Circuit | Marina Bay Street Circuit |
| location | Las Vegas | Nevada | Marina Bay |
| country | United States | USA | Singapore |
| lat | 36.1147 | 36.1162 | 1.2914 |
| lng | -115.173 | -115.174 | 103.864 |
| alt | 642 | 639 | 18 |
| url | https://en.wikipedia.org/wiki/Las_Vegas_Grand_Prix#Circuit | http://en.wikipedia.org/wiki/Las_Vegas_Street_Circuit | http://en.wikipedia.org/wiki/Marina_Bay_Street_Circuit |

## Columns

- circuit_id: unique identifier, int 1..80
- circuit_ref: all distinct
- name: all distinct
- location: 75 distinct
- country: 35 distinct
- lat: all distinct, num -37.8497..57.2653
  - stats: average=33.4429, median=40.9517
- lng: all distinct, num -118.189..144.968
  - stats: average=1.07668, median=3.93083
- alt: 66 distinct, int -7..2227
  - stats: average=247.013, median=129
- url: all distinct


# circuits_ext

```sql
CREATE TABLE circuits_ext(
  circuit_id INT,
  circuit_ref TEXT,
  name TEXT,
  location TEXT,
  country TEXT,
  lat REAL,
  lng REAL,
  alt INT,
  url TEXT,
  last_race_year,
  number_of_races
);
```

## Rows

- total=77

| column | latest | sample | sample |
|---|---|---|---|
| circuit_id | 80 | 49 | 43 |
| circuit_ref | vegas | montjuic | long_beach |
| name | Las Vegas Strip Street Circuit | Montjuïc | Long Beach |
| location | Las Vegas | Barcelona | California |
| country | United States | Spain | USA |
| lat | 36.1147 | 41.3664 | 33.7651 |
| lng | -115.173 | 2.15167 | -118.189 |
| alt | 642 | 79 | 12 |
| url | https://en.wikipedia.org/wiki/Las_Vegas_Grand_Prix#Circuit | http://en.wikipedia.org/wiki/Montju%C3%AFc_circuit | http://en.wikipedia.org/wiki/Long_Beach,_California |
| last_race_year | 2024 | 1975 | 1983 |
| number_of_races | 2 | 4 | 8 |

## Columns

- circuit_id: unique identifier, int 1..80
- circuit_ref: all distinct
- name: all distinct
- location: 75 distinct
- country: 35 distinct
- lat: all distinct, num -37.8497..57.2653
  - stats: average=33.4429, median=40.9517
- lng: all distinct, num -118.189..144.968
  - stats: average=1.07668, median=3.93083
- alt: 66 distinct, int -7..2227
  - stats: average=247.013, median=129
- url: all distinct
- last_race_year: 41 distinct
- number_of_races: 34 distinct


# constructor_results

```sql
CREATE TABLE "constructor_results" (
  "constructor_results_id" INT(11) NOT NULL,
  "race_id" INT(11) NOT NULL DEFAULT '0',
  "constructor_id" INT(11) NOT NULL DEFAULT '0',
  "points" FLOAT DEFAULT NULL,
  "status" VARCHAR(255) DEFAULT NULL,
  PRIMARY KEY ("constructor_results_id")
);
```

## Rows

- total=12505

| column | latest | sample | sample |
|---|---|---|---|
| constructor_results_id | 17009 | 12889 | 10522 |
| race_id | 1132 | 589 | 719 |
| constructor_id | 214 | 67 | 172 |
| points | 0 | 0 | 1 |
| status | null | null | null |

## Columns

- constructor_results_id: unique identifier, int 1..17009
- race_id: 1048 distinct, int 1..1132
- constructor_id: 175 distinct, int 1..215
- points: 60 distinct, num 0..66
  - stats: average=3.98617, median=0
- status: "D"=17, nulls=12488


# constructor_standings

```sql
CREATE TABLE "constructor_standings" (
  "constructor_standings_id" INT(11) NOT NULL,
  "race_id" INT(11) NOT NULL DEFAULT '0',
  "constructor_id" INT(11) NOT NULL DEFAULT '0',
  "points" FLOAT NOT NULL DEFAULT '0',
  "position" INT(11) DEFAULT NULL,
  "position_text" VARCHAR(255) DEFAULT NULL,
  "wins" INT(11) NOT NULL DEFAULT '0',
  PRIMARY KEY ("constructor_standings_id")
);
```

## Rows

- total=13271

| column | latest | sample | sample |
|---|---|---|---|
| constructor_standings_id | 28852 | 19521 | 11274 |
| race_id | 1132 | 730 | 496 |
| constructor_id | 214 | 95 | 25 |
| points | 9 | 3 | 10 |
| position | 8 | 6 | 9 |
| position_text | 8 | 6 | 9 |
| wins | 0 | 0 | 0 |

## Columns

- constructor_standings_id: unique identifier, int 1..28852
- race_id: 1049 distinct, int 1..1132
- constructor_id: 160 distinct, int 1..215
- points: 557 distinct, num 0..860
  - stats: average=35.6811, median=7
- position: 22 distinct, int 1..22
  - stats: average=7.24165, median=7
- position_text: 23 distinct
- wins: 22 distinct, int 0..21
  - stats: average=0.686987, median=0


# constructors

```sql
CREATE TABLE "constructors" (
  "constructor_id" INT(11) NOT NULL,
  "constructor_ref" VARCHAR(255) NOT NULL DEFAULT '',
  "name" VARCHAR(255) NOT NULL DEFAULT '',
  "nationality" VARCHAR(255) DEFAULT NULL,
  "url" VARCHAR(255) NOT NULL DEFAULT '',
  PRIMARY KEY ("constructor_id")
);
```

## Rows

- total=212

| column | latest | sample | sample |
|---|---|---|---|
| constructor_id | 215 | 56 | 124 |
| constructor_ref | rb | fittipaldi | tec-mec |
| name | RB F1 Team | Fittipaldi | Tec-Mec |
| nationality | Italian | Brazilian | Italian |
| url | http://en.wikipedia.org/wiki/RB_Formula_One_Team | http://en.wikipedia.org/wiki/Fittipaldi_%28constructor%29 | http://en.wikipedia.org/wiki/Tec-Mec |

## Columns

- constructor_id: unique identifier, int 1..215
- constructor_ref: all distinct
- name: all distinct
- nationality: 24 distinct
- url: 175 distinct


# constructors_ext

```sql
CREATE TABLE constructors_ext(
  constructor_id INT,
  constructor_ref TEXT,
  name TEXT,
  nationality TEXT,
  url TEXT,
  short_name
);
```

## Rows

- total=212

| column | latest | sample | sample |
|---|---|---|---|
| constructor_id | 215 | 198 | 49 |
| constructor_ref | rb | mclaren-alfa_romeo | zakspeed |
| name | RB F1 Team | McLaren-Alfa Romeo | Zakspeed |
| nationality | Italian | British | German |
| url | http://en.wikipedia.org/wiki/RB_Formula_One_Team | http://en.wikipedia.org/wiki/McLaren_(racing) | http://en.wikipedia.org/wiki/Zakspeed |
| short_name | RB F1 Team | McLaren | Zakspeed |

## Columns

- constructor_id: unique identifier, int 1..215
- constructor_ref: all distinct
- name: all distinct
- nationality: 24 distinct
- url: 175 distinct
- short_name: 172 distinct


# driver_standings

```sql
CREATE TABLE "driver_standings" (
  "driver_standings_id" INT(11) NOT NULL,
  "race_id" INT(11) NOT NULL DEFAULT '0',
  "driver_id" INT(11) NOT NULL DEFAULT '0',
  "points" FLOAT NOT NULL DEFAULT '0',
  "position" INT(11) DEFAULT NULL,
  "position_text" VARCHAR(255) DEFAULT NULL,
  "wins" INT(11) NOT NULL DEFAULT '0',
  PRIMARY KEY ("driver_standings_id")
);
```

## Rows

- total=34595

| column | latest | sample | sample |
|---|---|---|---|
| driver_standings_id | 72871 | 63982 | 72344 |
| race_id | 1132 | 346 | 1115 |
| driver_id | 860 | 30 | 4 |
| points | 6 | 36 | 183 |
| position | 14 | 9 | 4 |
| position_text | 14 | 9 | 4 |
| wins | 0 | 0 | 0 |

## Columns

- driver_standings_id: unique identifier, int 1..72871
- race_id: 1113 distinct, int 1..1132
- driver_id: 852 distinct, int 1..860
- points: 429 distinct, num 0..575
  - stats: average=14.1149, median=1
- position: 108 distinct, int 1..108
  - stats: average=19.7789, median=16
- position_text: 109 distinct
- wins: 20 distinct, int 0..19
  - stats: average=0.273074, median=0


# driver_standings_ext

```sql
CREATE TABLE driver_standings_ext(
  driver_standings_id INT,
  race_id INT,
  driver_id INT,
  points REAL,
  position INT,
  position_text TEXT,
  wins INT
);
```

## Rows

- total=35012

| column | latest | sample | sample |
|---|---|---|---|
| driver_standings_id | 72871 | 56216 | 21608 |
| race_id | 1132 | 584 | 453 |
| driver_id | 860 | 182 | 105 |
| points | 6 | 47 | 0 |
| position | 14 | 1 | 13 |
| position_text | 14 | 1 | 13 |
| wins | 0 | 4 | 0 |

## Columns

- driver_standings_id: 34596 distinct, int 0..72871
- race_id: 1113 distinct, int 1..1132
- driver_id: 852 distinct, int 1..860
- points: 429 distinct, num 0..575
  - stats: average=13.9468, median=1
- position: 108 distinct, int 1..108
  - stats: average=19.7878, median=16
- position_text: 109 distinct, nulls=417
- wins: 20 distinct, int 0..19
  - stats: average=0.269822, median=0


# drivers

```sql
CREATE TABLE "drivers" (
  "driver_id" INT(11) NOT NULL,
  "driver_ref" VARCHAR(255) NOT NULL DEFAULT '',
  "number" INT(11) DEFAULT NULL,
  "code" VARCHAR(3) DEFAULT NULL,
  "forename" VARCHAR(255) NOT NULL DEFAULT '',
  "surname" VARCHAR(255) NOT NULL DEFAULT '',
  "full_name" VARCHAR(255) AS (forename || ' ' || surname) VIRTUAL,
  "dob" DATE DEFAULT NULL,
  "nationality" VARCHAR(255) DEFAULT NULL,
  "url" VARCHAR(255) NOT NULL DEFAULT '',
  PRIMARY KEY ("driver_id")
);
```

## Rows

- total=859

| column | latest | sample | sample |
|---|---|---|---|
| driver_id | 860 | 624 | 242 |
| driver_ref | bearman | ramos | galica |
| number | 38 | null | null |
| code | BEA | null | null |
| forename | Oliver | Hernando | Divina |
| surname | Bearman | da Silva Ramos | Galica |
| full_name | Oliver Bearman | Hernando da Silva Ramos | Divina Galica |
| dob | 2005-05-08 | 1925-12-07 | 1944-08-13 |
| nationality | British | Brazilian | British |
| url | http://en.wikipedia.org/wiki/Oliver_Bearman | http://en.wikipedia.org/wiki/Hernando_da_Silva_Ramos | http://en.wikipedia.org/wiki/Divina_Galica |

## Columns

- driver_id: unique identifier, int 1..860
- driver_ref: all distinct
- number: 46 distinct, nulls=802, int 2..99
  - stats: average=33.5088, median=24
- code: 96 distinct, nulls=757
- forename: 478 distinct
- surname: 800 distinct
- full_name: all distinct
- dob: 841 distinct
- nationality: 42 distinct
- url: all distinct


# drivers_ext

```sql
CREATE TABLE drivers_ext(
  driver_id INT,
  driver_ref TEXT,
  number INT,
  code,
  forename TEXT,
  surname TEXT,
  full_name TEXT,
  dob NUM,
  nationality TEXT,
  url TEXT
);
```


# drives

```sql
CREATE TABLE drives(
  year INT,
  driver_id INT,
  drive_id,
  constructor_id INT,
  first_round INT,
  last_round INT,
  is_first_drive_of_season,
  is_final_drive_of_season
);
```

## Rows

- total=3784

| column | latest | sample | sample |
|---|---|---|---|
| year | 2024 | 1955 | 1961 |
| driver_id | 860 | 648 | 394 |
| drive_id | 1 | 1 | 1 |
| constructor_id | 6 | 131 | 6 |
| first_round | 2 | 1 | 4 |
| last_round | 2 | 7 | 7 |
| is_first_drive_of_season | 1 | 1 | 1 |
| is_final_drive_of_season | 1 | 1 | 1 |

## Columns

- year: 75 distinct, int 1950..2024
  - stats: average=1976.01, median=1972
- driver_id: 859 distinct, int 1..860
- drive_id: 1=3222, 2=299, -1=163, 3=78, 4=19, 5=3
- constructor_id: 212 distinct, int -1..215
- first_round: 1=1721, 2=391, 3=325, 5=194, 4=188, 7=165, 6=157, 8=141, 9=112, 10=85, 11=64, 12=58, 14=52, 13=45, 15=45, 16=30, 17=9, 18=1, 19=1, int 1..19
- last_round: 22 distinct, int 1..22
  - stats: average=10.226, median=10
- is_first_drive_of_season: 1=3222, 0=562
- is_final_drive_of_season: 1=3218, 0=566


# lap_positions

```sql
CREATE TABLE lap_positions(
  race_id INT,
  driver_id INT,
  lap INT,
  position INT,
  lap_type
);
```

## Rows

- total≈613112 (estimated from db stats; row/column profiling skipped)


# lap_time_stats

```sql
CREATE TABLE lap_time_stats(
  race_id INT,
  driver_id INT,
  avg_milliseconds,
  avg_seconds,
  stdev_milliseconds,
  stdev_seconds
);
```

## Rows

- total=10789

| column | latest | sample | sample |
|---|---|---|---|
| race_id | 1131 | 1035 | 1054 |
| driver_id | 858 | 846 | 1 |
| avg_milliseconds | 73465.3 | 93221.9 | 85930.6 |
| avg_seconds | 73.4653 | 93.2219 | 85.9306 |
| stdev_milliseconds | 4993.76 | 4244.42 | 12629.2 |
| stdev_seconds | 4.99376 | 4.24442 | 12.6292 |

## Columns

- race_id: 531 distinct, int 1..1131
- driver_id: 141 distinct, int 1..860
- avg_milliseconds: 10784 distinct
- avg_seconds: 10788 distinct
- stdev_milliseconds: 10676 distinct
- stdev_seconds: 10676 distinct


# lap_times

```sql
CREATE TABLE "lap_times" (
  "race_id" INT(11) NOT NULL,
  "driver_id" INT(11) NOT NULL,
  "lap" INT(11) NOT NULL,
  "position" INT(11) DEFAULT NULL,
  "time" VARCHAR(255) DEFAULT NULL,
  "milliseconds" INT(11) DEFAULT NULL,
  "seconds" FLOAT AS (CAST(milliseconds AS FLOAT) / 1000) VIRTUAL,
  PRIMARY KEY ("race_id", "driver_id", "lap")
);
```

## Rows

- total≈575029 (estimated from db stats; row/column profiling skipped)


# lap_times_ext

```sql
CREATE TABLE lap_times_ext(
  race_id INT,
  driver_id INT,
  lap INT,
  position INT,
  time TEXT,
  milliseconds INT,
  seconds REAL,
  running_milliseconds
);
```

## Rows

- total≈575029 (estimated from db stats; row/column profiling skipped)


# liveries

```sql
CREATE TABLE "liveries" (
  "constructor_ref" VARCHAR(255) NOT NULL DEFAULT '',
  "start_year" INT(11) NOT NULL DEFAULT '0',
  "end_year" INT(11) NULL DEFAULT '0',
  "primary_hex_code" VARCHAR(255) NOT NULL DEFAULT '',
  PRIMARY KEY ("constructor_ref", "start_year", "end_year")
);
```

## Rows

- total=64

| column | latest | sample | sample |
|---|---|---|---|
| constructor_ref | williams | renault | sauber |
| start_year | 2014 | 2002 | 1993 |
| end_year | null | 2006 | 1994 |
| primary_hex_code | #005AFF | #2486E1 | #000000 |

## Columns

- constructor_ref: 37 distinct
  - top_values: "renault"=6, "sauber"=5, "williams"=5, "jordan"=4, "mclaren"=4, "benneton"=3, "hrt"=3, "caterham"=2, "force_india"=2, "haas"=2
- start_year: 32 distinct, int 1950..2021
  - stats: average=2004.72, median=2007
  - top_values: 2006=6, 2010=6, 1997=4, 2012=4, 2016=3, 2017=3, 2021=3, 1985=2, 1991=2, 1992=2
- end_year: 28 distinct, nulls=10, int 1985..2020
  - stats: average=2007.46, median=2009
  - top_values: 2005=4, 2009=4, 2011=4, 2016=4, 2006=3, 2020=3, 1991=2, 1996=2, 2001=2, 2008=2
- primary_hex_code: 52 distinct


# pit_stops

```sql
CREATE TABLE "pit_stops" (
  "race_id" INT(11) NOT NULL,
  "driver_id" INT(11) NOT NULL,
  "stop" INT(11) NOT NULL,
  "lap" INT(11) NOT NULL,
  "time" TIME NOT NULL,
  "duration" VARCHAR(255) DEFAULT NULL,
  "milliseconds" INT(11) DEFAULT NULL,
  "seconds" FLOAT AS (CAST(milliseconds AS FLOAT) / 1000) VIRTUAL,
  PRIMARY KEY ("race_id", "driver_id", "stop")
);
```

## Rows

- total=10990

| column | latest | sample | sample |
|---|---|---|---|
| race_id | 1132 | 1110 | 913 |
| driver_id | 858 | 807 | 815 |
| stop | 2 | 1 | 2 |
| lap | 38 | 12 | 29 |
| time | 16:05:23 | 15:26:56 | 21:00:56 |
| duration | 29.444 | 24.571 | 29.502 |
| milliseconds | 29444 | 24571 | 29502 |
| seconds | 29.444 | 24.571 | 29.502 |

## Columns

- race_id: 273 distinct, int 841..1132
  - top_values: 1111=101, 936=96, 851=88, 844=82, 970=82, 982=82, 884=79, 914=79, 1071=79, 1020=78
- driver_id: 74 distinct, int 1..860
  - top_values: 1=537, 815=517, 20=463, 817=462, 4=456, 822=435, 807=367, 830=361, 8=356, 832=329
- stop: 1=5344, 2=3602, 3=1467, 4=418, 5=120, 6=29, 7=3, 15=1, 42=1, 48=1, 51=1, 52=1, 57=1, 70=1, int 1..70
- lap: 74 distinct, int 1..78
  - stats: average=25.3147, median=25
- time: 7983 distinct
- duration: 7434 distinct
- milliseconds: 7434 distinct, int 12897..3069017
  - stats: average=85304.3, median=23629
- seconds: 7434 distinct, num 12.897..3069.02
  - stats: average=85.3043, median=23.629


# qualifying

```sql
CREATE TABLE "qualifying" (
  "qualify_id" INT(11) NOT NULL,
  "race_id" INT(11) NOT NULL DEFAULT '0',
  "driver_id" INT(11) NOT NULL DEFAULT '0',
  "constructor_id" INT(11) NOT NULL DEFAULT '0',
  "number" INT(11) NOT NULL DEFAULT '0',
  "position" INT(11) DEFAULT NULL,
  "q1" VARCHAR(255) DEFAULT NULL,
  "q2" VARCHAR(255) DEFAULT NULL,
  "q3" VARCHAR(255) DEFAULT NULL,
  PRIMARY KEY ("qualify_id")
);
```

## Rows

- total=10254

| column | latest | sample | sample |
|---|---|---|---|
| qualify_id | 10311 | 7496 | 6720 |
| race_id | 1132 | 986 | 949 |
| driver_id | 842 | 836 | 836 |
| constructor_id | 214 | 15 | 209 |
| number | 10 | 94 | 94 |
| position | 20 | 17 | 16 |
| q1 | 1:39.804 | 1:19.333 | 1:32.806 |
| q2 | null | null | null |
| q3 | null | null | null |

## Columns

- qualify_id: unique identifier, int 1..10311
- race_id: 482 distinct, int 1..1132
- driver_id: 170 distinct, int 1..860
- constructor_id: 47 distinct, int 1..215
- number: 55 distinct, int 0..99
  - stats: average=18.5266, median=14
- position: 28 distinct, int 1..28
  - stats: average=11.2121, median=11
- q1: 8954 distinct, nulls=154
- q2: 5320 distinct, nulls=4572
- q3: 3374 distinct, nulls=6713


# races

```sql
CREATE TABLE "races" (
  "race_id" INT(11) NOT NULL,
  "year" INT(11) NOT NULL DEFAULT '0',
  "round" INT(11) NOT NULL DEFAULT '0',
  "circuit_id" INT(11) NOT NULL DEFAULT '0',
  "name" VARCHAR(255) NOT NULL DEFAULT '',
  "date" DATE NOT NULL,
  "time" TIME DEFAULT NULL,
  "url" VARCHAR(255) DEFAULT NULL,
  "fp1_date" VARCHAR(255) DEFAULT NULL,
  "fp1_time" VARCHAR(255) DEFAULT NULL,
  "fp2_date" VARCHAR(255) DEFAULT NULL,
  "fp2_time" VARCHAR(255) DEFAULT NULL,
  "fp3_date" VARCHAR(255) DEFAULT NULL,
  "fp3_time" VARCHAR(255) DEFAULT NULL,
  "quali_date" VARCHAR(255) DEFAULT NULL,
  "quali_time" VARCHAR(255) DEFAULT NULL,
  "sprint_date" VARCHAR(255) DEFAULT NULL,
  "sprint_time" VARCHAR(255) DEFAULT NULL,
  PRIMARY KEY ("race_id")
);
```

## Rows

- total=1125

| column | latest | sample | sample |
|---|---|---|---|
| race_id | 1144 | 1055 | 11 |
| year | 2024 | 2021 | 2009 |
| round | 24 | 4 | 11 |
| circuit_id | 24 | 4 | 12 |
| name | Abu Dhabi Grand Prix | Spanish Grand Prix | European Grand Prix |
| date | 2024-12-08 | 2021-05-09 | 2009-08-23 |
| time | 13:00:00 | 13:00:00 | 12:00:00 |
| url | https://en.wikipedia.org/wiki/2024_Abu_Dhabi_Grand_Prix | http://en.wikipedia.org/wiki/2021_Spanish_Grand_Prix | http://en.wikipedia.org/wiki/2009_European_Grand_Prix |
| fp1_date | 2024-12-06 | 2021-05-07 | null |
| fp1_time | 09:30:00 | null | null |
| fp2_date | 2024-12-06 | 2021-05-07 | null |
| fp2_time | 13:00:00 | null | null |
| fp3_date | 2024-12-07 | 2021-05-08 | null |
| fp3_time | 10:30:00 | null | null |
| quali_date | 2024-12-07 | 2021-05-08 | null |
| quali_time | 14:00:00 | null | null |
| sprint_date | null | null | null |
| sprint_time | null | null | null |

## Columns

- race_id: unique identifier, int 1..1144
- year: 75 distinct, int 1950..2024
  - stats: average=1992.7, median=1994
- round: 24 distinct, int 1..24
  - stats: average=8.57956, median=8
- circuit_id: 77 distinct, int 1..80
- name: 54 distinct
- date: all distinct
- time: 34 distinct, nulls=731
- url: all distinct
- fp1_date: all distinct, nulls=1035
- fp1_time: 20 distinct, nulls=1057
- fp2_date: all distinct, nulls=1035
- fp2_time: "15:00:00"=22, "13:00:00"=8, "06:00:00"=5, "10:30:00"=4, "14:00:00"=4, "21:00:00"=4, "17:00:00"=3, "21:30:00"=3, "22:00:00"=3, "05:00:00"=2, "14:30:00"=2, "07:30:00"=1, "08:00:00"=1, "09:30:00"=1, "15:30:00"=1, "17:30:00"=1, "18:00:00"=1, "18:30:00"=1, "20:30:00"=1, nulls=1057
- fp3_date: all distinct, nulls=1053
- fp3_time: "10:30:00"=14, "11:00:00"=9, "09:30:00"=4, "02:30:00"=3, "16:30:00"=3, "17:00:00"=3, "01:30:00"=2, "03:00:00"=2, "10:00:00"=2, "13:30:00"=2, "17:30:00"=2, "04:30:00"=1, "08:30:00"=1, "11:30:00"=1, "12:00:00"=1, "12:30:00"=1, "14:00:00"=1, "19:00:00"=1, nulls=1072
- quali_date: all distinct, nulls=1035
- quali_time: "14:00:00"=24, "13:00:00"=7, "20:00:00"=7, "15:00:00"=6, "06:00:00"=5, "17:00:00"=5, "21:00:00"=3, "05:00:00"=2, "18:00:00"=2, "22:00:00"=2, "07:00:00"=1, "08:00:00"=1, "12:00:00"=1, "16:00:00"=1, "19:00:00"=1, nulls=1057
- sprint_date: "2021-07-17"=1, "2021-09-11"=1, "2021-11-13"=1, "2022-04-23"=1, "2022-07-09"=1, "2022-11-12"=1, "2023-04-29"=1, "2023-07-01"=1, "2023-07-29"=1, "2023-10-07"=1, "2023-10-21"=1, "2023-11-04"=1, "2024-04-20"=1, "2024-05-04"=1, "2024-06-29"=1, "2024-10-19"=1, "2024-11-02"=1, "2024-11-30"=1, nulls=1107
- sprint_time: "14:30:00"=4, "03:00:00"=1, "10:00:00"=1, "13:00:00"=1, "13:30:00"=1, "14:00:00"=1, "16:00:00"=1, "17:30:00"=1, "18:00:00"=1, "18:30:00"=1, "19:30:00"=1, "22:00:00"=1, nulls=1110


# races_ext

```sql
CREATE TABLE races_ext(
  race_id INT,
  year INT,
  round INT,
  circuit_id INT,
  name TEXT,
  date NUM,
  time NUM,
  url TEXT,
  fp1_date TEXT,
  fp1_time TEXT,
  fp2_date TEXT,
  fp2_time TEXT,
  fp3_date TEXT,
  fp3_time TEXT,
  quali_date TEXT,
  quali_time TEXT,
  sprint_date TEXT,
  sprint_time TEXT,
  is_pit_data_available,
  short_name,
  has_sprint,
  max_points
);
```


# results

```sql
CREATE TABLE "results" (
  "result_id" INT(11) NOT NULL,
  "race_id" INT(11) NOT NULL DEFAULT '0',
  "driver_id" INT(11) NOT NULL DEFAULT '0',
  "constructor_id" INT(11) NOT NULL DEFAULT '0',
  "number" INT(11) DEFAULT NULL,
  "grid" INT(11) NOT NULL DEFAULT '0',
  "position" INT(11) DEFAULT NULL,
  "position_text" VARCHAR(255) NOT NULL DEFAULT '',
  "position_order" INT(11) NOT NULL DEFAULT '0',
  "points" FLOAT NOT NULL DEFAULT '0',
  "laps" INT(11) NOT NULL DEFAULT '0',
  "time" VARCHAR(255) DEFAULT NULL,
  "milliseconds" INT(11) DEFAULT NULL,
  "fastest_lap" INT(11) DEFAULT NULL,
  "rank" INT(11) DEFAULT '0',
  "fastest_lap_time" VARCHAR(255) DEFAULT NULL,
  "fastest_lap_speed" VARCHAR(255) DEFAULT NULL,
  "status_id" INT(11) NOT NULL DEFAULT '0',
  PRIMARY KEY ("result_id")
);
```

## Rows

- total=26519

| column | latest | sample | sample |
|---|---|---|---|
| result_id | 26524 | 15023 | 2773 |
| race_id | 1132 | 607 | 150 |
| driver_id | 842 | 235 | 31 |
| constructor_id | 214 | 6 | 3 |
| number | 10 | 8 | 6 |
| grid | 19 | 11 | 6 |
| position | null | null | null |
| position_text | W | R | R |
| position_order | 20 | 24 | 19 |
| points | 0 | 0 | 0 |
| laps | 0 | 2 | 52 |
| time | null | null | null |
| milliseconds | null | null | null |
| fastest_lap | null | null | null |
| rank | 0 | null | null |
| fastest_lap_time | null | null | null |
| fastest_lap_speed | null | null | null |
| status_id | 6 | 3 | 5 |

## Columns

- result_id: unique identifier, int 1..26524
- race_id: 1113 distinct, int 1..1132
- driver_id: 859 distinct, int 1..860
- constructor_id: 211 distinct, int 1..215
- number: 129 distinct, nulls=6, int 0..208
  - stats: average=18.0477, median=16
- grid: 35 distinct, int 0..34
  - stats: average=11.1458, median=11
- position: 33 distinct, nulls=10928, int 1..33
  - stats: average=7.99974, median=7
- position_text: 39 distinct
- position_order: 39 distinct, int 1..39
  - stats: average=12.8148, median=12
- points: 39 distinct, num 0..50
  - stats: average=1.95958, median=0
- laps: 172 distinct, int 0..200
  - stats: average=46.2283, median=53
- time: 7271 distinct, nulls=18986
- milliseconds: 7492 distinct, nulls=18986, int 207071..15090540
  - stats: average=6.20872e+06, median=5.79688e+06
- fastest_lap: 80 distinct, nulls=18499, int 1..85
  - stats: average=42.6167, median=46
- rank: 25 distinct, nulls=18249, int 0..24
  - stats: average=10.3485, median=10
- fastest_lap_time: 7297 distinct, nulls=18499
- fastest_lap_speed: 7513 distinct, nulls=18499
- status_id: 137 distinct, int 1..141


# retirements

```sql
CREATE TABLE retirements(
  race_id INT,
  driver_id INT,
  lap,
  position_order INT,
  status_id INT,
  retirement_type
);
```

## Rows

- total=11568

| column | latest | sample | sample |
|---|---|---|---|
| race_id | 1132 | 568 | 129 |
| driver_id | 847 | 276 | 8 |
| lap | 34 | 25 | 6 |
| position_order | 19 | 19 | 20 |
| status_id | 34 | 6 | 5 |
| retirement_type | Retirement (Mechanical Problem) | Retirement (Mechanical Problem) | Retirement (Mechanical Problem) |

## Columns

- race_id: 1100 distinct, int 1..1132
- driver_id: 790 distinct, int 1..858
- lap: 153 distinct
- position_order: 38 distinct, int 2..39
  - stats: average=19.2922, median=19
- status_id: 105 distinct, int 2..141
- retirement_type: "Retirement (Mechanical Problem)"=8723, "Retirement (Driver Error)"=2700, "Retirement (Disqualification)"=145


# seasons

```sql
CREATE TABLE "seasons" (
  "year" INT(11) NOT NULL DEFAULT '0',
  "url" VARCHAR(255) NOT NULL DEFAULT '',
  PRIMARY KEY ("year")
);
```

## Rows

- total=75

| column | latest | sample | sample |
|---|---|---|---|
| year | 2024 | 2003 | 1957 |
| url | https://en.wikipedia.org/wiki/2024_Formula_One_World_Championship | http://en.wikipedia.org/wiki/2003_Formula_One_season | http://en.wikipedia.org/wiki/1957_Formula_One_season |

## Columns

- year: unique identifier, int 1950..2024
  - stats: average=1987, median=1987
- url: all distinct


# short_constructor_names

```sql
CREATE TABLE "short_constructor_names" (
  "constructor_ref" VARCHAR(255) NOT NULL DEFAULT '',
  "short_name" VARCHAR(255) NOT NULL DEFAULT '',
  PRIMARY KEY ("constructor_ref")
);
```

## Rows

- total=44

| column | latest | sample | sample |
|---|---|---|---|
| constructor_ref | team_lotus | mclaren-alfa_romeo | haas |
| short_name | Lotus | McLaren | Haas |

## Columns

- constructor_ref: unique identifier
- short_name: "Cooper"=10, "Lotus"=8, "Brabham"=5, "McLaren"=4, "De Tomaso"=3, "Eagle"=2, "LDS"=2, "March"=2, "Shadow"=2, "Alpha Tauri"=1, "Alpine"=1, "BRM"=1, "Haas"=1, "Matra"=1, "Spkyer"=1


# short_grand_prix_names

```sql
CREATE TABLE "short_grand_prix_names" (
  "full_name" VARCHAR(255) NOT NULL DEFAULT '',
  "short_name" VARCHAR(255) NOT NULL DEFAULT '',
  PRIMARY KEY ("full_name")
);
```

## Rows

- total=40

| column | latest | sample | sample |
|---|---|---|---|
| full_name | United States Grand Prix | Spanish Grand Prix | San Marino Grand Prix |
| short_name | United States | Spain | San Marino |

## Columns

- full_name: unique identifier
- short_name: 38 distinct


# sprint_results

```sql
CREATE TABLE "sprint_results" (
  "result_id" INT(11) NOT NULL,
  "race_id" INT(11) NOT NULL DEFAULT '0',
  "driver_id" INT(11) NOT NULL DEFAULT '0',
  "constructor_id" INT(11) NOT NULL DEFAULT '0',
  "number" INT(11) DEFAULT NULL,
  "grid" INT(11) NOT NULL DEFAULT '0',
  "position" INT(11) DEFAULT NULL,
  "position_text" VARCHAR(255) NOT NULL DEFAULT '',
  "position_order" INT(11) NOT NULL DEFAULT '0',
  "points" FLOAT NOT NULL DEFAULT '0',
  "laps" INT(11) NOT NULL DEFAULT '0',
  "time" VARCHAR(255) DEFAULT NULL,
  "milliseconds" INT(11) DEFAULT NULL,
  "fastest_lap" INT(11) DEFAULT NULL,
  "fastest_lap_time" VARCHAR(255) DEFAULT NULL,
  "fastest_lap_speed" VARCHAR(255) DEFAULT NULL,
  "status_id" INT(11) NOT NULL DEFAULT '0',
  PRIMARY KEY ("result_id")
);
```

## Rows

- total=300

| column | latest | sample | sample |
|---|---|---|---|
| result_id | 300 | 287 | 99 |
| race_id | 1131 | 1131 | 1084 |
| driver_id | 855 | 844 | 20 |
| constructor_id | 15 | 6 | 117 |
| number | 24 | 16 | 5 |
| grid | 19 | 10 | 20 |
| position | 20 | 7 | 19 |
| position_text | 20 | 7 | 19 |
| position_order | 20 | 7 | 19 |
| points | 0 | 2 | 0 |
| laps | 23 | 23 | 21 |
| time | +53.143 | +13.424 | null |
| milliseconds | 1654532 | 1614813 | null |
| fastest_lap | 6 | 5 | 4 |
| fastest_lap_time | 1:10.613 | 1:09.352 | 1:10.317 |
| fastest_lap_speed | null | null | null |
| status_id | 1 | 1 | 130 |

## Columns

- result_id: unique identifier, int 1..300
- race_id: 1061=20, 1065=20, 1071=20, 1077=20, 1084=20, 1095=20, 1101=20, 1107=20, 1110=20, 1115=20, 1116=20, 1118=20, 1125=20, 1126=20, 1131=20, int 1061..1131
- driver_id: 29 distinct, int 1..859
- constructor_id: 1=30, 3=30, 6=30, 9=30, 117=30, 131=30, 210=30, 214=30, 51=24, 213=24, 15=6, 215=6, int 1..215
- number: 30 distinct, int 1..99
  - stats: average=27.5733, median=20
- grid: 21 distinct, int 0..20
  - stats: average=10.1933, median=10
- position: 20 distinct, nulls=15, int 1..20
  - stats: average=10.0421, median=10
- position_text: 23 distinct
- position_order: 20 distinct, int 1..20
  - stats: average=10.5, median=10.5
- points: 0=195, 1=15, 2=15, 3=15, 4=12, 5=12, 6=12, 7=12, 8=12, num 0..8
- laps: 24=79, 19=71, 17=38, 23=38, 21=20, 11=19, 18=19, 0=6, 2=3, 10=2, 16=2, 1=1, 8=1, 12=1, int 0..24
- time: all distinct, nulls=19
- milliseconds: all distinct, nulls=19, int 1498433..2128165
  - stats: average=1.81086e+06, median=1.84778e+06
- fastest_lap: 23 distinct, nulls=9, int 2..24
  - stats: average=9.5567, median=8
- fastest_lap_time: 290 distinct, nulls=9
- fastest_lap_speed: all NULL
- status_id: 1=281, 31=10, 3=3, 130=3, 10=1, 23=1, 76=1, int 1..130


# status

```sql
CREATE TABLE "status" (
  "status_id" INT(11) NOT NULL,
  "status" VARCHAR(255) NOT NULL DEFAULT '',
  PRIMARY KEY ("status_id")
);
```

## Rows

- total=139

| column | latest | sample | sample |
|---|---|---|---|
| status_id | 141 | 37 | 30 |
| status | Cooling system | Throttle | Driveshaft |

## Columns

- status_id: unique identifier, int 1..141
- status: all distinct


# tdr_overrides

```sql
CREATE TABLE "tdr_overrides" (
  "year" INT(11) NOT NULL DEFAULT '0',
  "constructor_ref" VARCHAR(255) NOT NULL DEFAULT '',
  "driver_ref" VARCHAR(255) NOT NULL DEFAULT '',
  "team_driver_rank" INT(11) NULL DEFAULT '0',
  PRIMARY KEY ("year", "constructor_ref", "driver_ref")
);
```

## Rows

- total=48

| column | latest | sample | sample |
|---|---|---|---|
| year | 2022 | 2021 | 2016 |
| constructor_ref | mercedes | mclaren | red_bull |
| driver_ref | russell | ricciardo | max_verstappen |
| team_driver_rank | 2 | 1 | 3 |

## Columns

- year: 2022=7, 2004=4, 2007=4, 2015=4, 2016=4, 2018=4, 2019=4, 2021=4, 2017=3, 2008=2, 2009=2, 2012=2, 2014=2, 2020=2, int 2004..2022
- constructor_ref: "red_bull"=10, "ferrari"=8, "mclaren"=6, "renault"=5, "haas"=4, "mercedes"=4, "toyota"=4, "aston_martin"=3, "alphatauri"=2, "toro_rosso"=2
- driver_ref: 30 distinct
  - top_values: "ricciardo"=5, "vettel"=4, "hamilton"=3, "leclerc"=3, "alonso"=2, "grosjean"=2, "hulkenberg"=2, "kevin_magnussen"=2, "kvyat"=2, "max_verstappen"=2
- team_driver_rank: 2=22, 1=21, 3=4, 4=1, int 1..4


# team_driver_ranks

```sql
CREATE TABLE team_driver_ranks(
  year INT,
  constructor_id INT,
  constructor_ref TEXT,
  driver_id INT,
  driver_ref TEXT,
  team_driver_rank
);
```

## Rows

- total=3530

| column | latest | sample | sample |
|---|---|---|---|
| year | 2024 | 1950 | 1966 |
| constructor_id | 215 | 105 | 167 |
| constructor_ref | rb | maserati | cooper-maserati |
| driver_id | 852 | 800 | 358 |
| driver_ref | tsunoda | pagani | rindt |
| team_driver_rank | 1 | 6 | 2 |

## Columns

- year: 75 distinct, int 1950..2024
  - stats: average=1976.43, median=1973
- constructor_id: 210 distinct, int 1..215
- constructor_ref: 210 distinct
- driver_id: 852 distinct, int 1..860
- driver_ref: 852 distinct
- team_driver_rank: 29 distinct


- Skipped 2 table(s) due to Profile generation errors: drivers_ext, races_ext
