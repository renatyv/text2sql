---
generator: db-snooper
version: 0.0.26
generated_at_utc: 2026-08-16T07:19:19.629141Z
dialect: sqlite
database: /Users/renatyuldashev/Documents/ai-sql/custom-bench/data/bird_mini_dev/databases/dev_databases/student_club/student_club.sqlite
schema: main
---

## Relationships

- budget.budget_id ← expense.link_to_budget
- event.event_id ← attendance.link_to_event, budget.link_to_event
- major.major_id ← member.link_to_major
- member.member_id ← attendance.link_to_member, expense.link_to_member, income.link_to_member
- zip_code.zip_code ← member.zip

# attendance

```sql
CREATE TABLE "attendance"
(
    link_to_event  TEXT,
    link_to_member TEXT,
    primary key (link_to_event, link_to_member),
    foreign key (link_to_event) references event(event_id),
    foreign key (link_to_member) references member(member_id)
);
```

## Rows

- total=326

| column | latest | sample | sample |
|---|---|---|---|
| link_to_event | reczhS8wix6Kzbp9P | recGxVCwaLW3mDIa3 | recI43CzsZ0Q625ma |
| link_to_member | recxBj3tjKTGHqucS | recD078PnS3x2doBe | recVsoJJHFI8bgtfw |

## Columns

- link_to_event: "recLKj8BbTNqxFbTb"=30, "recykdvf4LgsyA3wZ"=30, "recEVTik3MlqbvLFi"=29, "recI43CzsZ0Q625ma"=27, "reciRZdAqNIKuMC96"=27, "reczhS8wix6Kzbp9P"=27, "recmbOVHSyzXQZpQr"=25, "recggMW2eyCYceNcy"=23, "rec5XDvJLyxDsGZWc"=20, "rec2N69DMcrqN9PJC"=17, "recvCUOytx5jPw7kh"=17, "recGxVCwaLW3mDIa3"=14, "recIuIXdbLe5j5vCA"=12, "recsgSUqFCJqekzL5"=11, "recoVo6dFSzG1ypX7"=8, "reckYL4xtQWpkTJ8k"=5, "recLrY8kyOR1PcZeF"=4
- link_to_member: 30 distinct
  - top_values: "recD078PnS3x2doBe"=16, "recro8T1MPMwRadVH"=16, "rec4BLdZHS2Blfp4v"=14, "recEFd8s6pkrTt4Pz"=14, "recTjHY5xXhvkCdVT"=14, "recZ4PkGERzl9ziHO"=14, "recP6DJPyi5donvXL"=13, "rec28ORZgcm1dtqBZ"=12, "rec75vvFxgYtHmqxY"=12, "recT92PyyZCGq1R68"=12


# budget

```sql
CREATE TABLE "budget"
(
    budget_id     TEXT
            primary key,
    category      TEXT,
    spent         REAL,
    remaining     REAL,
    amount        INTEGER,
    event_status  TEXT,
    link_to_event TEXT,
    foreign key (link_to_event) references event(event_id)
);
```

## Rows

- total=52

| column | latest | sample | sample |
|---|---|---|---|
| budget_id | recziC0Fccvve12RF | recmdREMTVnyW11OD | rec4yM47hEjVVsCuq |
| category | Parking | Parking | Parking |
| spent | 0 | 0 | 0 |
| remaining | 10 | 10 | 10 |
| amount | 10 | 10 | 10 |
| event_status | Open | Planning | Open |
| link_to_event | recAlAwtBZ0Fqbr5K | rec2mJrCofveboaz6 | recs4x1BYWAsU2SKg |

## Columns

- budget_id: unique identifier
- category: "Food"=22, "Advertisement"=15, "Parking"=7, "Speaker Gifts"=7, "Club T-Shirts"=1
- spent: 0=28, 6=3, 20.2=3, 54.25=3, 13.45=2, 67.81=2, 16.28=1, 74.59=1, 101.94=1, 121.14=1, 122.06=1, 122.33=1, 154.34=1, 173.06=1, 174.25=1, 295.12=1, 327.07=1, num 0..327.07
- remaining: 22 distinct, num -24.25..150
  - stats: average=40.6529, median=20
- amount: 150=14, 10=7, 20=7, 25=7, 55=7, 75=7, 155=1, 300=1, 350=1, int 10..350
- event_status: "Open"=23, "Closed"=22, "Planning"=7
- link_to_event: 23 distinct


# event

```sql
CREATE TABLE event
(
    event_id   TEXT
        constraint event_pk
            primary key,
    event_name TEXT,
    event_date TEXT,
    type       TEXT,
    notes      TEXT,
    location   TEXT,
    status     TEXT
);
```

## Rows

- total=42

