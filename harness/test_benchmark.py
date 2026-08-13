from __future__ import annotations

import unittest
from unittest.mock import patch

import run_experiment
from harness import manifest, prompts


class BenchmarkTests(unittest.TestCase):
    def test_per_database_samples_are_validated(self) -> None:
        self.assertEqual(run_experiment._parse_samples(["neutron=12", "dw=7"]),
                         [("neutron", 12), ("dw", 7)])
        with self.assertRaises(Exception):
            run_experiment._parse_samples(["neutron=0"])

    def test_sampling_is_proportional_and_stable(self) -> None:
        questions = ([{"id": f"a{i}", "category": "a"} for i in range(80)]
                     + [{"id": f"b{i}", "category": "b"} for i in range(20)])
        first = manifest._stratified_sample(questions, 10, 77)
        second = manifest._stratified_sample(questions, 10, 77)
        self.assertEqual([q["id"] for q in first], [q["id"] for q in second])
        self.assertEqual(sum(q["category"] == "a" for q in first), 8)

    @patch("harness.prompts._profile", return_value="PROFILE")
    @patch("harness.prompts._metadata", return_value="METADATA")
    def test_four_arms_only_change_context(self, _metadata, _profile) -> None:
        expected = {
            "raw": (False, False), "profile": (True, False),
            "metadata": (False, True), "profile_metadata": (True, True),
        }
        for arm, (has_profile, has_metadata) in expected.items():
            _, user = prompts.agent_prompts("neutron", "question", arm, 10)
            self.assertEqual("PROFILE" in user, has_profile)
            self.assertEqual("METADATA" in user, has_metadata)


if __name__ == "__main__":
    unittest.main()
