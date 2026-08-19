---
generator: db-snooper
version: 0.0.26
generated_at_utc: 2026-08-16T08:08:42.121099Z
dialect: sqlite
database: /var/folders/9j/b9bx_drd53sc6zbpsqyrjy4h0000gn/T/dbsnoop-wg4z36tp/Pagila.sqlite
schema: main
---

## Relationships

- actor.actor_id ← film_actor.actor_id
- address.address_id ← customer.address_id, staff.address_id, store.address_id
- category.category_id ← film_category.category_id
- city.city_id ← address.city_id
- country.country_id ← city.country_id
- customer.customer_id ← payment.customer_id, rental.customer_id
- film.film_id ← film_actor.film_id, film_category.film_id, inventory.film_id
- inventory.inventory_id ← rental.inventory_id
- language.language_id ← film.language_id, film.original_language_id
- rental.rental_id ← payment.rental_id
- staff.staff_id ← payment.staff_id, rental.staff_id, store.manager_staff_id
- store.store_id ← customer.store_id, inventory.store_id, staff.store_id

# actor

```sql
CREATE TABLE actor (
  actor_id numeric NOT NULL ,
  first_name VARCHAR(45) NOT NULL,
  last_name VARCHAR(45) NOT NULL,
  last_update TIMESTAMP NOT NULL,
  PRIMARY KEY  (actor_id)
  );
```

## Indexes

- (last_name)

## Rows

- total=200

| column | latest | sample | sample |
|---|---|---|---|
| actor_id | 200.0000000000 | 40.0000000000 | 72.0000000000 |
| first_name | THORA | JOHNNY | SEAN |
| last_name | TEMPLE | CAGE | WILLIAMS |
| last_update | 2021-03-06T15:52:00 | 2021-03-06T15:51:59 | 2021-03-06T15:51:59 |

## Columns

- actor_id: unique identifier, num 1.0000000000..200.0000000000
- first_name: 128 distinct
- last_name: 121 distinct
  - top_values: "KILMER"=5, "NOLTE"=4, "TEMPLE"=4, "AKROYD"=3, "ALLEN"=3, "BERRY"=3, "DAVIS"=3, "DEGENERES"=3, "GARLAND"=3, "GUINESS"=3
- last_update: 2021-03-06 15:51:59=123, 2021-03-06 15:52:00=77


# address

```sql
CREATE TABLE address (
  address_id int NOT NULL,
  address VARCHAR(50) NOT NULL,
  address2 VARCHAR(50) DEFAULT NULL,
  district VARCHAR(20) NOT NULL,
  city_id INT  NOT NULL,
  postal_code VARCHAR(10) DEFAULT NULL,
  phone VARCHAR(20) NOT NULL,
  last_update TIMESTAMP NOT NULL,
  PRIMARY KEY  (address_id),
  CONSTRAINT fk_address_city FOREIGN KEY (city_id) REFERENCES city (city_id) ON DELETE NO ACTION ON UPDATE CASCADE
);
```

## Indexes

- (city_id)

## Rows

- total=603

| column | latest | sample | sample |
|---|---|---|---|
| address_id | 605 | 551 | 41 |
| address | 1325 Fukuyama Street | 182 Nukualofa Drive | 1440 Fukuyama Loop |
| address2 | null | null | null |
| district |   |   |   |
| city_id | 537 | 275 | 362 |
| postal_code | 27107 | 15414 | 47929 |
| phone |   |   |   |
| last_update | 2021-03-06T15:51:59 | 2021-03-06T15:51:58 | 2021-03-06T15:51:54 |

## Columns

- address_id: unique identifier, int 1..605
- address: all distinct
- address2: all NULL
- district: " "=603
- city_id: 599 distinct, int 1..600
  - top_values: 42=2, 300=2, 312=2, 576=2, 1=1, 2=1, 3=1, 4=1, 5=1, 6=1
- postal_code: 596 distinct, nulls=4
- phone: " "=603
- last_update: 2021-03-06 15:51:55=131, 2021-03-06 15:51:58=131, 2021-03-06 15:51:57=128, 2021-03-06 15:51:56=124, 2021-03-06 15:51:54=72, 2021-03-06 15:51:59=17


