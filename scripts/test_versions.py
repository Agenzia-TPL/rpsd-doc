#!/usr/bin/env python3
"""Prove di profile-versioning: una versione NeTEx precedente (5.0.0) e una corrente (5.1.0).

La fixture parte dai sorgenti reali del sito (mkdocs.yml, overrides/, docs/), simula la
pubblicazione di NeTEx 5.1.0 seguendo la procedura di CONTRIBUTING.md e costruisce i due
siti (prima e dopo) con Zensical. Seguono i casi non conformi delle regole V1–V7.

Uso: python scripts/test_versions.py [-v]
"""
from __future__ import annotations

import re
import shutil
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT / "scripts"))
import check_versions as cv  # noqa: E402
from check_sidebar import hrefs, primary_nav, top_level_items  # noqa: E402
from check_urls import build, compare  # noqa: E402
from spike import copy_site_sources, load_config  # noqa: E402

OLD, NEW = "5.0.0", "5.1.0"
FRAME = "# ResourceFrame\n\n!!! note \"Pagina di prova\"\n\n    Pagina della fixture di test_versions.py.\n"


def replace(path: Path, old: str, new: str) -> None:
    text = path.read_text(encoding="utf-8")
    if old not in text:
        raise AssertionError(f"{path.name}: testo atteso non trovato: {old!r}")
    path.write_text(text.replace(old, new), encoding="utf-8")


def make_base(dest: Path) -> None:
    """Sito reale con una pagina ResourceFrame nella versione 5.0.0 (corrente)."""
    copy_site_sources(dest, ROOT)
    (dest / "docs/netex" / OLD / "frame").mkdir(parents=True)
    (dest / "docs/netex" / OLD / "frame/resourceframe.md").write_text(FRAME, encoding="utf-8")


def publish_new_version(dest: Path) -> None:
    """Procedura di CONTRIBUTING.md per pubblicare NeTEx 5.1.0."""
    new = dest / "docs/netex" / NEW
    shutil.copytree(dest / "docs/netex" / OLD, new)  # pagine nuove; la 5.0.0 non si tocca
    replace(new / "index.md", f"# Profilo NeTEx {OLD}", f"# Profilo NeTEx {NEW}")
    cfg = dest / "mkdocs.yml"
    replace(cfg, f'corrente: "{OLD}"\n      versioni:\n        "{OLD}": corrente',
            f'corrente: "{NEW}"\n      versioni:\n        "{NEW}": corrente\n        "{OLD}": precedente')
    replace(cfg, f"netex/corrente/index.md: netex/{OLD}/index.md", f"netex/corrente/index.md: netex/{NEW}/index.md")
    replace(dest / "docs/netex/.nav.yml", f"Profilo {OLD}: {OLD}", f"Profilo {NEW}: {NEW}")
    replace(dest / "docs/netex/index.md", f"| [{OLD}]({OLD}/index.md) | corrente |",
            f"| [{NEW}]({NEW}/index.md) | corrente | _da completare_ | _da completare_ |\n"
            f"| [{OLD}]({OLD}/index.md) | precedente |")


