"""Runner for zero-shot arms — single LLM call, NO tools / NO agent loop.

Primary path: a direct OpenRouter chat-completions request (isolates the
profile's standalone value). When OPENROUTER_API_KEY is absent, falls back to a
single `pi -p --no-tools` call so the pipeline still runs end-to-end (e.g. for a
smoke test against another configured provider).
"""
from __future__ import annotations

import json
import os
import subprocess
import time
import urllib.error
import urllib.request
from pathlib import Path

from . import config, parse_sql, prompts


def _has_openrouter_key() -> bool:
    return bool(os.environ.get("OPENROUTER_API_KEY"))


def _cost_from_tokens(usage: dict) -> dict:
    """Price an OpenRouter response from its token usage.

    OpenRouter's `/usage` object carries no cost, so derive it here from the
    model's $/Mtok rates (config.OPENROUTER_RATES). The returned dict matches the
    shape pi reports for the agentic arms — dollars, keys {input, output,
    cacheRead, cacheWrite, total} — so metrics.aggregate / project_cost treat all
    arms alike.
    """
    r = config.OPENROUTER_RATES
    inp = usage.get("input", 0) * r["input"] / 1_000_000
    out = usage.get("output", 0) * r["output"] / 1_000_000
    cache_read = usage.get("cacheRead", 0) * r["cacheRead"] / 1_000_000
    cache_write = usage.get("cacheWrite", 0) * r["cacheWrite"] / 1_000_000
    return {
        "input": inp, "output": out,
        "cacheRead": cache_read, "cacheWrite": cache_write,
        "total": inp + out + cache_read + cache_write,
    }


def _direct_openrouter(db_label: str, question: str, arm: str) -> dict:
    system, user = prompts.zeroshot_prompt(db_label, question, arm)
    body = {
        "model": config.ZEROSHOT_MODEL_SLUG,
        "messages": [
            {"role": "system", "content": system},
            {"role": "user", "content": user},
        ],
        "reasoning": {"effort": "none" if config.PI_THINKING == "off" else config.PI_THINKING},
    }
    req = urllib.request.Request(
        f"{config.OPENROUTER_BASE_URL}/chat/completions",
        data=json.dumps(body).encode("utf-8"),
        headers={
            "Authorization": f"Bearer {os.environ['OPENROUTER_API_KEY']}",
            "Content-Type": "application/json",
        },
        method="POST",
    )
    started = time.time()
    rec: dict = {"arm": arm, "runner": "openrouter-direct", "db_label": db_label}
    try:
        with urllib.request.urlopen(req, timeout=config.ZEROSHOT_WALL_CLOCK) as resp:
            data = json.loads(resp.read().decode("utf-8"))
    except urllib.error.HTTPError as e:
        rec["error"] = f"OpenRouter HTTP {e.code}: {e.read().decode('utf-8', 'replace')[:500]}"
        rec["latency_s"] = round(time.time() - started, 2)
        return rec
    except Exception as e:
        rec["error"] = f"{type(e).__name__}: {e}"
        rec["latency_s"] = round(time.time() - started, 2)
        return rec

    msg = (data.get("choices") or [{}])[0].get("message", {}).get("content", "") or ""
    usage = data.get("usage") or {}
    rec["raw_text"] = msg
    rec["pred_sql"] = parse_sql.extract_sql(msg)
    rec["turns"] = 1
    rec["db_queries"] = 0
    rec["usage"] = {
        "input": usage.get("prompt_tokens", 0),
        "output": usage.get("completion_tokens", 0),
        "cacheRead": 0, "cacheWrite": 0, "reasoning": 0,
        "totalTokens": usage.get("total_tokens", 0),
    }
    rec["cost"] = _cost_from_tokens(rec["usage"])
    rec["latency_s"] = round(time.time() - started, 2)
    rec["model"] = data.get("model", config.ZEROSHOT_MODEL_SLUG)
    return rec


def _pi_fallback(db_label: str, question: str, arm: str, sandbox: Path) -> dict:
    """Single pi call, no tools, no agent loop, clean zero-shot system prompt."""
    system, user = prompts.zeroshot_prompt(db_label, question, arm)
    sandbox.mkdir(parents=True, exist_ok=True)
    argv = [
        config.PI_BIN, "-p",
        "--mode", "json",
        "--no-session",
        "--offline",
        "--no-extensions",
        "--no-skills",
        "--no-context-files",
        "--no-themes",
        "--no-tools",
        "--thinking", config.PI_THINKING,
        "--system-prompt", system,
        "--provider", config.DEFAULT_PROVIDER,
        "--model", config.DEFAULT_MODEL_ID,
    ]
    started = time.time()
    rec: dict = {"arm": arm, "runner": "pi-fallback", "db_label": db_label}
    try:
        proc = subprocess.run(
            argv, input=user, env=os.environ.copy(), cwd=str(sandbox),
            capture_output=True, text=True, timeout=config.ZEROSHOT_WALL_CLOCK,
        )
        rec["returncode"] = proc.returncode
        rec["stderr_tail"] = (proc.stderr or "")[-1000:]
        parsed = _parse_pi(proc.stdout or "")
    except subprocess.TimeoutExpired as e:
        rec["error"] = f"pi wall-clock timeout ({config.ZEROSHOT_WALL_CLOCK}s)"
        parsed = _parse_pi((e.stdout or "") if isinstance(e.stdout, str) else "")
    except FileNotFoundError:
        rec["error"] = "`pi` not found on PATH."
        return rec
    rec.update(parsed)
    rec["pred_sql"] = parse_sql.extract_sql(parsed.get("raw_text", ""))
    rec["latency_s"] = round(time.time() - started, 2)
    return rec


def _parse_pi(stdout: str) -> dict:
    final_text = ""
    usage = {"input": 0, "output": 0, "cacheRead": 0, "cacheWrite": 0,
             "reasoning": 0, "totalTokens": 0}
    cost = {"input": 0.0, "output": 0.0, "cacheRead": 0.0, "cacheWrite": 0.0, "total": 0.0}
    model = None
    for line in stdout.splitlines():
        line = line.strip()
        if not line.startswith("{"):
            continue
        try:
            e = json.loads(line)
        except json.JSONDecodeError:
            continue
        if e.get("type") == "agent_end":
            for m in e.get("messages", []):
                if m.get("role") == "assistant":
                    model = model or m.get("model")
                    final_text = "".join(c.get("text", "") for c in m.get("content", [])
                                         if c.get("type") == "text") or final_text
                    u = m.get("usage") or {}
                    for k in usage:
                        usage[k] += u.get(k, 0) or 0
                    c = u.get("cost") or {}
                    for k in cost:
                        cost[k] += c.get(k, 0) or 0.0
    return {"raw_text": final_text, "usage": usage, "cost": cost,
            "turns": 1, "db_queries": 0, "model": model}


def run(db_label: str, question: str, arm: str, sandbox: Path) -> dict:
    if _has_openrouter_key():
        return _direct_openrouter(db_label, question, arm)
    return _pi_fallback(db_label, question, arm, sandbox)
