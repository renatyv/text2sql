---
generator: db-snooper
version: 0.0.26
generated_at_utc: 2026-08-16T08:08:41.100723Z
dialect: sqlite
database: /var/folders/9j/b9bx_drd53sc6zbpsqyrjy4h0000gn/T/dbsnoop-j2317hdd/EntertainmentAgency.sqlite
schema: main
---

## Relationships

- Agents.AgentID ← Engagements.AgentID
- Customers.CustomerID ← Engagements.CustomerID, Musical_Preferences.CustomerID
- Entertainers.EntertainerID ← Engagements.EntertainerID, Entertainer_Members.EntertainerID, Entertainer_Styles.EntertainerID
- Members.MemberID ← Entertainer_Members.MemberID
- Musical_Styles.StyleID ← Entertainer_Styles.StyleID, Musical_Preferences.StyleID

# Agents

## All rows

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
| Salary | 35000.00 | 27000.00 | 30000.00 | 22000.00 | 24500.00 | 33000.00 | 22100.00 | 30000.00 | 50.00 |
| CommissionRate | 0.04 | 0.04 | 0.05 | 0.055 | 0.045 | 0.06 | 0.035 | 0.04 | 0.01 |


# Customers

```sql
CREATE TABLE Customers (
    CustomerID int NOT NULL PRIMARY KEY,
    CustFirstName nvarchar (25) NULL,
    CustLastName nvarchar (25) NULL,
    CustStreetAddress nvarchar (50) NULL,
    CustCity nvarchar (30) NULL,
    CustState nvarchar (2) NULL,
    CustZipCode nvarchar (10) NULL,
    CustPhoneNumber nvarchar (15) NULL
);
```

## Indexes

- (CustZipCode)

## Rows

- total=15

| column | latest | sample | sample |
|---|---|---|---|
| CustomerID | 10015 | 10014 | 10008 |
| CustFirstName | Carol | Mark | Darren |
| CustLastName | Viescas | Rosales | Gehring |
| CustStreetAddress | 754 Fourth Ave | 323 Advocate Lane | 2601 Seaview Lane |
| CustCity | Seattle | Bellevue | Kirkland |
| CustState | WA | WA | WA |
| CustZipCode | 98115 | 98006 | 98033 |
| CustPhoneNumber | 555-2296 | 555-2286 | 555-2616 |

## Columns

- CustomerID: unique identifier, int 10001..10015
  - stats: average=10008, median=10008
- CustFirstName: "Carol"=1, "Darren"=1, "Dean"=1, "Deb"=1, "Doris"=1, "Elizabeth"=1, "Estella"=1, "Joyce"=1, "Kerry"=1, "Liz"=1, "Mark"=1, "Matt"=1, "Peter"=1, "Sarah"=1, "Zachary"=1
- CustLastName: "Berg"=1, "Bonnicksen"=1, "Brehm"=1, "Ehrlich"=1, "Gehring"=1, "Hallmark"=1, "Hartwig"=1, "Keyser"=1, "McCrae"=1, "Patterson"=1, "Pundt"=1, "Rosales"=1, "Thompson"=1, "Viescas"=1, "Waldal"=1
- CustStreetAddress: "908 W. Capital Way"=2, "12330 Kingman Drive"=1, "13920 S.E. 40th Street"=1, "2222 Springer Road"=1, "2424 Thames Drive"=1, "2500 Rosales Lane"=1, "2601 Seaview Lane"=1, "323 Advocate Lane"=1, "4110 Old Redmond Rd."=1, "4726 - 11th Ave. N.E."=1, "722 Moss Bay Blvd."=1, "754 Fourth Ave"=1, "777 Fenexet Blvd"=1, "Route 2, Box 203B"=1
- CustCity: "Bellevue"=5, "Kirkland"=3, "Redmond"=2, "Seattle"=2, "Tacoma"=2, "Auburn"=1
- CustState: "WA"=15
- CustZipCode: "98006"=5, "98033"=3, "98052"=2, "98413"=2, "98002"=1, "98105"=1, "98115"=1
- CustPhoneNumber: "555-0399"=1, "555-2286"=1, "555-2296"=1, "555-2496"=1, "555-2501"=1, "555-2506"=1, "555-2521"=1, "555-2556"=1, "555-2581"=1, "555-2616"=1, "555-2626"=1, "555-2671"=1, "555-2721"=1, "555-2726"=1, "555-9938"=1


