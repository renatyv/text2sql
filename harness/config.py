"""Configuration constants for the db-snooper profiling experiment.

Arms are a 2×2 matrix over profile and aggregated-metadata injection. Database
tools and the error-avoidance checklist are fixed across every arm.
  * pi is the default runner; BEAVER_AGENT can select another installed CLI
  * identical caps across cells (turns, token guard, MySQL timeout)
"""
from __future__ import annotations

import atexit
import json
import os
import secrets
import tempfile
from pathlib import Path
from urllib.parse import quote
from urllib.request import Request, urlopen

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
# db_label -> spec. BEAVER datasets run on MySQL (one schema per dataset);
# bird_mini_dev / sp2_lite_sqlite run natively on SQLite files (one file per
# benchmark database, referenced per question — nothing is loaded into MySQL,
# so the original benchmark dialects are preserved end-to-end).
#
# Keys (see _DATASET_DEFAULTS for the full shape):
#   engine   "mysql" | "sqlite" — which executor agents and the scorer use
#   mysql_db MySQL schema (engine=mysql only); per-question `db` overrides it
#   scoring  scorer comparison mode: "beaver" | "bird" | "spider2"
#   strata   question fields used for stratified sampling
#   subgroups question fields reported as by_<field> subgroups in summary.json
#   databases_dir (engine=sqlite) host dir holding the .sqlite files; it is
#            mounted read-only at /dbs in the agent container
DATASETS: dict[str, dict] = {
    "neutron": {"mysql_db": "neutron", "full": 1017, "profile": "neutron.md"},
    "nova":    {"mysql_db": "nova",    "full": 1053, "profile": "nova.md"},
    "dw":      {"mysql_db": "dw",      "full": 5787, "profile": "dw.md"},
    "dw_real": {"mysql_db": "dw",      "full": 121,  "profile": "dw.md"},  # reuses dw profile/DB
    # BIRD Mini-Dev (bird-bench/mini_dev), SQLite build: 500 questions, 11
    # databases, official SQLite gold SQL. Scoring follows BIRD's official
    # execution-accuracy semantics (unordered set comparison).
    "bird_mini_dev": {
        "benchmark": "bird", "engine": "sqlite", "scoring": "bird",
        "strata": ["difficulty"], "subgroups": ["difficulty", "query_shape"],
        "full": 500, "databases_dir": "data/bird_mini_dev/databases",
    },
    # Spider 2.0-lite, SQLite subset: local .sqlite databases + official gold
    # CSVs (gold SQL is only partially released, so scoring compares the
    # predicted result rows against the gold CSV with the official fuzzy match).
    "sp2_lite_sqlite": {
        "benchmark": "spider2", "engine": "sqlite", "scoring": "spider2",
        "strata": ["db_id"], "subgroups": ["db_id", "query_shape"],
        "full": 135, "databases_dir": "data/sp2_lite_sqlite/databases",
    },
}

_DATASET_DEFAULTS = {
    "benchmark": "beaver",
    "engine": "mysql",
    "scoring": "beaver",
    "strata": ["category", "contains_domain_knowledge"],
    "subgroups": ["category", "contains_domain_knowledge", "query_shape"],
}


def dataset_spec(db_label: str) -> dict:
    """Dataset spec with benchmark-plumbing defaults filled in."""
    try:
        spec = dict(_DATASET_DEFAULTS)
        spec.update(DATASETS[db_label])
    except KeyError:
        raise KeyError(f"unknown dataset '{db_label}'; choose from {list(DATASETS)}") from None
    return spec


def engine_for(db_label: str) -> str:
    return dataset_spec(db_label)["engine"]


# Phase-2 per-dataset sample sizes (plan). Overridable via --num-samples.
PHASE2_SAMPLE_SIZES = {"neutron": 1017, "nova": 1053, "dw": 500, "dw_real": 121,
                       "bird_mini_dev": 500, "sp2_lite_sqlite": 135}
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
# xhigh|max). Overridable via the CLI or env for effort ablations.
PI_THINKING = os.environ.get("PI_THINKING", "medium")
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
CONTAINER_AGENT_MODEL = os.environ.get("BEAVER_AGENT_MODEL", AGENT_MODELS[CONTAINER_AGENT]).removeprefix("openrouter/")


