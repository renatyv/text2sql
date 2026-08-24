---
generator: db-snooper
version: 0.0.34
generated_at_utc: 2026-08-24T21:59:24.018860Z
dialect: sqlite
database: /var/folders/9j/b9bx_drd53sc6zbpsqyrjy4h0000gn/T/dbsnoop-485vvam2/f1.sqlite
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

samples:
| column | latest | sample | sample |
|---|---|---|---|
| circuit_id | 80 | 6 | 15 |
| circuit_ref | vegas | monaco | marina_bay |
| name | Las Vegas Strip Street Circuit | Circuit de Monaco | Marina Bay Street Circuit |
| location | Las Vegas | Monte-Carlo | Marina Bay |
| country | United States | Monaco | Singapore |
| lat | 36.1147 | 43.7347 | 1.2914 |
| lng | -115.173 | 7.42056 | 103.864 |
| alt | 642 | 7 | 18 |
| url | https://en.wikipedia.org/wiki/Las_Vegas_Grand_Prix#Circuit | http://en.wikipedia.org/wiki/Circuit_de_Monaco | http://en.wikipedia.org/wiki/Marina_Bay_Street_Circuit |

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

samples:
| column | latest | sample | sample |
|---|---|---|---|
| circuit_id | 80 | 29 | 40 |
| circuit_ref | vegas | adelaide | zolder |
| name | Las Vegas Strip Street Circuit | Adelaide Street Circuit | Zolder |
| location | Las Vegas | Adelaide | Heusden-Zolder |
| country | United States | Australia | Belgium |
| lat | 36.1147 | -34.9272 | 50.9894 |
| lng | -115.173 | 138.617 | 5.25694 |
| alt | 642 | 58 | 36 |
| url | https://en.wikipedia.org/wiki/Las_Vegas_Grand_Prix#Circuit | http://en.wikipedia.org/wiki/Adelaide_Street_Circuit | http://en.wikipedia.org/wiki/Zolder |
| last_race_year | 2024 | 1995 | 1984 |
| number_of_races | 2 | 11 | 10 |

# "constructor_results"  (rows=12505)

columns:
"constructor_results_id" int PK: unique identifier, 1..17009
"race_id" int NOTNULL: 1048 distinct, 1..1132
"constructor_id" int NOTNULL: 175 distinct, 1..215
"points" float: 60 distinct, 0..66, avg=3.98617, median=0
"status" varchar255: "D"=17, nulls=12488

indexes: none

samples:
| column | latest | sample | sample |
|---|---|---|---|
| constructor_results_id | 17009 | 4574 | 5272 |
| race_id | 1132 | 387 | 436 |
| constructor_id | 214 | 32 | 3 |
| points | 0 | 4 | 6 |
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

samples:
| column | latest | sample | sample |
|---|---|---|---|
| constructor_standings_id | 28852 | 27747 | 19336 |
| race_id | 1132 | 1057 | 740 |
| constructor_id | 214 | 213 | 6 |
| points | 9 | 39 | 24 |
| position | 8 | 5 | 1 |
| position_text | 8 | 5 | 1 |
| wins | 0 | 0 | 2 |

# "constructors"  (rows=212)

columns:
"constructor_id" int PK: unique identifier, 1..215
"constructor_ref" varchar255 NOTNULL: all distinct
"name" varchar255 NOTNULL: all distinct
"nationality" varchar255: 24 distinct
"url" varchar255 NOTNULL: 175 distinct

indexes: none

samples:
| column | latest | sample | sample |
|---|---|---|---|
| constructor_id | 215 | 153 | 99 |
| constructor_ref | rb | cisitalia | emeryson |
| name | RB F1 Team | Cisitalia | Emeryson |
| nationality | Italian | Italian | British |
| url | http://en.wikipedia.org/wiki/RB_Formula_One_Team | http://en.wikipedia.org/wiki/Cisitalia | http://en.wikipedia.org/wiki/Emeryson |

