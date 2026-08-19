---
generator: db-snooper
version: 0.0.26
generated_at_utc: 2026-08-16T08:07:42.521179Z
dialect: sqlite
database: /var/folders/9j/b9bx_drd53sc6zbpsqyrjy4h0000gn/T/dbsnoop-nsnkhs7v/California_Traffic_Collision.sqlite
schema: main
---

# case_ids

```sql
CREATE TABLE "case_ids" (
"case_id" REAL,
  "db_year" INTEGER
);
```

## Rows

- total=94243

| column | latest | sample | sample |
|---|---|---|---|
| case_id | 9.87001e+18 | 9.52501e+18 | 5.17539e+06 |
| db_year | 2018 | 2018 | 2021 |

## Columns

- case_id: 94242 distinct, num 45..9.87001e+18
- db_year: 2021=52813, 2018=36903, 2020=4526, 2017=1, int 2017..2021


# collisions

```sql
CREATE TABLE "collisions" (
"case_id" REAL,
  "jurisdiction" REAL,
  "officer_id" TEXT,
  "reporting_district" TEXT,
  "chp_shift" TEXT,
  "population" TEXT,
  "county_city_location" INTEGER,
  "county_location" TEXT,
  "special_condition" REAL,
  "beat_type" TEXT,
  "chp_beat_type" TEXT,
  "city_division_lapd" TEXT,
  "chp_beat_class" TEXT,
  "beat_number" TEXT,
  "primary_road" TEXT,
  "secondary_road" TEXT,
  "distance" REAL,
  "direction" TEXT,
  "intersection" REAL,
  "weather_1" TEXT,
  "weather_2" TEXT,
  "state_highway_indicator" REAL,
  "caltrans_county" TEXT,
  "caltrans_district" REAL,
  "state_route" REAL,
  "route_suffix" TEXT,
  "postmile_prefix" TEXT,
  "postmile" REAL,
  "location_type" TEXT,
  "ramp_intersection" TEXT,
  "side_of_highway" TEXT,
  "tow_away" REAL,
  "collision_severity" TEXT,
  "killed_victims" REAL,
  "injured_victims" REAL,
  "party_count" REAL,
  "primary_collision_factor" TEXT,
  "pcf_violation_code" TEXT,
  "pcf_violation_category" TEXT,
  "pcf_violation" REAL,
  "pcf_violation_subsection" TEXT,
  "hit_and_run" TEXT,
  "type_of_collision" TEXT,
  "motor_vehicle_involved_with" TEXT,
  "pedestrian_action" TEXT,
  "road_surface" TEXT,
  "road_condition_1" TEXT,
  "road_condition_2" TEXT,
  "lighting" TEXT,
  "control_device" TEXT,
  "chp_road_type" TEXT,
  "pedestrian_collision" INTEGER,
  "bicycle_collision" INTEGER,
  "motorcycle_collision" INTEGER,
  "truck_collision" INTEGER,
  "not_private_property" REAL,
  "alcohol_involved" REAL,
  "statewide_vehicle_type_at_fault" TEXT,
  "chp_vehicle_type_at_fault" TEXT,
  "severe_injury_count" INTEGER,
  "other_visible_injury_count" INTEGER,
  "complaint_of_pain_injury_count" INTEGER,
  "pedestrian_killed_count" INTEGER,
  "pedestrian_injured_count" INTEGER,
  "bicyclist_killed_count" INTEGER,
  "bicyclist_injured_count" INTEGER,
  "motorcyclist_killed_count" INTEGER,
  "motorcyclist_injured_count" REAL,
  "primary_ramp" TEXT,
  "secondary_ramp" TEXT,
  "latitude" REAL,
  "longitude" REAL,
  "collision_date" TEXT,
  "collision_time" TEXT,
  "process_date" TEXT
);
```

## Rows

- total=94243

