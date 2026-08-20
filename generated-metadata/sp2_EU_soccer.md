# Additional Metadata

## Clarified Semantics

- `Country` / `League`: 1 league per country (11/11 rows); one-to-one via `League.country_id`. `League.name` is the league label (e.g. "England Premier League").
- `Match.country_id` is fully redundant with the league's country: joins against `League.country_id` match 100% (0 mismatches across all 25,979 rows). Use `league_id` alone to locate a match's league/country.
- `Match` is the core fact table: one row per match (id 1..25979), 8 seasons (2008/2009..2015/2016), stages 1..38, up to 11 leagues. `match_api_id` is a unique external key, distinct from the internal `id`.
- `home_team_goal` / `away_team_goal` are aggregated final-score integers (0..10 / 0..9). They are aliases to what the XML streams count, not raw event tables.
- `goal`, `shoton`, `shotoff`, `foulcommit`, `card`, `cross`, `corner`, `possession` are TEXT columns holding full match event streams serialized as XML (the `<...>` dumps). To aggregate counts you must parse the embedded `stats`/`<value>` nodes; NULL when event data is absent (~11,762 rows), so many mega-matches lack event/odds detail.
- Player lineup columns `home_player_N` / `away_player_N` (N=1..11) store the starting XI as FK to `Player.player_api_id`; the `_XN`/`_YN` integer columns are duplicates of the player's pitch slot (formation coordinates), not DB keys. As the `match_view` shows: slot 1 = goalkeeper, 2–5 = back line, 6–9 = midfield, 10–11 = forwards.
- Many lineup-slots have NULLs (~1,200–1,800 per slot); joins on those slots must tolerate missing players.
- `Team_Attributes` and `Player_Attributes` are periodic snapshot tables: a player has many rows (183,978 rows / 11,060 players / 197 dates); a team has ~6 rows / date (1,458 / 288 teams / 6 dates). Use the snapshot valid at/before the match date, not an arbitrary row.
- Betting odds columns (`B365*`, `PS*`, `VCH*`, etc.) are decimal odds (home/draw/away fames). Coverage varies widely: `PS*` only ~41% populated (~14,811 nulls); `SJ*` and `G*/BS*` also heavily null.
- `Player.fifa_api_id` ← `Player_fifa_api_id` and `Player.api_id` are separate, both unique; `Match` and `Player_Attributes` link via `api_id` (not the fifa id), while `Team_Attributes` links to `Team` via both `api_id` and `fifa_api_id`.

## Potential Join Strategies

- League grouping: `Match.league_id = League.id`, then `League.country_id = Country.id` to aggregate by country/league/season. Note `Match` also carries a redundant `country_id`; prefer `league_id` to avoid implying matches belong to a different country (always identical here).
- Team home vs away: `Match.home_team_api_id = Team.team_api_id` and `Match.away_team_api_id = Team.team_api_id` (two distinct joins; for per-team totals UNION both). ~299 distinct team_api_ids appear in matches.
- Team attributes by date: join `Match.team_api_id = Team_Attributes.team_api_id` filtering to the run/card with `Team_Attributes.date <= Match.date`, taking the latest such snapshot; otherwise a team may take on attributes from a season it never played.
- Player attributes by date: `Match.home_player_N = Player_Attributes.player_api_id` (N=1..11) with earliest-dated attributes per player + match-date fetch (correlated subquery / window); same approach for `away_player_N`.
- Squad composition: to map lineups get Player via `Match.home_player_N = Player.player_api_id`, then player attributes via `Player_Attributes.player_api_id = Player.player_api_id`. Beware `home_player_1..11` are only player_api_id; the `_XN/_YN` columns hold on-pitch positions, not attribute keys.
- The `match_view` bundles the above: gives `league`, both team names, all 22 lineup player names, goals, and raw `goal`/`card` XML in one relation — convenient read-only join target.
- Event-level filtering (scorers, cards, possession) requires parsing the XML columns together with `home_player_*`/`away_player_*` to attribute events to a team; XML `player1`/`team` ids are per-match internal event ids.