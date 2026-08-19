---
generator: db-snooper
version: 0.0.26
generated_at_utc: 2026-08-16T08:07:37.634673Z
dialect: sqlite
database: /var/folders/9j/b9bx_drd53sc6zbpsqyrjy4h0000gn/T/dbsnoop-91qewbgw/Baseball.sqlite
schema: main
---

# all_star

```sql
CREATE TABLE all_star (
    player_id TEXT,
    year INTEGER,
    game_num INTEGER,
    game_id TEXT,
    team_id TEXT,
    league_id TEXT,
    gp NUMERIC,
    starting_pos NUMERIC);
```


# appearances

```sql
CREATE TABLE appearances (
    year INTEGER,
    team_id TEXT,
    league_id TEXT,
    player_id TEXT,
    g_all NUMERIC,
    gs NUMERIC,
    g_batting INTEGER,
    g_defense NUMERIC,
    g_p INTEGER,
    g_c INTEGER,
    g_1b INTEGER,
    g_2b INTEGER,
    g_3b INTEGER,
    g_ss INTEGER,
    g_lf INTEGER,
    g_cf INTEGER,
    g_rf INTEGER,
    g_of INTEGER,
    g_dh NUMERIC,
    g_ph NUMERIC,
    g_pr NUMERIC);
```


# batting

```sql
CREATE TABLE batting (
    player_id TEXT,
    year INTEGER,
    stint INTEGER,
    team_id TEXT,
    league_id TEXT,
    g INTEGER,
    ab NUMERIC,
    r NUMERIC,
    h NUMERIC,
    double NUMERIC,
    triple NUMERIC,
    hr NUMERIC,
    rbi NUMERIC,
    sb NUMERIC,
    cs NUMERIC,
    bb NUMERIC,
    so NUMERIC,
    ibb NUMERIC,
    hbp NUMERIC,
    sh NUMERIC,
    sf NUMERIC,
    g_idp NUMERIC);
```


# batting_postseason

```sql
CREATE TABLE batting_postseason (
    year INTEGER,
    round TEXT,
    player_id TEXT,
    team_id TEXT,
    league_id TEXT,
    g INTEGER,
    ab INTEGER,
    r INTEGER,
    h INTEGER,
    double INTEGER,
    triple INTEGER,
    hr INTEGER,
    rbi INTEGER,
    sb INTEGER,
    cs NUMERIC,
    bb INTEGER,
    so INTEGER,
    ibb NUMERIC,
    hbp NUMERIC,
    sh NUMERIC,
    sf NUMERIC,
    g_idp NUMERIC);
```


# college

```sql
CREATE TABLE college (
    college_id TEXT,
    name_full TEXT,
    city TEXT,
    state TEXT,
    country TEXT);
```

## Rows

- total=1207

| column | latest | sample | sample |
|---|---|---|---|
| college_id | youngst | wayakim | benedctnks |
| name_full | Youngstown State University | Yakima Valley Community College | Benedictine College |
| city | Youngstown | Yakima | Atchison |
| state | OH | WA | KS |
| country | USA | USA | USA |

## Columns

- college_id: unique identifier
- name_full: 1199 distinct
- city: 856 distinct
- state: 49 distinct
- country: "USA"=1207


# fielding

```sql
CREATE TABLE fielding (
    player_id TEXT,
    year INTEGER,
    stint INTEGER,
    team_id TEXT,
    league_id TEXT,
    pos TEXT,
    g INTEGER,
    gs NUMERIC,
    inn_outs NUMERIC,
    po NUMERIC,
    a NUMERIC,
    e NUMERIC,
    dp NUMERIC,
    pb NUMERIC,
    wp NUMERIC,
    sb NUMERIC,
    cs NUMERIC,
    zr NUMERIC);
```


# fielding_outfield

```sql
CREATE TABLE fielding_outfield (
    player_id TEXT,
    year INTEGER,
    stint INTEGER,
    glf NUMERIC,
    gcf NUMERIC,
    grf NUMERIC);
```


# fielding_postseason

