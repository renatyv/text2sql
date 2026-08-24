---
generator: db-snooper
version: 0.0.34
generated_at_utc: 2026-08-24T21:59:27.374559Z
dialect: sqlite
database: /var/folders/9j/b9bx_drd53sc6zbpsqyrjy4h0000gn/T/dbsnoop-7_k1q89g/sqlite-sakila.sqlite
schema: main
---

## Relationships

- "actor"."actor_id" ← "film_actor"."actor_id"
- "address"."address_id" ← "customer"."address_id", "staff"."address_id", "store"."address_id"
- "category"."category_id" ← "film_category"."category_id"
- "city"."city_id" ← "address"."city_id"
- "country"."country_id" ← "city"."country_id"
- "customer"."customer_id" ← "payment"."customer_id", "rental"."customer_id"
- "film"."film_id" ← "film_actor"."film_id", "film_category"."film_id", "inventory"."film_id"
- "inventory"."inventory_id" ← "rental"."inventory_id"
- "language"."language_id" ← "film"."language_id", "film"."original_language_id"
- "rental"."rental_id" ← "payment"."rental_id"
- "staff"."staff_id" ← "payment"."staff_id", "rental"."staff_id", "store"."manager_staff_id"
- "store"."store_id" ← "customer"."store_id", "inventory"."store_id", "staff"."store_id"

# "actor"  (rows=200)

columns:
"actor_id" numeric PK: unique identifier, 1..200
"first_name" varchar45 NOTNULL: 128 distinct
"last_name" varchar45 NOTNULL: 121 distinct, "KILMER"=5, "NOLTE"=4, "TEMPLE"=4, "AKROYD"=3, "ALLEN"=3, "BERRY"=3, "DAVIS"=3, "DEGENERES"=3, "GARLAND"=3, "GUINESS"=3
"last_update" timestamp NOTNULL: "2021-03-06 15:51:59"=123, "2021-03-06 15:52:00"=77

indexes: "last_name"

samples:
| column | latest | sample | sample |
|---|---|---|---|
| actor_id | 200 | 135 | 123 |
| first_name | THORA | RITA | JULIANNE |
| last_name | TEMPLE | REYNOLDS | DENCH |
| last_update | 2021-03-06T15:52:00 | 2021-03-06T15:52:00 | 2021-03-06T15:51:59 |

# "address"  (rows=603)

columns:
"address_id" int PK: unique identifier, 1..605
"address" varchar50 NOTNULL: all distinct
"address2" varchar50: all NULL
"district" varchar20 NOTNULL: " "=603
"city_id" int NOTNULL FK: 599 distinct, 1..600
"postal_code" varchar10: digits, 596 distinct, nulls=4
"phone" varchar20 NOTNULL: " "=603
"last_update" timestamp NOTNULL: "2021-03-06 15:51:55"=131, "2021-03-06 15:51:58"=131, "2021-03-06 15:51:57"=128, "2021-03-06 15:51:56"=124, "2021-03-06 15:51:54"=72, "2021-03-06 15:51:59"=17

indexes: "city_id"

samples:
| column | latest | sample | sample |
|---|---|---|---|
| address_id | 605 | 422 | 458 |
| address | 1325 Fukuyama Street | 289 Santo Andr Manor | 138 Caracas Boulevard |
| address2 | null | null | null |
| district |   |   |   |
| city_id | 537 | 16 | 326 |
| postal_code | 27107 | 72410 | 16790 |
| phone |   |   |   |
| last_update | 2021-03-06T15:51:59 | 2021-03-06T15:51:57 | 2021-03-06T15:51:58 |

# "category"  (rows=16)

columns:
"category_id" smallint PK: unique identifier, 1..16
"name" varchar25 NOTNULL: "Action"=1, "Animation"=1, "Children"=1, "Classics"=1, "Comedy"=1, "Documentary"=1, "Drama"=1, "Family"=1, "Foreign"=1, "Games"=1, "Horror"=1, "Music"=1, "New"=1, "Sci-Fi"=1, "Sports"=1, "Travel"=1
"last_update" timestamp NOTNULL: "2021-03-06 15:52:00"=16

indexes: none

samples:
| column | latest | sample | sample |
|---|---|---|---|
| category_id | 16 | 13 | 3 |
| name | Travel | New | Children |
| last_update | 2021-03-06T15:52:00 | 2021-03-06T15:52:00 | 2021-03-06T15:52:00 |