| column | latest | sample | sample |
|---|---|---|---|
| case_id | 9.87001e+18 | 4.29832e+06 | 1.14114e+06 |
| jurisdiction | 9870 | 9435 | 1942 |
| officer_id | 16011 | 15026 | 31448 |
| reporting_district | 0 | null | null |
| chp_shift | 0600 thru 1359 | 1400 thru 2159 | not chp |
| population | unincorporated | >250000 | >250000 |
| county_city_location | 3600 | 1005 | 1942 |
| county_location | san bernardino | fresno | los angeles |
| special_condition | null | 0 | 0 |
| beat_type | chp state highway | chp state highway | not chp |
| chp_beat_type | state route | state route | not chp |
| city_division_lapd | null | null | null |
| chp_beat_class | chp primary | chp other | not chp |
| beat_number | 031 | 105 | 0W3 |
| primary_road | RT 62 | RT 99 | 23RD ST |
| secondary_road | JUNIPER RD | HERNDON AV | HARCOURT AV |
| distance | 267 | 2640 | 75 |
| direction | east | south | west |
| intersection | 0 | 0 | 0 |
| weather_1 | clear | clear | clear |
| weather_2 | null | null | null |
| state_highway_indicator | 1 | 1 | 0 |
| caltrans_county | san bernardino | fresno | null |
| caltrans_district | 8 | 6 | null |
| state_route | 62 | 99 | null |
| route_suffix | B | null | null |
| postmile_prefix | B | null | null |
| postmile | 17.32 | 30.49 | null |
| location_type | highway | highway | null |
| ramp_intersection | highway | null | null |
| side_of_highway | eastbound | southbound | null |
| tow_away | 1 | 1 | 1 |
| collision_severity | property damage only | pain | property damage only |
| killed_victims | 0 | 0 | 0 |
| injured_victims | 0 | 2 | 0 |
| party_count | 2 | 3 | 1 |
| primary_collision_factor | vehicle code violation | vehicle code violation | vehicle code violation |
| pcf_violation_code | vehicle | null | null |
| pcf_violation_category | automobile right of way | speeding | speeding |
| pcf_violation | 21801 | 22350 | 22350 |
| pcf_violation_subsection | A | null | null |
| hit_and_run | not hit and run | not hit and run | misdemeanor |
| type_of_collision | broadside | rear end | hit object |
| motor_vehicle_involved_with | other motor vehicle | other motor vehicle | fixed object |
| pedestrian_action | no pedestrian involved | no pedestrian involved | no pedestrian involved |
| road_surface | dry | dry | dry |
| road_condition_1 | normal | normal | normal |
| road_condition_2 | null | null | null |
| lighting | daylight | daylight | dark with street lights |
| control_device | none | none | none |
| chp_road_type | 0 | 1 | 0 |
| pedestrian_collision | 0 | 0 | 0 |
| bicycle_collision | 0 | 0 | 0 |
| motorcycle_collision | 0 | 0 | 0 |
| truck_collision | 0 | 0 | 0 |
| not_private_property | 1 | 1 | 1 |
| alcohol_involved | null | null | null |
| statewide_vehicle_type_at_fault | passenger car | passenger car | null |
| chp_vehicle_type_at_fault | passenger car, station | passenger car, station | null |
| severe_injury_count | 0 | 0 | 0 |
| other_visible_injury_count | 0 | 0 | 0 |
| complaint_of_pain_injury_count | 0 | 2 | 0 |
| pedestrian_killed_count | 0 | 0 | 0 |
| pedestrian_injured_count | 0 | 0 | 0 |
| bicyclist_killed_count | 0 | 0 | 0 |
| bicyclist_injured_count | 0 | 0 | 0 |
| motorcyclist_killed_count | 0 | 0 | 0 |
| motorcyclist_injured_count | 0 | 0 | 0 |
| primary_ramp | null | null | null |
| secondary_ramp | null | null | null |
| latitude | null | null | null |
| longitude | null | null | null |
| collision_date | 2001-11-06 | 2009-06-17 | 2003-11-26 |
| collision_time | 10:00:00 | 15:40:00 | 20:30:00 |
| process_date | 2002-04-04 | 2010-03-16 | 2004-01-06 |

## Columns

- case_id: unique identifier, num 11..9.87001e+18
- jurisdiction: 467 distinct, nulls=121, num 100..9870
  - stats: average=5867.06, median=4807
- officer_id: 30277 distinct, nulls=209
- reporting_district: 6259 distinct, nulls=55424
- chp_shift: "not chp"=50956, "1400 thru 2159"=19812, "0600 thru 1359"=16394, "2200 thru 0559"=6799, "chp not stated"=282
- population: ">250000"=23436, "unincorporated"=22095, "100000 to 250000"=17700, "50000 to 100000"=16957, "25000 to 50000"=8438, "10000 to 25000"=3846, "2500 to 10000"=1297, "<2500"=455, nulls=19
- county_city_location: 525 distinct, int 100..5802
  - stats: average=2789.71, median=3001
