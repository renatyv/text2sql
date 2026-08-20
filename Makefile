.DEFAULT_GOAL := help
DB ?= neutron
GENERATE_DBS := neutron nova dw bird_mini_dev sp2_lite_sqlite
ifeq ($(origin DB), file)
PROFILE_DBS := $(GENERATE_DBS)
else
PROFILE_DBS := $(DB)
endif
BENCH_ARGS ?= --dataset $(DB) --phase phase0
METADATA_ARGS ?=
SPIDER2_REPO ?= $(HOME)/.cache/custom-bench/Spider2
SPIDER2_ZIP ?= $(HOME)/.cache/custom-bench/spider2-localdb.zip
BIRD_ZIP ?= $(HOME)/.cache/custom-bench/minidev.zip
MODEL_ARGS ?= --model openai/gpt-5.6-luna-pro --effort medium

.PHONY: help agent-image generate-profiles generate-schema-links generate-metadata benchmark benchmark-1 benchmark-10 benchmark-100 benchmark-300 load-bird load-spider2 benchmark-bird benchmark-spider2

help:
	@printf '%s\n' 'make generate-profiles                   # all BEAVER, BIRD, and Spider2 profiles' 'make generate-schema-links               # all local link hints' 'make generate-metadata                   # all metadata (after profiles and links)' 'Add DB=neutron to run one dataset; METADATA_ARGS="--max-turns 16". SQLite setup: make load-bird / load-spider2 first.' 'make benchmark BENCH_ARGS="--dataset neutron --phase pilot"' benchmark-1 benchmark-20 benchmark-100 benchmark-300

agent-image:
	docker build -t beaver-agent -f Dockerfile.agent .

generate-profiles:
	for db in $(PROFILE_DBS); do uv run -m harness.generate_profiles --database "$$db"; done

generate-schema-links:
	for db in $(PROFILE_DBS); do uv run -m harness.generate_schema_links --database "$$db"; done

generate-metadata:
	for db in $(PROFILE_DBS); do uv run -m harness.generate_metadata --database "$$db" $(METADATA_ARGS); done

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

# --- BIRD Mini-Dev & Spider 2.0-lite (native SQLite benchmarks) ------------
# Both stages run agents against the original .sqlite files (nothing is
# loaded into MySQL); see README "Other benchmarks" for the one-time downloads.

load-bird: ## fetch minidev.zip (if needed) and build data/bird_mini_dev
	@test -f "$(BIRD_ZIP)" || curl -L -o "$(BIRD_ZIP)" "https://bird-bench.oss-cn-beijing.aliyuncs.com/minidev.zip"
	@uv run python data/build_bird_mini_dev.py --zip "$(BIRD_ZIP)"

load-spider2: ## sparse-clone Spider2 + fetch localdb zip (if needed), build data/sp2_lite_sqlite
	@test -d "$(SPIDER2_REPO)/spider2-lite" || { git clone --filter=blob:none --sparse --depth 1 \
	  https://github.com/xlang-ai/Spider2.git "$(SPIDER2_REPO)" && \
	  cd "$(SPIDER2_REPO)" && git sparse-checkout set --no-cone \
	  '/spider2-lite/spider2-lite.jsonl' '/spider2-lite/evaluation_suite/**' '/spider2-lite/resource/documents/**'; }
	@test -f "$(SPIDER2_ZIP)" || curl -L -o "$(SPIDER2_ZIP)" \
	  "https://drive.usercontent.google.com/download?id=1coEVsCZq-Xvj9p2TnhBFoFTsY-UoYGmG&export=download&authuser=0&confirm=t"
	@uv run python data/build_spider2.py --repo "$(SPIDER2_REPO)" --dbs-zip "$(SPIDER2_ZIP)"

benchmark-bird:
	@uv run python run_experiment.py \
	 --phase main \
	 --dataset bird_mini_dev \
	 --samples bird_mini_dev=500 \
	 --arms raw profile \
	 $(MODEL_ARGS) \
	 --workers 4\
	 --max-turns 15;

benchmark-spider2:
	@uv run python run_experiment.py \
	 --phase main \
	 --dataset sp2_lite_sqlite \
	 --samples sp2_lite_sqlite=135 \
	 --arms raw profile \
	 $(MODEL_ARGS) \
	 --workers 4\
	 --max-turns 15;
