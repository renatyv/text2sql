---
generator: db-snooper
version: 0.0.31
generated_at_utc: 2026-08-20T17:26:39.386442Z
dialect: sqlite
database: /var/folders/9j/b9bx_drd53sc6zbpsqyrjy4h0000gn/T/dbsnoop-piuecq4q/student_club.sqlite
schema: main
---

## Relationships

- "budget"."budget_id" ← "expense"."link_to_budget"
- "event"."event_id" ← "attendance"."link_to_event", "budget"."link_to_event"
- "major"."major_id" ← "member"."link_to_major"
- "member"."member_id" ← "attendance"."link_to_member", "expense"."link_to_member", "income"."link_to_member"
- "zip_code"."zip_code" ← "member"."zip"

# "attendance"  (rows=326)

columns:
"link_to_event" text PK FK: "recLKj8BbTNqxFbTb"=30, "recykdvf4LgsyA3wZ"=30, "recEVTik3MlqbvLFi"=29, "recI43CzsZ0Q625ma"=27, "reciRZdAqNIKuMC96"=27, "reczhS8wix6Kzbp9P"=27, "recmbOVHSyzXQZpQr"=25, "recggMW2eyCYceNcy"=23, "rec5XDvJLyxDsGZWc"=20, "rec2N69DMcrqN9PJC"=17, "recvCUOytx5jPw7kh"=17, "recGxVCwaLW3mDIa3"=14, "recIuIXdbLe5j5vCA"=12, "recsgSUqFCJqekzL5"=11, "recoVo6dFSzG1ypX7"=8, "reckYL4xtQWpkTJ8k"=5, "recLrY8kyOR1PcZeF"=4
"link_to_member" text PK FK: 30 distinct, "recD078PnS3x2doBe"=16, "recro8T1MPMwRadVH"=16, "rec4BLdZHS2Blfp4v"=14, "recEFd8s6pkrTt4Pz"=14, "recTjHY5xXhvkCdVT"=14, "recZ4PkGERzl9ziHO"=14, "recP6DJPyi5donvXL"=13, "rec28ORZgcm1dtqBZ"=12, "rec75vvFxgYtHmqxY"=12, "recT92PyyZCGq1R68"=12

indexes: none
fk: "link_to_event"→"event"."event_id", "link_to_member"→"member"."member_id"

samples:
| column | latest | sample | sample |
|---|---|---|---|
| link_to_event | reczhS8wix6Kzbp9P | rec5XDvJLyxDsGZWc | recoVo6dFSzG1ypX7 |
| link_to_member | recxBj3tjKTGHqucS | recf4UKTfipCzgcSA | recVsoJJHFI8bgtfw |

# "budget"  (rows=52)

columns:
"budget_id" text PK: unique identifier
"category" text: "Food"=22, "Advertisement"=15, "Parking"=7, "Speaker Gifts"=7, "Club T-Shirts"=1
"spent" float: 0=28, 6=3, 20.2=3, 54.25=3, 13.45=2, 67.81=2, 16.28=1, 74.59=1, 101.94=1, 121.14=1, 122.06=1, 122.33=1, 154.34=1, 173.06=1, 174.25=1, 295.12=1, 327.07=1, 0..327.07
"remaining" float: 22 distinct, -24.25..150, avg=40.6529, median=20
"amount" int: 150=14, 10=7, 20=7, 25=7, 55=7, 75=7, 155=1, 300=1, 350=1, 10..350
"event_status" text: "Open"=23, "Closed"=22, "Planning"=7
"link_to_event" text FK: 23 distinct

indexes: none
fk: "link_to_event"→"event"."event_id"

samples:
| column | latest | sample | sample |
|---|---|---|---|
| budget_id | recziC0Fccvve12RF | recynAp4ySkYoycct | recsI0IzpUuxl2bPh |
| category | Parking | Food | Advertisement |
| spent | 0 | 0 | 67.81 |
| remaining | 10 | 20 | 7.19 |
| amount | 10 | 20 | 75 |
| event_status | Open | Planning | Closed |
| link_to_event | recAlAwtBZ0Fqbr5K | recLrY8kyOR1PcZeF | recEVTik3MlqbvLFi |

# "event"  (rows=42)

