---
generator: db-snooper
version: 0.0.26
generated_at_utc: 2026-08-16T07:18:45.736846Z
dialect: sqlite
database: /Users/renatyuldashev/Documents/ai-sql/custom-bench/data/bird_mini_dev/databases/dev_databases/european_football_2/european_football_2.sqlite
schema: main
---

## Relationships

- Country.id ← Match.country_id
- League.id ← Match.league_id
- Player.player_api_id ← Match.away_player_1, Match.away_player_10, Match.away_player_11, Match.away_player_2, Match.away_player_3, Match.away_player_4, Match.away_player_5, Match.away_player_6, Match.away_player_7, Match.away_player_8, Match.away_player_9, Match.home_player_1, Match.home_player_10, Match.home_player_11, Match.home_player_2, Match.home_player_3, Match.home_player_4, Match.home_player_5, Match.home_player_6, Match.home_player_7, Match.home_player_8, Match.home_player_9, Player_Attributes.player_api_id
- Player.player_fifa_api_id ← Player_Attributes.player_fifa_api_id
- Team.team_api_id ← Match.away_team_api_id, Match.home_team_api_id, Team_Attributes.team_api_id
- Team.team_fifa_api_id ← Team_Attributes.team_fifa_api_id
- country.id ← League.country_id

# Country

```sql
CREATE TABLE `Country` (
	`id`	INTEGER PRIMARY KEY AUTOINCREMENT,
	`name`	TEXT UNIQUE
);
```

## Rows

- total=11

| column | latest | sample | sample |
|---|---|---|---|
| id | 24558 | 4769 | 15722 |
| name | Switzerland | France | Poland |

## Columns

- id: unique identifier, int 1..24558
- name: unique identifier


# League

```sql
CREATE TABLE `League` (
	`id`	INTEGER PRIMARY KEY AUTOINCREMENT,
	`country_id`	INTEGER,
	`name`	TEXT UNIQUE,
	FOREIGN KEY(`country_id`) REFERENCES `country`(`id`)
);
```

## Rows

- total=11

| column | latest | sample | sample |
|---|---|---|---|
| id | 24558 | 10257 | 1 |
| country_id | 24558 | 10257 | 1 |
| name | Switzerland Super League | Italy Serie A | Belgium Jupiler League |

## Columns

- id: unique identifier, int 1..24558
- country_id: unique identifier, int 1..24558
- name: unique identifier


# Match

```sql
CREATE TABLE "Match"
(
    id               INTEGER
        primary key autoincrement,
    country_id       INTEGER
        references Country,
    league_id        INTEGER
        references League,
    season           TEXT,
    stage            INTEGER,
    date             TEXT,
    match_api_id     INTEGER
        unique,
    home_team_api_id INTEGER
        references Team (team_api_id),
    away_team_api_id INTEGER
        references Team (team_api_id),
    home_team_goal   INTEGER,
    away_team_goal   INTEGER,
    home_player_X1   INTEGER,
    home_player_X2   INTEGER,
    home_player_X3   INTEGER,
    home_player_X4   INTEGER,
    home_player_X5   INTEGER,
    home_player_X6   INTEGER,
    home_player_X7   INTEGER,
    home_player_X8   INTEGER,
    home_player_X9   INTEGER,
    home_player_X10  INTEGER,
    home_player_X11  INTEGER,
    away_player_X1   INTEGER,
    away_player_X2   INTEGER,
    away_player_X3   INTEGER,
    away_player_X4   INTEGER,
    away_player_X5   INTEGER,
    away_player_X6   INTEGER,
    away_player_X7   INTEGER,
    away_player_X8   INTEGER,
    away_player_X9   INTEGER,
    away_player_X10  INTEGER,
    away_player_X11  INTEGER,
    home_player_Y1   INTEGER,
    home_player_Y2   INTEGER,
    home_player_Y3   INTEGER,
    home_player_Y4   INTEGER,
    home_player_Y5   INTEGER,
    home_player_Y6   INTEGER,
    home_player_Y7   INTEGER,
    home_player_Y8   INTEGER,
    home_player_Y9   INTEGER,
    home_player_Y10  INTEGER,
    home_player_Y11  INTEGER,
    away_player_Y1   INTEGER,
    away_player_Y2   INTEGER,
    away_player_Y3   INTEGER,
    away_player_Y4   INTEGER,
    away_player_Y5   INTEGER,
    away_player_Y6   INTEGER,
    away_player_Y7   INTEGER,
    away_player_Y8   INTEGER,
    away_player_Y9   INTEGER,
    away_player_Y10  INTEGER,
    away_player_Y11  INTEGER,
    home_player_1    INTEGER
        references Player (player_api_id),
    home_player_2    INTEGER
        references Player (player_api_id),
    home_player_3    INTEGER
        references Player (player_api_id),
    home_player_4    INTEGER
        references Player (player_api_id),
    home_player_5    INTEGER
        references Player (player_api_id),
    home_player_6    INTEGER
        references Player (player_api_id),
    home_player_7    INTEGER
        references Player (player_api_id),
    home_player_8    INTEGER
        references Player (player_api_id),
    home_player_9    INTEGER
        references Player (player_api_id),
    home_player_10   INTEGER
        references Player (player_api_id),
    home_player_11   INTEGER
        references Player (player_api_id),
    away_player_1    INTEGER
        references Player (player_api_id),
    away_player_2    INTEGER
        references Player (player_api_id),
    away_player_3    INTEGER
        references Player (player_api_id),
    away_player_4    INTEGER
        references Player (player_api_id),
    away_player_5    INTEGER
        references Player (player_api_id),
    away_player_6    INTEGER
        references Player (player_api_id),
    away_player_7    INTEGER
        references Player (player_api_id),
    away_player_8    INTEGER
        references Player (player_api_id),
    away_player_9    INTEGER
        references Player (player_api_id),
    away_player_10   INTEGER
        references Player (player_api_id),
    away_player_11   INTEGER
        references Player (player_api_id),
    goal             TEXT,
    shoton           TEXT,
    shotoff          TEXT,
    foulcommit       TEXT,
    card             TEXT,
    "cross"          TEXT,
    corner           TEXT,
    possession       TEXT,
    B365H            REAL,
    B365D            REAL,
    B365A            REAL,
    BWH              REAL,
    BWD              REAL,
    BWA              REAL,
    IWH              REAL,
    IWD              REAL,
    IWA              REAL,
    LBH              REAL,
    LBD              REAL,
    LBA              REAL,
    PSH              REAL,
    PSD              REAL,
    PSA              REAL,
    WHH              REAL,
    WHD              REAL,
    WHA              REAL,
    SJH              REAL,
    SJD              REAL,
    SJA              REAL,
    VCH              REAL,
    VCD              REAL,
    VCA              REAL,
    GBH              REAL,
    GBD              REAL,
    GBA              REAL,
    BSH              REAL,
    BSD              REAL,
    BSA              REAL
);
```

