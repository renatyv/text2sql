---
generator: db-snooper
version: 0.0.26
generated_at_utc: 2026-08-16T08:08:47.812227Z
dialect: sqlite
database: /var/folders/9j/b9bx_drd53sc6zbpsqyrjy4h0000gn/T/dbsnoop-ssyh8fx6/complex_oracle.sqlite
schema: main
---

## Relationships

- channels.channel_id ← costs.channel_id, sales.channel_id
- countries.country_id ← customers.country_id
- customers.cust_id ← sales.cust_id
- products.prod_id ← costs.prod_id, sales.prod_id
- promotions.promo_id ← costs.promo_id, sales.promo_id
- times.time_id ← costs.time_id, sales.time_id

# cal_month_sales_mv

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

## Rows

- total=48

| column | latest | sample | sample |
|---|---|---|---|
| calendar_month_desc | 2022-12 | 2020-12 | 2022-11 |
| dollars | 2.54704e+06 | 1.93193e+06 | 2.47469e+06 |

## Columns

- calendar_month_desc: all distinct
- dollars: all distinct


# channels

## All rows

| column | row 1 | row 2 | row 3 | row 4 | row 5 |
|---|---|---|---|---|---|
| channel_id | 2 | 3 | 4 | 5 | 9 |
| channel_desc | Partners | Direct Sales | Internet | Catalog | Tele Sales |
| channel_class | Others | Direct | Indirect | Indirect | Direct |
| channel_class_id | 14 | 12 | 13 | 13 | 12 |
| channel_total | Channel total | Channel total | Channel total | Channel total | Channel total |
| channel_total_id | 1 | 1 | 1 | 1 | 1 |


# costs

```sql
CREATE TABLE costs (
   prod_id      INTEGER         NOT NULL,
   time_id      DATE            NOT NULL,
   promo_id     INTEGER         NOT NULL,
   channel_id   INTEGER         NOT NULL,
   unit_cost    REAL            NOT NULL,
   unit_price   REAL            NOT NULL,
   FOREIGN KEY (promo_id)   REFERENCES promotions (promo_id),
   FOREIGN KEY (prod_id)    REFERENCES products (prod_id),
   FOREIGN KEY (time_id)    REFERENCES times (time_id),
   FOREIGN KEY (channel_id) REFERENCES channels (channel_id)
);
```

## Indexes

- (channel_id)
- (promo_id)

## Rows

- total=82112

| column | latest | sample | sample |
|---|---|---|---|
| prod_id | 148 | 13 | 130 |
| time_id | 2022-12-28 | 2022-05-23 | 2022-03-31 |
| promo_id | 999 | 999 | 999 |
| channel_id | 4 | 4 | 2 |
| unit_cost | 17.36 | 703.69 | 78.41 |
| unit_price | 21.98 | 989.06 | 102.03 |

## Columns

- prod_id: 72 distinct, int 13..148
- time_id: 1459 distinct
- promo_id: 999=78425, 351=2182, 350=1505, int 350..999
- channel_id: 3=35104, 2=27635, 4=19373, int 2..4
- unit_cost: 5675 distinct, num -23.74..1342.06
  - stats: average=117.759, median=28.39
- unit_price: 3609 distinct, num 6.4..1782.72
  - stats: average=148.246, median=38.12


# countries

```sql
CREATE TABLE countries (
   country_id             INTEGER         NOT NULL,
   country_iso_code       CHAR(2)         NOT NULL,
   country_name           TEXT            NOT NULL,
   country_subregion      TEXT            NOT NULL,
   country_subregion_id   INTEGER         NOT NULL,
   country_region         TEXT            NOT NULL,
   country_region_id      INTEGER         NOT NULL,
   country_total          TEXT            NOT NULL,
   country_total_id       INTEGER         NOT NULL,
   PRIMARY KEY (country_id)
);
```

## Rows

- total=35

