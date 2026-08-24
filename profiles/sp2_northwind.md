---
generator: db-snooper
version: 0.0.34
generated_at_utc: 2026-08-24T21:59:26.629997Z
dialect: sqlite
database: /var/folders/9j/b9bx_drd53sc6zbpsqyrjy4h0000gn/T/dbsnoop-b2a938j0/northwind.sqlite
schema: main
---

# "categories"  (rows=8)

columns:
"categoryid" int NOTNULL
"categoryname" text NOTNULL
"description" text
"picture" bytes→text

indexes: none

all rows:
| column | row 1 | row 2 | row 3 | row 4 | row 5 | row 6 | row 7 | row 8 |
|---|---|---|---|---|---|---|---|---|
| categoryid | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 |
| categoryname | Beverages | Condiments | Confections | Dairy Products | Grains/Cereals | Meat/Poultry | Produce | Seafood |
| description | Soft drinks, coffees, teas, beers, and ales | Sweet and savory sauces, relishes, spreads, and seasonings | Desserts, candies, and sweet breads | Cheeses | Breads, crackers, pasta, and cereal | Prepared meats | Dried fruit and bean curd | Seaweed and fish |

# "customergroupthreshold"  (rows=4)

columns:
"groupname" text NOTNULL
"rangebottom" numeric NOTNULL
"rangetop" numeric NOTNULL

indexes: none

all rows:
| column | row 1 | row 2 | row 3 | row 4 |
|---|---|---|---|---|
| groupname | High | Low | Medium | Very High |
| rangebottom | 5000 | 0 | 1000 | 10000 |
| rangetop | 10000 | 1000 | 5000 | 9.2e+14 |

# "customers"  (rows=91)

columns:
"customerid" text NOTNULL: unique identifier
"companyname" text NOTNULL: all distinct
"contactname" text: all distinct
"contacttitle" text: "Owner"=17, "Sales Representative"=17, "Marketing Manager"=12, "Sales Manager"=11, "Accounting Manager"=10, "Sales Associate"=7, "Marketing Assistant"=6, "Sales Agent"=5, "Assistant Sales Agent"=2, "Order Administrator"=2, "Assistant Sales Representative"=1, "Owner/Marketing Assistant"=1
"address" text: all distinct
"city" text: 69 distinct
"region" text: "SP"=6, "OR"=4, "RJ"=3, "WA"=3, "BC"=2, "AK"=1, "CA"=1, "Co. Cork"=1, "DF"=1, "ID"=1, "Isle of Wight"=1, "Lara"=1, "MT"=1, "NM"=1, "Nueva Esparta"=1, "Québec"=1, "Táchira"=1, "WY"=1, nulls=60
"postalcode" text: 86 distinct, nulls=1
"country" text: 21 distinct
"phone" text: all distinct
"fax" text: all distinct, nulls=22

indexes: none

samples:
| column | latest | sample | sample |
|---|---|---|---|
| customerid | WOLZA | FRANK | ROMEY |
| companyname | Wolski  Zajazd | Frankenversand | Romero y tomillo |
| contactname | Zbyszek Piestrzeniewicz | Peter Franken | Alejandra Camino |
| contacttitle | Owner | Marketing Manager | Accounting Manager |
| address | ul. Filtrowa 68 | Berliner Platz 43 | Gran Vía, 1 |
| city | Warszawa | München | Madrid |
| region | null | null | null |
| postalcode | 01-012 | 80805 | 28001 |
| country | Poland | Germany | Spain |
| phone | (26) 642-7012 | 089-0877310 | (91) 745 6200 |
| fax | (26) 642-7012 | 089-0877451 | (91) 745 6210 |

# "employees"  (rows=9)

columns:
"employeeid" int NOTNULL
"lastname" text NOTNULL
"firstname" text NOTNULL
"title" text
"titleofcourtesy" text
"birthdate" date
"hiredate" date
"address" text
"city" text
"region" text
"postalcode" text
"country" text
"homephone" text
"extension" text
"photo" bytes→text
"notes" text
"reportsto" int
"photopath" text

indexes: none