# Engagements

```sql
CREATE TABLE Engagements (
    EngagementNumber int NOT NULL PRIMARY KEY DEFAULT 0,
    StartDate date NULL,
    EndDate date NULL,
    StartTime time NULL,
    StopTime time NULL,
    ContractPrice decimal(15, 2) NULL DEFAULT 0,
    CustomerID int NULL DEFAULT 0,
    AgentID int NULL DEFAULT 0,
    EntertainerID int NULL DEFAULT 0,
    FOREIGN KEY (AgentID) REFERENCES Agents(AgentID),
    FOREIGN KEY (CustomerID) REFERENCES Customers(CustomerID),
    FOREIGN KEY (EntertainerID) REFERENCES Entertainers(EntertainerID)
);
```

## Indexes

- (AgentID)
- (CustomerID)
- (AgentID)
- (EntertainerID)

## Rows

- total=111

| column | latest | sample | sample |
|---|---|---|---|
| EngagementNumber | 131 | 76 | 17 |
| StartDate | 2018-03-04 | 2017-12-31 | 2017-09-30 |
| EndDate | 2018-03-13 | 2018-01-04 | 2017-10-03 |
| StartTime | 15:00:00 | 16:00:00 | 18:00:00 |
| StopTime | 17:00:00 | 22:00:00 | 20:00:00 |
| ContractPrice | 1850.00 | 500.00 | 530.00 |
| CustomerID | 10014 | 10005 | 10002 |
| AgentID | 1 | 7 | 8 |
| EntertainerID | 1003 | 1012 | 1010 |

## Columns

- EngagementNumber: unique identifier, int 2..131
  - stats: average=67.2793, median=70
- StartDate: 64 distinct
- EndDate: 77 distinct
- StartTime: 20:00:00=17, 17:00:00=16, 14:00:00=15, 12:00:00=13, 13:00:00=13, 16:00:00=12, 15:00:00=10, 18:00:00=9, 19:00:00=6
- StopTime: 19:00:00=15, 22:00:00=13, 17:00:00=12, 20:00:00=11, 15:00:00=9, 18:00:00=9, 21:00:00=9, 01:00:00=7, 16:00:00=7, 23:00:00=7, 00:00:00=6, 02:00:00=4, 14:00:00=2
- ContractPrice: 48 distinct, num 110.00..14105.00
  - stats: average=1266.22, median=950
- CustomerID: 10010=13, 10004=11, 10002=10, 10014=10, 10006=9, 10001=8, 10005=8, 10009=8, 10003=7, 10007=7, 10012=7, 10015=7, 10013=6, int 10001..10015
- AgentID: 3=19, 5=18, 4=17, 1=16, 8=15, 6=12, 7=8, 2=6, int 1..8
- EntertainerID: 1008=15, 1001=11, 1013=11, 1003=10, 1006=10, 1004=9, 1010=9, 1007=8, 1011=8, 1002=7, 1005=7, 1012=6, int 1001..1013


# Entertainer_Members

```sql
CREATE TABLE Entertainer_Members (
    EntertainerID int NOT NULL,
    MemberID int NOT NULL DEFAULT 0,
    Status smallint NULL DEFAULT 0,
    PRIMARY KEY (EntertainerID, MemberID),
    FOREIGN KEY (EntertainerID) REFERENCES Entertainers(EntertainerID),
    FOREIGN KEY (MemberID) REFERENCES Members(MemberID)
);
```

## Indexes

- (EntertainerID)
- (MemberID)

## Rows

- total=40

| column | latest | sample | sample |
|---|---|---|---|
| EntertainerID | 1013 | 1002 | 1006 |
| MemberID | 124 | 120 | 120 |
| Status | 2 | 2 | 2 |

## Columns

- EntertainerID: 1003=6, 1007=5, 1008=5, 1006=4, 1010=4, 1013=4, 1001=3, 1005=3, 1002=2, 1004=1, 1009=1, 1011=1, 1012=1, int 1001..1013
- MemberID: 25 distinct, int 101..125
  - stats: average=113.4, median=114
  - top_values: 120=3, 121=3, 102=2, 103=2, 104=2, 105=2, 107=2, 112=2, 114=2, 117=2
