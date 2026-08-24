---
generator: db-snooper
version: 0.0.34
generated_at_utc: 2026-08-24T21:21:44.218692Z
dialect: sqlite
database: /var/folders/9j/b9bx_drd53sc6zbpsqyrjy4h0000gn/T/dbsnoop-tddvw4eh/Db-IMDB.sqlite
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
| index | 33 | 6 | 24 |
| Name | Georgia | Canada | South Africa |
| CID | 33 | 6 | 24 |

# "Genre"  (rows=328)

columns:
"index" int: all distinct, 0..327, avg=163.5, median=163.5
"Name" text: all distinct
"GID" int: unique identifier, 0..327, avg=163.5, median=163.5

indexes: "index"

samples:
| column | latest | sample | sample |
|---|---|---|---|
| index | 327 | 132 | 184 |
| Name | Drama, Mystery, Sci-Fi             | Adventure, Drama, Romance             | Adventure, Romance             |
| GID | 327 | 132 | 184 |

# "Language"  (rows=32)

columns:
"index" int: all distinct, 0..31, avg=15.5, median=15.5
"Name" text: all distinct
"LAID" int: unique identifier, 0..31, avg=15.5, median=15.5

indexes: "index"

samples:
| column | latest | sample | sample |
|---|---|---|---|
| index | 31 | 5 | 23 |
| Name | Georgian | Mandarin | Sanskrit |
| LAID | 31 | 5 | 23 |

# "Location"  (rows=559)

columns:
"index" int: all distinct, 0..558, avg=279, median=279
"Name" text: all distinct
"LID" int: unique identifier, 0..558, avg=279, median=279

indexes: "index"

samples:
| column | latest | sample | sample |
|---|---|---|---|
| index | 558 | 236 | 538 |
| Name | Aftab Studio, India | Mohan Studios, Mumbai, Maharashtra, India | Ye Olde Cheshire Cheese, Fleet Street, London, UK |
| LID | 558 | 236 | 538 |

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
| index | 82836 | 30533 | 43668 |
| MID | tt0375890 | tt0371735 | tt0148706 |
| PID |  nm0438467 |  nm0451379 |  nm1677538 |
| ID | 82836 | 30533 | 43668 |

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
| index | 3474 | 59 | 786 |
| MID | tt0375890 | tt7720922 | tt0121989 |
| CID | 2 | 2 | 2 |
| ID | 3474 | 59 | 786 |

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
| index | 3474 | 773 | 870 |
| MID | tt0375890 | tt0084667 | tt2633598 |
| PID | nm1421793 | nm0802693 | nm2219430 |
| ID | 3474 | 773 | 870 |

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
| index | 3474 | 1143 | 2940 |
| MID | tt0375890 | tt2571140 | tt0121659 |
| GID | 46 | 112 | 10 |
| ID | 3474 | 1143 | 2940 |

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
| index | 3474 | 3274 | 27 |
| MID | tt0375890 | tt5049906 | tt5474036 |
| LAID | 2 | 2 | 2 |
| ID | 3474 | 3274 | 27 |

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
| index | 3474 | 1120 | 3184 |
| MID | tt0375890 | tt3776484 | tt0361515 |
| LID | 7 | 115 | 297 |
| ID | 3474 | 1120 | 3184 |

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
| index | 11750 | 10242 | 4737 |
| MID | tt0375890 | tt0094958 | tt0433425 |
| PID |  nm1421793 |  nm0451211 |  nm1663638 |
| ID | 11750 | 10242 | 4737 |

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
| index | 3474 | 342 | 2463 |
| MID | tt0375890 | tt7142506 | tt6189880 |
| title | Kanoon | Sir | Alif |
| year | 1994 | I 2018 | I 2017 |
| rating | 3.2 | 7 | 6.7 |
| num_votes | 103 | 146 | 116 |

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
| index | 38284 | 9068 | 28896 |
| PID | nm1421793 | nm0202111 | nm1783471 |
| Name | Sushma Shiromani |  Master Farzaan Dastoor |  Mahendra Singh |
| Gender | Female | Male | Male |
