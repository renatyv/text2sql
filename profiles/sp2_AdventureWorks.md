---
generator: db-snooper
version: 0.0.26
generated_at_utc: 2026-08-16T08:07:35.952578Z
dialect: sqlite
database: /var/folders/9j/b9bx_drd53sc6zbpsqyrjy4h0000gn/T/dbsnoop-_obk3w61/AdventureWorks.sqlite
schema: main
---

# SalesPersonQuotaHistory

```sql
CREATE TABLE SalesPersonQuotaHistory (
    BusinessEntityID INTEGER,
    QuotaDate TEXT,
    SalesQuota REAL,
    rowguid TEXT,
    ModifiedDate TEXT
);
```

## Rows

- total=163

| column | latest | sample | sample |
|---|---|---|---|
| BusinessEntityID | 290 | 279 | 274 |
| QuotaDate | 2014-03-01 00:00:00 | 2013-11-30 00:00:00 | 2013-11-30 00:00:00 |
| SalesQuota | 908000 | 538000 | 84000 |
| rowguid | {00F2F9F8-5158-4436-B134-7E0C462289E5} | {95B4B50B-08E7-4B71-A68C-B55F9400395B} | {7CEA47B5-8391-4414-A866-FF6EC6628CD3} |
| ModifiedDate | 2014-01-15 00:00:00 | 2013-10-16 00:00:00 | 2013-10-16 00:00:00 |

## Columns

- BusinessEntityID: 274=12, 275=12, 276=12, 277=12, 278=12, 279=12, 280=12, 281=12, 282=12, 283=12, 287=8, 289=8, 290=8, 284=7, 285=4, 286=4, 288=4, int 274..290
- QuotaDate: "2013-05-30 00:00:00"=17, "2013-08-30 00:00:00"=17, "2013-11-30 00:00:00"=17, "2014-03-01 00:00:00"=17, "2012-08-30 00:00:00"=14, "2012-11-30 00:00:00"=14, "2013-02-28 00:00:00"=14, "2012-05-30 00:00:00"=13, "2011-05-31 00:00:00"=10, "2011-08-31 00:00:00"=10, "2011-12-01 00:00:00"=10, "2012-02-29 00:00:00"=10
- SalesQuota: 154 distinct, num 1000..1.898e+06
  - stats: average=587202, median=507000
- rowguid: unique identifier
- ModifiedDate: "2013-04-15 00:00:00"=17, "2013-07-16 00:00:00"=17, "2013-10-16 00:00:00"=17, "2014-01-15 00:00:00"=17, "2012-07-16 00:00:00"=14, "2012-10-16 00:00:00"=14, "2013-01-14 00:00:00"=14, "2012-04-15 00:00:00"=13, "2011-04-16 00:00:00"=10, "2011-07-17 00:00:00"=10, "2011-10-17 00:00:00"=10, "2012-01-15 00:00:00"=10


# countryregioncurrency

```sql
CREATE TABLE countryregioncurrency (
    countryregioncode TEXT,
    currencycode TEXT,
    modifieddate DATE
    );
```

## Rows

- total=109

- (no rows sampled)

## Columns

- countryregioncode: 96 distinct
- currencycode: 97 distinct
- modifieddate: 2 distinct
  - value counts: skipped (query timeout > 10s)


# currencyrate

```sql
CREATE TABLE currencyrate (
    currencyrateid INTEGER,
    currencyratedate DATE,
    fromcurrencycode TEXT,
    tocurrencycode TEXT,
    averagerate FLOAT,
    endofdayrate FLOAT,
    modifieddate DATE
    );
```

## Rows

- total=13532

- (no rows sampled)

## Columns

- currencyrateid: unique identifier, int 1..13532
  - stats: average=6766.5, median=6766.5
