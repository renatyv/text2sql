---
generator: db-snooper
version: 0.0.31
generated_at_utc: 2026-08-20T17:28:12.709980Z
dialect: sqlite
database: /var/folders/9j/b9bx_drd53sc6zbpsqyrjy4h0000gn/T/dbsnoop-04ccdkgw/chinook.sqlite
schema: main
---

## Relationships

- "albums"."AlbumId" ← "tracks"."AlbumId"
- "artists"."ArtistId" ← "albums"."ArtistId"
- "customers"."CustomerId" ← "invoices"."CustomerId"
- "employees"."EmployeeId" ← "customers"."SupportRepId", "employees"."ReportsTo"
- "genres"."GenreId" ← "tracks"."GenreId"
- "invoices"."InvoiceId" ← "invoice_items"."InvoiceId"
- "media_types"."MediaTypeId" ← "tracks"."MediaTypeId"
- "playlists"."PlaylistId" ← "playlist_track"."PlaylistId"
- "tracks"."TrackId" ← "invoice_items"."TrackId", "playlist_track"."TrackId"

# "albums"  (rows=347)

columns:
"AlbumId" int PK: unique identifier, 1..347, avg=174, median=174
"Title" nvarchar160 NOTNULL: all distinct
"ArtistId" int NOTNULL FK: 204 distinct, 1..275, avg=121.942, median=112, 90=21, 22=14, 58=11, 50=10, 150=10, 114=6, 118=5, 21=4, 82=4, 84=4

indexes: "ArtistId"
fk: "ArtistId"→"artists"."ArtistId"

samples:
| column | latest | sample | sample |
|---|---|---|---|
| AlbumId | 347 | 131 | 184 |
| Title | Koyaanisqatsi (Soundtrack from the Motion Picture) | IV | Os Cães Ladram Mas A Caravana Não Pára |
| ArtistId | 275 | 22 | 121 |

# "artists"  (rows=275)

columns:
"ArtistId" int PK: unique identifier, 1..275, avg=138, median=138
"Name" nvarchar120: all distinct

indexes: none
fk: none

samples:
| column | latest | sample | sample |
|---|---|---|---|
| ArtistId | 275 | 124 | 238 |
| Name | Philip Glass Ensemble | R.E.M. | Maurizio Pollini |

# "customers"  (rows=59)

columns:
"CustomerId" int PK: unique identifier, 1..59, avg=30, median=30
"FirstName" nvarchar40 NOTNULL: 57 distinct
"LastName" nvarchar20 NOTNULL: all distinct
"Company" nvarchar80: "Apple Inc."=1, "Banco do Brasil S.A."=1, "Embraer - Empresa Brasileira de Aeronáutica S.A."=1, "Google Inc."=1, "JetBrains s.r.o."=1, "Microsoft Corporation"=1, "Riotur"=1, "Rogers Canada"=1, "Telus"=1, "Woodstock Discos"=1, nulls=49
"Address" nvarchar70: all distinct
"City" nvarchar40: 53 distinct
"State" nvarchar40: 25 distinct, nulls=29
"Country" nvarchar40: 24 distinct
"PostalCode" nvarchar10: all distinct, nulls=4
"Phone" nvarchar24: all distinct, nulls=1
"Fax" nvarchar24: "+1 (212) 221-4679"=1, "+1 (408) 996-1011"=1, "+1 (425) 882-8081"=1, "+1 (604) 688-8756"=1, "+1 (650) 253-0000"=1, "+1 (780) 434-5565"=1, "+420 2 4172 5555"=1, "+55 (11) 3033-4564"=1, "+55 (11) 3055-8131"=1, "+55 (12) 3923-5566"=1, "+55 (21) 2271-7070"=1, "+55 (61) 3363-7855"=1, nulls=47
"Email" nvarchar60 NOTNULL: all distinct
"SupportRepId" int FK: 3=21, 4=20, 5=18, 3..5

indexes: "SupportRepId"
fk: "SupportRepId"→"employees"."EmployeeId"

samples:
| column | latest | sample | sample |
|---|---|---|---|
| CustomerId | 59 | 31 | 52 |
| FirstName | Puja | Martha | Emma |
| LastName | Srivastava | Silk | Jones |
| Company | null | null | null |
| Address | 3,Raj Bhavan Road | 194A Chain Lake Drive | 202 Hoxton Street |
| City | Bangalore | Halifax | London |
| State | null | NS | null |
| Country | India | Canada | United Kingdom |
| PostalCode | 560001 | B3S 1C5 | N1 5LH |
| Phone | +91 080 22289999 | +1 (902) 450-0450 | +44 020 7707 0707 |
| Fax | null | null | null |
| Email | puja_srivastava@yahoo.in | marthasilk@gmail.com | emma_jones@hotmail.com |
| SupportRepId | 3 | 5 | 3 |