- Status: 1=27, 2=13


# Entertainer_Styles

```sql
CREATE TABLE Entertainer_Styles (
    EntertainerID int NOT NULL,
    StyleID smallint NOT NULL DEFAULT 0,
    StyleStrength smallint NOT NULL,
    PRIMARY KEY (EntertainerID, StyleID),
    FOREIGN KEY (EntertainerID) REFERENCES Entertainers(EntertainerID),
    FOREIGN KEY (StyleID) REFERENCES Musical_Styles(StyleID)
);
```

## Indexes

- (EntertainerID)
- (StyleID)

## Rows

- total=32

| column | latest | sample | sample |
|---|---|---|---|
| EntertainerID | 1013 | 1008 | 1007 |
| StyleID | 15 | 3 | 6 |
| StyleStrength | 1 | 2 | 2 |

## Columns

- EntertainerID: 1001=3, 1002=3, 1005=3, 1006=3, 1009=3, 1010=3, 1011=3, 1003=2, 1007=2, 1008=2, 1012=2, 1013=2, 1004=1, int 1001..1013
- StyleID: 7=3, 21=3, 3=2, 6=2, 10=2, 13=2, 14=2, 15=2, 19=2, 20=2, 22=2, 23=2, 24=2, 4=1, 8=1, 11=1, 17=1, int 3..24
- StyleStrength: 1=13, 2=12, 3=7, int 1..3


# Entertainers

```sql
CREATE TABLE Entertainers (
    EntertainerID int NOT NULL PRIMARY KEY,
    EntStageName nvarchar (50) NULL,
    EntSSN nvarchar (12) NULL,
    EntStreetAddress nvarchar (50) NULL,
    EntCity nvarchar (30) NULL,
    EntState nvarchar (2) NULL,
    EntZipCode nvarchar (10) NULL,
    EntPhoneNumber nvarchar (15) NULL,
    EntWebPage nvarchar (50) NULL,
    EntEMailAddress nvarchar (50) NULL,
    DateEntered date NULL
);
```

## Indexes

- (EntZipCode)

## Rows

- total=13

| column | latest | sample | sample |
|---|---|---|---|
| EntertainerID | 1013 | 1001 | 1003 |
| EntStageName | Caroline Coie Cuartet | Carol Peacock Trio | JV & the Deep Six |
| EntSSN | 888-71-1123 | 888-90-1121 | 888-18-1013 |
| EntStreetAddress | 298 Forest Lane | 4110 Old Redmond Rd. | 15127 NE 24th, #383 |
| EntCity | Auburn | Redmond | Redmond |
| EntState | WA | WA | WA |
| EntZipCode | 98002 | 98052 | 98052 |
| EntPhoneNumber | 555-2306 | 555-2691 | 555-2511 |
| EntWebPage | null | www.cptrio.com | www.jvd6.com |
| EntEMailAddress | carolinec@willow.com | carolp@cptrio.com | jv@myspring.com |
| DateEntered | 1997-07-11 | 1997-05-24 | 1998-03-18 |

## Columns

- EntertainerID: unique identifier, int 1001..1013
  - stats: average=1007, median=1007