## Rows

- total=25979

| column | latest | sample | sample |
|---|---|---|---|
| id | 25979 | 17675 | 6164 |
| country_id | 24558 | 17642 | 4769 |
| league_id | 24558 | 17642 | 4769 |
| season | 2015/2016 | 2008/2009 | 2011/2012 |
| stage | 9 | 13 | 32 |
| date | 2015-09-23 00:00:00 | 2009-01-04 00:00:00 | 2012-04-16 00:00:00 |
| match_api_id | 1992095 | 509226 | 1020126 |
| home_team_api_id | 10192 | 10213 | 9851 |
| away_team_api_id | 9931 | 9809 | 9831 |
| home_team_goal | 4 | 1 | 3 |
| away_team_goal | 3 | 0 | 1 |
| home_player_X1 | 1 | null | 1 |
| home_player_X2 | 2 | null | 2 |
| home_player_X3 | 4 | null | 4 |
| home_player_X4 | 6 | null | 6 |
| home_player_X5 | 8 | null | 8 |
| home_player_X6 | 2 | null | 4 |
| home_player_X7 | 4 | null | 6 |
| home_player_X8 | 6 | null | 3 |
| home_player_X9 | 8 | null | 5 |
| home_player_X10 | 4 | null | 7 |
| home_player_X11 | 6 | null | 5 |
| away_player_X1 | 1 | null | 1 |
| away_player_X2 | 2 | null | 2 |
| away_player_X3 | 4 | null | 4 |
| away_player_X4 | 6 | null | 6 |
| away_player_X5 | 8 | null | 8 |
| away_player_X6 | 4 | null | 5 |
| away_player_X7 | 6 | null | 4 |
| away_player_X8 | 3 | null | 6 |
| away_player_X9 | 5 | null | 4 |
| away_player_X10 | 7 | null | 6 |
| away_player_X11 | 5 | null | 6 |
| home_player_Y1 | 1 | null | 1 |
| home_player_Y2 | 3 | null | 3 |
| home_player_Y3 | 3 | null | 3 |
| home_player_Y4 | 3 | null | 3 |
| home_player_Y5 | 3 | null | 3 |
| home_player_Y6 | 7 | null | 6 |
| home_player_Y7 | 7 | null | 6 |
| home_player_Y8 | 7 | null | 8 |
| home_player_Y9 | 7 | null | 8 |
| home_player_Y10 | 10 | null | 8 |
| home_player_Y11 | 10 | null | 11 |
| away_player_Y1 | 1 | null | 1 |
| away_player_Y2 | 3 | null | 3 |
| away_player_Y3 | 3 | null | 3 |
| away_player_Y4 | 3 | null | 3 |
| away_player_Y5 | 3 | null | 3 |
| away_player_Y6 | 6 | null | 5 |
| away_player_Y7 | 6 | null | 7 |
| away_player_Y8 | 8 | null | 7 |
| away_player_Y9 | 8 | null | 9 |
| away_player_Y10 | 8 | null | 9 |
| away_player_Y11 | 11 | null | 11 |
| home_player_1 | 274787 | null | 11319 |
| home_player_2 | 492132 | null | 41189 |
| home_player_3 | 108451 | null | 41120 |
| home_player_4 | 25815 | null | 103470 |
| home_player_5 | 94553 | null | 159882 |
| home_player_6 | 384376 | null | 166020 |
| home_player_7 | 598355 | null | 109330 |
| home_player_8 | 36785 | null | 38216 |
| home_player_9 | 45174 | null | 46757 |
| home_player_10 | 302079 | null | 179795 |
| home_player_11 | 71764 | null | 25538 |
| away_player_1 | 156175 | null | 50065 |
| away_player_2 | 95216 | null | 41122 |
| away_player_3 | 172768 | null | 157288 |
| away_player_4 | 22834 | null | 33128 |
| away_player_5 | 458806 | null | 26162 |
| away_player_6 | 207234 | null | 26351 |
| away_player_7 | 25772 | null | 40725 |
| away_player_8 | 40274 | null | 46650 |
| away_player_9 | 34035 | null | 103487 |
| away_player_10 | 41726 | null | 26394 |
| away_player_11 | 527103 | null | 244774 |
| goal | null | null | <goal><value><comment>n</comment><stats><goals>1</goals><shoton>1</shoton></stats><event_incident_typefk>71</event_incident_typefk><elapsed>23</elapsed><player1>46757</player1><sortorder>0</sortorder><team>9851</team><id>2065284</id><n>18</n><type>goal</type><goal_type>n</goal_type></value><value><comment>n</comment><stats><goals>1</goals><shoton>1</shoton></stats><event_incident_typefk>71</event_incident_typefk><elapsed>44</elapsed><player1>166020</player1><sortorder>0</sortorder><team>9851</team><id>2065346</id><n>19</n><type>goal</type><goal_type>n</goal_type></value><value><comment>n</comment><stats><goals>1</goals><shoton>1</shoton></stats><event_incident_typefk>71</event_incident_typefk><elapsed>59</elapsed><player1>26162</player1><sortorder>0</sortorder><team>9831</team><id>2065397</id><n>21</n><type>goal</type><goal_type>n</goal_type></value><value><comment>n</comment><stats><goals>1</goals><shoton>1</shoton></stats><event_incident_typefk>71</event_incident_typefk><elapsed>82</elapsed><player1>38216</player1><sortorder>0</sortorder><team>9851</team><id>2065473</id><n>23</n><type>goal</type><goal_type>n</goal_type></value></goal> |
| shoton | null | null | <shoton /> |
| shotoff | null | null | <shotoff /> |
| foulcommit | null | null | <foulcommit /> |
| card | null | null | <card><value><comment>y</comment><stats><ycards>1</ycards></stats><event_incident_typefk>70</event_incident_typefk><elapsed>30</elapsed><card_type>y</card_type><player1>33128</player1><sortorder>0</sortorder><team>9831</team><n>20</n><type>card</type><id>2065316</id></value><value><comment>y</comment><stats><ycards>1</ycards></stats><event_incident_typefk>70</event_incident_typefk><elapsed>61</elapsed><card_type>y</card_type><player1>26162</player1><sortorder>0</sortorder><team>9831</team><n>22</n><type>card</type><id>2065420</id></value><value><comment>y</comment><stats><ycards>1</ycards></stats><event_incident_typefk>70</event_incident_typefk><elapsed>79</elapsed><card_type>y</card_type><player1>41192</player1><sortorder>0</sortorder><team>9851</team><n>24</n><type>card</type><id>2065474</id></value></card> |
| cross | null | null | <cross /> |
| corner | null | null | <corner /> |
| possession | null | null | <possession /> |
| B365H | null | 2.25 | 1.67 |
| B365D | null | 3 | 3.4 |
| B365A | null | 3.2 | 6 |
| BWH | null | 2.3 | 1.72 |
| BWD | null | 2.85 | 3.25 |
| BWA | null | 3.2 | 5.5 |
| IWH | null | 2.1 | 1.65 |
| IWD | null | 3 | 3.4 |
| IWA | null | 3.1 | 4.8 |
| LBH | null | 2.1 | 1.67 |
| LBD | null | 3.1 | 3.3 |
| LBA | null | 3.1 | 4.5 |
| PSH | null | null | null |
| PSD | null | null | null |
| PSA | null | null | null |
| WHH | null | 2.3 | 1.67 |
| WHD | null | 2.9 | 3.5 |
| WHA | null | 2.9 | 5.5 |
| SJH | null | 2.25 | 1.7 |
| SJD | null | 3 | 3.4 |
| SJA | null | 3.2 | 5.5 |
| VCH | null | 2.2 | 1.7 |
| VCD | null | 3.1 | 3.5 |
| VCA | null | 3 | 6.25 |
| GBH | null | 2.25 | 1.72 |
| GBD | null | 3 | 3.3 |
| GBA | null | 3.1 | 5.25 |
| BSH | null | 2.25 | 1.7 |
| BSD | null | 2.88 | 3.5 |
| BSA | null | 3.1 | 5 |

