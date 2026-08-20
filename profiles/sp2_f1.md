---
generator: db-snooper
version: 0.0.31
generated_at_utc: 2026-08-20T17:29:05.742849Z
dialect: sqlite
database: /var/folders/9j/b9bx_drd53sc6zbpsqyrjy4h0000gn/T/dbsnoop-q7_4iocc/f1.sqlite
schema: main
---

# "circuits"  (rows=77)

columns:
"circuit_id" int PK: unique identifier, 1..80
"circuit_ref" varchar255 NOTNULL: all distinct
"name" varchar255 NOTNULL: all distinct
"location" varchar255: 75 distinct
"country" varchar255: 35 distinct
"lat" float: all distinct, -37.8497..57.2653, avg=33.4429, median=40.9517
"lng" float: all distinct, -118.189..144.968, avg=1.07668, median=3.93083
"alt" int: 66 distinct, -7..2227, avg=247.013, median=129
"url" varchar255 NOTNULL: all distinct

indexes: none
fk: none

samples:
| column | latest | sample | sample |
|---|---|---|---|
| circuit_id | 80 | 39 | 79 |
| circuit_ref | vegas | zandvoort | miami |
| name | Las Vegas Strip Street Circuit | Circuit Park Zandvoort | Miami International Autodrome |
| location | Las Vegas | Zandvoort | Miami |
| country | United States | Netherlands | USA |
| lat | 36.1147 | 52.3888 | 25.9581 |
| lng | -115.173 | 4.54092 | -80.2389 |
| alt | 642 | 6 | 0 |
| url | https://en.wikipedia.org/wiki/Las_Vegas_Grand_Prix#Circuit | http://en.wikipedia.org/wiki/Circuit_Zandvoort | http://en.wikipedia.org/wiki/Miami_International_Autodrome |

# "circuits_ext"  (rows=77)

columns:
"circuit_id" int: unique identifier, 1..80
"circuit_ref" text: all distinct
"name" text: all distinct
"location" text: 75 distinct
"country" text: 35 distinct
"lat" float: all distinct, -37.8497..57.2653, avg=33.4429, median=40.9517
"lng" float: all distinct, -118.189..144.968, avg=1.07668, median=3.93083
"alt" int: 66 distinct, -7..2227, avg=247.013, median=129
"url" text: all distinct
"last_race_year" int: 41 distinct
"number_of_races" int: 34 distinct

indexes: none
fk: none

samples:
| column | latest | sample | sample |
|---|---|---|---|
| circuit_id | 80 | 1 | 18 |
| circuit_ref | vegas | albert_park | interlagos |
| name | Las Vegas Strip Street Circuit | Albert Park Grand Prix Circuit | Autódromo José Carlos Pace |
| location | Las Vegas | Melbourne | São Paulo |
| country | United States | Australia | Brazil |
| lat | 36.1147 | -37.8497 | -23.7036 |
| lng | -115.173 | 144.968 | -46.6997 |
| alt | 642 | 10 | 785 |
| url | https://en.wikipedia.org/wiki/Las_Vegas_Grand_Prix#Circuit | http://en.wikipedia.org/wiki/Melbourne_Grand_Prix_Circuit | http://en.wikipedia.org/wiki/Aut%C3%B3dromo_Jos%C3%A9_Carlos_Pace |
| last_race_year | 2024 | 2024 | 2024 |
| number_of_races | 2 | 27 | 41 |

# "constructor_results"  (rows=12505)

columns:
"constructor_results_id" int PK: unique identifier, 1..17009
"race_id" int NOTNULL: 1048 distinct, 1..1132
"constructor_id" int NOTNULL: 175 distinct, 1..215
"points" float: 60 distinct, 0..66, avg=3.98617, median=0
"status" varchar255: "D"=17, nulls=12488

indexes: none
fk: none

samples:
| column | latest | sample | sample |
|---|---|---|---|
| constructor_results_id | 17009 | 16981 | 4892 |
| race_id | 1132 | 1130 | 408 |
| constructor_id | 214 | 1 | 18 |
| points | 0 | 25 | 0 |
| status | null | null | null |

# "constructor_standings"  (rows=13271)

columns:
"constructor_standings_id" int PK: unique identifier, 1..28852
"race_id" int NOTNULL: 1049 distinct, 1..1132
"constructor_id" int NOTNULL: 160 distinct, 1..215
"points" float NOTNULL: 557 distinct, 0..860, avg=35.6811, median=7
"position" int: 22 distinct, 1..22, avg=7.24165, median=7
"position_text" varchar255: 23 distinct
"wins" int NOTNULL: 22 distinct, 0..21, avg=0.686987, median=0

indexes: none
fk: none

