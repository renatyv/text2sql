---
generator: db-snooper
version: 0.0.26
generated_at_utc: 2026-08-16T08:08:45.073315Z
dialect: sqlite
database: /var/folders/9j/b9bx_drd53sc6zbpsqyrjy4h0000gn/T/dbsnoop-4f2l5yh6/city_legislation.sqlite
schema: main
---

# alien_data

```sql
CREATE TABLE "alien_data" (
"id" INTEGER,
  "first_name" TEXT,
  "last_name" TEXT,
  "email" TEXT,
  "gender" TEXT,
  "type" TEXT,
  "birth_year" INTEGER,
  "age" INTEGER,
  "favorite_food" TEXT,
  "feeding_frequency" TEXT,
  "aggressive" INTEGER,
  "occupation" TEXT,
  "current_location" TEXT,
  "state" TEXT,
  "us_region" TEXT,
  "country" TEXT
);
```

## Rows

- total=50000

| column | latest | sample | sample |
|---|---|---|---|
| id | 50000 | 45917 | 39949 |
| first_name | theressa | luther | wilek |
| last_name | wahncke | marking | jillions |
| email | twahncke12kv@telegraph.co.uk | lmarkingzfg@admin.ch | wjillionsuto@loc.gov |
| gender | female | male | male |
| type | green | flatwoods | grey |
| birth_year | 1822 | 1854 | 1687 |
| age | 202 | 170 | 337 |
| favorite_food | galapagos mockingbird | red howler monkey | sun gazer |
| feeding_frequency | never | once | never |
| aggressive | 1 | 1 | 0 |
| occupation | chief design engineer | marketing assistant | environmental tech |
| current_location | dayton | san jose | new york city |
| state | ohio | california | new york |
| us_region | great lakes | far west | mideast |
| country | united states | united states | united states |

## Columns

- id: unique identifier, int 1..50000
- first_name: 8392 distinct, nulls=4
- last_name: 31034 distinct
- email: all distinct
- gender: "female"=22730, "male"=22323, "non-binary"=4947
- type: "flatwoods"=10124, "nordic"=10033, "reptile"=9964, "green"=9948, "grey"=9931
- birth_year: 301 distinct, int 1672..1972
  - stats: average=1822.07, median=1823
- age: 301 distinct, int 52..352
  - stats: average=201.929, median=201
- favorite_food: 1498 distinct
- feeding_frequency: "once"=6490, "weekly"=6300, "never"=6290, "daily"=6283, "seldom"=6201, "yearly"=6192, "often"=6167, "monthly"=6077
- aggressive: 0=25053, 1=24947
- occupation: 195 distinct
- current_location: 461 distinct
- state: 51 distinct
- us_region: "southeast"=13856, "far west"=7885, "southwest"=7600, "mideast"=7205, "great lakes"=5725, "plains"=4052, "rocky mountain"=2006, "new england"=1671
- country: "united states"=50000


# aliens

```sql
CREATE TABLE "aliens" (
"id" INTEGER,
  "first_name" TEXT,
  "last_name" TEXT,
  "email" TEXT,
  "gender" TEXT,
  "type" TEXT,
  "birth_year" INTEGER
);
```

## Rows

- total=50000

| column | latest | sample | sample |
|---|---|---|---|
| id | 50000 | 13868 | 43728 |
| first_name | Theressa | Fania | Neda |
| last_name | Wahncke | Mintoft | Giottoi |
| email | twahncke12kv@telegraph.co.uk | fmintoftap7@sitemeter.com | ngiottoixqn@digg.com |
| gender | Female | Female | Bigender |
| type | Green | Grey | Green |
| birth_year | 1822 | 1890 | 1763 |

## Columns

- id: unique identifier, int 1..50000
- first_name: 8393 distinct
- last_name: 31037 distinct
- email: all distinct
- gender: "Female"=22730, "Male"=22323, "Bigender"=856, "Non-binary"=848, "Polygender"=847, "Agender"=828, "Genderfluid"=784, "Genderqueer"=784
- type: "Flatwoods"=10124, "Nordic"=10033, "Reptile"=9964, "Green"=9948, "Grey"=9931
- birth_year: 301 distinct, int 1672..1972
  - stats: average=1822.07, median=1823


