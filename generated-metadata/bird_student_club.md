# Additional Metadata

## Clarified Semantics

- `expense.link_to_member` identifies the club officer who recorded the expense (only President, Treasurer, Vice President appear), not the member who benefited; it is not an account/user attribution.
- `budget` is a per-line-item ledger: 52 rows map to only 23 distinct `link_to_event` values, i.e. a single event can have multiple budget lines (up to 4), so per-event spend/remaining must be summed (`spent`, `amount`) across its budget rows.
- `income.link_to_member` is NULL for non-Dues sources (`Fundraising`, `School Appropriation`, `Sponsorship`); only `Dues` rows are attributed per-member. Treat NULL as club-wide/unattributed income.
- `expense.approved` is essentially all "true" with a single NULL row; it is not a meaningful discriminator.
- `attendance` has a composite primary key (`link_to_event`, `link_to_member`); an event-member pair appears at most once, so plain event/member counts need no de-duplication.
- `member.zip` is an integer that references the (83k+ row) US `zip_code` lookup; the member table itself stores only the code — city/county/state must be pulled from `zip_code`.
- `member.position`: only one active officer each for President/Secretary/Treasurer/Vice President; the rest are "Member" or "Inactive".
- `member.link_to_major` is NULL for 1 member; `major` itself carries department/college hierarchy (college → department → major_name).

## Potential Join Strategies

- **Member → major → college/department**: `member.link_to_major = major.major_id`, optionally grouping by `major.college`/`major.department`. Note 1 member has a NULL major (integer/FK comparisons may drop it unless LEFT JOIN).
- **Member → zip_code geography**: `member.zip = zip_code.zip_code` to attach `city`/`county`/`state`. `zip_code` is a large lookup (41k rows); only joined member zips match. No NULL members found in data but use LEFT JOIN to be safe.
- **Attendance → event + member**: `attendance.link_to_event = event.event_id` AND `attendance.link_to_member = member.member_id`. Drive from `attendance` as the fact table; joining `event` for type/name/location and `member` for member attributes. 326 rows, 17 distinct events / 30 distinct members.
- **Dues income ↔ membership**: `income.link_to_member = member.member_id` where `source='Dues'` — this is the per-member revenue link (33 of 36 income rows); non-Dues rows have NULL member and should be excluded/treated separately.
- **Expense ↔ budget ↔ event**: `expense.link_to_budget = budget.budget_id`, then `budget.link_to_event = event.event_id` to roll expenses up to an event. One budget line = one expense row (differing `link_to_budget` count of 24 vs 32 expense rows — some events share/duplicate budget usage, so an event's realized spend may also be read from `budget.spent` directly).
- **Expense ↔ member (officer)**: `expense.link_to_member = member.member_id` yields which officer handled expenses; useful only for officer-level attribution, not clubwide member activity.
- **Budget filter caveat**: `budget.event_status` (`Open`/`Closed`/`Planning`) is a status copy that does NOT match `event.status` one-to-one (23 vs 42 event rows); do not JOIN the two status columns on value equality — align via `link_to_event = event_id` instead.