samples:
| column | latest | sample | sample |
|---|---|---|---|
| constructor_standings_id | 28852 | 10973 | 24359 |
| race_id | 1132 | 481 | 346 |
| constructor_id | 214 | 54 | 5 |
| points | 9 | 4 | 10 |
| position | 8 | 11 | 9 |
| position_text | 8 | 11 | 9 |
| wins | 0 | 0 | 0 |

# "constructors"  (rows=212)

columns:
"constructor_id" int PK: unique identifier, 1..215
"constructor_ref" varchar255 NOTNULL: all distinct
"name" varchar255 NOTNULL: all distinct
"nationality" varchar255: 24 distinct
"url" varchar255 NOTNULL: 175 distinct

indexes: none
fk: none

samples:
| column | latest | sample | sample |
|---|---|---|---|
| constructor_id | 215 | 118 | 108 |
| constructor_ref | rb | vanwall | epperly |
| name | RB F1 Team | Vanwall | Epperly |
| nationality | Italian | British | American |
| url | http://en.wikipedia.org/wiki/RB_Formula_One_Team | http://en.wikipedia.org/wiki/Vanwall | http://en.wikipedia.org/wiki/Epperly |

# "constructors_ext"  (rows=212)

columns:
"constructor_id" int: unique identifier, 1..215
"constructor_ref" text: all distinct
"name" text: all distinct
"nationality" text: 24 distinct
"url" text: 175 distinct
"short_name" text: 172 distinct

indexes: none
fk: none

samples:
| column | latest | sample | sample |
|---|---|---|---|
| constructor_id | 215 | 62 | 188 |
| constructor_ref | rb | rebaque | mclaren-seren |
| name | RB F1 Team | Rebaque | McLaren-Serenissima |
| nationality | Italian | Mexican | British |
| url | http://en.wikipedia.org/wiki/RB_Formula_One_Team | http://en.wikipedia.org/wiki/Rebaque | http://en.wikipedia.org/wiki/Team_McLaren |
| short_name | RB F1 Team | Rebaque | McLaren |

# "driver_standings"  (rows=34595)

columns:
"driver_standings_id" int PK: unique identifier, 1..72871
"race_id" int NOTNULL: 1113 distinct, 1..1132
"driver_id" int NOTNULL: 852 distinct, 1..860
"points" float NOTNULL: 429 distinct, 0..575, avg=14.1149, median=1
"position" int: 108 distinct, 1..108, avg=19.7789, median=16
"position_text" varchar255: digits, 109 distinct
"wins" int NOTNULL: 20 distinct, 0..19, avg=0.273074, median=0

indexes: none
fk: none

samples:
| column | latest | sample | sample |
|---|---|---|---|
| driver_standings_id | 72871 | 69231 | 58644 |
| race_id | 1132 | 1012 | 518 |
| driver_id | 860 | 830 | 203 |
| points | 6 | 39 | 20 |
| position | 14 | 3 | 3 |
| position_text | 14 | 3 | 3 |
| wins | 0 | 0 | 2 |

# "driver_standings_ext"  (rows=35012)

columns:
"driver_standings_id" int: 34596 distinct, 0..72871
"race_id" int: 1113 distinct, 1..1132
"driver_id" int: 852 distinct, 1..860
"points" float: 429 distinct, 0..575, avg=13.9468, median=1
"position" int: 108 distinct, 1..108, avg=19.7878, median=16
"position_text" text: digits, 109 distinct, nulls=417
"wins" int: 20 distinct, 0..19, avg=0.269822, median=0

indexes: none
fk: none

samples:
| column | latest | sample | sample |
|---|---|---|---|
| driver_standings_id | 72871 | 68284 | 72311 |
| race_id | 1132 | 975 | 1114 |
| driver_id | 860 | 8 | 856 |
| points | 6 | 73 | 0 |
| position | 14 | 4 | 21 |
| position_text | 14 | 4 | 21 |
| wins | 0 | 0 | 0 |

# "drivers"  (rows=859)

columns:
"driver_id" int PK: unique identifier, 1..860
"driver_ref" varchar255 NOTNULL: all distinct
"number" int: 46 distinct, nulls=802, 2..99, avg=33.5088, median=24
"code" varchar3: 96 distinct, nulls=757
"forename" varchar255 NOTNULL: 478 distinct
"surname" varchar255 NOTNULL: 800 distinct
"full_name" varchar255: all distinct
"dob" date: 841 distinct
"nationality" varchar255: 42 distinct
"url" varchar255 NOTNULL: all distinct

indexes: none
fk: none