# "constructors_ext"  (rows=212)

columns:
"constructor_id" int: unique identifier, 1..215
"constructor_ref" text: all distinct
"name" text: all distinct
"nationality" text: 24 distinct
"url" text: 175 distinct
"short_name" text: 172 distinct

indexes: none

samples:
| column | latest | sample | sample |
|---|---|---|---|
| constructor_id | 215 | 72 | 203 |
| constructor_ref | rb | kojima | shadow-matra |
| name | RB F1 Team | Kojima | Shadow-Matra |
| nationality | Italian | Japanese | British |
| url | http://en.wikipedia.org/wiki/RB_Formula_One_Team | http://en.wikipedia.org/wiki/Kojima_Engineering | http://en.wikipedia.org/wiki/Shadow_Racing_Cars |
| short_name | RB F1 Team | Kojima | Shadow |

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

samples:
| column | latest | sample | sample |
|---|---|---|---|
| driver_standings_id | 72871 | 67819 | 71203 |
| race_id | 1132 | 958 | 88 |
| driver_id | 860 | 821 | 31 |
| points | 6 | 0 | 60 |
| position | 14 | 19 | 4 |
| position_text | 14 | 19 | 4 |
| wins | 0 | 0 | 3 |

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

samples:
| column | latest | sample | sample |
|---|---|---|---|
| driver_standings_id | 72871 | 58681 | 22611 |
| race_id | 1132 | 519 | 481 |
| driver_id | 860 | 202 | 90 |
| points | 6 | 8 | 0 |
| position | 14 | 10 | 40 |
| position_text | 14 | 10 | 40 |
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

samples:
| column | latest | sample | sample |
|---|---|---|---|
| driver_id | 860 | 486 | 193 |
| driver_ref | bearman | fairman | sullivan |
| number | 38 | null | null |
| code | BEA | null | null |
| forename | Oliver | Jack | Danny |
| surname | Bearman | Fairman | Sullivan |
| full_name | Oliver Bearman | Jack Fairman | Danny Sullivan |
| dob | 2005-05-08 | 1913-03-15 | 1950-03-09 |
| nationality | British | British | American |
| url | http://en.wikipedia.org/wiki/Oliver_Bearman | http://en.wikipedia.org/wiki/Jack_Fairman | http://en.wikipedia.org/wiki/Danny_Sullivan |

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

samples:
| column | latest | sample | sample |
|---|---|---|---|
| driver_id | 860 | 599 | 674 |
| driver_ref | bearman | bisch | crockett |
| number | 38 | null | null |
| code | BEA | BIS | CRO |
| forename | Oliver | Art | Larry |
| surname | Bearman | Bisch | Crockett |
| full_name | Oliver Bearman | Art Bisch | Larry Crockett |
| dob | 2005-05-08 | 1926-11-10 | 1926-10-23 |
| nationality | British | American | American |
| url | http://en.wikipedia.org/wiki/Oliver_Bearman | http://en.wikipedia.org/wiki/Art_Bisch | http://en.wikipedia.org/wiki/Larry_Crockett |

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

samples:
| column | latest | sample | sample |
|---|---|---|---|
| year | 2024 | 1961 | 1989 |
| driver_id | 860 | 444 | 148 |
| drive_id | 1 | 1 | 1 |
| constructor_id | 6 | 174 | 44 |
| first_round | 2 | 7 | 1 |
| last_round | 2 | 7 | 11 |
| is_first_drive_of_season | 1 | 1 | 1 |
| is_final_drive_of_season | 1 | 1 | 0 |

# "lap_positions"  (rows=≈613112)

columns:
"race_id" int
"driver_id" int
"lap" int
"position" int
"lap_type" null

indexes: none


# "lap_time_stats"  (rows=10789)

columns:
"race_id" int: 531 distinct, 1..1131
"driver_id" int: 141 distinct, 1..860
"avg_milliseconds" float: 10784 distinct
"avg_seconds" float: 10788 distinct
"stdev_milliseconds" float: 10676 distinct
"stdev_seconds" float: 10676 distinct

