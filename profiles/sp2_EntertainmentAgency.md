---
generator: db-snooper
version: 0.0.31
generated_at_utc: 2026-08-20T17:28:08.576804Z
dialect: sqlite
database: /var/folders/9j/b9bx_drd53sc6zbpsqyrjy4h0000gn/T/dbsnoop-kyy_t57r/EntertainmentAgency.sqlite
schema: main
---

## Relationships

- "Agents"."AgentID" ← "Engagements"."AgentID"
- "Customers"."CustomerID" ← "Engagements"."CustomerID", "Musical_Preferences"."CustomerID"
- "Entertainers"."EntertainerID" ← "Engagements"."EntertainerID", "Entertainer_Members"."EntertainerID", "Entertainer_Styles"."EntertainerID"
- "Members"."MemberID" ← "Entertainer_Members"."MemberID"
- "Musical_Styles"."StyleID" ← "Entertainer_Styles"."StyleID", "Musical_Preferences"."StyleID"

# "Agents"  (rows=9)

columns:
"AgentID" int PK: unique identifier, 1..9, avg=5, median=5
"AgtFirstName" text: "Caleb"=1, "Carol"=1, "Daffy"=1, "John"=1, "Karen"=1, "Maria"=1, "Marianne"=1, "Scott"=1, "William"=1
"AgtLastName" text: "Viescas"=2, "Bishop"=1, "Dumbwit"=1, "Kennedy"=1, "Patterson"=1, "Smith"=1, "Thompson"=1, "Wier"=1
"AgtStreetAddress" text: "122 Spring River Drive"=1, "1234 Main Street"=1, "16679 NE 41st Court"=1, "30301 - 166th Ave. N.E."=1, "3445 Cheyenne Road"=1, "4501 Wetland Road"=1, "66 Spring Valley Drive"=1, "667 Red River Road"=1, "908 W. Capital Way"=1
"AgtCity" text: "Seattle"=3, "Bellevue"=2, "Redmond"=2, "Kirkland"=1, "Tacoma"=1
"AgtState" text: "WA"=9
"AgtZipCode" text: "98125"=3, "98006"=2, "98033"=1, "98052"=1, "98053"=1, "98413"=1
"AgtPhoneNumber" text: "555-0037"=1, "555-1234"=1, "555-2291"=1, "555-2551"=1, "555-2571"=1, "555-2606"=1, "555-2621"=1, "555-2666"=1, "555-2681"=1
"DateHired" date: "1997-05-15"=2, "1997-09-03"=1, "1997-11-19"=1, "1998-02-02"=1, "1998-02-05"=1, "1998-02-16"=1, "1998-03-05"=1, "2000-02-05"=1
"Salary" numeric: 30000=2, 50=1, 22000=1, 22100=1, 24500=1, 27000=1, 33000=1, 35000=1, 50..35000
"CommissionRate" float: 0.04=3, 0.01=1, 0.035=1, 0.045=1, 0.05=1, 0.055=1, 0.06=1, 0.01..0.06

indexes: "AgtZipCode"
fk: none

all rows:
| column | row 1 | row 2 | row 3 | row 4 | row 5 | row 6 | row 7 | row 8 | row 9 |
|---|---|---|---|---|---|---|---|---|---|
| AgentID | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9 |
| AgtFirstName | William | Scott | Carol | Karen | Marianne | John | Caleb | Maria | Daffy |
| AgtLastName | Thompson | Bishop | Viescas | Smith | Wier | Kennedy | Viescas | Patterson | Dumbwit |
| AgtStreetAddress | 122 Spring River Drive | 66 Spring Valley Drive | 667 Red River Road | 30301 - 166th Ave. N.E. | 908 W. Capital Way | 16679 NE 41st Court | 4501 Wetland Road | 3445 Cheyenne Road | 1234 Main Street |
| AgtCity | Redmond | Seattle | Bellevue | Seattle | Tacoma | Seattle | Redmond | Bellevue | Kirkland |
| AgtState | WA | WA | WA | WA | WA | WA | WA | WA | WA |
| AgtZipCode | 98053 | 98125 | 98006 | 98125 | 98413 | 98125 | 98052 | 98006 | 98033 |
| AgtPhoneNumber | 555-2681 | 555-2666 | 555-2571 | 555-2551 | 555-2606 | 555-2621 | 555-0037 | 555-2291 | 555-1234 |
| DateHired | 1997-05-15 | 1998-02-05 | 1997-11-19 | 1998-03-05 | 1998-02-02 | 1997-05-15 | 1998-02-16 | 1997-09-03 | 2000-02-05 |
| Salary | 35000 | 27000 | 30000 | 22000 | 24500 | 33000 | 22100 | 30000 | 50 |
| CommissionRate | 0.04 | 0.04 | 0.05 | 0.055 | 0.045 | 0.06 | 0.035 | 0.04 | 0.01 |

