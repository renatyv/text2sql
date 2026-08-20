---
generator: db-snooper
version: 0.0.31
generated_at_utc: 2026-08-20T17:27:02.053243Z
dialect: sqlite
database: /var/folders/9j/b9bx_drd53sc6zbpsqyrjy4h0000gn/T/dbsnoop-6k_cxowt/Db-IMDB.sqlite
schema: main
---

# "Country"  (rows=34)

columns:
"index" int: all distinct, 0..33, avg=16.5, median=16.5
"Name" text: all distinct
"CID" int: unique identifier, 0..33, avg=16.5, median=16.5

indexes: "index"
fk: none

samples:
| column | latest | sample | sample |
|---|---|---|---|
| index | 33 | 2 | 16 |
| Name | Georgia | India | Pakistan |
| CID | 33 | 2 | 16 |

# "Genre"  (rows=328)

columns:
"index" int: all distinct, 0..327, avg=163.5, median=163.5
"Name" text: all distinct
"GID" int: unique identifier, 0..327, avg=163.5, median=163.5

indexes: "index"
fk: none

samples:
| column | latest | sample | sample |
|---|---|---|---|
| index | 327 | 203 | 249 |
| Name | Drama, Mystery, Sci-Fi             | Action, Comedy, Mystery             | Comedy, Drama, Mystery             |
| GID | 327 | 203 | 249 |

# "Language"  (rows=32)

columns:
"index" int: all distinct, 0..31, avg=15.5, median=15.5
"Name" text: all distinct
"LAID" int: unique identifier, 0..31, avg=15.5, median=15.5

indexes: "index"
fk: none

samples:
| column | latest | sample | sample |
|---|---|---|---|
| index | 31 | 15 | 31 |
| Name | Georgian | Kannada | Georgian |
| LAID | 31 | 15 | 31 |

# "Location"  (rows=559)

columns:
"index" int: all distinct, 0..558, avg=279, median=279
"Name" text: all distinct
"LID" int: unique identifier, 0..558, avg=279, median=279

indexes: "index"
fk: none

samples:
| column | latest | sample | sample |
|---|---|---|---|
| index | 558 | 421 | 353 |
| Name | Aftab Studio, India | Haryana, India | Coorg, Karnataka, India |
| LID | 558 | 421 | 353 |

# "M_Cast"  (rows=82837)

columns:
"index" int: all distinct, 0..82836, avg=41418, median=41418
"MID" text: 3475 distinct
"PID" text: 32127 distinct, nulls=2
"ID" int: unique identifier, 0..82836, avg=41418, median=41418

indexes: "index"
fk: none

samples:
| column | latest | sample | sample |
|---|---|---|---|
| index | 82836 | 34068 | 24136 |
| MID | tt0375890 | tt0232079 | tt0118751 |
| PID |  nm0438467 |  nm0044085 |  nm1623050 |
| ID | 82836 | 34068 | 24136 |

# "M_Country"  (rows=3475)

columns:
"index" int: all distinct, 0..3474, avg=1737, median=1737
"MID" text: unique identifier
"CID" float: 34 distinct, nulls=5, 0..33, avg=2.1781, median=2
"ID" int: unique identifier, 0..3474, avg=1737, median=1737

indexes: "index"
fk: none

samples:
| column | latest | sample | sample |
|---|---|---|---|
| index | 3474 | 1228 | 600 |
| MID | tt0375890 | tt2319889 | tt0444767 |
| CID | 2 | 2 | 2 |
| ID | 3474 | 1228 | 600 |

# "M_Director"  (rows=3475)

columns:
"index" int: all distinct, 0..3474, avg=1737, median=1737
"MID" text: unique identifier
"PID" text: 1464 distinct
"ID" int: unique identifier, 0..3474, avg=1737, median=1737

indexes: "index"
fk: none

samples:
| column | latest | sample | sample |
|---|---|---|---|
| index | 3474 | 2789 | 2522 |
| MID | tt0375890 | tt1191118 | tt0100401 |
| PID | nm1421793 | nm2124532 | nm0684314 |
| ID | 3474 | 2789 | 2522 |

