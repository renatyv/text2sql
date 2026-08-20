---
generator: db-snooper
version: 0.0.31
generated_at_utc: 2026-08-20T17:27:02.860709Z
dialect: sqlite
database: /var/folders/9j/b9bx_drd53sc6zbpsqyrjy4h0000gn/T/dbsnoop-54jdwhum/EU_soccer.sqlite
schema: main
---

## Relationships

- "League"."id" ← "Match"."league_id"
- "Player"."player_api_id" ← "Match"."away_player_1", "Match"."away_player_10", "Match"."away_player_11", "Match"."away_player_2", "Match"."away_player_3", "Match"."away_player_4", "Match"."away_player_5", "Match"."away_player_6", "Match"."away_player_7", "Match"."away_player_8", "Match"."away_player_9", "Match"."home_player_1", "Match"."home_player_10", "Match"."home_player_11", "Match"."home_player_2", "Match"."home_player_3", "Match"."home_player_4", "Match"."home_player_5", "Match"."home_player_6", "Match"."home_player_7", "Match"."home_player_8", "Match"."home_player_9", "Player_Attributes"."player_api_id"
- "Player"."player_fifa_api_id" ← "Player_Attributes"."player_fifa_api_id"
- "Team"."team_api_id" ← "Match"."away_team_api_id", "Match"."home_team_api_id", "Team_Attributes"."team_api_id"
- "Team"."team_fifa_api_id" ← "Team_Attributes"."team_fifa_api_id"
- "country"."id" ← "League"."country_id", "Match"."country_id"

# "Country"  (rows=11)

columns:
"id" int PK: unique identifier, 1..24558
"name" text UNIQ: unique identifier

indexes: none
fk: none

samples:
| column | latest | sample | sample |
|---|---|---|---|
| id | 24558 | 13274 | 4769 |
| name | Switzerland | Netherlands | France |

# "League"  (rows=11)

columns:
"id" int PK: unique identifier, 1..24558
"country_id" int FK: unique identifier, 1..24558
"name" text UNIQ: unique identifier

indexes: none
fk: "country_id"→"country"."id"

samples:
| column | latest | sample | sample |
|---|---|---|---|
| id | 24558 | 21518 | 17642 |
| country_id | 24558 | 21518 | 17642 |
| name | Switzerland Super League | Spain LIGA BBVA | Portugal Liga ZON Sagres |

# "Match"  (rows=25979)

columns:
"id" int PK: unique identifier, 1..25979
"country_id" int FK: 1729=3040, 4769=3040, 21518=3040, 10257=3017, 7809=2448, 13274=2448, 17642=2052, 15722=1920, 19694=1824, 1=1728, 24558=1422, 1..24558
"league_id" int FK: 1729=3040, 4769=3040, 21518=3040, 10257=3017, 7809=2448, 13274=2448, 17642=2052, 15722=1920, 19694=1824, 1=1728, 24558=1422, 1..24558
"season" text: "2008/2009"=3326, "2015/2016"=3326, "2014/2015"=3325, "2010/2011"=3260, "2012/2013"=3260, "2009/2010"=3230, "2011/2012"=3220, "2013/2014"=3032
"stage" int: 38 distinct, 1..38, avg=18.2428, median=18
"date" text: iso-date, 1694 distinct
"match_api_id" int UNIQ: unique identifier, 483129..2216672
"home_team_api_id" int FK: 299 distinct, 1601..274581
"away_team_api_id" int FK: 299 distinct, 1601..274581
"home_team_goal" int: 1=8400, 2=6339, 0=5896, 3=3288, 4=1385, 5=457, 6=161, 7=38, 8=9, 9=4, 10=2, 0..10
"away_team_goal" int: 1=8989, 0=8687, 2=5146, 3=2145, 4=718, 5=215, 6=63, 7=10, 8=5, 9=1, 0..9
"home_player_X1" int: 1=24146, 0=11, 2=1, nulls=1821, 0..2
"home_player_X2" int: 2=22229, 3=1414, 1=258, 4=188, 6=31, 8=19, 0=11, 5=6, 7=2, nulls=1821, 0..8
"home_player_X3" int: 4=22575, 5=920, 6=274, 3=257, 8=70, 2=33, 7=17, 1=1, nulls=1832, 1..8
"home_player_X4" int: 6=21967, 7=1409, 8=313, 5=264, 2=93, 4=92, 3=9, nulls=1832, 2..8
"home_player_X5" int: 8=22056, 1=796, 2=690, 7=253, 6=175, 4=120, 5=27, 3=24, 9=6, nulls=1832, 1..9
"home_player_X6" int: 4=7549, 2=7245, 3=6034, 5=1960, 1=932, 9=255, 6=121, 7=37, 8=14, nulls=1832, 1..9
"home_player_X7" int: 4=8073, 6=7526, 5=5998, 3=1543, 2=796, 7=161, 8=41, 9=7, 1=2, nulls=1832, 1..9
"home_player_X8" int: 6=8069, 3=6302, 7=5991, 5=1603, 8=828, 4=747, 2=584, 9=17, 1=6, nulls=1832, 1..9
"home_player_X9" int: 8=7757, 5=7686, 3=4738, 7=1524, 4=826, 9=809, 6=756, 2=45, 1=6, nulls=1832, 1..9
"home_player_X10" int: 4=9696, 7=6357, 5=5522, 9=921, 6=874, 8=682, 3=76, 1=10, 2=9, nulls=1832, 1..9
"home_player_X11" int: 6=9796, 5=9571, 7=4654, 4=65, 3=59, 1=2, nulls=1832, 1..7
"away_player_X1" int: 1=24144, 2=2, 6=1, nulls=1832, 1..6
"away_player_X2" int: 2=22109, 3=1469, 1=329, 4=175, 6=28, 8=28, 5=7, 7=2, nulls=1832, 1..8
"away_player_X3" int: 4=22465, 5=967, 3=331, 6=271, 8=65, 2=34, 7=13, 9=1, nulls=1832, 2..9
"away_player_X4" int: 6=21856, 7=1468, 5=331, 8=325, 2=88, 4=69, 3=7, 1=3, nulls=1832, 1..8
"away_player_X5" int: 8=21915, 1=837, 2=695, 7=321, 6=175, 4=152, 3=21, 5=19, 9=12, nulls=1832, 1..9
"away_player_X6" int: 4=7564, 2=6865, 3=6038, 5=1978, 1=1214, 9=322, 6=117, 7=37, 8=12, nulls=1832, 1..9
"away_player_X7" int: 4=7637, 6=7530, 5=6022, 3=1868, 2=914, 7=137, 8=35, 1=3, 9=1, nulls=1832, 1..9
"away_player_X8" int: 6=7621, 3=6268, 7=6007, 5=1894, 4=905, 8=858, 2=574, 9=17, 1=3, nulls=1832, 1..9
"away_player_X9" int: 5=7525, 8=7350, 3=4749, 7=1823, 6=929, 4=879, 9=847, 2=39, 1=5, nulls=1833, 1..9
"away_player_X10" int: 4=9193, 7=6332, 5=5544, 9=1206, 6=921, 8=840, 3=97, 2=8, 1=5, nulls=1833, 1..9
"away_player_X11" int: 5=10043, 6=9322, 7=4664, 4=61, 3=49, 8=1, nulls=1839, 3..8
"home_player_Y1" int: 1=24146, 0=11, 3=1, nulls=1821, 0..3
"home_player_Y2" int: 3=24147, 0=11, nulls=1821
"home_player_Y3" int: 3=24146, 5=1, nulls=1832
"home_player_Y4" int: 3=24142, 5=5, nulls=1832
"home_player_Y5" int: 3=22691, 7=1403, 5=45, 6=7, 8=1, nulls=1832, 3..8
"home_player_Y6" int: 7=14027, 6=7967, 5=1793, 3=288, 8=69, 9=3, nulls=1832, 3..9
"home_player_Y7" int: 7=15634, 6=7016, 5=795, 8=694, 9=5, 3=3, nulls=1832, 3..9
"home_player_Y8" int: 7=15943, 8=7194, 6=519, 5=463, 9=21, 3=6, 10=1, nulls=1832, 3..10
"home_player_Y9" int: 7=10024, 8=8041, 10=4772, 9=1247, 6=62, 1=1, nulls=1832, 1..10
"home_player_Y10" int: 10=13568, 8=7083, 9=1516, 7=1188, 11=711, 6=80, 3=1, nulls=1832, 3..11
"home_player_Y11" int: 10=13567, 11=10577, 1=2, 3=1, nulls=1832, 1..11
"away_player_Y1" int: 1=24144, 3=3, nulls=1832
"away_player_Y2" int: 3=24147, nulls=1832
"away_player_Y3" int: 3=24146, 7=1, nulls=1832
"away_player_Y4" int: 3=24145, 5=1, 7=1, nulls=1832, 3..7
"away_player_Y5" int: 3=22645, 7=1448, 5=38, 6=15, 9=1, nulls=1832, 3..9
"away_player_Y6" int: 7=13954, 6=8054, 5=1715, 3=350, 8=70, 9=3, 10=1, nulls=1832, 3..10
"away_player_Y7" int: 7=15607, 6=7037, 8=772, 5=725, 3=3, 9=2, 10=1, nulls=1832, 3..10
"away_player_Y8" int: 7=15903, 8=7265, 6=541, 5=412, 9=22, 10=3, 3=1, nulls=1832, 3..10
"away_player_Y9" int: 7=10043, 8=8057, 10=4767, 9=1199, 6=78, 5=1, 11=1, nulls=1833, 5..11
"away_player_Y10" int: 10=13145, 8=7173, 7=1575, 9=1518, 11=655, 6=80, nulls=1833, 6..11
"away_player_Y11" int: 10=13145, 11=10993, 7=1, 8=1, nulls=1839, 7..11
"home_player_1" int FK: 906 distinct, nulls=1224, 2984..698273, avg=76638.4, median=38230
"home_player_2" int FK: 2414 distinct, nulls=1315, 2802..748432, avg=106854, median=42388
"home_player_3" int FK: 2375 distinct, nulls=1281, 2752..705484, avg=91601.3, median=39731
"home_player_4" int FK: 2606 distinct, nulls=1323, 2752..723037, avg=94540.2, median=41060
"home_player_5" int FK: 2769 distinct, nulls=1316, 2752..733787, avg=109528, median=45996
"home_player_6" int FK: 3798 distinct, nulls=1325, 2625..750584, avg=102309, median=41467
"home_player_7" int FK: 3422 distinct, nulls=1227, 2625..692984, avg=97287.6, median=41432
"home_player_8" int FK: 4076 distinct, nulls=1309, 2625..693171, avg=107291, median=43319
"home_player_9" int FK: 4114 distinct, nulls=1273, 2625..730065, avg=111132, median=45605
"home_player_10" int FK: 3642 distinct, nulls=1436, 2625..742405, avg=105613, median=43296
"home_player_11" int FK: 2890 distinct, nulls=1555, 2802..726956, avg=103414, median=42091
"away_player_1" int FK: 926 distinct, nulls=1234, 2796..698273, avg=76628.2, median=38289
"away_player_2" int FK: 2504 distinct, nulls=1278, 2790..748432, avg=107615, median=42388
"away_player_3" int FK: 2470 distinct, nulls=1293, 2752..705484, avg=91126.8, median=39892
"away_player_4" int FK: 2657 distinct, nulls=1321, 2752..728414, avg=95083.9, median=41083
"away_player_5" int FK: 2884 distinct, nulls=1335, 2790..746419, avg=109801, median=46212
"away_player_6" int FK: 3930 distinct, nulls=1313, 2625..722766, avg=102308, median=41634.5
"away_player_7" int FK: 3620 distinct, nulls=1235, 2625..750435, avg=97898.1, median=41433
"away_player_8" int FK: 4249 distinct, nulls=1341, 2625..717248, avg=109265, median=45816
"away_player_9" int FK: 4319 distinct, nulls=1328, 2625..722766, avg=111087, median=45860
"away_player_10" int FK: 3891 distinct, nulls=1441, 2770..722766, avg=107149, median=45358
"away_player_11" int FK: 3040 distinct, nulls=1554, 2802..726956, avg=104933, median=42652
"goal" text: 13225 distinct, nulls=11762
"shoton" text: 8464 distinct, nulls=11762
"shotoff" text: 8464 distinct, nulls=11762
"foulcommit" text: 8466 distinct, nulls=11762
"card" text: 13777 distinct, nulls=11762
"cross" text: 8466 distinct, nulls=11762
"corner" text: 8465 distinct, nulls=11762
"possession" text: 8420 distinct, nulls=11762
"B365H" numeric: 121 distinct, nulls=3387, 1.04..26, avg=2.62882, median=2.1
"B365D" numeric: 72 distinct, nulls=3387, 1.4..17, avg=3.83968, median=3.5
"B365A" numeric: 115 distinct, nulls=3387, 1.08..51, avg=4.66222, median=3.5
"BWH" numeric: 237 distinct, nulls=3404, 1.03..34, avg=2.55924, median=2.1
"BWD" numeric: 133 distinct, nulls=3404, 1.65..19.5, avg=3.7476, median=3.4
"BWA" numeric: 261 distinct, nulls=3404, 1.1..51, avg=4.39695, median=3.4
"IWH" numeric: 147 distinct, nulls=3459, 1.03..20, avg=2.46761, median=2.1
"IWD" numeric: 73 distinct, nulls=3459, 1.5..11, avg=3.60893, median=3.3
"IWA" numeric: 159 distinct, nulls=3459, 1.1..25, avg=4.15058, median=3.3
"LBH" numeric: 129 distinct, nulls=3423, 1.04..26, avg=2.5362, median=2.1
"LBD" numeric: 72 distinct, nulls=3423, 1.4..19, avg=3.71174, median=3.4
"LBA" numeric: 128 distinct, nulls=3423, 1.1..51, avg=4.38535, median=3.3
"PSH" numeric: 948 distinct, nulls=14811, 1.04..36, avg=2.81645, median=2.2
"PSD" numeric: 665 distinct, nulls=14811, 2.2..29, avg=4.13232, median=3.64
"PSA" numeric: 1475 distinct, nulls=14811, 1.09..47.5, avg=4.97274, median=3.61
"WHH" numeric: 125 distinct, nulls=3408, 1.02..26, avg=2.57874, median=2.15
"WHD" numeric: 78 distinct, nulls=3408, 1.02..17, avg=3.6653, median=3.3
"WHA" numeric: 136 distinct, nulls=3408, 1.08..51, avg=4.48259, median=3.4
"SJH" numeric: 137 distinct, nulls=8882, 1.04..23, avg=2.56606, median=2.1
"SJD" numeric: 79 distinct, nulls=8882, 1.4..15, avg=3.75588, median=3.4
"SJA" numeric: 132 distinct, nulls=8882, 1.1..41, avg=4.62234, median=3.5
"VCH" numeric: 160 distinct, nulls=3411, 1.03..36, avg=2.66811, median=2.15
"VCD" numeric: 82 distinct, nulls=3411, 1.62..26, avg=3.89905, median=3.5
"VCA" numeric: 151 distinct, nulls=3411, 1.08..67, avg=4.84028, median=3.5
"GBH" numeric: 159 distinct, nulls=11817, 1.05..21, avg=2.49876, median=2.1
"GBD" numeric: 84 distinct, nulls=11817, 1.45..11, avg=3.64819, median=3.3
"GBA" numeric: 172 distinct, nulls=11817, 1.12..34, avg=4.3531, median=3.4
"BSH" numeric: 101 distinct, nulls=11818, 1.04..17, avg=2.49789, median=2.1
"BSD" numeric: 59 distinct, nulls=11818, 1.33..13, avg=3.66074, median=3.4
"BSA" numeric: 96 distinct, nulls=11818, 1.12..34, avg=4.40566, median=3.4