## Columns

- id: unique identifier, int 1..25979
- country_id: 1729=3040, 4769=3040, 21518=3040, 10257=3017, 7809=2448, 13274=2448, 17642=2052, 15722=1920, 19694=1824, 1=1728, 24558=1422, int 1..24558
- league_id: 1729=3040, 4769=3040, 21518=3040, 10257=3017, 7809=2448, 13274=2448, 17642=2052, 15722=1920, 19694=1824, 1=1728, 24558=1422, int 1..24558
- season: "2008/2009"=3326, "2015/2016"=3326, "2014/2015"=3325, "2010/2011"=3260, "2012/2013"=3260, "2009/2010"=3230, "2011/2012"=3220, "2013/2014"=3032
- stage: 38 distinct, int 1..38
  - stats: average=18.2428, median=18
- date: 1694 distinct
- match_api_id: unique identifier, int 483129..2216672
- home_team_api_id: 299 distinct, int 1601..274581
- away_team_api_id: 299 distinct, int 1601..274581
- home_team_goal: 1=8400, 2=6339, 0=5896, 3=3288, 4=1385, 5=457, 6=161, 7=38, 8=9, 9=4, 10=2, int 0..10
- away_team_goal: 1=8989, 0=8687, 2=5146, 3=2145, 4=718, 5=215, 6=63, 7=10, 8=5, 9=1, int 0..9
- home_player_X1: 1=24146, 0=11, 2=1, nulls=1821, int 0..2
- home_player_X2: 2=22229, 3=1414, 1=258, 4=188, 6=31, 8=19, 0=11, 5=6, 7=2, nulls=1821, int 0..8
- home_player_X3: 4=22575, 5=920, 6=274, 3=257, 8=70, 2=33, 7=17, 1=1, nulls=1832, int 1..8
- home_player_X4: 6=21967, 7=1409, 8=313, 5=264, 2=93, 4=92, 3=9, nulls=1832, int 2..8
- home_player_X5: 8=22056, 1=796, 2=690, 7=253, 6=175, 4=120, 5=27, 3=24, 9=6, nulls=1832, int 1..9
- home_player_X6: 4=7549, 2=7245, 3=6034, 5=1960, 1=932, 9=255, 6=121, 7=37, 8=14, nulls=1832, int 1..9
- home_player_X7: 4=8073, 6=7526, 5=5998, 3=1543, 2=796, 7=161, 8=41, 9=7, 1=2, nulls=1832, int 1..9
- home_player_X8: 6=8069, 3=6302, 7=5991, 5=1603, 8=828, 4=747, 2=584, 9=17, 1=6, nulls=1832, int 1..9
- home_player_X9: 8=7757, 5=7686, 3=4738, 7=1524, 4=826, 9=809, 6=756, 2=45, 1=6, nulls=1832, int 1..9
- home_player_X10: 4=9696, 7=6357, 5=5522, 9=921, 6=874, 8=682, 3=76, 1=10, 2=9, nulls=1832, int 1..9
- home_player_X11: 6=9796, 5=9571, 7=4654, 4=65, 3=59, 1=2, nulls=1832, int 1..7
- away_player_X1: 1=24144, 2=2, 6=1, nulls=1832, int 1..6
- away_player_X2: 2=22109, 3=1469, 1=329, 4=175, 6=28, 8=28, 5=7, 7=2, nulls=1832, int 1..8
- away_player_X3: 4=22465, 5=967, 3=331, 6=271, 8=65, 2=34, 7=13, 9=1, nulls=1832, int 2..9
- away_player_X4: 6=21856, 7=1468, 5=331, 8=325, 2=88, 4=69, 3=7, 1=3, nulls=1832, int 1..8
- away_player_X5: 8=21915, 1=837, 2=695, 7=321, 6=175, 4=152, 3=21, 5=19, 9=12, nulls=1832, int 1..9
- away_player_X6: 4=7564, 2=6865, 3=6038, 5=1978, 1=1214, 9=322, 6=117, 7=37, 8=12, nulls=1832, int 1..9
- away_player_X7: 4=7637, 6=7530, 5=6022, 3=1868, 2=914, 7=137, 8=35, 1=3, 9=1, nulls=1832, int 1..9
- away_player_X8: 6=7621, 3=6268, 7=6007, 5=1894, 4=905, 8=858, 2=574, 9=17, 1=3, nulls=1832, int 1..9
- away_player_X9: 5=7525, 8=7350, 3=4749, 7=1823, 6=929, 4=879, 9=847, 2=39, 1=5, nulls=1833, int 1..9
- away_player_X10: 4=9193, 7=6332, 5=5544, 9=1206, 6=921, 8=840, 3=97, 2=8, 1=5, nulls=1833, int 1..9
- away_player_X11: 5=10043, 6=9322, 7=4664, 4=61, 3=49, 8=1, nulls=1839, int 3..8
- home_player_Y1: 1=24146, 0=11, 3=1, nulls=1821, int 0..3
- home_player_Y2: 3=24147, 0=11, nulls=1821
- home_player_Y3: 3=24146, 5=1, nulls=1832
- home_player_Y4: 3=24142, 5=5, nulls=1832
- home_player_Y5: 3=22691, 7=1403, 5=45, 6=7, 8=1, nulls=1832, int 3..8
- home_player_Y6: 7=14027, 6=7967, 5=1793, 3=288, 8=69, 9=3, nulls=1832, int 3..9
- home_player_Y7: 7=15634, 6=7016, 5=795, 8=694, 9=5, 3=3, nulls=1832, int 3..9
- home_player_Y8: 7=15943, 8=7194, 6=519, 5=463, 9=21, 3=6, 10=1, nulls=1832, int 3..10
- home_player_Y9: 7=10024, 8=8041, 10=4772, 9=1247, 6=62, 1=1, nulls=1832, int 1..10
- home_player_Y10: 10=13568, 8=7083, 9=1516, 7=1188, 11=711, 6=80, 3=1, nulls=1832, int 3..11
- home_player_Y11: 10=13567, 11=10577, 1=2, 3=1, nulls=1832, int 1..11
- away_player_Y1: 1=24144, 3=3, nulls=1832
- away_player_Y2: 3=24147, nulls=1832
- away_player_Y3: 3=24146, 7=1, nulls=1832
- away_player_Y4: 3=24145, 5=1, 7=1, nulls=1832, int 3..7
- away_player_Y5: 3=22645, 7=1448, 5=38, 6=15, 9=1, nulls=1832, int 3..9
- away_player_Y6: 7=13954, 6=8054, 5=1715, 3=350, 8=70, 9=3, 10=1, nulls=1832, int 3..10
- away_player_Y7: 7=15607, 6=7037, 8=772, 5=725, 3=3, 9=2, 10=1, nulls=1832, int 3..10
- away_player_Y8: 7=15903, 8=7265, 6=541, 5=412, 9=22, 10=3, 3=1, nulls=1832, int 3..10
- away_player_Y9: 7=10043, 8=8057, 10=4767, 9=1199, 6=78, 5=1, 11=1, nulls=1833, int 5..11
- away_player_Y10: 10=13145, 8=7173, 7=1575, 9=1518, 11=655, 6=80, nulls=1833, int 6..11
- away_player_Y11: 10=13145, 11=10993, 7=1, 8=1, nulls=1839, int 7..11
- home_player_1: 906 distinct, nulls=1224, int 2984..698273
  - stats: average=76638.4, median=38230
