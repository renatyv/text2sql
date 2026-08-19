---
generator: db-snooper
version: 0.0.26
generated_at_utc: 2026-08-16T08:07:49.824823Z
dialect: sqlite
database: /var/folders/9j/b9bx_drd53sc6zbpsqyrjy4h0000gn/T/dbsnoop-qizka7yw/Db-IMDB.sqlite
schema: main
---

# Country

```sql
CREATE TABLE "Country" (
"index" INTEGER,
  "Name" TEXT,
  "CID" INTEGER
);
```

## Indexes

- CREATE INDEX "ix_Country_index"ON "Country" ("index")

## Rows

- total=34

| column | latest | sample | sample |
|---|---|---|---|
| index | 33 | 6 | 15 |
| Name | Georgia | Canada | France |
| CID | 33 | 6 | 15 |

## Columns

- index: all distinct, int 0..33
  - stats: average=16.5, median=16.5
- Name: all distinct
- CID: unique identifier, int 0..33
  - stats: average=16.5, median=16.5


# Genre

```sql
CREATE TABLE "Genre" (
"index" INTEGER,
  "Name" TEXT,
  "GID" INTEGER
);
```

## Indexes

- CREATE INDEX "ix_Genre_index"ON "Genre" ("index")

## Rows

- total=328

| column | latest | sample | sample |
|---|---|---|---|
| index | 327 | 212 | 235 |
| Name | Drama, Mystery, Sci-Fi             | Romance, Action, Crime             | Comedy, Romance, Drama             |
| GID | 327 | 212 | 235 |

## Columns

- index: all distinct, int 0..327
  - stats: average=163.5, median=163.5
- Name: all distinct
- GID: unique identifier, int 0..327
  - stats: average=163.5, median=163.5


# Language

```sql
CREATE TABLE "Language" (
"index" INTEGER,
  "Name" TEXT,
  "LAID" INTEGER
);
```

## Indexes

- CREATE INDEX "ix_Language_index"ON "Language" ("index")

## Rows

- total=32

| column | latest | sample | sample |
|---|---|---|---|
| index | 31 | 1 | 21 |
| Name | Georgian | Marathi | Russian |
| LAID | 31 | 1 | 21 |

## Columns

- index: all distinct, int 0..31
  - stats: average=15.5, median=15.5
- Name: all distinct
- LAID: unique identifier, int 0..31
  - stats: average=15.5, median=15.5


# Location

```sql
CREATE TABLE "Location" (
"index" INTEGER,
  "Name" TEXT,
  "LID" INTEGER
);
```

## Indexes

- CREATE INDEX "ix_Location_index"ON "Location" ("index")

## Rows

- total=559

| column | latest | sample | sample |
|---|---|---|---|
| index | 558 | 472 | 178 |
| Name | Aftab Studio, India | Hollywood, Los Angeles, California, USA | Bhopal, India |
| LID | 558 | 472 | 178 |

## Columns

- index: all distinct, int 0..558
  - stats: average=279, median=279
- Name: all distinct
- LID: unique identifier, int 0..558
  - stats: average=279, median=279


# M_Cast

```sql
CREATE TABLE "M_Cast" (
"index" INTEGER,
  "MID" TEXT,
  "PID" TEXT,
  "ID" INTEGER
);
```

## Indexes

- CREATE INDEX "ix_M_Cast_index"ON "M_Cast" ("index")

## Rows

- total=82837

| column | latest | sample | sample |
|---|---|---|---|
| index | 82836 | 37900 | 59918 |
| MID | tt0375890 | tt1535467 | tt0071730 |
| PID |  nm0438467 |  nm4547925 |  nm0802107 |
| ID | 82836 | 37900 | 59918 |

## Columns

- index: all distinct, int 0..82836
  - stats: average=41418, median=41418
- MID: 3475 distinct
- PID: 32127 distinct, nulls=2
- ID: unique identifier, int 0..82836
  - stats: average=41418, median=41418


# M_Country

```sql
CREATE TABLE "M_Country" (
"index" INTEGER,
  "MID" TEXT,
  "CID" REAL,
  "ID" INTEGER
);
```

## Indexes

- CREATE INDEX "ix_M_Country_index"ON "M_Country" ("index")

## Rows

- total=3475

| column | latest | sample | sample |
|---|---|---|---|
| index | 3474 | 1862 | 1462 |
| MID | tt0375890 | tt0087417 | tt0043306 |
| CID | 2 | 2 | 2 |
| ID | 3474 | 1862 | 1462 |

## Columns

- index: all distinct, int 0..3474
  - stats: average=1737, median=1737
- MID: unique identifier
- CID: 34 distinct, nulls=5, num 0..33
  - stats: average=2.1781, median=2
- ID: unique identifier, int 0..3474
  - stats: average=1737, median=1737


# M_Director

```sql
CREATE TABLE "M_Director" (
"index" INTEGER,
  "MID" TEXT,
  "PID" TEXT,
  "ID" INTEGER
);
```

## Indexes

- CREATE INDEX "ix_M_Director_index"ON "M_Director" ("index")

## Rows

- total=3475

| column | latest | sample | sample |
|---|---|---|---|
| index | 3474 | 126 | 3064 |
| MID | tt0375890 | tt0238936 | tt0271023 |
| PID | nm1421793 | nm0080220 | nm0385758 |
| ID | 3474 | 126 | 3064 |

## Columns

- index: all distinct, int 0..3474
  - stats: average=1737, median=1737