# "employees"  (rows=8)

columns:
"EmployeeId" int PK: unique identifier, 1..8, avg=4.5, median=4.5
"LastName" nvarchar20 NOTNULL: "Adams"=1, "Callahan"=1, "Edwards"=1, "Johnson"=1, "King"=1, "Mitchell"=1, "Park"=1, "Peacock"=1
"FirstName" nvarchar20 NOTNULL: "Andrew"=1, "Jane"=1, "Laura"=1, "Margaret"=1, "Michael"=1, "Nancy"=1, "Robert"=1, "Steve"=1
"Title" nvarchar30: "Sales Support Agent"=3, "IT Staff"=2, "General Manager"=1, "IT Manager"=1, "Sales Manager"=1
"ReportsTo" int FK: 2=3, 1=2, 6=2, nulls=1, 1..6
"BirthDate" datetime: "1947-09-19 00:00:00"=1, "1958-12-08 00:00:00"=1, "1962-02-18 00:00:00"=1, "1965-03-03 00:00:00"=1, "1968-01-09 00:00:00"=1, "1970-05-29 00:00:00"=1, "1973-07-01 00:00:00"=1, "1973-08-29 00:00:00"=1
"HireDate" datetime: "2003-10-17 00:00:00"=2, "2002-04-01 00:00:00"=1, "2002-05-01 00:00:00"=1, "2002-08-14 00:00:00"=1, "2003-05-03 00:00:00"=1, "2004-01-02 00:00:00"=1, "2004-03-04 00:00:00"=1
"Address" nvarchar70: "1111 6 Ave SW"=1, "11120 Jasper Ave NW"=1, "5827 Bowness Road NW"=1, "590 Columbia Boulevard West"=1, "683 10 Street SW"=1, "7727B 41 Ave"=1, "825 8 Ave SW"=1, "923 7 ST NW"=1
"City" nvarchar40: "Calgary"=5, "Lethbridge"=2, "Edmonton"=1
"State" nvarchar40: "AB"=8
"Country" nvarchar40: "Canada"=8
"PostalCode" nvarchar10: "T1H 1Y8"=1, "T1K 5N8"=1, "T2P 2T3"=1, "T2P 5G3"=1, "T2P 5M5"=1, "T3B 0C5"=1, "T3B 1Y7"=1, "T5K 2N1"=1
"Phone" nvarchar24: "+1 (403) 262-3443"=2, "+1 (403) 246-9887"=1, "+1 (403) 263-4423"=1, "+1 (403) 456-9986"=1, "+1 (403) 467-3351"=1, "+1 (780) 428-9482"=1, "1 (780) 836-9987"=1
"Fax" nvarchar24: "+1 (403) 246-9899"=1, "+1 (403) 262-3322"=1, "+1 (403) 262-6712"=1, "+1 (403) 263-4289"=1, "+1 (403) 456-8485"=1, "+1 (403) 467-8772"=1, "+1 (780) 428-3457"=1, "1 (780) 836-9543"=1
"Email" nvarchar60: "andrew@chinookcorp.com"=1, "jane@chinookcorp.com"=1, "laura@chinookcorp.com"=1, "margaret@chinookcorp.com"=1, "michael@chinookcorp.com"=1, "nancy@chinookcorp.com"=1, "robert@chinookcorp.com"=1, "steve@chinookcorp.com"=1

indexes: "ReportsTo"
fk: "ReportsTo"→"employees"."EmployeeId"

