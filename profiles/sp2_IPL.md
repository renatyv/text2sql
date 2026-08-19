---
generator: db-snooper
version: 0.0.26
generated_at_utc: 2026-08-16T08:08:41.431657Z
dialect: sqlite
database: /var/folders/9j/b9bx_drd53sc6zbpsqyrjy4h0000gn/T/dbsnoop-22ne7895/IPL.sqlite
schema: main
---

# ball_by_ball

```sql
CREATE TABLE ball_by_ball(
        match_id INTEGER NOT NULL,
        over_id INTEGER NOT NULL,
        ball_id INTEGER NOT NULL,
        innings_no INTEGER NOT NULL,
        team_batting INTEGER,
        team_bowling INTEGER,
        striker_batting_position INTEGER,
        striker INTEGER,
        non_striker INTEGER,
        bowler INTEGER,
        PRIMARY KEY(match_id, over_id, ball_id, innings_no)
    );
```

## Rows

- total=134703

| column | latest | sample | sample |
|---|---|---|---|
| match_id | 981024 | 548366 | 981006 |
| over_id | 20 | 20 | 4 |
| ball_id | 6 | 1 | 2 |
| innings_no | 2 | 1 | 1 |
| team_batting | 2 | 5 | 1 |
| team_bowling | 11 | 3 | 13 |
| striker_batting_position | 9 | 8 | 3 |
| striker | 140 | 277 | 96 |
| non_striker | 369 | 266 | 46 |
| bowler | 299 | 71 | 80 |

## Columns

- match_id: 568 distinct, int 335987..981024
- over_id: 20 distinct, int 1..20
- ball_id: 1=21831, 2=21782, 3=21718, 4=21666, 5=21597, 6=21526, 7=3878, 8=607, 9=98, int 1..9
- innings_no: 1=69691, 2=65012
- team_batting: int 1..13
  - stats: average=5.182
- team_bowling: int 1..13
  - stats: average=5.17173
- striker_batting_position: int 1..11
  - stats: average=3.58602
- striker: int 1..434
  - stats: average=126.382
- non_striker: int 1..451
  - stats: average=125.726
- bowler: int 1..465
  - stats: average=180.118


# batsman_scored

```sql
CREATE TABLE batsman_scored(
        match_id INTEGER NOT NULL,
        over_id INTEGER NOT NULL,
        ball_id INTEGER NOT NULL,
        runs_scored INTEGER,
        innings_no INTEGER NOT NULL,
        PRIMARY KEY(match_id, over_id, ball_id, innings_no)
    );
```

## Rows

- total=131259

| column | latest | sample | sample |
|---|---|---|---|
| match_id | 981024 | 501212 | 829790 |
| over_id | 20 | 19 | 12 |
| ball_id | 6 | 1 | 2 |
| runs_scored | 4 | 0 | 0 |
| innings_no | 2 | 2 | 2 |

## Columns

- match_id: 568 distinct, int 335987..981024
- over_id: 20 distinct, int 1..20
- ball_id: 2=21217, 1=21196, 3=21191, 4=21150, 5=21068, 6=20997, 7=3759, 8=584, 9=97, int 1..9
- runs_scored: int 0..6
  - stats: average=1.247
- innings_no: 1=67949, 2=63310


# extra_runs

```sql
CREATE TABLE extra_runs(
        match_id INTEGER NOT NULL,
        over_id INTEGER NOT NULL,
        ball_id INTEGER NOT NULL,
        extra_type TEXT,
        extra_runs INTEGER,
        innings_no INTEGER NOT NULL,
        PRIMARY KEY(match_id, over_id, ball_id, innings_no)
    );
```

## Rows

- total=7349

| column | latest | sample | sample |
|---|---|---|---|
| match_id | 981024 | 392243 | 733992 |
| over_id | 20 | 11 | 11 |
| ball_id | 4 | 5 | 6 |
| extra_type | legbyes | wides | wides |
| extra_runs | 1 | 1 | 1 |
| innings_no | 2 | 1 | 1 |

## Columns

- match_id: 568 distinct, int 335987..981024
  - top_values: 829742=26, 336023=25, 548382=25, 335987=24, 335991=24, 392197=24, 419130=24, 501215=24, 501232=24, 501265=24
