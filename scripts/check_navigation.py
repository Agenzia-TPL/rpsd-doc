#!/usr/bin/env python3
"""Controlla i tab di primo livello del sito costruito (scenario *Reader on any page*).

Per la home e per la pagina indice di ogni sezione verifica che:
- i tab siano esattamente Home, NeTEx, SIRI, Indicatori, Guida operativa, in quest'ordine;
- ci sia un solo tab attivo e sia quello della sezione della pagina.

Uso: python scripts/check_navigation.py [site]
"""
from __future__ import annotations

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from check_sidebar import Node, TreeBuilder  # noqa: E402

EXPECTED_TABS = ["Home", "NeTEx", "SIRI", "Indicatori", "Guida operativa"]

# pagina (relativa a site/) -> tab che deve risultare attivo
PAGES = {
    "index.html": "Home",
    "netex/index.html": "NeTEx",
    "siri/index.html": "SIRI",
    "indicatori/index.html": "Indicatori",
    "guida/index.html": "Guida operativa",
}


def text(node: Node) -> str:
    return " ".join(node.texts()).strip()


def tabs(html: str) -> list[tuple[str, bool]]:
    builder = TreeBuilder()
    builder.feed(html)
    items = [n for n in builder.root.iter() if n.tag == "li" and "md-tabs__item" in n.classes()]
    if not items:
        raise SystemExit("Tab di primo livello non trovati nell'HTML: struttura del tema cambiata?")
    return [(text(li), "md-tabs__item--active" in li.classes()) for li in items]


def check(site: Path) -> int:
    problems = []
    for rel, expected_active in PAGES.items():
        page = site / rel
        if not page.exists():
            problems.append(f"{rel}: pagina assente")
            continue
        found = tabs(page.read_text(encoding="utf-8"))
        labels = [label for label, _ in found]
        active = [label for label, is_active in found if is_active]
        if labels != EXPECTED_TABS:
            problems.append(f"{rel}: tab {labels}, attesi {EXPECTED_TABS}")
        if active != [expected_active]:
            problems.append(f"{rel}: tab attivi {active}, atteso [{expected_active!r}]")
        print(f"{rel}: tab {labels}, attivo {active}")
    if problems:
        print("Controllo tab: FALLITO")
        for p in problems:
            print(f"  - {p}")
        return 1
    print("Controllo tab: OK (cinque tab nell'ordine richiesto, tab attivo corretto su ogni pagina)")
    return 0


if __name__ == "__main__":
    root = Path(__file__).resolve().parent.parent
    sys.exit(check(Path(sys.argv[1]) if len(sys.argv) > 1 else root / "site"))
