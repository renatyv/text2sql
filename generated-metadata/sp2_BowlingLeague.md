# Additional Metadata

## Clarified Semantics

- `Match_Games` represents per-game league match results; every one of its 56 `MatchID`s also exists in `Tourney_Matches`, so it is the per-game detail of a tournament match. `WinningTeamID` is the team that won that individual game.
- `Tourney_Matches` is the parent match header (assigning two teams to odd/even lanes). All 56 `Match_Games` rows join to it on `MatchID`; `Tourney_Matches` has MatchID 57 with no corresponding `Match_Games`/`Bowler_Scores` rows.
- `Bowler_Scores` is per-bowler, per-game detail (1344 = 56 matches × 3 games × 8 active bowlers, BowlerID 1..32). `WonGame` is a per-bowler boolean indicating that bowler beat their lane opponent; it does not consistently equal the match `WinningTeamID` outcome (695 true vs. per-game team wins), so it is not the same event.
- `HandiCapScore` = `RawScore` plus a handicap; it does not always equal `RawScore + BowlerCurrentHcp` stored on `Bowlers`, so a stored/per-game handicap differs from the bowler's current handicap.
- `Teams` 9 ("Huckleberrys") and 10 ("Never Show Ups") have no bowlers assigned — they only appear in `Tourney_Matches` OddLane/EvenLaneTeamID, not in `Bowlers` or `Bowler_Scores`.
- `Teams.CaptainID` references a `Bowlers.BowlerID` (a bowler is captain of a team); no FK is declared.
- `Bowlers` only covers TeamID 1..8; `BowlerTeamID` on `Bowlers` ties each bowler to a league team.
- `WAZips` is a canonical ZIP→City/State lookup (State=WA). Two bowlers have a non-canonical/nested `City` in `Bowlers.BowlerCity` (e.g., "Ballard") not present in `WAZips.City`, so ZIP-based lookups are the reliable join key.

## Potential Join Strategies

- League game → teams: `Bowler_Scores(MatchID, GameNumber)` → `Match_Games(MatchID, GameNumber)` → `Tourney_Matches(MatchID)`. Use this to link a bowler's score to both `WinningTeamID` and the odd/even lane teams. Caveat: dots 24 `Bowler_Scores` rows per match but each game has only 8 participating bowlers (2 teams), so match-level joins must be filtered by team to attribute wins per game.
- Bowler → league team: `Bowler_Scores.BowlerID` → `Bowlers.BowlerID` → `Teams.TeamID`, then compare `Match_Games.WinningTeamID` to `Bowlers.TeamID` to find whose scores correspond to a won game.
- Tournament schedule: `Tourney_Matches.TourneyID` → `Tournaments.TourneyID` for date/location of a match; then `Tourney_Matches.EvenLaneTeamID`/`OddLaneTeamID` → `Teams.TeamID` to get the two opposing teams per match. Note TeamIDs 9/10 appear here but have no bowlers/scores.
- Team captains: `Teams.CaptainID` → `Bowlers.BowlerID` to join captain demographic data to a team; require a self-join on `Bowlers` (no declared FK).
- ZIP geography: `Bowlers.BowlerCity/BowlerZip` → `WAZips(ZIP)` (join on ZIP; City is secondary and imperfect for 2 bowlers) to normalize addresses or aggregate bowlers by canonical city.
- Winning-team aggregation for a match is 1:1 on (`Match_Games.MatchID, GameNumber`); each game has exactly one `WinningTeamID`. Caveat: league `Match_Games.WinningTeamID` spans only TeamID 1–8.