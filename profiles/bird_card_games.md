---
generator: db-snooper
version: 0.0.26
generated_at_utc: 2026-08-16T07:18:33.370065Z
dialect: sqlite
database: /Users/renatyuldashev/Documents/ai-sql/custom-bench/data/bird_mini_dev/databases/dev_databases/card_games/card_games.sqlite
schema: main
---

## Relationships

- cards.uuid ← foreign_data.uuid, legalities.uuid, rulings.uuid
- sets.code ← set_translations.setCode

# cards

```sql
CREATE TABLE "cards"
(
    id                      INTEGER           not null
        primary key autoincrement,
    artist                  TEXT,
    asciiName               TEXT,
    availability            TEXT,
    borderColor             TEXT,
    cardKingdomFoilId       TEXT,
    cardKingdomId           TEXT,
    colorIdentity           TEXT,
    colorIndicator          TEXT,
    colors                  TEXT,
    convertedManaCost       REAL,
    duelDeck                TEXT,
    edhrecRank              INTEGER,
    faceConvertedManaCost   REAL,
    faceName                TEXT,
    flavorName              TEXT,
    flavorText              TEXT,
    frameEffects            TEXT,
    frameVersion            TEXT,
    hand                    TEXT,
    hasAlternativeDeckLimit INTEGER default 0 not null,
    hasContentWarning       INTEGER default 0 not null,
    hasFoil                 INTEGER default 0 not null,
    hasNonFoil              INTEGER default 0 not null,
    isAlternative           INTEGER default 0 not null,
    isFullArt               INTEGER default 0 not null,
    isOnlineOnly            INTEGER default 0 not null,
    isOversized             INTEGER default 0 not null,
    isPromo                 INTEGER default 0 not null,
    isReprint               INTEGER default 0 not null,
    isReserved              INTEGER default 0 not null,
    isStarter               INTEGER default 0 not null,
    isStorySpotlight        INTEGER default 0 not null,
    isTextless              INTEGER default 0 not null,
    isTimeshifted           INTEGER default 0 not null,
    keywords                TEXT,
    layout                  TEXT,
    leadershipSkills        TEXT,
    life                    TEXT,
    loyalty                 TEXT,
    manaCost                TEXT,
    mcmId                   TEXT,
    mcmMetaId               TEXT,
    mtgArenaId              TEXT,
    mtgjsonV4Id             TEXT,
    mtgoFoilId              TEXT,
    mtgoId                  TEXT,
    multiverseId            TEXT,
    name                    TEXT,
    number                  TEXT,
    originalReleaseDate     TEXT,
    originalText            TEXT,
    originalType            TEXT,
    otherFaceIds            TEXT,
    power                   TEXT,
    printings               TEXT,
    promoTypes              TEXT,
    purchaseUrls            TEXT,
    rarity                  TEXT,
    scryfallId              TEXT,
    scryfallIllustrationId  TEXT,
    scryfallOracleId        TEXT,
    setCode                 TEXT,
    side                    TEXT,
    subtypes                TEXT,
    supertypes              TEXT,
    tcgplayerProductId      TEXT,
    text                    TEXT,
    toughness               TEXT,
    type                    TEXT,
    types                   TEXT,
    uuid                    TEXT              not null
        unique,
    variations              TEXT,
    watermark               TEXT
);
```

## Rows

- total=56822