# category

```sql
CREATE TABLE category (
  category_id SMALLINT NOT NULL,
  name VARCHAR(25) NOT NULL,
  last_update TIMESTAMP NOT NULL,
  PRIMARY KEY  (category_id)
);
```

## Rows

- total=16

| column | latest | sample | sample |
|---|---|---|---|
| category_id | 16 | 11 | 6 |
| name | Travel | Horror | Documentary |
| last_update | 2021-03-06T15:52:00 | 2021-03-06T15:52:00 | 2021-03-06T15:52:00 |

## Columns

- category_id: unique identifier, int 1..16
- name: "Action"=1, "Animation"=1, "Children"=1, "Classics"=1, "Comedy"=1, "Documentary"=1, "Drama"=1, "Family"=1, "Foreign"=1, "Games"=1, "Horror"=1, "Music"=1, "New"=1, "Sci-Fi"=1, "Sports"=1, "Travel"=1
- last_update: 2021-03-06 15:52:00=16


# city

```sql
CREATE TABLE city (
  city_id int NOT NULL,
  city VARCHAR(50) NOT NULL,
  country_id SMALLINT NOT NULL,
  last_update TIMESTAMP NOT NULL,
  PRIMARY KEY  (city_id),
  CONSTRAINT fk_city_country FOREIGN KEY (country_id) REFERENCES country (country_id) ON DELETE NO ACTION ON UPDATE CASCADE
);
```

## Indexes

- (country_id)

## Rows

- total=600

| column | latest | sample | sample |
|---|---|---|---|
| city_id | 600 | 446 | 284 |
| city | Ziguinchor | Salinas | Kurashiki |
| country_id | 83 | 103 | 50 |
| last_update | 2021-03-06T15:51:54 | 2021-03-06T15:51:53 | 2021-03-06T15:51:51 |

## Columns

- city_id: unique identifier, int 1..600
- city: 599 distinct
- country_id: 109 distinct, int 1..109
  - top_values: 44=60, 23=53, 103=35, 50=31, 60=30, 15=28, 80=28, 75=20, 97=15, 45=14
- last_update: 2021-03-06 15:51:51=138, 2021-03-06 15:51:50=135, 2021-03-06 15:51:52=131, 2021-03-06 15:51:53=128, 2021-03-06 15:51:54=55, 2021-03-06 15:51:49=13


# country

```sql
CREATE TABLE country (
  country_id SMALLINT NOT NULL,
  country VARCHAR(50) NOT NULL,
  last_update TIMESTAMP,
  PRIMARY KEY  (country_id)
);
```

## Rows

- total=109

| column | latest | sample | sample |
|---|---|---|---|
| country_id | 109 | 68 | 49 |
| country | Zambia | New Zealand | Italy |
| last_update | 2021-03-06T15:51:49 | 2021-03-06T15:51:49 | 2021-03-06T15:51:49 |

## Columns

- country_id: unique identifier, int 1..109
- country: all distinct
- last_update: 2021-03-06 15:51:49=109


# customer

```sql
CREATE TABLE customer (
  customer_id INT NOT NULL,
  store_id INT NOT NULL,
  first_name VARCHAR(45) NOT NULL,
  last_name VARCHAR(45) NOT NULL,
  email VARCHAR(50) DEFAULT NULL,
  address_id INT NOT NULL,
  active CHAR(1) DEFAULT 'Y' NOT NULL,
  create_date TIMESTAMP NOT NULL,
  last_update TIMESTAMP NOT NULL,
  PRIMARY KEY  (customer_id),
  CONSTRAINT fk_customer_store FOREIGN KEY (store_id) REFERENCES store (store_id) ON DELETE NO ACTION ON UPDATE CASCADE,
  CONSTRAINT fk_customer_address FOREIGN KEY (address_id) REFERENCES address (address_id) ON DELETE NO ACTION ON UPDATE CASCADE
);
```

## Indexes

