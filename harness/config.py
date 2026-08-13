"""Configuration constants for the db-snooper profiling experiment.

Arms are a 2×2 matrix over profile and aggregated-metadata injection. Database
tools and the error-avoidance checklist are fixed across every arm.
  * pi is the default runner; BEAVER_AGENT can select another installed CLI
  * identical caps across cells (turns, token guard, MySQL timeout)
"""
from __future__ import annotations

import json
import os
import secrets
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parent.parent


def _load_env_file() -> None:
    """Load REPO_ROOT/.env into os.environ (without overwriting real env vars).

    Stdlib only (no python-dotenv dependency). Keys already present in the real
    environment win, so exports on the shell still take precedence. Values are
    stripped of surrounding quotes; blank/`` lines and ``#`` comments are skipped.
    Called at import time, before the ``os.environ.get`` lookups below, so every
    module that imports ``config`` picks up the local credentials automatically.
    """
    env_path = REPO_ROOT / ".env"
    if not env_path.is_file():
        return
    for raw in env_path.read_text(encoding="utf-8").splitlines():
        line = raw.strip()
        if not line or line.startswith("#") or "=" not in line:
            continue
        key, _, value = line.partition("=")
        key = key.strip()
        if not key or key in os.environ:  # real env wins
            continue
        value = value.strip()
        if len(value) >= 2 and value[0] == value[-1] and value[0] in ("'", '"'):
            value = value[1:-1]
        os.environ[key] = value


_load_env_file()

DATA_DIR = REPO_ROOT / "data"
PROFILES_DIR = REPO_ROOT / "profiles"
SCHEMA_LINKS_DIR = REPO_ROOT / "schema-links"
GENERATED_METADATA_DIR = REPO_ROOT / "generated-metadata"
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
# Arms (profile × aggregated metadata)
# ---------------------------------------------------------------------------
# All arms use the same agent, MySQL tools, checklist, caps, and model. Only the
# two injected artifacts vary, so pairwise differences isolate their effects.
ARMS: dict[str, dict] = {
    "raw": {
        "tools": True, "profile": False, "metadata": False, "checklist": True,
        "description": "raw database access",
    },
    "profile": {
        "tools": True, "profile": True, "metadata": False, "checklist": True,
        "description": "raw database access + db-snooper profile",
    },
    "metadata": {
        "tools": True, "profile": False, "metadata": True, "checklist": True,
        "description": "raw database access + aggregated metadata",
    },
    "profile_metadata": {
        "tools": True, "profile": True, "metadata": True, "checklist": True,
        "description": "raw database access + profile + aggregated metadata",
    },
}

# name -> human description (kept as a flat dict so the orchestrator's progress
# bar and summary printer can do ARM_DESCRIPTIONS[arm] unchanged).
ARM_DESCRIPTIONS = {name: spec["description"] for name, spec in ARMS.items()}


def arm_spec(name: str) -> dict:
    """Return the ``{tools, profile, checklist, description}`` spec for an arm."""
    try:
        return ARMS[name]
    except KeyError:
        raise KeyError(f"unknown arm '{name}'; choose from {list(ARMS)}")


# Pairwise comparisons reported when both selected arms are present.
PAIRWISE = [
    ("raw", "profile"),
    ("raw", "metadata"),
    ("profile", "profile_metadata"),
    ("metadata", "profile_metadata"),
]

# ---------------------------------------------------------------------------
# Model (plan §Locked decisions #2) — overridable via env for smoke tests.
# ---------------------------------------------------------------------------
DEFAULT_PROVIDER = os.environ.get("PI_PROVIDER", "openrouter")
DEFAULT_MODEL_ID = os.environ.get("PI_MODEL", "deepseek/deepseek-v4-flash-0731")
# When pi drives the model, the CLI selector is "<provider>/<model_id>".
PI_MODEL_SELECTOR = f"{DEFAULT_PROVIDER}/{DEFAULT_MODEL_ID}"
# Reasoning effort passed to pi via --thinking (off|minimal|low|medium|high|
# xhigh|max). low by default: DeepSeek-V4-flash is strong enough at low effort
# for text-to-SQL, and this caps per-question token cost/latency. Overridable
# via env so ablations can raise it without code changes.
PI_THINKING = os.environ.get("PI_THINKING", "low")
# Raw slug used for the direct OpenRouter call in the zero-shot arm.
ZEROSHOT_MODEL_SLUG = DEFAULT_MODEL_ID
OPENROUTER_BASE_URL = os.environ.get("OPENROUTER_BASE_URL", "https://openrouter.ai/api/v1")