| column | latest | sample | sample |
|---|---|---|---|
| id | 56832 | 12740 | 38516 |
| artist | Colin Boyer | Terese Nielsen | Grzegorz Rutkowski |
| asciiName | null | null | null |
| availability | mtgo,paper | mtgo,paper | paper |
| borderColor | black | black | black |
| cardKingdomFoilId | 238370 | null | 218413 |
| cardKingdomId | 237883 | 184779 | null |
| colorIdentity | R,W | G | B,W |
| colorIndicator | null | null | null |
| colors | R,W | G | B,W |
| convertedManaCost | 3 | 3 | 4 |
| duelDeck | null | null | null |
| edhrecRank | 10632 | 37 | 3402 |
| faceConvertedManaCost | null | null | null |
| faceName | null | null | null |
| flavorName | null | null | null |
| flavorText | From rebellion against the Akoum Skyclave to fighting the Eldrazi titans, the dragon-riding Kargan tribes have never missed an opportunity to defy the odds. | She remembers every word spoken, from the hero's oath to the baby's cry. | null |
| frameEffects | inverted | null | legendary |
| frameVersion | 2015 | 2003 | 2015 |
| hand | null | null | null |
| hasAlternativeDeckLimit | [REDACTED] | [REDACTED] | [REDACTED] |
| hasContentWarning | 0 | 0 | 0 |
| hasFoil | 1 | 0 | 1 |
| hasNonFoil | 1 | 1 | 0 |
| isAlternative | [REDACTED] | [REDACTED] | [REDACTED] |
| isFullArt | 0 | 0 | 0 |
| isOnlineOnly | 0 | 0 | 0 |
| isOversized | 0 | 0 | 0 |
| isPromo | 1 | 0 | 1 |
| isReprint | 0 | 1 | 1 |
| isReserved | 0 | 0 | 0 |
| isStarter | 1 | 1 | 1 |
| isStorySpotlight | 0 | 0 | 0 |
| isTextless | 0 | 0 | 0 |
| isTimeshifted | 0 | 0 | 0 |
| keywords | null | null | Vigilance |
| layout | normal | normal | normal |
| leadershipSkills | null | null | {'brawl': False, 'commander': True, 'oathbreaker': False} |
| life | null | null | null |
| loyalty | null | null | null |
| manaCost | {1}{R}{W} | {1}{G}{G} | {2}{W}{B} |
| mcmId | 501980 | 247215 | 355718 |
| mcmMetaId | 317195 | null | null |
| mtgArenaId | null | null | null |
| mtgjsonV4Id | 28565911-47f4-53d3-9f0b-1b7360bd444c | 9766d0eb-cbaf-5da6-b8c4-53e3aa970ed2 | c1ecb04b-e52a-5f1d-99c9-b7ba660289dc |
| mtgoFoilId | null | 41026 | null |
| mtgoId | null | 40706 | null |
| multiverseId | null | 247148 | null |
| name | Kargan Warleader | Eternal Witness | Aryel, Knight of Windgrace |
| number | 391 | 152 | 192s |
| originalReleaseDate | null | null | null |
| originalText | null | When Eternal Witness enters the battlefield, you may return target card from your graveyard to your hand. | null |
| originalType | null | Creature — Human Shaman | null |
| otherFaceIds | null | null | null |
| power | 3 | 2 | 4 |
| printings | ZNR | 5DN,C15,CM2,CMA,CMD,CMR,DDJ,F08,MB1,MMA,PLIST,PRM,PUMA,PZ1,SLD,TD0,UMA,WC04 | DOM,PDOM |
| promoTypes | promopack | null | setpromo,prerelease,datestamped |
| purchaseUrls | {'cardKingdom': 'https://mtgjson.com/links/5e41d001e708490c', 'cardKingdomFoil': 'https://mtgjson.com/links/daf4f53f54b28b9e', 'cardmarket': 'https://mtgjson.com/links/5bf73e54801f56c0', 'tcgplayer': 'https://mtgjson.com/links/61bbe73992398cd8'} | {'cardKingdom': 'https://mtgjson.com/links/827d00d78c36e6a9', 'tcgplayer': 'https://mtgjson.com/links/0e4262aa55a33480'} | {'cardKingdomFoil': 'https://mtgjson.com/links/76e42638f1cc239a', 'tcgplayer': 'https://mtgjson.com/links/aec44895b1d132ba'} |
| rarity | uncommon | uncommon | rare |
| scryfallId | cbef1409-4e7c-445e-ae6b-b3133faf1f73 | 101cccfb-17c3-4b11-8a3e-c382ec7143c3 | eec96d0e-f2b4-47f2-ada0-873ff33bcce4 |
| scryfallIllustrationId | f7a16dfb-c794-4391-82ca-2e37ddf30ef2 | 9ee21d9a-a2db-41ef-b1b3-87d2c047a5b4 | 56c432bd-c4ee-43a1-9920-17ea3d18e38a |
| scryfallOracleId | 63324e72-e580-456a-91be-766c9f07b7b3 | 30b24e8e-3b0e-4d8e-90f3-f66eb7c1858c | 9956f9b7-0140-484c-b606-3685690b84cc |
| setCode | ZNR | CMD | PDOM |
| side | null | null | null |
| subtypes | Human,Warrior | Human,Shaman | Human,Knight |
| supertypes | null | null | Legendary |
| tcgplayerProductId | 222853 | 47489 | 165534 |
| text | Other Warriors you control get +1/+1. | When Eternal Witness enters the battlefield, you may return target card from your graveyard to your hand. | Vigilance {2}{W}, {T}: Create a 2/2 white Knight creature token with vigilance. {B}, {T}, Tap X untapped Knights you control: Destroy target creature with power X or less. |
| toughness | 3 | 1 | 4 |
| type | Creature — Human Warrior | Creature — Human Shaman | Legendary Creature — Human Knight |
| types | Creature | Creature | Creature |
| uuid | 46407d93-df48-5161-95fe-f24086746663 | bce48b88-674e-5bb1-b8ee-70ee3182fb59 | 4f50d67e-5472-53f0-8308-84f17f194190 |
| variations | f3434acf-7796-572c-a889-487c84cf7948 | null | null |
| watermark | planeswalker | null | null |

