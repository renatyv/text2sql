# Schema Links

- version: 0.0.5
- dialect: sqlite
- database: file:/Users/renatyuldashev/Documents/ai-sql/custom-bench/data/sp2_lite_sqlite/databases/school_scheduling.sqlite
- schema: main

## Declared PK/FK Links

Class_Rooms.BuildingCode -> Buildings.BuildingCode
Classes.ClassRoomID -> Class_Rooms.ClassRoomID
Classes.SubjectID -> Subjects.SubjectID
Departments.DeptChair -> Staff.StaffID
Faculty.StaffID -> Staff.StaffID
Faculty_Categories.CategoryID -> Categories.CategoryID
Faculty_Categories.StaffID -> Faculty.StaffID
Faculty_Classes.ClassID -> Classes.ClassID
Faculty_Classes.StaffID -> Staff.StaffID
Faculty_Subjects.StaffID -> Faculty.StaffID
Faculty_Subjects.SubjectID -> Subjects.SubjectID
Student_Schedules.ClassID -> Classes.ClassID
Student_Schedules.ClassStatus -> Student_Class_Status.ClassStatus
Student_Schedules.StudentID -> Students.StudentID
Students.StudMajor -> Majors.MajorID
Subjects.CategoryID -> Categories.CategoryID
Subjects.SubjectPreReq -> Subjects.SubjectCode

## Inferred Links

### departmentid
- inferred: Categories.DepartmentID, Departments.DepartmentID

### shared values
- inferred: Staff.StfState, Students.StudState
