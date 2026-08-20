# Additional Metadata

## Clarified Semantics

- `movies.id` is the unique movie key (7997 rows); `genre.movie_id`, `ratings.movie_id`, `role_mapping.movie_id`, and `director_mapping.movie_id` all resolve to it, but there are no declared FK constraints (all inferred).
- `names.id` is the unique person key; `director_mapping.name_id` and `role_mapping.name_id` resolve to it (3603 and 12611 distinct persons respectively, all present in `names`).
- `role_mapping` links people to films as performers only; `category` is a binary attribute (`actor` vs `actress`, roughly 60%/40%). It encodes no character/film credits beyond the category label.
- `director_mapping` links people to films as directors; it is a separate credit channel from `role_mapping` (a person can appear in both).
- `movies.worlwide_gross_income` (sic, misspelled) is stored as text with a `"$ "` currency prefix (e.g. `$ 32783733`), not a numeric type; ~3724 rows are NULL. It should be parsed/stripped before numeric comparison.
- `movies.country` and `movies.languages` are free-text and often contain multiple comma-separated values in one field; country also appears combined like `%USA%` causing substring matches. Match via LIKE/sub-part rather than equality.
- `movies.date_published` is a timestamp; `year` is a separate int column constraining to 2017–2019 but they are not identical in granularity.
- `names.known_for_movies` is a comma-separated list of movie IDs (e.g. `tt1389072,tt2762506,tt1667354`), not a single scalar FK. Only ~8248 `names` rows hold a value that directly equals a `movies.id`; many entries contain multiple IDs or values not present in `movies`, so it is not a clean joinable key.
- `genre` is a normalized many-to-many table: one movie can have several genre rows (7997 distinct movies across 14662 rows); `Others` is a catch-all genre bucket.
- `ratings.movie_id` is unique — exactly one ratings row per movie (1:1 with `movies`). `median_rating` takes numeric step values (and fractional steps like 6.5), while `avg_rating` is continuous.
- `director_mapping` and `role_mapping` are many-to-many: a movie can have multiple directors/performers and a person can appear in multiple films. `genre.movie_id` covers the full movies table (7997 = all movies), so every movie has ≥1 genre; but `role_mapping`/`director_mapping` cover subsets (3757 and 3577 distinct movies).

## Potential Join Strategies

- **movies → ratings (1:1):** `movies.id = ratings.movie_id`. Exact unique join on both sides; no fan-out, safe for direct aggregation on either table.
- **movies → genre (1:many):** `movies.id = genre.movie_id`. Covers all 7997 movies, so a filter on `genre` never drops movies that lack genre data; but one movie yields multiple rows, so count/aggregate on `movies` becomes per-genre unless de-duplicated first.
- **movies → director_mapping and role_mapping (1:many):** `movies.id = director_mapping.movie_id` and `movies.id = role_mapping.movie_id`. Only 3577/3757 of 7997 movies have a director/role row, so outer join (or starting from the mapping table) is needed to retain all movies; inner joins silently restrict to credited films.
- **names → role_mapping → movies (people as cast):** join `names.id` → `role_mapping.name_id` → `role_mapping.movie_id` → `movies.id`. Filter/group by `category` to split actor vs actress; results only cover the 3757 cast-credited movies.
- **names → director_mapping → movies (people as directors):** join `names.id` → `director_mapping.name_id` → `director_mapping.movie_id` → `movies.id`. Distinct subsets: 3603 directors vs 12611 performers; a person appearing in both channels can be queried by intersecting these two join paths via `names.id`.
- **Performer-director bridge via names:** `role_mapping.name_id = director_mapping.name_id` (through `names.id`) identifies people who are both cast and crew for the same/different films; join both mapping tables on `movie_id` + `name_id` to link a film's cast to its director.
- **known_for_movies mining (multi-valued, unreliable):** because the field is a comma-separated list and ~22% of non-null values don't match a `movies.id`, it cannot be used as a direct `names.known_for_movies = movies.id` join. Only valid as a non-authoritative, approximate link requiring splitting and existence checks against `movies.id`.