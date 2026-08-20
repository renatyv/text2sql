# Schema Links

- version: 0.0.5
- dialect: sqlite
- database: file:/Users/renatyuldashev/Documents/ai-sql/custom-bench/data/bird_mini_dev/databases/dev_databases/financial/financial.sqlite
- schema: main

## Declared PK/FK Links

account.district_id -> district.district_id
card.disp_id -> disp.disp_id
client.district_id -> district.district_id
disp.account_id -> account.account_id
disp.client_id -> client.client_id
loan.account_id -> account.account_id
order.account_id -> account.account_id
trans.account_id -> account.account_id

## Inferred Links

All inferred links are implied by the declared PK/FK links above.
