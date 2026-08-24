---
generator: db-snooper
version: 0.0.34
generated_at_utc: 2026-08-24T21:56:56.462093Z
dialect: sqlite
database: /var/folders/9j/b9bx_drd53sc6zbpsqyrjy4h0000gn/T/dbsnoop-unc16lu8/Baseball.sqlite
schema: main
---

# "all_star"  (rows=5069)

columns:
"player_id" text: 1741 distinct
"year" int: 83 distinct, 1933..2015, avg=1976.43, median=1976
"game_num" int: 0=4615, 2=240, 1=214, 0..2
"game_id" text: 106 distinct
"team_id" text: 49 distinct
"league_id" text: "AL"=2544, "NL"=2525
"gp" numeric: 1=3930, 0=1120, ""=19
"starting_pos" numeric: ""=3489, 1=172, 2=172, 3=172, 4=172, 5=172, 6=172, 7=172, 8=172, 9=172, 10=22, 0=10

indexes: none

samples:
| column | latest | sample | sample |
|---|---|---|---|
| player_id | zobribe01 | marioma01 | moonwa01 |
| year | 2013 | 1943 | 1957 |
| game_num | 0 | 0 | 0 |
| game_id | NLS201307160 | ALS194307130 | NLS195707090 |
| team_id | TBA | SLN | SLN |
| league_id | AL | NL | NL |
| gp | 0 | 1 | 1 |
| starting_pos |  | 6 |  |

# "appearances"  (rows=100951)

columns:
"year" int: 1871..2015, avg=1963.35
"team_id" text: profile metrics skipped
"league_id" text: profile metrics skipped
"player_id" text: profile metrics skipped
"g_all" numeric: profile metrics skipped
"gs" numeric: profile metrics skipped
"g_batting" int: 0..165, avg=48.6825
"g_defense" numeric: profile metrics skipped
"g_p" int: 0..106, avg=10.3492
"g_c" int: 0..160, avg=4.76603
"g_1b" int: 0..162, avg=4.61472
"g_2b" int: 0..163, avg=4.59789
"g_3b" int: 0..164, avg=4.61361
"g_ss" int: 0..165, avg=4.58756
"g_lf" int: 0..163, avg=4.864
"g_cf" int: 0..162, avg=4.59522
"g_rf" int: 0..162, avg=4.7268
"g_of" int: 0..164, avg=13.8813
"g_dh" numeric: profile metrics skipped
"g_ph" numeric: profile metrics skipped
"g_pr" numeric: profile metrics skipped

indexes: none

samples:
| column | latest | sample | sample |
|---|---|---|---|
| year | 2015 | 1913 | 1987 |
| team_id | WAS | CHA | PIT |
| league_id | NL | AL | NL |
| player_id | zimmery01 | bretoji01 | drummti01 |
| g_all | 95 | 12 | 6 |
| gs | 92 |  | 0 |
| g_batting | 95 | 12 | 6 |
| g_defense | 93 | 12 | 6 |
| g_p | 0 | 0 | 6 |
| g_c | 0 | 0 | 0 |
| g_1b | 93 | 0 | 0 |
| g_2b | 0 | 0 | 0 |
| g_3b | 0 | 3 | 0 |
| g_ss | 0 | 7 | 0 |
| g_lf | 1 | 0 | 0 |
| g_cf | 0 | 0 | 0 |
| g_rf | 0 | 0 | 0 |
| g_of | 1 | 0 | 0 |
| g_dh | 0 |  | 0 |
| g_ph | 3 |  | 0 |
| g_pr | 0 |  | 0 |

# "batting"  (rows=101332)

columns:
"player_id" text: profile metrics skipped
"year" int: 1871..2015, avg=1963.51
"stint" int: 1..5, avg=1.07757
"team_id" text: profile metrics skipped
"league_id" text: profile metrics skipped
"g" int: 0..165, avg=51.4001
"ab" numeric: profile metrics skipped
"r" numeric: profile metrics skipped
"h" numeric: profile metrics skipped
"double" numeric: profile metrics skipped
"triple" numeric: profile metrics skipped
"hr" numeric: profile metrics skipped
"rbi" numeric: profile metrics skipped
"sb" numeric: profile metrics skipped
"cs" numeric: profile metrics skipped
"bb" numeric: profile metrics skipped
"so" numeric: profile metrics skipped
"ibb" numeric: profile metrics skipped
"hbp" numeric: profile metrics skipped
"sh" numeric: profile metrics skipped
"sf" numeric: profile metrics skipped
"g_idp" numeric: profile metrics skipped

indexes: none

samples:
| column | latest | sample | sample |
|---|---|---|---|
| player_id | zychto01 | radfopa01 | morrilo01 |
| year | 2015 | 1887 | 2013 |
| stint | 1 | 1 | 1 |
| team_id | SEA | NY4 | MIA |
| league_id | AL | AA | NL |
| g | 13 | 128 | 85 |
| ab | 0 | 486 | 293 |
| r | 0 | 127 | 32 |
| h | 0 | 129 | 71 |
| double | 0 | 15 | 13 |
| triple | 0 | 5 | 4 |
| hr | 0 | 4 | 6 |
| rbi | 0 | 45 | 36 |
| sb | 0 | 73 | 0 |
| cs | 0 |  | 0 |
| bb | 0 | 106 | 38 |
| so | 0 |  | 56 |
| ibb | 0 |  | 5 |
| hbp | 0 | 6 | 2 |
| sh | 0 |  | 0 |
| sf | 0 |  | 0 |
| g_idp | 0 |  | 10 |

# "batting_postseason"  (rows=11690)

