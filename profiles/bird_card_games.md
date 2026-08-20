---
generator: db-snooper
version: 0.0.31
generated_at_utc: 2026-08-20T17:25:45.738563Z
dialect: sqlite
database: /var/folders/9j/b9bx_drd53sc6zbpsqyrjy4h0000gn/T/dbsnoop-if253x_v/card_games.sqlite
schema: main
---

## Relationships

- "cards"."uuid" ← "foreign_data"."uuid", "legalities"."uuid", "rulings"."uuid"
- "sets"."code" ← "set_translations"."setCode"

# "cards"  (rows=56822)

columns:
"id" int PK: unique identifier, 1..56832
"artist" text: 991 distinct, nulls=3
"asciiName" text: 26 distinct, nulls=56755
"availability" text: "mtgo,paper"=25459, "paper"=21531, "arena,mtgo,paper"=4609, "mtgo"=3697, "arena"=999, "arena,paper"=490, "arena,mtgo"=14, "shandalar"=12, "dreamcast"=10, nulls=1
"borderColor" text: "black"=49729, "white"=5017, "gold"=1244, "silver"=591, "borderless"=241
"cardKingdomFoilId" text: digits, all distinct, nulls=27910
"cardKingdomId" text: digits, all distinct, nulls=13622
"colorIdentity" text: 31 distinct, nulls=6224
"colorIndicator" text: "R"=41, "G"=36, "U"=34, "B"=29, "W"=14, "G,R"=7, "B,R,U"=3, "B,G"=2, "G,R,W"=1, nulls=56655
"colors" text: 39 distinct, nulls=12540
"convertedManaCost" float: 3=11776, 2=10760, 4=9174, 0=7327, 1=6223, 5=5674, 6=3431, 7=1515, 8=555, 9=203, 10=89, 11=34, 12=28, 15=14, 13=12, 16=3, 1e+06=2, 0.5=1, 14=1, 0..1e+06
"duelDeck" text: "a"=804, "b"=790, nulls=55228
"edhrecRank" int: 20660 distinct, nulls=4761, 1..20900, avg=8547.52, median=7731
"faceConvertedManaCost" float: 2=239, 3=189, 0=182, 4=132, 1=110, 5=50, 6=31, 7=22, nulls=55867, 0..7
"faceName" text: 607 distinct, nulls=55455
"flavorName" text: all distinct, nulls=56801
"flavorText" text: 17295 distinct, nulls=26020
"frameEffects" text: 36 distinct, nulls=53864
"frameVersion" text: "2015"=25500, "2003"=16462, "1997"=9257, "1993"=5510, "future"=93
"hand" text: "0"=45, "1"=29, "-1"=23, "-2"=8, "2"=7, "3"=4, "-3"=1, "-4"=1, nulls=56704
"hasAlternativeDeckLimit" int NOTNULL: redacted
"hasContentWarning" int NOTNULL: 0=56793, 1=29
"hasFoil" int NOTNULL: 1=34618, 0=22204
"hasNonFoil" int NOTNULL: 1=51413, 0=5409
"isAlternative" int NOTNULL: redacted
"isFullArt" int NOTNULL: 0=56336, 1=486
"isOnlineOnly" int NOTNULL: 0=52089, 1=4733
"isOversized" int NOTNULL: 0=56420, 1=402
"isPromo" int NOTNULL: 0=51234, 1=5588
"isReprint" int NOTNULL: 1=33657, 0=23165
"isReserved" int NOTNULL: 0=55489, 1=1333
"isStarter" int NOTNULL: 0=40865, 1=15957
"isStorySpotlight" int NOTNULL: 0=56718, 1=104
"isTextless" int NOTNULL: 0=56707, 1=115
"isTimeshifted" int NOTNULL: 0=56607, 1=215
"keywords" text: 1157 distinct, nulls=36183
"layout" text: "normal"=54906, "transform"=360, "modal_dfc"=322, "adventure"=228, "split"=221, "planar"=178, "aftermath"=146, "vanguard"=118, "saga"=92, "flip"=72, "scheme"=70, "leveler"=47, "host"=28, "meld"=18, "augment"=16
"leadershipSkills" text: "{'brawl': False, 'commander': True, 'oathbreaker': False}"=2660, "{'brawl': False, 'commander': False, 'oathbreaker': True}"=724, "{'brawl': True, 'commander': True, 'oathbreaker': False}"=255, "{'brawl': True, 'commander': False, 'oathbreaker': True}"=66, "{'brawl': False, 'commander': True, 'oathbreaker': True}"=45, nulls=53072
"life" text: numeric, 23 distinct, nulls=56704
"loyalty" text: "5"=265, "4"=253, "3"=205, "6"=42, "7"=42, "2"=12, "X"=5, "*"=2, "0"=2, "1d4+1"=1, "20"=1, nulls=55992
"manaCost" text: 696 distinct, nulls=7323
"mcmId" text: digits, 47971 distinct, nulls=8024
"mcmMetaId" text: digits, 20902 distinct, nulls=17906
"mtgArenaId" text: digits, 5654 distinct, nulls=50975
"mtgjsonV4Id" text: uuid, unique identifier
"mtgoFoilId" text: digits, 24242 distinct, nulls=32462
"mtgoId" text: digits, 31811 distinct, nulls=24684
"multiverseId" text: digits, 41871 distinct, nulls=14753
"name" text: 21738 distinct
"number" text: 6621 distinct
"originalReleaseDate" text: 383 distinct, nulls=54757
"originalText" text: 27607 distinct, nulls=15616
"originalType" text: 2992 distinct, nulls=14766
"otherFaceIds" text: 1361 distinct, nulls=55455
"power" text: 28 distinct, nulls=30624
"printings" text: 6231 distinct
"promoTypes" text: 64 distinct, nulls=50685
"purchaseUrls" text: all distinct, nulls=6371
"rarity" text: "common"=20745, "rare"=17626, "uncommon"=15251, "mythic"=3200
"scryfallId" text: uuid, 56144 distinct
"scryfallIllustrationId" text: uuid, 27250 distinct, nulls=2
"scryfallOracleId" text: uuid, 21769 distinct
"setCode" text: 536 distinct
"side" text: "a"=683, "b"=677, "c"=3, "d"=2, "e"=2, nulls=55455
"subtypes" text: 1505 distinct, nulls=22228
"supertypes" text: "Legendary"=4286, "Basic"=3269, "Snow"=142, "World"=47, "Basic,Snow"=35, "Host"=28, "Legendary,Snow"=21, "Ongoing"=12, nulls=48982
"tcgplayerProductId" text: digits, 49470 distinct, nulls=6600
"text" text: 20592 distinct, nulls=955
"toughness" text: 32 distinct, nulls=30624
"type" text: 2022 distinct
"types" text: 37 distinct
"uuid" text NOTNULL: uuid, unique identifier
"variations" text: 8256 distinct, nulls=48186
"watermark" text: 161 distinct, nulls=52373

