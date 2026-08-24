---
generator: db-snooper
version: 0.0.34
generated_at_utc: 2026-08-24T21:59:25.844374Z
dialect: sqlite
database: /var/folders/9j/b9bx_drd53sc6zbpsqyrjy4h0000gn/T/dbsnoop-kwsjknvq/imdb_movies.sqlite
schema: main
---

# "ERD"  (rows=25)

columns:
"table" text: "movie"=9, "names"=5, "ratings"=4, "role_mapping"=3, "director_mapping"=2, "genre"=2
"column" text: 20 distinct
"Unnamed: 2" float: all NULL
"Unnamed: 3" float: all NULL
"Unnamed: 4" float: all NULL
"Unnamed: 5" float: all NULL
"Unnamed: 6" text: "* movie_id"=1, "* name_id"=1, "category"=1, "role_mapping"=1, nulls=21
"Unnamed: 7" float: all NULL
"Unnamed: 8" float: all NULL
"Unnamed: 9" text: "* id"=2, "* genre"=1, "* movie_id"=1, "country"=1, "date_of_birth"=1, "date_published"=1, "duration"=1, "genre"=1, "height"=1, "known_for_movies"=1, "languages"=1, "movie"=1, "name"=1, "names"=1, "production_company"=1, "title"=1, "worlwide_gross_income"=1, "year"=1, nulls=6
"Unnamed: 10" float: all NULL
"Unnamed: 11" float: all NULL
"Unnamed: 12" text: "* movie_id"=2, "* name_id"=1, "avg_rating"=1, "director_mapping"=1, "median_rating"=1, "ratings"=1, "total_votes"=1, nulls=17

indexes: none

samples:
| column | latest | sample | sample |
|---|---|---|---|
| table | role_mapping | movie | names |
| column | name_id | production_company | id |
| Unnamed: 2 | null | null | null |
| Unnamed: 3 | null | null | null |
| Unnamed: 4 | null | null | null |
| Unnamed: 5 | null | null | null |
| Unnamed: 6 | * name_id | null | null |
| Unnamed: 7 | null | null | null |
| Unnamed: 8 | null | null | null |
| Unnamed: 9 | worlwide_gross_income | * id | production_company |
| Unnamed: 10 | null | null | null |
| Unnamed: 11 | null | null | null |
| Unnamed: 12 | * name_id | null | null |

# "director_mapping"  (rows=3867)

columns:
"movie_id" text: 3577 distinct
"name_id" text: 3603 distinct

indexes: none

samples:
| column | latest | sample | sample |
|---|---|---|---|
| movie_id | tt9903716 | tt6743942 | tt10255320 |
| name_id | nm10532693 | nm1280221 | nm0006395 |

# "genre"  (rows=14662)

columns:
"movie_id" text: 7997 distinct
"genre" text: "Drama"=4285, "Comedy"=2412, "Thriller"=1484, "Action"=1289, "Horror"=1208, "Romance"=906, "Crime"=813, "Adventure"=591, "Mystery"=555, "Sci-Fi"=375, "Fantasy"=342, "Family"=302, "Others"=100

indexes: none

samples:
| column | latest | sample | sample |
|---|---|---|---|
| movie_id | tt9914286 | tt7752454 | tt6917272 |
| genre | Family | Mystery | Comedy |

# "movies"  (rows=7997)

columns:
"id" text: unique identifier
"title" text: 7932 distinct
"year" int: 2017=3052, 2018=2944, 2019=2001, 2017..2019
"date_published" timestamp: 948 distinct
"duration" int: 150 distinct, 41..808, avg=103.894, median=99
"country" text: 986 distinct, nulls=20
"worlwide_gross_income" text: 4256 distinct, nulls=3724
"languages" text: 880 distinct, nulls=198
"production_company" text: 5332 distinct, nulls=528

indexes: none

samples:
| column | latest | sample | sample |
|---|---|---|---|
| id | tt9914286 | tt6820184 | tt6876488 |
| title | Sokagin Çocuklari | Madame Mills, une voisine si parfaite | Gek van Geluk |
| year | 2019 | 2018 | 2017 |
| date_published | 2019-03-15T00:00:00 | 2018-03-07T00:00:00 | 2017-12-07T00:00:00 |
| duration | 98 | 88 | 106 |
| country | Turkey | Belgium, France, China | Netherlands |
| worlwide_gross_income | $ 2833 | $ 2141498 | $ 1418659 |
| languages | Turkish | French, English, Chinese | Dutch |
| production_company | Gizem Ajans | Films du Cap, Les | Johan Nijenhuis & Co |

# "names"  (rows=25735)

columns:
"id" text: unique identifier
"name" text: 25674 distinct
"height" float: 55 distinct, nulls=17335, 76..201, avg=161.55, median=200
"date_of_birth" text: 9329 distinct, nulls=13431
"known_for_movies" text: 6245 distinct, nulls=15226

indexes: none

samples:
| column | latest | sample | sample |
|---|---|---|---|
| id | nm9992720 | nm0675114 | nm6646364 |
| name | McMagic Cardenas | Jeff Perry | Elizabeth Rhoades |
| height | null | null | 200 |
| date_of_birth | null | 1955-08-16 | null |
| known_for_movies | tt7233828 | null | tt6619250,tt6557704 |

# "ratings"  (rows=7997)

columns:
"movie_id" text: unique identifier
"avg_rating" float: 90 distinct, 1..10, avg=5.80678, median=6
"total_votes" int: 3061 distinct, 100..725138, avg=6764.59, median=472
"median_rating" float: 7=2235, 6=1963, 8=1021, 5=971, 4=472, 9=424, 10=345, 3=279, 2=119, 1=94, 6.5=22, 4.5=14, 5.5=12, 7.5=9, 3.5=7, 8.5=5, 2.5=4, 9.5=1, 1..10

indexes: none

samples:
| column | latest | sample | sample |
|---|---|---|---|
| movie_id | tt9914286 | tt6613878 | tt2039380 |
| avg_rating | 7.2 | 6.7 | 3 |
| total_votes | 190 | 2321 | 478 |
| median_rating | 10 | 7 | 3 |

# "role_mapping"  (rows=15615)

columns:
"movie_id" text: 3757 distinct
"name_id" text: 12611 distinct
"category" text: "actor"=9362, "actress"=6253

indexes: none

samples:
| column | latest | sample | sample |
|---|---|---|---|
| movie_id | tt9903716 | tt7241654 | tt9047474 |
| name_id | nm7237124 | nm0000574 | nm3198515 |
| category | actress | actor | actress |
