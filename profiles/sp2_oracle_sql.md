---
generator: db-snooper
version: 0.0.34
generated_at_utc: 2026-08-24T21:23:56.975469Z
dialect: sqlite
database: /var/folders/9j/b9bx_drd53sc6zbpsqyrjy4h0000gn/T/dbsnoop-qkgmu2gm/oracle_sql.sqlite
schema: main
---

## Relationships

- "breweries"."id" ← "purchases"."brewery_id"
- "customers"."id" ← "customer_favorites"."customer_id", "customer_reviews"."customer_id", "orders"."customer_id"
- "employees"."id" ← "emp_hire_periods"."emp_id", "employees"."supervisor_id", "picking_list"."picker_emp_id"
- "id_name_coll_type"."collection_id" ← "id_name_coll_entries"."collection_id"
- "locations"."id" ← "inventory"."location_id", "picking_line"."location_id", "picking_log"."location_id"
- "orders"."id" ← "orderlines"."order_id", "picking_line"."order_id"
- "packaging"."id" ← "packaging_relations"."contains_id", "packaging_relations"."packaging_id"
- "picking_line".("picklist_id", "line_no") ← "picking_log".("picklist_id", "pickline_no")
- "picking_list"."id" ← "picking_line"."picklist_id", "picking_log"."picklist_id"
- "product_groups"."id" ← "products"."group_id"
- "products"."id" ← "inventory"."product_id", "monthly_budget"."product_id", "monthly_sales"."product_id", "orderlines"."product_id", "picking_line"."product_id", "product_alcohol"."product_id", "product_minimums"."product_id", "purchases"."product_id"
- "purchases"."id" ← "inventory"."purchase_id"
- "stock"."symbol" ← "ticker"."symbol"
- "web_apps"."id" ← "web_pages"."app_id"
- "web_pages".("app_id", "page_no") ← "web_counter_hist".("app_id", "page_no"), "web_page_visits".("app_id", "page_no")

# "breweries"  (rows=3)

columns:
"id" int PK
"name" text NOTNULL

indexes: none

all rows:
| column | row 1 | row 2 | row 3 |
|---|---|---|---|
| id | 518 | 523 | 536 |
| name | Balthazar Brauerei | Happy Hoppy Hippo | Brewing Barbarian |

# "brewery_products"  (rows=10)

```sql
CREATE VIEW brewery_products AS
SELECT
   b.id AS brewery_id,
   b.name AS brewery_name,
   p.id AS product_id,
   p.name AS product_name
FROM breweries b
CROSS JOIN products p
WHERE EXISTS (
   SELECT 1
   FROM purchases pu
   WHERE pu.brewery_id = b.id
   AND pu.product_id = p.id
);
```

columns:
"brewery_id" int
"brewery_name" text
"product_id" int
"product_name" text

all rows:
| column | row 1 | row 2 | row 3 | row 4 | row 5 | row 6 | row 7 | row 8 | row 9 | row 10 |
|---|---|---|---|---|---|---|---|---|---|---|
| brewery_id | 518 | 518 | 518 | 523 | 523 | 523 | 536 | 536 | 536 | 536 |
| brewery_name | Balthazar Brauerei | Balthazar Brauerei | Balthazar Brauerei | Happy Hoppy Hippo | Happy Hoppy Hippo | Happy Hoppy Hippo | Brewing Barbarian | Brewing Barbarian | Brewing Barbarian | Brewing Barbarian |
| product_id | 5310 | 5430 | 6520 | 6600 | 7790 | 7870 | 4040 | 4160 | 4280 | 7950 |
| product_name | Monks and Nuns | Hercule Trippel | Der Helle Kumpel | Hazy Pink Cloud | Summer in India | Ghost of Hops | Coalminers Sweat | Reindeer Fuel | Hoppy Crude Oil | Pale Rider Rides |

# "channels_dim"  (rows=2)

columns:
"id" int PK
"name" text NOTNULL
"shortcut" text NOTNULL

indexes: none

all rows:
| column | row 1 | row 2 |
|---|---|---|
| id | 42 | 44 |
| name | Twitter | Facebook |
| shortcut | tw | fb |

# "customer_favorites"  (rows=4)

columns:
"customer_id" int PK FK
"favorite_list" text

indexes: none

all rows:
| column | row 1 | row 2 | row 3 | row 4 |
|---|---|---|---|---|
| customer_id | 50042 | 50741 | 51007 | 51069 |
| favorite_list | 4040,5310 | 5430,7790,7870 | null | 6520 |

# "customer_order_products"  (rows=18)

```sql
CREATE VIEW customer_order_products AS
SELECT
   c.id AS customer_id,
   c.name AS customer_name,
   o.ordered,
   p.id AS product_id,
   p.name AS product_name,
   ol.qty
FROM customers c
JOIN orders o ON o.customer_id = c.id
JOIN orderlines ol ON ol.order_id = o.id
JOIN products p ON p.id = ol.product_id;
```

