---
generator: db-snooper
version: 0.0.26
generated_at_utc: 2026-08-16T08:08:43.011046Z
dialect: sqlite
database: /var/folders/9j/b9bx_drd53sc6zbpsqyrjy4h0000gn/T/dbsnoop-8r7yn72o/WWE.sqlite
schema: main
---

# Belts

```sql
CREATE TABLE Belts (
            id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
            name TEXT UNIQUE
    );
```

## Rows

- total=143

| column | latest | sample | sample |
|---|---|---|---|
| id | 70791 | 57137 | 1642 |
| name | EVOLVE Tag Team Titles | WCW Cruiserweight Tag Team Titles | WWF European Title |

## Columns

- id: unique identifier, int 1..70791
- name: unique identifier


# Cards

```sql
CREATE TABLE Cards (
            id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
            table_id INTEGER,
            location_id INTEGER,
            promotion_id INTEGER,
            event_date TEXT,
            event_id INTEGER,
            url TEXT UNIQUE,
            info_html TEXT,
            match_html TEXT UNIQUE
        );
```

## Rows

- total=12639

| column | latest | sample | sample |
|---|---|---|---|
| id | 14344 | 5751 | 122 |
| table_id | 3221 | 5751 | 121 |
| location_id | 312 | 285 | 1 |
| promotion_id | 3211 | 3211 | 1 |
| event_date | 2023-12-29 | 2015-07-02 | 1968-11-18 |
| event_id | 3429 | 551 | 122 |
| url | http://www.profightdb.com/cards/wwe/wwe-live---holiday-tour-51464.html | http://www.profightdb.com/cards/wwe/wwe-live-22063.html | http://www.profightdb.com/cards/wwwf/msg-show-nov-3968-4853.html |
| info_html | <table border="0" width="100%">  <tr>   <td align="left" height="23" width="40%">    <strong>     Date:    </strong>    <a href="/this-day-in-history/12-29-2023.html">     Fri, Dec 29th 2023    </a>   </td>   <td align="left" width="52%">    <strong>     Pay Per View:    </strong>    no   </td>  </tr>  <tr>   <td align="left">    <strong>     Venue:    </strong>    <img alt="United States" height="11" src="/img/flags/us.gif" width="16"/>    <a href="/locations/united-states/nevada/las-vegas/mgm-grand-garden-arena-165.html">     MGM Grand Garden Arena    </a>    ,    <a href="/locations/united-states/nevada/las-vegas-50.html">     Las Vegas    </a>    ,    <a href="/locations/united-states/nevada-33.html">     Nevada    </a>   </td>   <td align="left">    <strong>     Promotion:    </strong>    WWE   </td>  </tr>  <tr>   <td align="left">    <strong>     Attendance:    </strong>    unknown   </td>   <td align="left">    &nbsp;   </td>  </tr> </table>  | <table border="0" width="100%">  <tr>   <td align="left" height="23" width="40%">    <strong>     Date:    </strong>    <a href="/this-day-in-history/07-02-2015.html">     Thu, Jul 2nd 2015    </a>   </td>   <td align="left" width="52%">    <strong>     Pay Per View:    </strong>    no   </td>  </tr>  <tr>   <td align="left">    <strong>     Venue:    </strong>    <img alt="Singapore" height="11" src="/img/flags/05123c2de5singapore-flag.jpg" width="16"/>    <a href="/locations/singapore/central-region/kallang/singapore-indoor-stadium-5661.html">     Singapore Indoor Stadium    </a>    ,    <a href="/locations/singapore/central-region/kallang-4435.html">     Kallang    </a>    ,    <a href="/locations/singapore/central-region-560.html">     Central Region    </a>   </td>   <td align="left">    <strong>     Promotion:    </strong>    WWE   </td>  </tr>  <tr>   <td align="left">    <strong>     Attendance:    </strong>    unknown   </td>   <td align="left">    &nbsp;   </td>  </tr> </table>  | <table border="0" width="100%">  <tr>   <td align="left" height="23" width="40%">    <strong>     Date:    </strong>    <a href="/this-day-in-history/11-18-1968.html">     Mon, Nov 18th 1968    </a>   </td>   <td align="left" width="52%">    <strong>     Pay Per View:    </strong>    no   </td>  </tr>  <tr>   <td align="left">    <strong>     Venue:    </strong>    <img alt="United States" height="11" src="/img/flags/us.gif" width="16"/>    <a href="/locations/united-states/new-york/new-york/madison-square-garden-1.html">     Madison Square Garden    </a>    ,    <a href="/locations/united-states/new-york/new-york-69.html">     New York    </a>    ,    <a href="/locations/united-states/new-york-34.html">     New York    </a>   </td>   <td align="left">    <strong>     Promotion:    </strong>    WWWF   </td>  </tr>  <tr>   <td align="left">    <strong>     Attendance:    </strong>    unknown   </td>   <td align="left">    &nbsp;   </td>  </tr> </table>  |
| match_html | <table cellpadding="0" cellspacing="1" width="100%">  <tr class="head">   <th width="3%">    no.   </th>   <th colspan="3" width="50%">    match   </th>   <th width="5%">    duration   </th>   <th width="19%">    match type   </th>   <th width="18%">    title(s)   </th>   <th width="5%">    rating   </th>  </tr>  <tr class="chequered">   <td>    1   </td>   <td width="22%">    <a href="/wrestlers/aj-styles-752.html">     A.J. Styles    </a>    &amp;    <a href="/wrestlers/karl-anderson-3250.html">     Karl Anderson    </a>    &amp;    <a href="/wrestlers/doc-gallows-448.html">     Luke Gallows    </a>   </td>   <td width="6%">    def.   </td>   <td width="22%">    <a href="/wrestlers/elton-prince-14914.html">     Elton Prince    </a>    &amp;    <a href="/wrestlers/grayson-waller-18406.html">     Grayson Waller    </a>    &amp;    <a href="/wrestlers/kit-wilson-14915.html">     Kit Wilson    </a>   </td>   <td>   </td>   <td>    6-person tag   </td>   <td>   </td>   <td class="center">   </td>  </tr>  <tr>   <td>    2   </td>   <td width="22%">    <a href="/wrestlers/butch-9700.html">     Butch    </a>   </td>   <td width="6%">    def.   </td>   <td width="22%">    <a href="/wrestlers/austin-theory-12876.html">     Austin Theory    </a>   </td>   <td>   </td>   <td>    &nbsp;   </td>   <td>   </td>   <td class="center">   </td>  </tr>  <tr class="chequered">   <td>    3   </td>   <td width="22%">    <a href="/wrestlers/bobby-lashley-434.html">     Bobby Lashley    </a>   </td>   <td width="6%">    def.   </td>   <td width="22%">    <a href="/wrestlers/cameron-grimes-9579.html">     Cameron Grimes    </a>   </td>   <td>   </td>   <td>    &nbsp;   </td>   <td>   </td>   <td class="center">   </td>  </tr>  <tr>   <td>    4   </td>   <td width="22%">    <a href="/wrestlers/kevin-owens-1862.html">     Kevin Owens    </a>   </td>   <td width="6%">    def.   </td>   <td width="22%">    <a href="/wrestlers/solo-sikoa-17257.html">     Solo Sikoa    </a>   </td>   <td>   </td>   <td>    "Last Man Standing"   </td>   <td>   </td>   <td class="center">   </td>  </tr>  <tr class="chequered">   <td>    5   </td>   <td width="22%">    <a href="/wrestlers/angelo-dawkins-9426.html">     Angelo Dawkins    </a>    &amp;    <a href="/wrestlers/montez-ford-12075.html">     Montez Ford    </a>   </td>   <td width="6%">    def.   </td>   <td width="22%">    <a href="/wrestlers/raul-mendoza-10106.html">     Cruz Del Toro    </a>    &amp;    <a href="/wrestlers/joaquin-wilde-3292.html">     Joaquin Wilde    </a>   </td>   <td>   </td>   <td>    &nbsp;   </td>   <td>   </td>   <td class="center">   </td>  </tr>  <tr>   <td>    6   </td>   <td width="22%">    <a href="/wrestlers/bianca-belair-13039.html">     Bianca BelAir    </a>    &amp;    <a href="/wrestlers/shotzi-blackheart-13176.html">     Shotzi    </a>   </td>   <td width="6%">    def.   </td>   <td width="22%">    <a href="/wrestlers/bayley-8206.html">     Bayley    </a>    &amp;    <a href="/wrestlers/iyo-sky-7183.html">     Iyo Sky    </a>   </td>   <td>   </td>   <td>    &nbsp;   </td>   <td>   </td>   <td class="center">   </td>  </tr>  <tr class="chequered">   <td>    7   </td>   <td width="22%">    <a href="/wrestlers/eli-drake-3386.html">     L.A. Knight    </a>   </td>   <td width="6%">    def.   </td>   <td width="22%">    <a href="/wrestlers/jimmy-uso-6303.html">     Jimmy Uso    </a>   </td>   <td>   </td>   <td>    steel cage   </td>   <td>   </td>   <td class="center">   </td>  </tr> </table>  | <table cellpadding="0" cellspacing="1" width="100%">  <tr class="head">   <th width="3%">    no.   </th>   <th colspan="3" width="50%">    match   </th>   <th width="5%">    duration   </th>   <th width="19%">    match type   </th>   <th width="18%">    title(s)   </th>   <th width="5%">    rating   </th>  </tr>  <tr class="chequered">   <td>    1   </td>   <td width="22%">    <a href="/wrestlers/pac-1935.html">     Neville    </a>   </td>   <td width="6%">    def. (pin)   </td>   <td width="22%">    <a href="/wrestlers/kofi-kingston-3295.html">     Kofi Kingston    </a>   </td>   <td>   </td>   <td>    &nbsp;   </td>   <td>   </td>   <td class="center">   </td>  </tr>  <tr>   <td>    2   </td>   <td width="22%">    <a href="/wrestlers/kalisto-6604.html">     Kalisto    </a>    &amp;    <a href="/wrestlers/cinta-de-oro-927.html">     Sin Cara    </a>   </td>   <td width="6%">    def. (pin)   </td>   <td width="22%">    <a href="/wrestlers/primo-3240.html">     Diego    </a>    &amp;    <a href="/wrestlers/epico-3404.html">     Fernando    </a>   </td>   <td>   </td>   <td>    &nbsp;   </td>   <td>   </td>   <td class="center">   </td>  </tr>  <tr class="chequered">   <td>    3   </td>   <td width="22%">    <a href="/wrestlers/finn-balor-3023.html">     Finn B&aacute;lor    </a>   </td>   <td width="6%">    def. (pin)   </td>   <td width="22%">    <a href="/wrestlers/wade-barrett-6096.html">     King Barrett    </a>   </td>   <td>   </td>   <td>    &nbsp;   </td>   <td>   </td>   <td class="center">   </td>  </tr>  <tr>   <td>    4   </td>   <td width="22%">    <a href="/wrestlers/dolph-ziggler-450.html">     Dolph Ziggler    </a>   </td>   <td width="6%">    def. (pin)   </td>   <td width="22%">    <a href="/wrestlers/kane-197.html">     Kane    </a>   </td>   <td>   </td>   <td>    street fight   </td>   <td>   </td>   <td class="center">   </td>  </tr>  <tr class="chequered">   <td>    5   </td>   <td width="22%">    <a href="/wrestlers/nikki-bella-3341.html">     Nikki Bella    </a>    &nbsp;(c)   </td>   <td width="6%">    def. (pin)   </td>   <td width="22%">    <a href="/wrestlers/tamina-6310.html">     Tamina Snuka    </a>   </td>   <td>   </td>   <td>    &nbsp;   </td>   <td>    WWE Divas Championship    <br/>   </td>   <td class="center">   </td>  </tr>  <tr>   <td>    6   </td>   <td width="22%">    <a href="/wrestlers/claudio-castagnoli-1874.html">     Cesaro    </a>   </td>   <td width="6%">    def. (sub)   </td>   <td width="22%">    <a href="/wrestlers/big-e-6446.html">     Big E    </a>   </td>   <td>   </td>   <td>    &nbsp;   </td>   <td>   </td>   <td class="center">   </td>  </tr>  <tr class="chequered">   <td>    7   </td>   <td width="22%">    <a href="/wrestlers/john-cena-350.html">     John Cena    </a>   </td>   <td width="6%">    def. (DQ)   </td>   <td width="22%">    <a href="/wrestlers/kevin-owens-1862.html">     Kevin Owens    </a>   </td>   <td>   </td>   <td>    &nbsp;   </td>   <td>   </td>   <td class="center">   </td>  </tr> </table>  | <table cellpadding="0" cellspacing="1" width="100%">  <tr class="head">   <th width="3%">    no.   </th>   <th colspan="3" width="50%">    match   </th>   <th width="5%">    duration   </th>   <th width="19%">    match type   </th>   <th width="18%">    title(s)   </th>   <th width="5%">    rating   </th>  </tr>  <tr class="chequered">   <td>    1   </td>   <td width="22%">    <a href="/wrestlers/captain-lou-albano-945.html">     Captain Lou Albano    </a>   </td>   <td width="6%">    def.   </td>   <td width="22%">    <a href="/wrestlers/angelo-savoldi-3305.html">     Angelo Savoldi    </a>   </td>   <td>   </td>   <td>    &nbsp;   </td>   <td>   </td>   <td class="center">   </td>  </tr>  <tr>   <td>    2   </td>   <td width="22%">    <a href="/wrestlers/tony-altimore-4989.html">     Tony Altimore    </a>   </td>   <td width="6%">    def.   </td>   <td width="22%">    <a href="/wrestlers/jack-armstrong-4999.html">     Lenny Solomon    </a>   </td>   <td>   </td>   <td>    &nbsp;   </td>   <td>   </td>   <td class="center">   </td>  </tr>  <tr class="chequered">   <td>    3   </td>   <td width="22%">    <a href="/wrestlers/johnny-rodz-948.html">     Johnny Rodz    </a>   </td>   <td width="6%">    def. (DQ)   </td>   <td width="22%">    <a href="/wrestlers/chuck-adcox-5003.html">     Chuck Adcox    </a>   </td>   <td>   </td>   <td>    &nbsp;   </td>   <td>   </td>   <td class="center">   </td>  </tr>  <tr>   <td>    4   </td>   <td width="22%">    <a href="/wrestlers/pete-sanchez-3721.html">     Pete Sanchez    </a>   </td>   <td width="6%">    def. (DQ)   </td>   <td width="22%">    <a href="/wrestlers/bull-ramos-4992.html">     Bull Ramos    </a>   </td>   <td>   </td>   <td>    &nbsp;   </td>   <td>   </td>   <td class="center">   </td>  </tr>  <tr class="chequered">   <td>    5   </td>   <td width="22%">    <a href="/wrestlers/bob-orton-sr-5004.html">     Rocky Fitzpatrick    </a>   </td>   <td width="6%">    def.   </td>   <td width="22%">    <a href="/wrestlers/ernie-lassiter-5005.html">     Ernie Lassiter    </a>   </td>   <td>   </td>   <td>    &nbsp;   </td>   <td>   </td>   <td class="center">   </td>  </tr>  <tr>   <td>    6   </td>   <td width="22%">    <a href="/wrestlers/haystacks-calhoun-4958.html">     Haystacks Calhoun    </a>    &amp;    <a href="/wrestlers/spiros-arion-4983.html">     Spiros Arion    </a>    &amp;    <a href="/wrestlers/victor-rivera-4991.html">     Victor Rivera    </a>   </td>   <td width="6%">    def.   </td>   <td width="22%">    <a href="/wrestlers/baron-mikel-scicluna-944.html">     Baron Mikel Scicluna    </a>    &amp;    <a href="/wrestlers/gorilla-monsoon-939.html">     Gorilla Monsoon    </a>    &amp;    <a href="/wrestlers/john-quinn-4815.html">     Virgil the Kentucky Butcher    </a>   </td>   <td>   </td>   <td>    6-person tag   </td>   <td>   </td>   <td class="center">   </td>  </tr>  <tr class="chequered">   <td>    7   </td>   <td width="22%">    <a href="/wrestlers/bruno-sammartino-55.html">     Bruno Sammartino    </a>    &nbsp;(c)   </td>   <td width="6%">    def. (DQ)   </td>   <td width="22%">    <a href="/wrestlers/the-sheik-957.html">     The Sheik    </a>   </td>   <td>    06:14   </td>   <td>    &nbsp;   </td>   <td>    WWWF World Heavyweight Title    <br/>   </td>   <td class="center">   </td>  </tr> </table>  |

