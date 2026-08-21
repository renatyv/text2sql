---
generator: db-snooper
version: 0.0.33
generated_at_utc: 2026-08-21T12:30:53.928667Z
dialect: sqlite
database: /var/folders/9j/b9bx_drd53sc6zbpsqyrjy4h0000gn/T/dbsnoop-t1v95_vh/california_schools.sqlite
schema: main
---

## Relationships

- "schools"."CDSCode" ← "frpm"."CDSCode", "satscores"."cds"

# "frpm"  (rows=9986)

columns:
"CDSCode" text PK FK: digits, unique identifier
"Academic Year" text: "2014-2015"=9986
"County Code" text: digits, 58 distinct
"District Code" int: 1012 distinct, 10017..76901
"School Code" text: digits, 9942 distinct
"County Name" text: 58 distinct
"District Name" text: 1000 distinct
"School Name" text: 8652 distinct
"District Type" text: "Unified School District"=6744, "Elementary School District"=2356, "High School District"=529, "County Office of Education (COE)"=334, "State Board of Education"=10, "Statewide Benefit Charter"=6, "Non-School Locations"=4, "State Special Schools"=3
"School Type" text: "Elementary Schools (Public)"=5584, "High Schools (Public)"=1331, "Intermediate/Middle Schools (Public)"=1299, "Continuation High Schools"=459, "Alternative Schools of Choice"=259, "K-12 Schools (Public)"=240, "Elemen Schools In 1 School Dist. (Public)"=206, "District Community Day Schools"=203, "Special Education Schools (Public)"=132, "County Community"=75, "Juvenile Court Schools"=74, "Junior High Schools (Public)"=46, "Opportunity Schools"=23, "Youth Authority Facilities"=4, "State Special Schools"=3, "Preschool"=2, "High Schools In 1 School Dist. (Public)"=1, nulls=45
"Educational Option Type" text: "Traditional"=8696, "Continuation School"=459, "Alternative School of Choice"=259, "Community Day School"=203, "Special Education School"=128, "County Community School"=84, "Juvenile Court School"=74, "Opportunity School"=24, "District Special Education Consortia School"=4, "Youth Authority School"=4, "Home and Hospital"=3, "State Special School"=3, nulls=45
"NSLP Provision Status" text: "Provision 2"=1365, "Breakfast Provision 2"=285, "CEP"=172, "Multiple Provision Types"=11, "Provision 1"=7, "Lunch Provision 2"=5, "Provision 3"=2, nulls=8139
"Charter School (Y/N)" int: 0=8774, 1=1167, nulls=45
"Charter School Number" text: 1152 distinct, nulls=8819
"Charter Funding Type" text: "Directly funded"=838, "Locally funded"=328, "Not in CS funding model"=1, nulls=8819
"IRC" int: 0=9212, 1=729, nulls=45
"Low Grade" text: "K"=6057, "9"=1733, "6"=1024, "7"=651, "P"=181, "5"=99, "4"=68, "10"=44, "1"=42, "3"=38, "2"=19, "11"=14, "8"=10, "12"=3, "Adult"=3
"High Grade" text: "12"=2641, "5"=2534, "8"=2401, "6"=2091, "3"=68, "4"=65, "2"=40, "Adult"=35, "7"=30, "1"=22, "9"=19, "K"=18, "10"=13, "11"=5, "P"=2, "13"=1, "Post Secondary"=1
"Enrollment (K-12)" float: 1882 distinct, 1..5333, avg=620.826, median=528
"Free Meal Count (K-12)" float: 1216 distinct, nulls=56, 1..3927, avg=312.004, median=235
"Percent (%) Eligible Free (K-12)" float: 8658 distinct, nulls=56, 0.00176056..1, avg=0.529639, median=0.568935
"FRPM Count (K-12)" float: 1361 distinct, nulls=50, 1..4419, avg=365.48, median=285
"Percent (%) Eligible FRPM (K-12)" float: 8623 distinct, nulls=50, 0.00220507..1, avg=0.612085, median=0.682927
"Enrollment (Ages 5-17)" float: 1845 distinct, nulls=14, 1..5271, avg=605.325, median=517.5
"Free Meal Count (Ages 5-17)" float: 1205 distinct, nulls=78, 1..3864, avg=304.032, median=230
"Percent (%) Eligible Free (Ages 5-17)" float: 8552 distinct, nulls=78, 0.00179856..1, avg=0.531708, median=0.57199
"FRPM Count (Ages 5-17)" float: 1330 distinct, nulls=72, 1..4347, avg=356.514, median=279
"Percent (%) Eligible FRPM (Ages 5-17)" float: 8557 distinct, nulls=72, 0.00220507..1, avg=0.614618, median=0.687139
"2013-14 CALPADS Fall 1 Certification Status" int: 1=9986

