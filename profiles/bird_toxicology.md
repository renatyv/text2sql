---
generator: db-snooper
version: 0.0.34
generated_at_utc: 2026-08-24T21:56:15.563927Z
dialect: sqlite
database: /var/folders/9j/b9bx_drd53sc6zbpsqyrjy4h0000gn/T/dbsnoop-mjhpf_eh/toxicology.sqlite
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
| atom_id | TR501_9 | TR033_23 | TR359_8 |
| molecule_id | TR501 | TR033 | TR359 |
| element | c | h | c |

# "bond"  (rows=9156)

columns:
"bond_id" text PK: unique identifier
"molecule_id" text FK: 343 distinct
"bond_type" text: "-"=7743, "="=1408, "#"=5

indexes: none

samples:
| column | latest | sample | sample |
|---|---|---|---|
| bond_id | TR501_9_21 | TR193_42_77 | TR424_4_9 |
| molecule_id | TR501 | TR193 | TR424 |
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
| atom_id | TR501_9 | TR007_12 | TR033_7 |
| atom_id2 | TR501_5 | TR007_27 | TR033_4 |
| bond_id | TR501_5_9 | TR007_12_27 | TR033_4_7 |

# "molecule"  (rows=343)

columns:
"molecule_id" text PK: unique identifier
"label" text: "-"=191, "+"=152

indexes: none

samples:
| column | latest | sample | sample |
|---|---|---|---|
| molecule_id | TR501 | TR226 | TR373 |
| label | - | + | - |
