---
generator: db-snooper
version: 0.0.26
generated_at_utc: 2026-08-16T07:19:20.985681Z
dialect: sqlite
database: /Users/renatyuldashev/Documents/ai-sql/custom-bench/data/bird_mini_dev/databases/dev_databases/toxicology/toxicology.sqlite
schema: main
---

## Relationships

- atom.atom_id ← connected.atom_id, connected.atom_id2
- bond.bond_id ← connected.bond_id
- molecule.molecule_id ← atom.molecule_id, bond.molecule_id

# atom

```sql
CREATE TABLE `atom` (
  `atom_id` TEXT NOT NULL,
  `molecule_id` TEXT DEFAULT NULL,
  `element` TEXT DEFAULT NULL,
  PRIMARY KEY (`atom_id`),
  FOREIGN KEY (`molecule_id`) REFERENCES `molecule` (`molecule_id`)
);
```

## Rows

- total=9111

| column | latest | sample | sample |
|---|---|---|---|
| atom_id | TR501_9 | TR435_8 | TR050_26 |
| molecule_id | TR501 | TR435 | TR050 |
| element | c | c | h |

## Columns

- atom_id: unique identifier
- molecule_id: 343 distinct
- element: "h"=4034, "c"=3433, "o"=737, "n"=373, "cl"=317, "s"=94, "br"=46, "na"=32, "p"=23, "f"=10, "i"=3, "cu"=2, "sn"=2, "ca"=1, "k"=1, "pb"=1, "y"=1, "zn"=1


# bond

```sql
CREATE TABLE `bond` (
  `bond_id` TEXT NOT NULL,
  `molecule_id` TEXT DEFAULT NULL,
  `bond_type` TEXT DEFAULT NULL,
  PRIMARY KEY (`bond_id`),
  FOREIGN KEY (`molecule_id`) REFERENCES `molecule` (`molecule_id`)
);
```

## Rows

- total=9156

| column | latest | sample | sample |
|---|---|---|---|
| bond_id | TR501_9_21 | TR036_1_2 | TR322_26_27 |
| molecule_id | TR501 | TR036 | TR322 |
| bond_type | - | = | - |

## Columns

- bond_id: unique identifier
- molecule_id: 343 distinct
- bond_type: "-"=7743, "="=1408, "#"=5


# connected

```sql
CREATE TABLE `connected` (
  `atom_id` TEXT NOT NULL,
  `atom_id2` TEXT NOT NULL,
  `bond_id` TEXT DEFAULT NULL,
  PRIMARY KEY (`atom_id`,`atom_id2`),
  FOREIGN KEY (`atom_id`) REFERENCES `atom` (`atom_id`) ON DELETE CASCADE ON UPDATE CASCADE,
  FOREIGN KEY (`atom_id2`) REFERENCES `atom` (`atom_id`) ON DELETE CASCADE ON UPDATE CASCADE,
  FOREIGN KEY (`bond_id`) REFERENCES `bond` (`bond_id`) ON DELETE CASCADE ON UPDATE CASCADE
);
```

## Rows

- total=18312

| column | latest | sample | sample |
|---|---|---|---|
| atom_id | TR501_9 | TR430_79 | TR092_10 |
| atom_id2 | TR501_5 | TR430_80 | TR092_22 |
| bond_id | TR501_5_9 | TR430_79_80 | TR092_10_22 |

## Columns

- atom_id: 9073 distinct
  - top_values: "TR000_2"=4, "TR001_1"=4, "TR001_2"=4, "TR001_3"=4, "TR001_4"=4, "TR001_5"=4, "TR001_6"=4, "TR001_7"=4, "TR001_8"=4, "TR001_9"=4
- atom_id2: 9073 distinct
  - top_values: "TR000_2"=4, "TR001_1"=4, "TR001_2"=4, "TR001_3"=4, "TR001_4"=4, "TR001_5"=4, "TR001_6"=4, "TR001_7"=4, "TR001_8"=4, "TR001_9"=4
- bond_id: 9156 distinct


# molecule

```sql
CREATE TABLE `molecule` (
  `molecule_id` TEXT NOT NULL,
  `label` TEXT DEFAULT NULL,
  PRIMARY KEY (`molecule_id`)
);
```

## Rows

- total=343

| column | latest | sample | sample |
|---|---|---|---|
| molecule_id | TR501 | TR309 | TR316 |
| label | - | + | + |

## Columns

- molecule_id: unique identifier
- label: "-"=191, "+"=152
