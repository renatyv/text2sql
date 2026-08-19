---
generator: db-snooper
version: 0.0.26
generated_at_utc: 2026-08-16T08:09:26.425943Z
dialect: sqlite
database: /var/folders/9j/b9bx_drd53sc6zbpsqyrjy4h0000gn/T/dbsnoop-s545z2r5/oracle_sql.sqlite
schema: main
---

## Relationships

- breweries.id ← purchases.brewery_id
- customers.id ← customer_favorites.customer_id, customer_reviews.customer_id, orders.customer_id
- employees.id ← emp_hire_periods.emp_id, employees.supervisor_id, picking_list.picker_emp_id
- id_name_coll_type.collection_id ← id_name_coll_entries.collection_id
- locations.id ← inventory.location_id, picking_line.location_id, picking_log.location_id
- orders.id ← orderlines.order_id, picking_line.order_id
- packaging.id ← packaging_relations.contains_id, packaging_relations.packaging_id
- picking_line.(picklist_id, line_no) ← picking_log.(picklist_id, pickline_no)
- picking_list.id ← picking_line.picklist_id, picking_log.picklist_id
- product_groups.id ← products.group_id
- products.id ← inventory.product_id, monthly_budget.product_id, monthly_sales.product_id, orderlines.product_id, picking_line.product_id, product_alcohol.product_id, product_minimums.product_id, purchases.product_id
- purchases.id ← inventory.purchase_id
- stock.symbol ← ticker.symbol
- web_apps.id ← web_pages.app_id
- web_pages.(app_id, page_no) ← web_counter_hist.(app_id, page_no), web_page_visits.(app_id, page_no)

# breweries

## All rows

| column | row 1 | row 2 | row 3 |
|---|---|---|---|
| id | 518 | 523 | 536 |
| name | Balthazar Brauerei | Happy Hoppy Hippo | Brewing Barbarian |


# brewery_products

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

## All rows

| column | row 1 | row 2 | row 3 | row 4 | row 5 | row 6 | row 7 | row 8 | row 9 | row 10 |
|---|---|---|---|---|---|---|---|---|---|---|
| brewery_id | 518 | 518 | 518 | 523 | 523 | 523 | 536 | 536 | 536 | 536 |
| brewery_name | Balthazar Brauerei | Balthazar Brauerei | Balthazar Brauerei | Happy Hoppy Hippo | Happy Hoppy Hippo | Happy Hoppy Hippo | Brewing Barbarian | Brewing Barbarian | Brewing Barbarian | Brewing Barbarian |
| product_id | 5310 | 5430 | 6520 | 6600 | 7790 | 7870 | 4040 | 4160 | 4280 | 7950 |
| product_name | Monks and Nuns | Hercule Trippel | Der Helle Kumpel | Hazy Pink Cloud | Summer in India | Ghost of Hops | Coalminers Sweat | Reindeer Fuel | Hoppy Crude Oil | Pale Rider Rides |


# channels_dim

## All rows

| column | row 1 | row 2 |
|---|---|---|
| id | 42 | 44 |
| name | Twitter | Facebook |
| shortcut | tw | fb |


# customer_favorites

## All rows

| column | row 1 | row 2 | row 3 | row 4 |
|---|---|---|---|---|
| customer_id | 50042 | 50741 | 51007 | 51069 |
| favorite_list | 4040,5310 | 5430,7790,7870 | null | 6520 |


# customer_order_products

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

## Rows

- total=18

| column | latest | sample | sample |
|---|---|---|---|
| customer_id | 51069 | 50042 | 50042 |
| customer_name | Der Wichtelmann | The White Hart | The White Hart |
| ordered | 2019-02-17 | 2019-03-22 | 2019-01-15 |
| product_id | 6600 | 4280 | 6520 |
| product_name | Hazy Pink Cloud | Hoppy Crude Oil | Der Helle Kumpel |
| qty | 24 | 80 | 140 |

## Columns

- customer_id: 50741=7, 51069=6, 50042=5, int 50042..51069
- customer_name: "Hygge og Humle"=7, "Der Wichtelmann"=6, "The White Hart"=5
- ordered: "2019-02-17"=3, "2019-01-15"=2, "2019-01-17"=2, "2019-01-18"=2, "2019-02-26"=2, "2019-03-12"=2, "2019-03-22"=2, "2019-01-28"=1, "2019-03-02"=1, "2019-03-29"=1
- product_id: 4280=6, 6520=4, 6600=3, 5430=2, 7950=2, 5310=1, int 4280..7950
- product_name: "Hoppy Crude Oil"=6, "Der Helle Kumpel"=4, "Hazy Pink Cloud"=3, "Hercule Trippel"=2, "Pale Rider Rides"=2, "Monks and Nuns"=1
- qty: 40=4, 60=3, 80=3, 16=2, 24=1, 50=1, 90=1, 100=1, 110=1, 140=1, num 16..140


# customer_order_products_obj

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

