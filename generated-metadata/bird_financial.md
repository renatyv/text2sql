# Additional Metadata

## Clarified Semantics

- **account.frequency** (Czech): "POPLATEK MESICNE" = monthly billing, "POPLATEK TYDNE" = weekly, "POPLATEK PO OBRATU" = per-transaction / after each operation.
- **trans.type**: `PRIJEM` = incoming/credit (405k), `VYDAJ` = outgoing/debit (634k), `VYBER` = ATM withdrawal (16k). `type` is a coarse grouping while `operation` refines it.
- **trans.operation**: `VYBER` (outgoing cash), `VYBER KARTOU` (card payment), `PREVOD NA UCET` (incoming transfer), `PREVOD Z UCTU` (outgoing transfer), `VKLAD` (cash deposit, incoming), empty (interest/other).
- **trans.k_symbol**: classification of the operation — `UROK` = interest, `DUCHOD` = pension, `SIPO` = standing-order household bills, `POJISTNE` = insurance, `SLUZBY` = fees, `SANKC. UROK` = penalty interest, `UVER` = loan repayment, empty = not classified (largest group).
- **trans.bank / trans.bank_to**: external counterparty bank (two-letter codes AB–QR); blank/large share empty for own-bank or internal moves. **trans.bank** (counterparty ACH bank here) covers internal transfers; many rows blank.
- **trans.account** (table column name `account`): counterparty account number for transfers (large numeric, e.g. 41403269), blank for internal/cash ops.
- **district A2–A16**: fixed census-region encoding (NOT free metrics):
  - A2 = district name, A3 = region (e.g. north Bohemia), A4 = inhabitants.
  - A5 = municipalities <499, A6 = 500–1999, A7 = 2000–9999, A8 = >10000, A9 = number of cities.
  - A10 = % people in towns (float 33.9..100), A11 = average salary (CZK), A12 = unemployment rate (1995), A13 = unemployment rate (1996), A14 = entrepreneurs per 1000 inhabitants.
  - A15 = number of crimes 1995, A16 = number of crimes 1996. A12 and A15 have 1 NULL each.
- **loan.status**: A = finished contract, no problems (203); C = running, no problems (403); B = finished with repayment problems (31); D = running, in default (45).
- **disp.type**: `OWNER` (4500, exactly one per account) vs `DISPONENT` (dispositionary, 869). Since OWNER count == account count, every account has exactly one owner row.
- **card.type**: `classic` (659), `junior` (145), `gold` (88); issued to a `disp_id` (owner or disponency).

## Potential Join Strategies

- **account → district** via `account_district_id = district.district_id`: enrich accounts with region/salary/unemployment for cohort analysis. Left join preserves all 4500 accounts (Cardinality 4500→77 log) and is cheap.
- **district → client → disp → account**: anchor on region to find accounts whose owner lives; useful for regional account distribution. The 77 districts expand once client/account join; filter on region early.
- **card → disp → account (and client)**: join `card.disp_id = disp.disp_id`, then `disp.account_id = account.account_id`; gives card holders' demographics (gender via client) restricted to OWNER/DISPONENT rows. Cardinality caveat: card is sparse (892) vs disp (5369) — left join if retention of all installments desired.
- **account → order** (`order.account_id`): one account owning multiple standing orders (orders only ~3758 distinct accounts). Orders carry only recurring payment orders; `account_to` is destination.
- **account → loan** (`loan.account_id`): loan per account linkage for risk/lifetime analysis; note many accounts have no loan so join mass 682.
- **order vs trans**: `order.account_id` and `trans.bank`/`trans.bank_to` share the two-letter bank code set (AB…QR), enabling matching recurring orders (k_symbol SIPO/UVER) to related outgoing transactions.
- **trans → account**: `trans.account_id = account.account_id` gives per-account transaction streams used PUA-side continuation; trans is ~1,056,000 rows with no index, so any filtered scan on trans should apply date/type guards and LIMIT on the driving side.
- **Cardinality warning**: `account.account_id` values range up to 11382 but only 4500 account rows exist; `order.account_to` spans huge numbers (399..99994199) unrelated to `account.account_id`, so never join those two columns.