# "M_Genre"  (rows=3475)

columns:
"index" int: all distinct, 0..3474, avg=1737, median=1737
"MID" text: unique identifier
"GID" int: 328 distinct, 0..327, avg=62.7606, median=46
"ID" int: unique identifier, 0..3474, avg=1737, median=1737

indexes: "index"
fk: none

samples:
| column | latest | sample | sample |
|---|---|---|---|
| index | 3474 | 2033 | 1378 |
| MID | tt0375890 | tt0118931 | tt0096827 |
| GID | 46 | 36 | 23 |
| ID | 3474 | 2033 | 1378 |

# "M_Language"  (rows=3475)

columns:
"index" int: all distinct, 0..3474, avg=1737, median=1737
"MID" text: unique identifier
"LAID" int: 32 distinct, 0..31, avg=2.55367, median=2
"ID" int: unique identifier, 0..3474, avg=1737, median=1737

indexes: "index"
fk: none

samples:
| column | latest | sample | sample |
|---|---|---|---|
| index | 3474 | 1742 | 565 |
| MID | tt0375890 | tt0250483 | tt0072783 |
| LAID | 2 | 2 | 2 |
| ID | 3474 | 1742 | 565 |

# "M_Location"  (rows=3475)

columns:
"index" int: all distinct, 0..3474, avg=1737, median=1737
"MID" text: unique identifier
"LID" float: 559 distinct, nulls=1626, 0..558, avg=166.056, median=124
"ID" int: unique identifier, 0..3474, avg=1737, median=1737

indexes: "index"
fk: none

samples:
| column | latest | sample | sample |
|---|---|---|---|
| index | 3474 | 360 | 2961 |
| MID | tt0375890 | tt3802576 | tt2953786 |
| LID | 7 | 16 | 528 |
| ID | 3474 | 360 | 2961 |

# "M_Producer"  (rows=11751)

columns:
"index" int: all distinct, 0..11750, avg=5875, median=5875
"MID" text: 3475 distinct
"PID" text: 5436 distinct, nulls=21
"ID" int: unique identifier, 0..11750, avg=5875, median=5875

indexes: "index"
fk: none

samples:
| column | latest | sample | sample |
|---|---|---|---|
| index | 11750 | 4031 | 1846 |
| MID | tt0375890 | tt1992138 | tt6514010 |
| PID |  nm1421793 |  nm3083004 |  nm5720462 |
| ID | 11750 | 4031 | 1846 |

# "Movie"  (rows=3475)

columns:
"index" int: all distinct, 0..3474, avg=1737, median=1737
"MID" text: unique identifier
"title" text: 3344 distinct
"year" text: 125 distinct
"rating" float: 82 distinct, 1.3..9.6, avg=6.03678, median=6.2
"num_votes" int: 1763 distinct, 51..1137529, avg=4544.73, median=388

indexes: "index"
fk: none

samples:
| column | latest | sample | sample |
|---|---|---|---|
| index | 3474 | 2758 | 3149 |
| MID | tt0375890 | tt1204913 | tt0267617 |
| title | Kanoon | Karma: Crime. Passion. Reincarnation | Jigar |
| year | 1994 | 2008 | 1992 |
| rating | 3.2 | 5.9 | 4.8 |
| num_votes | 103 | 99 | 670 |

# "Person"  (rows=38285)

columns:
"index" int: all distinct, 0..38284, avg=19142, median=19142
"PID" text: 37565 distinct, nulls=1
"Name" text: 36312 distinct, nulls=1
"Gender" text: "Male"=20055, "Female"=9435, nulls=8795

indexes: "index"
fk: none

samples:
| column | latest | sample | sample |
|---|---|---|---|
| index | 38284 | 33740 | 23026 |
| PID | nm1421793 | nm0080299 | nm1560914 |
| Name | Sushma Shiromani |  Vanraj Bhatia |  Aroop Kumar Ganguly |
| Gender | Female | null | Male |
