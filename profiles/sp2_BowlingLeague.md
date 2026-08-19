---
generator: db-snooper
version: 0.0.26
generated_at_utc: 2026-08-16T08:07:39.581712Z
dialect: sqlite
database: /var/folders/9j/b9bx_drd53sc6zbpsqyrjy4h0000gn/T/dbsnoop-5qylf7w_/BowlingLeague.sqlite
schema: main
---

## Relationships

- Bowlers.BowlerID ← Bowler_Scores.BowlerID
- Match_Games.(MatchID, GameNumber) ← Bowler_Scores.(MatchID, GameNumber)
- Match_Games_Archive.(MatchID, GameNumber) ← Bowler_Scores_Archive.(MatchID, GameNumber)
- Teams.TeamID ← Bowlers.TeamID, Tourney_Matches.EvenLaneTeamID, Tourney_Matches.OddLaneTeamID
- Tournaments.TourneyID ← Tourney_Matches.TourneyID
- Tournaments_Archive.TourneyID ← Tourney_Matches_Archive.TourneyID

# Bowler_Scores

```sql
CREATE TABLE Bowler_Scores (
    MatchID int NOT NULL DEFAULT 0,
    GameNumber smallint NOT NULL DEFAULT 0,
    BowlerID int NOT NULL DEFAULT 0,
    RawScore smallint NULL DEFAULT 0,
    HandiCapScore smallint NULL DEFAULT 0,
    WonGame BOOLEAN NOT NULL DEFAULT 0,
    PRIMARY KEY (MatchID, GameNumber, BowlerID),
    FOREIGN KEY (BowlerID) REFERENCES Bowlers(BowlerID),
    FOREIGN KEY (MatchID, GameNumber) REFERENCES Match_Games(MatchID, GameNumber)
);
```

## Indexes

- (BowlerID)
- (MatchID, GameNumber)

## Rows

- total=1344

| column | latest | sample | sample |
|---|---|---|---|
| MatchID | 56 | 14 | 47 |
| GameNumber | 3 | 2 | 1 |
| BowlerID | 32 | 24 | 5 |
| RawScore | 148 | 172 | 136 |
| HandiCapScore | 200 | 198 | 182 |
| WonGame | true | true | false |

## Columns

- MatchID: 56 distinct, int 1..56
  - stats: average=28.5, median=28.5
  - top_values: 1=24, 2=24, 3=24, 4=24, 5=24, 6=24, 7=24, 8=24, 9=24, 10=24
- GameNumber: 1=448, 2=448, 3=448, int 1..3
- BowlerID: 32 distinct, int 1..32
  - stats: average=16.5, median=16.5
  - top_values: 1=42, 2=42, 3=42, 4=42, 5=42, 6=42, 7=42, 8=42, 9=42, 10=42
- RawScore: 61 distinct, int 135..195
  - stats: average=154.507, median=150
- HandiCapScore: 70 distinct, int 161..231
  - stats: average=195.332, median=195
- WonGame: True=695, False=649


# Bowlers

```sql
CREATE TABLE Bowlers (
    BowlerID INTEGER PRIMARY KEY AUTOINCREMENT,
    BowlerLastName TEXT NULL,
    BowlerFirstName TEXT NULL,
    BowlerMiddleInit TEXT NULL,
    BowlerAddress TEXT NULL,
    BowlerCity TEXT NULL,
    BowlerState TEXT NULL,
    BowlerZip TEXT NULL,
    BowlerPhoneNumber TEXT NULL,
    TeamID int NULL,
    BowlerTotalPins int NULL DEFAULT 0,
    BowlerGamesBowled int NULL DEFAULT 0,
    BowlerCurrentAverage smallint NULL DEFAULT 0,
    BowlerCurrentHcp smallint NULL DEFAULT 0,
    FOREIGN KEY (TeamID) REFERENCES Teams(TeamID)
);
```

## Indexes

- (BowlerLastName)
- (TeamID)

## Rows

- total=34