- MID: unique identifier
- PID: 1464 distinct
- ID: unique identifier, int 0..3474
  - stats: average=1737, median=1737


# M_Genre

```sql
CREATE TABLE "M_Genre" (
"index" INTEGER,
  "MID" TEXT,
  "GID" INTEGER,
  "ID" INTEGER
);
```

## Indexes

- CREATE INDEX "ix_M_Genre_index"ON "M_Genre" ("index")

## Rows

- total=3475

| column | latest | sample | sample |
|---|---|---|---|
| index | 3474 | 809 | 81 |
| MID | tt0375890 | tt1288638 | tt6206564 |
| GID | 46 | 16 | 39 |
| ID | 3474 | 809 | 81 |

## Columns

- index: all distinct, int 0..3474
  - stats: average=1737, median=1737
- MID: unique identifier
- GID: 328 distinct, int 0..327
  - stats: average=62.7606, median=46
- ID: unique identifier, int 0..3474
  - stats: average=1737, median=1737


# M_Language

```sql
CREATE TABLE "M_Language" (
"index" INTEGER,
  "MID" TEXT,
  "LAID" INTEGER,
  "ID" INTEGER
);
```

## Indexes

- CREATE INDEX "ix_M_Language_index"ON "M_Language" ("index")

## Rows

- total=3475

| column | latest | sample | sample |
|---|---|---|---|
| index | 3474 | 2619 | 889 |
| MID | tt0375890 | tt0246687 | tt3615160 |
| LAID | 2 | 2 | 16 |
| ID | 3474 | 2619 | 889 |

## Columns

- index: all distinct, int 0..3474
  - stats: average=1737, median=1737
- MID: unique identifier
- LAID: 32 distinct, int 0..31
  - stats: average=2.55367, median=2
- ID: unique identifier, int 0..3474
  - stats: average=1737, median=1737


# M_Location

```sql
CREATE TABLE "M_Location" (
"index" INTEGER,
  "MID" TEXT,
  "LID" REAL,
  "ID" INTEGER
);
```

## Indexes

- CREATE INDEX "ix_M_Location_index"ON "M_Location" ("index")

## Rows

- total=3475

| column | latest | sample | sample |
|---|---|---|---|
| index | 3474 | 1352 | 1545 |
| MID | tt0375890 | tt2375567 | tt3338188 |
| LID | 7 | 216 | 389 |
| ID | 3474 | 1352 | 1545 |

## Columns

- index: all distinct, int 0..3474
  - stats: average=1737, median=1737
- MID: unique identifier
- LID: 559 distinct, nulls=1626, num 0..558
  - stats: average=166.056, median=124
- ID: unique identifier, int 0..3474
  - stats: average=1737, median=1737


# M_Producer

```sql
CREATE TABLE "M_Producer" (
"index" INTEGER,
  "MID" TEXT,
  "PID" TEXT,
  "ID" INTEGER
);
```

## Indexes

- CREATE INDEX "ix_M_Producer_index"ON "M_Producer" ("index")

## Rows

- total=11751

| column | latest | sample | sample |
|---|---|---|---|
| index | 11750 | 11535 | 2374 |
| MID | tt0375890 | tt0142521 | tt5456546 |
| PID |  nm1421793 |  nm0481568 |  nm3049612 |
| ID | 11750 | 11535 | 2374 |

## Columns

- index: all distinct, int 0..11750
  - stats: average=5875, median=5875
- MID: 3475 distinct
- PID: 5436 distinct, nulls=21
- ID: unique identifier, int 0..11750
  - stats: average=5875, median=5875


# Movie

```sql
CREATE TABLE "Movie" (
"index" INTEGER,
  "MID" TEXT,
  "title" TEXT,
  "year" TEXT,
  "rating" REAL,
  "num_votes" INTEGER
);
```

## Indexes

- CREATE INDEX "ix_Movie_index"ON "Movie" ("index")

## Rows

- total=3475

| column | latest | sample | sample |
|---|---|---|---|
| index | 3474 | 3443 | 2332 |
| MID | tt0375890 | tt0257416 | tt0215196 |
| title | Kanoon | Ashwamedham | Split Wide Open |
| year | 1994 | 1992 | 1999 |
| rating | 3.2 | 7.2 | 6.4 |
| num_votes | 103 | 52 | 212 |

## Columns

- index: all distinct, int 0..3474
  - stats: average=1737, median=1737
- MID: unique identifier
- title: 3344 distinct
- year: 125 distinct
- rating: 82 distinct, num 1.3..9.6
  - stats: average=6.03678, median=6.2
- num_votes: 1763 distinct, int 51..1137529
  - stats: average=4544.73, median=388


# Person

```sql
CREATE TABLE "Person" (
"index" INTEGER,
  "PID" TEXT,
  "Name" TEXT,
  "Gender" TEXT
);
```

## Indexes

- CREATE INDEX "ix_Person_index"ON "Person" ("index")

## Rows

- total=38285

| column | latest | sample | sample |
|---|---|---|---|
| index | 38284 | 18840 | 21710 |
| PID | nm1421793 | nm0014135 | nm4444549 |
| Name | Sushma Shiromani |  Ahmed Ahmed |  Prabir Kumar |
| Gender | Female | Male | Male |

## Columns

- index: all distinct, int 0..38284
  - stats: average=19142, median=19142
- PID: 37565 distinct, nulls=1
- Name: 36312 distinct, nulls=1
- Gender: "Male"=20055, "Female"=9435, nulls=8795
