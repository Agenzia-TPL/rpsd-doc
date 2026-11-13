#!/usr/bin/env python3
"""Prove dei controlli di content-conventions: per ogni regola casi conformi e non conformi.

Uso: python scripts/test_conventions.py [-v]
"""
from __future__ import annotations

import subprocess
import sys
import tempfile
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT / "scripts"))
import check_conventions as cc  # noqa: E402
import check_urls as cu  # noqa: E402

GENERATED_PATHS = "docs/indicatori/catalogo/\ndocs/indicatori/matrice/\n"
GENERATED_FM = "---\ngenerato: true\ngenerato_da: rpsd-tools 0.1.0\n---\n"
GLOSSARY = "# Glossario\n\n### PdE {#pde .sigla}\n\nDefinizione di prova.\n\n### Frame {#frame}\n\nVoce non sigla.\n"
GLOSSARY_LINK = "[PdE](../panoramica/glossario.md#pde)"


class Fixture(unittest.TestCase):
    """Repository di prova in una directory temporanea."""

    def setUp(self):
        self.tmp = tempfile.TemporaryDirectory()
        self.root = Path(self.tmp.name)
        (self.root / "generated-paths.txt").write_text(GENERATED_PATHS, encoding="utf-8")
        self.write("docs/index.md", "# Home\n")

    def tearDown(self):
        self.tmp.cleanup()

    def write(self, rel: str, text: str) -> None:
        path = self.root / rel
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_text(text, encoding="utf-8")

    def rules(self, problems) -> list[str]:
        return [p.rule for p in problems]


class GeneratedPages(Fixture):
    def test_generated_page_with_front_matter_passes(self):
        self.write("docs/indicatori/catalogo/ind-1.md", GENERATED_FM + "# Indicatore\n")
        self.assertEqual(cc.check_generated_pages(self.root), [])

    def test_generated_page_without_front_matter_fails(self):
        self.write("docs/indicatori/catalogo/ind-1.md", "# Indicatore\n")
        self.assertEqual(self.rules(cc.check_generated_pages(self.root)), ["G1"])

    def test_generated_page_without_tool_fails(self):
        self.write("docs/indicatori/catalogo/ind-1.md", "---\ngenerato: true\n---\n# Indicatore\n")
        self.assertEqual(self.rules(cc.check_generated_pages(self.root)), ["G1"])

    def test_generated_page_outside_generated_paths_fails(self):
        self.write("docs/guida/pagina.md", GENERATED_FM + "# Pagina\n")
        self.assertEqual(self.rules(cc.check_generated_pages(self.root)), ["G2"])


class HandEditCommits(Fixture):
    def git(self, *args: str, message: str | None = None) -> str:
        cmd = ["git", "-c", "user.name=Prova", "-c", "user.email=prova@example.invalid", *args]
        if message is not None:
            cmd += ["-m", message]
        return subprocess.run(cmd, cwd=self.root, capture_output=True, text=True, check=True).stdout

    def setUp(self):
        super().setUp()
        self.git("init", "-q", "-b", "main")
        self.write("docs/indicatori/catalogo/ind-1.md", GENERATED_FM + "# Indicatore\n")
        self.git("add", "-A")
        self.git("commit", "-q", message="base")
        self.git("tag", "base")

    def test_commit_without_trailer_fails_and_explains(self):
        self.write("docs/indicatori/catalogo/ind-1.md", GENERATED_FM + "# Indicatore corretto a mano\n")
        self.git("commit", "-qa", message="correzione a mano")
        problems = cc.check_commits(self.root, "base")
        self.assertEqual(self.rules(problems), ["G3"])
        self.assertIn("data/", problems[0].message)
        self.assertIn("docs/indicatori/catalogo/ind-1.md", problems[0].message)

    def test_commit_with_trailer_passes(self):
        self.write("docs/indicatori/catalogo/ind-1.md", GENERATED_FM + "# Indicatore rigenerato\n")
        self.git("commit", "-qa", message="rigenerazione\n\nGenerato-da: rpsd-tools 0.2.0")
        self.assertEqual(cc.check_commits(self.root, "base"), [])

    def test_commit_outside_generated_paths_passes(self):
        self.write("docs/guida/pagina.md", "# Pagina\n")
        self.git("add", "-A")
        self.git("commit", "-q", message="pagina redazionale")
        self.assertEqual(cc.check_commits(self.root, "base"), [])


class PageLength(Fixture):
    def test_1500_words_passes(self):
        self.write("docs/guida/pagina.md", "# Titolo\n\n" + "parola " * 1499 + "\n")
        self.assertEqual(cc.check_length(self.root), [])

    def test_1501_words_fails_with_count(self):
        self.write("docs/guida/pagina.md", "# Titolo\n\n" + "parola " * 1500 + "\n")
        problems = cc.check_length(self.root)
        self.assertEqual(self.rules(problems), ["L1"])
        self.assertIn("1501 parole", problems[0].message)

    def test_code_blocks_do_not_count(self):
        code = "```xml\n" + "<Elemento/> " * 800 + "\n```\n"
        self.write("docs/guida/pagina.md", "# Titolo\n\n" + "parola " * 1400 + "\n\n" + code)
        self.assertEqual(cc.check_length(self.root), [])

    def test_generated_pages_are_not_counted(self):
        self.write("docs/indicatori/catalogo/ind-1.md", GENERATED_FM + "parola " * 3000)
        self.assertEqual(cc.check_length(self.root), [])