## All rows

| column | row 1 | row 2 | row 3 |
|---|---|---|---|
| customer_id | 50042 | 50741 | 51069 |
| customer_name | The White Hart | Hygge og Humle | Der Wichtelmann |
| product_coll | [{ "product_id": 4280, "product_name": "Hoppy Crude Oil" },{ "product_id": 6520, "product_name": "Der Helle Kumpel" },{ "product_id": 4280, "product_name": "Hoppy Crude Oil" },{ "product_id": 4280, "product_name": "Hoppy Crude Oil" },{ "product_id": 5430, "product_name": "Hercule Trippel" }] | [{ "product_id": 4280, "product_name": "Hoppy Crude Oil" },{ "product_id": 6520, "product_name": "Der Helle Kumpel" },{ "product_id": 6520, "product_name": "Der Helle Kumpel" },{ "product_id": 6600, "product_name": "Hazy Pink Cloud" },{ "product_id": 4280, "product_name": "Hoppy Crude Oil" },{ "product_id": 7950, "product_name": "Pale Rider Rides" },{ "product_id": 7950, "product_name": "Pale Rider Rides" }] | [{ "product_id": 4280, "product_name": "Hoppy Crude Oil" },{ "product_id": 6520, "product_name": "Der Helle Kumpel" },{ "product_id": 6600, "product_name": "Hazy Pink Cloud" },{ "product_id": 5310, "product_name": "Monks and Nuns" },{ "product_id": 5430, "product_name": "Hercule Trippel" },{ "product_id": 6600, "product_name": "Hazy Pink Cloud" }] |


# customer_reviews

## All rows

| column | row 1 | row 2 | row 3 | row 4 |
|---|---|---|---|---|
| customer_id | 50042 | 50741 | 51007 | 51069 |
| review_list | 4040:A,6600:C,7950:B | 4160:A | null | 4280:B,7790:B |


# customers

## All rows

| column | row 1 | row 2 | row 3 | row 4 |
|---|---|---|---|---|
| id | 50042 | 50741 | 51007 | 51069 |
| name | The White Hart | Hygge og Humle | Boom Beer Bar | Der Wichtelmann |


# emp_hire_periods

```sql
CREATE TABLE emp_hire_periods (
    emp_id INTEGER NOT NULL,
    start_ TEXT NOT NULL,
    end_ TEXT,
    title TEXT NOT NULL,
    PRIMARY KEY (emp_id, start_),
    FOREIGN KEY (emp_id) REFERENCES employees(id)
);
```

## Rows

- total=15

| column | latest | sample | sample |
|---|---|---|---|
| emp_id | 147 | 142 | 143 |
| start_ | 2016-11-01 | 2010-07-01 | 2016-06-01 |
| end_ | null | 2012-04-01 | null |
| title | Operations Chief | Product Director | IT Manager |

## Columns

- emp_id: 143=4, 147=3, 142=2, 144=2, 145=2, 146=2, int 142..147
- start_: "2010-07-01"=3, "2012-04-01"=2, "2014-10-01"=2, "2014-01-01"=1, "2014-02-01"=1, "2014-04-01"=1, "2016-05-01"=1, "2016-06-01"=1, "2016-11-01"=1, "2017-03-01"=1, "2019-02-01"=1
- end_: "2012-04-01"=1, "2013-07-01"=1, "2014-01-01"=1, "2015-05-01"=1, "2015-10-01"=1, "2016-02-01"=1, "2016-06-01"=1, "2017-03-01"=1, nulls=7
- title: "Product Director"=2, "Warehouse Manager"=2, "Code Tester"=1, "Delivery Manager"=1, "Forklift Operator"=1, "IT Developer"=1, "IT Manager"=1, "IT Technician"=1, "Managing Director"=1, "Operations Chief"=1, "Sales Manager"=1, "Scrum Master"=1, "Sys Admin"=1


# emp_hire_periods_with_name

