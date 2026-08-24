---
generator: db-snooper
version: 0.0.34
generated_at_utc: 2026-08-24T21:58:33.529267Z
dialect: sqlite
database: /var/folders/9j/b9bx_drd53sc6zbpsqyrjy4h0000gn/T/dbsnoop-bpl9u64p/complex_oracle.sqlite
schema: main
---

## Relationships

- "channels"."channel_id" ← "costs"."channel_id", "sales"."channel_id"
- "countries"."country_id" ← "customers"."country_id"
- "customers"."cust_id" ← "sales"."cust_id"
- "products"."prod_id" ← "costs"."prod_id", "sales"."prod_id"
- "promotions"."promo_id" ← "costs"."promo_id", "sales"."promo_id"
- "times"."time_id" ← "costs"."time_id", "sales"."time_id"

# "cal_month_sales_mv"  (rows=48)

```sql
CREATE VIEW cal_month_sales_mv AS
SELECT
   t.calendar_month_desc,
   SUM(s.amount_sold) AS dollars
FROM
   sales s
   JOIN times t ON s.time_id = t.time_id
GROUP BY
   t.calendar_month_desc;
```

columns:
"calendar_month_desc" text: all distinct
"dollars" float: all distinct

samples:
| column | latest | sample | sample |
|---|---|---|---|
| calendar_month_desc | 2022-12 | 2019-11 | 2019-12 |
| dollars | 2.5e+06 | 2e+06 | 1.7e+06 |

# "channels"  (rows=5)

columns:
"channel_id" int PK
"channel_desc" text NOTNULL
"channel_class" text NOTNULL
"channel_class_id" int NOTNULL
"channel_total" text NOTNULL
"channel_total_id" int NOTNULL

indexes: none

all rows:
| column | row 1 | row 2 | row 3 | row 4 | row 5 |
|---|---|---|---|---|---|
| channel_id | 2 | 3 | 4 | 5 | 9 |
| channel_desc | Partners | Direct Sales | Internet | Catalog | Tele Sales |
| channel_class | Others | Direct | Indirect | Indirect | Direct |
| channel_class_id | 14 | 12 | 13 | 13 | 12 |
| channel_total | Channel total | Channel total | Channel total | Channel total | Channel total |
| channel_total_id | 1 | 1 | 1 | 1 | 1 |

# "costs"  (rows=82112)

columns:
"prod_id" int NOTNULL FK: 72 distinct, 13..148
"time_id" date NOTNULL FK: 1459 distinct
"promo_id" int NOTNULL FK: 999=78425, 351=2182, 350=1505, 350..999
"channel_id" int NOTNULL FK: 3=35104, 2=27635, 4=19373, 2..4
"unit_cost" float NOTNULL: 5675 distinct, -23.74..1342.06, avg=117.759, median=28.39
"unit_price" float NOTNULL: 3609 distinct, 6.4..1782.72, avg=148.246, median=38.12

indexes: "channel_id", "promo_id"

samples:
| column | latest | sample | sample |
|---|---|---|---|
| prod_id | 148 | 36 | 30 |
| time_id | 2022-12-28 | 2019-01-07 | 2021-09-19 |
| promo_id | 999 | 999 | 999 |
| channel_id | 4 | 4 | 4 |
| unit_cost | 17.36 | 38.09 | 8.29 |
| unit_price | 21.98 | 49.01 | 9.35 |

# "countries"  (rows=35)

columns:
"country_id" int PK: unique identifier, 52769..52803
"country_iso_code" char2 NOTNULL: all distinct
"country_name" text NOTNULL: all distinct
"country_subregion" text NOTNULL: "Western Europe"=11, "Asia"=6, "Middle East"=4, "Africa"=3, "Eastern Europe"=3, "Northern America"=3, "Southern America"=3, "Australia"=2
"country_subregion_id" int NOTNULL: 52799=11, 52793=6, 52796=4, 52792=3, 52795=3, 52797=3, 52798=3, 52794=2, 52792..52799
"country_region" text NOTNULL: "Europe"=14, "Americas"=6, "Asia"=6, "Middle East"=4, "Africa"=3, "Oceania"=2
"country_region_id" int NOTNULL: 52803=14, 52802=6, 52801=5, 52804=4, 52800=3, 52805=2, 52798=1, 52798..52805
"country_total" text NOTNULL: "World total"=35
"country_total_id" int NOTNULL: 52806=35