all rows:
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
| notes | Education includes a BA in psychology from Colorado State University in 1970.  She also completed The Art of the Cold Call.  Nancy is a member of Toastmasters International. | Andrew received his BTS commercial in 1974 and a Ph.D. in international marketing from the University of Dallas in 1981.  He is fluent in French and Italian and reads German.  He joined the company a… | Janet has a BS degree in chemistry from Boston College (1984).  She has also completed a certificate program in food retailing management.  Janet was hired as a sales associate in 1991 and promoted t… | Margaret holds a BA in English literature from Concordia College (1958) and an MA from the American Institute of Culinary Arts (1966).  She was assigned to the London office temporarily from July thr… | Steven Buchanan graduated from St. Andrews University, Scotland, with a BSC degree in 1976.  Upon joining the company as a sales representative in 1992, he spent 6 months in an orientation program at… | Michael is a graduate of Sussex University (MA, economics, 1983) and the University of California at Los Angeles (MBA, marketing, 1986).  He has also taken the courses Multi-Cultural Selling and Time… | Robert King served in the Peace Corps and traveled extensively before completing his degree in English at the University of Michigan in 1992, the year he joined the company.  After completing a cours… | Laura received a BA in psychology from the University of Washington.  She has also completed a course in business French.  She reads and writes French. | Anne has a BA degree in English from St. Lawrence College.  She is fluent in French and German. |
| reportsto | 2 | null | 2 | 2 | 2 | 5 | 5 | 2 | 5 |
| photopath | http://accweb/emmployees/davolio.bmp | http://accweb/emmployees/fuller.bmp | http://accweb/emmployees/leverling.bmp | http://accweb/emmployees/peacock.bmp | http://accweb/emmployees/buchanan.bmp | http://accweb/emmployees/davolio.bmp | http://accweb/emmployees/davolio.bmp | http://accweb/emmployees/davolio.bmp | http://accweb/emmployees/davolio.bmp |

# "employeeterritories"  (rows=49)

columns:
"employeeid" int NOTNULL: 7=10, 2=7, 5=7, 9=7, 6=5, 3=4, 8=4, 4=3, 1=2, 1..9
"territoryid" text NOTNULL: digits, unique identifier

indexes: none

samples:
| column | latest | sample | sample |
|---|---|---|---|
| employeeid | 9 | 1 | 4 |
| territoryid | 55439 | 06897 | 27511 |

# "order_details"  (rows=2155)

columns:
"orderid" int NOTNULL: 830 distinct, 10248..11077, avg=10659.4, median=10657
"productid" int NOTNULL: 77 distinct, 1..77, avg=40.793, median=41
"unitprice" float NOTNULL: 116 distinct, 2..263.5, avg=26.2185, median=18.4
"quantity" int NOTNULL: 55 distinct, 1..130, avg=23.813, median=20
"discount" float NOTNULL: 0=1317, 0.05=185, 0.1=173, 0.2=161, 0.15=157, 0.25=154, 0.03=3, 0.02=2, 0.01=1, 0.04=1, 0.06=1, 0..0.25

indexes: none

samples:
| column | latest | sample | sample |
|---|---|---|---|
| orderid | 11077 | 11039 | 10446 |
| productid | 77 | 35 | 52 |
| unitprice | 13 | 18 | 5.6 |
| quantity | 2 | 24 | 15 |
| discount | 0 | 0 | 0.1 |

# "orders"  (rows=830)

columns:
"orderid" int NOTNULL: unique identifier, 10248..11077, avg=10662.5, median=10662.5
"customerid" text: 89 distinct
"employeeid" int: 4=156, 3=127, 1=123, 8=104, 2=96, 7=72, 6=67, 9=43, 5=42, 1..9
"orderdate" date: 480 distinct
"requireddate" date: 454 distinct
"shippeddate" date: 387 distinct, nulls=21
"shipvia" int: 2=326, 3=255, 1=249, 1..3
"freight" float: 799 distinct, 0.02..1007.64, avg=78.2442, median=41.36
"shipname" text: 90 distinct
"shipaddress" text: 89 distinct
"shipcity" text: 70 distinct
"shipregion" text: "SP"=49, "RJ"=34, "ID"=31, "OR"=28, "Co. Cork"=19, "WA"=19, "NM"=18, "Táchira"=18, "BC"=17, "Lara"=14, "Essex"=13, "Québec"=13, "Nueva Esparta"=12, "AK"=10, "Isle of Wight"=10, "WY"=9, "CA"=4, "MT"=3, "DF"=2, nulls=507
"shippostalcode" text: 84 distinct, nulls=19
"shipcountry" text: 21 distinct

