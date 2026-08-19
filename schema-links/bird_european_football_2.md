# Schema Links

- generator: local introspection
- dialect: sqlite
- database: european_football_2

## Declared Links

- `League.country_id` → `country.id`
- `Match.away_player_1` → `Player.player_api_id`
- `Match.away_player_10` → `Player.player_api_id`
- `Match.away_player_11` → `Player.player_api_id`
- `Match.away_player_2` → `Player.player_api_id`
- `Match.away_player_3` → `Player.player_api_id`
- `Match.away_player_4` → `Player.player_api_id`
- `Match.away_player_5` → `Player.player_api_id`
- `Match.away_player_6` → `Player.player_api_id`
- `Match.away_player_7` → `Player.player_api_id`
- `Match.away_player_8` → `Player.player_api_id`
- `Match.away_player_9` → `Player.player_api_id`
- `Match.away_team_api_id` → `Team.team_api_id`
- `Match.country_id` → `Country.rowid`
- `Match.home_player_1` → `Player.player_api_id`
- `Match.home_player_10` → `Player.player_api_id`
- `Match.home_player_11` → `Player.player_api_id`
- `Match.home_player_2` → `Player.player_api_id`
- `Match.home_player_3` → `Player.player_api_id`
- `Match.home_player_4` → `Player.player_api_id`
- `Match.home_player_5` → `Player.player_api_id`
- `Match.home_player_6` → `Player.player_api_id`
- `Match.home_player_7` → `Player.player_api_id`
- `Match.home_player_8` → `Player.player_api_id`
- `Match.home_player_9` → `Player.player_api_id`
- `Match.home_team_api_id` → `Team.team_api_id`
- `Match.league_id` → `League.rowid`
- `Player_Attributes.player_api_id` → `Player.player_api_id`
- `Player_Attributes.player_fifa_api_id` → `Player.player_fifa_api_id`
- `Team_Attributes.team_api_id` → `Team.team_api_id`
- `Team_Attributes.team_fifa_api_id` → `Team.team_fifa_api_id`

## Same-name Candidates

- `country_id`: `League.country_id`, `Match.country_id`
- `date`: `Match.date`, `Player_Attributes.date`, `Team_Attributes.date`
- `name`: `Country.name`, `League.name`
- `player_api_id`: `Player.player_api_id`, `Player_Attributes.player_api_id`
- `player_fifa_api_id`: `Player.player_fifa_api_id`, `Player_Attributes.player_fifa_api_id`
- `team_api_id`: `Team.team_api_id`, `Team_Attributes.team_api_id`
- `team_fifa_api_id`: `Team.team_fifa_api_id`, `Team_Attributes.team_fifa_api_id`
