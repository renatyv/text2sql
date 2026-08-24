---
generator: db-snooper
version: 0.0.34
generated_at_utc: 2026-08-24T21:21:19.851352Z
dialect: sqlite
database: /var/folders/9j/b9bx_drd53sc6zbpsqyrjy4h0000gn/T/dbsnoop-x43txxxs/AdventureWorks.sqlite
schema: main
---

# "SalesPersonQuotaHistory"  (rows=163)

columns:
"BusinessEntityID" int: 274=12, 275=12, 276=12, 277=12, 278=12, 279=12, 280=12, 281=12, 282=12, 283=12, 287=8, 289=8, 290=8, 284=7, 285=4, 286=4, 288=4, 274..290
"QuotaDate" text: "2013-05-30 00:00:00"=17, "2013-08-30 00:00:00"=17, "2013-11-30 00:00:00"=17, "2014-03-01 00:00:00"=17, "2012-08-30 00:00:00"=14, "2012-11-30 00:00:00"=14, "2013-02-28 00:00:00"=14, "2012-05-30 00:00:00"=13, "2011-05-31 00:00:00"=10, "2011-08-31 00:00:00"=10, "2011-12-01 00:00:00"=10, "2012-02-29 00:00:00"=10
"SalesQuota" float: 154 distinct, 1000..1.9e+06, avg=587202, median=507000
"rowguid" text: unique identifier
"ModifiedDate" text: "2013-04-15 00:00:00"=17, "2013-07-16 00:00:00"=17, "2013-10-16 00:00:00"=17, "2014-01-15 00:00:00"=17, "2012-07-16 00:00:00"=14, "2012-10-16 00:00:00"=14, "2013-01-14 00:00:00"=14, "2012-04-15 00:00:00"=13, "2011-04-16 00:00:00"=10, "2011-07-17 00:00:00"=10, "2011-10-17 00:00:00"=10, "2012-01-15 00:00:00"=10

indexes: none

samples:
| column | latest | sample | sample |
|---|---|---|---|
| BusinessEntityID | 290 | 279 | 290 |
| QuotaDate | 2014-03-01 00:00:00 | 2013-02-28 00:00:00 | 2013-11-30 00:00:00 |
| SalesQuota | 908000 | 572000 | 707000 |
| rowguid | {00F2F9F8-5158-4436-B134-7E0C462289E5} | {173AD1F3-C953-4182-8168-97190CA5F929} | {A6CF1E2A-DA84-407A-9BEC-4AD473708C0B} |
| ModifiedDate | 2014-01-15 00:00:00 | 2013-01-14 00:00:00 | 2013-10-16 00:00:00 |

# "countryregioncurrency"  (rows=109)

columns:
"countryregioncode" text: 96 distinct
"currencycode" text: 97 distinct
"modifieddate" date: "2014-02-08 10:17:21.51"=99, "2008-04-30 00:00:00"=10

indexes: none

- latest rows skipped (unreadable values); random rows skipped (unreadable values)

# "currencyrate"  (rows=13532)

columns:
"currencyrateid" int: unique identifier, 1..13532, avg=6766.5, median=6766.5
"currencyratedate" date: 1097 distinct
"fromcurrencycode" text: "USD"=13532
"tocurrencycode" text: "ARS"=1097, "AUD"=1097, "BRL"=1097, "CAD"=1097, "CNY"=1097, "EUR"=1097, "GBP"=1097, "JPY"=1097, "MXN"=1097, "SAR"=1097, "USD"=1097, "VEB"=1097, "DEM"=184, "FRF"=184
"averagerate" float: 6127 distinct, 0.6046..1500, avg=79.2363, median=1.9816
"endofdayrate" float: 7232 distinct, 0.6041..1499.95, avg=79.2363, median=1.982
"modifieddate" date: 1098 distinct

indexes: none

- latest rows skipped (unreadable values); random rows skipped (unreadable values)

# "product"  (rows=504)

