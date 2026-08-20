# Schema Links

- version: 0.0.5
- dialect: sqlite
- database: file:/Users/renatyuldashev/Documents/ai-sql/custom-bench/data/bird_mini_dev/databases/dev_databases/superhero/superhero.sqlite
- schema: main

## Declared PK/FK Links

hero_attribute.attribute_id -> attribute.id
hero_attribute.hero_id -> superhero.id
hero_power.hero_id -> superhero.id
hero_power.power_id -> superpower.id
superhero.alignment_id -> alignment.id
superhero.eye_colour_id -> colour.id
superhero.gender_id -> gender.id
superhero.hair_colour_id -> colour.id
superhero.publisher_id -> publisher.id
superhero.race_id -> race.id
superhero.skin_colour_id -> colour.id

## Inferred Links

All inferred links are implied by the declared PK/FK links above.
