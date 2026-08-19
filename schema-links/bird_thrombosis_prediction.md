# Schema Links

- generator: local introspection
- dialect: sqlite
- database: thrombosis_prediction

## Declared Links

- `Examination.ID` → `Patient.ID`
- `Laboratory.ID` → `Patient.ID`

## Same-name Candidates

- `Diagnosis`: `Examination.Diagnosis`, `Patient.Diagnosis`
- `ID`: `Examination.ID`, `Laboratory.ID`, `Patient.ID`
