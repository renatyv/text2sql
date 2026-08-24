---
generator: db-snooper
version: 0.0.34
generated_at_utc: 2026-08-24T21:59:19.847886Z
dialect: sqlite
database: /var/folders/9j/b9bx_drd53sc6zbpsqyrjy4h0000gn/T/dbsnoop-xo7ngxkp/education_business.sqlite
schema: main
---

# "SalaryDataset"  (rows=4344)

columns:
"index" int: all distinct, 0..4343, avg=2171.5, median=2171.5
"CompanyName" text: 2529 distinct, nulls=3
"JobTitle" text: 26 distinct
"SalariesReported" float: 49 distinct, nulls=2, 1..105, avg=2.77591, median=1
"Location" text: "Bangalore"=1584, "Pune"=818, "Hyderabad"=669, "New Delhi"=656, "Mumbai"=617
"Salary" text: 3101 distinct

indexes: none

samples:
| column | latest | sample | sample |
|---|---|---|---|
| index | 4343 | 3026 | 1292 |
| CompanyName | vPhrase | Accenture | JCB |
| JobTitle | Machine Learning Engineer | Data Engineer | Data Science |
| SalariesReported | 1 | 3 | 1 |
| Location | Mumbai | Bangalore | Pune |
| Salary | ₹9,39,843/yr | ₹50,367/mo | ₹1,12,474/yr |

# "StaffHours"  (rows=236)

columns:
"StaffMember" text: 26 distinct
"EventDate" text: 64 distinct
"EventTime" text: 107 distinct
"EventType" text: "Enter"=123, "Exit"=113

indexes: none

samples:
| column | latest | sample | sample |
|---|---|---|---|
| StaffMember | Z | M | W |
| EventDate | 2013-03-09 | 2013-03-12 | 2013-03-05 |
| EventTime | 11:45 | 07:55 | 12:20 |
| EventType | Enter | Enter | Enter |

# "hardware_dim_customer"  (rows=209)

columns:
"customer_code" int: all distinct, 70002017..90027207
"customer" text: 75 distinct
"platform" text: "Brick & Mortar"=150, "E-Commerce"=59
"channel" text: "Retailer"=164, "Direct"=40, "Distributor"=5
"market" text: 27 distinct
"sub_zone" text: "NE"=61, "SE"=44, "ROA"=38, "India"=18, "ANZ"=15, "LATAM"=7, nulls=26
"region" text: "EU"=105, "APAC"=71, "LATAM"=7, nulls=26

indexes: none

samples:
| column | latest | sample | sample |
|---|---|---|---|
| customer_code | 90027207 | 90021088 | 70014143 |
| customer | Amazon  | Electricalslytical | Atliq e Store |
| platform | E-Commerce | Brick & Mortar | E-Commerce |
| channel | Retailer | Retailer | Direct |
| market | Brazil | United Kingdom | Netherlands |
| sub_zone | LATAM | NE | NE |
| region | LATAM | EU | EU |

# "hardware_dim_product"  (rows=397)

columns:
"product_code" text: all distinct
"division" text: "P & A"=200, "PC"=161, "N & S"=36
"segment" text: "Notebook"=129, "Accessories"=116, "Peripherals"=84, "Desktop"=32, "Storage"=27, "Networking"=9
"category" text: "Personal Laptop"=61, "Keyboard"=48, "Mouse"=48, "Business Laptop"=44, "Gaming Laptop"=40, "Graphic Card"=36, "Batteries"=20, "MotherBoard"=20, "Processors"=18, "Personal Desktop"=16, "External Solid State Drives"=15, "USB Flash Drives"=12, "Internal HDD"=10, "Wi fi extender"=9
"product" text: 73 distinct
"variant" text: 27 distinct

indexes: none

samples:
| column | latest | sample | sample |
|---|---|---|---|
| product_code | A7321160303 | A0519150206 | A3320150501 |
| division | N & S | P & A | P & A |
| segment | Networking | Peripherals | Accessories |
| category | Wi fi extender | Graphic Card | Keyboard |
| product | AQ Wi Power Dx3 | AQ Mforce Gen Y | AQ Maxima |
| variant | Premium | Plus 3 | Standard 1 |

# "hardware_fact_gross_price"  (rows=579)

