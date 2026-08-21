"""Tests for the SQLite benchmark paths: BIRD (Mini-Dev) and Spider 2.0-lite.

Covers the official-semantics comparison ports (set equality for BIRD,
column-vector fuzzy matching for Spider 2.0), the read-only SQLite executor,
and per-benchmark stratification. Runs entirely on temporary files — no MySQL,
no downloaded datasets."""
from __future__ import annotations

import json
import sqlite3
import unittest
from pathlib import Path
from tempfile import TemporaryDirectory

from harness import manifest, scorer, spider2_eval, sqlite_io
from harness.generate_schema_links import _link_sqlite


def _make_db(path: Path) -> None:
    conn = sqlite3.connect(path)
    conn.executescript("""
        CREATE TABLE dept (id INTEGER PRIMARY KEY, name TEXT);
        CREATE TABLE emp (id INTEGER PRIMARY KEY, name TEXT,
                          dept_id INTEGER REFERENCES dept(id), salary REAL);
        INSERT INTO dept VALUES (1, 'eng'), (2, 'sales');
        INSERT INTO emp VALUES (1, 'ada', 1, 100.0), (2, 'bob', 2, 50.0),
                               (3, 'eve', 1, 200.0);
    """)
    conn.commit()
    conn.close()


class SqliteIoTests(unittest.TestCase):
    def setUp(self) -> None:
        self._tmp = TemporaryDirectory()
        self.db = Path(self._tmp.name) / "t.sqlite"
        _make_db(self.db)

    def tearDown(self) -> None:
        self._tmp.cleanup()

    def test_select_returns_tuples(self) -> None:
        res = sqlite_io.execute("SELECT name FROM dept ORDER BY id", self.db, 10)
        self.assertIsNone(res.error)
        self.assertFalse(res.timed_out)
        self.assertEqual(res.rows, [("eng",), ("sales",)])

    def test_connection_is_read_only(self) -> None:
        res = sqlite_io.execute("DELETE FROM emp", self.db, 10)
        self.assertIsNotNone(res.error)
        self.assertIsNone(res.rows)
        # table untouched
        check = sqlite_io.execute("SELECT COUNT(*) FROM emp", self.db, 10)
        self.assertEqual(check.rows, [(3,)])

    def test_missing_table_is_reported_as_error(self) -> None:
        res = sqlite_io.execute("SELECT * FROM nope", self.db, 10)
        self.assertIn("no such table", res.error)


class BirdScoringTests(unittest.TestCase):
    """BIRD official EX: set(pred rows) == set(gold rows) — order and
    duplicates ignored, everything else exact."""

    def setUp(self) -> None:
        self._tmp = TemporaryDirectory()
        self.db = Path(self._tmp.name) / "bird.sqlite"
        _make_db(self.db)

    def tearDown(self) -> None:
        self._tmp.cleanup()

    def _score(self, pred: str, gold: str) -> dict:
        return scorer.score_prediction(pred, gold, str(self.db),
                                       engine="sqlite", mode="bird")

    def test_exact_match_with_reordered_rows_and_duplicates(self) -> None:
        gold = "SELECT name FROM dept ORDER BY id"
        pred = "SELECT name FROM dept UNION ALL SELECT name FROM dept"
        rec = self._score(pred, gold)
        self.assertTrue(rec["valid_sql"])
        self.assertTrue(rec["correct"])

    def test_order_by_only_difference_is_correct(self) -> None:
        rec = self._score("SELECT name FROM dept ORDER BY name",
                          "SELECT name FROM dept")
        self.assertTrue(rec["correct"])

    def test_extra_row_is_wrong(self) -> None:
        rec = self._score("SELECT name FROM dept UNION ALL SELECT 'x'",
                          "SELECT name FROM dept")
        self.assertFalse(rec["correct"])
        self.assertEqual(rec["missing_rows"], [])
        self.assertEqual(rec["extra_rows"], [["x"]])

    def test_cell_value_difference_is_wrong(self) -> None:
        rec = self._score("SELECT name || '!' FROM dept", "SELECT name FROM dept")
        self.assertFalse(rec["correct"])