columns:
"event_id" text PK: unique identifier
"event_name" text: 39 distinct
"event_date" text: iso-date, 41 distinct
"type" text: "Meeting"=16, "Guest Speaker"=7, "Game"=6, "Community Service"=4, "Social"=4, "Budget"=2, "Election"=2, "Registration"=1
"notes" text: "All active members can vote for new officers between 4pm-8pm."=2, "Attend school football game as a group."=2, "Members and alumni can attend a community theater play at a reduced price. Active membership required."=2, "Officers and Budget Committee only"=2, "Semester social event. Optional attendance."=2, "Attend Women's soccer game as a group."=1, "Attend school Woman's Lacrosse game as a group."=1, "Attend school teams Lacrosse game as a group."=1, "Attend school teams baseball game as a group."=1, "Monthly officers meeting"=1, "Students can stop by the table to get information on the club and register."=1, "Volunteer opportunity to help paint new home."=1, "Volunteer opportunity to pack backpacks for underprivileged youth."=1, "Volunteer opportunity to remove graffiti in town."=1, "Volunteer opportunity to sort donations for distribution."=1, nulls=22
"location" text: "MU 215"=19, "Campus Soccer/Lacrosse stadium"=3, "100 W. Main Street"=2, "900 E. Washington St."=2, "Campus Football stadium"=2, "Conference Room BA 452"=2, "1308 106th Ave."=1, "258 S. Maple St."=1, "45 N. Smith St."=1, "Campus Baseball Stadium"=1, "Campus Common"=1, "Various locations"=1, nulls=6
"status" text: "Closed"=18, "Open"=13, "Planning"=11

indexes: none
fk: none

samples:
| column | latest | sample | sample |
|---|---|---|---|
| event_id | reczhS8wix6Kzbp9P | recwM7GMBSLDlb1Ix | recLePFQvYN36qANI |
| event_name | September Meeting | April Meeting | Fall Elections |
| event_date | 2019-09-10T12:00:00 | 2020-04-07T12:00:00 | 2020-04-26T09:00:00 |
| type | Meeting | Meeting | Election |
| notes | null | null | All active members can vote for new officers between 4pm-8pm. |
| location | MU 215 | MU 215 | MU 215 |
| status | Closed | Open | Planning |

# "expense"  (rows=32)

columns:
"expense_id" text PK: unique identifier
"expense_description" text: "Pizza"=7, "Posters"=6, "Water, chips, cookies"=5, "Parking"=3, "Water, Cookies"=3, "Travel Mug"=2, "Alumni Glass"=1, "Bakery - Donuts, muffins"=1, "Club shirts"=1, "Post Cards, Posters"=1, "Water, Veggie tray, supplies"=1, "Water, cookies, chips"=1
"expense_date" text: "2019-09-03"=3, "2019-09-10"=3, "2019-09-24"=3, "2019-10-08"=3, "2019-10-22"=3, "2019-11-05"=3, "2019-11-19"=3, "2019-11-04"=2, "2019-08-20"=1, "2019-09-01"=1, "2019-09-04"=1, "2019-09-15"=1, "2019-09-18"=1, "2019-10-01"=1, "2019-10-10"=1, "2019-10-15"=1, "2019-11-14"=1
"cost" float: 21 distinct, 6..295.12, avg=65.1891, median=54.25
"approved" text: "true"=31, nulls=1
"link_to_member" text FK: "rec4BLdZHS2Blfp4v"=12, "recD078PnS3x2doBe"=11, "recro8T1MPMwRadVH"=9
"link_to_budget" text FK: 24 distinct

indexes: none
fk: "link_to_member"→"member"."member_id", "link_to_budget"→"budget"."budget_id"

samples:
| column | latest | sample | sample |
|---|---|---|---|
| expense_id | recytertXPNtYtkC3 | reckyNexGnIVMiNGn | recnK8dKtLnRpm34U |
| expense_description | Bakery - Donuts, muffins | Travel Mug | Pizza |
| expense_date | 2019-09-03 | 2019-10-15 | 2019-09-24 |
| cost | 195.3 | 13.45 | 113.33 |
| approved | true | true | true |
| link_to_member | rec4BLdZHS2Blfp4v | rec4BLdZHS2Blfp4v | recro8T1MPMwRadVH |
| link_to_budget | recca5tkvdQgoLKZz | recZuCiQzCDAs4zDQ | rec5V70sIuIgpOzDT |

# "income"  (rows=36)