- county_location: 58 distinct
- special_condition: 0=88670, 1=377, nulls=5196
- beat_type: "not chp"=50956, "chp state highway"=30446, "chp county roadarea"=8124, "chp county roadline"=4479, "schoolbus on city roadway"=238
- chp_beat_type: "not chp"=50956, "interstate"=15291, "state route"=11474, "county road area"=8133, "county road line"=4390, "us highway"=3638, "safety services program"=340, "administrative"=21
- city_division_lapd: "L"=464, "J"=411, "Q"=409, "O"=401, "G"=381, "C"=363, "I"=363, "M"=363, "K"=355, "N"=345, "H"=315, "F"=307, "P"=300, "B"=291, "R"=290, "A"=261, "D"=231, "E"=226, nulls=88167
- chp_beat_class: "not chp"=50956, "chp other"=36378, "chp primary"=6883, nulls=26
- beat_number: 5049 distinct, nulls=8075
- primary_road: 21661 distinct
- secondary_road: 33560 distinct, nulls=1
- distance: 2121 distinct, num 0..5.57568e+06
  - stats: average=716.122, median=100
- direction: "south"=19444, "north"=19178, "east"=16095, "west"=15960, nulls=23566
- intersection: 0=71354, 1=21947, nulls=942
- weather_1: "clear"=77489, "cloudy"=12330, "raining"=3301, "fog"=389, "snowing"=134, "other"=98, "wind"=33, nulls=469
- weather_2: "raining"=1963, "wind"=270, "cloudy"=175, "other"=83, "snowing"=70, "fog"=66, nulls=91616
- state_highway_indicator: 0=58953, 1=35261, nulls=29
- caltrans_county: 58 distinct, nulls=68771
- caltrans_district: 7=7147, 4=5082, 0=3329, 8=3093, 12=2312, 11=1803, 3=1589, 6=1366, 5=1188, 10=1096, 1=362, 2=362, 9=72, nulls=65442, num 0..12
- state_route: 227 distinct, nulls=65442, num 0..980
  - stats: average=129.129, median=78
- route_suffix: "B"=1898, "S"=60, "U"=26, nulls=92259
- postmile_prefix: "R"=7126, "B"=1324, "M"=349, "L"=135, "T"=126, "S"=17, "C"=4, "D"=4, "H"=1, "N"=1, nulls=85156
- postmile: 8755 distinct, nulls=65442, num 0..608.611
  - stats: average=17.7815, median=13
- location_type: "highway"=20125, "ramp"=3743, "intersection"=1604, nulls=68771
- ramp_intersection: "not state highway"=3329, "highway"=1519, "not state highway, ramp-related, within 100 feet"=1337, "intersection"=1217, "mid-ramp"=1120, "ramp exit, last 50 feet"=1093, "not state highway, intersection-related, within 250 feet"=386, "ramp entry, first 50 feet"=193, nulls=84049
- side_of_highway: "northbound"=7973, "southbound"=7925, "westbound"=4823, "eastbound"=4751, nulls=68771
- tow_away: 1=47305, 0=46270, nulls=668
- collision_severity: "property damage only"=57175, "pain"=22565, "other injury"=11660, "severe injury"=2213, "fatal"=630
- killed_victims: 0=93590, 1=584, 2=34, 3=8, 4=3, 13=1, nulls=23, num 0..13
- injured_victims: 0=57534, 1=26114, 2=7180, 3=2204, 4=750, 5=270, 6=108, 7=24, 8=22, 9=7, 16=2, 10=1, 11=1, 20=1, 21=1, 31=1, nulls=23, num 0..31
- party_count: 2=64165, 1=17768, 3=9676, 4=2031, 5=443, 6=112, 7=30, 8=11, 10=4, 9=3, num 1..10
- primary_collision_factor: "vehicle code violation"=88339, "unknown"=2562, "other than driver"=2002, "other improper driving"=685, "fell asleep"=91, nulls=564
- pcf_violation_code: "vehicle"=4813, "A"=5, "city ordinance"=4, "'"=1, "D"=1, nulls=89419
- pcf_violation_category: 23 distinct, nulls=1602
- pcf_violation: 193 distinct, nulls=6595, num 0..83123
  - stats: average=22040.3, median=22107