## Columns

- id: unique identifier, int 1..14344
- table_id: 1270 distinct, int 1..12673
- location_id: 596 distinct, int 1..12645
- promotion_id: 3211=6616, 230=2967, 10963=1749, 9876=1078, 1=229, int 1..10963
- event_date: 6782 distinct
- event_id: 5020 distinct, int 1..14341
- url: unique identifier
- info_html: 8705 distinct
- match_html: unique identifier


# Events

```sql
CREATE TABLE Events (
            id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
            name TEXT UNIQUE
        );
```

## Rows

- total=5033

| column | latest | sample | sample |
|---|---|---|---|
| id | 14341 | 12424 | 131 |
| name | Monday Night Raw - Day 1 2024 | TV Taping #128 | MSG Show (Oct '67) |

## Columns

- id: unique identifier, int 1..14341
- name: unique identifier


# Locations

```sql
CREATE TABLE Locations (
            id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
            name TEXT UNIQUE
        );
```

## Rows

- total=609

| column | latest | sample | sample |
|---|---|---|---|
| id | 12645 | 3464 | 2369 |
| name | Plant City, Florida | Allentown, Pennsylvania | Fairbanks, Alaska |

## Columns

- id: unique identifier, int 1..12645
- name: unique identifier


# Match_Types

```sql
CREATE TABLE Match_Types (
            id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
            name TEXT UNIQUE
    );
```

