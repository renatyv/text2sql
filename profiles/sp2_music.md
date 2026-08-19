---
generator: db-snooper
version: 0.0.26
generated_at_utc: 2026-08-16T08:09:25.807843Z
dialect: sqlite
database: /var/folders/9j/b9bx_drd53sc6zbpsqyrjy4h0000gn/T/dbsnoop-ss0i7ffo/music.sqlite
schema: main
---

## Relationships

- Album.AlbumId ← Track.AlbumId
- Artist.ArtistId ← Album.ArtistId
- Customer.CustomerId ← Invoice.CustomerId
- Employee.EmployeeId ← Customer.SupportRepId, Employee.ReportsTo
- Genre.GenreId ← Track.GenreId
- Invoice.InvoiceId ← InvoiceLine.InvoiceId
- MediaType.MediaTypeId ← Track.MediaTypeId
- Playlist.PlaylistId ← PlaylistTrack.PlaylistId
- Track.TrackId ← InvoiceLine.TrackId, PlaylistTrack.TrackId

# Album

```sql
CREATE TABLE [Album]
(
    [AlbumId] INTEGER  NOT NULL,
    [Title] NVARCHAR(160)  NOT NULL,
    [ArtistId] INTEGER  NOT NULL,
    CONSTRAINT [PK_Album] PRIMARY KEY  ([AlbumId]),
    FOREIGN KEY ([ArtistId]) REFERENCES [Artist] ([ArtistId]) 
		ON DELETE NO ACTION ON UPDATE NO ACTION
);
```

## Indexes

- ([ArtistId])
- UNIQUE ([AlbumId])

## Rows

- total=347

| column | latest | sample | sample |
|---|---|---|---|
| AlbumId | 347 | 115 | 53 |
| Title | Koyaanisqatsi (Soundtrack from the Motion Picture) | Sex Machine | Vozes do MPB |
| ArtistId | 275 | 91 | 21 |

## Columns

- AlbumId: unique identifier, int 1..347
  - stats: average=174, median=174
- Title: all distinct
- ArtistId: 204 distinct, int 1..275
  - stats: average=121.942, median=112
  - top_values: 90=21, 22=14, 58=11, 50=10, 150=10, 114=6, 118=5, 21=4, 82=4, 84=4


# Artist

```sql
CREATE TABLE [Artist]
(
    [ArtistId] INTEGER  NOT NULL,
    [Name] NVARCHAR(120),
    CONSTRAINT [PK_Artist] PRIMARY KEY  ([ArtistId])
);
```

## Indexes

- UNIQUE ([ArtistId])

## Rows

- total=275

| column | latest | sample | sample |
|---|---|---|---|
| ArtistId | 275 | 131 | 163 |
| Name | Philip Glass Ensemble | Smashing Pumpkins | Corinne Bailey Rae |

## Columns

- ArtistId: unique identifier, int 1..275
  - stats: average=138, median=138
- Name: all distinct


# Customer

```sql
CREATE TABLE [Customer]
(
    [CustomerId] INTEGER  NOT NULL,
    [FirstName] NVARCHAR(40)  NOT NULL,
    [LastName] NVARCHAR(20)  NOT NULL,
    [Company] NVARCHAR(80),
    [Address] NVARCHAR(70),
    [City] NVARCHAR(40),
    [State] NVARCHAR(40),
    [Country] NVARCHAR(40),
    [PostalCode] NVARCHAR(10),
    [Phone] NVARCHAR(24),
    [Fax] NVARCHAR(24),
    [Email] NVARCHAR(60)  NOT NULL,
    [SupportRepId] INTEGER,
    CONSTRAINT [PK_Customer] PRIMARY KEY  ([CustomerId]),
    FOREIGN KEY ([SupportRepId]) REFERENCES [Employee] ([EmployeeId]) 
		ON DELETE NO ACTION ON UPDATE NO ACTION
);
```

## Indexes

- ([SupportRepId])
- UNIQUE ([CustomerId])

## Rows

- total=59

