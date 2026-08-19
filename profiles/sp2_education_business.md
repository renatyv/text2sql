---
generator: db-snooper
version: 0.0.26
generated_at_utc: 2026-08-16T08:09:20.190569Z
dialect: sqlite
database: /var/folders/9j/b9bx_drd53sc6zbpsqyrjy4h0000gn/T/dbsnoop-5l5ypss3/education_business.sqlite
schema: main
---

# SalaryDataset

```sql
CREATE TABLE "SalaryDataset" (
"index" INTEGER,
  "CompanyName" TEXT,
  "JobTitle" TEXT,
  "SalariesReported" REAL,
  "Location" TEXT,
  "Salary" TEXT
);
```

## Rows

- total=4344

| column | latest | sample | sample |
|---|---|---|---|
| index | 4343 | 2660 | 3371 |
| CompanyName | vPhrase | Keysight Technologies | Kagool |
| JobTitle | Machine Learning Engineer | Data Analyst | Data Engineer |
| SalariesReported | 1 | 3 | 1 |
| Location | Mumbai | New Delhi | Hyderabad |
| Salary | ₹9,39,843/yr | ₹7,05,134/yr | ₹26,823/mo |

## Columns

- index: all distinct, int 0..4343
  - stats: average=2171.5, median=2171.5
- CompanyName: 2529 distinct, nulls=3
- JobTitle: 26 distinct
- SalariesReported: 49 distinct, nulls=2, num 1..105
  - stats: average=2.77591, median=1
- Location: "Bangalore"=1584, "Pune"=818, "Hyderabad"=669, "New Delhi"=656, "Mumbai"=617
- Salary: 3101 distinct


# StaffHours

```sql
CREATE TABLE "StaffHours" (
"StaffMember" TEXT,
  "EventDate" TEXT,
  "EventTime" TEXT,
  "EventType" TEXT
);
```

## Rows

- total=236

| column | latest | sample | sample |
|---|---|---|---|
| StaffMember | Z | Y | I |
| EventDate | 2013-03-09 | 2013-01-17 | 2013-03-04 |
| EventTime | 11:45 | 08:10 | 08:45 |
| EventType | Enter | Enter | Enter |

## Columns

- StaffMember: 26 distinct
- EventDate: 64 distinct
- EventTime: 107 distinct
- EventType: "Enter"=123, "Exit"=113


# hardware_dim_customer

```sql
CREATE TABLE "hardware_dim_customer" (
"customer_code" INTEGER,
  "customer" TEXT,
  "platform" TEXT,
  "channel" TEXT,
  "market" TEXT,
  "sub_zone" TEXT,
  "region" TEXT
);
```

## Rows

- total=209

| column | latest | sample | sample |
|---|---|---|---|
| customer_code | 90027207 | 90014139 | 90009129 |
| customer | Amazon  | Elkjøp | Leader |
| platform | E-Commerce | Brick & Mortar | Brick & Mortar |
| channel | Retailer | Retailer | Retailer |
| market | Brazil | Netherlands | Newzealand |
| sub_zone | LATAM | NE | ANZ |
| region | LATAM | EU | APAC |

## Columns

- customer_code: all distinct, int 70002017..90027207
  - stats: average=8.59465e+07, median=9.0012e+07
- customer: 75 distinct
- platform: "Brick & Mortar"=150, "E-Commerce"=59
- channel: "Retailer"=164, "Direct"=40, "Distributor"=5
- market: 27 distinct
- sub_zone: "NE"=61, "SE"=44, "ROA"=38, "India"=18, "ANZ"=15, "LATAM"=7, nulls=26
- region: "EU"=105, "APAC"=71, "LATAM"=7, nulls=26


# hardware_dim_product

```sql
CREATE TABLE "hardware_dim_product" (
"product_code" TEXT,
  "division" TEXT,
  "segment" TEXT,
  "category" TEXT,
  "product" TEXT,
  "variant" TEXT
);
```

## Rows

- total=397

| column | latest | sample | sample |
|---|---|---|---|
| product_code | A7321160303 | A7321160303 | A4821110805 |
| division | N & S | N & S | PC |
| segment | Networking | Networking | Notebook |
| category | Wi fi extender | Wi fi extender | Personal Laptop |
| product | AQ Wi Power Dx3 | AQ Wi Power Dx3 | AQ F16 |
| variant | Premium | Premium | Plus Blue |

