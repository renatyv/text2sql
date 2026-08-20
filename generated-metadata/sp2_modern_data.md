# Additional Metadata

## Clarified Semantics

- The database is a concatenation of unrelated sub-datasets: a company-universe bank, an NYC street-tree census, a ZIP-level income dataset, US COVID state statistics, and the pizza orders case.
- `pizza_*_orders` (raw) vs `pizza_clean_*_orders` (cleaned): both have identical row counts; the raw variants store `distance`/`duration` as text strings ("20km", "32 minutes"), while the clean variants hold numeric values. `pizza_clean_runner_orders` null `pickup_time`/`distance`/`duration` rows correspond to cancelled (Restaurant/Customer) orders.
- `pizza_get_exclusions` / `pizza_get_extras` denormalize the comma-delimited `exclusions`/`extras` text in `pizza_customer_orders`. Fields `row_id`, `total_exclusions`, `extras_count` group how many distinct rows/items belong to one order's exclusion or extra set.
- `pizza_recipes.toppings` is a comma-space-delimited list of `pizza_toppings.topping_id` values (no foreign key); `pizza_names` maps `pizza_id` 1=Meatlovers, 2=Vegetarian.
- `trees` is a ~690k-row NYC street-tree census: `status` is Alive/Dead (with a small tail of other values), `health` is Good/Fair/Poor, and `spc_common` may be empty for some rows. It contains only ~191 distinct NYC zipcodes and `borocode`/`boroname`/`nta_name` location attributes.
- `income_trees` is ACS-style income data keyed by zipcode, with paired Estimate/Margin-of-Error columns (Total, Median_income, Mean_income).
- `companies_dates.date_joined` is a full timestamp (ISO), while `year_founded` is an integer year; `companies_dates` and `companies_funding` `company_id` have repeated values (many-to-one per company), not a unique key.

## Potential Join Strategies

- `trees.zipcode` ↔ `income_trees.zipcode`: per-ZIP income context for each tree record. Caveat: `income_trees` holds 216 distinct zipcodes covering NYC generally, while `trees` covers only ~191; many tree rows share one zipcode, so expect a many-to-one fan-out and possible missing income rows for some tree zips.
- `pizza_customer_orders` ↔ `pizza_clean_customer_orders` on `order_id` (and `customer_id`): the raw and cleaned order sets carry the same order rows, so they join row-for-row by `order_id` when both populated. Use one as the join driver to avoid double counting.
- `pizza_runner_orders` ↔ `pizza_clean_runner_orders` on `order_id`: same 10 orders, with the raw side producing unclean numeric distance/duration text; prefer the clean side when computing distances/durations.
- `pizza_customer_orders.order_id` ↔ `pizza_runner_orders.order_id` ↔ `pizza_runners.runner_id` via runner_orders: pairs ordered pizzas with the delivery runner (many pizzas per order, one runner per order). Caveat: cancelled orders have null pickup_time; join `pizza_runners` on `runner_id` for registration context (runner 4 has no deliveries).
- `pizza_customer_orders.exclusions`/`extras` (comma text) ↔ `pizza_get_exclusions`/`pizza_get_extras` on `order_id`: exploded lookup for per-topping exclusion/extras analysis, matched back to `pizza_toppings.topping_id` and `pizza_names.pizza_id` for names.
- `pizza_clean_customer_orders.pizza_id` ↔ `pizza_names.pizza_id` and `pizza_recipes.pizza_id`: assigns pizza names and base topping sets to each ordered pizza; join `pizza_recipes.toppings` to `pizza_toppings` by splitting the delimited list (not a direct key equality).
- `companies_dates.company_id`, `companies_funding.company_id`, `companies_industries.company_id`: all keyed on the same `company_id` with repeated per-company rows, so joins on `company_id` produce a many-to-many expansion of industries/funding dates unless grouped to one row per company first.