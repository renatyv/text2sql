"""Runner for agentic arms — pi headless, sql_exec tool.

Handles every arm with ``tools=True`` in config.ARMS (the profile and checklist
dimensions are resolved inside prompts.agent_prompts, so this runner stays
agnostic to them).

Per-question flow (plan §Anti-cheat #1):
  * fresh sandbox cwd, only the prompt (via stdin) and write-only output;
  * built-ins off, web/fetch/search off, only `sql_exec` enabled;
  * env-injected MySQL creds + caps so the agent never sees the repo.
"""
from __future__ import annotations

import os
import subprocess
import time
from pathlib import Path

from . import config, parse_sql, pi_stream, prompts


def _env(db_label: str, max_turns: int) -> dict:
    env = dict(os.environ)
    env.update({
        "BEAVER_MYSQL_HOST": config.MYSQL_HOST,
        "BEAVER_MYSQL_PORT": str(config.MYSQL_PORT),
        "BEAVER_MYSQL_USER": config.MYSQL_USER,
        "BEAVER_MYSQL_PWD": config.MYSQL_PWD,
        "BEAVER_DB": config.mysql_db_for(db_label),
        "BEAVER_QUERY_TIMEOUT": str(config.MYSQL_QUERY_TIMEOUT),
        "BEAVER_MAX_TURNS": str(max_turns),
        "BEAVER_EXPLORE_ROW_CAP": str(config.EXPLORE_ROW_CAP),
    })
    return env


def _argv(append_prompt: str) -> list[str]:
    # Anti-cheat (plan §#1–2): isolated cwd, no built-ins/web/fetch/search, no
    # global skills/context/themes that could leak gold, --offline so pi makes no
    # startup network calls beyond the LLM endpoint.
    #
    # System prompt: pi's default coding-assistant prompt is used as the base
    # (better-tuned for agentic tool use than a hand-rolled one); we only
    # --append-system-prompt the experiment-specific contract (output format,
    # sql_exec framing, rules). The append text is identical across agentic arms
    # except for the optional checklist section — the profile manipulation lives
    # in the user turn, not here, per the plan invariant.
    # Reasoning effort: DeepSeek defaults to pi's built-in thinking level; we
    # pin --thinking low (config.PI_THINKING) for cost/latency control.
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
        "--no-builtin-tools",
        "--tools", "sql_exec",
        "--thinking", config.PI_THINKING,
        "--append-system-prompt", append_prompt,
        "--provider", config.DEFAULT_PROVIDER,
        "--model", config.DEFAULT_MODEL_ID,
    ]


# The JSON-stream parser is shared with the container runner (see
# pi_stream.py). Kept as a local alias so this module's call sites are unchanged.
_parse_stream = pi_stream.parse_stream


def run(db_label: str, question: str, arm: str, max_turns: int,
        sandbox: Path) -> dict:
    system_prompt, user_prompt = prompts.agent_prompts(db_label, question, arm, max_turns)
    sandbox.mkdir(parents=True, exist_ok=True)
    started = time.time()
    rec: dict = {
        "arm": arm, "runner": "pi", "db_label": db_label,
        "max_turns": max_turns, "sandbox": str(sandbox),
    }
    try:
        proc = subprocess.run(
            _argv(system_prompt),  # now an APPEND prompt, not a replacement
            input=user_prompt,
            env=_env(db_label, max_turns),
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
        rec["stdout"] = (e.stdout or "") if isinstance(e.stdout, str) else ""
        parsed = _parse_stream(rec.get("stdout", ""))
    except FileNotFoundError:
        rec["error"] = "`pi` not found on PATH — install pi or set PI_BIN."
        return rec

    rec.update(parsed)
    rec["latency_s"] = round(time.time() - started, 2)
    # pick the best SQL candidate: prefer the last fenced block in any assistant
    # text; fall back to the last SELECT the agent actually executed.
    candidate = None
    for txt in reversed(parsed.get("all_text") or []):
        candidate = parse_sql.extract_sql(txt)
        if candidate:
            break
    if not candidate:
        candidate = parse_sql.last_select(parsed.get("executed_sqls") or [])
    rec["pred_sql"] = candidate
    # token runaway guard (plan §Locked decisions #4)
    if parsed["usage"]["totalTokens"] > config.TOKEN_GUARD:
        rec["token_guard_hit"] = True
    return rec
