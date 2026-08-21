---
generator: db-snooper
version: 0.0.33
generated_at_utc: 2026-08-21T12:31:49.386689Z
dialect: sqlite
database: /var/folders/9j/b9bx_drd53sc6zbpsqyrjy4h0000gn/T/dbsnoop-pvghbozp/toxicology.sqlite
schema: main
---

## Relationships

- "atom"."atom_id" ← "connected"."atom_id", "connected"."atom_id2"
- "bond"."bond_id" ← "connected"."bond_id"
- "molecule"."molecule_id" ← "atom"."molecule_id", "bond"."molecule_id"

# "atom"  (rows=9111)

columns:
"atom_id" text PK: unique identifier
"molecule_id" text FK: 343 distinct
"element" text: "h"=4034, "c"=3433, "o"=737, "n"=373, "cl"=317, "s"=94, "br"=46, "na"=32, "p"=23, "f"=10, "i"=3, "cu"=2, "sn"=2, "ca"=1, "k"=1, "pb"=1, "y"=1, "zn"=1

indexes: none

samples:
| column | latest | sample | sample |
|---|---|---|---|
| atom_id | TR501_9 | TR099_10 | TR049_3 |
| molecule_id | TR501 | TR099 | TR049 |
| element | c | n | c |

# "bond"  (rows=9156)

columns:
"bond_id" text PK: unique identifier
"molecule_id" text FK: 343 distinct
"bond_type" text: "-"=7743, "="=1408, "#"=5

indexes: none

samples:
| column | latest | sample | sample |
|---|---|---|---|
| bond_id | TR501_9_21 | TR390_7_19 | TR134_8_28 |
| molecule_id | TR501 | TR390 | TR134 |
| bond_type | - | - | - |

# "connected"  (rows=18312)

columns:
"atom_id" text PK FK: 9073 distinct
"atom_id2" text PK FK: 9073 distinct
"bond_id" text FK: 9156 distinct

indexes: none

samples:
| column | latest | sample | sample |
|---|---|---|---|
| atom_id | TR501_9 | TR173_8 | TR030_4 |
| atom_id2 | TR501_5 | TR173_18 | TR030_2 |
| bond_id | TR501_5_9 | TR173_8_18 | TR030_2_4 |

# "molecule"  (rows=343)

columns:
"molecule_id" text PK: unique identifier
"label" text: "-"=191, "+"=152

indexes: none

samples:
| column | latest | sample | sample |
|---|---|---|---|
| molecule_id | TR501 | TR234 | TR483 |
| label | - | + | + |
