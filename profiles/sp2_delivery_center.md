---
generator: db-snooper
version: 0.0.26
generated_at_utc: 2026-08-16T08:09:19.932189Z
dialect: sqlite
database: /var/folders/9j/b9bx_drd53sc6zbpsqyrjy4h0000gn/T/dbsnoop-x2eo3p77/delivery_center.sqlite
schema: main
---

# channels

```sql
CREATE TABLE channels (
        channel_id INTEGER PRIMARY KEY,
        channel_name VARCHAR(50),
        channel_type VARCHAR(50)
    );
```

## Rows

- total=40

| column | latest | sample | sample |
|---|---|---|---|
| channel_id | 49 | 9 | 15 |
| channel_name | RIBA PLACE | THINK PLACE | EATS PLACE |
| channel_type | OWN CHANNEL | OWN CHANNEL | MARKETPLACE |

## Columns

- channel_id: unique identifier, int 1..49
- channel_name: all distinct
- channel_type: "MARKETPLACE"=26, "OWN CHANNEL"=14


# deliveries

```sql
CREATE TABLE deliveries (
        delivery_id INTEGER PRIMARY KEY,
        delivery_order_id INTEGER,
        driver_id INTEGER NULL,
        delivery_distance_meters DECIMAL(10, 2),
        delivery_status VARCHAR(50)
    );
```

## Rows

- total≈378843 (estimated from db stats; row/column profiling skipped)


# drivers

```sql
CREATE TABLE drivers (
        driver_id INTEGER PRIMARY KEY,
        driver_modal VARCHAR(50),
        driver_type VARCHAR(50)
    );
```

## Rows

- total=4824

| column | latest | sample | sample |
|---|---|---|---|
| driver_id | 66494 | 12716 | 15528 |
| driver_modal | MOTOBOY | MOTOBOY | BIKER |
| driver_type | FREELANCE | FREELANCE | FREELANCE |

## Columns

- driver_id: unique identifier, int 133..66494
- driver_modal: "MOTOBOY"=3222, "BIKER"=1602
- driver_type: "FREELANCE"=3939, "LOGISTIC OPERATOR"=885


# hubs

```sql
CREATE TABLE hubs (
        hub_id INTEGER PRIMARY KEY,
        hub_name VARCHAR(50),
        hub_city VARCHAR(50),
        hub_state CHAR(2),
        hub_latitude DECIMAL(9, 6),
        hub_longitude DECIMAL(9, 6)
    );
```

## Rows

- total=32

| column | latest | sample | sample |
|---|---|---|---|
| hub_id | 91 | 16 | 42 |
| hub_name | GAROA SHOPPING | PEOPLE SHOPPING | PHP SHOPPING |
| hub_city | SÃO PAULO | RIO DE JANEIRO | CURITIBA |
| hub_state | SP | RJ | PR |
| hub_latitude | -23.525124 | -23.017472 | -25.438105 |
| hub_longitude | -46.546807 | -43.479939 | -49.266532 |

## Columns

- hub_id: unique identifier, int 2..91
- hub_name: all distinct
- hub_city: "SÃO PAULO"=15, "RIO DE JANEIRO"=9, "CURITIBA"=4, "PORTO ALEGRE"=4
- hub_state: "SP"=15, "RJ"=9, "PR"=4, "RS"=4
- hub_latitude: all distinct, num -30.085743..-22.885820
  - stats: average=-24.4207, median=-23.5557
- hub_longitude: all distinct, num -51.245997..-43.182181
  - stats: average=-46.5115, median=-46.6303


# orders

```sql
CREATE TABLE orders (
        order_id INTEGER PRIMARY KEY,
        store_id INTEGER,
        channel_id INTEGER,
        payment_order_id INTEGER,
        delivery_order_id INTEGER,
        order_status VARCHAR(50),
        order_amount DECIMAL(10, 2),
        order_delivery_fee DECIMAL(10, 2),
        order_delivery_cost DECIMAL(10, 2),
        order_created_hour INTEGER,
        order_created_minute INTEGER,
        order_created_day INTEGER,
        order_created_month INTEGER,
        order_created_year INTEGER,
        order_moment_created DATETIME,
        order_moment_accepted DATETIME,
        order_moment_ready DATETIME,
        order_moment_collected DATETIME,
        order_moment_in_expedition DATETIME,
        order_moment_delivering DATETIME,
        order_moment_delivered DATETIME,
        order_moment_finished DATETIME,
        order_metric_collected_time DECIMAL(10, 2),
        order_metric_paused_time DECIMAL(10, 2),
        order_metric_production_time DECIMAL(10, 2),
        order_metric_walking_time DECIMAL(10, 2),
        order_metric_expediton_speed_time DECIMAL(10, 2),
        order_metric_transit_time DECIMAL(10, 2),
        order_metric_cycle_time DECIMAL(10, 2)
    );
```

## Rows

- total≈368999 (estimated from db stats; row/column profiling skipped)


# payments

```sql
CREATE TABLE payments (
        payment_id INTEGER PRIMARY KEY,
        payment_order_id INTEGER,
        payment_amount DECIMAL(10, 2),
        payment_fee DECIMAL(10, 2),
        payment_method VARCHAR(50),
        payment_status VARCHAR(50)
    );
```

## Rows

- total≈400834 (estimated from db stats; row/column profiling skipped)


# stores

```sql
CREATE TABLE stores (
        store_id INTEGER PRIMARY KEY,
        hub_id INTEGER,
        store_name VARCHAR(50),
        store_segment VARCHAR(50),
        store_plan_price DECIMAL(10, 2),
        store_latitude DECIMAL(9, 6),
        store_longitude DECIMAL(9, 6)
    );
```

## Rows

- total=951

| column | latest | sample | sample |
|---|---|---|---|
| store_id | 4679 | 1792 | 3641 |
| hub_id | 85 | 36 | 13 |
| store_name | PIGUE PIPACO  | ASASS  | MRUS GIROUS  |
| store_segment | FOOD | FOOD | FOOD |
| store_plan_price | 49.90 | 49.00 | 49.00 |
| store_latitude | -23.513353 | -30.085743 | -22.887521 |
| store_longitude | -46.618490 | -51.245997 | -43.283366 |

## Columns

- store_id: unique identifier, int 3..4679
- hub_id: 32 distinct, int 2..91
- store_name: 480 distinct
- store_segment: "GOOD"=567, "FOOD"=384
- store_plan_price: 29.00=252, 29.90=177, 49.00=173, 49.90=159, 0.00=62, 1.00=7, 0.01=3, 19.90=1, 29.29=1, 39.00=1, nulls=115, num 0.00..49.90
- store_latitude: 92 distinct, nulls=16, num -30.085743..-19.875356
  - stats: average=-23.8864, median=-23.5611
- store_longitude: 87 distinct, nulls=16, num -51.245997..-43.176536
  - stats: average=-46.0429, median=-46.6185