class Spider2EvalTests(unittest.TestCase):
    def setUp(self) -> None:
        self._tmp = TemporaryDirectory()
        self.dir = Path(self._tmp.name)

    def tearDown(self) -> None:
        self._tmp.cleanup()

    def _gold(self, name: str, header: list[str], rows: list[list]) -> str:
        path = self.dir / name
        lines = [",".join(header)] + [",".join(str(c) for c in r) for r in rows]
        path.write_text("\n".join(lines) + "\n", encoding="utf-8")
        return str(path)

    def test_column_coercion_matches_pandas(self) -> None:
        self.assertEqual(spider2_eval._coerce_column(["1", "2.5"]), [1.0, 2.5])
        # one non-numeric cell keeps the whole column as strings
        self.assertEqual(spider2_eval._coerce_column(["1", "x"]), ["1", "x"])
        # empty cells are NaN-equivalent
        self.assertEqual(spider2_eval._coerce_column(["", None]), [None, None])

    def test_exact_column_match(self) -> None:
        gold = self._gold("g.csv", ["a", "b"], [["eng", 10], ["sales", 20]])
        self.assertEqual(spider2_eval.score_pred([("eng", 10), ("sales", 20)], [gold]), 1)

    def test_extra_predicted_columns_allowed(self) -> None:
        gold = self._gold("g.csv", ["a"], [["eng"], ["sales"]])
        pred = [("eng", 1), ("sales", 2)]
        self.assertEqual(spider2_eval.score_pred(pred, [gold]), 1)

    def test_missing_gold_column_fails(self) -> None:
        gold = self._gold("g.csv", ["a", "b"], [["eng", 10], ["sales", 20]])
        self.assertEqual(spider2_eval.score_pred([("eng",), ("sales",)], [gold]), 0)

    def test_numeric_tolerance_is_one_hundredth(self) -> None:
        gold = self._gold("g.csv", ["v"], [[10.0]])
        self.assertEqual(spider2_eval.score_pred([(10.009,)], [gold]), 1)
        self.assertEqual(spider2_eval.score_pred([(10.02,)], [gold]), 0)

    def test_string_comparison_is_exact(self) -> None:
        gold = self._gold("g.csv", ["a"], [["Engineering"]])
        self.assertEqual(spider2_eval.score_pred([("engineering",)], [gold]), 0)
        self.assertEqual(spider2_eval.score_pred([("Engineering",)], [gold]), 1)

    def test_condition_cols_restrict_gold_columns(self) -> None:
        gold = self._gold("g.csv", ["a", "b"], [["eng", 10], ["sales", 20]])
        # only gold column 0 must be matched by some pred column
        self.assertEqual(spider2_eval.score_pred([("eng",), ("sales",)], [gold],
                                                condition_cols=[0]), 1)
        # column 1 is required now
        self.assertEqual(spider2_eval.score_pred([("eng",), ("sales",)], [gold],
                                                condition_cols=[1]), 0)

    def test_ignore_order_sorts_vectors(self) -> None:
        gold = self._gold("g.csv", ["v"], [[3], [1], [2]])
        # positional comparison: [1,2,3] != [3,1,2]
        self.assertEqual(spider2_eval.score_pred([(1,), (2,), (3,)], [gold]), 0)
        self.assertEqual(
            spider2_eval.score_pred([(2,), (1,), (3,)], [gold], ignore_order=True), 1)

    def test_multi_gold_is_any_of(self) -> None:
        g1 = self._gold("g_a.csv", ["a"], [["eng"]])
        g2 = self._gold("g_b.csv", ["a"], [["sales"]])
        self.assertEqual(spider2_eval.score_pred([("sales",)], [g1, g2]), 1)
        self.assertEqual(spider2_eval.score_pred([("other",)], [g1, g2]), 0)

    def test_mismatch_diagnostics_select_closest_gold_variant(self) -> None:
        g1 = self._gold("g_a.csv", ["a", "b"], [["eng", 10]])
        g2 = self._gold("g_b.csv", ["a"], [["sales"]])
        details = spider2_eval.score_pred_details([("other",)], [g1, g2], [[0, 1], [0]])
        self.assertEqual(details["selected_index"], 1)
        self.assertEqual(details["condition_cols"], [0])
        self.assertEqual(details["unmatched_gold_columns"], [["sales"]])

    def test_empty_gold_csv_scores_vacuously(self) -> None:
        gold = self._gold("g.csv", ["a"], [])
        self.assertEqual(spider2_eval.score_pred([], [gold]), 1)
        self.assertEqual(spider2_eval.score_pred([("x",)], [gold]), 0)

    def test_scoring_via_score_prediction(self) -> None:
        db = self.dir / "sp.sqlite"
        _make_db(db)
        gold = self._gold("g.csv", ["name"], [["eng"], ["sales"]])
        rec = scorer.score_prediction(
            "SELECT name FROM dept ORDER BY id", None, str(db),
            engine="sqlite", mode="spider2",
            eval_meta={"gold_csvs": [gold], "condition_cols": None, "ignore_order": False},
        )
        self.assertTrue(rec["valid_sql"])
        self.assertTrue(rec["correct"])
        self.assertEqual(rec["gold_rows"], 2)

    def test_scoring_record_carries_spider_diagnostics(self) -> None:
        db = self.dir / "sp.sqlite"
        _make_db(db)
        g1 = self._gold("g_a.csv", ["name", "count"], [["other", 1]])
        g2 = self._gold("g_b.csv", ["name"], [["other"]])
        rec = scorer.score_prediction(
            "SELECT name FROM dept ORDER BY id", None, str(db),
            engine="sqlite", mode="spider2",
            eval_meta={"gold_csvs": [g1, g2], "condition_cols": [[0, 1], [0]],
                       "ignore_order": False},
        )
        self.assertEqual(rec["selected_gold_variant"], g2)
        self.assertEqual(rec["condition_cols"], [0])
        self.assertEqual(rec["unmatched_gold_columns"], [["other"]])


