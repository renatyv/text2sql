# Additional Metadata

## Clarified Semantics

- `Staff` is a superset table: `Position` partitions it into Faculty (24), plus non-teaching roles (Graduate Advisor, Registrar, Secretary). `Faculty` is the teaching subset.
- `Faculty_Categories` vs `Faculty_Subjects`: the former links staff to broad teaching *categories* (e.g. MAT); the latter links staff to specific *subjects* and carries a `ProficiencyRating` (8–10). `Faculty_Classes` is the actual assigned teaching workload (which staff member teaches which class instance).
- `Subjects.SubjectPreReq` is a self-referencing FK that points at `SubjectCode` (text), not `SubjectID`. Only 9 of 56 subjects have a listed prerequisite; most are null.
- `Categories.DepartmentID ↔ Departments.DepartmentID` is an inferred value link (not a declared FK), grouping categories (disciplines) under one of 5 departments.
- There is no direct Class→Building key: a class reaches its building only through `Classes.ClassRoomID → Class_Rooms → Buildings`.
- `Student_Schedules.ClassID` touches only 32 distinct class IDs while `Classes` has 147 — most classes have no student enrollments.
- `Grade = 0` in `Student_Schedules` is the sentinel for not-yet-completed/missing grade (statuses Enrolled/Withdrew, 52 of 120 combos have non-Completed status).
- `StartDate` encodes two term cohorts (2017-09 and 2018-01).
- `ProficiencyRating` values are 8/9/10 only, so it encodes a coarse skill tier rather than a continuous scale.
- `Students.StudMajor` has 1 null student; not every student is assigned a major.

## Potential Join Strategies

- **Class → Subject → Category → Department**: join `Classes.SubjectID → Subjects.SubjectID`, then `Subjects.CategoryID → Categories.CategoryID`, then `Categories.DepartmentID = Departments.DepartmentID` (inferred). Useful for counting classes per department; cardinality many classes→1 subject→1 category.
- **Building assignment for classes**: `Classes.ClassRoomID → Class_Rooms.ClassRoomID`, then `Class_Rooms.BuildingCode → Buildings.BuildingCode`. Rows fan out ~multiple classes per room (up to 12) per building; includes `BuildingCode` and `NumberOfFloors`.
- **Instructor teaching a class**: `Classes.ClassID → Faculty_Classes.ClassID`, then `Faculty_Classes.StaffID → Staff.StaffID`. Filter by semester/day via `Classes` columns; not every class has an assigned instructor (Faculty_Classes covers 145 vs 147 classes).
- **Who can teach a subject (suitability)**: `Subjects.SubjectID → Faculty_Subjects.SubjectID → Faculty`. Join carries `ProficiencyRating`; distinct staff per subject is thin (about 2 per subject), so detection/suits queries need care.
- **Faculty ↔ broad discipline**: join `Faculty_Subjects`/`Faculty_Classes` back through `Faculty_Categories` (via shared StaffID) to relate staff to both specific subjects and category-level areas.
- **A student's full schedule with instructors/rooms**: `Students.StudentID → Student_Schedules.StudentID → Classes.ClassID → Faculty_Classes → Staff`, plus Class_Rooms/Buildings branch. Caveat: a student has up to 7 schedule rows; use ClassStatus to filter Enrolled vs Completed.
- **Student class outcomes**: `Student_Schedules.ClassStatus → Student_Class_Status.ClassStatus` to separate Enrolled/Completed/Withdrew; `Grade` only meaningful for status 2 (Completed), otherwise 0.
- **Prerequisite chains**: self-join `Subjects` on `SubjectPreReq = SubjectCode` to build subject dependency lists; limited by the 9 non-null prerequisites.
- **Geographic overlap (inferred value link)**: join `Staff.StfState = Students.StudState` for state-level staff/student distribution; this is a value coincidence (both use WA/OR/CA/TX) not an ID FK, so it is only meaningful as an aggregate grouping.
- **Join on `Majors`**: `Students.StudMajor → Majors.MajorID` for enrollment by declared major; null `StudMajor` rows are excluded in inner joins.