- home_player_2: 2414 distinct, nulls=1315, int 2802..748432
  - stats: average=106854, median=42388
- home_player_3: 2375 distinct, nulls=1281, int 2752..705484
  - stats: average=91601.3, median=39731
- home_player_4: 2606 distinct, nulls=1323, int 2752..723037
  - stats: average=94540.2, median=41060
- home_player_5: 2769 distinct, nulls=1316, int 2752..733787
  - stats: average=109528, median=45996
- home_player_6: 3798 distinct, nulls=1325, int 2625..750584
  - stats: average=102309, median=41467
- home_player_7: 3422 distinct, nulls=1227, int 2625..692984
  - stats: average=97287.6, median=41432
- home_player_8: 4076 distinct, nulls=1309, int 2625..693171
  - stats: average=107291, median=43319
- home_player_9: 4114 distinct, nulls=1273, int 2625..730065
  - stats: average=111132, median=45605
- home_player_10: 3642 distinct, nulls=1436, int 2625..742405
  - stats: average=105613, median=43296
- home_player_11: 2890 distinct, nulls=1555, int 2802..726956
  - stats: average=103414, median=42091
- away_player_1: 926 distinct, nulls=1234, int 2796..698273
  - stats: average=76628.2, median=38289
- away_player_2: 2504 distinct, nulls=1278, int 2790..748432
  - stats: average=107615, median=42388
