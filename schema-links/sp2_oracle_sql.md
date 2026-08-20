# Schema Links

- version: 0.0.5
- dialect: sqlite
- database: file:/Users/renatyuldashev/Documents/ai-sql/custom-bench/data/sp2_lite_sqlite/databases/oracle_sql.sqlite
- schema: main

## Declared PK/FK Links

customer_favorites.customer_id -> customers.id
customer_reviews.customer_id -> customers.id
emp_hire_periods.emp_id -> employees.id
employees.supervisor_id -> employees.id
id_name_coll_entries.collection_id -> id_name_coll_type.collection_id
inventory.location_id -> locations.id
inventory.product_id -> products.id
inventory.purchase_id -> purchases.id
monthly_budget.product_id -> products.id
monthly_sales.product_id -> products.id
orderlines.order_id -> orders.id
orderlines.product_id -> products.id
orders.customer_id -> customers.id
packaging_relations.contains_id -> packaging.id
packaging_relations.packaging_id -> packaging.id
picking_line.location_id -> locations.id
picking_line.order_id -> orders.id
picking_line.picklist_id -> picking_list.id
picking_line.product_id -> products.id
picking_list.picker_emp_id -> employees.id
picking_log.location_id -> locations.id
picking_log.picklist_id -> picking_list.id
picking_log.picklist_id, picking_log.pickline_no -> picking_line.picklist_id, picking_line.line_no
product_alcohol.product_id -> products.id
product_minimums.product_id -> products.id
products.group_id -> product_groups.id
purchases.brewery_id -> breweries.id
purchases.product_id -> products.id
ticker.symbol -> stock.symbol
web_counter_hist.app_id, web_counter_hist.page_no -> web_pages.app_id, web_pages.page_no
web_page_visits.app_id, web_page_visits.page_no -> web_pages.app_id, web_pages.page_no
web_pages.app_id -> web_apps.id

## Inferred Links

All inferred links are implied by the declared PK/FK links above.
