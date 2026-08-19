---
generator: db-snooper
version: 0.0.26
generated_at_utc: 2026-08-16T08:09:26.129048Z
dialect: sqlite
database: /var/folders/9j/b9bx_drd53sc6zbpsqyrjy4h0000gn/T/dbsnoop-fhz1th7x/northwind.sqlite
schema: main
---

# categories

## All rows

| column | row 1 | row 2 | row 3 | row 4 | row 5 | row 6 | row 7 | row 8 |
|---|---|---|---|---|---|---|---|---|
| categoryid | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 |
| categoryname | Beverages | Condiments | Confections | Dairy Products | Grains/Cereals | Meat/Poultry | Produce | Seafood |
| description | Soft drinks, coffees, teas, beers, and ales | Sweet and savory sauces, relishes, spreads, and seasonings | Desserts, candies, and sweet breads | Cheeses | Breads, crackers, pasta, and cereal | Prepared meats | Dried fruit and bean curd | Seaweed and fish |
| picture | \x | \x | \x | \x | \x | \x | \x | \x |


# customergroupthreshold

## All rows

| column | row 1 | row 2 | row 3 | row 4 |
|---|---|---|---|---|
| groupname | High | Low | Medium | Very High |
| rangebottom | 5000.0000000000 | 0E-10 | 1000.0000000000 | 10000.0000000000 |
| rangetop | 9999.9999000000 | 999.9999000000 | 4999.9999000000 | 922337203685477.6250000000 |


# customers

```sql
CREATE TABLE customers (
    customerid TEXT NOT NULL,
    companyname TEXT NOT NULL,
    contactname TEXT,
    contacttitle TEXT,
    address TEXT,
    city TEXT,
    region TEXT,
    postalcode TEXT,
    country TEXT,
    phone TEXT,
    fax TEXT
);
```

## Rows

- total=91

| column | latest | sample | sample |
|---|---|---|---|
| customerid | WOLZA | LAUGB | NORTS |
| companyname | Wolski  Zajazd | Laughing Bacchus Wine Cellars | North/South |
| contactname | Zbyszek Piestrzeniewicz | Yoshi Tannamuri | Simon Crowther |
| contacttitle | Owner | Marketing Assistant | Sales Associate |
| address | ul. Filtrowa 68 | 1900 Oak St. | South House 300 Queensbridge |
| city | Warszawa | Vancouver | London |
| region | null | BC | null |
| postalcode | 01-012 | V3F 2K1 | SW7 1RZ |
| country | Poland | Canada | UK |
| phone | (26) 642-7012 | (604) 555-3392 | (171) 555-7733 |
| fax | (26) 642-7012 | (604) 555-7293 | (171) 555-2530 |

## Columns

- customerid: unique identifier
- companyname: all distinct
- contactname: all distinct
- contacttitle: "Owner"=17, "Sales Representative"=17, "Marketing Manager"=12, "Sales Manager"=11, "Accounting Manager"=10, "Sales Associate"=7, "Marketing Assistant"=6, "Sales Agent"=5, "Assistant Sales Agent"=2, "Order Administrator"=2, "Assistant Sales Representative"=1, "Owner/Marketing Assistant"=1
- address: all distinct
- city: 69 distinct
- region: "SP"=6, "OR"=4, "RJ"=3, "WA"=3, "BC"=2, "AK"=1, "CA"=1, "Co. Cork"=1, "DF"=1, "ID"=1, "Isle of Wight"=1, "Lara"=1, "MT"=1, "NM"=1, "Nueva Esparta"=1, "Québec"=1, "Táchira"=1, "WY"=1, nulls=60
- postalcode: 86 distinct, nulls=1
- country: 21 distinct
- phone: all distinct
- fax: all distinct, nulls=22


# employees

## All rows