class BeaverDiagnosticTests(unittest.TestCase):
    def test_column_counts_and_missing_extra_samples(self) -> None:
        with TemporaryDirectory() as tmp:
            db = Path(tmp) / "beaver.sqlite"
            _make_db(db)
            rec = scorer.score_prediction(
                "SELECT name, id FROM dept WHERE id = 2",
                "SELECT name FROM dept WHERE id = 1",
                str(db), engine="sqlite", mode="beaver",
            )
        self.assertEqual((rec["gold_columns"], rec["pred_columns"]), (1, 2))
        self.assertEqual(rec["missing_row_sample"], ["eng"])
        self.assertEqual(rec["extra_row_sample"], ["sales", 2])

    def test_no_gold_csvs_is_unscorable(self) -> None:
        rec = scorer.score_prediction("SELECT 1", None, "whatever.sqlite",
                                      engine="sqlite", mode="spider2", eval_meta={})
        self.assertEqual(rec["gold_error"], "no gold CSVs for spider2 question")
        self.assertFalse(rec["correct"])


class StratificationTests(unittest.TestCase):
    def test_stratified_sample_by_difficulty(self) -> None:
        questions = [{"id": f"bird_{i}", "question": "q", "sql": "SELECT 1",
                      "difficulty": d}
                     for i, d in enumerate(
                         ["simple"] * 30 + ["moderate"] * 50 + ["challenging"] * 20)]
        sample = manifest._stratified_sample(questions, 50, seed=7,
                                             strata=["difficulty"])
        self.assertEqual(len(sample), 50)
        per = {d: sum(1 for q in sample if q["difficulty"] == d)
               for d in ("simple", "moderate", "challenging")}
        # proportional to stratum size (30/50/20 of 100 → 15/25/10 of 50)
        self.assertEqual(per, {"simple": 15, "moderate": 25, "challenging": 10})

    def test_sample_carries_optional_fields(self) -> None:
        questions = [{"id": "bird_1", "question": "q", "sql": "SELECT 1",
                      "engine": "sqlite", "db": "data/x/y.sqlite",
                      "evidence": "external knowledge", "difficulty": "simple",
                      "gold_csvs": ["gold/1.csv"], "condition_cols": [0],
                      "ignore_order": True}]
        sample = manifest._stratified_sample(questions, 1, seed=1, strata=["difficulty"])
        for key in ("engine", "db", "evidence", "difficulty", "gold_csvs",
                    "condition_cols", "ignore_order"):
            self.assertIn(key, sample[0])


class SchemaLinksSqliteTests(unittest.TestCase):
    def test_schema_linker_report(self) -> None:
        with TemporaryDirectory() as tmp:
            db = Path(tmp) / "corp.sqlite"
            _make_db(db)
            text = _link_sqlite(db)
            self.assertIn("- version: ", text)
            self.assertIn("emp.dept_id -> dept.id", text)


if __name__ == "__main__":
    unittest.main()