indexes: none
fk: "away_player_8"→"Player"."player_api_id", "home_player_11"→"Player"."player_api_id", "home_player_3"→"Player"."player_api_id", "away_player_7"→"Player"."player_api_id", "home_player_10"→"Player"."player_api_id", "home_player_2"→"Player"."player_api_id", "away_player_6"→"Player"."player_api_id", "home_player_9"→"Player"."player_api_id", "home_player_1"→"Player"."player_api_id", "away_player_5"→"Player"."player_api_id", "home_player_8"→"Player"."player_api_id", "away_player_10"→"Player"."player_api_id", "away_player_4"→"Player"."player_api_id", "home_player_7"→"Player"."player_api_id", "away_team_api_id"→"Team"."team_api_id", "away_player_3"→"Player"."player_api_id", "home_player_6"→"Player"."player_api_id", "home_team_api_id"→"Team"."team_api_id", "away_player_11"→"Player"."player_api_id", "away_player_2"→"Player"."player_api_id", "home_player_5"→"Player"."player_api_id", "league_id"→"League"."id", "away_player_9"→"Player"."player_api_id", "away_player_1"→"Player"."player_api_id", "home_player_4"→"Player"."player_api_id", "country_id"→"country"."id"

samples:
| column | latest | sample | sample |
|---|---|---|---|
| id | 25979 | 10641 | 25127 |
| country_id | 24558 | 10257 | 24558 |
| league_id | 24558 | 10257 | 24558 |
| season | 2015/2016 | 2009/2010 | 2011/2012 |
| stage | 9 | 1 | 14 |
| date | 2015-09-23 00:00:00 | 2009-08-23 00:00:00 | 2011-10-30 00:00:00 |
| match_api_id | 1992095 | 704357 | 1026998 |
| home_team_api_id | 10192 | 9885 | 10243 |
| away_team_api_id | 9931 | 8533 | 10199 |
| home_team_goal | 4 | 1 | 1 |
| away_team_goal | 3 | 0 | 1 |
| home_player_X1 | 1 | 1 | 1 |
| home_player_X2 | 2 | 2 | 2 |
| home_player_X3 | 4 | 4 | 4 |
| home_player_X4 | 6 | 6 | 6 |
| home_player_X5 | 8 | 8 | 8 |
| home_player_X6 | 2 | 3 | 2 |
| home_player_X7 | 4 | 5 | 4 |
| home_player_X8 | 6 | 7 | 6 |
| home_player_X9 | 8 | 5 | 8 |
| home_player_X10 | 4 | 4 | 4 |
| home_player_X11 | 6 | 6 | 6 |
| away_player_X1 | 1 | 1 | 1 |
| away_player_X2 | 2 | 2 | 3 |
| away_player_X3 | 4 | 4 | 5 |
| away_player_X4 | 6 | 6 | 7 |
| away_player_X5 | 8 | 8 | 2 |
| away_player_X6 | 4 | 3 | 4 |
| away_player_X7 | 6 | 5 | 6 |
| away_player_X8 | 3 | 7 | 8 |
| away_player_X9 | 5 | 5 | 3 |
| away_player_X10 | 7 | 4 | 4 |
| away_player_X11 | 5 | 6 | 7 |
| home_player_Y1 | 1 | 1 | 1 |
| home_player_Y2 | 3 | 3 | 3 |
| home_player_Y3 | 3 | 3 | 3 |
| home_player_Y4 | 3 | 3 | 3 |
| home_player_Y5 | 3 | 3 | 3 |
| home_player_Y6 | 7 | 5 | 7 |
| home_player_Y7 | 7 | 5 | 7 |
| home_player_Y8 | 7 | 5 | 7 |
| home_player_Y9 | 7 | 8 | 7 |
| home_player_Y10 | 10 | 10 | 10 |
| home_player_Y11 | 10 | 10 | 10 |
| away_player_Y1 | 1 | 1 | 1 |
| away_player_Y2 | 3 | 3 | 3 |
| away_player_Y3 | 3 | 3 | 3 |
| away_player_Y4 | 3 | 3 | 3 |
| away_player_Y5 | 3 | 3 | 7 |
| away_player_Y6 | 6 | 5 | 7 |
| away_player_Y7 | 6 | 5 | 7 |
| away_player_Y8 | 8 | 5 | 7 |
| away_player_Y9 | 8 | 8 | 10 |
| away_player_Y10 | 8 | 10 | 10 |
| away_player_Y11 | 11 | 10 | 10 |
| home_player_1 | 274787 | 30717 | 25811 |
| home_player_2 | 492132 | 30861 | 115591 |
| home_player_3 | 108451 | 34520 | 171338 |
| home_player_4 | 25815 | 41884 | 25257 |
| home_player_5 | 94553 | 27287 | 181275 |
| home_player_6 | 384376 | 30871 | 39136 |
| home_player_7 | 598355 | 41890 | 198082 |
| home_player_8 | 36785 | 32937 | 25806 |
| home_player_9 | 45174 | 31235 | 132844 |
| home_player_10 | 302079 | 38827 | 31100 |
| home_player_11 | 71764 | 30712 | 25824 |
| away_player_1 | 156175 | 39477 | 42276 |
| away_player_2 | 95216 | 42008 | 25839 |
| away_player_3 | 172768 | 113762 | 178119 |
| away_player_4 | 22834 | 26315 | 166889 |
| away_player_5 | 458806 | 24443 | 42294 |
| away_player_6 | 207234 | 24436 | 113235 |
| away_player_7 | 25772 | 42651 | 42263 |
| away_player_8 | 40274 | 39286 | 25813 |
| away_player_9 | 34035 | 27731 | 114790 |
| away_player_10 | 41726 | 39638 | 36382 |
| away_player_11 | 527103 | 24448 | 25809 |
| goal | null | <goal><value><comment>n</comment><stats><goals>1</goals><shoton>1</shoton></stats><event_incident_typefk>406</event_incident_typefk><elapsed>11</elapsed><player2>31235</player2><subtype>header</subtype><player1>30712</player1><sortorder>3</sortorder><team>9885</team><id>735774</id><n>248</n><type>goal</type><goal_type>n</goal_type></value></goal> | null |
| shoton | null | <shoton><value><stats><shoton>1</shoton></stats><event_incident_typefk>148</event_incident_typefk><elapsed>26</elapsed><subtype>header</subtype><player1>30712</player1><sortorder>1</sortorder><team>9885</team><n>252</n><type>shoton</type><id>735845</id></value><value><stats><shoton>1</shoton></stats><event_incident_typefk>311</event_incident_typefk><elapsed>27</elapsed><subtype>deflected</subtype><player1>32937</player1><sortorder>0</sortorder><team>9885</team><n>236</n><type>shoton</type><id>735848</id></value><value><stats><blocked>1</blocked></stats><event_incident_typefk>62</event_incident_typefk><elapsed>40</elapsed><subtype>blocked_shot</subtype><sortorder>2</sortorder><team>9885</team><n>261</n><type>shoton</type><id>735943</id></value><value><stats><blocked>1</blocked></stats><event_incident_typefk>61</event_incident_typefk><elapsed>42</elapsed><subtype>blocked_shot</subtype><player1>41884</player1><sortorder>2</sortorder><team>9885</team><n>257</n><type>shoton</type><id>735953</id></value><value><stats><blocked>1</blocked></stats><elapsed_plus>1</elapsed_plus><event_incident_typefk>61</event_incident_typefk><elapsed>45</elapsed><subtype>blocked_shot</subtype><player1>42651</player1><sortorder>2</sortorder><team>8533</team><n>284</n><type>shoton</type><id>735995</id></value><value><stats><blocked>1</blocked></stats><event_incident_typefk>61</event_incident_typefk><elapsed>63</elapsed><subtype>blocked_shot</subtype><player1>27731</player1><sortorder>0</sortorder><team>8533</team><n>285</n><type>shoton</type><id>736175</id></value><value><event_incident_typefk>126</event_incident_typefk><elapsed>77</elapsed><subtype>direct_freekick</subtype><sortorder>0</sortorder><team>8533</team><n>185</n><type>shoton</type><id>736278</id></value></shoton> | null |
| shotoff | null | <shotoff><value><stats><shotoff>1</shotoff></stats><event_incident_typefk>46</event_incident_typefk><elapsed>8</elapsed><subtype>shot</subtype><player1>41884</player1><sortorder>1</sortorder><team>9885</team><n>227</n><type>shotoff</type><id>735757</id></value><value><stats><shotoff>1</shotoff></stats><event_incident_typefk>47</event_incident_typefk><elapsed>16</elapsed><subtype>header</subtype><player1>27731</player1><sortorder>0</sortorder><team>8533</team><n>237</n><type>shotoff</type><id>735790</id></value><value><stats><shotoff>1</shotoff></stats><event_incident_typefk>47</event_incident_typefk><elapsed>33</elapsed><subtype>header</subtype><player1>41884</player1><sortorder>2</sortorder><team>9885</team><n>283</n><type>shotoff</type><id>735901</id></value><value><stats><shotoff>1</shotoff></stats><event_incident_typefk>46</event_incident_typefk><elapsed>40</elapsed><subtype>shot</subtype><player1>31235</player1><sortorder>0</sortorder><team>9885</team><n>241</n><type>shotoff</type><id>735935</id></value><value><stats><shotoff>1</shotoff></stats><event_incident_typefk>47</event_incident_typefk><elapsed>43</elapsed><subtype>header</subtype><player1>41890</player1><sortorder>4</sortorder><team>9885</team><n>291</n><type>shotoff</type><id>735972</id></value><value><stats><shotoff>1</shotoff></stats><event_incident_typefk>113</event_incident_typefk><elapsed>58</elapsed><subtype>post</subtype><player1>38827</player1><sortorder>0</sortorder><team>9885</team><n>307</n><type>shotoff</type><id>736144</id></value><value><stats><shotoff>1</shotoff></stats><event_incident_typefk>9</event_incident_typefk><elapsed>67</elapsed><subtype>distance</subtype><player1>31235</player1><sortorder>3</sortorder><team>9885</team><n>322</n><type>shotoff</type><id>736208</id></value><value><stats><shotoff>1</shotoff></stats><event_incident_typefk>85</event_incident_typefk><elapsed>80</elapsed><subtype>distance</subtype><sortorder>0</sortorder><team>8533</team><n>300</n><type>shotoff</type><id>736305</id></value></shotoff> | null |
| foulcommit | null | <foulcommit><value><stats><foulscommitted>1</foulscommitted></stats><event_incident_typefk>42</event_incident_typefk><elapsed>5</elapsed><sortorder>0</sortorder><team>8533</team><n>217</n><type>foulcommit</type><id>735741</id></value><value><stats><foulscommitted>1</foulscommitted></stats><event_incident_typefk>43</event_incident_typefk><elapsed>5</elapsed><player1>27731</player1><sortorder>1</sortorder><team>8533</team><n>224</n><type>foulcommit</type><id>735747</id></value><value><stats><foulscommitted>1</foulscommitted></stats><event_incident_typefk>43</event_incident_typefk><elapsed>7</elapsed><player1>26315</player1><sortorder>0</sortorder><team>8533</team><n>218</n><type>foulcommit</type><id>735752</id></value><value><stats><foulscommitted>1</foulscommitted></stats><event_incident_typefk>42</event_incident_typefk><elapsed>9</elapsed><sortorder>0</sortorder><team>9885</team><n>230</n><type>foulcommit</type><id>735760</id></value><value><stats><foulscommitted>1</foulscommitted></stats><event_incident_typefk>5</event_incident_typefk><elapsed>11</elapsed><player2>31235</player2><subtype>serious_foul</subtype><player1>42651</player1><sortorder>1</sortorder><team>8533</team><n>223</n><type>foulcommit</type><id>735770</id></value><value><stats><foulscommitted>1</foulscommitted></stats><event_incident_typefk>42</event_incident_typefk><elapsed>18</elapsed><sortorder>0</sortorder><team>9885</team><n>247</n><type>foulcommit</type><id>735801</id></value><value><stats><foulscommitted>1</foulscommitted></stats><event_incident_typefk>43</event_incident_typefk><elapsed>19</elapsed><player1>30871</player1><sortorder>0</sortorder><team>9885</team><n>234</n><type>foulcommit</type><id>735806</id></value><value><stats><foulscommitted>1</foulscommitted></stats><event_incident_typefk>42</event_incident_typefk><elapsed>21</elapsed><sortorder>0</sortorder><team>8533</team><n>242</n><type>foulcommit</type><id>735815</id></value><value><stats><foulscommitted>1</foulscommitted></stats><event_incident_typefk>43</event_incident_typefk><elapsed>21</elapsed><player1>38827</player1><sortorder>1</sortorder><team>9885</team><n>228</n><type>foulcommit</type><id>735821</id></value><value><stats><foulscommitted>1</foulscommitted></stats><event_incident_typefk>37</event_incident_typefk><elapsed>22</elapsed><player2>27731</player2><player1>31235</player1><sortorder>0</sortorder><team>9885</team><n>263</n><type>foulcommit</type><id>735825</id></value><value><stats><foulscommitted>1</foulscommitted></stats><event_incident_typefk>43</event_incident_typefk><elapsed>24</elapsed><player1>24436</player1><sortorder>1</sortorder><team>8533</team><n>226</n><type>foulcommit</type><id>735835</id></value><value><stats><foulscommitted>1</foulscommitted></stats><event_incident_typefk>42</event_incident_typefk><elapsed>30</elapsed><sortorder>0</sortorder><team>9885</team><n>238</n><type>foulcommit</type><id>735875</id></value><value><stats><foulscommitted>1</foulscommitted></stats><event_incident_typefk>42</event_incident_typefk><elapsed>30</elapsed><sortorder>1</sortorder><team>8533</team><n>271</n><type>foulcommit</type><id>735878</id></value><value><stats><foulscommitted>1</foulscommitted></stats><event_incident_typefk>37</event_incident_typefk><elapsed>31</elapsed><player2>38827</player2><player1>42008</player1><sortorder>0</sortorder><team>8533</team><n>250</n><type>foulcommit</type><id>735886</id></value><value><stats><foulscommitted>1</foulscommitted></stats><event_incident_typefk>43</event_incident_typefk><elapsed>36</elapsed><player1>30712</player1><sortorder>0</sortorder><team>9885</team><n>235</n><type>foulcommit</type><id>735915</id></value><value><stats><foulscommitted>1</foulscommitted></stats><event_incident_typefk>37</event_incident_typefk><elapsed>48</elapsed><player2>41892</player2><player1>27731</player1><sortorder>2</sortorder><team>8533</team><n>286</n><type>foulcommit</type><id>736078</id></value><value><stats><foulscommitted>1</foulscommitted></stats><event_incident_typefk>37</event_incident_typefk><elapsed>54</elapsed><player2>31235</player2><player1>24436</player1><sortorder>0</sortorder><team>8533</team><n>276</n><type>foulcommit</type><id>736114</id></value><value><stats><foulscommitted>1</foulscommitted></stats><event_incident_typefk>3</event_incident_typefk><elapsed>54</elapsed><subtype>hands</subtype><player1>38827</player1><sortorder>2</sortorder><team>9885</team><n>282</n><type>foulcommit</type><id>736117</id></value><value><stats><foulscommitted>1</foulscommitted></stats><event_incident_typefk>43</event_incident_typefk><elapsed>55</elapsed><player1>32937</player1><sortorder>2</sortorder><team>9885</team><n>281</n><type>foulcommit</type><id>736128</id></value><value><stats><foulscommitted>1</foulscommitted></stats><event_incident_typefk>42</event_incident_typefk><elapsed>59</elapsed><sortorder>0</sortorder><team>9885</team><n>295</n><type>foulcommit</type><id>736149</id></value><value><stats><foulscommitted>1</foulscommitted></stats><event_incident_typefk>43</event_incident_typefk><elapsed>60</elapsed><player1>41890</player1><sortorder>0</sortorder><team>9885</team><n>317</n><type>foulcommit</type><id>736154</id></value><value><stats><foulscommitted>1</foulscommitted></stats><event_incident_typefk>43</event_incident_typefk><elapsed>61</elapsed><player1>41890</player1><sortorder>2</sortorder><team>9885</team><n>288</n><type>foulcommit</type><id>736164</id></value><value><stats><foulscommitted>1</foulscommitted></stats><event_incident_typefk>43</event_incident_typefk><elapsed>63</elapsed><player1>38827</player1><sortorder>1</sortorder><team>9885</team><n>268</n><type>foulcommit</type><id>736177</id></value><value><stats><foulscommitted>1</foulscommitted></stats><event_incident_typefk>42</event_incident_typefk><elapsed>64</elapsed><sortorder>0</sortorder><team>8533</team><n>318</n><type>foulcommit</type><id>736187</id></value><value><stats><foulscommitted>1</foulscommitted></stats><event_incident_typefk>43</event_incident_typefk><elapsed>64</elapsed><player1>34520</player1><sortorder>1</sortorder><team>9885</team><n>262</n><type>foulcommit</type><id>736188</id></value><value><stats><foulscommitted>1</foulscommitted></stats><event_incident_typefk>5</event_incident_typefk><elapsed>69</elapsed><player2>27731</player2><subtype>serious_foul</subtype><player1>34520</player1><sortorder>5</sortorder><team>9885</team><n>314</n><type>foulcommit</type><id>736231</id></value><value><stats><foulscommitted>1</foulscommitted></stats><event_incident_typefk>5</event_incident_typefk><elapsed>76</elapsed><player2>26315</player2><subtype>serious_foul</subtype><player1>182606</player1><sortorder>0</sortorder><team>9885</team><n>323</n><type>foulcommit</type><id>736270</id></value><value><stats><foulscommitted>1</foulscommitted></stats><event_incident_typefk>37</event_incident_typefk><elapsed>78</elapsed><player2>24436</player2><player1>41890</player1><sortorder>1</sortorder><team>9885</team><n>313</n><type>foulcommit</type><id>736290</id></value><value><stats><foulscommitted>1</foulscommitted></stats><event_incident_typefk>43</event_incident_typefk><elapsed>81</elapsed><player1>26315</player1><sortorder>2</sortorder><team>8533</team><n>336</n><type>foulcommit</type><id>736314</id></value><value><stats><foulscommitted>1</foulscommitted></stats><event_incident_typefk>43</event_incident_typefk><elapsed>88</elapsed><player1>113762</player1><sortorder>0</sortorder><team>8533</team><n>328</n><type>foulcommit</type><id>736358</id></value></foulcommit> | null |
| card | null | <card><value><comment>y</comment><stats><ycards>1</ycards></stats><event_incident_typefk>73</event_incident_typefk><elapsed>11</elapsed><card_type>y</card_type><subtype>serious_fouls</subtype><player1>42651</player1><sortorder>2</sortorder><team>8533</team><n>239</n><type>card</type><id>735771</id></value><value><comment>y</comment><stats><ycards>1</ycards></stats><event_incident_typefk>505</event_incident_typefk><elapsed>14</elapsed><card_type>y</card_type><subtype>Unsportsmanlike Cond</subtype><player1>27731</player1><sortorder>0</sortorder><team>8533</team><n>240</n><type>card</type><id>735785</id></value><value><comment>y</comment><stats><ycards>1</ycards></stats><event_incident_typefk>505</event_incident_typefk><elapsed>14</elapsed><card_type>y</card_type><subtype>Unsportsmanlike Cond</subtype><player1>32937</player1><sortorder>1</sortorder><team>9885</team><n>222</n><type>card</type><id>735786</id></value><value><comment>y</comment><stats><ycards>1</ycards></stats><event_incident_typefk>73</event_incident_typefk><elapsed>69</elapsed><card_type>y</card_type><subtype>serious_fouls</subtype><player1>34520</player1><sortorder>6</sortorder><team>9885</team><n>320</n><type>card</type><id>736232</id></value><value><comment>y</comment><stats><ycards>1</ycards></stats><event_incident_typefk>73</event_incident_typefk><elapsed>76</elapsed><card_type>y</card_type><subtype>serious_fouls</subtype><player1>182606</player1><sortorder>1</sortorder><team>9885</team><n>333</n><type>card</type><id>736272</id></value></card> | null |
| cross | null | <cross><value><stats><crosses>1</crosses></stats><event_incident_typefk>7</event_incident_typefk><elapsed>6</elapsed><subtype>cross</subtype><player1>38827</player1><sortorder>0</sortorder><team>9885</team><n>229</n><type>cross</type><id>735750</id></value><value><stats><crosses>1</crosses></stats><event_incident_typefk>7</event_incident_typefk><elapsed>8</elapsed><subtype>cross</subtype><player1>30861</player1><sortorder>0</sortorder><team>9885</team><n>219</n><type>cross</type><id>735756</id></value><value><stats><crosses>1</crosses></stats><event_incident_typefk>35</event_incident_typefk><elapsed>10</elapsed><subtype>cross</subtype><sortorder>0</sortorder><team>9885</team><n>220</n><type>cross</type><id>735766</id></value><value><stats><crosses>1</crosses></stats><event_incident_typefk>35</event_incident_typefk><elapsed>13</elapsed><subtype>cross</subtype><sortorder>0</sortorder><team>8533</team><n>225</n><type>cross</type><id>735781</id></value><value><stats><crosses>1</crosses></stats><event_incident_typefk>7</event_incident_typefk><elapsed>17</elapsed><subtype>cross</subtype><player1>24443</player1><sortorder>0</sortorder><team>8533</team><n>221</n><type>cross</type><id>735796</id></value><value><stats><crosses>1</crosses></stats><event_incident_typefk>35</event_incident_typefk><elapsed>25</elapsed><subtype>cross</subtype><sortorder>1</sortorder><team>8533</team><n>243</n><type>cross</type><id>735841</id></value><value><stats><crosses>1</crosses></stats><event_incident_typefk>7</event_incident_typefk><elapsed>26</elapsed><subtype>cross</subtype><player1>38827</player1><sortorder>0</sortorder><team>9885</team><n>270</n><type>cross</type><id>735844</id></value><value><stats><corners>1</corners></stats><event_incident_typefk>329</event_incident_typefk><elapsed>26</elapsed><subtype>cross</subtype><player1>30871</player1><sortorder>2</sortorder><team>9885</team><n>265</n><type>corner</type><id>735847</id></value><value><stats><corners>1</corners></stats><event_incident_typefk>329</event_incident_typefk><elapsed>27</elapsed><subtype>cross</subtype><player1>30871</player1><sortorder>1</sortorder><team>9885</team><n>232</n><type>corner</type><id>735853</id></value><value><stats><crosses>1</crosses></stats><event_incident_typefk>7</event_incident_typefk><elapsed>27</elapsed><subtype>cross</subtype><player1>39286</player1><sortorder>3</sortorder><team>8533</team><n>245</n><type>cross</type><id>735856</id></value><value><stats><corners>1</corners></stats><event_incident_typefk>329</event_incident_typefk><elapsed>28</elapsed><subtype>cross</subtype><player1>39286</player1><sortorder>1</sortorder><team>8533</team><n>231</n><type>corner</type><id>735862</id></value><value><stats><corners>1</corners></stats><event_incident_typefk>329</event_incident_typefk><elapsed>29</elapsed><subtype>cross</subtype><player1>41890</player1><sortorder>1</sortorder><team>9885</team><n>277</n><type>corner</type><id>735872</id></value><value><stats><crosses>1</crosses></stats><event_incident_typefk>7</event_incident_typefk><elapsed>32</elapsed><subtype>cross</subtype><player1>31235</player1><sortorder>3</sortorder><team>9885</team><n>255</n><type>cross</type><id>735894</id></value><value><stats><corners>1</corners></stats><event_incident_typefk>327</event_incident_typefk><elapsed>33</elapsed><subtype>cross</subtype><sortorder>1</sortorder><team>9885</team><n>253</n><type>corner</type><id>735899</id></value><value><stats><crosses>1</crosses></stats><event_incident_typefk>7</event_incident_typefk><elapsed>41</elapsed><subtype>cross</subtype><player1>38827</player1><sortorder>1</sortorder><team>9885</team><n>266</n><type>cross</type><id>735947</id></value><value><stats><corners>1</corners></stats><event_incident_typefk>329</event_incident_typefk><elapsed>42</elapsed><subtype>cross</subtype><player1>31235</player1><sortorder>0</sortorder><team>9885</team><n>246</n><type>corner</type><id>735951</id></value><value><stats><crosses>1</crosses></stats><event_incident_typefk>7</event_incident_typefk><elapsed>42</elapsed><subtype>cross</subtype><player1>30871</player1><sortorder>4</sortorder><team>9885</team><n>274</n><type>cross</type><id>735956</id></value><value><stats><corners>1</corners></stats><event_incident_typefk>329</event_incident_typefk><elapsed>43</elapsed><subtype>cross</subtype><player1>31235</player1><sortorder>1</sortorder><team>9885</team><n>260</n><type>corner</type><id>735964</id></value><value><stats><corners>1</corners></stats><event_incident_typefk>329</event_incident_typefk><elapsed>43</elapsed><subtype>cross</subtype><player1>31235</player1><sortorder>3</sortorder><team>9885</team><n>269</n><type>corner</type><id>735969</id></value><value><stats><crosses>1</crosses></stats><event_incident_typefk>7</event_incident_typefk><elapsed>44</elapsed><subtype>cross</subtype><player1>31235</player1><sortorder>0</sortorder><team>9885</team><n>272</n><type>cross</type><id>735976</id></value><value><stats><crosses>1</crosses></stats><elapsed_plus>1</elapsed_plus><event_incident_typefk>7</event_incident_typefk><elapsed>45</elapsed><subtype>cross</subtype><player1>113762</player1><sortorder>0</sortorder><team>8533</team><n>273</n><type>cross</type><id>735992</id></value><value><stats><crosses>1</crosses></stats><elapsed_plus>1</elapsed_plus><event_incident_typefk>7</event_incident_typefk><elapsed>45</elapsed><subtype>cross</subtype><player1>39286</player1><sortorder>1</sortorder><team>8533</team><n>251</n><type>cross</type><id>735994</id></value><value><stats><crosses>1</crosses></stats><elapsed_plus>1</elapsed_plus><event_incident_typefk>7</event_incident_typefk><elapsed>45</elapsed><subtype>cross</subtype><player1>42008</player1><sortorder>3</sortorder><team>8533</team><n>267</n><type>cross</type><id>735996</id></value><value><stats><crosses>1</crosses></stats><elapsed_plus>1</elapsed_plus><event_incident_typefk>7</event_incident_typefk><elapsed>45</elapsed><subtype>cross</subtype><player1>113762</player1><sortorder>4</sortorder><team>8533</team><n>275</n><type>cross</type><id>735997</id></value><value><stats><crosses>1</crosses></stats><elapsed_plus>2</elapsed_plus><event_incident_typefk>7</event_incident_typefk><elapsed>45</elapsed><subtype>cross</subtype><player1>38827</player1><sortorder>3</sortorder><team>9885</team><n>254</n><type>cross</type><id>736004</id></value><value><stats><crosses>1</crosses></stats><event_incident_typefk>35</event_incident_typefk><elapsed>48</elapsed><subtype>cross</subtype><sortorder>3</sortorder><team>9885</team><n>293</n><type>cross</type><id>736079</id></value><value><stats><crosses>1</crosses></stats><event_incident_typefk>7</event_incident_typefk><elapsed>50</elapsed><subtype>cross</subtype><player1>24436</player1><sortorder>0</sortorder><team>8533</team><n>278</n><type>cross</type><id>736088</id></value><value><stats><crosses>1</crosses></stats><event_incident_typefk>35</event_incident_typefk><elapsed>50</elapsed><subtype>cross</subtype><sortorder>2</sortorder><team>8533</team><n>309</n><type>cross</type><id>736096</id></value><value><stats><crosses>1</crosses></stats><event_incident_typefk>7</event_incident_typefk><elapsed>51</elapsed><subtype>cross</subtype><player1>24436</player1><sortorder>2</sortorder><team>8533</team><n>297</n><type>cross</type><id>736099</id></value><value><stats><crosses>1</crosses></stats><event_incident_typefk>7</event_incident_typefk><elapsed>51</elapsed><subtype>cross</subtype><player1>27731</player1><sortorder>3</sortorder><team>8533</team><n>296</n><type>cross</type><id>736100</id></value><value><stats><crosses>1</crosses></stats><event_incident_typefk>7</event_incident_typefk><elapsed>51</elapsed><subtype>cross</subtype><player1>24443</player1><sortorder>5</sortorder><team>8533</team><n>249</n><type>cross</type><id>736105</id></value><value><stats><crosses>1</crosses></stats><event_incident_typefk>7</event_incident_typefk><elapsed>52</elapsed><subtype>cross</subtype><player1>26315</player1><sortorder>0</sortorder><team>8533</team><n>259</n><type>cross</type><id>736107</id></value><value><stats><crosses>1</crosses></stats><event_incident_typefk>35</event_incident_typefk><elapsed>54</elapsed><subtype>cross</subtype><sortorder>1</sortorder><team>9885</team><n>290</n><type>cross</type><id>736115</id></value><value><stats><crosses>1</crosses></stats><event_incident_typefk>7</event_incident_typefk><elapsed>55</elapsed><subtype>cross</subtype><player1>41892</player1><sortorder>0</sortorder><team>9885</team><n>298</n><type>cross</type><id>736124</id></value><value><stats><crosses>1</crosses></stats><event_incident_typefk>7</event_incident_typefk><elapsed>56</elapsed><subtype>cross</subtype><player1>24448</player1><sortorder>0</sortorder><team>8533</team><n>302</n><type>cross</type><id>736129</id></value><value><stats><crosses>1</crosses></stats><event_incident_typefk>7</event_incident_typefk><elapsed>57</elapsed><subtype>cross</subtype><player1>39286</player1><sortorder>1</sortorder><team>8533</team><n>292</n><type>cross</type><id>736138</id></value><value><stats><crosses>1</crosses></stats><event_incident_typefk>7</event_incident_typefk><elapsed>60</elapsed><subtype>cross</subtype><player1>24448</player1><sortorder>1</sortorder><team>8533</team><n>305</n><type>cross</type><id>736155</id></value><value><stats><crosses>1</crosses></stats><event_incident_typefk>7</event_incident_typefk><elapsed>61</elapsed><subtype>cross</subtype><player1>41892</player1><sortorder>0</sortorder><team>9885</team><n>301</n><type>cross</type><id>736159</id></value><value><stats><crosses>1</crosses></stats><event_incident_typefk>7</event_incident_typefk><elapsed>62</elapsed><subtype>cross</subtype><player1>24436</player1><sortorder>1</sortorder><team>8533</team><n>303</n><type>cross</type><id>736172</id></value><value><stats><crosses>1</crosses></stats><event_incident_typefk>7</event_incident_typefk><elapsed>63</elapsed><subtype>cross</subtype><player1>24443</player1><sortorder>2</sortorder><team>8533</team><n>315</n><type>cross</type><id>736180</id></value><value><stats><crosses>1</crosses></stats><event_incident_typefk>7</event_incident_typefk><elapsed>65</elapsed><subtype>cross</subtype><player1>30712</player1><sortorder>0</sortorder><team>9885</team><n>310</n><type>cross</type><id>736192</id></value><value><stats><corners>1</corners></stats><event_incident_typefk>329</event_incident_typefk><elapsed>66</elapsed><subtype>cross</subtype><player1>31235</player1><sortorder>1</sortorder><team>9885</team><n>326</n><type>corner</type><id>736197</id></value><value><stats><crosses>1</crosses></stats><event_incident_typefk>7</event_incident_typefk><elapsed>66</elapsed><subtype>cross</subtype><player1>30861</player1><sortorder>2</sortorder><team>9885</team><n>280</n><type>cross</type><id>736198</id></value><value><stats><crosses>1</crosses></stats><event_incident_typefk>7</event_incident_typefk><elapsed>67</elapsed><subtype>cross</subtype><player1>32937</player1><sortorder>1</sortorder><team>9885</team><n>306</n><type>cross</type><id>736205</id></value><value><stats><crosses>1</crosses></stats><event_incident_typefk>7</event_incident_typefk><elapsed>69</elapsed><subtype>cross</subtype><player1>41892</player1><sortorder>0</sortorder><team>9885</team><n>312</n><type>cross</type><id>736222</id></value><value><stats><crosses>1</crosses></stats><event_incident_typefk>7</event_incident_typefk><elapsed>69</elapsed><subtype>cross</subtype><player1>30871</player1><sortorder>2</sortorder><team>9885</team><n>332</n><type>cross</type><id>736224</id></value><value><stats><crosses>1</crosses></stats><event_incident_typefk>7</event_incident_typefk><elapsed>72</elapsed><subtype>cross</subtype><player1>24443</player1><sortorder>1</sortorder><team>8533</team><n>308</n><type>cross</type><id>736241</id></value><value><stats><crosses>1</crosses></stats><event_incident_typefk>7</event_incident_typefk><elapsed>73</elapsed><subtype>cross</subtype><player1>26315</player1><sortorder>0</sortorder><team>8533</team><n>316</n><type>cross</type><id>736246</id></value><value><stats><crosses>1</crosses></stats><event_incident_typefk>7</event_incident_typefk><elapsed>73</elapsed><subtype>cross</subtype><player1>30871</player1><sortorder>2</sortorder><team>9885</team><n>331</n><type>cross</type><id>736250</id></value><value><stats><crosses>1</crosses></stats><event_incident_typefk>7</event_incident_typefk><elapsed>73</elapsed><subtype>cross</subtype><player1>38827</player1><sortorder>3</sortorder><team>9885</team><n>304</n><type>cross</type><id>736252</id></value><value><stats><crosses>1</crosses></stats><event_incident_typefk>7</event_incident_typefk><elapsed>74</elapsed><subtype>cross</subtype><player1>24436</player1><sortorder>1</sortorder><team>8533</team><n>311</n><type>cross</type><id>736260</id></value><value><stats><crosses>1</crosses></stats><event_incident_typefk>7</event_incident_typefk><elapsed>75</elapsed><subtype>cross</subtype><player1>31235</player1><sortorder>0</sortorder><team>9885</team><n>319</n><type>cross</type><id>736266</id></value><value><stats><crosses>1</crosses></stats><event_incident_typefk>7</event_incident_typefk><elapsed>78</elapsed><subtype>cross</subtype><player1>31235</player1><sortorder>0</sortorder><team>9885</team><n>321</n><type>cross</type><id>736288</id></value><value><stats><crosses>1</crosses></stats><event_incident_typefk>7</event_incident_typefk><elapsed>89</elapsed><subtype>cross</subtype><player1>42008</player1><sortorder>0</sortorder><team>8533</team><n>289</n><type>cross</type><id>736362</id></value><value><stats><crosses>1</crosses></stats><event_incident_typefk>7</event_incident_typefk><elapsed>90</elapsed><subtype>cross</subtype><player1>24443</player1><sortorder>0</sortorder><team>8533</team><n>329</n><type>cross</type><id>736370</id></value><value><stats><crosses>1</crosses></stats><event_incident_typefk>7</event_incident_typefk><elapsed>90</elapsed><subtype>cross</subtype><player1>24436</player1><sortorder>2</sortorder><team>8533</team><n>330</n><type>cross</type><id>736373</id></value><value><stats><crosses>1</crosses></stats><elapsed_plus>1</elapsed_plus><event_incident_typefk>7</event_incident_typefk><elapsed>90</elapsed><subtype>cross</subtype><player1>24436</player1><sortorder>1</sortorder><team>8533</team><n>327</n><type>cross</type><id>736375</id></value><value><stats><crosses>1</crosses></stats><elapsed_plus>2</elapsed_plus><event_incident_typefk>7</event_incident_typefk><elapsed>90</elapsed><subtype>cross</subtype><player1>42008</player1><sortorder>1</sortorder><team>8533</team><n>334</n><type>cross</type><id>736389</id></value><value><stats><crosses>1</crosses></stats><elapsed_plus>3</elapsed_plus><event_incident_typefk>7</event_incident_typefk><elapsed>90</elapsed><subtype>cross</subtype><player1>41890</player1><sortorder>0</sortorder><team>9885</team><n>337</n><type>cross</type><id>736395</id></value></cross> | null |
| corner | null | <corner><value><stats><corners>1</corners></stats><event_incident_typefk>329</event_incident_typefk><elapsed>26</elapsed><subtype>cross</subtype><player1>30871</player1><sortorder>2</sortorder><team>9885</team><n>265</n><type>corner</type><id>735847</id></value><value><stats><corners>1</corners></stats><event_incident_typefk>329</event_incident_typefk><elapsed>27</elapsed><subtype>cross</subtype><player1>30871</player1><sortorder>1</sortorder><team>9885</team><n>232</n><type>corner</type><id>735853</id></value><value><stats><corners>1</corners></stats><event_incident_typefk>329</event_incident_typefk><elapsed>28</elapsed><subtype>cross</subtype><player1>39286</player1><sortorder>1</sortorder><team>8533</team><n>231</n><type>corner</type><id>735862</id></value><value><stats><corners>1</corners></stats><event_incident_typefk>329</event_incident_typefk><elapsed>29</elapsed><subtype>cross</subtype><player1>41890</player1><sortorder>1</sortorder><team>9885</team><n>277</n><type>corner</type><id>735872</id></value><value><stats><corners>1</corners></stats><event_incident_typefk>327</event_incident_typefk><elapsed>33</elapsed><subtype>cross</subtype><sortorder>1</sortorder><team>9885</team><n>253</n><type>corner</type><id>735899</id></value><value><stats><corners>1</corners></stats><event_incident_typefk>329</event_incident_typefk><elapsed>42</elapsed><subtype>cross</subtype><player1>31235</player1><sortorder>0</sortorder><team>9885</team><n>246</n><type>corner</type><id>735951</id></value><value><stats><corners>1</corners></stats><event_incident_typefk>329</event_incident_typefk><elapsed>43</elapsed><subtype>cross</subtype><player1>31235</player1><sortorder>1</sortorder><team>9885</team><n>260</n><type>corner</type><id>735964</id></value><value><stats><corners>1</corners></stats><event_incident_typefk>329</event_incident_typefk><elapsed>43</elapsed><subtype>cross</subtype><player1>31235</player1><sortorder>3</sortorder><team>9885</team><n>269</n><type>corner</type><id>735969</id></value><value><stats><corners>1</corners></stats><event_incident_typefk>330</event_incident_typefk><elapsed>57</elapsed><subtype>short</subtype><player1>39286</player1><sortorder>0</sortorder><team>8533</team><n>299</n><type>corner</type><id>736137</id></value><value><stats><corners>1</corners></stats><event_incident_typefk>329</event_incident_typefk><elapsed>66</elapsed><subtype>cross</subtype><player1>31235</player1><sortorder>1</sortorder><team>9885</team><n>326</n><type>corner</type><id>736197</id></value><value><stats><corners>1</corners></stats><event_incident_typefk>330</event_incident_typefk><elapsed>67</elapsed><subtype>short</subtype><player1>30871</player1><sortorder>0</sortorder><team>9885</team><n>287</n><type>corner</type><id>736203</id></value></corner> | null |
| possession | null | <possession /> | null |
| B365H | null | 1.29 | null |
| B365D | null | 5.25 | null |
| B365A | null | 11 | null |
| BWH | null | 1.3 | null |
| BWD | null | 4.55 | null |
| BWA | null | 8.75 | null |
| IWH | null | 1.25 | null |
| IWD | null | 5 | null |
| IWA | null | 12 | null |
| LBH | null | 1.3 | null |
| LBD | null | 4.2 | null |
| LBA | null | 9 | null |
| PSH | null | null | null |
| PSD | null | null | null |
| PSA | null | null | null |
| WHH | null | 1.25 | null |
| WHD | null | 4.5 | null |
| WHA | null | 10 | null |
| SJH | null | 1.29 | null |
| SJD | null | 5 | null |
| SJA | null | 11 | null |
| VCH | null | 1.25 | null |
| VCD | null | 5 | null |
| VCA | null | 10 | null |
| GBH | null | 1.3 | null |
| GBD | null | 5 | null |
| GBA | null | 9 | null |
| BSH | null | 1.25 | null |
| BSD | null | 5 | null |
| BSA | null | 11 | null |