- (address_id)
- (store_id)
- (last_name)

## Rows

- total=599

| column | latest | sample | sample |
|---|---|---|---|
| customer_id | 599 | 383 | 71 |
| store_id | 2 | 1 | 1 |
| first_name | AUSTIN | MARTIN | KATHY |
| last_name | CINTRON | BALES | JAMES |
| email | AUSTIN.CINTRON@sakilacustomer.org | MARTIN.BALES@sakilacustomer.org | KATHY.JAMES@sakilacustomer.org |
| address_id | 605 | 388 | 75 |
| active | 1 | 1 | 1 |
| create_date | 2006-02-14T22:04:37 | 2006-02-14T22:04:37 | 2006-02-14T22:04:36 |
| last_update | 2021-03-06T15:53:41 | 2021-03-06T15:53:39 | 2021-03-06T15:53:36 |

## Columns

- customer_id: unique identifier, int 1..599
- store_id: 1=326, 2=273
- first_name: 591 distinct
- last_name: all distinct
- email: all distinct
- address_id: unique identifier, int 5..605
- active: "1"=584, "0"=15
- create_date: 2006-02-14 22:04:37=328, 2006-02-14 22:04:36=271
- last_update: 2021-03-06 15:53:39=120, 2021-03-06 15:53:38=118, 2021-03-06 15:53:40=118, 2021-03-06 15:53:37=116, 2021-03-06 15:53:36=111, 2021-03-06 15:53:41=16


# customer_list

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

## Rows

- total=599

| column | latest | sample | sample |
|---|---|---|---|
| ID | 599 | 308 | 245 |
| name | AUSTIN CINTRON | THOMAS GRIGSBY | COURTNEY DAY |
| address | 1325 Fukuyama Street | 1191 Sungai Petani Boulevard | 300 Junan Street |
| zip_code | 27107 | 9668 | 81314 |
| phone |   |   |   |
| city | Tieli | Kansas City | Uijongbu |
| country | China | United States | South Korea |
| notes | active | active | active |
| SID | 2 | 1 | 1 |

## Columns

- ID: unique identifier, int 1..599
  - stats: average=300, median=300
- name: all distinct
- address: all distinct
- zip_code: 596 distinct
- phone: " "=599
- city: 597 distinct
- country: 108 distinct
- notes: "active"=584, ""=15
- SID: 1=326, 2=273


# film

```sql
CREATE TABLE film (
  film_id int NOT NULL,
  title VARCHAR(255) NOT NULL,
  description BLOB SUB_TYPE TEXT DEFAULT NULL,
  release_year VARCHAR(4) DEFAULT NULL,
  language_id SMALLINT NOT NULL,
  original_language_id SMALLINT DEFAULT NULL,
  rental_duration SMALLINT  DEFAULT 3 NOT NULL,
  rental_rate DECIMAL(4,2) DEFAULT 4.99 NOT NULL,
  length SMALLINT DEFAULT NULL,
  replacement_cost DECIMAL(5,2) DEFAULT 19.99 NOT NULL,
  rating VARCHAR(10) DEFAULT 'G',
  special_features VARCHAR(100) DEFAULT NULL,
  last_update TIMESTAMP NOT NULL,
  PRIMARY KEY  (film_id),
  CONSTRAINT CHECK_special_features CHECK(special_features is null or
                                                           special_features like '%Trailers%' or
                                                           special_features like '%Commentaries%' or
                                                           special_features like '%Deleted Scenes%' or
                                                           special_features like '%Behind the Scenes%'),
  CONSTRAINT CHECK_special_rating CHECK(rating in ('G','PG','PG-13','R','NC-17')),
  CONSTRAINT fk_film_language FOREIGN KEY (language_id) REFERENCES language (language_id) ,
  CONSTRAINT fk_film_language_original FOREIGN KEY (original_language_id) REFERENCES language (language_id)
);
```

## Indexes

- (language_id)
- (original_language_id)

## Rows

- total=1000

