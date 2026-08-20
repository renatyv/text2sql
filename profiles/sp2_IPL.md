---
generator: db-snooper
version: 0.0.31
generated_at_utc: 2026-08-20T17:28:08.718562Z
dialect: sqlite
database: /var/folders/9j/b9bx_drd53sc6zbpsqyrjy4h0000gn/T/dbsnoop-eujbdprk/IPL.sqlite
schema: main
---

# "ball_by_ball"  (rows=134703)

columns:
"match_id" int PK: 568 distinct, 335987..981024
"over_id" int PK: 20 distinct, 1..20
"ball_id" int PK: 1=21831, 2=21782, 3=21718, 4=21666, 5=21597, 6=21526, 7=3878, 8=607, 9=98, 1..9
"innings_no" int PK: 1=69691, 2=65012
"team_batting" int: 1..13, avg=5.182
"team_bowling" int: 1..13, avg=5.17173
"striker_batting_position" int: 1..11, avg=3.58602
"striker" int: 1..434, avg=126.382
"non_striker" int: 1..451, avg=125.726
"bowler" int: 1..465, avg=180.118

indexes: none
fk: none

samples:
| column | latest | sample | sample |
|---|---|---|---|
| match_id | 981024 | 419112 | 598024 |
| over_id | 20 | 10 | 4 |
| ball_id | 6 | 2 | 3 |
| innings_no | 2 | 2 | 2 |
| team_batting | 2 | 5 | 7 |
| team_bowling | 11 | 7 | 5 |
| striker_batting_position | 9 | 3 | 3 |
| striker | 140 | 211 | 88 |
| non_striker | 369 | 31 | 57 |
| bowler | 299 | 194 | 297 |

# "batsman_scored"  (rows=131259)

columns:
"match_id" int PK: 568 distinct, 335987..981024
"over_id" int PK: 20 distinct, 1..20
"ball_id" int PK: 2=21217, 1=21196, 3=21191, 4=21150, 5=21068, 6=20997, 7=3759, 8=584, 9=97, 1..9
"runs_scored" int: 0..6, avg=1.247
"innings_no" int PK: 1=67949, 2=63310

indexes: none
fk: none

samples:
| column | latest | sample | sample |
|---|---|---|---|
| match_id | 981024 | 980906 | 335991 |
| over_id | 20 | 1 | 16 |
| ball_id | 6 | 6 | 6 |
| runs_scored | 4 | 4 | 2 |
| innings_no | 2 | 2 | 1 |

# "extra_runs"  (rows=7349)

columns:
"match_id" int PK: 568 distinct, 335987..981024, 829742=26, 336023=25, 548382=25, 335987=24, 335991=24, 392197=24, 419130=24, 501215=24, 501232=24, 501265=24
"over_id" int PK: 20 distinct, 1..20, 1=508, 2=499, 3=437, 17=435, 4=412, 20=411, 19=399, 18=394, 6=387, 5=374
"ball_id" int PK: 1=1255, 3=1228, 2=1219, 6=1133, 5=1121, 4=1098, 7=249, 8=45, 9=1, 1..9
"extra_type" text: "wides"=4091, "legbyes"=2317, "noballs"=567, "byes"=373, "penalty"=1
"extra_runs" int: 1=6499, 2=335, 4=273, 5=192, 3=50, 1..5
"innings_no" int PK: 1=3808, 2=3541

indexes: none
fk: none

samples:
| column | latest | sample | sample |
|---|---|---|---|
| match_id | 981024 | 980970 | 335993 |
| over_id | 20 | 10 | 10 |
| ball_id | 4 | 5 | 1 |
| extra_type | legbyes | wides | wides |
| extra_runs | 1 | 1 | 1 |
| innings_no | 2 | 1 | 1 |

# "match"  (rows=567)

columns:
"match_id" int PK: unique identifier, 335987..981024
"team_1" int: 2=75, 3=73, 6=67, 4=65, 7=62, 1=60, 5=51, 8=39, 11=29, 10=23, 13=9, 9=7, 12=7, 1..13
"team_2" int: 7=78, 1=69, 4=67, 5=63, 6=62, 2=60, 3=57, 8=36, 11=32, 10=22, 9=7, 12=7, 13=7, 1..13
"match_date" date: 403 distinct
"season_id" int: 5=74, 6=74, 4=72, 9=60, 7=59, 1=58, 3=58, 2=56, 8=56, 1..9
"venue" text: 35 distinct
"toss_winner" int: 7=74, 1=68, 3=65, 4=63, 6=62, 5=61, 2=58, 8=43, 11=30, 10=20, 9=8, 13=8, 12=7, 1..13
"toss_decision" text: "field"=309, "bat"=258
"win_type" text: "wickets"=307, "runs"=260
"win_margin" int: 81 distinct, 1..144, avg=17.3104, median=8
"outcome_type" text: "Result"=567
"match_winner" int: 7=80, 3=79, 2=69, 1=68, 4=61, 5=61, 6=55, 11=33, 8=29, 10=12, 13=9, 9=6, 12=5, 1..13
"man_of_the_match" int: 186 distinct, 1..460, avg=139.376, median=105

indexes: none
fk: none