| column | latest | sample | sample |
|---|---|---|---|
| CustomerId | 59 | 57 | 7 |
| FirstName | Puja | Luis | Astrid |
| LastName | Srivastava | Rojas | Gruber |
| Company | null | null | null |
| Address | 3,Raj Bhavan Road | Calle Lira, 198 | Rotenturmstraße 4, 1010 Innere Stadt |
| City | Bangalore | Santiago | Vienne |
| State | null | null | null |
| Country | India | Chile | Austria |
| PostalCode | 560001 | null | 1010 |
| Phone | +91 080 22289999 | +56 (0)2 635 4444 | +43 01 5134505 |
| Fax | null | null | null |
| Email | puja_srivastava@yahoo.in | luisrojas@yahoo.cl | astrid.gruber@apple.at |
| SupportRepId | 3 | 5 | 5 |

## Columns

- CustomerId: unique identifier, int 1..59
  - stats: average=30, median=30
- FirstName: 57 distinct
- LastName: all distinct
- Company: "Apple Inc."=1, "Banco do Brasil S.A."=1, "Embraer - Empresa Brasileira de Aeronáutica S.A."=1, "Google Inc."=1, "JetBrains s.r.o."=1, "Microsoft Corporation"=1, "Riotur"=1, "Rogers Canada"=1, "Telus"=1, "Woodstock Discos"=1, nulls=49
- Address: all distinct
- City: 53 distinct
- State: 25 distinct, nulls=29
- Country: 24 distinct
- PostalCode: all distinct, nulls=4
- Phone: all distinct, nulls=1
- Fax: "+1 (212) 221-4679"=1, "+1 (408) 996-1011"=1, "+1 (425) 882-8081"=1, "+1 (604) 688-8756"=1, "+1 (650) 253-0000"=1, "+1 (780) 434-5565"=1, "+420 2 4172 5555"=1, "+55 (11) 3033-4564"=1, "+55 (11) 3055-8131"=1, "+55 (12) 3923-5566"=1, "+55 (21) 2271-7070"=1, "+55 (61) 3363-7855"=1, nulls=47
- Email: all distinct
- SupportRepId: 3=21, 4=20, 5=18, int 3..5


# Employee

## All rows

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


# Genre

```sql
CREATE TABLE [Genre]
(
    [GenreId] INTEGER  NOT NULL,
    [Name] NVARCHAR(120),
    CONSTRAINT [PK_Genre] PRIMARY KEY  ([GenreId])
);
```

## Indexes

- UNIQUE ([GenreId])

## Rows

- total=25

| column | latest | sample | sample |
|---|---|---|---|
| GenreId | 25 | 23 | 10 |
| Name | Opera | Alternative | Soundtrack |

## Columns

- GenreId: unique identifier, int 1..25
  - stats: average=13, median=13
- Name: all distinct


# Invoice

```sql
CREATE TABLE [Invoice]
(
    [InvoiceId] INTEGER  NOT NULL,
    [CustomerId] INTEGER  NOT NULL,
    [InvoiceDate] DATETIME  NOT NULL,
    [BillingAddress] NVARCHAR(70),
    [BillingCity] NVARCHAR(40),
    [BillingState] NVARCHAR(40),
    [BillingCountry] NVARCHAR(40),
    [BillingPostalCode] NVARCHAR(10),
    [Total] NUMERIC(10,2)  NOT NULL,
    CONSTRAINT [PK_Invoice] PRIMARY KEY  ([InvoiceId]),
    FOREIGN KEY ([CustomerId]) REFERENCES [Customer] ([CustomerId]) 
		ON DELETE NO ACTION ON UPDATE NO ACTION
);
```

## Indexes

- ([CustomerId])
- UNIQUE ([InvoiceId])

## Rows

- total=412

| column | latest | sample | sample |
|---|---|---|---|
| InvoiceId | 412 | 119 | 44 |
| CustomerId | 58 | 56 | 55 |
| InvoiceDate | 2013-12-22T00:00:00 | 2010-06-12T00:00:00 | 2009-07-07T00:00:00 |
| BillingAddress | 12,Community Centre | 307 Macacha Güemes | 421 Bourke Street |
| BillingCity | Delhi | Buenos Aires | Sidney |
| BillingState | null | null | NSW |
| BillingCountry | India | Argentina | Australia |
| BillingPostalCode | 110017 | 1106 | 2010 |
| Total | 1.99 | 1.98 | 3.96 |

## Columns

