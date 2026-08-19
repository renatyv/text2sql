---
generator: db-snooper
version: 0.0.26
generated_at_utc: 2026-08-16T08:09:26.794266Z
dialect: sqlite
database: /var/folders/9j/b9bx_drd53sc6zbpsqyrjy4h0000gn/T/dbsnoop-90cr0if6/school_scheduling.sqlite
schema: main
---

## Relationships

- Buildings.BuildingCode ← Class_Rooms.BuildingCode
- Categories.CategoryID ← Faculty_Categories.CategoryID, Subjects.CategoryID
- Class_Rooms.ClassRoomID ← Classes.ClassRoomID
- Classes.ClassID ← Faculty_Classes.ClassID, Student_Schedules.ClassID
- Faculty.StaffID ← Faculty_Categories.StaffID, Faculty_Subjects.StaffID
- Majors.MajorID ← Students.StudMajor
- Staff.StaffID ← Departments.DeptChair, Faculty.StaffID, Faculty_Classes.StaffID
- Student_Class_Status.ClassStatus ← Student_Schedules.ClassStatus
- Students.StudentID ← Student_Schedules.StudentID
- Subjects.SubjectCode ← Subjects.SubjectPreReq
- Subjects.SubjectID ← Classes.SubjectID, Faculty_Subjects.SubjectID

# Buildings

## All rows

| column | row 1 | row 2 | row 3 | row 4 | row 5 | row 6 |
|---|---|---|---|---|---|---|
| BuildingCode | AS | CC | GYM | IB | LB | TB |
| BuildingName | Arts and Sciences | College Center | PE and Wellness | Instructional Building | Library | Technology Building |
| NumberOfFloors | 3 | 3 | 1 | 3 | 2 | 2 |
| ElevatorAccess | true | true | false | true | true | true |
| SiteParkingAvailable | true | false | true | true | true | true |


# Categories

```sql
CREATE TABLE Categories (
    CategoryID TEXT NOT NULL,
    CategoryDescription TEXT,
    DepartmentID INTEGER DEFAULT 0,
    PRIMARY KEY (CategoryID)
);
```

## Indexes

- (DepartmentID)

## Rows

- total=19

| column | latest | sample | sample |
|---|---|---|---|
| CategoryID | PSY | FRE | BIO |
| CategoryDescription | Psychology | French | Biology |
| DepartmentID | 4 | 3 | 2 |

## Columns

- CategoryID: unique identifier
- CategoryDescription: "Accounting"=1, "Art"=1, "Biology"=1, "Business"=1, "Chemistry"=1, "Computer Information Systems"=1, "Computer Science"=1, "Economics"=1, "English"=1, "French"=1, "Geography"=1, "German"=1, "History"=1, "Journalism"=1, "Math"=1, "Music"=1, "Physics"=1, "Political Science"=1, "Psychology"=1
- DepartmentID: 3=5, 4=5, 2=4, 1=3, 5=2, int 1..5


# Class_Rooms

```sql
CREATE TABLE Class_Rooms (
    ClassRoomID INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
    BuildingCode TEXT,
    PhoneAvailable BOOLEAN NOT NULL DEFAULT 0,
    FOREIGN KEY (BuildingCode) REFERENCES Buildings(BuildingCode)
);
```

## Indexes

- (BuildingCode)

## Rows

- total=47

| column | latest | sample | sample |
|---|---|---|---|
| ClassRoomID | 3455 | 2408 | 1514 |
| BuildingCode | CC | IB | AS |
| PhoneAvailable | true | false | true |

## Columns

- ClassRoomID: unique identifier, int 1131..3455
  - stats: average=2637.45, median=3313
- BuildingCode: "IB"=18, "CC"=12, "AS"=10, "TB"=4, "LB"=3
- PhoneAvailable: False=27, True=20


# Classes

