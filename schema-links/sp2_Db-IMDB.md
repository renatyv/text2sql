# Schema Links

- version: 0.0.5
- dialect: sqlite
- database: file:/Users/renatyuldashev/Documents/ai-sql/custom-bench/data/sp2_lite_sqlite/databases/Db-IMDB.sqlite
- schema: main

## Declared PK/FK Links

No declared PK/FK links found.

## Inferred Links

### mid
- inferred: M_Cast.MID, M_Country.MID, M_Director.MID, M_Genre.MID, M_Language.MID, M_Location.MID, M_Producer.MID, Movie.MID

### m
- inferred: Language.LAID, Location.LID, M_Language.LAID, M_Location.LID

### country
- inferred: Country.CID, M_Country.CID

### gid
- inferred: Genre.GID, M_Genre.GID

### pid
- inferred: M_Director.PID, Person.PID