# "Player"  (rows=11060)

columns:
"id" int PK: unique identifier, 1..11075
"player_api_id" int UNIQ: unique identifier, 2625..750584
"player_name" text: 10848 distinct
"player_fifa_api_id" int UNIQ: unique identifier, 2..234141
"birthday" text: iso-date, 5762 distinct
"height" int: 20 distinct, 157.48..208.28, avg=181.867, median=182.88
"weight" int: 50 distinct, 117..243, avg=168.38, median=168

indexes: none
fk: none

samples:
| column | latest | sample | sample |
|---|---|---|---|
| id | 11075 | 9307 | 4026 |
| player_api_id | 39902 | 500618 | 13480 |
| player_name | Zvjezdan Misimovic | Rui Correia | Grzegorz Wojtkowiak |
| player_fifa_api_id | 102359 | 223625 | 152950 |
| birthday | 1982-06-05 00:00:00 | 1990-08-23 00:00:00 | 1984-01-26 00:00:00 |
| height | 180.34 | 187.96 | 182.88 |
| weight | 176 | 165 | 165 |

# "Player_Attributes"  (rows=183978)

columns:
"id" int PK: unique identifier, 1..183978
"player_fifa_api_id" int FK: 2..234141
"player_api_id" int FK: 2625..750584
"date" text: iso-date
"overall_rating" int: nulls=836, 33..94, avg=68.6
"potential" int: nulls=836, 39..97, avg=73.4604
"preferred_foot" text: nulls=836
"attacking_work_rate" text: nulls=3230
"defensive_work_rate" text: nulls=836
"crossing" int: nulls=836, 1..95, avg=55.0869
"finishing" int: nulls=836, 1..97, avg=49.9211
"heading_accuracy" int: nulls=836, 1..98, avg=57.266
"short_passing" int: nulls=836, 3..97, avg=62.4297
"volleys" int: nulls=2713, 1..93, avg=49.4684
"dribbling" int: nulls=836, 1..97, avg=59.1752
"curve" int: nulls=2713, 2..94, avg=52.9657
"free_kick_accuracy" int: nulls=836, 1..97, avg=49.381
"long_passing" int: nulls=836, 3..97, avg=57.0699
"ball_control" int: nulls=836, 5..97, avg=63.3889
"acceleration" int: nulls=836, 10..97, avg=67.6594
"sprint_speed" int: nulls=836, 12..97, avg=68.0512
"agility" int: nulls=2713, 11..96, avg=65.9709
"reactions" int: nulls=836, 17..96, avg=66.1037
"balance" int: nulls=2713, 12..96, avg=65.1895
"shot_power" int: nulls=836, 2..97, avg=61.8084
"jumping" int: nulls=2713, 14..96, avg=66.969
"stamina" int: nulls=836, 10..96, avg=67.0385
"strength" int: nulls=836, 10..96, avg=67.4245
"long_shots" int: nulls=836, 1..96, avg=53.3394
"aggression" int: nulls=836, 6..97, avg=60.948
"interceptions" int: nulls=836, 1..96, avg=52.0093
"positioning" int: nulls=836, 2..96, avg=55.7865
"vision" int: nulls=2713, 1..97, avg=57.8735
"penalties" int: nulls=836, 2..96, avg=55.004
"marking" int: nulls=836, 1..96, avg=46.7722
"standing_tackle" int: nulls=836, 1..95, avg=50.3513
"sliding_tackle" int: nulls=2713, 2..95, avg=48.0015
"gk_diving" int: nulls=836, 1..94, avg=14.7044
"gk_handling" int: nulls=836, 1..93, avg=16.0636
"gk_kicking" int: nulls=836, 1..97, avg=20.9984
"gk_positioning" int: nulls=836, 1..96, avg=16.1322
"gk_reflexes" int: nulls=836, 1..96, avg=16.4414