- away_player_3: 2470 distinct, nulls=1293, int 2752..705484
  - stats: average=91126.8, median=39892
- away_player_4: 2657 distinct, nulls=1321, int 2752..728414
  - stats: average=95083.9, median=41083
- away_player_5: 2884 distinct, nulls=1335, int 2790..746419
  - stats: average=109801, median=46212
- away_player_6: 3930 distinct, nulls=1313, int 2625..722766
  - stats: average=102308, median=41634.5
- away_player_7: 3620 distinct, nulls=1235, int 2625..750435
  - stats: average=97898.1, median=41433
- away_player_8: 4249 distinct, nulls=1341, int 2625..717248
  - stats: average=109265, median=45816
- away_player_9: 4319 distinct, nulls=1328, int 2625..722766
  - stats: average=111087, median=45860
- away_player_10: 3891 distinct, nulls=1441, int 2770..722766
  - stats: average=107149, median=45358
- away_player_11: 3040 distinct, nulls=1554, int 2802..726956
  - stats: average=104933, median=42652
- goal: 13225 distinct, nulls=11762
- shoton: 8464 distinct, nulls=11762
- shotoff: 8464 distinct, nulls=11762
- foulcommit: 8466 distinct, nulls=11762
- card: 13777 distinct, nulls=11762
- cross: 8466 distinct, nulls=11762
- corner: 8465 distinct, nulls=11762
- possession: 8420 distinct, nulls=11762
- B365H: 121 distinct, nulls=3387, num 1.04..26
  - stats: average=2.62882, median=2.1
- B365D: 72 distinct, nulls=3387, num 1.4..17
  - stats: average=3.83968, median=3.5
- B365A: 115 distinct, nulls=3387, num 1.08..51
  - stats: average=4.66222, median=3.5
- BWH: 237 distinct, nulls=3404, num 1.03..34
  - stats: average=2.55924, median=2.1
- BWD: 133 distinct, nulls=3404, num 1.65..19.5
  - stats: average=3.7476, median=3.4
- BWA: 261 distinct, nulls=3404, num 1.1..51
  - stats: average=4.39695, median=3.4
- IWH: 147 distinct, nulls=3459, num 1.03..20
  - stats: average=2.46761, median=2.1
- IWD: 73 distinct, nulls=3459, num 1.5..11
  - stats: average=3.60893, median=3.3
- IWA: 159 distinct, nulls=3459, num 1.1..25
  - stats: average=4.15058, median=3.3
- LBH: 129 distinct, nulls=3423, num 1.04..26
  - stats: average=2.5362, median=2.1
- LBD: 72 distinct, nulls=3423, num 1.4..19
  - stats: average=3.71174, median=3.4
- LBA: 128 distinct, nulls=3423, num 1.1..51
  - stats: average=4.38535, median=3.3
- PSH: 948 distinct, nulls=14811, num 1.04..36
  - stats: average=2.81645, median=2.2
- PSD: 665 distinct, nulls=14811, num 2.2..29
  - stats: average=4.13232, median=3.64
- PSA: 1475 distinct, nulls=14811, num 1.09..47.5
  - stats: average=4.97274, median=3.61
- WHH: 125 distinct, nulls=3408, num 1.02..26
  - stats: average=2.57874, median=2.15
- WHD: 78 distinct, nulls=3408, num 1.02..17
  - stats: average=3.6653, median=3.3
- WHA: 136 distinct, nulls=3408, num 1.08..51
  - stats: average=4.48259, median=3.4