samples:
| column | latest | sample | sample |
|---|---|---|---|
| driver_id | 860 | 133 | 501 |
| driver_ref | bearman | caffi | schell |
| number | 38 | null | null |
| code | BEA | null | null |
| forename | Oliver | Alex | Harry |
| surname | Bearman | Caffi | Schell |
| full_name | Oliver Bearman | Alex Caffi | Harry Schell |
| dob | 2005-05-08 | 1964-03-18 | 1921-06-29 |
| nationality | British | Italian | American |
| url | http://en.wikipedia.org/wiki/Oliver_Bearman | http://en.wikipedia.org/wiki/Alex_Caffi | http://en.wikipedia.org/wiki/Harry_Schell |

# "drivers_ext"  (rows=859)

columns:
"driver_id" int: unique identifier, 1..860
"driver_ref" text: all distinct
"number" int: 46 distinct, nulls=802, 2..99, avg=33.5088, median=24
"code" text: 521 distinct
"forename" text: 478 distinct
"surname" text: 800 distinct
"full_name" text: all distinct
"dob" numeric→text: 841 distinct
"nationality" text: 42 distinct
"url" text: all distinct

indexes: none
fk: none

samples:
| column | latest | sample | sample |
|---|---|---|---|
| driver_id | 860 | 757 | 828 |
| driver_ref | bearman | peters | ericsson |
| number | 38 | null | 9 |
| code | BEA | PET | ERI |
| forename | Oliver | Josef | Marcus |
| surname | Bearman | Peters | Ericsson |
| full_name | Oliver Bearman | Josef Peters | Marcus Ericsson |
| dob | 2005-05-08 | 1914-09-16 | 1990-09-02 |
| nationality | British | German | Swedish |
| url | http://en.wikipedia.org/wiki/Oliver_Bearman | http://en.wikipedia.org/wiki/Josef_Peters_(driver) | http://en.wikipedia.org/wiki/Marcus_Ericsson |

# "drives"  (rows=3784)

columns:
"year" int: 75 distinct, 1950..2024, avg=1976.01, median=1972
"driver_id" int: 859 distinct, 1..860
"drive_id" int: 1=3222, 2=299, -1=163, 3=78, 4=19, 5=3
"constructor_id" int: 212 distinct, -1..215
"first_round" int: 1=1721, 2=391, 3=325, 5=194, 4=188, 7=165, 6=157, 8=141, 9=112, 10=85, 11=64, 12=58, 14=52, 13=45, 15=45, 16=30, 17=9, 18=1, 19=1, 1..19
"last_round" int: 22 distinct, 1..22, avg=10.226, median=10
"is_first_drive_of_season" int: 1=3222, 0=562
"is_final_drive_of_season" int: 1=3218, 0=566

indexes: none
fk: none

samples:
| column | latest | sample | sample |
|---|---|---|---|
| year | 2024 | 1957 | 1976 |
| driver_id | 860 | 525 | 246 |
| drive_id | 1 | 1 | 2 |
| constructor_id | 6 | 114 | 59 |
| first_round | 2 | 3 | 16 |
| last_round | 2 | 3 | 16 |
| is_first_drive_of_season | 1 | 1 | 0 |
| is_final_drive_of_season | 1 | 1 | 1 |

# "lap_positions"  (rows=≈613112)

columns:
"race_id" int
"driver_id" int
"lap" int
"position" int
"lap_type" null

indexes: none
fk: none


# "lap_time_stats"  (rows=10789)

columns:
"race_id" int: 531 distinct, 1..1131
"driver_id" int: 141 distinct, 1..860
"avg_milliseconds" float: 10784 distinct
"avg_seconds" float: 10788 distinct
"stdev_milliseconds" float: 10676 distinct
"stdev_seconds" float: 10676 distinct

indexes: none
fk: none

samples:
| column | latest | sample | sample |
|---|---|---|---|
| race_id | 1131 | 929 | 216 |
| driver_id | 858 | 831 | 82 |
| avg_milliseconds | 73465.3 | 102246 | 110883 |
| avg_seconds | 73.4653 | 102.246 | 110.883 |
| stdev_milliseconds | 4993.76 | 5120.49 | 4184.03 |
| stdev_seconds | 4.99376 | 5.12049 | 4.18403 |

# "lap_times"  (rows=≈575029)

columns:
"race_id" int PK
"driver_id" int PK
"lap" int PK
"position" int
"time" varchar255
"milliseconds" int
"seconds" float

indexes: none
fk: none


# "lap_times_ext"  (rows=≈575029)

columns:
"race_id" int
"driver_id" int
"lap" int
"position" int
"time" text
"milliseconds" int
"seconds" float
"running_milliseconds" null

indexes: none
fk: none


# "liveries"  (rows=64)