indexes: none
fk: "player_fifa_api_id"→"Player"."player_fifa_api_id", "player_api_id"→"Player"."player_api_id"

samples:
| column | latest | sample | sample |
|---|---|---|---|
| id | 183978 | 112445 | 83563 |
| player_fifa_api_id | 102359 | 114356 | 228279 |
| player_api_id | 39902 | 25947 | 588337 |
| date | 2007-02-22 00:00:00 | 2015-09-21 00:00:00 | 2007-02-22 00:00:00 |
| overall_rating | 80 | 65 | 57 |
| potential | 81 | 65 | 70 |
| preferred_foot | right | right | right |
| attacking_work_rate | medium | medium | medium |
| defensive_work_rate | low | medium | medium |
| crossing | 74 | 12 | 25 |
| finishing | 68 | 13 | 25 |
| heading_accuracy | 57 | 13 | 20 |
| short_passing | 88 | 13 | 31 |
| volleys | 77 | 14 | 25 |
| dribbling | 87 | 11 | 25 |
| curve | 86 | 16 | 20 |
| free_kick_accuracy | 53 | 14 | 20 |
| long_passing | 78 | 12 | 26 |
| ball_control | 91 | 12 | 20 |
| acceleration | 58 | 53 | 41 |
| sprint_speed | 64 | 52 | 44 |
| agility | 77 | 48 | 39 |
| reactions | 66 | 66 | 58 |
| balance | 73 | 57 | 44 |
| shot_power | 72 | 13 | 20 |
| jumping | 58 | 68 | 53 |
| stamina | 67 | 24 | 51 |
| strength | 59 | 60 | 68 |
| long_shots | 78 | 12 | 25 |
| aggression | 63 | 36 | 54 |
| interceptions | 63 | 23 | 25 |
| positioning | 68 | 16 | 25 |
| vision | 88 | 50 | 20 |
| penalties | 53 | 11 | 31 |
| marking | 38 | 11 | 25 |
| standing_tackle | 32 | 11 | 25 |
| sliding_tackle | 30 | 13 | 25 |
| gk_diving | 9 | 70 | 64 |
| gk_handling | 9 | 53 | 55 |
| gk_kicking | 78 | 75 | 50 |
| gk_positioning | 7 | 64 | 50 |
| gk_reflexes | 15 | 71 | 59 |