columns:
"product_code" text: 347 distinct
"fiscal_year" int: 2021=334, 2020=245
"gross_price" float: all distinct, 2.9168..834.981, avg=206.053, median=35.1332

indexes: none

samples:
| column | latest | sample | sample |
|---|---|---|---|
| product_code | A7321160303 | A1018150102 | A4218110204 |
| fiscal_year | 2021 | 2020 | 2020 |
| gross_price | 42.8483 | 117.15 | 225.693 |

# "hardware_fact_manufacturing_cost"  (rows=579)

columns:
"product_code" text: 347 distinct
"cost_year" int: 2021=334, 2020=245
"manufacturing_cost" float: 488 distinct, 0.892..240.536, avg=61.5661, median=10.4828

indexes: none

samples:
| column | latest | sample | sample |
|---|---|---|---|
| product_code | A7321160303 | A0620150305 | A3120150304 |
| cost_year | 2021 | 2021 | 2020 |
| manufacturing_cost | 12.9502 | 10.9579 | 4.3931 |

# "hardware_fact_pre_invoice_deductions"  (rows=418)

columns:
"customer_code" int: 209 distinct, 70002017..90027207
"fiscal_year" int: 2020=209, 2021=209
"pre_invoice_discount_pct" float: 351 distinct, 0.0531..0.3095, avg=0.233616, median=0.24005

indexes: none

samples:
| column | latest | sample | sample |
|---|---|---|---|
| customer_code | 90027207 | 90017057 | 90004064 |
| fiscal_year | 2021 | 2021 | 2020 |
| pre_invoice_discount_pct | 0.2772 | 0.1844 | 0.2174 |

# "hardware_fact_sales_monthly"  (rows=≈971631)

columns:
"date" text
"product_code" text
"customer_code" int
"sold_quantity" int
"fiscal_year" int

indexes: none


# "university_course"  (rows=7)

columns:
"CourseNo" text
"CrsDesc" text
"CrsUnits" int

indexes: none

all rows:
| column | row 1 | row 2 | row 3 | row 4 | row 5 | row 6 | row 7 |
|---|---|---|---|---|---|---|---|
| CourseNo | FIN300 | FIN450 | FIN480 | IS320 | IS460 | IS470 | IS480 |
| CrsDesc | FUNDAMENTALS OF FINANCE | PRINCIPLES OF INVESTMENTS | CORPORATE FINANCE | FUNDAMENTALS OF BUSINESS PROGRAMMING | SYSTEMS ANALYSIS | BUSINESS DATA COMMUNICATIONS | FUNDAMENTALS OF DATABASE MANAGEMENT |
| CrsUnits | 4 | 4 | 4 | 4 | 4 | 4 | 4 |

# "university_enrollment"  (rows=37)

columns:
"OfferNo" int: 9876=7, 1234=6, 4321=6, 5679=6, 5678=5, 7777=3, 5555=2, 6666=2, 1234..9876
"StdNo" int: 123456789=5, 124567890=4, 234567890=4, 567890123=4, 901234567=4, 345678901=3, 456789012=3, 678901234=3, 890123456=3, 789012345=2, 876543210=2, 123456789..901234567
"EnrGrade" float: 3.2=6, 3.4=6, 3.1=5, 3.3=4, 3.5=4, 2.6=2, 3.7=2, 3.8=2, 2=1, 2.7=1, 2.8=1, 2.9=1, 3.6=1, 4=1, 2..4

indexes: none

samples:
| column | latest | sample | sample |
|---|---|---|---|
| OfferNo | 9876 | 1234 | 4321 |
| StdNo | 901234567 | 678901234 | 123456789 |
| EnrGrade | 4 | 3.4 | 3.5 |

# "university_faculty"  (rows=8)

columns:
"FacNo" int
"FacFirstName" text
"FacLastName" text
"FacCity" text
"FacState" text
"FacDept" text
"FacRank" text
"FacSalary" int
"FacSupervisor" float
"FacHireDate" text
"FacZipCode" text

indexes: none

all rows:
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
| FacSupervisor | 6.5e+08 | 5.4e+08 | null | 5.4e+08 | null | 6.5e+08 | 7.7e+08 | 5.4e+08 |
| FacHireDate | 1997-04-10 | 2005-06-15 | 1998-04-15 | 1996-05-01 | 1999-04-11 | 2001-03-01 | 2002-03-15 | 2007-08-20 |
| FacZipCode | 98111-9921 | 98111-1234 | 98011-2242 | 98121-0094 | 98015-9945 | 98114-1332 | 98114-9954 | 98052-1234 |

