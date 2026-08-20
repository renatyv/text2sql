# Additional Metadata

## Clarified Semantics

- **Match.X/Y composition**: `home_player_X1..11` / `home_player_Y1..11` (and away counterparts) are pitch-position grid coordinates (X = column, Y = row of the 11-slot lineup), whereas `home_player_1..11` / `away_player_1..11` hold the actual `Player.player_api_id` occupying each numbered slot. Slot `i`'s player corresponds to coordinate pair `(X_i, Y_i)`.
- **Player ID keys**: `Match.home_player_*` / `away_player_*`, and `Player_Attributes.player_api_id`, reference `Player.player_api_id` (not `Player.id`). `Player.player_fifa_api_id` and `player_api_id` are alternative unique keys; both are UNIQUE.
- **Time-series snapshots**: `Player_Attributes` is a history of attribute ratings per player (`date` 2007–2016, up to ~56 rows/player, 183,978 rows); `Team_Attributes` is dated team-style snapshots (`date` 2010–2015, up to ~6 rows/team, 1,458 rows). The `date` field selects the snapshot applicable to a given match date.
- **Team coverage**: `Team_Attributes` covers only ~288 of 299 `team_api_id`s, and 11 `Team` rows have null `team_fifa_api_id`.
- **Match event text columns**: `goal`, `shoton`, `shotoff`, `foulcommit`, `card`, `cross`, `corner`, `possession` are per-match XML event breakdowns (e.g. `goal` records incidents with `elapsed`, `type`, `subtype`, `team`, `player1`, `player2`); they are populated for only a subset of matches (~14k of 25,979).
- **Betting odds**: columns are bookmakers (B365, BW, IW, LB, PS, WH, SJ, VC, GB, BS) suffixed H/D/A = home/draw/away win odds; heavy nulls (PS ~14.8k nulls, GB/BS ~11.8k nulls).
- **Consistency invariant**: `League.country_id` and `Match.country_id` always agree (country_id–league_id pairing is consistent), so a match's league unambiguously determines its country.
- **Season format**: `season` is text `"YYYY/YYYY"`; `stage` (1–38) is the matchweek numbering.

## Potential Join Strategies

- **Match → League / Country**: join `Match.league_id = League.id`, then `League.country_id = Country.id` (or `Match.country_id = Country.id` directly) to filter or aggregate matches by league or nation. One-to-one, no fan-out.
- **Team fixtures (both roles)**: to gather all matches for a team, join `Match.home_team_api_id = Team.team_api_id` OR `Match.away_team_api_id = Team.team_api_id`; a team must be matched separately on the home side and away side (unpivot or UNION) because team_api_id only occupies one of the two columns per row.
- **Lineup player joins**: `Match.home_player_N` / `away_player_N` → `Player.player_api_id` to resolve actual player names/attributes for a specific lineup slot; requires N-way iteration across the 11 slots (or repeated joins) to cover the first XI.
- **Player attributes at match time**: join `Player_Attributes.player_api_id = Player.player_api_id` filtered to the closest `Player_Attributes.date` ≤ match date (time-series, many rows per player), then to `Match` via the lineup slot. Do not equate with `Player.id`.
- **Team style at match time**: join `Team_Attributes.team_api_id = Team.team_api_id` (or by `team_fifa_api_id`, which is null for 11 teams) filtered to the snapshot nearest the match date; note 11 teams lack any attributes row.
- **Player object ↔ attributes**: join on `player_api_id` or on `player_fifa_api_id` (both declared); `player_fifa_api_id` is the key used inside `Player_Attributes` alongside `player_api_id`. Cardinality is many (attributes) to one (player), so aggregate or pick one dated row per player.