columns:
"year" int: 119 distinct, 1884..2015, avg=1983.04, median=1995
"round" text: "WS"=4594, "NLCS"=2089, "ALCS"=1409, "NLDS2"=973, "NLDS1"=945, "ALDS1"=637, "ALDS2"=622, "ALWC"=134, "NLWC"=117, "NWDIV"=46, "NEDIV"=45, "AEDIV"=28, "AWDIV"=26, "CS"=25
"player_id" text: 3973 distinct
"team_id" text: 48 distinct
"league_id" text: "NL"=6565, "AL"=5039, "AA"=86
"g" int: 1=2725, 2=2074, 3=2028, 4=1702, 5=1486, 6=833, 7=741, 8=61, 9=14, 10=11, 15=11, 11=2, 13=1, 14=1, 1..15
"ab" int: 52 distinct, 0..66, avg=8.84089, median=5
"r" int: 0=6478, 1=2076, 2=1253, 3=831, 4=487, 5=320, 6=131, 7=49, 8=40, 9=12, 10=7, 12=5, 13=1, 0..13
"h" int: 0=5057, 1=1567, 2=1063, 3=876, 4=819, 5=714, 6=572, 7=417, 8=236, 9=169, 10=88, 11=62, 12=29, 13=10, 14=5, 15=2, 21=2, 17=1, 19=1, 0..21
"double" int: 0=8675, 1=2008, 2=720, 3=222, 4=56, 5=6, 6=3, 0..6
"triple" int: 0=11097, 1=544, 2=43, 3=5, 4=1, 0..4
"hr" int: 0=9796, 1=1390, 2=382, 3=95, 4=22, 5=4, 6=1, 0..6
"rbi" int: 0=7109, 1=1732, 2=1132, 3=684, 4=456, 5=253, 6=150, 7=85, 8=42, 9=24, 10=12, 11=6, 12=4, 13=1, 0..13
"sb" int: 0=10380, 1=936, 2=225, 3=85, 4=25, 5=19, 6=9, 7=6, 8=2, 10=1, 11=1, 15=1, 0..15
"cs" numeric: 0=10698, 1=688, ""=201, 2=89, 3=11, 4=2, 5=1
"bb" int: 0=7047, 1=2110, 2=1213, 3=677, 4=311, 5=188, 6=78, 7=39, 8=15, 9=5, 10=3, 11=2, 12=1, 13=1, 0..13
"so" int: 0=4583, 1=2329, 2=1678, 3=1133, 4=785, 5=510, 6=285, 7=201, 8=101, 9=50, 10=14, 11=12, 12=6, 13=3, 0..13
"ibb" numeric: 0=9839, ""=1039, 1=651, 2=121, 3=32, 4=4, 5=2, 6=1, 7=1
"hbp" numeric: 0=9767, ""=1237, 1=622, 2=57, 3=5, 4=2
"sh" numeric: 0=9336, ""=1244, 1=932, 2=150, 3=20, 4=7, 5=1
"sf" numeric: 0=9877, ""=1248, 1=519, 2=45, 3=1
"g_idp" numeric: 0=8912, 1=1345, ""=1205, 2=198, 3=25, 4=4, 5=1

indexes: none

samples:
| column | latest | sample | sample |
|---|---|---|---|
| year | 2015 | 1929 | 1989 |
| round | WS | WS | NLCS |
| player_id | zobribe01 | tolsoch01 | wilkecu01 |
| team_id | KCA | CHN | CHN |
| league_id | AL | NL | NL |
| g | 5 | 1 | 3 |
| ab | 23 | 1 | 2 |
| r | 5 | 0 | 1 |
| h | 6 | 0 | 1 |
| double | 4 | 0 | 0 |
| triple | 0 | 0 | 0 |
| hr | 0 | 0 | 0 |
| rbi | 0 | 0 | 0 |
| sb | 0 | 0 | 0 |
| cs | 0 | 0 | 0 |
| bb | 3 | 0 | 0 |
| so | 2 | 1 | 0 |
| ibb | 2 | 0 | 0 |
| hbp | 0 | 0 | 0 |
| sh | 0 | 0 | 0 |
| sf | 0 | 0 | 0 |
| g_idp | 0 | 0 | 0 |

# "college"  (rows=1207)

columns:
"college_id" text: unique identifier
"name_full" text: 1199 distinct
"city" text: 856 distinct
"state" text: 49 distinct
"country" text: "USA"=1207

indexes: none

samples:
| column | latest | sample | sample |
|---|---|---|---|
| college_id | youngst | ilswijc | ohcapit |
| name_full | Youngstown State University | Southwestern Illinois College | Capital University |
| city | Youngstown | Belleville | Bexley |
| state | OH | IL | OH |
| country | USA | USA | USA |

# "fielding"  (rows=170526)

columns:
"player_id" text: profile metrics skipped
"year" int: 1871..2015, avg=1966.52
"stint" int: 1..5, avg=1.07782
"team_id" text: profile metrics skipped
"league_id" text: profile metrics skipped
"pos" text: profile metrics skipped
"g" int: 0..165, avg=33.6519
"gs" numeric: profile metrics skipped
"inn_outs" numeric: profile metrics skipped
"po" numeric: profile metrics skipped
"a" numeric: profile metrics skipped
"e" numeric: profile metrics skipped
"dp" numeric: profile metrics skipped
"pb" numeric: profile metrics skipped
"wp" numeric: profile metrics skipped
"sb" numeric: profile metrics skipped
"cs" numeric: profile metrics skipped
"zr" numeric: profile metrics skipped

indexes: none

samples:
| column | latest | sample | sample |
|---|---|---|---|
| player_id | zychto01 | bellhma01 | recciph01 |
| year | 2015 | 2003 | 1885 |
| stint | 1 | 2 | 1 |
| team_id | SEA | COL | LS2 |
| league_id | AL | NL | AA |
| pos | P | SS | 3B |
| g | 13 | 6 | 97 |
| gs |  |  |  |
| inn_outs |  | 69 |  |
| po | 0 | 1 | 105 |
| a | 3 | 9 | 181 |
| e | 0 | 0 | 59 |
| dp | 0 | 1 | 17 |
| pb |  |  |  |
| wp |  |  |  |
| sb |  |  |  |
| cs |  |  |  |
| zr |  |  |  |