| column | latest | sample | sample |
|---|---|---|---|
| country_id | 52803 | 52799 | 52803 |
| country_iso_code | HU | ZW | HU |
| country_name | Hungary | Zimbabwe | Hungary |
| country_subregion | Eastern Europe | Africa | Eastern Europe |
| country_subregion_id | 52795 | 52792 | 52795 |
| country_region | Europe | Africa | Europe |
| country_region_id | 52803 | 52800 | 52803 |
| country_total | World total | World total | World total |
| country_total_id | 52806 | 52806 | 52806 |

## Columns

- country_id: unique identifier, int 52769..52803
- country_iso_code: all distinct
- country_name: all distinct
- country_subregion: "Western Europe"=11, "Asia"=6, "Middle East"=4, "Africa"=3, "Eastern Europe"=3, "Northern America"=3, "Southern America"=3, "Australia"=2
- country_subregion_id: 52799=11, 52793=6, 52796=4, 52792=3, 52795=3, 52797=3, 52798=3, 52794=2, int 52792..52799
- country_region: "Europe"=14, "Americas"=6, "Asia"=6, "Middle East"=4, "Africa"=3, "Oceania"=2
- country_region_id: 52803=14, 52802=6, 52801=5, 52804=4, 52800=3, 52805=2, 52798=1, int 52798..52805
- country_total: "World total"=35
- country_total_id: 52806=35


# currency

```sql
CREATE TABLE currency (
   country TEXT,
   year INTEGER,
   month INTEGER,
   to_us REAL
);
```

## Rows

- total=1260

| column | latest | sample | sample |
|---|---|---|---|
| country | Zimbabwe | Romania | Zimbabwe |
| year | 2021 | 2021 | 2021 |
| month | 12 | 1 | 11 |
| to_us | 1 | 1 | 1 |

## Columns

- country: 35 distinct
- year: 2019=420, 2020=420, 2021=420, int 2019..2021
- month: 1=105, 2=105, 3=105, 4=105, 5=105, 6=105, 7=105, 8=105, 9=105, 10=105, 11=105, 12=105, int 1..12
- to_us: 1=1224, 0.74=36


# customers

```sql
CREATE TABLE customers (
   cust_id                  INTEGER         NOT NULL,
   cust_first_name          TEXT            NOT NULL,
   cust_last_name           TEXT            NOT NULL,
   cust_gender              CHAR(1)         NOT NULL,
   cust_year_of_birth       INTEGER         NOT NULL,
   cust_marital_status      TEXT,
   cust_street_address      TEXT            NOT NULL,
   cust_postal_code         TEXT            NOT NULL,
   cust_city                TEXT            NOT NULL,
   cust_city_id             INTEGER         NOT NULL,
   cust_state_province      TEXT            NOT NULL,
   cust_state_province_id   INTEGER         NOT NULL,
   country_id               INTEGER         NOT NULL,
   cust_main_phone_number   TEXT            NOT NULL,
   cust_income_level        TEXT,
   cust_credit_limit        REAL,
   cust_email               TEXT,
   cust_total               TEXT            NOT NULL,
   cust_total_id            INTEGER         NOT NULL,
   cust_src_id              INTEGER,
   cust_eff_from            DATE,
   cust_eff_to              DATE,
   cust_valid               CHAR(1),
   PRIMARY KEY (cust_id),
   FOREIGN KEY (country_id) REFERENCES countries (country_id)
);
```

## Rows

- total=55500