indexes: none

samples:
| column | latest | sample | sample |
|---|---|---|---|
| country_id | 52803 | 52784 | 52790 |
| country_iso_code | HU | NL | US |
| country_name | Hungary | Netherlands | United States of America |
| country_subregion | Eastern Europe | Western Europe | Northern America |
| country_subregion_id | 52795 | 52799 | 52797 |
| country_region | Europe | Europe | Americas |
| country_region_id | 52803 | 52803 | 52801 |
| country_total | World total | World total | World total |
| country_total_id | 52806 | 52806 | 52806 |

# "currency"  (rows=1260)

columns:
"country" text: 35 distinct
"year" int: 2019=420, 2020=420, 2021=420, 2019..2021
"month" int: 1=105, 2=105, 3=105, 4=105, 5=105, 6=105, 7=105, 8=105, 9=105, 10=105, 11=105, 12=105, 1..12
"to_us" float: 1=1224, 0.74=36

indexes: none

samples:
| column | latest | sample | sample |
|---|---|---|---|
| country | Zimbabwe | Germany | Mexico |
| year | 2021 | 2021 | 2020 |
| month | 12 | 8 | 11 |
| to_us | 1 | 1 | 1 |

# "customers"  (rows=55500)

columns:
"cust_id" int PK: unique identifier, 1..104500
"cust_first_name" text NOTNULL: 1304 distinct
"cust_last_name" text NOTNULL: 916 distinct
"cust_gender" char1 NOTNULL: "M"=37175, "F"=18325
"cust_year_of_birth" int NOTNULL: 75 distinct, 1924..2001, avg=1968.4, median=1967
"cust_marital_status" text: "single"=19094, "married"=16287, "never married"=1503, "divorced"=765, "widowed"=211, "separated"=134, nulls=17506
"cust_street_address" text NOTNULL: 50945 distinct
"cust_postal_code" text NOTNULL: digits, 623 distinct
"cust_city" text NOTNULL: 620 distinct
"cust_city_id" int NOTNULL: 620 distinct, 51040..52531
"cust_state_province" text NOTNULL: 145 distinct
"cust_state_province_id" int NOTNULL: 145 distinct, 52533..52771
"country_id" int NOTNULL FK: 52790=18520, 52776=8173, 52770=7780, 52789=7557, 52779=3833, 52778=2039, 52772=2010, 52775=832, 52774=831, 52771=712, 52786=708, 52782=624, 52769=597, 52773=403, 52777=383, 52785=244, 52788=91, 52791=88, 52787=75, 52769..52791
"cust_main_phone_number" text NOTNULL: 51000 distinct
"cust_income_level" text: "F: 110,000 - 129,999"=10537, "E: 90,000 - 109,999"=7936, "G: 130,000 - 149,999"=5465, "H: 150,000 - 169,999"=5465, "D: 70,000 - 89,999"=5217, "I: 170,000 - 189,999"=4566, "C: 50,000 - 69,999"=4255, "J: 190,000 - 249,999"=3006, "B: 30,000 - 49,999"=2764, "A: Below 30,000"=2630, "K: 250,000 - 299,999"=1934, "L: 300,000 and above"=1684, nulls=41
"cust_credit_limit" float: 1500=11334, 9000=9093, 7000=8634, 3000=7975, 5000=7724, 10000=5935, 11000=2935, 15000=1870, 1500..15000
"cust_email" text: 1706 distinct
"cust_total" text NOTNULL: "Customer total"=55500
"cust_total_id" int NOTNULL: 52772=55500
"cust_src_id" int: all NULL
"cust_eff_from" date: "2019-01-01"=55500
"cust_eff_to" date: all NULL
"cust_valid" char1: "I"=44879, "A"=10621