# aliens_details

```sql
CREATE TABLE "aliens_details" (
"detail_id" INTEGER,
  "favorite_food" TEXT,
  "feeding_frequency" TEXT,
  "aggressive" INTEGER
);
```

## Rows

- total=50000

| column | latest | sample | sample |
|---|---|---|---|
| detail_id | 50000 | 17202 | 20477 |
| favorite_food | Galapagos mockingbird | Grey-footed squirrel | Possum, common brushtail |
| feeding_frequency | Never | Yearly | Monthly |
| aggressive | 1 | 0 | 0 |

## Columns

- detail_id: unique identifier, int 1..50000
- favorite_food: 1498 distinct
- feeding_frequency: "Once"=6490, "Weekly"=6300, "Never"=6290, "Daily"=6283, "Seldom"=6201, "Yearly"=6192, "Often"=6167, "Monthly"=6077
- aggressive: 0=25053, 1=24947


# aliens_location

```sql
CREATE TABLE "aliens_location" (
"loc_id" INTEGER,
  "current_location" TEXT,
  "state" TEXT,
  "country" TEXT,
  "occupation" TEXT
);
```

## Rows

- total=50000

| column | latest | sample | sample |
|---|---|---|---|
| loc_id | 50000 | 13643 | 5484 |
| current_location | Dayton | Vienna | Phoenix |
| state | Ohio | Virginia | Arizona |
| country | United States | United States | United States |
| occupation | Chief Design Engineer | Developer III | Human Resources Assistant I |

## Columns

- loc_id: unique identifier, int 1..50000
- current_location: 461 distinct
- state: 51 distinct
- country: "United States"=50000
- occupation: 195 distinct


# cities

```sql
CREATE TABLE "cities" (
"city_id" INTEGER,
  "city_name" TEXT,
  "latitude" REAL,
  "longitude" REAL,
  "country_code_2" TEXT,
  "capital" INTEGER,
  "population" REAL,
  "insert_date" TEXT
);
```

## Rows

- total=44622

| column | latest | sample | sample |
|---|---|---|---|
| city_id | 44622 | 29439 | 28669 |
| city_name | nordvik | patapatnam | defiance |
| latitude | 111.51 | 84.0833 | -84.3657 |
| longitude | 74.0165 | 18.75 | 41.2813 |
| country_code_2 | ru | in | us |
| capital | 0 | 0 | 0 |
| population | 0 | 15954 | 17155 |
| insert_date | 2022-04-27 | 2021-04-13 | 2022-12-01 |

## Columns

- city_id: unique identifier, int 1..44622
- city_name: 41062 distinct, nulls=1
- latitude: 37063 distinct, num -179.6..179.37
  - stats: average=14.5078, median=13.3804
- longitude: 34608 distinct, num -54.9333..81.7166
  - stats: average=25.9138, median=32.3286
- country_code_2: 236 distinct
- capital: 0=44376, 1=246
- population: 29611 distinct, nulls=305, num 0..3.7732e+07
  - stats: average=114467, median=20992
- insert_date: 943 distinct


# cities_countries

```sql
CREATE TABLE "cities_countries" (
"country_id" INTEGER,
  "country_name" TEXT,
  "country_code_2" TEXT,
  "country_code_3" TEXT,
  "region" TEXT,
  "sub_region" TEXT,
  "intermediate_region" TEXT,
  "created_on" TEXT
);
```

## Rows

- total=241

| column | latest | sample | sample |
|---|---|---|---|
| country_id | 256 | 39 | 231 |
| country_name | zambia | burundi | thailand |
| country_code_2 | zm | bi | th |
| country_code_3 | zmb | bdi | tha |
| region | africa | africa | asia |
| sub_region | subsaharan africa | subsaharan africa | southeastern asia |
| intermediate_region | eastern africa | eastern africa | null |
| created_on | 2024-07-18 | 2024-07-18 | 2024-07-18 |

