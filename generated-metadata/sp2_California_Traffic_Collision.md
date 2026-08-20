# Additional Metadata

## Clarified Semantics
- `collisions.case_id` is the unique key for each collision; `case_ids.case_id` is the same value, so `case_ids` is effectively a registry/enumerator of collision keys (distinct `case_id` → `db_year` of reporting year).
- `county_city_location` and `jurisdiction` are both numeric jurisdiction/location codes; they can differ for the same row (e.g. jurisdiction 9590 vs county_city_location 1942, both Los Angeles). Use `county_location` (county name text) for county-level grouping.
- `county_location` and `caltrans_county` hold parallel county names; a given row's `caltrans_county`/`caltrans_district`/`state_route`/`postmile` are populated only when the location is a state highway (`state_highway_indicator=1`); they are null for most city/local roads.
- `caltrans_district` is the Caltrans district number (0–12), an administrative region larger than a county; many counties map to one district.
- `pcf_violation` is a numeric CA Vehicle Code section number (e.g. 22350 → speeding); `pcf_violation_category` is its human-readable grouping, and `pcf_violation_subsection` is a letter/suffix refinement. `primary_collision_factor` is the broad cause label.
- `collision_date` / `collision_time` / `process_date` are TEXT ISO-format values (dates sortable as strings; times `HH:MM:SS`). `process_date` is the CAD/report submission date, which can lag `collision_date`.
- Count columns are split both ways: `collisions` has aggregate victim counts (`killed_victims`, `injured_victims`, `severe_injury_count`, `pedestrian_*_count`, etc.), while `victims` holds row-level per-person injury detail tied to `victim_degree_of_injury`.
- `collisions.not_private_property` is constant 1 (all rows are public-road collisions); null-valued victim/party counts vs. the aggregate count columns can differ slightly (address mixes and non-person entries).
- A `collision_severity` uses text buckets (fatal/severe injury/other injury/pain/property damage only) that do not exactly map one-to-one to code-guarded flag columns; prefer the explicit count columns for exact tallies.

## Potential Join Strategies
- `collisions.case_id = parties.case_id` (one-to-many). About 2 parties per collision on average; recover the at-fault driver with `parties.at_fault = 1` to analyze the at-fault vehicle/person. Cardinality: 94k collisions → 187k parties.
- `collisions.case_id = victims.case_id` (mostly one-to-few, ~1 victim row per event). Use to drill from aggregate `injured_victims`/`killed_victims` down to per-person `victim_degree_of_injury`. Cardinality: 94k collisions → 96k victims.
- `parties.case_id = victims.case_id AND parties.party_number = victims.party_number` (composite). `victims.party_number` references the party number within the same collision, so this links a victim to their specific party; filter `parties.at_fault=1` to isolate the at-fault party's injured occupants. `party_number` alone is not globally unique — always pair with `case_id`.
- `collisions.case_id = case_ids.case_id` to restrict a working set by reporting year (`case_ids.db_year IN (2021, 2018, 2020)`), where `collisions` itself does not store a year column.
- Independent geographic keying: `county_location` (county names) vs `caltrans_county` (Caltrans names) mirror each other for route-level rows, so `caltrans_county = county_location` is a valid coarse join/cluster predicate only for state-highway rows; for non-state rows `caltrans_*` are null. For CHP beats, `chp_beat_type`/`chp_beat_class` describe road ownership only where `chp_shift != 'not chp'`.