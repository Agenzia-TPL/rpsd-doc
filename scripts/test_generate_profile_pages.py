#!/usr/bin/env python3
"""Test di generate_profile_pages.py su un bundle minimo scritto a mano (design D5).

Uso: python scripts/test_generate_profile_pages.py
"""
from __future__ import annotations

import sys
import tempfile
import unittest
from pathlib import Path

import yaml

sys.path.insert(0, str(Path(__file__).resolve().parent))
import generate_profile_pages as gen  # noqa: E402

BUNDLE = {
    "profile": "netex-it",
    "title": "Profilo di prova",
    "xsd": "prova@0000000",
    "guidelines": {"document": "Linee guida di prova.docx"},
    "version": "9.9.9",
    "generator": "rpsd-tools 0.0.0",
    "pages": [
        {"id": "index", "file": "index.md", "title": "Panoramica", "kind": "overview",
         "roots": ["netex:PublicationDelivery"], "tables": []},
        {"id": "timetable-frame", "file": "timetable-frame.md", "title": "TimetableFrame",
         "kind": "area", "tables": [
             {"anchor": "vehiclejourneys-servicejourney",
              "title": "vehicleJourneys / ServiceJourney", "level": 3,
              "section": "5.2.6", "table": 40, "rows": [
                  {"field": "passingTimes", "card": "0..1", "type": "x",
                   "link": {"kind": "child", "page": "timetable-frame",
                            "anchor": "passingtimes-timetabledpassingtime"},
                   "note": {"path": "//p", "meaning": "Orari",
                            "sources": [{"section": "5.2.6", "table": 40, "field": "x"}],
                            "issues": ["Nome diverso"]}},
                  {"field": "DayType", "card": "1..1", "type": "DayTypeEnumeration",
                   "enumeration": "DayTypeEnumeration"},
              ],
              "other_fields": [{"field": "Extensions", "card": "0..1", "type": "any"}]},
             {"anchor": "passingtimes-timetabledpassingtime",
              "title": "passingTimes / TimetabledPassingTime", "level": 4,
              "parent": "vehiclejourneys-servicejourney",
              "section": "5.2.6", "table": 41, "rows": []},
         ]},
    ],
    "enumerations": [{"name": "DayTypeEnumeration", "anchor": "daytypeenumeration",
                      "values": ["weekday", "holiday"]}],
    "issues": [
        {"id": "40-p", "path": "//p", "issue": "Nome diverso",
         "sources": [{"section": "5.2.6", "table": 40, "field": "x"}],
         "page": "timetable-frame", "anchor": "vehiclejourneys-servicejourney"},
        {"id": "40-p", "path": "//p", "issue": "Altra",
         "sources": [{"section": "5.2.6", "table": 40, "field": "x"}]},
    ],
}


class GenerateTest(unittest.TestCase):
    def setUp(self):
        self.tmp = Path(tempfile.mkdtemp())
        self.bundle = self.tmp / "site.yaml"
        self.bundle.write_text(yaml.safe_dump(BUNDLE, allow_unicode=True), encoding="utf-8")
        self.out = self.tmp / "out"

    def run_gen(self, *extra):
        return gen.main([str(self.bundle), str(self.out), *extra])

    def page(self, name):
        return (self.out / name).read_text(encoding="utf-8")

    def test_front_matter(self):
        self.run_gen()
        for name in ("index.md", "timetable-frame.md", "enumerations.md", "issues.md"):
            self.assertTrue(self.page(name).startswith(
                "---\ngenerato: true\ngenerato_da: rpsd-tools 0.0.0\n---\n<!-- GENERATED"), name)

    def test_anchors_links_and_box(self):
        self.run_gen()
        text = self.page("timetable-frame.md")
        self.assertIn("### vehicleJourneys / ServiceJourney {#vehiclejourneys-servicejourney}", text)
        self.assertIn("[`passingTimes`](#passingtimes-timetabledpassingtime)", text)
        self.assertIn("[⚠ Incongruenza](issues.md#40-p)", text)
        self.assertIn("[`DayTypeEnumeration`](enumerations.md#daytypeenumeration)", text)
        self.assertIn('??? note "Altri campi dell\'XSD"', text)
        issues = self.page("issues.md")
        self.assertEqual(issues.count('<a id="40-p"></a>'), 1)  # stesso id, una sola ancora
        self.assertIn("## DayTypeEnumeration {#daytypeenumeration}", self.page("enumerations.md"))
        self.assertIn("TimetableFrame: timetable-frame.md", self.page(".nav.yml"))

    def test_repeatable(self):
        self.run_gen()
        first = {p.name: p.read_bytes() for p in self.out.iterdir()}
        self.run_gen()
        self.assertEqual(first, {p.name: p.read_bytes() for p in self.out.iterdir()})

    def test_check(self):
        self.run_gen()
        self.assertEqual(self.run_gen("--check"), 0)
        target = self.out / "timetable-frame.md"
        target.write_text(target.read_text(encoding="utf-8") + "a mano\n", encoding="utf-8")
        self.assertEqual(self.run_gen("--check"), 1)
        self.run_gen()
        (self.out / "extra.md").write_text("x", encoding="utf-8")
        self.assertEqual(self.run_gen("--check"), 1)

    def test_replaces_folder(self):
        self.out.mkdir()
        (self.out / "vecchia.md").write_text("x", encoding="utf-8")
        self.run_gen()
        self.assertFalse((self.out / "vecchia.md").exists())

    def test_missing_keys(self):
        self.bundle.write_text(yaml.safe_dump({"profile": "x"}), encoding="utf-8")
        self.assertEqual(self.run_gen(), 1)
        self.assertFalse(self.out.exists())


if __name__ == "__main__":
    unittest.main()
