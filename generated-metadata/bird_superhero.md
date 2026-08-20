# Additional Metadata

## Clarified Semantics

- `superhero.id` ranges 1..756 but the table holds only 750 rows; ids are non-contiguous (gaps), so joins should use FK equality, not id arithmetic.
- `hero_attribute.attribute_value` is an integer on a 5..100 scale of multiples of 5 (20 distinct values); it is the character's stat for that attribute, not a rank or boolean.
- `hero_attribute` is complete per hero: every one of the six attribute ids appears for every hero, so one attribute filter does not restrict hero set; filtering instead narrows the stat value.
- `superhero.weight_kg` (max 90,000,000; avg 144,518) and `height_cm` (max 30,480) contain extreme outliers and zeros, so raw aggregates are misleading; median (72 kg / 178 cm) is the robust central tendency.
- `superhero.superhero_name` is 743 distinct over 750 rows (aliases/duplicates); `full_name` has 122 nulls and only 483 distinct values (multiple heroes share real names).
- `colour`, `race`, `publisher`, and `superpower` are flat lookup dictionaries with no other columns; id is the only meaningful join key.
- The `colour` table serves all three colour axes (eye/hair/skin), each of which references only a subset of the 35 colours (21, 26, and ~13 distinct values respectively).
- `publisher` includes a blank/empty-string publisher_name, and `publisher_id`/`race_id`/`alignment_id` contain NULLs, so counts must account for nulls.

## Potential Join Strategies

- Join `superhero` to `colour` three separate times, once per body-colour FK: `colour.id = superhero.eye_colour_id`, `.hair_colour_id`, and `.skin_colour_id`; use different table aliases and match each colour attribute independently (e.g. heroes with blond hair + blue eyes).
- Join `superhero` → `hero_attribute` on `hero_attribute.hero_id = superhero.id` and `hero_attribute.attribute_id = attribute.id` to map stat name to value; filter on `attribute_value` only when a numeric stat threshold is intended.
- Join `superhero` → `hero_power` on `hero_id`, and `hero_power.power_id = superpower.id` to resolve power names; a single hero can hold many `hero_power` rows (up to 167 distinct powers), so hero-count queries over heroes matching one power need `COUNT(DISTINCT superhero.id)`.
- `hero_attribute.hero_id` has 623 distinct ids vs `superhero` 750 rows and `hero_power` 652 distinct ids — not every hero has attribute/power rows, so these are inner joins only over a subset of heroes.
- Join filters on multiple powers/attributes require self-joins (multiple `hero_power` aliases keyed on the same `hero_id`) rather than OR filters, to capture heroes that satisfy all conditions.
- Publisher-aware queries join `superhero.publisher_id = publisher.id`; treat the blank-named publisher row and the 3 NULL publisher ids as distinct buckets when grouping.
- Skin-colour aggregations are heavily skewed: colour id 1 (default) accounts for 681 of 750 heroes, so measures on `skin_colour_id` are dominated by the single majority value and are rarely discriminating.