# Containerized agent CLI. All choices keep the same ephemeral Docker sandbox,
# MySQL account, and OpenRouter-only egress boundary. BEAVER_AGENT_MODEL is a
# agent-specific OpenRouter model name; provider prefixes are added by the
# relevant CLI where required.
CONTAINER_AGENT = os.environ.get("BEAVER_AGENT", "pi").lower()
AGENT_MODELS = {
    "pi": DEFAULT_MODEL_ID,
    "claude": "~anthropic/claude-sonnet-latest",
    "opencode": "~openai/gpt-latest",
    "codex": "~openai/gpt-latest",
}
if CONTAINER_AGENT not in AGENT_MODELS:
    raise ValueError(f"unknown BEAVER_AGENT={CONTAINER_AGENT!r}; choose from {list(AGENT_MODELS)}")
CONTAINER_AGENT_MODEL = os.environ.get("BEAVER_AGENT_MODEL", AGENT_MODELS[CONTAINER_AGENT])


def _load_openrouter_rates() -> dict[str, float]:
    """OpenRouter $/Mtok rates for the locked model, read from
    openrouter_models.json (the same fragment setup_openrouter.py merges into pi).

    Falls back to the known DeepSeek V4 Flash 0731 rates if the file is missing
    or shaped differently. Used by runner_zeroshot to price the zero-shot arm so
    its `cost` dict matches the shape pi returns for the agentic arms (dollars,
    not $/Mtok).
    """
    fallback = {"input": 0.08, "output": 0.18, "cacheRead": 0.016, "cacheWrite": 0.0}
    frag = HARNESS_DIR / "openrouter_models.json"
    try:
        data = json.loads(frag.read_text(encoding="utf-8"))
        models = data["providers"]["openrouter"]["models"]
        rates = next(m["cost"] for m in models if m.get("id") == DEFAULT_MODEL_ID)
        return {k: float(rates.get(k, fallback[k])) for k in fallback}
    except Exception:
        return fallback


# $/Mtok. Single source of truth for pricing the zero-shot arm and cost projections.
OPENROUTER_RATES = _load_openrouter_rates()

# ---------------------------------------------------------------------------
# Caps — identical across all cells (plan §Locked decisions #4)
# ---------------------------------------------------------------------------
MYSQL_QUERY_TIMEOUT = 10          # seconds, per MySQL query (gold/pred/exploration)
MAX_TURNS_PILOT = 6
MAX_TURNS_MAIN = 6
TOKEN_GUARD = 320_000             # runaway guard, total tokens/question
EXPLORE_ROW_CAP = 100             # rows returned per exploration sql_exec call
PI_WALL_CLOCK = 300               # seconds; exceeding the evaluation budget is incorrect
ZEROSHOT_WALL_CLOCK = 120         # seconds, hard timeout for the zero-shot arm
PROTOCOL_VERSION = 3              # bump when runner semantics change outside prompt/config hashes
PI_AGENT_VERSION = "0.84.1"       # pinned in Dockerfile.agent

