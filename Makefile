.DEFAULT_GOAL := help
DB ?= neutron
BENCH_ARGS ?= --dataset $(DB) --phase phase0
METADATA_ARGS ?=

.PHONY: help generate-profiles generate-schema-links generate-metadata benchmark benchmark-1 benchmark-10 benchmark-100 benchmark-300

help:
	@printf '%s\n' 'make generate-profiles DB=neutron        # regenerate db-snooper profile' 'make generate-schema-links DB=neutron    # regenerate local link hints' 'make generate-metadata DB=neutron        # isolated Pi metadata agent' 'make benchmark BENCH_ARGS="--dataset neutron --phase pilot"' 'Useful args: DB=neutron|nova|dw, METADATA_ARGS="--max-turns 16"; benchmark accepts run_experiment.py args.' benchmark-1 benchmark-20 benchmark-100 benchmark-300

generate-profiles:
	@set -a; . ./.env; set +a; uv run db-snooper profile --db-type mysql --database "$(DB)" --host "$$MYSQL_HOST" --port "$$MYSQL_PORT" --user "$$MYSQL_USER" --password "$$MYSQL_PASSWORD" --output profiles

generate-schema-links:
	@uv run -m harness.generate_schema_links --database "$(DB)"

generate-metadata:
	@uv run -m harness.generate_metadata --database "$(DB)" $(METADATA_ARGS)

benchmark:
	@uv run run_experiment.py $(BENCH_ARGS)

benchmark-1:
	@uv run python run_experiment.py \
	 --phase main \
	 --samples dw=1 neutron=1 nova=1 \
	 --arms raw profile metadata \
	 --model openai/gpt-5.6-luna-pro\
	 --effort medium\
	 --workers 4\
	 --max-turns 15;

benchmark-10:
	@uv run python run_experiment.py \
	 --phase main \
	 --samples dw=10 neutron=10 nova=10 \
	 --arms raw profile metadata \
	 --model openai/gpt-5.6-luna-pro\
	 --effort medium\
	 --workers 4\
	 --max-turns 15;

benchmark-100:
	@uv run python run_experiment.py \
	 --phase main \
	 --samples dw=100 neutron=100 nova=100 \
	 --arms raw profile metadata \
	 --model openai/gpt-5.6-luna-pro\
	 --effort medium\
	 --workers 4\
	 --max-turns 15;

benchmark-300:
	@uv run python run_experiment.py \
	 --phase main \
	 --samples dw=300 neutron=300 nova=300 \
	 --arms raw profile metadata \
	 --model openai/gpt-5.6-luna-pro\
	 --effort medium\
	 --workers 4\
	 --max-turns 15;
