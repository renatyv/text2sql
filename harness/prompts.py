"""Prompt construction for the profile × metadata experiment arms.

Engine-aware: BEAVER runs on MySQL, BIRD / Spider 2.0 on their original
SQLite files. Both engine templates carry the same workflow; only dialect
details differ. Cached records are keyed by a prompt hash, so any change
here invalidates prior runs automatically.
"""
from __future__ import annotations

from pathlib import Path

from . import config

# Common text-to-SQL failure modes (grouping, schema linking, predicates, ...).
# Loaded once; spliced into the system prompt ONLY for arms with checklist=True.
# SQLite runs use the .sqlite.txt variant (the base file stays MySQL-specific).
_CHECKLIST_PATH = Path(__file__).resolve().parent / "error_avoidance_checklist.txt"
_ERROR_CHECKLIST = {
    "mysql": _CHECKLIST_PATH.read_text(encoding="utf-8").strip(),
    "sqlite": (_CHECKLIST_PATH.with_suffix(".sqlite.txt")
               .read_text(encoding="utf-8").strip()),
}

# The agentic system prompt with the checklist slot left as a placeholder. The
# slot is filled with the checklist text (checklist=True) or an empty string
# (checklist=False) by _agent_system() below.
_AGENT_SYSTEM_TEMPLATE = r"""\
You are an expert text-to-SQL agent targeting a MySQL database.

Use the `sql_exec` tool when it is available. Independent lookups may be issued
together in one turn.
Other supported agents expose `bash`; for those, run MySQL with:

  mysql --skip-ssl -D "$BEAVER_DB" -e "<SQL>"
The MySQL server is at $MYSQL_HOST:$MYSQL_PORT (user $MYSQL_USER, password in
$MYSQL_PWD). Each query should finish within {timeout}s.

Workflow:
1. Use any supplied database context first to choose tables and columns. It may be
   incomplete or stale, so query the database for anything it does not fully
   answer (missing columns, uncertain values/joins). If context is absent or
   insufficient, inspect only relevant tables. Batch independent DESCRIBE/SHOW
   calls in one turn. Use `SHOW TABLES` only when you cannot identify tables
   otherwise.
2. Reason about joins, filters, and aggregations needed to answer the question.
3. VALIDATION IS MANDATORY and supplied context never replaces it. By turn {validation_turn}, run the complete candidate query with a LIMIT against
   the database — even when the supplied context already describes the schema.
   Before answering, check the returned rows against the question:
    - Projection: the SELECT list returns exactly the columns the question
      asks for — remove any extra id, name, or aggregate columns.
    - Cardinality: DISTINCT only when the question says distinct/unique;
      LIMIT/top-N where a bounded number of rows is requested.
    - Values: rows are non-empty; literal values (strings, dates, IDs) match
      the question or database exactly.
   Then verify the query against the error checklist. If any check changes
   the query. Use turn {repair_turn} only to repair and execute the complete
   corrected query again. Never submit a query you have not executed.
4. Output the last successfully executed complete query inside exactly one answer block.

<ans>
<your final query>
</ans>

Rules:
- Run ONLY read-only statements (SELECT / WITH / SHOW / DESCRIBE / EXPLAIN) —
  never INSERT/UPDATE/DELETE/DROP. The DB is a shared; do not mutate it.
- Return exactly ONE final SELECT/WITH statement that answers the question.
- Do NOT wrap the final query in a transaction or procedure; it must run standalone.
- Do NOT include Markdown fences or commentary inside or after the final </ans>.
- Prefer explicit table-qualified columns. Respect MySQL syntax (backticks for
  reserved/odd-case identifiers).
- Budget: you have at most {max_turns} agent turns. Turn {max_turns} is reserved
  for your FINAL SQL response, so finish all tool use by turn {penultimate_turn}.
  Leave at least 1 (better 2) steps for final corrections before returning final answer.
{checklist_block}\
"""

