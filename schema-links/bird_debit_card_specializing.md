# Schema Links

- generator: local introspection
- dialect: sqlite
- database: debit_card_specializing

## Declared Links

- `yearmonth.CustomerID` → `customers.rowid`
- `yearmonth.CustomerID` → `customers.rowid`

## Same-name Candidates

- `CustomerID`: `customers.CustomerID`, `transactions_1k.CustomerID`, `yearmonth.CustomerID`
- `Date`: `transactions_1k.Date`, `yearmonth.Date`
- `GasStationID`: `gasstations.GasStationID`, `transactions_1k.GasStationID`
- `ProductID`: `products.ProductID`, `transactions_1k.ProductID`
- `Segment`: `customers.Segment`, `gasstations.Segment`