# "Team"  (rows=299)

columns:
"id" int PK: unique identifier, 1..51606
"team_api_id" int UNIQ: unique identifier, 1601..274581
"team_fifa_api_id" int: 285 distinct, nulls=11, 1..112513
"team_long_name" text: 296 distinct
"team_short_name" text: 259 distinct

indexes: none
fk: none

samples:
| column | latest | sample | sample |
|---|---|---|---|
| id | 51606 | 43051 | 20518 |
| team_api_id | 7896 | 8315 | 10233 |
| team_fifa_api_id | null | 448 | 110556 |
| team_long_name | Lugano | Athletic Club de Bilbao | Genoa |
| team_short_name | LUG | BIL | GEN |

# "Team_Attributes"  (rows=1458)

columns:
"id" int PK: unique identifier, 1..1458
"team_fifa_api_id" int FK: 285 distinct, 1..112513
"team_api_id" int FK: 288 distinct, 1601..274581
"date" text: "2015-09-10 00:00:00"=245, "2011-02-22 00:00:00"=244, "2014-09-19 00:00:00"=244, "2012-02-22 00:00:00"=242, "2013-09-20 00:00:00"=242, "2010-02-22 00:00:00"=241
"buildUpPlaySpeed" int: 57 distinct, 20..80, avg=52.4623, median=52
"buildUpPlaySpeedClass" text: "Balanced"=1184, "Fast"=172, "Slow"=102
"buildUpPlayDribbling" int: 49 distinct, nulls=969, 24..77, avg=48.6074, median=49
"buildUpPlayDribblingClass" text: "Little"=1004, "Normal"=433, "Lots"=21
"buildUpPlayPassing" int: 58 distinct, 20..80, avg=48.4904, median=50
"buildUpPlayPassingClass" text: "Mixed"=1236, "Short"=128, "Long"=94
"buildUpPlayPositioningClass" text: "Organised"=1386, "Free Form"=72
"chanceCreationPassing" int: 50 distinct, 21..80, avg=52.1653, median=52
"chanceCreationPassingClass" text: "Normal"=1231, "Risky"=171, "Safe"=56
"chanceCreationCrossing" int: 56 distinct, 20..80, avg=53.7318, median=53
"chanceCreationCrossingClass" text: "Normal"=1195, "Lots"=211, "Little"=52
"chanceCreationShooting" int: 57 distinct, 22..80, avg=53.9691, median=53
"chanceCreationShootingClass" text: "Normal"=1224, "Lots"=197, "Little"=37
"chanceCreationPositioningClass" text: "Organised"=1309, "Free Form"=149
"defencePressure" int: 48 distinct, 23..72, avg=46.0171, median=45
"defencePressureClass" text: "Medium"=1243, "Deep"=154, "High"=61
"defenceAggression" int: 47 distinct, 24..72, avg=49.251, median=48
"defenceAggressionClass" text: "Press"=1274, "Double"=99, "Contain"=85
"defenceTeamWidth" int: 43 distinct, 29..73, avg=52.1859, median=52
"defenceTeamWidthClass" text: "Normal"=1286, "Wide"=111, "Narrow"=61
"defenceDefenderLineClass" text: "Cover"=1362, "Offside Trap"=96