def _load_openrouter_rates(model_id: str = DEFAULT_MODEL_ID) -> dict[str, float]:
    """OpenRouter $/Mtok rates for ``model_id``, read from
    openrouter_models.json (the same fragment setup_openrouter.py merges into pi).

    Unknown custom models report zero cost rather than DeepSeek's rate.
    """
    fallback = {"input": 0.08, "output": 0.18, "cacheRead": 0.016, "cacheWrite": 0.0}
    frag = HARNESS_DIR / "openrouter_models.json"
    try:
        data = json.loads(frag.read_text(encoding="utf-8"))
        models = data["providers"]["openrouter"]["models"]
        rates = next(m["cost"] for m in models if m.get("id") == model_id)
        return {k: float(rates.get(k, fallback[k])) for k in fallback}
    except Exception:
        return fallback if model_id == "deepseek/deepseek-v4-flash-0731" else dict.fromkeys(fallback, 0.0)


# $/Mtok. Single source of truth for pricing the zero-shot arm and cost projections.
OPENROUTER_RATES = _load_openrouter_rates()
_MODEL_CONFIGS: dict[str, Path] = {}
_REMOTE_MODELS: dict[str, dict] = {}


def _per_million(pricing: dict, key: str) -> float:
    """Convert OpenRouter's per-token price strings to pi's $/Mtok units."""
    try:
        return round(float(pricing.get(key, 0)) * 1_000_000, 12)
    except (TypeError, ValueError):
        return 0.0


def _fetch_openrouter_model(model: str) -> dict:
    """Resolve a complete pi model definition from OpenRouter once per run."""
    if cached := _REMOTE_MODELS.get(model):
        return cached
    headers = {"Accept": "application/json", "User-Agent": "beaver-profile-harness"}
    if api_key := os.environ.get("OPENROUTER_API_KEY"):
        headers["Authorization"] = f"Bearer {api_key}"
    url = f"{OPENROUTER_BASE_URL.rstrip('/')}/model/{quote(model, safe='/:~')}"
    try:
        with urlopen(Request(url, headers=headers), timeout=30) as response:
            payload = json.loads(response.read())
    except Exception as e:
        raise RuntimeError(f"failed to resolve OpenRouter metadata for {model!r}: {e}") from e

    remote = payload.get("data") if isinstance(payload, dict) else None
    if not isinstance(remote, dict):
        raise RuntimeError(f"OpenRouter returned no model metadata for {model!r}")
    top = remote.get("top_provider") or {}
    context_window = top.get("context_length") or remote.get("context_length")
    max_tokens = top.get("max_completion_tokens") or remote.get("max_completion_tokens")
    if not context_window or not max_tokens:
        raise RuntimeError(f"OpenRouter returned incomplete token limits for {model!r}")

    modalities = set((remote.get("architecture") or {}).get("input_modalities") or [])
    if "text" not in modalities:
        raise RuntimeError(f"OpenRouter model {model!r} does not accept text input")
    supported = set(remote.get("supported_parameters") or [])
    pricing = remote.get("pricing") or {}
    cost = {
        "input": _per_million(pricing, "prompt"),
        "output": _per_million(pricing, "completion"),
        "cacheRead": _per_million(pricing, "input_cache_read"),
        "cacheWrite": _per_million(pricing, "input_cache_write"),
    }
    tiers = []
    for override in pricing.get("overrides") or []:
        if not override.get("min_prompt_tokens"):
            continue
        merged = pricing | override
        tiers.append({
            "inputTokensAbove": int(override["min_prompt_tokens"]),
            "input": _per_million(merged, "prompt"),
            "output": _per_million(merged, "completion"),
            "cacheRead": _per_million(merged, "input_cache_read"),
            "cacheWrite": _per_million(merged, "input_cache_write"),
        })
    if tiers:
        cost["tiers"] = sorted(tiers, key=lambda tier: tier["inputTokensAbove"])

    resolved = {
        "id": model,
        "name": remote.get("name") or model,
        "reasoning": bool(supported & {"reasoning", "reasoning_effort", "include_reasoning"}),
        "input": [kind for kind in ("text", "image") if kind in modalities],
        "contextWindow": int(context_window),
        "maxTokens": int(max_tokens),
        "cost": cost,
    }
    _REMOTE_MODELS[model] = resolved
    return resolved


