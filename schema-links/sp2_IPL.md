# Schema Links

- version: 0.0.5
- dialect: sqlite
- database: file:/Users/renatyuldashev/Documents/ai-sql/custom-bench/data/sp2_lite_sqlite/databases/IPL.sqlite
- schema: main

## Declared PK/FK Links

No declared PK/FK links found.

## Inferred Links

### team
- inferred: match.team_1, match.team_2, player_match.team_id, team.team_id

### player
- inferred: player.player_id, player_match.player_id, wicket_taken.player_out