| column | latest | sample | sample |
|---|---|---|---|
| cust_id | 104500 | 50382 | 14558 |
| cust_first_name | Lauren | Teri | Gerald |
| cust_last_name | Fenton | Ruddy | Wood |
| cust_gender | F | F | M |
| cust_year_of_birth | 1973 | 1951 | 1975 |
| cust_marital_status | divorced | single | single |
| cust_street_address | 47 South Guayanilla Road | 27 South Lassen Boulevard | 7 South De Baca Circle |
| cust_postal_code | 68524 | 48557 | 33415 |
| cust_city | Glasco | Aladdin | Pala |
| cust_city_id | 51583 | 51048 | 52101 |
| cust_state_province | KS | WY | CA |
| cust_state_province_id | 52630 | 52763 | 52567 |
| country_id | 52790 | 52790 | 52790 |
| cust_main_phone_number | 236-199-2209 | 184-729-4899 | 189-231-5647 |
| cust_income_level | K: 250,000 - 299,999 | A: Below 30,000 | D: 70,000 - 89,999 |
| cust_credit_limit | 15000 | 1500 | 3000 |
| cust_email | Fenton@company.example.com | Ruddy@company.example.com | Wood@company.example.com |
| cust_total | Customer total | Customer total | Customer total |
| cust_total_id | 52772 | 52772 | 52772 |
| cust_src_id | null | null | null |
| cust_eff_from | 2019-01-01 | 2019-01-01 | 2019-01-01 |
| cust_eff_to | null | null | null |
| cust_valid | A | I | I |

## Columns

- cust_id: unique identifier, int 1..104500
- cust_first_name: 1304 distinct
- cust_last_name: 916 distinct
- cust_gender: "M"=37175, "F"=18325
- cust_year_of_birth: 75 distinct, int 1924..2001
  - stats: average=1968.4, median=1967
- cust_marital_status: "single"=19094, "married"=16287, "never married"=1503, "divorced"=765, "widowed"=211, "separated"=134, nulls=17506
- cust_street_address: 50945 distinct
- cust_postal_code: 623 distinct
- cust_city: 620 distinct
- cust_city_id: 620 distinct, int 51040..52531
- cust_state_province: 145 distinct
- cust_state_province_id: 145 distinct, int 52533..52771
- country_id: 52790=18520, 52776=8173, 52770=7780, 52789=7557, 52779=3833, 52778=2039, 52772=2010, 52775=832, 52774=831, 52771=712, 52786=708, 52782=624, 52769=597, 52773=403, 52777=383, 52785=244, 52788=91, 52791=88, 52787=75, int 52769..52791
- cust_main_phone_number: 51000 distinct
- cust_income_level: "F: 110,000 - 129,999"=10537, "E: 90,000 - 109,999"=7936, "G: 130,000 - 149,999"=5465, "H: 150,000 - 169,999"=5465, "D: 70,000 - 89,999"=5217, "I: 170,000 - 189,999"=4566, "C: 50,000 - 69,999"=4255, "J: 190,000 - 249,999"=3006, "B: 30,000 - 49,999"=2764, "A: Below 30,000"=2630, "K: 250,000 - 299,999"=1934, "L: 300,000 and above"=1684, nulls=41
- cust_credit_limit: 1500=11334, 9000=9093, 7000=8634, 3000=7975, 5000=7724, 10000=5935, 11000=2935, 15000=1870, num 1500..15000
- cust_email: 1706 distinct
- cust_total: "Customer total"=55500
- cust_total_id: 52772=55500
- cust_src_id: all NULL
- cust_eff_from: 2019-01-01=55500
- cust_eff_to: all NULL
- cust_valid: "I"=44879, "A"=10621


# fweek_pscat_sales_mv

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

## Rows

- total=3652

| column | latest | sample | sample |
|---|---|---|---|
| week_ending_day | 2023-01-01 | 2019-09-08 | 2022-03-27 |
| prod_subcategory | Training Aids and Equipment | Cricket Bat | Cricket |
| dollars | 25186.4 | 9733.13 | 223.92 |
| channel_id | 3 | 3 | 2 |
| promo_id | 351 | 999 | 999 |

## Columns

- week_ending_day: 209 distinct
- prod_subcategory: "Baseballs"=642, "Cricket Bat"=633, "Bats"=631, "Training Aids and Equipment"=604, "Cricket Fan Gear"=584, "Cricket"=558
- dollars: 3545 distinct
- channel_id: 3=1361, 2=1202, 4=1053, 9=36, int 2..9
- promo_id: 999=3384, 350=119, 351=113, 33=36, int 33..999


# products

