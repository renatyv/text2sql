# Additional Metadata

## Clarified Semantics

- `foreign_keys` pragma is OFF (0) in this SQLite file; referential integrity is implied by the declared PK/FK links but not enforced by the engine.
- `address.district` and `address.phone` are not NULL but all equal a single space `" "`; `address.address2` is NULL for every row. These are effectively placeholder/filler fields, not real data.
- `film.release_year` is uniformly `"2006"` (stored as varchar4).
- `film.language_id` is `1` (= English) for all 1000 films; `film.original_language_id` is NULL for every row, so the `original_language_id` FK is never usable.
- `rental.return_date` is NULL for 183 rows (outstanding/unreturned rentals); all other rentals have a return date.
- `payment.rental_id` has 5 NULL rows (payments not tied to a rental record).
- `payment.amount` includes a 0-valued set (24 rows) and fractional/odd amounts (e.g. 3.98, 5.98), implying special price/credit cases distinct from the standard `film.rental_rate` tiers (0.99/2.99/4.99).
- `rental` (16044 rows) and `payment` (16049 rows) have similar but not identical row counts; rental_id keys present in payment are all valid rental_ids.
- `staff.picture` is NULL for all 2 staff; `staff.password` is redacted.
- `film_text` is an empty table (skipped in the profile).
- Built-in views exist: `customer_list`, `film_list`, `sales_by_film_category`, `sales_by_store`, `staff_list`.

## Potential Join Strategies

- **Sales per film (no direct film↔rental link):** join `payment.rental_id` → `rental.rental_id` → `rental.inventory_id` → `inventory.inventory_id` → `inventory.film_id` → `film.film_id`. This is the only path from film to revenue; a film reachable only through inventory.
- **Geography chain (customer/staff/store to country):** `customer.address_id` → `address.city_id` → `city.country_id` → `country.country_id`; the same `address→city→country` pattern applies to `staff.address_id` and `store.address_id`.
- **Category membership:** `film.film_id` → `film_category.film_id` → `category.category_id`. `film_category` has exactly 1000 rows (each film appears once: `film_id` unique), so it is a 1:1 enrichment from film to category with no fan-out.
- **Actor membership (many-to-many fan-out):** `actor.actor_id` → `film_actor` → `film.film_id`. `film_actor` has 5462 rows across 200 actors / 997 films; joining film to actor via `film_actor` multiplies rows by the number of actors per film (up to 15).
- **Store-level grouping:** `inventory.store_id` → `store.store_id` is the way to attach rentals/payments to a store; `store.manager_staff_id` → `staff.staff_id` gives the manager. Note `customer.staff_id` does not exist — sales attribution to staff is via `payment.staff_id`/`rental.staff_id`, not through the store.
- **Staff vs rental staff:** join `payment.rental_id` → `rental.rental_id` to compare `payment.staff_id` and `rental.staff_id`; the two can differ (staff processed the payment vs. staff who processed the rental), so don't assume they always match.
- **Coverage caveats for rentals/sales:** only 958 of 1000 films have `inventory` and 997 have `film_actor` entries; films without inventory copies can never appear in rental/payment aggregation. Left-join from `film` (or `inventory`) when completeness of the film list matters.
- **`payment.rental_id` NULL handling:** for payment-to-rental joins, filter `rental_id IS NOT NULL` (5 rows) or the 5 unlinked payments drop out silently.