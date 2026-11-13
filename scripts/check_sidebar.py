#!/usr/bin/env python3
"""Controlla che la sidebar mostri solo le pagine della sezione corrente (scenario *Large section*).

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

    def classes(self) -> list[str]:
        return (self.attrs.get("class") or "").split()

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
    if problems:
        raise SystemExit("Controllo sidebar: FALLITO\n  - " + "\n  - ".join(problems))
    print("Controllo sidebar: OK (la sezione attiva contiene solo le pagine della sezione corrente)")


if __name__ == "__main__":
    check(Path(sys.argv[1]) if len(sys.argv) > 1 else Path(__file__).resolve().parent.parent / "spike" / "site")
