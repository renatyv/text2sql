# Schema Links

- generator: local introspection
- dialect: sqlite
- database: formula_1

## Declared Links

- `constructorResults.constructorId` → `constructors.constructorId`
- `constructorResults.raceId` → `races.raceId`
- `constructorStandings.constructorId` → `constructors.constructorId`
- `constructorStandings.raceId` → `races.raceId`
- `driverStandings.driverId` → `drivers.driverId`
- `driverStandings.raceId` → `races.raceId`
- `lapTimes.driverId` → `drivers.driverId`
- `lapTimes.raceId` → `races.raceId`
- `pitStops.driverId` → `drivers.driverId`
- `pitStops.raceId` → `races.raceId`
- `qualifying.constructorId` → `constructors.constructorId`
- `qualifying.driverId` → `drivers.driverId`
- `qualifying.raceId` → `races.raceId`
- `races.circuitId` → `circuits.circuitId`
- `races.year` → `seasons.year`
- `results.constructorId` → `constructors.constructorId`
- `results.driverId` → `drivers.driverId`
- `results.raceId` → `races.raceId`
- `results.statusId` → `status.statusId`

## Same-name Candidates

- `circuitId`: `circuits.circuitId`, `races.circuitId`
- `constructorId`: `constructorResults.constructorId`, `constructorStandings.constructorId`, `constructors.constructorId`, `qualifying.constructorId`, `results.constructorId`
- `driverId`: `driverStandings.driverId`, `drivers.driverId`, `lapTimes.driverId`, `pitStops.driverId`, `qualifying.driverId`, `results.driverId`
- `lap`: `lapTimes.lap`, `pitStops.lap`
- `milliseconds`: `lapTimes.milliseconds`, `pitStops.milliseconds`, `results.milliseconds`
- `name`: `circuits.name`, `constructors.name`, `races.name`
- `nationality`: `constructors.nationality`, `drivers.nationality`
- `number`: `drivers.number`, `qualifying.number`, `results.number`
- `points`: `constructorResults.points`, `constructorStandings.points`, `driverStandings.points`, `results.points`
- `position`: `constructorStandings.position`, `driverStandings.position`, `lapTimes.position`, `qualifying.position`, `results.position`
- `positionText`: `constructorStandings.positionText`, `driverStandings.positionText`, `results.positionText`
- `raceId`: `constructorResults.raceId`, `constructorStandings.raceId`, `driverStandings.raceId`, `lapTimes.raceId`, `pitStops.raceId`, `qualifying.raceId`, `races.raceId`, `results.raceId`
- `status`: `constructorResults.status`, `status.status`
- `statusId`: `results.statusId`, `status.statusId`
- `time`: `lapTimes.time`, `pitStops.time`, `races.time`, `results.time`
- `url`: `circuits.url`, `constructors.url`, `drivers.url`, `races.url`, `seasons.url`
- `wins`: `constructorStandings.wins`, `driverStandings.wins`
- `year`: `races.year`, `seasons.year`
