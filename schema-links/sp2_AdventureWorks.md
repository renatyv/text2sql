# Schema Links

- version: 0.0.5
- dialect: sqlite
- database: file:/Users/renatyuldashev/Documents/ai-sql/custom-bench/data/sp2_lite_sqlite/databases/AdventureWorks.sqlite
- schema: main

## Declared PK/FK Links

No declared PK/FK links found.

## Inferred Links

### productsubcategoryid
- inferred: product.productsubcategoryid, productcategory.productcategoryid, productsubcategory.productcategoryid, productsubcategory.productsubcategoryid

### currencyrate
- inferred: countryregioncurrency.currencycode, currencyrate.fromcurrencycode, currencyrate.tocurrencycode

### territoryid
- inferred: salesorderheader.territoryid, salesperson.territoryid, salesterritory.territoryid

### businessentityid
- inferred: SalesPersonQuotaHistory.BusinessEntityID, salesperson.businessentityid

### currencyrateid
- inferred: currencyrate.currencyrateid, salesorderheader.currencyrateid

### productdescriptionid
- inferred: productdescription.productdescriptionid, productmodelproductdescriptionculture.productdescriptionid

### productmodelid
- inferred: product.productmodelid, productmodelproductdescriptionculture.productmodelid
