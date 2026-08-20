---
generator: db-snooper
version: 0.0.31
generated_at_utc: 2026-08-20T17:26:42.380910Z
dialect: sqlite
database: /var/folders/9j/b9bx_drd53sc6zbpsqyrjy4h0000gn/T/dbsnoop-ouztrf0f/Airlines.sqlite
schema: main
---

# "aircrafts_data"  (rows=9)

columns:
"aircraft_code" text NOTNULL: "319"=1, "320"=1, "321"=1, "733"=1, "763"=1, "773"=1, "CN1"=1, "CR2"=1, "SU9"=1
"model" numeric→text NOTNULL: "{"en": "Airbus A319-100", "ru": "Аэробус A319-100"}"=1, "{"en": "Airbus A320-200", "ru": "Аэробус A320-200"}"=1, "{"en": "Airbus A321-200", "ru": "Аэробус A321-200"}"=1, "{"en": "Boeing 737-300", "ru": "Боинг 737-300"}"=1, "{"en": "Boeing 767-300", "ru": "Боинг 767-300"}"=1, "{"en": "Boeing 777-300", "ru": "Боинг 777-300"}"=1, "{"en": "Bombardier CRJ-200", "ru": "Бомбардье CRJ-200"}"=1, "{"en": "Cessna 208 Caravan", "ru": "Сессна 208 Караван"}"=1, "{"en": "Sukhoi Superjet-100", "ru": "Сухой Суперджет-100"}"=1
"range" int NOTNULL: 1200=1, 2700=1, 3000=1, 4200=1, 5600=1, 5700=1, 6700=1, 7900=1, 11100=1, 1200..11100

indexes: none
fk: none

all rows:
| column | row 1 | row 2 | row 3 | row 4 | row 5 | row 6 | row 7 | row 8 | row 9 |
|---|---|---|---|---|---|---|---|---|---|
| aircraft_code | 319 | 320 | 321 | 733 | 763 | 773 | CN1 | CR2 | SU9 |
| model | {"en": "Airbus A319-100", "ru": "Аэробус A319-100"} | {"en": "Airbus A320-200", "ru": "Аэробус A320-200"} | {"en": "Airbus A321-200", "ru": "Аэробус A321-200"} | {"en": "Boeing 737-300", "ru": "Боинг 737-300"} | {"en": "Boeing 767-300", "ru": "Боинг 767-300"} | {"en": "Boeing 777-300", "ru": "Боинг 777-300"} | {"en": "Cessna 208 Caravan", "ru": "Сессна 208 Караван"} | {"en": "Bombardier CRJ-200", "ru": "Бомбардье CRJ-200"} | {"en": "Sukhoi Superjet-100", "ru": "Сухой Суперджет-100"} |
| range | 6700 | 5700 | 5600 | 4200 | 7900 | 11100 | 1200 | 2700 | 3000 |

# "airports_data"  (rows=104)

columns:
"airport_code" text NOTNULL: all distinct
"airport_name" numeric→text NOTNULL: all distinct
"city" numeric→text NOTNULL: 101 distinct
"coordinates" int→text NOTNULL: all distinct
"timezone" text NOTNULL: "Europe/Moscow"=44, "Asia/Yekaterinburg"=22, "Asia/Krasnoyarsk"=8, "Asia/Irkutsk"=5, "Asia/Yakutsk"=5, "Europe/Samara"=5, "Asia/Vladivostok"=3, "Asia/Novokuznetsk"=2, "Europe/Volgograd"=2, "Asia/Anadyr"=1, "Asia/Chita"=1, "Asia/Kamchatka"=1, "Asia/Magadan"=1, "Asia/Novosibirsk"=1, "Asia/Omsk"=1, "Asia/Sakhalin"=1, "Europe/Kaliningrad"=1

indexes: none
fk: none