- pcf_violation_subsection: "A"=31496, "B"=1165, "1"=377, "C"=302, "D"=228, "F"=125, "5"=77, "E"=66, "G"=31, "I"=16, "2"=4, "3"=3, "H"=1, nulls=60352
- hit_and_run: "not hit and run"=75820, "misdemeanor"=15810, "felony"=2613
- type_of_collision: "rear end"=30895, "broadside"=18510, "sideswipe"=16962, "hit object"=15334, "head-on"=4102, "other"=2647, "overturned"=2526, "pedestrian"=2501, nulls=766
- motor_vehicle_involved_with: "other motor vehicle"=61336, "fixed object"=14717, "parked motor vehicle"=7071, "pedestrian"=2677, "non-collision"=2605, "bicycle"=2299, "other object"=1912, "motor vehicle on other roadway"=663, "animal"=435, "train"=26, "2"=2, nulls=500
- pedestrian_action: "no pedestrian involved"=91454, "crossing in intersection crosswalk"=1184, "crossing not in crosswalk"=770, "in road"=501, "not in road"=210, "crossing non-intersection crosswalk"=62, "using school bus"=3, nulls=59
- road_surface: "dry"=85050, "wet"=7790, "snowy"=430, "slippery"=103, "H"=2, nulls=868
- road_condition_1: "normal"=90556, "construction"=1475, "other"=396, "obstruction"=377, "holes"=270, "loose material"=182, "reduced width"=95, "flooded"=58, nulls=834
- road_condition_2: "normal"=173, "reduced width"=142, "construction"=24, "other"=19, "obstruction"=6, "flooded"=4, "loose material"=3, "holes"=2, nulls=93870
- lighting: "daylight"=62901, "dark with street lights"=19652, "dark with no street lights"=7551, "dusk or dawn"=3386, "dark with street lights not functioning"=185, nulls=568
- control_device: "none"=62402, "functioning"=30907, "not functioning"=282, "obscured"=63, nulls=589
- chp_road_type: "0"=76425, "1"=15503, "6"=1137, "5"=841, "0.0"=147, "4"=131, "3"=23, "1.0"=16, "7"=13, "2"=5, "6.0"=2
- pedestrian_collision: 0=91445, 1=2798
- bicycle_collision: 0=91652, 1=2591
- motorcycle_collision: 0=91447, 1=2796
- truck_collision: 0=88738, 1=5505
- not_private_property: 1=94243
- alcohol_involved: 1=9411, nulls=84832
- statewide_vehicle_type_at_fault: "passenger car"=56217, "pickup or panel truck"=10660, "motorcycle or scooter"=1586, "truck or truck tractor with trailer"=1487, "bicycle"=1435, "truck or truck tractor"=1110, "pedestrian"=920, "emergency vehicle"=474, "pickup or panel truck with trailer"=460, "other vehicle"=326, "other bus"=297, "schoolbus"=187, "passenger car with trailer"=146, "highway construction equipment"=19, "moped"=9, nulls=18910
- chp_vehicle_type_at_fault: 76 distinct, nulls=25444
- severe_injury_count: 0=91919, 1=2100, 2=176, 3=31, 4=14, 5=1, 8=1, 10=1, int 0..10
- other_visible_injury_count: 0=82030, 1=10641, 2=1256, 3=227, 4=66, 5=11, 6=7, 7=3, 13=1, 20=1, int 0..20
- complaint_of_pain_injury_count: 0=68314, 1=18964, 2=5046, 3=1312, 4=408, 5=129, 6=46, 7=11, 8=7, 9=5, 20=1, int 0..20
- pedestrian_killed_count: 0=94090, 1=151, 2=1, 3=1, int 0..3
- pedestrian_injured_count: 0=91713, 1=2419, 2=93, 3=14, 4=2, 5=1, 8=1, int 0..8
- bicyclist_killed_count: 0=94213, 1=30
- bicyclist_injured_count: 0=91918, 1=2289, 2=34, 3=1, 4=1, int 0..4
- motorcyclist_killed_count: 0=94158, 1=80, 2=5, int 0..2
- motorcyclist_injured_count: 0=92131, 1=1981, 2=120, 3=9, 4=2, num 0..4
- primary_ramp: "TO"=1032, "FR"=432, "northbound off-ramp"=41, "southbound off-ramp"=40, "TR"=30, "northbound on-ramp"=29, "southbound on-ramp"=24, "westbound off-ramp"=23, "eastbound off-ramp"=17, "eastbound on-ramp"=12, "westbound on-ramp"=11, "CN"=7, "CO"=2, nulls=92543
- secondary_ramp: "northbound off-ramp"=165, "southbound off-ramp"=162, "northbound on-ramp"=117, "southbound on-ramp"=110, "westbound off-ramp"=88, "eastbound off-ramp"=86, "eastbound on-ramp"=66, "westbound on-ramp"=60, "TO"=42, "FR"=14, "CN"=6, "TR"=5, "CO"=3, nulls=93319
- latitude: 24977 distinct, nulls=67280, num 32.5056..41.9263
  - stats: average=35.6027, median=34.3765
