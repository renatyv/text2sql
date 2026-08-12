"""Configuration constants for the db-snooper profiling experiment.

Implements the locked decisions in AGENT_PROFILE_EXPERIMENT_PLAN.md:
  * 3 arms: A (baseline), B (profile), C (zero-shot + profile)
  * pi is the only agent runner; deepseek-v4-flash via OpenRouter is the default model
  * identical caps across cells (turns, token guard, MySQL timeout)
"""
from __future__ import annotations

import os
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parent.parent
DATA_DIR = REPO_ROOT / "data"
PROFILES_DIR = REPO_ROOT / "profiles"
HARNESS_DIR = REPO_ROOT / "harness"
PI_EXTENSION = HARNESS_DIR / "pi_extension" / "sql_exec.ts"
RESULTS_DIR = REPO_ROOT / "results"
MANIFEST_DIR = REPO_ROOT / "runs"

# ---------------------------------------------------------------------------
# Datasets (plan §"Datasets & sampling")
# ---------------------------------------------------------------------------
# db_label -> (mysql_database, full question count for Phase-2 default sampling)
DATASETS: dict[str, dict] = {
    "neutron": {"mysql_db": "neutron", "full": 1017, "profile": "neutron.md"},
    "nova":    {"mysql_db": "nova",    "full": 1053, "profile": "nova.md"},
    "dw":      {"mysql_db": "dw",      "full": 5787, "profile": "dw.md"},
    "dw_real": {"mysql_db": "dw",      "full": 121,  "profile": "dw.md"},  # reuses dw profile/DB
}
# Phase-2 per-dataset sample sizes (plan). Overridable via --num-samples.
PHASE2_SAMPLE_SIZES = {"neutron": 1017, "nova": 1053, "dw": 500, "dw_real": 121}
PILOT_N = 20  # Phase-1 pilot (neutron)

# ---------------------------------------------------------------------------
# Arms
# ---------------------------------------------------------------------------
ARMS = ("A", "B", "C")
ARM_DESCRIPTIONS = {
    "A": "baseline: NL question + MySQL + sql_exec tool, no schema hints",
    "B": "profile:  same as A + frozen db-snooper <db>.md in the initial prompt",
    "C": "zero-shot + profile: single LLM call, profile + question, no DB / no tools",
}

# ---------------------------------------------------------------------------
# Model (plan §Locked decisions #2) — overridable via env for smoke tests.
# ---------------------------------------------------------------------------
DEFAULT_PROVIDER = os.environ.get("PI_PROVIDER", "openrouter")
DEFAULT_MODEL_ID = os.environ.get("PI_MODEL", "deepseek/deepseek-v4-flash-0731")
# When pi drives the model, the CLI selector is "<provider>/<model_id>".
PI_MODEL_SELECTOR = f"{DEFAULT_PROVIDER}/{DEFAULT_MODEL_ID}"
# Raw slug used for the direct OpenRouter call in arm C.
ZEROSHOT_MODEL_SLUG = DEFAULT_MODEL_ID
OPENROUTER_BASE_URL = os.environ.get("OPENROUTER_BASE_URL", "https://openrouter.ai/api/v1")

# ---------------------------------------------------------------------------
# Caps — identical across all cells (plan §Locked decisions #4)
# ---------------------------------------------------------------------------
MYSQL_QUERY_TIMEOUT = 20          # seconds, per MySQL query (gold/pred/exploration)
MAX_TURNS_PILOT = 6
MAX_TURNS_MAIN = 10
TOKEN_GUARD = 320_000             # runaway guard, total tokens/question
EXPLORE_ROW_CAP = 100             # rows returned per exploration sql_exec call
PI_WALL_CLOCK = 600               # seconds, hard subprocess kill for arms A/B
ZEROSHOT_WALL_CLOCK = 120         # seconds, hard timeout for arm C

# ---------------------------------------------------------------------------
# MySQL connection (loaded BEAVER DBs on port 3307)
# ---------------------------------------------------------------------------
MYSQL_HOST = os.environ.get("BEAVER_MYSQL_HOST", "127.0.0.1")
MYSQL_PORT = int(os.environ.get("BEAVER_MYSQL_PORT", "3307"))
MYSQL_USER = os.environ.get("BEAVER_MYSQL_USER", "beaver")
MYSQL_PWD = os.environ.get("BEAVER_MYSQL_PWD", "beaver")

# pi binary (defaults to PATH; override for a specific install)
PI_BIN = os.environ.get("PI_BIN", "pi")

# Sandbox base dir for per-question isolation (plan §Anti-cheat #1)
SANDBOX_ROOT = Path(os.environ.get("BEAVER_SANDBOX_ROOT", "/tmp/beaver-sbx"))


def profile_path(db_label: str) -> Path:
    return PROFILES_DIR / DATASETS[db_label]["profile"]


def mysql_db_for(db_label: str) -> str:
    return DATASETS[db_label]["mysql_db"]
