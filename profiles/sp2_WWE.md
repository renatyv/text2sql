---
generator: db-snooper
version: 0.0.34
generated_at_utc: 2026-08-24T21:58:28.255968Z
dialect: sqlite
database: /var/folders/9j/b9bx_drd53sc6zbpsqyrjy4h0000gn/T/dbsnoop-9xux4x9a/WWE.sqlite
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
| id | 70791 | 48530 | 2686 |
| name | EVOLVE Tag Team Titles | WWE Intercontinental Championship WWE Women's Championship (original) | WCW United States Title WWF Intercontinental Title |

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
| id | 14344 | 1577 | 11343 |
| table_id | 3221 | 1570 | 11343 |
| location_id | 312 | 325 | 4255 |
| promotion_id | 3211 | 230 | 10963 |
| event_date | 2023-12-29 | 1996-05-28 | 2020-03-23 |
| event_id | 3429 | 1577 | 11343 |
| url | http://www.profightdb.com/cards/wwe/wwe-live---holiday-tour-51464.html | http://www.profightdb.com/cards/wwf/superstars-of-wrestling-taping-505-13379.html | http://www.profightdb.com/cards/nxt/tv-taping-394-32340.html |
| info_html | <table border="0" width="100%">  <tr>   <td align="left" height="23" width="40%">    <strong>     Date:    </strong>    <a href="/this-day-in-history/12-29-2023.html">     Fri, Dec 29th 2023    </a>… | <table border="0" width="100%">  <tr>   <td align="left" height="23" width="40%">    <strong>     Date:    </strong>    <a href="/this-day-in-history/05-28-1996.html">     Tue, May 28th 1996    </a>… | <table border="0" width="100%">  <tr>   <td align="left" height="23" width="40%">    <strong>     Date:    </strong>    <a href="/this-day-in-history/03-23-2020.html">     Mon, Mar 23rd 2020    </a>… |
| match_html | <table cellpadding="0" cellspacing="1" width="100%">  <tr class="head">   <th width="3%">    no.   </th>   <th colspan="3" width="50%">    match   </th>   <th width="5%">    duration   </th>   <th wi… | <table cellpadding="0" cellspacing="1" width="100%">  <tr class="head">   <th width="3%">    no.   </th>   <th colspan="3" width="50%">    match   </th>   <th width="5%">    duration   </th>   <th wi… | <table cellpadding="0" cellspacing="1" width="100%">  <tr class="head">   <th width="3%">    no.   </th>   <th colspan="3" width="50%">    match   </th>   <th width="5%">    duration   </th>   <th wi… |

# "Events"  (rows=5033)

columns:
"id" int PK UNIQ: unique identifier, 1..14341
"name" text UNIQ: unique identifier

indexes: none

samples:
| column | latest | sample | sample |
|---|---|---|---|
| id | 14341 | 747 | 2100 |
| name | Monday Night Raw - Day 1 2024 | Sunday Night Heat #115 Taping | Superstars of Wrestling Taping #359 |

# "Locations"  (rows=609)

columns:
"id" int PK UNIQ: unique identifier, 1..12645
"name" text UNIQ: unique identifier

indexes: none

samples:
| column | latest | sample | sample |
|---|---|---|---|
| id | 12645 | 4920 | 81 |
| name | Plant City, Florida | Alexandria, Louisiana | Boston, Massachusetts |

# "Match_Types"  (rows=1208)

columns:
"id" int PK UNIQ: unique identifier, 1..385709
"name" text UNIQ: unique identifier

indexes: none

samples:
| column | latest | sample | sample |
|---|---|---|---|
| id | 385709 | 26924 | 15409 |
| name | referee: Stevie Turner | referee: Elias handicap tag | Desert Storm |

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
| id | 12673 | 6901 | 2140 |
| html | <table cellpadding="0" cellspacing="1">  <tr class="head">   <th>    <a href="?order=date&amp;ppv=no&amp;type=asc" rel="nofollow">     date    </a>   </th>   <th>    <a href="?order=promotion&amp;ppv… | <table cellpadding="0" cellspacing="1">  <tr class="head">   <th>    <a href="?order=date&amp;ppv=no&amp;type=asc" rel="nofollow">     date    </a>   </th>   <th>    <a href="?order=promotion&amp;ppv… | <table cellpadding="0" cellspacing="1">  <tr class="head">   <th>    <a href="?order=date&amp;ppv=no&amp;type=asc" rel="nofollow">     date    </a>   </th>   <th>    <a href="?order=promotion&amp;ppv… |
| url | http://www.profightdb.com/cards/nxt-cards-pg172-no-103.html?order=&type= | http://www.profightdb.com/cards/wwe-cards-pg370-no-2.html?order=&type= | http://www.profightdb.com/cards/wwf-cards-pg192-no-1.html?order=&type= |

# "Wrestlers"  (rows=17182)

columns:
"id" int PK UNIQ: unique identifier, 1..1081588
"name" text: all distinct

indexes: none

samples:
| column | latest | sample | sample |
|---|---|---|---|
| id | 1081588 | 15018 | 141039 |
| name | Elton Prince & Grayson Waller & Kit Wilson | Head | Dakota Kai & Nikki Cross & Steffanie Newell |