| column | row 1 | row 2 | row 3 | row 4 | row 5 | row 6 | row 7 | row 8 | row 9 |
|---|---|---|---|---|---|---|---|---|---|
| employeeid | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9 |
| lastname | Davolio | Fuller | Leverling | Peacock | Buchanan | Suyama | King | Callahan | Dodsworth |
| firstname | Nancy | Andrew | Janet | Margaret | Steven | Michael | Robert | Laura | Anne |
| title | Sales Representative | Vice President, Sales | Sales Representative | Sales Representative | Sales Manager | Sales Representative | Sales Representative | Inside Sales Coordinator | Sales Representative |
| titleofcourtesy | Ms. | Dr. | Ms. | Mrs. | Mr. | Mr. | Mr. | Ms. | Ms. |
| birthdate | 1948-12-08 | 1952-02-19 | 1963-08-30 | 1937-09-19 | 1955-03-04 | 1963-07-02 | 1960-05-29 | 1958-01-09 | 1966-01-27 |
| hiredate | 1992-05-01 | 1992-08-14 | 1992-04-01 | 1993-05-03 | 1993-10-17 | 1993-10-17 | 1994-01-02 | 1994-03-05 | 1994-11-15 |
| address | 507 - 20th Ave. E.\nApt. 2A | 908 W. Capital Way | 722 Moss Bay Blvd. | 4110 Old Redmond Rd. | 14 Garrett Hill | Coventry House\nMiner Rd. | Edgeham Hollow\nWinchester Way | 4726 - 11th Ave. N.E. | 7 Houndstooth Rd. |
| city | Seattle | Tacoma | Kirkland | Redmond | London | London | London | Seattle | London |
| region | WA | WA | WA | WA | null | null | null | WA | null |
| postalcode | 98122 | 98401 | 98033 | 98052 | SW1 8JR | EC2 7JR | RG1 9SP | 98105 | WG2 7LT |
| country | USA | USA | USA | USA | UK | UK | UK | USA | UK |
| homephone | (206) 555-9857 | (206) 555-9482 | (206) 555-3412 | (206) 555-8122 | (71) 555-4848 | (71) 555-7773 | (71) 555-5598 | (206) 555-1189 | (71) 555-4444 |
| extension | 5467 | 3457 | 3355 | 5176 | 3453 | 428 | 465 | 2344 | 452 |
| photo | \x | \x | \x | \x | \x | \x | \x | \x | \x |
| notes | Education includes a BA in psychology from Colorado State University in 1970.  She also completed The Art of the Cold Call.  Nancy is a member of Toastmasters International. | Andrew received his BTS commercial in 1974 and a Ph.D. in international marketing from the University of Dallas in 1981.  He is fluent in French and Italian and reads German.  He joined the company as a sales representative, was promoted to sales manager in January 1992 and to vice president of sales in March 1993.  Andrew is a member of the Sales Management Roundtable, the Seattle Chamber of Commerce, and the Pacific Rim Importers Association. | Janet has a BS degree in chemistry from Boston College (1984).  She has also completed a certificate program in food retailing management.  Janet was hired as a sales associate in 1991 and promoted to sales representative in February 1992. | Margaret holds a BA in English literature from Concordia College (1958) and an MA from the American Institute of Culinary Arts (1966).  She was assigned to the London office temporarily from July through November 1992. | Steven Buchanan graduated from St. Andrews University, Scotland, with a BSC degree in 1976.  Upon joining the company as a sales representative in 1992, he spent 6 months in an orientation program at the Seattle office and then returned to his permanent post in London.  He was promoted to sales manager in March 1993.  Mr. Buchanan has completed the courses Successful Telemarketing and International Sales Management.  He is fluent in French. | Michael is a graduate of Sussex University (MA, economics, 1983) and the University of California at Los Angeles (MBA, marketing, 1986).  He has also taken the courses Multi-Cultural Selling and Time Management for the Sales Professional.  He is fluent in Japanese and can read and write French, Portuguese, and Spanish. | Robert King served in the Peace Corps and traveled extensively before completing his degree in English at the University of Michigan in 1992, the year he joined the company.  After completing a course entitled Selling in Europe, he was transferred to the London office in March 1993. | Laura received a BA in psychology from the University of Washington.  She has also completed a course in business French.  She reads and writes French. | Anne has a BA degree in English from St. Lawrence College.  She is fluent in French and German. |
| reportsto | 2 | null | 2 | 2 | 2 | 5 | 5 | 2 | 5 |
| photopath | http://accweb/emmployees/davolio.bmp | http://accweb/emmployees/fuller.bmp | http://accweb/emmployees/leverling.bmp | http://accweb/emmployees/peacock.bmp | http://accweb/emmployees/buchanan.bmp | http://accweb/emmployees/davolio.bmp | http://accweb/emmployees/davolio.bmp | http://accweb/emmployees/davolio.bmp | http://accweb/emmployees/davolio.bmp |


