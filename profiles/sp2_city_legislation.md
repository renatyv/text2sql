---
generator: db-snooper
version: 0.0.31
generated_at_utc: 2026-08-20T17:28:12.993041Z
dialect: sqlite
database: /var/folders/9j/b9bx_drd53sc6zbpsqyrjy4h0000gn/T/dbsnoop-xwazsad0/city_legislation.sqlite
schema: main
---

# "alien_data"  (rows=50000)

columns:
"id" int: unique identifier, 1..50000
"first_name" text: 8392 distinct, nulls=4
"last_name" text: 31034 distinct
"email" text: all distinct
"gender" text: "female"=22730, "male"=22323, "non-binary"=4947
"type" text: "flatwoods"=10124, "nordic"=10033, "reptile"=9964, "green"=9948, "grey"=9931
"birth_year" int: 301 distinct, 1672..1972, avg=1822.07, median=1823
"age" int: 301 distinct, 52..352, avg=201.929, median=201
"favorite_food" text: 1498 distinct
"feeding_frequency" text: "once"=6490, "weekly"=6300, "never"=6290, "daily"=6283, "seldom"=6201, "yearly"=6192, "often"=6167, "monthly"=6077
"aggressive" int: 0=25053, 1=24947
"occupation" text: 195 distinct
"current_location" text: 461 distinct
"state" text: 51 distinct
"us_region" text: "southeast"=13856, "far west"=7885, "southwest"=7600, "mideast"=7205, "great lakes"=5725, "plains"=4052, "rocky mountain"=2006, "new england"=1671
"country" text: "united states"=50000

indexes: none
fk: none

samples:
| column | latest | sample | sample |
|---|---|---|---|
| id | 50000 | 16235 | 42170 |
| first_name | theressa | frederigo | joshia |
| last_name | wahncke | wild | fraczak |
| email | twahncke12kv@telegraph.co.uk | fwildciy@mozilla.org | jfraczakwjd@google.es |
| gender | female | male | male |
| type | green | reptile | reptile |
| birth_year | 1822 | 1758 | 1873 |
| age | 202 | 266 | 151 |
| favorite_food | galapagos mockingbird | anteater, giant | avocet, pied |
| feeding_frequency | never | once | never |
| aggressive | 1 | 1 | 0 |
| occupation | chief design engineer | account representative iv | quality control specialist |
| current_location | dayton | winston salem | albany |
| state | ohio | north carolina | new york |
| us_region | great lakes | southeast | mideast |
| country | united states | united states | united states |

# "aliens"  (rows=50000)

columns:
"id" int: unique identifier, 1..50000
"first_name" text: 8393 distinct
"last_name" text: 31037 distinct
"email" text: all distinct
"gender" text: "Female"=22730, "Male"=22323, "Bigender"=856, "Non-binary"=848, "Polygender"=847, "Agender"=828, "Genderfluid"=784, "Genderqueer"=784
"type" text: "Flatwoods"=10124, "Nordic"=10033, "Reptile"=9964, "Green"=9948, "Grey"=9931
"birth_year" int: 301 distinct, 1672..1972, avg=1822.07, median=1823

indexes: none
fk: none

samples:
| column | latest | sample | sample |
|---|---|---|---|
| id | 50000 | 10838 | 14129 |
| first_name | Theressa | Vladimir | Shandra |
| last_name | Wahncke | Pead | Saunder |
| email | twahncke12kv@telegraph.co.uk | vpead8d1@t.co | ssaunderawg@msu.edu |
| gender | Female | Male | Non-binary |
| type | Green | Flatwoods | Grey |
| birth_year | 1822 | 1956 | 1863 |

# "aliens_details"  (rows=50000)

columns:
"detail_id" int: unique identifier, 1..50000
"favorite_food" text: 1498 distinct
"feeding_frequency" text: "Once"=6490, "Weekly"=6300, "Never"=6290, "Daily"=6283, "Seldom"=6201, "Yearly"=6192, "Often"=6167, "Monthly"=6077
"aggressive" int: 0=25053, 1=24947