```sql
CREATE TABLE fielding_postseason (
    player_id TEXT,
    year INTEGER,
    team_id TEXT,
    league_id TEXT,
    round TEXT,
    pos TEXT,
    g INTEGER,
    gs NUMERIC,
    inn_outs NUMERIC,
    po INTEGER,
    a INTEGER,
    e INTEGER,
    dp INTEGER,
    tp INTEGER,
    pb NUMERIC,
    sb NUMERIC,
    cs NUMERIC);
```


# hall_of_fame

```sql
CREATE TABLE hall_of_fame (
    player_id TEXT,
    yearid INTEGER,
    votedby TEXT,
    ballots NUMERIC,
    needed NUMERIC,
    votes NUMERIC,
    inducted TEXT,
    category TEXT,
    needed_note TEXT);
```


# home_game

```sql
CREATE TABLE home_game (
    year INTEGER,
    league_id TEXT,
    team_id TEXT,
    park_id TEXT,
    span_first TEXT,
    span_last TEXT,
    games INTEGER,
    openings INTEGER,
    attendance INTEGER);
```

## Rows

- total=2944

| column | latest | sample | sample |
|---|---|---|---|
| year | 2014 | 2002 | 1992 |
| league_id | NL | AL | NL |
| team_id | WAS | BOS | NYN |
| park_id | WAS11 | BOS07 | NYC17 |
| span_first | 2014-04-04 | 2002-04-01 | 1992-04-10 |
| span_last | 2014-09-28 | 2002-09-29 | 1992-10-04 |
| games | 81 | 81 | 81 |
| openings | 81 | 81 | 76 |
| attendance | 2579389 | 2650859 | 1779534 |

## Columns

- year: 144 distinct, int 1871..2014
  - stats: average=1952.11, median=1959
- league_id: "NL"=1482, "AL"=1235, "AA"=112, ""=77, "FL"=16, "UA"=14, "PL"=8
- team_id: 148 distinct
- park_id: 249 distinct
- span_first: 1052 distinct
- span_last: 1103 distinct
- games: 87 distinct, int 1..89
  - stats: average=70.804, median=78
- openings: 84 distinct, int 0..83
  - stats: average=48.9412, median=66
- attendance: 2388 distinct, int 0..4483203
  - stats: average=1.07779e+06, median=874752


# manager

```sql
CREATE TABLE manager (
    player_id TEXT,
    year INTEGER,
    team_id TEXT,
    league_id TEXT,
    inseason INTEGER,
    g INTEGER,
    w INTEGER,
    l INTEGER,
    rank NUMERIC,
    plyr_mgr TEXT);
```


# manager_award

```sql
CREATE TABLE manager_award (
    player_id TEXT,
    award_id TEXT,
    year INTEGER,
    league_id TEXT,
    tie TEXT,
    notes NUMERIC);
```


# manager_award_vote

```sql
CREATE TABLE manager_award_vote (
    award_id TEXT,
    year INTEGER,
    league_id TEXT,
    player_id TEXT,
    points_won INTEGER,
    points_max INTEGER,
    votes_first INTEGER);
```

## Rows

- total=414

| column | latest | sample | sample |
|---|---|---|---|
| award_id | Mgr of the year | Mgr of the year | Mgr of the year |
| year | 2012 | 2009 | 1985 |
| league_id | NL | NL | NL |
| player_id | mathemi01 | bochybr01 | herzowh01 |
| points_won | 1 | 18 | 86 |
| points_max | 160 | 160 | 120 |
| votes_first | 0 | 0 | 11 |

## Columns

- award_id: "Mgr of the year"=333, "Mgr of the Year"=81
- year: 33 distinct, int 1983..2015
  - stats: average=1999.78, median=2000
- league_id: "AL"=213, "NL"=201
- player_id: 110 distinct
- points_won: 117 distinct, int 1..154
  - stats: average=39.8792, median=22
- points_max: 140=220, 160=102, 120=43, 150=42, 24=4, 28=3, int 24..160
- votes_first: 30 distinct, int 0..30
  - stats: average=4.54348, median=1


# manager_half

```sql
CREATE TABLE manager_half (
    player_id TEXT,
    year INTEGER,
    team_id TEXT,
    league_id TEXT,
    inseason INTEGER,
    half INTEGER,
    g INTEGER,
    w INTEGER,
    l INTEGER,
    rank INTEGER);
```

## Rows

- total=93