# "fielding_outfield"  (rows=12028)

columns:
"player_id" text: 3513 distinct
"year" int: 85 distinct, 1871..1955, avg=1912.74, median=1912
"stint" int: 1=11067, 2=890, 3=63, 4=7, 5=1, 1..5
"glf" numeric: 158 distinct
"gcf" numeric: 160 distinct
"grf" numeric: 160 distinct

indexes: none

samples:
| column | latest | sample | sample |
|---|---|---|---|
| player_id | zwilldu01 | thronfa01 | hoydu01 |
| year | 1916 | 1955 | 1901 |
| stint | 1 | 1 | 1 |
| glf | 0 | 32 | 0 |
| gcf | 5 | 0 | 132 |
| grf | 4 | 3 | 0 |

# "fielding_postseason"  (rows=12311)

columns:
"player_id" text: 3726 distinct
"year" int: 111 distinct, 1903..2015, avg=1986.4, median=1996
"team_id" text: 41 distinct
"league_id" text: "NL"=6203, "AL"=6108
"round" text: "WS"=4340, "NLCS"=2022, "ALCS"=1947, "NLDS2"=944, "ALDS1"=912, "ALDS2"=881, "NLDS1"=873, "ALWC"=129, "NLWC"=110, "NEDIV"=43, "NWDIV"=40, "AEDIV"=38, "AWDIV"=32
"pos" text: "P"=5059, "LF"=1064, "RF"=1021, "C"=976, "1B"=852, "2B"=837, "CF"=837, "3B"=827, "SS"=802, "DH"=34, "OF"=2
"g" int: 1=3554, 2=2514, 3=1996, 4=1514, 5=1321, 6=691, 7=663, 8=54, 9=2, 10=1, 11=1, 1..11
"gs" numeric: 0=4011, 1=2152, 2=1295, 4=1087, 5=1066, 3=1044, 7=612, 6=604, ""=387, 8=53
"inn_outs" numeric: 212 distinct
"po" int: 83 distinct, 0..91, avg=6.44351, median=1
"a" int: 34 distinct, 0..33, avg=2.45821, median=1
"e" int: 0=10517, 1=1404, 2=285, 3=77, 4=18, 5=6, 6=3, 8=1, 0..8
"dp" int: 0=9556, 1=1167, 2=568, 3=436, 4=266, 5=154, 6=94, 7=34, 8=22, 9=9, 10=2, 11=2, 13=1, 0..13
"tp" int: 0=12310, 1=1
"pb" numeric: ""=10960, 0=1188, 1=138, 2=19, 3=6
"sb" numeric: ""=6756, 0=3895, 1=956, 2=368, 3=144, 4=67, 5=48, 6=28, 7=23, 8=9, 9=7, 11=3, 12=3, 15=2, 13=1, 16=1
"cs" numeric: ""=6756, 0=4410, 1=807, 2=187, 3=89, 4=33, 5=14, 6=11, 7=2, 9=1, 10=1

indexes: none

samples:
| column | latest | sample | sample |
|---|---|---|---|
| player_id | zumayjo01 | harvema01 | mabryjo01 |
| year | 2006 | 2015 | 2004 |
| team_id | DET | NYN | SLN |
| league_id | AL | NL | NL |
| round | WS | NLCS | NLCS |
| pos | P | P | LF |
| g | 3 | 1 | 1 |
| gs | 0 |  | 1 |
| inn_outs | 9 | 23 | 12 |
| po | 0 | 0 | 1 |
| a | 0 | 2 | 0 |
| e | 1 | 0 | 0 |
| dp | 0 | 0 | 0 |
| tp | 0 | 0 | 0 |
| pb |  |  |  |
| sb | 0 |  |  |
| cs | 0 |  |  |

# "hall_of_fame"  (rows=4120)

columns:
"player_id" text: 1239 distinct
"yearid" int: 78 distinct, 1936..2016, avg=1968.89, median=1964
"votedby" text: "BBWAA"=3689, "Veterans"=189, "Run Off"=81, "Nominating Vote"=76, "Old Timers"=30, "Negro League"=26, "Final Ballot"=21, "Centennial"=6, "Special Election"=2
"ballots" numeric: 73 distinct
"needed" numeric: 64 distinct
"votes" numeric: 360 distinct
"inducted" text: "N"=3808, "Y"=312
"category" text: "Player"=3997, "Manager"=74, "Pioneer/Executive"=39, "Umpire"=10
"needed_note" text: ""=3963, "1st"=81, "Top 20"=76

indexes: none

samples:
| column | latest | sample | sample |
|---|---|---|---|
| player_id | ziskri01 | wallabo01 | wilsoji01 |
| yearid | 1989 | 1945 | 1960 |
| votedby | BBWAA | BBWAA | BBWAA |
| ballots | 447 | 247 | 269 |
| needed | 336 | 186 | 202 |
| votes | 0 | 3 | 6 |
| inducted | N | N | N |
| category | Player | Player | Player |
| needed_note |  |  |  |

# "home_game"  (rows=2944)

columns:
"year" int: 144 distinct, 1871..2014, avg=1952.11, median=1959
"league_id" text: "NL"=1482, "AL"=1235, "AA"=112, ""=77, "FL"=16, "UA"=14, "PL"=8
"team_id" text: 148 distinct
"park_id" text: 249 distinct
"span_first" text: iso-date, 1052 distinct
"span_last" text: iso-date, 1103 distinct
"games" int: 87 distinct, 1..89, avg=70.804, median=78
"openings" int: 84 distinct, 0..83, avg=48.9412, median=66
"attendance" int: 2388 distinct, 0..4483203, avg=1.1e+06, median=874752