_AGENT_SYSTEM_TEMPLATE_SQLITE = r"""\
You are an expert text-to-SQL agent targeting a SQLite database.

Use the `sql_exec` tool when it is available. Independent lookups may be issued
together in one turn.
Other supported agents expose `bash`; for those, run SQLite with:

  sqlite3 -readonly -header "$BEAVER_DB_PATH" "<SQL>"
The database is the read-only file at $BEAVER_DB_PATH. Each query should finish
within {timeout}s.

Workflow:
1. Use any supplied database context first to choose tables and columns. It may be
   incomplete or stale, so query the database for anything it does not fully
   answer (missing columns, uncertain values/joins). If context is absent or
   insufficient, inspect only relevant tables. Batch independent lookups in
   one turn. List tables only when you cannot identify them otherwise.
2. Reason about joins, filters, and aggregations needed to answer the question.
3. VALIDATION IS MANDATORY and supplied context never replaces it. By turn {validation_turn}, run the complete candidate query with a LIMIT against
   the database — even when the supplied context already describes the schema.
   Before answering, check the returned rows against the question:
    - Projection: the SELECT list returns exactly the columns the question
      asks for — remove any extra id, name, or aggregate columns.
    - Cardinality: DISTINCT only when the question says distinct/unique;
      LIMIT/top-N where a bounded number of rows is requested.
    - Values: rows are non-empty; literal values (strings, dates, IDs) match
      the question or database exactly.
   Then verify the query against the error checklist. If any check changes
   the query. Use turn {repair_turn} only to repair and execute the complete
   corrected query again. Never submit a query you have not executed.
4. Output the last successfully executed complete query inside exactly one answer block.

<ans>
<your final query>
</ans>

Rules:
- Run ONLY read-only statements (SELECT / WITH / EXPLAIN / PRAGMA table_info) —
never INSERT/UPDATE/DELETE/DROP. The DB file is shared; do not mutate it.
- Return exactly ONE final SELECT/WITH statement that answers the question.
- Do NOT wrap the final query in a transaction or procedure; it must run standalone.
- Do NOT include Markdown fences or commentary inside or after the final </ans>.
- Prefer explicit table-qualified columns. Respect SQLite syntax (double quotes
for reserved/odd-case identifiers — never backticks; date()/strftime()/julianday()
for date math; integer division needs CAST).
- Budget: you have at most {max_turns} agent turns. Turn {max_turns} is reserved
for your FINAL SQL response, so finish all tool use by turn {penultimate_turn}.
Leave at least 1 (better 2) steps for final corrections before returning final answer.
{checklist_block}\
"""

# Trailer appended to the agentic system prompt when checklist=True. Indented to
# sit cleanly under the Rules block above.
_AGENT_CHECKLIST_BLOCK = """
Before finalizing your query, re-check it against this list of common
text-to-SQL errors and avoid them:

"""

_SYSTEM_TEMPLATES = {"mysql": _AGENT_SYSTEM_TEMPLATE, "sqlite": _AGENT_SYSTEM_TEMPLATE_SQLITE}


def _agent_system(timeout: int, max_turns: int, checklist: bool, engine: str = "mysql") -> str:
    """Format the agentic system-prompt APPEND text, optionally with checklist."""
    return _SYSTEM_TEMPLATES[engine].format(
        timeout=timeout,
        max_turns=max_turns,
        penultimate_turn=max(0, max_turns - 1),
        validation_turn=max(1, max_turns - 2),
        repair_turn=max(1, max_turns - 1),
        checklist_block=(_AGENT_CHECKLIST_BLOCK + _ERROR_CHECKLIST[engine] + "\n") if checklist else "",
    )


def _zero_system(checklist: bool, engine: str = "mysql") -> str:
    """Zero-shot system prompt; the checklist is spliced in only when requested."""
    dialect = "MySQL" if engine == "mysql" else "SQLite"
    base = (
        f"You are an expert text-to-SQL engine. Given a database profile and a "
        f"natural-language question, output exactly one {dialect} SELECT/WITH statement "
        f"that answers the question. The statement must run standalone. Do not explain."
    )
    if not checklist:
        return base
    return (
        base
        + "\n\nBefore outputting the query, re-check it against this list of common "
        + "text-to-SQL errors and avoid them:\n\n"
        + _ERROR_CHECKLIST[engine]
    )


def _profile_for(profile_key: str) -> str:
    return config.profile_path_for(profile_key).read_text(encoding="utf-8")


