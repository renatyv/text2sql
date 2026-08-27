"""Runner for agentic arms — pi headless with built-ins, subagents, and sql_exec.

Handles every arm with ``tools=True`` in config.ARMS (the profile and checklist
dimensions are resolved inside prompts.agent_prompts, so this runner stays
agnostic to them).

Per-question flow (plan §Anti-cheat #1):
  * fresh sandbox cwd, only the prompt (via stdin) and write-only output;
  * built-ins and the project critic subagent enabled; web/fetch/search off;
  * env-injected MySQL creds + caps so the agent never sees the repo.
"""
from __future__ import annotations

import os
import shutil
import subprocess
import time
from pathlib import Path

from . import config, parse_sql, pi_stream, prompts


def _env(db_label: str, max_turns: int, engine: str = "mysql", db: str | None = None) -> dict:
    env = dict(os.environ)
    env.update({
        "BEAVER_QUERY_TIMEOUT": str(config.MYSQL_QUERY_TIMEOUT),
        "BEAVER_MAX_TURNS": str(max_turns),
    })
    if engine == "sqlite":
        env["BEAVER_DB_PATH"] = str(config.sqlite_db_path(db))
        env["BEAVER_DB"] = Path(db).stem
    else:
        env.update({
            "BEAVER_MYSQL_HOST": config.MYSQL_HOST,
            "BEAVER_MYSQL_PORT": str(config.MYSQL_PORT),
            "BEAVER_MYSQL_USER": config.MYSQL_USER,
            "BEAVER_MYSQL_PWD": config.MYSQL_PWD,
            "BEAVER_DB": db or config.mysql_db_for(db_label),
        })
    return env


def _argv(append_prompt: str) -> list[str]:
    # Anti-cheat (plan §#1–2): isolated cwd, no web/fetch/search, no
    # global skills/context/themes that could leak gold, --offline so pi makes no
    # startup network calls beyond the LLM endpoint.
    #
    # System prompt: pi's default coding-assistant prompt is used as the base
    # (better-tuned for agentic tool use than a hand-rolled one); we only
    # --append-system-prompt the experiment-specific contract (output format,
    # sql_exec framing, rules). The append text is identical across agentic arms
    # except for the optional checklist section — the profile manipulation lives
    # in the user turn, not here, per the plan invariant.
    # Pin reasoning effort so every experiment arm uses the same setting.
    return [
        config.PI_BIN, "-p",
        "--mode", "json",
        "--no-session",
        "--offline",
        "--no-extensions",
        "--no-skills",
        "--no-context-files",
        "--no-themes",
        "-e", str(config.PI_EXTENSION),
        "-e", str(Path(shutil.which(config.PI_BIN) or config.PI_BIN).resolve().parent.parent
                    / "examples/extensions/subagent/index.ts"),
        "--tools", ("read,bash,edit,write,grep,find,ls,sql_exec,subagent"
                    if config.CRITIC_ENABLED
                    else "read,bash,edit,write,grep,find,ls,sql_exec"),
        "--thinking", config.PI_THINKING,
        "--append-system-prompt", append_prompt,
        "--provider", config.DEFAULT_PROVIDER,
        "--model", config.DEFAULT_MODEL_ID,
    ]


# The JSON-stream parser is shared with the container runner (see
# pi_stream.py). Kept as a local alias so this module's call sites are unchanged.
_parse_stream = pi_stream.parse_stream


def run(db_label: str, question: str, arm: str, max_turns: int,
        sandbox: Path, engine: str = "mysql", db: str | None = None,
        evidence: str | None = None, profile_key: str | None = None) -> dict:
    system_prompt, user_prompt = prompts.agent_prompts(
        db_label, question, arm, max_turns, engine=engine, db=db,
        evidence=evidence, profile_key=profile_key,
    )
    sandbox.mkdir(parents=True, exist_ok=True)
    if config.arm_spec(arm)["profile"]:
        key = profile_key or db or config.mysql_db_for(db_label)
        shutil.copyfile(config.profile_path_for(key), sandbox / "profile.md")
        shutil.copyfile(config.profile_toc_path_for(key), sandbox / "profile.toc.md")
        shutil.copyfile(config.schema_links_path_for(key), sandbox / "schema-links.md")
    agents_dir = sandbox / ".pi" / "agents"
    agents_dir.mkdir(parents=True, exist_ok=True)
    if config.CRITIC_ENABLED:
        critic = (config.HARNESS_DIR / "pi_agents" / "critic.md").read_text(encoding="utf-8")
        (agents_dir / "critic.md").write_text(
            critic.replace("__CRITIC_MODEL__", f"{config.DEFAULT_PROVIDER}/{config.DEFAULT_MODEL_ID}"),
            encoding="utf-8",
        )
    started = time.time()
    rec: dict = {
        "arm": arm, "runner": "pi", "db_label": db_label,
        "max_turns": max_turns, "sandbox": str(sandbox),
    }
    try:
        proc = subprocess.run(
            _argv(system_prompt),  # now an APPEND prompt, not a replacement
            input=user_prompt,
            env=_env(db_label, max_turns, engine, db),
            cwd=str(sandbox),
            capture_output=True,
            text=True,
            timeout=config.PI_WALL_CLOCK,
        )
        rec["returncode"] = proc.returncode
        rec["stderr_tail"] = (proc.stderr or "")[-1000:]
        parsed = _parse_stream(proc.stdout or "")
    except subprocess.TimeoutExpired as e:
        rec["error"] = f"pi wall-clock timeout ({config.PI_WALL_CLOCK}s)"
        rec["budget_exhausted"] = "wall_clock"
        output = e.stdout or ""
        rec["stdout"] = output.decode("utf-8", "replace") if isinstance(output, bytes) else output
        parsed = _parse_stream(rec.get("stdout", ""))
    except FileNotFoundError:
        rec["error"] = "`pi` not found on PATH — install pi or set PI_BIN."
        rec["infrastructure_error"] = True
        return rec

    if pi_stream.is_turn_limit_abort(parsed.get("api_error"), parsed.get("turns", 0), max_turns):
        parsed["api_error"] = None
        parsed["turns"] = max_turns
    rec.update(parsed)
    candidate = None
    if not rec.get("budget_exhausted") and not parsed.get("api_error"):
        for txt in reversed(parsed.get("all_text") or []):
            candidate = parse_sql.extract_sql(txt)
            if candidate:
                break
    if parsed.get("api_error"):
        rec["error"] = f"model API error: {parsed['api_error']}"
        rec["infrastructure_error"] = True
        rec["retryable_error"] = pi_stream.retryable_api_error(parsed["api_error"])
    if parsed.get("turns", 0) >= max_turns and not candidate and not rec.get("api_error"):
        rec["error"] = rec.get("error") or f"no final SQL within {max_turns}-turn budget"
        rec["budget_exhausted"] = "turns"
    rec["latency_s"] = round(time.time() - started, 2)
    rec["pred_sql"] = candidate
    # token runaway guard (plan §Locked decisions #4)
    if parsed["usage"]["totalTokens"] > config.TOKEN_GUARD:
        rec["token_guard_hit"] = True
    return rec
