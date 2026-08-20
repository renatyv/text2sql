# Additional Metadata

## Clarified Semantics

- `Invoice.Total` equals the sum of that invoice's `InvoiceLine.UnitPrice * Quantity` (verified: no mismatches aside from floating-point rounding); it is a derived/denormalized value, not independent.
- `Invoice` `Billing*` columns (Address/City/State/Country/PostalCode) are denormalized copies of the `Customer` address at sale time; in this dataset `BillingCountry` always equals `Customer.Country`.
- `InvoiceLine.Quantity` is always 1 here; `UnitPrice` is either 0.99 (majority) or 1.99, mirroring `Track.UnitPrice` tiers.
- `Track.AlbumId` and `Track.GenreId` are declared nullable, but no rows are null in this dataset.
- `Track.Composer` is nullable (about 978 nulls); `Bytes` and `Milliseconds` are close to distinct per row (per-file metadata).
- `MediaType` is a small lookup (5 rows) distinguishing audio vs video and protected vs purchased encodings.
- Every `Track` appears in at least one `PlaylistTrack` (no orphaned tracks vs playlists), so playlist coverage is complete.

## Potential Join Strategies

- **Sales-by-artist/genre/album**: join `Artist → Album (ArtistId) → Track (AlbumId) → InvoiceLine (TrackId) → Invoice` to attribute revenue; filter caveat: follow through `InvoiceLine` (the fact table), not `PlaylistTrack`.
- **Playlist composition**: `Playlist (PlaylistId) → PlaylistTrack → Track` to list members or counts per playlist. Cardinality caveat: ~66% of `PlaylistTrack` rows belong to just PlaylistId 1 and 8 (3290 each), so genre/media aggregates per playlist are skewed unless filtered to a specific playlist; `PlaylistTrack` uses a composite (PlaylistId, TrackId) key and duplicates are possible, so dedupe (e.g. for track totals) when joining.
- **Salesperson performance**: `Employee (EmployeeId) → Customer (SupportRepId) → Invoice (CustomerId)` to measure rep revenue; only EmployeeIds 3–5 are SupportReps (all Sales Support Agents), so restrict to those for sales analysis.
- **Org hierarchy**: self-join `Employee.ReportsTo → Employee.EmployeeId` gives the reporting tree; the General Manager (Id 1) has no `ReportsTo` (null), IT staff (7–8) report to IT Manager (6).
- **Genre/media-type mix per playlist**: `PlaylistTrack → Track → Genre / MediaType` to characterize playlist content; caveat: `Track.GenreId` can be null in schema, though non-null here.
- **Repeated/large purchasers**: `Invoice → Customer (Location fields)` to segment by country/city; caveat: many customers share identical addresses/cities, so aggregate on roles like `Country` before using address-level equality.