# "city"  (rows=600)

columns:
"city_id" int PK: unique identifier, 1..600
"city" varchar50 NOTNULL: 599 distinct
"country_id" smallint NOTNULL FK: 109 distinct, 1..109, 44=60, 23=53, 103=35, 50=31, 60=30, 15=28, 80=28, 75=20, 97=15, 45=14
"last_update" timestamp NOTNULL: "2021-03-06 15:51:51"=138, "2021-03-06 15:51:50"=135, "2021-03-06 15:51:52"=131, "2021-03-06 15:51:53"=128, "2021-03-06 15:51:54"=55, "2021-03-06 15:51:49"=13

indexes: "country_id"

samples:
| column | latest | sample | sample |
|---|---|---|---|
| city_id | 600 | 262 | 217 |
| city | Ziguinchor | Kansas City | Ife |
| country_id | 83 | 103 | 69 |
| last_update | 2021-03-06T15:51:54 | 2021-03-06T15:51:51 | 2021-03-06T15:51:51 |

# "country"  (rows=109)

columns:
"country_id" smallint PK: unique identifier, 1..109
"country" varchar50 NOTNULL: all distinct
"last_update" timestamp: "2021-03-06 15:51:49"=109

indexes: none

samples:
| column | latest | sample | sample |
|---|---|---|---|
| country_id | 109 | 33 | 29 |
| country | Zambia | Finland | Egypt |
| last_update | 2021-03-06T15:51:49 | 2021-03-06T15:51:49 | 2021-03-06T15:51:49 |

# "customer"  (rows=599)

columns:
"customer_id" int PK: unique identifier, 1..599
"store_id" int NOTNULL FK: 1=326, 2=273
"first_name" varchar45 NOTNULL: 591 distinct
"last_name" varchar45 NOTNULL: all distinct
"email" varchar50: all distinct
"address_id" int NOTNULL FK: unique identifier, 5..605
"active" char1 NOTNULL: "1"=584, "0"=15
"create_date" timestamp NOTNULL: "2006-02-14 22:04:37.000"=328, "2006-02-14 22:04:36.000"=271
"last_update" timestamp NOTNULL: "2021-03-06 15:53:39"=120, "2021-03-06 15:53:38"=118, "2021-03-06 15:53:40"=118, "2021-03-06 15:53:37"=116, "2021-03-06 15:53:36"=111, "2021-03-06 15:53:41"=16

indexes: "address_id", "store_id", "last_name"

samples:
| column | latest | sample | sample |
|---|---|---|---|
| customer_id | 599 | 376 | 536 |
| store_id | 2 | 1 | 2 |
| first_name | AUSTIN | RANDY | FERNANDO |
| last_name | CINTRON | GAITHER | CHURCHILL |
| email | AUSTIN.CINTRON@sakilacustomer.org | RANDY.GAITHER@sakilacustomer.org | FERNANDO.CHURCHILL@sakilacustomer.org |
| address_id | 605 | 381 | 542 |
| active | 1 | 1 | 1 |
| create_date | 2006-02-14T22:04:37 | 2006-02-14T22:04:37 | 2006-02-14T22:04:37 |
| last_update | 2021-03-06T15:53:41 | 2021-03-06T15:53:39 | 2021-03-06T15:53:40 |

# "customer_list"  (rows=599)

```sql
CREATE VIEW customer_list
AS
SELECT cu.customer_id AS ID,
       cu.first_name||' '||cu.last_name AS name,
       a.address AS address,
       a.postal_code AS zip_code,
       a.phone AS phone,
       city.city AS city,
       country.country AS country,
       case when cu.active=1 then 'active' else '' end AS notes,
       cu.store_id AS SID
FROM customer AS cu JOIN address AS a ON cu.address_id = a.address_id JOIN city ON a.city_id = city.city_id
    JOIN country ON city.country_id = country.country_id;
```

columns:
"ID" int: unique identifier, 1..599
"name" text: all distinct
"address" varchar50: all distinct
"zip_code" varchar10: digits, 596 distinct
"phone" varchar20: " "=599
"city" varchar50: 597 distinct
"country" varchar50: 108 distinct
"notes" text: "active"=584, ""=15
"SID" int: 1=326, 2=273