indexes: none

samples:
| column | latest | sample | sample |
|---|---|---|---|
| year | 2014 | 1993 | 1905 |
| league_id | NL | NL | NL |
| team_id | WAS | PIT | CIN |
| park_id | WAS11 | PIT07 | CIN06 |
| span_first | 2014-04-04 | 1993-04-06 | 1905-04-14 |
| span_last | 2014-09-28 | 1993-09-30 | 1905-10-08 |
| games | 81 | 81 | 79 |
| openings | 81 | 79 | 0 |
| attendance | 2579389 | 1652922 | 0 |

# "manager"  (rows=3405)

columns:
"player_id" text: 696 distinct
"year" int: 145 distinct, 1871..2015, avg=1953.66, median=1962
"team_id" text: 149 distinct
"league_id" text: "NL"=1731, "AL"=1431, "AA"=124, ""=67, "FL"=22, "UA"=18, "PL"=12
"inseason" int: 1=2805, 2=458, 3=108, 4=21, 5=8, 6=2, 7=1, 8=1, 9=1, 1..9
"g" int: 165 distinct, 1..165, avg=123.873, median=154
"w" int: 114 distinct, 0..116, avg=61.5789, median=70
"l" int: 118 distinct, 0..120, avg=61.5874, median=68
"rank" numeric: 5=494, 4=482, 3=475, 2=472, 1=435, 6=377, 7=290, 8=248, 10=43, 9=42, 11=25, 12=21, ""=1
"plyr_mgr" text: "N"=2760, "Y"=645

indexes: none

samples:
| column | latest | sample | sample |
|---|---|---|---|
| player_id | zimmedo01 | collite99 | dunlafr01 |
| year | 1991 | 2011 | 1885 |
| team_id | CHN | NYN | SL5 |
| league_id | NL | NL | NL |
| inseason | 1 | 1 | 1 |
| g | 37 | 162 | 50 |
| w | 18 | 77 | 21 |
| l | 19 | 85 | 29 |
| rank | 4 | 4 | 8 |
| plyr_mgr | N | N | Y |

# "manager_award"  (rows=177)

columns:
"player_id" text: 83 distinct
"award_id" text: "TSN Manager of the Year"=110, "BBWAA Manager of the year"=67
"year" int: 80 distinct, 1936..2015, avg=1988.62, median=1994
"league_id" text: "AL"=64, "NL"=63, "ML"=50
"tie" text: ""=175, "Y"=2
"notes" numeric→text: ""=177

indexes: none

samples:
| column | latest | sample | sample |
|---|---|---|---|
| player_id | zimmedo01 | gibsoki01 | martibi02 |
| award_id | TSN Manager of the Year | BBWAA Manager of the year | TSN Manager of the Year |
| year | 1989 | 2011 | 1981 |
| league_id | NL | NL | ML |
| tie |  |  |  |
| notes |  |  |  |

# "manager_award_vote"  (rows=414)

columns:
"award_id" text: "Mgr of the year"=333, "Mgr of the Year"=81
"year" int: 33 distinct, 1983..2015, avg=1999.78, median=2000
"league_id" text: "AL"=213, "NL"=201
"player_id" text: 110 distinct
"points_won" int: 117 distinct, 1..154, avg=39.8792, median=22
"points_max" int: 140=220, 160=102, 120=43, 150=42, 24=4, 28=3, 24..160
"votes_first" int: 30 distinct, 0..30, avg=4.54348, median=1

indexes: none

samples:
| column | latest | sample | sample |
|---|---|---|---|
| award_id | Mgr of the year | Mgr of the Year | Mgr of the year |
| year | 2012 | 2001 | 1998 |
| league_id | NL | AL | NL |
| player_id | mathemi01 | torrejo01 | coxbo01 |
| points_won | 1 | 8 | 17 |
| points_max | 160 | 140 | 160 |
| votes_first | 0 | 0 | 0 |

# "manager_half"  (rows=93)

columns:
"player_id" text: 54 distinct
"year" int: 1981=58, 1892=35
"team_id" text: 33 distinct
"league_id" text: "NL"=60, "AL"=33
"inseason" int: 1=68, 2=17, 3=6, 4=1, 5=1, 1..5
"half" int: 1=48, 2=45
"g" int: 40 distinct, 2..80, avg=49.7849, median=53
"w" int: 42 distinct, 0..53, avg=24.6452, median=25
"l" int: 34 distinct, 2..46, avg=24.6452, median=25
"rank" int: 6=13, 1=12, 4=12, 2=11, 5=10, 3=9, 7=8, 11=5, 12=5, 9=4, 8=2, 10=2, 1..12

indexes: none

samples:
| column | latest | sample | sample |
|---|---|---|---|
| player_id | zimmedo01 | herzowh01 | pfefffr01 |
| year | 1981 | 1981 | 1892 |
| team_id | TEX | SLN | LS3 |
| league_id | AL | NL | NL |
| inseason | 1 | 1 | 2 |
| half | 2 | 2 | 2 |
| g | 50 | 52 | 77 |
| w | 24 | 29 | 33 |
| l | 26 | 23 | 42 |
| rank | 3 | 2 | 9 |

# "park"  (rows=250)

columns:
"park_id" text: unique identifier
"park_name" text: 240 distinct
"park_alias" text: 57 distinct
"city" text: 83 distinct
"state" text: 35 distinct
"country" text: "US"=242, "CA"=4, "AU"=1, "JP"=1, "MX"=1, "PR"=1

indexes: none

