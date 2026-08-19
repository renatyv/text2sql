---
generator: db-snooper
version: 0.0.26
generated_at_utc: 2026-08-16T07:19:19.992510Z
dialect: sqlite
database: /Users/renatyuldashev/Documents/ai-sql/custom-bench/data/bird_mini_dev/databases/dev_databases/superhero/superhero.sqlite
schema: main
---

## Relationships

- alignment.id ← superhero.alignment_id
- attribute.id ← hero_attribute.attribute_id
- colour.id ← superhero.eye_colour_id, superhero.hair_colour_id, superhero.skin_colour_id
- gender.id ← superhero.gender_id
- publisher.id ← superhero.publisher_id
- race.id ← superhero.race_id
- superhero.id ← hero_attribute.hero_id, hero_power.hero_id
- superpower.id ← hero_power.power_id

# alignment

## All rows

| column | row 1 | row 2 | row 3 | row 4 |
|---|---|---|---|---|
| id | 1 | 2 | 3 | 4 |
| alignment | Good | Bad | Neutral | N/A |


# attribute

## All rows

| column | row 1 | row 2 | row 3 | row 4 | row 5 | row 6 |
|---|---|---|---|---|---|---|
| id | 1 | 2 | 3 | 4 | 5 | 6 |
| attribute_name | Intelligence | Strength | Speed | Durability | Power | Combat |


# colour

```sql
CREATE TABLE colour
(
    id     INTEGER not null
            primary key,
    colour TEXT default NULL
);
```

## Rows

- total=35

| column | latest | sample | sample |
|---|---|---|---|
| id | 35 | 14 | 13 |
| colour | Yellow/Red | Green | Grey |

## Columns

- id: unique identifier, int 1..35
- colour: all distinct


# gender

## All rows

| column | row 1 | row 2 | row 3 |
|---|---|---|---|
| id | 1 | 2 | 3 |
| gender | Male | Female | N/A |


# hero_attribute

```sql
CREATE TABLE hero_attribute
(
    hero_id         INTEGER default NULL,
    attribute_id    INTEGER default NULL,
    attribute_value INTEGER default NULL,
    foreign key (attribute_id) references attribute(id),
    foreign key (hero_id) references superhero(id)
);
```

## Rows

- total=3738

| column | latest | sample | sample |
|---|---|---|---|
| hero_id | 756 | 382 | 621 |
| attribute_id | 6 | 6 | 2 |
| attribute_value | 100 | 15 | 50 |

## Columns

- hero_id: 623 distinct, int 1..756
- attribute_id: 1=623, 2=623, 3=623, 4=623, 5=623, 6=623, int 1..6
- attribute_value: 20 distinct, int 5..100
  - stats: average=52.4264, median=50


# hero_power

```sql
CREATE TABLE hero_power
(
    hero_id  INTEGER default NULL,
    power_id INTEGER default NULL,
    foreign key (hero_id) references superhero(id),
    foreign key (power_id) references superpower(id)
);
```

## Rows

- total=5825

| column | latest | sample | sample |
|---|---|---|---|
| hero_id | 756 | 735 | 286 |
| power_id | 132 | 34 | 48 |

## Columns

- hero_id: 652 distinct, int 1..756
- power_id: 167 distinct, int 1..167


# publisher

```sql
CREATE TABLE publisher
(
    id             INTEGER not null
            primary key,
    publisher_name TEXT default NULL
);
```

## Rows

- total=25

| column | latest | sample | sample |
|---|---|---|---|
| id | 25 | 25 | 12 |
| publisher_name | Wildstorm | Wildstorm | J. R. R. Tolkien |

## Columns

- id: unique identifier, int 1..25
- publisher_name: all distinct


# race

```sql
CREATE TABLE race
(
    id   INTEGER not null
            primary key,
    race TEXT default NULL
);
```

## Rows

- total=61

| column | latest | sample | sample |
|---|---|---|---|
| id | 61 | 48 | 14 |
| race | Zombie | Rodian | Czarnian |

## Columns

- id: unique identifier, int 1..61
- race: all distinct


# superhero

```sql
CREATE TABLE superhero
(
    id             INTEGER not null
            primary key,
    superhero_name TEXT default NULL,
    full_name      TEXT default NULL,
    gender_id      INTEGER          default NULL,
    eye_colour_id  INTEGER          default NULL,
    hair_colour_id INTEGER          default NULL,
    skin_colour_id INTEGER          default NULL,
    race_id        INTEGER          default NULL,
    publisher_id   INTEGER          default NULL,
    alignment_id   INTEGER          default NULL,
    height_cm      INTEGER          default NULL,
    weight_kg      INTEGER          default NULL,
    foreign key (alignment_id) references alignment(id),
    foreign key (eye_colour_id) references colour(id),
    foreign key (gender_id) references gender(id),
    foreign key (hair_colour_id) references colour(id),
    foreign key (publisher_id) references publisher(id),
    foreign key (race_id) references race(id),
    foreign key (skin_colour_id) references colour(id)
);
```

## Rows

- total=750

| column | latest | sample | sample |
|---|---|---|---|
| id | 756 | 203 | 149 |
| superhero_name | Zoom | Cypher | Cable |
| full_name | Hunter Zolomon | Douglas Aaron Ramsey | Nathan Christopher Charles Summers Dayspring |
| gender_id | 1 | 3 | 1 |
| eye_colour_id | 23 | 7 | 7 |
| hair_colour_id | 9 | 6 | 31 |
| skin_colour_id | 1 | 1 | 1 |
| race_id | 1 | 1 | 42 |
| publisher_id | 4 | 13 | 13 |
| alignment_id | 2 | 1 | 1 |
| height_cm | 185 | 175 | 203 |
| weight_kg | 81 | 68 | 158 |

## Columns

- id: unique identifier, int 1..756
- superhero_name: 743 distinct
- full_name: 483 distinct, nulls=122
- gender_id: 1=519, 2=203, 3=28, int 1..3
- eye_colour_id: 21 distinct, int 1..35
- hair_colour_id: 26 distinct, int 1..33
- skin_colour_id: 1=681, 14=21, 7=9, 23=9, 31=7, 28=5, 13=4, 22=3, 12=2, 21=2, 33=2, 4=1, 8=1, 19=1, 20=1, 24=1, int 1..33
- race_id: 61 distinct, nulls=4, int 1..61
- publisher_id: 25 distinct, nulls=3, int 1..25
- alignment_id: 1=504, 2=212, 3=28, nulls=6, int 1..3
- height_cm: 55 distinct, nulls=58, int 0..30480
  - stats: average=267.751, median=178
- weight_kg: 140 distinct, nulls=64, int 0..90000000
  - stats: average=144518, median=72


# superpower

```sql
CREATE TABLE superpower
(
    id         INTEGER not null
            primary key,
    power_name TEXT default NULL
);
```

## Rows

- total=167

| column | latest | sample | sample |
|---|---|---|---|
| id | 167 | 52 | 56 |
| power_name | Omniscient | Element Control | Fire Control |

## Columns

- id: unique identifier, int 1..167
- power_name: all distinct