| column | latest | sample | sample |
|---|---|---|---|
| BowlerID | 34 | 4 | 12 |
| BowlerLastName | Patterson | Sheskey | Viescas |
| BowlerFirstName | Maria | Sara | Carol |
| BowlerMiddleInit | null | J | M |
| BowlerAddress | 16 Maple Lane | 17950 N 59th | 16345 NE 32nd Street |
| BowlerCity | Auburn | Seattle | Bellevue |
| BowlerState | WA | WA | WA |
| BowlerZip | 98002 | 98011 | 98004 |
| BowlerPhoneNumber | (206) 555-3487 | (206) 555-9893 | (206) 555-7295 |
| TeamID | 7 | 1 | 3 |
| BowlerTotalPins | 0 | 5534 | 5560 |
| BowlerGamesBowled | 0 | 39 | 39 |
| BowlerCurrentAverage | 0 | 142 | 143 |
| BowlerCurrentHcp | 0 | 52 | 51 |

## Columns

- BowlerID: unique identifier, int 1..34
  - stats: average=17.5, median=17.5
- BowlerLastName: "Patterson"=7, "Viescas"=7, "Hallmark"=4, "Thompson"=3, "Fournier"=2, "Hernandez"=2, "Kennedy"=2, "Sheskey"=2, "Black"=1, "Clothier"=1, "Cunningham"=1, "Ehrlich"=1, "Rosales"=1
- BowlerFirstName: 30 distinct
- BowlerMiddleInit: "L"=4, "A"=2, "K"=2, "G"=1, "J"=1, "M"=1, nulls=23
- BowlerAddress: "16 Maple Lane"=7, "Route 2, Box 203B"=4, "122 Spring Valley Drive"=3, "16679 NE 42nd Court"=3, "218 Main Street"=3, "17950 N 59th"=2, "2957 W 33rd"=2, "47 Harvard Drive"=2, "67 Willow Drive"=2, "16345 NE 32nd Street"=1, "4110 Old Redmond Rd."=1, "4726 - 11th Ave. N.E."=1, "507 - 20th Ave. E."=1, "722 Moss Bay Blvd."=1, "908 W. Capital Way"=1
- BowlerCity: "Auburn"=7, "Redmond"=7, "Seattle"=4, "Woodinville"=4, "Duvall"=3, "Kirkland"=3, "Ballard"=2, "Bothell"=2, "Bellevue"=1, "Tacoma"=1
- BowlerState: "WA"=34
- BowlerZip: "98002"=7, "98052"=7, "98072"=4, "98019"=3, "98033"=3, "98011"=2, "98014"=2, "98154"=2, "98004"=1, "98105"=1, "98122"=1, "98404"=1
- BowlerPhoneNumber: "(206) 555-3487"=7, "(206) 555-8990"=4, "(206) 555-8989"=3, "(206) 881-5596"=3, "(206) 882-8878"=3, "(206) 555-7854"=2, "(206) 555-9876"=2, "(206) 555-9893"=2, "(206) 889-9191"=2, "(206) 555-1189"=1, "(206) 555-3412"=1, "(206) 555-7295"=1, "(206) 555-8122"=1, "(206) 555-9482"=1, "(206) 555-9857"=1
- TeamID: 7=6, 1=4, 2=4, 3=4, 4=4, 5=4, 6=4, 8=4, int 1..8
- BowlerTotalPins: 33 distinct, int 0..6607
  - stats: average=5676.12, median=6022
- BowlerGamesBowled: 39=32, 0=2
- BowlerCurrentAverage: 143=4, 157=4, 142=3, 150=3, 158=3, 169=3, 0=2, 148=2, 165=2, 149=1, 151=1, 152=1, 159=1, 162=1, 163=1, 164=1, 167=1, int 0..169
- BowlerCurrentHcp: 39=4, 51=4, 28=3, 32=3, 38=3, 45=3, 52=3, 0=2, 47=2, 30=1, 33=1, 34=1, 37=1, 43=1, 44=1, 46=1, int 0..52


# Match_Games

```sql
CREATE TABLE Match_Games (
    MatchID int NOT NULL DEFAULT 0,
    GameNumber smallint NOT NULL DEFAULT 0,
    WinningTeamID int NULL DEFAULT 0,
    PRIMARY KEY (MatchID, GameNumber)
);
```

## Indexes

- (WinningTeamID)
- (MatchID)

## Rows

- total=168

| column | latest | sample | sample |
|---|---|---|---|
| MatchID | 56 | 53 | 52 |
| GameNumber | 3 | 3 | 1 |
| WinningTeamID | 8 | 2 | 4 |

## Columns

- MatchID: 56 distinct, int 1..56
  - stats: average=28.5, median=28.5
  - top_values: 1=3, 2=3, 3=3, 4=3, 5=3, 6=3, 7=3, 8=3, 9=3, 10=3
