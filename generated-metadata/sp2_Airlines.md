# Additional Metadata

## Clarified Semantics

- `aircrafts_data.model` and `airports_data.airport_name` / `city` are JSON blobs with `"en"`/`"ru"` language keys; use JSON extraction (e.g. `->> '$.en'`) to read a single language name.
- `airports_data.coordinates` is a point-style value `(longitude, latitude)` stored as text; longitude first.
- `flights.status` distinguishes operational states: `Arrived`/`Departure`/`On Time` etc. reflect flown segments, while `Scheduled`/`Cancelled`/`Delayed` reflect planned/un-flown ones. `actual_departure`/`actual_arrival` are NULL for non-flown statuses.
- `seats.fare_conditions` are `Economy`, `Comfort`, `Business` (Economy is the majority).
- A `seat_no` is only meaningful together with an `aircraft_code`: each aircraft type has its own cabin layout. `seat_no` values (1A, 2A, …) repeat across different airframes, so `seats` is effectively keyed by `(aircraft_code, seat_no)`.
- Timestamps carry `+03` (or other) UTC offsets and follow `airports_data.timezone`; cross-timezone comparisons may need offset normalization.
- `flights.flight_no` repeats (a route is flown many times over the schedule window); `flight_id` is the unique per-departure identifier.

## Potential Join Strategies

- `seats (aircraft_code, seat_no)` ⇔ `boarding_passes`: join via the airframe that carried the flight — `boarding_passes.flight_id → flights.flight_id`, then `flights.aircraft_code` + `boarding_passes.seat_no` = `seats (aircraft_code, seat_no)`. `seats.fare_conditions` can be compared against `ticket_flights.fare_conditions`. Cardinality caveat: not every sold seat has a boarding pass, and `seat_no` alone is not unique.
- `boarding_passes (ticket_no, flight_id)` ⇔ `ticket_flights (ticket_no, flight_id)`: composite join on both columns; each ticket usually has a boarding pass per flight on its itinerary.
- `ticket_flights` ⇔ `flights` on `flight_id` (amount per flight per ticket; multiple rows per flight). Combine with `flights.status`/`actual_arrival` to split booked vs actually-flown revenue.
- `tickets.book_ref` ⇔ `bookings.book_ref`: many tickets per booking; `bookings.total_amount` should equal the sum of that booking's `ticket_flights.amount` (useful for revenue/consistency checks).
- `tickets`/`ticket_flights` ⇔ `airports_data` via path `flights.departure_airport` / `arrival_airport` = `airports_data.airport_code` for per-routing/per-city traffic and revenue aggregation.
- `flights.aircraft_code` ⇔ `aircrafts_data.aircraft_code` for per-model utilization/range comparisons (e.g. range vs actual route pairing).
- `airports_data.airport_code` self-set: `departure_airport` and `arrival_airport` both reference it; joining a flight to one airport table twice (departure & arrival) is needed for origin↔destination routing aggregates. Blocks flights where origin == destination are degenerate (and any with same city code but different airports).
- Bookings/`book_date` range is ~2017 (samples Aug–Sep 2017); filter on date range to bound non-indexed scans.