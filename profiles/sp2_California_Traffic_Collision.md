---
generator: db-snooper
version: 0.0.33
generated_at_utc: 2026-08-21T12:32:01.058608Z
dialect: sqlite
database: /var/folders/9j/b9bx_drd53sc6zbpsqyrjy4h0000gn/T/dbsnoop-2wxeb2if/California_Traffic_Collision.sqlite
schema: main
---

# "case_ids"  (rows=94243)

columns:
"case_id" float: 94242 distinct, 45..9.9e+18
"db_year" int: 2021=52813, 2018=36903, 2020=4526, 2017=1, 2017..2021

indexes: none

samples:
| column | latest | sample | sample |
|---|---|---|---|
| case_id | 9.9e+18 | 5.2e+06 | 6.7e+06 |
| db_year | 2018 | 2021 | 2021 |

# "collisions"  (rows=94243)

columns:
"case_id" float: unique identifier, 11..9.9e+18
"jurisdiction" float: 467 distinct, nulls=121, 100..9870, avg=5867.06, median=4807
"officer_id" text: 30277 distinct, nulls=209
"reporting_district" text: 6259 distinct, nulls=55424
"chp_shift" text: "not chp"=50956, "1400 thru 2159"=19812, "0600 thru 1359"=16394, "2200 thru 0559"=6799, "chp not stated"=282
"population" text: ">250000"=23436, "unincorporated"=22095, "100000 to 250000"=17700, "50000 to 100000"=16957, "25000 to 50000"=8438, "10000 to 25000"=3846, "2500 to 10000"=1297, "<2500"=455, nulls=19
"county_city_location" int: 525 distinct, 100..5802, avg=2789.71, median=3001
"county_location" text: 58 distinct
"special_condition" float: 0=88670, 1=377, nulls=5196
"beat_type" text: "not chp"=50956, "chp state highway"=30446, "chp county roadarea"=8124, "chp county roadline"=4479, "schoolbus on city roadway"=238
"chp_beat_type" text: "not chp"=50956, "interstate"=15291, "state route"=11474, "county road area"=8133, "county road line"=4390, "us highway"=3638, "safety services program"=340, "administrative"=21
"city_division_lapd" text: "L"=464, "J"=411, "Q"=409, "O"=401, "G"=381, "C"=363, "I"=363, "M"=363, "K"=355, "N"=345, "H"=315, "F"=307, "P"=300, "B"=291, "R"=290, "A"=261, "D"=231, "E"=226, nulls=88167
"chp_beat_class" text: "not chp"=50956, "chp other"=36378, "chp primary"=6883, nulls=26
"beat_number" text: 5049 distinct, nulls=8075
"primary_road" text: 21661 distinct
"secondary_road" text: 33560 distinct, nulls=1
"distance" float: 2121 distinct, 0..5.6e+06, avg=716.122, median=100
"direction" text: "south"=19444, "north"=19178, "east"=16095, "west"=15960, nulls=23566
"intersection" float: 0=71354, 1=21947, nulls=942
"weather_1" text: "clear"=77489, "cloudy"=12330, "raining"=3301, "fog"=389, "snowing"=134, "other"=98, "wind"=33, nulls=469
"weather_2" text: "raining"=1963, "wind"=270, "cloudy"=175, "other"=83, "snowing"=70, "fog"=66, nulls=91616
"state_highway_indicator" float: 0=58953, 1=35261, nulls=29
"caltrans_county" text: 58 distinct, nulls=68771
"caltrans_district" float: 7=7147, 4=5082, 0=3329, 8=3093, 12=2312, 11=1803, 3=1589, 6=1366, 5=1188, 10=1096, 1=362, 2=362, 9=72, nulls=65442, 0..12
"state_route" float: 227 distinct, nulls=65442, 0..980, avg=129.129, median=78
"route_suffix" text: "B"=1898, "S"=60, "U"=26, nulls=92259
"postmile_prefix" text: "R"=7126, "B"=1324, "M"=349, "L"=135, "T"=126, "S"=17, "C"=4, "D"=4, "H"=1, "N"=1, nulls=85156
"postmile" float: 8755 distinct, nulls=65442, 0..608.611, avg=17.7815, median=13
"location_type" text: "highway"=20125, "ramp"=3743, "intersection"=1604, nulls=68771
"ramp_intersection" text: "not state highway"=3329, "highway"=1519, "not state highway, ramp-related, within 100 feet"=1337, "intersection"=1217, "mid-ramp"=1120, "ramp exit, last 50 feet"=1093, "not state highway, intersection-related, within 250 feet"=386, "ramp entry, first 50 feet"=193, nulls=84049
"side_of_highway" text: "northbound"=7973, "southbound"=7925, "westbound"=4823, "eastbound"=4751, nulls=68771
"tow_away" float: 1=47305, 0=46270, nulls=668
"collision_severity" text: "property damage only"=57175, "pain"=22565, "other injury"=11660, "severe injury"=2213, "fatal"=630
"killed_victims" float: 0=93590, 1=584, 2=34, 3=8, 4=3, 13=1, nulls=23, 0..13
"injured_victims" float: 0=57534, 1=26114, 2=7180, 3=2204, 4=750, 5=270, 6=108, 7=24, 8=22, 9=7, 16=2, 10=1, 11=1, 20=1, 21=1, 31=1, nulls=23, 0..31
"party_count" float: 2=64165, 1=17768, 3=9676, 4=2031, 5=443, 6=112, 7=30, 8=11, 10=4, 9=3, 1..10
"primary_collision_factor" text: "vehicle code violation"=88339, "unknown"=2562, "other than driver"=2002, "other improper driving"=685, "fell asleep"=91, nulls=564
"pcf_violation_code" text: "vehicle"=4813, "A"=5, "city ordinance"=4, "'"=1, "D"=1, nulls=89419
"pcf_violation_category" text: 23 distinct, nulls=1602
"pcf_violation" float: 193 distinct, nulls=6595, 0..83123, avg=22040.3, median=22107
"pcf_violation_subsection" text: "A"=31496, "B"=1165, "1"=377, "C"=302, "D"=228, "F"=125, "5"=77, "E"=66, "G"=31, "I"=16, "2"=4, "3"=3, "H"=1, nulls=60352
"hit_and_run" text: "not hit and run"=75820, "misdemeanor"=15810, "felony"=2613
"type_of_collision" text: "rear end"=30895, "broadside"=18510, "sideswipe"=16962, "hit object"=15334, "head-on"=4102, "other"=2647, "overturned"=2526, "pedestrian"=2501, nulls=766
"motor_vehicle_involved_with" text: "other motor vehicle"=61336, "fixed object"=14717, "parked motor vehicle"=7071, "pedestrian"=2677, "non-collision"=2605, "bicycle"=2299, "other object"=1912, "motor vehicle on other roadway"=663, "animal"=435, "train"=26, "2"=2, nulls=500
"pedestrian_action" text: "no pedestrian involved"=91454, "crossing in intersection crosswalk"=1184, "crossing not in crosswalk"=770, "in road"=501, "not in road"=210, "crossing non-intersection crosswalk"=62, "using school bus"=3, nulls=59
"road_surface" text: "dry"=85050, "wet"=7790, "snowy"=430, "slippery"=103, "H"=2, nulls=868
"road_condition_1" text: "normal"=90556, "construction"=1475, "other"=396, "obstruction"=377, "holes"=270, "loose material"=182, "reduced width"=95, "flooded"=58, nulls=834
"road_condition_2" text: "normal"=173, "reduced width"=142, "construction"=24, "other"=19, "obstruction"=6, "flooded"=4, "loose material"=3, "holes"=2, nulls=93870
"lighting" text: "daylight"=62901, "dark with street lights"=19652, "dark with no street lights"=7551, "dusk or dawn"=3386, "dark with street lights not functioning"=185, nulls=568
"control_device" text: "none"=62402, "functioning"=30907, "not functioning"=282, "obscured"=63, nulls=589
"chp_road_type" text: "0"=76425, "1"=15503, "6"=1137, "5"=841, "0.0"=147, "4"=131, "3"=23, "1.0"=16, "7"=13, "2"=5, "6.0"=2
"pedestrian_collision" int: 0=91445, 1=2798
"bicycle_collision" int: 0=91652, 1=2591
"motorcycle_collision" int: 0=91447, 1=2796
"truck_collision" int: 0=88738, 1=5505
"not_private_property" float: 1=94243
"alcohol_involved" float: 1=9411, nulls=84832
"statewide_vehicle_type_at_fault" text: "passenger car"=56217, "pickup or panel truck"=10660, "motorcycle or scooter"=1586, "truck or truck tractor with trailer"=1487, "bicycle"=1435, "truck or truck tractor"=1110, "pedestrian"=920, "emergency vehicle"=474, "pickup or panel truck with trailer"=460, "other vehicle"=326, "other bus"=297, "schoolbus"=187, "passenger car with trailer"=146, "highway construction equipment"=19, "moped"=9, nulls=18910
"chp_vehicle_type_at_fault" text: 76 distinct, nulls=25444
"severe_injury_count" int: 0=91919, 1=2100, 2=176, 3=31, 4=14, 5=1, 8=1, 10=1, 0..10
"other_visible_injury_count" int: 0=82030, 1=10641, 2=1256, 3=227, 4=66, 5=11, 6=7, 7=3, 13=1, 20=1, 0..20
"complaint_of_pain_injury_count" int: 0=68314, 1=18964, 2=5046, 3=1312, 4=408, 5=129, 6=46, 7=11, 8=7, 9=5, 20=1, 0..20
"pedestrian_killed_count" int: 0=94090, 1=151, 2=1, 3=1, 0..3
"pedestrian_injured_count" int: 0=91713, 1=2419, 2=93, 3=14, 4=2, 5=1, 8=1, 0..8
"bicyclist_killed_count" int: 0=94213, 1=30
"bicyclist_injured_count" int: 0=91918, 1=2289, 2=34, 3=1, 4=1, 0..4
"motorcyclist_killed_count" int: 0=94158, 1=80, 2=5, 0..2
"motorcyclist_injured_count" float: 0=92131, 1=1981, 2=120, 3=9, 4=2, 0..4
"primary_ramp" text: "TO"=1032, "FR"=432, "northbound off-ramp"=41, "southbound off-ramp"=40, "TR"=30, "northbound on-ramp"=29, "southbound on-ramp"=24, "westbound off-ramp"=23, "eastbound off-ramp"=17, "eastbound on-ramp"=12, "westbound on-ramp"=11, "CN"=7, "CO"=2, nulls=92543
"secondary_ramp" text: "northbound off-ramp"=165, "southbound off-ramp"=162, "northbound on-ramp"=117, "southbound on-ramp"=110, "westbound off-ramp"=88, "eastbound off-ramp"=86, "eastbound on-ramp"=66, "westbound on-ramp"=60, "TO"=42, "FR"=14, "CN"=6, "TR"=5, "CO"=3, nulls=93319
"latitude" float: 24977 distinct, nulls=67280, 32.5056..41.9263, avg=35.6027, median=34.3765
"longitude" float: 25670 distinct, nulls=67280, -124.346..-114.177, avg=-119.432, median=-118.553
"collision_date" text: iso-date, 7454 distinct
"collision_time" text: 1440 distinct, nulls=804
"process_date" text: iso-date, 5432 distinct