- InvoiceId: unique identifier, int 1..412
  - stats: average=206.5, median=206.5
- CustomerId: 59 distinct, int 1..59
  - stats: average=29.9296, median=30
  - top_values: 1=7, 2=7, 3=7, 4=7, 5=7, 6=7, 7=7, 8=7, 9=7, 10=7
- InvoiceDate: 354 distinct
- BillingAddress: 59 distinct
- BillingCity: 53 distinct
- BillingState: 25 distinct, nulls=202
- BillingCountry: 24 distinct
- BillingPostalCode: 55 distinct, nulls=28
- Total: 23 distinct, num 0.99..25.86
  - stats: average=5.65194, median=3.96


# InvoiceLine

```sql
CREATE TABLE [InvoiceLine]
(
    [InvoiceLineId] INTEGER  NOT NULL,
    [InvoiceId] INTEGER  NOT NULL,
    [TrackId] INTEGER  NOT NULL,
    [UnitPrice] NUMERIC(10,2)  NOT NULL,
    [Quantity] INTEGER  NOT NULL,
    CONSTRAINT [PK_InvoiceLine] PRIMARY KEY  ([InvoiceLineId]),
    FOREIGN KEY ([InvoiceId]) REFERENCES [Invoice] ([InvoiceId]) 
		ON DELETE NO ACTION ON UPDATE NO ACTION,
    FOREIGN KEY ([TrackId]) REFERENCES [Track] ([TrackId]) 
		ON DELETE NO ACTION ON UPDATE NO ACTION
);
```

## Indexes

- ([InvoiceId])
- ([TrackId])
- UNIQUE ([InvoiceLineId])

## Rows

- total=2240

| column | latest | sample | sample |
|---|---|---|---|
| InvoiceLineId | 2240 | 1689 | 565 |
| InvoiceId | 412 | 312 | 103 |
| TrackId | 3177 | 3268 | 3446 |
| UnitPrice | 1.99 | 0.99 | 0.99 |
| Quantity | 1 | 1 | 1 |

## Columns

- InvoiceLineId: unique identifier, int 1..2240
  - stats: average=1120.5, median=1120.5
- InvoiceId: 412 distinct, int 1..412
  - stats: average=206.869, median=207
  - top_values: 5=14, 12=14, 19=14, 26=14, 33=14, 40=14, 47=14, 54=14, 61=14, 68=14
- TrackId: 1984 distinct, int 1..3500
  - stats: average=1717.73, median=1708
  - top_values: 2=2, 8=2, 9=2, 20=2, 32=2, 48=2, 66=2, 84=2, 161=2, 162=2
- UnitPrice: 0.99=2129, 1.99=111
- Quantity: 1=2240


# MediaType

## All rows

| column | row 1 | row 2 | row 3 | row 4 | row 5 |
|---|---|---|---|---|---|
| MediaTypeId | 1 | 2 | 3 | 4 | 5 |
| Name | MPEG audio file | Protected AAC audio file | Protected MPEG-4 video file | Purchased AAC audio file | AAC audio file |


# Playlist

```sql
CREATE TABLE [Playlist]
(
    [PlaylistId] INTEGER  NOT NULL,
    [Name] NVARCHAR(120),
    CONSTRAINT [PK_Playlist] PRIMARY KEY  ([PlaylistId])
);
```

## Indexes

- UNIQUE ([PlaylistId])

## Rows

- total=18

| column | latest | sample | sample |
|---|---|---|---|
| PlaylistId | 18 | 12 | 14 |
| Name | On-The-Go 1 | Classical | Classical 101 - Next Steps |

## Columns

- PlaylistId: unique identifier, int 1..18
  - stats: average=9.5, median=9.5
- Name: "Audiobooks"=2, "Movies"=2, "Music"=2, "TV Shows"=2, "90’s Music"=1, "Brazilian Music"=1, "Classical"=1, "Classical 101 - Deep Cuts"=1, "Classical 101 - Next Steps"=1, "Classical 101 - The Basics"=1, "Grunge"=1, "Heavy Metal Classic"=1, "Music Videos"=1, "On-The-Go 1"=1


# PlaylistTrack