# "university_offering"  (rows=13)

columns:
"OfferNo" int: 1111=1, 1234=1, 2222=1, 3333=1, 4321=1, 4444=1, 5555=1, 5678=1, 5679=1, 6666=1, 7777=1, 8888=1, 9876=1, 1111..9876
"CourseNo" text: "IS320"=6, "IS460"=2, "IS480"=2, "FIN300"=1, "FIN450"=1, "FIN480"=1
"OffTerm" text: "SPRING"=4, "WINTER"=4, "SUMMER"=3, "FALL"=2
"OffYear" int: 2010=10, 2009=3
"OffLocation" text: "BLM302"=4, "BLM214"=2, "BLM412"=2, "BLM207"=1, "BLM212"=1, "BLM305"=1, "BLM307"=1, "BLM405"=1
"OffTime" text: "10:30 AM"=4, "1:30 PM"=4, "3:30 PM"=3, "8:30 AM"=2
"FacNo" float: 9.9e+07=3, 6.5e+08=2, 7.7e+08=2, 9.9e+08=2, 5.4e+08=1, 8.8e+08=1, nulls=2, 9.9e+07..9.9e+08
"OffDays" text: "MW"=7, "TTH"=6

indexes: none

samples:
| column | latest | sample | sample |
|---|---|---|---|
| OfferNo | 9876 | 4444 | 9876 |
| CourseNo | IS460 | IS320 | IS460 |
| OffTerm | SPRING | WINTER | SPRING |
| OffYear | 2010 | 2010 | 2010 |
| OffLocation | BLM307 | BLM302 | BLM307 |
| OffTime | 1:30 PM | 3:30 PM | 1:30 PM |
| FacNo | 6.5e+08 | 5.4e+08 | 6.5e+08 |
| OffDays | TTH | TTH | TTH |

# "university_student"  (rows=11)

columns:
"StdNo" int: 123456789=1, 124567890=1, 234567890=1, 345678901=1, 456789012=1, 567890123=1, 678901234=1, 789012345=1, 876543210=1, 890123456=1, 901234567=1, 123456789..901234567
"StdFirstName" text: "BOB"=1, "CANDY"=1, "CRISTOPHER"=1, "HOMER"=1, "JOE"=1, "LUKE"=1, "MARIAH"=1, "ROBERTO"=1, "TESS"=1, "WALLY"=1, "WILLIAM"=1
"StdLastName" text: "DODGE"=2, "KENDALL"=2, "BRAZZI"=1, "COLAN"=1, "ESTRADA"=1, "MORALES"=1, "NORBERT"=1, "PILGRIM"=1, "WELLS"=1
"StdCity" text: "SEATTLE"=7, "BOTHELL"=2, "REDMOND"=1, "TACOMA"=1
"StdState" text: "WA"=11
"StdZip" text: "98011-2121"=1, "98113-1885"=1, "98114-0021"=1, "98114-1332"=1, "98116-0021"=1, "98116-2344"=1, "98121-1111"=1, "98121-2212"=1, "98121-2333"=1, "98123-1141"=1, "99042-3321"=1
"StdMajor" text: "IS"=6, "FIN"=3, "ACCT"=2
"StdClass" text: "JR"=4, "SR"=4, "SO"=2, "FR"=1
"StdGPA" float: 2.2=1, 2.5=1, 2.7=1, 2.8=1, 3=1, 3.2=1, 3.3=1, 3.5=1, 3.6=1, 3.8=1, 4=1, 2.2..4

indexes: none

samples:
| column | latest | sample | sample |
|---|---|---|---|
| StdNo | 901234567 | 234567890 | 890123456 |
| StdFirstName | WILLIAM | CANDY | LUKE |
| StdLastName | PILGRIM | KENDALL | BRAZZI |
| StdCity | BOTHELL | TACOMA | SEATTLE |
| StdState | WA | WA | WA |
| StdZip | 98113-1885 | 99042-3321 | 98116-0021 |
| StdMajor | IS | ACCT | IS |
| StdClass | SO | JR | SR |
| StdGPA | 3.8 | 3.5 | 2.2 |