# ---------------------------------------------------------------------------
# MySQL connection (loaded BEAVER DBs on port 3307).
# Reads BEAVER_MYSQL_* first (legacy harness names), then falls back to the
# MYSQL_* names used in .env / data/build_local.py, then to the defaults.
# ---------------------------------------------------------------------------
MYSQL_HOST = os.environ.get("BEAVER_MYSQL_HOST") or os.environ.get("MYSQL_HOST") or "127.0.0.1"
MYSQL_PORT = int(os.environ.get("BEAVER_MYSQL_PORT") or os.environ.get("MYSQL_PORT") or "3307")
MYSQL_USER = os.environ.get("BEAVER_MYSQL_USER") or os.environ.get("MYSQL_USER") or "beaver"
MYSQL_PWD = os.environ.get("BEAVER_MYSQL_PWD") or os.environ.get("MYSQL_PASSWORD") or "beaver"
# The host uses MYSQL_* above to build/score the benchmark. Agents must never
# receive those credentials: setup() provisions this separate SELECT-only user.
AGENT_MYSQL_USER = os.environ.get("BEAVER_AGENT_MYSQL_USER", "beaver_agent")
AGENT_MYSQL_PWD = os.environ.get("BEAVER_AGENT_MYSQL_PWD") or secrets.token_urlsafe(32)

# pi binary (defaults to PATH; override for a specific install). Used by the
# legacy --no-container runner; the containerized runner uses the pi baked into
# CONTAINER_IMAGE instead.
PI_BIN = os.environ.get("PI_BIN", "pi")

# Sandbox base dir for per-question isolation (plan §Anti-cheat #1).
# Used by the legacy host runner; the container runner is ephemeral per query.
SANDBOX_ROOT = Path(os.environ.get("BEAVER_SANDBOX_ROOT", "/tmp/beaver-sbx"))

# ---------------------------------------------------------------------------
# Containerized agent (plan: containerize pi). See harness/network.py for the
# full topology. The default image/tag matches Dockerfile.agent / Dockerfile.proxy.
# ---------------------------------------------------------------------------
CONTAINER_IMAGE = os.environ.get("BEAVER_AGENT_IMAGE", "beaver-agent")
EGRESS_PROXY_IMAGE = os.environ.get("BEAVER_PROXY_IMAGE", "beaver-egress-proxy")
# Networks: beaver-net (egress, has internet) + beaver-sandbox (internal, no
# internet). Agents live on beaver-sandbox only.
AGENT_NET_EGRESS = os.environ.get("BEAVER_NET_EGRESS", "beaver-net")
AGENT_NET_SANDBOX = os.environ.get("BEAVER_NET_SANDBOX", "beaver-sandbox")
# Container names.
MYSQL_CONTAINER = os.environ.get("BEAVER_MYSQL_CONTAINER", "beaver-mysql")
EGRESS_PROXY_CONTAINER = os.environ.get("BEAVER_PROXY_CONTAINER", "beaver-egress-proxy")
EGRESS_PROXY_PORT = int(os.environ.get("BEAVER_PROXY_PORT", "8888"))
# The experiment permits exactly one external hostname. Keep this out of the
# environment so a stray shell setting cannot silently broaden agent egress.
EGRESS_ALLOW_HOSTS = "openrouter.ai"
# Per-container resource caps (contain runaway bash/SQL from one question).
CONTAINER_CPUS = os.environ.get("BEAVER_CONTAINER_CPUS", "1.0")
CONTAINER_MEMORY = os.environ.get("BEAVER_CONTAINER_MEMORY", "1g")
CONTAINER_PIDS_LIMIT = os.environ.get("BEAVER_CONTAINER_PIDS_LIMIT", "256")
# MySQL as seen FROM INSIDE the agent container (by container name, port 3306).
# The host-side scorer still uses MYSQL_HOST/MYSQL_PORT above (127.0.0.1:3307).
MYSQL_HOST_CONTAINER = os.environ.get("BEAVER_MYSQL_HOST_CONTAINER", MYSQL_CONTAINER)
MYSQL_PORT_CONTAINER = int(os.environ.get("BEAVER_MYSQL_PORT_CONTAINER", "3306"))
def profile_path(db_label: str) -> Path:
    return PROFILES_DIR / DATASETS[db_label]["profile"]


def schema_links_path(db_label: str) -> Path:
    return SCHEMA_LINKS_DIR / DATASETS[db_label]["profile"]


def metadata_path(db_label: str) -> Path:
    return GENERATED_METADATA_DIR / DATASETS[db_label]["profile"]


def mysql_db_for(db_label: str) -> str:
    return DATASETS[db_label]["mysql_db"]