| column | latest | sample | sample |
|---|---|---|---|
| player_id | zimmedo01 | mcnamjo99 | mattibo01 |
| year | 1981 | 1981 | 1981 |
| team_id | TEX | CIN | TOR |
| league_id | AL | NL | AL |
| inseason | 1 | 1 | 1 |
| half | 2 | 1 | 2 |
| g | 50 | 56 | 48 |
| w | 24 | 35 | 21 |
| l | 26 | 21 | 27 |
| rank | 3 | 2 | 7 |

## Columns

- player_id: 54 distinct
- year: 1981=58, 1892=35
- team_id: 33 distinct
- league_id: "NL"=60, "AL"=33
- inseason: 1=68, 2=17, 3=6, 4=1, 5=1, int 1..5
- half: 1=48, 2=45
- g: 40 distinct, int 2..80
  - stats: average=49.7849, median=53
- w: 42 distinct, int 0..53
  - stats: average=24.6452, median=25
- l: 34 distinct, int 2..46
  - stats: average=24.6452, median=25
- rank: 6=13, 1=12, 4=12, 2=11, 5=10, 3=9, 7=8, 11=5, 12=5, 9=4, 8=2, 10=2, int 1..12


# park

```sql
CREATE TABLE park (
    park_id TEXT,
    park_name TEXT,
    park_alias TEXT,
    city TEXT,
    state TEXT,
    country TEXT);
```

## Rows

- total=250

| column | latest | sample | sample |
|---|---|---|---|
| park_id | WOR03 | BAL07 | NYC21 |
| park_name | Worcester Driving Park Grounds | Oriole Park III | Yankee Stadium II |
| park_alias |  |  |  |
| city | Worcester | Baltimore | New York |
| state | MA | MD | NY |
| country | US | US | US |

## Columns

- park_id: unique identifier
- park_name: 240 distinct
- park_alias: 57 distinct
- city: 83 distinct
- state: 35 distinct
- country: "US"=242, "CA"=4, "AU"=1, "JP"=1, "MX"=1, "PR"=1


# pitching

```sql
CREATE TABLE pitching (
    player_id TEXT,
    year INTEGER,
    stint INTEGER,
    team_id TEXT,
    league_id TEXT,
    w INTEGER,
    l INTEGER,
    g INTEGER,
    gs INTEGER,
    cg INTEGER,
    sho INTEGER,
    sv INTEGER,
    ipouts NUMERIC,
    h INTEGER,
    er INTEGER,
    hr INTEGER,
    bb INTEGER,
    so INTEGER,
    baopp NUMERIC,
    era NUMERIC,
    ibb NUMERIC,
    wp NUMERIC,
    hbp NUMERIC,
    bk INTEGER,
    bfp NUMERIC,
    gf NUMERIC,
    r INTEGER,
    sh NUMERIC,
    sf NUMERIC,
    g_idp NUMERIC);
```


# pitching_postseason

```sql
CREATE TABLE pitching_postseason (
    player_id TEXT,
    year INTEGER,
    round TEXT,
    team_id TEXT,
    league_id TEXT,
    w INTEGER,
    l INTEGER,
    g INTEGER,
    gs INTEGER,
    cg INTEGER,
    sho INTEGER,
    sv INTEGER,
    ipouts INTEGER,
    h INTEGER,
    er INTEGER,
    hr INTEGER,
    bb INTEGER,
    so INTEGER,
    baopp TEXT,
    era NUMERIC,
    ibb NUMERIC,
    wp NUMERIC,
    hbp NUMERIC,
    bk NUMERIC,
    bfp NUMERIC,
    gf INTEGER,
    r INTEGER,
    sh NUMERIC,
    sf NUMERIC,
    g_idp NUMERIC);
```


# player

```sql
CREATE TABLE player (
    player_id TEXT,
    birth_year NUMERIC,
    birth_month NUMERIC,
    birth_day NUMERIC,
    birth_country TEXT,
    birth_state TEXT,
    birth_city TEXT,
    death_year NUMERIC,
    death_month NUMERIC,
    death_day NUMERIC,
    death_country TEXT,
    death_state TEXT,
    death_city TEXT,
    name_first TEXT,
    name_last TEXT,
    name_given TEXT,
    weight NUMERIC,
    height NUMERIC,
    bats TEXT,
    throws TEXT,
    debut TEXT,
    final_game TEXT,
    retro_id TEXT,
    bbref_id TEXT);
```


