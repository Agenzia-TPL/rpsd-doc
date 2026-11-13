#!/usr/bin/env python3
"""Verifica che una sottosezione nuova compaia senza modificare la configurazione (scenario *New subsection*).

Copia mkdocs.yml e docs/ in una directory temporanea, aggiunge sotto una sezione
esistente (Guida operativa) una cartella con due pagine e il proprio .nav.yml,
costruisce in strict e verifica che:
- la sidebar della sezione contenga la sottosezione con il titolo dichiarato nel suo .nav.yml
  e le sue pagine nell'ordine dichiarato;
- mkdocs.yml e i .nav.yml esistenti non siano stati modificati.

Uso: python scripts/check_new_subsection.py [--without-glob]
  --without-glob  controllo di sanità: toglie "*" dal .nav.yml della sezione; lo script deve fallire
"""
from __future__ import annotations

import argparse
import hashlib
import shutil
import subprocess
import sys
import tempfile
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT / "scripts"))
from check_sidebar import hrefs, primary_nav, top_level_items  # noqa: E402
from spike import zensical  # noqa: E402

SECTION = "guida"
SUBSECTION = "prova-sottosezione"
TITLE = "Sottosezione di prova"
PAGES = {"seconda.md": "# Seconda pagina di prova\n", "prima.md": "# Prima pagina di prova\n"}
# Ordine volutamente non alfabetico, per verificare che conti quello del .nav.yml
NAV = f'title: {TITLE}\nnav:\n  - seconda.md\n  - prima.md\n'


def digest(paths: list[Path]) -> dict[str, str]:
    return {str(p): hashlib.sha256(p.read_bytes()).hexdigest() for p in paths}


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument("--without-glob", action="store_true", help='togli "*" dal .nav.yml della sezione')
    args = parser.parse_args()

    problems = []
    with tempfile.TemporaryDirectory() as tmp:
        tmp_root = Path(tmp)
        shutil.copy(ROOT / "mkdocs.yml", tmp_root / "mkdocs.yml")
        shutil.copytree(ROOT / "docs", tmp_root / "docs")
        if args.without_glob:
            nav = tmp_root / "docs" / SECTION / ".nav.yml"
            nav.write_text(nav.read_text(encoding="utf-8").replace('  - "*"\n', ""), encoding="utf-8")

        config_files = [tmp_root / "mkdocs.yml", *sorted((tmp_root / "docs").rglob(".nav.yml"))]
        before = digest(config_files)

        sub = tmp_root / "docs" / SECTION / SUBSECTION
        sub.mkdir()
        for name, content in PAGES.items():
            (sub / name).write_text(content, encoding="utf-8")
        (sub / ".nav.yml").write_text(NAV, encoding="utf-8")

        result = subprocess.run([zensical(), "build", "--strict"], cwd=tmp_root, capture_output=True, text=True)
        if result.returncode != 0:
            print(result.stdout + result.stderr)
            problems.append(f"build strict fallito (exit {result.returncode})")
        else:
            if digest(config_files) != before:
                problems.append("mkdocs.yml o un .nav.yml esistente risultano modificati")
            page = tmp_root / "site" / SECTION / "index.html"
            items = top_level_items(primary_nav(page.read_text(encoding="utf-8")))
            active = [i for i in items if "md-nav__item--active" in i.classes()]
            if len(active) != 1:
                problems.append(f"{len(active)} sezioni attive nella sidebar invece di 1")
            else:
                links = [h for h in hrefs(active[0]) if SUBSECTION in h]
                texts = " ".join(active[0].texts())
                if not links:
                    problems.append(f"la sidebar di {SECTION}/ non contiene la sottosezione {SUBSECTION}/")
                elif not (links[0].endswith("seconda/") and any(h.endswith("prima/") for h in links)):
                    problems.append(f"ordine delle pagine della sottosezione non rispettato: {links}")
                if TITLE not in texts:
                    problems.append(f"il titolo {TITLE!r} dichiarato nel .nav.yml della sottosezione non compare")
                print(f"Sidebar di {SECTION}/: link della sottosezione {links}")

    if problems:
        print("Controllo sottosezione nuova: FALLITO")
        for p in problems:
            print(f"  - {p}")
        return 1
    print("Controllo sottosezione nuova: OK (compare con titolo e ordine del proprio .nav.yml, "
          "configurazione invariata)")
    return 0


if __name__ == "__main__":
    sys.exit(main())