# "Customers"  (rows=15)

columns:
"CustomerID" int PK: unique identifier, 10001..10015, avg=10008, median=10008
"CustFirstName" text: "Carol"=1, "Darren"=1, "Dean"=1, "Deb"=1, "Doris"=1, "Elizabeth"=1, "Estella"=1, "Joyce"=1, "Kerry"=1, "Liz"=1, "Mark"=1, "Matt"=1, "Peter"=1, "Sarah"=1, "Zachary"=1
"CustLastName" text: "Berg"=1, "Bonnicksen"=1, "Brehm"=1, "Ehrlich"=1, "Gehring"=1, "Hallmark"=1, "Hartwig"=1, "Keyser"=1, "McCrae"=1, "Patterson"=1, "Pundt"=1, "Rosales"=1, "Thompson"=1, "Viescas"=1, "Waldal"=1
"CustStreetAddress" text: "908 W. Capital Way"=2, "12330 Kingman Drive"=1, "13920 S.E. 40th Street"=1, "2222 Springer Road"=1, "2424 Thames Drive"=1, "2500 Rosales Lane"=1, "2601 Seaview Lane"=1, "323 Advocate Lane"=1, "4110 Old Redmond Rd."=1, "4726 - 11th Ave. N.E."=1, "722 Moss Bay Blvd."=1, "754 Fourth Ave"=1, "777 Fenexet Blvd"=1, "Route 2, Box 203B"=1
"CustCity" text: "Bellevue"=5, "Kirkland"=3, "Redmond"=2, "Seattle"=2, "Tacoma"=2, "Auburn"=1
"CustState" text: "WA"=15
"CustZipCode" text: "98006"=5, "98033"=3, "98052"=2, "98413"=2, "98002"=1, "98105"=1, "98115"=1
"CustPhoneNumber" text: "555-0399"=1, "555-2286"=1, "555-2296"=1, "555-2496"=1, "555-2501"=1, "555-2506"=1, "555-2521"=1, "555-2556"=1, "555-2581"=1, "555-2616"=1, "555-2626"=1, "555-2671"=1, "555-2721"=1, "555-2726"=1, "555-9938"=1

indexes: "CustZipCode"
fk: none

samples:
| column | latest | sample | sample |
|---|---|---|---|
| CustomerID | 10015 | 10012 | 10007 |
| CustFirstName | Carol | Kerry | Liz |
| CustLastName | Viescas | Patterson | Keyser |
| CustStreetAddress | 754 Fourth Ave | 777 Fenexet Blvd | 13920 S.E. 40th Street |
| CustCity | Seattle | Redmond | Bellevue |
| CustState | WA | WA | WA |
| CustZipCode | 98115 | 98052 | 98006 |
| CustPhoneNumber | 555-2296 | 555-0399 | 555-2556 |

# "Engagements"  (rows=111)

columns:
"EngagementNumber" int PK: unique identifier, 2..131, avg=67.2793, median=70
"StartDate" date: 64 distinct
"EndDate" date: 77 distinct
"StartTime" time: "20:00:00"=17, "17:00:00"=16, "14:00:00"=15, "12:00:00"=13, "13:00:00"=13, "16:00:00"=12, "15:00:00"=10, "18:00:00"=9, "19:00:00"=6
"StopTime" time: "19:00:00"=15, "22:00:00"=13, "17:00:00"=12, "20:00:00"=11, "15:00:00"=9, "18:00:00"=9, "21:00:00"=9, "01:00:00"=7, "16:00:00"=7, "23:00:00"=7, "00:00:00"=6, "02:00:00"=4, "14:00:00"=2
"ContractPrice" numeric: 48 distinct, 110..14105, avg=1266.22, median=950
"CustomerID" int FK: 10010=13, 10004=11, 10002=10, 10014=10, 10006=9, 10001=8, 10005=8, 10009=8, 10003=7, 10007=7, 10012=7, 10015=7, 10013=6, 10001..10015
"AgentID" int FK: 3=19, 5=18, 4=17, 1=16, 8=15, 6=12, 7=8, 2=6, 1..8
"EntertainerID" int FK: 1008=15, 1001=11, 1013=11, 1003=10, 1006=10, 1004=9, 1010=9, 1007=8, 1011=8, 1002=7, 1005=7, 1012=6, 1001..1013

