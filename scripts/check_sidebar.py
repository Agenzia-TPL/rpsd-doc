#!/usr/bin/env python3
"""Controlla la sidebar sullo spike costruito.

Scenari: *Large section* (site-platform) e *Deep page* (site-navigation).
La sidebar deve mostrare solo le pagine della sezione corrente.

Con navigation.tabs il tema inserisce nell'HTML la navigazione di tutte le sezioni
(serve al menu su mobile) e sulla sidebar desktop mostra solo la sezione attiva
(navigazione "lifted"). Il controllo verifica quindi, nella navigazione primaria:

- che la sezione di primo livello attiva sia quella della pagina e contenga le sue pagine;
- che i link alle pagine dell'altra sezione stiano solo dentro sezioni non attive.

Uso: python scripts/check_sidebar.py [spike/site]
"""
from __future__ import annotations

import sys
from html.parser import HTMLParser
from pathlib import Path

VOID = {"area", "base", "br", "col", "embed", "hr", "img", "input", "link", "meta", "source", "track", "wbr"}


class Node:
    def __init__(self, tag: str, attrs: dict[str, str], parent: "Node | None"):
        self.tag, self.attrs, self.parent, self.children = tag, attrs, parent, []
        self.data: list[str] = []

    def classes(self) -> list[str]:
        return (self.attrs.get("class") or "").split()

    def texts(self) -> list[str]:
        """Testo del nodo e dei discendenti, a frammenti non vuoti."""
        out = [d.strip() for d in self.data if d.strip()]
        for c in self.children:
            out.extend(c.texts())
        return out

    def iter(self):
        yield self
        for c in self.children:
            yield from c.iter()


class TreeBuilder(HTMLParser):
    def __init__(self):
        super().__init__()
        self.root = Node("root", {}, None)
        self.cur = self.root

    def handle_starttag(self, tag, attrs):
        node = Node(tag, dict(attrs), self.cur)
        self.cur.children.append(node)
        if tag not in VOID:
            self.cur = node

    def handle_data(self, data):
        self.cur.data.append(data)

    def handle_endtag(self, tag):
        n = self.cur
        while n is not None and n.tag != tag:
            n = n.parent
        if n is not None and n.parent is not None:
            self.cur = n.parent


def primary_nav(html: str) -> Node:
    builder = TreeBuilder()
    builder.feed(html)
    for n in builder.root.iter():
        if n.tag == "nav" and "md-nav--primary" in n.classes():
            return n
    raise SystemExit("Navigazione primaria non trovata nell'HTML: struttura del tema cambiata?")


def top_level_items(nav: Node) -> list[Node]:
    ul = next(c for c in nav.children if c.tag == "ul")
    return [c for c in ul.children if c.tag == "li"]


def hrefs(node: Node) -> list[str]:
    return [n.attrs["href"] for n in node.iter() if n.tag == "a" and "href" in n.attrs]


def check(site: Path) -> None:
    cases = [
        # pagina, link della propria sezione, link dell'altra sezione
        (site / "funzioni" / "xml-annotato" / "index.html", "diagrammi/", "scala/pagina-"),
        (site / "scala" / "pagina-200" / "index.html", "pagina-201", "funzioni/"),
    ]
    problems = []
    for page, own, other in cases:
        rel = page.relative_to(site)
        items = top_level_items(primary_nav(page.read_text(encoding="utf-8")))
        active = [i for i in items if "md-nav__item--active" in i.classes()]
        if len(active) != 1:
            problems.append(f"{rel}: {len(active)} sezioni attive invece di 1")
            continue
        active_links = hrefs(active[0])
        if not any(own in h for h in active_links):
            problems.append(f"{rel}: la sezione attiva non contiene le pagine della propria sezione")
        leaked = [h for h in active_links if other in h]
        if leaked:
            problems.append(f"{rel}: la sezione attiva contiene {len(leaked)} link all'altra sezione")
        hidden = sum(1 for i in items if i is not active[0] for h in hrefs(i) if other in h)
        print(f"Sidebar di {rel}: {len(active_links)} link nella sezione attiva, "
              f"{len(leaked)} fuori sezione; {hidden} link dell'altra sezione in sezioni non attive (non mostrate)")
    problems += check_deep(site)
    if problems:
        raise SystemExit("Controllo sidebar: FALLITO\n  - " + "\n  - ".join(problems))
    print("Controllo sidebar: OK (la sezione attiva contiene solo le pagine della sezione corrente; "
          "nella pagina profonda antenati espansi e ramo fratello chiuso)")


# Pagina a tre livelli dello spike (scenario *Deep page* di site-navigation):
# rami annidati attesi espansi (True) o chiusi (False) nella sua sidebar.
DEEP_PAGE = "navigazione/ramo-a/livello-2/pagina-profonda/index.html"
DEEP_EXPECTED = {"Navigazione": True, "Ramo A": True, "Livello 2": True, "Ramo B": False}


def check_deep(site: Path) -> list[str]:
    """Antenati della pagina profonda espansi, rami fratelli chiusi."""
    nav = primary_nav((site / DEEP_PAGE).read_text(encoding="utf-8"))
    labels = {n.attrs["id"]: " ".join(n.texts()) for n in nav.iter() if n.tag == "label" and "id" in n.attrs}
    state = {}
    for n in nav.iter():
        if n.tag == "nav" and "aria-labelledby" in n.attrs and "aria-expanded" in n.attrs:
            name = labels.get(n.attrs["aria-labelledby"], "")
            if not name:  # con navigation.indexes il nome sta nel titolo interno della nav
                title = next((c for c in n.children if c.tag == "label" and "md-nav__title" in c.classes()), None)
                name = " ".join(title.texts()) if title else "?"
            # Un gruppo reso come sezione (navigation.sections) è sempre visibile anche se
            # aria-expanded resta "false": va considerato aperto.
            as_section = n.parent is not None and "md-nav__item--section" in n.parent.classes()
            state[name] = n.attrs["aria-expanded"] == "true" or as_section
    print(f"Sidebar di {DEEP_PAGE}: " + ", ".join(f"{k} {'espanso' if v else 'chiuso'}" for k, v in state.items()))
    problems = []
    for name, expanded in DEEP_EXPECTED.items():
        if name not in state:
            problems.append(f"{DEEP_PAGE}: ramo {name!r} assente dalla sidebar")
        elif state[name] != expanded:
            problems.append(f"{DEEP_PAGE}: ramo {name!r} {'chiuso' if expanded else 'espanso'}, "
                            f"atteso {'espanso' if expanded else 'chiuso'}")
    return problems


if __name__ == "__main__":
    check(Path(sys.argv[1]) if len(sys.argv) > 1 else Path(__file__).resolve().parent.parent / "spike" / "site")