| column | latest | sample | sample |
|---|---|---|---|
| film_id | 1000 | 448 | 649 |
| title | ZORRO ARK | IDAHO LOVE | OZ LIAISONS |
| description | A Intrepid Panorama of a Mad Scientist And a Boy who must Redeem a Boy in A Monastery | A Fast-Paced Drama of a Student And a Crocodile who must Meet a Database Administrator in The Outback | A Epic Yarn of a Mad Scientist And a Cat who must Confront a Womanizer in A Baloon Factory |
| release_year | 2006 | 2006 | 2006 |
| language_id | 1 | 1 | 1 |
| original_language_id | null | null | null |
| rental_duration | 3 | 3 | 4 |
| rental_rate | 4.99 | 2.99 | 2.99 |
| length | 50 | 172 | 85 |
| replacement_cost | 18.99 | 25.99 | 14.99 |
| rating | NC-17 | PG-13 | R |
| special_features | Trailers,Commentaries,Behind the Scenes | Trailers,Commentaries,Deleted Scenes,Behind the Scenes | Commentaries,Deleted Scenes,Behind the Scenes |
| last_update | 2021-03-06T15:52:08 | 2021-03-06T15:52:04 | 2021-03-06T15:52:05 |

## Columns

- film_id: unique identifier, int 1..1000
- title: all distinct
- description: all distinct
- release_year: "2006"=1000
- language_id: 1=1000
- original_language_id: all NULL
- rental_duration: 6=212, 3=203, 4=203, 5=191, 7=191, int 3..7
- rental_rate: 0.99=341, 4.99=336, 2.99=323, num 0.99..4.99
- length: 140 distinct, int 46..185
  - stats: average=115.272, median=114
- replacement_cost: 21 distinct, num 9.99..29.99
  - stats: average=19.984, median=19.99
- rating: "PG-13"=223, "NC-17"=210, "R"=195, "PG"=194, "G"=178
- special_features: "Trailers,Commentaries,Behind the Scenes"=79, "Trailers"=72, "Trailers,Behind the Scenes"=72, "Trailers,Commentaries"=72, "Deleted Scenes,Behind the Scenes"=71, "Behind the Scenes"=70, "Commentaries,Behind the Scenes"=70, "Commentaries,Deleted Scenes,Behind the Scenes"=66, "Trailers,Deleted Scenes"=66, "Commentaries,Deleted Scenes"=65, "Trailers,Commentaries,Deleted Scenes"=64, "Commentaries"=62, "Deleted Scenes"=61, "Trailers,Commentaries,Deleted Scenes,Behind the Scenes"=61, "Trailers,Deleted Scenes,Behind the Scenes"=49
- last_update: 2021-03-06 15:52:02=129, 2021-03-06 15:52:04=127, 2021-03-06 15:52:03=124, 2021-03-06 15:52:01=123, 2021-03-06 15:52:06=121, 2021-03-06 15:52:05=118, 2021-03-06 15:52:07=117, 2021-03-06 15:52:08=107, 2021-03-06 15:52:00=34


# film_actor

```sql
CREATE TABLE film_actor (
  actor_id INT NOT NULL,
  film_id  INT NOT NULL,
  last_update TIMESTAMP NOT NULL,
  PRIMARY KEY  (actor_id,film_id),
  CONSTRAINT fk_film_actor_actor FOREIGN KEY (actor_id) REFERENCES actor (actor_id) ON DELETE NO ACTION ON UPDATE CASCADE,
  CONSTRAINT fk_film_actor_film FOREIGN KEY (film_id) REFERENCES film (film_id) ON DELETE NO ACTION ON UPDATE CASCADE
);
```

## Indexes

- (actor_id)
- (film_id)

## Rows

- total=5462

| column | latest | sample | sample |
|---|---|---|---|
| actor_id | 200 | 171 | 32 |
| film_id | 993 | 892 | 651 |
| last_update | 2021-03-06T15:53:28 | 2021-03-06T15:53:22 | 2021-03-06T15:52:51 |

## Columns

- actor_id: 200 distinct, int 1..200
  - top_values: 107=42, 102=41, 198=40, 181=39, 23=37, 81=36, 13=35, 37=35, 60=35, 106=35
