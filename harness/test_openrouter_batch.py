from __future__ import annotations

import unittest
from unittest.mock import patch

from harness import runner_zeroshot


class OpenRouterBatchTests(unittest.TestCase):
    @patch("harness.runner_zeroshot.time.sleep")
    @patch("harness.runner_zeroshot._batch_request")
    def test_submits_polls_and_maps_results(self, request, _sleep) -> None:
        request.side_effect = [
            {"id": "batch-1", "status": "validating"},
            {"id": "batch-1", "status": "in_progress",
             "request_counts": {"completed": 0, "failed": 0}},
            {
                "id": "batch-1", "status": "completed",
                "usage": {"prompt_tokens": 10, "completion_tokens": 2,
                          "total_tokens": 12, "cost": 0.001},
                "results": [{
                    "custom_id": "q1", "error": None,
                    "response": {"status_code": 200, "body": {
                        "model": "test/model",
                        "choices": [{"message": {"content": "<ans>SELECT 1</ans>"}}],
                    }},
                }],
            },
        ]

        records = runner_zeroshot.run_batch([{
            "custom_id": "q1", "db_label": "neutron", "question": "Return one",
            "arm": "zeroshot_profile", "db": "neutron",
        }])

        submitted = request.call_args_list[0].args[2]
        self.assertEqual(list(submitted), ["endpoint", "model", "requests"])
        self.assertEqual(submitted["requests"][0]["custom_id"], "q1")
        self.assertEqual(request.call_args_list[-1].args[:2],
                         ("GET", "https://openrouter.ai/api/beta/batches/batch-1"))
        self.assertEqual(records["q1"]["pred_sql"], "SELECT 1;")
        self.assertEqual(records["q1"]["usage"]["totalTokens"], 12)
        self.assertEqual(records["q1"]["cost"]["total"], 0.001)
        self.assertEqual(records["q1"]["openrouter_batch_id"], "batch-1")


if __name__ == "__main__":
    unittest.main()