```sql
CREATE TABLE Classes (
    ClassID INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
    SubjectID INTEGER DEFAULT 0,
    ClassRoomID INTEGER DEFAULT 0,
    Credits INTEGER DEFAULT 0,
    StartDate DATE,
    StartTime TIME,
    Duration INTEGER DEFAULT 0,
    MondaySchedule BOOLEAN NOT NULL DEFAULT 0,
    TuesdaySchedule BOOLEAN NOT NULL DEFAULT 0,
    WednesdaySchedule BOOLEAN NOT NULL DEFAULT 0,
    ThursdaySchedule BOOLEAN NOT NULL DEFAULT 0,
    FridaySchedule BOOLEAN NOT NULL DEFAULT 0,
    SaturdaySchedule BOOLEAN NOT NULL DEFAULT 0,
    FOREIGN KEY (ClassRoomID) REFERENCES Class_Rooms(ClassRoomID),
    FOREIGN KEY (SubjectID) REFERENCES Subjects(SubjectID)
);
```

## Indexes

- (ClassRoomID)
- (SubjectID)

## Rows

- total=147

| column | latest | sample | sample |
|---|---|---|---|
| ClassID | 6600 | 2889 | 2917 |
| SubjectID | 41 | 45 | 47 |
| ClassRoomID | 3420 | 2423 | 3422 |
| Credits | 5 | 5 | 5 |
| StartDate | 2018-01-15 | 2017-09-11 | 2017-09-11 |
| StartTime | 13:00:00 | 16:00:00 | 14:00:00 |
| Duration | 140 | 50 | 50 |
| MondaySchedule | true | true | true |
| TuesdaySchedule | false | true | true |
| WednesdaySchedule | true | true | true |
| ThursdaySchedule | false | true | true |
| FridaySchedule | false | true | true |
| SaturdaySchedule | false | false | false |

## Columns

- ClassID: unique identifier, int 1000..6600
  - stats: average=3825.17, median=4030
- SubjectID: 52 distinct, int 1..56
  - stats: average=30.9116, median=32
  - top_values: 37=6, 38=6, 45=6, 46=6, 47=6, 1=4, 13=4, 16=4, 20=4, 23=4
- ClassRoomID: 39 distinct, int 1131..3446
  - stats: average=2652.28, median=3315
  - top_values: 3352=12, 3346=10, 1624=8, 3415=8, 1231=7, 1627=6, 2423=6, 3353=6, 3422=6, 3445=6
- Credits: 5=111, 4=19, 3=15, 2=2, int 2..5
- StartDate: 2018-01-15=65, 2017-09-11=52, 2018-01-16=15, 2017-09-12=13, 2017-09-16=1, 2018-01-20=1
- StartTime: 09:00:00=18, 08:00:00=16, 10:00:00=16, 11:00:00=16, 13:00:00=15, 16:00:00=14, 12:00:00=11, 15:00:00=11, 14:00:00=9, 13:30:00=7, 07:00:00=2, 07:30:00=2, 10:30:00=2, 11:30:00=2, 14:30:00=2, 15:30:00=2, 18:00:00=2
- Duration: 50=100, 140=30, 110=12, 80=3, 280=2, int 50..280
- MondaySchedule: True=118, False=29
- TuesdaySchedule: True=97, False=50
- WednesdaySchedule: True=112, False=35
- ThursdaySchedule: True=99, False=48
- FridaySchedule: True=99, False=48
- SaturdaySchedule: False=127, True=20


# Departments

## All rows

| column | row 1 | row 2 | row 3 | row 4 | row 5 |
|---|---|---|---|---|---|
| DepartmentID | 1 | 2 | 3 | 4 | 5 |
| DeptName | Business Administration | Sciences | Humanities | Social Sciences | Information Technology |
| DeptChair | 98012 | 98010 | 98005 | 98059 | 98007 |


# Faculty

```sql
CREATE TABLE Faculty (
    StaffID INTEGER NOT NULL DEFAULT 0,
    Title TEXT,
    Status TEXT,
    Tenured BOOLEAN NOT NULL DEFAULT 0,
    PRIMARY KEY (StaffID),
    FOREIGN KEY (StaffID) REFERENCES Staff(StaffID)
);
```

## Rows

- total=24

| column | latest | sample | sample |
|---|---|---|---|
| StaffID | 98064 | 98014 | 98030 |
| Title | Professor | Associate Professor | Instructor |
| Status | Full Time | Full Time | Full Time |
| Tenured | true | true | true |

