# Schema Links

- version: 0.0.5
- dialect: sqlite
- database: file:/Users/renatyuldashev/Documents/ai-sql/custom-bench/data/bird_mini_dev/databases/dev_databases/debit_card_specializing/debit_card_specializing.sqlite
- schema: main

## Declared PK/FK Links

yearmonth.CustomerID -> customers.CustomerID

## Inferred Links

### gasstationid
- inferred: gasstations.GasStationID, transactions_1k.GasStationID

### productid
- inferred: products.ProductID, transactions_1k.ProductID
