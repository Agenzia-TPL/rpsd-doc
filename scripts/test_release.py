#!/usr/bin/env python3
"""Prove di site-releases: regole R1–R4 di check_release.py.

R1–R3 sul solo testo della pagina; R4 su un repository git temporaneo con un branch
main, un branch laterale e tag annotati e leggeri.

Uso: python scripts/test_release.py [-v]
"""
from __future__ import annotations

import subprocess
import sys
import tempfile
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT / "scripts"))
import check_release as cr  # noqa: E402

START = "<!-- --8<-- [start:recenti] -->"
END = "<!-- --8<-- [end:recenti] -->"
HEAD = "| Versione | Data | Novità |\n|---|---|---|\n"


def row(version: str, date: str = "22 nov 2026", news: str = "Novità") -> str:
    return f"| **{version}** | {date} | {news} |\n"


def page(rows: list[str], recent: int | None = None) -> str:
    """Pagina con le prime `recent` righe fra i marcatori (default min(3, righe))."""
    n = min(3, len(rows)) if recent is None else recent
    return "# Release del sito\n\n" + START + "\n" + HEAD + "".join(rows[:n]) + END + "\n" + "".join(rows[n:])


def rules(text: str) -> list[str]:
    releases, r1, block = cr.parse(text)
    problems = r1 + cr.check_order(releases) + (cr.check_recent(block) if block else [])
    return sorted({p.rule for p in problems})


class PageRules(unittest.TestCase):
    def test_empty_table_passes(self):
        self.assertEqual(rules(page([])), [])

    def test_valid_table_passes(self):
        rows = [row("0.3.0", "1 dic 2026"), row("0.2.1", "28 nov 2026"), row("0.2.0", "25 nov 2026"),
                row("0.1.0", "22 nov 2026")]
        self.assertEqual(rules(page(rows)), [])

    def test_real_page_passes(self):
        self.assertEqual(rules((ROOT / cr.RELEASE).read_text(encoding="utf-8")), [])

    def test_malformed_version(self):
        self.assertEqual(rules(page([row("0.1")])), ["R1"])

    def test_version_not_bold(self):
        self.assertEqual(rules(page(["| 0.1.0 | 22 nov 2026 | Novità |\n"])), ["R1"])

    def test_invalid_date(self):
        self.assertEqual(rules(page([row("0.1.0", "31 nov 2026")])), ["R1"])
        self.assertEqual(rules(page([row("0.1.0", "2026-11-22")])), ["R1"])

    def test_empty_news(self):
        self.assertEqual(rules(page([row("0.1.0", news="")])), ["R1"])

    def test_missing_header(self):
        self.assertEqual(rules("# Release del sito\n\nNiente tabella.\n"), ["R1"])

    def test_versions_not_decreasing(self):
        self.assertEqual(rules(page([row("0.1.0"), row("0.2.0")])), ["R2"])
        self.assertEqual(rules(page([row("0.1.0"), row("0.1.0")])), ["R2"])

    def test_dates_increasing(self):
        self.assertEqual(rules(page([row("0.2.0", "20 nov 2026"), row("0.1.0", "22 nov 2026")])), ["R2"])

    def test_markers_missing(self):
        text = "# Release del sito\n\n" + HEAD + row("0.1.0")
        self.assertEqual(rules(text), ["R3"])

    def test_too_many_recent_rows(self):
        rows = [row(f"0.{n}.0", "22 nov 2026") for n in (4, 3, 2, 1)]
        self.assertEqual(rules(page(rows, recent=4)), ["R3"])

    def test_too_few_recent_rows(self):
        rows = [row(f"0.{n}.0", "22 nov 2026") for n in (3, 2, 1)]
        self.assertEqual(rules(page(rows, recent=1)), ["R3"])


class TagRule(unittest.TestCase):
    """R4 su un repository temporaneo: main con la 0.1.0, branch laterale con la 0.2.0."""

    def setUp(self):
        self.tmp = tempfile.TemporaryDirectory()
        self.root = Path(self.tmp.name)
        self.git("init", "-q", "-b", "main")
        self.git("config", "user.email", "test@example.com")
        self.git("config", "user.name", "Test")
        self.commit(page([row("0.1.0")]), "Release 0.1.0")

    def tearDown(self):
        self.tmp.cleanup()

    def git(self, *args: str) -> None:
        subprocess.run(["git", *args], cwd=self.root, check=True, capture_output=True)

    def commit(self, text: str, message: str) -> None:
        path = self.root / cr.RELEASE
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_text(text, encoding="utf-8")
        self.git("add", "-A")
        self.git("commit", "-q", "-m", message)

    def rules(self, tag: str) -> list[str]:
        return sorted({p.rule for p in cr.check_tag(self.root, tag, "main")})

    def test_annotated_tag_on_main_matching_first_row_passes(self):
        self.git("tag", "-a", "v0.1.0", "-m", "rpsd-doc 0.1.0")
        self.assertEqual(self.rules("v0.1.0"), [])

    def test_lightweight_tag_fails(self):
        self.git("tag", "v0.1.0")
        self.assertEqual(self.rules("v0.1.0"), ["R4"])

    def test_tag_not_matching_first_row_fails(self):
        self.git("tag", "-a", "v0.2.0", "-m", "rpsd-doc 0.2.0")
        problems = cr.check_tag(self.root, "v0.2.0", "main")
        self.assertEqual([p.rule for p in problems], ["R4"])
        self.assertIn("0.1.0", problems[0].message)

    def test_tag_outside_main_fails(self):
        self.git("checkout", "-q", "-b", "laterale")
        self.commit(page([row("0.2.0"), row("0.1.0")]), "Release 0.2.0 fuori da main")
        self.git("tag", "-a", "v0.2.0", "-m", "rpsd-doc 0.2.0")
        problems = cr.check_tag(self.root, "v0.2.0", "main")
        self.assertEqual([p.rule for p in problems], ["R4"])
        self.assertIn("non è su main", problems[0].message)

    def test_ref_that_is_not_a_release_tag_fails(self):
        self.assertEqual(self.rules("main"), ["R4"])
        self.assertEqual(self.rules("v0.1"), ["R4"])


if __name__ == "__main__":
    unittest.main()