## Columns

- StaffID: unique identifier, int 98005..98064
  - stats: average=98033.9, median=98033
- Title: "Professor"=11, "Instructor"=8, "Associate Professor"=5
- Status: "Full Time"=22, "On Leave"=1, "Part Time"=1
- Tenured: True=22, False=2


# Faculty_Categories

```sql
CREATE TABLE Faculty_Categories (
    StaffID INTEGER NOT NULL,
    CategoryID TEXT NOT NULL DEFAULT 'ACC',
    PRIMARY KEY (StaffID, CategoryID),
    FOREIGN KEY (CategoryID) REFERENCES Categories(CategoryID),
    FOREIGN KEY (StaffID) REFERENCES Faculty(StaffID)
);
```

## Indexes

- (CategoryID)
- (StaffID)

## Rows

- total=76

| column | latest | sample | sample |
|---|---|---|---|
| StaffID | 98064 | 98030 | 98019 |
| CategoryID | JRN | MAT | MAT |

## Columns

- StaffID: 24 distinct, int 98005..98064
  - stats: average=98034, median=98033
  - top_values: 98007=4, 98030=4, 98052=4, 98055=4, 98005=3, 98010=3, 98011=3, 98012=3, 98013=3, 98014=3
- CategoryID: "MAT"=12, "ART"=8, "ENG"=7, "ACC"=6, "CIS"=6, "ECO"=6, "BUS"=4, "CHE"=4, "HIS"=4, "MUS"=4, "PHY"=4, "BIO"=3, "POL"=3, "CSC"=2, "GEG"=2, "JRN"=1


# Faculty_Classes

```sql
CREATE TABLE Faculty_Classes (
    ClassID INTEGER NOT NULL,
    StaffID INTEGER NOT NULL,
    PRIMARY KEY (ClassID, StaffID),
    FOREIGN KEY (ClassID) REFERENCES Classes(ClassID),
    FOREIGN KEY (StaffID) REFERENCES Staff(StaffID)
);
```

## Indexes

- (ClassID)
- (StaffID)

## Rows

- total=145

| column | latest | sample | sample |
|---|---|---|---|
| ClassID | 6600 | 2633 | 2895 |
| StaffID | 98042 | 98030 | 98013 |

## Columns

- ClassID: unique identifier, int 1000..6600
  - stats: average=3834.59, median=4030
- StaffID: 23 distinct, int 98005..98064
  - stats: average=98032.3, median=98030
  - top_values: 98012=11, 98013=10, 98030=10, 98055=9, 98007=8, 98011=8, 98036=8, 98053=8, 98059=8, 98020=7


# Faculty_Subjects

```sql
CREATE TABLE Faculty_Subjects (
    StaffID INTEGER NOT NULL DEFAULT 0,
    SubjectID INTEGER NOT NULL DEFAULT 0,
    ProficiencyRating REAL DEFAULT 0,
    PRIMARY KEY (StaffID, SubjectID),
    FOREIGN KEY (StaffID) REFERENCES Faculty(StaffID),
    FOREIGN KEY (SubjectID) REFERENCES Subjects(SubjectID)
);
```

## Indexes

- (StaffID)
- (SubjectID)

## Rows

- total=110

| column | latest | sample | sample |
|---|---|---|---|
| StaffID | 98064 | 98007 | 98053 |
| SubjectID | 41 | 2 | 18 |
| ProficiencyRating | 8 | 9 | 9 |

## Columns

- StaffID: 24 distinct, int 98005..98064
  - stats: average=98034.7, median=98036
  - top_values: 98062=6, 98063=6, 98005=5, 98007=5, 98013=5, 98014=5, 98020=5, 98028=5, 98030=5, 98042=5
- SubjectID: 55 distinct, int 1..56
  - stats: average=28.4909, median=28
  - top_values: 1=2, 2=2, 3=2, 4=2, 5=2, 6=2, 7=2, 8=2, 9=2, 10=2
- ProficiencyRating: 9=40, 8=37, 10=33, num 8..10


# Majors

## All rows