columns:
"constructor_ref" varchar255 PK: 37 distinct, "renault"=6, "sauber"=5, "williams"=5, "jordan"=4, "mclaren"=4, "benneton"=3, "hrt"=3, "caterham"=2, "force_india"=2, "haas"=2
"start_year" int PK: 32 distinct, 1950..2021, avg=2004.72, median=2007, 2006=6, 2010=6, 1997=4, 2012=4, 2016=3, 2017=3, 2021=3, 1985=2, 1991=2, 1992=2
"end_year" int PK: 28 distinct, nulls=10, 1985..2020, avg=2007.46, median=2009, 2005=4, 2009=4, 2011=4, 2016=4, 2006=3, 2020=3, 1991=2, 1996=2, 2001=2, 2008=2
"primary_hex_code" varchar255 NOTNULL: 52 distinct

indexes: none
fk: none

samples:
| column | latest | sample | sample |
|---|---|---|---|
| constructor_ref | williams | sauber | toyota |
| start_year | 2014 | 1993 | 2002 |
| end_year | null | 1994 | 2009 |
| primary_hex_code | #005AFF | #000000 | #B30101 |

# "pit_stops"  (rows=10990)

columns:
"race_id" int PK: 273 distinct, 841..1132, 1111=101, 936=96, 851=88, 844=82, 970=82, 982=82, 884=79, 914=79, 1071=79, 1020=78
"driver_id" int PK: 74 distinct, 1..860, 1=537, 815=517, 20=463, 817=462, 4=456, 822=435, 807=367, 830=361, 8=356, 832=329
"stop" int PK: 1=5344, 2=3602, 3=1467, 4=418, 5=120, 6=29, 7=3, 15=1, 42=1, 48=1, 51=1, 52=1, 57=1, 70=1, 1..70
"lap" int NOTNULL: 74 distinct, 1..78, avg=25.3147, median=25
"time" time NOTNULL: 7983 distinct
"duration" varchar255: 7434 distinct
"milliseconds" int: 7434 distinct, 12897..3069017, avg=85304.3, median=23629
"seconds" float: 7434 distinct, 12.897..3069.02, avg=85.3043, median=23.629

indexes: none
fk: none

samples:
| column | latest | sample | sample |
|---|---|---|---|
| race_id | 1132 | 1083 | 940 |
| driver_id | 858 | 839 | 832 |
| stop | 2 | 2 | 2 |
| lap | 38 | 22 | 27 |
| time | 16:05:23 | 16:31:35 | 14:49:26 |
| duration | 29.444 | 30.342 | 39.345 |
| milliseconds | 29444 | 30342 | 39345 |
| seconds | 29.444 | 30.342 | 39.345 |

# "qualifying"  (rows=10254)

columns:
"qualify_id" int PK: unique identifier, 1..10311
"race_id" int NOTNULL: 482 distinct, 1..1132
"driver_id" int NOTNULL: 170 distinct, 1..860
"constructor_id" int NOTNULL: 47 distinct, 1..215
"number" int NOTNULL: 55 distinct, 0..99, avg=18.5266, median=14
"position" int: 28 distinct, 1..28, avg=11.2121, median=11
"q1" varchar255: 8954 distinct, nulls=154
"q2" varchar255: 5320 distinct, nulls=4572
"q3" varchar255: 3374 distinct, nulls=6713

indexes: none
fk: none

samples:
| column | latest | sample | sample |
|---|---|---|---|
| qualify_id | 10311 | 419 | 5861 |
| race_id | 1132 | 38 | 900 |
| driver_id | 842 | 21 | 817 |
| constructor_id | 214 | 4 | 9 |
| number | 10 | 3 | 3 |
| position | 20 | 7 | 2 |
| q1 | 1:39.804 | 1:33.556 | 1:30.775 |
| q2 | null | 1:32.889 | 1:42.295 |
| q3 | null | 1:34.056 | 1:44.548 |

# "races"  (rows=1125)