samples:
| column | latest | sample | sample |
|---|---|---|---|
| ID | 599 | 71 | 357 |
| name | AUSTIN CINTRON | KATHY JAMES | KEITH RICO |
| address | 1325 Fukuyama Street | 492 Cam Ranh Street | 482 Kowloon and New Kowloon Manor |
| zip_code | 27107 | 50805 | 97056 |
| phone |   |   |   |
| city | Tieli | Baybay | Bratislava |
| country | China | Philippines | Slovakia |
| notes | active | active | active |
| SID | 2 | 1 | 1 |

# "film"  (rows=1000)

columns:
"film_id" int PK: unique identifier, 1..1000
"title" varchar255 NOTNULL: all distinct
"description" text: all distinct
"release_year" varchar4: "2006"=1000
"language_id" smallint NOTNULL FK: 1=1000
"original_language_id" smallint FK: all NULL
"rental_duration" smallint NOTNULL: 6=212, 3=203, 4=203, 5=191, 7=191, 3..7
"rental_rate" numeric NOTNULL: 0.99=341, 4.99=336, 2.99=323, 0.99..4.99
"length" smallint: 140 distinct, 46..185, avg=115.272, median=114
"replacement_cost" numeric NOTNULL: 21 distinct, 9.99..29.99, avg=19.984, median=19.99
"rating" varchar10: "PG-13"=223, "NC-17"=210, "R"=195, "PG"=194, "G"=178
"special_features" varchar100: "Trailers,Commentaries,Behind the Scenes"=79, "Trailers"=72, "Trailers,Behind the Scenes"=72, "Trailers,Commentaries"=72, "Deleted Scenes,Behind the Scenes"=71, "Behind the Scenes"=70, "Commentaries,Behind the Scenes"=70, "Commentaries,Deleted Scenes,Behind the Scenes"=66, "Trailers,Deleted Scenes"=66, "Commentaries,Deleted Scenes"=65, "Trailers,Commentaries,Deleted Scenes"=64, "Commentaries"=62, "Deleted Scenes"=61, "Trailers,Commentaries,Deleted Scenes,Behind the Scenes"=61, "Trailers,Deleted Scenes,Behind the Scenes"=49
"last_update" timestamp NOTNULL: "2021-03-06 15:52:02"=129, "2021-03-06 15:52:04"=127, "2021-03-06 15:52:03"=124, "2021-03-06 15:52:01"=123, "2021-03-06 15:52:06"=121, "2021-03-06 15:52:05"=118, "2021-03-06 15:52:07"=117, "2021-03-06 15:52:08"=107, "2021-03-06 15:52:00"=34

indexes: "language_id", "original_language_id"

samples:
| column | latest | sample | sample |
|---|---|---|---|
| film_id | 1000 | 415 | 637 |
| title | ZORRO ARK | HIGH ENCINO | OPEN AFRICAN |
| description | A Intrepid Panorama of a Mad Scientist And a Boy who must Redeem a Boy in A Monastery | A Fateful Saga of a Waitress And a Hunter who must Outrace a Sumo Wrestler in Australia | A Lacklusture Drama of a Secret Agent And a Explorer who must Discover a Car in A U-Boat |
| release_year | 2006 | 2006 | 2006 |
| language_id | 1 | 1 | 1 |
| original_language_id | null | null | null |
| rental_duration | 3 | 3 | 7 |
| rental_rate | 4.99 | 2.99 | 4.99 |
| length | 50 | 84 | 131 |
| replacement_cost | 18.99 | 23.99 | 16.99 |
| rating | NC-17 | R | PG |
| special_features | Trailers,Commentaries,Behind the Scenes | Trailers,Commentaries,Behind the Scenes | Trailers,Commentaries |
| last_update | 2021-03-06T15:52:08 | 2021-03-06T15:52:04 | 2021-03-06T15:52:05 |

# "film_actor"  (rows=5462)

columns:
"actor_id" int PK FK: 200 distinct, 1..200
"film_id" int PK FK: 997 distinct, 1..1000, 508=15, 87=13, 146=13, 188=13, 249=13, 606=13, 714=13, 34=12, 414=12, 517=12
"last_update" timestamp NOTNULL: 44 distinct

indexes: "actor_id", "film_id"

samples:
| column | latest | sample | sample |
|---|---|---|---|
| actor_id | 200 | 22 | 138 |
| film_id | 993 | 802 | 583 |
| last_update | 2021-03-06T15:53:28 | 2021-03-06T15:52:49 | 2021-03-06T15:53:15 |

# "film_category"  (rows=1000)

