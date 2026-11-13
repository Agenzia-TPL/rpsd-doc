#!/usr/bin/env python3
"""Verifica che nessun URL pubblicato sparisca (scenario *Page moved*, requisito Stable URLs).

Costruisce il sito della revisione BASE (sulle PR: il branch di destinazione, cioè ciò che è
pubblicato) e quello della copia corrente, ciascuno in una directory temporanea, e confronta
gli URL delle pagine servite. Ogni URL di BASE deve esistere anche nella copia corrente,
come pagina o come redirect (plugin `redirects`, `redirect_maps` in mkdocs.yml).

Uso: python scripts/check_urls.py BASE [--root DIR]
"""
from __future__ import annotations

import argparse
import io
import shutil
import subprocess
import sys
import tarfile
import tempfile
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT / "scripts"))
from spike import zensical  # noqa: E402

SOURCES = ["mkdocs.yml", "docs"]


def served_urls(site: Path) -> set[str]:
    """URL relativi delle pagine HTML servite (esclusa la pagina 404)."""
    urls = set()
    for page in site.rglob("*.html"):
        rel = page.relative_to(site).as_posix()
        if rel == "404.html":
            continue
        urls.add(rel[: -len("index.html")] if rel.endswith("index.html") else rel)
    return urls


def build(source: Path, strict: bool) -> tuple[set[str], str]:
    cmd = [zensical(), "build"] + (["--strict"] if strict else [])
    result = subprocess.run(cmd, cwd=source, capture_output=True, text=True)
    if result.returncode != 0:
        raise RuntimeError(result.stdout + result.stderr)
    return served_urls(source / "site"), result.stdout


def export_revision(root: Path, rev: str, dest: Path) -> None:
    data = subprocess.run(["git", "archive", "--format=tar", rev, *SOURCES], cwd=root,
                          capture_output=True, check=True).stdout
    with tarfile.open(fileobj=io.BytesIO(data)) as tar:
        tar.extractall(dest, filter="data")


def copy_worktree(root: Path, dest: Path) -> None:
    shutil.copy(root / "mkdocs.yml", dest / "mkdocs.yml")
    shutil.copytree(root / "docs", dest / "docs")


def compare(base_urls: set[str], head_urls: set[str]) -> list[str]:
    return sorted(base_urls - head_urls)


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument("base", help="revisione di riferimento, es. origin/main")
    parser.add_argument("--root", type=Path, default=ROOT)
    args = parser.parse_args()
    root = args.root.resolve()

    with tempfile.TemporaryDirectory() as tmp:
        base_dir, head_dir = Path(tmp) / "base", Path(tmp) / "head"
        base_dir.mkdir()
        head_dir.mkdir()
        try:
            export_revision(root, args.base, base_dir)
        except subprocess.CalledProcessError as exc:
            print(f"Controllo URL: impossibile leggere la revisione {args.base!r}: {exc.stderr.decode().strip()}")
            return 1
        copy_worktree(root, head_dir)
        base_urls, _ = build(base_dir, strict=False)
        head_urls, _ = build(head_dir, strict=True)

    lost = compare(base_urls, head_urls)
    print(f"URL in {args.base}: {len(base_urls)}; nella copia corrente: {len(head_urls)}")
    if lost:
        print("Controllo URL: FALLITO — URL pubblicati non più serviti:")
        for url in lost:
            print(f"  - /{url}")
        print("Se la pagina è stata spostata o rinominata, aggiungere in mkdocs.yml, sotto "
              "plugins → redirects → redirect_maps, una voce 'vecchio/percorso.md: nuovo/percorso.md'.")
        return 1
    print("Controllo URL: OK (ogni URL pubblicato è ancora servito, come pagina o come redirect)")
    return 0


if __name__ == "__main__":
    sys.exit(main())
