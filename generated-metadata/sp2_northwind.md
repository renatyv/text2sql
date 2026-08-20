# Additional Metadata

## Clarified Semantics

- `employees.reportsto` is a self-reference to `employees.employeeid` (manager hierarchy); the lone NULL row is the top manager (employeeid 2).
- `categories.picture`, `employees.photo`, and `suppliers.homepage` are stored binary/URL-ish blobs; not usable for textual matching.
- `orders.shipvia ∈ {1,2,3}` maps only to the first three shippers; `shippers` contains 6 rows (ids 4-6 are unused/legacy), so joining by id is safe but shipvia only ever reaches 1-3.
- `orders.ship*` columns describe the actual shipping destination and may differ from the ordering `customers` address (e.g., consolidated/shippable city), so customer country/region is not guaranteed to equal shipcountry/shipregion.
- `customergroupthreshold` defines spend bands as inclusive ranges (`rangebottom..rangetop`); "Very High" uses a sentinel top (≈9.22e14, i.e., open-ended) rather than a real bound. Bands are Low [0,1000), Medium [1000,5000), High [5000,10000), Very High ≥10000.
- `region` (4 broad descriptions, e.g., Eastern/Western) is a separate taxonomy from `usstates.stateregion` (5 divisions of US states: east/midwest/west/south/north); do not equate these two.
- `territories.regionid` ranges 1..4 referencing the `region` table; `territories.territoryid` is a digit string, so join/compare as text, not integer.
- `customergroupthreshold`, `customercustomerdemo`/`customerdemographics` and `usstates` have no FK to other tables (the two customer_* tables are empty); they are reference/enrichment tables.

## Potential Join Strategies

- **Employee→Territory→Region chain**: `employeeterritories.employeeid = employees.employeeid`, then `employeeterritories.territoryid = territories.territoryid`, then `territories.regionid = region.regionid`. Many-to-many (49 rows); an employee may span several territories and regions.
- **Order lines to product catalog / pricing**: `order_details.orderid = orders.orderid` and `order_details.productid = products.productid`; note `order_details.unitprice` is a snapshot price that can differ from `products.unitprice`.
- **Product categorization/sourcing**: `products.categoryid = categories.categoryid` and `products.supplierid = suppliers.supplierid` (only 29 suppliers, so many products per supplier).
- **Order→customer and order→employee**: `orders.customerid = customers.customerid` and `orders.employeeid = employees.employeeid`; customerid is text, employeeid int.
- **Freight/shipping**: `orders.shipvia = shippers.shipperid` — restrict to ids 1..3; avoids the two idle shipper rows.
- **Ship-to vs customer address (shared postal values)**: `orders.shippostalcode = customers.postalcode` matches on shipping geography, but is only meaningful where both share the same region/country (region/country mismatches common; many nulls in both). Treat as enrichment, not a key.
- **Customer spend banding**: `customergroupthreshold` has no key; classify each customer/order amount by `rangebottom <= amount < rangetop` (or `<= rangetop` given the sentinel), a range-membership join rather than equality.
- **Manager hierarchy**: self-join `employees.reportsto = employees.employeeid` to build the org tree; the root has NULL reportsto.
- **Region-based territory summaries**: `territories.regionid = region.regionid`, optionally to `employeeterritories` for coverage of a `region`'s territories by employees.