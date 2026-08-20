# Schema Links

- version: 0.0.5
- dialect: sqlite
- database: file:/Users/renatyuldashev/Documents/ai-sql/custom-bench/data/sp2_lite_sqlite/databases/northwind.sqlite
- schema: main

## Declared PK/FK Links

No declared PK/FK links found.

## Inferred Links

### employeeid
- inferred: employees.employeeid, employeeterritories.employeeid, orders.employeeid

### categoryid
- inferred: categories.categoryid, products.categoryid

### customerid
- inferred: customers.customerid, orders.customerid

### orderid
- inferred: order_details.orderid, orders.orderid

### productid
- inferred: order_details.productid, products.productid

### regionid
- inferred: region.regionid, territories.regionid

### shared values
- inferred: customers.postalcode, orders.shippostalcode

### supplierid
- inferred: products.supplierid, suppliers.supplierid

### territoryid
- inferred: employeeterritories.territoryid, territories.territoryid
