---
generator: db-snooper
version: 0.0.31
generated_at_utc: 2026-08-20T17:29:08.272777Z
dialect: sqlite
database: /var/folders/9j/b9bx_drd53sc6zbpsqyrjy4h0000gn/T/dbsnoop-glin9yia/school_scheduling.sqlite
schema: main
---

## Relationships

- "Buildings"."BuildingCode" ← "Class_Rooms"."BuildingCode"
- "Categories"."CategoryID" ← "Faculty_Categories"."CategoryID", "Subjects"."CategoryID"
- "Class_Rooms"."ClassRoomID" ← "Classes"."ClassRoomID"
- "Classes"."ClassID" ← "Faculty_Classes"."ClassID", "Student_Schedules"."ClassID"
- "Faculty"."StaffID" ← "Faculty_Categories"."StaffID", "Faculty_Subjects"."StaffID"
- "Majors"."MajorID" ← "Students"."StudMajor"
- "Staff"."StaffID" ← "Departments"."DeptChair", "Faculty"."StaffID", "Faculty_Classes"."StaffID"
- "Student_Class_Status"."ClassStatus" ← "Student_Schedules"."ClassStatus"
- "Students"."StudentID" ← "Student_Schedules"."StudentID"
- "Subjects"."SubjectCode" ← "Subjects"."SubjectPreReq"
- "Subjects"."SubjectID" ← "Classes"."SubjectID", "Faculty_Subjects"."SubjectID"

# "Buildings"  (rows=6)

columns:
"BuildingCode" text PK: unique identifier
"BuildingName" text: "Arts and Sciences"=1, "College Center"=1, "Instructional Building"=1, "Library"=1, "PE and Wellness"=1, "Technology Building"=1
"NumberOfFloors" int: 3=3, 2=2, 1=1, 1..3
"ElevatorAccess" bool NOTNULL: 1=5, 0=1
"SiteParkingAvailable" bool NOTNULL: 1=5, 0=1

indexes: "NumberOfFloors"
fk: none

all rows:
| column | row 1 | row 2 | row 3 | row 4 | row 5 | row 6 |
|---|---|---|---|---|---|---|
| BuildingCode | AS | CC | GYM | IB | LB | TB |
| BuildingName | Arts and Sciences | College Center | PE and Wellness | Instructional Building | Library | Technology Building |
| NumberOfFloors | 3 | 3 | 1 | 3 | 2 | 2 |
| ElevatorAccess | true | true | false | true | true | true |
| SiteParkingAvailable | true | false | true | true | true | true |

# "Categories"  (rows=19)

columns:
"CategoryID" text PK: unique identifier
"CategoryDescription" text: "Accounting"=1, "Art"=1, "Biology"=1, "Business"=1, "Chemistry"=1, "Computer Information Systems"=1, "Computer Science"=1, "Economics"=1, "English"=1, "French"=1, "Geography"=1, "German"=1, "History"=1, "Journalism"=1, "Math"=1, "Music"=1, "Physics"=1, "Political Science"=1, "Psychology"=1
"DepartmentID" int: 3=5, 4=5, 2=4, 1=3, 5=2, 1..5

indexes: "DepartmentID"
fk: none

samples:
| column | latest | sample | sample |
|---|---|---|---|
| CategoryID | PSY | PHY | BUS |
| CategoryDescription | Psychology | Physics | Business |
| DepartmentID | 4 | 2 | 1 |

# "Class_Rooms"  (rows=47)

columns:
"ClassRoomID" int PK: unique identifier, 1131..3455, avg=2637.45, median=3313
"BuildingCode" text FK: "IB"=18, "CC"=12, "AS"=10, "TB"=4, "LB"=3
"PhoneAvailable" bool NOTNULL: 0=27, 1=20

indexes: "BuildingCode"
fk: "BuildingCode"→"Buildings"."BuildingCode"

samples:
| column | latest | sample | sample |
|---|---|---|---|
| ClassRoomID | 3455 | 3319 | 3406 |
| BuildingCode | CC | IB | IB |
| PhoneAvailable | true | false | true |

# "Classes"  (rows=147)