## Columns

- country_id: unique identifier, int 1..256
- country_name: all distinct
- country_code_2: all distinct
- country_code_3: all distinct
- region: "africa"=59, "americas"=57, "asia"=50, "europe"=48, "oceania"=26, "antartica"=1
- sub_region: "subsaharan africa"=53, "latin america and the caribbean"=52, "western asia"=17, "southern europe"=16, "northern europe"=13, "southeastern asia"=11, "eastern europe"=10, "polynesia"=9, "southern asia"=9, "western europe"=9, "eastern asia"=8, "micronesia"=7, "northern africa"=6, "australia and new zealand"=5, "central asia"=5, "melanesia"=5, "northern america"=5, nulls=1
- intermediate_region: "caribbean"=28, "eastern africa"=22, "western africa"=17, "south america"=16, "middle africa"=9, "central america"=8, "southern africa"=5, "channel islands"=1, nulls=135
- created_on: "2024-07-18"=241


# cities_currencies

```sql
CREATE TABLE "cities_currencies" (
"currency_id" INTEGER,
  "country_code_2" TEXT,
  "currency_name" TEXT,
  "currency_code" TEXT
);
```

## Rows

- total=254

| column | latest | sample | sample |
|---|---|---|---|
| currency_id | 254 | 92 | 155 |
| country_code_2 | zw | gu | mz |
| currency_name | zimbabwe dollar | us dollar | mozambique metical |
| currency_code | zwl | usd | mzn |

## Columns

- currency_id: unique identifier, int 1..254
- country_code_2: 233 distinct
- currency_name: 165 distinct
- currency_code: 166 distinct, nulls=1


# cities_languages

```sql
CREATE TABLE "cities_languages" (
"language_id" INTEGER,
  "language" TEXT,
  "country_code_2" TEXT
);
```

## Rows

- total=608

| column | latest | sample | sample |
|---|---|---|---|
| language_id | 608 | 476 | 447 |
| language | shona | dutch | chuvash |
| country_code_2 | zw | sx | ru |

## Columns

- language_id: unique identifier, int 1..608
- language: 229 distinct
- country_code_2: 237 distinct


# job_company

```sql
CREATE TABLE "job_company" (
"company_id" INTEGER,
  "name" TEXT,
  "link" TEXT,
  "link_google" TEXT,
  "thumbnail" TEXT
);
```

## Rows

- total=14003

| column | latest | sample | sample |
|---|---|---|---|
| company_id | 787652 | 12554 | 357448 |
| name | Rotary Engineering Pte. Ltd. | Aeropm | BRIK |
| link | http://www.rotaryeng.com.sg/ | null | null |
| link_google | null | https://www.google.com/search?sca_esv=589510079&hl=en&gl=us&q=Aeropm&sa=X&ved=0ahUKEwiJsbPkmoSDAxXLFlkFHSU4BEg4ChCYkAIIxgs | https://www.google.com/search?sca_esv=572781667&hl=en&gl=us&q=BRIK&sa=X&ved=0ahUKEwjZx8Sk7u-BAxUjM1kFHeebDKAQmJACCI4L |
| thumbnail | https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQcgZKxQBsMj83FmbDN7BE6mCKD63zc8F70HMUOUllYYRByt3Pz_q_c&s | https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcRy7BDVLI1v0TTiEd_1-A9erQIeLXnbzmstT3FzCrk&s | null |

## Columns

- company_id: unique identifier, int 31..787652
- name: all distinct
- link: 5008 distinct, nulls=8648
- link_google: all distinct, nulls=5
- thumbnail: 6032 distinct, nulls=5884


# job_postings_fact