| column | row 1 | row 2 | row 3 | row 4 | row 5 | row 6 | row 7 |
|---|---|---|---|---|---|---|---|
| MajorID | 1 | 2 | 3 | 4 | 5 | 6 | 7 |
| Major | General Studies | English | Music | Information Sciences | Accounting | Art | Mathematics |


# Staff

```sql
CREATE TABLE Staff (
    StaffID INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
    StfFirstName TEXT,
    StfLastname TEXT,
    StfStreetAddress TEXT,
    StfCity TEXT,
    StfState TEXT,
    StfZipCode TEXT,
    StfAreaCode TEXT,
    StfPhoneNumber TEXT,
    Salary REAL,
    DateHired DATE,
    Position TEXT
);
```

## Indexes

- (StfZipCode)

## Rows

- total=27

| column | latest | sample | sample |
|---|---|---|---|
| StaffID | 98064 | 98036 | 98040 |
| StfFirstName | Luke | Sam | Jim |
| StfLastname | Patterson | Abolrous | Wilson |
| StfStreetAddress | 877 145th Ave SE | 611 Alpine Drive | 101 NE 88th |
| StfCity | Portland | Palm Springs | Salem |
| StfState | OR | CA | OR |
| StfZipCode | 97208 | 92263 | 97301 |
| StfAreaCode | 503 | 760 | 503 |
| StfPhoneNumber | 555-2316 | 555-2611 | 555-2636 |
| Salary | 56000 | 60000 | 50000 |
| DateHired | 1989-08-20 | 1982-11-20 | 1987-01-13 |
| Position | Faculty | Faculty | Faculty |

## Columns

- StaffID: unique identifier, int 98005..98064
  - stats: average=98034.6, median=98036
- StfFirstName: 26 distinct
- StfLastname: "Patterson"=4, "Smith"=3, "Viescas"=3, "Hallmark"=2, "Abolrous"=1, "Black"=1, "Bonnicksen"=1, "Brehm"=1, "Brown"=1, "Coie"=1, "DeGrasse"=1, "Ehrlich"=1, "Glynn"=1, "Hernandez"=1, "Keyser"=1, "Rosales III"=1, "Sergienko"=1, "Waldal"=1, "Wilson"=1
- StfStreetAddress: 22 distinct
- StfCity: "Seattle"=4, "Bellevue"=3, "Tacoma"=3, "Fremont"=2, "Kirkland"=2, "Marysville"=2, "Portland"=2, "Redmond"=2, "Auburn"=1, "El Paso"=1, "Houston"=1, "Long Beach"=1, "Palm Springs"=1, "Salem"=1, "San Antonio"=1
- StfState: "WA"=17, "CA"=4, "OR"=3, "TX"=3
- StfZipCode: "98413"=3, "94538"=2, "97208"=2, "98006"=2, "98033"=2, "98052"=2, "98125"=2, "77201"=1, "78284"=1, "79993"=1, "90809"=1, "92263"=1, "97301"=1, "98002"=1, "98009"=1, "98106"=1, "98115"=1, "98270"=1, "98271"=1
- StfAreaCode: "425"=8, "253"=5, "206"=4, "503"=3, "510"=2, "210"=1, "562"=1, "713"=1, "760"=1, "915"=1
- StfPhoneNumber: all distinct
- Salary: 45000=6, 60000=5, 52000=3, 44000=2, 48000=2, 50000=2, 25000=1, 35000=1, 40000=1, 49000=1, 53000=1, 56000=1, 57000=1, num 25000..60000
- DateHired: all distinct
- Position: "Faculty"=24, "Graduate Advisor"=1, "Registrar"=1, "Secretary"=1


# Student_Class_Status

## All rows

| column | row 1 | row 2 | row 3 |
|---|---|---|---|
| ClassStatus | 1 | 2 | 3 |
| ClassStatusDescription | Enrolled | Completed | Withdrew |


# Student_Schedules

```sql
CREATE TABLE Student_Schedules (
    StudentID INTEGER NOT NULL,
    ClassID INTEGER NOT NULL,
    ClassStatus INTEGER DEFAULT 0,
    Grade REAL DEFAULT 0,
    PRIMARY KEY (StudentID, ClassID),
    FOREIGN KEY (ClassID) REFERENCES Classes(ClassID),
    FOREIGN KEY (ClassStatus) REFERENCES Student_Class_Status(ClassStatus),
    FOREIGN KEY (StudentID) REFERENCES Students(StudentID)
);
```