# employeeterritories

```sql
CREATE TABLE employeeterritories (
    employeeid INTEGER NOT NULL,
    territoryid TEXT NOT NULL
);
```

## Rows

- total=49

| column | latest | sample | sample |
|---|---|---|---|
| employeeid | 9 | 7 | 1 |
| territoryid | 55439 | 80202 | 06897 |

## Columns

- employeeid: 7=10, 2=7, 5=7, 9=7, 6=5, 3=4, 8=4, 4=3, 1=2, int 1..9
- territoryid: unique identifier


# order_details

```sql
CREATE TABLE order_details (
    orderid INTEGER NOT NULL,
    productid INTEGER NOT NULL,
    unitprice REAL NOT NULL,
    quantity INTEGER NOT NULL,
    discount REAL NOT NULL
);
```

## Rows

- total=2155

| column | latest | sample | sample |
|---|---|---|---|
| orderid | 11077 | 10633 | 10833 |
| productid | 77 | 12 | 7 |
| unitprice | 13 | 38 | 30 |
| quantity | 2 | 36 | 20 |
| discount | 0 | 0.15 | 0.1 |

## Columns

- orderid: 830 distinct, int 10248..11077
  - stats: average=10659.4, median=10657
- productid: 77 distinct, int 1..77
  - stats: average=40.793, median=41
- unitprice: 116 distinct, num 2..263.5
  - stats: average=26.2185, median=18.4
- quantity: 55 distinct, int 1..130
  - stats: average=23.813, median=20
- discount: 0=1317, 0.05=185, 0.1=173, 0.2=161, 0.15=157, 0.25=154, 0.03=3, 0.02=2, 0.01=1, 0.04=1, 0.06=1, num 0..0.25


# orders

```sql
CREATE TABLE orders (
    orderid INTEGER NOT NULL,
    customerid TEXT,
    employeeid INTEGER,
    orderdate DATE,
    requireddate DATE,
    shippeddate DATE,
    shipvia INTEGER,
    freight REAL,
    shipname TEXT,
    shipaddress TEXT,
    shipcity TEXT,
    shipregion TEXT,
    shippostalcode TEXT,
    shipcountry TEXT
);
```

## Rows

- total=830

| column | latest | sample | sample |
|---|---|---|---|
| orderid | 11077 | 10501 | 10487 |
| customerid | RATTC | BLAUS | QUEEN |
| employeeid | 1 | 9 | 2 |
| orderdate | 1998-05-06 | 1997-04-09 | 1997-03-26 |
| requireddate | 1998-06-03 | 1997-05-07 | 1997-04-23 |
| shippeddate | null | 1997-04-16 | 1997-03-28 |
| shipvia | 2 | 3 | 2 |
| freight | 8.53 | 8.85 | 71.07 |
| shipname | Rattlesnake Canyon Grocery | Blauer See Delikatessen | Queen Cozinha |
| shipaddress | 2817 Milton Dr. | Forsterstr. 57 | Alameda dos Canàrios, 891 |
| shipcity | Albuquerque | Mannheim | Sao Paulo |
| shipregion | NM | null | SP |
| shippostalcode | 87110 | 68306 | 05487-020 |
| shipcountry | USA | Germany | Brazil |

## Columns

- orderid: unique identifier, int 10248..11077
  - stats: average=10662.5, median=10662.5
- customerid: 89 distinct
- employeeid: 4=156, 3=127, 1=123, 8=104, 2=96, 7=72, 6=67, 9=43, 5=42, int 1..9
- orderdate: 480 distinct
- requireddate: 454 distinct
- shippeddate: 387 distinct, nulls=21
- shipvia: 2=326, 3=255, 1=249, int 1..3
- freight: 799 distinct, num 0.02..1007.64
  - stats: average=78.2442, median=41.36
