"""Prompt construction for the profile × metadata experiment arms."""
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

Use the read-only `sql_exec` tool when it is available. It accepts one SQL
statement per call, and independent lookups may be issued together in one turn.
Other supported agents expose `bash`; for those, run MySQL with:

  mysql --skip-ssl -D "$BEAVER_DB" -e "<SQL>"
The MySQL server is at $MYSQL_HOST:$MYSQL_PORT (user $MYSQL_USER, password in
$MYSQL_PWD). Keep exploratory output small: LIMIT to ~{row_cap} rows. Each
query should finish within {timeout}s.

Workflow:
1. Use any supplied database context first. Query the database only to resolve
   missing schema details or validate candidate SQL; do not repeat lookups that
   the context already answers. If context is absent or insufficient, inspect
   only relevant tables. Batch independent DESCRIBE/SHOW calls in one turn. Use
   `SHOW TABLES` only when you cannot identify tables otherwise, and use
   `SELECT ... LIMIT 5` only to confirm a needed value or join.
2. Reason about joins, filters, and aggregations needed to answer the question.
3. By turn {validation_turn}, run the complete candidate query, not merely pieces
   of it. Use turn {repair_turn} only to repair and re-run that complete query.
4. Output the last successfully executed complete query inside exactly one answer block.

<ans>
<your final query>
</ans>

Rules:
- Run ONLY read-only statements (SELECT / WITH / SHOW / DESCRIBE / EXPLAIN) —
  never INSERT/UPDATE/DELETE/DROP. The DB is a shared benchmark; do not mutate it.
- Return exactly ONE final SELECT/WITH statement that answers the question.
- Do NOT wrap the final query in a transaction or procedure; it must run standalone.
- Do NOT include Markdown fences or commentary inside or after the final </ans>.
- Prefer explicit table-qualified columns. Respect MySQL syntax (backticks for
  reserved/odd-case identifiers).
- Budget: you have at most {max_turns} agent turns. Turn {max_turns} is reserved
  for your FINAL SQL response, so finish all tool use by turn {penultimate_turn}.
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
        penultimate_turn=max(0, max_turns - 1),
        validation_turn=max(1, max_turns - 2),
        repair_turn=max(1, max_turns - 1),
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


def _metadata(db_label: str) -> str:
    return config.metadata_path(db_label).read_text(encoding="utf-8")


def agent_prompts(db_label: str, question: str, arm: str, max_turns: int) -> tuple[str, str]:
    """Return (system_prompt, user_prompt) for an agentic arm (tools=True).

    All arms share tooling, checklist, and base instructions. The arm only
    controls whether the frozen profile and/or aggregated metadata are included.
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
    context = []
    if spec["profile"]:
        context.append(
            f"===== BEGIN DB PROFILE ({db_label}) =====\n{_profile(db_label)}\n"
            "===== END DB PROFILE ====="
        )
    if spec["metadata"]:
        context.append(
            f"===== BEGIN AGGREGATED METADATA ({db_label}) =====\n{_metadata(db_label)}\n"
            "===== END AGGREGATED METADATA ====="
        )
    grounding = "\n\n".join(context) if context else "(none supplied)"
    user = (
        f"Target MySQL database: `{db}`.\n\n"
        f"===== BEGIN SUPPLIED DATABASE CONTEXT =====\n{grounding}\n"
        f"===== END SUPPLIED DATABASE CONTEXT =====\n\n"
        f"Natural-language question:\n\"\"\"\n{question}\n\"\"\"\n\n"
        f"Return your FINAL SQL inside <ans>...</ans>."
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
        f"Output the single MySQL query that answers it inside <ans>...</ans>."
    )
    return system, user