indexes: none
fk: "team_api_id"→"Team"."team_api_id", "team_fifa_api_id"→"Team"."team_fifa_api_id"

samples:
| column | latest | sample | sample |
|---|---|---|---|
| id | 1458 | 993 | 227 |
| team_fifa_api_id | 15005 | 110746 | 1943 |
| team_api_id | 10000 | 8023 | 8678 |
| date | 2015-09-10 00:00:00 | 2013-09-20 00:00:00 | 2012-02-22 00:00:00 |
| buildUpPlaySpeed | 54 | 67 | 46 |
| buildUpPlaySpeedClass | Balanced | Fast | Balanced |
| buildUpPlayDribbling | 42 | null | null |
| buildUpPlayDribblingClass | Normal | Little | Little |
| buildUpPlayPassing | 51 | 54 | 46 |
| buildUpPlayPassingClass | Mixed | Mixed | Mixed |
| buildUpPlayPositioningClass | Organised | Organised | Organised |
| chanceCreationPassing | 47 | 56 | 54 |
| chanceCreationPassingClass | Normal | Normal | Normal |
| chanceCreationCrossing | 52 | 62 | 60 |
| chanceCreationCrossingClass | Normal | Normal | Normal |
| chanceCreationShooting | 32 | 67 | 52 |
| chanceCreationShootingClass | Little | Lots | Normal |
| chanceCreationPositioningClass | Organised | Organised | Organised |
| defencePressure | 44 | 47 | 48 |
| defencePressureClass | Medium | Medium | Medium |
| defenceAggression | 58 | 47 | 50 |
| defenceAggressionClass | Press | Press | Press |
| defenceTeamWidth | 37 | 63 | 62 |
| defenceTeamWidthClass | Normal | Normal | Normal |
| defenceDefenderLineClass | Cover | Cover | Cover |

