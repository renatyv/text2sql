# Schema Links

- version: 0.0.5
- dialect: sqlite
- database: file:/Users/renatyuldashev/Documents/ai-sql/custom-bench/data/sp2_lite_sqlite/databases/BowlingLeague.sqlite
- schema: main

## Declared PK/FK Links

Bowler_Scores.BowlerID -> Bowlers.BowlerID
Bowler_Scores.MatchID, Bowler_Scores.GameNumber -> Match_Games.MatchID, Match_Games.GameNumber
Bowler_Scores_Archive.MatchID, Bowler_Scores_Archive.GameNumber -> Match_Games_Archive.MatchID, Match_Games_Archive.GameNumber
Bowlers.TeamID -> Teams.TeamID
Tourney_Matches.EvenLaneTeamID -> Teams.TeamID
Tourney_Matches.OddLaneTeamID -> Teams.TeamID
Tourney_Matches.TourneyID -> Tournaments.TourneyID
Tourney_Matches_Archive.TourneyID -> Tournaments_Archive.TourneyID

## Inferred Links

No inferred links found.