## Columns

- product_code: all distinct
- division: "P & A"=200, "PC"=161, "N & S"=36
- segment: "Notebook"=129, "Accessories"=116, "Peripherals"=84, "Desktop"=32, "Storage"=27, "Networking"=9
- category: "Personal Laptop"=61, "Keyboard"=48, "Mouse"=48, "Business Laptop"=44, "Gaming Laptop"=40, "Graphic Card"=36, "Batteries"=20, "MotherBoard"=20, "Processors"=18, "Personal Desktop"=16, "External Solid State Drives"=15, "USB Flash Drives"=12, "Internal HDD"=10, "Wi fi extender"=9
- product: 73 distinct
- variant: 27 distinct


# hardware_fact_gross_price

```sql
CREATE TABLE "hardware_fact_gross_price" (
"product_code" TEXT,
  "fiscal_year" INTEGER,
  "gross_price" REAL
);
```

## Rows

- total=579

| column | latest | sample | sample |
|---|---|---|---|
| product_code | A7321160303 | A4319110304 | A1421150503 |
| fiscal_year | 2021 | 2021 | 2021 |
| gross_price | 42.8483 | 267.064 | 176.439 |

## Columns

- product_code: 347 distinct
- fiscal_year: 2021=334, 2020=245
- gross_price: all distinct, num 2.9168..834.981
  - stats: average=206.053, median=35.1332


# hardware_fact_manufacturing_cost

```sql
CREATE TABLE "hardware_fact_manufacturing_cost" (
"product_code" TEXT,
  "cost_year" INTEGER,
  "manufacturing_cost" REAL
);
```

## Rows

- total=579

| column | latest | sample | sample |
|---|---|---|---|
| product_code | A7321160303 | A4218110208 | A5519110302 |
| cost_year | 2021 | 2020 | 2020 |
| manufacturing_cost | 12.9502 | 67.1724 | 171.437 |

## Columns

- product_code: 347 distinct
- cost_year: 2021=334, 2020=245
- manufacturing_cost: 488 distinct, num 0.892..240.536
  - stats: average=61.5661, median=10.4828


# hardware_fact_pre_invoice_deductions

```sql
CREATE TABLE "hardware_fact_pre_invoice_deductions" (
"customer_code" INTEGER,
  "fiscal_year" INTEGER,
  "pre_invoice_discount_pct" REAL
);
```

## Rows

- total=418

| column | latest | sample | sample |
|---|---|---|---|
| customer_code | 90027207 | 90014136 | 90002006 |
| fiscal_year | 2021 | 2021 | 2021 |
| pre_invoice_discount_pct | 0.2772 | 0.2034 | 0.3038 |

## Columns

- customer_code: 209 distinct, int 70002017..90027207
  - stats: average=8.59465e+07, median=9.0012e+07
- fiscal_year: 2020=209, 2021=209
- pre_invoice_discount_pct: 351 distinct, num 0.0531..0.3095
  - stats: average=0.233616, median=0.24005


# hardware_fact_sales_monthly

```sql
CREATE TABLE "hardware_fact_sales_monthly" (
"date" TEXT,
  "product_code" TEXT,
  "customer_code" INTEGER,
  "sold_quantity" INTEGER,
  "fiscal_year" INTEGER
);
```

## Rows

- total≈971631 (estimated from db stats; row/column profiling skipped)


# university_course

## All rows

| column | row 1 | row 2 | row 3 | row 4 | row 5 | row 6 | row 7 |
|---|---|---|---|---|---|---|---|
| CourseNo | FIN300 | FIN450 | FIN480 | IS320 | IS460 | IS470 | IS480 |
| CrsDesc | FUNDAMENTALS OF FINANCE | PRINCIPLES OF INVESTMENTS | CORPORATE FINANCE | FUNDAMENTALS OF BUSINESS PROGRAMMING | SYSTEMS ANALYSIS | BUSINESS DATA COMMUNICATIONS | FUNDAMENTALS OF DATABASE MANAGEMENT |
| CrsUnits | 4 | 4 | 4 | 4 | 4 | 4 | 4 |