samples:
| column | latest | sample | sample |
|---|---|---|---|
| airport_code | YKS | IJK | EGO |
| airport_name | {"en": "Yakutsk Airport", "ru": "Якутск"} | {"en": "Izhevsk Airport", "ru": "Ижевск"} | {"en": "Belgorod International Airport", "ru": "Белгород"} |
| city | {"en": "Yakutsk", "ru": "Якутск"} | {"en": "Izhevsk", "ru": "Ижевск"} | {"en": "Belgorod", "ru": "Белгород"} |
| coordinates | (129.77099609375,62.0932998657226562) | (53.4575004577636719,56.8280982971191406) | (36.5900993347167969,50.643798828125) |
| timezone | Asia/Yakutsk | Europe/Samara | Europe/Moscow |

# "boarding_passes"  (rows=≈579686)

columns:
"ticket_no" text NOTNULL
"flight_id" int NOTNULL
"boarding_no" int NOTNULL
"seat_no" text NOTNULL

indexes: none
fk: none


# "bookings"  (rows=≈262788)

columns:
"book_ref" text NOTNULL
"book_date" numeric NOTNULL
"total_amount" numeric NOTNULL

indexes: none
fk: none


# "flights"  (rows=33121)

columns:
"flight_id" int NOTNULL: unique identifier, 1..33121
"flight_no" text NOTNULL: 710 distinct
"scheduled_departure" numeric→text NOTNULL: 10365 distinct
"scheduled_arrival" numeric→text NOTNULL: 9648 distinct
"departure_airport" text NOTNULL: 104 distinct
"arrival_airport" text NOTNULL: 104 distinct
"status" text NOTNULL: "Arrived"=16707, "Scheduled"=15383, "On Time"=518, "Cancelled"=414, "Departed"=58, "Delayed"=41
"aircraft_code" text NOTNULL: "CN1"=9273, "CR2"=9048, "SU9"=8504, "321"=1952, "733"=1274, "319"=1239, "763"=1221, "773"=610
"actual_departure" numeric→text: 12108 distinct
"actual_arrival" numeric→text: 11851 distinct

indexes: none
fk: none

samples:
| column | latest | sample | sample |
|---|---|---|---|
| flight_id | 33121 | 1675 | 15682 |
| flight_no | PG0063 | PG0095 | PG0153 |
| scheduled_departure | 2017-08-26 19:25:00+03 | 2017-08-09 10:45:00+03 | 2017-09-03 10:05:00+03 |
| scheduled_arrival | 2017-08-26 20:10:00+03 | 2017-08-09 13:00:00+03 | 2017-09-03 12:00:00+03 |
| departure_airport | SKX | DME | MMK |
| arrival_airport | SVO | URJ | SVO |
| status | Scheduled | Arrived | Scheduled |
| aircraft_code | CR2 | SU9 | SU9 |
| actual_departure | \N | 2017-08-09 10:47:00+03 | \N |
| actual_arrival | \N | 2017-08-09 13:01:00+03 | \N |

# "seats"  (rows=1339)

columns:
"aircraft_code" text NOTNULL: "773"=402, "763"=222, "321"=170, "320"=140, "733"=130, "319"=116, "SU9"=97, "CR2"=50, "CN1"=12
"seat_no" text NOTNULL: 461 distinct
"fare_conditions" text NOTNULL: "Economy"=1139, "Business"=152, "Comfort"=48

indexes: none
fk: none

samples:
| column | latest | sample | sample |
|---|---|---|---|
| aircraft_code | SU9 | 763 | 773 |
| seat_no | 9F | 30B | 25C |
| fare_conditions | Economy | Economy | Economy |

# "ticket_flights"  (rows=≈1045726)

columns:
"ticket_no" text NOTNULL
"flight_id" int NOTNULL
"fare_conditions" text NOTNULL
"amount" numeric NOTNULL

indexes: none
fk: none


# "tickets"  (rows=≈366733)

columns:
"ticket_no" text NOTNULL
"book_ref" text NOTNULL
"passenger_id" text NOTNULL

indexes: none
fk: none