| column | latest | sample | sample |
|---|---|---|---|
| event_id | reczhS8wix6Kzbp9P | reciRZdAqNIKuMC96 | recsgSUqFCJqekzL5 |
| event_name | September Meeting | November Speaker | Food Bank |
| event_date | 2019-09-10T12:00:00 | 2019-11-19T12:00:00 | 2019-11-21T02:00:00 |
| type | Meeting | Guest Speaker | Community Service |
| notes | null | null | Volunteer opportunity to sort donations for distribution. |
| location | MU 215 | MU 215 | 1308 106th Ave. |
| status | Closed | Closed | Closed |

## Columns

- event_id: unique identifier
- event_name: 39 distinct
- event_date: 41 distinct
- type: "Meeting"=16, "Guest Speaker"=7, "Game"=6, "Community Service"=4, "Social"=4, "Budget"=2, "Election"=2, "Registration"=1
- notes: "All active members can vote for new officers between 4pm-8pm."=2, "Attend school football game as a group."=2, "Members and alumni can attend a community theater play at a reduced price. Active membership required."=2, "Officers and Budget Committee only"=2, "Semester social event. Optional attendance."=2, "Attend Women's soccer game as a group."=1, "Attend school Woman's Lacrosse game as a group."=1, "Attend school teams Lacrosse game as a group."=1, "Attend school teams baseball game as a group."=1, "Monthly officers meeting"=1, "Students can stop by the table to get information on the club and register."=1, "Volunteer opportunity to help paint new home."=1, "Volunteer opportunity to pack backpacks for underprivileged youth."=1, "Volunteer opportunity to remove graffiti in town."=1, "Volunteer opportunity to sort donations for distribution."=1, nulls=22
- location: "MU 215"=19, "Campus Soccer/Lacrosse stadium"=3, "100 W. Main Street"=2, "900 E. Washington St."=2, "Campus Football stadium"=2, "Conference Room BA 452"=2, "1308 106th Ave."=1, "258 S. Maple St."=1, "45 N. Smith St."=1, "Campus Baseball Stadium"=1, "Campus Common"=1, "Various locations"=1, nulls=6
- status: "Closed"=18, "Open"=13, "Planning"=11


# expense

```sql
CREATE TABLE "expense"
(
    expense_id          TEXT
            primary key,
    expense_description TEXT,
    expense_date        TEXT,
    cost                REAL,
    approved            TEXT,
    link_to_member      TEXT,
    link_to_budget      TEXT,
    foreign key (link_to_budget) references budget(budget_id),
    foreign key (link_to_member) references member(member_id)
);
```

## Rows

- total=32

| column | latest | sample | sample |
|---|---|---|---|
| expense_id | recytertXPNtYtkC3 | recOMqTkoXlx8RFt4 | recoi6IqHyFHYxGzO |
| expense_description | Bakery - Donuts, muffins | Parking | Parking |
| expense_date | 2019-09-03 | 2019-10-22 | 2019-09-24 |
| cost | 195.3 | 6 | 6 |
| approved | true | true | true |
| link_to_member | rec4BLdZHS2Blfp4v | recro8T1MPMwRadVH | recro8T1MPMwRadVH |
| link_to_budget | recca5tkvdQgoLKZz | recJOc7f9KgpgJm5q | recZdw5TjWrRTj4kp |

## Columns

- expense_id: unique identifier
- expense_description: "Pizza"=7, "Posters"=6, "Water, chips, cookies"=5, "Parking"=3, "Water, Cookies"=3, "Travel Mug"=2, "Alumni Glass"=1, "Bakery - Donuts, muffins"=1, "Club shirts"=1, "Post Cards, Posters"=1, "Water, Veggie tray, supplies"=1, "Water, cookies, chips"=1
- expense_date: "2019-09-03"=3, "2019-09-10"=3, "2019-09-24"=3, "2019-10-08"=3, "2019-10-22"=3, "2019-11-05"=3, "2019-11-19"=3, "2019-11-04"=2, "2019-08-20"=1, "2019-09-01"=1, "2019-09-04"=1, "2019-09-15"=1, "2019-09-18"=1, "2019-10-01"=1, "2019-10-10"=1, "2019-10-15"=1, "2019-11-14"=1
- cost: 21 distinct, num 6..295.12
  - stats: average=65.1891, median=54.25
- approved: "true"=31, nulls=1
- link_to_member: "rec4BLdZHS2Blfp4v"=12, "recD078PnS3x2doBe"=11, "recro8T1MPMwRadVH"=9
- link_to_budget: 24 distinct


# income

```sql
CREATE TABLE "income"
(
    income_id      TEXT
        constraint income_pk
            primary key,
    date_received  TEXT,
    amount         INTEGER,
    source         TEXT,
    notes          TEXT,
    link_to_member TEXT,
    foreign key (link_to_member) references member(member_id)
);
```

## Rows

- total=36