```sql
CREATE TABLE products (
   prod_id                 INTEGER         NOT NULL,
   prod_name               TEXT            NOT NULL,
   prod_desc               TEXT            NOT NULL,
   prod_subcategory        TEXT            NOT NULL,
   prod_subcategory_id     INTEGER         NOT NULL,
   prod_subcategory_desc   TEXT            NOT NULL,
   prod_category           TEXT            NOT NULL,
   prod_category_id        INTEGER         NOT NULL,
   prod_category_desc      TEXT            NOT NULL,
   prod_weight_class       INTEGER         NOT NULL,
   prod_unit_of_measure    TEXT,
   prod_pack_size          TEXT            NOT NULL,
   supplier_id             INTEGER         NOT NULL,
   prod_status             TEXT            NOT NULL,
   prod_list_price         REAL            NOT NULL,
   prod_min_price          REAL            NOT NULL,
   prod_total              TEXT            NOT NULL,
   prod_total_id           INTEGER         NOT NULL,
   prod_src_id             INTEGER,
   prod_eff_from           DATE,
   prod_eff_to             DATE,
   prod_valid              CHAR(1),
   PRIMARY KEY (prod_id)
);
```

## Rows

- total=24

- (no rows sampled)

## Columns

- prod_id: unique identifier, int 14..130
- prod_name: "Team shirt"=6, "2 Competition Grade NFHS Baseballs"=1, "6 Gallon Empty Ball Bucket"=1, "Cricket Bat Bag"=1, "Cricket Bat Pad"=1, "Cricket Gloves"=1, "English Willow Cricket Bat"=1, "Fiber Tape"=1, "Genuine Series MIX Wood Bat"=1, "Indoor Cricket Ball"=1, "Linseed Oil"=1, "MLB Official Game Baseball w/ Display Case"=1, "Outdoor Cricket Ball"=1, "Pitching Machine and Batting Cage Combo"=1, "Plastic Cricket Bat"=1, "Pro Maple Bat"=1, "Pro Maple Youth Bat"=1, "Slugger Youth Series Maple Bat"=1, "Speed Trainer Bats and Training Program"=1
- prod_desc: all distinct
- prod_subcategory: "Cricket Fan Gear"=6, "Cricket Bat"=5, "Bats"=4, "Cricket"=4, "Baseballs"=3, "Training Aids and Equipment"=2
- prod_subcategory_id: 2054=6, 2051=5, 2036=4, 2055=4, 2031=3, 2035=2, int 2031..2055
- prod_subcategory_desc: "Cricket Fan Gear"=6, "Cricket"=5, "Bats"=4, "Cricket Bat"=4, "Baseballs"=3, "Training Aids and Equipment"=2
- prod_category: "Cricket"=15, "Baseball"=9
- prod_category_id: 205=15, 203=9
- prod_category_desc: "Cricket"=15, "Baseball"=9
- prod_weight_class: 1=24
- prod_unit_of_measure: "U"=24
- prod_pack_size: "P"=24
- supplier_id: 1=24
- prod_status: "STATUS"=24
- prod_list_price: 44.99=6, 8.99=1, 9.99=1, 11.99=1, 15.99=1, 19.99=1, 21.99=1, 22.99=1, 24.99=1, 27.99=1, 28.99=1, 29.99=1, 36.99=1, 55.99=1, 89.99=1, 192.99=1, 199.99=1, 899.99=1, 999.99=1, num 8.99..999.99
- prod_min_price: 44.99=6, 8.99=1, 9.99=1, 11.99=1, 15.99=1, 19.99=1, 21.99=1, 22.99=1, 24.99=1, 27.99=1, 28.99=1, 29.99=1, 36.99=1, 55.99=1, 89.99=1, 192.99=1, 199.99=1, 899.99=1, 999.99=1, num 8.99..999.99
- prod_total: "TOTAL"=24
- prod_total_id: 1=24
- prod_src_id: ""=24
- prod_eff_from: 1 distinct
  - value counts: skipped (query timeout > 10s)
- prod_eff_to: 1 distinct
  - value counts: skipped (query timeout > 10s)
- prod_valid: "A"=24


# profits

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

## Rows