columns:
"customer_id" int: 50741=7, 51069=6, 50042=5, 50042..51069
"customer_name" text: "Hygge og Humle"=7, "Der Wichtelmann"=6, "The White Hart"=5
"ordered" text: "2019-02-17"=3, "2019-01-15"=2, "2019-01-17"=2, "2019-01-18"=2, "2019-02-26"=2, "2019-03-12"=2, "2019-03-22"=2, "2019-01-28"=1, "2019-03-02"=1, "2019-03-29"=1
"product_id" int: 4280=6, 6520=4, 6600=3, 5430=2, 7950=2, 5310=1, 4280..7950
"product_name" text: "Hoppy Crude Oil"=6, "Der Helle Kumpel"=4, "Hazy Pink Cloud"=3, "Hercule Trippel"=2, "Pale Rider Rides"=2, "Monks and Nuns"=1
"qty" float: 40=4, 60=3, 80=3, 16=2, 24=1, 50=1, 90=1, 100=1, 110=1, 140=1, 16..140

samples:
| column | latest | sample | sample |
|---|---|---|---|
| customer_id | 51069 | 50741 | 50741 |
| customer_name | Der Wichtelmann | Hygge og Humle | Hygge og Humle |
| ordered | 2019-02-17 | 2019-02-26 | 2019-03-12 |
| product_id | 6600 | 6600 | 4280 |
| product_name | Hazy Pink Cloud | Hazy Pink Cloud | Hoppy Crude Oil |
| qty | 24 | 16 | 90 |

# "customer_order_products_obj"  (rows=3)

```sql
CREATE VIEW customer_order_products_obj AS
SELECT
   customer_id,
   MAX(customer_name) AS customer_name,
   '[' || GROUP_CONCAT(
      '{ "product_id": ' || product_id || ', "product_name": "' || product_name || '" }'
   ) || ']' AS product_coll
FROM customer_order_products
GROUP BY customer_id;
```

columns:
"customer_id" int
"customer_name" text
"product_coll" text

