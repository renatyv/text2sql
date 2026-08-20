# Additional Metadata

## Clarified Semantics

- Database is the classic **Pagila** (Sakila-style) schema despite the dataset profile labeling; this is a denormalized rental-store sample (customer discounts/active tracking, employee-managed stores, film catalog with actors/categories).
- `rental.return_date` is nullable; NULL rows (183 of 16044) mean the copy has not yet been returned (outstanding rentals).
- `payment.rental_id` is nullable with only 5 NULLs; payments without a linked rental also have no `rental` row.
- `payment.amount` is the actual transaction amount charged, not a per-unit rental rate; values are grouped around price tiers but include chargebacks/credits (e.g. amount = 0).
- `film.original_language_id` is entirely NULL (no dubbed original-language films); only `film.language_id` (English, =1 for all films) is populated.
- `address` columns `address2`, `district`, and `phone` are populated with placeholder blank/space values in this dataset (all-NULL for address2, all-space for district/phone), so they carry no discriminating information.
- `customer.active` is a char `'1'`/`'0'` flag (584 active, 15 inactive), while `staff.active` is a smallint flag (both 1).
- `customer.email` uses `first.last@sakilacustomer.org` convention and is unique per customer.
- Views (`customer_list`, `film_list`, `sales_by_film_category`, `sales_by_store`, `staff_list`) re-express joins in the schema-links but reference underlying tables; they can be used for pre-joined pivots rather than re-joining.
- `store.address_id` and `staff.address_id` live in the same `address` space, but each store/staff address is unique (no shared address rows between staff and stores).
- `<empty>` `film_text` table is skipped/empty and irrelevant.

## Potential Join Strategies

- **Rental-to-payment** `payment.rental_id = rental.rental_id`: 1:1 (payment.rental_id all-distinct when present); use LEFT JOIN to capture payments with NULL rental_id (n=5), and be aware ~16044 rental rows vs ~16049 payments (one payment can reference a rental_id beyond 16044).
- **Rental-to-income**: derive sales only from payments that resolve through rental → inventory → film. Chain `payment.rental_id→rental.rental_id→inventory.inventory_id→film.film_id` gives per-film/store revenue; filtering out NULL rental_id rows (5) avoids dropping orphaned payments in totals.
- **Category x actor fan-out trap**: `film_list` view joins category→film_category→film→film_actor→actor, so each film appears once per actor (5462 rows). Pre-aggregate film_actor by film before joining to film/category to get true per-film cardinality.
- **Store → manager de-dup**: join `store.manager_staff_id = staff.staff_id` (FK) for store managers; `staff.store_id` also equals the store, so joining staff→store on store_id yields 1:1 (2 staff, 2 stores) but joining via manager_staff_id is the canonical manager link.
- **Geo chain for location grouping**: `address.city_id→city.city_id→city.country_id→country.country_id` links customers/staff/stores to city/country; district and phone fields are unusable (all placeholder), so group geography by city/country only. country_id is low-cardinality (109) with many cities per country, so pre-filtering by country before address/customer joins is effective.
- **Inventory uniqueness**: index `(store_id, film_id)` exists; a film can have up to 8 copies (max inventory per film) split across the 2 stores. To count titles available at a store, join `inventory.store_id→store.store_id` and dedupe on film_id.
- **Membership joins vs fan-out**: actor↔film (film_actor) and film↔category (film_category) are explicit many-to-many junction tables; join through the junction to count films per actor/category, but aggregate before re-joining to avoid row multiplication.