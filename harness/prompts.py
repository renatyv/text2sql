"""Prompt construction for arms A / B / C.

Design (mirrors AGENT_PROFILE_EXPERIMENT_PLAN.md):
  * Arms A and B share the SAME system prompt; only the user turn differs
    (B prepends the frozen <db>.md profile). This keeps the only manipulation
    the profile itself.
  * Arm C is a clean zero-shot text-to-SQL call with the profile baked in and
    no tooling — a single LLM response is expected.
"""
from __future__ import annotations

from . import config

_AGENT_SYSTEM = r"""\
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
"""

_ZERO_SYSTEM = """\
You are an expert text-to-SQL engine. Given a database profile and a
natural-language question, output exactly one MySQL SELECT/WITH statement that
answers the question. The statement must run standalone. Do not explain.
"""


def _profile(db_label: str) -> str:
    path = config.profile_path(db_label)
    return path.read_text(encoding="utf-8")


def agent_prompts(db_label: str, question: str, arm: str, max_turns: int) -> tuple[str, str]:
    """Return (system_prompt, user_prompt) for arms A and B."""
    assert arm in ("A", "B")
    system = _AGENT_SYSTEM.format(
        row_cap=config.EXPLORE_ROW_CAP,
        timeout=config.MYSQL_QUERY_TIMEOUT,
        max_turns=max_turns,
    )
    db = config.mysql_db_for(db_label)
    if arm == "A":
        user = (
            f"Target MySQL database: `{db}` (explore it with sql_exec).\n\n"
            f"Natural-language question:\n\"\"\"\n{question}\n\"\"\"\n\n"
            f"Explore the schema as needed, then return your FINAL SQL in a ```sql block."
        )
    else:  # B — inject the frozen profile into the initial prompt
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


def zeroshot_prompt(db_label: str, question: str) -> tuple[str, str]:
    """Return (system_prompt, user_prompt) for arm C (no tools)."""
    prof = _profile(db_label)
    user = (
        f"Database profile ({db_label}):\n\n"
        f"===== BEGIN DB PROFILE =====\n{prof}\n===== END DB PROFILE =====\n\n"
        f"Natural-language question:\n\"\"\"\n{question}\n\"\"\"\n\n"
        f"Output the single MySQL query that answers it inside one ```sql block."
    )
    return _ZERO_SYSTEM, user
