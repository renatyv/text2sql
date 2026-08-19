# Schema Links

- generator: local introspection
- dialect: sqlite
- database: financial

## Declared Links

- `account.district_id` → `district.district_id`
- `card.disp_id` → `disp.disp_id`
- `client.district_id` → `district.district_id`
- `disp.account_id` → `account.account_id`
- `disp.client_id` → `client.client_id`
- `loan.account_id` → `account.account_id`
- `order.account_id` → `account.account_id`
- `trans.account_id` → `account.account_id`

## Same-name Candidates

- `account_id`: `account.account_id`, `disp.account_id`, `loan.account_id`, `order.account_id`, `trans.account_id`
- `amount`: `loan.amount`, `order.amount`, `trans.amount`
- `client_id`: `client.client_id`, `disp.client_id`
- `date`: `account.date`, `loan.date`, `trans.date`
- `disp_id`: `card.disp_id`, `disp.disp_id`
- `district_id`: `account.district_id`, `client.district_id`, `district.district_id`
- `k_symbol`: `order.k_symbol`, `trans.k_symbol`
- `type`: `card.type`, `disp.type`, `trans.type`
