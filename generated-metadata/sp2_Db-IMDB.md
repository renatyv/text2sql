# Additional Metadata

## Clarified Semantics

- Every table has an `index` column that is a surrogate row counter, not a natural key; ignore unless used as a stable row id.
- `Movie.MID` (text, tt... form) is the movie primary key; only `Movie` has MID as a true key (3475 distinct).
- `Movie.year` is TEXT, not an integer. ~117 movies have non-4-digit values prefixed with a tag (e.g., `I 1964`); parse/normalize before numeric year filters.
- `Movie.rating` (1.3–9.6) and `Movie.num_votes` are per-title review aggregates; `num_votes` is very skewed (median 388, max >1.1M).
- `Genre.Name` holds a comma-joined genre *combination* (e.g., `Drama, Mystery, Sci-Fi`), not a single genre. `M_Genre` has exactly 1 row per movie, so a movie maps to one combination via `GID`.
- `M_Country`, `M_Language`, `M_Location`, `M_Genre` each have exactly one row per movie (MID unique). Their foreign-id columns (`CID`, `LAID`, `LID`, `GID`) are stored as integer-valued floats.
- `M_Location.LID` is nullable (~46.8% of movies lack a location); treat as LEFT-join/optional. `M_Country.CID` (~5 nulls) and `M_Producer.PID`/`M_Cast.PID` also have small null counts.
- `M_Cast` is one-to-many from Movie (up to 238 rows per movie) and covers every movie; `M_Producer` is one-to-many (avg ~3.4 per movie).
- `Person.Name` leading whitespace is common; `Person.Gender` is nullable (~23% null) and roughly 2:1 Male:Female among non-null.
- A director is never also credited in the cast of the same film (M_Director ∩ M_Cast on MID+PID = 0 rows).

## Potential Join Strategies

- Movie as hub: `Movie.MID` = `M_*.<MID>` for all seven M_* tables. Joining Movie→M_Cast / M_Producer is fan-out (many rows per movie); joining Movie→M_Country / M_Genre / M_Language / M_Location is 1:1 (no fan-out).
- Person hub: `Person.PID` links into `M_Director.PID`, `M_Cast.PID`, and `M_Producer.PID`. To associate a person's role(s), join each M_* table separately on `PID` (and match `MID` to attribute the role to a specific title).
- Genre combination lookup: join `M_Genre.GID` = `Genre.GID` to get the nominal combined-genre text; filter against the `Genre.Name` string when posing multi-genre conditions.
- Country lookup: join `M_Country.CID` = `Country.CID` (compare on the integer-valued float; `CID` in Country is 0–33 ints). Join is LEFT for the ~5 null CID rows.
- Language lookup: `M_Language.LAID` = `Language.LAID` (0–31). Do NOT cross-match `Language.LAID` with `Location.LID` by value — they share the same column name but reference different dimensions (ranges 32 vs 559) despite being grouped in the same schema-link cluster.
- Location lookup: `M_Location.LID` = `Location.LID`, always LEFT-join because ~46.8% of LID values are null.
- Group people work: distinct `Person.PID` (37565) is much larger than any single M_* PID set, so driving from `Person` fans out heavily; drive from the M_* side to filter by role first.