indexes: none

samples:
| column | latest | sample | sample |
|---|---|---|---|
| race_id | 1131 | 860 | 116 |
| driver_id | 858 | 808 | 49 |
| avg_milliseconds | 73465.3 | 96438.6 | 97459.9 |
| avg_seconds | 73.4653 | 96.4386 | 97.4599 |
| stdev_milliseconds | 4993.76 | 5235.95 | 5005.7 |
| stdev_seconds | 4.99376 | 5.23595 | 5.0057 |

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


# "liveries"  (rows=64)

columns:
"constructor_ref" varchar255 PK: 37 distinct, "renault"=6, "sauber"=5, "williams"=5, "jordan"=4, "mclaren"=4, "benneton"=3, "hrt"=3, "caterham"=2, "force_india"=2, "haas"=2
"start_year" int PK: 32 distinct, 1950..2021, avg=2004.72, median=2007, 2006=6, 2010=6, 1997=4, 2012=4, 2016=3, 2017=3, 2021=3, 1985=2, 1991=2, 1992=2
"end_year" int PK: 28 distinct, nulls=10, 1985..2020, avg=2007.46, median=2009, 2005=4, 2009=4, 2011=4, 2016=4, 2006=3, 2020=3, 1991=2, 1996=2, 2001=2, 2008=2
"primary_hex_code" varchar255 NOTNULL: 52 distinct

indexes: none

samples:
| column | latest | sample | sample |
|---|---|---|---|
| constructor_ref | williams | brawn | renault |
| start_year | 2014 | 2009 | 2011 |
| end_year | null | 2009 | 2011 |
| primary_hex_code | #005AFF | #A0E601 | #C1A43E |

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

samples:
| column | latest | sample | sample |
|---|---|---|---|
| race_id | 1132 | 918 | 881 |
| driver_id | 858 | 3 | 16 |
| stop | 2 | 2 | 1 |
| lap | 38 | 34 | 6 |
| time | 16:05:23 | 18:05:35 | 16:15:54 |
| duration | 29.444 | 24.083 | 37.833 |
| milliseconds | 29444 | 24083 | 37833 |
| seconds | 29.444 | 24.083 | 37.833 |

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

samples:
| column | latest | sample | sample |
|---|---|---|---|
| qualify_id | 10311 | 3407 | 1987 |
| race_id | 1132 | 340 | 215 |
| driver_id | 842 | 16 | 57 |
| constructor_id | 214 | 10 | 1 |
| number | 10 | 14 | 9 |
| position | 20 | 10 | 3 |
| q1 | 1:39.804 | 1:36.671 | 1:21.797 |
| q2 | null | 1:35.665 | null |
| q3 | null | 1:35.963 | null |

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

samples:
| column | latest | sample | sample |
|---|---|---|---|
| race_id | 1144 | 524 | 813 |
| year | 2024 | 1979 | 1953 |
| round | 24 | 13 | 6 |
| circuit_id | 24 | 14 | 9 |
| name | Abu Dhabi Grand Prix | Italian Grand Prix | British Grand Prix |
| date | 2024-12-08 | 1979-09-09 | 1953-07-18 |
| time | 13:00:00 | null | null |
| url | https://en.wikipedia.org/wiki/2024_Abu_Dhabi_Grand_Prix | http://en.wikipedia.org/wiki/1979_Italian_Grand_Prix | http://en.wikipedia.org/wiki/1953_British_Grand_Prix |
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