- longitude: 25670 distinct, nulls=67280, num -124.346..-114.177
  - stats: average=-119.432, median=-118.553
- collision_date: 7454 distinct
- collision_time: 1440 distinct, nulls=804
- process_date: 5432 distinct


# parties

```sql
CREATE TABLE "parties" (
"id" INTEGER,
  "case_id" REAL,
  "party_number" INTEGER,
  "party_type" TEXT,
  "at_fault" INTEGER,
  "party_sex" TEXT,
  "party_age" REAL,
  "party_sobriety" TEXT,
  "party_drug_physical" TEXT,
  "direction_of_travel" TEXT,
  "party_safety_equipment_1" TEXT,
  "party_safety_equipment_2" TEXT,
  "financial_responsibility" TEXT,
  "hazardous_materials" REAL,
  "cellphone_in_use" REAL,
  "cellphone_use_type" TEXT,
  "school_bus_related" REAL,
  "oaf_violation_code" TEXT,
  "oaf_violation_category" TEXT,
  "oaf_violation_section" REAL,
  "oaf_violation_suffix" TEXT,
  "other_associate_factor_1" TEXT,
  "other_associate_factor_2" TEXT,
  "party_number_killed" INTEGER,
  "party_number_injured" INTEGER,
  "movement_preceding_collision" TEXT,
  "vehicle_year" REAL,
  "vehicle_make" TEXT,
  "statewide_vehicle_type" TEXT,
  "chp_vehicle_type_towing" TEXT,
  "chp_vehicle_type_towed" TEXT,
  "party_race" TEXT
);
```

## Rows

- total=186692

| column | latest | sample | sample |
|---|---|---|---|
| id | 16432232 | 3333194 | 3397379 |
| case_id | 9.87001e+18 | 6.01004e+06 | 6.04535e+06 |
| party_number | 2 | 1 | 1 |
| party_type | driver | driver | driver |
| at_fault | 0 | 1 | 1 |
| party_sex | male | female | male |
| party_age | 20 | 24 | 22 |
| party_sobriety | had not been drinking | had not been drinking | had not been drinking |
| party_drug_physical | null | null | null |
| direction_of_travel | south | south | west |
| party_safety_equipment_1 | lap/shoulder harness used | air bag not deployed | air bag deployed |
| party_safety_equipment_2 | null | lap/shoulder harness used | lap/shoulder harness used |
| financial_responsibility | proof of insurance obtained | proof of insurance obtained | proof of insurance obtained |
| hazardous_materials | null | null | null |
| cellphone_in_use | null | 0 | 0 |
| cellphone_use_type | no cellphone/unknown | cellphone not in use | cellphone not in use |
| school_bus_related | null | null | null |
| oaf_violation_code | null | null | null |
| oaf_violation_category | null | null | null |
| oaf_violation_section | 0 | null | null |
| oaf_violation_suffix | null | null | null |
| other_associate_factor_1 | none apparent | none apparent | none apparent |
| other_associate_factor_2 | null | null | null |
| party_number_killed | 0 | 0 | 0 |
| party_number_injured | 0 | 0 | 0 |
| movement_preceding_collision | slowing/stopping | changing lanes | proceeding straight |
| vehicle_year | 2001 | 2003 | 2002 |
| vehicle_make | ford | chevrolet | ford |
| statewide_vehicle_type | pickup or panel truck | passenger car | passenger car |
| chp_vehicle_type_towing | pickups & panels | passenger car, station | passenger car, station |
| chp_vehicle_type_towed | 00 | 00 | null |
| party_race | null | white | white |

## Columns

- id: int 34..16432232
- case_id: num 15..9.87001e+18
- party_number: int 1..92
  - stats: average=1.60592
