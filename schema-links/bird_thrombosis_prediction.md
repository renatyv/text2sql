# Schema Links

- version: 0.0.5
- dialect: sqlite
- database: file:/Users/renatyuldashev/Documents/ai-sql/custom-bench/data/bird_mini_dev/databases/dev_databases/thrombosis_prediction/thrombosis_prediction.sqlite
- schema: main

## Declared PK/FK Links

Examination.ID -> Patient.ID
Laboratory.ID -> Patient.ID

## Inferred Links

### date
- inferred: Examination."Examination Date", Laboratory.Date, Patient."First Date"
