---
generator: db-snooper
version: 0.0.34
generated_at_utc: 2026-08-24T21:55:18.789126Z
dialect: sqlite
database: /var/folders/9j/b9bx_drd53sc6zbpsqyrjy4h0000gn/T/dbsnoop-voi1gump/card_games.sqlite
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

samples:
| column | latest | sample | sample |
|---|---|---|---|
| id | 56832 | 39668 | 1205 |
| artist | Colin Boyer | Chris Rahn | Sandra Everingham |
| asciiName | null | null | null |
| availability | mtgo,paper | paper | paper |
| borderColor | black | black | white |
| cardKingdomFoilId | 238370 | 209375 | null |
| cardKingdomId | 237883 | null | 26035 |
| colorIdentity | R,W | G | W |
| colorIndicator | null | null | null |
| colors | R,W | G | W |
| convertedManaCost | 3 | 4 | 2 |
| duelDeck | null | null | null |
| edhrecRank | 10632 | 7470 | 11514 |
| faceConvertedManaCost | null | null | null |
| faceName | null | null | null |
| flavorName | null | null | null |
| flavorText | From rebellion against the Akoum Skyclave to fighting the Eldrazi titans, the dragon-riding Kargan tribes have never missed an opportunity to defy the odds. | null | null |
| frameEffects | inverted | null | null |
| frameVersion | 2015 | 2015 | 1993 |
| hand | null | null | null |
| hasContentWarning | 0 | 0 | 0 |
| hasFoil | 1 | 1 | 0 |
| hasNonFoil | 1 | 0 | 1 |
| isFullArt | 0 | 0 | 0 |
| isOnlineOnly | 0 | 0 | 0 |
| isOversized | 0 | 0 | 0 |
| isPromo | 1 | 1 | 0 |
| isReprint | 0 | 1 | 1 |
| isReserved | 0 | 0 | 0 |
| isStarter | 1 | 1 | 0 |
| isStorySpotlight | 0 | 0 | 0 |
| isTextless | 0 | 0 | 0 |
| isTimeshifted | 0 | 0 | 0 |
| keywords | null | null | null |
| layout | normal | normal | normal |
| leadershipSkills | null | null | null |
| life | null | null | null |
| loyalty | null | null | null |
| manaCost | {1}{R}{W} | {2}{G}{G} | {1}{W} |
| mcmId | 501980 | 292943 | 5723 |
| mcmMetaId | 317195 | null | null |
| mtgArenaId | null | null | null |
| mtgjsonV4Id | 28565911-47f4-53d3-9f0b-1b7360bd444c | 559ecfa7-9e38-5f3e-96b3-02ca3814ff73 | 28262cc3-56c1-597c-ac52-9e6b6b88c8ab |
| mtgoFoilId | null | null | null |
| mtgoId | null | null | null |
| multiverseId | null | null | 1337 |
| name | Kargan Warleader | Bristling Hydra | Circle of Protection: Green |
| number | 391 | 147s | 11 |
| originalReleaseDate | null | null | null |
| originalText | null | null | o1: Prevents all damage against you from one green source. If a source does damage to you more than once in a turn, you must pay 1 mana each time you want to prevent the damage. |
| originalType | null | null | Enchantment |
| otherFaceIds | null | null | null |
| power | 3 | 4 | null |
| printings | ZNR | KLD,KLR,PKLD,PRES | 2ED,3ED,4BB,4ED,5ED,6ED,7ED,8ED,CED,CEI,FBB,ICE,LEA,LEB,PTC,SUM,TMP |
| promoTypes | promopack | setpromo,prerelease,datestamped | null |
| purchaseUrls | {'cardKingdom': 'https://mtgjson.com/links/5e41d001e708490c', 'cardKingdomFoil': 'https://mtgjson.com/links/daf4f53f54b28b9e', 'cardmarket': 'https://mtgjson.com/links/5bf73e54801f56c0', 'tcgplayer':… | {'cardKingdomFoil': 'https://mtgjson.com/links/d63136a173067627', 'tcgplayer': 'https://mtgjson.com/links/c28ec0e0583f07ff'} | {'cardKingdom': 'https://mtgjson.com/links/067cbbfb8116f9ce', 'tcgplayer': 'https://mtgjson.com/links/1f3d54be7f98c978'} |
| rarity | uncommon | rare | common |
| scryfallId | cbef1409-4e7c-445e-ae6b-b3133faf1f73 | 095ac316-dd28-4e2d-83f9-6e2d05a499a6 | 251e0407-b49a-4ee5-83a1-1523ff03a7a7 |
| scryfallIllustrationId | f7a16dfb-c794-4391-82ca-2e37ddf30ef2 | 1706c503-8a79-4846-90c9-5ae1fe36fd42 | 3826a644-d46a-4800-ae87-382b809a284b |
| scryfallOracleId | 63324e72-e580-456a-91be-766c9f07b7b3 | b3b23c58-0b7a-4fe4-a8e8-5320a7605724 | 41b0f347-1398-4778-bf3f-4007d8a77162 |
| setCode | ZNR | PKLD | 3ED |
| side | null | null | null |
| subtypes | Human,Warrior | Hydra | null |
| supertypes | null | null | null |
| tcgplayerProductId | 222853 | 123352 | 1362 |
| text | Other Warriors you control get +1/+1. | When Bristling Hydra enters the battlefield, you get {E}{E}{E} (three energy counters). Pay {E}{E}{E}: Put a +1/+1 counter on Bristling Hydra. It gains hexproof until end of turn. | {1}: The next time a green source of your choice would deal damage to you this turn, prevent that damage. |
| toughness | 3 | 3 | null |
| type | Creature — Human Warrior | Creature — Hydra | Enchantment |
| types | Creature | Creature | Enchantment |
| uuid | 46407d93-df48-5161-95fe-f24086746663 | 8ae68f83-585e-5ce9-9db6-366786f0ee8a | 43ef269c-93d4-5a0f-89d4-3d0e8a34e0b1 |
| variations | f3434acf-7796-572c-a889-487c84cf7948 | null | null |
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


# "legalities"  (rows=≈427907)

columns:
"id" int PK
"format" text
"status" text
"uuid" text FK

indexes: none


# "rulings"  (rows=87769)

columns:
"id" int PK: unique identifier, 1..87769
"date" date: 109 distinct
"text" text: 19593 distinct
"uuid" text FK: uuid, 26141 distinct

indexes: none

samples:
| column | latest | sample | sample |
|---|---|---|---|
| id | 87769 | 63397 | 71691 |
| date | 2013-09-15 | 2015-08-25 | 2013-07-01 |
| text | Mana symbols in the text boxes of permanents you control don’t count toward your devotion to any color. | Eldrazi and Scion are each separate creature types. Anything that affects Eldrazi will affect these tokens, for example. | Auras attached to the exiled creature will be put into their owners’ graveyards. Equipment attached to the exiled creature will become unattached and remain on the battlefield. Any counters on the ex… |
| uuid | 43a82ca6-338d-5ef9-ae82-1ed44ebb6c0a | 78361f75-8f21-58fd-9968-7f12de34c277 | 923f67c6-b478-5f00-a349-1a9b0e789f7d |

# "set_translations"  (rows=1210)

columns:
"id" int PK: unique identifier, 1..1210
"language" text: "Chinese Simplified"=121, "Chinese Traditional"=121, "French"=121, "German"=121, "Italian"=121, "Japanese"=121, "Korean"=121, "Portuguese (Brazil)"=121, "Russian"=121, "Spanish"=121
"setCode" text FK: 121 distinct
"translation" text: 504 distinct, nulls=231

indexes: none

samples:
| column | latest | sample | sample |
|---|---|---|---|
| id | 1210 | 939 | 518 |
| language | Spanish | Russian | Portuguese (Brazil) |
| setCode | WTH | RAV | DKM |
| translation | null | Равника: Город Гильдий | Deckmasters 2001 |

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

samples:
| column | latest | sample | sample |
|---|---|---|---|
| id | 551 | 111 | 241 |
| baseSetSize | 285 | 12 | 4 |
| block | null | Friday Night Magic | Commander |
| booster | {'arena': {'boosters': [{'contents': {'common': 10, 'rareMythic': 1, 'uncommon': 3}, 'weight': 1}], 'boostersTotalWeight': 1, 'name': 'Zendikar Rising Arena Booster', 'sheets': {'common': {'balanceCo… | null | null |
| code | ZNR | F07 | OC17 |
| isFoilOnly | 0 | 1 | 1 |
| isForeignOnly | 0 | 0 | 0 |
| isNonFoilOnly | 0 | 0 | 0 |
| isOnlineOnly | 0 | 0 | 0 |
| isPartialPreview | 0 | 0 | 0 |
| keyruneCode | ZNR | DCI | C17 |
| mcmId | 3404 | null | null |
| mcmIdExtras | 3474 | null | null |
| mcmName | Zendikar Rising | null | null |
| mtgoCode | ZNR | null | null |
| name | Zendikar Rising | Friday Night Magic 2007 | Commander 2017 Oversized |
| parentCode | null | null | C17 |
| releaseDate | 2020-09-25 | 2007-01-01 | 2017-08-25 |
| tcgplayerGroupId | 2648 | null | null |
| totalSetSize | 392 | 12 | 4 |
| type | expansion | promo | memorabilia |
