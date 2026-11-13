#!/usr/bin/env python3
"""Genera 400 pagine sintetiche deterministiche in spike/docs/scala/ (scenario *Large section*).

Contenuto neutro e non normativo: serve solo a misurare tempo di build e resa della
sidebar. La cartella viene ricreata a ogni esecuzione ed è ignorata da git.
"""
from __future__ import annotations

import shutil
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
TARGET = ROOT / "spike" / "docs" / "scala"
COUNT = 400

PARAGRAPH = (
    "Pagina sintetica generata per la prova di scala. Il testo è volutamente "
    "ripetitivo e non ha valore documentale: serve a dare a ogni pagina un "
    "volume paragonabile a quello di una pagina generata reale."
)


def page(i: int) -> str:
    prev_link = f"[Pagina precedente](pagina-{i - 1:03d}.md)" if i > 1 else ""
    next_link = f"[Pagina successiva](pagina-{i + 1:03d}.md)" if i < COUNT else ""
    rows = "\n".join(f"| campo-{k} | testo | {'sì' if k % 2 else 'no'} | valore {i}-{k} |" for k in range(1, 9))
    return f"""# Pagina di scala {i:03d}

!!! warning "Pagina di prova generata — contenuto non normativo"

{PARAGRAPH}

## Tabella

| Campo | Tipo | Obbligatorio | Esempio |
|---|---|---|---|
{rows}

## Codice

``` xml
<Esempio numero="{i}">
  <Nome>pagina {i:03d}</Nome>
</Esempio>
```

## Testo

{PARAGRAPH} {PARAGRAPH}

{prev_link} {next_link}
"""


def generate() -> int:
    if TARGET.exists():
        shutil.rmtree(TARGET)
    TARGET.mkdir(parents=True)
    (TARGET / "index.md").write_text("# Scala\n\nSezione di 400 pagine generate per la prova di scala.\n", encoding="utf-8")
    for i in range(1, COUNT + 1):
        (TARGET / f"pagina-{i:03d}.md").write_text(page(i), encoding="utf-8")
    return COUNT


if __name__ == "__main__":
    print(f"{generate()} pagine generate in {TARGET.relative_to(ROOT)}")