## Rows

- total=1208

| column | latest | sample | sample |
|---|---|---|---|
| id | 385709 | 5235 | 64666 |
| name | referee: Stevie Turner | "Brooklyn Strap" | leather strap |

## Columns

- id: unique identifier, int 1..385709
- name: unique identifier


# Matches

```sql
CREATE TABLE Matches (
            id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
            card_id INTEGER,
            winner_id TEXT,
            win_type TEXT,
            loser_id TEXT,
            match_type_id TEXT,
            duration TEXT,
            title_id TEXT,
            title_change INTEGER
    );
```

## Rows

- total≈540800 (estimated from db stats; row/column profiling skipped)


# Promotions

## All rows

| column | row 1 | row 2 | row 3 | row 4 | row 5 | row 6 |
|---|---|---|---|---|---|---|
| id | 1 | 230 | 3211 | 9876 | 10963 | 12682 |
| name | WWWF | WWF | WWE | WCW | NXT | ECW |


# Tables

```sql
CREATE TABLE Tables (
            id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
            html TEXT UNIQUE,
            url TEXT UNIQUE
        );
```

## Rows

- total=1270

| column | latest | sample | sample |
|---|---|---|---|
| id | 12673 | 2130 | 870 |
| html | <table cellpadding="0" cellspacing="1">  <tr class="head">   <th>    <a href="?order=date&amp;ppv=no&amp;type=asc" rel="nofollow">     date    </a>   </th>   <th>    <a href="?order=promotion&amp;ppv=no&amp;type=asc" rel="nofollow">     promotion    </a>   </th>   <th>    <a href="?order=card&amp;ppv=no&amp;type=asc" rel="nofollow">     card name    </a>   </th>   <th>    location   </th>  </tr>  <tr class="gray">   <td>    <a href="/this-day-in-history/07-11-2012.html">     Jul 11th 2012    </a>   </td>   <td>    <a class="black" href="/cards/nxt-cards-pg1-no-103.html">     <strong>      NXT     </strong>    </a>   </td>   <td>    <a href="/cards/nxt/tv-taping-9-16002.html">     TV Taping #9    </a>   </td>   <td class="gray">    <img alt="" src="/img/flags/us.gif">     <a href="/locations/united-states/florida/winter-park-2581.html">      Winter Park     </a>     ,     <a href="/locations/united-states/florida-9.html">      Florida     </a>    </img>   </td>  </tr>  <tr class="gray">   <td>    <a href="/this-day-in-history/07-11-2012.html">     Jul 11th 2012    </a>   </td>   <td>    <a class="black" href="/cards/nxt-cards-pg1-no-103.html">     <strong>      NXT     </strong>    </a>   </td>   <td>    <a href="/cards/nxt/tv-taping-8-16001.html">     TV Taping #8    </a>   </td>   <td class="gray">    <img alt="" src="/img/flags/us.gif">     <a href="/locations/united-states/florida/winter-park-2581.html">      Winter Park     </a>     ,     <a href="/locations/united-states/florida-9.html">      Florida     </a>    </img>   </td>  </tr>  <tr class="gray">   <td>    <a href="/this-day-in-history/07-11-2012.html">     Jul 11th 2012    </a>   </td>   <td>    <a class="black" href="/cards/nxt-cards-pg1-no-103.html">     <strong>      NXT     </strong>    </a>   </td>   <td>    <a href="/cards/nxt/tv-taping-7-16000.html">     TV Taping #7    </a>   </td>   <td class="gray">    <img alt="" src="/img/flags/us.gif">     <a href="/locations/united-states/florida/winter-park-2581.html">      Winter Park     </a>     ,     <a href="/locations/united-states/florida-9.html">      Florida     </a>    </img>   </td>  </tr>  <tr class="gray">   <td>    <a href="/this-day-in-history/06-13-2012.html">     Jun 13th 2012    </a>   </td>   <td>    <a class="black" href="/cards/nxt-cards-pg1-no-103.html">     <strong>      NXT     </strong>    </a>   </td>   <td>    <a href="/cards/nxt/tv-taping-6-15922.html">     TV Taping #6    </a>   </td>   <td class="gray">    <img alt="" src="/img/flags/us.gif">     <a href="/locations/united-states/florida/winter-park-2581.html">      Winter Park     </a>     ,     <a href="/locations/united-states/florida-9.html">      Florida     </a>    </img>   </td>  </tr>  <tr class="gray">   <td>    <a href="/this-day-in-history/06-13-2012.html">     Jun 13th 2012    </a>   </td>   <td>    <a class="black" href="/cards/nxt-cards-pg1-no-103.html">     <strong>      NXT     </strong>    </a>   </td>   <td>    <a href="/cards/nxt/tv-taping-5-15921.html">     TV Taping #5    </a>   </td>   <td class="gray">    <img alt="" src="/img/flags/us.gif">     <a href="/locations/united-states/florida/winter-park-2581.html">      Winter Park     </a>     ,     <a href="/locations/united-states/florida-9.html">      Florida     </a>    </img>   </td>  </tr>  <tr class="gray">   <td>    <a href="/this-day-in-history/06-13-2012.html">     Jun 13th 2012    </a>   </td>   <td>    <a class="black" href="/cards/nxt-cards-pg1-no-103.html">     <strong>      NXT     </strong>    </a>   </td>   <td>    <a href="/cards/nxt/tv-taping-4-15920.html">     TV Taping #4    </a>   </td>   <td class="gray">    <img alt="" src="/img/flags/us.gif">     <a href="/locations/united-states/florida/winter-park-2581.html">      Winter Park     </a>     ,     <a href="/locations/united-states/florida-9.html">      Florida     </a>    </img>   </td>  </tr>  <tr class="gray">   <td>    <a href="/this-day-in-history/05-17-2012.html">     May 17th 2012    </a>   </td>   <td>    <a class="black" href="/cards/nxt-cards-pg1-no-103.html">     <strong>      NXT     </strong>    </a>   </td>   <td>    <a href="/cards/nxt/tv-taping-3-15790.html">     TV Taping #3    </a>   </td>   <td class="gray">    <img alt="" src="/img/flags/us.gif">     <a href="/locations/united-states/florida/winter-park-2581.html">      Winter Park     </a>     ,     <a href="/locations/united-states/florida-9.html">      Florida     </a>    </img>   </td>  </tr>  <tr class="gray">   <td>    <a href="/this-day-in-history/05-17-2012.html">     May 17th 2012    </a>   </td>   <td>    <a class="black" href="/cards/nxt-cards-pg1-no-103.html">     <strong>      NXT     </strong>    </a>   </td>   <td>    <a href="/cards/nxt/tv-taping-2-15789.html">     TV Taping #2    </a>   </td>   <td class="gray">    <img alt="" src="/img/flags/us.gif">     <a href="/locations/united-states/florida/winter-park-2581.html">      Winter Park     </a>     ,     <a href="/locations/united-states/florida-9.html">      Florida     </a>    </img>   </td>  </tr>  <tr class="gray">   <td>    <a href="/this-day-in-history/05-17-2012.html">     May 17th 2012    </a>   </td>   <td>    <a class="black" href="/cards/nxt-cards-pg1-no-103.html">     <strong>      NXT     </strong>    </a>   </td>   <td>    <a href="/cards/nxt/tv-taping-1-15788.html">     TV Taping #1    </a>   </td>   <td class="gray">    <img alt="" src="/img/flags/us.gif">     <a href="/locations/united-states/florida/winter-park-2581.html">      Winter Park     </a>     ,     <a href="/locations/united-states/florida-9.html">      Florida     </a>    </img>   </td>  </tr> </table>  | <table cellpadding="0" cellspacing="1">  <tr class="head">   <th>    <a href="?order=date&amp;ppv=no&amp;type=asc" rel="nofollow">     date    </a>   </th>   <th>    <a href="?order=promotion&amp;ppv=no&amp;type=asc" rel="nofollow">     promotion    </a>   </th>   <th>    <a href="?order=card&amp;ppv=no&amp;type=asc" rel="nofollow">     card name    </a>   </th>   <th>    location   </th>  </tr>  <tr class="gray">   <td>    <a href="/this-day-in-history/05-24-1993.html">     May 24th 1993    </a>   </td>   <td>    <a class="black" href="/cards/wwf-cards-pg1-no-1.html">     <strong>      WWF     </strong>    </a>   </td>   <td>    <a href="/cards/wwf/superstars-of-wrestling-taping-352-12968.html">     Superstars of Wrestling Taping #352    </a>   </td>   <td class="gray">    <img alt="" src="/img/flags/ca.gif">     <a href="/locations/canada/nova-scotia/halifax-202.html">      Halifax     </a>     ,     <a href="/locations/canada/nova-scotia-58.html">      Nova Scotia     </a>    </img>   </td>  </tr>  <tr class="gray">   <td>    <a href="/this-day-in-history/05-24-1993.html">     May 24th 1993    </a>   </td>   <td>    <a class="black" href="/cards/wwf-cards-pg1-no-1.html">     <strong>      WWF     </strong>    </a>   </td>   <td>    <a href="/cards/wwf/superstars-of-wrestling-taping-351-12967.html">     Superstars of Wrestling Taping #351    </a>   </td>   <td class="gray">    <img alt="" src="/img/flags/ca.gif">     <a href="/locations/canada/nova-scotia/halifax-202.html">      Halifax     </a>     ,     <a href="/locations/canada/nova-scotia-58.html">      Nova Scotia     </a>    </img>   </td>  </tr>  <tr class="gray">   <td>    <a href="/this-day-in-history/05-24-1993.html">     May 24th 1993    </a>   </td>   <td>    <a class="black" href="/cards/wwf-cards-pg1-no-1.html">     <strong>      WWF     </strong>    </a>   </td>   <td>    <a href="/cards/wwf/superstars-of-wrestling-taping-350-12966.html">     Superstars of Wrestling Taping #350    </a>   </td>   <td class="gray">    <img alt="" src="/img/flags/ca.gif">     <a href="/locations/canada/nova-scotia/halifax-202.html">      Halifax     </a>     ,     <a href="/locations/canada/nova-scotia-58.html">      Nova Scotia     </a>    </img>   </td>  </tr>  <tr class="gray">   <td>    <a href="/this-day-in-history/05-17-1993.html">     May 17th 1993    </a>   </td>   <td>    <a class="black" href="/cards/wwf-cards-pg1-no-1.html">     <strong>      WWF     </strong>    </a>   </td>   <td>    <a href="/cards/wwf/monday-night-raw-taping-821.html">     Monday Night Raw Taping    </a>   </td>   <td class="gray">    <img alt="" src="/img/flags/us.gif">     <a href="/locations/united-states/new-york/new-york-69.html">      New York     </a>     ,     <a href="/locations/united-states/new-york-34.html">      New York     </a>    </img>   </td>  </tr>  <tr class="gray">   <td>    <a href="/this-day-in-history/05-17-1993.html">     May 17th 1993    </a>   </td>   <td>    <a class="black" href="/cards/wwf-cards-pg1-no-1.html">     <strong>      WWF     </strong>    </a>   </td>   <td>    <a href="/cards/wwf/monday-night-raw-820.html">     Monday Night Raw    </a>   </td>   <td class="gray">    <img alt="" src="/img/flags/us.gif">     <a href="/locations/united-states/new-york/new-york-69.html">      New York     </a>     ,     <a href="/locations/united-states/new-york-34.html">      New York     </a>    </img>   </td>  </tr>  <tr class="gray">   <td>    <a href="/this-day-in-history/05-10-1993.html">     May 10th 1993    </a>   </td>   <td>    <a class="black" href="/cards/wwf-cards-pg1-no-1.html">     <strong>      WWF     </strong>    </a>   </td>   <td>    <a href="/cards/wwf/monday-night-raw-819.html">     Monday Night Raw    </a>   </td>   <td class="gray">    <img alt="" src="/img/flags/us.gif">     <a href="/locations/united-states/new-york/new-york-69.html">      New York     </a>     ,     <a href="/locations/united-states/new-york-34.html">      New York     </a>    </img>   </td>  </tr>  <tr class="gray">   <td>    <a href="/this-day-in-history/05-05-1993.html">     May 5th 1993    </a>   </td>   <td>    <a class="black" href="/cards/wwf-cards-pg1-no-1.html">     <strong>      WWF     </strong>    </a>   </td>   <td>    <a href="/cards/wwf/wrestling-challenge-taping-351-15277.html">     Wrestling Challenge Taping #351    </a>   </td>   <td class="gray">    <img alt="" src="/img/flags/us.gif">     <a href="/locations/united-states/maine/portland-208.html">      Portland     </a>     ,     <a href="/locations/united-states/maine-21.html">      Maine     </a>    </img>   </td>  </tr>  <tr class="gray">   <td>    <a href="/this-day-in-history/05-05-1993.html">     May 5th 1993    </a>   </td>   <td>    <a class="black" href="/cards/wwf-cards-pg1-no-1.html">     <strong>      WWF     </strong>    </a>   </td>   <td>    <a href="/cards/wwf/wrestling-challenge-taping-350-15276.html">     Wrestling Challenge Taping #350    </a>   </td>   <td class="gray">    <img alt="" src="/img/flags/us.gif">     <a href="/locations/united-states/maine/portland-208.html">      Portland     </a>     ,     <a href="/locations/united-states/maine-21.html">      Maine     </a>    </img>   </td>  </tr>  <tr class="gray">   <td>    <a href="/this-day-in-history/05-05-1993.html">     May 5th 1993    </a>   </td>   <td>    <a class="black" href="/cards/wwf-cards-pg1-no-1.html">     <strong>      WWF     </strong>    </a>   </td>   <td>    <a href="/cards/wwf/wrestling-challenge-taping-349-15275.html">     Wrestling Challenge Taping #349    </a>   </td>   <td class="gray">    <img alt="" src="/img/flags/us.gif">     <a href="/locations/united-states/maine/portland-208.html">      Portland     </a>     ,     <a href="/locations/united-states/maine-21.html">      Maine     </a>    </img>   </td>  </tr>  <tr class="gray">   <td>    <a href="/this-day-in-history/05-04-1993.html">     May 4th 1993    </a>   </td>   <td>    <a class="black" href="/cards/wwf-cards-pg1-no-1.html">     <strong>      WWF     </strong>    </a>   </td>   <td>    <a href="/cards/wwf/superstars-of-wrestling-taping-349-12965.html">     Superstars of Wrestling Taping #349    </a>   </td>   <td class="gray">    <img alt="" src="/img/flags/us.gif">     <a href="/locations/united-states/massachusetts/worcester-122.html">      Worcester     </a>     ,     <a href="/locations/united-states/massachusetts-19.html">      Massachusetts     </a>    </img>   </td>  </tr> </table>  | <table cellpadding="0" cellspacing="1">  <tr class="head">   <th>    <a href="?order=date&amp;ppv=no&amp;type=asc" rel="nofollow">     date    </a>   </th>   <th>    <a href="?order=promotion&amp;ppv=no&amp;type=asc" rel="nofollow">     promotion    </a>   </th>   <th>    <a href="?order=card&amp;ppv=no&amp;type=asc" rel="nofollow">     card name    </a>   </th>   <th>    location   </th>  </tr>  <tr class="gray">   <td>    <a href="/this-day-in-history/03-27-2000.html">     Mar 27th 2000    </a>   </td>   <td>    <a class="black" href="/cards/wwf-cards-pg1-no-1.html">     <strong>      WWF     </strong>    </a>   </td>   <td>    <a href="/cards/wwf/jakked-32-taping-1273.html">     Jakked #32 Taping    </a>   </td>   <td class="gray">    <img alt="" src="/img/flags/us.gif">     <a href="/locations/united-states/texas/houston-42.html">      Houston     </a>     ,     <a href="/locations/united-states/texas-43.html">      Texas     </a>    </img>   </td>  </tr>  <tr class="gray">   <td>    <a href="/this-day-in-history/03-21-2000.html">     Mar 21st 2000    </a>   </td>   <td>    <a class="black" href="/cards/wwf-cards-pg1-no-1.html">     <strong>      WWF     </strong>    </a>   </td>   <td>    <a href="/cards/wwf/smackdown-taping-1271.html">     Smackdown! Taping    </a>   </td>   <td class="gray">    <img alt="" src="/img/flags/us.gif">     <a href="/locations/united-states/wisconsin/milwaukee-61.html">      Milwaukee     </a>     ,     <a href="/locations/united-states/wisconsin-48.html">      Wisconsin     </a>    </img>   </td>  </tr>  <tr class="gray">   <td>    <a href="/this-day-in-history/03-21-2000.html">     Mar 21st 2000    </a>   </td>   <td>    <a class="black" href="/cards/wwf-cards-pg1-no-1.html">     <strong>      WWF     </strong>    </a>   </td>   <td>    <a href="/cards/wwf/sunday-night-heat-87-taping-1270.html">     Sunday Night Heat #87 Taping    </a>   </td>   <td class="gray">    <img alt="" src="/img/flags/us.gif">     <a href="/locations/united-states/wisconsin/milwaukee-61.html">      Milwaukee     </a>     ,     <a href="/locations/united-states/wisconsin-48.html">      Wisconsin     </a>    </img>   </td>  </tr>  <tr class="gray">   <td>    <a href="/this-day-in-history/03-20-2000.html">     Mar 20th 2000    </a>   </td>   <td>    <a class="black" href="/cards/wwf-cards-pg1-no-1.html">     <strong>      WWF     </strong>    </a>   </td>   <td>    <a href="/cards/wwf/monday-night-raw-1269.html">     Monday Night Raw    </a>   </td>   <td class="gray">    <img alt="" src="/img/flags/us.gif">     <a href="/locations/united-states/illinois/chicago-23.html">      Chicago     </a>     ,     <a href="/locations/united-states/illinois-14.html">      Illinois     </a>    </img>   </td>  </tr>  <tr class="gray">   <td>    <a href="/this-day-in-history/03-20-2000.html">     Mar 20th 2000    </a>   </td>   <td>    <a class="black" href="/cards/wwf-cards-pg1-no-1.html">     <strong>      WWF     </strong>    </a>   </td>   <td>    <a href="/cards/wwf/jakked-31-taping-1268.html">     Jakked #31 Taping    </a>   </td>   <td class="gray">    <img alt="" src="/img/flags/us.gif">     <a href="/locations/united-states/illinois/chicago-23.html">      Chicago     </a>     ,     <a href="/locations/united-states/illinois-14.html">      Illinois     </a>    </img>   </td>  </tr>  <tr class="gray">   <td>    <a href="/this-day-in-history/03-14-2000.html">     Mar 14th 2000    </a>   </td>   <td>    <a class="black" href="/cards/wwf-cards-pg1-no-1.html">     <strong>      WWF     </strong>    </a>   </td>   <td>    <a href="/cards/wwf/smackdown-taping-1267.html">     Smackdown! Taping    </a>   </td>   <td class="gray">    <img alt="" src="/img/flags/us.gif">     <a href="/locations/united-states/new-york/uniondale-115.html">      Uniondale     </a>     ,     <a href="/locations/united-states/new-york-34.html">      New York     </a>    </img>   </td>  </tr>  <tr class="gray">   <td>    <a href="/this-day-in-history/03-14-2000.html">     Mar 14th 2000    </a>   </td>   <td>    <a class="black" href="/cards/wwf-cards-pg1-no-1.html">     <strong>      WWF     </strong>    </a>   </td>   <td>    <a href="/cards/wwf/sunday-night-heat-86-taping-1266.html">     Sunday Night Heat #86 Taping    </a>   </td>   <td class="gray">    <img alt="" src="/img/flags/us.gif">     <a href="/locations/united-states/new-york/uniondale-115.html">      Uniondale     </a>     ,     <a href="/locations/united-states/new-york-34.html">      New York     </a>    </img>   </td>  </tr>  <tr class="gray">   <td>    <a href="/this-day-in-history/03-13-2000.html">     Mar 13th 2000    </a>   </td>   <td>    <a class="black" href="/cards/wwf-cards-pg1-no-1.html">     <strong>      WWF     </strong>    </a>   </td>   <td>    <a href="/cards/wwf/monday-night-raw-1265.html">     Monday Night Raw    </a>   </td>   <td class="gray">    <img alt="" src="/img/flags/us.gif">     <a href="/locations/united-states/new-jersey/east-rutherford-33.html">      East Rutherford     </a>     ,     <a href="/locations/united-states/new-jersey-31.html">      New Jersey     </a>    </img>   </td>  </tr>  <tr class="gray">   <td>    <a href="/this-day-in-history/03-13-2000.html">     Mar 13th 2000    </a>   </td>   <td>    <a class="black" href="/cards/wwf-cards-pg1-no-1.html">     <strong>      WWF     </strong>    </a>   </td>   <td>    <a href="/cards/wwf/jakked-30-taping-1264.html">     Jakked #30 Taping    </a>   </td>   <td class="gray">    <img alt="" src="/img/flags/us.gif">     <a href="/locations/united-states/new-jersey/east-rutherford-33.html">      East Rutherford     </a>     ,     <a href="/locations/united-states/new-jersey-31.html">      New Jersey     </a>    </img>   </td>  </tr>  <tr class="gray">   <td>    <a href="/this-day-in-history/03-07-2000.html">     Mar 7th 2000    </a>   </td>   <td>    <a class="black" href="/cards/wwf-cards-pg1-no-1.html">     <strong>      WWF     </strong>    </a>   </td>   <td>    <a href="/cards/wwf/smackdown-taping-1263.html">     Smackdown! Taping    </a>   </td>   <td class="gray">    <img alt="" src="/img/flags/us.gif">     <a href="/locations/united-states/massachusetts/boston-16.html">      Boston     </a>     ,     <a href="/locations/united-states/massachusetts-19.html">      Massachusetts     </a>    </img>   </td>  </tr> </table>  |
| url | http://www.profightdb.com/cards/nxt-cards-pg172-no-103.html?order=&type= | http://www.profightdb.com/cards/wwf-cards-pg191-no-1.html?order=&type= | http://www.profightdb.com/cards/wwf-cards-pg65-no-1.html?order=&type= |

## Columns

- id: unique identifier, int 1..12673
- html: unique identifier
- url: unique identifier


# Wrestlers

```sql
CREATE TABLE Wrestlers (
            id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
            name UNIQUE
    );
```

## Rows

- total=17182

| column | latest | sample | sample |
|---|---|---|---|
| id | 1081588 | 24944 | 127489 |
| name | Elton Prince & Grayson Waller & Kit Wilson | Jacques Rougeau & Johnny Polo & Pierre Ouellette | Marcus Alexander Bagwell |

## Columns

- id: unique identifier, int 1..1081588
- name: all distinct
