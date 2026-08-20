# Schema Links

- version: 0.0.5
- dialect: sqlite
- database: file:/Users/renatyuldashev/Documents/ai-sql/custom-bench/data/bird_mini_dev/databases/dev_databases/card_games/card_games.sqlite
- schema: main

## Declared PK/FK Links

foreign_data.uuid -> cards.uuid
legalities.uuid -> cards.uuid
rulings.uuid -> cards.uuid
set_translations.setCode -> sets.code

## Inferred Links

No inferred links found.
