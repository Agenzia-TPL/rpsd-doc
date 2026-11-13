#!/usr/bin/env python3
"""Verifica che il build strict fallisca su link interni rotti (scenario *Broken internal link*).

Copia lo spike in una directory temporanea, aggiunge due pagine rotte (link a una
pagina inesistente, link a un anchor inesistente), lancia il build strict e si
aspetta che fallisca nominando ogni pagina, la riga e il link. Termina con exit 0
solo se il comportamento è quello atteso.

Uso: python scripts/check_broken_link.py [--no-broken]
  --no-broken  controllo di sanità: senza pagine rotte lo script deve fallire
"""
from __future__ import annotations

import argparse
import re
import shutil
import subprocess
import sys
import tempfile
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT / "scripts"))
from spike import copy_assets, zensical  # noqa: E402

ANSI = re.compile(r"\x1b\[[0-9;]*m")

CASES = [
    # (file, contenuto, riga del link, link, messaggio atteso)
    ("rotto-pagina.md", "# Link a pagina inesistente\n\n[rotto](pagina-inesistente.md)\n",
     3, "pagina-inesistente.md", "page does not exist"),
    ("rotto-anchor.md", "# Link ad anchor inesistente\n\n[rotto](index.md#anchor-inesistente)\n",
     3, "anchor-inesistente", "anchor does not exist"),
]


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument("--no-broken", action="store_true", help="non aggiungere le pagine rotte")
    args = parser.parse_args()

    copy_assets()
    with tempfile.TemporaryDirectory() as tmp:
        tmp_root = Path(tmp)
        # Stessa struttura relativa dello spike: tmp/spike/{mkdocs.yml,docs}, tmp/mkdocs.yml
        shutil.copy(ROOT / "mkdocs.yml", tmp_root / "mkdocs.yml")
        spike = tmp_root / "spike"
        shutil.copytree(ROOT / "spike" / "docs", spike / "docs", ignore=shutil.ignore_patterns("scala"))
        shutil.copy(ROOT / "spike" / "mkdocs.yml", spike / "mkdocs.yml")
        if not args.no_broken:
            for name, content, *_ in CASES:
                (spike / "docs" / name).write_text(content, encoding="utf-8")

        result = subprocess.run(
            [zensical(), "build", "--strict", "-f", str(spike / "mkdocs.yml")],
            cwd=tmp_root, capture_output=True, text=True,
        )
    output = ANSI.sub("", result.stdout + result.stderr)

    problems = []
    if result.returncode == 0:
        problems.append("il build strict è riuscito, doveva fallire")
    for name, _, line, link, message in CASES:
        for expected in (f"{name}:{line}:", link, message):
            if expected not in output:
                problems.append(f"{name}: l'output non contiene {expected!r}")

    if problems:
        print("Controllo link rotti: FALLITO")
        for p in problems:
            print(f"  - {p}")
        print("--- output del build ---")
        print(output)
        return 1
    print(f"Controllo link rotti: OK (build strict fallito con exit {result.returncode}, "
          f"{len(CASES)} link rotti segnalati con pagina, riga e link)")
    return 0


if __name__ == "__main__":
    sys.exit(main())