indexes: none

samples:
| column | latest | sample | sample |
|---|---|---|---|
| case_id | 9.9e+18 | 6e+06 | 1.8e+06 |
| jurisdiction | 9870 | 9860 | 9670 |
| officer_id | 16011 | 011402 | 13317 |
| reporting_district | 0 | null | null |
| chp_shift | 0600 thru 1359 | 0600 thru 1359 | 1400 thru 2159 |
| population | unincorporated | unincorporated | 50000 to 100000 |
| county_city_location | 3600 | 3600 | 3003 |
| county_location | san bernardino | san bernardino | orange |
| special_condition | null | 0 | 0 |
| beat_type | chp state highway | chp county roadarea | chp state highway |
| chp_beat_type | state route | county road area | state route |
| city_division_lapd | null | null | null |
| chp_beat_class | chp primary | chp other | chp other |
| beat_number | 031 | 002 | 091 |
| primary_road | RT 62 | STATE ST | RT 91 |
| secondary_road | JUNIPER RD | KERN ST | STANTON AV |
| distance | 267 | 580 | 200 |
| direction | east | south | west |
| intersection | 0 | 0 | 0 |
| weather_1 | clear | clear | clear |
| weather_2 | null | null | null |
| state_highway_indicator | 1 | 0 | 0 |
| caltrans_county | san bernardino | null | null |
| caltrans_district | 8 | null | null |
| state_route | 62 | null | null |
| route_suffix | B | null | null |
| postmile_prefix | B | null | null |
| postmile | 17.32 | null | null |
| location_type | highway | null | null |
| ramp_intersection | highway | null | null |
| side_of_highway | eastbound | null | null |
| tow_away | 1 | 1 | 1 |
| collision_severity | property damage only | property damage only | pain |
| killed_victims | 0 | 0 | 0 |
| injured_victims | 0 | 0 | 3 |
| party_count | 2 | 1 | 2 |
| primary_collision_factor | vehicle code violation | vehicle code violation | vehicle code violation |
| pcf_violation_code | vehicle | null | null |
| pcf_violation_category | automobile right of way | speeding | improper turning |
| pcf_violation | 21801 | 22350 | 22107 |
| pcf_violation_subsection | A | null | null |
| hit_and_run | not hit and run | misdemeanor | not hit and run |
| type_of_collision | broadside | hit object | sideswipe |
| motor_vehicle_involved_with | other motor vehicle | fixed object | parked motor vehicle |
| pedestrian_action | no pedestrian involved | no pedestrian involved | no pedestrian involved |
| road_surface | dry | dry | dry |
| road_condition_1 | normal | normal | normal |
| road_condition_2 | null | null | null |
| lighting | daylight | daylight | daylight |
| control_device | none | functioning | none |
| chp_road_type | 0 | 0 | 0 |
| pedestrian_collision | 0 | 0 | 0 |
| bicycle_collision | 0 | 0 | 0 |
| motorcycle_collision | 0 | 0 | 0 |
| truck_collision | 0 | 0 | 0 |
| not_private_property | 1 | 1 | 1 |
| alcohol_involved | null | null | null |
| statewide_vehicle_type_at_fault | passenger car | passenger car | passenger car |
| chp_vehicle_type_at_fault | passenger car, station | passenger car, station | passenger car, station |
| severe_injury_count | 0 | 0 | 0 |
| other_visible_injury_count | 0 | 0 | 0 |
| complaint_of_pain_injury_count | 0 | 0 | 3 |
| pedestrian_killed_count | 0 | 0 | 0 |
| pedestrian_injured_count | 0 | 0 | 0 |
| bicyclist_killed_count | 0 | 0 | 0 |
| bicyclist_injured_count | 0 | 0 | 0 |
| motorcyclist_killed_count | 0 | 0 | 0 |
| motorcyclist_injured_count | 0 | 0 | 0 |
| primary_ramp | null | null | null |
| secondary_ramp | null | null | null |
| latitude | null | 34.1553 | null |
| longitude | null | -117.335 | null |
| collision_date | 2001-11-06 | 2013-01-15 | 2004-09-07 |
| collision_time | 10:00:00 | 13:45:00 | 16:15:00 |
| process_date | 2002-04-04 | 2014-06-23 | 2005-03-22 |

