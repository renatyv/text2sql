# Additional Metadata

## Clarified Semantics

- `results.position` is NULL for non-classified (non-finishing) entries (~10,326 rows); `results.positionOrder` is always populated and represents the actual finishing ranking even for DNFs. `results.positionText` carries code letters beyond digits: `R` (retired), `W` (withdrew), `D` (disqualified), `N` (did not qualify), `E` (excluded), `F` (finished).
- `results.statusId` (join `status`) is the reason for the final condition: "Finished", "+N Laps", mechanical failures (Engine, Gearbox...), "Did not qualify", "Accident", etc. `status` values with digits/monikers identify non-finishers, not positions.
- `results.grid=0` appears (1,559 rows) — starting from pit/back of grid; `grid` and `position` are not necessarily comparable with a simple predicate.
- `results.fastestLap`, `fastestLapTime`, `fastestLapSpeed`, `rank` are NULL for most rows; `rank` is the top-10 fastest lap rank, `0` meaning not ranked.
- `lapTimes` has composite PK `(raceId, driverId, lap)`; `position` = running position during that lap; `milliseconds` = lap time in ms (base 0 for race start). `time` is the wall-clock lap time.
- `pitStops` has composite PK `(raceId, driverId, stop)` where `stop` is the sequential pit-stop number per driver (1..6); `duration`/`milliseconds` is the stop length; `lap`/`time` is when the stop occurred.
- `constructorResults.status` has only value `D` (= disqualified); otherwise NULL. This table records deprecated/early-era constructor points distinct from `constructorStandings`.
- `results.points` uses modern scoring; `constructorResults.points`/`constructorStandings.points` are constructor totals separately from driver `results.points`.
- `races.time` is mostly NULL (722 rows) — historical races lack a scheduled start time; `races.date` is always present.
- `pitStops` and `lapTimes` cover only the modern era (pitStops raceId 842..982; lapTimes heavily populated in recent years), so joins onto older races produce sparse results.
- `drivers.number`/`code` are NULL for most historical drivers; `drivers.dob` has one NULL.

## Potential Join Strategies

- **Grid vs. finishing position**: `qualifying.raceId=driverId` joins `results.raceId=driverId`; but `races.year/round` + `qualifying.round`... Use `results.grid` (from qualifying position) vs `results.positionOrder` rather than `results.position` (which is NULL on DNF). Filter `results.statusId=1` ("Finished") when comparing positions.
- **Pit-stop vs. lap detail per driver**: join `pitStops(raceId, driverId)` to `lapTimes(raceId, driverId)` on equal `lap` to get the lap on which a stop occurred and surrounding per-lap times. Same join key used to count stops per race/driver.
- **Laps completed vs per-lap data**: `results.laps` (total completed) vs `lapTimes.laps`; a driver's `results.laps` equals the number of `lapTimes` rows for that `(raceId, driverId)` except when DNF early.
- **Constructor standings per race**: `constructorStandings(raceId, constructorId)` and `constructorResults(raceId, constructorId)` both join `results(raceId, constructorId)`; aggregate `results.points` by `(raceId, constructorId)` to reconcile with per-race standings, handling `constructorResults.status='D'` exclusions.
- **Season/driver championship accumulation**: `driverStandings(raceId, driverId)` is cumulative through `raceId`; to filter by season join `races` on `raceId` and match `races.year` (standings rows exist even mid-season, so order by `races.date`/`round`).
- **Qualifying constructor context**: `qualifying(raceId, driverId, constructorId)` links drivers and constructors at a race before `results`; useful where `results.constructorId` differs (late driver swap) — `qualifying.constructorId` may not equal `results.constructorId` for the same driver.
- **Race/circuit/season fan-out**: `races` central hub joining `circuits` (per-location stats) and `seasons`. `circuits.alt` is entirely NULL (unusable); `results`/`driverStandings` cover nearly all `races` while `qualifying`, `pitStops`, `lapTimes` cover far fewer races — prefer the higher-cardinality tables when quantifying races.