def _schema_links_for(profile_key: str) -> str:
    return config.schema_links_path_for(profile_key).read_text(encoding="utf-8")


def _metadata_for(profile_key: str) -> str:
    return config.metadata_path_for(profile_key).read_text(encoding="utf-8")


def _target_line(engine: str, db: str) -> str:
    if engine == "sqlite":
        return "Target SQLite database: the read-only file at $BEAVER_DB_PATH."
    return f"Target MySQL database: `{db}`."


def _question_block(question: str, evidence: str | None) -> str:
    block = f"Natural-language question:\n\"\"\"\n{question}\n\"\"\""
    if evidence and evidence.strip():
        block += (
            f"\n\nExternal knowledge provided with the question:\n{evidence.strip()}\n"
            "External knowledge is authoritative for derived metrics — reproduce "
            "its formula exactly (operand order, sign, no ABS) as a single column; "
            "never add label or companion columns."
        )
    return block


def agent_prompts(db_label: str, question: str, arm: str, max_turns: int,
                  engine: str = "mysql", db: str | None = None,
                  evidence: str | None = None,
                  profile_key: str | None = None) -> tuple[str, str]:
    """Return (system_prompt, user_prompt) for an agentic arm (tools=True).

    All arms share tooling, checklist, and base instructions. The arm only
    controls whether the frozen profile and/or aggregated metadata are included.
    ``db``/``profile_key`` resolve per question for multi-database benchmarks
    (BIRD / Spider 2.0); the defaults reproduce the single-database BEAVER setup.
    """
    spec = config.arm_spec(arm)
    assert spec["tools"], f"agent_prompts called for non-agentic arm '{arm}'"
    system = _agent_system(
        timeout=config.MYSQL_QUERY_TIMEOUT,
        max_turns=max_turns,
        checklist=spec["checklist"],
        engine=engine,
    )
    db = db or config.mysql_db_for(db_label)
    key = profile_key or db
    context = []
    if spec["profile"]:
        context.append(
            f"===== BEGIN DB PROFILE ({key}) =====\n{_profile_for(key)}\n"
            "===== END DB PROFILE ====="
        )
    if spec.get("links"):
        context.append(
            f"===== BEGIN SCHEMA LINKS ({key}) =====\n{_schema_links_for(key)}\n"
            "===== END SCHEMA LINKS ====="
        )
    if spec["metadata"]:
        context.append(
            f"===== BEGIN AGGREGATED METADATA ({key}) =====\n{_metadata_for(key)}\n"
            "===== END AGGREGATED METADATA ====="
        )
    grounding = "\n\n".join(context) if context else "(none supplied)"
    user = (
        f"{_target_line(engine, db)}\n\n"
        f"===== BEGIN SUPPLIED DATABASE CONTEXT =====\n{grounding}\n"
        f"===== END SUPPLIED DATABASE CONTEXT =====\n\n"
        f"{_question_block(question, evidence)}\n\n"
        f"Return your FINAL SQL inside <ans>...</ans>."
    )
    return system, user


def zeroshot_prompt(db_label: str, question: str, arm: str,
                    engine: str = "mysql", db: str | None = None,
                    evidence: str | None = None,
                    profile_key: str | None = None) -> tuple[str, str]:
    """Return (system_prompt, user_prompt) for a zero-shot arm (tools=False).

    Profile is always injected (the zero-shot arm has no other schema source);
    the checklist is gated by the arm spec, matching the agentic arms.
    """
    spec = config.arm_spec(arm)
    assert not spec["tools"], f"zeroshot_prompt called for agentic arm '{arm}'"
    system = _zero_system(checklist=spec["checklist"], engine=engine)
    db = db or config.mysql_db_for(db_label)
    key = profile_key or db
    prof = _profile_for(key)
    user = (
        f"Database profile ({key}):\n\n"
        f"===== BEGIN DB PROFILE =====\n{prof}\n===== END DB PROFILE =====\n\n"
        f"{_question_block(question, evidence)}\n\n"
        f"Output the single {'MySQL' if engine == 'mysql' else 'SQLite'} query "
        f"that answers it inside <ans>...</ans>."
    )
    return system, user