- total=916039

| column | latest | sample | sample |
|---|---|---|---|
| channel_id | 4 | 4 | 3 |
| cust_id | 50840 | 2892 | 2475 |
| prod_id | 148 | 121 | 47 |
| promo_id | 999 | 999 | 351 |
| time_id | 2022-08-02 | 2021-02-25 | 2022-12-17 |
| unit_cost | 17.28 | 11.3 | 23.23 |
| unit_price | 22.14 | 12.42 | 28.77 |
| amount_sold | 22.14 | 12.42 | 28.77 |
| quantity_sold | 1 | 1 | 1 |
| TOTAL_COST | 17.28 | 11.3 | 23.23 |

## Columns

- channel_id: int 2..4
- cust_id: int 2..50840
- prod_id: int 13..148
- promo_id: int 350..999
- time_id: profile metrics skipped
- unit_cost: num -23.74..1342.06
  - stats: average=84.8406
- unit_price: num 6.4..1782.72
  - stats: average=106.807
- amount_sold: num 6.4..1782.72
  - stats: average=106.807
- quantity_sold: int 1..1
  - stats: average=1
- TOTAL_COST: profile metrics skipped


# promotions

```sql
CREATE TABLE promotions (
   promo_id               INTEGER         NOT NULL,
   promo_name             TEXT            NOT NULL,
   promo_subcategory      TEXT            NOT NULL,
   promo_subcategory_id   INTEGER         NOT NULL,
   promo_category         TEXT            NOT NULL,
   promo_category_id      INTEGER         NOT NULL,
   promo_cost             REAL            NOT NULL,
   promo_begin_date       DATE            NOT NULL,
   promo_end_date         DATE            NOT NULL,
   promo_total            TEXT            NOT NULL,
   promo_total_id         INTEGER         NOT NULL,
   PRIMARY KEY (promo_id)
);
```

## Rows

- total=503

| column | latest | sample | sample |
|---|---|---|---|
| promo_id | 999 | 366 | 365 |
| promo_name | NO PROMOTION # | newspaper promotion #19-366 | TV promotion #30-365 |
| promo_subcategory | NO PROMOTION | coupon news | promotion movie |
| promo_subcategory_id | 11 | 19 | 30 |
| promo_category | NO PROMOTION | newspaper | TV |
| promo_category_id | 2 | 8 | 3 |
| promo_cost | 0 | 90800 | 43000 |
| promo_begin_date | 9999-01-01 | 2020-04-18 | 2019-09-25 |
| promo_end_date | 9999-01-01 | 2020-07-18 | 2019-11-25 |
| promo_total | Promotion total | Promotion total | Promotion total |
| promo_total_id | 1 | 1 | 1 |

## Columns

- promo_id: unique identifier, int 33..999
- promo_name: all distinct
- promo_subcategory: 22 distinct
- promo_subcategory_id: 22 distinct, int 11..32
- promo_category: "TV"=115, "newspaper"=110, "internet"=85, "magazine"=65, "post"=65, "flyer"=40, "radio"=20, "ad news"=2, "NO PROMOTION"=1
- promo_category_id: 3=115, 8=110, 6=85, 7=65, 9=65, 5=40, 10=20, 4=2, 2=1, int 2..10
- promo_cost: 501 distinct, num 0..100000
  - stats: average=50160.8, median=51600
- promo_begin_date: 192 distinct
- promo_end_date: 191 distinct
- promo_total: "Promotion total"=503
- promo_total_id: 1=503


# sales

```sql
CREATE TABLE sales (
   prod_id         INTEGER         NOT NULL,
   cust_id         INTEGER         NOT NULL,
   time_id         DATE            NOT NULL,
   channel_id      INTEGER         NOT NULL,
   promo_id        INTEGER         NOT NULL,
   quantity_sold   INTEGER         NOT NULL,
   amount_sold     REAL            NOT NULL,
   FOREIGN KEY (promo_id)   REFERENCES promotions (promo_id),
   FOREIGN KEY (cust_id)    REFERENCES customers (cust_id),
   FOREIGN KEY (prod_id)    REFERENCES products (prod_id),
   FOREIGN KEY (channel_id) REFERENCES channels (channel_id),
   FOREIGN KEY (time_id) REFERENCES times (time_id)
);
```

