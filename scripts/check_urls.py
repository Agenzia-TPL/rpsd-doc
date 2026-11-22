#!/usr/bin/env python3
"""Verifica che nessun URL pubblicato sparisca (scenario *Page moved*, requisito Stable URLs).

Costruisce il sito della revisione BASE (sulle PR: il branch di destinazione, cioè ciò che è
pubblicato) e quello della copia corrente, ciascuno in una directory temporanea, e confronta
gli URL delle pagine servite. Ogni URL di BASE deve esistere anche nella copia corrente,
come pagina o come redirect (plugin `redirects`, `redirect_maps` in mkdocs.yml).

Eccezione (requisito Stable URLs): un URL la cui pagina in BASE è solo un segnaposto
(titolo e callout «Sezione in preparazione», nient'altro) può sparire senza redirect.

Uso: python scripts/check_urls.py BASE [--root DIR]
"""
from __future__ import annotations

import argparse
import io
import re
import subprocess
import sys
import tarfile
import tempfile
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT / "scripts"))
from spike import SITE_SOURCES, copy_site_sources, zensical  # noqa: E402

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
    """Estrae da rev i sorgenti del sito presenti in quella revisione."""
    present = subprocess.run(["git", "ls-tree", "--name-only", rev, *SITE_SOURCES], cwd=root,
                             capture_output=True, text=True, check=True).stdout.split()
    data = subprocess.run(["git", "archive", "--format=tar", rev, *present], cwd=root,
                          capture_output=True, check=True).stdout
    with tarfile.open(fileobj=io.BytesIO(data)) as tar:
        tar.extractall(dest, filter="data")


PLACEHOLDER_NOTE = re.compile(r'^!!!\s+note\s+"Sezione in preparazione"\s*$')


def strip_front_matter(text: str) -> str:
    lines = text.splitlines()
    if lines and lines[0].strip() == "---":
        for i in range(1, len(lines)):
            if lines[i].strip() in ("---", "..."):
                return "\n".join(lines[i + 1:])
    return text


def is_placeholder_text(text: str) -> bool:
    """Vero se la pagina contiene solo il titolo e il callout «Sezione in preparazione»."""
    lines = [line for line in strip_front_matter(text).splitlines() if line.strip()]
    if len(lines) < 2 or not lines[0].startswith("# ") or not PLACEHOLDER_NOTE.match(lines[1]):
        return False
    # dopo il callout solo il suo corpo, indentato
    return all(line.startswith(("    ", "\t")) for line in lines[2:])


def source_page(docs: Path, url: str) -> Path | None:
    """File Markdown di docs/ che produce l'URL (x/ → x.md oppure x/index.md)."""
    stem = url.rstrip("/")
    candidates = [docs / "index.md"] if not stem else [docs / f"{stem}.md", docs / stem / "index.md"]
    return next((c for c in candidates if c.is_file()), None)


def is_placeholder(docs: Path, url: str) -> bool:
    page = source_page(docs, url)
    return page is not None and is_placeholder_text(page.read_text(encoding="utf-8"))


def compare(base_urls: set[str], head_urls: set[str], base_docs: Path | None = None) -> tuple[list[str], list[str]]:
    """(URL persi, URL tolti perché segnaposto in BASE)."""
    missing = sorted(base_urls - head_urls)
    if base_docs is None:
        return missing, []
    placeholders = [u for u in missing if is_placeholder(base_docs, u)]
    return [u for u in missing if u not in placeholders], placeholders


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
        copy_site_sources(head_dir, root)
        base_urls, _ = build(base_dir, strict=False)
        head_urls, _ = build(head_dir, strict=True)
        lost, removed_placeholders = compare(base_urls, head_urls, base_dir / "docs")

    print(f"URL in {args.base}: {len(base_urls)}; nella copia corrente: {len(head_urls)}")
    for url in removed_placeholders:
        print(f"  segnaposto tolto, nessun redirect richiesto: /{url}")
    if lost:
        print("Controllo URL: FALLITO — URL pubblicati non più serviti:")
        for url in lost:
            print(f"  - /{url}")
        print("Se la pagina è stata spostata o rinominata, aggiungere in mkdocs.yml, sotto "
              "plugins → redirects → redirect_maps, una voce 'vecchio/percorso.md: nuovo/percorso.md'.")
        return 1
    print("Controllo URL: OK (ogni URL pubblicato è ancora servito, come pagina o come redirect, salvo i segnaposto tolti)")
    return 0


if __name__ == "__main__":
    sys.exit(main())
