# Schema Links

- version: 0.0.5
- dialect: sqlite
- database: file:/Users/renatyuldashev/Documents/ai-sql/custom-bench/data/bird_mini_dev/databases/dev_databases/student_club/student_club.sqlite
- schema: main

## Declared PK/FK Links

attendance.link_to_event -> event.event_id
attendance.link_to_member -> member.member_id
budget.link_to_event -> event.event_id
expense.link_to_budget -> budget.budget_id
expense.link_to_member -> member.member_id
income.link_to_member -> member.member_id
member.link_to_major -> major.major_id
member.zip -> zip_code.zip_code

## Inferred Links

### status
- inferred: budget.event_status, event.status