```sql
CREATE TABLE "job_postings_fact" (
"job_id" INTEGER,
  "company_id" INTEGER,
  "job_title_short" TEXT,
  "job_title" TEXT,
  "job_location" TEXT,
  "job_via" TEXT,
  "job_schedule_type" TEXT,
  "job_work_from_home" INTEGER,
  "search_location" TEXT,
  "job_posted_date" TEXT,
  "job_no_degree_mention" INTEGER,
  "job_health_insurance" INTEGER,
  "job_country" TEXT,
  "salary_rate" TEXT,
  "salary_year_avg" REAL,
  "salary_hour_avg" REAL
);
```

## Rows

- total=78769

| column | latest | sample | sample |
|---|---|---|---|
| job_id | 1826663 | 88 | 67405 |
| company_id | 87729 | 4190 | 184820 |
| job_title_short | Data Scientist | Data Scientist | Machine Learning Engineer |
| job_title | Data Scientist, Data Science – Bangalore, Karnataka – Cardinal Health | Data Scientist II (Hybrid/Remote) | Product engineer in Mol |
| job_location | Anywhere | Jacksonville, FL | Antwerp, Belgium |
| job_via | via MySmartPros | via Diversity Jobs | via BeBee Belgique |
| job_schedule_type | Full-time | Full-time | Full-time |
| job_work_from_home | 1 | 0 | 0 |
| search_location | India | Florida, United States | Belgium |
| job_posted_date | 2023-03-21 20:33:44 | 2023-06-21 12:05:49 | 2023-09-23 07:36:17 |
| job_no_degree_mention | 0 | 0 | 0 |
| job_health_insurance | 0 | 1 | 0 |
| job_country | India | United States | Belgium |
| salary_rate | null | null | null |
| salary_year_avg | null | null | null |
| salary_hour_avg | null | null | null |

## Columns

- job_id: unique identifier, int 23..1826663
- company_id: 34870 distinct, int 2..787360
- job_title_short: "Data Analyst"=19743, "Data Engineer"=18878, "Data Scientist"=17189, "Business Analyst"=4948, "Software Engineer"=4459, "Senior Data Engineer"=4411, "Senior Data Scientist"=3679, "Senior Data Analyst"=2891, "Machine Learning Engineer"=1405, "Cloud Engineer"=1166
- job_title: 37666 distinct, nulls=1
- job_location: 6061 distinct, nulls=102
- job_via: 2410 distinct, nulls=3
- job_schedule_type: 33 distinct, nulls=1300
- job_work_from_home: 0=71755, 1=7014
- search_location: 159 distinct
- job_posted_date: 75984 distinct
- job_no_degree_mention: 0=54549, 1=24220
- job_health_insurance: 0=70203, 1=8566
- job_country: 150 distinct, nulls=6
- salary_rate: "year"=2174, "hour"=1090, "month"=23, "day"=1, "week"=1, nulls=75480
- salary_year_avg: 618 distinct, nulls=76595, num 23496..375000
  - stats: average=122397, median=115000
- salary_hour_avg: 334 distinct, nulls=77679, num 8.5..391
  - stats: average=47.737, median=46.3775


# legislation_date_dim

```sql
CREATE TABLE "legislation_date_dim" (
"date" TEXT,
  "month_name" TEXT,
  "day_of_month" INTEGER
);
```

## Rows

- total=30315

| column | latest | sample | sample |
|---|---|---|---|
| date | 1999-12-31 | 1967-07-11 | 1952-10-06 |
| month_name | December | July | October |
| day_of_month | 31 | 11 | 6 |

## Columns

- date: all distinct
- month_name: "August"=2573, "December"=2573, "January"=2573, "July"=2573, "March"=2573, "May"=2573, "October"=2573, "April"=2490, "June"=2490, "November"=2490, "September"=2490, "February"=2344
- day_of_month: 31 distinct, int 1..31
  - stats: average=15.7293, median=16


# legislators