columns:
"film_id" int PK FK: unique identifier, 1..1000
"category_id" smallint PK FK: 15=74, 9=73, 8=69, 6=68, 2=66, 1=64, 13=63, 7=62, 10=61, 14=61, 3=60, 5=58, 4=57, 16=57, 11=56, 12=51, 1..16
"last_update" timestamp NOTNULL: "2021-03-06 15:53:29"=130, "2021-03-06 15:53:34"=129, "2021-03-06 15:53:35"=127, "2021-03-06 15:53:33"=126, "2021-03-06 15:53:30"=124, "2021-03-06 15:53:32"=123, "2021-03-06 15:53:31"=118, "2021-03-06 15:53:28"=117, "2021-03-06 15:53:36"=6

indexes: "category_id", "film_id"

samples:
| column | latest | sample | sample |
|---|---|---|---|
| film_id | 1000 | 941 | 525 |
| category_id | 5 | 10 | 4 |
| last_update | 2021-03-06T15:53:36 | 2021-03-06T15:53:35 | 2021-03-06T15:53:32 |

# "film_list"  (rows=5462)

```sql
CREATE VIEW film_list
AS
SELECT film.film_id AS FID,
       film.title AS title,
       film.description AS description,
       category.name AS category,
       film.rental_rate AS price,
       film.length AS length,
       film.rating AS rating,
       actor.first_name||' '||actor.last_name AS actors
FROM category LEFT JOIN film_category ON category.category_id = film_category.category_id LEFT JOIN film ON film_category.film_id = film.film_id
        JOIN film_actor ON film.film_id = film_actor.film_id
    JOIN actor ON film_actor.actor_id = actor.actor_id;
```

columns:
"FID" int: 997 distinct, 1..1000, avg=501.142, median=503
"title" varchar255: 997 distinct
"description" text: 997 distinct
"category" varchar25: "Sports"=441, "Foreign"=397, "Documentary"=385, "Action"=363, "Animation"=361, "Drama"=350, "Family"=347, "Children"=344, "New"=343, "Sci-Fi"=326, "Travel"=321, "Horror"=317, "Classics"=307, "Games"=293, "Comedy"=286, "Music"=281
"price" numeric: 0.99=1860, 2.99=1831, 4.99=1771, 0.99..4.99
"length" smallint: 140 distinct, 46..185, avg=115.337, median=114
"rating" varchar10: "PG-13"=1184, "PG"=1143, "NC-17"=1128, "R"=1031, "G"=976
"actors" text: 199 distinct

samples:
| column | latest | sample | sample |
|---|---|---|---|
| FID | 1000 | 880 | 520 |
| title | ZORRO ARK | TELEMARK HEARTBREAKERS | LICENSE WEEKEND |
| description | A Intrepid Panorama of a Mad Scientist And a Boy who must Redeem a Boy in A Monastery | A Action-Packed Panorama of a Technical Writer And a Man who must Build a Forensic Psychologist in A Manhattan Penthouse | A Insightful Story of a Man And a Husband who must Overcome a Madman in A Monastery |
| category | Comedy | Animation | Sci-Fi |
| price | 4.99 | 2.99 | 2.99 |
| length | 50 | 152 | 91 |
| rating | NC-17 | PG-13 | NC-17 |
| actors | NICK DEGENERES | HELEN VOIGHT | NATALIE HOPKINS |

# "inventory"  (rows=4581)

columns:
"inventory_id" int PK: unique identifier, 1..4581
"film_id" int NOTNULL FK: 958 distinct, 1..1000
"store_id" int NOTNULL FK: 2=2311, 1=2270
"last_update" timestamp NOTNULL: 38 distinct

indexes: "film_id", ("store_id","film_id")

samples:
| column | latest | sample | sample |
|---|---|---|---|
| inventory_id | 4581 | 404 | 1565 |
| film_id | 1000 | 89 | 344 |
| store_id | 2 | 2 | 1 |
| last_update | 2021-03-06T15:52:45 | 2021-03-06T15:52:11 | 2021-03-06T15:52:21 |

# "language"  (rows=6)

columns:
"language_id" smallint PK
"name" char20 NOTNULL
"last_update" timestamp NOTNULL

indexes: none