- SJH: 137 distinct, nulls=8882, num 1.04..23
  - stats: average=2.56606, median=2.1
- SJD: 79 distinct, nulls=8882, num 1.4..15
  - stats: average=3.75588, median=3.4
- SJA: 132 distinct, nulls=8882, num 1.1..41
  - stats: average=4.62234, median=3.5
- VCH: 160 distinct, nulls=3411, num 1.03..36
  - stats: average=2.66811, median=2.15
- VCD: 82 distinct, nulls=3411, num 1.62..26
  - stats: average=3.89905, median=3.5
- VCA: 151 distinct, nulls=3411, num 1.08..67
  - stats: average=4.84028, median=3.5
- GBH: 159 distinct, nulls=11817, num 1.05..21
  - stats: average=2.49876, median=2.1
- GBD: 84 distinct, nulls=11817, num 1.45..11
  - stats: average=3.64819, median=3.3
- GBA: 172 distinct, nulls=11817, num 1.12..34
  - stats: average=4.3531, median=3.4
- BSH: 101 distinct, nulls=11818, num 1.04..17
  - stats: average=2.49789, median=2.1
- BSD: 59 distinct, nulls=11818, num 1.33..13
  - stats: average=3.66074, median=3.4
- BSA: 96 distinct, nulls=11818, num 1.12..34
  - stats: average=4.40566, median=3.4


# Player

```sql
CREATE TABLE `Player` (
	`id`	INTEGER PRIMARY KEY AUTOINCREMENT,
	`player_api_id`	INTEGER UNIQUE,
	`player_name`	TEXT,
	`player_fifa_api_id`	INTEGER UNIQUE,
	`birthday`	TEXT,
	`height`	INTEGER,
	`weight`	INTEGER
);
```

## Rows

- total=11060

| column | latest | sample | sample |
|---|---|---|---|
| id | 11075 | 5587 | 506 |
| player_api_id | 39902 | 243501 | 27667 |
| player_name | Zvjezdan Misimovic | Kai Heerings | Alfonso De Lucia |
| player_fifa_api_id | 102359 | 205672 | 149599 |
| birthday | 1982-06-05 00:00:00 | 1990-01-12 00:00:00 | 1983-11-12 00:00:00 |
| height | 180 | 190 | 185 |
| weight | 176 | 179 | 185 |

## Columns

- id: unique identifier, int 1..11075
- player_api_id: unique identifier, int 2625..750584
- player_name: 10848 distinct
- player_fifa_api_id: unique identifier, int 2..234141
- birthday: 5762 distinct
- height: 20 distinct, int 157..208
  - stats: average=181.284, median=182
- weight: 50 distinct, int 117..243
  - stats: average=168.38, median=168


# Player_Attributes

```sql
CREATE TABLE "Player_Attributes" (
	`id`	INTEGER PRIMARY KEY AUTOINCREMENT,
	`player_fifa_api_id`	INTEGER,
	`player_api_id`	INTEGER,
	`date`	TEXT,
	`overall_rating`	INTEGER,
	`potential`	INTEGER,
	`preferred_foot`	TEXT,
	`attacking_work_rate`	TEXT,
	`defensive_work_rate`	TEXT,
	`crossing`	INTEGER,
	`finishing`	INTEGER,
	`heading_accuracy`	INTEGER,
	`short_passing`	INTEGER,
	`volleys`	INTEGER,
	`dribbling`	INTEGER,
	`curve`	INTEGER,
	`free_kick_accuracy`	INTEGER,
	`long_passing`	INTEGER,
	`ball_control`	INTEGER,
	`acceleration`	INTEGER,
	`sprint_speed`	INTEGER,
	`agility`	INTEGER,
	`reactions`	INTEGER,
	`balance`	INTEGER,
	`shot_power`	INTEGER,
	`jumping`	INTEGER,
	`stamina`	INTEGER,
	`strength`	INTEGER,
	`long_shots`	INTEGER,
	`aggression`	INTEGER,
	`interceptions`	INTEGER,
	`positioning`	INTEGER,
	`vision`	INTEGER,
	`penalties`	INTEGER,
	`marking`	INTEGER,
	`standing_tackle`	INTEGER,
	`sliding_tackle`	INTEGER,
	`gk_diving`	INTEGER,
	`gk_handling`	INTEGER,
	`gk_kicking`	INTEGER,
	`gk_positioning`	INTEGER,
	`gk_reflexes`	INTEGER,
	FOREIGN KEY(`player_fifa_api_id`) REFERENCES `Player`(`player_fifa_api_id`),
	FOREIGN KEY(`player_api_id`) REFERENCES `Player`(`player_api_id`)
);
```

## Rows

- total=183978

