---
generator: db-snooper
version: 0.0.26
generated_at_utc: 2026-08-16T07:18:32.304835Z
dialect: sqlite
database: /Users/renatyuldashev/Documents/ai-sql/custom-bench/data/bird_mini_dev/databases/dev_databases/california_schools/california_schools.sqlite
schema: main
---

## Relationships

- schools.CDSCode ← frpm.CDSCode, satscores.cds

# frpm

```sql
CREATE TABLE frpm
(
    CDSCode                                       TEXT not null
        primary key,
    `Academic Year`                               TEXT  null,
    `County Code`                                 TEXT  null,
    `District Code`                               INTEGER         null,
    `School Code`                                 TEXT  null,
    `County Name`                                 TEXT null,
    `District Name`                               TEXT null,
    `School Name`                                 TEXT null,
    `District Type`                               TEXT null,
    `School Type`                                 TEXT null,
    `Educational Option Type`                     TEXT null,
    `NSLP Provision Status`                       TEXT null,
    `Charter School (Y/N)`                        INTEGER    null,
    `Charter School Number`                       TEXT  null,
    `Charter Funding Type`                        TEXT null,
    IRC                                           INTEGER    null,
    `Low Grade`                                   TEXT  null,
    `High Grade`                                  TEXT null,
    `Enrollment (K-12)`                           REAL      null,
    `Free Meal Count (K-12)`                      REAL       null,
    `Percent (%) Eligible Free (K-12)`            REAL       null,
    `FRPM Count (K-12)`                           REAL       null,
    `Percent (%) Eligible FRPM (K-12)`            REAL       null,
    `Enrollment (Ages 5-17)`                      REAL       null,
    `Free Meal Count (Ages 5-17)`                 REAL       null,
    `Percent (%) Eligible Free (Ages 5-17)`       REAL       null,
    `FRPM Count (Ages 5-17)`                      REAL       null,
    `Percent (%) Eligible FRPM (Ages 5-17)`       REAL       null,
    `2013-14 CALPADS Fall 1 Certification Status` INTEGER    null,
    foreign key (CDSCode) references schools (CDSCode)
);
```

## Rows

- total=9986

| column | latest | sample | sample |
|---|---|---|---|
| CDSCode | 58727695838305 | 50755726053219 | 31669510113068 |
| Academic Year | 2014-2015 | 2014-2015 | 2014-2015 |
| County Code | 58 | 50 | 31 |
| District Code | 72769 | 75572 | 66951 |
| School Code | 5838305 | 6053219 | 0113068 |
| County Name | Yuba | Stanislaus | Placer |
| District Name | Wheatland Union High | Waterford Unified | Western Placer Unified |
| School Name | Wheatland Union High | Waterford Junior | Lincoln Crossing Elementary |
| District Type | High School District | Unified School District | Unified School District |
| School Type | High Schools (Public) | Junior High Schools (Public) | Elementary Schools (Public) |
| Educational Option Type | Traditional | Traditional | Traditional |
| NSLP Provision Status | null | null | null |
| Charter School (Y/N) | 0 | 0 | 0 |
| Charter School Number | null | null | null |
| Charter Funding Type | null | null | null |
| IRC | 0 | 0 | 0 |
| Low Grade | 9 | 7 | K |
| High Grade | 12 | 8 | 5 |
| Enrollment (K-12) | 732 | 248 | 666 |
| Free Meal Count (K-12) | 164 | 176 | 101 |
| Percent (%) Eligible Free (K-12) | 0.224044 | 0.709677 | 0.151652 |
| FRPM Count (K-12) | 227 | 212 | 128 |
| Percent (%) Eligible FRPM (K-12) | 0.310109 | 0.854839 | 0.192192 |
| Enrollment (Ages 5-17) | 711 | 248 | 666 |
| Free Meal Count (Ages 5-17) | 158 | 176 | 101 |
| Percent (%) Eligible Free (Ages 5-17) | 0.222222 | 0.709677 | 0.151652 |
| FRPM Count (Ages 5-17) | 220 | 212 | 128 |
| Percent (%) Eligible FRPM (Ages 5-17) | 0.309423 | 0.854839 | 0.192192 |
| 2013-14 CALPADS Fall 1 Certification Status | 1 | 1 | 1 |

