---
generator: db-snooper
version: 0.0.34
generated_at_utc: 2026-08-24T21:21:28.846771Z
dialect: sqlite
database: /var/folders/9j/b9bx_drd53sc6zbpsqyrjy4h0000gn/T/dbsnoop-rw94_61t/BowlingLeague.sqlite
schema: main
---

## Relationships

- "Bowlers"."BowlerID" ← "Bowler_Scores"."BowlerID"
- "Match_Games".("MatchID", "GameNumber") ← "Bowler_Scores".("MatchID", "GameNumber")
- "Match_Games_Archive".("MatchID", "GameNumber") ← "Bowler_Scores_Archive".("MatchID", "GameNumber")
- "Teams"."TeamID" ← "Bowlers"."TeamID", "Tourney_Matches"."EvenLaneTeamID", "Tourney_Matches"."OddLaneTeamID"
- "Tournaments"."TourneyID" ← "Tourney_Matches"."TourneyID"
- "Tournaments_Archive"."TourneyID" ← "Tourney_Matches_Archive"."TourneyID"

# "Bowler_Scores"  (rows=1344)

columns:
"MatchID" int PK: 56 distinct, 1..56, avg=28.5, median=28.5
"GameNumber" smallint PK: 1=448, 2=448, 3=448, 1..3
"BowlerID" int PK FK: 32 distinct, 1..32, avg=16.5, median=16.5
"RawScore" smallint: 61 distinct, 135..195, avg=154.507, median=150
"HandiCapScore" smallint: 70 distinct, 161..231, avg=195.332, median=195
"WonGame" bool NOTNULL: 1=695, 0=649

indexes: "BowlerID", ("MatchID","GameNumber")

samples:
| column | latest | sample | sample |
|---|---|---|---|
| MatchID | 56 | 6 | 39 |
| GameNumber | 3 | 1 | 1 |
| BowlerID | 32 | 5 | 12 |
| RawScore | 148 | 164 | 145 |
| HandiCapScore | 200 | 211 | 196 |
| WonGame | true | true | false |

# "Bowlers"  (rows=34)

columns:
"BowlerID" int PK: unique identifier, 1..34, avg=17.5, median=17.5
"BowlerLastName" text: "Patterson"=7, "Viescas"=7, "Hallmark"=4, "Thompson"=3, "Fournier"=2, "Hernandez"=2, "Kennedy"=2, "Sheskey"=2, "Black"=1, "Clothier"=1, "Cunningham"=1, "Ehrlich"=1, "Rosales"=1
"BowlerFirstName" text: 30 distinct
"BowlerMiddleInit" text: "L"=4, "A"=2, "K"=2, "G"=1, "J"=1, "M"=1, nulls=23
"BowlerAddress" text: "16 Maple Lane"=7, "Route 2, Box 203B"=4, "122 Spring Valley Drive"=3, "16679 NE 42nd Court"=3, "218 Main Street"=3, "17950 N 59th"=2, "2957 W 33rd"=2, "47 Harvard Drive"=2, "67 Willow Drive"=2, "16345 NE 32nd Street"=1, "4110 Old Redmond Rd."=1, "4726 - 11th Ave. N.E."=1, "507 - 20th Ave. E."=1, "722 Moss Bay Blvd."=1, "908 W. Capital Way"=1
"BowlerCity" text: "Auburn"=7, "Redmond"=7, "Seattle"=4, "Woodinville"=4, "Duvall"=3, "Kirkland"=3, "Ballard"=2, "Bothell"=2, "Bellevue"=1, "Tacoma"=1
"BowlerState" text: "WA"=34
"BowlerZip" text: "98002"=7, "98052"=7, "98072"=4, "98019"=3, "98033"=3, "98011"=2, "98014"=2, "98154"=2, "98004"=1, "98105"=1, "98122"=1, "98404"=1
"BowlerPhoneNumber" text: "(206) 555-3487"=7, "(206) 555-8990"=4, "(206) 555-8989"=3, "(206) 881-5596"=3, "(206) 882-8878"=3, "(206) 555-7854"=2, "(206) 555-9876"=2, "(206) 555-9893"=2, "(206) 889-9191"=2, "(206) 555-1189"=1, "(206) 555-3412"=1, "(206) 555-7295"=1, "(206) 555-8122"=1, "(206) 555-9482"=1, "(206) 555-9857"=1
"TeamID" int FK: 7=6, 1=4, 2=4, 3=4, 4=4, 5=4, 6=4, 8=4, 1..8
"BowlerTotalPins" int: 33 distinct, 0..6607, avg=5676.12, median=6022
"BowlerGamesBowled" int: 39=32, 0=2
"BowlerCurrentAverage" smallint: 143=4, 157=4, 142=3, 150=3, 158=3, 169=3, 0=2, 148=2, 165=2, 149=1, 151=1, 152=1, 159=1, 162=1, 163=1, 164=1, 167=1, 0..169
"BowlerCurrentHcp" smallint: 39=4, 51=4, 28=3, 32=3, 38=3, 45=3, 52=3, 0=2, 47=2, 30=1, 33=1, 34=1, 37=1, 43=1, 44=1, 46=1, 0..52