| column | latest | sample | sample |
|---|---|---|---|
| id | 183978 | 112529 | 13636 |
| player_fifa_api_id | 102359 | 192638 | 159302 |
| player_api_id | 39902 | 196169 | 23369 |
| date | 2007-02-22 00:00:00 | 2015-01-16 00:00:00 | 2015-07-31 00:00:00 |
| overall_rating | 80 | 68 | 71 |
| potential | 81 | 74 | 71 |
| preferred_foot | right | left | right |
| attacking_work_rate | medium | high | medium |
| defensive_work_rate | low | medium | medium |
| crossing | 74 | 70 | 58 |
| finishing | 68 | 49 | 25 |
| heading_accuracy | 57 | 53 | 73 |
| short_passing | 88 | 65 | 64 |
| volleys | 77 | 32 | 25 |
| dribbling | 87 | 63 | 59 |
| curve | 86 | 60 | 50 |
| free_kick_accuracy | 53 | 70 | 31 |
| long_passing | 78 | 60 | 56 |
| ball_control | 91 | 66 | 64 |
| acceleration | 58 | 69 | 67 |
| sprint_speed | 64 | 72 | 64 |
| agility | 77 | 66 | 66 |
| reactions | 66 | 74 | 61 |
| balance | 73 | 56 | 72 |
| shot_power | 72 | 74 | 26 |
| jumping | 58 | 66 | 75 |
| stamina | 67 | 78 | 78 |
| strength | 59 | 69 | 76 |
| long_shots | 78 | 70 | 24 |
| aggression | 63 | 72 | 85 |
| interceptions | 63 | 66 | 74 |
| positioning | 68 | 60 | 22 |
| vision | 88 | 43 | 43 |
| penalties | 53 | 63 | 47 |
| marking | 38 | 66 | 73 |
| standing_tackle | 32 | 69 | 77 |
| sliding_tackle | 30 | 69 | 74 |
| gk_diving | 9 | 8 | 15 |
| gk_handling | 9 | 6 | 15 |
| gk_kicking | 78 | 12 | 8 |
| gk_positioning | 7 | 8 | 14 |
| gk_reflexes | 15 | 11 | 7 |

## Columns

- id: unique identifier, int 1..183978
- player_fifa_api_id: int 2..234141
- player_api_id: int 2625..750584
- date: profile metrics skipped
- overall_rating: nulls=836, int 33..94
  - stats: average=68.6
- potential: nulls=836, int 39..97
  - stats: average=73.4604
- preferred_foot: nulls=836
- attacking_work_rate: nulls=3230
- defensive_work_rate: nulls=836
- crossing: nulls=836, int 1..95
  - stats: average=55.0869
- finishing: nulls=836, int 1..97
  - stats: average=49.9211
- heading_accuracy: nulls=836, int 1..98
  - stats: average=57.266
- short_passing: nulls=836, int 3..97
  - stats: average=62.4297
- volleys: nulls=2713, int 1..93
  - stats: average=49.4684
- dribbling: nulls=836, int 1..97
  - stats: average=59.1752
- curve: nulls=2713, int 2..94
  - stats: average=52.9657
- free_kick_accuracy: nulls=836, int 1..97
  - stats: average=49.381
- long_passing: nulls=836, int 3..97
  - stats: average=57.0699
- ball_control: nulls=836, int 5..97
  - stats: average=63.3889
- acceleration: nulls=836, int 10..97
  - stats: average=67.6594
- sprint_speed: nulls=836, int 12..97
  - stats: average=68.0512
- agility: nulls=2713, int 11..96
  - stats: average=65.9709
- reactions: nulls=836, int 17..96
  - stats: average=66.1037
- balance: nulls=2713, int 12..96
  - stats: average=65.1895
- shot_power: nulls=836, int 2..97
  - stats: average=61.8084
- jumping: nulls=2713, int 14..96
  - stats: average=66.969
- stamina: nulls=836, int 10..96
  - stats: average=67.0385
- strength: nulls=836, int 10..96
  - stats: average=67.4245
- long_shots: nulls=836, int 1..96
  - stats: average=53.3394
- aggression: nulls=836, int 6..97
  - stats: average=60.948
- interceptions: nulls=836, int 1..96
  - stats: average=52.0093
- positioning: nulls=836, int 2..96
  - stats: average=55.7865
- vision: nulls=2713, int 1..97
  - stats: average=57.8735
- penalties: nulls=836, int 2..96
  - stats: average=55.004
- marking: nulls=836, int 1..96
  - stats: average=46.7722
- standing_tackle: nulls=836, int 1..95
  - stats: average=50.3513
- sliding_tackle: nulls=2713, int 2..95
  - stats: average=48.0015
- gk_diving: nulls=836, int 1..94
  - stats: average=14.7044
- gk_handling: nulls=836, int 1..93
  - stats: average=16.0636
- gk_kicking: nulls=836, int 1..97
  - stats: average=20.9984
- gk_positioning: nulls=836, int 1..96
  - stats: average=16.1322
- gk_reflexes: nulls=836, int 1..96
  - stats: average=16.4414


# Team

```sql
CREATE TABLE "Team" (
	`id`	INTEGER PRIMARY KEY AUTOINCREMENT,
	`team_api_id`	INTEGER UNIQUE,
	`team_fifa_api_id`	INTEGER,
	`team_long_name`	TEXT,
	`team_short_name`	TEXT
);
```

## Rows

- total=299

| column | latest | sample | sample |
|---|---|---|---|
| id | 51606 | 6 | 1513 |
| team_api_id | 7896 | 8635 | 1773 |
| team_fifa_api_id | null | 229 | 100087 |
| team_long_name | Lugano | RSC Anderlecht | Oud-Heverlee Leuven |
| team_short_name | LUG | AND | O-H |

## Columns

- id: unique identifier, int 1..51606
- team_api_id: unique identifier, int 1601..274581
- team_fifa_api_id: 285 distinct, nulls=11, int 1..112513
- team_long_name: 296 distinct
- team_short_name: 259 distinct


# Team_Attributes