columns:
"productid" int: unique identifier, 1..999, avg=673.04, median=747.5
"NAME" text: all distinct
"productnumber" text: all distinct
"makeflag" bool→text: "f"=265, "t"=239
"finishedgoodsflag" bool→text: "t"=295, "f"=209
"color" text: ""=248, "Black"=93, "Silver"=43, "Red"=38, "Yellow"=36, "Blue"=26, "Multi"=8, "Silver/Black"=7, "White"=4, "Grey"=1
"safetystocklevel" int: 500=167, 1000=156, 100=97, 4=54, 800=25, 60=5, 4..1000
"reorderpoint" int: 375=167, 750=156, 75=97, 3=54, 600=25, 45=5, 3..750
"standardcost" float: 114 distinct, 0..2171.29, avg=258.603, median=23.3722
"listprice" float: 103 distinct, 0..3578.27, avg=438.666, median=49.99
"size" text: ""=293, "44"=29, "48"=25, "52"=16, "42"=15, "58"=15, "38"=12, "40"=11, "46"=11, "60"=11, "62"=11, "L"=11, "M"=11, "50"=9, "54"=9, "S"=9, "XL"=3, "56"=2, "70"=1
"sizeunitmeasurecode" text: ""=328, "CM "=176
"weightunitmeasurecode" text: ""=299, "LB "=176, "G  "=29
"weight" float: 128 distinct
"daystomanufacture" int: 0=246, 1=154, 4=97, 2=7, 0..4
"productline" text: ""=226, "R "=100, "M "=91, "T "=52, "S "=35
"class" text: ""=257, "L "=97, "H "=82, "M "=68
"style" text: ""=293, "U "=176, "W "=28, "M "=7
"productsubcategoryid" int: 38 distinct
"productmodelid" int: 120 distinct
"sellstartdate" date: "2008-04-30 00:00:00"=211, "2013-05-30 00:00:00"=136, "2012-05-30 00:00:00"=85, "2011-05-31 00:00:00"=72
"sellenddate" date: ""=406, "2013-05-29 00:00:00"=69, "2012-05-29 00:00:00"=29
"discontinueddate" date: ""=504
"rowguid" text: uuid, unique identifier
"modifieddate" date: "2014-02-08 10:01:36.827"=503, "2014-02-08 10:03:55.51"=1

indexes: none

- latest rows skipped (unreadable values); random rows skipped (unreadable values)

# "productcategory"  (rows=4)

columns:
"productcategoryid" int
"name" text
"rowguid" text
"modifieddate" date

indexes: none

all rows:
| column |  |
- sampled rows skipped (unreadable values)

# "productdescription"  (rows=762)

columns:
"productdescriptionid" int: unique identifier, 3..2010, avg=1542.58, median=1620.5
"description" text: 733 distinct
"rowguid" text: uuid, unique identifier
"modifieddate" date: "2013-04-30 00:00:00"=636, "2014-02-08 10:32:17.973"=126

indexes: none

- latest rows skipped (unreadable values); random rows skipped (unreadable values)

# "productmodelproductdescriptionculture"  (rows=762)

columns:
"productmodelid" int: 127 distinct, 1..127, avg=64, median=64
"productdescriptionid" int: unique identifier, 3..2010, avg=1542.58, median=1620.5
"cultureid" text: "ar"=127, "en"=127, "fr"=127, "he"=127, "th"=127, "zh-cht"=127
"modifieddate" date: "2013-04-30 00:00:00"=762

indexes: none

- latest rows skipped (unreadable values); random rows skipped (unreadable values)

# "productreview"  (rows=4)

columns:
"productreviewid" int
"productid" int
"reviewername" text
"reviewdate" date
"emailaddress" text
"rating" int
"comments" text
"modifeddate" date
"modifieddate" varchar19

indexes: none

all rows:
| column |  |
- sampled rows skipped (unreadable values)

# "productsubcategory"  (rows=37)

columns:
"productsubcategoryid" int: unique identifier, 1..37, avg=19, median=19
"productcategoryid" int: 2=14, 4=12, 3=8, 1=3, 1..4
"name" text: all distinct
"rowguid" text: uuid, unique identifier
"modifieddate" date: "2008-04-30 00:00:00"=37

indexes: none

- latest rows skipped (unreadable values); random rows skipped (unreadable values)

# "salesorderdetail"  (rows=121317)

columns:
"salesorderid" int: 43659..75123, avg=57827.4
"salesorderdetailid" int: 1..121317, avg=60659
"carriertrackingnumber" text: profile metrics skipped
"orderqty" int: 1..44, avg=2.26608
"productid" int: 707..999, avg=841.681
"specialofferid" int: 1..16, avg=1.16254
"unitprice" float: 1.3282..3578.27, avg=465.093
"unitpricediscount" float: 0..0.4, avg=0.00282607
"rowguid" text: uuid
"modifieddate" date: profile metrics skipped

indexes: none

