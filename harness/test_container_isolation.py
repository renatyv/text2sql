"""Small regression checks for container-run isolation bookkeeping."""
from __future__ import annotations

import subprocess
import sys
import unittest
from pathlib import Path
from unittest.mock import patch

from harness import parse_sql, pi_stream, runner_container


class ContainerIsolationTests(unittest.TestCase):
    def test_all_agent_choices_have_noninteractive_argv(self) -> None:
        for agent in ("pi", "claude", "opencode", "codex"):
            argv = runner_container._agent_argv(agent, "system", "user", 3)
            self.assertTrue(argv)
        self.assertIn("--max-turns", runner_container._agent_argv("claude", "s", "u", 3))
        self.assertEqual(runner_container._agent_argv("codex", "s", "u", 3)[0], "exec")

    def test_mysql_bash_is_counted_and_recoverable(self) -> None:
        events = ('{"type":"tool_execution_start","toolName":"bash",'
                  '"args":{"command":"mysql -D neutron -e \'SELECT 1\'"}}\n')
        parsed = pi_stream.parse_stream(events)
        self.assertEqual(parsed["db_queries"], 1)
        self.assertEqual(parsed["executed_sqls"], ["SELECT 1"])

    def test_unclosed_sql_fence_is_recoverable(self) -> None:
        self.assertEqual(parse_sql.extract_sql("```sql\nSELECT 1;"), "SELECT 1;")
        self.assertEqual(parse_sql.extract_sql("<ans>SELECT 2</ans>"), "SELECT 2;")
        self.assertEqual(parse_sql.extract_sql("<ans>WITH q AS (SELECT 3) SELECT * FROM q"),
                         "WITH q AS (SELECT 3) SELECT * FROM q;")

    def test_non_pi_telemetry_is_not_reported_as_zero(self) -> None:
        parsed = runner_container._parse_agent_output("codex", "```sql\nSELECT 1\n```")
        self.assertFalse(parsed["metrics_available"])
        self.assertEqual(parsed["turns"], 0)

    @patch("harness.runner_container.network.is_ready", return_value=True)
    @patch("harness.runner_container.prompts.agent_prompts", return_value=("system", "user"))
    @patch("harness.runner_container.subprocess.run")
    def test_timeout_force_removes_the_named_container(self, run, _prompts, _ready) -> None:
        run.side_effect = [
            subprocess.TimeoutExpired(["docker", "run"], 1, output=""),
            subprocess.CompletedProcess(["docker", "rm"], 0),
        ]
        with patch("harness.runner_container.uuid.uuid4", return_value=type("U", (), {"hex": "test"})()):
            rec = runner_container.run("neutron", "question", "raw", 1, Path("/tmp/x"))
        self.assertIn("wall-clock timeout", rec["error"])
        self.assertEqual(rec["budget_exhausted"], "wall_clock")
        self.assertNotIn("infrastructure_error", rec)
        self.assertIn("-i", run.call_args_list[0].args[0])
        self.assertEqual(run.call_args_list[1].args[0][:3], ["docker", "rm", "-f"])
        self.assertTrue(any("mysql_timeout.sh:/usr/local/bin/mysql:ro" in str(arg)
                            for arg in run.call_args_list[0].args[0]))

    def test_terminal_api_error_is_visible_despite_zero_exit(self) -> None:
        events = ('{"type":"auto_retry_start"}\n'
                  '{"type":"turn_end","message":{"role":"assistant",'
                  '"stopReason":"error","errorMessage":"429 rate limited","content":[]}}\n')
        parsed = pi_stream.parse_stream(events)
        self.assertEqual(parsed["retry_count"], 1)
        self.assertEqual(parsed["api_error"], "429 rate limited")
        self.assertTrue(pi_stream.retryable_api_error(parsed["api_error"]))
        self.assertTrue(pi_stream.retryable_api_error(
            "Upstream error: generation ended before the streamed tool call was complete"
        ))
        self.assertFalse(pi_stream.retryable_api_error("HTTP 401 invalid API key"))

    @patch("harness.runner_container.network.is_ready", return_value=True)
    @patch("harness.runner_container.prompts.agent_prompts", return_value=("system", "user"))
    @patch("harness.runner_container.subprocess.run")
    def test_turn_guard_abort_is_budget_exhaustion(self, run, _prompts, _ready) -> None:
        tool_turn = ('{"type":"turn_end","message":{"role":"assistant",'
                     '"stopReason":"toolUse","content":[]}}\n')
        error_turn = ('{"type":"turn_end","message":{"role":"assistant",'
                      '"stopReason":"error","errorMessage":"This operation was aborted",'
                      '"content":[]}}\n')
        run.return_value = subprocess.CompletedProcess(
            ["docker", "run"], 0, tool_turn * 6 + error_turn, ""
        )
        rec = runner_container.run("neutron", "question", "raw", 6, Path("/tmp/x"))
        self.assertEqual(rec["budget_exhausted"], "turns")
        self.assertEqual(rec["turns"], 6)
        self.assertEqual(rec["error"], "no final SQL within 6-turn budget")
        self.assertNotIn("infrastructure_error", rec)
        self.assertIsNone(rec["api_error"])

    def test_streamed_runner_reports_turns(self) -> None:
        events = [
            '{"type":"tool_execution_start","toolName":"bash",'
            '"args":{"command":"mysql -e SELECT"}}',
            '{"type":"turn_end","message":{"role":"assistant"}}',
        ]
        script = "import sys; sys.stdin.read(); " + "; ".join(
            f"print({event!r})" for event in events
        )
        statuses = []
        completed = runner_container._run_pi_streamed(
            [sys.executable, "-c", script], "prompt", lambda turn, dbq: statuses.append((turn, dbq))
        )
        self.assertEqual(completed.returncode, 0)
        self.assertEqual(statuses, [(1, 1)])


if __name__ == "__main__":
    unittest.main()