indexes: none
fk: none

samples:
| column | latest | sample | sample |
|---|---|---|---|
| detail_id | 50000 | 20559 | 9851 |
| favorite_food | Galapagos mockingbird | Kingfisher, malachite | Lion, south american sea |
| feeding_frequency | Never | Often | Weekly |
| aggressive | 1 | 0 | 0 |

# "aliens_location"  (rows=50000)

columns:
"loc_id" int: unique identifier, 1..50000
"current_location" text: 461 distinct
"state" text: 51 distinct
"country" text: "United States"=50000
"occupation" text: 195 distinct

indexes: none
fk: none

samples:
| column | latest | sample | sample |
|---|---|---|---|
| loc_id | 50000 | 36110 | 13327 |
| current_location | Dayton | Winston Salem | Birmingham |
| state | Ohio | North Carolina | Alabama |
| country | United States | United States | United States |
| occupation | Chief Design Engineer | Marketing Manager | Human Resources Assistant II |

# "cities"  (rows=44622)

columns:
"city_id" int: unique identifier, 1..44622
"city_name" text: 41062 distinct, nulls=1
"latitude" float: 37063 distinct, -179.6..179.37, avg=14.5078, median=13.3804
"longitude" float: 34608 distinct, -54.9333..81.7166, avg=25.9138, median=32.3286
"country_code_2" text: 236 distinct
"capital" int: 0=44376, 1=246
"population" float: 29611 distinct, nulls=305, 0..3.7732e+07, avg=114467, median=20992
"insert_date" text: iso-date, 943 distinct

indexes: none
fk: none

samples:
| column | latest | sample | sample |
|---|---|---|---|
| city_id | 44622 | 6146 | 4168 |
| city_name | nordvik | bhola | kerch |
| latitude | 111.51 | 90.6461 | 36.4711 |
| longitude | 74.0165 | 22.6863 | 45.3619 |
| country_code_2 | ru | bd | ua |
| capital | 0 | 0 | 0 |
| population | 0 | 87243 | 149566 |
| insert_date | 2022-04-27 | 2022-09-24 | 2021-05-16 |

# "cities_countries"  (rows=241)

columns:
"country_id" int: unique identifier, 1..256
"country_name" text: all distinct
"country_code_2" text: all distinct
"country_code_3" text: all distinct
"region" text: "africa"=59, "americas"=57, "asia"=50, "europe"=48, "oceania"=26, "antartica"=1
"sub_region" text: "subsaharan africa"=53, "latin america and the caribbean"=52, "western asia"=17, "southern europe"=16, "northern europe"=13, "southeastern asia"=11, "eastern europe"=10, "polynesia"=9, "southern asia"=9, "western europe"=9, "eastern asia"=8, "micronesia"=7, "northern africa"=6, "australia and new zealand"=5, "central asia"=5, "melanesia"=5, "northern america"=5, nulls=1
"intermediate_region" text: "caribbean"=28, "eastern africa"=22, "western africa"=17, "south america"=16, "middle africa"=9, "central america"=8, "southern africa"=5, "channel islands"=1, nulls=135
"created_on" text: "2024-07-18"=241

indexes: none
fk: none

samples:
| column | latest | sample | sample |
|---|---|---|---|
| country_id | 256 | 104 | 13 |
| country_name | zambia | hong kong | armenia |
| country_code_2 | zm | hk | am |
| country_code_3 | zmb | hkg | arm |
| region | africa | asia | asia |
| sub_region | subsaharan africa | eastern asia | western asia |
| intermediate_region | eastern africa | null | null |
| created_on | 2024-07-18 | 2024-07-18 | 2024-07-18 |

# "cities_currencies"  (rows=254)

columns:
"currency_id" int: unique identifier, 1..254
"country_code_2" text: 233 distinct
"currency_name" text: 165 distinct
"currency_code" text: 166 distinct, nulls=1

indexes: none
fk: none

