# Additional Metadata

## Clarified Semantics

- **SalaryDataset**: `JobTitle` is coarse (only 26 distinct values), not individual job postings; it groups rows by role type. `SalariesReported` appears to be a count/percentage (1..105, median 1), not a monetary amount. `Salary` is freeform text (currency strings with `₹`, `/mo` or `/yr` suffixes, e.g. `₹12,00,000/yr`) and is not directly numeric; it must be parsed/procured before aggregation. `CompanyName` has 3 nulls and is not linked to any other table.
- **StaffHours**: a time-punch log per staff member (single-letter `StaffMember` codes, `Enter`/`Exit` event types). It has no joining key to `SalaryDataset`/`CompanyName`; staff members are not company employees in any linked table.
- **hardware_fact_sales_monthly**: the core fact/transaction table (~971k rows), one recurrence per date+product+customer; it records sold_quantity but no monetary amount (amounts live in separate fact tables). Covers fiscal_years 2020 (363k) and 2021 (608k).
- **hardware_fact_gross_price / hardware_fact_manufacturing_cost**: both 579 rows keyed by product_code + year (347 distinct products), but `gross_price` and `manufacturing_cost` do not both exist for every product_year — coverage differs, so joins need left handling.
- **hardware_fact_pre_invoice_deductions**: exactly one row per customer_code × fiscal_year (209 customers × 2 years = 418 rows, all unique); it is customer-year level, not order-level.
- **university_offering.FacNo** is nullable (2 nulls, i.e. offerings without assigned instructor) and is stored as float alongside the int `university_faculty.FacNo`.
- **university_faculty.FacSupervisor** is a self-referencing manager link to `FacNo` (2 nulls for top-level faculty).
- **web_orders.account_id** references 350 of the 351 accounts (one account has no orders); **web_events.account_id** covers all 351 accounts.

## Potential Join Strategies

- **hardware product-year price vs cost**: `hardware_fact_gross_price.product_code` + `fiscal_year` → `hardware_fact_manufacturing_cost.product_code` + `cost_year`, comparing gross price to manufacturing cost per product per year. Both have 579 rows; use LEFT JOIN as per-product year coverage differs between the two fact tables.
- **hardware sales → product dim**: `hardware_fact_sales_monthly.product_code` → `hardware_dim_product.product_code` (each sale to its division/segment/category). 347 distinct products present in both fact and dim.
- **hardware sales → customer dim**: `hardware_fact_sales_monthly.customer_code` → `hardware_dim_customer.customer_code`, to attribute quantities by region/channel/platform/market.
- **hardware customer-year discounts**: `hardware_fact_pre_invoice_deductions.customer_code` + `fiscal_year` → `hardware_dim_customer`, and to `sales_monthly` by customer_code+fiscal_year (discounts apply to all of that customer's sales in that year; 209×2 unique pairs form the join key).
- **web accounts hub**: `web_orders.account_id` and `web_events.account_id` → `web_accounts.id` (account ids in 1001–4501). All 351 accounts appear in events; only 350 have orders — LEFT JOIN from accounts to orders to include accounts with no orders.
- **web sales rep/region**: `web_accounts.sales_rep_id` → `web_sales_reps.id`, then `web_sales_reps.region_id` → `web_region.id` (4 regions), for regional aggregation of orders/events per account.
- **university enrollment hub**: `university_enrollment.OfferNo` → `university_offering.OfferNo` and `university_enrollment.StdNo` → `university_student.StdNo` (many-to-many, 37 enrollments).
- **university offering → course/faculty**: `university_offering.CourseNo` → `university_course.CourseNo`; `university_offering.FacNo` → `university_faculty.FacNo` — filter out the 2 NULL FacNo rows unless instructorless offerings are to be included.
- **faculty manager hierarchy**: self-join `university_faculty.FacSupervisor` → `university_faculty.FacNo` (supervisor has no supervisor, 2 at top).