- shipname: 90 distinct
- shipaddress: 89 distinct
- shipcity: 70 distinct
- shipregion: "SP"=49, "RJ"=34, "ID"=31, "OR"=28, "Co. Cork"=19, "WA"=19, "NM"=18, "Táchira"=18, "BC"=17, "Lara"=14, "Essex"=13, "Québec"=13, "Nueva Esparta"=12, "AK"=10, "Isle of Wight"=10, "WY"=9, "CA"=4, "MT"=3, "DF"=2, nulls=507
- shippostalcode: 84 distinct, nulls=19
- shipcountry: 21 distinct


# products

```sql
CREATE TABLE products (
    productid INTEGER NOT NULL,
    productname TEXT NOT NULL,
    supplierid INTEGER,
    categoryid INTEGER,
    quantityperunit TEXT,
    unitprice REAL,
    unitsinstock INTEGER,
    unitsonorder INTEGER,
    reorderlevel INTEGER,
    discontinued INTEGER NOT NULL
);
```

## Rows

- total=77

| column | latest | sample | sample |
|---|---|---|---|
| productid | 77 | 1 | 9 |
| productname | Original Frankfurter grüne Soße | Chai | Mishi Kobe Niku |
| supplierid | 12 | 8 | 4 |
| categoryid | 2 | 1 | 6 |
| quantityperunit | 12 boxes | 10 boxes x 30 bags | 18 - 500 g pkgs. |
| unitprice | 13 | 18 | 97 |
| unitsinstock | 32 | 39 | 29 |
| unitsonorder | 0 | 0 | 0 |
| reorderlevel | 15 | 10 | 0 |
| discontinued | 0 | 1 | 1 |

## Columns

- productid: unique identifier, int 1..77
  - stats: average=39, median=39
- productname: all distinct
- supplierid: 29 distinct, int 1..29
  - stats: average=13.7403, median=13
- categoryid: 3=13, 1=12, 2=12, 8=12, 4=10, 5=7, 6=6, 7=5, int 1..8
- quantityperunit: 70 distinct
- unitprice: 61 distinct, num 2.5..263.5
  - stats: average=28.8339, median=19.5
- unitsinstock: 51 distinct, int 0..125
  - stats: average=40.5065, median=26
- unitsonorder: 0=60, 10=4, 70=4, 40=3, 20=1, 30=1, 50=1, 60=1, 80=1, 100=1, int 0..100
- reorderlevel: 0=24, 25=12, 15=10, 5=8, 20=8, 30=8, 10=7, int 0..30
- discontinued: 0=67, 1=10


# region

## All rows

| column | row 1 | row 2 | row 3 | row 4 |
|---|---|---|---|---|
| regionid | 1 | 2 | 3 | 4 |
| regiondescription | Eastern | Western | Northern | Southern |


# shippers

## All rows

| column | row 1 | row 2 | row 3 | row 4 | row 5 | row 6 |
|---|---|---|---|---|---|---|
| shipperid | 1 | 2 | 3 | 4 | 5 | 6 |
| companyname | Speedy Express | United Package | Federal Shipping | Alliance Shippers | UPS | DHL |
| phone | (503) 555-9831 | (503) 555-3199 | (503) 555-9931 | 1-800-222-0451 | 1-800-782-7892 | 1-800-225-5345 |


# suppliers

```sql
CREATE TABLE suppliers (
    supplierid INTEGER NOT NULL,
    companyname TEXT NOT NULL,
    contactname TEXT,
    contacttitle TEXT,
    address TEXT,
    city TEXT,
    region TEXT,
    postalcode TEXT,
    country TEXT,
    phone TEXT,
    fax TEXT,
    homepage TEXT
);
```

## Rows

- total=29