all rows:
| column | row 1 | row 2 | row 3 | row 4 | row 5 | row 6 | row 7 | row 8 |
|---|---|---|---|---|---|---|---|---|
| EmployeeId | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 |
| LastName | Adams | Edwards | Peacock | Park | Johnson | Mitchell | King | Callahan |
| FirstName | Andrew | Nancy | Jane | Margaret | Steve | Michael | Robert | Laura |
| Title | General Manager | Sales Manager | Sales Support Agent | Sales Support Agent | Sales Support Agent | IT Manager | IT Staff | IT Staff |
| ReportsTo | null | 1 | 2 | 2 | 2 | 1 | 6 | 6 |
| BirthDate | 1962-02-18T00:00:00 | 1958-12-08T00:00:00 | 1973-08-29T00:00:00 | 1947-09-19T00:00:00 | 1965-03-03T00:00:00 | 1973-07-01T00:00:00 | 1970-05-29T00:00:00 | 1968-01-09T00:00:00 |
| HireDate | 2002-08-14T00:00:00 | 2002-05-01T00:00:00 | 2002-04-01T00:00:00 | 2003-05-03T00:00:00 | 2003-10-17T00:00:00 | 2003-10-17T00:00:00 | 2004-01-02T00:00:00 | 2004-03-04T00:00:00 |
| Address | 11120 Jasper Ave NW | 825 8 Ave SW | 1111 6 Ave SW | 683 10 Street SW | 7727B 41 Ave | 5827 Bowness Road NW | 590 Columbia Boulevard West | 923 7 ST NW |
| City | Edmonton | Calgary | Calgary | Calgary | Calgary | Calgary | Lethbridge | Lethbridge |
| State | AB | AB | AB | AB | AB | AB | AB | AB |
| Country | Canada | Canada | Canada | Canada | Canada | Canada | Canada | Canada |
| PostalCode | T5K 2N1 | T2P 2T3 | T2P 5M5 | T2P 5G3 | T3B 1Y7 | T3B 0C5 | T1K 5N8 | T1H 1Y8 |
| Phone | +1 (780) 428-9482 | +1 (403) 262-3443 | +1 (403) 262-3443 | +1 (403) 263-4423 | 1 (780) 836-9987 | +1 (403) 246-9887 | +1 (403) 456-9986 | +1 (403) 467-3351 |
| Fax | +1 (780) 428-3457 | +1 (403) 262-3322 | +1 (403) 262-6712 | +1 (403) 263-4289 | 1 (780) 836-9543 | +1 (403) 246-9899 | +1 (403) 456-8485 | +1 (403) 467-8772 |
| Email | andrew@chinookcorp.com | nancy@chinookcorp.com | jane@chinookcorp.com | margaret@chinookcorp.com | steve@chinookcorp.com | michael@chinookcorp.com | robert@chinookcorp.com | laura@chinookcorp.com |

# "genres"  (rows=25)

columns:
"GenreId" int PK: unique identifier, 1..25, avg=13, median=13
"Name" nvarchar120: all distinct

indexes: none
fk: none

samples:
| column | latest | sample | sample |
|---|---|---|---|
| GenreId | 25 | 22 | 5 |
| Name | Opera | Comedy | Rock And Roll |

# "invoice_items"  (rows=2240)

columns:
"InvoiceLineId" int PK: unique identifier, 1..2240, avg=1120.5, median=1120.5
"InvoiceId" int NOTNULL FK: 412 distinct, 1..412, avg=206.869, median=207, 5=14, 12=14, 19=14, 26=14, 33=14, 40=14, 47=14, 54=14, 61=14, 68=14
"TrackId" int NOTNULL FK: 1984 distinct, 1..3500, avg=1717.73, median=1708, 2=2, 8=2, 9=2, 20=2, 32=2, 48=2, 66=2, 84=2, 161=2, 162=2
"UnitPrice" numeric NOTNULL: 0.99=2129, 1.99=111
"Quantity" int NOTNULL: 1=2240

indexes: "InvoiceId", "TrackId"
fk: "InvoiceId"→"invoices"."InvoiceId", "TrackId"→"tracks"."TrackId"

samples:
| column | latest | sample | sample |
|---|---|---|---|
| InvoiceLineId | 2240 | 1966 | 196 |
| InvoiceId | 412 | 362 | 37 |
| TrackId | 3177 | 1476 | 1172 |
| UnitPrice | 1.99 | 0.99 | 0.99 |
| Quantity | 1 | 1 | 1 |

# "invoices"  (rows=412)

columns:
"InvoiceId" int PK: unique identifier, 1..412, avg=206.5, median=206.5
"CustomerId" int NOTNULL FK: 59 distinct, 1..59, avg=29.9296, median=30, 1=7, 2=7, 3=7, 4=7, 5=7, 6=7, 7=7, 8=7, 9=7, 10=7
"InvoiceDate" datetime NOTNULL: 354 distinct
"BillingAddress" nvarchar70: 59 distinct
"BillingCity" nvarchar40: 53 distinct
"BillingState" nvarchar40: 25 distinct, nulls=202
"BillingCountry" nvarchar40: 24 distinct
"BillingPostalCode" nvarchar10: 55 distinct, nulls=28
"Total" numeric NOTNULL: 23 distinct, 0.99..25.86, avg=5.65194, median=3.96

indexes: "CustomerId"
fk: "CustomerId"→"customers"."CustomerId"

