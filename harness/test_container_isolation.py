"""Small regression checks for container-run isolation bookkeeping."""
from __future__ import annotations

import subprocess
import unittest
from pathlib import Path
from unittest.mock import patch

from harness import pi_stream, runner_container


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
        self.assertTrue(rec["infrastructure_error"])
        self.assertEqual(run.call_args_list[1].args[0][:3], ["docker", "rm", "-f"])

    def test_terminal_api_error_is_visible_despite_zero_exit(self) -> None:
        events = ('{"type":"auto_retry_start"}\n'
                  '{"type":"turn_end","message":{"role":"assistant",'
                  '"stopReason":"error","errorMessage":"429 rate limited","content":[]}}\n')
        parsed = pi_stream.parse_stream(events)
        self.assertEqual(parsed["retry_count"], 1)
        self.assertEqual(parsed["api_error"], "429 rate limited")


if __name__ == "__main__":
    unittest.main()