- emp_hire_periods_with_name: skipped (DDL generation failed: OperationalError: (sqlite3.OperationalError) no such column: ehp.start_date
[SQL: PRAGMA "main".table_xinfo("emp_hire_periods_with_name")]
(Background on this error at: https://sqlalche.me/e/20/e3q8))


# employees

```sql
CREATE TABLE employees (
    id INTEGER PRIMARY KEY,
    name TEXT NOT NULL,
    title TEXT NOT NULL,
    supervisor_id INTEGER,
    FOREIGN KEY (supervisor_id) REFERENCES employees(id)
);
```

## Indexes

- (supervisor_id)

## Rows

- total=14

| column | latest | sample | sample |
|---|---|---|---|
| id | 155 | 150 | 152 |
| name | Susanne Hoff | Laura Jensen | Evelyn Smith |
| title | Janitor | Bulk Salesman | Forklift Operator |
| supervisor_id | 146 | 151 | 146 |

## Columns

- id: unique identifier, int 142..155
- name: "Axel de Proef"=1, "Dan Hoeffler"=1, "Evelyn Smith"=1, "Harold King"=1, "Jim Kronzki"=1, "Kurt Zollman"=1, "Laura Jensen"=1, "Lim Tok Lo"=1, "Maria Juarez"=1, "Mogens Juel"=1, "Simon Chang"=1, "Susanne Hoff"=1, "Ursula Mwbesi"=1, "Zoe Thorston"=1
- title: "Forklift Operator"=2, "Bulk Salesman"=1, "IT Developer"=1, "IT Manager"=1, "IT Supporter"=1, "Janitor"=1, "Managing Director"=1, "Operations Chief"=1, "Product Director"=1, "Purchaser"=1, "Retail Salesman"=1, "Sales Manager"=1, "Warehouse Manager"=1
- supervisor_id: 146=3, 142=2, 143=2, 144=2, 147=2, 151=2, nulls=1, int 142..151


# gender_dim

## All rows

| column | row 1 | row 2 |
|---|---|---|
| letter | F | M |
| name | Female | Male |


# inventory

```sql
CREATE TABLE inventory (
    id INTEGER PRIMARY KEY,
    location_id INTEGER NOT NULL,
    product_id INTEGER NOT NULL,
    purchase_id INTEGER NOT NULL,
    qty REAL NOT NULL,
    FOREIGN KEY (location_id) REFERENCES locations(id),
    FOREIGN KEY (product_id) REFERENCES products(id),
    FOREIGN KEY (purchase_id) REFERENCES purchases(id)
);
```

## Indexes

- (location_id)
- (product_id)
- (purchase_id)

## Rows

- total=113

| column | latest | sample | sample |
|---|---|---|---|
| id | 1484 | 1280 | 1181 |
| location_id | 245 | 164 | 185 |
| product_id | 7870 | 5310 | 7950 |
| purchase_id | 780 | 742 | 725 |
| qty | 48 | 48 | 48 |

## Columns

- id: unique identifier, int 1148..1484
- location_id: unique identifier, int 2..252
- product_id: 4160=17, 7870=14, 7950=13, 5310=12, 5430=12, 4040=11, 6520=11, 7790=11, 4280=6, 6600=6, int 4040..7950
- purchase_id: 62 distinct, int 719..780
  - top_values: 729=4, 726=3, 736=3, 746=3, 756=3, 766=3, 719=2, 721=2, 722=2, 724=2
- qty: 31 distinct, num 3..72
  - stats: average=36.2389, median=42


# inventory_totals

```sql
CREATE VIEW inventory_totals AS
SELECT
   i.product_id,
   SUM(i.qty) AS qty
FROM inventory i
GROUP BY i.product_id;
```

## All rows

| column | row 1 | row 2 | row 3 | row 4 | row 5 | row 6 | row 7 | row 8 | row 9 | row 10 |
|---|---|---|---|---|---|---|---|---|---|---|
| product_id | 4040 | 4160 | 4280 | 5310 | 5430 | 6520 | 6600 | 7790 | 7870 | 7950 |
| qty | 300 | 700 | 200 | 500 | 500 | 400 | 100 | 300 | 559 | 536 |


# inventory_with_dims

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

## Rows

- total=113

| column | latest | sample | sample |
|---|---|---|---|
| id | 1484 | 1382 | 1232 |
| product_id | 7870 | 7870 | 7790 |
| product_name | Ghost of Hops | Ghost of Hops | Summer in India |
| purchase_id | 780 | 760 | 734 |
| purchased | 2018-12-29 | 2018-08-29 | 2018-03-28 |
| location_id | 245 | 39 | 219 |
| warehouse | 2 | 1 | 2 |
| aisle | D | B | C |
| position | 21 | 7 | 27 |
| qty | 48 | 48 | 48 |

## Columns

- id: unique identifier, int 1148..1484
- product_id: 4160=17, 7870=14, 7950=13, 5310=12, 5430=12, 4040=11, 6520=11, 7790=11, 4280=6, 6600=6, int 4040..7950
- product_name: "Reindeer Fuel"=17, "Ghost of Hops"=14, "Pale Rider Rides"=13, "Hercule Trippel"=12, "Monks and Nuns"=12, "Coalminers Sweat"=11, "Der Helle Kumpel"=11, "Summer in India"=11, "Hazy Pink Cloud"=6, "Hoppy Crude Oil"=6
- purchase_id: 62 distinct, int 719..780
- purchased: 62 distinct
- location_id: unique identifier, int 2..252
- warehouse: 1=57, 2=56
- aisle: "C"=30, "A"=29, "D"=29, "B"=25
- position: 32 distinct, int 1..32
  - stats: average=16.6726, median=17
- qty: 31 distinct, num 3..72
  - stats: average=36.2389, median=42


# locations

```sql
CREATE TABLE locations (
    id INTEGER PRIMARY KEY,
    warehouse INTEGER NOT NULL,
    aisle TEXT NOT NULL,
    position INTEGER NOT NULL,
    UNIQUE (warehouse, aisle, position)
);
```

## Rows

- total=256

| column | latest | sample | sample |
|---|---|---|---|
| id | 256 | 2 | 128 |
| warehouse | 2 | 1 | 1 |
| aisle | D | A | D |
| position | 32 | 2 | 32 |

## Columns

- id: unique identifier, int 1..256
- warehouse: 1=128, 2=128
- aisle: "A"=64, "B"=64, "C"=64, "D"=64
- position: 32 distinct, int 1..32
  - stats: average=16.5, median=16.5
  - top_values: 1=8, 2=8, 3=8, 4=8, 5=8, 6=8, 7=8, 8=8, 9=8, 10=8


# monthly_budget

```sql
CREATE TABLE monthly_budget (
    product_id INTEGER NOT NULL,
    mth TEXT NOT NULL,
    qty REAL NOT NULL,
    PRIMARY KEY (product_id, mth),
    FOREIGN KEY (product_id) REFERENCES products(id),
    CHECK (strftime('%d', mth) = '01')
);
```

## Rows

- total=48

| column | latest | sample | sample |
|---|---|---|---|
| product_id | 6600 | 6520 | 6520 |
| mth | 2019-12-01 | 2018-10-01 | 2018-11-01 |
| qty | 20 | 30 | 30 |

## Columns

- product_id: 6520=24, 6600=24
- mth: 24 distinct
  - top_values: "2018-01-01"=2, "2018-02-01"=2, "2018-03-01"=2, "2018-04-01"=2, "2018-05-01"=2, "2018-06-01"=2, "2018-07-01"=2, "2018-08-01"=2, "2018-09-01"=2, "2018-10-01"=2
- qty: 6=12, 20=12, 30=8, 50=6, 40=4, 45=2, 55=2, 60=2, num 6..60


# monthly_orders

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

## All rows

| column | row 1 | row 2 | row 3 | row 4 | row 5 | row 6 | row 7 | row 8 | row 9 | row 10 |
|---|---|---|---|---|---|---|---|---|---|---|
| product_id | 4280 | 4280 | 5310 | 5430 | 5430 | 6520 | 6520 | 6600 | 6600 | 7950 |
| mth | 2019-01-01 | 2019-03-01 | 2019-02-01 | 2019-02-01 | 2019-03-01 | 2019-01-01 | 2019-02-01 | 2019-01-01 | 2019-02-01 | 2019-03-01 |
| qty | 250 | 230 | 40 | 60 | 40 | 260 | 40 | 16 | 40 | 150 |


# monthly_sales

```sql
CREATE TABLE monthly_sales (
    product_id INTEGER NOT NULL,
    mth TEXT NOT NULL,
    qty INTEGER NOT NULL,
    PRIMARY KEY (product_id, mth),
    FOREIGN KEY (product_id) REFERENCES products(id),
    CHECK (strftime('%d', mth) = '01')
);
```

## Rows

- total=360

| column | latest | sample | sample |
|---|---|---|---|
| product_id | 7950 | 4280 | 4040 |
| mth | 2018-12-01 | 2017-01-01 | 2017-04-01 |
| qty | 50 | 9 | 19 |

## Columns

- product_id: 4040=36, 4160=36, 4280=36, 5310=36, 5430=36, 6520=36, 6600=36, 7790=36, 7870=36, 7950=36, int 4040..7950
- mth: 36 distinct
  - top_values: "2016-01-01"=10, "2016-02-01"=10, "2016-03-01"=10, "2016-04-01"=10, "2016-05-01"=10, "2016-06-01"=10, "2016-07-01"=10, "2016-08-01"=10, "2016-09-01"=10, "2016-10-01"=10
- qty: 80 distinct, int 0..247
  - stats: average=28.1778, median=21


# orderlines

```sql
CREATE TABLE orderlines (
    id INTEGER PRIMARY KEY,
    order_id INTEGER NOT NULL,
    product_id INTEGER NOT NULL,
    qty REAL NOT NULL,
    amount REAL NOT NULL,
    FOREIGN KEY (order_id) REFERENCES orders(id),
    FOREIGN KEY (product_id) REFERENCES products(id)
);
```

## Indexes

- (order_id)

## Rows

- total=18

| column | latest | sample | sample |
|---|---|---|---|
| id | 9299 | 9276 | 9286 |
| order_id | 430 | 424 | 426 |
| product_id | 7950 | 6600 | 6520 |
| qty | 50 | 16 | 40 |
| amount | 480 | 320 | 680 |

## Columns

- id: unique identifier, int 9120..9299
- order_id: 425=3, 421=2, 422=2, 423=2, 426=2, 428=2, 429=2, 424=1, 427=1, 430=1, int 421..430
- product_id: 4280=6, 6520=4, 6600=3, 5430=2, 7950=2, 5310=1, int 4280..7950
- qty: 40=4, 60=3, 80=3, 16=2, 24=1, 50=1, 90=1, 100=1, 110=1, 140=1, num 16..140
- amount: 320=2, 480=2, 1750=2, 650=1, 680=1, 750=1, 875=1, 960=1, 1150=1, 1275=1, 1300=1, 1480=1, 1925=1, 2250=1, 2400=1, num 320..2400


# orders

## All rows

| column | row 1 | row 2 | row 3 | row 4 | row 5 | row 6 | row 7 | row 8 | row 9 | row 10 |
|---|---|---|---|---|---|---|---|---|---|---|
| id | 421 | 422 | 423 | 424 | 425 | 426 | 427 | 428 | 429 | 430 |
| customer_id | 50042 | 51069 | 50741 | 51069 | 51069 | 50741 | 50042 | 50741 | 50042 | 50741 |
| ordered | 2019-01-15 | 2019-01-17 | 2019-01-18 | 2019-01-28 | 2019-02-17 | 2019-02-26 | 2019-03-02 | 2019-03-12 | 2019-03-22 | 2019-03-29 |
| delivery | null | null | null | null | null | null | null | null | null | null |


# packaging

```sql
CREATE TABLE packaging (
    id INTEGER PRIMARY KEY,
    name TEXT NOT NULL
);
```

## Rows

- total=11

| column | latest | sample | sample |
|---|---|---|---|
| id | 534 | 533 | 521 |
| name | Pallet Mix SG | Pallet Mix MS | Box Large |

## Columns

- id: unique identifier, int 501..534
- name: "Bottle 330cl"=1, "Bottle 500cl"=1, "Box Large"=1, "Box Medium"=1, "Box Small"=1, "Gift Box"=1, "Gift Carton"=1, "Pallet Mix MS"=1, "Pallet Mix SG"=1, "Pallet of L"=1, "Pallet of M"=1


# packaging_relations

```sql
CREATE TABLE packaging_relations (
    packaging_id INTEGER NOT NULL,
    contains_id INTEGER NOT NULL,
    qty INTEGER NOT NULL,
    PRIMARY KEY (packaging_id, contains_id),
    FOREIGN KEY (packaging_id) REFERENCES packaging(id),
    FOREIGN KEY (contains_id) REFERENCES packaging(id)
);
```

## Indexes

- (contains_id)

## Rows

- total=12

| column | latest | sample | sample |
|---|---|---|---|
| packaging_id | 534 | 511 | 534 |
| contains_id | 524 | 501 | 523 |
| qty | 16 | 3 | 20 |

## Columns

- packaging_id: 511=2, 533=2, 534=2, 521=1, 522=1, 523=1, 524=1, 531=1, 532=1, int 511..534
- contains_id: 502=3, 501=2, 522=2, 523=2, 511=1, 521=1, 524=1, int 501..524
- qty: 20=3, 2=1, 3=1, 8=1, 10=1, 12=1, 16=1, 30=1, 36=1, 72=1, int 2..72


# picking_line

```sql
CREATE TABLE picking_line (
    picklist_id INTEGER NOT NULL,
    line_no INTEGER NOT NULL,
    location_id INTEGER NOT NULL,
    order_id INTEGER NOT NULL,
    product_id INTEGER NOT NULL,
    qty REAL NOT NULL,
    PRIMARY KEY (picklist_id, line_no),
    FOREIGN KEY (picklist_id) REFERENCES picking_list(id),
    FOREIGN KEY (location_id) REFERENCES locations(id),
    FOREIGN KEY (order_id) REFERENCES orders(id),
    FOREIGN KEY (product_id) REFERENCES products(id)
);
```

## Indexes

- (location_id)
- (order_id)
- (product_id)

## Rows

- total=21

| column | latest | sample | sample |
|---|---|---|---|
| picklist_id | 842 | 842 | 842 |
| line_no | 12 | 11 | 5 |
| location_id | 233 | 233 | 114 |
| order_id | 423 | 422 | 422 |
| product_id | 6520 | 6520 | 4280 |
| qty | 18 | 8 | 39 |

## Columns

- picklist_id: 842=12, 841=9
- line_no: 1=2, 2=2, 3=2, 4=2, 5=2, 6=2, 7=2, 8=2, 9=2, 10=1, 11=1, 12=1, int 1..12
- location_id: 163=3, 233=3, 16=2, 29=2, 65=2, 77=2, 114=2, 165=2, 186=2, 212=1, int 16..233
- order_id: 421=9, 422=8, 423=4, int 421..423
- product_id: 6520=13, 4280=8
- qty: 14=4, 20=2, 24=2, 30=2, 36=2, 39=2, 5=1, 8=1, 18=1, 22=1, 26=1, 35=1, 42=1, num 5..42


# picking_list

## All rows

| column | row 1 | row 2 |
|---|---|---|
| id | 841 | 842 |
| created | 2019-01-16 14:03:41 | 2019-01-19 15:57:42 |
| picker_emp_id | 149 | 152 |


# picking_log

```sql
CREATE TABLE picking_log (
    picklist_id INTEGER NOT NULL,
    log_time TEXT NOT NULL,
    activity TEXT NOT NULL CHECK (activity IN ('A', 'P', 'D')),
    location_id INTEGER,
    pickline_no INTEGER,
    PRIMARY KEY (picklist_id, log_time),
    FOREIGN KEY (picklist_id) REFERENCES picking_list(id),
    FOREIGN KEY (location_id) REFERENCES locations(id),
    FOREIGN KEY (picklist_id, pickline_no) REFERENCES picking_line(picklist_id, line_no),
    CHECK (NOT (activity = 'P' AND pickline_no IS NULL))
);
```

## Indexes

- (location_id)
- (picklist_id, pickline_no)

## Rows

- total=63

| column | latest | sample | sample |
|---|---|---|---|
| picklist_id | 842 | 841 | 841 |
| log_time | 2019-01-19 16:11:42 | 2019-01-16 14:10:57 | 2019-01-16 14:11:26 |
| activity | A | P | D |
| location_id | null | 165 | 163 |
| pickline_no | null | 7 | null |

## Columns

- picklist_id: 842=34, 841=29
- log_time: all distinct
- activity: "A"=21, "D"=21, "P"=21
- location_id: 163=7, 233=7, 16=6, 29=6, 65=6, 77=6, 114=6, 165=6, 186=6, 212=3, nulls=4, int 16..233
- pickline_no: 1=2, 2=2, 3=2, 4=2, 5=2, 6=2, 7=2, 8=2, 9=2, 10=1, 11=1, 12=1, nulls=42, int 1..12


# product_alcohol

## All rows

| column | row 1 | row 2 | row 3 | row 4 | row 5 | row 6 | row 7 | row 8 | row 9 | row 10 |
|---|---|---|---|---|---|---|---|---|---|---|
| product_id | 4040 | 4160 | 4280 | 5310 | 5430 | 6520 | 6600 | 7790 | 7870 | 7950 |
| sales_volume | 330 | 500 | 330 | 330 | 330 | 500 | 500 | 500 | 330 | 330 |
| abv | 8.5 | 6 | 7 | 5 | 6.5 | 4.5 | 4 | 5.5 | 4.5 | 5 |


# product_groups

## All rows

| column | row 1 | row 2 | row 3 | row 4 |
|---|---|---|---|---|
| id | 142 | 152 | 202 | 232 |
| name | Stout | Belgian | Wheat | IPA |


# product_minimums

## All rows

| column | row 1 | row 2 |
|---|---|---|
| product_id | 6520 | 6600 |
| qty_minimum | 100 | 30 |
| qty_purchase | 400 | 100 |


# products

## All rows

| column | row 1 | row 2 | row 3 | row 4 | row 5 | row 6 | row 7 | row 8 | row 9 | row 10 |
|---|---|---|---|---|---|---|---|---|---|---|
| id | 4040 | 4160 | 4280 | 5310 | 5430 | 6520 | 6600 | 7790 | 7870 | 7950 |
| name | Coalminers Sweat | Reindeer Fuel | Hoppy Crude Oil | Monks and Nuns | Hercule Trippel | Der Helle Kumpel | Hazy Pink Cloud | Summer in India | Ghost of Hops | Pale Rider Rides |
| group_id | 142 | 142 | 142 | 152 | 152 | 202 | 202 | 232 | 232 | 232 |


# purchases

```sql
CREATE TABLE purchases (
    id INTEGER PRIMARY KEY,
    purchased TEXT NOT NULL,
    brewery_id INTEGER NOT NULL,
    product_id INTEGER NOT NULL,
    qty INTEGER NOT NULL,
    cost REAL NOT NULL,
    FOREIGN KEY (brewery_id) REFERENCES breweries(id),
    FOREIGN KEY (product_id) REFERENCES products(id)
);
```

## Indexes

- (brewery_id)
- (product_id)

## Rows

- total=180

| column | latest | sample | sample |
|---|---|---|---|
| id | 780 | 695 | 644 |
| purchased | 2018-12-29 | 2017-07-18 | 2016-09-08 |
| brewery_id | 523 | 523 | 523 |
| product_id | 7870 | 7790 | 7790 |
| qty | 54 | 68 | 70 |
| cost | 391 | 435 | 518 |

## Columns

- id: unique identifier, int 601..780
- purchased: all distinct
- brewery_id: 536=72, 518=54, 523=54, int 518..536
- product_id: 4040=18, 4160=18, 4280=18, 5310=18, 5430=18, 6520=18, 6600=18, 7790=18, 7870=18, 7950=18, int 4040..7950
- qty: 61 distinct, int 8..127
  - stats: average=62.7778, median=64
- cost: 142 distinct, num 60..1001
  - stats: average=446.222, median=441.5


# purchases_with_dims

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

## Rows

- total=180

| column | latest | sample | sample |
|---|---|---|---|
| id | 780 | 720 | 713 |
| purchased | 2018-12-29 | 2017-12-20 | 2017-11-16 |
| brewery_id | 523 | 536 | 518 |
| brewery_name | Happy Hoppy Hippo | Brewing Barbarian | Balthazar Brauerei |
| product_id | 7870 | 7950 | 6520 |
| product_name | Ghost of Hops | Pale Rider Rides | Der Helle Kumpel |
| group_id | 232 | 232 | 202 |
| group_name | IPA | IPA | Wheat |
| qty | 54 | 36 | 59 |
| cost | 391 | 203 | 427 |

## Columns

- id: unique identifier, int 601..780
- purchased: all distinct
- brewery_id: 536=72, 518=54, 523=54, int 518..536
- brewery_name: "Brewing Barbarian"=72, "Balthazar Brauerei"=54, "Happy Hoppy Hippo"=54
- product_id: 4040=18, 4160=18, 4280=18, 5310=18, 5430=18, 6520=18, 6600=18, 7790=18, 7870=18, 7950=18, int 4040..7950
- product_name: "Coalminers Sweat"=18, "Der Helle Kumpel"=18, "Ghost of Hops"=18, "Hazy Pink Cloud"=18, "Hercule Trippel"=18, "Hoppy Crude Oil"=18, "Monks and Nuns"=18, "Pale Rider Rides"=18, "Reindeer Fuel"=18, "Summer in India"=18
- group_id: 142=54, 232=54, 152=36, 202=36, int 142..232
- group_name: "IPA"=54, "Stout"=54, "Belgian"=36, "Wheat"=36
- qty: 61 distinct, int 8..127
  - stats: average=62.7778, median=64
- cost: 142 distinct, num 60..1001
  - stats: average=446.222, median=441.5


# server_heartbeat

```sql
CREATE TABLE server_heartbeat (
    server TEXT NOT NULL,
    beat_time TEXT NOT NULL,
    UNIQUE (server, beat_time)
);
```

## Rows

- total=14

| column | latest | sample | sample |
|---|---|---|---|
| server | 10.0.0.142 | 10.0.0.142 | 10.0.0.100 |
| beat_time | 2019-04-10 13:55 | 2019-04-10 13:25 | 2019-04-10 13:05 |

## Columns

- server: "10.0.0.100"=9, "10.0.0.142"=5
- beat_time: "2019-04-10 13:00"=2, "2019-04-10 13:20"=2, "2019-04-10 13:55"=2, "2019-04-10 13:05"=1, "2019-04-10 13:10"=1, "2019-04-10 13:15"=1, "2019-04-10 13:25"=1, "2019-04-10 13:35"=1, "2019-04-10 13:40"=1, "2019-04-10 13:45"=1, "2019-04-10 13:50"=1


# stock

## All rows

| column | row 1 |
|---|---|
| symbol | BEER |
| company | Good Beer Trading Co |


# ticker

```sql
CREATE TABLE ticker (
    symbol TEXT NOT NULL,
    day TEXT NOT NULL,
    price REAL NOT NULL,
    PRIMARY KEY (symbol, day),
    FOREIGN KEY (symbol) REFERENCES stock(symbol)
);
```

## Rows

- total=15

| column | latest | sample | sample |
|---|---|---|---|
| symbol | BEER | BEER | BEER |
| day | 2019-04-19 | 2019-04-08 | 2019-04-10 |
| price | 15.5 | 14.8 | 14 |

## Columns

- symbol: "BEER"=15
- day: "2019-04-01"=1, "2019-04-02"=1, "2019-04-03"=1, "2019-04-04"=1, "2019-04-05"=1, "2019-04-08"=1, "2019-04-09"=1, "2019-04-10"=1, "2019-04-11"=1, "2019-04-12"=1, "2019-04-15"=1, "2019-04-16"=1, "2019-04-17"=1, "2019-04-18"=1, "2019-04-19"=1
- price: 14.2=2, 14.3=2, 14.8=2, 13.7=1, 14=1, 14.4=1, 14.9=1, 15=1, 15.2=1, 15.5=1, 15.6=1, 15.7=1, num 13.7..15.7


# total_sales

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

## All rows

| column | row 1 | row 2 | row 3 | row 4 | row 5 | row 6 | row 7 | row 8 | row 9 | row 10 |
|---|---|---|---|---|---|---|---|---|---|---|
| product_id | 4040 | 4160 | 4280 | 5310 | 5430 | 6520 | 6600 | 7790 | 7870 | 7950 |
| product_name | Coalminers Sweat | Reindeer Fuel | Hoppy Crude Oil | Monks and Nuns | Hercule Trippel | Der Helle Kumpel | Hazy Pink Cloud | Summer in India | Ghost of Hops | Pale Rider Rides |
| total_qty | 813 | 1604 | 303 | 1485 | 1056 | 1230 | 324 | 961 | 1485 | 883 |


# web_apps

## All rows

| column | row 1 |
|---|---|
| id | 542 |
| name | Webshop |


# web_counter_hist

```sql
CREATE TABLE web_counter_hist (
    app_id INTEGER NOT NULL,
    page_no INTEGER NOT NULL,
    day TEXT NOT NULL,
    counter INTEGER NOT NULL,
    PRIMARY KEY (app_id, page_no, day),
    FOREIGN KEY (app_id, page_no) REFERENCES web_pages(app_id, page_no)
);
```

## Rows

- total=120

| column | latest | sample | sample |
|---|---|---|---|
| app_id | 542 | 542 | 542 |
| page_no | 4 | 4 | 3 |
| day | 2019-04-30 | 2019-04-11 | 2019-04-19 |
| counter | 586 | 508 | 2692 |

## Columns

- app_id: 542=120
- page_no: 1=30, 2=30, 3=30, 4=30, int 1..4
- day: 30 distinct
  - top_values: "2019-04-01"=4, "2019-04-02"=4, "2019-04-03"=4, "2019-04-04"=4, "2019-04-05"=4, "2019-04-06"=4, "2019-04-07"=4, "2019-04-08"=4, "2019-04-09"=4, "2019-04-10"=4
- counter: 112 distinct, int 455..7833
  - stats: average=3395.19, median=3256


# web_demographics

## All rows

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


# web_devices

## All rows

| column | row 1 | row 2 |
|---|---|---|
| day | 2019-05-01 | 2019-05-02 |
| pc | 1042 | 967 |
| tablet | 812 | 1102 |
| phone | 1610 | 2159 |


# web_page_counter_hist

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

## Rows

- total=120

| column | latest | sample | sample |
|---|---|---|---|
| app_id | 542 | 542 | 542 |
| app_name | Webshop | Webshop | Webshop |
| page_no | 4 | 4 | 1 |
| friendly_url | /About | /About | /Shop |
| day | 2019-04-30 | 2019-04-08 | 2019-04-21 |
| counter | 586 | 501 | 7401 |

## Columns

- app_id: 542=120
- app_name: "Webshop"=120
- page_no: 1=30, 2=30, 3=30, 4=30, int 1..4
- friendly_url: "/About"=30, "/Breweries"=30, "/Categories"=30, "/Shop"=30
- day: 30 distinct
- counter: 112 distinct, int 455..7833
  - stats: average=3395.19, median=3256


# web_page_visits

```sql
CREATE TABLE web_page_visits (
    client_ip TEXT NOT NULL,
    visit_time TEXT NOT NULL,
    app_id INTEGER NOT NULL,
    page_no INTEGER NOT NULL,
    FOREIGN KEY (app_id, page_no) REFERENCES web_pages(app_id, page_no)
);
```

## Indexes

- (app_id, page_no)

## Rows

- total=23

| column | latest | sample | sample |
|---|---|---|---|
| client_ip | 85.237.86.200 | 104.130.89.12 | 104.130.89.12 |
| visit_time | 2019-04-20 12:02:02 | 2019-04-20 08:42:37 | 2019-04-20 14:45:10 |
| app_id | 542 | 542 | 542 |
| page_no | 3 | 2 | 1 |

## Columns

- client_ip: "104.130.89.12"=19, "85.237.86.200"=4
- visit_time: all distinct
- app_id: 542=23
- page_no: 2=12, 3=6, 1=3, 4=2, int 1..4


# web_pages

## All rows

| column | row 1 | row 2 | row 3 | row 4 |
|---|---|---|---|---|
| app_id | 542 | 542 | 542 | 542 |
| page_no | 1 | 2 | 3 | 4 |
| friendly_url | /Shop | /Categories | /Breweries | /About |


# yearly_sales

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

## Rows

- total=30

| column | latest | sample | sample |
|---|---|---|---|
| yr | 2018 | 2018 | 2018 |
| product_id | 7950 | 4160 | 6600 |
| product_name | Pale Rider Rides | Reindeer Fuel | Hazy Pink Cloud |
| yr_qty | 491 | 691 | 98 |

## Columns

- yr: "2016"=10, "2017"=10, "2018"=10
- product_id: 4040=3, 4160=3, 4280=3, 5310=3, 5430=3, 6520=3, 6600=3, 7790=3, 7870=3, 7950=3, int 4040..7950
- product_name: "Coalminers Sweat"=3, "Der Helle Kumpel"=3, "Ghost of Hops"=3, "Hazy Pink Cloud"=3, "Hercule Trippel"=3, "Hoppy Crude Oil"=3, "Monks and Nuns"=3, "Pale Rider Rides"=3, "Reindeer Fuel"=3, "Summer in India"=3
- yr_qty: 28 distinct


- Skipped 1 table(s) due to DDL generation errors: emp_hire_periods_with_name

- Skipped 5 empty table(s): conway_gen_zero, favorite_coll_type, id_name_coll_entries, id_name_coll_type, id_name_type