- film_id: 997 distinct, int 1..1000
  - top_values: 508=15, 87=13, 146=13, 188=13, 249=13, 606=13, 714=13, 34=12, 414=12, 517=12
- last_update: 44 distinct


# film_category

```sql
CREATE TABLE film_category (
  film_id INT NOT NULL,
  category_id SMALLINT  NOT NULL,
  last_update TIMESTAMP NOT NULL,
  PRIMARY KEY (film_id, category_id),
  CONSTRAINT fk_film_category_film FOREIGN KEY (film_id) REFERENCES film (film_id) ON DELETE NO ACTION ON UPDATE CASCADE,
  CONSTRAINT fk_film_category_category FOREIGN KEY (category_id) REFERENCES category (category_id) ON DELETE NO ACTION ON UPDATE CASCADE
);
```

## Indexes

- (category_id)
- (film_id)

## Rows

- total=1000

| column | latest | sample | sample |
|---|---|---|---|
| film_id | 1000 | 829 | 705 |
| category_id | 5 | 8 | 9 |
| last_update | 2021-03-06T15:53:36 | 2021-03-06T15:53:34 | 2021-03-06T15:53:33 |

## Columns

- film_id: unique identifier, int 1..1000
- category_id: 15=74, 9=73, 8=69, 6=68, 2=66, 1=64, 13=63, 7=62, 10=61, 14=61, 3=60, 5=58, 4=57, 16=57, 11=56, 12=51, int 1..16
- last_update: 2021-03-06 15:53:29=130, 2021-03-06 15:53:34=129, 2021-03-06 15:53:35=127, 2021-03-06 15:53:33=126, 2021-03-06 15:53:30=124, 2021-03-06 15:53:32=123, 2021-03-06 15:53:31=118, 2021-03-06 15:53:28=117, 2021-03-06 15:53:36=6


# film_list

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

## Rows

- total=5462

| column | latest | sample | sample |
|---|---|---|---|
| FID | 1000 | 553 | 132 |
| title | ZORRO ARK | MAKER GABLES | CHAINSAW UPTOWN |
| description | A Intrepid Panorama of a Mad Scientist And a Boy who must Redeem a Boy in A Monastery | A Stunning Display of a Moose And a Database Administrator who must Pursue a Composer in A Jet Boat | A Beautiful Documentary of a Boy And a Robot who must Discover a Squirrel in Australia |
| category | Comedy | Children | Sci-Fi |
| price | 4.99 | 0.99 | 0.99 |
| length | 50 | 136 | 114 |
| rating | NC-17 | PG-13 | PG |
| actors | NICK DEGENERES | CUBA ALLEN | NICK WAHLBERG |

## Columns

- FID: 997 distinct, int 1..1000
  - stats: average=501.142, median=503
- title: 997 distinct
- description: 997 distinct
- category: "Sports"=441, "Foreign"=397, "Documentary"=385, "Action"=363, "Animation"=361, "Drama"=350, "Family"=347, "Children"=344, "New"=343, "Sci-Fi"=326, "Travel"=321, "Horror"=317, "Classics"=307, "Games"=293, "Comedy"=286, "Music"=281
- price: 0.99=1860, 2.99=1831, 4.99=1771, num 0.99..4.99
- length: 140 distinct, int 46..185
  - stats: average=115.337, median=114
- rating: "PG-13"=1184, "PG"=1143, "NC-17"=1128, "R"=1031, "G"=976
- actors: 199 distinct


# inventory

```sql
CREATE TABLE inventory (
  inventory_id INT NOT NULL,
  film_id INT NOT NULL,
  store_id INT NOT NULL,
  last_update TIMESTAMP NOT NULL,
  PRIMARY KEY  (inventory_id),
  CONSTRAINT fk_inventory_store FOREIGN KEY (store_id) REFERENCES store (store_id) ON DELETE NO ACTION ON UPDATE CASCADE,
  CONSTRAINT fk_inventory_film FOREIGN KEY (film_id) REFERENCES film (film_id) ON DELETE NO ACTION ON UPDATE CASCADE
);
```

