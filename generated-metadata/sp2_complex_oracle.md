# Additional Metadata

## Clarified Semantics

- `sales` (≈918,843 rows) has no index; `quantity_sold` is always `1` and `amount_sold` equals the per-unit price actually charged, matching `costs.unit_price` for the same key set.
- `profits` is a view = `costs` joined to `sales` on the four-part composite key (prod_id, time_id, channel_id, promo_id). Use it as a shortcut instead of re-joining `costs`+`sales`. Its `TOTAL_COST` = `unit_cost * quantity_sold`.
- `customers` is a slowly-changing-dimension table: `cust_valid` `'A'` = Active, `'I'` = Inactive. All sales reference Active customers (every one of the 918,843 sales joins to `cust_valid='A'`); time-banding via `cust_eff_from`/`cust_eff_to`.
- `supplementary_demographics.cust_id` covers only the 100001..104500 range (4,500 rows) — a subset of `customers` carrying extra attributes (education, occupation, household_size, hobby flags).
- `currency.to_us`: only Canada has a real FX rate (`0.74`, exactly 36 rows = 1 country × 3 years × 12 months); every other country is the placeholder `1.0`. Not a true multi-currency-conversion table.
- `currency.country` is free-form text and does not always equal `countries.country_name` (the US row is the truncated `"United States of Ame"` vs `countries` `"United States of America"`). Names match for most other countries.
- `promotions.promo_id = 999` is the `"NO PROMOTION"` sentinel (dominates, e.g. 78,425/82,112 cost rows); its `promo_begin/end_date = 9999-01-01` are sentinel values.
- `channels.channel_id = 9` ("Tele Sales") is far rarer in facts than ids 2–4.
- `times` carries BOTH calendar and fiscal dimensions; they differ (e.g. `fiscal_year` extends to 2024 with 2 rows, fiscal months can span 25–35 days). Pick either all-calendar or all-fiscal per query.
- `countries` has region/subregion hierarchy columns and sentinel total rows; normal country_id range is 52769..52791 (35 countries).
- MVs pre-aggregate facts: `cal_month_sales_mv` (48 rows) by `times.calendar_month_desc`; `fweek_pscat_sales_mv` (3,652 rows) by week, product subcategory, channel, promo.

## Potential Join Strategies

- `costs`↔`sales`: must match on ALL FOUR keys (prod_id, time_id, channel_id, promo_id) because both are composite fact tables; joining on fewer keys fan-outs/multiplies rows. Prefer the `profits` view which encodes this.
- `sales`→`customers` on `cust_id` (FK, 1:1 per sale; note `customers` has no index, so expect per-row lookups).
- `sales`/`costs`→`times` on `time_id` (FK); reduce fan-out by aggregating on `times.week_ending_day`, `calendar_month_id`, or fiscal equivalents (1,826 time rows vs ~918k sales).
- `products` (24), `channels` (5), `promotions` (503) are small dimensions — use for filtering/grouping with cheap joins (FKs prod_id, channel_id, promo_id).
- `customers`→`countries` on `country_id` (FK) for geographic rollups.
- `currency`→`times`: link by exact `year`=calendar/fiscal_year and `month`=calendar_month_number; `currency`→`countries` only via approximate country-name text match (cardinality caveat: the US name is truncated and won't match, so prefer year+month aggregation over name-based joins).
- `supplementary_demographics`→`customers` on `cust_id` for demographic segmentation; only ~4,500 customers have these attributes, so other customers appear as no-join (inner joins shrink the population).
- Filter `promotions` excluding sentinel `promo_id=999` / `promo_category_id=2` before promotion-level aggregates to drop the dominant "NO PROMOTION" mass.