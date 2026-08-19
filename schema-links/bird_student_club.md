# Schema Links

- generator: local introspection
- dialect: sqlite
- database: student_club

## Declared Links

- `attendance.link_to_event` → `event.event_id`
- `attendance.link_to_member` → `member.member_id`
- `budget.link_to_event` → `event.event_id`
- `expense.link_to_budget` → `budget.budget_id`
- `expense.link_to_member` → `member.member_id`
- `income.link_to_member` → `member.member_id`
- `member.link_to_major` → `major.major_id`
- `member.zip` → `zip_code.zip_code`

## Same-name Candidates

- `amount`: `budget.amount`, `income.amount`
- `link_to_event`: `attendance.link_to_event`, `budget.link_to_event`
- `link_to_member`: `attendance.link_to_member`, `expense.link_to_member`, `income.link_to_member`
- `notes`: `event.notes`, `income.notes`
- `type`: `event.type`, `zip_code.type`
