"""Prompt construction for the experiment arms.

Arms are dimension-driven (see config.ARMS): each arm fixes three booleans —
``tools`` (pi agent with sql_exec vs. a single zero-shot LLM call), ``profile``
(inject the frozen <db>.md), and ``checklist`` (inject the error-avoidance
checklist). This module builds the system + user prompts from those flags:

  * Agentic arms (tools=True) share ONE system-prompt APPEND text (passed to pi
    via --append-system-prompt, on top of pi's default coding-assistant prompt);
    the user turn optionally prepends the profile. So two agentic arms differ
    only in {profile, checklist}, never in tooling or base instructions.
  * The zero-shot arm (tools=False) uses a separate single-call system prompt
    with the profile baked into the user turn and no tooling.

The checklist is an EXPLICIT manipulation: arms with checklist=False get no
checklist text at all, so its marginal effect is isolatable by differencing
two arms that differ only in that flag.
"""
from __future__ import annotations

from pathlib import Path

from . import config

# Common text-to-SQL failure modes (grouping, schema linking, predicates, ...).
# Loaded once; spliced into the system prompt ONLY for arms with checklist=True.
_CHECKLIST_PATH = Path(__file__).resolve().parent / "error_avoidance_checklist.txt"
_ERROR_CHECKLIST = _CHECKLIST_PATH.read_text(encoding="utf-8").strip()

# The agentic system prompt with the checklist slot left as a placeholder. The
# slot is filled with the checklist text (checklist=True) or an empty string
# (checklist=False) by _agent_system() below.
_AGENT_SYSTEM_TEMPLATE = r"""\
You are an expert text-to-SQL agent targeting a MySQL database.

You have ONE tool: `sql_exec`, which runs a READ-ONLY SQL statement
(SELECT / WITH / SHOW / DESCRIBE / EXPLAIN) against the target database and
returns up to {row_cap} rows. Write statements are rejected; each call has a
{timeout}s timeout.

Workflow:
1. Explore the schema: `SHOW TABLES;`, then `SHOW CREATE TABLE `<t>`;` or
   `DESCRIBE <t>;` for relevant tables. Use `SELECT ... LIMIT 5;` to sample data
   and confirm column meaning, formats, and join keys.
2. Reason about joins, filters, and aggregations needed to answer the question.
3. Iterate using sql_exec to validate intermediate results.
4. When confident, output your FINAL query inside a single fenced block:

```sql
<your final query>
```

Rules:
- Return exactly ONE final SELECT/WITH statement that answers the question.
- Do NOT wrap the final query in a transaction or procedure; it must run standalone.
- Do NOT include any commentary after the final ```sql block.
- Prefer explicit table-qualified columns. Respect MySQL syntax (backticks for
  reserved/odd-case identifiers).
- Budget: you have at most {max_turns} agent turns — explore efficiently.
{checklist_block}\
"""

# Trailer appended to the agentic system prompt when checklist=True. Indented to
# sit cleanly under the Rules block above.
_AGENT_CHECKLIST_BLOCK = """
Before finalizing your query, re-check it against this list of common
text-to-SQL errors and avoid them:

""" + _ERROR_CHECKLIST + "\n"


def _agent_system(row_cap: int, timeout: int, max_turns: int, checklist: bool) -> str:
    """Format the agentic system-prompt APPEND text, optionally with checklist."""
    return _AGENT_SYSTEM_TEMPLATE.format(
        row_cap=row_cap,
        timeout=timeout,
        max_turns=max_turns,
        checklist_block=_AGENT_CHECKLIST_BLOCK if checklist else "",
    )


def _zero_system(checklist: bool) -> str:
    """Zero-shot system prompt; the checklist is spliced in only when requested."""
    base = (
        "You are an expert text-to-SQL engine. Given a database profile and a "
        "natural-language question, output exactly one MySQL SELECT/WITH statement "
        "that answers the question. The statement must run standalone. Do not explain."
    )
    if not checklist:
        return base
    return (
        base
        + "\n\nBefore outputting the query, re-check it against this list of common "
        "text-to-SQL errors and avoid them:\n\n"
        + _ERROR_CHECKLIST
    )


def _profile(db_label: str) -> str:
    path = config.profile_path(db_label)
    return path.read_text(encoding="utf-8")


def agent_prompts(db_label: str, question: str, arm: str, max_turns: int) -> tuple[str, str]:
    """Return (system_prompt, user_prompt) for an agentic arm (tools=True).

    The arm's spec drives two dimensions: ``profile`` (prepend the frozen
    <db>.md to the user turn) and ``checklist`` (append the error-avoidance
    checklist to the system prompt). Tooling and base instructions are identical
    across all agentic arms, so any two differ only in those two flags.
    """
    spec = config.arm_spec(arm)
    assert spec["tools"], f"agent_prompts called for non-agentic arm '{arm}'"
    system = _agent_system(
        row_cap=config.EXPLORE_ROW_CAP,
        timeout=config.MYSQL_QUERY_TIMEOUT,
        max_turns=max_turns,
        checklist=spec["checklist"],
    )
    db = config.mysql_db_for(db_label)
    if not spec["profile"]:
        user = (
            f"Target MySQL database: `{db}` (explore it with sql_exec).\n\n"
            f"Natural-language question:\n\"\"\"\n{question}\n\"\"\"\n\n"
            f"Explore the schema as needed, then return your FINAL SQL in a ```sql block."
        )
    else:  # inject the frozen profile into the initial prompt
        prof = _profile(db_label)
        user = (
            f"Target MySQL database: `{db}`.\n\n"
            f"A pre-generated profile of this database follows. Use it to ground your "
            f"schema understanding; you may still verify with sql_exec.\n\n"
            f"===== BEGIN DB PROFILE ({db_label}) =====\n{prof}\n===== END DB PROFILE =====\n\n"
            f"Natural-language question:\n\"\"\"\n{question}\n\"\"\"\n\n"
            f"Return your FINAL SQL in a ```sql block."
        )
    return system, user


def zeroshot_prompt(db_label: str, question: str, arm: str) -> tuple[str, str]:
    """Return (system_prompt, user_prompt) for a zero-shot arm (tools=False).

    Profile is always injected (the zero-shot arm has no other schema source);
    the checklist is gated by the arm spec, matching the agentic arms.
    """
    spec = config.arm_spec(arm)
    assert not spec["tools"], f"zeroshot_prompt called for agentic arm '{arm}'"
    system = _zero_system(checklist=spec["checklist"])
    prof = _profile(db_label)
    user = (
        f"Database profile ({db_label}):\n\n"
        f"===== BEGIN DB PROFILE =====\n{prof}\n===== END DB PROFILE =====\n\n"
        f"Natural-language question:\n\"\"\"\n{question}\n\"\"\"\n\n"
        f"Output the single MySQL query that answers it inside one ```sql block."
    )
    return system, user
