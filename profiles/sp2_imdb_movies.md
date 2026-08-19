---
generator: db-snooper
version: 0.0.26
generated_at_utc: 2026-08-16T08:09:24.828254Z
dialect: sqlite
database: /var/folders/9j/b9bx_drd53sc6zbpsqyrjy4h0000gn/T/dbsnoop-tfq4_59h/imdb_movies.sqlite
schema: main
---

# ERD

```sql
CREATE TABLE "ERD" (
"table" TEXT,
  "column" TEXT,
  "Unnamed: 2" REAL,
  "Unnamed: 3" REAL,
  "Unnamed: 4" REAL,
  "Unnamed: 5" REAL,
  "Unnamed: 6" TEXT,
  "Unnamed: 7" REAL,
  "Unnamed: 8" REAL,
  "Unnamed: 9" TEXT,
  "Unnamed: 10" REAL,
  "Unnamed: 11" REAL,
  "Unnamed: 12" TEXT
);
```

## Rows

- total=25

| column | latest | sample | sample |
|---|---|---|---|
| table | role_mapping | role_mapping | movie |
| column | name_id | movie_id | date_published |
| Unnamed: 2 | null | null | null |
| Unnamed: 3 | null | null | null |
| Unnamed: 4 | null | null | null |
| Unnamed: 5 | null | null | null |
| Unnamed: 6 | * name_id | * movie_id | null |
| Unnamed: 7 | null | null | null |
| Unnamed: 8 | null | null | null |
| Unnamed: 9 | worlwide_gross_income | country | null |
| Unnamed: 10 | null | null | null |
| Unnamed: 11 | null | null | null |
| Unnamed: 12 | * name_id | * movie_id | total_votes |

## Columns

- table: "movie"=9, "names"=5, "ratings"=4, "role_mapping"=3, "director_mapping"=2, "genre"=2
- column: 20 distinct
- Unnamed: 2: all NULL
- Unnamed: 3: all NULL
- Unnamed: 4: all NULL
- Unnamed: 5: all NULL
- Unnamed: 6: "* movie_id"=1, "* name_id"=1, "category"=1, "role_mapping"=1, nulls=21
- Unnamed: 7: all NULL
- Unnamed: 8: all NULL
- Unnamed: 9: "* id"=2, "* genre"=1, "* movie_id"=1, "country"=1, "date_of_birth"=1, "date_published"=1, "duration"=1, "genre"=1, "height"=1, "known_for_movies"=1, "languages"=1, "movie"=1, "name"=1, "names"=1, "production_company"=1, "title"=1, "worlwide_gross_income"=1, "year"=1, nulls=6
- Unnamed: 10: all NULL
- Unnamed: 11: all NULL
- Unnamed: 12: "* movie_id"=2, "* name_id"=1, "avg_rating"=1, "director_mapping"=1, "median_rating"=1, "ratings"=1, "total_votes"=1, nulls=17


# director_mapping

```sql
CREATE TABLE "director_mapping" (
"movie_id" TEXT,
  "name_id" TEXT
);
```

## Rows

- total=3867

| column | latest | sample | sample |
|---|---|---|---|
| movie_id | tt9903716 | tt5827212 | tt4799064 |
| name_id | nm10532693 | nm1732946 | nm1088485 |

## Columns

- movie_id: 3577 distinct
- name_id: 3603 distinct


# genre

```sql
CREATE TABLE "genre" (
"movie_id" TEXT,
  "genre" TEXT
);
```

## Rows

- total=14662

| column | latest | sample | sample |
|---|---|---|---|
| movie_id | tt9914286 | tt4951982 | tt8941440 |
| genre | Family | Drama | Thriller |

## Columns

- movie_id: 7997 distinct
- genre: "Drama"=4285, "Comedy"=2412, "Thriller"=1484, "Action"=1289, "Horror"=1208, "Romance"=906, "Crime"=813, "Adventure"=591, "Mystery"=555, "Sci-Fi"=375, "Fantasy"=342, "Family"=302, "Others"=100