def openrouter_models_path() -> Path:
    """Return pi's registry, resolving complete metadata for missing slugs."""
    fragment = HARNESS_DIR / "openrouter_models.json"
    data = json.loads(fragment.read_text(encoding="utf-8"))
    models = data["providers"]["openrouter"]["models"]
    if any(item.get("id") == CONTAINER_AGENT_MODEL for item in models):
        return fragment
    if path := _MODEL_CONFIGS.get(CONTAINER_AGENT_MODEL):
        return path
    resolved = _fetch_openrouter_model(CONTAINER_AGENT_MODEL)
    models.append(resolved)
    global OPENROUTER_RATES
    OPENROUTER_RATES = {key: resolved["cost"][key]
                        for key in ("input", "output", "cacheRead", "cacheWrite")}
    with tempfile.NamedTemporaryFile("w", encoding="utf-8", prefix="beaver-openrouter-",
                                     suffix=".json", delete=False) as f:
        json.dump(data, f)
        path = Path(f.name)
    _MODEL_CONFIGS[CONTAINER_AGENT_MODEL] = path
    atexit.register(path.unlink, missing_ok=True)
    return path


def set_openrouter_model(model: str) -> None:
    """Use one OpenRouter model slug consistently across all experiment arms."""
    model = model.removeprefix("openrouter/").strip()
    if not model:
        raise ValueError("OpenRouter model must not be empty")
    global DEFAULT_MODEL_ID, PI_MODEL_SELECTOR, ZEROSHOT_MODEL_SLUG, CONTAINER_AGENT_MODEL, OPENROUTER_RATES
    DEFAULT_MODEL_ID = ZEROSHOT_MODEL_SLUG = CONTAINER_AGENT_MODEL = model
    PI_MODEL_SELECTOR = f"{DEFAULT_PROVIDER}/{model}"
    OPENROUTER_RATES = _load_openrouter_rates(model)

# ---------------------------------------------------------------------------
# Caps — identical across all cells (plan §Locked decisions #4)
# ---------------------------------------------------------------------------
MYSQL_QUERY_TIMEOUT = 10          # seconds, per agent-side MySQL/SQLite query (exploration)
SCORING_QUERY_TIMEOUT = 60        # seconds, per gold/pred query when scoring BIRD/Spider2
                                  # (their official evaluators use a 60s budget; BEAVER keeps
                                  # the historical 10s MYSQL_QUERY_TIMEOUT)
MAX_TURNS_PILOT = 10
MAX_TURNS_MAIN = 10
TOKEN_GUARD = 320_000             # runaway guard, total tokens/question
PI_WALL_CLOCK = 600               # seconds; exceeding the evaluation budget is incorrect
ZEROSHOT_WALL_CLOCK = 120         # seconds, hard timeout for the zero-shot arm
PROTOCOL_VERSION = 6              # bump when runner semantics change outside prompt/config hashes
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
def profile_path_for(profile_key: str) -> Path:
    """Artifact paths are keyed by the question's profile key: the MySQL schema
    name for BEAVER datasets, `<prefix>_<db_id>` for SQLite benchmarks."""
    return PROFILES_DIR / f"{profile_key}.md"


def schema_links_path_for(profile_key: str) -> Path:
    return SCHEMA_LINKS_DIR / f"{profile_key}.md"


def metadata_path_for(profile_key: str) -> Path:
    return GENERATED_METADATA_DIR / f"{profile_key}.md"


def profile_path(db_label: str) -> Path:
    """Dataset-level profile (single-DB datasets only)."""
    return profile_path_for(mysql_db_for(db_label))


def schema_links_path(db_label: str) -> Path:
    return schema_links_path_for(mysql_db_for(db_label))


def metadata_path(db_label: str) -> Path:
    return metadata_path_for(mysql_db_for(db_label))


def mysql_db_for(db_label: str) -> str:
    """MySQL schema for single-DB datasets; empty string for SQLite benchmarks
    (their per-question `db` field carries the .sqlite file path instead)."""
    return DATASETS[db_label].get("mysql_db", "")


def all_mysql_dbs() -> set[str]:
    """Every MySQL schema across datasets (for the SELECT-only agent grant)."""
    return {spec["mysql_db"] for spec in DATASETS.values() if spec.get("mysql_db")}


def databases_dir_for(db_label: str) -> Path:
    """Host dir holding a SQLite benchmark's .sqlite files (mounted at /dbs)."""
    return REPO_ROOT / dataset_spec(db_label)["databases_dir"]


def sqlite_db_path(db: str) -> Path:
    """Resolve a question's `db` (repo-relative or absolute) to a .sqlite path."""
    path = Path(db)
    return path if path.is_absolute() else REPO_ROOT / path