## Indexes

- (film_id)
- (store_id,film_id)

## Rows

- total=4581

| column | latest | sample | sample |
|---|---|---|---|
| inventory_id | 4581 | 902 | 1089 |
| film_id | 1000 | 200 | 243 |
| store_id | 2 | 2 | 1 |
| last_update | 2021-03-06T15:52:45 | 2021-03-06T15:52:15 | 2021-03-06T15:52:17 |

## Columns

- inventory_id: unique identifier, int 1..4581
- film_id: 958 distinct, int 1..1000
  - top_values: 1=8, 31=8, 69=8, 73=8, 86=8, 91=8, 103=8, 109=8, 127=8, 174=8
- store_id: 2=2311, 1=2270
- last_update: 38 distinct


# language

## All rows

| column | row 1 | row 2 | row 3 | row 4 | row 5 | row 6 |
|---|---|---|---|---|---|---|
| language_id | 1 | 2 | 3 | 4 | 5 | 6 |
| name | English | Italian | Japanese | Mandarin | French | German |
| last_update | 2021-03-06T15:51:48 | 2021-03-06T15:51:48 | 2021-03-06T15:51:48 | 2021-03-06T15:51:48 | 2021-03-06T15:51:48 | 2021-03-06T15:51:48 |


# payment

```sql
CREATE TABLE payment (
  payment_id int NOT NULL,
  customer_id INT  NOT NULL,
  staff_id SMALLINT NOT NULL,
  rental_id INT DEFAULT NULL,
  amount DECIMAL(5,2) NOT NULL,
  payment_date TIMESTAMP NOT NULL,
  last_update TIMESTAMP NOT NULL,
  PRIMARY KEY  (payment_id),
  CONSTRAINT fk_payment_rental FOREIGN KEY (rental_id) REFERENCES rental (rental_id) ON DELETE SET NULL ON UPDATE CASCADE,
  CONSTRAINT fk_payment_customer FOREIGN KEY (customer_id) REFERENCES customer (customer_id) ,
  CONSTRAINT fk_payment_staff FOREIGN KEY (staff_id) REFERENCES staff (staff_id)
);
```

## Indexes

- (customer_id)
- (staff_id)

## Rows

- total=16049

| column | latest | sample | sample |
|---|---|---|---|
| payment_id | 16049 | 9742 | 9981 |
| customer_id | 599 | 360 | 369 |
| staff_id | 2 | 1 | 2 |
| rental_id | 15725 | 15310 | 3903 |
| amount | 2.99 | 2.99 | 2.99 |
| payment_date | 2005-08-23T11:25:00 | 2005-08-22T19:56:41 | 2005-07-06T19:27:32 |
| last_update | 2021-03-06T15:58:09 | 2021-03-06T15:57:18 | 2021-03-06T15:57:20 |

## Columns

- payment_id: unique identifier, int 1..16049
- customer_id: 599 distinct, int 1..599
  - top_values: 148=46, 526=45, 144=42, 236=42, 75=41, 197=40, 469=40, 137=39, 178=39, 468=39
- staff_id: 1=8057, 2=7992
- rental_id: all distinct, nulls=5, int 1..16049
- amount: 4.99=3789, 2.99=3542, 0.99=2979, 5.99=1299, 6.99=1119, 3.99=1109, 7.99=670, 1.99=640, 8.99=485, 9.99=256, 10.99=104, 0.00=24, 11.99=10, 3.98=8, 5.98=7, 7.98=5, 1.98=1, 8.97=1, 9.98=1, num 0.00..11.99
- payment_date: 15819 distinct
- last_update: 133 distinct


# rental