## Columns

- id: unique identifier, int 1..56832
- artist: 991 distinct, nulls=3
- asciiName: 26 distinct, nulls=56755
- availability: "mtgo,paper"=25459, "paper"=21531, "arena,mtgo,paper"=4609, "mtgo"=3697, "arena"=999, "arena,paper"=490, "arena,mtgo"=14, "shandalar"=12, "dreamcast"=10, nulls=1
- borderColor: "black"=49729, "white"=5017, "gold"=1244, "silver"=591, "borderless"=241
- cardKingdomFoilId: all distinct, nulls=27910
- cardKingdomId: all distinct, nulls=13622
- colorIdentity: 31 distinct, nulls=6224
- colorIndicator: "R"=41, "G"=36, "U"=34, "B"=29, "W"=14, "G,R"=7, "B,R,U"=3, "B,G"=2, "G,R,W"=1, nulls=56655
- colors: 39 distinct, nulls=12540
- convertedManaCost: 3=11776, 2=10760, 4=9174, 0=7327, 1=6223, 5=5674, 6=3431, 7=1515, 8=555, 9=203, 10=89, 11=34, 12=28, 15=14, 13=12, 16=3, 1e+06=2, 0.5=1, 14=1, num 0..1e+06
- duelDeck: "a"=804, "b"=790, nulls=55228
- edhrecRank: 20660 distinct, nulls=4761, int 1..20900
  - stats: average=8547.52, median=7731
- faceConvertedManaCost: 2=239, 3=189, 0=182, 4=132, 1=110, 5=50, 6=31, 7=22, nulls=55867, num 0..7
- faceName: 607 distinct, nulls=55455
- flavorName: all distinct, nulls=56801
- flavorText: 17295 distinct, nulls=26020
- frameEffects: 36 distinct, nulls=53864
- frameVersion: "2015"=25500, "2003"=16462, "1997"=9257, "1993"=5510, "future"=93
- hand: "0"=45, "1"=29, "-1"=23, "-2"=8, "2"=7, "3"=4, "-3"=1, "-4"=1, nulls=56704
- hasAlternativeDeckLimit: 2 distinct, int 0..1
  - stats: average=0.000211186, median=0
- hasContentWarning: 0=56793, 1=29
- hasFoil: 1=34618, 0=22204
- hasNonFoil: 1=51413, 0=5409
- isAlternative: 2 distinct, int 0..1
  - stats: average=0.00506846, median=0