## Columns

- CDSCode: unique identifier
- Academic Year: "2014-2015"=9986
- County Code: 58 distinct
- District Code: 1012 distinct, int 10017..76901
  - stats: average=65651.5, median=67082
- School Code: 9942 distinct
- County Name: 58 distinct
- District Name: 1000 distinct
- School Name: 8652 distinct
- District Type: "Unified School District"=6744, "Elementary School District"=2356, "High School District"=529, "County Office of Education (COE)"=334, "State Board of Education"=10, "Statewide Benefit Charter"=6, "Non-School Locations"=4, "State Special Schools"=3
- School Type: "Elementary Schools (Public)"=5584, "High Schools (Public)"=1331, "Intermediate/Middle Schools (Public)"=1299, "Continuation High Schools"=459, "Alternative Schools of Choice"=259, "K-12 Schools (Public)"=240, "Elemen Schools In 1 School Dist. (Public)"=206, "District Community Day Schools"=203, "Special Education Schools (Public)"=132, "County Community"=75, "Juvenile Court Schools"=74, "Junior High Schools (Public)"=46, "Opportunity Schools"=23, "Youth Authority Facilities"=4, "State Special Schools"=3, "Preschool"=2, "High Schools In 1 School Dist. (Public)"=1, nulls=45
- Educational Option Type: "Traditional"=8696, "Continuation School"=459, "Alternative School of Choice"=259, "Community Day School"=203, "Special Education School"=128, "County Community School"=84, "Juvenile Court School"=74, "Opportunity School"=24, "District Special Education Consortia School"=4, "Youth Authority School"=4, "Home and Hospital"=3, "State Special School"=3, nulls=45
- NSLP Provision Status: "Provision 2"=1365, "Breakfast Provision 2"=285, "CEP"=172, "Multiple Provision Types"=11, "Provision 1"=7, "Lunch Provision 2"=5, "Provision 3"=2, nulls=8139
- Charter School (Y/N): 0=8774, 1=1167, nulls=45
- Charter School Number: 1152 distinct, nulls=8819
- Charter Funding Type: "Directly funded"=838, "Locally funded"=328, "Not in CS funding model"=1, nulls=8819
- IRC: 0=9212, 1=729, nulls=45
- Low Grade: "K"=6057, "9"=1733, "6"=1024, "7"=651, "P"=181, "5"=99, "4"=68, "10"=44, "1"=42, "3"=38, "2"=19, "11"=14, "8"=10, "12"=3, "Adult"=3
- High Grade: "12"=2641, "5"=2534, "8"=2401, "6"=2091, "3"=68, "4"=65, "2"=40, "Adult"=35, "7"=30, "1"=22, "9"=19, "K"=18, "10"=13, "11"=5, "P"=2, "13"=1, "Post Secondary"=1
- Enrollment (K-12): 1882 distinct, num 1..5333
  - stats: average=620.826, median=528
- Free Meal Count (K-12): 1216 distinct, nulls=56, num 1..3927
  - stats: average=312.004, median=235
- Percent (%) Eligible Free (K-12): 8658 distinct, nulls=56, num 0.00176056..1
  - stats: average=0.529639, median=0.568935
- FRPM Count (K-12): 1361 distinct, nulls=50, num 1..4419
  - stats: average=365.48, median=285
- Percent (%) Eligible FRPM (K-12): 8623 distinct, nulls=50, num 0.00220507..1
  - stats: average=0.612085, median=0.682927
- Enrollment (Ages 5-17): 1845 distinct, nulls=14, num 1..5271
  - stats: average=605.325, median=517.5
- Free Meal Count (Ages 5-17): 1205 distinct, nulls=78, num 1..3864
  - stats: average=304.032, median=230