all rows:
| column | row 1 | row 2 | row 3 | row 4 | row 5 | row 6 |
|---|---|---|---|---|---|---|
| language_id | 1 | 2 | 3 | 4 | 5 | 6 |
| name | English | Italian | Japanese | Mandarin | French | German |
| last_update | 2021-03-06T15:51:48 | 2021-03-06T15:51:48 | 2021-03-06T15:51:48 | 2021-03-06T15:51:48 | 2021-03-06T15:51:48 | 2021-03-06T15:51:48 |

# "payment"  (rows=16049)

columns:
"payment_id" int PK: unique identifier, 1..16049
"customer_id" int NOTNULL FK: 599 distinct, 1..599
"staff_id" smallint NOTNULL FK: 1=8057, 2=7992
"rental_id" int FK: all distinct, nulls=5, 1..16049
"amount" numeric NOTNULL: 4.99=3789, 2.99=3542, 0.99=2979, 5.99=1299, 6.99=1119, 3.99=1109, 7.99=670, 1.99=640, 8.99=485, 9.99=256, 10.99=104, 0=24, 11.99=10, 3.98=8, 5.98=7, 7.98=5, 1.98=1, 8.97=1, 9.98=1, 0..11.99
"payment_date" timestamp NOTNULL: 15819 distinct
"last_update" timestamp NOTNULL: 133 distinct

indexes: "customer_id", "staff_id"

samples:
| column | latest | sample | sample |
|---|---|---|---|
| payment_id | 16049 | 1835 | 6541 |
| customer_id | 599 | 67 | 242 |
| staff_id | 2 | 2 | 1 |
| rental_id | 15725 | 8563 | 2691 |
| amount | 2.99 | 1.99 | 4.99 |
| payment_date | 2005-08-23T11:25:00 | 2005-07-29T11:32:58 | 2005-06-19T13:06:50 |
| last_update | 2021-03-06T15:58:09 | 2021-03-06T15:56:13 | 2021-03-06T15:56:52 |

# "rental"  (rows=16044)

columns:
"rental_id" int PK: unique identifier, 1..16049
"rental_date" timestamp NOTNULL: 15815 distinct, "2006-02-14 15:16:03.000"=182, "2005-05-30 14:47:31.000"=2, "2005-06-20 10:10:29.000"=2, "2005-06-21 09:04:50.000"=2, "2005-07-09 14:55:07.000"=2, "2005-07-10 20:41:41.000"=2, "2005-07-12 14:22:08.000"=2, "2005-07-27 08:14:34.000"=2, "2005-07-27 12:39:48.000"=2, "2005-07-27 15:18:42.000"=2
"inventory_id" int NOTNULL FK: 4580 distinct, 1..4581
"customer_id" int NOTNULL FK: 599 distinct, 1..599
"return_date" timestamp: 15836 distinct, nulls=183
"staff_id" smallint NOTNULL FK: 1=8040, 2=8004
"last_update" timestamp NOTNULL: 137 distinct

indexes: "customer_id", "inventory_id", "staff_id", UNIQUE ("rental_date","inventory_id","customer_id")

samples:
| column | latest | sample | sample |
|---|---|---|---|
| rental_id | 16049 | 3690 | 5667 |
| rental_date | 2005-08-23T22:50:12 | 2005-07-06T09:46:03 | 2005-07-10T08:11:03 |
| inventory_id | 2666 | 4405 | 683 |
| customer_id | 393 | 435 | 336 |
| return_date | 2005-08-30T01:01:12 | 2005-07-07T12:12:03 | 2005-07-15T08:23:03 |
| staff_id | 2 | 1 | 2 |
| last_update | 2021-03-06T15:55:57 | 2021-03-06T15:54:11 | 2021-03-06T15:54:27 |

# "sales_by_film_category"  (rows=16)

```sql
CREATE VIEW sales_by_film_category
AS
SELECT
c.name AS category
, SUM(p.amount) AS total_sales
FROM payment AS p
INNER JOIN rental AS r ON p.rental_id = r.rental_id
INNER JOIN inventory AS i ON r.inventory_id = i.inventory_id
INNER JOIN film AS f ON i.film_id = f.film_id
INNER JOIN film_category AS fc ON f.film_id = fc.film_id
INNER JOIN category AS c ON fc.category_id = c.category_id
GROUP BY c.name;
```