- isFullArt: 0=56336, 1=486
- isOnlineOnly: 0=52089, 1=4733
- isOversized: 0=56420, 1=402
- isPromo: 0=51234, 1=5588
- isReprint: 1=33657, 0=23165
- isReserved: 0=55489, 1=1333
- isStarter: 0=40865, 1=15957
- isStorySpotlight: 0=56718, 1=104
- isTextless: 0=56707, 1=115
- isTimeshifted: 0=56607, 1=215
- keywords: 1157 distinct, nulls=36183
- layout: "normal"=54906, "transform"=360, "modal_dfc"=322, "adventure"=228, "split"=221, "planar"=178, "aftermath"=146, "vanguard"=118, "saga"=92, "flip"=72, "scheme"=70, "leveler"=47, "host"=28, "meld"=18, "augment"=16
- leadershipSkills: "{'brawl': False, 'commander': True, 'oathbreaker': False}"=2660, "{'brawl': False, 'commander': False, 'oathbreaker': True}"=724, "{'brawl': True, 'commander': True, 'oathbreaker': False}"=255, "{'brawl': True, 'commander': False, 'oathbreaker': True}"=66, "{'brawl': False, 'commander': True, 'oathbreaker': True}"=45, nulls=53072
- life: 23 distinct, nulls=56704
- loyalty: "5"=265, "4"=253, "3"=205, "6"=42, "7"=42, "2"=12, "X"=5, "*"=2, "0"=2, "1d4+1"=1, "20"=1, nulls=55992
- manaCost: 696 distinct, nulls=7323
- mcmId: 47971 distinct, nulls=8024
- mcmMetaId: 20902 distinct, nulls=17906
- mtgArenaId: 5654 distinct, nulls=50975
- mtgjsonV4Id: unique identifier
- mtgoFoilId: 24242 distinct, nulls=32462
- mtgoId: 31811 distinct, nulls=24684
- multiverseId: 41871 distinct, nulls=14753
- name: 21738 distinct
- number: 6621 distinct
- originalReleaseDate: 383 distinct, nulls=54757
- originalText: 27607 distinct, nulls=15616
- originalType: 2992 distinct, nulls=14766
- otherFaceIds: 1361 distinct, nulls=55455
- power: 28 distinct, nulls=30624
- printings: 6231 distinct
- promoTypes: 64 distinct, nulls=50685
- purchaseUrls: all distinct, nulls=6371
- rarity: "common"=20745, "rare"=17626, "uncommon"=15251, "mythic"=3200
- scryfallId: 56144 distinct
- scryfallIllustrationId: 27250 distinct, nulls=2
- scryfallOracleId: 21769 distinct
- setCode: 536 distinct
- side: "a"=683, "b"=677, "c"=3, "d"=2, "e"=2, nulls=55455
- subtypes: 1505 distinct, nulls=22228
- supertypes: "Legendary"=4286, "Basic"=3269, "Snow"=142, "World"=47, "Basic,Snow"=35, "Host"=28, "Legendary,Snow"=21, "Ongoing"=12, nulls=48982
- tcgplayerProductId: 49470 distinct, nulls=6600
- text: 20592 distinct, nulls=955
- toughness: 32 distinct, nulls=30624
- type: 2022 distinct
- types: 37 distinct
- uuid: unique identifier
- variations: 8256 distinct, nulls=48186
- watermark: 161 distinct, nulls=52373


# foreign_data

```sql
CREATE TABLE "foreign_data"
(
    id           INTEGER not null
        primary key autoincrement,
    flavorText   TEXT,
    language     TEXT,
    multiverseid INTEGER,
    name         TEXT,
    text         TEXT,
    type         TEXT,
    uuid         TEXT
        references cards (uuid)
);
```

## Rows

- total=229186

