import sqlite3
from pathlib import Path
from tempfile import TemporaryDirectory
from unittest import TestCase
from unittest.mock import patch

from harness import generate_profiles


class GenerateProfilesTests(TestCase):
    def test_sqlite_profile_writes_toc(self) -> None:
        with TemporaryDirectory() as temp:
            root = Path(temp)
            db = root / "db.sqlite"
            sqlite3.connect(db).close()
            with (patch.object(generate_profiles.config, "PROFILES_DIR", root),
                  patch.object(generate_profiles, "profile_database_with_toc",
                               return_value=("PROFILE", "TOC"))):
                generate_profiles.run_sqlite(db, "test")
            self.assertEqual((root / "test.md").read_text(), "PROFILE")
            self.assertEqual((root / "test.toc.md").read_text(), "TOC")
