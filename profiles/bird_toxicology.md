---
generator: db-snooper
version: 0.0.31
generated_at_utc: 2026-08-20T17:26:40.231024Z
dialect: sqlite
database: /var/folders/9j/b9bx_drd53sc6zbpsqyrjy4h0000gn/T/dbsnoop-od4dnj41/toxicology.sqlite
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
fk: "molecule_id"→"molecule"."molecule_id"

samples:
| column | latest | sample | sample |
|---|---|---|---|
| atom_id | TR501_9 | TR446_22 | TR107_17 |
| molecule_id | TR501 | TR446 | TR107 |
| element | c | c | h |

# "bond"  (rows=9156)

columns:
"bond_id" text PK: unique identifier
"molecule_id" text FK: 343 distinct
"bond_type" text: "-"=7743, "="=1408, "#"=5

indexes: none
fk: "molecule_id"→"molecule"."molecule_id"

samples:
| column | latest | sample | sample |
|---|---|---|---|
| bond_id | TR501_9_21 | TR435_18_43 | TR378_2_10 |
| molecule_id | TR501 | TR435 | TR378 |
| bond_type | - | - | - |

# "connected"  (rows=18312)

columns:
"atom_id" text PK FK: 9073 distinct, "TR000_2"=4, "TR001_1"=4, "TR001_2"=4, "TR001_3"=4, "TR001_4"=4, "TR001_5"=4, "TR001_6"=4, "TR001_7"=4, "TR001_8"=4, "TR001_9"=4
"atom_id2" text PK FK: 9073 distinct, "TR000_2"=4, "TR001_1"=4, "TR001_2"=4, "TR001_3"=4, "TR001_4"=4, "TR001_5"=4, "TR001_6"=4, "TR001_7"=4, "TR001_8"=4, "TR001_9"=4
"bond_id" text FK: 9156 distinct

indexes: none
fk: "bond_id"→"bond"."bond_id", "atom_id"→"atom"."atom_id", "atom_id2"→"atom"."atom_id"

samples:
| column | latest | sample | sample |
|---|---|---|---|
| atom_id | TR501_9 | TR151_3 | TR405_37 |
| atom_id2 | TR501_5 | TR151_10 | TR405_38 |
| bond_id | TR501_5_9 | TR151_3_10 | TR405_37_38 |

# "molecule"  (rows=343)

columns:
"molecule_id" text PK: unique identifier
"label" text: "-"=191, "+"=152

indexes: none
fk: none

samples:
| column | latest | sample | sample |
|---|---|---|---|
| molecule_id | TR501 | TR298 | TR311 |
| label | - | + | + |
