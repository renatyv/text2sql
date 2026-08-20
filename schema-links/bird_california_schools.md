# Schema Links

- version: 0.0.5
- dialect: sqlite
- database: file:/Users/renatyuldashev/Documents/ai-sql/custom-bench/data/bird_mini_dev/databases/dev_databases/california_schools/california_schools.sqlite
- schema: main

## Declared PK/FK Links

frpm.CDSCode -> schools.CDSCode
satscores.cds -> schools.CDSCode

## Inferred Links

### county
- inferred: frpm."County Name", satscores.cname, schools.County

### district
- inferred: frpm."District Name", satscores.dname, schools.District

### school
- inferred: frpm."School Name", satscores.sname, schools.School