samples:
| column | latest | sample | sample |
|---|---|---|---|
| race_id | 1144 | 892 | 521 |
| year | 2024 | 2013 | 1979 |
| round | 24 | 12 | 10 |
| circuit_id | 24 | 14 | 10 |
| name | Abu Dhabi Grand Prix | Italian Grand Prix | German Grand Prix |
| date | 2024-12-08 | 2013-09-08 | 1979-07-29 |
| time | 13:00:00 | 12:00:00 | null |
| url | https://en.wikipedia.org/wiki/2024_Abu_Dhabi_Grand_Prix | http://en.wikipedia.org/wiki/2013_Italian_Grand_Prix | http://en.wikipedia.org/wiki/1979_German_Grand_Prix |
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
| is_pit_data_available | 0 | 1 | 0 |
| short_name | Abu Dhabi | Italy | Germany |
| has_sprint | 0 | 0 | 0 |
| max_points | 26 | 25 | 9 |

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
"milliseconds" int: 7492 distinct, nulls=18986, 207071..15090540, avg=6.2e+06, median=5.8e+06
"fastest_lap" int: 80 distinct, nulls=18499, 1..85, avg=42.6167, median=46
"rank" int: 25 distinct, nulls=18249, 0..24, avg=10.3485, median=10
"fastest_lap_time" varchar255: 7297 distinct, nulls=18499
"fastest_lap_speed" varchar255: numeric, 7513 distinct, nulls=18499
"status_id" int NOTNULL: 137 distinct, 1..141

indexes: none

samples:
| column | latest | sample | sample |
|---|---|---|---|
| result_id | 26524 | 20166 | 14446 |
| race_id | 1132 | 839 | 587 |
| driver_id | 842 | 647 | 200 |
| constructor_id | 214 | 6 | 1 |
| number | 10 | 16 | 2 |
| grid | 19 | 2 | 9 |
| position | null | null | 4 |
| position_text | W | R | 4 |
| position_order | 20 | 17 | 4 |
| points | 0 | 0 | 1.5 |
| laps | 0 | 21 | 29 |
| time | null | null | +1:12.66 |
| milliseconds | null | null | 3549350 |
| fastest_lap | null | null | null |
| rank | 0 | null | null |
| fastest_lap_time | null | null | null |
| fastest_lap_speed | null | null | null |
| status_id | 6 | 5 | 1 |

# "retirements"  (rows=11568)

columns:
"race_id" int: 1100 distinct, 1..1132
"driver_id" int: 790 distinct, 1..858
"lap" int: 153 distinct
"position_order" int: 38 distinct, 2..39, avg=19.2922, median=19
"status_id" int: 105 distinct, 2..141
"retirement_type" text: "Retirement (Mechanical Problem)"=8723, "Retirement (Driver Error)"=2700, "Retirement (Disqualification)"=145

indexes: none

samples:
| column | latest | sample | sample |
|---|---|---|---|
| race_id | 1132 | 647 | 389 |
| driver_id | 847 | 364 | 138 |
| lap | 34 | 3 | 58 |
| position_order | 19 | 19 | 6 |
| status_id | 34 | 5 | 60 |
| retirement_type | Retirement (Mechanical Problem) | Retirement (Mechanical Problem) | Retirement (Mechanical Problem) |

# "seasons"  (rows=75)

columns:
"year" int PK: unique identifier, 1950..2024, avg=1987, median=1987
"url" varchar255 NOTNULL: all distinct

indexes: none

samples:
| column | latest | sample | sample |
|---|---|---|---|
| year | 2024 | 2004 | 2015 |
| url | https://en.wikipedia.org/wiki/2024_Formula_One_World_Championship | http://en.wikipedia.org/wiki/2004_Formula_One_season | http://en.wikipedia.org/wiki/2015_Formula_One_season |

# "short_constructor_names"  (rows=44)

columns:
"constructor_ref" varchar255 PK: unique identifier
"short_name" varchar255 NOTNULL: "Cooper"=10, "Lotus"=8, "Brabham"=5, "McLaren"=4, "De Tomaso"=3, "Eagle"=2, "LDS"=2, "March"=2, "Shadow"=2, "Alpha Tauri"=1, "Alpine"=1, "BRM"=1, "Haas"=1, "Matra"=1, "Spkyer"=1