- currencyratedate: 1097 distinct
- fromcurrencycode: "USD"=13532
- tocurrencycode: "ARS"=1097, "AUD"=1097, "BRL"=1097, "CAD"=1097, "CNY"=1097, "EUR"=1097, "GBP"=1097, "JPY"=1097, "MXN"=1097, "SAR"=1097, "USD"=1097, "VEB"=1097, "DEM"=184, "FRF"=184
- averagerate: 6127 distinct, num 0.6046..1500
  - stats: average=79.2363, median=1.9816
- endofdayrate: 7232 distinct, num 0.6041..1499.95
  - stats: average=79.2363, median=1.982
- modifieddate: 1098 distinct


# product

```sql
CREATE TABLE product (
    productid INTEGER,
    NAME TEXT,
    productnumber TEXT,
    makeflag BOOLEAN,
    finishedgoodsflag BOOLEAN,
    color TEXT,
    safetystocklevel INTEGER,
    reorderpoint INTEGER,
    standardcost FLOAT,
    listprice FLOAT,
    size TEXT,
    sizeunitmeasurecode TEXT,
    weightunitmeasurecode TEXT,
    weight FLOAT,
    daystomanufacture INTEGER,
    productline TEXT,
    class TEXT,
    style TEXT,
    productsubcategoryid INTEGER,
    productmodelid INTEGER,
    sellstartdate DATE,
    sellenddate DATE,
    discontinueddate DATE,
    rowguid TEXT,
    modifieddate DATE
    );
```

## Rows

- total=504

- (no rows sampled)

## Columns

- productid: unique identifier, int 1..999
  - stats: average=673.04, median=747.5
- NAME: all distinct
- productnumber: all distinct
- makeflag: True=265, True=239
- finishedgoodsflag: True=295, True=209
- color: ""=248, "Black"=93, "Silver"=43, "Red"=38, "Yellow"=36, "Blue"=26, "Multi"=8, "Silver/Black"=7, "White"=4, "Grey"=1
- safetystocklevel: 500=167, 1000=156, 100=97, 4=54, 800=25, 60=5, int 4..1000
- reorderpoint: 375=167, 750=156, 75=97, 3=54, 600=25, 45=5, int 3..750
- standardcost: 114 distinct, num 0..2171.29
  - stats: average=258.603, median=23.3722
- listprice: 103 distinct, num 0..3578.27
  - stats: average=438.666, median=49.99
- size: ""=293, "44"=29, "48"=25, "52"=16, "42"=15, "58"=15, "38"=12, "40"=11, "46"=11, "60"=11, "62"=11, "L"=11, "M"=11, "50"=9, "54"=9, "S"=9, "XL"=3, "56"=2, "70"=1
- sizeunitmeasurecode: ""=328, "CM "=176
- weightunitmeasurecode: ""=299, "LB "=176, "G  "=29
- weight: 128 distinct, num 2.12..
  - stats: average=30.1274, median=0
- daystomanufacture: 0=246, 1=154, 4=97, 2=7, int 0..4
- productline: ""=226, "R "=100, "M "=91, "T "=52, "S "=35
- class: ""=257, "L "=97, "H "=82, "M "=68
- style: ""=293, "U "=176, "W "=28, "M "=7
- productsubcategoryid: 38 distinct, int 1..
  - stats: average=7.19643, median=22
- productmodelid: 120 distinct, int 1..
  - stats: average=21.9167, median=85.5
- sellstartdate: 4 distinct
  - value counts: skipped (query timeout > 10s)
- sellenddate: 3 distinct
  - value counts: skipped (query timeout > 10s)
- discontinueddate: 1 distinct
  - value counts: skipped (query timeout > 10s)
- rowguid: unique identifier
- modifieddate: 2 distinct
  - value counts: skipped (query timeout > 10s)


# productcategory

## Rows

- total=4

- (no rows sampled)


# productdescription

```sql
CREATE TABLE productdescription (
    productdescriptionid INTEGER,
    description TEXT,
    rowguid TEXT,
    modifieddate DATE
    );
```

## Rows

- total=762

