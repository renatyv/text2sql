# Schema Links

- generator: local introspection
- dialect: sqlite
- database: card_games

## Declared Links

- `foreign_data.uuid` → `cards.uuid`
- `legalities.uuid` → `cards.uuid`
- `rulings.uuid` → `cards.uuid`
- `set_translations.setCode` → `sets.code`

## Same-name Candidates

- `flavorText`: `cards.flavorText`, `foreign_data.flavorText`
- `isOnlineOnly`: `cards.isOnlineOnly`, `sets.isOnlineOnly`
- `language`: `foreign_data.language`, `set_translations.language`
- `mcmId`: `cards.mcmId`, `sets.mcmId`
- `name`: `cards.name`, `foreign_data.name`, `sets.name`
- `setCode`: `cards.setCode`, `set_translations.setCode`
- `text`: `cards.text`, `foreign_data.text`, `rulings.text`
- `type`: `cards.type`, `foreign_data.type`, `sets.type`
- `uuid`: `cards.uuid`, `foreign_data.uuid`, `legalities.uuid`, `rulings.uuid`