# "parties"  (rows=186692)

columns:
"id" int: 34..16432232
"case_id" float: 15..9.9e+18
"party_number" int: 1..92, avg=1.60592
"party_type" text: nulls=431
"at_fault" int: 0..1, avg=0.463421
"party_sex" text: nulls=25037
"party_age" float: nulls=29143, 0..110, avg=38.4937
"party_sobriety" text: nulls=5523
"party_drug_physical" text: nulls=156360
"direction_of_travel" text: nulls=5208
"party_safety_equipment_1" text: nulls=31438
"party_safety_equipment_2" text: nulls=70127
"financial_responsibility" text: nulls=15249
"hazardous_materials" float: nulls=186331, 1..1, avg=1
"cellphone_in_use" float: nulls=56934, 0..1, avg=0.0204612
"cellphone_use_type" text: nulls=43216
"school_bus_related" float: nulls=186163, 1..1, avg=1
"oaf_violation_code" text: nulls=185889
"oaf_violation_category" text: nulls=173903
"oaf_violation_section" float: nulls=164317, 0..47207, avg=12514.6
"oaf_violation_suffix" text: nulls=182554
"other_associate_factor_1" text: nulls=11151
"other_associate_factor_2" text: nulls=183158
"party_number_killed" int: 0..6, avg=0.00392625
"party_number_injured" int: 0..33, avg=0.283633
"movement_preceding_collision" text: nulls=3344
"vehicle_year" float: nulls=17757, 1905..2918, avg=2001.6
"vehicle_make" text: nulls=19553
"statewide_vehicle_type" text: nulls=20955
"chp_vehicle_type_towing" text: nulls=40125
"chp_vehicle_type_towed" text: nulls=90939
"party_race" text: nulls=43837

