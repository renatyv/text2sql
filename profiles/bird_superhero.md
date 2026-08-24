---
generator: db-snooper
version: 0.0.34
generated_at_utc: 2026-08-24T21:21:18.679857Z
dialect: sqlite
database: /var/folders/9j/b9bx_drd53sc6zbpsqyrjy4h0000gn/T/dbsnoop-j8_b5y0b/superhero.sqlite
schema: main
---

## Relationships

- "alignment"."id" ← "superhero"."alignment_id"
- "attribute"."id" ← "hero_attribute"."attribute_id"
- "colour"."id" ← "superhero"."eye_colour_id", "superhero"."hair_colour_id", "superhero"."skin_colour_id"
- "gender"."id" ← "superhero"."gender_id"
- "publisher"."id" ← "superhero"."publisher_id"
- "race"."id" ← "superhero"."race_id"
- "superhero"."id" ← "hero_attribute"."hero_id", "hero_power"."hero_id"
- "superpower"."id" ← "hero_power"."power_id"

# "alignment"  (rows=4)

columns:
"id" int PK
"alignment" text

indexes: none

all rows:
| column | row 1 | row 2 | row 3 | row 4 |
|---|---|---|---|---|
| id | 1 | 2 | 3 | 4 |
| alignment | Good | Bad | Neutral | N/A |

# "attribute"  (rows=6)

columns:
"id" int PK
"attribute_name" text

indexes: none

all rows:
| column | row 1 | row 2 | row 3 | row 4 | row 5 | row 6 |
|---|---|---|---|---|---|---|
| id | 1 | 2 | 3 | 4 | 5 | 6 |
| attribute_name | Intelligence | Strength | Speed | Durability | Power | Combat |

# "colour"  (rows=35)

columns:
"id" int PK: unique identifier, 1..35
"colour" text: all distinct

indexes: none

samples:
| column | latest | sample | sample |
|---|---|---|---|
| id | 35 | 21 | 15 |
| colour | Yellow/Red | Pink | Green/Blue |

# "gender"  (rows=3)

columns:
"id" int PK
"gender" text

indexes: none

all rows:
| column | row 1 | row 2 | row 3 |
|---|---|---|---|
| id | 1 | 2 | 3 |
| gender | Male | Female | N/A |

# "hero_attribute"  (rows=3738)

columns:
"hero_id" int FK: 623 distinct, 1..756
"attribute_id" int FK: 1=623, 2=623, 3=623, 4=623, 5=623, 6=623, 1..6
"attribute_value" int: 20 distinct, 5..100, avg=52.4264, median=50

indexes: none

samples:
| column | latest | sample | sample |
|---|---|---|---|
| hero_id | 756 | 66 | 124 |
| attribute_id | 6 | 2 | 3 |
| attribute_value | 100 | 55 | 35 |

# "hero_power"  (rows=5825)

columns:
"hero_id" int FK: 652 distinct, 1..756
"power_id" int FK: 167 distinct, 1..167

indexes: none

samples:
| column | latest | sample | sample |
|---|---|---|---|
| hero_id | 756 | 517 | 247 |
| power_id | 132 | 123 | 86 |

# "publisher"  (rows=25)

columns:
"id" int PK: unique identifier, 1..25
"publisher_name" text: all distinct

indexes: none

samples:
| column | latest | sample | sample |
|---|---|---|---|
| id | 25 | 16 | 5 |
| publisher_name | Wildstorm | Rebellion | George Lucas |

# "race"  (rows=61)

columns:
"id" int PK: unique identifier, 1..61
"race" text: all distinct

indexes: none

samples:
| column | latest | sample | sample |
|---|---|---|---|
| id | 61 | 60 | 15 |
| race | Zombie | Zen-Whoberian | Dathomirian Zabrak |

# "superhero"  (rows=750)

columns:
"id" int PK: unique identifier, 1..756
"superhero_name" text: 743 distinct
"full_name" text: 483 distinct, nulls=122
"gender_id" int FK: 1=519, 2=203, 3=28, 1..3
"eye_colour_id" int FK: 21 distinct, 1..35
"hair_colour_id" int FK: 26 distinct, 1..33
"skin_colour_id" int FK: 1=681, 14=21, 7=9, 23=9, 31=7, 28=5, 13=4, 22=3, 12=2, 21=2, 33=2, 4=1, 8=1, 19=1, 20=1, 24=1, 1..33
"race_id" int FK: 61 distinct, nulls=4, 1..61
"publisher_id" int FK: 25 distinct, nulls=3, 1..25
"alignment_id" int FK: 1=504, 2=212, 3=28, nulls=6, 1..3
"height_cm" int: 55 distinct, nulls=58, 0..30480, avg=267.751, median=178
"weight_kg" int: 140 distinct, nulls=64, 0..90000000, avg=144518, median=72

indexes: none

samples:
| column | latest | sample | sample |
|---|---|---|---|
| id | 756 | 364 | 635 |
| superhero_name | Zoom | James T. Kirk | Space Ghost |
| full_name | Hunter Zolomon | James Tiberius Kirk | Thaddeus Bach |
| gender_id | 1 | 1 | 1 |
| eye_colour_id | 23 | 16 | 1 |
| hair_colour_id | 9 | 9 | 1 |
| skin_colour_id | 1 | 1 | 1 |
| race_id | 1 | 24 | 24 |
| publisher_id | 4 | 20 | 4 |
| alignment_id | 2 | 1 | 1 |
| height_cm | 185 | 178 | 188 |
| weight_kg | 81 | 77 | 113 |

# "superpower"  (rows=167)

columns:
"id" int PK: unique identifier, 1..167
"power_name" text: all distinct

indexes: none

samples:
| column | latest | sample | sample |
|---|---|---|---|
| id | 167 | 151 | 121 |
| power_name | Omniscient | Vision - Heat | Spatial Awareness |