| column | latest | sample | sample |
|---|---|---|---|
| id | 229205 | 136887 | 154625 |
| flavorText |  | "Despedaçar a mente alheia é condenar a um destino pior que a morte. É um poder aterrorizante." — Jace Beleren | 「我不治病。 治病代表了已经有痛苦； 而为了停止苦难，必须同时对抗世界上所有的创伤。」 |
| language | Chinese Traditional | Portuguese (Brazil) | Chinese Simplified |
| multiverseid | 495152 | 449171 | 164108 |
| name | 樹林 | Corrosão Psíquica | 战局炼金术士 |
| text |  | Toda vez que você compra um card, cada oponente coloca os dois cards do topo do próprio grimório no próprio cemitério. | 如果某来源将对任一牌手造成伤害，则你可以防止其中的X点伤害，X为由你操控的僧侣数量。 |
| type | 基本地 ～樹林 | Encantamento | 生物～洁英／僧侣 |
| uuid | 2f8a3f3d-3b11-5f26-b766-0b0bbda0a5bb | 4f4e5d1d-73ea-5fe0-9aa1-a0e5490dd7ac | cd9faa11-55aa-572a-a589-13e2a23a628d |

## Columns

- id: unique identifier, int 1..229205
- flavorText: profile metrics skipped
- language: profile metrics skipped
- multiverseid: nulls=38418, int 73246..507640
  - stats: average=336048
- name: profile metrics skipped
- text: profile metrics skipped
- type: profile metrics skipped
- uuid: profile metrics skipped


# legalities

```sql
CREATE TABLE "legalities"
(
    id     INTEGER not null
        primary key autoincrement,
    format TEXT,
    status TEXT,
    uuid   TEXT
        references cards (uuid)
            on update cascade on delete cascade
);
```

## Rows

- total=427907

| column | latest | sample | sample |
|---|---|---|---|
| id | 427907 | 391870 | 261924 |
| format | vintage | pioneer | duel |
| status | Legal | Legal | Legal |
| uuid | 46407d93-df48-5161-95fe-f24086746663 | e68fdf69-2f0d-5369-8f3b-3fce3995168b | c93b2785-10c8-54a8-8729-0e903269b0a1 |

## Columns

- id: unique identifier, int 1..427907
- format: profile metrics skipped
- status: profile metrics skipped
- uuid: profile metrics skipped


# rulings

```sql
CREATE TABLE "rulings"
(
    id   INTEGER not null
        primary key autoincrement,
    date DATE,
    text TEXT,
    uuid TEXT
        references cards (uuid)
            on update cascade on delete cascade
);
```

## Rows

- total=87769

| column | latest | sample | sample |
|---|---|---|---|
| id | 87769 | 39355 | 31500 |
| date | 2013-09-15 | 2013-09-15 | 2016-07-13 |
| text | Mana symbols in the text boxes of permanents you control don’t count toward your devotion to any color. | When you scry, you may put all the cards you look at back on top of your library, you may put all of those cards on the bottom of your library, or you may put some of those cards on top and the rest of them on the bottom. | The converted mana cost of a creature spell with emerge isn’t affected by whether its emerge cost is paid. For example, if you cast Elder Deep-Fiend for its emerge cost and sacrifice a creature whose converted mana cost is 3, Elder Deep-Fiend’s converted  |
| uuid | 43a82ca6-338d-5ef9-ae82-1ed44ebb6c0a | e93e81d3-440e-5f4f-aaed-979dfdc81dbd | a8fd720a-678a-549c-932e-a8d6398bf5e6 |

## Columns

- id: unique identifier, int 1..87769
- date: 109 distinct
- text: 19593 distinct
- uuid: 26141 distinct


# set_translations

```sql
CREATE TABLE "set_translations"
(
    id          INTEGER not null
        primary key autoincrement,
    language    TEXT,
    setCode     TEXT
        references sets (code)
            on update cascade on delete cascade,
    translation TEXT
);
```

## Rows

- total=1210

| column | latest | sample | sample |
|---|---|---|---|
| id | 1210 | 1174 | 47 |
| language | Spanish | German | Korean |
| setCode | WTH | V15 | 6ED |
| translation | null | From the Vault: Angels | null |

## Columns