indexes: none

samples:
| column | latest | sample | sample |
|---|---|---|---|
| id | 16432232 | 7167746 | 1867493 |
| case_id | 9.9e+18 | 8.9e+06 | 5.2e+06 |
| party_number | 2 | 1 | 1 |
| party_type | driver | driver | driver |
| at_fault | 0 | 1 | 1 |
| party_sex | male | male | null |
| party_age | 20 | 31 | null |
| party_sobriety | had not been drinking | had not been drinking | impairment unknown |
| party_drug_physical | null | null | G |
| direction_of_travel | south | west | null |
| party_safety_equipment_1 | lap/shoulder harness used | air bag not deployed | null |
| party_safety_equipment_2 | null | lap/shoulder harness used | null |
| financial_responsibility | proof of insurance obtained | no proof of insurance obtained | null |
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
| movement_preceding_collision | slowing/stopping | proceeding straight | proceeding straight |
| vehicle_year | 2001 | 2002 | null |
| vehicle_make | ford | mercedes-benz | null |
| statewide_vehicle_type | pickup or panel truck | passenger car | null |
| chp_vehicle_type_towing | pickups & panels | passenger car, station | null |
| chp_vehicle_type_towed | 00 | null | 00 |
| party_race | null | asian | null |

# "victims"  (rows=96393)