indexes: "AgentID", "CustomerID", "AgentID", "EntertainerID"
fk: "EntertainerID"→"Entertainers"."EntertainerID", "CustomerID"→"Customers"."CustomerID", "AgentID"→"Agents"."AgentID"

samples:
| column | latest | sample | sample |
|---|---|---|---|
| EngagementNumber | 131 | 11 | 13 |
| StartDate | 2018-03-04 | 2017-09-16 | 2017-09-18 |
| EndDate | 2018-03-13 | 2017-09-17 | 2017-09-21 |
| StartTime | 15:00:00 | 18:00:00 | 20:00:00 |
| StopTime | 17:00:00 | 00:00:00 | 23:00:00 |
| ContractPrice | 1850 | 950 | 770 |
| CustomerID | 10014 | 10005 | 10003 |
| AgentID | 1 | 4 | 1 |
| EntertainerID | 1003 | 1008 | 1006 |

# "Entertainer_Members"  (rows=40)

columns:
"EntertainerID" int PK FK: 1003=6, 1007=5, 1008=5, 1006=4, 1010=4, 1013=4, 1001=3, 1005=3, 1002=2, 1004=1, 1009=1, 1011=1, 1012=1, 1001..1013
"MemberID" int PK FK: 25 distinct, 101..125, avg=113.4, median=114, 120=3, 121=3, 102=2, 103=2, 104=2, 105=2, 107=2, 112=2, 114=2, 117=2
"Status" smallint: 1=27, 2=13

indexes: "EntertainerID", "MemberID"
fk: "EntertainerID"→"Entertainers"."EntertainerID", "MemberID"→"Members"."MemberID"

samples:
| column | latest | sample | sample |
|---|---|---|---|
| EntertainerID | 1013 | 1001 | 1011 |
| MemberID | 124 | 107 | 122 |
| Status | 2 | 1 | 2 |

# "Entertainer_Styles"  (rows=32)

columns:
"EntertainerID" int PK FK: 1001=3, 1002=3, 1005=3, 1006=3, 1009=3, 1010=3, 1011=3, 1003=2, 1007=2, 1008=2, 1012=2, 1013=2, 1004=1, 1001..1013
"StyleID" smallint PK FK: 7=3, 21=3, 3=2, 6=2, 10=2, 13=2, 14=2, 15=2, 19=2, 20=2, 22=2, 23=2, 24=2, 4=1, 8=1, 11=1, 17=1, 3..24
"StyleStrength" smallint NOTNULL: 1=13, 2=12, 3=7, 1..3

indexes: "EntertainerID", "StyleID"
fk: "EntertainerID"→"Entertainers"."EntertainerID", "StyleID"→"Musical_Styles"."StyleID"

samples:
| column | latest | sample | sample |
|---|---|---|---|
| EntertainerID | 1013 | 1002 | 1005 |
| StyleID | 15 | 23 | 15 |
| StyleStrength | 1 | 3 | 3 |

# "Entertainers"  (rows=13)