columns:
"race_id" int PK: unique identifier, 1..1144
"year" int NOTNULL: 75 distinct, 1950..2024, avg=1992.7, median=1994
"round" int NOTNULL: 24 distinct, 1..24, avg=8.57956, median=8
"circuit_id" int NOTNULL: 77 distinct, 1..80
"name" varchar255 NOTNULL: 54 distinct
"date" date NOTNULL: all distinct
"time" time: 34 distinct, nulls=731
"url" varchar255: all distinct
"fp1_date" varchar255: iso-date, all distinct, nulls=1035
"fp1_time" varchar255: 20 distinct, nulls=1057
"fp2_date" varchar255: iso-date, all distinct, nulls=1035
"fp2_time" varchar255: "15:00:00"=22, "13:00:00"=8, "06:00:00"=5, "10:30:00"=4, "14:00:00"=4, "21:00:00"=4, "17:00:00"=3, "21:30:00"=3, "22:00:00"=3, "05:00:00"=2, "14:30:00"=2, "07:30:00"=1, "08:00:00"=1, "09:30:00"=1, "15:30:00"=1, "17:30:00"=1, "18:00:00"=1, "18:30:00"=1, "20:30:00"=1, nulls=1057
"fp3_date" varchar255: iso-date, all distinct, nulls=1053
"fp3_time" varchar255: "10:30:00"=14, "11:00:00"=9, "09:30:00"=4, "02:30:00"=3, "16:30:00"=3, "17:00:00"=3, "01:30:00"=2, "03:00:00"=2, "10:00:00"=2, "13:30:00"=2, "17:30:00"=2, "04:30:00"=1, "08:30:00"=1, "11:30:00"=1, "12:00:00"=1, "12:30:00"=1, "14:00:00"=1, "19:00:00"=1, nulls=1072
"quali_date" varchar255: iso-date, all distinct, nulls=1035
"quali_time" varchar255: "14:00:00"=24, "13:00:00"=7, "20:00:00"=7, "15:00:00"=6, "06:00:00"=5, "17:00:00"=5, "21:00:00"=3, "05:00:00"=2, "18:00:00"=2, "22:00:00"=2, "07:00:00"=1, "08:00:00"=1, "12:00:00"=1, "16:00:00"=1, "19:00:00"=1, nulls=1057
"sprint_date" varchar255: "2021-07-17"=1, "2021-09-11"=1, "2021-11-13"=1, "2022-04-23"=1, "2022-07-09"=1, "2022-11-12"=1, "2023-04-29"=1, "2023-07-01"=1, "2023-07-29"=1, "2023-10-07"=1, "2023-10-21"=1, "2023-11-04"=1, "2024-04-20"=1, "2024-05-04"=1, "2024-06-29"=1, "2024-10-19"=1, "2024-11-02"=1, "2024-11-30"=1, nulls=1107
"sprint_time" varchar255: "14:30:00"=4, "03:00:00"=1, "10:00:00"=1, "13:00:00"=1, "13:30:00"=1, "14:00:00"=1, "16:00:00"=1, "17:30:00"=1, "18:00:00"=1, "18:30:00"=1, "19:30:00"=1, "22:00:00"=1, nulls=1110

indexes: none
fk: none

samples:
| column | latest | sample | sample |
|---|---|---|---|
| race_id | 1144 | 961 | 336 |
| year | 2024 | 2016 | 1990 |
| round | 24 | 14 | 16 |
| circuit_id | 24 | 14 | 29 |
| name | Abu Dhabi Grand Prix | Italian Grand Prix | Australian Grand Prix |
| date | 2024-12-08 | 2016-09-04 | 1990-11-04 |
| time | 13:00:00 | 12:00:00 | null |
| url | https://en.wikipedia.org/wiki/2024_Abu_Dhabi_Grand_Prix | http://en.wikipedia.org/wiki/2016_Italian_Grand_Prix | http://en.wikipedia.org/wiki/1990_Australian_Grand_Prix |
| fp1_date | 2024-12-06 | null | null |
| fp1_time | 09:30:00 | null | null |
| fp2_date | 2024-12-06 | null | null |
| fp2_time | 13:00:00 | null | null |
| fp3_date | 2024-12-07 | null | null |
| fp3_time | 10:30:00 | null | null |
| quali_date | 2024-12-07 | null | null |
| quali_time | 14:00:00 | null | null |
| sprint_date | null | null | null |
| sprint_time | null | null | null |

# "races_ext"  (rows=1125)