# university_enrollment

```sql
CREATE TABLE "university_enrollment" (
"OfferNo" INTEGER,
  "StdNo" INTEGER,
  "EnrGrade" REAL
);
```

## Rows

- total=37

| column | latest | sample | sample |
|---|---|---|---|
| OfferNo | 9876 | 5679 | 4321 |
| StdNo | 901234567 | 678901234 | 124567890 |
| EnrGrade | 4 | 3.3 | 3.2 |

## Columns

- OfferNo: 9876=7, 1234=6, 4321=6, 5679=6, 5678=5, 7777=3, 5555=2, 6666=2, int 1234..9876
- StdNo: 123456789=5, 124567890=4, 234567890=4, 567890123=4, 901234567=4, 345678901=3, 456789012=3, 678901234=3, 890123456=3, 789012345=2, 876543210=2, int 123456789..901234567
- EnrGrade: 3.2=6, 3.4=6, 3.1=5, 3.3=4, 3.5=4, 2.6=2, 3.7=2, 3.8=2, 2=1, 2.7=1, 2.8=1, 2.9=1, 3.6=1, 4=1, num 2..4


# university_faculty

## All rows

| column | row 1 | row 2 | row 3 | row 4 | row 5 | row 6 | row 7 | row 8 |
|---|---|---|---|---|---|---|---|---|
| FacNo | 98765432 | 123456789 | 543210987 | 654321098 | 765432109 | 876543210 | 987654321 | 987654322 |
| FacFirstName | LEONARD | JOHN | VICTORIA | LEONARD | NICKI | CRISTOPHER | JULIA | JANE |
| FacLastName | VINCE | DOE | EMMANUEL | FIBON | MACON | COLAN | MILLS | SMITH |
| FacCity | SEATTLE | SEATTLE | BOTHELL | SEATTLE | BELLEVUE | SEATTLE | SEATTLE | REDMOND |
| FacState | WA | WA | WA | WA | WA | WA | WA | WA |
| FacDept | MS | CS | MS | MS | FIN | MS | FIN | CS |
| FacRank | ASST | ASST | PROF | ASSC | PROF | ASST | ASSC | PROF |
| FacSalary | 35000 | 55000 | 120000 | 70000 | 65000 | 40000 | 75000 | 110000 |
| FacSupervisor | 6.54321e+08 | 5.43211e+08 | null | 5.43211e+08 | null | 6.54321e+08 | 7.65432e+08 | 5.43211e+08 |
| FacHireDate | 1997-04-10 | 2005-06-15 | 1998-04-15 | 1996-05-01 | 1999-04-11 | 2001-03-01 | 2002-03-15 | 2007-08-20 |
| FacZipCode | 98111-9921 | 98111-1234 | 98011-2242 | 98121-0094 | 98015-9945 | 98114-1332 | 98114-9954 | 98052-1234 |


# university_offering

```sql
CREATE TABLE "university_offering" (
"OfferNo" INTEGER,
  "CourseNo" TEXT,
  "OffTerm" TEXT,
  "OffYear" INTEGER,
  "OffLocation" TEXT,
  "OffTime" TEXT,
  "FacNo" REAL,
  "OffDays" TEXT
);
```

## Rows

- total=13

| column | latest | sample | sample |
|---|---|---|---|
| OfferNo | 9876 | 5678 | 5679 |
| CourseNo | IS460 | IS480 | IS480 |
| OffTerm | SPRING | WINTER | SPRING |
| OffYear | 2010 | 2010 | 2010 |
| OffLocation | BLM307 | BLM302 | BLM412 |
| OffTime | 1:30 PM | 10:30 AM | 3:30 PM |
| FacNo | 6.54321e+08 | 9.87654e+08 | 8.76543e+08 |
| OffDays | TTH | MW | TTH |

## Columns