## Rows

- total≈918843 (estimated from db stats; row/column profiling skipped)


# supplementary_demographics

```sql
CREATE TABLE supplementary_demographics (
   cust_id                   INTEGER           NOT NULL,
   education                 TEXT,
   occupation                TEXT,
   household_size            TEXT,
   yrs_residence             INTEGER,
   affinity_card             INTEGER,
   cricket                   INTEGER,
   baseball                  INTEGER,
   tennis                    INTEGER,
   soccer                    INTEGER,
   golf                      INTEGER,
   unknown                   INTEGER,
   misc                      INTEGER,
   comments                  TEXT,
   PRIMARY KEY (cust_id)
);
```

## Rows

- total=4500

| column | latest | sample | sample |
|---|---|---|---|
| cust_id | 104500 | 102601 | 100489 |
| education | HS-grad | HS-grad | Assoc-A |
| occupation | Crafts | Prof. | TechSup |
| household_size | 9+ | 9+ | 1 |
| yrs_residence | 5 | 5 | 3 |
| affinity_card | 0 | 1 | 0 |
| cricket | 1 | 0 | 1 |
| baseball | 1 | 0 | 1 |
| tennis | 1 | 1 | 0 |
| soccer | 1 | 1 | 1 |
| golf | 1 | 1 | 1 |
| unknown | 0 | 0 | 1 |
| misc | 0 | 0 | 0 |
| comments | Affinity card is a great idea. But your store is still too expensive. I am tired of your lousy junk mail. | I am not going to waste my time filling up this three page form. Lousy idea. | I purchased the new model and love it. I also purchased one for my sister and one for my brother. |

## Columns

- cust_id: unique identifier, int 100001..104500
- education: "HS-grad"=1462, "< Bach."=1041, "Bach."=779, "Assoc-V"=196, "Masters"=190, "Assoc-A"=172, "10th"=122, "11th"=121, "Profsc"=94, "7th-8th"=87, "9th"=76, "12th"=52, "PhD"=49, "5th-6th"=39, "1st-4th"=17, "Presch."=3
- occupation: "Crafts"=572, "Sales"=560, "Exec."=559, "Prof."=545, "Cleric."=520, "Other"=468, "Machine"=276, "?"=236, "Transp."=187, "TechSup"=177, "Handler"=168, "Farming"=122, "Protec."=89, "House-s"=19, "Armed-F"=2
- household_size: "3"=1787, "2"=1149, "1"=692, "9+"=505, "4-5"=219, "6-8"=148
- yrs_residence: 3=961, 4=937, 5=757, 2=625, 6=473, 1=276, 7=231, 8=101, 9=49, 0=48, 10=25, 11=9, 12=3, 14=3, 13=2, int 0..14
- affinity_card: 0=3428, 1=1072
- cricket: 1=2868, 0=1632
- baseball: 1=2597, 0=1903
- tennis: 1=2539, 0=1961
- soccer: 1=3983, 0=517
- golf: 1=4500
- unknown: 0=3094, 1=1406
- misc: 0=4489, 1=11
- comments: 44 distinct, nulls=205


# times

