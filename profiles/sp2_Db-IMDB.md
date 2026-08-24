---
generator: db-snooper
version: 0.0.34
generated_at_utc: 2026-08-24T21:57:18.282010Z
dialect: sqlite
database: /var/folders/9j/b9bx_drd53sc6zbpsqyrjy4h0000gn/T/dbsnoop-h21mm3tt/Db-IMDB.sqlite
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
| index | 33 | 27 | 8 |
| Name | Georgia | Iran | Belgium |
| CID | 33 | 27 | 8 |

# "Genre"  (rows=328)

columns:
"index" int: all distinct, 0..327, avg=163.5, median=163.5
"Name" text: all distinct
"GID" int: unique identifier, 0..327, avg=163.5, median=163.5

indexes: "index"

samples:
| column | latest | sample | sample |
|---|---|---|---|
| index | 327 | 34 | 234 |
| Name | Drama, Mystery, Sci-Fi             | Drama, Thriller             | Comedy, Crime, Romance             |
| GID | 327 | 34 | 234 |

# "Language"  (rows=32)

columns:
"index" int: all distinct, 0..31, avg=15.5, median=15.5
"Name" text: all distinct
"LAID" int: unique identifier, 0..31, avg=15.5, median=15.5

indexes: "index"

samples:
| column | latest | sample | sample |
|---|---|---|---|
| index | 31 | 16 | 10 |
| Name | Georgian | Japanese | Spanish |
| LAID | 31 | 16 | 10 |

# "Location"  (rows=559)

columns:
"index" int: all distinct, 0..558, avg=279, median=279
"Name" text: all distinct
"LID" int: unique identifier, 0..558, avg=279, median=279

indexes: "index"

samples:
| column | latest | sample | sample |
|---|---|---|---|
| index | 558 | 348 | 50 |
| Name | Aftab Studio, India | Holy Spirit Hospital, Andheri, Mumbai, Maharashtra, India | Stage 11, Warner Brothers Burbank Studios - 4000 Warner Boulevard, Burbank, California, USA |
| LID | 558 | 348 | 50 |

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
| index | 82836 | 14329 | 13317 |
| MID | tt0375890 | tt0118983 | tt2609218 |
| PID |  nm0438467 |  nm1022366 |  nm1586516 |
| ID | 82836 | 14329 | 13317 |

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
| index | 3474 | 1443 | 511 |
| MID | tt0375890 | tt0246420 | tt0498351 |
| CID | 2 | 2 | 1 |
| ID | 3474 | 1443 | 511 |

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
| index | 3474 | 2874 | 3089 |
| MID | tt0375890 | tt0423087 | tt0485204 |
| PID | nm1421793 | nm1374768 | nm0049335 |
| ID | 3474 | 2874 | 3089 |

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
| index | 3474 | 2416 | 3200 |
| MID | tt0375890 | tt0081968 | tt0097926 |
| GID | 46 | 5 | 179 |
| ID | 3474 | 2416 | 3200 |

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
| index | 3474 | 3312 | 1508 |
| MID | tt0375890 | tt2924844 | tt0363833 |
| LAID | 2 | 15 | 2 |
| ID | 3474 | 3312 | 1508 |

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
| index | 3474 | 1116 | 1968 |
| MID | tt0375890 | tt0311413 | tt0095198 |
| LID | 7 | null | null |
| ID | 3474 | 1116 | 1968 |

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
| index | 11750 | 5138 | 739 |
| MID | tt0375890 | tt0126871 | tt0051383 |
| PID |  nm1421793 |  nm1159481 |  nm0196536 |
| ID | 11750 | 5138 | 739 |

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
| index | 3474 | 3266 | 1375 |
| MID | tt0375890 | tt0213532 | tt0843328 |
| title | Kanoon | Budtameez | Chatrapathi |
| year | 1994 | 1966 | 2005 |
| rating | 3.2 | 7.4 | 7.6 |
| num_votes | 103 | 54 | 3339 |

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
| index | 38284 | 31017 | 32138 |
| PID | nm1421793 | nm4634246 | nm3355596 |
| Name | Sushma Shiromani |  Urmi Khakkar |  Sandino Moya-Smith |
| Gender | Female | Female | null |