- OfferNo: 1111=1, 1234=1, 2222=1, 3333=1, 4321=1, 4444=1, 5555=1, 5678=1, 5679=1, 6666=1, 7777=1, 8888=1, 9876=1, int 1111..9876
- CourseNo: "IS320"=6, "IS460"=2, "IS480"=2, "FIN300"=1, "FIN450"=1, "FIN480"=1
- OffTerm: "SPRING"=4, "WINTER"=4, "SUMMER"=3, "FALL"=2
- OffYear: 2010=10, 2009=3
- OffLocation: "BLM302"=4, "BLM214"=2, "BLM412"=2, "BLM207"=1, "BLM212"=1, "BLM305"=1, "BLM307"=1, "BLM405"=1
- OffTime: "10:30 AM"=4, "1:30 PM"=4, "3:30 PM"=3, "8:30 AM"=2
- FacNo: 9.87654e+07=3, 6.54321e+08=2, 7.65432e+08=2, 9.87654e+08=2, 5.43211e+08=1, 8.76543e+08=1, nulls=2, num 9.87654e+07..9.87654e+08
- OffDays: "MW"=7, "TTH"=6


# university_student

```sql
CREATE TABLE "university_student" (
"StdNo" INTEGER,
  "StdFirstName" TEXT,
  "StdLastName" TEXT,
  "StdCity" TEXT,
  "StdState" TEXT,
  "StdZip" TEXT,
  "StdMajor" TEXT,
  "StdClass" TEXT,
  "StdGPA" REAL
);
```

## Rows

- total=11

| column | latest | sample | sample |
|---|---|---|---|
| StdNo | 901234567 | 123456789 | 789012345 |
| StdFirstName | WILLIAM | HOMER | ROBERTO |
| StdLastName | PILGRIM | WELLS | MORALES |
| StdCity | BOTHELL | SEATTLE | SEATTLE |
| StdState | WA | WA | WA |
| StdZip | 98113-1885 | 98121-1111 | 98121-2212 |
| StdMajor | IS | IS | FIN |
| StdClass | SO | FR | JR |
| StdGPA | 3.8 | 3 | 2.5 |

## Columns

- StdNo: 123456789=1, 124567890=1, 234567890=1, 345678901=1, 456789012=1, 567890123=1, 678901234=1, 789012345=1, 876543210=1, 890123456=1, 901234567=1, int 123456789..901234567
- StdFirstName: "BOB"=1, "CANDY"=1, "CRISTOPHER"=1, "HOMER"=1, "JOE"=1, "LUKE"=1, "MARIAH"=1, "ROBERTO"=1, "TESS"=1, "WALLY"=1, "WILLIAM"=1
- StdLastName: "DODGE"=2, "KENDALL"=2, "BRAZZI"=1, "COLAN"=1, "ESTRADA"=1, "MORALES"=1, "NORBERT"=1, "PILGRIM"=1, "WELLS"=1
- StdCity: "SEATTLE"=7, "BOTHELL"=2, "REDMOND"=1, "TACOMA"=1
- StdState: "WA"=11
- StdZip: "98011-2121"=1, "98113-1885"=1, "98114-0021"=1, "98114-1332"=1, "98116-0021"=1, "98116-2344"=1, "98121-1111"=1, "98121-2212"=1, "98121-2333"=1, "98123-1141"=1, "99042-3321"=1
- StdMajor: "IS"=6, "FIN"=3, "ACCT"=2
- StdClass: "JR"=4, "SR"=4, "SO"=2, "FR"=1
- StdGPA: 2.2=1, 2.5=1, 2.7=1, 2.8=1, 3=1, 3.2=1, 3.3=1, 3.5=1, 3.6=1, 3.8=1, 4=1, num 2.2..4


# web_accounts

```sql
CREATE TABLE "web_accounts" (
"id" INTEGER,
  "name" TEXT,
  "website" TEXT,
  "lat" REAL,
  "long" REAL,
  "primary_poc" TEXT,
  "sales_rep_id" INTEGER
);
```

## Rows

- total=351

| column | latest | sample | sample |
|---|---|---|---|
| id | 4501 | 1951 | 1661 |
| name | SpartanNash | Twenty-First Century Fox | American Airlines Group |
| website | www.spartannash.com | www.21cf.com | www.aa.com |
| lat | 45.5557 | 42.3547 | 40.7716 |
| long | -122.657 | -71.0548 | -73.982 |
| primary_poc | Jewell Likes | Nichelle Singley | Sasha Haughey |
| sales_rep_id | 321970 | 321560 | 321500 |

## Columns

