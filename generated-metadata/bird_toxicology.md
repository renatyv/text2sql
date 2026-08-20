# Additional Metadata

## Clarified Semantics

- `molecule.label` is a binary activity/toxicity outcome: `+` (152 molecules) vs `-` (191 molecules). `<molecule_id>` values (`TR###`) identify individual molecular structures, and bond/atom ids embed the molecule id as a prefix.
- `connected` is an *undirected* adjacency representation of the molecular graph, stored redundantly: every bond contributes **two** ordered rows (`(atom_id, atom_id2)` and `(atom_id2, atom_id)`). Confirmed: 18,312 rows = 9,156 bonds × 2, every `bond_id` appears exactly twice, and no `atom_id = atom_id2` self-rows exist.
- `connected` is a two-step indirection: it links `atom` and `atom_id2` through a shared `bond_id`, rather than storing a structural property of the atoms themselves.
- `atom.bond_id`-dependent attributes live on `bond` (bond_type), while atom attributes live on `atom` (element); traversal between the two requires passing through `connected`.
- `bond.bond_type` encodes bond order: `-` single (7,743), `=` double (1,408), `#` triple (5). Only 2,216 of 9,156 bonds are non-single.
- `atom.element` is dominated by a small number of elements (`h`, `c` make up ~82%), with many rare elements present as singletons.
- FK cascades exist (`ON DELETE CASCADE`) only on `connected`'s FKs to `atom`/`bond`; `atom.molecule_id` and `bond.molecule_id` have plain FKs (no cascade).

## Potential Join Strategies

- Molecule → atoms: join `molecule.molecule_id = atom.molecule_id`. One `molecule` fans out to many atoms (343 molecules vs 9,111 atoms). Element/atom counts are only meaningful after restricting to a single molecule or a label group.
- Molecule → bonds: join `molecule.molecule_id = bond.molecule_id`; same fan-out shape (343 → 9,156). Use this to look at bond_type distributions per molecule (e.g., count triple bonds under a label).
- Atom ↔ atom neighbor lookup: join `atom` to `connected.atom_id = atom.atom_id` then `connected.atom_id2` back to a second `atom` instance — yields full neighbor lists; because rows are stored both directions, always pair by `atom_id`/`atom_id2` or cap ordering rather than counting both ways to avoid double-counts.
- Atom ↔ bond through connected: `connected` is the pivot: join `connected.atom_id → atom.atom_id` and `connected.bond_id → bond.bond_id`, then `bond.molecule_id → molecule.molecule_id`. This assembles per-bond incident atoms for one molecule.
- Full molecule-of-`molecule_id` constraint cartesian risk: because every `connected` row touches two atoms and the adjacency is doubled, join only within a fixed molecule (filter on shared `molecule_id`) to avoid counting edges more than once.