- EntStageName: "Carol Peacock Trio"=1, "Caroline Coie Cuartet"=1, "Coldwater Cattle Company"=1, "Country Feeling"=1, "JV & the Deep Six"=1, "Jazz Persuasion"=1, "Jim Glynn"=1, "Julia Schnebly"=1, "Katherine Ehrlich"=1, "Modern Dance"=1, "Saturday Revue"=1, "Susan McLain"=1, "Topazz"=1
- EntSSN: "888-18-1013"=1, "888-26-1025"=1, "888-30-1031"=1, "888-38-1043"=1, "888-50-1061"=1, "888-61-1103"=1, "888-64-1109"=1, "888-65-1111"=1, "888-66-1085"=1, "888-70-1121"=1, "888-71-1123"=1, "888-90-1121"=1, "888-98-1133"=1
- EntStreetAddress: "13920 S.E. 40th Street"=1, "15127 NE 24th, #383"=1, "16 Maple Lane"=1, "233 West Valley Hwy"=1, "2343 Harmony Lane"=1, "298 Forest Lane"=1, "3887 Easy Street"=1, "4110 Old Redmond Rd."=1, "4726 - 11th Ave. N.E."=1, "511 Lenora Ave"=1, "777 Fenexet Blvd"=1, "PO Box 223311"=1, "Route 2, Box 203B"=1
- EntCity: "Seattle"=4, "Bellevue"=3, "Auburn"=2, "Redmond"=2, "Woodinville"=2
- EntState: "WA"=13
- EntZipCode: "98002"=2, "98052"=2, "98072"=2, "98125"=2, "98005"=1, "98006"=1, "98009"=1, "98105"=1, "99837"=1
- EntPhoneNumber: "555-0039"=1, "555-0399"=1, "555-2301"=1, "555-2306"=1, "555-2511"=1, "555-2531"=1, "555-2541"=1, "555-2561"=1, "555-2591"=1, "555-2631"=1, "555-2691"=1, "555-2711"=1, "555-9936"=1
- EntWebPage: "www.coldwatercows.com"=1, "www.cptrio.com"=1, "www.greensleeves.com"=1, "www.jazzper.com"=1, "www.jvd6.com"=1, "www.moderndance.com"=1, "www.satrevue.com"=1, "www.topazz.com"=1, nulls=5
- EntEMailAddress: "carolinec@willow.com"=1, "carolp@cptrio.com"=1, "edz@coolness.com"=1, "jv@myspring.com"=1, "ke@mzo.com"=1, "mikeh@moderndance.com"=1, "susan@gs.com"=1, nulls=6
- DateEntered: 1995-01-20=1, 1995-05-16=1, 1995-11-30=1, 1996-02-14=1, 1996-02-28=1, 1996-04-01=1, 1996-04-12=1, 1997-05-12=1, 1997-05-24=1, 1997-07-11=1, 1998-03-18=1, 1998-09-13=1, 1998-10-12=1


# Members

```sql
CREATE TABLE Members (
    MemberID int NOT NULL PRIMARY KEY DEFAULT 0,
    MbrFirstName nvarchar (25) NULL,
    MbrLastName nvarchar (25) NULL,
    MbrPhoneNumber nvarchar (15) NULL,
    Gender nvarchar (2) NULL
);
```

## Rows

- total=25

| column | latest | sample | sample |
|---|---|---|---|
| MemberID | 125 | 119 | 125 |
| MbrFirstName | Jim | John | Jim |
| MbrLastName | Glynn | Viescas | Glynn |
| MbrPhoneNumber | 555-2531 | 555-2511 | 555-2531 |
| Gender | null | M | null |

## Columns

- MemberID: unique identifier, int 101..125
  - stats: average=113, median=113
- MbrFirstName: 24 distinct
- MbrLastName: 21 distinct
- MbrPhoneNumber: all distinct
- Gender: "F"=12, "M"=12, nulls=1


# Musical_Preferences

```sql
CREATE TABLE Musical_Preferences (
    CustomerID int NOT NULL DEFAULT 0,
    StyleID smallint NOT NULL DEFAULT 0,
    PreferenceSeq smallint NOT NULL,
    PRIMARY KEY (CustomerID, StyleID),
    FOREIGN KEY (CustomerID) REFERENCES Customers(CustomerID),
    FOREIGN KEY (StyleID) REFERENCES Musical_Styles(StyleID)
);
```

## Indexes

- (CustomerID)
- (StyleID)

## Rows

- total=36

| column | latest | sample | sample |
|---|---|---|---|
| CustomerID | 10015 | 10004 | 10009 |
| StyleID | 21 | 15 | 11 |
| PreferenceSeq | 1 | 1 | 1 |

## Columns

- CustomerID: 10007=3, 10009=3, 10010=3, 10011=3, 10014=3, 10015=3, 10001=2, 10002=2, 10003=2, 10004=2, 10005=2, 10006=2, 10008=2, 10012=2, 10013=2, int 10001..10015
- StyleID: 20 distinct, int 1..24
  - stats: average=14.2222, median=15
  - top_values: 21=4, 10=3, 15=3, 19=3, 1=2, 7=2, 8=2, 18=2, 20=2, 22=2
- PreferenceSeq: 1=15, 2=15, 3=6, int 1..3


# Musical_Styles

```sql
CREATE TABLE Musical_Styles (
    StyleID smallint NOT NULL PRIMARY KEY DEFAULT 0,
    StyleName nvarchar (75) NULL
);
```

