# Schema Links

- version: 0.0.5
- dialect: sqlite
- database: file:/Users/renatyuldashev/Documents/ai-sql/custom-bench/data/bird_mini_dev/databases/dev_databases/toxicology/toxicology.sqlite
- schema: main

## Declared PK/FK Links

atom.molecule_id -> molecule.molecule_id
bond.molecule_id -> molecule.molecule_id
connected.atom_id -> atom.atom_id
connected.atom_id2 -> atom.atom_id
connected.bond_id -> bond.bond_id

## Inferred Links

All inferred links are implied by the declared PK/FK links above.