columns:
"id" int: 95894 distinct, 5..8817516
"case_id" float: 95458 distinct, 26..9.9e+18
"party_number" int: 2=45270, 1=44290, 3=5579, 4=949, 5=221, 6=48, 7=17, 8=12, 9=2, 10=1, 12=1, 13=1, 51=1, 84=1, 1..84
"victim_role" text: "passenger"=54810, "driver"=33197, "non-injured party"=2974, "pedestrian"=2968, "bicyclist"=2344, "other"=99, nulls=1
"victim_sex" text: "female"=47056, "male"=46995, "2"=1, "4"=1, nulls=2340
"victim_age" float: 109 distinct, nulls=3191, 0..999, avg=31.0895, median=27
"victim_degree_of_injury" text: "no injury"=42655, "complaint of pain"=33400, "other visible injury"=12932, "possible injury"=2696, "severe injury"=2215, "suspected minor injury"=1378, "killed"=743, "suspected serious injury"=374
"victim_seating_position" text: "driver"=35067, "passenger seat 3"=28911, "passenger seat 6"=10317, "passenger seat 4"=8314, "position unknown"=5245, "passenger seat 5"=3476, "other occupants"=1595, "passenger seat 2"=1459, "station wagon rear"=1062, "rear occupant of truck or van"=763, nulls=184
"victim_safety_equipment_1" text: 23 distinct, nulls=5542
"victim_safety_equipment_2" text: 24 distinct, nulls=31094
"victim_ejected" text: "not ejected"=85677, "unknown"=6886, "fully ejected"=3037, "partially ejected"=356, nulls=437

indexes: none

samples:
| column | latest | sample | sample |
|---|---|---|---|
| id | 8817516 | 1604644 | 2510391 |
| case_id | 9.9e+18 | 1.6e+06 | 6.7e+06 |
| party_number | 2 | 1 | 2 |
| victim_role | non-injured party | passenger | driver |
| victim_sex | male | male | female |
| victim_age | 26 | 9 | 30 |
| victim_degree_of_injury | no injury | no injury | complaint of pain |
| victim_seating_position | passenger seat 3 | passenger seat 6 | driver |
| victim_safety_equipment_1 | lap/shoulder harness used | air bag not deployed | air bag deployed |
| victim_safety_equipment_2 | null | lap/shoulder harness used | lap/shoulder harness used |
| victim_ejected | not ejected | not ejected | not ejected |