- over_id: 20 distinct, int 1..20
  - top_values: 1=508, 2=499, 3=437, 17=435, 4=412, 20=411, 19=399, 18=394, 6=387, 5=374
- ball_id: 1=1255, 3=1228, 2=1219, 6=1133, 5=1121, 4=1098, 7=249, 8=45, 9=1, int 1..9
- extra_type: "wides"=4091, "legbyes"=2317, "noballs"=567, "byes"=373, "penalty"=1
- extra_runs: 1=6499, 2=335, 4=273, 5=192, 3=50, int 1..5
- innings_no: 1=3808, 2=3541


# match

```sql
CREATE TABLE match(
        match_id INTEGER PRIMARY KEY,
        team_1 INTEGER,
        team_2 INTEGER,
        match_date DATE,
        season_id INTEGER,
        venue TEXT,
        toss_winner INTEGER,
        toss_decision TEXT,
        win_type TEXT,
        win_margin INTEGER,
        outcome_type TEXT,
        match_winner INTEGER,
        man_of_the_match INTEGER
    );
```

## Rows

- total=567

| column | latest | sample | sample |
|---|---|---|---|
| match_id | 981024 | 829722 | 734046 |
| team_1 | 2 | 7 | 7 |
| team_2 | 11 | 4 | 5 |
| match_date | 2016-05-29 | 2015-04-12 | 2014-05-25 |
| season_id | 9 | 8 | 7 |
| venue | M Chinnaswamy Stadium | Wankhede Stadium | Wankhede Stadium |
| toss_winner | 11 | 7 | 7 |
| toss_decision | bat | field | field |
| win_type | runs | runs | wickets |
| win_margin | 8 | 18 | 5 |
| outcome_type | Result | Result | Result |
| match_winner | 11 | 4 | 7 |
| man_of_the_match | 385 | 197 | 372 |

## Columns

- match_id: unique identifier, int 335987..981024
- team_1: 2=75, 3=73, 6=67, 4=65, 7=62, 1=60, 5=51, 8=39, 11=29, 10=23, 13=9, 9=7, 12=7, int 1..13
- team_2: 7=78, 1=69, 4=67, 5=63, 6=62, 2=60, 3=57, 8=36, 11=32, 10=22, 9=7, 12=7, 13=7, int 1..13
- match_date: 403 distinct
- season_id: 5=74, 6=74, 4=72, 9=60, 7=59, 1=58, 3=58, 2=56, 8=56, int 1..9
- venue: 35 distinct
- toss_winner: 7=74, 1=68, 3=65, 4=63, 6=62, 5=61, 2=58, 8=43, 11=30, 10=20, 9=8, 13=8, 12=7, int 1..13
- toss_decision: "field"=309, "bat"=258
- win_type: "wickets"=307, "runs"=260
- win_margin: 81 distinct, int 1..144
  - stats: average=17.3104, median=8
- outcome_type: "Result"=567
- match_winner: 7=80, 3=79, 2=69, 1=68, 4=61, 5=61, 6=55, 11=33, 8=29, 10=12, 13=9, 9=6, 12=5, int 1..13
- man_of_the_match: 186 distinct, int 1..460
  - stats: average=139.376, median=105


# player

```sql
CREATE TABLE player(
        player_id INTEGER PRIMARY KEY,
        player_name TEXT,
        dob DATE,
        batting_hand TEXT,
        bowling_skill TEXT,
        country_name TEXT
    );
```

## Rows

- total=468

| column | latest | sample | sample |
|---|---|---|---|
| player_id | 469 | 230 | 202 |
| player_name | T Mishra | AC Voges | Mohammad Ashraful |
| dob | 1986-12-22 | 1979-10-04 | 1984-07-07 |
| batting_hand | Right-hand bat | Right-hand bat | Right-hand bat |
| bowling_skill | Right-arm fast-medium | Slow left-arm orthodox | Right-arm offbreak |
| country_name | India | Australia | Bangladesh |

## Columns

