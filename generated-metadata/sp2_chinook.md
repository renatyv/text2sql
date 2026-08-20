# Additional Metadata

## Clarified Semantics

- `employees.ReportsTo` is a self-referencing FK to `employees.EmployeeId`; the org root (EmployeeId 1, General Manager) has `ReportsTo = NULL`, others point upward. Only employees 3, 4, 5 (Sales Support Agents) are referenced by `customers.SupportRepId`.
- `playlist_track` is a pure many-to-many junction between `playlists` and `tracks`; its composite PK spans both `PlaylistId` and `TrackId`, so a given track can appear in multiple playlists.
- `invoice_items.Quantity` is always 1, so each line amount equals `UnitPrice`; `invoices.Total` is effectively the sum of its line `UnitPrice` values.
- `tracks.Composer` has ~978 NULLs (tracks without a listed composer); `tracks.Milliseconds`/`Bytes` are file size/length metadata, not song content semantics.
- `tracks.MediaTypeId` (1 = MPEG audio) dominates with 3034 of 3503 tracks; only 5 fixed media types exist.
- `tracks.AlbumId` is nullable while `tracks.MediaTypeId` is NOT NULL; not every track is tied to an album.
- `customers.Company` is null for the majority (49/59); company values are incidental, not a reliable grouping key.
- `invoices.Billing*` columns duplicate customer address info per sale and are not linked by any key.

## Potential Join Strategies

- **Sales attribution by support rep**: `customers.SupportRepId = employees.EmployeeId` then `customers.CustomerId = invoices.CustomerId` to measure revenue per sales agent. Caveat: only the 3 sales support agents (EmployeeId 3–5) are reachable; manager/IT staff have no customers.
- **Purchase lineage**: `invoice_items.TrackId = tracks.TrackId`, then `tracks.AlbumId = albums.AlbumId`, then `albums.ArtistId = artists.ArtistId` to attribute sold tracks to albums/artists. Caveat: only 1984 of 3503 tracks are actually sold; many tracks have no album (NULL AlbumId).
- **Track-to-playlist coverage**: `playlist_track.TrackId = tracks.TrackId` to see which tracks are curated into playlists. Caveat: playlist membership is sparse per track but overall nearly all tracks appear; `playlist_track` (8715 rows) exceeds `tracks` (3503), so an inner join fans out.
- **Genre/media-type analysis**: `tracks.GenreId = genres.GenreId` and `tracks.MediaTypeId = media_types.MediaTypeId` (both indexed) to bucket catalog or sales by genre/format.
- **Org hierarchy**: self-join `employees.ReportsTo = employees.EmployeeId` to flatten manager/report chains; note the root employee has NULL and the manager rows (1, 6) are the parents.
- **Full catalog-sales fan-out caveat**: joining `tracks` → `playlist_track` → `invoice_items` in one pass multiplies rows because each track can match multiple playlists and multiple invoices; prefer aggregating at the `tracks` (or `invoice_items`) level before further joins to avoid count inflation.