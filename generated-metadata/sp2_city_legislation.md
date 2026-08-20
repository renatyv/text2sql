# Additional Metadata

## Clarified Semantics

- Even though the database is named `city_legislation`, it aggregates unrelated synthetic domains: alien records, US legislator terms, city/country reference data, and job postings. The "city/legislation" pair is only the cities + legislators portion.
- `alien_data`, `aliens`, `aliens_details`, `aliens_location` are four denormalized fragments of the same 50,000 alien rows. They align 1:1 row-for-row on a shared id space: `aliens.id` ↔ `alien_data.id` ↔ `aliens_details.detail_id` ↔ `aliens_location.loc_id` (all 50000 match). No declared FK exists; the alignment is positional.
  - `aliens` is the core entity (names, email, gender, `type`, birth_year).
  - `alien_data` carries redundant, differently-cased copies of the same attributes (gender/type casing, and per-row numeric id surviving `aliens`).
  - `aliens_details` holds only favorite_food / feeding_frequency / aggressive on the shared id.
  - `aliens_location` holds only current_location / state / country / occupation on the shared id.
  - Prefer joining the fragments on the shared id column rather than on names/email (only email is unique; names repeat).
- `aliens` gender is a richer set (Female, Male, Bigender, ...) while `alien_data.gender` is reduced to female/male/non-binary. `alien_data`'s `type`, `feeding_frequency`, `first/last_name` are lower-cased copies of `aliens` values.
- `email` in `aliens`/`alien_data` is all-distinct and is the sole reliable natural key for de-duplicating the fragments.
- `aliens_location.country` is a constant "United States" for all 50,000 rows; it provides no geographical variety.
- `cities` is global (rows have country_code_2 of 236 countries and some out-of-range lat/lon values), not US-only.
- `districts` in `legislators_terms` are null for senators (all 3873 sen rows have `district` null), and `class` is non-null only for senators.
- `legislators_terms.state` uses two-letter codes (e.g., "MT", "TX"), distinct from `aliens_location.state` (full names).
- `job_postings_fact.job_country` stores free-text country names (150 distinct), matching the same convention as `cities_countries.country_name`; `aliens_location.country` is the link to that column but is degenerate (single value).
- `job_postings_fact` is heavy in nulls: salary_rate (75,480) and salary_year_avg (76,595) are null for ~97% of rows; job_via, job_title, job_location also have some nulls. Salary aggregates are therefore mostly empty.
- `legislation_date_dim` is a sparse date dimension (month_name / day_of_month) covering ~30k dates, not every calendar day; useful for monthly/dom aggregation of term or posting dates.
- `skills_dim` has only 26 rows (skill_id up to 250) while `skill_id` values in `skills_job_dim` go beyond it; join on `skills_dim.skill_id` filters to recognized skills.

## Potential Join Strategies

- **Alien fragments unification**: join `aliens.id = alien_data.id = aliens_details.detail_id = aliens_location.loc_id` (all 1:1, 50,000 rows). This reconstructs the full alien record. Card=1:1, no fan-out. Alternative: join `aliens.email = alien_data.email` as a second cross-check.
- **Country hub**: `cities_countries.country_code_2` is the hub key shared by `cities`, `cities_currencies`, and `cities_languages`. Join `cities.country_code_2 = cities_countries.country_code_2`.
- **Currency/language fan-out caveat**: a single country_code_2 maps to multiple rows in `cities_currencies` (254 rows, 233 distinct codes) and `cities_languages` (608 rows, 237 distinct codes), so joining cities→currencies or cities→languages multiplies rows per city. Prefer aggregating or semi-joining on country_code_2 instead of inner-joining directly.
- **Job → company**: `job_postings_fact.company_id = job_company.company_id`. `job_company.link`, `thumbnail` are null for most companies (8,648 / 5,884 of 14,003); expect nulls when joining company metadata.
- **Job → skills fan-out**: `job_postings_fact.job_id = skills_job_dim.job_id`, then `skills_job_dim.skill_id = skills_dim.skill_id`. `skills_job_dim` has ~366,960 rows, so each job fans out to several skills; filter by `skills_dim.type` for programming/cloud/database clusters.
- **Legislator → terms**: `legislators.id_bioguide = legislators_terms.id_bioguide` (1:N, each legislator has up-to-30 terms, term_id unique). `term_type` splits rep (40,190) vs sen (3,873). Filter on `term_type = 'sen'` to also require non-null `class` and avoid null `district`.
- **Date-based joins**: use `job_postings_fact.job_posted_date` and `legislation_date_dim.date` for temporal aggregation; both are ISO text/datetime so string date-prefix grouping (e.g., day_of_month / month_name from the dim) works.
- **Cross-domain (name) link**: the schema `country` edge (aliens_location.country ↔ job_postings_fact.job_country) is nominal only and non-informative since `aliens_location.country` is a single constant value; treat any such join as a constant-equality filter, not a meaningful relationship.