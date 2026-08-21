---
generator: db-snooper
version: 0.0.33
generated_at_utc: 2026-08-21T12:33:23.181753Z
dialect: sqlite
database: /var/folders/9j/b9bx_drd53sc6zbpsqyrjy4h0000gn/T/dbsnoop-kuz97xfl/WWE.sqlite
schema: main
---

# "Belts"  (rows=143)

columns:
"id" int PK UNIQ: unique identifier, 1..70791
"name" text UNIQ: unique identifier

indexes: none

samples:
| column | latest | sample | sample |
|---|---|---|---|
| id | 70791 | 20610 | 20577 |
| name | EVOLVE Tag Team Titles | WWE Intercontinental Championship | WWE United States Championship |

# "Cards"  (rows=12639)

columns:
"id" int PK UNIQ: unique identifier, 1..14344
"table_id" int: 1270 distinct, 1..12673
"location_id" int: 596 distinct, 1..12645
"promotion_id" int: 3211=6616, 230=2967, 10963=1749, 9876=1078, 1=229, 1..10963
"event_date" text: iso-date, 6782 distinct
"event_id" int: 5020 distinct, 1..14341
"url" text UNIQ: unique identifier
"info_html" text: 8705 distinct
"match_html" text UNIQ: unique identifier

indexes: none

samples:
| column | latest | sample | sample |
|---|---|---|---|
| id | 14344 | 13733 | 454 |
| table_id | 3221 | 3211 | 450 |
| location_id | 312 | 256 | 246 |
| promotion_id | 3211 | 3211 | 230 |
| event_date | 2023-12-29 | 2023-12-04 | 2001-09-14 |
| event_id | 3429 | 3212 | 454 |
| url | http://www.profightdb.com/cards/wwe/wwe-live---holiday-tour-51464.html | http://www.profightdb.com/cards/wwe/main-event-taping-50925.html | http://www.profightdb.com/cards/wwf/sunday-night-heat-164-taping-1690.html |
| info_html | <table border="0" width="100%">  <tr>   <td align="left" height="23" width="40%">    <strong>     Date:    </strong>    <a href="/this-day-in-history/12-29-2023.html">     Fri, Dec 29th 2023    </a>… | <table border="0" width="100%">  <tr>   <td align="left" height="23" width="40%">    <strong>     Date:    </strong>    <a href="/this-day-in-history/12-04-2023.html">     Mon, Dec 4th 2023    </a>… | <table border="0" width="100%">  <tr>   <td align="left" height="23" width="40%">    <strong>     Date:    </strong>    <a href="/this-day-in-history/09-14-2001.html">     Fri, Sep 14th 2001    </a>… |
| match_html | <table cellpadding="0" cellspacing="1" width="100%">  <tr class="head">   <th width="3%">    no.   </th>   <th colspan="3" width="50%">    match   </th>   <th width="5%">    duration   </th>   <th wi… | <table cellpadding="0" cellspacing="1" width="100%">  <tr class="head">   <th width="3%">    no.   </th>   <th colspan="3" width="50%">    match   </th>   <th width="5%">    duration   </th>   <th wi… | <table cellpadding="0" cellspacing="1" width="100%">  <tr class="head">   <th width="3%">    no.   </th>   <th colspan="3" width="50%">    match   </th>   <th width="5%">    duration   </th>   <th wi… |

# "Events"  (rows=5033)

columns:
"id" int PK UNIQ: unique identifier, 1..14341
"name" text UNIQ: unique identifier

indexes: none

samples:
| column | latest | sample | sample |
|---|---|---|---|
| id | 14341 | 499 | 2454 |
| name | Monday Night Raw - Day 1 2024 | Sunday Night Heat #157 Taping | Superstars of Wrestling Taping #253 |

# "Locations"  (rows=609)

columns:
"id" int PK UNIQ: unique identifier, 1..12645
"name" text UNIQ: unique identifier

indexes: none

samples:
| column | latest | sample | sample |
|---|---|---|---|
| id | 12645 | 5269 | 10850 |
| name | Plant City, Florida | Pasay, Manila | Halle, North Rhine-Westphalia |

# "Match_Types"  (rows=1208)

columns:
"id" int PK UNIQ: unique identifier, 1..385709
"name" text UNIQ: unique identifier

indexes: none

samples:
| column | latest | sample | sample |
|---|---|---|---|
| id | 385709 | 57484 | 31864 |
| name | referee: Stevie Turner | Oktoberfest hardcore | commentator: Sasha Banks |

# "Matches"  (rows=≈540800)

columns:
"id" int PK UNIQ
"card_id" int
"winner_id" text
"win_type" text
"loser_id" text
"match_type_id" text
"duration" text
"title_id" text
"title_change" int

indexes: none


# "Promotions"  (rows=6)

columns:
"id" int PK UNIQ
"name" text UNIQ

indexes: none

all rows:
| column | row 1 | row 2 | row 3 | row 4 | row 5 | row 6 |
|---|---|---|---|---|---|---|
| id | 1 | 230 | 3211 | 9876 | 10963 | 12682 |
| name | WWWF | WWF | WWE | WCW | NXT | ECW |

# "Tables"  (rows=1270)

columns:
"id" int PK UNIQ: unique identifier, 1..12673
"html" text UNIQ: unique identifier
"url" text UNIQ: unique identifier

indexes: none

samples:
| column | latest | sample | sample |
|---|---|---|---|
| id | 12673 | 3881 | 3351 |
| html | <table cellpadding="0" cellspacing="1">  <tr class="head">   <th>    <a href="?order=date&amp;ppv=no&amp;type=asc" rel="nofollow">     date    </a>   </th>   <th>    <a href="?order=promotion&amp;ppv… | <table cellpadding="0" cellspacing="1">  <tr class="head">   <th>    <a href="?order=date&amp;ppv=no&amp;type=asc" rel="nofollow">     date    </a>   </th>   <th>    <a href="?order=promotion&amp;ppv… | <table cellpadding="0" cellspacing="1">  <tr class="head">   <th>    <a href="?order=date&amp;ppv=no&amp;type=asc" rel="nofollow">     date    </a>   </th>   <th>    <a href="?order=promotion&amp;ppv… |
| url | http://www.profightdb.com/cards/nxt-cards-pg172-no-103.html?order=&type= | http://www.profightdb.com/cards/wwe-cards-pg68-no-2.html?order=&type= | http://www.profightdb.com/cards/wwe-cards-pg15-no-2.html?order=&type= |

# "Wrestlers"  (rows=17182)

columns:
"id" int PK UNIQ: unique identifier, 1..1081588
"name" text: all distinct

indexes: none

samples:
| column | latest | sample | sample |
|---|---|---|---|
| id | 1081588 | 101086 | 138832 |
| name | Elton Prince & Grayson Waller & Kit Wilson | Jim Duggan & Scotty 2 Hotty | Denzel Dejournette & M. J. Jenkins |