# "match_view"  (rows=25979)

```sql
CREATE VIEW match_view AS SELECT
    M.id,
    L.name AS league,
    M.season,
    M.match_api_id,
    T.team_long_name AS home_team,
    TM.team_long_name AS away_team,
    M.home_team_goal,
    M.away_team_goal,
    P1.player_name AS home_gk,
    P2.player_name AS home_center_back_1,
    P3.player_name AS home_center_back_2,
    P4.player_name AS home_right_back,
    P5.player_name AS home_left_back,
    P6.player_name AS home_midfield_1,
    P7.player_name AS home_midfield_2,
    P8.player_name AS home_midfield_3,
    P9.player_name AS home_midfield_4,
    P10.player_name AS home_second_forward,
    P11.player_name AS home_center_forward,
    P12.player_name AS away_gk,
    P13.player_name AS away_center_back_1,
    P14.player_name AS away_center_back_2,
    P15.player_name AS away_right_back,
    P16.player_name AS away_left_back,
    P17.player_name AS away_midfield_1,
    P18.player_name AS away_midfield_2,
    P19.player_name AS away_midfield_3,
    P20.player_name AS away_midfield_4,
    P21.player_name AS away_second_forward,
    P22.player_name AS away_center_forward,
    M.goal,
    M.card
FROM
    match M
LEFT JOIN
    league L ON M.league_id = L.id
LEFT JOIN
    team T ON M.home_team_api_id = T.team_api_id
LEFT JOIN
    team TM ON M.away_team_api_id = TM.team_api_id
LEFT JOIN
    player P1 ON M.home_player_1 = P1.player_api_id
LEFT JOIN
    player P2 ON M.home_player_2 = P2.player_api_id
LEFT JOIN
    player P3 ON M.home_player_3 = P3.player_api_id
LEFT JOIN
    player P4 ON M.home_player_4 = P4.player_api_id
LEFT JOIN
    player P5 ON M.home_player_5 = P5.player_api_id
LEFT JOIN
    player P6 ON M.home_player_6 = P6.player_api_id
LEFT JOIN
    player P7 ON M.home_player_7 = P7.player_api_id
LEFT JOIN
    player P8 ON M.home_player_8 = P8.player_api_id
LEFT JOIN
    player P9 ON M.home_player_9 = P9.player_api_id
LEFT JOIN
    player P10 ON M.home_player_10 = P10.player_api_id
LEFT JOIN
    player P11 ON M.home_player_11 = P11.player_api_id
LEFT JOIN
    player P12 ON M.away_player_1 = P12.player_api_id
LEFT JOIN
    player P13 ON M.away_player_2 = P13.player_api_id
LEFT JOIN
    player P14 ON M.away_player_3 = P14.player_api_id
LEFT JOIN
    player P15 ON M.away_player_4 = P15.player_api_id
LEFT JOIN
    player P16 ON M.away_player_5 = P16.player_api_id
LEFT JOIN
    player P17 ON M.away_player_6 = P17.player_api_id
LEFT JOIN
    player P18 ON M.away_player_7 = P18.player_api_id
LEFT JOIN
    player P19 ON M.away_player_8 = P19.player_api_id
LEFT JOIN
    player P20 ON M.away_player_9 = P20.player_api_id
LEFT JOIN
    player P21 ON M.away_player_10 = P21.player_api_id
LEFT JOIN
    player P22 ON M.away_player_11 = P22.player_api_id;
```