columns:
"race_id" int: unique identifier, 1..1144
"year" int: 75 distinct, 1950..2024, avg=1992.7, median=1994
"round" int: 24 distinct, 1..24, avg=8.57956, median=8
"circuit_id" int: 77 distinct, 1..80
"name" text: 54 distinct
"date" numeric→text: all distinct
"time" numeric→text: 34 distinct, nulls=731
"url" text: all distinct
"fp1_date" text: iso-date, all distinct, nulls=1035
"fp1_time" text: 20 distinct, nulls=1057
"fp2_date" text: iso-date, all distinct, nulls=1035
"fp2_time" text: "15:00:00"=22, "13:00:00"=8, "06:00:00"=5, "10:30:00"=4, "14:00:00"=4, "21:00:00"=4, "17:00:00"=3, "21:30:00"=3, "22:00:00"=3, "05:00:00"=2, "14:30:00"=2, "07:30:00"=1, "08:00:00"=1, "09:30:00"=1, "15:30:00"=1, "17:30:00"=1, "18:00:00"=1, "18:30:00"=1, "20:30:00"=1, nulls=1057
"fp3_date" text: iso-date, all distinct, nulls=1053
"fp3_time" text: "10:30:00"=14, "11:00:00"=9, "09:30:00"=4, "02:30:00"=3, "16:30:00"=3, "17:00:00"=3, "01:30:00"=2, "03:00:00"=2, "10:00:00"=2, "13:30:00"=2, "17:30:00"=2, "04:30:00"=1, "08:30:00"=1, "11:30:00"=1, "12:00:00"=1, "12:30:00"=1, "14:00:00"=1, "19:00:00"=1, nulls=1072
"quali_date" text: iso-date, all distinct, nulls=1035
"quali_time" text: "14:00:00"=24, "13:00:00"=7, "20:00:00"=7, "15:00:00"=6, "06:00:00"=5, "17:00:00"=5, "21:00:00"=3, "05:00:00"=2, "18:00:00"=2, "22:00:00"=2, "07:00:00"=1, "08:00:00"=1, "12:00:00"=1, "16:00:00"=1, "19:00:00"=1, nulls=1057
"sprint_date" text: "2021-07-17"=1, "2021-09-11"=1, "2021-11-13"=1, "2022-04-23"=1, "2022-07-09"=1, "2022-11-12"=1, "2023-04-29"=1, "2023-07-01"=1, "2023-07-29"=1, "2023-10-07"=1, "2023-10-21"=1, "2023-11-04"=1, "2024-04-20"=1, "2024-05-04"=1, "2024-06-29"=1, "2024-10-19"=1, "2024-11-02"=1, "2024-11-30"=1, nulls=1107
"sprint_time" text: "14:30:00"=4, "03:00:00"=1, "10:00:00"=1, "13:00:00"=1, "13:30:00"=1, "14:00:00"=1, "16:00:00"=1, "17:30:00"=1, "18:00:00"=1, "18:30:00"=1, "19:30:00"=1, "22:00:00"=1, nulls=1110
"is_pit_data_available" int: 0=852, 1=273
"short_name" text: 52 distinct
"has_sprint" int: 0=1110, 1=15
"max_points" int: 9=490, 10=320, 25=177, 26=113, 34=12, 8=10, 29=3

indexes: none
fk: none

samples:
| column | latest | sample | sample |
|---|---|---|---|
| race_id | 1144 | 413 | 777 |
| year | 2024 | 1986 | 1957 |
| round | 24 | 10 | 2 |
| circuit_id | 24 | 10 | 6 |
| name | Abu Dhabi Grand Prix | German Grand Prix | Monaco Grand Prix |
| date | 2024-12-08 | 1986-07-27 | 1957-05-19 |
| time | 13:00:00 | null | null |
| url | https://en.wikipedia.org/wiki/2024_Abu_Dhabi_Grand_Prix | http://en.wikipedia.org/wiki/1986_German_Grand_Prix | http://en.wikipedia.org/wiki/1957_Monaco_Grand_Prix |
| fp1_date | 2024-12-06 | null | null |
| fp1_time | 09:30:00 | null | null |
| fp2_date | 2024-12-06 | null | null |
| fp2_time | 13:00:00 | null | null |
| fp3_date | 2024-12-07 | null | null |
| fp3_time | 10:30:00 | null | null |
| quali_date | 2024-12-07 | null | null |
| quali_time | 14:00:00 | null | null |
| sprint_date | null | null | null |
| sprint_time | null | null | null |
| is_pit_data_available | 0 | 0 | 0 |
| short_name | Abu Dhabi | Germany | Monaco |
| has_sprint | 0 | 0 | 0 |
| max_points | 26 | 9 | 9 |

# "results"  (rows=26519)

columns:
"result_id" int PK: unique identifier, 1..26524
"race_id" int NOTNULL: 1113 distinct, 1..1132
"driver_id" int NOTNULL: 859 distinct, 1..860
"constructor_id" int NOTNULL: 211 distinct, 1..215
"number" int: 129 distinct, nulls=6, 0..208, avg=18.0477, median=16
"grid" int NOTNULL: 35 distinct, 0..34, avg=11.1458, median=11
"position" int: 33 distinct, nulls=10928, 1..33, avg=7.99974, median=7
"position_text" varchar255 NOTNULL: 39 distinct
"position_order" int NOTNULL: 39 distinct, 1..39, avg=12.8148, median=12
"points" float NOTNULL: 39 distinct, 0..50, avg=1.95958, median=0
"laps" int NOTNULL: 172 distinct, 0..200, avg=46.2283, median=53
"time" varchar255: 7271 distinct, nulls=18986
"milliseconds" int: 7492 distinct, nulls=18986, 207071..15090540, avg=6.20872e+06, median=5.79688e+06
"fastest_lap" int: 80 distinct, nulls=18499, 1..85, avg=42.6167, median=46
"rank" int: 25 distinct, nulls=18249, 0..24, avg=10.3485, median=10
"fastest_lap_time" varchar255: 7297 distinct, nulls=18499
"fastest_lap_speed" varchar255: numeric, 7513 distinct, nulls=18499
"status_id" int NOTNULL: 137 distinct, 1..141

