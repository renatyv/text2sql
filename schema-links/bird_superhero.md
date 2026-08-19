# Schema Links

- generator: local introspection
- dialect: sqlite
- database: superhero

## Declared Links

- `hero_attribute.attribute_id` → `attribute.id`
- `hero_attribute.hero_id` → `superhero.id`
- `hero_power.hero_id` → `superhero.id`
- `hero_power.power_id` → `superpower.id`
- `superhero.alignment_id` → `alignment.id`
- `superhero.eye_colour_id` → `colour.id`
- `superhero.gender_id` → `gender.id`
- `superhero.hair_colour_id` → `colour.id`
- `superhero.publisher_id` → `publisher.id`
- `superhero.race_id` → `race.id`
- `superhero.skin_colour_id` → `colour.id`

## Same-name Candidates

- `hero_id`: `hero_attribute.hero_id`, `hero_power.hero_id`