indexes: "BowlerLastName", "TeamID"

samples:
| column | latest | sample | sample |
|---|---|---|---|
| BowlerID | 34 | 10 | 8 |
| BowlerLastName | Patterson | Cunningham | Viescas |
| BowlerFirstName | Maria | David | Stephanie |
| BowlerMiddleInit | null | null | null |
| BowlerAddress | 16 Maple Lane | 4110 Old Redmond Rd. | 16679 NE 42nd Court |
| BowlerCity | Auburn | Redmond | Redmond |
| BowlerState | WA | WA | WA |
| BowlerZip | 98002 | 98052 | 98052 |
| BowlerPhoneNumber | (206) 555-3487 | (206) 555-8122 | (206) 882-8878 |
| TeamID | 7 | 3 | 2 |
| BowlerTotalPins | 0 | 6184 | 5558 |
| BowlerGamesBowled | 0 | 39 | 39 |
| BowlerCurrentAverage | 0 | 159 | 143 |
| BowlerCurrentHcp | 0 | 37 | 51 |

# "Match_Games"  (rows=168)

columns:
"MatchID" int PK: 56 distinct, 1..56, avg=28.5, median=28.5
"GameNumber" smallint PK: 1=56, 2=56, 3=56, 1..3
"WinningTeamID" int: 1=21, 2=21, 3=21, 4=21, 5=21, 6=21, 7=21, 8=21, 1..8

indexes: "WinningTeamID", "MatchID"

samples:
| column | latest | sample | sample |
|---|---|---|---|
| MatchID | 56 | 55 | 42 |
| GameNumber | 3 | 1 | 1 |
| WinningTeamID | 8 | 6 | 2 |

# "Teams"  (rows=10)

columns:
"TeamID" int PK
"TeamName" text NOTNULL
"CaptainID" int

indexes: none

all rows:
| column | row 1 | row 2 | row 3 | row 4 | row 5 | row 6 | row 7 | row 8 | row 9 | row 10 |
|---|---|---|---|---|---|---|---|---|---|---|
| TeamID | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9 | 10 |
| TeamName | Marlins | Sharks | Terrapins | Barracudas | Dolphins | Orcas | Manatees | Swordfish | Huckleberrys | Never Show Ups |
| CaptainID | 2 | 5 | 12 | 16 | 20 | 24 | 28 | 32 | 7 | 22 |

# "Tournaments"  (rows=20)

columns:
"TourneyID" int PK: unique identifier, 1..20, avg=10.5, median=10.5
"TourneyDate" date: all distinct
"TourneyLocation" text: "Bolero Lanes"=3, "Imperial Lanes"=3, "Red Rooster Lanes"=3, "Sports World Lanes"=3, "Thunderbird Lanes"=3, "Totem Lanes"=3, "Acapulco Lanes"=2

indexes: none

samples:
| column | latest | sample | sample |
|---|---|---|---|
| TourneyID | 20 | 19 | 17 |
| TourneyDate | 2018-08-16 | 2018-08-09 | 2018-07-26 |
| TourneyLocation | Totem Lanes | Imperial Lanes | Bolero Lanes |

# "Tourney_Matches"  (rows=57)

columns:
"MatchID" int PK: unique identifier, 1..57, avg=29, median=29
"TourneyID" int FK: 11=5, 1=4, 2=4, 3=4, 4=4, 5=4, 6=4, 7=4, 8=4, 9=4, 10=4, 12=4, 13=4, 14=4, 1..14
"Lanes" text: "15-16"=8, "11-12"=6, "13-14"=6, "17-18"=6, "19-20"=5, "05-06"=4, "07-08"=4, "09-10"=4, "21-22"=4, "01-02"=2, "03-04"=2, "23-24"=2, "25-26"=2, "27-28"=2
"OddLaneTeamID" int FK: 1=7, 2=7, 3=7, 4=7, 5=7, 6=7, 7=7, 8=7, 10=1, 1..10
"EvenLaneTeamID" int FK: 1=7, 2=7, 3=7, 4=7, 5=7, 6=7, 7=7, 8=7, 9=1, 1..9

indexes: "OddLaneTeamID", "EvenLaneTeamID", "TourneyID"

samples:
| column | latest | sample | sample |
|---|---|---|---|
| MatchID | 57 | 23 | 8 |
| TourneyID | 11 | 6 | 2 |
| Lanes | 19-20 | 09-10 | 27-28 |
| OddLaneTeamID | 10 | 2 | 8 |
| EvenLaneTeamID | 9 | 8 | 6 |

# "WAZips"  (rows=523)

columns:
"ZIP" text PK: digits, unique identifier
"City" text: 385 distinct
"State" text: "WA"=523

indexes: none

samples:
| column | latest | sample | sample |
|---|---|---|---|
| ZIP | 99403 | 98564 | 99153 |
| City | Clarkston | Mossyrock | Metaline Falls |
| State | WA | WA | WA |

- Skipped 4 empty table(s): "Bowler_Scores_Archive", "Match_Games_Archive", "Tournaments_Archive", "Tourney_Matches_Archive"
