# Schema Links

- version: 0.0.5
- dialect: sqlite
- database: file:/Users/renatyuldashev/Documents/ai-sql/custom-bench/data/sp2_lite_sqlite/databases/music.sqlite
- schema: main

## Declared PK/FK Links

Album.ArtistId -> Artist.ArtistId
Customer.SupportRepId -> Employee.EmployeeId
Employee.ReportsTo -> Employee.EmployeeId
Invoice.CustomerId -> Customer.CustomerId
InvoiceLine.InvoiceId -> Invoice.InvoiceId
InvoiceLine.TrackId -> Track.TrackId
PlaylistTrack.PlaylistId -> Playlist.PlaylistId
PlaylistTrack.TrackId -> Track.TrackId
Track.AlbumId -> Album.AlbumId
Track.GenreId -> Genre.GenreId
Track.MediaTypeId -> MediaType.MediaTypeId

## Inferred Links

All inferred links are implied by the declared PK/FK links above.