samples:
| column | latest | sample | sample |
|---|---|---|---|
| park_id | WOR03 | CHI05 | CHI10 |
| park_name | Worcester Driving Park Grounds | South Side Park I | Comiskey Park I |
| park_alias |  | Cricket Club Grounds; Union Grounds | White Sox Park |
| city | Worcester | Chicago | Chicago |
| state | MA | IL | IL |
| country | US | US | US |

# "pitching"  (rows=44139)

columns:
"player_id" text: 9126 distinct
"year" int: 145 distinct, 1871..2015, avg=1967.79, median=1977
"stint" int: 1=40810, 2=3166, 3=157, 4=6, 1..4
"team_id" text: 149 distinct
"league_id" text: "NL"=22405, "AL"=20620, "AA"=657, "FL"=173, ""=131, "UA"=96, "PL"=57
"w" int: 54 distinct, 0..59, avg=4.74879, median=2
"l" int: 43 distinct, 0..48, avg=4.74877, median=3
"g" int: 94 distinct, 1..106, avg=23.6671, median=22
"gs" int: 75 distinct, 0..75, avg=9.55255, median=3
"cg" int: 74 distinct, 0..75, avg=3.20798, median=0
"sho" int: 0=34507, 1=4711, 2=2268, 3=1215, 4=724, 5=334, 6=192, 7=89, 8=49, 9=23, 10=12, 11=8, 12=3, 13=2, 16=2, 0..16
"sv" int: 57 distinct, 0..62, avg=1.50398, median=0
"ipouts" numeric: 1314 distinct
"h" int: 533 distinct, 0..772, avg=85.5398, median=56
"er" int: 216 distinct, 0..291, avg=36.3211, median=25
"hr" int: 48 distinct, 0..50, avg=6.42722, median=4
"bb" int: 210 distinct, 0..289, avg=30.1218, median=22
"so" int: 339 distinct, 0..513, avg=46.4858, median=31
"baopp" numeric: 426 distinct
"era" numeric: 1157 distinct
"ibb" numeric: 23 distinct
"wp" numeric: 53 distinct
"hbp" numeric: 35 distinct
"bk" int: 0=35083, 1=6476, 2=1644, 3=545, 4=195, 5=91, 6=42, 7=31, 8=13, 9=6, 10=4, 11=4, 12=2, 13=1, 15=1, 16=1, 0..16
"bfp" numeric: 1637 distinct
"gf" numeric: 79 distinct
"r" int: 345 distinct, 0..519, avg=43.3323, median=29
"sh" numeric: 22 distinct
"sf" numeric: ""=32900, 0=3613, 1=2615, 2=1695, 3=1171, 4=759, 5=508, 6=360, 7=232, 8=131, 9=76, 10=48, 11=21, 12=7, 13=2, 14=1
"g_idp" numeric: 28 distinct

indexes: none

samples:
| column | latest | sample | sample |
|---|---|---|---|
| player_id | zychto01 | facero01 | andrena01 |
| year | 2015 | 1959 | 1943 |
| stint | 1 | 1 | 1 |
| team_id | SEA | PIT | BSN |
| league_id | AL | NL | NL |
| w | 0 | 18 | 14 |
| l | 0 | 1 | 20 |
| g | 13 | 57 | 36 |
| gs | 1 | 0 | 34 |
| cg | 0 | 0 | 23 |
| sho | 0 | 0 | 3 |
| sv | 0 | 10 | 0 |
| ipouts | 55 | 280 | 851 |
| h | 17 | 91 | 253 |
| er | 5 | 28 | 81 |
| hr | 1 | 5 | 11 |
| bb | 3 | 25 | 75 |
| so | 24 | 69 | 80 |
| baopp | 0.239 | 0.26 | 0.23 |
| era | 2.45 | 2.7 | 2.57 |
| ibb | 0 | 8 |  |
| wp | 1 | 4 | 4 |
| hbp | 2 | 1 | 6 |
| bk | 0 | 0 | 1 |
| bfp | 76 | 380 | 1167 |
| gf | 4 | 47 | 2 |
| r | 6 | 29 | 100 |
| sh | 0 |  |  |
| sf | 0 |  |  |
| g_idp |  |  |  |

# "pitching_postseason"  (rows=5109)

columns:
"player_id" text: 1673 distinct
"year" int: 119 distinct, 1884..2015, avg=1987.57, median=1998
"round" text: "WS"=1737, "NLCS"=839, "ALCS"=800, "NLDS2"=409, "ALDS1"=404, "NLDS1"=399, "ALDS2"=383, "ALWC"=39, "NLWC"=34, "NEDIV"=17, "AEDIV"=16, "NWDIV"=16, "AWDIV"=10, "CS"=6
"team_id" text: 48 distinct
"league_id" text: "NL"=2610, "AL"=2477, "AA"=22
"w" int: 0=3817, 1=1079, 2=192, 3=16, 4=5, 0..4
"l" int: 0=3759, 1=1179, 2=162, 3=8, 4=1, 0..4
"g" int: 1=2194, 2=1687, 3=838, 4=288, 5=83, 6=17, 7=1, 8=1, 1..8
"gs" int: 0=2934, 1=1399, 2=682, 3=78, 4=7, 5=7, 6=1, 8=1, 0..8
"cg" int: 0=4648, 1=331, 2=89, 3=26, 4=9, 5=4, 6=1, 8=1, 0..8
"sho" int: 0=4973, 1=131, 2=4, 3=1, 0..3
"sv" int: 0=4716, 1=262, 2=100, 3=28, 4=3, 0..4
"ipouts" int: 90 distinct, 0..213, avg=16.1491, median=12
"h" int: 39 distinct, 0..64, avg=4.92171, median=4
"er" int: 20 distinct, 0..26, avg=2.11118, median=1
"hr" int: 0=3314, 1=1255, 2=378, 3=127, 4=28, 5=7, 0..5
"bb" int: 0=1385, 1=1318, 2=955, 3=595, 4=344, 5=203, 6=124, 7=63, 8=58, 9=28, 10=16, 11=10, 12=2, 13=2, 14=2, 15=1, 16=1, 18=1, 32=1, 0..32
"so" int: 31 distinct, 0..35, avg=3.83852, median=3
"baopp" text: numeric, 221 distinct
"era" numeric: 326 distinct
"ibb" numeric: 0=4151, 1=761, 2=125, ""=50, 3=18, 4=4
"wp" numeric: 0=4418, 1=553, 2=77, ""=50, 3=9, 4=1, 5=1
"hbp" numeric: 0=4335, 1=645, 2=68, ""=50, 3=11
"bk" numeric: 0=4818, ""=225, 1=66
"bfp" numeric: 109 distinct
"gf" int: 0=3501, 1=1073, 2=325, 3=156, 4=46, 5=6, 6=2, 0..6
"r" int: 28 distinct, 0..36, avg=2.41319, median=2
"sh" numeric: 0=3423, 1=761, ""=711, 2=154, 3=43, 4=9, 5=6, 6=1, 7=1
"sf" numeric: 0=3868, ""=711, 1=482, 2=43, 3=4, 4=1
"g_idp" numeric: 0=3601, 1=1086, 2=289, 3=66, ""=50, 4=12, 5=3, 6=2