indexes: none
fk: none

samples:
| column | latest | sample | sample |
|---|---|---|---|
| id | 56832 | 51666 | 45258 |
| artist | Colin Boyer | Rob Alexander | Raymond Swanland |
| asciiName | null | null | null |
| availability | mtgo,paper | mtgo,paper | paper |
| borderColor | black | black | black |
| cardKingdomFoilId | 238370 | 121558 | 214600 |
| cardKingdomId | 237883 | 121268 | null |
| colorIdentity | R,W | R | G |
| colorIndicator | null | null | null |
| colors | R,W | R | G |
| convertedManaCost | 3 | 10 | 2 |
| duelDeck | null | null | null |
| edhrecRank | 10632 | 6388 | 7803 |
| faceConvertedManaCost | null | null | null |
| faceName | null | null | null |
| flavorName | null | null | null |
| flavorText | From rebellion against the Akoum Skyclave to fighting the Eldrazi titans, the dragon-riding Kargan tribes have never missed an opportunity to defy the odds. | null | "No good will come from what you seek. Turn back now or suffer an ignoble death far from your home." |
| frameEffects | inverted | null | null |
| frameVersion | 2015 | 2003 | 2015 |
| hand | null | null | null |
| hasContentWarning | 0 | 0 | 0 |
| hasFoil | 1 | 1 | 1 |
| hasNonFoil | 1 | 1 | 0 |
| isFullArt | 0 | 0 | 0 |
| isOnlineOnly | 0 | 0 | 0 |
| isOversized | 0 | 0 | 0 |
| isPromo | 1 | 0 | 1 |
| isReprint | 0 | 0 | 1 |
| isReserved | 0 | 0 | 0 |
| isStarter | 1 | 0 | 1 |
| isStorySpotlight | 0 | 0 | 0 |
| isTextless | 0 | 0 | 0 |
| isTimeshifted | 0 | 0 | 0 |
| keywords | null | Suspend | null |
| layout | normal | normal | normal |
| leadershipSkills | null | null | null |
| life | null | null | null |
| loyalty | null | null | null |
| manaCost | {1}{R}{W} | {9}{R} | {1}{G} |
| mcmId | 501980 | 13861 | 302027 |
| mcmMetaId | 317195 | 8404 | null |
| mtgArenaId | null | null | null |
| mtgjsonV4Id | 28565911-47f4-53d3-9f0b-1b7360bd444c | 869aa858-e82b-5fa6-92cd-6239515334a2 | b7b0ce46-18cd-53aa-b8f6-bfe5c5f1b9fb |
| mtgoFoilId | null | 25582 | null |
| mtgoId | null | 25581 | null |
| multiverseId | null | 111048 | null |
| name | Kargan Warleader | Greater Gargadon | Deeproot Champion |
| number | 391 | 161 | 185s |
| originalReleaseDate | null | null | null |
| originalText | null | Suspend 10—{R} Sacrifice an artifact, creature, or land: Remove a time counter from Greater Gargadon. Play this ability only if Greater Gargadon is suspended. | null |
| originalType | null | Creature - Beast | null |
| otherFaceIds | null | null | null |
| power | 3 | 9 | 1 |
| printings | ZNR | MB1,MMA,TSP | PXLN,XLN |
| promoTypes | promopack | null | setpromo,prerelease,datestamped |
| purchaseUrls | {'cardKingdom': 'https://mtgjson.com/links/5e41d001e708490c', 'cardKingdomFoil': 'https://mtgjson.com/links/daf4f53f54b28b9e', 'cardmarket': 'https://mtgjson.com/links/5bf73e54801f56c0', 'tcgplayer': 'https://mtgjson.com/links/61bbe73992398cd8'} | {'cardKingdom': 'https://mtgjson.com/links/acf47e60161eb039', 'cardKingdomFoil': 'https://mtgjson.com/links/d8d56420a373287f', 'cardmarket': 'https://mtgjson.com/links/8b1be5a44878e32d', 'tcgplayer': 'https://mtgjson.com/links/5725d2f83b1a9078'} | {'cardKingdomFoil': 'https://mtgjson.com/links/e89a1e13f523705d', 'tcgplayer': 'https://mtgjson.com/links/19b961095042dc43'} |
| rarity | uncommon | rare | rare |
| scryfallId | cbef1409-4e7c-445e-ae6b-b3133faf1f73 | 653ddfa0-2088-4503-a3ab-b0f1d55d8351 | a3370921-9d06-429f-9553-0931416f0fc7 |
| scryfallIllustrationId | f7a16dfb-c794-4391-82ca-2e37ddf30ef2 | 54a888c0-e6ec-4c0a-8ec7-c50357d368b6 | f67e3fd3-c685-477a-9dd6-40ce1c5d1d68 |
| scryfallOracleId | 63324e72-e580-456a-91be-766c9f07b7b3 | 406b4b1d-756b-4062-897d-3693832086a0 | 507c2921-7070-482d-8754-dc667e3315bd |
| setCode | ZNR | TSP | PXLN |
| side | null | null | null |
| subtypes | Human,Warrior | Beast | Merfolk,Shaman |
| supertypes | null | null | null |
| tcgplayerProductId | 222853 | 14251 | 146068 |
| text | Other Warriors you control get +1/+1. | Suspend 10—{R} Sacrifice an artifact, creature, or land: Remove a time counter from Greater Gargadon. Activate this ability only if Greater Gargadon is suspended. | Whenever you cast a noncreature spell, put a +1/+1 counter on Deeproot Champion. |
| toughness | 3 | 7 | 1 |
| type | Creature — Human Warrior | Creature — Beast | Creature — Merfolk Shaman |
| types | Creature | Creature | Creature |
| uuid | 46407d93-df48-5161-95fe-f24086746663 | 545dcd44-2511-5e0a-b499-87bed1688545 | 6889685e-1f11-5fb4-8584-eab3ff541c5d |
| variations | f3434acf-7796-572c-a889-487c84cf7948 | null | 106f4ebb-0f46-56ef-905d-0ba3346d3183,d25e957f-bc27-5054-963b-7caf8a6fe991 |
| watermark | planeswalker | null | null |