- latest rows skipped (unreadable values); random rows skipped (unreadable values)

# "salesorderheader"  (rows=31465)

columns:
"salesorderid" int: unique identifier, 43659..75123, avg=59391, median=59391
"revisionnumber" int: 8=31435, 9=30
"orderdate" date: 1124 distinct
"duedate" date: 1124 distinct
"shipdate" date: 1124 distinct
"STATUS" text: "5"=31465
"onlineorderflag" bool→text: "t"=27659, "f"=3806
"purchaseordernumber" text: 3807 distinct
"accountnumber" text: 19119 distinct
"customerid" int: 19119 distinct, 11000..30118, avg=20170.2, median=19452
"salespersonid" int: ""=27659, 277=473, 275=450, 279=429, 276=418, 289=348, 282=271, 281=242, 278=234, 283=189, 290=175, 284=140, 288=130, 286=109, 280=95, 274=48, 287=39, 285=16
"territoryid" int: 9=6843, 4=6224, 1=4594, 6=4067, 10=3219, 7=2672, 8=2623, 5=486, 3=385, 2=352, 1..10
"billtoaddressid" int: 19119 distinct, 405..29883, avg=18263.2, median=19449
"shiptoaddressid" int: 19119 distinct, 9..29883, avg=18249.2, median=19438
"shipmethodid" int: 1=27659, 5=3806
"creditcardid" int: 18385 distinct
"creditcardapprovalcode" text: 30335 distinct
"currencyrateid" int: 2515 distinct
"subtotal" float: 4747 distinct, 1.374..163930, avg=3491.07, median=782.99
"taxamt" float: 4745 distinct, 0.1099..17948.5, avg=323.756, median=62.6392
"freight" float: 4744 distinct, 0.0344..5608.91, avg=101.174, median=19.5748
"totaldue" float: 4754 distinct, 1.5183..187488, avg=3916, median=865.204
"comment" text: ""=31465
"rowguid" text: uuid, unique identifier
"modifieddate" date: 1124 distinct

indexes: none

- latest rows skipped (unreadable values); random rows skipped (unreadable values)

# "salesperson"  (rows=17)

columns:
"businessentityid" int: unique identifier, 274..290, avg=282, median=282
"territoryid" int: 1=3, ""=3, 4=2, 6=2, 2=1, 3=1, 5=1, 7=1, 8=1, 9=1, 10=1
"salesquota" int: 250000=11, 300000=3, ""=3
"bonus" int: 0=3, 5000=2, 75=1, 500=1, 985=1, 2000=1, 2500=1, 3500=1, 3550=1, 3900=1, 4100=1, 5150=1, 5650=1, 6700=1, 0..6700
"commissionpct" float: 0.01=4, 0=3, 0.015=3, 0.012=2, 0.018=2, 0.016=1, 0.019=1, 0.02=1, 0..0.02
"salesytd" float: 172524=1, 519906=1, 559698=1, 1.4e+06=1, 1.4e+06=1, 1.5e+06=1, 1.6e+06=1, 1.6e+06=1, 1.8e+06=1, 2.3e+06=1, 2.5e+06=1, 2.6e+06=1, 3.1e+06=1, 3.2e+06=1, 3.8e+06=1, 4.1e+06=1, 4.3e+06=1, 172524..4.3e+06
"saleslastyear" float: 0=4, 1.3e+06=1, 1.4e+06=1, 1.4e+06=1, 1.6e+06=1, 1.6e+06=1, 1.8e+06=1, 1.8e+06=1, 1.9e+06=1, 2e+06=1, 2e+06=1, 2.1e+06=1, 2.3e+06=1, 2.4e+06=1, 0..2.4e+06
"rowguid" text: uuid, unique identifier
"modifieddate" date: "2011-05-24 00:00:00"=9, "2012-05-23 00:00:00"=2, "2013-05-23 00:00:00"=2, "2010-12-28 00:00:00"=1, "2012-04-09 00:00:00"=1, "2012-09-23 00:00:00"=1, "2013-03-07 00:00:00"=1

indexes: none

- latest rows skipped (unreadable values); random rows skipped (unreadable values)

# "salesterritory"  (rows=10)

columns:
"territoryid" int
"name" text
"countryregioncode" text
"group" text
"salesytd" float
"saleslastyear" float
"costytd" float
"costlastyear" float
"rowguid" text
"modifieddate" date

indexes: none

all rows:
| column |  |
- sampled rows skipped (unreadable values)