- player_id: unique identifier, int 1..469
- player_name: all distinct
- dob: 454 distinct
- batting_hand: "Right-hand bat"=343, "Left-hand bat"=125
- bowling_skill: "Right-arm medium"=147, "Right-arm offbreak"=81, "Right-arm fast-medium"=53, "Slow left-arm orthodox"=43, "Right-arm medium-fast"=38, "Legbreak"=24, "Legbreak googly"=21, "Right-arm fast"=20, "Left-arm fast-medium"=13, "Left-arm medium"=11, "Left-arm medium-fast"=8, "Slow left-arm chinaman"=5, "Left-arm fast"=3, "Right-arm bowler"=1
- country_name: "India"=261, "Australia"=72, "South Africa"=39, "New Zealand"=22, "Sri Lanka"=20, "West Indies"=19, "England"=14, "Pakistan"=13, "Bangladesh"=5, "Zimbabwea"=2, "Netherlands"=1


# player_match

```sql
CREATE TABLE player_match(
        match_id INTEGER NOT NULL,
        player_id INTEGER NOT NULL,
        role TEXT,
        team_id INTEGER,
        PRIMARY KEY(match_id, player_id)
    );
```

## Rows

- total=12495

| column | latest | sample | sample |
|---|---|---|---|
| match_id | 981024 | 598026 | 598058 |
| player_id | 460 | 10 | 214 |
| role | Player | Captain | Keeper |
| team_id | 11 | 11 | 1 |

## Columns

- match_id: 568 distinct, int 335987..981024
  - top_values: 335987=22, 335988=22, 335989=22, 335990=22, 335991=22, 335992=22, 335993=22, 335994=22, 335995=22, 335996=22
- player_id: 468 distinct, int 1..469
  - top_values: 21=145, 20=142, 57=142, 88=136, 8=134, 31=133, 46=133, 40=130, 50=125, 35=124
- role: "Player"=10471, "Keeper"=889, "Captain"=888, "CaptainKeeper"=247
- team_id: 7=1540, 2=1485, 4=1452, 3=1430, 6=1430, 1=1429, 5=1254, 8=825, 11=671, 10=495, 13=176, 9=154, 12=154, int 1..13


# team

```sql
CREATE TABLE team(
        team_id INTEGER PRIMARY KEY,
        name TEXT
    );
```

## Rows

- total=12

| column | latest | sample | sample |
|---|---|---|---|
| team_id | 13 | 2 | 10 |
| name | Gujarat Lions | Royal Challengers Bangalore | Pune Warriors |

## Columns

- team_id: unique identifier, int 2..13
- name: "Chennai Super Kings"=1, "Deccan Chargers"=1, "Delhi Daredevils"=1, "Gujarat Lions"=1, "Kings XI Punjab"=1, "Kochi Tuskers Kerala"=1, "Mumbai Indians"=1, "Pune Warriors"=1, "Rajasthan Royals"=1, "Rising Pune Supergiants"=1, "Royal Challengers Bangalore"=1, "Sunrisers Hyderabad"=1


# wicket_taken

```sql
CREATE TABLE wicket_taken(
        match_id INTEGER NOT NULL,
        over_id INTEGER NOT NULL,
        ball_id INTEGER NOT NULL,
        player_out INTEGER,
        kind_out TEXT,
        innings_no INTEGER NOT NULL,
        PRIMARY KEY(match_id, over_id, ball_id, innings_no)
    );
```

## Rows

- total=6618

| column | latest | sample | sample |
|---|---|---|---|
| match_id | 981024 | 392241 | 392228 |
| over_id | 20 | 11 | 19 |
| ball_id | 3 | 6 | 4 |
| player_out | 434 | 178 | 61 |
| kind_out | run out | caught | run out |
| innings_no | 2 | 2 | 2 |

## Columns

- match_id: 568 distinct, int 335987..981024
  - top_values: 419146=20, 335996=19, 336043=19, 729312=19, 733994=19, 829784=19, 980960=19, 336009=18, 392187=18, 392211=18
- over_id: 20 distinct, int 1..20
  - top_values: 20=667, 19=527, 18=498, 17=404, 16=370, 15=336, 14=310, 11=298, 5=295, 3=291
- ball_id: 4=1123, 6=1094, 2=1089, 5=1060, 3=1057, 1=983, 7=185, 8=24, 9=3, int 1..9
- player_out: 411 distinct, int 1..438
  - stats: average=137.332, median=97
- kind_out: "caught"=3894, "bowled"=1234, "run out"=677, "lbw"=393, "stumped"=219, "caught and bowled"=184, "hit wicket"=8, "retired hurt"=8, "obstructing the field"=1
- innings_no: 1=3447, 2=3171