- party_type: nulls=431
- at_fault: int 0..1
  - stats: average=0.463421
- party_sex: nulls=25037
- party_age: nulls=29143, num 0..110
  - stats: average=38.4937
- party_sobriety: nulls=5523
- party_drug_physical: nulls=156360
- direction_of_travel: nulls=5208
- party_safety_equipment_1: nulls=31438
- party_safety_equipment_2: nulls=70127
- financial_responsibility: nulls=15249
- hazardous_materials: nulls=186331, num 1..1
  - stats: average=1
- cellphone_in_use: nulls=56934, num 0..1
  - stats: average=0.0204612
- cellphone_use_type: nulls=43216
- school_bus_related: nulls=186163, num 1..1
  - stats: average=1
- oaf_violation_code: nulls=185889
- oaf_violation_category: nulls=173903
- oaf_violation_section: nulls=164317, num 0..47207
  - stats: average=12514.6
- oaf_violation_suffix: nulls=182554
- other_associate_factor_1: nulls=11151
- other_associate_factor_2: nulls=183158
- party_number_killed: int 0..6
  - stats: average=0.00392625
- party_number_injured: int 0..33
  - stats: average=0.283633
- movement_preceding_collision: nulls=3344
- vehicle_year: nulls=17757, num 1905..2918
  - stats: average=2001.6
- vehicle_make: nulls=19553
- statewide_vehicle_type: nulls=20955
- chp_vehicle_type_towing: nulls=40125
- chp_vehicle_type_towed: nulls=90939
- party_race: nulls=43837


# victims

```sql
CREATE TABLE "victims" (
"id" INTEGER,
  "case_id" REAL,
  "party_number" INTEGER,
  "victim_role" TEXT,
  "victim_sex" TEXT,
  "victim_age" REAL,
  "victim_degree_of_injury" TEXT,
  "victim_seating_position" TEXT,
  "victim_safety_equipment_1" TEXT,
  "victim_safety_equipment_2" TEXT,
  "victim_ejected" TEXT
);
```

## Rows

- total=96393

| column | latest | sample | sample |
|---|---|---|---|
| id | 8817516 | 4589446 | 8806060 |
| case_id | 9.87001e+18 | 9.07188e+07 | 9.85501e+18 |
| party_number | 2 | 1 | 1 |
| victim_role | non-injured party | driver | passenger |
| victim_sex | male | female | female |
| victim_age | 26 | 41 | 15 |
| victim_degree_of_injury | no injury | possible injury | other visible injury |
| victim_seating_position | passenger seat 3 | driver | passenger seat 4 |
| victim_safety_equipment_1 | lap/shoulder harness used | air bag deployed | lap/shoulder harness used |
| victim_safety_equipment_2 | null | lap/shoulder harness used | null |
| victim_ejected | not ejected | not ejected | not ejected |

## Columns

- id: 95894 distinct, int 5..8817516
- case_id: 95458 distinct, num 26..9.87001e+18
- party_number: 2=45270, 1=44290, 3=5579, 4=949, 5=221, 6=48, 7=17, 8=12, 9=2, 10=1, 12=1, 13=1, 51=1, 84=1, int 1..84
- victim_role: "passenger"=54810, "driver"=33197, "non-injured party"=2974, "pedestrian"=2968, "bicyclist"=2344, "other"=99, nulls=1
- victim_sex: "female"=47056, "male"=46995, "2"=1, "4"=1, nulls=2340
- victim_age: 109 distinct, nulls=3191, num 0..999
  - stats: average=31.0895, median=27
- victim_degree_of_injury: "no injury"=42655, "complaint of pain"=33400, "other visible injury"=12932, "possible injury"=2696, "severe injury"=2215, "suspected minor injury"=1378, "killed"=743, "suspected serious injury"=374
- victim_seating_position: "driver"=35067, "passenger seat 3"=28911, "passenger seat 6"=10317, "passenger seat 4"=8314, "position unknown"=5245, "passenger seat 5"=3476, "other occupants"=1595, "passenger seat 2"=1459, "station wagon rear"=1062, "rear occupant of truck or van"=763, nulls=184
- victim_safety_equipment_1: 23 distinct, nulls=5542
- victim_safety_equipment_2: 24 distinct, nulls=31094
- victim_ejected: "not ejected"=85677, "unknown"=6886, "fully ejected"=3037, "partially ejected"=356, nulls=437