```sql
CREATE TABLE rental (
  rental_id INT NOT NULL,
  rental_date TIMESTAMP NOT NULL,
  inventory_id INT  NOT NULL,
  customer_id INT  NOT NULL,
  return_date TIMESTAMP DEFAULT NULL,
  staff_id SMALLINT  NOT NULL,
  last_update TIMESTAMP NOT NULL,
  PRIMARY KEY (rental_id),
  CONSTRAINT fk_rental_staff FOREIGN KEY (staff_id) REFERENCES staff (staff_id) ,
  CONSTRAINT fk_rental_inventory FOREIGN KEY (inventory_id) REFERENCES inventory (inventory_id) ,
  CONSTRAINT fk_rental_customer FOREIGN KEY (customer_id) REFERENCES customer (customer_id)
);
```

## Indexes

- (customer_id)
- (inventory_id)
- (staff_id)
- UNIQUE (rental_date,inventory_id,customer_id)

## Rows

- total=16044

| column | latest | sample | sample |
|---|---|---|---|
| rental_id | 16049 | 12180 | 6594 |
| rental_date | 2005-08-23T22:50:12 | 2005-08-18T01:28:15 | 2005-07-12T07:25:43 |
| inventory_id | 2666 | 2276 | 4458 |
| customer_id | 393 | 20 | 517 |
| return_date | 2005-08-30T01:01:12 | 2005-08-20T20:52:15 | 2005-07-13T07:59:43 |
| staff_id | 2 | 2 | 1 |
| last_update | 2021-03-06T15:55:57 | 2021-03-06T15:55:21 | 2021-03-06T15:54:35 |

## Columns

- rental_id: unique identifier, int 1..16049
- rental_date: 15815 distinct
  - top_values: 2006-02-14 15:16:03=182, 2005-05-30 14:47:31=2, 2005-06-20 10:10:29=2, 2005-06-21 09:04:50=2, 2005-07-09 14:55:07=2, 2005-07-10 20:41:41=2, 2005-07-12 14:22:08=2, 2005-07-27 08:14:34=2, 2005-07-27 12:39:48=2, 2005-07-27 15:18:42=2
- inventory_id: 4580 distinct, int 1..4581
  - top_values: 2=5, 6=5, 14=5, 17=5, 23=5, 26=5, 30=5, 37=5, 39=5, 40=5
- customer_id: 599 distinct, int 1..599
  - top_values: 148=46, 526=45, 144=42, 236=42, 75=41, 197=40, 469=40, 137=39, 178=39, 468=39
- return_date: 15836 distinct, nulls=183
- staff_id: 1=8040, 2=8004
- last_update: 137 distinct


# sales_by_film_category

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

## Rows

- total=16

| column | latest | sample | sample |
|---|---|---|---|
| category | Travel | Animation | Family |
| total_sales | 3549.64 | 4656.3 | 4226.07 |

## Columns

- category: "Action"=1, "Animation"=1, "Children"=1, "Classics"=1, "Comedy"=1, "Documentary"=1, "Drama"=1, "Family"=1, "Foreign"=1, "Games"=1, "Horror"=1, "Music"=1, "New"=1, "Sci-Fi"=1, "Sports"=1, "Travel"=1
- total_sales: 3417.72=1, 3549.64=1, 3639.59=1, 3655.55=1, 3722.54=1, 4217.52=1, 4226.07=1, 4270.67=1, 4281.33=1, 4351.62=1, 4375.85=1, 4383.58=1, 4587.39=1, 4656.3=1, 4756.98=1, 5314.21=1


# sales_by_store

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

## All rows

| column | row 1 | row 2 |
|---|---|---|
| store_id | 1 | 2 |
| store | Lethbridge,Canada | Woodridge,Australia |
| manager | Mike Hillyer | Jon Stephens |
| total_sales | 33679.8 | 33726.8 |


# staff

## All rows

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
| password | [REDACTED] | [REDACTED] |
| last_update | 2021-03-06T15:52:00 | 2021-03-06T15:52:00 |


# staff_list

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

## All rows

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


# store

## All rows

| column | row 1 | row 2 |
|---|---|---|
| store_id | 1 | 2 |
| manager_staff_id | 1 | 2 |
| address_id | 1 | 2 |
| last_update | 2021-03-06T15:52:00 | 2021-03-06T15:52:00 |


- Skipped 1 empty table(s): film_text