```sql
CREATE TABLE times (
   time_id                   DATE          NOT NULL,
   day_name                  TEXT          NOT NULL,
   day_number_in_week        INTEGER       NOT NULL,
   day_number_in_month       INTEGER       NOT NULL,
   calendar_week_number      INTEGER       NOT NULL,
   fiscal_week_number        INTEGER       NOT NULL,
   week_ending_day           DATE          NOT NULL,
   week_ending_day_id        INTEGER       NOT NULL,
   calendar_month_number     INTEGER       NOT NULL,
   fiscal_month_number       INTEGER       NOT NULL,
   calendar_month_desc       TEXT          NOT NULL,
   calendar_month_id         INTEGER       NOT NULL,
   fiscal_month_desc         TEXT          NOT NULL,
   fiscal_month_id           INTEGER       NOT NULL,
   days_in_cal_month         INTEGER       NOT NULL,
   days_in_fis_month         INTEGER       NOT NULL,
   end_of_cal_month          DATE          NOT NULL,
   end_of_fis_month          DATE          NOT NULL,
   calendar_month_name       TEXT          NOT NULL,
   fiscal_month_name         TEXT          NOT NULL,
   calendar_quarter_desc     CHAR(7)       NOT NULL,
   calendar_quarter_id       INTEGER       NOT NULL,
   fiscal_quarter_desc       CHAR(7)       NOT NULL,
   fiscal_quarter_id         INTEGER       NOT NULL,
   days_in_cal_quarter       INTEGER       NOT NULL,
   days_in_fis_quarter       INTEGER       NOT NULL,
   end_of_cal_quarter        DATE          NOT NULL,
   end_of_fis_quarter        DATE          NOT NULL,
   calendar_quarter_number   INTEGER       NOT NULL,
   fiscal_quarter_number     INTEGER       NOT NULL,
   calendar_year             INTEGER       NOT NULL,
   calendar_year_id          INTEGER       NOT NULL,
   fiscal_year               INTEGER       NOT NULL,
   fiscal_year_id            INTEGER       NOT NULL,
   days_in_cal_year          INTEGER       NOT NULL,
   days_in_fis_year          INTEGER       NOT NULL,
   end_of_cal_year           DATE          NOT NULL,
   end_of_fis_year           DATE          NOT NULL,
   PRIMARY KEY (time_id)
);
```

## Rows

- total=1826

| column | latest | sample | sample |
|---|---|---|---|
| time_id | 2023-12-31 | 2019-11-17 | 2023-11-04 |
| day_name | Sunday | Sunday | Saturday |
| day_number_in_week | 7 | 7 | 6 |
| day_number_in_month | 31 | 17 | 4 |
| calendar_week_number | 53 | 46 | 44 |
| fiscal_week_number | 53 | 46 | 44 |
| week_ending_day | 2023-12-31 | 2019-11-17 | 2023-11-05 |
| week_ending_day_id | 2257 | 1612 | 2191 |
| calendar_month_number | 12 | 11 | 11 |
| fiscal_month_number | 1 | 11 | 11 |
| calendar_month_desc | 2023-12 | 2019-11 | 2023-11 |
| calendar_month_id | 2223 | 1682 | 2187 |
| fiscal_month_desc | 2024-01 | 2019-11 | 2023-11 |
| fiscal_month_id | 2258 | 1730 | 2182 |
| days_in_cal_month | 31 | 30 | 30 |
| days_in_fis_month | 28 | 35 | 28 |
| end_of_cal_month | 2023-12-31 | 2019-11-30 | 2023-11-30 |
| end_of_fis_month | 2024-01-26 | 2019-11-29 | 2023-11-24 |
| calendar_month_name | December | November | November |
| fiscal_month_name | January | November | November |
| calendar_quarter_desc | 2023-04 | 2019-04 | 2023-04 |
| calendar_quarter_id | 2150 | 1772 | 2150 |
| fiscal_quarter_desc | 2024-01 | 2019-04 | 2023-04 |
| fiscal_quarter_id | 2260 | 1788 | 2147 |
| days_in_cal_quarter | 92 | 92 | 92 |
| days_in_fis_quarter | 91 | 91 | 91 |
| end_of_cal_quarter | 2023-12-31 | 2019-12-31 | 2023-12-31 |
| end_of_fis_quarter | 2024-03-30 | 2019-12-27 | 2023-12-29 |
| calendar_quarter_number | 4 | 4 | 4 |
| fiscal_quarter_number | 1 | 4 | 4 |
| calendar_year | 2023 | 2019 | 2023 |
| calendar_year_id | 1813 | 1802 | 1813 |
| fiscal_year | 2024 | 2019 | 2023 |
| fiscal_year_id | 2259 | 1806 | 1810 |
| days_in_cal_year | 365 | 365 | 365 |
| days_in_fis_year | 364 | 361 | 364 |
| end_of_cal_year | 2023-12-31 | 2019-12-31 | 2023-12-31 |
| end_of_fis_year | 2024-12-28 | 2019-12-27 | 2023-12-29 |

