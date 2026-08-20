# Schema Links

- version: 0.0.5
- dialect: sqlite
- database: file:/Users/renatyuldashev/Documents/ai-sql/custom-bench/data/sp2_lite_sqlite/databases/sqlite-sakila.sqlite
- schema: main

## Declared PK/FK Links

address.city_id -> city.city_id
city.country_id -> country.country_id
customer.address_id -> address.address_id
customer.store_id -> store.store_id
film.language_id -> language.language_id
film.original_language_id -> language.language_id
film_actor.actor_id -> actor.actor_id
film_actor.film_id -> film.film_id
film_category.category_id -> category.category_id
film_category.film_id -> film.film_id
inventory.film_id -> film.film_id
inventory.store_id -> store.store_id
payment.customer_id -> customer.customer_id
payment.rental_id -> rental.rental_id
payment.staff_id -> staff.staff_id
rental.customer_id -> customer.customer_id
rental.inventory_id -> inventory.inventory_id
rental.staff_id -> staff.staff_id
staff.address_id -> address.address_id
staff.store_id -> store.store_id
store.address_id -> address.address_id
store.manager_staff_id -> staff.staff_id

## Inferred Links

### rental.rental_id
- inferred: film.rental_duration
- declared: payment.rental_id