indexes: none
fk: none

samples:
| column | latest | sample | sample |
|---|---|---|---|
| result_id | 26524 | 16942 | 1256 |
| race_id | 1132 | 696 | 77 |
| driver_id | 842 | 328 | 2 |
| constructor_id | 214 | 66 | 3 |
| number | 10 | 28 | 8 |
| grid | 19 | 9 | 1 |
| position | null | null | 2 |
| position_text | W | R | 2 |
| position_order | 20 | 18 | 2 |
| points | 0 | 0 | 8 |
| laps | 0 | 5 | 59 |
| time | null | null | +16.567 |
| milliseconds | null | null | 5523215 |
| fastest_lap | null | null | 9 |
| rank | 0 | null | 4 |
| fastest_lap_time | null | null | 1:31.124 |
| fastest_lap_speed | null | null | 203.380 |
| status_id | 6 | 95 | 1 |

# "retirements"  (rows=11568)

columns:
"race_id" int: 1100 distinct, 1..1132
"driver_id" int: 790 distinct, 1..858
"lap" int: 153 distinct
"position_order" int: 38 distinct, 2..39, avg=19.2922, median=19
"status_id" int: 105 distinct, 2..141
"retirement_type" text: "Retirement (Mechanical Problem)"=8723, "Retirement (Driver Error)"=2700, "Retirement (Disqualification)"=145

indexes: none
fk: none

samples:
| column | latest | sample | sample |
|---|---|---|---|
| race_id | 1132 | 299 | 724 |
| driver_id | 847 | 129 | 435 |
| lap | 34 | 14 | 2 |
| position_order | 19 | 19 | 20 |
| status_id | 34 | 4 | 3 |
| retirement_type | Retirement (Mechanical Problem) | Retirement (Driver Error) | Retirement (Driver Error) |

# "seasons"  (rows=75)

columns:
"year" int PK: unique identifier, 1950..2024, avg=1987, median=1987
"url" varchar255 NOTNULL: all distinct

indexes: none
fk: none

samples:
| column | latest | sample | sample |
|---|---|---|---|
| year | 2024 | 1983 | 1980 |
| url | https://en.wikipedia.org/wiki/2024_Formula_One_World_Championship | http://en.wikipedia.org/wiki/1983_Formula_One_season | http://en.wikipedia.org/wiki/1980_Formula_One_season |

# "short_constructor_names"  (rows=44)

columns:
"constructor_ref" varchar255 PK: unique identifier
"short_name" varchar255 NOTNULL: "Cooper"=10, "Lotus"=8, "Brabham"=5, "McLaren"=4, "De Tomaso"=3, "Eagle"=2, "LDS"=2, "March"=2, "Shadow"=2, "Alpha Tauri"=1, "Alpine"=1, "BRM"=1, "Haas"=1, "Matra"=1, "Spkyer"=1

indexes: none
fk: none

samples:
| column | latest | sample | sample |
|---|---|---|---|
| constructor_ref | team_lotus | brabham-ford | lotus-borgward |
| short_name | Lotus | Brabham | Lotus |

# "short_grand_prix_names"  (rows=40)

columns:
"full_name" varchar255 PK: unique identifier
"short_name" varchar255 NOTNULL: 38 distinct

indexes: none
fk: none

samples:
| column | latest | sample | sample |
|---|---|---|---|
| full_name | United States Grand Prix | Malaysian Grand Prix | Styrian Grand Prix |
| short_name | United States | Malaysia | Styria |

# "sprint_results"  (rows=300)