```sql
CREATE TABLE "legislators" (
"full_name" TEXT,
  "first_name" TEXT,
  "last_name" TEXT,
  "middle_name" TEXT,
  "nickname" TEXT,
  "suffix" TEXT,
  "other_names_end" TEXT,
  "other_names_middle" REAL,
  "other_names_last" TEXT,
  "birthday" TEXT,
  "gender" TEXT,
  "id_bioguide" TEXT,
  "id_bioguide_previous_0" TEXT,
  "id_govtrack" INTEGER,
  "id_icpsr" REAL,
  "id_wikipedia" TEXT,
  "id_wikidata" TEXT,
  "id_google_entity_id" TEXT,
  "id_house_history" REAL,
  "id_house_history_alternate" REAL,
  "id_thomas" REAL,
  "id_cspan" REAL,
  "id_votesmart" REAL,
  "id_lis" TEXT,
  "id_ballotpedia" TEXT,
  "id_opensecrets" TEXT,
  "id_fec_0" TEXT,
  "id_fec_1" TEXT,
  "id_fec_2" TEXT
);
```

## Rows

- total=12518

| column | latest | sample | sample |
|---|---|---|---|
| full_name | Zoe Lofgren | William Parker Cutler | Thomas Jefferson Rusk |
| first_name | Zoe | William | Thomas |
| last_name | Lofgren | Cutler | Rusk |
| middle_name | null | Parker | Jefferson |
| nickname | null | null | null |
| suffix | null | null | null |
| other_names_end | null | null | null |
| other_names_middle | null | null | null |
| other_names_last | null | null | null |
| birthday | 1947-12-21 | 1812-07-12 | 1803-12-05 |
| gender | F | M | M |
| id_bioguide | L000397 | C001027 | R000518 |
| id_bioguide_previous_0 | null | null | null |
| id_govtrack | 400245 | 403134 | 409476 |
| id_icpsr | 29504 | 2288 | 8121 |
| id_wikipedia | Zoe Lofgren | William P. Cutler | Thomas Jefferson Rusk |
| id_wikidata | Q218217 | Q6814836 | Q2290948 |
| id_google_entity_id | kg:/m/024t94 | kg:/m/02rm3rh | kg:/m/037_c0 |
| id_house_history | 17087 | 11734 | null |
| id_house_history_alternate | null | null | null |
| id_thomas | 701 | null | null |
| id_cspan | 36520 | null | null |
| id_votesmart | 21899 | null | null |
| id_lis | null | null | null |
| id_ballotpedia | Zoe Lofgren | null | null |
| id_opensecrets | [REDACTED] | [REDACTED] | [REDACTED] |
| id_fec_0 | H4CA16049 | null | null |
| id_fec_1 | null | null | null |
| id_fec_2 | null | null | null |

## Columns

- full_name: 12310 distinct
- first_name: 1684 distinct
- last_name: 5724 distinct
- middle_name: 2914 distinct, nulls=3959
- nickname: 131 distinct, nulls=12262
- suffix: "Jr."=383, "III"=31, "Sr."=13, "II"=10, "IV"=3, nulls=12078
- other_names_end: "1846-01-12"=1, "1995-01-03"=1, "1995-09-03"=1, "2007-12-17"=1, nulls=12514
- other_names_middle: all NULL
- other_names_last: "Bono"=1, "Lambert"=1, "Levy"=1, "Long"=1, "Menendez"=1, nulls=12513
- birthday: 11038 distinct, nulls=551
- gender: "M"=12152, "F"=366
- id_bioguide: all distinct
- id_bioguide_previous_0: "F000246"=1, "L000266"=1, "W000790"=1, nulls=12515
- id_govtrack: all distinct, int 300001..456792
  - stats: average=405486, median=406348
- id_icpsr: all distinct, nulls=220, num 1..99342
  - stats: average=7968.1, median=6441.5
- id_wikipedia: all distinct, nulls=2
- id_wikidata: all distinct, nulls=2
- id_google_entity_id: all distinct, nulls=69
- id_house_history: all distinct, nulls=1492, num 7672..1.50324e+10
  - stats: average=6.00041e+07, median=16356.5