indexes: none

samples:
| column | latest | sample | sample |
|---|---|---|---|
| constructor_ref | team_lotus | lotus-pw | alphatauri |
| short_name | Lotus | Lotus | Alpha Tauri |

# "short_grand_prix_names"  (rows=40)

columns:
"full_name" varchar255 PK: unique identifier
"short_name" varchar255 NOTNULL: 38 distinct

indexes: none

samples:
| column | latest | sample | sample |
|---|---|---|---|
| full_name | United States Grand Prix | Belgian Grand Prix | Austrian Grand Prix |
| short_name | United States | Belgium | Austria |

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
"milliseconds" int: all distinct, nulls=19, 1498433..2128165, avg=1.8e+06, median=1.8e+06
"fastest_lap" int: 23 distinct, nulls=9, 2..24, avg=9.5567, median=8
"fastest_lap_time" varchar255: 290 distinct, nulls=9
"fastest_lap_speed" varchar255: all NULL
"status_id" int NOTNULL: 1=281, 31=10, 3=3, 130=3, 10=1, 23=1, 76=1, 1..130

indexes: none

samples:
| column | latest | sample | sample |
|---|---|---|---|
| result_id | 300 | 123 | 210 |
| race_id | 1131 | 1101 | 1116 |
| driver_id | 855 | 830 | 857 |
| constructor_id | 15 | 9 | 1 |
| number | 24 | 1 | 81 |
| grid | 19 | 3 | 5 |
| position | 20 | 3 | 10 |
| position_text | 20 | 3 | 10 |
| position_order | 20 | 3 | 10 |
| points | 0 | 6 | 0 |
| laps | 23 | 17 | 19 |
| time | +53.143 | +5.065 | +42.403 |
| milliseconds | 1654532 | 2002732 | 1933252 |
| fastest_lap | 6 | 10 | 16 |
| fastest_lap_time | 1:10.613 | 1:43.723 | 1:41.037 |
| fastest_lap_speed | null | null | null |
| status_id | 1 | 1 | 1 |

# "status"  (rows=139)

columns:
"status_id" int PK: unique identifier, 1..141
"status" varchar255 NOTNULL: all distinct

indexes: none

samples:
| column | latest | sample | sample |
|---|---|---|---|
| status_id | 141 | 11 | 98 |
| status | Cooling system | +1 Lap | Injection |

# "tdr_overrides"  (rows=48)

columns:
"year" int PK: 2022=7, 2004=4, 2007=4, 2015=4, 2016=4, 2018=4, 2019=4, 2021=4, 2017=3, 2008=2, 2009=2, 2012=2, 2014=2, 2020=2, 2004..2022
"constructor_ref" varchar255 PK: "red_bull"=10, "ferrari"=8, "mclaren"=6, "renault"=5, "haas"=4, "mercedes"=4, "toyota"=4, "aston_martin"=3, "alphatauri"=2, "toro_rosso"=2
"driver_ref" varchar255 PK: 30 distinct, "ricciardo"=5, "vettel"=4, "hamilton"=3, "leclerc"=3, "alonso"=2, "grosjean"=2, "hulkenberg"=2, "kevin_magnussen"=2, "kvyat"=2, "max_verstappen"=2
"team_driver_rank" int: 2=22, 1=21, 3=4, 4=1, 1..4

indexes: none

samples:
| column | latest | sample | sample |
|---|---|---|---|
| year | 2022 | 2022 | 2007 |
| constructor_ref | mercedes | aston_martin | renault |
| driver_ref | russell | vettel | kovalainen |
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

samples:
| column | latest | sample | sample |
|---|---|---|---|
| year | 2024 | 1991 | 1974 |
| constructor_id | 215 | 39 | 79 |
| constructor_ref | rb | ags | token |
| driver_id | 852 | 120 | 252 |
| driver_ref | tsunoda | barbazza | pryce |
| team_driver_rank | 1 | 4 | 1 |
