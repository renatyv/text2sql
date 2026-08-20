# Additional Metadata

## Clarified Semantics

- `sets.type` is a categorical list not in the profile: values include core, expansion, masters, starter, commander, duel_deck, promo, token, masterpiece, meme/funny, from_the_vault, planechase, archenemy, vanguard, box, spellbook, premium_deck, memorabilia, treasure_chest, draft_innovation.
- `sets.parentCode` is not a real FK but a soft self-reference to `sets.code`: it flags a side/supplementary set (e.g. promo or special print run) whose "parent" is the main expansion set; a set can have multiple children with a common parent (e.g. ZNR has 6).
- `cards.otherFaceIds` is a soft self-reference to `cards.uuid`: it stores the UUID(s) of the opposite face of multi-faced cards (transform, modal_dfc, split, aftermath, flip, meld). Most values resolve to an existing card row (1348 of 1367 in the sample resolve). The `side` column ('a'/'b'/'c'...) marks which face the row represents; `faceName`, `faceConvertedManaCost` hold per-face data for these rows.
- `cards.variations` is a soft reference to `cards.uuid` (often comma-separated list) listing alternate printings/versions (border, foil, showcase) of the same card; null for ~48186 rows.
- `cards.scryfallOracleId` groups functionally identical printings (many card rows across sets share the same oracle id), distinct from the per-print `scryfallId`.
- `legalities.status` is a single-word status only (e.g. "Legal", "Banned", "Restricted", "Not Legal"; "Legal" dominates all formats); `format` is the banned-list format name (commander, vintage, legacy, modern, pauper, pioneer, historic, duel, penny, premodern, etc.).
- Handy card metadata conventions: `convertedManaCost` one-row oddity "1e+06" (for a card with X+1M CMC) and `0.5` (halves); `power`/`toughness`/'life'/'hand' are text (may be "*", "X", or non-numeric) and only populated for creatures/vanguards/planeswalkers where relevant.
- `set_translations` holds ~10 foreign languages (121 codes each, 504 distinct translated names), 231 translations null.

## Potential Join Strategies

- `set_translations.setCode` ↔ `sets.code` (declared FK): join set to its foreign-language name; useful to constrain/filter sets by either English or translated name. Cardinality: many-to-one (set appears up to ~10 language rows), so aggregate or pick `language` to avoid row multiplication.
- `legalities.uuid` ↔ `cards.uuid` (declared FK): map each card to its format-status rows. Note legalities is the largest table (~428k rows, ~18k distinct uuids), so joining to it on an unrestricted subset expands many card rows; filter by `legalities.format`/`status` in the WHERE or distinct to control cardinality.
- `rulings.uuid` ↔ `cards.uuid` (declared FK): rulings are many-to-one per card (26k distinct uuids across 88k rows); join only when card-level ruling text is needed.
- `foreign_data.uuid` ↔ `cards.uuid` (declared FK): row-multiplying many-to-one; a card has one row per non-English `language`. Constrain `language` if you only need one translation.
- `cards.otherFaceIds` self-join on `cards.uuid = cards.otherFaceIds` (not declared, but resolves): pairs the two faces of transform/split/aftermath cards. Filter `layout` to the multi-face layouts and note the 19 orphan ids with no matching row.
- `cards.variations` → `cards.uuid`: relates a printed card to its alternate-printing rows (split ids by comma when joining).
- `cards.scryfallOracleId` self-group: collates all printings of a same underlying card; use it (not `name`) to deduplicate printings/art flexes.
- `cards.setCode` ↔ `sets.code` (implicit, both are the set-code domain): join card master data to set metadata (release date, type, sizes). Note not declared as FK but set_code is on `cards` too; `sets.type` and `baseSetSize`/`totalSetSize` are set-level attributes.