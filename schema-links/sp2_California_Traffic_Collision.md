# Schema Links

- version: 0.0.5
- dialect: sqlite
- database: file:/Users/renatyuldashev/Documents/ai-sql/custom-bench/data/sp2_lite_sqlite/databases/California_Traffic_Collision.sqlite
- schema: main

## Declared PK/FK Links

No declared PK/FK links found.

## Inferred Links

### victims
- inferred: collisions.injured_victims, collisions.killed_victims, victims.victim_age

### party
- inferred: collisions.party_count, victims.party_number