- Percent (%) Eligible Free (Ages 5-17): 8552 distinct, nulls=78, num 0.00179856..1
  - stats: average=0.531708, median=0.57199
- FRPM Count (Ages 5-17): 1330 distinct, nulls=72, num 1..4347
  - stats: average=356.514, median=279
- Percent (%) Eligible FRPM (Ages 5-17): 8557 distinct, nulls=72, num 0.00220507..1
  - stats: average=0.614618, median=0.687139
- 2013-14 CALPADS Fall 1 Certification Status: 1=9986


# satscores

```sql
CREATE TABLE satscores
(
    cds         TEXT not null
        primary key,
    rtype       TEXT  not null,
    sname       TEXT null,
    dname       TEXT null,
    cname       TEXT null,
    enroll12    INTEGER         not null,
    NumTstTakr  INTEGER          not null,
    AvgScrRead  INTEGER          null,
    AvgScrMath  INTEGER          null,
    AvgScrWrite INTEGER          null,
    NumGE1500   INTEGER          null,
--     PctGE1500   double      null,
        foreign key (cds) references schools (CDSCode)
);
```

## Rows

- total=2269

| column | latest | sample | sample |
|---|---|---|---|
| cds | 58727695838305 | 04614320433201 | 31669443130010 |
| rtype | S | S | S |
| sname | Wheatland Union High | Durham High | North Tahoe High |
| dname | Wheatland Union High | Durham Unified | Tahoe-Truckee Unified |
| cname | Yuba | Butte | Placer |
| enroll12 | 160 | 76 | 71 |
| NumTstTakr | 54 | 43 | 55 |
| AvgScrRead | 480 | 498 | 518 |
| AvgScrMath | 475 | 484 | 512 |
| AvgScrWrite | 463 | 472 | 508 |
| NumGE1500 | 21 | 19 | 34 |

## Columns

- cds: unique identifier
- rtype: "S"=1749, "D"=520
- sname: 1665 distinct, nulls=520
- dname: 520 distinct
- cname: 57 distinct
- enroll12: 835 distinct, int 0..43324
  - stats: average=419.519, median=220
- NumTstTakr: 547 distinct, int 0..24305
  - stats: average=185.098, median=83
- AvgScrRead: 269 distinct, nulls=596, int 308..653
  - stats: average=479.699, median=481
- AvgScrMath: 295 distinct, nulls=596, int 289..699
  - stats: average=484.461, median=483
- AvgScrWrite: 267 distinct, nulls=596, int 312..671
  - stats: average=472.529, median=471
- NumGE1500: 368 distinct, nulls=596, int 0..5837
  - stats: average=111.079, median=44


# schools

```sql
CREATE TABLE schools
(
    CDSCode     TEXT not null
        primary key,
    NCESDist    TEXT  null,
    NCESSchool  TEXT  null,
    StatusType  TEXT  not null,
    County      TEXT not null,
    District    TEXT not null,
    School      TEXT null,
    Street      TEXT null,
    StreetAbr   TEXT null,
    City        TEXT null,
    Zip         TEXT null,
    State       TEXT  null,
    MailStreet  TEXT null,
    MailStrAbr  TEXT null,
    MailCity    TEXT null,
    MailZip     TEXT null,
    MailState   TEXT  null,
    Phone       TEXT null,
    Ext         TEXT  null,
    Website     TEXT null,
    OpenDate    DATE        null,
    ClosedDate  DATE        null,
    Charter     INTEGER    null,
    CharterNum  TEXT  null,
    FundingType TEXT null,
    DOC         TEXT  not null,
    DOCType     TEXT not null,
    SOC         TEXT  null,
    SOCType     TEXT null,
    EdOpsCode   TEXT  null,
    EdOpsName   TEXT null,
    EILCode     TEXT  null,
    EILName     TEXT null,
    GSoffered   TEXT null,
    GSserved    TEXT  null,
    Virtual     TEXT  null,
    Magnet      INTEGER   null,
    Latitude    REAL      null,
    Longitude   REAL      null,
    AdmFName1   TEXT null,
    AdmLName1   TEXT null,
    AdmEmail1   TEXT null,
    AdmFName2   TEXT null,
    AdmLName2   TEXT null,
    AdmEmail2   TEXT null,
    AdmFName3   TEXT  null,
    AdmLName3   TEXT null,
    AdmEmail3   TEXT null,
    LastUpdate  DATE        not null
);
```

