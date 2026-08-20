# Schema Links

- version: 0.0.5
- dialect: sqlite
- database: file:/Users/renatyuldashev/Documents/ai-sql/custom-bench/data/sp2_lite_sqlite/databases/imdb_movies.sqlite
- schema: main

## Declared PK/FK Links

No declared PK/FK links found.

## Inferred Links

### movie
- inferred: director_mapping.movie_id, genre.movie_id, movies.id, ratings.movie_id, role_mapping.movie_id

### name
- inferred: director_mapping.name_id, names.id, role_mapping.name_id