class Callouts(Fixture):
    def check(self, line: str) -> list[str]:
        self.write("docs/guida/pagina.md", f"# Pagina\n\n{line}\n\n    Testo.\n")
        return self.rules(cc.check_callouts(self.root))

    def test_free_types_pass(self):
        for kind in ("note", "tip", "warning", "example"):
            self.assertEqual(self.check(f'!!! {kind} "Titolo qualsiasi"'), [], kind)

    def test_reserved_titles_pass(self):
        self.assertEqual(self.check('!!! danger "Obbligatorio per KPI"'), [])
        self.assertEqual(self.check('??? info "Novità Rapsodia"'), [])

    def test_danger_with_other_title_fails(self):
        self.assertEqual(self.check('!!! danger "Attenzione"'), ["C1"])

    def test_info_without_title_fails(self):
        self.assertEqual(self.check("!!! info"), ["C1"])

    def test_reserved_title_on_other_type_fails(self):
        self.assertEqual(self.check('!!! warning "Obbligatorio per KPI"'), ["C1"])

    def test_unknown_type_fails(self):
        self.assertEqual(self.check('!!! abstract "Sintesi"'), ["C1"])

    def test_callout_inside_code_block_is_ignored(self):
        self.write("docs/guida/pagina.md", '# Pagina\n\n```markdown\n!!! abstract "Esempio"\n```\n')
        self.assertEqual(cc.check_callouts(self.root), [])


class Glossary(Fixture):
    def setUp(self):
        super().setUp()
        self.write(cc.GLOSSARY, GLOSSARY)

    def check(self, body: str) -> list[str]:
        self.write("docs/guida/pagina.md", "# Pagina\n\n" + body + "\n")
        return self.rules(cc.check_glossary(self.root))

    def test_first_use_linked_passes(self):
        self.assertEqual(self.check(f"Il {GLOSSARY_LINK} è trasmesso. Poi il PdE cambia."), [])

    def test_link_to_built_url_passes(self):
        self.assertEqual(self.check("Il [PdE](../../panoramica/glossario/#pde) è trasmesso."), [])

    def test_first_use_not_linked_fails(self):
        self.assertEqual(self.check(f"Il PdE è trasmesso. Poi il {GLOSSARY_LINK} cambia."), ["S1"])

    def test_link_to_wrong_anchor_fails(self):
        self.assertEqual(self.check("Il [PdE](../panoramica/glossario.md#frame) è trasmesso."), ["S1"])

    def test_code_and_headings_are_ignored(self):
        self.assertEqual(self.check(f"## Il PdE\n\nIl campo `PdE` e poi il {GLOSSARY_LINK}."), [])

    def test_callout_title_is_ignored(self):
        body = f'!!! note "Il PdE"\n\n    Il {GLOSSARY_LINK} nel testo del callout.'
        self.assertEqual(self.check(body), [])

    def test_callout_body_counts(self):
        body = f'!!! note "Nota"\n\n    Il PdE nel testo.\n\nPoi il {GLOSSARY_LINK}.'
        self.assertEqual(self.check(body), ["S1"])

    def test_term_not_marked_as_acronym_is_free(self):
        self.assertEqual(self.check("Il Frame contiene dati."), [])

    def test_whole_word_only(self):
        self.assertEqual(self.check("Il valore PdEx non è una sigla del glossario."), [])

    def test_missing_glossary_passes(self):
        (self.root / cc.GLOSSARY).unlink()
        self.assertEqual(self.check("Il PdE è trasmesso."), [])


class StableUrls(unittest.TestCase):
    """Spostamento di una pagina con e senza redirect (build reali con Zensical)."""

    def setUp(self):
        self.tmp = tempfile.TemporaryDirectory()
        base = Path(self.tmp.name)
        self.base, self.head = base / "base", base / "head"
        for d in (self.base, self.head):
            d.mkdir()
            cu.copy_site_sources(d, ROOT)  # sito reale: configurazione, override, pagine
        (self.base / "docs" / "vecchia.md").write_text("# Pagina\n", encoding="utf-8")
        (self.head / "docs" / "nuova").mkdir()
        (self.head / "docs" / "nuova" / "pagina.md").write_text("# Pagina\n", encoding="utf-8")

    def tearDown(self):
        self.tmp.cleanup()

    def lost(self) -> list[str]:
        base_urls, _ = cu.build(self.base, strict=False)
        head_urls, _ = cu.build(self.head, strict=True)
        return cu.compare(base_urls, head_urls)

    def test_moved_page_without_redirect_fails(self):
        self.assertEqual(self.lost(), ["vecchia/"])

    def test_moved_page_with_redirect_passes(self):
        config = self.head / "mkdocs.yml"
        text = config.read_text(encoding="utf-8")
        self.assertIn("      redirect_maps:\n", text)
        config.write_text(text.replace("      redirect_maps:\n",
                                       "      redirect_maps:\n        vecchia.md: nuova/pagina.md\n", 1),
                          encoding="utf-8")
        self.assertEqual(self.lost(), [])
        redirect = (self.head / "site" / "vecchia" / "index.html").read_text(encoding="utf-8")
        self.assertIn("../nuova/pagina/", redirect)


if __name__ == "__main__":
    unittest.main()