samples:
| column | latest | sample | sample |
|---|---|---|---|
| match_id | 981024 | 501244 | 729296 |
| team_1 | 2 | 8 | 5 |
| team_2 | 11 | 1 | 4 |
| match_date | 2016-05-29 | 2011-05-03 | 2014-04-20 |
| season_id | 9 | 4 | 7 |
| venue | M Chinnaswamy Stadium | Rajiv Gandhi International Stadium Uppal | Sharjah Cricket Stadium |
| toss_winner | 11 | 8 | 4 |
| toss_decision | bat | field | field |
| win_type | runs | runs | wickets |
| win_margin | 8 | 20 | 7 |
| outcome_type | Result | Result | Result |
| match_winner | 11 | 1 | 4 |
| man_of_the_match | 385 | 31 | 305 |

# "player"  (rows=468)

columns:
"player_id" int PK: unique identifier, 1..469
"player_name" text: all distinct
"dob" date: 454 distinct
"batting_hand" text: "Right-hand bat"=343, "Left-hand bat"=125
"bowling_skill" text: "Right-arm medium"=147, "Right-arm offbreak"=81, "Right-arm fast-medium"=53, "Slow left-arm orthodox"=43, "Right-arm medium-fast"=38, "Legbreak"=24, "Legbreak googly"=21, "Right-arm fast"=20, "Left-arm fast-medium"=13, "Left-arm medium"=11, "Left-arm medium-fast"=8, "Slow left-arm chinaman"=5, "Left-arm fast"=3, "Right-arm bowler"=1
"country_name" text: "India"=261, "Australia"=72, "South Africa"=39, "New Zealand"=22, "Sri Lanka"=20, "West Indies"=19, "England"=14, "Pakistan"=13, "Bangladesh"=5, "Zimbabwea"=2, "Netherlands"=1

indexes: none
fk: none

samples:
| column | latest | sample | sample |
|---|---|---|---|
| player_id | 469 | 294 | 141 |
| player_name | T Mishra | P Parameswaran | Younis Khan |
| dob | 1986-12-22 | 1985-05-30 | 1977-11-29 |
| batting_hand | Right-hand bat | Right-hand bat | Right-hand bat |
| bowling_skill | Right-arm fast-medium | Left-arm medium | Right-arm medium |
| country_name | India | India | Pakistan |

# "player_match"  (rows=12495)

columns:
"match_id" int PK: 568 distinct, 335987..981024, 335987=22, 335988=22, 335989=22, 335990=22, 335991=22, 335992=22, 335993=22, 335994=22, 335995=22, 335996=22
"player_id" int PK: 468 distinct, 1..469, 21=145, 20=142, 57=142, 88=136, 8=134, 31=133, 46=133, 40=130, 50=125, 35=124
"role" text: "Player"=10471, "Keeper"=889, "Captain"=888, "CaptainKeeper"=247
"team_id" int: 7=1540, 2=1485, 4=1452, 3=1430, 6=1430, 1=1429, 5=1254, 8=825, 11=671, 10=495, 13=176, 9=154, 12=154, 1..13

indexes: none
fk: none

samples:
| column | latest | sample | sample |
|---|---|---|---|
| match_id | 981024 | 734002 | 829748 |
| player_id | 460 | 333 | 46 |
| role | Player | Player | Keeper |
| team_id | 11 | 4 | 1 |

# "team"  (rows=12)

columns:
"team_id" int PK: unique identifier, 2..13
"name" text: "Chennai Super Kings"=1, "Deccan Chargers"=1, "Delhi Daredevils"=1, "Gujarat Lions"=1, "Kings XI Punjab"=1, "Kochi Tuskers Kerala"=1, "Mumbai Indians"=1, "Pune Warriors"=1, "Rajasthan Royals"=1, "Rising Pune Supergiants"=1, "Royal Challengers Bangalore"=1, "Sunrisers Hyderabad"=1

indexes: none
fk: none

samples:
| column | latest | sample | sample |
|---|---|---|---|
| team_id | 13 | 11 | 13 |
| name | Gujarat Lions | Sunrisers Hyderabad | Gujarat Lions |

# "wicket_taken"  (rows=6618)

columns:
"match_id" int PK: 568 distinct, 335987..981024, 419146=20, 335996=19, 336043=19, 729312=19, 733994=19, 829784=19, 980960=19, 336009=18, 392187=18, 392211=18
"over_id" int PK: 20 distinct, 1..20, 20=667, 19=527, 18=498, 17=404, 16=370, 15=336, 14=310, 11=298, 5=295, 3=291
"ball_id" int PK: 4=1123, 6=1094, 2=1089, 5=1060, 3=1057, 1=983, 7=185, 8=24, 9=3, 1..9
"player_out" int: 411 distinct, 1..438, avg=137.332, median=97
"kind_out" text: "caught"=3894, "bowled"=1234, "run out"=677, "lbw"=393, "stumped"=219, "caught and bowled"=184, "hit wicket"=8, "retired hurt"=8, "obstructing the field"=1
"innings_no" int PK: 1=3447, 2=3171

indexes: none
fk: none

samples:
| column | latest | sample | sample |
|---|---|---|---|
| match_id | 981024 | 829802 | 392197 |
| over_id | 20 | 19 | 16 |
| ball_id | 3 | 5 | 4 |
| player_out | 434 | 310 | 97 |
| kind_out | run out | caught | run out |
| innings_no | 2 | 2 | 1 |
