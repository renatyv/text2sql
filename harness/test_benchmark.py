from __future__ import annotations

import unittest
from pathlib import Path
from tempfile import TemporaryDirectory
from unittest.mock import patch

import run_experiment
from harness import manifest, metrics, prompts, scorer


class BenchmarkTests(unittest.TestCase):
    def test_per_database_samples_are_validated(self) -> None:
        self.assertEqual(run_experiment._parse_samples(["neutron=12", "dw=7"]),
                         [("neutron", 12), ("dw", 7)])
        with self.assertRaises(Exception):
            run_experiment._parse_samples(["neutron=0"])

    def test_empty_agent_record_is_resumable(self) -> None:
        self.assertTrue(run_experiment._is_infrastructure_failure({
            "turns": 0, "usage": {"totalTokens": 0}, "model": None, "pred_sql": None,
        }))
        self.assertFalse(run_experiment._is_infrastructure_failure({
            "turns": 1, "usage": {"totalTokens": 10}, "model": "m", "pred_sql": None,
        }))
        self.assertFalse(run_experiment._is_infrastructure_failure({
            "turns": 0, "budget_exhausted": "wall_clock", "pred_sql": None,
        }))

    @patch("run_experiment._protocol_fingerprint", return_value="new")
    @patch("run_experiment._score", side_effect=lambda rec, *_a: rec | {"correct": False})
    @patch("run_experiment._run_one", return_value={"budget_exhausted": "wall_clock"})
    def test_budget_timeout_is_scored_not_retried(self, run_one, _score, _fingerprint) -> None:
        rec, _ = run_experiment._run_one_and_score(
            {"id": "q", "question": "?", "sql": "SELECT 1"},
            "raw", "neutron", 6, 1,
        )
        self.assertEqual(run_one.call_count, 1)
        self.assertEqual(rec["harness_attempts"], 1)
        self.assertFalse(rec["correct"])

    def test_cache_requires_matching_protocol(self) -> None:
        with TemporaryDirectory() as temp:
            path = Path(temp) / "records.jsonl"
            metrics.write_jsonl(path, [
                {"id": "old", "protocol_fingerprint": "old"},
                {"id": "new", "protocol_fingerprint": "new"},
            ])
            self.assertEqual(set(run_experiment._load_existing(
                path, {"old": "new", "new": "new"}
            )), {"new"})

    def test_sampling_is_proportional_and_stable(self) -> None:
        questions = ([{"id": f"a{i}", "category": "a"} for i in range(80)]
                     + [{"id": f"b{i}", "category": "b"} for i in range(20)])
        first = manifest._stratified_sample(questions, 10, 77)
        second = manifest._stratified_sample(questions, 10, 77)
        self.assertEqual([q["id"] for q in first], [q["id"] for q in second])
        self.assertEqual(sum(q["category"] == "a" for q in first), 8)

    def test_only_outer_order_by_makes_result_order_significant(self) -> None:
        self.assertFalse(scorer._has_top_level_order_by(
            "WITH q AS (SELECT 1 ORDER BY 1) SELECT * FROM q"
        ))
        self.assertFalse(scorer._has_top_level_order_by(
            "SELECT ROW_NUMBER() OVER (ORDER BY id) FROM t"
        ))
        self.assertTrue(scorer._has_top_level_order_by(
            "WITH q AS (SELECT 1 ORDER BY 1) SELECT * FROM q ORDER BY 1"
        ))

    def test_validation_turns_follow_the_budget(self) -> None:
        system, _ = prompts.agent_prompts("neutron", "question", "raw", 16)
        self.assertIn("By turn 14, run the complete candidate query", system)
        self.assertIn("use turn 15 to repair", system)
        self.assertIn("Turn 16 is reserved", system)

    def test_arms_only_change_context(self) -> None:
        for arm, has_profile in {"raw": False, "profile": True}.items():
            system, user = prompts.agent_prompts("neutron", "question", arm, 10)
            self.assertEqual("profile.toc.md" in user, has_profile)
            self.assertEqual("schema-links.md" in user, has_profile)
            self.assertNotIn("BEGIN DB PROFILE", user)
            self.assertIn("Use any supplied database context first", system)
            self.assertIn("Turn 10 is reserved", system)
            self.assertIn("finish all tool use by turn 9", system)
            self.assertIn("By turn 8, run the complete candidate query", system)
            self.assertIn("use turn 9 to repair", system)
            self.assertIn("<ans>", system)
            self.assertIn("<ans>...</ans>", user)
            self.assertIn("BEGIN SUPPLIED DATABASE CONTEXT", user)
            self.assertNotIn("primary schema briefing", user)


if __name__ == "__main__":
    unittest.main()