columns:
"id" int: unique identifier, 1..25979
"league" text: "England Premier League"=3040, "France Ligue 1"=3040, "Spain LIGA BBVA"=3040, "Italy Serie A"=3017, "Germany 1. Bundesliga"=2448, "Netherlands Eredivisie"=2448, "Portugal Liga ZON Sagres"=2052, "Poland Ekstraklasa"=1920, "Scotland Premier League"=1824, "Belgium Jupiler League"=1728, "Switzerland Super League"=1422
"season" text: "2008/2009"=3326, "2015/2016"=3326, "2014/2015"=3325, "2010/2011"=3260, "2012/2013"=3260, "2009/2010"=3230, "2011/2012"=3220, "2013/2014"=3032
"match_api_id" int: unique identifier, 483129..2216672
"home_team" text: 296 distinct
"away_team" text: 296 distinct
"home_team_goal" int: 1=8400, 2=6339, 0=5896, 3=3288, 4=1385, 5=457, 6=161, 7=38, 8=9, 9=4, 10=2, 0..10
"away_team_goal" int: 1=8989, 0=8687, 2=5146, 3=2145, 4=718, 5=215, 6=63, 7=10, 8=5, 9=1, 0..9
"home_gk" text: 894 distinct, nulls=1224
"home_center_back_1" text: 2397 distinct, nulls=1315
"home_center_back_2" text: 2360 distinct, nulls=1281
"home_right_back" text: 2590 distinct, nulls=1323
"home_left_back" text: 2754 distinct, nulls=1316
"home_midfield_1" text: 3770 distinct, nulls=1325
"home_midfield_2" text: 3403 distinct, nulls=1227
"home_midfield_3" text: 4049 distinct, nulls=1309
"home_midfield_4" text: 4087 distinct, nulls=1273
"home_second_forward" text: 3623 distinct, nulls=1436
"home_center_forward" text: 2880 distinct, nulls=1555
"away_gk" text: 913 distinct, nulls=1234
"away_center_back_1" text: 2487 distinct, nulls=1278
"away_center_back_2" text: 2453 distinct, nulls=1293
"away_right_back" text: 2642 distinct, nulls=1321
"away_left_back" text: 2867 distinct, nulls=1335
"away_midfield_1" text: 3904 distinct, nulls=1313
"away_midfield_2" text: 3593 distinct, nulls=1235
"away_midfield_3" text: 4214 distinct, nulls=1341
"away_midfield_4" text: 4294 distinct, nulls=1328
"away_second_forward" text: 3872 distinct, nulls=1441
"away_center_forward" text: 3027 distinct, nulls=1554
"goal" text: 13225 distinct, nulls=11762
"card" text: 13777 distinct, nulls=11762

samples:
| column | latest | sample | sample |
|---|---|---|---|
| id | 25979 | 2420 | 2706 |
| league | Switzerland Super League | England Premier League | England Premier League |
| season | 2015/2016 | 2009/2010 | 2010/2011 |
| match_api_id | 1992095 | 659370 | 840142 |
| home_team | BSC Young Boys | Everton | Birmingham City |
| away_team | FC Basel | Portsmouth | West Bromwich Albion |
| home_team_goal | 4 | 1 | 1 |
| away_team_goal | 3 | 0 | 3 |
| home_gk | Yvon Mvogo | Tim Howard | Ben Foster |
| home_center_back_1 | Florent Hadergjonaj | Tony Hibbert | Stephen Carr |
| home_center_back_2 | Milan Vilotic | Phil Jagielka | Roger Johnson |
| home_right_back | Steve von Bergen | Sylvain Distin | Curtis Davies |
| home_left_back | Jan Lecjaks | Leighton Baines | Liam Ridgewell |
| home_midfield_1 | Renato Steffen | Leon Osman | Jean Beausejour |
| home_midfield_2 | Denis Zakaria | Jack Rodwell | Keith Fahey |
| home_midfield_3 | Alain Rochat | Mikel Arteta | Lee Bowyer |
| home_midfield_4 | Miralem Sulejmani | Steven Pienaar | David Bentley |
| home_second_forward | Yuya Kubo | Victor Anichebe | Cameron Jerome |
| home_center_forward | Alexander Gerndt | Louis Saha | Obafemi Martins |
| away_gk | Tomas Vaclik | Jamie Ashdown | Scott Carson |
| away_center_back_1 | Michael Lang | Steve Finnan | Steven Reid |
| away_center_back_2 | Daniel Hoeegh | Ricardo Rocha | Jonas Olsson |
| away_right_back | Marek Suchy | Aaron Mokoena | Abdoulaye Meite |
| away_left_back | Naser Aliji | Anthony Vanden Borre | Nicky Shorey |
| away_midfield_1 | Taulant Xhaka | Hayden Mullins | Chris Brunt |
| away_midfield_2 | Zdravko Kuzmanovic | Papa Bouba Diop | Paul Scharner |
| away_midfield_3 | Birkir Bjarnason | Marc Wilson | James Morrison |
| away_midfield_4 | Matias Emilio Delgado | Kevin-Prince Boateng | Youssuf Mulumbu |
| away_second_forward | Shkelzen Gashi | Frederic Piquionne | Jerome Thomas |
| away_center_forward | Breel Embolo | John Utaka | Marc-Antoine Fortune |
| goal | null | <goal><value><comment>n</comment><stats><goals>1</goals><shoton>1</shoton></stats><elapsed_plus>4</elapsed_plus><event_incident_typefk>393</event_incident_typefk><elapsed>90</elapsed><player2>30839</player2><subtype>shot</subtype><player1>10491</player1><sortorder>1</sortorder><team>8668</team><id>1083239</id><n>183</n><type>goal</type><goal_type>n</goal_type></value></goal> | <goal><value><comment>n</comment><stats><goals>1</goals><shoton>1</shoton></stats><event_incident_typefk>393</event_incident_typefk><elapsed>47</elapsed><player2>25550</player2><subtype>shot</subtype><player1>71502</player1><sortorder>0</sortorder><team>8659</team><id>1439659</id><n>287</n><type>goal</type><goal_type>n</goal_type></value><value><comment>n</comment><stats><goals>1</goals><shoton>1</shoton></stats><event_incident_typefk>393</event_incident_typefk><elapsed>48</elapsed><player2>33049</player2><subtype>shot</subtype><player1>38254</player1><sortorder>1</sortorder><team>8658</team><id>1439661</id><n>288</n><type>goal</type><goal_type>n</goal_type></value><value><comment>n</comment><stats><goals>1</goals><shoton>1</shoton></stats><event_incident_typefk>393</event_incident_typefk><elapsed>58</elapsed><player2>23922</player2><subtype>shot</subtype><player1>24171</player1><sortorder>0</sortorder><team>8659</team><id>1439683</id><n>301</n><type>goal</type><goal_type>n</goal_type></value><value><comment>n</comment><stats><goals>1</goals><shoton>1</shoton></stats><event_incident_typefk>406</event_incident_typefk><elapsed>72</elapsed><player2>24171</player2><subtype>header</subtype><player1>25005</player1><sortorder>4</sortorder><team>8659</team><id>1439726</id><n>317</n><type>goal</type><goal_type>n</goal_type></value></goal> |
| card | null | <card /> | <card><value><comment>y</comment><stats><ycards>1</ycards></stats><event_incident_typefk>73</event_incident_typefk><elapsed>51</elapsed><card_type>y</card_type><subtype>serious_fouls</subtype><player1>33049</player1><sortorder>2</sortorder><team>8658</team><n>291</n><type>card</type><id>1439666</id></value><value><comment>y</comment><stats><ycards>1</ycards></stats><event_incident_typefk>505</event_incident_typefk><elapsed>53</elapsed><card_type>y</card_type><subtype>Unsportsmanlike Cond</subtype><player1>25005</player1><sortorder>0</sortorder><team>8659</team><n>293</n><type>card</type><id>1439668</id></value><value><comment>y</comment><stats><ycards>1</ycards></stats><event_incident_typefk>505</event_incident_typefk><elapsed>53</elapsed><card_type>y</card_type><subtype>Unsportsmanlike Cond</subtype><player1>23787</player1><sortorder>1</sortorder><team>8658</team><n>294</n><type>card</type><id>1439669</id></value><value><comment>y</comment><stats><ycards>1</ycards></stats><event_incident_typefk>73</event_incident_typefk><elapsed>88</elapsed><card_type>y</card_type><subtype>serious_fouls</subtype><player1>77704</player1><sortorder>3</sortorder><team>8658</team><n>334</n><type>card</type><id>1439770</id></value></card> |