- id: unique identifier, int 1001..4501
- name: all distinct
- website: all distinct
- lat: all distinct, num 30.4219..45.5557
  - stats: average=37.8614, median=38.6049
- long: all distinct, num -122.682..-71.0513
  - stats: average=-92.3437, median=-84.4718
- primary_poc: 330 distinct
- sales_rep_id: 50 distinct, int 321500..321990


# web_events

```sql
CREATE TABLE "web_events" (
"id" INTEGER,
  "account_id" INTEGER,
  "occurred_at" TEXT,
  "channel" TEXT
);
```

## Rows

- total=9073

| column | latest | sample | sample |
|---|---|---|---|
| id | 9073 | 8077 | 4025 |
| account_id | 4501 | 3711 | 4201 |
| occurred_at | 2016-05-30T00:46:53.000Z | 2016-06-27T04:26:37.000Z | 2016-09-20T12:58:49.000Z |
| channel | organic | organic | direct |

## Columns

- id: unique identifier, int 1..9073
- account_id: 351 distinct, int 1001..4501
- occurred_at: all distinct
- channel: "direct"=5298, "facebook"=967, "organic"=952, "adwords"=906, "banner"=476, "twitter"=474


# web_orders

```sql
CREATE TABLE "web_orders" (
"id" INTEGER,
  "account_id" INTEGER,
  "occurred_at" TEXT,
  "standard_qty" INTEGER,
  "gloss_qty" INTEGER,
  "poster_qty" INTEGER,
  "total" INTEGER,
  "standard_amt_usd" REAL,
  "gloss_amt_usd" REAL,
  "poster_amt_usd" REAL,
  "total_amt_usd" REAL
);
```

## Rows

- total=6912

| column | latest | sample | sample |
|---|---|---|---|
| id | 6912 | 1090 | 5750 |
| account_id | 4501 | 1761 | 2751 |
| occurred_at | 2016-12-21T13:30:42.000Z | 2016-11-03T06:09:53.000Z | 2016-11-26T08:53:34.000Z |
| standard_qty | 61 | 99 | 0 |
| gloss_qty | 150 | 64 | 615 |
| poster_qty | 52 | 51 | 331 |
| total | 263 | 214 | 946 |
| standard_amt_usd | 304.39 | 494.01 | 0 |
| gloss_amt_usd | 1123.5 | 479.36 | 4606.35 |
| poster_amt_usd | 422.24 | 414.12 | 2687.72 |
| total_amt_usd | 1850.13 | 1387.49 | 7294.07 |

## Columns

- id: unique identifier, int 1..6912
- account_id: 350 distinct, int 1001..4501
- occurred_at: 6908 distinct
- standard_qty: 678 distinct, int 0..22591
  - stats: average=280.432, median=290
- gloss_qty: 607 distinct, int 0..14281
  - stats: average=146.669, median=31
- poster_qty: 533 distinct, int 0..28262
  - stats: average=104.694, median=25
- total: 1359 distinct, int 0..28799
  - stats: average=531.795, median=480
- standard_amt_usd: 678 distinct, num 0..112729
  - stats: average=1399.36, median=1447.1
- gloss_amt_usd: 607 distinct, num 0..106965
  - stats: average=1098.55, median=232.19
- poster_amt_usd: 533 distinct, num 0..229487
  - stats: average=850.117, median=203
- total_amt_usd: 6597 distinct, num 0..232207
  - stats: average=3348.02, median=2482.86


# web_region

## All rows

| column | row 1 | row 2 | row 3 | row 4 |
|---|---|---|---|---|
| id | 1 | 2 | 3 | 4 |
| name | Northeast | Midwest | Southeast | West |


# web_sales_reps

```sql
CREATE TABLE "web_sales_reps" (
"id" INTEGER,
  "name" TEXT,
  "region_id" INTEGER
);
```

## Rows

- total=50

| column | latest | sample | sample |
|---|---|---|---|
| id | 321990 | 321850 | 321550 |
| name | Dawna Agnew | Calvin Ollison | Lavera Oles |
| region_id | 4 | 3 | 1 |

## Columns

- id: unique identifier, int 321500..321990
- name: all distinct
- region_id: 1=21, 3=10, 4=10, 2=9, int 1..4