- id_house_history_alternate: 13283=1, nulls=12517
- id_thomas: all distinct, nulls=10337, num 1..2296
  - stats: average=1110.53, median=1092
- id_cspan: all distinct, nulls=11664, num 5..9.27826e+06
  - stats: average=569127, median=76348
- id_votesmart: all distinct, nulls=11437, num 0..182310
  - stats: average=58344.8, median=29674
- id_lis: all distinct, nulls=12226
- id_ballotpedia: all distinct, nulls=11998
- id_opensecrets: all distinct, nulls=11309
- id_fec_0: all distinct, nulls=11435
- id_fec_1: all distinct, nulls=12408
- id_fec_2: "H0GA03017"=1, "H0MD07114"=1, "P80003247"=1, "S0NV00237"=1, "S4TN00096"=1, "S8ND00120"=1, nulls=12512


# legislators_terms

```sql
CREATE TABLE "legislators_terms" (
"id_bioguide" TEXT,
  "term_number" INTEGER,
  "term_id" TEXT,
  "term_type" TEXT,
  "term_start" TEXT,
  "term_end" TEXT,
  "state" TEXT,
  "district" REAL,
  "class" REAL,
  "party" TEXT,
  "how" TEXT,
  "url" TEXT,
  "address" TEXT,
  "phone" TEXT,
  "fax" TEXT,
  "contact_form" TEXT,
  "office" TEXT,
  "state_rank" TEXT,
  "rss_url" TEXT,
  "caucus" TEXT
);
```

## Rows

- total=44063

| column | latest | sample | sample |
|---|---|---|---|
| id_bioguide | Z000018 | R000159 | S000500 |
| term_number | 1 | 2 | 9 |
| term_id | Z000018-1 | R000159-2 | S000500-9 |
| term_type | rep | rep | rep |
| term_start | 2017-01-03 | 1969-01-03 | 1917-04-02 |
| term_end | 2017-03-01 | 1971-01-03 | 1919-03-03 |
| state | MT | CA | NC |
| district | 0 | 27 | 1 |
| class | null | null | null |
| party | Republican | Republican | Democrat |
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

## Columns

- id_bioguide: 12518 distinct
- term_number: 30 distinct, int 0..29
  - stats: average=2.86717, median=2
- term_id: unique identifier
- term_type: "rep"=40190, "sen"=3873
- term_start: 721 distinct
- term_end: 632 distinct
- state: 59 distinct
- district: 55 distinct, nulls=3873, num -1..53
  - stats: average=8.39005, median=6
- class: 2=1317, 3=1279, 1=1277, nulls=40190, num 1..3
- party: 67 distinct, nulls=452
- how: "appointment"=201, nulls=43862
- url: 2081 distinct, nulls=39677
- address: 1807 distinct, nulls=41564
- phone: 554 distinct, nulls=41569
- fax: 575 distinct, nulls=42251
- contact_form: 953 distinct, nulls=42633
- office: 601 distinct, nulls=41571
- state_rank: "senior"=120, "junior"=97, nulls=43846
- rss_url: 511 distinct, nulls=42574
- caucus: "Democrat"=14, nulls=44049


# skills_dim

```sql
CREATE TABLE "skills_dim" (
"skill_id" INTEGER,
  "skills" TEXT,
  "type" TEXT
);
```

## Rows

- total=26

| column | latest | sample | sample |
|---|---|---|---|
| skill_id | 250 | 34 | 140 |
| skills | twilio | objective-c | vue.js |
| type | sync | programming | webframeworks |

## Columns

- skill_id: unique identifier, int 1..250
- skills: all distinct
- type: "programming"=9, "analyst_tools"=4, "databases"=4, "cloud"=3, "webframeworks"=3, "async"=2, "sync"=1


# skills_job_dim

```sql
CREATE TABLE "skills_job_dim" (
"job_id" INTEGER,
  "skill_id" INTEGER
);
```

## Rows

- total≈366960 (estimated from db stats; row/column profiling skipped)