## Rows

- total=17686

| column | latest | sample | sample |
|---|---|---|---|
| CDSCode | 58727695838305 | 10621176110258 | 19642460115337 |
| NCESDist | 0642350 | 0609030 | 0602820 |
| NCESSchool | 06930 | 01982 | 12172 |
| StatusType | Active | Active | Active |
| County | Yuba | Fresno | Los Angeles |
| District | Wheatland Union High | Clovis Unified | Antelope Valley Union High |
| School | Wheatland Union High | Garfield Elementary | Los Angeles County Online High |
| Street | 1010 Wheatland Road | 1315 North Peach Avenue | 2600 Foothill Boulevard, #301 |
| StreetAbr | 1010 Wheatland Rd. | 1315 North Peach Ave. | 2600 Foothill Blvd., #301 |
| City | Wheatland | Clovis | La Crescenta |
| Zip | 95692-9798 | 93611-8342 | 91214-3588 |
| State | CA | CA | CA |
| MailStreet | 1010 Wheatland Road | 1315 North Peach Avenue | 2600 Foothill Boulevard, #301 |
| MailStrAbr | 1010 Wheatland Rd. | 1315 North Peach Ave. | 2600 Foothill Blvd., #301 |
| MailCity | Wheatland | Clovis | La Crescenta |
| MailZip | 95692-9798 | 93611-8342 | 91214-3588 |
| MailState | CA | CA | CA |
| Phone | (530) 633-3100 | (559) 327-6800 | (800) 985-0770 |
| Ext | null | null | null |
| Website | www.wheatlandhigh.org | null | www.olinacademy.org |
| OpenDate | 1980-07-01 | 1993-08-10 | 2007-09-04 |
| ClosedDate | null | null | null |
| Charter | 0 | 0 | 1 |
| CharterNum | null | null | 0915 |
| FundingType | null | null | Directly funded |
| DOC | 56 | 54 | 56 |
| DOCType | High School District | Unified School District | High School District |
| SOC | 66 | 60 | 66 |
| SOCType | High Schools (Public) | Elementary Schools (Public) | High Schools (Public) |
| EdOpsCode | TRAD | TRAD | TRAD |
| EdOpsName | Traditional | Traditional | Traditional |
| EILCode | HS | ELEM | HS |
| EILName | High School | Elementary | High School |
| GSoffered | 9-12 | K-6 | 9-12 |
| GSserved | 9-12 | K-6 | 9-12 |
| Virtual | N | N | F |
| Magnet | 0 | 0 | 0 |
| Latitude | 38.999 | 36.8533 | 34.221 |
| Longitude | -121.455 | -119.719 | -118.235 |
| AdmFName1 | Vic | Jennifer | Kim |
| AdmLName1 | Ramos | Bump | Fairburn |
| AdmEmail1 | vramos@wheatlandhigh.org | jenniferbump@cusd.com | kfairburn@olinacademy.org |
| AdmFName2 | null | null | null |
| AdmLName2 | null | null | null |
| AdmEmail2 | null | null | null |
| AdmFName3 | null | null | null |
| AdmLName3 | null | null | null |
| AdmEmail3 | null | null | null |
| LastUpdate | 2015-06-18 | 2016-07-19 | 2016-08-02 |

## Columns