columns:
"income_id" text PK: unique identifier
"date_received" text: iso-date, 29 distinct
"amount" int: 50=33, 200=1, 1000=1, 3000=1, 50..3000
"source" text: "Dues"=33, "Fundraising"=1, "School Appropration"=1, "Sponsorship"=1
"notes" text: "Ad revenue for use on flyers used to advertise upcoming events."=1, "Annual funding from Student Government."=1, "Secured donations to help pay for speaker gifts."=1, nulls=33
"link_to_member" text FK: 31 distinct, nulls=3

indexes: none
fk: "link_to_member"→"member"."member_id"

samples:
| column | latest | sample | sample |
|---|---|---|---|
| income_id | reczYkzM4iPYdi8rh | rech1nxcukSGGnyJC | recpiEFskUe0ccvmq |
| date_received | 2019-09-12 | 2019-10-10 | 2019-09-25 |
| amount | 50 | 50 | 50 |
| source | Dues | Dues | Dues |
| notes | null | null | null |
| link_to_member | rec3pH4DxMcWHMRB7 | recuSfhAZIlKba4s2 | recWh2lJVOT6HjChK |

# "major"  (rows=113)

columns:
"major_id" text PK: unique identifier
"major_name" text: all distinct
"department" text: 47 distinct
"college" text: "College of Agriculture and Applied Sciences"=36, "College of Humanities and Social Sciences"=24, "College of Education & Human Services"=13, "College of Science"=12, "College of Natural Resources"=9, "School of Business"=7, "College of Engineering"=6, "College of the Arts"=6

indexes: none
fk: none

samples:
| column | latest | sample | sample |
|---|---|---|---|
| major_id | recz2waxrgL2KJEHe | recsiWnUNDT2kmOnr | rec8UcO67UAV7r4dm |
| major_name | Art History | Landscape Architecture | Psychology |
| department | Art and Design Department | Landscape Architecture and Environmental Planning Department | Psychology Department |
| college | College of the Arts | College of Agriculture and Applied Sciences | College of Education & Human Services |

# "member"  (rows=33)

columns:
"member_id" text PK: unique identifier
"first_name" text: all distinct
"last_name" text: all distinct
"email" text: all distinct
"position" text: "Member"=26, "Inactive"=3, "President"=1, "Secretary"=1, "Treasurer"=1, "Vice President"=1
"t_shirt_size" text: "Large"=13, "Medium"=10, "X-Large"=8, "Small"=2
"phone" text: all distinct
"zip" int FK: all distinct, 1020..98290, avg=37892.8, median=29440
"link_to_major" text FK: 26 distinct, nulls=1

indexes: none
fk: "zip"→"zip_code"."zip_code", "link_to_major"→"major"."major_id"

samples:
| column | latest | sample | sample |
|---|---|---|---|
| member_id | recxBj3tjKTGHqucS | rec4O9rmGnLx3j8vt | reccW7q1KkhSKZsea |
| first_name | Sherri | Christof | Adela |
| last_name | Ramsey | Nielson | O'Gallagher |
| email | sherri.ramsey@lpu.edu | christof.nielson@lpu.edu | adela.o'gallagher@lpu.edu |
| position | Member | Member | Member |
| t_shirt_size | Large | X-Large | Medium |
| phone | 942-555-1132 | (701) 932-1903 | 887-555-7733 |
| zip | 8861 | 58102 | 46123 |
| link_to_major | recVYIFAwjT91pnv7 | rectOU2QnznthfWv7 | recVNDNQrJxsXPFXa |

# "zip_code"  (rows=41877)

columns:
"zip_code" int PK: unique identifier, 501..99950, avg=49616, median=48850
"type" text: "Standard"=29973, "PO Box"=9438, "Unique"=2466
"city" text: 18729 distinct
"county" text: 2010 distinct, nulls=88
"state" text: 52 distinct
"short_state" text: 52 distinct

indexes: none
fk: none

samples:
| column | latest | sample | sample |
|---|---|---|---|
| zip_code | 99950 | 33991 | 17970 |
| type | PO Box | Standard | Standard |
| city | Ketchikan | Cape Coral | Saint Clair |
| county | Prince of Wales-Outer Ketchikan Borough | Lee County | Schuylkill County |
| state | Alaska | Florida | Pennsylvania |
| short_state | AK | FL | PA |