indexes: none

samples:
| column | latest | sample | sample |
|---|---|---|---|
| cust_id | 104500 | 50583 | 17595 |
| cust_first_name | Lauren | August | Deanna |
| cust_last_name | Fenton | Laycock | Painter |
| cust_gender | F | F | F |
| cust_year_of_birth | 1973 | 1982 | 1957 |
| cust_marital_status | divorced | null | single |
| cust_street_address | 47 South Guayanilla Road | 27 South Pickaway Boulevard | 67 East Poinsett Avenue |
| cust_postal_code | 68524 | 78558 | 39318 |
| cust_city | Glasco | Los Angeles | Torrevieja |
| cust_city_id | 51583 | 51806 | 52374 |
| cust_state_province | KS | CA | Alicante |
| cust_state_province_id | 52630 | 52567 | 52544 |
| country_id | 52790 | 52790 | 52778 |
| cust_main_phone_number | 236-199-2209 | 444-346-5634 | 239-792-7522 |
| cust_income_level | K: 250,000 - 299,999 | D: 70,000 - 89,999 | F: 110,000 - 129,999 |
| cust_credit_limit | 15000 | 10000 | 9000 |
| cust_email | Fenton@company.example.com | Laycock@company.example.com | Painter@company.example.com |
| cust_total | Customer total | Customer total | Customer total |
| cust_total_id | 52772 | 52772 | 52772 |
| cust_src_id | null | null | null |
| cust_eff_from | 2019-01-01 | 2019-01-01 | 2019-01-01 |
| cust_eff_to | null | null | null |
| cust_valid | A | I | I |

# "fweek_pscat_sales_mv"  (rows=3652)

```sql
CREATE VIEW fweek_pscat_sales_mv AS
SELECT
   t.week_ending_day,
   p.prod_subcategory,
   SUM(s.amount_sold) AS dollars,
   s.channel_id,
   s.promo_id
FROM
   sales s
   JOIN times t ON s.time_id = t.time_id
   JOIN products p ON s.prod_id = p.prod_id
GROUP BY
   t.week_ending_day,
   p.prod_subcategory,
   s.channel_id,
   s.promo_id;
```

columns:
"week_ending_day" date: 209 distinct
"prod_subcategory" text: "Baseballs"=642, "Cricket Bat"=633, "Bats"=631, "Training Aids and Equipment"=604, "Cricket Fan Gear"=584, "Cricket"=558
"dollars" float: 3545 distinct
"channel_id" int: 3=1361, 2=1202, 4=1053, 9=36, 2..9
"promo_id" int: 999=3384, 350=119, 351=113, 33=36, 33..999

samples:
| column | latest | sample | sample |
|---|---|---|---|
| week_ending_day | 2023-01-01 | 2022-08-14 | 2019-09-15 |
| prod_subcategory | Training Aids and Equipment | Training Aids and Equipment | Bats |
| dollars | 25186.4 | 1190.69 | 10987.7 |
| channel_id | 3 | 3 | 4 |
| promo_id | 351 | 351 | 999 |

# "products"  (rows=24)