indexes: none

samples:
| column | latest | sample | sample |
|---|---|---|---|
| player_id | zumayjo01 | wendetu01 | mainejo01 |
| year | 2006 | 2000 | 2006 |
| round | WS | WS | NLDS1 |
| team_id | DET | NYN | NYN |
| league_id | AL | NL | NL |
| w | 0 | 0 | 0 |
| l | 1 | 1 | 0 |
| g | 3 | 2 | 1 |
| gs | 0 | 0 | 1 |
| cg | 0 | 0 | 0 |
| sho | 0 | 0 | 0 |
| sv | 0 | 0 | 0 |
| ipouts | 9 | 5 | 13 |
| h | 1 | 3 | 6 |
| er | 1 | 1 | 1 |
| hr | 0 | 0 | 0 |
| bb | 3 | 2 | 2 |
| so | 3 | 2 | 5 |
| baopp | 0.09 | 0.37 | 0.37 |
| era | 3 | 5.4 | 2.08 |
| ibb | 0 | 1 | 1 |
| wp | 1 | 0 | 0 |
| hbp | 0 | 0 | 0 |
| bk | 0 | 0 | 0 |
| bfp | 14 | 10 | 19 |
| gf | 2 | 1 | 0 |
| r | 3 | 1 | 1 |
| sh | 0 | 0 | 1 |
| sf | 0 | 0 | 0 |
| g_idp | 0 | 0 | 0 |

# "player"  (rows=18846)

columns:
"player_id" text: unique identifier
"birth_year" numeric: 166 distinct
"birth_month" numeric: 8=1808, 10=1740, 9=1636, 1=1612, 11=1596, 12=1534, 3=1511, 7=1480, 4=1427, 5=1424, 2=1413, 6=1350, ""=315
"birth_day" numeric: 32 distinct
"birth_country" text: 53 distinct
"birth_state" text: 246 distinct
"birth_city" text: 4714 distinct
"death_year" numeric: 146 distinct
"death_month" numeric: ""=9511, 1=864, 12=828, 10=823, 3=816, 4=815, 11=810, 5=771, 2=747, 9=745, 8=711, 7=709, 6=696
"death_day" numeric: 32 distinct
"death_country" text: 24 distinct
"death_state" text: 93 distinct
"death_city" text: 2554 distinct
"name_first" text: 2313 distinct
"name_last" text: 9713 distinct
"name_given" text: 12437 distinct
"weight" numeric: 132 distinct
"height" numeric: 23 distinct
"bats" text: "R"=11615, "L"=4877, ""=1191, "B"=1163
"throws" text: "R"=14272, "L"=3596, ""=978
"debut" text: iso-date, 10037 distinct
"final_game" text: iso-date, 9029 distinct
"retro_id" text: 18793 distinct
"bbref_id" text: unique identifier

indexes: none

samples:
| column | latest | sample | sample |
|---|---|---|---|
| player_id | zychto01 | randajo01 | harpete01 |
| birth_year | 1990 | 1969 | 1955 |
| birth_month | 8 | 12 | 8 |
| birth_day | 7 | 18 | 19 |
| birth_country | USA | USA | USA |
| birth_state | IL | WI | GA |
| birth_city | Monee | Milwaukee | Douglasville |
| death_year |  |  |  |
| death_month |  |  |  |
| death_day |  |  |  |
| death_country |  |  |  |
| death_state |  |  |  |
| death_city |  |  |  |
| name_first | Tony | Joe | Terry |
| name_last | Zych | Randa | Harper |
| name_given | Anthony Aaron | Joseph Gregory | Terry Joe |
| weight | 190 | 190 | 195 |
| height | 75 | 71 | 76 |
| bats | R | R | R |
| throws | R | R | R |
| debut | 2015-09-04 | 1995-04-30 | 1980-09-12 |
| final_game | 2015-10-03 | 2006-10-01 | 1987-10-02 |
| retro_id | zycht001 | randj002 | harpt001 |
| bbref_id | zychto01 | randajo01 | harpete01 |

# "player_award"  (rows=6078)

columns:
"player_id" text: 1323 distinct
"award_id" text: 27 distinct
"year" int: 117 distinct, 1877..2015, avg=1968.46, median=1974
"league_id" text: "AL"=2413, "NL"=2378, "ML"=1285, "AA"=2
"tie" text: ""=6033, "Y"=45
"notes" text: 29 distinct