- GameNumber: 1=56, 2=56, 3=56, int 1..3
- WinningTeamID: 1=21, 2=21, 3=21, 4=21, 5=21, 6=21, 7=21, 8=21, int 1..8


# Teams

## All rows

| column | row 1 | row 2 | row 3 | row 4 | row 5 | row 6 | row 7 | row 8 | row 9 | row 10 |
|---|---|---|---|---|---|---|---|---|---|---|
| TeamID | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9 | 10 |
| TeamName | Marlins | Sharks | Terrapins | Barracudas | Dolphins | Orcas | Manatees | Swordfish | Huckleberrys | Never Show Ups |
| CaptainID | 2 | 5 | 12 | 16 | 20 | 24 | 28 | 32 | 7 | 22 |


# Tournaments

```sql
CREATE TABLE Tournaments (
    TourneyID INTEGER PRIMARY KEY AUTOINCREMENT,
    TourneyDate DATE NULL,
    TourneyLocation TEXT NULL
);
```

## Rows

- total=20

| column | latest | sample | sample |
|---|---|---|---|
| TourneyID | 20 | 18 | 12 |
| TourneyDate | 2018-08-16 | 2018-08-02 | 2017-11-20 |
| TourneyLocation | Totem Lanes | Sports World Lanes | Sports World Lanes |

## Columns

- TourneyID: unique identifier, int 1..20
  - stats: average=10.5, median=10.5
- TourneyDate: all distinct
- TourneyLocation: "Bolero Lanes"=3, "Imperial Lanes"=3, "Red Rooster Lanes"=3, "Sports World Lanes"=3, "Thunderbird Lanes"=3, "Totem Lanes"=3, "Acapulco Lanes"=2


# Tourney_Matches

```sql
CREATE TABLE Tourney_Matches (
    MatchID INTEGER PRIMARY KEY AUTOINCREMENT,
    TourneyID int NULL DEFAULT 0,
    Lanes TEXT NULL,
    OddLaneTeamID int NULL DEFAULT 0,
    EvenLaneTeamID int NULL DEFAULT 0,
    FOREIGN KEY (EvenLaneTeamID) REFERENCES Teams(TeamID),
    FOREIGN KEY (OddLaneTeamID) REFERENCES Teams(TeamID),
    FOREIGN KEY (TourneyID) REFERENCES Tournaments(TourneyID)
);
```

## Indexes

- (OddLaneTeamID)
- (EvenLaneTeamID)
- (TourneyID)

## Rows

- total=57

| column | latest | sample | sample |
|---|---|---|---|
| MatchID | 57 | 8 | 33 |
| TourneyID | 11 | 2 | 9 |
| Lanes | 19-20 | 27-28 | 15-16 |
| OddLaneTeamID | 10 | 8 | 3 |
| EvenLaneTeamID | 9 | 6 | 2 |

## Columns

- MatchID: unique identifier, int 1..57
  - stats: average=29, median=29
- TourneyID: 11=5, 1=4, 2=4, 3=4, 4=4, 5=4, 6=4, 7=4, 8=4, 9=4, 10=4, 12=4, 13=4, 14=4, int 1..14
- Lanes: "15-16"=8, "11-12"=6, "13-14"=6, "17-18"=6, "19-20"=5, "05-06"=4, "07-08"=4, "09-10"=4, "21-22"=4, "01-02"=2, "03-04"=2, "23-24"=2, "25-26"=2, "27-28"=2
- OddLaneTeamID: 1=7, 2=7, 3=7, 4=7, 5=7, 6=7, 7=7, 8=7, 10=1, int 1..10
- EvenLaneTeamID: 1=7, 2=7, 3=7, 4=7, 5=7, 6=7, 7=7, 8=7, 9=1, int 1..9


# WAZips

```sql
CREATE TABLE WAZips (
    ZIP TEXT NOT NULL,
    City TEXT NULL,
    State TEXT NULL,
    PRIMARY KEY (ZIP)
);
```

## Rows

- total=523

| column | latest | sample | sample |
|---|---|---|---|
| ZIP | 99403 | 98203 | 98526 |
| City | Clarkston | Everett | Amanda Park |
| State | WA | WA | WA |

## Columns

- ZIP: unique identifier
- City: 385 distinct
- State: "WA"=523


- Skipped 4 empty table(s): Bowler_Scores_Archive, Match_Games_Archive, Tournaments_Archive, Tourney_Matches_Archive