columns:
"prod_id" int PK: unique identifier, 14..130
"prod_name" text NOTNULL: "Team shirt"=6, "2 Competition Grade NFHS Baseballs"=1, "6 Gallon Empty Ball Bucket"=1, "Cricket Bat Bag"=1, "Cricket Bat Pad"=1, "Cricket Gloves"=1, "English Willow Cricket Bat"=1, "Fiber Tape"=1, "Genuine Series MIX Wood Bat"=1, "Indoor Cricket Ball"=1, "Linseed Oil"=1, "MLB Official Game Baseball w/ Display Case"=1, "Outdoor Cricket Ball"=1, "Pitching Machine and Batting Cage Combo"=1, "Plastic Cricket Bat"=1, "Pro Maple Bat"=1, "Pro Maple Youth Bat"=1, "Slugger Youth Series Maple Bat"=1, "Speed Trainer Bats and Training Program"=1
"prod_desc" text NOTNULL: all distinct
"prod_subcategory" text NOTNULL: "Cricket Fan Gear"=6, "Cricket Bat"=5, "Bats"=4, "Cricket"=4, "Baseballs"=3, "Training Aids and Equipment"=2
"prod_subcategory_id" int NOTNULL: 2054=6, 2051=5, 2036=4, 2055=4, 2031=3, 2035=2, 2031..2055
"prod_subcategory_desc" text NOTNULL: "Cricket Fan Gear"=6, "Cricket"=5, "Bats"=4, "Cricket Bat"=4, "Baseballs"=3, "Training Aids and Equipment"=2
"prod_category" text NOTNULL: "Cricket"=15, "Baseball"=9
"prod_category_id" int NOTNULL: 205=15, 203=9
"prod_category_desc" text NOTNULL: "Cricket"=15, "Baseball"=9
"prod_weight_class" int NOTNULL: 1=24
"prod_unit_of_measure" text: "U"=24
"prod_pack_size" text NOTNULL: "P"=24
"supplier_id" int NOTNULL: 1=24
"prod_status" text NOTNULL: "STATUS"=24
"prod_list_price" float NOTNULL: 44.99=6, 8.99=1, 9.99=1, 11.99=1, 15.99=1, 19.99=1, 21.99=1, 22.99=1, 24.99=1, 27.99=1, 28.99=1, 29.99=1, 36.99=1, 55.99=1, 89.99=1, 192.99=1, 199.99=1, 899.99=1, 999.99=1, 8.99..999.99
"prod_min_price" float NOTNULL: 44.99=6, 8.99=1, 9.99=1, 11.99=1, 15.99=1, 19.99=1, 21.99=1, 22.99=1, 24.99=1, 27.99=1, 28.99=1, 29.99=1, 36.99=1, 55.99=1, 89.99=1, 192.99=1, 199.99=1, 899.99=1, 999.99=1, 8.99..999.99
"prod_total" text NOTNULL: "TOTAL"=24
"prod_total_id" int NOTNULL: 1=24
"prod_src_id" int→text: ""=24
"prod_eff_from" date: "2019-01-01 00:00:00"=24
"prod_eff_to" date: ""=24
"prod_valid" char1: "A"=24

indexes: none

- latest rows skipped (unreadable values); random rows skipped (unreadable values)

# "profits"  (rows=916039)

```sql
CREATE VIEW profits AS
SELECT 
  s.channel_id, 
  s.cust_id, 
  s.prod_id, 
  s.promo_id, 
  s.time_id,
  c.unit_cost, 
  c.unit_price, 
  s.amount_sold, 
  s.quantity_sold,
  c.unit_cost * s.quantity_sold AS TOTAL_COST
FROM 
  costs c
  JOIN sales s ON c.prod_id = s.prod_id
               AND c.time_id = s.time_id
               AND c.channel_id = s.channel_id
               AND c.promo_id = s.promo_id;
```

columns:
"channel_id" int: 2..4
"cust_id" int: 2..50840
"prod_id" int: 13..148
"promo_id" int: 350..999
"time_id" date: profile metrics skipped
"unit_cost" float: -23.74..1342.06, avg=84.8406
"unit_price" float: 6.4..1782.72, avg=106.807
"amount_sold" float: 6.4..1782.72, avg=106.807
"quantity_sold" int: 1..1, avg=1
"TOTAL_COST" float: profile metrics skipped

samples:
| column | latest | sample | sample |
|---|---|---|---|
| channel_id | 4 | 3 | 3 |
| cust_id | 50840 | 7657 | 1817 |
| prod_id | 148 | 120 | 134 |
| promo_id | 999 | 999 | 999 |
| time_id | 2022-08-02 | 2019-05-24 | 2021-10-31 |
| unit_cost | 17.28 | 6.37 | 20.36 |
| unit_price | 22.14 | 9.09 | 22.31 |
| amount_sold | 22.14 | 9.09 | 22.31 |
| quantity_sold | 1 | 1 | 1 |
| TOTAL_COST | 17.28 | 6.37 | 20.36 |