- CDSCode: unique identifier
- NCESDist: 1193 distinct, nulls=1030
- NCESSchool: 12321 distinct, nulls=5040
- StatusType: "Active"=11708, "Closed"=4518, "Merged"=1448, "Pending"=12
- County: 58 distinct
- District: 1411 distinct
- School: 13875 distinct, nulls=1369
- Street: 13593 distinct, nulls=294
- StreetAbr: 13633 distinct, nulls=294
- City: 1165 distinct, nulls=293
- Zip: 11184 distinct, nulls=293
- State: "CA"=17393, nulls=293
- MailStreet: 12395 distinct, nulls=292
- MailStrAbr: 12429 distinct, nulls=292
- MailCity: 1132 distinct, nulls=292
- MailZip: 10298 distinct, nulls=292
- MailState: "CA"=17394, nulls=292
- Phone: 10632 distinct, nulls=5969
- Ext: 379 distinct, nulls=17146
- Website: 4082 distinct, nulls=10722
- OpenDate: 1406 distinct, nulls=1369
- ClosedDate: 899 distinct, nulls=11992
- Charter: 0=14588, 1=1729, nulls=1369
- CharterNum: 1763 distinct, nulls=15885
- FundingType: "Directly funded"=1176, "Locally funded"=460, "Not in CS funding model"=6, nulls=16044
- DOC: "54"=10190, "52"=4378, "00"=1703, "56"=1079, "98"=156, "02"=69, "34"=49, "58"=33, "03"=11, "99"=10, "31"=6, "42"=2
- DOCType: "Unified School District"=10190, "Elementary School District"=4378, "County Office of Education (COE)"=1703, "High School District"=1079, "Regional Occupation Center/Program (ROC/P)"=156, "State Board of Education"=69, "Non-School Locations"=49, "Community College District"=33, "Statewide Benefit Charter"=11, "Administration Only"=10, "State Special Schools"=6, "Joint Powers Authority (JPA)"=2
- SOC: 20 distinct, nulls=1369
- SOCType: 20 distinct, nulls=1369
- EdOpsCode: "TRAD"=10103, "CON"=539, "COMMDAY"=486, "ALTSOC"=320, "SPEC"=228, "COMM"=133, "JUV"=94, "OPP"=47, "ROP"=6, "YTH"=6, "HOMHOS"=5, "SPECON"=5, "SSS"=3, nulls=5711
- EdOpsName: "Traditional"=10103, "Continuation School"=539, "Community Day School"=486, "Alternative School of Choice"=320, "Special Education School"=228, "County Community School"=133, "Juvenile Court School"=94, "Opportunity School"=47, "ROP"=6, "Youth Authority School"=6, "District Special Education Consortia School"=5, "Home and Hospital"=5, "State Special School"=3, nulls=5711
- EILCode: "ELEM"=7298, "HS"=3367, "UG"=2525, "INTMIDJR"=1845, "ELEMHIGH"=774, "A"=352, "PS"=156, nulls=1369
- EILName: "Elementary"=7298, "High School"=3367, "Ungraded"=2525, "Intermediate/Middle/Junior High"=1845, "Elementary-High Combination"=774, "Adult"=352, "Preschool"=156, nulls=1369
- GSoffered: 94 distinct, nulls=3882
- GSserved: 81 distinct, nulls=5743
- Virtual: "N"=9703, "P"=1046, "F"=69, nulls=6868
- Magnet: 0=10091, 1=519, nulls=7076
- Latitude: 11436 distinct, nulls=4823, num 32.5477..44.2193
  - stats: average=36.0077, median=35.678
- Longitude: 11278 distinct, nulls=4823, num -124.285..-83.7811
  - stats: average=-119.694, median=-119.313
- AdmFName1: 2327 distinct, nulls=5986
- AdmLName1: 6394 distinct, nulls=5986
- AdmEmail1: 10492 distinct, nulls=6012
- AdmFName2: 285 distinct, nulls=17255
- AdmLName2: 363 distinct, nulls=17255
- AdmEmail2: 382 distinct, nulls=17262
- AdmFName3: 40 distinct, nulls=17644
- AdmLName3: all distinct, nulls=17644
- AdmEmail3: all distinct, nulls=17644
- LastUpdate: 757 distinct
