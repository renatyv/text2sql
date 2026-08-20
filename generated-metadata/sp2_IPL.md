# Additional Metadata

## Clarified Semantics

- All tables describe IPL T20 matches (seasons 1-9, dated 2008-2016). `match.outcome_type` is always "Result"; wins are decided either by `win_type` "runs" or "wickets" with `win_margin` as the tally.
- De-facto functional key joining the four ball-level tables (`ball_by_ball`, `batsman_scored`, `extra_runs`, `wicket_taken`) is the composite `(match_id, over_id, ball_id, innings_no)`; no foreign keys are declared.
- `over_id` spans 1-20 (20 overs per innings). `ball_id` ranges 1-9 because an over can exceed 6 scoring balls: `extra_runs` rows ("wides"/"noballs") add deliveries. `innings_no` is 1 or 2.
- `ball_by_ball` has 134,703 deliveries vs 131,259 `batsman_scored` rows (a ~3.4k gap): not every legal/extra delivery produces a `batsman_scored` entry, so scoring splits into batsman-runs (batsman_scored) plus separate `extra_runs` (`extra_type` = wides, legbyes, noballs, byes, penalty, with penalty=1 rare).
- `team_batting`/`team_bowling`/`team_1`/`team_2`/`toss_winner`/`match_winner`/`player_match.team_id` are team_id codes (1-13). Caveat: `team_id=1` appears (60 times as `match.team_1`; 1,429 `player_match` rows) but has no row in `team` (whose ids are 2-13), so it is effectively an orphan/sentinel team with no name.
- `ball_by_ball.striker`, `non_striker`, `bowler`, `wicket_taken.player_out`, and `match.man_of_the_match` are player_id codes resolving to `player.player_id`. Almost all resolve (e.g. `man_of_the_match` 35 and one `non_striker` value are dangling).
- `striker_batting_position` (1-11) is the player's position in the batting order at that moment, not an innings/team ordinal.
- `player_match` records each player's participation per match with `role` (Player/Keeper/Captain/CaptainKeeper), giving per-match team membership and leadership roles.

## Potential Join Strategies

- **Scoring per delivery**: join `ball_by_ball` ↔ `batsman_scored` ← `extra_runs` on `(match_id, over_id, ball_id, innings_no)`; use LEFT JOIN for extras so balls with no run/extra entry are preserved and to avoid double-counting (wides/noballs appear only as `extra_runs`, not batsman runs). Team total = sum of both sources per match/innings.
- **Ball-level to player names**: join `ball_by_ball.striker`, `non_striker`, `bowler` (and `wicket_taken.player_out`, `match.man_of_the_match`) to `player.player_id` to resolve a player's runs, balls faced, bowling workload, or dismissals. Filtering `striker` = a player_id and then joining `batsman_scored` isolates that player's scoring.
- **Match ↔ team**: link `match.team_1`/`team_2`/`toss_winner`/`match_winner` and `player_match.team_id` to `team.team_id`. Use LEFT JOIN and expect team_id=1 rows to be dropped (no matching `team` row), affecting ~60 matches as team_1.
- **Player ↔ team per match**: join `player_match` to `match` on `match_id` and to `team` on `team_id` (or `match.team_1/team_2`) to determine which side a player represented in a given match; `role` distinguishes captains/keepers.
- **Player aggregations across matches**: join `player_match` (distinct matches a player played) with `match` for the season/date filter; `player.player_id` ↔ `wicket_taken.player_out` counts dismissals, `ball_by_ball.bowler` counts wickets/balls, and `ball_by_ball.striker` counts runs/balls faced.