indexes: none

samples:
| column | latest | sample | sample |
|---|---|---|---|
| orderid | 11077 | 10424 | 10756 |
| customerid | RATTC | MEREP | SPLIR |
| employeeid | 1 | 7 | 8 |
| orderdate | 1998-05-06 | 1997-01-23 | 1997-11-27 |
| requireddate | 1998-06-03 | 1997-02-20 | 1997-12-25 |
| shippeddate | null | 1997-01-27 | 1997-12-02 |
| shipvia | 2 | 2 | 2 |
| freight | 8.53 | 370.61 | 73.21 |
| shipname | Rattlesnake Canyon Grocery | Mère Paillarde | Split Rail Beer & Ale |
| shipaddress | 2817 Milton Dr. | 43 rue St. Laurent | P.O. Box 555 |
| shipcity | Albuquerque | Montréal | Lander |
| shipregion | NM | Québec | WY |
| shippostalcode | 87110 | H1J 1C3 | 82520 |
| shipcountry | USA | Canada | USA |

# "products"  (rows=77)

columns:
"productid" int NOTNULL: unique identifier, 1..77, avg=39, median=39
"productname" text NOTNULL: all distinct
"supplierid" int: 29 distinct, 1..29, avg=13.7403, median=13
"categoryid" int: 3=13, 1=12, 2=12, 8=12, 4=10, 5=7, 6=6, 7=5, 1..8
"quantityperunit" text: 70 distinct
"unitprice" float: 61 distinct, 2.5..263.5, avg=28.8339, median=19.5
"unitsinstock" int: 51 distinct, 0..125, avg=40.5065, median=26
"unitsonorder" int: 0=60, 10=4, 70=4, 40=3, 20=1, 30=1, 50=1, 60=1, 80=1, 100=1, 0..100
"reorderlevel" int: 0=24, 25=12, 15=10, 5=8, 20=8, 30=8, 10=7, 0..30
"discontinued" int NOTNULL: 0=67, 1=10

indexes: none

samples:
| column | latest | sample | sample |
|---|---|---|---|
| productid | 77 | 54 | 22 |
| productname | Original Frankfurter grüne Soße | Tourtière | Gustaf's Knäckebröd |
| supplierid | 12 | 25 | 9 |
| categoryid | 2 | 6 | 5 |
| quantityperunit | 12 boxes | 16 pies | 24 - 500 g pkgs. |
| unitprice | 13 | 7.45 | 21 |
| unitsinstock | 32 | 21 | 104 |
| unitsonorder | 0 | 0 | 0 |
| reorderlevel | 15 | 10 | 25 |
| discontinued | 0 | 0 | 0 |

# "region"  (rows=4)

columns:
"regionid" int NOTNULL
"regiondescription" text NOTNULL

indexes: none

all rows:
| column | row 1 | row 2 | row 3 | row 4 |
|---|---|---|---|---|
| regionid | 1 | 2 | 3 | 4 |
| regiondescription | Eastern | Western | Northern | Southern |

# "shippers"  (rows=6)

columns:
"shipperid" int NOTNULL
"companyname" text NOTNULL
"phone" text

indexes: none

all rows:
| column | row 1 | row 2 | row 3 | row 4 | row 5 | row 6 |
|---|---|---|---|---|---|---|
| shipperid | 1 | 2 | 3 | 4 | 5 | 6 |
| companyname | Speedy Express | United Package | Federal Shipping | Alliance Shippers | UPS | DHL |
| phone | (503) 555-9831 | (503) 555-3199 | (503) 555-9931 | 1-800-222-0451 | 1-800-782-7892 | 1-800-225-5345 |

# "suppliers"  (rows=29)

