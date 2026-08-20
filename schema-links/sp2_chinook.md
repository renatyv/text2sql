# Schema Links

- version: 0.0.5
- dialect: sqlite
- database: file:/Users/renatyuldashev/Documents/ai-sql/custom-bench/data/sp2_lite_sqlite/databases/chinook.sqlite
- schema: main

## Declared PK/FK Links

albums.ArtistId -> artists.ArtistId
customers.SupportRepId -> employees.EmployeeId
employees.ReportsTo -> employees.EmployeeId
invoice_items.InvoiceId -> invoices.InvoiceId
invoice_items.TrackId -> tracks.TrackId
invoices.CustomerId -> customers.CustomerId
playlist_track.PlaylistId -> playlists.PlaylistId
playlist_track.TrackId -> tracks.TrackId
tracks.AlbumId -> albums.AlbumId
tracks.GenreId -> genres.GenreId
tracks.MediaTypeId -> media_types.MediaTypeId

## Inferred Links

All inferred links are implied by the declared PK/FK links above.
