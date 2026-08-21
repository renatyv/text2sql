---
generator: db-snooper
version: 0.0.33
generated_at_utc: 2026-08-21T12:32:11.812616Z
dialect: sqlite
database: /var/folders/9j/b9bx_drd53sc6zbpsqyrjy4h0000gn/T/dbsnoop-3_cohins/Db-IMDB.sqlite
schema: main
---

# "Country"  (rows=34)

columns:
"index" int: all distinct, 0..33, avg=16.5, median=16.5
"Name" text: all distinct
"CID" int: unique identifier, 0..33, avg=16.5, median=16.5

indexes: "index"

samples:
| column | latest | sample | sample |
|---|---|---|---|
| index | 33 | 17 | 3 |
| Name | Georgia | Japan | Australia |
| CID | 33 | 17 | 3 |

# "Genre"  (rows=328)

columns:
"index" int: all distinct, 0..327, avg=163.5, median=163.5
"Name" text: all distinct
"GID" int: unique identifier, 0..327, avg=163.5, median=163.5

indexes: "index"

samples:
| column | latest | sample | sample |
|---|---|---|---|
| index | 327 | 16 | 137 |
| Name | Drama, Mystery, Sci-Fi             | Comedy, Drama             | Drama, Musical             |
| GID | 327 | 16 | 137 |

# "Language"  (rows=32)

columns:
"index" int: all distinct, 0..31, avg=15.5, median=15.5
"Name" text: all distinct
"LAID" int: unique identifier, 0..31, avg=15.5, median=15.5

indexes: "index"

samples:
| column | latest | sample | sample |
|---|---|---|---|
| index | 31 | 5 | 2 |
| Name | Georgian | Mandarin | Hindi |
| LAID | 31 | 5 | 2 |

# "Location"  (rows=559)

columns:
"index" int: all distinct, 0..558, avg=279, median=279
"Name" text: all distinct
"LID" int: unique identifier, 0..558, avg=279, median=279

indexes: "index"

samples:
| column | latest | sample | sample |
|---|---|---|---|
| index | 558 | 95 | 239 |
| Name | Aftab Studio, India | Stansted Airport - Bassingbourn Rd, Stansted CM24 1QW, London, England, UK | Annapoorna Studios, Hyderabad, Telangana, India |
| LID | 558 | 95 | 239 |

# "M_Cast"  (rows=82837)

columns:
"index" int: all distinct, 0..82836, avg=41418, median=41418
"MID" text: 3475 distinct
"PID" text: 32127 distinct, nulls=2
"ID" int: unique identifier, 0..82836

indexes: "index"

samples:
| column | latest | sample | sample |
|---|---|---|---|
| index | 82836 | 39854 | 59725 |
| MID | tt0375890 | tt0060104 | tt0079584 |
| PID |  nm0438467 |  nm0348467 |  nm0025630 |
| ID | 82836 | 39854 | 59725 |

# "M_Country"  (rows=3475)

columns:
"index" int: all distinct, 0..3474, avg=1737, median=1737
"MID" text: unique identifier
"CID" float: 34 distinct, nulls=5, 0..33, avg=2.1781, median=2
"ID" int: unique identifier, 0..3474

indexes: "index"

samples:
| column | latest | sample | sample |
|---|---|---|---|
| index | 3474 | 2140 | 3323 |
| MID | tt0375890 | tt0116407 | tt0827202 |
| CID | 2 | 2 | 2 |
| ID | 3474 | 2140 | 3323 |

# "M_Director"  (rows=3475)

columns:
"index" int: all distinct, 0..3474, avg=1737, median=1737
"MID" text: unique identifier
"PID" text: 1464 distinct
"ID" int: unique identifier, 0..3474

indexes: "index"

samples:
| column | latest | sample | sample |
|---|---|---|---|
| index | 3474 | 2723 | 856 |
| MID | tt0375890 | tt0178203 | tt2073070 |
| PID | nm1421793 | nm0695162 | nm0223606 |
| ID | 3474 | 2723 | 856 |

# "M_Genre"  (rows=3475)

columns:
"index" int: all distinct, 0..3474, avg=1737, median=1737
"MID" text: unique identifier
"GID" int: 328 distinct, 0..327, avg=62.7606, median=46
"ID" int: unique identifier, 0..3474

indexes: "index"

samples:
| column | latest | sample | sample |
|---|---|---|---|
| index | 3474 | 2864 | 442 |
| MID | tt0375890 | tt0154653 | tt8581230 |
| GID | 46 | 5 | 19 |
| ID | 3474 | 2864 | 442 |

# "M_Language"  (rows=3475)

columns:
"index" int: all distinct, 0..3474, avg=1737, median=1737
"MID" text: unique identifier
"LAID" int: 32 distinct, 0..31, avg=2.55367, median=2
"ID" int: unique identifier, 0..3474

indexes: "index"

samples:
| column | latest | sample | sample |
|---|---|---|---|
| index | 3474 | 1726 | 1538 |
| MID | tt0375890 | tt0057568 | tt5162476 |
| LAID | 2 | 2 | 2 |
| ID | 3474 | 1726 | 1538 |

# "M_Location"  (rows=3475)

columns:
"index" int: all distinct, 0..3474, avg=1737, median=1737
"MID" text: unique identifier
"LID" float: 559 distinct, nulls=1626, 0..558, avg=166.056, median=124
"ID" int: unique identifier, 0..3474

indexes: "index"

samples:
| column | latest | sample | sample |
|---|---|---|---|
| index | 3474 | 188 | 2019 |
| MID | tt0375890 | tt0367110 | tt0187109 |
| LID | 7 | 102 | null |
| ID | 3474 | 188 | 2019 |

# "M_Producer"  (rows=11751)

columns:
"index" int: all distinct, 0..11750, avg=5875, median=5875
"MID" text: 3475 distinct
"PID" text: 5436 distinct, nulls=21
"ID" int: unique identifier, 0..11750

indexes: "index"

samples:
| column | latest | sample | sample |
|---|---|---|---|
| index | 11750 | 8459 | 3145 |
| MID | tt0375890 | tt0290685 | tt5207116 |
| PID |  nm1421793 |  nm2528195 |  nm5712184 |
| ID | 11750 | 8459 | 3145 |

# "Movie"  (rows=3475)

columns:
"index" int: all distinct, 0..3474, avg=1737, median=1737
"MID" text: unique identifier
"title" text: 3344 distinct
"year" text: 125 distinct
"rating" float: 82 distinct, 1.3..9.6, avg=6.03678, median=6.2
"num_votes" int: 1763 distinct, 51..1137529, avg=4544.73, median=388

indexes: "index"

samples:
| column | latest | sample | sample |
|---|---|---|---|
| index | 3474 | 247 | 2587 |
| MID | tt0375890 | tt2283748 | tt2032530 |
| title | Kanoon | OMG: Oh My God! | Shabri |
| year | 1994 | 2012 | 2011 |
| rating | 3.2 | 8.2 | 5.8 |
| num_votes | 103 | 41975 | 116 |

# "Person"  (rows=38285)

columns:
"index" int: all distinct, 0..38284, avg=19142, median=19142
"PID" text: 37565 distinct, nulls=1
"Name" text: 36312 distinct, nulls=1
"Gender" text: "Male"=20055, "Female"=9435, nulls=8795

indexes: "index"

samples:
| column | latest | sample | sample |
|---|---|---|---|
| index | 38284 | 9040 | 20191 |
| PID | nm1421793 | nm4445339 | nm4701038 |
| Name | Sushma Shiromani |  Lawrie D'Couza |  Ashraf Patel |
| Gender | Female | Male | Male |