# "foreign_data"  (rows=≈229186)

columns:
"id" int PK
"flavorText" text
"language" text
"multiverseid" int
"name" text
"text" text
"type" text
"uuid" text FK

indexes: none
fk: "uuid"→"cards"."uuid"


# "legalities"  (rows=≈427907)

columns:
"id" int PK
"format" text
"status" text
"uuid" text FK

indexes: none
fk: "uuid"→"cards"."uuid"


# "rulings"  (rows=87769)

columns:
"id" int PK: unique identifier, 1..87769
"date" date: 109 distinct
"text" text: 19593 distinct
"uuid" text FK: uuid, 26141 distinct

indexes: none
fk: "uuid"→"cards"."uuid"

samples:
| column | latest | sample | sample |
|---|---|---|---|
| id | 87769 | 54188 | 55814 |
| date | 2013-09-15 | 2017-02-09 | 2009-10-01 |
| text | Mana symbols in the text boxes of permanents you control don’t count toward your devotion to any color. | Energy counters aren’t mana. They don’t go away as steps, phases, and turns end, and effects that add mana “of any type” to your mana pool can’t give you energy counters. | All Hallow’s Eve’s triggered ability functions from the exile zone. This ability has an “intervening ‘if’ clause.” It won’t trigger at all unless All Hallow’s Eve is exiled and has a scream counter on it (which can happen only if it resolves as a spell). |
| uuid | 43a82ca6-338d-5ef9-ae82-1ed44ebb6c0a | ecff3dec-1ea5-511d-9fb3-d5cc5c81ae46 | 70caad59-1395-50e6-93b9-c5d629518ae3 |