columns:
"supplierid" int NOTNULL: unique identifier, 1..29, avg=15, median=15
"companyname" text NOTNULL: all distinct
"contactname" text: all distinct
"contacttitle" text: "Sales Representative"=6, "Marketing Manager"=5, "Sales Manager"=4, "Accounting Manager"=2, "Order Administrator"=2, "Coordinator Foreign Markets"=1, "Export Administrator"=1, "International Marketing Mgr."=1, "Marketing Representative"=1, "Owner"=1, "Product Manager"=1, "Purchasing Manager"=1, "Regional Account Rep."=1, "Sales Agent"=1, "Wholesale Account Agent"=1
"address" text: all distinct
"city" text: all distinct
"region" text: "Québec"=2, "Asturias"=1, "LA"=1, "MA"=1, "MI"=1, "NSW"=1, "OR"=1, "Victoria"=1, nulls=20
"postalcode" text: all distinct
"country" text: "USA"=4, "France"=3, "Germany"=3, "Australia"=2, "Canada"=2, "Italy"=2, "Japan"=2, "Sweden"=2, "UK"=2, "Brazil"=1, "Denmark"=1, "Finland"=1, "Netherlands"=1, "Norway"=1, "Singapore"=1, "Spain"=1
"phone" text: all distinct
"fax" text: "(02) 555-4873"=1, "(03) 444-6588"=1, "(04721) 8714"=1, "(0544) 60603"=1, "(089) 6547667"=1, "(1) 03.83.00.62"=1, "(12345) 1210"=1, "(313) 555-3349"=1, "(514) 555-2921"=1, "(617) 555-3389"=1, "031-987 65 91"=1, "38.76.98.58"=1, "43844115"=1, nulls=16
"homepage" text: "#CAJUN.HTM#"=1, "#FORMAGGI.HTM#"=1, "G'day Mate (on the World Wide Web)#http://www.microsoft.com/accessdev/sampleapps/gdaymate.htm#"=1, "Mayumi's (on the World Wide Web)#http://www.microsoft.com/accessdev/sampleapps/mayumi.htm#"=1, "Plutzer (on the World Wide Web)#http://www.microsoft.com/accessdev/sampleapps/plutzer.htm#"=1, nulls=24

indexes: none

samples:
| column | latest | sample | sample |
|---|---|---|---|
| supplierid | 29 | 21 | 20 |
| companyname | Forêts d'érables | Lyngbysild | Leka Trading |
| contactname | Chantal Goulet | Niels Petersen | Chandra Leka |
| contacttitle | Accounting Manager | Sales Manager | Owner |
| address | 148 rue Chasseur | Lyngbysild Fiskebakken 10 | 471 Serangoon Loop, Suite #402 |
| city | Ste-Hyacinthe | Lyngby | Singapore |
| region | Québec | null | null |
| postalcode | J2S 7S8 | 2800 | 0512 |
| country | Canada | Denmark | Singapore |
| phone | (514) 555-2955 | 43844108 | 555-8787 |
| fax | (514) 555-2921 | 43844115 | null |
| homepage | null | null | null |

# "territories"  (rows=53)

columns:
"territoryid" text NOTNULL: digits, unique identifier
"territorydescription" text NOTNULL: 52 distinct
"regionid" int NOTNULL: 1=19, 2=15, 3=11, 4=8, 1..4

indexes: none

samples:
| column | latest | sample | sample |
|---|---|---|---|
| territoryid | 98104 | 53404 | 10019 |
| territorydescription | Seattle | Racine | New York |
| regionid | 2 | 3 | 1 |

# "usstates"  (rows=51)

columns:
"stateid" int NOTNULL: unique identifier, 1..51, avg=26, median=26
"statename" text: all distinct
"stateabbr" text: all distinct
"stateregion" text: "east"=13, "midwest"=12, "west"=12, "south"=9, "north"=5

indexes: none

samples:
| column | latest | sample | sample |
|---|---|---|---|
| stateid | 51 | 26 | 18 |
| statename | Wyoming | Missouri | Kentucky |
| stateabbr | WY | MO | KY |
| stateregion | west | south | south |

- Skipped 2 empty table(s): "customercustomerdemo", "customerdemographics"