## Columns

- time_id: unique identifier
- day_name: "Friday"=261, "Saturday"=261, "Sunday"=261, "Thursday"=261, "Tuesday"=261, "Wednesday"=261, "Monday"=260
- day_number_in_week: 2=261, 3=261, 4=261, 5=261, 6=261, 7=261, 1=260, int 1..7
- day_number_in_month: 31 distinct, int 1..31
  - stats: average=15.7278, median=16
- calendar_week_number: 53 distinct, int 1..53
  - stats: average=26.5871, median=27
- fiscal_week_number: 53 distinct, int 1..53
  - stats: average=26.5871, median=27
- week_ending_day: 261 distinct
- week_ending_day_id: 262 distinct, int 1462..2257
- calendar_month_number: 1=155, 3=155, 5=155, 7=155, 8=155, 10=155, 12=155, 4=150, 6=150, 9=150, 11=150, 2=141, int 1..12
- fiscal_month_number: 12=161, 4=154, 5=154, 7=154, 8=154, 9=154, 10=154, 1=153, 3=153, 6=147, 11=147, 2=141, int 1..12
- calendar_month_desc: 60 distinct
- calendar_month_id: 60 distinct, int 1672..2223
- fiscal_month_desc: 61 distinct
- fiscal_month_id: 61 distinct, int 1720..2258
- days_in_cal_month: 31=1085, 30=600, 28=112, 29=29, int 28..31
- days_in_fis_month: 28=1066, 35=735, 25=25, int 25..35
- end_of_cal_month: 60 distinct
- end_of_fis_month: 61 distinct
- calendar_month_name: "August"=155, "December"=155, "January"=155, "July"=155, "March"=155, "May"=155, "October"=155, "April"=150, "June"=150, "November"=150, "September"=150, "February"=141
- fiscal_month_name: "December"=161, "April"=154, "August"=154, "July"=154, "May"=154, "October"=154, "September"=154, "January"=153, "March"=153, "June"=147, "November"=147, "February"=141
- calendar_quarter_desc: 20 distinct
- calendar_quarter_id: 20 distinct, int 1769..2150
- fiscal_quarter_desc: 21 distinct
- fiscal_quarter_id: 21 distinct, int 1785..2260
- days_in_cal_quarter: 92=920, 91=545, 90=361, int 90..92
- days_in_fis_quarter: 91=1367, 98=196, 1=91, 88=88, 84=84, int 1..98
- end_of_cal_quarter: 20 distinct
- end_of_fis_quarter: 21 distinct
- calendar_quarter_number: 3=460, 4=460, 2=455, 1=451, int 1..4
- fiscal_quarter_number: 3=462, 4=462, 2=455, 1=447, int 1..4
- calendar_year: 2020=366, 2019=365, 2021=365, 2022=365, 2023=365, int 2019..2023
- calendar_year_id: 1803=366, 1802=365, 1804=365, 1805=365, 1813=365, int 1802..1813
- fiscal_year: 2021=370, 2020=365, 2022=364, 2023=364, 2019=361, 2024=2, int 2019..2024
- fiscal_year_id: 1808=370, 1807=365, 1809=364, 1810=364, 1806=361, 2259=2, int 1806..2259
- days_in_cal_year: 365=1460, 366=366
- days_in_fis_year: 364=1095, 371=370, 361=361, int 361..371
- end_of_cal_year: 2020-12-31=366, 2019-12-31=365, 2021-12-31=365, 2022-12-31=365, 2023-12-31=365
- end_of_fis_year: 2021-12-31=370, 2020-12-26=365, 2022-12-30=364, 2023-12-29=364, 2019-12-27=361, 2024-12-28=2