columns:
"ClassID" int PK: unique identifier, 1000..6600, avg=3825.17, median=4030
"SubjectID" int FK: 52 distinct, 1..56, avg=30.9116, median=32, 37=6, 38=6, 45=6, 46=6, 47=6, 1=4, 13=4, 16=4, 20=4, 23=4
"ClassRoomID" int FK: 39 distinct, 1131..3446, avg=2652.28, median=3315, 3352=12, 3346=10, 1624=8, 3415=8, 1231=7, 1627=6, 2423=6, 3353=6, 3422=6, 3445=6
"Credits" int: 5=111, 4=19, 3=15, 2=2, 2..5
"StartDate" date: "2018-01-15"=65, "2017-09-11"=52, "2018-01-16"=15, "2017-09-12"=13, "2017-09-16"=1, "2018-01-20"=1
"StartTime" time: "09:00:00"=18, "08:00:00"=16, "10:00:00"=16, "11:00:00"=16, "13:00:00"=15, "16:00:00"=14, "12:00:00"=11, "15:00:00"=11, "14:00:00"=9, "13:30:00"=7, "07:00:00"=2, "07:30:00"=2, "10:30:00"=2, "11:30:00"=2, "14:30:00"=2, "15:30:00"=2, "18:00:00"=2
"Duration" int: 50=100, 140=30, 110=12, 80=3, 280=2, 50..280
"MondaySchedule" bool NOTNULL: 1=118, 0=29
"TuesdaySchedule" bool NOTNULL: 1=97, 0=50
"WednesdaySchedule" bool NOTNULL: 1=112, 0=35
"ThursdaySchedule" bool NOTNULL: 1=99, 0=48
"FridaySchedule" bool NOTNULL: 1=99, 0=48
"SaturdaySchedule" bool NOTNULL: 0=127, 1=20

indexes: "ClassRoomID", "SubjectID"
fk: "ClassRoomID"→"Class_Rooms"."ClassRoomID", "SubjectID"→"Subjects"."SubjectID"

samples:
| column | latest | sample | sample |
|---|---|---|---|
| ClassID | 6600 | 2075 | 4000 |
| SubjectID | 41 | 51 | 11 |
| ClassRoomID | 3420 | 1624 | 1231 |
| Credits | 5 | 5 | 5 |
| StartDate | 2018-01-15 | 2017-09-11 | 2018-01-16 |
| StartTime | 13:00:00 | 07:00:00 | 10:00:00 |
| Duration | 140 | 140 | 50 |
| MondaySchedule | true | true | false |
| TuesdaySchedule | false | false | true |
| WednesdaySchedule | true | false | true |
| ThursdaySchedule | false | false | true |
| FridaySchedule | false | true | true |
| SaturdaySchedule | false | false | true |

# "Departments"  (rows=5)

columns:
"DepartmentID" int PK: unique identifier, 1..5, avg=3, median=3
"DeptName" text: "Business Administration"=1, "Humanities"=1, "Information Technology"=1, "Sciences"=1, "Social Sciences"=1
"DeptChair" int FK: 98005=1, 98007=1, 98010=1, 98012=1, 98059=1, 98005..98059

indexes: "DeptChair"
fk: "DeptChair"→"Staff"."StaffID"

all rows:
| column | row 1 | row 2 | row 3 | row 4 | row 5 |
|---|---|---|---|---|---|
| DepartmentID | 1 | 2 | 3 | 4 | 5 |
| DeptName | Business Administration | Sciences | Humanities | Social Sciences | Information Technology |
| DeptChair | 98012 | 98010 | 98005 | 98059 | 98007 |

# "Faculty"  (rows=24)

columns:
"StaffID" int PK FK: unique identifier, 98005..98064, avg=98033.9, median=98033
"Title" text: "Professor"=11, "Instructor"=8, "Associate Professor"=5
"Status" text: "Full Time"=22, "On Leave"=1, "Part Time"=1
"Tenured" bool NOTNULL: 1=22, 0=2

indexes: none
fk: "StaffID"→"Staff"."StaffID"

samples:
| column | latest | sample | sample |
|---|---|---|---|
| StaffID | 98064 | 98040 | 98059 |
| Title | Professor | Associate Professor | Professor |
| Status | Full Time | Full Time | Full Time |
| Tenured | true | true | true |

# "Faculty_Categories"  (rows=76)

columns:
"StaffID" int PK FK: 24 distinct, 98005..98064, avg=98034, median=98033, 98007=4, 98030=4, 98052=4, 98055=4, 98005=3, 98010=3, 98011=3, 98012=3, 98013=3, 98014=3
"CategoryID" text PK FK: "MAT"=12, "ART"=8, "ENG"=7, "ACC"=6, "CIS"=6, "ECO"=6, "BUS"=4, "CHE"=4, "HIS"=4, "MUS"=4, "PHY"=4, "BIO"=3, "POL"=3, "CSC"=2, "GEG"=2, "JRN"=1

indexes: "CategoryID", "StaffID"
fk: "StaffID"→"Faculty"."StaffID", "CategoryID"→"Categories"."CategoryID"