# "promotions"  (rows=503)

columns:
"promo_id" int PK: unique identifier, 33..999
"promo_name" text NOTNULL: all distinct
"promo_subcategory" text NOTNULL: 22 distinct
"promo_subcategory_id" int NOTNULL: 22 distinct, 11..32
"promo_category" text NOTNULL: "TV"=115, "newspaper"=110, "internet"=85, "magazine"=65, "post"=65, "flyer"=40, "radio"=20, "ad news"=2, "NO PROMOTION"=1
"promo_category_id" int NOTNULL: 3=115, 8=110, 6=85, 7=65, 9=65, 5=40, 10=20, 4=2, 2=1, 2..10
"promo_cost" float NOTNULL: 501 distinct, 0..100000, avg=50160.8, median=51600
"promo_begin_date" date NOTNULL: 192 distinct
"promo_end_date" date NOTNULL: 191 distinct
"promo_total" text NOTNULL: "Promotion total"=503
"promo_total_id" int NOTNULL: 1=503

indexes: none

samples:
| column | latest | sample | sample |
|---|---|---|---|
| promo_id | 999 | 288 | 395 |
| promo_name | NO PROMOTION # | TV promotion #13-288 | newspaper promotion #19-395 |
| promo_subcategory | NO PROMOTION | TV program sponsorship | coupon news |
| promo_subcategory_id | 11 | 13 | 19 |
| promo_category | NO PROMOTION | TV | newspaper |
| promo_category_id | 2 | 3 | 8 |
| promo_cost | 0 | 15200 | 97000 |
| promo_begin_date | 9999-01-01 | 2021-08-07 | 2021-08-28 |
| promo_end_date | 9999-01-01 | 2021-09-07 | 2021-09-28 |
| promo_total | Promotion total | Promotion total | Promotion total |
| promo_total_id | 1 | 1 | 1 |

# "sales"  (rows=≈918843)

columns:
"prod_id" int NOTNULL FK
"cust_id" int NOTNULL FK
"time_id" date NOTNULL FK
"channel_id" int NOTNULL FK
"promo_id" int NOTNULL FK
"quantity_sold" int NOTNULL
"amount_sold" float NOTNULL

indexes: none


# "supplementary_demographics"  (rows=4500)

columns:
"cust_id" int PK: unique identifier, 100001..104500
"education" text: "HS-grad"=1462, "< Bach."=1041, "Bach."=779, "Assoc-V"=196, "Masters"=190, "Assoc-A"=172, "10th"=122, "11th"=121, "Profsc"=94, "7th-8th"=87, "9th"=76, "12th"=52, "PhD"=49, "5th-6th"=39, "1st-4th"=17, "Presch."=3
"occupation" text: "Crafts"=572, "Sales"=560, "Exec."=559, "Prof."=545, "Cleric."=520, "Other"=468, "Machine"=276, "?"=236, "Transp."=187, "TechSup"=177, "Handler"=168, "Farming"=122, "Protec."=89, "House-s"=19, "Armed-F"=2
"household_size" text: "3"=1787, "2"=1149, "1"=692, "9+"=505, "4-5"=219, "6-8"=148
"yrs_residence" int: 3=961, 4=937, 5=757, 2=625, 6=473, 1=276, 7=231, 8=101, 9=49, 0=48, 10=25, 11=9, 12=3, 14=3, 13=2, 0..14
"affinity_card" int: 0=3428, 1=1072
"cricket" int: 1=2868, 0=1632
"baseball" int: 1=2597, 0=1903
"tennis" int: 1=2539, 0=1961
"soccer" int: 1=3983, 0=517
"golf" int: 1=4500
"unknown" int: 0=3094, 1=1406
"misc" int: 0=4489, 1=11
"comments" text: 44 distinct, nulls=205

indexes: none