# "web_accounts"  (rows=351)

columns:
"id" int: unique identifier, 1001..4501
"name" text: all distinct
"website" text: all distinct
"lat" float: all distinct, 30.4219..45.5557, avg=37.8614, median=38.6049
"long" float: all distinct, -122.682..-71.0513, avg=-92.3437, median=-84.4718
"primary_poc" text: 330 distinct
"sales_rep_id" int: 50 distinct, 321500..321990

indexes: none

samples:
| column | latest | sample | sample |
|---|---|---|---|
| id | 4501 | 1611 | 2041 |
| name | SpartanNash | Coca-Cola | Travelers Cos. |
| website | www.spartannash.com | www.coca-colacompany.com | www.travelers.com |
| lat | 45.5557 | 40.7622 | 42.3553 |
| long | -122.657 | -73.9802 | -71.0631 |
| primary_poc | Jewell Likes | Tisha Coletti | Vernie Pound |
| sales_rep_id | 321970 | 321690 | 321680 |

# "web_events"  (rows=9073)

columns:
"id" int: unique identifier, 1..9073
"account_id" int: 351 distinct, 1001..4501
"occurred_at" text: iso-date, all distinct
"channel" text: "direct"=5298, "facebook"=967, "organic"=952, "adwords"=906, "banner"=476, "twitter"=474

indexes: none

samples:
| column | latest | sample | sample |
|---|---|---|---|
| id | 9073 | 6991 | 4801 |
| account_id | 4501 | 2851 | 1331 |
| occurred_at | 2016-05-30T00:46:53.000Z | 2016-01-16T13:46:51.000Z | 2016-12-09T07:33:27.000Z |
| channel | organic | facebook | adwords |

# "web_orders"  (rows=6912)

columns:
"id" int: unique identifier, 1..6912
"account_id" int: 350 distinct, 1001..4501
"occurred_at" text: iso-date, 6908 distinct
"standard_qty" int: 678 distinct, 0..22591, avg=280.432, median=290
"gloss_qty" int: 607 distinct, 0..14281, avg=146.669, median=31
"poster_qty" int: 533 distinct, 0..28262, avg=104.694, median=25
"total" int: 1359 distinct, 0..28799, avg=531.795, median=480
"standard_amt_usd" float: 678 distinct, 0..112729, avg=1399.36, median=1447.1
"gloss_amt_usd" float: 607 distinct, 0..106965, avg=1098.55, median=232.19
"poster_amt_usd" float: 533 distinct, 0..229487, avg=850.117, median=203
"total_amt_usd" float: 6597 distinct, 0..232207, avg=3348.02, median=2482.86

indexes: none

samples:
| column | latest | sample | sample |
|---|---|---|---|
| id | 6912 | 1589 | 4751 |
| account_id | 4501 | 2181 | 1501 |
| occurred_at | 2016-12-21T13:30:42.000Z | 2016-02-02T07:11:27.000Z | 2016-12-05T01:27:01.000Z |
| standard_qty | 61 | 603 | 56 |
| gloss_qty | 150 | 5 | 480 |
| poster_qty | 52 | 0 | 445 |
| total | 263 | 608 | 981 |
| standard_amt_usd | 304.39 | 3008.97 | 279.44 |
| gloss_amt_usd | 1123.5 | 37.45 | 3595.2 |
| poster_amt_usd | 422.24 | 0 | 3613.4 |
| total_amt_usd | 1850.13 | 3046.42 | 7488.04 |

# "web_region"  (rows=4)

columns:
"id" int
"name" text

indexes: none

all rows:
| column | row 1 | row 2 | row 3 | row 4 |
|---|---|---|---|---|
| id | 1 | 2 | 3 | 4 |
| name | Northeast | Midwest | Southeast | West |

# "web_sales_reps"  (rows=50)

columns:
"id" int: unique identifier, 321500..321990
"name" text: all distinct
"region_id" int: 1=21, 3=10, 4=10, 2=9, 1..4

indexes: none

samples:
| column | latest | sample | sample |
|---|---|---|---|
| id | 321990 | 321830 | 321680 |
| name | Dawna Agnew | Maren Musto | Elna Condello |
| region_id | 4 | 3 | 1 |
