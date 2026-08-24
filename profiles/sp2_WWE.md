---
generator: db-snooper
version: 0.0.34
generated_at_utc: 2026-08-24T21:22:57.187609Z
dialect: sqlite
database: /var/folders/9j/b9bx_drd53sc6zbpsqyrjy4h0000gn/T/dbsnoop-f7neyduj/WWE.sqlite
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
| id | 70791 | 7012 | 70763 |
| name | EVOLVE Tag Team Titles | WWF European Title WWF Intercontinental Title | PROGRESS Women's Title |

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
| id | 14344 | 9171 | 8103 |
| table_id | 3221 | 9171 | 8101 |
| location_id | 312 | 270 | 479 |
| promotion_id | 3211 | 3211 | 3211 |
| event_date | 2023-12-29 | 2005-01-17 | 2009-06-30 |
| event_id | 3429 | 238 | 7914 |
| url | http://www.profightdb.com/cards/wwe/wwe-live---holiday-tour-51464.html | http://www.profightdb.com/cards/wwe/monday-night-raw-2428.html | http://www.profightdb.com/cards/wwe/ecw-taping-5090.html |
| info_html | <table border="0" width="100%">  <tr>   <td align="left" height="23" width="40%">    <strong>     Date:    </strong>    <a href="/this-day-in-history/12-29-2023.html">     Fri, Dec 29th 2023    </a>… | <table border="0" width="100%">  <tr>   <td align="left" height="23" width="40%">    <strong>     Date:    </strong>    <a href="/this-day-in-history/01-17-2005.html">     Mon, Jan 17th 2005    </a>… | <table border="0" width="100%">  <tr>   <td align="left" height="23" width="40%">    <strong>     Date:    </strong>    <a href="/this-day-in-history/06-30-2009.html">     Tue, Jun 30th 2009    </a>… |
| match_html | <table cellpadding="0" cellspacing="1" width="100%">  <tr class="head">   <th width="3%">    no.   </th>   <th colspan="3" width="50%">    match   </th>   <th width="5%">    duration   </th>   <th wi… | <table cellpadding="0" cellspacing="1" width="100%">  <tr class="head">   <th width="3%">    no.   </th>   <th colspan="3" width="50%">    match   </th>   <th width="5%">    duration   </th>   <th wi… | <table cellpadding="0" cellspacing="1" width="100%">  <tr class="head">   <th width="3%">    no.   </th>   <th colspan="3" width="50%">    match   </th>   <th width="5%">    duration   </th>   <th wi… |

# "Events"  (rows=5033)

columns:
"id" int PK UNIQ: unique identifier, 1..14341
"name" text UNIQ: unique identifier

indexes: none

samples:
| column | latest | sample | sample |
|---|---|---|---|
| id | 14341 | 2723 | 199 |
| name | Monday Night Raw - Day 1 2024 | Superstars of Wrestling Taping #147 | Washington Show (May '63 #2) |

# "Locations"  (rows=609)

columns:
"id" int PK UNIQ: unique identifier, 1..12645
"name" text UNIQ: unique identifier

indexes: none

samples:
| column | latest | sample | sample |
|---|---|---|---|
| id | 12645 | 400 | 438 |
| name | Plant City, Florida | Uniondale, New York | Baton Rouge, Louisiana |

# "Match_Types"  (rows=1208)

columns:
"id" int PK UNIQ: unique identifier, 1..385709
"name" text UNIQ: unique identifier

indexes: none

samples:
| column | latest | sample | sample |
|---|---|---|---|
| id | 385709 | 12343 | 57696 |
| name | referee: Stevie Turner | $10,000 challenge | scaffold (tag) |

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
| id | 12673 | 1230 | 1530 |
| html | <table cellpadding="0" cellspacing="1">  <tr class="head">   <th>    <a href="?order=date&amp;ppv=no&amp;type=asc" rel="nofollow">     date    </a>   </th>   <th>    <a href="?order=promotion&amp;ppv… | <table cellpadding="0" cellspacing="1">  <tr class="head">   <th>    <a href="?order=date&amp;ppv=no&amp;type=asc" rel="nofollow">     date    </a>   </th>   <th>    <a href="?order=promotion&amp;ppv… | <table cellpadding="0" cellspacing="1">  <tr class="head">   <th>    <a href="?order=date&amp;ppv=no&amp;type=asc" rel="nofollow">     date    </a>   </th>   <th>    <a href="?order=promotion&amp;ppv… |
| url | http://www.profightdb.com/cards/nxt-cards-pg172-no-103.html?order=&type= | http://www.profightdb.com/cards/wwf-cards-pg101-no-1.html?order=&type= | http://www.profightdb.com/cards/wwf-cards-pg131-no-1.html?order=&type= |

# "Wrestlers"  (rows=17182)

columns:
"id" int PK UNIQ: unique identifier, 1..1081588
"name" text: all distinct

indexes: none

samples:
| column | latest | sample | sample |
|---|---|---|---|
| id | 1081588 | 12834 | 102438 |
| name | Elton Prince & Grayson Waller & Kit Wilson | Mideon & The Brooklyn Brawler | Psicosis |