samples:
| column | latest | sample | sample |
|---|---|---|---|
| cust_id | 104500 | 100578 | 101138 |
| education | HS-grad | HS-grad | < Bach. |
| occupation | Crafts | Protec. | Sales |
| household_size | 9+ | 2 | 1 |
| yrs_residence | 5 | 3 | 1 |
| affinity_card | 0 | 0 | 0 |
| cricket | 1 | 1 | 1 |
| baseball | 1 | 1 | 1 |
| tennis | 1 | 1 | 0 |
| soccer | 1 | 1 | 1 |
| golf | 1 | 1 | 1 |
| unknown | 0 | 0 | 1 |
| misc | 0 | 0 | 0 |
| comments | Affinity card is a great idea. But your store is still too expensive. I am tired of your lousy junk mail. | I am not going to waste my time filling up this three page form. Lousy idea. | A great program but I have to complain just a bit. Why do you need to know how many children I have, where I shop, etc.?  Give us a discount for shopping at your store, but don't ask too many persona… |

# "times"  (rows=1826)

columns:
"time_id" date PK: unique identifier
"day_name" text NOTNULL: "Friday"=261, "Saturday"=261, "Sunday"=261, "Thursday"=261, "Tuesday"=261, "Wednesday"=261, "Monday"=260
"day_number_in_week" int NOTNULL: 2=261, 3=261, 4=261, 5=261, 6=261, 7=261, 1=260, 1..7
"day_number_in_month" int NOTNULL: 31 distinct, 1..31, avg=15.7278, median=16
"calendar_week_number" int NOTNULL: 53 distinct, 1..53, avg=26.5871, median=27
"fiscal_week_number" int NOTNULL: 53 distinct, 1..53, avg=26.5871, median=27
"week_ending_day" date NOTNULL: 261 distinct
"week_ending_day_id" int NOTNULL: 262 distinct, 1462..2257
"calendar_month_number" int NOTNULL: 1=155, 3=155, 5=155, 7=155, 8=155, 10=155, 12=155, 4=150, 6=150, 9=150, 11=150, 2=141, 1..12
"fiscal_month_number" int NOTNULL: 12=161, 4=154, 5=154, 7=154, 8=154, 9=154, 10=154, 1=153, 3=153, 6=147, 11=147, 2=141, 1..12
"calendar_month_desc" text NOTNULL: 60 distinct
"calendar_month_id" int NOTNULL: 60 distinct, 1672..2223
"fiscal_month_desc" text NOTNULL: 61 distinct
"fiscal_month_id" int NOTNULL: 61 distinct, 1720..2258
"days_in_cal_month" int NOTNULL: 31=1085, 30=600, 28=112, 29=29, 28..31
"days_in_fis_month" int NOTNULL: 28=1066, 35=735, 25=25, 25..35
"end_of_cal_month" date NOTNULL: 60 distinct
"end_of_fis_month" date NOTNULL: 61 distinct
"calendar_month_name" text NOTNULL: "August"=155, "December"=155, "January"=155, "July"=155, "March"=155, "May"=155, "October"=155, "April"=150, "June"=150, "November"=150, "September"=150, "February"=141
"fiscal_month_name" text NOTNULL: "December"=161, "April"=154, "August"=154, "July"=154, "May"=154, "October"=154, "September"=154, "January"=153, "March"=153, "June"=147, "November"=147, "February"=141
"calendar_quarter_desc" char7 NOTNULL: 20 distinct
"calendar_quarter_id" int NOTNULL: 20 distinct, 1769..2150
"fiscal_quarter_desc" char7 NOTNULL: 21 distinct
"fiscal_quarter_id" int NOTNULL: 21 distinct, 1785..2260
"days_in_cal_quarter" int NOTNULL: 92=920, 91=545, 90=361, 90..92
"days_in_fis_quarter" int NOTNULL: 91=1367, 98=196, 1=91, 88=88, 84=84, 1..98
"end_of_cal_quarter" date NOTNULL: 20 distinct
"end_of_fis_quarter" date NOTNULL: 21 distinct
"calendar_quarter_number" int NOTNULL: 3=460, 4=460, 2=455, 1=451, 1..4
"fiscal_quarter_number" int NOTNULL: 3=462, 4=462, 2=455, 1=447, 1..4
"calendar_year" int NOTNULL: 2020=366, 2019=365, 2021=365, 2022=365, 2023=365, 2019..2023
"calendar_year_id" int NOTNULL: 1803=366, 1802=365, 1804=365, 1805=365, 1813=365, 1802..1813
"fiscal_year" int NOTNULL: 2021=370, 2020=365, 2022=364, 2023=364, 2019=361, 2024=2, 2019..2024
"fiscal_year_id" int NOTNULL: 1808=370, 1807=365, 1809=364, 1810=364, 1806=361, 2259=2, 1806..2259
"days_in_cal_year" int NOTNULL: 365=1460, 366=366
"days_in_fis_year" int NOTNULL: 364=1095, 371=370, 361=361, 361..371
"end_of_cal_year" date NOTNULL: "2020-12-31"=366, "2019-12-31"=365, "2021-12-31"=365, "2022-12-31"=365, "2023-12-31"=365
"end_of_fis_year" date NOTNULL: "2021-12-31"=370, "2020-12-26"=365, "2022-12-30"=364, "2023-12-29"=364, "2019-12-27"=361, "2024-12-28"=2

