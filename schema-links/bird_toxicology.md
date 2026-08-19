# Schema Links

- generator: local introspection
- dialect: sqlite
- database: toxicology

## Declared Links

- `atom.molecule_id` → `molecule.molecule_id`
- `bond.molecule_id` → `molecule.molecule_id`
- `connected.atom_id` → `atom.atom_id`
- `connected.atom_id2` → `atom.atom_id`
- `connected.bond_id` → `bond.bond_id`

## Same-name Candidates

- `atom_id`: `atom.atom_id`, `connected.atom_id`
- `bond_id`: `bond.bond_id`, `connected.bond_id`
- `molecule_id`: `atom.molecule_id`, `bond.molecule_id`, `molecule.molecule_id`