| column | latest | sample | sample |
|---|---|---|---|
| supplierid | 29 | 9 | 15 |
| companyname | Forêts d'érables | PB Knäckebröd AB | Norske Meierier |
| contactname | Chantal Goulet | Lars Peterson | Beate Vileid |
| contacttitle | Accounting Manager | Sales Agent | Marketing Manager |
| address | 148 rue Chasseur | Kaloadagatan 13 | Hatlevegen 5 |
| city | Ste-Hyacinthe | Göteborg | Sandvika |
| region | Québec | null | null |
| postalcode | J2S 7S8 | S-345 67 | 1320 |
| country | Canada | Sweden | Norway |
| phone | (514) 555-2955 | 031-987 65 43 | (0)2-953010 |
| fax | (514) 555-2921 | 031-987 65 91 | null |
| homepage | null | null | null |

## Columns

- supplierid: unique identifier, int 1..29
  - stats: average=15, median=15
- companyname: all distinct
- contactname: all distinct
- contacttitle: "Sales Representative"=6, "Marketing Manager"=5, "Sales Manager"=4, "Accounting Manager"=2, "Order Administrator"=2, "Coordinator Foreign Markets"=1, "Export Administrator"=1, "International Marketing Mgr."=1, "Marketing Representative"=1, "Owner"=1, "Product Manager"=1, "Purchasing Manager"=1, "Regional Account Rep."=1, "Sales Agent"=1, "Wholesale Account Agent"=1
- address: all distinct
- city: all distinct
- region: "Québec"=2, "Asturias"=1, "LA"=1, "MA"=1, "MI"=1, "NSW"=1, "OR"=1, "Victoria"=1, nulls=20
- postalcode: all distinct
- country: "USA"=4, "France"=3, "Germany"=3, "Australia"=2, "Canada"=2, "Italy"=2, "Japan"=2, "Sweden"=2, "UK"=2, "Brazil"=1, "Denmark"=1, "Finland"=1, "Netherlands"=1, "Norway"=1, "Singapore"=1, "Spain"=1
- phone: all distinct
- fax: "(02) 555-4873"=1, "(03) 444-6588"=1, "(04721) 8714"=1, "(0544) 60603"=1, "(089) 6547667"=1, "(1) 03.83.00.62"=1, "(12345) 1210"=1, "(313) 555-3349"=1, "(514) 555-2921"=1, "(617) 555-3389"=1, "031-987 65 91"=1, "38.76.98.58"=1, "43844115"=1, nulls=16
- homepage: "#CAJUN.HTM#"=1, "#FORMAGGI.HTM#"=1, "G'day Mate (on the World Wide Web)#http://www.microsoft.com/accessdev/sampleapps/gdaymate.htm#"=1, "Mayumi's (on the World Wide Web)#http://www.microsoft.com/accessdev/sampleapps/mayumi.htm#"=1, "Plutzer (on the World Wide Web)#http://www.microsoft.com/accessdev/sampleapps/plutzer.htm#"=1, nulls=24


# territories

```sql
CREATE TABLE territories (
    territoryid TEXT NOT NULL,
    territorydescription TEXT NOT NULL,
    regionid INTEGER NOT NULL
);
```

## Rows

- total=53

| column | latest | sample | sample |
|---|---|---|---|
| territoryid | 98104 | 19713 | 10019 |
| territorydescription | Seattle | Neward | New York |
| regionid | 2 | 1 | 1 |

## Columns

- territoryid: unique identifier
- territorydescription: 52 distinct
- regionid: 1=19, 2=15, 3=11, 4=8, int 1..4


# usstates

```sql
CREATE TABLE usstates (
    stateid INTEGER NOT NULL,
    statename TEXT,
    stateabbr TEXT,
    stateregion TEXT
);
```

## Rows

- total=51

| column | latest | sample | sample |
|---|---|---|---|
| stateid | 51 | 34 | 18 |
| statename | Wyoming | North Carolina | Kentucky |
| stateabbr | WY | NC | KY |
| stateregion | west | east | south |

## Columns

- stateid: unique identifier, int 1..51
  - stats: average=26, median=26
- statename: all distinct
- stateabbr: all distinct
- stateregion: "east"=13, "midwest"=12, "west"=12, "south"=9, "north"=5


- Skipped 2 empty table(s): customercustomerdemo, customerdemographics