columns:
"EntertainerID" int PK: unique identifier, 1001..1013, avg=1007, median=1007
"EntStageName" text: "Carol Peacock Trio"=1, "Caroline Coie Cuartet"=1, "Coldwater Cattle Company"=1, "Country Feeling"=1, "JV & the Deep Six"=1, "Jazz Persuasion"=1, "Jim Glynn"=1, "Julia Schnebly"=1, "Katherine Ehrlich"=1, "Modern Dance"=1, "Saturday Revue"=1, "Susan McLain"=1, "Topazz"=1
"EntSSN" text: "888-18-1013"=1, "888-26-1025"=1, "888-30-1031"=1, "888-38-1043"=1, "888-50-1061"=1, "888-61-1103"=1, "888-64-1109"=1, "888-65-1111"=1, "888-66-1085"=1, "888-70-1121"=1, "888-71-1123"=1, "888-90-1121"=1, "888-98-1133"=1
"EntStreetAddress" text: "13920 S.E. 40th Street"=1, "15127 NE 24th, #383"=1, "16 Maple Lane"=1, "233 West Valley Hwy"=1, "2343 Harmony Lane"=1, "298 Forest Lane"=1, "3887 Easy Street"=1, "4110 Old Redmond Rd."=1, "4726 - 11th Ave. N.E."=1, "511 Lenora Ave"=1, "777 Fenexet Blvd"=1, "PO Box 223311"=1, "Route 2, Box 203B"=1
"EntCity" text: "Seattle"=4, "Bellevue"=3, "Auburn"=2, "Redmond"=2, "Woodinville"=2
"EntState" text: "WA"=13
"EntZipCode" text: "98002"=2, "98052"=2, "98072"=2, "98125"=2, "98005"=1, "98006"=1, "98009"=1, "98105"=1, "99837"=1
"EntPhoneNumber" text: "555-0039"=1, "555-0399"=1, "555-2301"=1, "555-2306"=1, "555-2511"=1, "555-2531"=1, "555-2541"=1, "555-2561"=1, "555-2591"=1, "555-2631"=1, "555-2691"=1, "555-2711"=1, "555-9936"=1
"EntWebPage" text: "www.coldwatercows.com"=1, "www.cptrio.com"=1, "www.greensleeves.com"=1, "www.jazzper.com"=1, "www.jvd6.com"=1, "www.moderndance.com"=1, "www.satrevue.com"=1, "www.topazz.com"=1, nulls=5
"EntEMailAddress" text: "carolinec@willow.com"=1, "carolp@cptrio.com"=1, "edz@coolness.com"=1, "jv@myspring.com"=1, "ke@mzo.com"=1, "mikeh@moderndance.com"=1, "susan@gs.com"=1, nulls=6
"DateEntered" date: "1995-01-20"=1, "1995-05-16"=1, "1995-11-30"=1, "1996-02-14"=1, "1996-02-28"=1, "1996-04-01"=1, "1996-04-12"=1, "1997-05-12"=1, "1997-05-24"=1, "1997-07-11"=1, "1998-03-18"=1, "1998-09-13"=1, "1998-10-12"=1

indexes: "EntZipCode"
fk: none

samples:
| column | latest | sample | sample |
|---|---|---|---|
| EntertainerID | 1013 | 1010 | 1009 |
| EntStageName | Caroline Coie Cuartet | Saturday Revue | Katherine Ehrlich |
| EntSSN | 888-71-1123 | 888-64-1109 | 888-61-1103 |
| EntStreetAddress | 298 Forest Lane | 3887 Easy Street | 777 Fenexet Blvd |
| EntCity | Auburn | Seattle | Woodinville |
| EntState | WA | WA | WA |
| EntZipCode | 98002 | 98125 | 98072 |
| EntPhoneNumber | 555-2306 | 555-0039 | 555-0399 |
| EntWebPage | null | www.satrevue.com | null |
| EntEMailAddress | carolinec@willow.com | edz@coolness.com | ke@mzo.com |
| DateEntered | 1997-07-11 | 1995-01-20 | 1998-09-13 |

# "Members"  (rows=25)

columns:
"MemberID" int PK: unique identifier, 101..125, avg=113, median=113
"MbrFirstName" text: 24 distinct
"MbrLastName" text: 21 distinct
"MbrPhoneNumber" text: all distinct
"Gender" text: "F"=12, "M"=12, nulls=1

indexes: none
fk: none

samples:
| column | latest | sample | sample |
|---|---|---|---|
| MemberID | 125 | 115 | 101 |
| MbrFirstName | Jim | Joe | David |
| MbrLastName | Glynn | Rosales III | Hamilton |
| MbrPhoneNumber | 555-2531 | 555-2281 | 555-2701 |
| Gender | null | M | M |

# "Musical_Preferences"  (rows=36)