indexes: none

samples:
| column | latest | sample | sample |
|---|---|---|---|
| CDSCode | 58727695838305 | 19649806061659 | 51713816053250 |
| Academic Year | 2014-2015 | 2014-2015 | 2014-2015 |
| County Code | 58 | 19 | 51 |
| District Code | 72769 | 64980 | 71381 |
| School Code | 5838305 | 6061659 | 6053250 |
| County Name | Yuba | Los Angeles | Sutter |
| District Name | Wheatland Union High | Santa Monica-Malibu Unified | Franklin Elementary |
| School Name | Wheatland Union High | Lincoln Middle | Franklin Elementary |
| District Type | High School District | Unified School District | Elementary School District |
| School Type | High Schools (Public) | Intermediate/Middle Schools (Public) | Elemen Schools In 1 School Dist. (Public) |
| Educational Option Type | Traditional | Traditional | Traditional |
| NSLP Provision Status | null | null | null |
| Charter School (Y/N) | 0 | 0 | 0 |
| Charter School Number | null | null | null |
| Charter Funding Type | null | null | null |
| IRC | 0 | 0 | 0 |
| Low Grade | 9 | 6 | K |
| High Grade | 12 | 8 | 8 |
| Enrollment (K-12) | 732 | 1027 | 477 |
| Free Meal Count (K-12) | 164 | 151 | 101 |
| Percent (%) Eligible Free (K-12) | 0.224044 | 0.14703 | 0.21174 |
| FRPM Count (K-12) | 227 | 188 | 142 |
| Percent (%) Eligible FRPM (K-12) | 0.310109 | 0.183057 | 0.297694 |
| Enrollment (Ages 5-17) | 711 | 1027 | 474 |
| Free Meal Count (Ages 5-17) | 158 | 151 | 100 |
| Percent (%) Eligible Free (Ages 5-17) | 0.222222 | 0.14703 | 0.21097 |
| FRPM Count (Ages 5-17) | 220 | 188 | 141 |
| Percent (%) Eligible FRPM (Ages 5-17) | 0.309423 | 0.183057 | 0.297468 |
| 2013-14 CALPADS Fall 1 Certification Status | 1 | 1 | 1 |

# "satscores"  (rows=2269)

columns:
"cds" text PK FK: digits, unique identifier
"rtype" text NOTNULL: "S"=1749, "D"=520
"sname" text: 1665 distinct, nulls=520
"dname" text: 520 distinct
"cname" text: 57 distinct
"enroll12" int NOTNULL: 835 distinct, 0..43324, avg=419.519, median=220
"NumTstTakr" int NOTNULL: 547 distinct, 0..24305, avg=185.098, median=83
"AvgScrRead" int: 269 distinct, nulls=596, 308..653, avg=479.699, median=481
"AvgScrMath" int: 295 distinct, nulls=596, 289..699, avg=484.461, median=483
"AvgScrWrite" int: 267 distinct, nulls=596, 312..671, avg=472.529, median=471
"NumGE1500" int: 368 distinct, nulls=596, 0..5837, avg=111.079, median=44

indexes: none

samples:
| column | latest | sample | sample |
|---|---|---|---|
| cds | 58727695838305 | 38684783830288 | 48705734830089 |
| rtype | S | S | S |
| sname | Wheatland Union High | Balboa High | Will C. Wood High |
| dname | Wheatland Union High | San Francisco Unified | Vacaville Unified |
| cname | Yuba | San Francisco | Solano |
| enroll12 | 160 | 297 | 335 |
| NumTstTakr | 54 | 184 | 137 |
| AvgScrRead | 480 | 467 | 487 |
| AvgScrMath | 475 | 504 | 523 |
| AvgScrWrite | 463 | 467 | 475 |
| NumGE1500 | 21 | 79 | 59 |

