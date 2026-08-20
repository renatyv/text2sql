# Schema Links

- version: 0.0.5
- dialect: sqlite
- database: file:/Users/renatyuldashev/Documents/ai-sql/custom-bench/data/sp2_lite_sqlite/databases/Baseball.sqlite
- schema: main

## Declared PK/FK Links

No declared PK/FK links found.

## Inferred Links

### postseason
- inferred: all_star.starting_pos, batting_postseason.bb, batting_postseason.cs, batting_postseason.double, batting_postseason.g, batting_postseason.g_idp, batting_postseason.h, batting_postseason.hbp, batting_postseason.hr, batting_postseason.ibb, batting_postseason.r, batting_postseason.sb, batting_postseason.sf, batting_postseason.sh, batting_postseason.so, batting_postseason.triple, fielding_outfield.stint, fielding_postseason.cs, fielding_postseason.g, fielding_postseason.gs, fielding_postseason.po, fielding_postseason.sb, hall_of_fame.votes, home_game.games, manager.g, manager.inseason, manager.l, manager.rank, manager.w, manager_award_vote.points_max, manager_award_vote.points_won, manager_award_vote.votes_first, manager_half.g, manager_half.inseason, manager_half.rank, manager_half.w, pitching.bk, pitching.cg, pitching.g, pitching.g_idp, pitching.gf, pitching.gs, pitching.hbp, pitching.hr, pitching.ibb, pitching.l, pitching.r, pitching.sf, pitching.sh, pitching.sho, pitching.so, pitching.stint, pitching.w, pitching.wp, pitching_postseason.bb, pitching_postseason.bfp, pitching_postseason.cg, pitching_postseason.er, pitching_postseason.g, pitching_postseason.g_idp, pitching_postseason.gf, pitching_postseason.gs, pitching_postseason.h, pitching_postseason.hbp, pitching_postseason.hr, pitching_postseason.ibb, pitching_postseason.ipouts, pitching_postseason.l, pitching_postseason.r, pitching_postseason.sf, pitching_postseason.sh, pitching_postseason.sho, pitching_postseason.so, pitching_postseason.sv, pitching_postseason.w, pitching_postseason.wp, player_award_vote.points_won, player_award_vote.votes_first, team.cg, team.cs, team.double, team.l, team.rank, team.sb, team.sho, team.sv, team.triple, team.w, team_half.g, team_half.rank

### year
- inferred: all_star.year, batting_postseason.year, fielding_outfield.year, fielding_postseason.year, hall_of_fame.yearid, home_game.year, manager.year, manager_award.year, manager_award_vote.year, manager_half.year, pitching.year, pitching_postseason.year, player.birth_year, player.death_year, player_award.year, player_award_vote.year, player_college.year, postseason.year, salary.year, team.year, team_half.year

### league
- inferred: all_star.league_id, batting_postseason.league_id, fielding_postseason.league_id, home_game.league_id, manager.league_id, manager_award.league_id, manager_award_vote.league_id, manager_half.league_id, pitching.league_id, pitching_postseason.league_id, player_award.league_id, player_award_vote.league_id, postseason.league_id_loser, postseason.league_id_winner, salary.league_id, team.league_id, team_half.league_id

### team
- inferred: all_star.team_id, batting_postseason.team_id, fielding_postseason.team_id, home_game.team_id, manager.team_id, manager_half.team_id, pitching.team_id, pitching_postseason.team_id, postseason.team_id_loser, postseason.team_id_winner, salary.team_id, team.team_id, team.team_id_lahman45, team.team_id_retro, team_half.team_id

### player
- inferred: batting_postseason.player_id, fielding_postseason.player_id, pitching_postseason.player_id, player_award.player_id

### state
- inferred: college.state, park.state, player.birth_state, player.death_state

### city
- inferred: park.city, player.birth_city, player.death_city

### country
- inferred: college.country, player.birth_country, player.death_country

### pitching
- inferred: pitching.bb, pitching.er, team.hr

### team
- inferred: team.franchise_id, team.team_id_br, team_franchise.franchise_id

### college
- inferred: college.college_id, player_college.college_id

### park
- inferred: home_game.park_id, park.park_id

### player
- inferred: player.player_id, player_college.player_id

### player
- inferred: manager.player_id, manager_half.player_id

### shared values
- inferred: all_star.game_num, pitching_postseason.bk

### team
- inferred: team.div_id, team_half.div_id

### team
- inferred: team.name, team_franchise.franchise_name