indexes: none

samples:
| column | latest | sample | sample |
|---|---|---|---|
| player_id | zitoba01 | robinbr01 | garvest01 |
| award_id | TSN Pitcher of the Year | Gold Glove | Roberto Clemente Award |
| year | 2002 | 1972 | 1981 |
| league_id | AL | AL | ML |
| tie |  |  |  |
| notes |  | 3B |  |

# "player_award_vote"  (rows=6795)

columns:
"award_id" text: "MVP"=5215, "Rookie of the Year"=816, "Cy Young"=764
"year" int: 97 distinct, 1911..2015, avg=1971.92, median=1974
"league_id" text: "AL"=3405, "NL"=3350, "ML"=40
"player_id" text: 2412 distinct
"points_won" numeric: 347 distinct, 0..448, avg=43.3476, median=12
"points_max" int: 21 distinct, 16..448, avg=266.878, median=336
"votes_first" numeric: 40 distinct

indexes: none

samples:
| column | latest | sample | sample |
|---|---|---|---|
| award_id | Rookie of the Year | MVP | MVP |
| year | 2015 | 1911 | 1944 |
| league_id | NL | AL | NL |
| player_id | syndeno01 | austiji01 | holmeto01 |
| points_won | 16 | 2 | 6 |
| points_max | 150 | 64 | 336 |
| votes_first | 0 | 0 | 0 |

# "player_college"  (rows=17350)

columns:
"player_id" text: 6575 distinct
"college_id" text: 1038 distinct
"year" int: 151 distinct, 1864..2014, avg=1969.49, median=1981

indexes: none

samples:
| column | latest | sample | sample |
|---|---|---|---|
| player_id | zuvelpa01 | lankffr01 | firovda01 |
| college_id | stanford | virginia | txcoast |
| year | 1980 | 1991 | 1977 |

# "postseason"  (rows=307)

columns:
"year" int: 119 distinct, 1884..2015, avg=1981.37, median=1995
"round" text: "WS"=118, "ALCS"=46, "NLCS"=46, "ALDS1"=21, "ALDS2"=21, "NLDS1"=21, "NLDS2"=21, "ALWC"=4, "NLWC"=4, "AEDIV"=1, "AWDIV"=1, "CS"=1, "NEDIV"=1, "NWDIV"=1
"team_id_winner" text: 43 distinct
"league_id_winner" text: "AL"=158, "NL"=148, "AA"=1
"team_id_loser" text: 45 distinct
"league_id_loser" text: "NL"=160, "AL"=141, "AA"=6
"wins" int: 4=168, 3=123, 1=8, 5=5, 6=2, 10=1, 1..10
"losses" int: 2=86, 0=82, 1=78, 3=59, 4=1, 5=1, 0..5
"ties" int: 0=304, 1=3

indexes: none

samples:
| column | latest | sample | sample |
|---|---|---|---|
| year | 2015 | 1922 | 1909 |
| round | WS | WS | WS |
| team_id_winner | KCA | NY1 | PIT |
| league_id_winner | AL | NL | NL |
| team_id_loser | NYN | NYA | DET |
| league_id_loser | NL | AL | AL |
| wins | 4 | 4 | 4 |
| losses | 1 | 0 | 3 |
| ties | 0 | 0 | 0 |

# "salary"  (rows=25575)

columns:
"year" int: 31 distinct, 1985..2015, avg=2000.37, median=2000
"team_id" text: 35 distinct
"league_id" text: "NL"=13037, "AL"=12538
"player_id" text: 4963 distinct
"salary" int: 3266 distinct, 0..33000000, avg=2e+06, median=550000

indexes: none

samples:
| column | latest | sample | sample |
|---|---|---|---|
| year | 2015 | 1997 | 1989 |
| team_id | WAS | SDN | TOR |
| league_id | NL | NL | AL |
| player_id | zimmery01 | ashbyan01 | henketo01 |
| salary | 14000000 | 3400000 | 975000 |

# "team"  (rows=2805)

columns:
"year" int: 145 distinct, 1871..2015, avg=1955.04, median=1963
"league_id" text: "NL"=1429, "AL"=1205, "AA"=85, ""=50, "FL"=16, "UA"=12, "PL"=8
"team_id" text: 149 distinct
"franchise_id" text: 120 distinct
"div_id" text: ""=1517, "E"=538, "W"=515, "C"=235
"rank" int: 2=422, 4=414, 1=412, 3=412, 5=388, 6=294, 7=207, 8=174, 9=31, 10=26, 11=13, 12=10, 13=2, 1..13
"g" int: 122 distinct, 6..165, avg=150.348, median=157
"ghome" numeric: 39 distinct
"w" int: 112 distinct, 0..116, avg=74.749, median=77
"l" int: 113 distinct, 4..134, avg=74.749, median=76
"div_win" text: ""=1545, "N"=1030, "Y"=230
"wc_win" text: ""=2181, "N"=574, "Y"=50
"lg_win" text: "N"=2505, "Y"=272, ""=28
"ws_win" text: "N"=2332, ""=357, "Y"=116
"r" int: 612 distinct, 24..1220, avg=681.946, median=690
"ab" int: 1096 distinct, 211..5781, avg=5142.49, median=5389
"h" int: 730 distinct, 33..1783, avg=1346.27, median=1393
"double" int: 312 distinct, 3..376, avg=227.625, median=231
"triple" int: 122 distinct, 0..150, avg=47.1041, median=41
"hr" int: 246 distinct, 0..264, avg=101.137, median=107
"bb" int: 566 distinct, 0..835, avg=473.649, median=493
"so" numeric: 1028 distinct
"sb" numeric: 324 distinct
"cs" numeric: 139 distinct
"hbp" numeric: 65 distinct
"sf" numeric: 47 distinct
"ra" int: 608 distinct, 34..1252, avg=681.946, median=688
"er" int: 630 distinct, 25..1023, avg=570.895, median=590
"era" numeric: 385 distinct, 1.22..8, avg=3.81497, median=3.82
"cg" int: 147 distinct, 0..148, avg=50.4809, median=45
"sho" int: 32 distinct, 0..32, avg=9.66417, median=9
"sv" int: 66 distinct, 0..68, avg=23.6677, median=24
"ipouts" int: 638 distinct, 162..4518, avg=4022.38, median=4236
"ha" int: 743 distinct, 49..1993, avg=1346.08, median=1392
"hra" int: 232 distinct, 0..241, avg=101.137, median=109
"bba" int: 566 distinct, 0..827, avg=474.011, median=494
"soa" int: 1050 distinct, 0..1450, avg=731.229, median=735
"e" int: 446 distinct, 47..639, avg=186.337, median=145
"dp" numeric: 168 distinct
"fp" numeric: 37 distinct, 0.76..0.991, avg=0.961519, median=0.97
"name" text: 139 distinct
"park" text: 213 distinct
"attendance" numeric: 2519 distinct
"bpf" int: 43 distinct, 60..129, avg=100.2, median=100
"ppf" int: 42 distinct, 60..141, avg=100.226, median=100
"team_id_br" text: 101 distinct
"team_id_lahman45" text: 148 distinct
"team_id_retro" text: 149 distinct