- (no rows sampled)

## Columns

- productdescriptionid: unique identifier, int 3..2010
  - stats: average=1542.58, median=1620.5
- description: 733 distinct
- rowguid: unique identifier
- modifieddate: 2 distinct
  - value counts: skipped (query timeout > 10s)


# productmodelproductdescriptionculture

```sql
CREATE TABLE productmodelproductdescriptionculture (
    productmodelid INTEGER,
    productdescriptionid INTEGER,
    cultureid TEXT,
    modifieddate DATE
    );
```

## Rows

- total=762

- (no rows sampled)

## Columns

- productmodelid: 127 distinct, int 1..127
  - stats: average=64, median=64
- productdescriptionid: unique identifier, int 3..2010
  - stats: average=1542.58, median=1620.5
- cultureid: "ar"=127, "en"=127, "fr"=127, "he"=127, "th"=127, "zh-cht"=127
- modifieddate: 1 distinct
  - value counts: skipped (query timeout > 10s)


# productreview

## Rows

- total=4

- (no rows sampled)


# productsubcategory

```sql
CREATE TABLE productsubcategory (
    productsubcategoryid INTEGER,
    productcategoryid INTEGER,
    name TEXT,
    rowguid TEXT,
    modifieddate DATE
    );
```

## Rows

- total=37

- (no rows sampled)

## Columns

- productsubcategoryid: unique identifier, int 1..37
  - stats: average=19, median=19
- productcategoryid: 2=14, 4=12, 3=8, 1=3, int 1..4
- name: all distinct
- rowguid: unique identifier
- modifieddate: 1 distinct
  - value counts: skipped (query timeout > 10s)


# salesorderdetail

```sql
CREATE TABLE salesorderdetail (
    salesorderid INTEGER,
    salesorderdetailid INTEGER,
    carriertrackingnumber TEXT,
    orderqty INTEGER,
    productid INTEGER,
    specialofferid INTEGER,
    unitprice FLOAT,
    unitpricediscount FLOAT,
    rowguid TEXT,
    modifieddate DATE
    );
```

## Rows

- total=121317

- (no rows sampled)

## Columns

- salesorderid: int 43659..75123
  - stats: average=57827.4
- salesorderdetailid: int 1..121317
  - stats: average=60659
- carriertrackingnumber: profile metrics skipped
- orderqty: int 1..44
  - stats: average=2.26608
- productid: int 707..999
  - stats: average=841.681
- specialofferid: int 1..16
  - stats: average=1.16254
- unitprice: num 1.3282..3578.27
  - stats: average=465.093
- unitpricediscount: num 0..0.4
  - stats: average=0.00282607
- rowguid: profile metrics skipped
- modifieddate: profile metrics skipped


# salesorderheader

```sql
CREATE TABLE salesorderheader (
    salesorderid INTEGER,
    revisionnumber INTEGER,
    orderdate DATE,
    duedate DATE,
    shipdate DATE,
    STATUS TEXT,
    onlineorderflag BOOLEAN,
    purchaseordernumber TEXT,
    accountnumber TEXT,
    customerid INTEGER,
    salespersonid INTEGER,
    territoryid INTEGER,
    billtoaddressid INTEGER,
    shiptoaddressid INTEGER,
    shipmethodid INTEGER,
    creditcardid INTEGER,
    creditcardapprovalcode TEXT,
    currencyrateid INTEGER,
    subtotal FLOAT,
    taxamt FLOAT,
    freight FLOAT,
    totaldue FLOAT,
    comment TEXT,
    rowguid TEXT,
    modifieddate DATE
    );
```

## Rows

- total=31465

- (no rows sampled)

## Columns

- salesorderid: unique identifier, int 43659..75123
  - stats: average=59391, median=59391