| column | latest | sample | sample |
|---|---|---|---|
| income_id | reczYkzM4iPYdi8rh | recCRWMfFqifuKMc6 | recXFdA0P6QkxSqg8 |
| date_received | 2019-09-12 | 2019-09-18 | 2019-09-18 |
| amount | 50 | 50 | 50 |
| source | Dues | Dues | Dues |
| notes | null | null | null |
| link_to_member | rec3pH4DxMcWHMRB7 | rec28ORZgcm1dtqBZ | recP6DJPyi5donvXL |

## Columns

- income_id: unique identifier
- date_received: 29 distinct
- amount: 50=33, 200=1, 1000=1, 3000=1, int 50..3000
- source: "Dues"=33, "Fundraising"=1, "School Appropration"=1, "Sponsorship"=1
- notes: "Ad revenue for use on flyers used to advertise upcoming events."=1, "Annual funding from Student Government."=1, "Secured donations to help pay for speaker gifts."=1, nulls=33
- link_to_member: 31 distinct, nulls=3


# major

```sql
CREATE TABLE major
(
    major_id   TEXT
        constraint major_pk
            primary key,
    major_name TEXT,
    department TEXT,
    college    TEXT
);
```

## Rows

- total=113

| column | latest | sample | sample |
|---|---|---|---|
| major_id | recz2waxrgL2KJEHe | recVYIFAwjT91pnv7 | recd4JTuI0ssyoz07 |
| major_name | Art History | Physics Teaching | Dietetics |
| department | Art and Design Department | Physics Department | Nutrition, Dietetics, and Food Sciences Department |
| college | College of the Arts | College of Science | College of Agriculture and Applied Sciences |

## Columns

- major_id: unique identifier
- major_name: all distinct
- department: 47 distinct
- college: "College of Agriculture and Applied Sciences"=36, "College of Humanities and Social Sciences"=24, "College of Education & Human Services"=13, "College of Science"=12, "College of Natural Resources"=9, "School of Business"=7, "College of Engineering"=6, "College of the Arts"=6


# member

```sql
CREATE TABLE "member"
(
    member_id     TEXT
        constraint member_pk
            primary key,
    first_name    TEXT,
    last_name     TEXT,
    email         TEXT,
    position      TEXT,
    t_shirt_size  TEXT,
    phone         TEXT,
    zip           INTEGER,
    link_to_major TEXT,
    foreign key (link_to_major) references major(major_id),
    foreign key (zip) references zip_code(zip_code)
);
```

## Rows

- total=33

| column | latest | sample | sample |
|---|---|---|---|
| member_id | recxBj3tjKTGHqucS | reccSUPwy30AeZLEb | recEFd8s6pkrTt4Pz |
| first_name | Sherri | Vincent | Matthew |
| last_name | Ramsey | Ratcliffe | Snay |
| email | sherri.ramsey@lpu.edu | vincent.ratcliffe@lpu.edu | matt.snay@lpu.edu |
| position | Member | Inactive | Member |
| t_shirt_size | Large | Large | Large |
| phone | 942-555-1132 | 894-555-4529 | 260-555-4328 |
| zip | 8861 | 35640 | 7002 |
| link_to_major | recVYIFAwjT91pnv7 | recKJHO1P6ZC5m567 | recxRBSgVYeSEGvyo |

## Columns

- member_id: unique identifier
- first_name: all distinct
- last_name: all distinct
- email: all distinct
- position: "Member"=26, "Inactive"=3, "President"=1, "Secretary"=1, "Treasurer"=1, "Vice President"=1
- t_shirt_size: "Large"=13, "Medium"=10, "X-Large"=8, "Small"=2
- phone: all distinct
- zip: all distinct, int 1020..98290
  - stats: average=37892.8, median=29440
- link_to_major: 26 distinct, nulls=1


# zip_code

```sql
CREATE TABLE zip_code
(
    zip_code    INTEGER
        constraint zip_code_pk
            primary key,
    type        TEXT,
    city        TEXT,
    county      TEXT,
    state       TEXT,
    short_state TEXT
);
```

## Rows

- total=41877

| column | latest | sample | sample |
|---|---|---|---|
| zip_code | 99950 | 28362 | 5740 |
| type | PO Box | PO Box | PO Box |
| city | Ketchikan | Marietta | East Middlebury |
| county | Prince of Wales-Outer Ketchikan Borough | Robeson County | Addison County |
| state | Alaska | North Carolina | Vermont |
| short_state | AK | NC | VT |

## Columns

- zip_code: unique identifier, int 501..99950
  - stats: average=49616, median=48850
- type: "Standard"=29973, "PO Box"=9438, "Unique"=2466
- city: 18729 distinct
- county: 2010 distinct, nulls=88
- state: 52 distinct
- short_state: 52 distinct