# movies

```sql
CREATE TABLE "movies" (
"id" TEXT,
  "title" TEXT,
  "year" INTEGER,
  "date_published" TIMESTAMP,
  "duration" INTEGER,
  "country" TEXT,
  "worlwide_gross_income" TEXT,
  "languages" TEXT,
  "production_company" TEXT
);
```

## Rows

- total=7997

| column | latest | sample | sample |
|---|---|---|---|
| id | tt9914286 | tt5320124 | tt6139732 |
| title | Sokagin Çocuklari | Everything Is Wonderful | Aladdin |
| year | 2019 | 2018 | 2019 |
| date_published | 2019-03-15T00:00:00 | 2018-10-01T00:00:00 | 2019-05-22T00:00:00 |
| duration | 98 | 79 | 128 |
| country | Turkey | USA, Greece | USA |
| worlwide_gross_income | $ 2833 | $ 202 | $ 1050693953 |
| languages | Turkish | English | Arabic, English |
| production_company | Gizem Ajans | Big Vision Creative | Walt Disney Pictures |

## Columns

- id: unique identifier
- title: 7932 distinct
- year: 2017=3052, 2018=2944, 2019=2001, int 2017..2019
- date_published: 948 distinct
- duration: 150 distinct, int 41..808
  - stats: average=103.894, median=99
- country: 986 distinct, nulls=20
- worlwide_gross_income: 4256 distinct, nulls=3724
- languages: 880 distinct, nulls=198
- production_company: 5332 distinct, nulls=528


# names

```sql
CREATE TABLE "names" (
"id" TEXT,
  "name" TEXT,
  "height" REAL,
  "date_of_birth" TEXT,
  "known_for_movies" TEXT
);
```

## Rows

- total=25735

| column | latest | sample | sample |
|---|---|---|---|
| id | nm9992720 | nm6394542 | nm0159325 |
| name | McMagic Cardenas | Sheik Afzal | Jehangir Choudhary |
| height | null | null | null |
| date_of_birth | null | null | null |
| known_for_movies | tt7233828 | tt5972292 | null |

## Columns

- id: unique identifier
- name: 25674 distinct
- height: 55 distinct, nulls=17335, num 76..201
  - stats: average=161.55, median=200
- date_of_birth: 9329 distinct, nulls=13431
- known_for_movies: 6245 distinct, nulls=15226


# ratings

```sql
CREATE TABLE "ratings" (
"movie_id" TEXT,
  "avg_rating" REAL,
  "total_votes" INTEGER,
  "median_rating" REAL
);
```

## Rows

- total=7997

| column | latest | sample | sample |
|---|---|---|---|
| movie_id | tt9914286 | tt9193612 | tt2051850 |
| avg_rating | 7.2 | 6.9 | 4.9 |
| total_votes | 190 | 151 | 606 |
| median_rating | 10 | 7 | 6 |

## Columns

- movie_id: unique identifier
- avg_rating: 90 distinct, num 1..10
  - stats: average=5.80678, median=6
- total_votes: 3061 distinct, int 100..725138
  - stats: average=6764.59, median=472
- median_rating: 7=2235, 6=1963, 8=1021, 5=971, 4=472, 9=424, 10=345, 3=279, 2=119, 1=94, 6.5=22, 4.5=14, 5.5=12, 7.5=9, 3.5=7, 8.5=5, 2.5=4, 9.5=1, num 1..10


# role_mapping

```sql
CREATE TABLE "role_mapping" (
"movie_id" TEXT,
  "name_id" TEXT,
  "category" TEXT
);
```

## Rows

- total=15615

| column | latest | sample | sample |
|---|---|---|---|
| movie_id | tt9903716 | tt5507934 | tt8484370 |
| name_id | nm7237124 | nm2720854 | nm7308346 |
| category | actress | actress | actor |

## Columns

- movie_id: 3757 distinct
- name_id: 12611 distinct
- category: "actor"=9362, "actress"=6253