samples:
| column | latest | sample | sample |
|---|---|---|---|
| StaffID | 98064 | 98059 | 98055 |
| CategoryID | JRN | ECO | ENG |

# "Faculty_Classes"  (rows=145)

columns:
"ClassID" int PK FK: unique identifier, 1000..6600, avg=3834.59, median=4030
"StaffID" int PK FK: 23 distinct, 98005..98064, avg=98032.3, median=98030, 98012=11, 98013=10, 98030=10, 98055=9, 98007=8, 98011=8, 98036=8, 98053=8, 98059=8, 98020=7

indexes: "ClassID", "StaffID"
fk: "StaffID"→"Staff"."StaffID", "ClassID"→"Classes"."ClassID"

samples:
| column | latest | sample | sample |
|---|---|---|---|
| ClassID | 6600 | 4030 | 5223 |
| StaffID | 98042 | 98036 | 98053 |

# "Faculty_Subjects"  (rows=110)

columns:
"StaffID" int PK FK: 24 distinct, 98005..98064, avg=98034.7, median=98036, 98062=6, 98063=6, 98005=5, 98007=5, 98013=5, 98014=5, 98020=5, 98028=5, 98030=5, 98042=5
"SubjectID" int PK FK: 55 distinct, 1..56, avg=28.4909, median=28, 1=2, 2=2, 3=2, 4=2, 5=2, 6=2, 7=2, 8=2, 9=2, 10=2
"ProficiencyRating" float: 9=40, 8=37, 10=33, 8..10

indexes: "StaffID", "SubjectID"
fk: "StaffID"→"Faculty"."StaffID", "SubjectID"→"Subjects"."SubjectID"

samples:
| column | latest | sample | sample |
|---|---|---|---|
| StaffID | 98064 | 98052 | 98045 |
| SubjectID | 41 | 17 | 23 |
| ProficiencyRating | 8 | 8 | 8 |

# "Majors"  (rows=7)

columns:
"MajorID" int PK: unique identifier, 1..7, avg=4, median=4
"Major" text: "Accounting"=1, "Art"=1, "English"=1, "General Studies"=1, "Information Sciences"=1, "Mathematics"=1, "Music"=1

indexes: none
fk: none

all rows:
| column | row 1 | row 2 | row 3 | row 4 | row 5 | row 6 | row 7 |
|---|---|---|---|---|---|---|---|
| MajorID | 1 | 2 | 3 | 4 | 5 | 6 | 7 |
| Major | General Studies | English | Music | Information Sciences | Accounting | Art | Mathematics |

# "Staff"  (rows=27)

columns:
"StaffID" int PK: unique identifier, 98005..98064, avg=98034.6, median=98036
"StfFirstName" text: 26 distinct
"StfLastname" text: "Patterson"=4, "Smith"=3, "Viescas"=3, "Hallmark"=2, "Abolrous"=1, "Black"=1, "Bonnicksen"=1, "Brehm"=1, "Brown"=1, "Coie"=1, "DeGrasse"=1, "Ehrlich"=1, "Glynn"=1, "Hernandez"=1, "Keyser"=1, "Rosales III"=1, "Sergienko"=1, "Waldal"=1, "Wilson"=1
"StfStreetAddress" text: 22 distinct
"StfCity" text: "Seattle"=4, "Bellevue"=3, "Tacoma"=3, "Fremont"=2, "Kirkland"=2, "Marysville"=2, "Portland"=2, "Redmond"=2, "Auburn"=1, "El Paso"=1, "Houston"=1, "Long Beach"=1, "Palm Springs"=1, "Salem"=1, "San Antonio"=1
"StfState" text: "WA"=17, "CA"=4, "OR"=3, "TX"=3
"StfZipCode" text: "98413"=3, "94538"=2, "97208"=2, "98006"=2, "98033"=2, "98052"=2, "98125"=2, "77201"=1, "78284"=1, "79993"=1, "90809"=1, "92263"=1, "97301"=1, "98002"=1, "98009"=1, "98106"=1, "98115"=1, "98270"=1, "98271"=1
"StfAreaCode" text: "425"=8, "253"=5, "206"=4, "503"=3, "510"=2, "210"=1, "562"=1, "713"=1, "760"=1, "915"=1
"StfPhoneNumber" text: all distinct
"Salary" float: 45000=6, 60000=5, 52000=3, 44000=2, 48000=2, 50000=2, 25000=1, 35000=1, 40000=1, 49000=1, 53000=1, 56000=1, 57000=1, 25000..60000
"DateHired" date: all distinct
"Position" text: "Faculty"=24, "Graduate Advisor"=1, "Registrar"=1, "Secretary"=1