all rows:
| column | row 1 | row 2 | row 3 |
|---|---|---|---|
| customer_id | 50042 | 50741 | 51069 |
| customer_name | The White Hart | Hygge og Humle | Der Wichtelmann |
| product_coll | [{ "product_id": 4280, "product_name": "Hoppy Crude Oil" },{ "product_id": 6520, "product_name": "Der Helle Kumpel" },{ "product_id": 4280, "product_name": "Hoppy Crude Oil" },{ "product_id": 4280, "… | [{ "product_id": 4280, "product_name": "Hoppy Crude Oil" },{ "product_id": 6520, "product_name": "Der Helle Kumpel" },{ "product_id": 6520, "product_name": "Der Helle Kumpel" },{ "product_id": 6600,… | [{ "product_id": 4280, "product_name": "Hoppy Crude Oil" },{ "product_id": 6520, "product_name": "Der Helle Kumpel" },{ "product_id": 6600, "product_name": "Hazy Pink Cloud" },{ "product_id": 5310, "… |

# "customer_reviews"  (rows=4)

columns:
"customer_id" int PK FK
"review_list" text

indexes: none

all rows:
| column | row 1 | row 2 | row 3 | row 4 |
|---|---|---|---|---|
| customer_id | 50042 | 50741 | 51007 | 51069 |
| review_list | 4040:A,6600:C,7950:B | 4160:A | null | 4280:B,7790:B |

# "customers"  (rows=4)

columns:
"id" int PK
"name" text NOTNULL

indexes: none

all rows:
| column | row 1 | row 2 | row 3 | row 4 |
|---|---|---|---|---|
| id | 50042 | 50741 | 51007 | 51069 |
| name | The White Hart | Hygge og Humle | Boom Beer Bar | Der Wichtelmann |

# "emp_hire_periods"  (rows=15)

columns:
"emp_id" int PK FK: 143=4, 147=3, 142=2, 144=2, 145=2, 146=2, 142..147
"start_" text PK: "2010-07-01"=3, "2012-04-01"=2, "2014-10-01"=2, "2014-01-01"=1, "2014-02-01"=1, "2014-04-01"=1, "2016-05-01"=1, "2016-06-01"=1, "2016-11-01"=1, "2017-03-01"=1, "2019-02-01"=1
"end_" text: "2012-04-01"=1, "2013-07-01"=1, "2014-01-01"=1, "2015-05-01"=1, "2015-10-01"=1, "2016-02-01"=1, "2016-06-01"=1, "2017-03-01"=1, nulls=7
"title" text NOTNULL: "Product Director"=2, "Warehouse Manager"=2, "Code Tester"=1, "Delivery Manager"=1, "Forklift Operator"=1, "IT Developer"=1, "IT Manager"=1, "IT Technician"=1, "Managing Director"=1, "Operations Chief"=1, "Sales Manager"=1, "Scrum Master"=1, "Sys Admin"=1

indexes: none

samples:
| column | latest | sample | sample |
|---|---|---|---|
| emp_id | 147 | 143 | 147 |
| start_ | 2016-11-01 | 2010-07-01 | 2016-05-01 |
| end_ | null | 2014-01-01 | 2017-03-01 |
| title | Operations Chief | IT Technician | Warehouse Manager |

# "employees"  (rows=14)

columns:
"id" int PK: unique identifier, 142..155
"name" text NOTNULL: "Axel de Proef"=1, "Dan Hoeffler"=1, "Evelyn Smith"=1, "Harold King"=1, "Jim Kronzki"=1, "Kurt Zollman"=1, "Laura Jensen"=1, "Lim Tok Lo"=1, "Maria Juarez"=1, "Mogens Juel"=1, "Simon Chang"=1, "Susanne Hoff"=1, "Ursula Mwbesi"=1, "Zoe Thorston"=1
"title" text NOTNULL: "Forklift Operator"=2, "Bulk Salesman"=1, "IT Developer"=1, "IT Manager"=1, "IT Supporter"=1, "Janitor"=1, "Managing Director"=1, "Operations Chief"=1, "Product Director"=1, "Purchaser"=1, "Retail Salesman"=1, "Sales Manager"=1, "Warehouse Manager"=1
"supervisor_id" int FK: 146=3, 142=2, 143=2, 144=2, 147=2, 151=2, nulls=1, 142..151

indexes: "supervisor_id"

samples:
| column | latest | sample | sample |
|---|---|---|---|
| id | 155 | 142 | 154 |
| name | Susanne Hoff | Harold King | Simon Chang |
| title | Janitor | Managing Director | Retail Salesman |
| supervisor_id | 146 | null | 151 |

# "gender_dim"  (rows=2)

columns:
"letter" text PK
"name" text

indexes: none

all rows:
| column | row 1 | row 2 |
|---|---|---|
| letter | F | M |
| name | Female | Male |

# "inventory"  (rows=113)

columns:
"id" int PK: unique identifier, 1148..1484
"location_id" int NOTNULL FK: unique identifier, 2..252
"product_id" int NOTNULL FK: 4160=17, 7870=14, 7950=13, 5310=12, 5430=12, 4040=11, 6520=11, 7790=11, 4280=6, 6600=6, 4040..7950
"purchase_id" int NOTNULL FK: 62 distinct, 719..780, 729=4, 726=3, 736=3, 746=3, 756=3, 766=3, 719=2, 721=2, 722=2, 724=2
"qty" float NOTNULL: 31 distinct, 3..72, avg=36.2389, median=42

indexes: "location_id", "product_id", "purchase_id"

samples:
| column | latest | sample | sample |
|---|---|---|---|
| id | 1484 | 1172 | 1451 |
| location_id | 245 | 133 | 101 |
| product_id | 7870 | 7790 | 6600 |
| purchase_id | 780 | 724 | 773 |
| qty | 48 | 6 | 8 |

# "inventory_totals"  (rows=10)

```sql
CREATE VIEW inventory_totals AS
SELECT
   i.product_id,
   SUM(i.qty) AS qty
FROM inventory i
GROUP BY i.product_id;
```

columns:
"product_id" int
"qty" float

all rows:
| column | row 1 | row 2 | row 3 | row 4 | row 5 | row 6 | row 7 | row 8 | row 9 | row 10 |
|---|---|---|---|---|---|---|---|---|---|---|
| product_id | 4040 | 4160 | 4280 | 5310 | 5430 | 6520 | 6600 | 7790 | 7870 | 7950 |
| qty | 300 | 700 | 200 | 500 | 500 | 400 | 100 | 300 | 559 | 536 |

# "inventory_with_dims"  (rows=113)

```sql
CREATE VIEW inventory_with_dims AS
SELECT
   i.id,
   i.product_id,
   p.name AS product_name,
   i.purchase_id,
   pu.purchased,
   i.location_id,
   l.warehouse,
   l.aisle,
   l.position,
   i.qty
FROM inventory i
JOIN purchases pu ON pu.id = i.purchase_id
JOIN products p ON p.id = i.product_id
JOIN locations l ON l.id = i.location_id;
```

columns:
"id" int: unique identifier, 1148..1484
"product_id" int: 4160=17, 7870=14, 7950=13, 5310=12, 5430=12, 4040=11, 6520=11, 7790=11, 4280=6, 6600=6, 4040..7950
"product_name" text: "Reindeer Fuel"=17, "Ghost of Hops"=14, "Pale Rider Rides"=13, "Hercule Trippel"=12, "Monks and Nuns"=12, "Coalminers Sweat"=11, "Der Helle Kumpel"=11, "Summer in India"=11, "Hazy Pink Cloud"=6, "Hoppy Crude Oil"=6
"purchase_id" int: 62 distinct, 719..780
"purchased" text: iso-date, 62 distinct
"location_id" int: unique identifier, 2..252
"warehouse" int: 1=57, 2=56
"aisle" text: "C"=30, "A"=29, "D"=29, "B"=25
"position" int: 32 distinct, 1..32, avg=16.6726, median=17
"qty" float: 31 distinct, 3..72, avg=36.2389, median=42

samples:
| column | latest | sample | sample |
|---|---|---|---|
| id | 1484 | 1325 | 1244 |
| product_id | 7870 | 7870 | 4160 |
| product_name | Ghost of Hops | Ghost of Hops | Reindeer Fuel |
| purchase_id | 780 | 750 | 736 |
| purchased | 2018-12-29 | 2018-06-29 | 2018-04-22 |
| location_id | 245 | 246 | 139 |
| warehouse | 2 | 2 | 2 |
| aisle | D | D | A |
| position | 21 | 22 | 11 |
| qty | 48 | 48 | 48 |

# "locations"  (rows=256)

columns:
"id" int PK: unique identifier, 1..256
"warehouse" int NOTNULL: 1=128, 2=128
"aisle" text NOTNULL: "A"=64, "B"=64, "C"=64, "D"=64
"position" int NOTNULL: 32 distinct, 1..32, avg=16.5, median=16.5

indexes: none

samples:
| column | latest | sample | sample |
|---|---|---|---|
| id | 256 | 103 | 64 |
| warehouse | 2 | 1 | 1 |
| aisle | D | D | B |
| position | 32 | 7 | 32 |

# "monthly_budget"  (rows=48)

columns:
"product_id" int PK FK: 6520=24, 6600=24
"mth" text PK: iso-date, 24 distinct
"qty" float NOTNULL: 6=12, 20=12, 30=8, 50=6, 40=4, 45=2, 55=2, 60=2, 6..60

indexes: none

samples:
| column | latest | sample | sample |
|---|---|---|---|
| product_id | 6600 | 6520 | 6600 |
| mth | 2019-12-01 | 2019-01-01 | 2018-02-01 |
| qty | 20 | 45 | 6 |

# "monthly_orders"  (rows=10)

```sql
CREATE VIEW monthly_orders AS
SELECT
   ol.product_id,
   strftime('%Y-%m-01', o.ordered) AS mth,
   SUM(ol.qty) AS qty
FROM orders o
JOIN orderlines ol ON ol.order_id = o.id
GROUP BY ol.product_id, strftime('%Y-%m-01', o.ordered);
```

columns:
"product_id" int
"mth" text
"qty" float

all rows:
| column | row 1 | row 2 | row 3 | row 4 | row 5 | row 6 | row 7 | row 8 | row 9 | row 10 |
|---|---|---|---|---|---|---|---|---|---|---|
| product_id | 4280 | 4280 | 5310 | 5430 | 5430 | 6520 | 6520 | 6600 | 6600 | 7950 |
| mth | 2019-01-01 | 2019-03-01 | 2019-02-01 | 2019-02-01 | 2019-03-01 | 2019-01-01 | 2019-02-01 | 2019-01-01 | 2019-02-01 | 2019-03-01 |
| qty | 250 | 230 | 40 | 60 | 40 | 260 | 40 | 16 | 40 | 150 |

# "monthly_sales"  (rows=360)

columns:
"product_id" int PK FK: 4040=36, 4160=36, 4280=36, 5310=36, 5430=36, 6520=36, 6600=36, 7790=36, 7870=36, 7950=36, 4040..7950
"mth" text PK: iso-date, 36 distinct
"qty" int NOTNULL: 80 distinct, 0..247, avg=28.1778, median=21

indexes: none

samples:
| column | latest | sample | sample |
|---|---|---|---|
| product_id | 7950 | 7870 | 4280 |
| mth | 2018-12-01 | 2016-11-01 | 2018-02-01 |
| qty | 50 | 41 | 13 |

# "orderlines"  (rows=18)

columns:
"id" int PK: unique identifier, 9120..9299
"order_id" int NOTNULL FK: 425=3, 421=2, 422=2, 423=2, 426=2, 428=2, 429=2, 424=1, 427=1, 430=1, 421..430
"product_id" int NOTNULL FK: 4280=6, 6520=4, 6600=3, 5430=2, 7950=2, 5310=1, 4280..7950
"qty" float NOTNULL: 40=4, 60=3, 80=3, 16=2, 24=1, 50=1, 90=1, 100=1, 110=1, 140=1, 16..140
"amount" float NOTNULL: 320=2, 480=2, 1750=2, 650=1, 680=1, 750=1, 875=1, 960=1, 1150=1, 1275=1, 1300=1, 1480=1, 1925=1, 2250=1, 2400=1, 320..2400

indexes: "order_id"

samples:
| column | latest | sample | sample |
|---|---|---|---|
| id | 9299 | 9298 | 9286 |
| order_id | 430 | 429 | 426 |
| product_id | 7950 | 5430 | 6520 |
| qty | 50 | 40 | 40 |
| amount | 480 | 875 | 680 |

# "orders"  (rows=10)

columns:
"id" int PK
"customer_id" int NOTNULL FK
"ordered" text
"delivery" text

indexes: "customer_id"

all rows:
| column | row 1 | row 2 | row 3 | row 4 | row 5 | row 6 | row 7 | row 8 | row 9 | row 10 |
|---|---|---|---|---|---|---|---|---|---|---|
| id | 421 | 422 | 423 | 424 | 425 | 426 | 427 | 428 | 429 | 430 |
| customer_id | 50042 | 51069 | 50741 | 51069 | 51069 | 50741 | 50042 | 50741 | 50042 | 50741 |
| ordered | 2019-01-15 | 2019-01-17 | 2019-01-18 | 2019-01-28 | 2019-02-17 | 2019-02-26 | 2019-03-02 | 2019-03-12 | 2019-03-22 | 2019-03-29 |
| delivery | null | null | null | null | null | null | null | null | null | null |

# "packaging"  (rows=11)

columns:
"id" int PK: unique identifier, 501..534
"name" text NOTNULL: "Bottle 330cl"=1, "Bottle 500cl"=1, "Box Large"=1, "Box Medium"=1, "Box Small"=1, "Gift Box"=1, "Gift Carton"=1, "Pallet Mix MS"=1, "Pallet Mix SG"=1, "Pallet of L"=1, "Pallet of M"=1

indexes: none

samples:
| column | latest | sample | sample |
|---|---|---|---|
| id | 534 | 531 | 523 |
| name | Pallet Mix SG | Pallet of L | Box Small |

# "packaging_relations"  (rows=12)

columns:
"packaging_id" int PK FK: 511=2, 533=2, 534=2, 521=1, 522=1, 523=1, 524=1, 531=1, 532=1, 511..534
"contains_id" int PK FK: 502=3, 501=2, 522=2, 523=2, 511=1, 521=1, 524=1, 501..524
"qty" int NOTNULL: 20=3, 2=1, 3=1, 8=1, 10=1, 12=1, 16=1, 30=1, 36=1, 72=1, 2..72

indexes: "contains_id"

samples:
| column | latest | sample | sample |
|---|---|---|---|
| packaging_id | 534 | 521 | 534 |
| contains_id | 524 | 502 | 524 |
| qty | 16 | 72 | 16 |

# "picking_line"  (rows=21)

columns:
"picklist_id" int PK FK: 842=12, 841=9
"line_no" int PK: 1=2, 2=2, 3=2, 4=2, 5=2, 6=2, 7=2, 8=2, 9=2, 10=1, 11=1, 12=1, 1..12
"location_id" int NOTNULL FK: 163=3, 233=3, 16=2, 29=2, 65=2, 77=2, 114=2, 165=2, 186=2, 212=1, 16..233
"order_id" int NOTNULL FK: 421=9, 422=8, 423=4, 421..423
"product_id" int NOTNULL FK: 6520=13, 4280=8
"qty" float NOTNULL: 14=4, 20=2, 24=2, 30=2, 36=2, 39=2, 5=1, 8=1, 18=1, 22=1, 26=1, 35=1, 42=1, 5..42

indexes: "location_id", "order_id", "product_id"

samples:
| column | latest | sample | sample |
|---|---|---|---|
| picklist_id | 842 | 841 | 842 |
| line_no | 12 | 6 | 11 |
| location_id | 233 | 186 | 233 |
| order_id | 423 | 421 | 422 |
| product_id | 6520 | 6520 | 6520 |
| qty | 18 | 24 | 8 |

# "picking_list"  (rows=2)

columns:
"id" int PK
"created" text NOTNULL
"picker_emp_id" int FK

indexes: "picker_emp_id"

all rows:
| column | row 1 | row 2 |
|---|---|---|
| id | 841 | 842 |
| created | 2019-01-16 14:03:41 | 2019-01-19 15:57:42 |
| picker_emp_id | 149 | 152 |

# "picking_log"  (rows=63)

columns:
"picklist_id" int PK FK: 842=34, 841=29
"log_time" text PK: iso-date, all distinct
"activity" text NOTNULL: "A"=21, "D"=21, "P"=21
"location_id" int FK: 163=7, 233=7, 16=6, 29=6, 65=6, 77=6, 114=6, 165=6, 186=6, 212=3, nulls=4, 16..233
"pickline_no" int: 1=2, 2=2, 3=2, 4=2, 5=2, 6=2, 7=2, 8=2, 9=2, 10=1, 11=1, 12=1, nulls=42, 1..12

indexes: "location_id", ("picklist_id","pickline_no")

samples:
| column | latest | sample | sample |
|---|---|---|---|
| picklist_id | 842 | 842 | 841 |
| log_time | 2019-01-19 16:11:42 | 2019-01-19 16:04:57 | 2019-01-16 14:10:57 |
| activity | A | A | P |
| location_id | null | 114 | 165 |
| pickline_no | null | null | 7 |

# "product_alcohol"  (rows=10)

columns:
"product_id" int PK FK
"sales_volume" float NOTNULL
"abv" float NOTNULL

indexes: none

all rows:
| column | row 1 | row 2 | row 3 | row 4 | row 5 | row 6 | row 7 | row 8 | row 9 | row 10 |
|---|---|---|---|---|---|---|---|---|---|---|
| product_id | 4040 | 4160 | 4280 | 5310 | 5430 | 6520 | 6600 | 7790 | 7870 | 7950 |
| sales_volume | 330 | 500 | 330 | 330 | 330 | 500 | 500 | 500 | 330 | 330 |
| abv | 8.5 | 6 | 7 | 5 | 6.5 | 4.5 | 4 | 5.5 | 4.5 | 5 |

# "product_groups"  (rows=4)

columns:
"id" int PK
"name" text NOTNULL

indexes: none

all rows:
| column | row 1 | row 2 | row 3 | row 4 |
|---|---|---|---|---|
| id | 142 | 152 | 202 | 232 |
| name | Stout | Belgian | Wheat | IPA |

# "product_minimums"  (rows=2)

columns:
"product_id" int PK FK
"qty_minimum" float NOTNULL
"qty_purchase" float NOTNULL

indexes: none

all rows:
| column | row 1 | row 2 |
|---|---|---|
| product_id | 6520 | 6600 |
| qty_minimum | 100 | 30 |
| qty_purchase | 400 | 100 |

# "products"  (rows=10)

columns:
"id" int PK
"name" text NOTNULL
"group_id" int NOTNULL FK

indexes: "group_id"

all rows:
| column | row 1 | row 2 | row 3 | row 4 | row 5 | row 6 | row 7 | row 8 | row 9 | row 10 |
|---|---|---|---|---|---|---|---|---|---|---|
| id | 4040 | 4160 | 4280 | 5310 | 5430 | 6520 | 6600 | 7790 | 7870 | 7950 |
| name | Coalminers Sweat | Reindeer Fuel | Hoppy Crude Oil | Monks and Nuns | Hercule Trippel | Der Helle Kumpel | Hazy Pink Cloud | Summer in India | Ghost of Hops | Pale Rider Rides |
| group_id | 142 | 142 | 142 | 152 | 152 | 202 | 202 | 232 | 232 | 232 |

# "purchases"  (rows=180)

columns:
"id" int PK: unique identifier, 601..780
"purchased" text NOTNULL: iso-date, all distinct
"brewery_id" int NOTNULL FK: 536=72, 518=54, 523=54, 518..536
"product_id" int NOTNULL FK: 4040=18, 4160=18, 4280=18, 5310=18, 5430=18, 6520=18, 6600=18, 7790=18, 7870=18, 7950=18, 4040..7950
"qty" int NOTNULL: 61 distinct, 8..127, avg=62.7778, median=64
"cost" float NOTNULL: 142 distinct, 60..1001, avg=446.222, median=441.5

indexes: "brewery_id", "product_id"

samples:
| column | latest | sample | sample |
|---|---|---|---|
| id | 780 | 706 | 654 |
| purchased | 2018-12-29 | 2017-10-11 | 2016-11-08 |
| brewery_id | 523 | 536 | 523 |
| product_id | 7870 | 4040 | 7790 |
| qty | 54 | 54 | 53 |
| cost | 391 | 316 | 394 |

# "purchases_with_dims"  (rows=180)

```sql
CREATE VIEW purchases_with_dims AS
SELECT
   pu.id,
   pu.purchased,
   pu.brewery_id,
   b.name AS brewery_name,
   pu.product_id,
   p.name AS product_name,
   p.group_id,
   pg.name AS group_name,
   pu.qty,
   pu.cost
FROM purchases pu
JOIN breweries b ON b.id = pu.brewery_id
JOIN products p ON p.id = pu.product_id
JOIN product_groups pg ON pg.id = p.group_id;
```

columns:
"id" int: unique identifier, 601..780
"purchased" text: iso-date, all distinct
"brewery_id" int: 536=72, 518=54, 523=54, 518..536
"brewery_name" text: "Brewing Barbarian"=72, "Balthazar Brauerei"=54, "Happy Hoppy Hippo"=54
"product_id" int: 4040=18, 4160=18, 4280=18, 5310=18, 5430=18, 6520=18, 6600=18, 7790=18, 7870=18, 7950=18, 4040..7950
"product_name" text: "Coalminers Sweat"=18, "Der Helle Kumpel"=18, "Ghost of Hops"=18, "Hazy Pink Cloud"=18, "Hercule Trippel"=18, "Hoppy Crude Oil"=18, "Monks and Nuns"=18, "Pale Rider Rides"=18, "Reindeer Fuel"=18, "Summer in India"=18
"group_id" int: 142=54, 232=54, 152=36, 202=36, 142..232
"group_name" text: "IPA"=54, "Stout"=54, "Belgian"=36, "Wheat"=36
"qty" int: 61 distinct, 8..127, avg=62.7778, median=64
"cost" float: 142 distinct, 60..1001, avg=446.222, median=441.5

samples:
| column | latest | sample | sample |
|---|---|---|---|
| id | 780 | 738 | 616 |
| purchased | 2018-12-29 | 2018-04-25 | 2016-04-02 |
| brewery_id | 523 | 518 | 536 |
| brewery_name | Happy Hoppy Hippo | Balthazar Brauerei | Brewing Barbarian |
| product_id | 7870 | 5430 | 4160 |
| product_name | Ghost of Hops | Hercule Trippel | Reindeer Fuel |
| group_id | 232 | 152 | 142 |
| group_name | IPA | Belgian | Stout |
| qty | 54 | 92 | 72 |
| cost | 391 | 662 | 475 |

# "server_heartbeat"  (rows=14)

columns:
"server" text NOTNULL: "10.0.0.100"=9, "10.0.0.142"=5
"beat_time" text NOTNULL: "2019-04-10 13:00"=2, "2019-04-10 13:20"=2, "2019-04-10 13:55"=2, "2019-04-10 13:05"=1, "2019-04-10 13:10"=1, "2019-04-10 13:15"=1, "2019-04-10 13:25"=1, "2019-04-10 13:35"=1, "2019-04-10 13:40"=1, "2019-04-10 13:45"=1, "2019-04-10 13:50"=1

indexes: none

samples:
| column | latest | sample | sample |
|---|---|---|---|
| server | 10.0.0.142 | 10.0.0.142 | 10.0.0.100 |
| beat_time | 2019-04-10 13:55 | 2019-04-10 13:25 | 2019-04-10 13:45 |

# "stock"  (rows=1)

columns:
"symbol" text PK
"company" text NOTNULL

indexes: none

all rows:
| column | row 1 |
|---|---|
| symbol | BEER |
| company | Good Beer Trading Co |

# "ticker"  (rows=15)

columns:
"symbol" text PK FK: "BEER"=15
"day" text PK: "2019-04-01"=1, "2019-04-02"=1, "2019-04-03"=1, "2019-04-04"=1, "2019-04-05"=1, "2019-04-08"=1, "2019-04-09"=1, "2019-04-10"=1, "2019-04-11"=1, "2019-04-12"=1, "2019-04-15"=1, "2019-04-16"=1, "2019-04-17"=1, "2019-04-18"=1, "2019-04-19"=1
"price" float NOTNULL: 14.2=2, 14.3=2, 14.8=2, 13.7=1, 14=1, 14.4=1, 14.9=1, 15=1, 15.2=1, 15.5=1, 15.6=1, 15.7=1, 13.7..15.7

indexes: none

samples:
| column | latest | sample | sample |
|---|---|---|---|
| symbol | BEER | BEER | BEER |
| day | 2019-04-19 | 2019-04-05 | 2019-04-18 |
| price | 15.5 | 15.6 | 14.3 |

# "total_sales"  (rows=10)

```sql
CREATE VIEW total_sales AS
SELECT
   ms.product_id,
   MAX(p.name) AS product_name,
   SUM(ms.qty) AS total_qty
FROM products p
JOIN monthly_sales ms ON ms.product_id = p.id
GROUP BY ms.product_id;
```

columns:
"product_id" int
"product_name" text
"total_qty" int

all rows:
| column | row 1 | row 2 | row 3 | row 4 | row 5 | row 6 | row 7 | row 8 | row 9 | row 10 |
|---|---|---|---|---|---|---|---|---|---|---|
| product_id | 4040 | 4160 | 4280 | 5310 | 5430 | 6520 | 6600 | 7790 | 7870 | 7950 |
| product_name | Coalminers Sweat | Reindeer Fuel | Hoppy Crude Oil | Monks and Nuns | Hercule Trippel | Der Helle Kumpel | Hazy Pink Cloud | Summer in India | Ghost of Hops | Pale Rider Rides |
| total_qty | 813 | 1604 | 303 | 1485 | 1056 | 1230 | 324 | 961 | 1485 | 883 |

# "web_apps"  (rows=1)

columns:
"id" int PK
"name" text NOTNULL

indexes: none

all rows:
| column | row 1 |
|---|---|
| id | 542 |
| name | Webshop |

# "web_counter_hist"  (rows=120)

columns:
"app_id" int PK: 542=120
"page_no" int PK: 1=30, 2=30, 3=30, 4=30, 1..4
"day" text PK: iso-date, 30 distinct
"counter" int NOTNULL: 112 distinct, 455..7833, avg=3395.19, median=3256

indexes: none

samples:
| column | latest | sample | sample |
|---|---|---|---|
| app_id | 542 | 542 | 542 |
| page_no | 4 | 4 | 3 |
| day | 2019-04-30 | 2019-04-21 | 2019-04-15 |
| counter | 586 | 524 | 2409 |

# "web_demographics"  (rows=2)

columns:
"day" text PK
"m_tw_cnt" int
"m_tw_qty" int
"m_fb_cnt" int
"m_fb_qty" int
"f_tw_cnt" int
"f_tw_qty" int
"f_fb_cnt" int
"f_fb_qty" int

indexes: none

all rows:
| column | row 1 | row 2 |
|---|---|---|
| day | 2019-05-01 | 2019-05-02 |
| m_tw_cnt | 1232 | 1438 |
| m_tw_qty | 86 | 142 |
| m_fb_cnt | 1017 | 1198 |
| m_fb_qty | 64 | 70 |
| f_tw_cnt | 651 | 840 |
| f_tw_qty | 76 | 92 |
| f_fb_cnt | 564 | 752 |
| f_fb_qty | 68 | 78 |

# "web_devices"  (rows=2)

columns:
"day" text PK
"pc" int
"tablet" int
"phone" int

indexes: none

all rows:
| column | row 1 | row 2 |
|---|---|---|
| day | 2019-05-01 | 2019-05-02 |
| pc | 1042 | 967 |
| tablet | 812 | 1102 |
| phone | 1610 | 2159 |

# "web_page_counter_hist"  (rows=120)

```sql
CREATE VIEW web_page_counter_hist AS
SELECT
   ch.app_id,
   a.name AS app_name,
   ch.page_no,
   p.friendly_url,
   ch.day,
   ch.counter
FROM web_apps a
JOIN web_pages p ON p.app_id = a.id
JOIN web_counter_hist ch ON ch.app_id = p.app_id AND ch.page_no = p.page_no;
```

columns:
"app_id" int: 542=120
"app_name" text: "Webshop"=120
"page_no" int: 1=30, 2=30, 3=30, 4=30, 1..4
"friendly_url" text: "/About"=30, "/Breweries"=30, "/Categories"=30, "/Shop"=30
"day" text: iso-date, 30 distinct
"counter" int: 112 distinct, 455..7833, avg=3395.19, median=3256

samples:
| column | latest | sample | sample |
|---|---|---|---|
| app_id | 542 | 542 | 542 |
| app_name | Webshop | Webshop | Webshop |
| page_no | 4 | 3 | 1 |
| friendly_url | /About | /Breweries | /Shop |
| day | 2019-04-30 | 2019-04-13 | 2019-04-18 |
| counter | 586 | 2331 | 7186 |

# "web_page_visits"  (rows=23)

columns:
"client_ip" text NOTNULL: "104.130.89.12"=19, "85.237.86.200"=4
"visit_time" text NOTNULL: iso-date, all distinct
"app_id" int NOTNULL: 542=23
"page_no" int NOTNULL: 2=12, 3=6, 1=3, 4=2, 1..4

indexes: ("app_id","page_no")

samples:
| column | latest | sample | sample |
|---|---|---|---|
| client_ip | 85.237.86.200 | 85.237.86.200 | 104.130.89.12 |
| visit_time | 2019-04-20 12:02:02 | 2019-04-20 12:02:02 | 2019-04-20 15:05:48 |
| app_id | 542 | 542 | 542 |
| page_no | 3 | 3 | 3 |

# "web_pages"  (rows=4)

columns:
"app_id" int PK FK
"page_no" int PK
"friendly_url" text NOTNULL

indexes: none

all rows:
| column | row 1 | row 2 | row 3 | row 4 |
|---|---|---|---|---|
| app_id | 542 | 542 | 542 | 542 |
| page_no | 1 | 2 | 3 | 4 |
| friendly_url | /Shop | /Categories | /Breweries | /About |

# "yearly_sales"  (rows=30)

```sql
CREATE VIEW yearly_sales AS
SELECT
   strftime('%Y', ms.mth) AS yr,
   ms.product_id,
   MAX(p.name) AS product_name,
   SUM(ms.qty) AS yr_qty
FROM products p
JOIN monthly_sales ms ON ms.product_id = p.id
GROUP BY strftime('%Y', ms.mth), ms.product_id;
```

columns:
"yr" text: "2016"=10, "2017"=10, "2018"=10
"product_id" int: 4040=3, 4160=3, 4280=3, 5310=3, 5430=3, 6520=3, 6600=3, 7790=3, 7870=3, 7950=3, 4040..7950
"product_name" text: "Coalminers Sweat"=3, "Der Helle Kumpel"=3, "Ghost of Hops"=3, "Hazy Pink Cloud"=3, "Hercule Trippel"=3, "Hoppy Crude Oil"=3, "Monks and Nuns"=3, "Pale Rider Rides"=3, "Reindeer Fuel"=3, "Summer in India"=3
"yr_qty" int: 28 distinct

samples:
| column | latest | sample | sample |
|---|---|---|---|
| yr | 2018 | 2016 | 2018 |
| product_id | 7950 | 6520 | 4040 |
| product_name | Pale Rider Rides | Der Helle Kumpel | Coalminers Sweat |
| yr_qty | 491 | 415 | 300 |

- Skipped 1 table(s) due to DDL generation errors: "emp_hire_periods_with_name"

- Skipped 5 empty table(s): "conway_gen_zero", "favorite_coll_type", "id_name_coll_entries", "id_name_coll_type", "id_name_type"