## Rows

- total=25

| column | latest | sample | sample |
|---|---|---|---|
| StyleID | 25 | 16 | 4 |
| StyleName | 90's Music | Karaoke | 70's Music |

## Columns

- StyleID: unique identifier, int 1..25
  - stats: average=13, median=13
- StyleName: all distinct


# ztblDays

```sql
CREATE TABLE ztblDays (
    DateField date NOT NULL PRIMARY KEY
);
```

## Rows

- total=1096

| column | latest | sample | sample |
|---|---|---|---|
| DateField | 2020-01-01 | 2017-05-13 | 2019-11-03 |

## Columns

- DateField: unique identifier


# ztblMonths

```sql
CREATE TABLE ztblMonths (
    MonthYear nvarchar (15) NULL,
    YearNumber smallint NOT NULL,
    MonthNumber smallint NOT NULL,
    MonthStart date NULL,
    MonthEnd date NULL,
    January smallint NULL DEFAULT 0,
    February smallint NULL DEFAULT 0,
    March smallint NULL DEFAULT 0,
    April smallint NULL DEFAULT 0,
    May smallint NULL DEFAULT 0,
    June smallint NULL DEFAULT 0,
    July smallint NULL DEFAULT 0,
    August smallint NULL DEFAULT 0,
    September smallint NULL DEFAULT 0,
    October smallint NULL DEFAULT 0,
    November smallint NULL DEFAULT 0,
    December smallint NULL DEFAULT 0,
    PRIMARY KEY (YearNumber, MonthNumber)
);
```

## Indexes

- UNIQUE (MonthStart)
- UNIQUE (MonthYear)
- UNIQUE (MonthEnd)

## Rows

- total=36

| column | latest | sample | sample |
|---|---|---|---|
| MonthYear | December 2019 | August 2019 | March 2017 |
| YearNumber | 2019 | 2019 | 2017 |
| MonthNumber | 12 | 8 | 3 |
| MonthStart | 2019-12-01 | 2019-08-01 | 2017-03-01 |
| MonthEnd | 2019-12-31 | 2019-08-31 | 2017-03-31 |
| January | 0 | 0 | 0 |
| February | 0 | 0 | 0 |
| March | 0 | 0 | 1 |
| April | 0 | 0 | 0 |
| May | 0 | 0 | 0 |
| June | 0 | 0 | 0 |
| July | 0 | 0 | 0 |
| August | 0 | 1 | 0 |
| September | 0 | 0 | 0 |
| October | 0 | 0 | 0 |
| November | 0 | 0 | 0 |
| December | 1 | 0 | 0 |

## Columns

- MonthYear: unique identifier
- YearNumber: 2017=12, 2018=12, 2019=12, int 2017..2019
- MonthNumber: 1=3, 2=3, 3=3, 4=3, 5=3, 6=3, 7=3, 8=3, 9=3, 10=3, 11=3, 12=3, int 1..12
- MonthStart: unique identifier
- MonthEnd: unique identifier
- January: 0=33, 1=3
- February: 0=33, 1=3
- March: 0=33, 1=3
- April: 0=33, 1=3
- May: 0=33, 1=3
- June: 0=33, 1=3
- July: 0=33, 1=3
- August: 0=33, 1=3
- September: 0=33, 1=3
- October: 0=33, 1=3
- November: 0=33, 1=3
- December: 0=33, 1=3


# ztblSkipLabels

```sql
CREATE TABLE ztblSkipLabels (
    LabelCount int NOT NULL PRIMARY KEY
);
```

## Rows

- total=60

| column | latest | sample | sample |
|---|---|---|---|
| LabelCount | 60 | 53 | 26 |

## Columns

- LabelCount: unique identifier, int 1..60
  - stats: average=30.5, median=30.5


# ztblWeeks

```sql
CREATE TABLE ztblWeeks (
    WeekStart date NOT NULL PRIMARY KEY,
    WeekEnd date NULL
);
```

## Rows

- total=156

| column | latest | sample | sample |
|---|---|---|---|
| WeekStart | 2019-12-22 | 2019-06-30 | 2019-02-03 |
| WeekEnd | 2019-12-28 | 2019-07-06 | 2019-02-09 |

## Columns

- WeekStart: unique identifier
- WeekEnd: all distinct
