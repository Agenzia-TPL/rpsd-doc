#!/usr/bin/env python3
"""Build delle pagine di prova dello spike (spike/), con la configurazione del sito.

Uso:
    python scripts/spike.py            build strict di spike/
    python scripts/spike.py --scale    + 400 pagine generate, soglia di tempo, controllo sidebar

Può essere lanciato da qualsiasi directory.
"""
from __future__ import annotations

import argparse
import shutil
import subprocess
import sys
import time
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
SPIKE = ROOT / "spike"
SPIKE_CONFIG = SPIKE / "mkdocs.yml"
SCALE_LIMIT_S = 60.0  # limite concordato (proposal di bootstrap-site)


def zensical() -> str:
    """Eseguibile zensical: quello del .venv del repo se esiste, altrimenti dal PATH."""
    for candidate in (ROOT / ".venv" / "bin" / "zensical", ROOT / ".venv" / "Scripts" / "zensical.exe"):
        if candidate.exists():
            return str(candidate)
    found = shutil.which("zensical")
    if not found:
        sys.exit("zensical non trovato: attivare il .venv o installare requirements.txt")
    return found


def copy_assets() -> None:
    """Copia docs/assets/ in spike/docs/assets/ (percorsi di extra_javascript ereditati)."""
    target = SPIKE / "docs" / "assets"
    if target.exists():
        shutil.rmtree(target)
    shutil.copytree(ROOT / "docs" / "assets", target)


def build(clean: bool = False) -> float:
    cmd = [zensical(), "build", "--strict", "-f", str(SPIKE_CONFIG)]
    if clean:
        cmd.append("--clean")
    start = time.perf_counter()
    result = subprocess.run(cmd, cwd=ROOT)
    elapsed = time.perf_counter() - start
    if result.returncode != 0:
        sys.exit(f"Build strict dello spike fallito (exit {result.returncode})")
    return elapsed


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument("--scale", action="store_true", help="genera 400 pagine e verifica tempo e sidebar")
    args = parser.parse_args()

    copy_assets()
    if not args.scale:
        build()
        return

    sys.path.insert(0, str(ROOT / "scripts"))
    import gen_scale_pages  # noqa: E402
    import check_sidebar  # noqa: E402

    n = gen_scale_pages.generate()
    elapsed = build(clean=True)
    print(f"Scala: {n} pagine generate, build strict pulito in {elapsed:.1f} s (limite {SCALE_LIMIT_S:.0f} s)")
    if elapsed > SCALE_LIMIT_S:
        sys.exit(f"Tempo di build oltre il limite: {elapsed:.1f} s > {SCALE_LIMIT_S:.0f} s")
    check_sidebar.check(SPIKE / "site")


if __name__ == "__main__":
    main()