## Rows

- total=120

| column | latest | sample | sample |
|---|---|---|---|
| StudentID | 1018 | 1008 | 1014 |
| ClassID | 5933 | 5917 | 5071 |
| ClassStatus | 1 | 1 | 1 |
| Grade | 0 | 0 | 0 |

## Columns

- StudentID: 1001=7, 1003=7, 1004=7, 1005=7, 1006=7, 1007=7, 1008=7, 1009=7, 1011=7, 1012=7, 1013=7, 1014=7, 1015=7, 1016=7, 1017=7, 1018=7, 1002=4, 1010=4, int 1001..1018
- ClassID: 32 distinct, int 1000..6082
  - stats: average=3197.24, median=2907
  - top_values: 2907=10, 4180=9, 1156=8, 1000=7, 4196=7, 6082=6, 1180=5, 1500=5, 2500=5, 5917=4
- ClassStatus: 2=68, 1=50, 3=2, int 1..3
- Grade: 68 distinct, num 0..99.83
  - stats: average=46.359, median=68.78


# Students

```sql
CREATE TABLE Students (
    StudentID INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
    StudFirstName TEXT,
    StudLastName TEXT,
    StudStreetAddress TEXT,
    StudCity TEXT,
    StudState TEXT,
    StudZipCode TEXT,
    StudAreaCode TEXT,
    StudPhoneNumber TEXT,
    StudGPA REAL DEFAULT 0,
    StudMajor INTEGER,
    FOREIGN KEY (StudMajor) REFERENCES Majors(MajorID)
);
```

## Indexes

- (StudAreaCode)
- (StudMajor)
- (StudZipCode)

## Rows

- total=19

| column | latest | sample | sample |
|---|---|---|---|
| StudentID | 1019 | 1003 | 1002 |
| StudFirstName | Daffy | Betsy | David |
| StudLastName | Dumbwit | Stadick | Hamilton |
| StudStreetAddress | 4567 NE 32nd Ct | 611 Alpine Drive | 908 W. Capital Way |
| StudCity | Bellevue | Palm Springs | Tacoma |
| StudState | WA | CA | WA |
| StudZipCode | 98002 | 92263 | 98413 |
| StudAreaCode | 425 | 760 | 253 |
| StudPhoneNumber | 555-9872 | 555-2696 | 555-2701 |
| StudGPA | 0 | 85.235 | 78.755 |
| StudMajor | null | 3 | 2 |

## Columns

- StudentID: unique identifier, int 1001..1019
  - stats: average=1010, median=1010