columns:
"category" varchar25: "Action"=1, "Animation"=1, "Children"=1, "Classics"=1, "Comedy"=1, "Documentary"=1, "Drama"=1, "Family"=1, "Foreign"=1, "Games"=1, "Horror"=1, "Music"=1, "New"=1, "Sci-Fi"=1, "Sports"=1, "Travel"=1
"total_sales" float: 3417.72=1, 3549.64=1, 3639.59=1, 3655.55=1, 3722.54=1, 4217.52=1, 4226.07=1, 4270.67=1, 4281.33=1, 4351.62=1, 4375.85=1, 4383.58=1, 4587.39=1, 4656.3=1, 4756.98=1, 5314.21=1

samples:
| column | latest | sample | sample |
|---|---|---|---|
| category | Travel | Children | Horror |
| total_sales | 3549.64 | 3655.55 | 3722.54 |

# "sales_by_store"  (rows=2)

```sql
CREATE VIEW sales_by_store
AS
SELECT
  s.store_id
 ,c.city||','||cy.country AS store
 ,m.first_name||' '||m.last_name AS manager
 ,SUM(p.amount) AS total_sales
FROM payment AS p
INNER JOIN rental AS r ON p.rental_id = r.rental_id
INNER JOIN inventory AS i ON r.inventory_id = i.inventory_id
INNER JOIN store AS s ON i.store_id = s.store_id
INNER JOIN address AS a ON s.address_id = a.address_id
INNER JOIN city AS c ON a.city_id = c.city_id
INNER JOIN country AS cy ON c.country_id = cy.country_id
INNER JOIN staff AS m ON s.manager_staff_id = m.staff_id
GROUP BY  
  s.store_id
, c.city||','||cy.country
, m.first_name||' '||m.last_name;
```

columns:
"store_id" int
"store" text
"manager" text
"total_sales" float

all rows:
| column | row 1 | row 2 |
|---|---|---|
| store_id | 1 | 2 |
| store | Lethbridge,Canada | Woodridge,Australia |
| manager | Mike Hillyer | Jon Stephens |
| total_sales | 33679.8 | 33726.8 |

# "staff"  (rows=2)

columns:
"staff_id" smallint PK
"first_name" varchar45 NOTNULL
"last_name" varchar45 NOTNULL
"address_id" int NOTNULL FK
"picture" bytes
"email" varchar50
"store_id" int NOTNULL FK
"active" smallint NOTNULL
"username" varchar16 NOTNULL
"password" varchar40
"last_update" timestamp NOTNULL

indexes: "address_id", "store_id"

all rows:
| column | row 1 | row 2 |
|---|---|---|
| staff_id | 1 | 2 |
| first_name | Mike | Jon |
| last_name | Hillyer | Stephens |
| address_id | 3 | 4 |
| picture | null | null |
| email | Mike.Hillyer@sakilastaff.com | Jon.Stephens@sakilastaff.com |
| store_id | 1 | 2 |
| active | 1 | 1 |
| username | Mike | Jon |
| last_update | 2021-03-06T15:52:00 | 2021-03-06T15:52:00 |

# "staff_list"  (rows=2)

```sql
CREATE VIEW staff_list
AS
SELECT s.staff_id AS ID,
       s.first_name||' '||s.last_name AS name,
       a.address AS address,
       a.postal_code AS zip_code,
       a.phone AS phone,
       city.city AS city,
       country.country AS country,
       s.store_id AS SID
FROM staff AS s JOIN address AS a ON s.address_id = a.address_id JOIN city ON a.city_id = city.city_id
    JOIN country ON city.country_id = country.country_id;
```

columns:
"ID" smallint
"name" text
"address" varchar50
"zip_code" varchar10
"phone" varchar20
"city" varchar50
"country" varchar50
"SID" int

all rows:
| column | row 1 | row 2 |
|---|---|---|
| ID | 1 | 2 |
| name | Mike Hillyer | Jon Stephens |
| address | 23 Workhaven Lane | 1411 Lillydale Drive |
| zip_code | null | null |
| phone |   |   |
| city | Lethbridge | Woodridge |
| country | Canada | Australia |
| SID | 1 | 2 |

# "store"  (rows=2)

columns:
"store_id" int PK
"manager_staff_id" smallint NOTNULL FK
"address_id" int NOTNULL FK
"last_update" timestamp NOTNULL

indexes: "address_id", "manager_staff_id"

all rows:
| column | row 1 | row 2 |
|---|---|---|
| store_id | 1 | 2 |
| manager_staff_id | 1 | 2 |
| address_id | 1 | 2 |
| last_update | 2021-03-06T15:52:00 | 2021-03-06T15:52:00 |

- Skipped 1 empty table(s): "film_text"