- id: unique identifier, int 1..1210
- language: "Chinese Simplified"=121, "Chinese Traditional"=121, "French"=121, "German"=121, "Italian"=121, "Japanese"=121, "Korean"=121, "Portuguese (Brazil)"=121, "Russian"=121, "Spanish"=121
- setCode: 121 distinct
- translation: 504 distinct, nulls=231


# sets

```sql
CREATE TABLE "sets"
(
    id               INTEGER           not null
        primary key autoincrement,
    baseSetSize      INTEGER,
    block            TEXT,
    booster          TEXT,
    code             TEXT              not null
        unique,
    isFoilOnly       INTEGER default 0 not null,
    isForeignOnly    INTEGER default 0 not null,
    isNonFoilOnly    INTEGER default 0 not null,
    isOnlineOnly     INTEGER default 0 not null,
    isPartialPreview INTEGER default 0 not null,
    keyruneCode      TEXT,
    mcmId            INTEGER,
    mcmIdExtras      INTEGER,
    mcmName          TEXT,
    mtgoCode         TEXT,
    name             TEXT,
    parentCode       TEXT,
    releaseDate      DATE,
    tcgplayerGroupId INTEGER,
    totalSetSize     INTEGER,
    type             TEXT
);
```

## Rows

- total=551

| column | latest | sample | sample |
|---|---|---|---|
| id | 551 | 154 | 183 |
| baseSetSize | 285 | 41 | 495 |
| block | null | null | null |
| booster | {'arena': {'boosters': [{'contents': {'common': 10, 'rareMythic': 1, 'uncommon': 3}, 'weight': 1}], 'boostersTotalWeight': 1, 'name': 'Zendikar Rising Arena Booster', 'sheets': {'common': {'balanceColors': True, 'cards': {'01d1ef65-cbcd-5b28-85c8-0edeca7e | null | null |
| code | ZNR | H09 | JMP |
| isFoilOnly | 0 | 1 | 0 |
| isForeignOnly | 0 | 0 | 0 |
| isNonFoilOnly | 0 | 0 | 0 |
| isOnlineOnly | 0 | 0 | 0 |
| isPartialPreview | 0 | 0 | 0 |
| keyruneCode | ZNR | H09 | JMP |
| mcmId | 3404 | 116 | 3053 |
| mcmIdExtras | 3474 | null | null |
| mcmName | Zendikar Rising | Premium Deck Series: Slivers | Jumpstart |
| mtgoCode | ZNR | H09 | null |
| name | Zendikar Rising | Premium Deck Series: Slivers | Jumpstart |
| parentCode | null | null | null |
| releaseDate | 2020-09-25 | 2009-11-20 | 2020-07-17 |
| tcgplayerGroupId | 2648 | 91 | 2654 |
| totalSetSize | 392 | 41 | 496 |
| type | expansion | premium_deck | draft_innovation |

## Columns

- id: unique identifier, int 1..551
- baseSetSize: 166 distinct, int 0..1694
  - stats: average=99.5572, median=26
- block: 33 distinct, nulls=279
- booster: 85 distinct, nulls=413
- code: all distinct
- isFoilOnly: 0=384, 1=167
- isForeignOnly: 0=535, 1=16
- isNonFoilOnly: 0=445, 1=106
- isOnlineOnly: 0=525, 1=26
- isPartialPreview: 0=550, 1=1
- keyruneCode: 249 distinct
- mcmId: all distinct, nulls=350, int 4..3660
  - stats: average=1123.39, median=1388
- mcmIdExtras: 2371=1, 2419=1, 2451=1, 2587=1, 2961=1, 3113=1, 3209=1, 3459=1, 3474=1, 3680=1, nulls=541, int 2371..3680
- mcmName: all distinct, nulls=350
- mtgoCode: all distinct, nulls=391
- name: all distinct
- parentCode: 117 distinct, nulls=397
- releaseDate: 342 distinct
- tcgplayerGroupId: 238 distinct, nulls=291, int 1..2778
  - stats: average=955.735, median=123
- totalSetSize: 181 distinct, int 0..1694
  - stats: average=102.61, median=26
- type: 20 distinct