- StudFirstName: "Betsy"=1, "Brannon"=1, "Daffy"=1, "David"=1, "Doris"=1, "Elizabeth"=1, "George"=1, "Janice"=1, "John"=1, "Karen"=1, "Kendra"=1, "Kerry"=1, "Marianne"=1, "Michael"=1, "Richard"=1, "Sara"=1, "Sarah"=1, "Scott"=1, "Steve"=1
- StudLastName: "Bishop"=1, "Bonnicksen"=1, "Chavez"=1, "Dumbwit"=1, "Galvin"=1, "Hallmark"=1, "Hamilton"=1, "Hartwig"=1, "Jones"=1, "Kennedy"=1, "Lum"=1, "Patterson"=1, "Pundt"=1, "Sheskey"=1, "Smith"=1, "Stadick"=1, "Thompson"=1, "Viescas"=1, "Wier"=1
- StudStreetAddress: "16679 NE 41st Court"=2, "908 W. Capital Way"=2, "12330 Larchlemont Lane"=1, "15127 NE 24th, #383"=1, "2222 Springer Road"=1, "2500 Rosales Lane"=1, "281 Old Navy Road"=1, "30301 - 166th Ave. N.E."=1, "4110 Old Redmond Rd."=1, "4567 NE 32nd Ct"=1, "4726 - 11th Ave. N.E."=1, "611 Alpine Drive"=1, "66 Spring Valley Drive"=1, "754 Fourth Ave"=1, "777 Fenexet Blvd"=1, "9877 Hacienda Drive"=1, "Route 2, Box 203B"=1
- StudCity: "Seattle"=3, "Marysville"=2, "Portland"=2, "Redmond"=2, "Tacoma"=2, "Bellevue"=1, "Dallas"=1, "Eugene"=1, "Long Beach"=1, "Lubbock"=1, "Medford"=1, "Palm Springs"=1, "San Antonio"=1
- StudState: "WA"=10, "OR"=4, "TX"=3, "CA"=2
- StudZipCode: "97208"=2, "98052"=2, "98105"=2, "98413"=2, "75204"=1, "78284"=1, "79402"=1, "90809"=1, "92263"=1, "97401"=1, "97501"=1, "98002"=1, "98115"=1, "98270"=1, "98271"=1
- StudAreaCode: "206"=4, "253"=3, "425"=3, "503"=2, "541"=2, "210"=1, "562"=1, "760"=1, "806"=1, "972"=1
- StudPhoneNumber: "555-0399"=1, "555-2296"=1, "555-2521"=1, "555-2551"=1, "555-2566"=1, "555-2606"=1, "555-2621"=1, "555-2626"=1, "555-2656"=1, "555-2666"=1, "555-2671"=1, "555-2691"=1, "555-2696"=1, "555-2701"=1, "555-2706"=1, "555-2716"=1, "555-9872"=1, "555-9930"=1, "555-9938"=1
- StudGPA: 0=1, 72.225=1, 72.55=1, 74.465=1, 77.125=1, 77.65=1, 78.755=1, 79.25=1, 80=1, 80.25=1, 81=1, 83.55=1, 84.625=1, 85.235=1, 85.55=1, 86=1, 87.65=1, 88.5=1, 89.5=1, num 0..89.5
- StudMajor: 2=3, 4=3, 6=3, 7=3, 1=2, 3=2, 5=2, nulls=1, int 1..7


# Subjects

```sql
CREATE TABLE Subjects (
    SubjectID INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
    CategoryID TEXT,
    SubjectCode TEXT UNIQUE,
    SubjectName TEXT,
    SubjectPreReq TEXT DEFAULT NULL,
    SubjectDescription TEXT,
    FOREIGN KEY (CategoryID) REFERENCES Categories(CategoryID),
    FOREIGN KEY (SubjectPreReq) REFERENCES Subjects(SubjectCode)
);
```

## Indexes

- (CategoryID)
- (SubjectPreReq)

## Rows

- total=56

| column | latest | sample | sample |
|---|---|---|---|
| SubjectID | 56 | 32 | 7 |
| CategoryID | POL | ECO | BUS |
| SubjectCode | POL 213 | ECO 201 | BUS 155 |
| SubjectName | Women and Politics | Principles of Economics: Macroeconomics | Developing A Feasibility Plan |
| SubjectPreReq | null | null | null |
| SubjectDescription | Introduction to concepts of power and policy issues as they relate to women. Theoretical, historical and empirical studies of women's participation in social and political movements nationally and internationally. Study of women's diverse roles in relations to family, economics, labor, government, and law. | Analysis of the aggregate economy: GDP, inflation, business cycles, trade and finance. Intermediate algebra or equivalent required. | With the aid of a counselor, a feasibility plan will be developed which will be the basis or start of your business plan. Must be concurrently enrolled in BUS 151. |

## Columns

- SubjectID: unique identifier, int 1..56
  - stats: average=28.5, median=28.5
- CategoryID: "ART"=6, "ACC"=5, "BUS"=5, "MAT"=5, "CIS"=4, "MUS"=4, "PHY"=4, "BIO"=3, "CHE"=3, "ECO"=3, "ENG"=3, "HIS"=3, "POL"=3, "CSC"=2, "GEG"=2, "JRN"=1
- SubjectCode: unique identifier
- SubjectName: all distinct
- SubjectPreReq: "ACC 220"=3, "ACC 210"=1, "BUS 170"=1, "ENG 101"=1, "MAT 098"=1, "MUS 101"=1, "PHY 201"=1, nulls=47
- SubjectDescription: all distinct