indexes: "StfZipCode"
fk: none

samples:
| column | latest | sample | sample |
|---|---|---|---|
| StaffID | 98064 | 98057 | 98007 |
| StfFirstName | Luke | Joe | Gary |
| StfLastname | Patterson | Rosales III | Hallmark |
| StfStreetAddress | 877 145th Ave SE | 7288 Barrister Ave N | Route 2, Box 203B |
| StfCity | Portland | Tacoma | Auburn |
| StfState | OR | WA | WA |
| StfZipCode | 97208 | 98413 | 98002 |
| StfAreaCode | 503 | 253 | 253 |
| StfPhoneNumber | 555-2316 | 555-2281 | 555-2676 |
| Salary | 56000 | 35000 | 53000 |
| DateHired | 1989-08-20 | 1988-11-25 | 1985-01-21 |
| Position | Faculty | Graduate Advisor | Faculty |

# "Student_Class_Status"  (rows=3)

columns:
"ClassStatus" int PK: unique identifier, 1..3, avg=2, median=2
"ClassStatusDescription" text: "Completed"=1, "Enrolled"=1, "Withdrew"=1

indexes: none
fk: none

all rows:
| column | row 1 | row 2 | row 3 |
|---|---|---|---|
| ClassStatus | 1 | 2 | 3 |
| ClassStatusDescription | Enrolled | Completed | Withdrew |

# "Student_Schedules"  (rows=120)

columns:
"StudentID" int PK FK: 1001=7, 1003=7, 1004=7, 1005=7, 1006=7, 1007=7, 1008=7, 1009=7, 1011=7, 1012=7, 1013=7, 1014=7, 1015=7, 1016=7, 1017=7, 1018=7, 1002=4, 1010=4, 1001..1018
"ClassID" int PK FK: 32 distinct, 1000..6082, avg=3197.24, median=2907, 2907=10, 4180=9, 1156=8, 1000=7, 4196=7, 6082=6, 1180=5, 1500=5, 2500=5, 5917=4
"ClassStatus" int FK: 2=68, 1=50, 3=2, 1..3
"Grade" float: 68 distinct, 0..99.83, avg=46.359, median=68.78

indexes: none
fk: "ClassStatus"→"Student_Class_Status"."ClassStatus", "ClassID"→"Classes"."ClassID", "StudentID"→"Students"."StudentID"

samples:
| column | latest | sample | sample |
|---|---|---|---|
| StudentID | 1018 | 1014 | 1017 |
| ClassID | 5933 | 1180 | 4002 |
| ClassStatus | 1 | 2 | 1 |
| Grade | 0 | 88.91 | 0 |

# "Students"  (rows=19)