columns:
"CustomerID" int PK FK: 10007=3, 10009=3, 10010=3, 10011=3, 10014=3, 10015=3, 10001=2, 10002=2, 10003=2, 10004=2, 10005=2, 10006=2, 10008=2, 10012=2, 10013=2, 10001..10015
"StyleID" smallint PK FK: 20 distinct, 1..24, avg=14.2222, median=15, 21=4, 10=3, 15=3, 19=3, 1=2, 7=2, 8=2, 18=2, 20=2, 22=2
"PreferenceSeq" smallint NOTNULL: 1=15, 2=15, 3=6, 1..3

indexes: "CustomerID", "StyleID"
fk: "CustomerID"→"Customers"."CustomerID", "StyleID"→"Musical_Styles"."StyleID"

samples:
| column | latest | sample | sample |
|---|---|---|---|
| CustomerID | 10015 | 10002 | 10003 |
| StyleID | 21 | 8 | 19 |
| PreferenceSeq | 1 | 2 | 1 |

# "Musical_Styles"  (rows=25)

columns:
"StyleID" smallint PK: unique identifier, 1..25, avg=13, median=13
"StyleName" text: all distinct

indexes: none
fk: none

samples:
| column | latest | sample | sample |
|---|---|---|---|
| StyleID | 25 | 2 | 23 |
| StyleName | 90's Music | 50's Music | Variety |

# "ztblDays"  (rows=1096)

columns:
"DateField" date PK: unique identifier

indexes: none
fk: none

samples:
| column | latest | sample | sample |
|---|---|---|---|
| DateField | 2020-01-01 | 2017-04-24 | 2018-06-07 |

# "ztblMonths"  (rows=36)

columns:
"MonthYear" text UNIQ: unique identifier
"YearNumber" smallint PK: 2017=12, 2018=12, 2019=12, 2017..2019
"MonthNumber" smallint PK: 1=3, 2=3, 3=3, 4=3, 5=3, 6=3, 7=3, 8=3, 9=3, 10=3, 11=3, 12=3, 1..12
"MonthStart" date UNIQ: unique identifier
"MonthEnd" date UNIQ: unique identifier
"January" smallint: 0=33, 1=3
"February" smallint: 0=33, 1=3
"March" smallint: 0=33, 1=3
"April" smallint: 0=33, 1=3
"May" smallint: 0=33, 1=3
"June" smallint: 0=33, 1=3
"July" smallint: 0=33, 1=3
"August" smallint: 0=33, 1=3
"September" smallint: 0=33, 1=3
"October" smallint: 0=33, 1=3
"November" smallint: 0=33, 1=3
"December" smallint: 0=33, 1=3

indexes: UNIQUE "MonthStart", UNIQUE "MonthYear", UNIQUE "MonthEnd"
fk: none

samples:
| column | latest | sample | sample |
|---|---|---|---|
| MonthYear | December 2019 | December 2019 | November 2018 |
| YearNumber | 2019 | 2019 | 2018 |
| MonthNumber | 12 | 12 | 11 |
| MonthStart | 2019-12-01 | 2019-12-01 | 2018-11-01 |
| MonthEnd | 2019-12-31 | 2019-12-31 | 2018-11-30 |
| January | 0 | 0 | 0 |
| February | 0 | 0 | 0 |
| March | 0 | 0 | 0 |
| April | 0 | 0 | 0 |
| May | 0 | 0 | 0 |
| June | 0 | 0 | 0 |
| July | 0 | 0 | 0 |
| August | 0 | 0 | 0 |
| September | 0 | 0 | 0 |
| October | 0 | 0 | 0 |
| November | 0 | 0 | 1 |
| December | 1 | 1 | 0 |

# "ztblSkipLabels"  (rows=60)

columns:
"LabelCount" int PK: unique identifier, 1..60, avg=30.5, median=30.5

indexes: none
fk: none

samples:
| column | latest | sample | sample |
|---|---|---|---|
| LabelCount | 60 | 44 | 37 |

# "ztblWeeks"  (rows=156)

columns:
"WeekStart" date PK: unique identifier
"WeekEnd" date: all distinct

indexes: none
fk: none

samples:
| column | latest | sample | sample |
|---|---|---|---|
| WeekStart | 2019-12-22 | 2017-05-28 | 2017-09-17 |
| WeekEnd | 2019-12-28 | 2017-06-03 | 2017-09-23 |