```sql
CREATE TABLE [PlaylistTrack]
(
    [PlaylistId] INTEGER  NOT NULL,
    [TrackId] INTEGER  NOT NULL,
    CONSTRAINT [PK_PlaylistTrack] PRIMARY KEY  ([PlaylistId], [TrackId]),
    FOREIGN KEY ([PlaylistId]) REFERENCES [Playlist] ([PlaylistId]) 
		ON DELETE NO ACTION ON UPDATE NO ACTION,
    FOREIGN KEY ([TrackId]) REFERENCES [Track] ([TrackId]) 
		ON DELETE NO ACTION ON UPDATE NO ACTION
);
```

## Indexes

- ([TrackId])
- UNIQUE ([PlaylistId], [TrackId])

## Rows

- total=8715

| column | latest | sample | sample |
|---|---|---|---|
| PlaylistId | 18 | 5 | 5 |
| TrackId | 597 | 1801 | 2792 |

## Columns

- PlaylistId: 1=3290, 8=3290, 5=1477, 3=213, 10=213, 12=75, 11=39, 17=26, 13=25, 14=25, 15=25, 16=15, 9=1, 18=1, int 1..18
- TrackId: 3503 distinct, int 1..3503
  - stats: average=1767.08, median=1773
  - top_values: 3403=5, 3404=5, 3408=5, 3409=5, 3410=5, 3411=5, 3415=5, 3416=5, 3417=5, 3418=5


# Track

```sql
CREATE TABLE [Track]
(
    [TrackId] INTEGER  NOT NULL,
    [Name] NVARCHAR(200)  NOT NULL,
    [AlbumId] INTEGER,
    [MediaTypeId] INTEGER  NOT NULL,
    [GenreId] INTEGER,
    [Composer] NVARCHAR(220),
    [Milliseconds] INTEGER  NOT NULL,
    [Bytes] INTEGER,
    [UnitPrice] NUMERIC(10,2)  NOT NULL,
    CONSTRAINT [PK_Track] PRIMARY KEY  ([TrackId]),
    FOREIGN KEY ([AlbumId]) REFERENCES [Album] ([AlbumId]) 
		ON DELETE NO ACTION ON UPDATE NO ACTION,
    FOREIGN KEY ([GenreId]) REFERENCES [Genre] ([GenreId]) 
		ON DELETE NO ACTION ON UPDATE NO ACTION,
    FOREIGN KEY ([MediaTypeId]) REFERENCES [MediaType] ([MediaTypeId]) 
		ON DELETE NO ACTION ON UPDATE NO ACTION
);
```

## Indexes

- ([AlbumId])
- ([GenreId])
- ([MediaTypeId])
- UNIQUE ([TrackId])

## Rows

- total=3503

| column | latest | sample | sample |
|---|---|---|---|
| TrackId | 3503 | 393 | 3138 |
| Name | Koyaanisqatsi | Tarde Em Itapoã | Slide It In |
| AlbumId | 347 | 34 | 141 |
| MediaTypeId | 2 | 1 | 1 |
| GenreId | 10 | 7 | 3 |
| Composer | Philip Glass | Vários | Coverdale |
| Milliseconds | 206005 | 313704 | 202475 |
| Bytes | 3305164 | 10344491 | 6615152 |
| UnitPrice | 0.99 | 0.99 | 0.99 |

## Columns

- TrackId: unique identifier, int 1..3503
  - stats: average=1752, median=1752
- Name: 3257 distinct
- AlbumId: 347 distinct, int 1..347
  - stats: average=140.929, median=141
  - top_values: 141=57, 23=34, 73=30, 229=26, 230=25, 251=25, 83=24, 231=24, 253=24, 24=23
- MediaTypeId: 1=3034, 2=237, 3=214, 5=11, 4=7, int 1..5
- GenreId: 25 distinct, int 1..25
  - stats: average=5.72538, median=3
  - top_values: 1=1297, 7=579, 3=374, 4=332, 2=130, 19=93, 6=81, 24=74, 21=64, 14=61
- Composer: 852 distinct, nulls=978
- Milliseconds: 3080 distinct, int 1071..5286953
  - stats: average=393599, median=255634
- Bytes: 3501 distinct, int 38747..1059546140
  - stats: average=3.35102e+07, median=8.1079e+06
- UnitPrice: 0.99=3290, 1.99=213