# "schools"  (rows=17686)

columns:
"CDSCode" text PK: digits, unique identifier
"NCESDist" text: digits, 1193 distinct, nulls=1030
"NCESSchool" text: digits, 12321 distinct, nulls=5040
"StatusType" text NOTNULL: "Active"=11708, "Closed"=4518, "Merged"=1448, "Pending"=12
"County" text NOTNULL: 58 distinct
"District" text NOTNULL: 1411 distinct
"School" text: 13875 distinct, nulls=1369
"Street" text: 13593 distinct, nulls=294
"StreetAbr" text: 13633 distinct, nulls=294
"City" text: 1165 distinct, nulls=293
"Zip" text: 11184 distinct, nulls=293
"State" text: "CA"=17393, nulls=293
"MailStreet" text: 12395 distinct, nulls=292
"MailStrAbr" text: 12429 distinct, nulls=292
"MailCity" text: 1132 distinct, nulls=292
"MailZip" text: 10298 distinct, nulls=292
"MailState" text: "CA"=17394, nulls=292
"Phone" text: 10632 distinct, nulls=5969
"Ext" text: digits, 379 distinct, nulls=17146
"Website" text: 4082 distinct, nulls=10722
"OpenDate" date: 1406 distinct, nulls=1369
"ClosedDate" date: 899 distinct, nulls=11992
"Charter" int: 0=14588, 1=1729, nulls=1369
"CharterNum" text: 1763 distinct, nulls=15885
"FundingType" text: "Directly funded"=1176, "Locally funded"=460, "Not in CS funding model"=6, nulls=16044
"DOC" text NOTNULL: "54"=10190, "52"=4378, "00"=1703, "56"=1079, "98"=156, "02"=69, "34"=49, "58"=33, "03"=11, "99"=10, "31"=6, "42"=2
"DOCType" text NOTNULL: "Unified School District"=10190, "Elementary School District"=4378, "County Office of Education (COE)"=1703, "High School District"=1079, "Regional Occupation Center/Program (ROC/P)"=156, "State Board of Education"=69, "Non-School Locations"=49, "Community College District"=33, "Statewide Benefit Charter"=11, "Administration Only"=10, "State Special Schools"=6, "Joint Powers Authority (JPA)"=2
"SOC" text: digits, 20 distinct, nulls=1369
"SOCType" text: 20 distinct, nulls=1369
"EdOpsCode" text: "TRAD"=10103, "CON"=539, "COMMDAY"=486, "ALTSOC"=320, "SPEC"=228, "COMM"=133, "JUV"=94, "OPP"=47, "ROP"=6, "YTH"=6, "HOMHOS"=5, "SPECON"=5, "SSS"=3, nulls=5711
"EdOpsName" text: "Traditional"=10103, "Continuation School"=539, "Community Day School"=486, "Alternative School of Choice"=320, "Special Education School"=228, "County Community School"=133, "Juvenile Court School"=94, "Opportunity School"=47, "ROP"=6, "Youth Authority School"=6, "District Special Education Consortia School"=5, "Home and Hospital"=5, "State Special School"=3, nulls=5711
"EILCode" text: "ELEM"=7298, "HS"=3367, "UG"=2525, "INTMIDJR"=1845, "ELEMHIGH"=774, "A"=352, "PS"=156, nulls=1369
"EILName" text: "Elementary"=7298, "High School"=3367, "Ungraded"=2525, "Intermediate/Middle/Junior High"=1845, "Elementary-High Combination"=774, "Adult"=352, "Preschool"=156, nulls=1369
"GSoffered" text: 94 distinct, nulls=3882
"GSserved" text: 81 distinct, nulls=5743
"Virtual" text: "N"=9703, "P"=1046, "F"=69, nulls=6868
"Magnet" int: 0=10091, 1=519, nulls=7076
"Latitude" float: 11436 distinct, nulls=4823, 32.5477..44.2193, avg=36.0077, median=35.678
"Longitude" float: 11278 distinct, nulls=4823, -124.285..-83.7811, avg=-119.694, median=-119.313
"AdmFName1" text: 2327 distinct, nulls=5986
"AdmLName1" text: 6394 distinct, nulls=5986
"AdmEmail1" text: 10492 distinct, nulls=6012
"AdmFName2" text: 285 distinct, nulls=17255
"AdmLName2" text: 363 distinct, nulls=17255
"AdmEmail2" text: 382 distinct, nulls=17262
"AdmFName3" text: 40 distinct, nulls=17644
"AdmLName3" text: all distinct, nulls=17644
"AdmEmail3" text: all distinct, nulls=17644
"LastUpdate" date NOTNULL: 757 distinct

