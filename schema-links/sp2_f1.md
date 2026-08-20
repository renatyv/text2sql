# Schema Links

- version: 0.0.5
- dialect: sqlite
- database: file:/Users/renatyuldashev/Documents/ai-sql/custom-bench/data/sp2_lite_sqlite/databases/f1.sqlite
- schema: main

## Declared PK/FK Links

No declared PK/FK links found.

## Inferred Links

### driver
- inferred: constructor_standings.position, constructor_standings.wins, driver_standings.driver_id, driver_standings.driver_standings_id, driver_standings.position, driver_standings.wins, driver_standings_ext.driver_id, driver_standings_ext.driver_standings_id, driver_standings_ext.position, driver_standings_ext.wins, drivers.driver_id, drivers.number, drivers_ext.driver_id, drivers_ext.number, drives.driver_id, drives.first_round, drives.last_round, lap_time_stats.driver_id, lap_times.driver_id, lap_times.lap, pit_stops.driver_id, pit_stops.lap, qualifying.driver_id, qualifying.position, races.round, races_ext.round, results.driver_id, results.fastest_lap, results.laps, results.number, results.position, results.position_order, results.rank, retirements.driver_id, retirements.position_order, sprint_results.driver_id, sprint_results.fastest_lap, sprint_results.laps, sprint_results.position, sprint_results.position_order, tdr_overrides.team_driver_rank, team_driver_ranks.driver_id

### constructor
- inferred: constructor_results.constructor_id, constructor_results.constructor_results_id, constructor_standings.constructor_id, constructor_standings.constructor_standings_id, constructors.constructor_id, constructors_ext.constructor_id, drives.constructor_id, qualifying.constructor_id, results.constructor_id, sprint_results.constructor_id, team_driver_ranks.constructor_id

### race
- inferred: constructor_results.race_id, constructor_standings.race_id, driver_standings.race_id, driver_standings_ext.race_id, lap_time_stats.race_id, lap_times.race_id, qualifying.race_id, races.race_id, races_ext.race_id, results.race_id, retirements.race_id

### year
- inferred: drives.year, races.year, races_ext.year, seasons.year, team_driver_ranks.year

### circuit
- inferred: circuits.circuit_id, circuits_ext.circuit_id, races.circuit_id, races_ext.circuit_id

### status
- inferred: results.status_id, retirements.status_id, sprint_results.status_id, status.status_id

### results
- inferred: results.grid, sprint_results.grid

### time
- inferred: races.fp3_time, races_ext.fp1_time

### time
- inferred: races.fp1_time, races_ext.fp3_time