# player_award

```sql
CREATE TABLE player_award (
    player_id TEXT,
    award_id TEXT,
    year INTEGER,
    league_id TEXT,
    tie TEXT,
    notes TEXT);
```

## Rows

- total=6078

| column | latest | sample | sample |
|---|---|---|---|
| player_id | zitoba01 | willite01 | brocklo01 |
| award_id | TSN Pitcher of the Year | TSN All-Star | Hutch Award |
| year | 2002 | 1941 | 1979 |
| league_id | AL | ML | ML |
| tie |  |  |  |
| notes |  | OF |  |

## Columns

- player_id: 1323 distinct
- award_id: 27 distinct
- year: 117 distinct, int 1877..2015
  - stats: average=1968.46, median=1974
- league_id: "AL"=2413, "NL"=2378, "ML"=1285, "AA"=2
- tie: ""=6033, "Y"=45
- notes: 29 distinct


# player_award_vote

```sql
CREATE TABLE player_award_vote (
    award_id TEXT,
    year INTEGER,
    league_id TEXT,
    player_id TEXT,
    points_won NUMERIC,
    points_max INTEGER,
    votes_first NUMERIC);
```


# player_college

```sql
CREATE TABLE player_college (
    player_id TEXT,
    college_id TEXT,
    year INTEGER);
```

## Rows

- total=17350

| column | latest | sample | sample |
|---|---|---|---|
| player_id | zuvelpa01 | richmsc01 | goodwto01 |
| college_id | stanford | okstate | fresnost |
| year | 1980 | 2005 | 1988 |

## Columns

- player_id: 6575 distinct
- college_id: 1038 distinct
- year: 151 distinct, int 1864..2014
  - stats: average=1969.49, median=1981


# postseason

```sql
CREATE TABLE postseason (
    year INTEGER,
    round TEXT,
    team_id_winner TEXT,
    league_id_winner TEXT,
    team_id_loser TEXT,
    league_id_loser TEXT,
    wins INTEGER,
    losses INTEGER,
    ties INTEGER);
```

## Rows

- total=307

| column | latest | sample | sample |
|---|---|---|---|
| year | 2015 | 2011 | 2001 |
| round | WS | ALDS2 | ALDS2 |
| team_id_winner | KCA | TEX | NYA |
| league_id_winner | AL | AL | AL |
| team_id_loser | NYN | TBA | OAK |
| league_id_loser | NL | AL | AL |
| wins | 4 | 3 | 3 |
| losses | 1 | 1 | 2 |
| ties | 0 | 0 | 0 |

## Columns

- year: 119 distinct, int 1884..2015
  - stats: average=1981.37, median=1995
- round: "WS"=118, "ALCS"=46, "NLCS"=46, "ALDS1"=21, "ALDS2"=21, "NLDS1"=21, "NLDS2"=21, "ALWC"=4, "NLWC"=4, "AEDIV"=1, "AWDIV"=1, "CS"=1, "NEDIV"=1, "NWDIV"=1
- team_id_winner: 43 distinct
- league_id_winner: "AL"=158, "NL"=148, "AA"=1
- team_id_loser: 45 distinct
- league_id_loser: "NL"=160, "AL"=141, "AA"=6
- wins: 4=168, 3=123, 1=8, 5=5, 6=2, 10=1, int 1..10
- losses: 2=86, 0=82, 1=78, 3=59, 4=1, 5=1, int 0..5
- ties: 0=304, 1=3


# salary

```sql
CREATE TABLE salary (
    year INTEGER,
    team_id TEXT,
    league_id TEXT,
    player_id TEXT,
    salary INTEGER);
```

## Rows

- total=25575

| column | latest | sample | sample |
|---|---|---|---|
| year | 2015 | 1986 | 2015 |
| team_id | WAS | PHI | BOS |
| league_id | NL | NL | AL |
| player_id | zimmery01 | tekulke01 | bogaexa01 |
| salary | 14000000 | 890000 | 543000 |

## Columns

- year: 31 distinct, int 1985..2015
  - stats: average=2000.37, median=2000