indexes: none

samples:
| column | latest | sample | sample |
|---|---|---|---|
| year | 2015 | 1964 | 1986 |
| league_id | NL | AL | NL |
| team_id | WAS | CLE | SDN |
| franchise_id | WSN | CLE | SDP |
| div_id | E |  | W |
| rank | 2 | 6 | 4 |
| g | 162 | 164 | 162 |
| ghome | 81 | 82 | 81 |
| w | 83 | 79 | 74 |
| l | 79 | 83 | 88 |
| div_win | N |  | N |
| wc_win | N |  |  |
| lg_win | N | N | N |
| ws_win | N | N | N |
| r | 703 | 689 | 656 |
| ab | 5428 | 5603 | 5515 |
| h | 1363 | 1386 | 1442 |
| double | 265 | 208 | 239 |
| triple | 13 | 22 | 25 |
| hr | 177 | 164 | 136 |
| bb | 539 | 500 | 484 |
| so | 1344 | 1063 | 917 |
| sb | 57 | 79 | 96 |
| cs | 23 | 51 | 68 |
| hbp | 44 |  |  |
| sf | 51 |  |  |
| ra | 635 | 693 | 723 |
| er | 577 | 620 | 640 |
| era | 3.62 | 3.75 | 3.99 |
| cg | 4 | 37 | 13 |
| sho | 13 | 16 | 7 |
| sv | 41 | 37 | 32 |
| ipouts | 4304 | 4461 | 4329 |
| ha | 1366 | 1443 | 1406 |
| hra | 145 | 154 | 150 |
| bba | 364 | 565 | 607 |
| soa | 1342 | 1162 | 934 |
| e | 90 | 118 | 135 |
| dp | 125 | 149 | 135 |
| fp | 0.985 | 0.98 | 0.97 |
| name | Washington Nationals | Cleveland Indians | San Diego Padres |
| park | Nationals Park | Cleveland Stadium | Jack Murphy Stadium |
| attendance | 2619843 | 653293 | 1805716 |
| bpf | 102 | 99 | 98 |
| ppf | 99 | 99 | 98 |
| team_id_br | WSN | CLE | SDP |
| team_id_lahman45 | MON | CLE | SDN |
| team_id_retro | WAS | CLE | SDN |

# "team_franchise"  (rows=120)

columns:
"franchise_id" text: unique identifier
"franchise_name" text: 99 distinct
"active" text: "N"=65, "Y"=30, ""=25
"na_assoc" text: ""=108, "ATH"=1, "ATL"=1, "BNA"=1, "CHC"=1, "CNA"=1, "HAR"=1, "HNA"=1, "NNA"=1, "NYU"=1, "PNA"=1, "SBS"=1, "SNA"=1

indexes: none

samples:
| column | latest | sample | sample |
|---|---|---|---|
| franchise_id | WST | WNL | KCC |
| franchise_name | Washington Statesmen | Washington Nationals | Kansas City Cowboys |
| active | N | N | N |
| na_assoc |  |  |  |

# "team_half"  (rows=52)

columns:
"year" int: 1981=52
"league_id" text: "AL"=28, "NL"=24
"team_id" text: 26 distinct
"half" int: 1=26, 2=26
"div_id" text: "E"=26, "W"=26
"div_win" text: "N"=52
"rank" int: 2=9, 5=9, 6=9, 1=8, 4=8, 3=7, 7=2, 1..7
"g" int: 52=10, 53=9, 56=6, 50=5, 51=4, 54=4, 57=4, 55=3, 48=2, 60=2, 49=1, 58=1, 59=1, 48..60
"w" int: 20 distinct, 15..37, avg=26.7115, median=27
"l" int: 23=10, 22=5, 26=5, 29=5, 21=4, 27=4, 30=3, 20=2, 25=2, 28=2, 33=2, 36=2, 24=1, 32=1, 34=1, 37=1, 39=1, 42=1, 20..42

indexes: none

samples:
| column | latest | sample | sample |
|---|---|---|---|
| year | 1981 | 1981 | 1981 |
| league_id | NL | NL | NL |
| team_id | SLN | HOU | ATL |
| half | 2 | 2 | 1 |
| div_id | E | W | W |
| div_win | N | N | N |
| rank | 2 | 1 | 4 |
| g | 52 | 53 | 54 |
| w | 29 | 33 | 25 |
| l | 23 | 20 | 29 |
