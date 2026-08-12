"""Runner for arms A (baseline) and B (profile) — pi headless, sql_exec tool.

Per-question flow (plan §Anti-cheat #1):
  * fresh sandbox cwd, only the prompt (via stdin) and write-only output;
  * built-ins off, web/fetch/search off, only `sql_exec` enabled;
  * env-injected MySQL creds + caps so the agent never sees the repo.
"""
from __future__ import annotations

import json
import os
import subprocess
import time
from pathlib import Path

from . import config, parse_sql, prompts


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
    # sql_exec framing, rules). This keeps arms A/B identical since the append
    # text is the same for both — the only manipulation between them remains the
    # profile, per the plan invariant.
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


def _parse_stream(stdout: str) -> dict:
    turns = 0
    tool_calls = 0
    texts: list[str] = []          # assistant text segments, in order
    executed_sqls: list[str] = []  # sql_exec args, in order
    usage_total = {"input": 0, "output": 0, "cacheRead": 0, "cacheWrite": 0,
                   "reasoning": 0, "totalTokens": 0}
    cost_total = {"input": 0.0, "output": 0.0, "cacheRead": 0.0,
                  "cacheWrite": 0.0, "total": 0.0}
    model = provider = None
    agent_ended = False
    for line in stdout.splitlines():
        line = line.strip()
        if not line or not line.startswith("{"):
            continue
        try:
            e = json.loads(line)
        except json.JSONDecodeError:
            continue
        t = e.get("type")
        if t == "turn_end":
            turns += 1
        if t == "tool_execution_start":
            tool_calls += 1
            sql = (e.get("args") or {}).get("sql")
            if sql:
                executed_sqls.append(sql)
        # Collect per-turn assistant TEXT from turn_end (so the final answer is
        # captured even when agent_end never fires, e.g. on a wall-clock abort).
        if t == "turn_end":
            m = e.get("message") or {}
            if m.get("role") == "assistant":
                provider = provider or m.get("provider")
                model = model or m.get("model")
                txt = "".join(c.get("text", "") for c in m.get("content", [])
                              if c.get("type") == "text")
                if txt.strip():
                    texts.append(txt)
        # Accumulate usage/cost ONCE, from the terminal agent_end event (which
        # carries the full assistant message list). Counting turn_end here too
        # would double-count every token, since agent_end repeats all messages.
        elif t == "agent_end":
            agent_ended = True
            for m in e.get("messages") or []:
                if m.get("role") != "assistant":
                    continue
                provider = provider or m.get("provider")
                model = model or m.get("model")
                # Fall back to per-turn text already collected from turn_end;
                # only append here if turn_end text was missing (e.g. a turn
                # whose turn_end event was dropped from the stream).
                txt = "".join(c.get("text", "") for c in m.get("content", [])
                              if c.get("type") == "text")
                if txt.strip() and txt not in texts:
                    texts.append(txt)
                u = m.get("usage") or {}
                for k in usage_total:
                    usage_total[k] += u.get(k, 0) or 0
                c = (u.get("cost") or {})
                for k in cost_total:
                    cost_total[k] += c.get(k, 0) or 0.0
    # If the run was aborted before agent_end, recover usage/cost from the
    # turn_end messages we already saw (better an estimate than zeros).
    if not agent_ended:
        for line in stdout.splitlines():
            line = line.strip()
            if not line or not line.startswith("{"):
                continue
            try:
                e = json.loads(line)
            except json.JSONDecodeError:
                continue
            if e.get("type") != "turn_end":
                continue
            m = e.get("message") or {}
            if m.get("role") != "assistant":
                continue
            u = m.get("usage") or {}
            for k in usage_total:
                usage_total[k] += u.get(k, 0) or 0
            c = (u.get("cost") or {})
            for k in cost_total:
                cost_total[k] += c.get(k, 0) or 0.0
    final_text = texts[-1] if texts else ""
    return {
        "turns": turns, "db_queries": tool_calls, "raw_text": final_text,
        "all_text": texts, "executed_sqls": executed_sqls,
        "usage": usage_total, "cost": cost_total, "model": model, "provider": provider,
    }


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