columns:
"result_id" int PK: unique identifier, 1..300
"race_id" int NOTNULL: 1061=20, 1065=20, 1071=20, 1077=20, 1084=20, 1095=20, 1101=20, 1107=20, 1110=20, 1115=20, 1116=20, 1118=20, 1125=20, 1126=20, 1131=20, 1061..1131
"driver_id" int NOTNULL: 29 distinct, 1..859
"constructor_id" int NOTNULL: 1=30, 3=30, 6=30, 9=30, 117=30, 131=30, 210=30, 214=30, 51=24, 213=24, 15=6, 215=6, 1..215
"number" int: 30 distinct, 1..99, avg=27.5733, median=20
"grid" int NOTNULL: 21 distinct, 0..20, avg=10.1933, median=10
"position" int: 20 distinct, nulls=15, 1..20, avg=10.0421, median=10
"position_text" varchar255 NOTNULL: 23 distinct
"position_order" int NOTNULL: 20 distinct, 1..20, avg=10.5, median=10.5
"points" float NOTNULL: 0=195, 1=15, 2=15, 3=15, 4=12, 5=12, 6=12, 7=12, 8=12, 0..8
"laps" int NOTNULL: 24=79, 19=71, 17=38, 23=38, 21=20, 11=19, 18=19, 0=6, 2=3, 10=2, 16=2, 1=1, 8=1, 12=1, 0..24
"time" varchar255: all distinct, nulls=19
"milliseconds" int: all distinct, nulls=19, 1498433..2128165, avg=1.81086e+06, median=1.84778e+06
"fastest_lap" int: 23 distinct, nulls=9, 2..24, avg=9.5567, median=8
"fastest_lap_time" varchar255: 290 distinct, nulls=9
"fastest_lap_speed" varchar255: all NULL
"status_id" int NOTNULL: 1=281, 31=10, 3=3, 130=3, 10=1, 23=1, 76=1, 1..130

indexes: none
fk: none

samples:
| column | latest | sample | sample |
|---|---|---|---|
| result_id | 300 | 284 | 258 |
| race_id | 1131 | 1131 | 1125 |
| driver_id | 855 | 847 | 858 |
| constructor_id | 15 | 131 | 3 |
| number | 24 | 63 | 2 |
| grid | 19 | 4 | 20 |
| position | 20 | 4 | 18 |
| position_text | 20 | 4 | 18 |
| position_order | 20 | 4 | 18 |
| points | 0 | 5 | 0 |
| laps | 23 | 23 | 19 |
| time | +53.143 | +8.354 | +46.352 |
| milliseconds | 1654532 | 1609743 | 1971012 |
| fastest_lap | 6 | 4 | 7 |
| fastest_lap_time | 1:10.613 | 1:09.194 | 1:42.516 |
| fastest_lap_speed | null | null | null |
| status_id | 1 | 1 | 1 |

# "status"  (rows=139)

columns:
"status_id" int PK: unique identifier, 1..141
"status" varchar255 NOTNULL: all distinct

indexes: none
fk: none

samples:
| column | latest | sample | sample |
|---|---|---|---|
| status_id | 141 | 78 | 102 |
| status | Cooling system | Safety | CV joint |

# "tdr_overrides"  (rows=48)

columns:
"year" int PK: 2022=7, 2004=4, 2007=4, 2015=4, 2016=4, 2018=4, 2019=4, 2021=4, 2017=3, 2008=2, 2009=2, 2012=2, 2014=2, 2020=2, 2004..2022
"constructor_ref" varchar255 PK: "red_bull"=10, "ferrari"=8, "mclaren"=6, "renault"=5, "haas"=4, "mercedes"=4, "toyota"=4, "aston_martin"=3, "alphatauri"=2, "toro_rosso"=2
"driver_ref" varchar255 PK: 30 distinct, "ricciardo"=5, "vettel"=4, "hamilton"=3, "leclerc"=3, "alonso"=2, "grosjean"=2, "hulkenberg"=2, "kevin_magnussen"=2, "kvyat"=2, "max_verstappen"=2
"team_driver_rank" int: 2=22, 1=21, 3=4, 4=1, 1..4

indexes: none
fk: none

samples:
| column | latest | sample | sample |
|---|---|---|---|
| year | 2022 | 2015 | 2012 |
| constructor_ref | mercedes | red_bull | toro_rosso |
| driver_ref | russell | ricciardo | vergne |
| team_driver_rank | 2 | 1 | 2 |

# "team_driver_ranks"  (rows=3530)

columns:
"year" int: 75 distinct, 1950..2024, avg=1976.43, median=1973
"constructor_id" int: 210 distinct, 1..215
"constructor_ref" text: 210 distinct
"driver_id" int: 852 distinct, 1..860
"driver_ref" text: 852 distinct
"team_driver_rank" int: 29 distinct

indexes: none
fk: none

samples:
| column | latest | sample | sample |
|---|---|---|---|
| year | 2024 | 1974 | 1972 |
| constructor_id | 215 | 58 | 1 |
| constructor_ref | rb | shadow | mclaren |
| driver_id | 852 | 309 | 304 |
| driver_ref | tsunoda | revson | hulme |
| team_driver_rank | 1 | 4 | 1 |
