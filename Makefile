.DEFAULT_GOAL := help
DB ?= neutron
BENCH_ARGS ?= --dataset $(DB) --phase phase0
METADATA_ARGS ?=

.PHONY: help generate-profiles generate-schema-links generate-metadata benchmark

help:
	@printf '%s\n' 'make generate-profiles DB=neutron        # regenerate db-snooper profile' 'make generate-schema-links DB=neutron    # regenerate local link hints' 'make generate-metadata DB=neutron        # isolated Pi metadata agent' 'make benchmark BENCH_ARGS="--dataset neutron --phase pilot"' 'Useful args: DB=neutron|nova|dw, METADATA_ARGS="--max-turns 16"; benchmark accepts run_experiment.py args.'

generate-profiles:
	@set -a; . ./.env; set +a; uv run db-snooper profile --db-type mysql --database "$(DB)" --host "$$MYSQL_HOST" --port "$$MYSQL_PORT" --user "$$MYSQL_USER" --password "$$MYSQL_PASSWORD" --output profiles

generate-schema-links:
	@uv run -m harness.generate_schema_links --database "$(DB)"

generate-metadata:
	@uv run -m harness.generate_metadata --database "$(DB)" $(METADATA_ARGS)

benchmark:
	@uv run run_experiment.py $(BENCH_ARGS)