- team_id: 35 distinct
- league_id: "NL"=13037, "AL"=12538
- player_id: 4963 distinct
- salary: 3266 distinct, int 0..33000000
  - stats: average=2.00856e+06, median=550000


# team

```sql
CREATE TABLE team (
    year INTEGER,
    league_id TEXT,
    team_id TEXT,
    franchise_id TEXT,
    div_id TEXT,
    rank INTEGER,
    g INTEGER,
    ghome NUMERIC,
    w INTEGER,
    l INTEGER,
    div_win TEXT,
    wc_win TEXT,
    lg_win TEXT,
    ws_win TEXT,
    r INTEGER,
    ab INTEGER,
    h INTEGER,
    double INTEGER,
    triple INTEGER,
    hr INTEGER,
    bb INTEGER,
    so NUMERIC,
    sb NUMERIC,
    cs NUMERIC,
    hbp NUMERIC,
    sf NUMERIC,
    ra INTEGER,
    er INTEGER,
    era NUMERIC,
    cg INTEGER,
    sho INTEGER,
    sv INTEGER,
    ipouts INTEGER,
    ha INTEGER,
    hra INTEGER,
    bba INTEGER,
    soa INTEGER,
    e INTEGER,
    dp NUMERIC,
    fp NUMERIC,
    name TEXT,
    park TEXT,
    attendance NUMERIC,
    bpf INTEGER,
    ppf INTEGER,
    team_id_br TEXT,
    team_id_lahman45 TEXT,
    team_id_retro TEXT);
```


# team_franchise

```sql
CREATE TABLE team_franchise (
    franchise_id TEXT,
    franchise_name TEXT,
    active TEXT,
    na_assoc TEXT);
```

## Rows

- total=120

| column | latest | sample | sample |
|---|---|---|---|
| franchise_id | WST | CLV | BLU |
| franchise_name | Washington Statesmen | Cleveland Spiders | Baltimore Monumentals |
| active | N | N | N |
| na_assoc |  |  |  |

## Columns

- franchise_id: unique identifier
- franchise_name: 99 distinct
- active: "N"=65, "Y"=30, ""=25
- na_assoc: ""=108, "ATH"=1, "ATL"=1, "BNA"=1, "CHC"=1, "CNA"=1, "HAR"=1, "HNA"=1, "NNA"=1, "NYU"=1, "PNA"=1, "SBS"=1, "SNA"=1


# team_half

```sql
CREATE TABLE team_half (
    year INTEGER,
    league_id TEXT,
    team_id TEXT,
    half INTEGER,
    div_id TEXT,
    div_win TEXT,
    rank INTEGER,
    g INTEGER,
    w INTEGER,
    l INTEGER);
```

## Rows

- total=52

| column | latest | sample | sample |
|---|---|---|---|
| year | 1981 | 1981 | 1981 |
| league_id | NL | AL | AL |
| team_id | SLN | CLE | NYA |
| half | 2 | 1 | 1 |
| div_id | E | E | E |
| div_win | N | N | N |
| rank | 2 | 6 | 1 |
| g | 52 | 50 | 56 |
| w | 29 | 26 | 34 |
| l | 23 | 24 | 22 |

## Columns

- year: 1981=52
- league_id: "AL"=28, "NL"=24
- team_id: 26 distinct
- half: 1=26, 2=26
- div_id: "E"=26, "W"=26
- div_win: "N"=52
- rank: 2=9, 5=9, 6=9, 1=8, 4=8, 3=7, 7=2, int 1..7
- g: 52=10, 53=9, 56=6, 50=5, 51=4, 54=4, 57=4, 55=3, 48=2, 60=2, 49=1, 58=1, 59=1, int 48..60
- w: 20 distinct, int 15..37
  - stats: average=26.7115, median=27
- l: 23=10, 22=5, 26=5, 29=5, 21=4, 27=4, 30=3, 20=2, 25=2, 28=2, 33=2, 36=2, 24=1, 32=1, 34=1, 37=1, 39=1, 42=1, int 20..42


- Skipped 15 table(s) due to Profile generation errors: all_star, appearances, batting, batting_postseason, fielding, fielding_outfield, fielding_postseason, hall_of_fame, manager, manager_award, pitching, pitching_postseason, player, player_award_vote, team
