# Additional Metadata

## Clarified Semantics

- `transactions_1k` is the only transaction/fact table (no full `transactions` table exists; name carries a "1k" sample suffix).
- `transactions_1k.Amount` is a quantity/volume (integer, mostly small values), while `transactions_1k.Price` is monetary value (real); they are distinct attributes, not synonyms.
- `transactions_1k` data covers only 4 days (2012-08-23 … 2012-08-26); `Date` is a `YYYY-MM-DD` literal.
- `yearmonth.Date` is a `YYYYMM` text period key (e.g. `201207`), *not* a full date — differing format from `transactions_1k.Date`.
- `yearmonth.Consumption` is a float (monthly consumption value); the PK is composite on `(Date, CustomerID)`.
- `products.Description` holds textual product names/categories; `ProductID` is essentially a dimension key (529 distinct descriptions vs 591 IDs).
- `gasstations.Country` values are CZE/SVK; `gasstations.Segment` is a qualitative station class (Premium/Other/Discount/etc.), distinct from `customers.Segment`.
- `customers.Currency` is CZK or EUR; `customers.Segment` is SME/LAM/KAM (unrelated to gasstation segment).
- No FK is declared from `transactions_1k` to any dimension table; links to `gasstations`, `products`, and `customers` rely on inferred reference keys.

## Potential Join Strategies

- **customers ↔ transactions_1k** on `customers.CustomerID = transactions_1k.CustomerID`. Many-to-one (transactions reference one customer); joins will multiply customer rows by their transaction count, so aggregate on `customers` side — custom caveats: `transactions_1k` only covers customers who transacted in those 4 days.
- **transactions_1k ↔ gasstations** on `transactions_1k.GasStationID = gasstations.GasStationID` (inferred link). Many-to-one; cardinality ~437 distinct GasStationIDs appear in the transactions sample vs 5716 stations, so many stations have no transactions.
- **transactions_1k ↔ products** on `transactions_1k.ProductID = products.ProductID` (inferred link). Many-to-one; only 28 distinct ProductIDs appear in the transactions sample, so most of the 591 products are unreferenced.
- **customers ↔ yearmonth** on `customers.CustomerID = yearmonth.CustomerID` (declared FK). One-to-many (one customer has many monthly rows). Composite time keys: if linking `yearmonth` to `transactions_1k` by calendar month, normalize `transactions_1k.Date` (YYYY-MM-DD) to `YYYYMM` to match `yearmonth.Date`.