samples:
| column | latest | sample | sample |
|---|---|---|---|
| InvoiceId | 412 | 334 | 121 |
| CustomerId | 58 | 39 | 1 |
| InvoiceDate | 2013-12-22T00:00:00 | 2013-01-07T00:00:00 | 2010-06-13T00:00:00 |
| BillingAddress | 12,Community Centre | 4, Rue Milton | Av. Brigadeiro Faria Lima, 2170 |
| BillingCity | Delhi | Paris | São José dos Campos |
| BillingState | null | null | SP |
| BillingCountry | India | France | Brazil |
| BillingPostalCode | 110017 | 75009 | 12227-000 |
| Total | 1.99 | 13.86 | 3.96 |

# "media_types"  (rows=5)

columns:
"MediaTypeId" int PK: unique identifier, 1..5, avg=3, median=3
"Name" nvarchar120: "AAC audio file"=1, "MPEG audio file"=1, "Protected AAC audio file"=1, "Protected MPEG-4 video file"=1, "Purchased AAC audio file"=1

indexes: none
fk: none

all rows:
| column | row 1 | row 2 | row 3 | row 4 | row 5 |
|---|---|---|---|---|---|
| MediaTypeId | 1 | 2 | 3 | 4 | 5 |
| Name | MPEG audio file | Protected AAC audio file | Protected MPEG-4 video file | Purchased AAC audio file | AAC audio file |

# "playlist_track"  (rows=8715)

columns:
"PlaylistId" int PK FK: 1=3290, 8=3290, 5=1477, 3=213, 10=213, 12=75, 11=39, 17=26, 13=25, 14=25, 15=25, 16=15, 9=1, 18=1, 1..18
"TrackId" int PK FK: 3503 distinct, 1..3503, avg=1767.08, median=1773, 3403=5, 3404=5, 3408=5, 3409=5, 3410=5, 3411=5, 3415=5, 3416=5, 3417=5, 3418=5

indexes: "TrackId"
fk: "TrackId"→"tracks"."TrackId", "PlaylistId"→"playlists"."PlaylistId"

samples:
| column | latest | sample | sample |
|---|---|---|---|
| PlaylistId | 18 | 5 | 1 |
| TrackId | 597 | 1305 | 3501 |

# "playlists"  (rows=18)

columns:
"PlaylistId" int PK: unique identifier, 1..18, avg=9.5, median=9.5
"Name" nvarchar120: "Audiobooks"=2, "Movies"=2, "Music"=2, "TV Shows"=2, "90’s Music"=1, "Brazilian Music"=1, "Classical"=1, "Classical 101 - Deep Cuts"=1, "Classical 101 - Next Steps"=1, "Classical 101 - The Basics"=1, "Grunge"=1, "Heavy Metal Classic"=1, "Music Videos"=1, "On-The-Go 1"=1

indexes: none
fk: none

samples:
| column | latest | sample | sample |
|---|---|---|---|
| PlaylistId | 18 | 1 | 17 |
| Name | On-The-Go 1 | Music | Heavy Metal Classic |

# "tracks"  (rows=3503)

columns:
"TrackId" int PK: unique identifier, 1..3503, avg=1752, median=1752
"Name" nvarchar200 NOTNULL: 3257 distinct
"AlbumId" int FK: 347 distinct, 1..347, avg=140.929, median=141, 141=57, 23=34, 73=30, 229=26, 230=25, 251=25, 83=24, 231=24, 253=24, 24=23
"MediaTypeId" int NOTNULL FK: 1=3034, 2=237, 3=214, 5=11, 4=7, 1..5
"GenreId" int FK: 25 distinct, 1..25, avg=5.72538, median=3, 1=1297, 7=579, 3=374, 4=332, 2=130, 19=93, 6=81, 24=74, 21=64, 14=61
"Composer" nvarchar220: 852 distinct, nulls=978
"Milliseconds" int NOTNULL: 3080 distinct, 1071..5286953, avg=393599, median=255634
"Bytes" int: 3501 distinct, 38747..1059546140, avg=3.35102e+07, median=8.1079e+06
"UnitPrice" numeric NOTNULL: 0.99=3290, 1.99=213

indexes: "AlbumId", "GenreId", "MediaTypeId"
fk: "AlbumId"→"albums"."AlbumId", "GenreId"→"genres"."GenreId", "MediaTypeId"→"media_types"."MediaTypeId"

samples:
| column | latest | sample | sample |
|---|---|---|---|
| TrackId | 3503 | 1028 | 3027 |
| Name | Koyaanisqatsi | Enough Space | "40" |
| AlbumId | 347 | 82 | 239 |
| MediaTypeId | 2 | 1 | 1 |
| GenreId | 10 | 1 | 1 |
| Composer | Philip Glass | Dave Grohl | U2 |
| Milliseconds | 206005 | 157387 | 157962 |
| Bytes | 3305164 | 5169280 | 5251767 |
| UnitPrice | 0.99 | 0.99 | 0.99 |
