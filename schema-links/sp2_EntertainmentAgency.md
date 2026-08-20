# Schema Links

- version: 0.0.5
- dialect: sqlite
- database: file:/Users/renatyuldashev/Documents/ai-sql/custom-bench/data/sp2_lite_sqlite/databases/EntertainmentAgency.sqlite
- schema: main

## Declared PK/FK Links

Engagements.AgentID -> Agents.AgentID
Engagements.CustomerID -> Customers.CustomerID
Engagements.EntertainerID -> Entertainers.EntertainerID
Entertainer_Members.EntertainerID -> Entertainers.EntertainerID
Entertainer_Members.MemberID -> Members.MemberID
Entertainer_Styles.EntertainerID -> Entertainers.EntertainerID
Entertainer_Styles.StyleID -> Musical_Styles.StyleID
Musical_Preferences.CustomerID -> Customers.CustomerID
Musical_Preferences.StyleID -> Musical_Styles.StyleID

## Inferred Links

All inferred links are implied by the declared PK/FK links above.