# "set_translations"  (rows=1210)

columns:
"id" int PK: unique identifier, 1..1210
"language" text: "Chinese Simplified"=121, "Chinese Traditional"=121, "French"=121, "German"=121, "Italian"=121, "Japanese"=121, "Korean"=121, "Portuguese (Brazil)"=121, "Russian"=121, "Spanish"=121
"setCode" text FK: 121 distinct
"translation" text: 504 distinct, nulls=231

indexes: none
fk: "setCode"→"sets"."code"

samples:
| column | latest | sample | sample |
|---|---|---|---|
| id | 1210 | 589 | 858 |
| language | Spanish | Russian | Portuguese (Brazil) |
| setCode | WTH | EVE | OGW |
| translation | null | Сумерки | Juramento das Sentinelas |

# "sets"  (rows=551)

columns:
"id" int PK: unique identifier, 1..551
"baseSetSize" int: 166 distinct, 0..1694, avg=99.5572, median=26
"block" text: 33 distinct, nulls=279
"booster" text: 85 distinct, nulls=413
"code" text NOTNULL: all distinct
"isFoilOnly" int NOTNULL: 0=384, 1=167
"isForeignOnly" int NOTNULL: 0=535, 1=16
"isNonFoilOnly" int NOTNULL: 0=445, 1=106
"isOnlineOnly" int NOTNULL: 0=525, 1=26
"isPartialPreview" int NOTNULL: 0=550, 1=1
"keyruneCode" text: 249 distinct
"mcmId" int: all distinct, nulls=350, 4..3660, avg=1123.39, median=1388
"mcmIdExtras" int: 2371=1, 2419=1, 2451=1, 2587=1, 2961=1, 3113=1, 3209=1, 3459=1, 3474=1, 3680=1, nulls=541, 2371..3680
"mcmName" text: all distinct, nulls=350
"mtgoCode" text: all distinct, nulls=391
"name" text: all distinct
"parentCode" text: 117 distinct, nulls=397
"releaseDate" date: 342 distinct
"tcgplayerGroupId" int: 238 distinct, nulls=291, 1..2778, avg=955.735, median=123
"totalSetSize" int: 181 distinct, 0..1694, avg=102.61, median=26
"type" text: 20 distinct

indexes: none
fk: none

samples:
| column | latest | sample | sample |
|---|---|---|---|
| id | 551 | 71 | 120 |
| baseSetSize | 285 | 80 | 12 |
| block | null | null | Friday Night Magic |
| booster | {'arena': {'boosters': [{'contents': {'common': 10, 'rareMythic': 1, 'uncommon': 3}, 'weight': 1}], 'boostersTotalWeight': 1, 'name': 'Zendikar Rising Arena Booster', 'sheets': {'common': {'balanceColors': True, 'cards': {'01d1ef65-cbcd-5b28-85c8-0edeca7e | null | null |
| code | ZNR | DDH | F16 |
| isFoilOnly | 0 | 0 | 1 |
| isForeignOnly | 0 | 0 | 0 |
| isNonFoilOnly | 0 | 0 | 0 |
| isOnlineOnly | 0 | 0 | 0 |
| isPartialPreview | 0 | 0 | 0 |
| keyruneCode | ZNR | DDH | PMEI |
| mcmId | 3404 | 1288 | null |
| mcmIdExtras | 3474 | null | null |
| mcmName | Zendikar Rising | Duel Decks: Ajani vs. Nicol Bolas | null |
| mtgoCode | ZNR | DDH | null |
| name | Zendikar Rising | Duel Decks: Ajani vs. Nicol Bolas | Friday Night Magic 2016 |
| parentCode | null | null | null |
| releaseDate | 2020-09-25 | 2011-09-02 | 2016-01-01 |
| tcgplayerGroupId | 2648 | 30 | null |
| totalSetSize | 392 | 80 | 12 |
| type | expansion | duel_deck | promo |