samples:
| column | latest | sample | sample |
|---|---|---|---|
| currency_id | 254 | 204 | 223 |
| country_code_2 | zw | sl | tw |
| currency_name | zimbabwe dollar | leone | new taiwan dollar |
| currency_code | zwl | sle | twd |

# "cities_languages"  (rows=608)

columns:
"language_id" int: unique identifier, 1..608
"language" text: 229 distinct
"country_code_2" text: 237 distinct

indexes: none
fk: none

samples:
| column | latest | sample | sample |
|---|---|---|---|
| language_id | 608 | 174 | 267 |
| language | shona | english | arabic |
| country_code_2 | zw | fj | iq |

# "job_company"  (rows=14003)

columns:
"company_id" int: unique identifier, 31..787652
"name" text: all distinct
"link" text: 5008 distinct, nulls=8648
"link_google" text: all distinct, nulls=5
"thumbnail" text: 6032 distinct, nulls=5884

indexes: none
fk: none

samples:
| column | latest | sample | sample |
|---|---|---|---|
| company_id | 787652 | 158713 | 64273 |
| name | Rotary Engineering Pte. Ltd. | SignalFire, LLC | iCore Pioneer Business Solution Pvt. LTD Technopark Trivandrum |
| link | http://www.rotaryeng.com.sg/ | http://www.signalfire.com/ | null |
| link_google | null | https://www.google.com/search?sca_esv=562982649&hl=en&gl=us&q=SignalFire,+LLC&sa=X&ved=0ahUKEwiP8suUqJWBAxVXSTABHYORC4k4eBCYkAII7Q0 | https://www.google.com/search?sca_esv=6cf689fb59020b19&gl=us&hl=en&q=iCore+Pioneer+Business+Solution+Pvt.+LTD+Technopark+Trivandrum&sa=X&ved=0ahUKEwiUldLP8qSDAxWtQzABHbM0CbI4FBCYkAIIqgo |
| thumbnail | https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQcgZKxQBsMj83FmbDN7BE6mCKD63zc8F70HMUOUllYYRByt3Pz_q_c&s | null | null |

# "job_postings_fact"  (rows=78769)

columns:
"job_id" int: unique identifier, 23..1826663
"company_id" int: 34870 distinct, 2..787360
"job_title_short" text: "Data Analyst"=19743, "Data Engineer"=18878, "Data Scientist"=17189, "Business Analyst"=4948, "Software Engineer"=4459, "Senior Data Engineer"=4411, "Senior Data Scientist"=3679, "Senior Data Analyst"=2891, "Machine Learning Engineer"=1405, "Cloud Engineer"=1166
"job_title" text: 37666 distinct, nulls=1
"job_location" text: 6061 distinct, nulls=102
"job_via" text: 2410 distinct, nulls=3
"job_schedule_type" text: 33 distinct, nulls=1300
"job_work_from_home" int: 0=71755, 1=7014
"search_location" text: 159 distinct
"job_posted_date" text: iso-date, 75984 distinct
"job_no_degree_mention" int: 0=54549, 1=24220
"job_health_insurance" int: 0=70203, 1=8566
"job_country" text: 150 distinct, nulls=6
"salary_rate" text: "year"=2174, "hour"=1090, "month"=23, "day"=1, "week"=1, nulls=75480
"salary_year_avg" float: 618 distinct, nulls=76595, 23496..375000, avg=122397, median=115000
"salary_hour_avg" float: 334 distinct, nulls=77679, 8.5..391, avg=47.737, median=46.3775

indexes: none
fk: none