indexes: none

samples:
| column | latest | sample | sample |
|---|---|---|---|
| time_id | 2023-12-31 | 2022-12-13 | 2023-01-08 |
| day_name | Sunday | Tuesday | Sunday |
| day_number_in_week | 7 | 2 | 7 |
| day_number_in_month | 31 | 13 | 8 |
| calendar_week_number | 53 | 50 | 2 |
| fiscal_week_number | 53 | 50 | 2 |
| week_ending_day | 2023-12-31 | 2022-12-18 | 2023-01-08 |
| week_ending_day_id | 2257 | 1568 | 1821 |
| calendar_month_number | 12 | 12 | 1 |
| fiscal_month_number | 1 | 12 | 1 |
| calendar_month_desc | 2023-12 | 2022-12 | 2023-01 |
| calendar_month_id | 2223 | 1719 | 1812 |
| fiscal_month_desc | 2024-01 | 2022-12 | 2023-01 |
| fiscal_month_id | 2258 | 1767 | 1768 |
| days_in_cal_month | 31 | 31 | 31 |
| days_in_fis_month | 28 | 35 | 28 |
| end_of_cal_month | 2023-12-31 | 2022-12-31 | 2023-01-31 |
| end_of_fis_month | 2024-01-26 | 2022-12-30 | 2023-01-27 |
| calendar_month_name | December | December | January |
| fiscal_month_name | January | December | January |
| calendar_quarter_desc | 2023-04 | 2022-04 | 2023-01 |
| calendar_quarter_id | 2150 | 1784 | 1814 |
| fiscal_quarter_desc | 2024-01 | 2022-04 | 2023-01 |
| fiscal_quarter_id | 2260 | 1800 | 1801 |
| days_in_cal_quarter | 92 | 92 | 90 |
| days_in_fis_quarter | 91 | 91 | 1 |
| end_of_cal_quarter | 2023-12-31 | 2022-12-31 | 2023-03-31 |
| end_of_fis_quarter | 2024-03-30 | 2022-12-30 | 2022-12-31 |
| calendar_quarter_number | 4 | 4 | 1 |
| fiscal_quarter_number | 1 | 4 | 1 |
| calendar_year | 2023 | 2022 | 2023 |
| calendar_year_id | 1813 | 1805 | 1813 |
| fiscal_year | 2024 | 2022 | 2023 |
| fiscal_year_id | 2259 | 1809 | 1810 |
| days_in_cal_year | 365 | 365 | 365 |
| days_in_fis_year | 364 | 364 | 364 |
| end_of_cal_year | 2023-12-31 | 2022-12-31 | 2023-12-31 |
| end_of_fis_year | 2024-12-28 | 2022-12-30 | 2023-12-29 |
