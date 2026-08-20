# Additional Metadata

## Clarified Semantics
- `Matches` has no PK and ~540k rows (largest table). No indexes/FKs defined; all FK-like relations are implicit by shared values.
- `Matches.winner_id` and `Matches.loser_id` are stored as TEXT but hold numeric Wrestlers.id values (verified: no winner_id/loser_id falls outside Wrestlers.id range). They appear as sequential odd/even (winner/loser) pairs per match.
- `Matches.match_type_id` (TEXT, numeric) references Match_Types.id; many matches use id 1 whose Match_Types.name is blank/None (default/no-stated type), while ids like 8, 9, 25, 33 carry specific labels.
- `Matches.title_id` (TEXT, numeric) references Belts.id and is only populated for title contests; max observed title_id (~9040) is far below the Belts max id (70791), so many belt rows never appear in Matches.
- `Matches.title_change` is a boolean (0/1) flag indicating whether the title changed hands.
- `Matches.duration` is TEXT (e.g. "04:02") and is frequently empty for non-televised/unrecorded bouts; can't be used as numeric without parsing.
- `Matches` columns are typed TEXT for the id-like fields because not all rows are populated (nullable/empty strings), requiring CAST where numeric comparison is needed.
- No declared PK/FK links in the database; only value-overlap-inferred links exist.
- `Promotions` is a tiny dimension (6 rows): 1=WWWF, 230=WWF, 3211=WWE, 9876=WCW, 10963=NXT, 12682=ECW. WWWF (1) and WWF (230) are historical precursors of WWE (3211), so treat them as related when aggregating by current promotion.
- `Cards.event_date` is ISO text; `Cards.event_id`, `location_id`, `promotion_id`, `table_id` are unindexed numeric references.
- `Tables.html`/`url` store full HTML snapshots of card-list pages; `Cards.match_html`/`info_html` and `Cards.url` duplicate card page content, so these carry no relational value beyond identity.

## Potential Join Strategies
- `Matches.card_id = Cards.id` — central 1:many expansion (~540k match rows across 12.6k cards); join is the main route to attach dates/locations/events to individual matches. Cardinality is high; filter via `Cards.event_date` or `promotion_id` early.
- `Cards.event_id = Events.id` — one event (named show/PPV) fans out to many cards; `Events.name` is unique so it also serves as a cleaner label for grouping card counts. Filter: repeated/DVD/taping cycles share event ids.
- `Cards.location_id = Locations.id` — venue/city lookup for cards; `Locations.name` includes venue, city, region in one string (e.g. "Plant City, Florida"), so region filtering must use substring not structured fields.
- `Cards.promotion_id = Promotions.id` — promotion fan-out is highly skewed: promotion 3211 (WWE) and 10963 (NXT) dominate (WWE alone ~6616 cards vs WWWF=229). Include WWWF/WWF ids (1/230) for full-of-history WWE aggregates.
- `Cards.table_id = Tables.id` — maps each card back to its originating listing page (HTML/url snapshot); low analytical value beyond provenance, useful only to de-duplicate or study page structure.
- `Matches.winner_id / Matches.loser_id = Wrestlers.id` — join names to both sides; winner_id/loser_id hold the full match-participant string as *one* Wrestlers row (e.g. "Elton Prince & Grayson Waller & Kit Wilson"), so multi-person teams are a single join row, not decomposed.
- `Matches.title_id = Belts.id` — for title-match analysis; always pair with `Matches.title_change` to distinguish defenses (0) from belt changes (1).
- `Matches.match_type_id = Match_Types.id` — decode match stipulations; watch the blank-name id 1 default and the presence of odd "referee: X" / storyline entries among the 1208 match-type names.