samples:
| column | latest | sample | sample |
|---|---|---|---|
| job_id | 1826663 | 324262 | 163034 |
| company_id | 87729 | 44018 | 6677 |
| job_title_short | Data Scientist | Data Analyst | Data Scientist |
| job_title | Data Scientist, Data Science – Bangalore, Karnataka – Cardinal Health | Consultant, Data Analyst | Traineeship Data Science |
| job_location | Anywhere | Budapest, Hungary | Amsterdam, Netherlands |
| job_via | via MySmartPros | via LinkedIn Hungary | via BeBee Nederland |
| job_schedule_type | Full-time | Full-time | Full-time |
| job_work_from_home | 1 | 0 | 0 |
| search_location | India | Hungary | Netherlands |
| job_posted_date | 2023-03-21 20:33:44 | 2023-02-03 15:54:57 | 2023-06-14 17:17:43 |
| job_no_degree_mention | 0 | 0 | 0 |
| job_health_insurance | 0 | 0 | 0 |
| job_country | India | Hungary | Netherlands |
| salary_rate | null | null | null |
| salary_year_avg | null | null | null |
| salary_hour_avg | null | null | null |

# "legislation_date_dim"  (rows=30315)

columns:
"date" text: iso-date, all distinct
"month_name" text: "August"=2573, "December"=2573, "January"=2573, "July"=2573, "March"=2573, "May"=2573, "October"=2573, "April"=2490, "June"=2490, "November"=2490, "September"=2490, "February"=2344
"day_of_month" int: 31 distinct, 1..31, avg=15.7293, median=16

indexes: none
fk: none

samples:
| column | latest | sample | sample |
|---|---|---|---|
| date | 1999-12-31 | 1993-06-01 | 1971-06-13 |
| month_name | December | June | June |
| day_of_month | 31 | 1 | 13 |

# "legislators"  (rows=12518)

columns:
"full_name" text: 12310 distinct
"first_name" text: 1684 distinct
"last_name" text: 5724 distinct
"middle_name" text: 2914 distinct, nulls=3959
"nickname" text: 131 distinct, nulls=12262
"suffix" text: "Jr."=383, "III"=31, "Sr."=13, "II"=10, "IV"=3, nulls=12078
"other_names_end" text: "1846-01-12"=1, "1995-01-03"=1, "1995-09-03"=1, "2007-12-17"=1, nulls=12514
"other_names_middle" float: all NULL
"other_names_last" text: "Bono"=1, "Lambert"=1, "Levy"=1, "Long"=1, "Menendez"=1, nulls=12513
"birthday" text: iso-date, 11038 distinct, nulls=551
"gender" text: "M"=12152, "F"=366
"id_bioguide" text: all distinct
"id_bioguide_previous_0" text: "F000246"=1, "L000266"=1, "W000790"=1, nulls=12515
"id_govtrack" int: all distinct, 300001..456792, avg=405486, median=406348
"id_icpsr" float: all distinct, nulls=220, 1..99342, avg=7968.1, median=6441.5
"id_wikipedia" text: all distinct, nulls=2
"id_wikidata" text: all distinct, nulls=2
"id_google_entity_id" text: all distinct, nulls=69
"id_house_history" float: all distinct, nulls=1492, 7672..1.50324e+10, avg=6.00041e+07, median=16356.5
"id_house_history_alternate" float: 13283=1, nulls=12517
"id_thomas" float: all distinct, nulls=10337, 1..2296, avg=1110.53, median=1092
"id_cspan" float: all distinct, nulls=11664, 5..9.27826e+06, avg=569127, median=76348
"id_votesmart" float: all distinct, nulls=11437, 0..182310, avg=58344.8, median=29674
"id_lis" text: all distinct, nulls=12226
"id_ballotpedia" text: all distinct, nulls=11998
"id_opensecrets" text: redacted
"id_fec_0" text: all distinct, nulls=11435
"id_fec_1" text: all distinct, nulls=12408
"id_fec_2" text: "H0GA03017"=1, "H0MD07114"=1, "P80003247"=1, "S0NV00237"=1, "S4TN00096"=1, "S8ND00120"=1, nulls=12512

indexes: none
fk: none

