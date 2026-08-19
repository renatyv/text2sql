---
generator: db-snooper
version: 0.0.26
generated_at_utc: 2026-08-16T08:07:37.355540Z
dialect: sqlite
database: /var/folders/9j/b9bx_drd53sc6zbpsqyrjy4h0000gn/T/dbsnoop-ch50fgtf/Airlines.sqlite
schema: main
---

# aircrafts_data

## Rows

- total=9

- (no rows sampled)


# airports_data

```sql
CREATE TABLE airports_data (
    airport_code character(3) NOT NULL,
    airport_name jsonb NOT NULL,
    city jsonb NOT NULL,
    coordinates point NOT NULL,
    timezone text NOT NULL
);
```


# boarding_passes

```sql
CREATE TABLE boarding_passes (
    ticket_no character(13) NOT NULL,
    flight_id integer NOT NULL,
    boarding_no integer NOT NULL,
    seat_no character varying(4) NOT NULL
);
```

## Rows

- total≈579686 (estimated from db stats; row/column profiling skipped)


# bookings

```sql
CREATE TABLE bookings (
    book_ref character(6) NOT NULL,
    book_date timestamp with time zone NOT NULL,
    total_amount numeric(10,2) NOT NULL
);
```

## Rows

- total≈262788 (estimated from db stats; row/column profiling skipped)


# flights

```sql
CREATE TABLE flights (
    flight_id integer NOT NULL,
    flight_no character(6) NOT NULL,
    scheduled_departure timestamp with time zone NOT NULL,
    scheduled_arrival timestamp with time zone NOT NULL,
    departure_airport character(3) NOT NULL,
    arrival_airport character(3) NOT NULL,
    status character varying(20) NOT NULL,
    aircraft_code character(3) NOT NULL,
    actual_departure timestamp with time zone,
    actual_arrival timestamp with time zone
);
```


# seats

```sql
CREATE TABLE seats (
    aircraft_code character(3) NOT NULL,
    seat_no character varying(4) NOT NULL,
    fare_conditions character varying(10) NOT NULL
);
```

## Rows

- total=1339

| column | latest | sample | sample |
|---|---|---|---|
| aircraft_code | SU9 | SU9 | 320 |
| seat_no | 9F | 14A | 20B |
| fare_conditions | Economy | Economy | Economy |

## Columns

- aircraft_code: "773"=402, "763"=222, "321"=170, "320"=140, "733"=130, "319"=116, "SU9"=97, "CR2"=50, "CN1"=12
- seat_no: 461 distinct
- fare_conditions: "Economy"=1139, "Business"=152, "Comfort"=48


# ticket_flights

```sql
CREATE TABLE ticket_flights (
    ticket_no character(13) NOT NULL,
    flight_id integer NOT NULL,
    fare_conditions character varying(10) NOT NULL,
    amount numeric(10,2) NOT NULL
);
```

## Rows

- total≈1045726 (estimated from db stats; row/column profiling skipped)


# tickets

```sql
CREATE TABLE tickets (
    ticket_no character(13) NOT NULL,
    book_ref character(6) NOT NULL,
    passenger_id character varying(20) NOT NULL);
```

## Rows

- total≈366733 (estimated from db stats; row/column profiling skipped)


- Skipped 2 table(s) due to Profile generation errors: airports_data, flights