columns:
"StudentID" int PK: unique identifier, 1001..1019, avg=1010, median=1010
"StudFirstName" text: "Betsy"=1, "Brannon"=1, "Daffy"=1, "David"=1, "Doris"=1, "Elizabeth"=1, "George"=1, "Janice"=1, "John"=1, "Karen"=1, "Kendra"=1, "Kerry"=1, "Marianne"=1, "Michael"=1, "Richard"=1, "Sara"=1, "Sarah"=1, "Scott"=1, "Steve"=1
"StudLastName" text: "Bishop"=1, "Bonnicksen"=1, "Chavez"=1, "Dumbwit"=1, "Galvin"=1, "Hallmark"=1, "Hamilton"=1, "Hartwig"=1, "Jones"=1, "Kennedy"=1, "Lum"=1, "Patterson"=1, "Pundt"=1, "Sheskey"=1, "Smith"=1, "Stadick"=1, "Thompson"=1, "Viescas"=1, "Wier"=1
"StudStreetAddress" text: "16679 NE 41st Court"=2, "908 W. Capital Way"=2, "12330 Larchlemont Lane"=1, "15127 NE 24th, #383"=1, "2222 Springer Road"=1, "2500 Rosales Lane"=1, "281 Old Navy Road"=1, "30301 - 166th Ave. N.E."=1, "4110 Old Redmond Rd."=1, "4567 NE 32nd Ct"=1, "4726 - 11th Ave. N.E."=1, "611 Alpine Drive"=1, "66 Spring Valley Drive"=1, "754 Fourth Ave"=1, "777 Fenexet Blvd"=1, "9877 Hacienda Drive"=1, "Route 2, Box 203B"=1
"StudCity" text: "Seattle"=3, "Marysville"=2, "Portland"=2, "Redmond"=2, "Tacoma"=2, "Bellevue"=1, "Dallas"=1, "Eugene"=1, "Long Beach"=1, "Lubbock"=1, "Medford"=1, "Palm Springs"=1, "San Antonio"=1
"StudState" text: "WA"=10, "OR"=4, "TX"=3, "CA"=2
"StudZipCode" text: "97208"=2, "98052"=2, "98105"=2, "98413"=2, "75204"=1, "78284"=1, "79402"=1, "90809"=1, "92263"=1, "97401"=1, "97501"=1, "98002"=1, "98115"=1, "98270"=1, "98271"=1
"StudAreaCode" text: "206"=4, "253"=3, "425"=3, "503"=2, "541"=2, "210"=1, "562"=1, "760"=1, "806"=1, "972"=1
"StudPhoneNumber" text: "555-0399"=1, "555-2296"=1, "555-2521"=1, "555-2551"=1, "555-2566"=1, "555-2606"=1, "555-2621"=1, "555-2626"=1, "555-2656"=1, "555-2666"=1, "555-2671"=1, "555-2691"=1, "555-2696"=1, "555-2701"=1, "555-2706"=1, "555-2716"=1, "555-9872"=1, "555-9930"=1, "555-9938"=1
"StudGPA" float: 0=1, 72.225=1, 72.55=1, 74.465=1, 77.125=1, 77.65=1, 78.755=1, 79.25=1, 80=1, 80.25=1, 81=1, 83.55=1, 84.625=1, 85.235=1, 85.55=1, 86=1, 87.65=1, 88.5=1, 89.5=1, 0..89.5
"StudMajor" int FK: 2=3, 4=3, 6=3, 7=3, 1=2, 3=2, 5=2, nulls=1, 1..7

indexes: "StudAreaCode", "StudMajor", "StudZipCode"
fk: "StudMajor"→"Majors"."MajorID"

samples:
| column | latest | sample | sample |
|---|---|---|---|
| StudentID | 1019 | 1001 | 1016 |
| StudFirstName | Daffy | Kerry | Steve |
| StudLastName | Dumbwit | Patterson | Pundt |
| StudStreetAddress | 4567 NE 32nd Ct | 9877 Hacienda Drive | 2500 Rosales Lane |
| StudCity | Bellevue | San Antonio | Dallas |
| StudState | WA | TX | TX |
| StudZipCode | 98002 | 78284 | 75204 |
| StudAreaCode | 425 | 210 | 972 |
| StudPhoneNumber | 555-9872 | 555-2706 | 555-9938 |
| StudGPA | 0 | 74.465 | 77.125 |
| StudMajor | null | 1 | 4 |

# "Subjects"  (rows=56)

columns:
"SubjectID" int PK: unique identifier, 1..56, avg=28.5, median=28.5
"CategoryID" text FK: "ART"=6, "ACC"=5, "BUS"=5, "MAT"=5, "CIS"=4, "MUS"=4, "PHY"=4, "BIO"=3, "CHE"=3, "ECO"=3, "ENG"=3, "HIS"=3, "POL"=3, "CSC"=2, "GEG"=2, "JRN"=1
"SubjectCode" text UNIQ: unique identifier
"SubjectName" text: all distinct
"SubjectPreReq" text FK: "ACC 220"=3, "ACC 210"=1, "BUS 170"=1, "ENG 101"=1, "MAT 098"=1, "MUS 101"=1, "PHY 201"=1, nulls=47
"SubjectDescription" text: all distinct

indexes: "CategoryID", "SubjectPreReq"
fk: "CategoryID"→"Categories"."CategoryID", "SubjectPreReq"→"Subjects"."SubjectCode"

samples:
| column | latest | sample | sample |
|---|---|---|---|
| SubjectID | 56 | 19 | 47 |
| CategoryID | POL | BIO | MAT |
| SubjectCode | POL 213 | BIO 280 | MAT 098 |
| SubjectName | Women and Politics | Microbiology | Intermediate Algebra |
| SubjectPreReq | null | null | null |
| SubjectDescription | Introduction to concepts of power and policy issues as they relate to women. Theoretical, historical and empirical studies of women's participation in social and political movements nationally and internationally. Study of women's diverse roles in relations to family, economics, labor, government, and law. | Introduction to micro-organisms including microbial cell structure and function; metabolism; microbial genetics; and the role of micro-organisms in disease, immunity, and other selected applied areas. | Sets and the real number system, polynomial and rational expressions, exponents and radicals, first and second degree equations, linear systems of equations, and graphs. |