- revisionnumber: 8=31435, 9=30
- orderdate: 1124 distinct
- duedate: 1124 distinct
- shipdate: 1124 distinct
- STATUS: "5"=31465
- onlineorderflag: True=27659, True=3806
- purchaseordernumber: 3807 distinct
- accountnumber: 19119 distinct
- customerid: 19119 distinct, int 11000..30118
  - stats: average=20170.2, median=19452
- salespersonid: ""=27659, 277=473, 275=450, 279=429, 276=418, 289=348, 282=271, 281=242, 278=234, 283=189, 290=175, 284=140, 288=130, 286=109, 280=95, 274=48, 287=39, 285=16, int 274..
- territoryid: 9=6843, 4=6224, 1=4594, 6=4067, 10=3219, 7=2672, 8=2623, 5=486, 3=385, 2=352, int 1..10
- billtoaddressid: 19119 distinct, int 405..29883
  - stats: average=18263.2, median=19449
- shiptoaddressid: 19119 distinct, int 9..29883
  - stats: average=18249.2, median=19438
- shipmethodid: 1=27659, 5=3806
- creditcardid: 18385 distinct, int 1..
  - stats: average=9336.01, median=10073
- creditcardapprovalcode: 30335 distinct
- currencyrateid: 2515 distinct, int 2..
  - stats: average=4082.64, median=0
- subtotal: 4747 distinct, num 1.374..163930
  - stats: average=3491.07, median=782.99
- taxamt: 4745 distinct, num 0.1099..17948.5
  - stats: average=323.756, median=62.6392
- freight: 4744 distinct, num 0.0344..5608.91
  - stats: average=101.174, median=19.5748
- totaldue: 4754 distinct, num 1.5183..187488
  - stats: average=3916, median=865.204
- comment: ""=31465
- rowguid: unique identifier
- modifieddate: 1124 distinct


# salesperson

```sql
CREATE TABLE salesperson (
 businessentityid INTEGER,
 territoryid INTEGER,
 salesquota INTEGER,
 bonus INTEGER,
 commissionpct FLOAT,
 salesytd FLOAT,
 saleslastyear FLOAT,
 rowguid TEXT,
 modifieddate DATE
 );
```

## Rows

- total=17

- (no rows sampled)

## Columns

- businessentityid: unique identifier, int 274..290
  - stats: average=282, median=282
- territoryid: 1=3, ""=3, 4=2, 6=2, 2=1, 3=1, 5=1, 7=1, 8=1, 9=1, 10=1, int 1..
- salesquota: 250000=11, 300000=3, ""=3, int 250000..
- bonus: 0=3, 5000=2, 75=1, 500=1, 985=1, 2000=1, 2500=1, 3500=1, 3550=1, 3900=1, 4100=1, 5150=1, 5650=1, 6700=1, int 0..6700
- commissionpct: 0.01=4, 0=3, 0.015=3, 0.012=2, 0.018=2, 0.016=1, 0.019=1, 0.02=1, num 0..0.02
- salesytd: 172524=1, 519906=1, 559698=1, 1.35258e+06=1, 1.42181e+06=1, 1.45372e+06=1, 1.57301e+06=1, 1.57656e+06=1, 1.82707e+06=1, 2.31519e+06=1, 2.45854e+06=1, 2.60454e+06=1, 3.12162e+06=1, 3.18942e+06=1, 3.76318e+06=1, 4.11687e+06=1, 4.25137e+06=1, num 172524..4.25137e+06
- saleslastyear: 0=4, 1.30795e+06=1, 1.37164e+06=1, 1.43916e+06=1, 1.62028e+06=1, 1.63582e+06=1, 1.75041e+06=1, 1.84964e+06=1, 1.92706e+06=1, 1.99719e+06=1, 2.03823e+06=1, 2.07351e+06=1, 2.27855e+06=1, 2.39654e+06=1, num 0..2.39654e+06
- rowguid: unique identifier
- modifieddate: 7 distinct
  - value counts: skipped (query timeout > 10s)


# salesterritory

## Rows

- total=10

- (no rows sampled)