```sql
CREATE TABLE `Team_Attributes` (
	`id`	INTEGER PRIMARY KEY AUTOINCREMENT,
	`team_fifa_api_id`	INTEGER,
	`team_api_id`	INTEGER,
	`date`	TEXT,
	`buildUpPlaySpeed`	INTEGER,
	`buildUpPlaySpeedClass`	TEXT,
	`buildUpPlayDribbling`	INTEGER,
	`buildUpPlayDribblingClass`	TEXT,
	`buildUpPlayPassing`	INTEGER,
	`buildUpPlayPassingClass`	TEXT,
	`buildUpPlayPositioningClass`	TEXT,
	`chanceCreationPassing`	INTEGER,
	`chanceCreationPassingClass`	TEXT,
	`chanceCreationCrossing`	INTEGER,
	`chanceCreationCrossingClass`	TEXT,
	`chanceCreationShooting`	INTEGER,
	`chanceCreationShootingClass`	TEXT,
	`chanceCreationPositioningClass`	TEXT,
	`defencePressure`	INTEGER,
	`defencePressureClass`	TEXT,
	`defenceAggression`	INTEGER,
	`defenceAggressionClass`	TEXT,
	`defenceTeamWidth`	INTEGER,
	`defenceTeamWidthClass`	TEXT,
	`defenceDefenderLineClass`	TEXT,
	FOREIGN KEY(`team_fifa_api_id`) REFERENCES `Team`(`team_fifa_api_id`),
	FOREIGN KEY(`team_api_id`) REFERENCES `Team`(`team_api_id`)
);
```

## Rows

- total=1458

| column | latest | sample | sample |
|---|---|---|---|
| id | 1458 | 1400 | 847 |
| team_fifa_api_id | 15005 | 1917 | 70 |
| team_api_id | 10000 | 8528 | 10249 |
| date | 2015-09-10 00:00:00 | 2011-02-22 00:00:00 | 2012-02-22 00:00:00 |
| buildUpPlaySpeed | 54 | 35 | 52 |
| buildUpPlaySpeedClass | Balanced | Balanced | Balanced |
| buildUpPlayDribbling | 42 | null | null |
| buildUpPlayDribblingClass | Normal | Little | Little |
| buildUpPlayPassing | 51 | 50 | 47 |
| buildUpPlayPassingClass | Mixed | Mixed | Mixed |
| buildUpPlayPositioningClass | Organised | Organised | Organised |
| chanceCreationPassing | 47 | 45 | 48 |
| chanceCreationPassingClass | Normal | Normal | Normal |
| chanceCreationCrossing | 52 | 65 | 49 |
| chanceCreationCrossingClass | Normal | Normal | Normal |
| chanceCreationShooting | 32 | 50 | 52 |
| chanceCreationShootingClass | Little | Normal | Normal |
| chanceCreationPositioningClass | Organised | Organised | Organised |
| defencePressure | 44 | 45 | 34 |
| defencePressureClass | Medium | Medium | Medium |
| defenceAggression | 58 | 55 | 43 |
| defenceAggressionClass | Press | Press | Press |
| defenceTeamWidth | 37 | 65 | 37 |
| defenceTeamWidthClass | Normal | Normal | Normal |
| defenceDefenderLineClass | Cover | Cover | Cover |

## Columns

- id: unique identifier, int 1..1458
- team_fifa_api_id: 285 distinct, int 1..112513
- team_api_id: 288 distinct, int 1601..274581
- date: "2015-09-10 00:00:00"=245, "2011-02-22 00:00:00"=244, "2014-09-19 00:00:00"=244, "2012-02-22 00:00:00"=242, "2013-09-20 00:00:00"=242, "2010-02-22 00:00:00"=241
- buildUpPlaySpeed: 57 distinct, int 20..80
  - stats: average=52.4623, median=52
- buildUpPlaySpeedClass: "Balanced"=1184, "Fast"=172, "Slow"=102
- buildUpPlayDribbling: 49 distinct, nulls=969, int 24..77
  - stats: average=48.6074, median=49
- buildUpPlayDribblingClass: "Little"=1004, "Normal"=433, "Lots"=21
- buildUpPlayPassing: 58 distinct, int 20..80
  - stats: average=48.4904, median=50
- buildUpPlayPassingClass: "Mixed"=1236, "Short"=128, "Long"=94
- buildUpPlayPositioningClass: "Organised"=1386, "Free Form"=72
- chanceCreationPassing: 50 distinct, int 21..80
  - stats: average=52.1653, median=52
- chanceCreationPassingClass: "Normal"=1231, "Risky"=171, "Safe"=56
- chanceCreationCrossing: 56 distinct, int 20..80
  - stats: average=53.7318, median=53
- chanceCreationCrossingClass: "Normal"=1195, "Lots"=211, "Little"=52
- chanceCreationShooting: 57 distinct, int 22..80
  - stats: average=53.9691, median=53
- chanceCreationShootingClass: "Normal"=1224, "Lots"=197, "Little"=37
- chanceCreationPositioningClass: "Organised"=1309, "Free Form"=149
- defencePressure: 48 distinct, int 23..72
  - stats: average=46.0171, median=45
- defencePressureClass: "Medium"=1243, "Deep"=154, "High"=61
- defenceAggression: 47 distinct, int 24..72
  - stats: average=49.251, median=48
- defenceAggressionClass: "Press"=1274, "Double"=99, "Contain"=85
- defenceTeamWidth: 43 distinct, int 29..73
  - stats: average=52.1859, median=52
- defenceTeamWidthClass: "Normal"=1286, "Wide"=111, "Narrow"=61
- defenceDefenderLineClass: "Cover"=1362, "Offside Trap"=96
