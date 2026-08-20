# Schema Links

- version: 0.0.5
- dialect: sqlite
- database: file:/Users/renatyuldashev/Documents/ai-sql/custom-bench/data/bird_mini_dev/databases/dev_databases/formula_1/formula_1.sqlite
- schema: main

## Declared PK/FK Links

constructorResults.constructorId -> constructors.constructorId
constructorResults.raceId -> races.raceId
constructorStandings.constructorId -> constructors.constructorId
constructorStandings.raceId -> races.raceId
driverStandings.driverId -> drivers.driverId
driverStandings.raceId -> races.raceId
lapTimes.driverId -> drivers.driverId
lapTimes.raceId -> races.raceId
pitStops.driverId -> drivers.driverId
pitStops.raceId -> races.raceId
qualifying.constructorId -> constructors.constructorId
qualifying.driverId -> drivers.driverId
qualifying.raceId -> races.raceId
races.circuitId -> circuits.circuitId
races.year -> seasons.year
results.constructorId -> constructors.constructorId
results.driverId -> drivers.driverId
results.raceId -> races.raceId
results.statusId -> status.statusId

## Inferred Links

### lap
- inferred: lapTimes.lap, pitStops.lap, results.laps

### shared values
- inferred: driverStandings.position, results.number
