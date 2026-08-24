---
generator: db-snooper
version: 0.0.34
generated_at_utc: 2026-08-24T21:56:56.209456Z
dialect: sqlite
database: /var/folders/9j/b9bx_drd53sc6zbpsqyrjy4h0000gn/T/dbsnoop-ythvxn6w/Airlines.sqlite
schema: main
---

# "aircrafts_data"  (rows=9)

columns:
"aircraft_code" text NOTNULL
"model" numeric→text NOTNULL
"range" int NOTNULL

indexes: none

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

samples:
| column | latest | sample | sample |
|---|---|---|---|
| airport_code | YKS | AER | EGO |
| airport_name | {"en": "Yakutsk Airport", "ru": "Якутск"} | {"en": "Sochi International Airport", "ru": "Сочи"} | {"en": "Belgorod International Airport", "ru": "Белгород"} |
| city | {"en": "Yakutsk", "ru": "Якутск"} | {"en": "Sochi", "ru": "Сочи"} | {"en": "Belgorod", "ru": "Белгород"} |
| coordinates | (129.77099609375,62.0932998657226562) | (39.9566001892089986,43.4499015808110016) | (36.5900993347167969,50.643798828125) |
| timezone | Asia/Yakutsk | Europe/Moscow | Europe/Moscow |

# "boarding_passes"  (rows=≈579686)

columns:
"ticket_no" text NOTNULL
"flight_id" int NOTNULL
"boarding_no" int NOTNULL
"seat_no" text NOTNULL

indexes: none


# "bookings"  (rows=≈262788)

columns:
"book_ref" text NOTNULL
"book_date" numeric NOTNULL
"total_amount" numeric NOTNULL

indexes: none


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

samples:
| column | latest | sample | sample |
|---|---|---|---|
| flight_id | 33121 | 17056 | 10080 |
| flight_no | PG0063 | PG0518 | PG0186 |
| scheduled_departure | 2017-08-26 19:25:00+03 | 2017-08-12 15:30:00+03 | 2017-08-06 13:50:00+03 |
| scheduled_arrival | 2017-08-26 20:10:00+03 | 2017-08-12 16:50:00+03 | 2017-08-06 16:00:00+03 |
| departure_airport | SKX | SCW | OVB |
| arrival_airport | SVO | DME | PEE |
| status | Scheduled | Arrived | Arrived |
| aircraft_code | CR2 | 763 | 319 |
| actual_departure | \N | 2017-08-12 15:33:00+03 | 2017-08-06 13:54:00+03 |
| actual_arrival | \N | 2017-08-12 16:52:00+03 | 2017-08-06 16:03:00+03 |

# "seats"  (rows=1339)

columns:
"aircraft_code" text NOTNULL: "773"=402, "763"=222, "321"=170, "320"=140, "733"=130, "319"=116, "SU9"=97, "CR2"=50, "CN1"=12
"seat_no" text NOTNULL: 461 distinct
"fare_conditions" text NOTNULL: "Economy"=1139, "Business"=152, "Comfort"=48

indexes: none

samples:
| column | latest | sample | sample |
|---|---|---|---|
| aircraft_code | SU9 | 763 | 773 |
| seat_no | 9F | 4A | 49H |
| fare_conditions | Economy | Business | Economy |

# "ticket_flights"  (rows=≈1045726)

columns:
"ticket_no" text NOTNULL
"flight_id" int NOTNULL
"fare_conditions" text NOTNULL
"amount" numeric NOTNULL

indexes: none


# "tickets"  (rows=≈366733)

columns:
"ticket_no" text NOTNULL
"book_ref" text NOTNULL
"passenger_id" text NOTNULL

indexes: none
