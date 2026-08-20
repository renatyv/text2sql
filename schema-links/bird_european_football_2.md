# Schema Links

- version: 0.0.5
- dialect: sqlite
- database: file:/Users/renatyuldashev/Documents/ai-sql/custom-bench/data/bird_mini_dev/databases/dev_databases/european_football_2/european_football_2.sqlite
- schema: main

## Declared PK/FK Links

Match.away_player_1 -> Player.player_api_id
Match.away_player_10 -> Player.player_api_id
Match.away_player_11 -> Player.player_api_id
Match.away_player_2 -> Player.player_api_id
Match.away_player_3 -> Player.player_api_id
Match.away_player_4 -> Player.player_api_id
Match.away_player_5 -> Player.player_api_id
Match.away_player_6 -> Player.player_api_id
Match.away_player_7 -> Player.player_api_id
Match.away_player_8 -> Player.player_api_id
Match.away_player_9 -> Player.player_api_id
Match.away_team_api_id -> Team.team_api_id
Match.country_id -> Country.id
Match.home_player_1 -> Player.player_api_id
Match.home_player_10 -> Player.player_api_id
Match.home_player_11 -> Player.player_api_id
Match.home_player_2 -> Player.player_api_id
Match.home_player_3 -> Player.player_api_id
Match.home_player_4 -> Player.player_api_id
Match.home_player_5 -> Player.player_api_id
Match.home_player_6 -> Player.player_api_id
Match.home_player_7 -> Player.player_api_id
Match.home_player_8 -> Player.player_api_id
Match.home_player_9 -> Player.player_api_id
Match.home_team_api_id -> Team.team_api_id
Match.league_id -> League.id
Player_Attributes.player_api_id -> Player.player_api_id
Player_Attributes.player_fifa_api_id -> Player.player_fifa_api_id
Team_Attributes.team_api_id -> Team.team_api_id
Team_Attributes.team_fifa_api_id -> Team.team_fifa_api_id

## Inferred Links

### player
- inferred: Match.away_player_X1, Match.away_player_X10, Match.away_player_X11, Match.away_player_X2, Match.away_player_X3, Match.away_player_X4, Match.away_player_X5, Match.away_player_X6, Match.away_player_X7, Match.away_player_X8, Match.away_player_X9, Match.away_player_Y1, Match.away_player_Y10, Match.away_player_Y11, Match.away_player_Y2, Match.away_player_Y3, Match.away_player_Y4, Match.away_player_Y5, Match.away_player_Y6, Match.away_player_Y7, Match.away_player_Y8, Match.away_player_Y9, Match.home_player_X10, Match.home_player_X11, Match.home_player_X2, Match.home_player_X3, Match.home_player_X4, Match.home_player_X5, Match.home_player_X6, Match.home_player_X7, Match.home_player_X8, Match.home_player_X9, Match.home_player_Y10, Match.home_player_Y11, Match.home_player_Y3, Match.home_player_Y4, Match.home_player_Y5, Match.home_player_Y6, Match.home_player_Y7, Match.home_player_Y8, Match.home_player_Y9, Player.id

### team
- inferred: Match.away_team_goal, Match.home_team_goal, Team.id

### Country.id
- inferred: League.country_id
- declared: Match.country_id
