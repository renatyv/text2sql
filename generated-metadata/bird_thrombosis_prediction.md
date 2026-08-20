# Additional Metadata

## Clarified Semantics

- **Patient.Diagnosis** uses shorthand disease codes: SLE (systemic lupus erythematosus), SJS/SjS (Sjögren syndrome), RA (rheumatoid arthritis), PSS (progressive systemic sclerosis), MCTD, APS (antiphospholipid syndrome), BEHCET. Suffixes `susp` mark a provisional/suspected diagnosis, and a comma list means multiple diagnoses.
- **Patient.Admission** is a flag field: `-` (not admitted, 713) vs `+` (admitted, 488), with some blanks/`+(` (partial). It is not free text.
- **Patient.Description** is a date (diagnosis/record date), not a text description; it is sparse (97 distinct, 216 nulls).
- **Patient."First Date"** is the patient's first monitored/visit date; its values overlap the date domain used by other tables.
- **Laboratory** has a composite primary key `(ID, Date)`; a patient (302 distinct IDs) has many dated lab-draw rows, so the Lab table is the long-format "many" side.
- **Examination** is the sparse (106-row) immunology/serology "one" side; many fields (`Symptoms`, `KCT`, `RVVT`, `LAC`, `ANA Pattern`) are largely NULL. `Thrombosis` is a coded outcome (0–3), with 0 the dominant value; `Symptoms` and `Diagnosis` are free-text in this table.
- **Laboratory.DNA-II** is entirely NULL and can be ignored. `DNA` is stored as text despite numeric semantics. `CRP`, `RA`, `RF`, `U-PRO` are text, with `U-PRO` using mixed qualitative (`-`, `TR`, `+1(30)`) and numeric-ish encodings, so caution is needed when treating them as numeric.
- `aCL IgG`/`aCL IgM` are float titers; `ANA` is an integer titer (0..4096) separate from the text `ANA Pattern`. `LAC`, KCT, RVVT, and `Symptoms` are all coagulation/symptom fields mostly missing.
- No indexes exist beyond the PK/FK columns; all FKs point to `Patient.ID` (`Examination.ID` and `Laboratory.ID`). Only ~20 patients appear in both `Laboratory` and `Examination`.

## Potential Join Strategies

- **Patient → Laboratory**: `Laboratory.ID = Patient.ID`. This is 1-to-many (13908 rows over 302 patients); no unique key besides `(ID, Date)`, so joining yields duplicate ID rows — always join with the lab `Date` context or aggregate (`MIN/MAX/...`) to avoid fan-out.
- **Patient → Examination**: `Examination.ID = Patient.ID` is 1-to-1-in-practice (69/1238 patients; 106 rows, 36 nulls in Exam ID), so a plain join naturally filters to examined patients.
- **Bridge through Patient**: `Laboratory.ID = Examination.ID` (via `Patient`) is a **many-to-many** ("Lab/Exam") mediated by the patient hub; it links only 20 patients, so results are tiny and resemble the outcome others.
- **Time-based linking**: `Laboratory, Date`, `Examination."Examination Date"`, and other dates are all links (see schema-links), so a strategy link visit-level labs with examinations/`Description` around the same exam window (e.g., aggregate labs per patient before the Examination Date to the closest `First Date`). Because the lab record count per patient can be large, apply the `Date` predicate before joining to control result cardinality.