class TwoVersions(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.tmp = tempfile.TemporaryDirectory()
        cls.base, cls.head = Path(cls.tmp.name) / "base", Path(cls.tmp.name) / "head"
        cls.base.mkdir()
        make_base(cls.base)
        shutil.copytree(cls.base, cls.head)
        publish_new_version(cls.head)
        cls.base_urls, _ = build(cls.base, strict=True)
        cls.head_urls, _ = build(cls.head, strict=True)
        cls.config = load_config(cls.head / "mkdocs.yml")

    @classmethod
    def tearDownClass(cls):
        cls.tmp.cleanup()

    def html(self, rel: str) -> str:
        return (self.head / "site" / rel / "index.html").read_text(encoding="utf-8")

    def test_current_netex_profile_url_contains_version(self):
        # Scenario: Current NeTEx profile
        self.assertIn(f"netex/{NEW}/frame/resourceframe/", self.head_urls)

    def test_new_version_keeps_previous_urls_and_sources(self):
        # Scenario: New profile version published
        self.assertEqual(compare(self.base_urls, self.head_urls), [])
        for page in sorted((self.base / "docs/netex" / OLD).rglob("*")):
            if page.is_file():
                twin = self.head / page.relative_to(self.base)
                self.assertEqual(page.read_bytes(), twin.read_bytes(), str(page.relative_to(self.base)))

    def test_version_list(self):
        # Scenario: Reader looks for an older version
        self.assertEqual(cv.check_version_list(self.head, self.config), [])
        html = self.html("netex")
        for v in (NEW, OLD):
            self.assertRegex(html, rf'href="(\./)?{re.escape(v)}/"')
        self.assertIn("precedente", html)

    def test_notice_on_previous_version(self):
        # Scenario: Page of a previous version
        self.assertEqual(cv.check_site_notices(self.head / "site", self.config), [])
        html = self.html(f"netex/{OLD}/frame/resourceframe")
        self.assertIn("Versione precedente del profilo", html)
        self.assertRegex(html, rf'href="[^"]*/netex/{re.escape(NEW)}/"')
        self.assertNotIn(cv.NOTICE_CLASS, self.html(f"netex/{NEW}/frame/resourceframe"))

    def test_sidebar_lists_current_version_only(self):
        # Scenario: Two versions documented
        items = top_level_items(primary_nav(self.html("netex")))
        active = [i for i in items if "md-nav__item--active" in i.classes()]
        links = hrefs(active[0])
        self.assertTrue(any(NEW in h for h in links), links)
        self.assertFalse(any(OLD in h for h in links), links)

    def test_alias_leads_to_current_version(self):
        # Scenario: Link from the operational guide
        self.assertIn(f"url=../{NEW}/", self.html("netex/corrente"))

    def test_all_rules_pass_on_fixture(self):
        problems = (cv.check_metadata(self.config) + cv.check_folders(self.head, self.config)
                    + cv.check_sidebar_nav(self.head, self.config) + cv.check_alias(self.config))
        self.assertEqual(problems, [])


class NonCompliant(unittest.TestCase):
    """Casi non conformi su copie dei sorgenti reali (senza build)."""

    def setUp(self):
        self.tmp = tempfile.TemporaryDirectory()
        self.root = Path(self.tmp.name)
        copy_site_sources(self.root, ROOT)

    def tearDown(self):
        self.tmp.cleanup()

    def config(self) -> dict:
        return load_config(self.root / "mkdocs.yml")

    def rules(self, problems) -> list[str]:
        return sorted({p.rule for p in problems})

    def test_current_not_declared(self):
        replace(self.root / "mkdocs.yml", 'corrente: "5.0.0"', 'corrente: "5.9.0"')
        self.assertEqual(self.rules(cv.check_metadata(self.config())), ["V1"])

    def test_two_current_versions(self):
        replace(self.root / "mkdocs.yml", '"5.0.0": corrente', '"5.0.0": corrente\n        "4.0.0": corrente')
        self.assertEqual(self.rules(cv.check_metadata(self.config())), ["V1"])

    def test_undeclared_version_folder(self):
        (self.root / "docs/netex/5.2.0").mkdir()
        (self.root / "docs/netex/5.2.0/index.md").write_text("# x\n", encoding="utf-8")
        self.assertEqual(self.rules(cv.check_folders(self.root, self.config())), ["V2"])

    def test_page_outside_version_folders(self):
        (self.root / "docs/netex/pagina.md").write_text("# x\n", encoding="utf-8")
        self.assertEqual(self.rules(cv.check_folders(self.root, self.config())), ["V2"])

    def test_glob_in_profile_nav(self):
        replace(self.root / "docs/netex/.nav.yml", "  - Profilo 5.0.0: 5.0.0\n", '  - Profilo 5.0.0: 5.0.0\n  - "*"\n')
        self.assertEqual(self.rules(cv.check_sidebar_nav(self.root, self.config())), ["V3"])

    def test_wrong_alias(self):
        replace(self.root / "mkdocs.yml", "netex/corrente/index.md: netex/5.0.0/index.md",
                "netex/corrente/index.md: netex/index.md")
        self.assertEqual(self.rules(cv.check_alias(self.config())), ["V4"])

    def test_version_list_with_wrong_state(self):
        replace(self.root / "docs/netex/index.md", "| [5.0.0](5.0.0/index.md) | corrente |",
                "| [5.0.0](5.0.0/index.md) | precedente |")
        self.assertEqual(self.rules(cv.check_version_list(self.root, self.config())), ["V5"])

    def test_version_list_missing_row(self):
        replace(self.root / "docs/netex/index.md", "| [5.0.0](5.0.0/index.md) | corrente |", "| 5.0.0 | corrente |")
        self.assertEqual(self.rules(cv.check_version_list(self.root, self.config())), ["V5"])

    def test_missing_notice_on_built_page(self):
        cfg = {"extra": {"profili": {"netex": {"corrente": "5.1.0", "versioni": {"5.1.0": "corrente",
                                                                                 "5.0.0": "precedente"}}}}}
        site = self.root / "site"
        for v in ("5.0.0", "5.1.0"):
            (site / "netex" / v).mkdir(parents=True)
            (site / "netex" / v / "index.html").write_text("<html>pagina</html>", encoding="utf-8")
        self.assertEqual(self.rules(cv.check_site_notices(site, cfg)), ["V6"])


class FrozenVersions(unittest.TestCase):
    """Commit su una versione non corrente con e senza trailer Errata."""

    def git(self, *args: str, message: str | None = None) -> None:
        cmd = ["git", "-c", "user.name=Prova", "-c", "user.email=prova@example.invalid", *args]
        if message is not None:
            cmd += ["-m", message]
        subprocess.run(cmd, cwd=self.root, capture_output=True, text=True, check=True)

    def setUp(self):
        self.tmp = tempfile.TemporaryDirectory()
        self.root = Path(self.tmp.name)
        copy_site_sources(self.root, ROOT)
        publish_new_version(self.root)
        self.git("init", "-q", "-b", "main")
        self.git("add", "-A")
        self.git("commit", "-q", message="base")
        self.git("tag", "base")
        self.page = self.root / "docs/netex" / OLD / "index.md"

    def tearDown(self):
        self.tmp.cleanup()

    def edit_old_version(self, message: str) -> list:
        self.page.write_text(self.page.read_text(encoding="utf-8") + "\nCorrezione.\n", encoding="utf-8")
        self.git("commit", "-qa", message=message)
        return cv.check_frozen(self.root, load_config(self.root / "mkdocs.yml"), "base")

    def test_edit_without_errata_fails(self):
        problems = self.edit_old_version("modifica")
        self.assertEqual([p.rule for p in problems], ["V7"])
        self.assertIn("nuova cartella", problems[0].message)

    def test_edit_with_errata_passes(self):
        self.assertEqual(self.edit_old_version("correzione refuso\n\nErrata: refuso nel titolo"), [])


if __name__ == "__main__":
    unittest.main()