indexes: none

samples:
| column | latest | sample | sample |
|---|---|---|---|
| CDSCode | 58727695838305 | 19647330106856 | 37680230101592 |
| NCESDist | 0642350 | 0622710 | 0608610 |
| NCESSchool | 06930 | 10850 | 11227 |
| StatusType | Active | Closed | Active |
| County | Yuba | Los Angeles | San Diego |
| District | Wheatland Union High | Los Angeles Unified | Chula Vista Elementary |
| School | Wheatland Union High | Southern California School of Arts and Sciences | Hedenkamp (Anne and William) Elementary |
| Street | 1010 Wheatland Road | 10513 Vermont Ave | 930 East Palomar |
| StreetAbr | 1010 Wheatland Rd. | 10513 Vermont Ave | 930 East Palomar |
| City | Wheatland | Los Angeles | Chula Vista |
| Zip | 95692-9798 | 90044 | 91913-2895 |
| State | CA | CA | CA |
| MailStreet | 1010 Wheatland Road | 2110 Artesia Boulevard, Suite B224 | 930 East Palomar |
| MailStrAbr | 1010 Wheatland Rd. | 2110 Artesia Blvd., Ste. B224 | 930 East Palomar |
| MailCity | Wheatland | Redondo Beach | Chula Vista |
| MailZip | 95692-9798 | 90278 | 91913-2895 |
| MailState | CA | CA | CA |
| Phone | (530) 633-3100 | null | (619) 397-5828 |
| Ext | null | null | null |
| Website | www.wheatlandhigh.org | null | http://schools.cvesd.org/schools/hedenkamp/ |
| OpenDate | 1980-07-01 | 2004-09-01 | 2003-09-02 |
| ClosedDate | null | 2006-05-12 | null |
| Charter | 0 | 1 | 0 |
| CharterNum | null | 0644 | null |
| FundingType | null | Directly funded | null |
| DOC | 56 | 54 | 52 |
| DOCType | High School District | Unified School District | Elementary School District |
| SOC | 66 | 66 | 60 |
| SOCType | High Schools (Public) | High Schools (Public) | Elementary Schools (Public) |
| EdOpsCode | TRAD | TRAD | TRAD |
| EdOpsName | Traditional | Traditional | Traditional |
| EILCode | HS | ELEMHIGH | ELEM |
| EILName | High School | Elementary-High Combination | Elementary |
| GSoffered | 9-12 | 6-12 | K-6 |
| GSserved | 9-12 | 6-11 | K-6 |
| Virtual | N | null | N |
| Magnet | 0 | null | 0 |
| Latitude | 38.999 | null | 32.6167 |
| Longitude | -121.455 | null | -117.015 |
| AdmFName1 | Vic | null | Ray |
| AdmLName1 | Ramos | null | DeVore |
| AdmEmail1 | vramos@wheatlandhigh.org | null | ray.devore@cvesd.org |
| AdmFName2 | null | null | Gina |
| AdmLName2 | null | null | Mazeau |
| AdmEmail2 | null | null | gina.mazeau@cvesd.org |
| AdmFName3 | null | null | null |
| AdmLName3 | null | null | null |
| AdmEmail3 | null | null | null |
| LastUpdate | 2015-06-18 | 2009-10-02 | 2016-01-21 |