samples:
| column | latest | sample | sample |
|---|---|---|---|
| full_name | Zoe Lofgren | Ralph Henry Cameron | Ferdinand Brucker |
| first_name | Zoe | Ralph | Ferdinand |
| last_name | Lofgren | Cameron | Brucker |
| middle_name | null | Henry | null |
| nickname | null | null | null |
| suffix | null | null | null |
| other_names_end | null | null | null |
| other_names_middle | null | null | null |
| other_names_last | null | null | null |
| birthday | 1947-12-21 | 1863-10-21 | 1858-01-08 |
| gender | F | M | M |
| id_bioguide | L000397 | C000066 | B000973 |
| id_bioguide_previous_0 | null | null | null |
| id_govtrack | 400245 | 402224 | 401925 |
| id_icpsr | 29504 | 1436 | 1158 |
| id_wikipedia | Zoe Lofgren | Ralph H. Cameron | Ferdinand Brucker |
| id_wikidata | Q218217 | Q976300 | Q1405148 |
| id_google_entity_id | kg:/m/024t94 | kg:/m/07sgkx | kg:/m/0494rk |
| id_house_history | 17087 | 10525 | 10035 |
| id_house_history_alternate | null | null | null |
| id_thomas | 701 | null | null |
| id_cspan | 36520 | null | null |
| id_votesmart | 21899 | null | null |
| id_lis | null | null | null |
| id_ballotpedia | Zoe Lofgren | null | null |
| id_fec_0 | H4CA16049 | null | null |
| id_fec_1 | null | null | null |
| id_fec_2 | null | null | null |

# "legislators_terms"  (rows=44063)

columns:
"id_bioguide" text: 12518 distinct
"term_number" int: 30 distinct, 0..29, avg=2.86717, median=2
"term_id" text: unique identifier
"term_type" text: "rep"=40190, "sen"=3873
"term_start" text: iso-date, 721 distinct
"term_end" text: iso-date, 632 distinct
"state" text: 59 distinct
"district" float: 55 distinct, nulls=3873, -1..53, avg=8.39005, median=6
"class" float: 2=1317, 3=1279, 1=1277, nulls=40190, 1..3
"party" text: 67 distinct, nulls=452
"how" text: "appointment"=201, nulls=43862
"url" text: 2081 distinct, nulls=39677
"address" text: 1807 distinct, nulls=41564
"phone" text: 554 distinct, nulls=41569
"fax" text: 575 distinct, nulls=42251
"contact_form" text: 953 distinct, nulls=42633
"office" text: 601 distinct, nulls=41571
"state_rank" text: "senior"=120, "junior"=97, nulls=43846
"rss_url" text: 511 distinct, nulls=42574
"caucus" text: "Democrat"=14, nulls=44049

indexes: none
fk: none

samples:
| column | latest | sample | sample |
|---|---|---|---|
| id_bioguide | Z000018 | L000076 | S000345 |
| term_number | 1 | 5 | 5 |
| term_id | Z000018-1 | L000076-5 | S000345-5 |
| term_type | rep | rep | rep |
| term_start | 2017-01-03 | 1929-04-15 | 1899-12-04 |
| term_end | 2017-03-01 | 1931-03-03 | 1901-03-03 |
| state | MT | TX | NY |
| district | 0 | 12 | 25 |
| class | null | null | null |
| party | Republican | Democrat | Republican |
| how | null | null | null |
| url | https://zinke.house.gov | null | null |
| address | 1419 Longworth HOB; Washington DC 20515-2600 | null | null |
| phone | 202-225-3211 | null | null |
| fax | 202-225-5687 | null | null |
| contact_form | null | null | null |
| office | 1419 Longworth House Office Building | null | null |
| state_rank | null | null | null |
| rss_url | null | null | null |
| caucus | null | null | null |

# "skills_dim"  (rows=26)

columns:
"skill_id" int: unique identifier, 1..250
"skills" text: all distinct
"type" text: "programming"=9, "analyst_tools"=4, "databases"=4, "cloud"=3, "webframeworks"=3, "async"=2, "sync"=1

indexes: none
fk: none

samples:
| column | latest | sample | sample |
|---|---|---|---|
| skill_id | 250 | 7 | 34 |
| skills | twilio | sas | objective-c |
| type | sync | programming | programming |

# "skills_job_dim"  (rows=≈366960)

columns:
"job_id" int
"skill_id" int

indexes: none
fk: none
