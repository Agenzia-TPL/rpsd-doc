#!/usr/bin/env python3
"""Pagine dei profili NeTEx e SIRI dal bundle di rpsd-tools (capability profile-docs).

Legge il bundle `site.yaml` scritto da `rpsd-tools profile-docs generate` (schema
`contracts/profile-data.schema.json` di rpsd-tools), applica i template Jinja di
templates/profili/ e sostituisce per intero la cartella della versione.

La struttura delle pagine sta nei template; qui ci sono solo il caricamento, i filtri
di formattazione delle celle (stessa resa del Markdown di riferimento di rpsd-tools)
e la scrittura. L'output dipende solo dal bundle: nessuna data, ordine delle liste.

Uso:
  python scripts/generate_profile_pages.py <bundle> <cartella> [--check]
  python scripts/generate_profile_pages.py --all [--check]
      ogni data/profili/<profilo>/<versione>/site.yaml → docs/<profilo>/<versione>/

Con --check non scrive: confronta e esce con 1 se una cartella non corrisponde.
"""
from __future__ import annotations

import argparse
import re
import shutil
import sys
from pathlib import Path

import yaml
from jinja2 import Environment, FileSystemLoader, StrictUndefined

ROOT = Path(__file__).resolve().parent.parent
TEMPLATES = ROOT / "templates" / "profili"
DATA = ROOT / "data" / "profili"
DOCS = ROOT / "docs"

MARKER = "GENERATED — DO NOT EDIT"
ENUMERATIONS = "enumerations.md"
ISSUES = "issues.md"
COMMON_FILE = "common.md"
IDENTIFICATION = "identificazione"

REQUIRED = ("profile", "title", "xsd", "guidelines", "generator", "pages")


class BundleError(Exception):
    pass


# ----------------------------------------------------------------------- formattazione


def cell(text) -> str:
    if not text:
        return ""
    return re.sub(r"\s+", " ", str(text)).replace("|", "\\|").strip()


def code(text) -> str:
    return f"`{text}`"


def source(s: dict) -> str:
    occ = s.get("occurrence", 1)
    occurrence = f" (occorrenza {occ})" if occ > 1 else ""
    return f"§{s['section']}, Tab. {s['table']}{occurrence}"


class Formatter:
    """Celle delle tabelle; replica rpsd_core.profile_docs.render di rpsd-tools."""

    def __init__(self, data: dict):
        self.data = data
        self.file_of = {p["id"]: p["file"] for p in data["pages"]}
        self.enumerations = {
            e["name"]: e["anchor"] for e in data.get("enumerations", []) if e.get("anchor")
        }
        self.issue_of: dict[str, str] = {}
        for issue in data.get("issues", []):
            self.issue_of.setdefault(issue["path"], issue["id"])
        self.table_title = {
            (p["id"], t["anchor"]): t["title"] for p in data["pages"] for t in p.get("tables", [])
        }

    def href(self, page: dict, link: dict) -> str:
        if link["page"] == page["id"]:
            return f"#{link['anchor']}"
        return f"{self.file_of[link['page']]}#{link['anchor']}"

    def field(self, row: dict, page: dict) -> str:
        name = code(row["field"])
        link = row.get("link")
        if link is None:
            return name
        if link.get("kind") == "ref":
            target = link["anchor"].rpartition("-")[2] or link["anchor"]
            title = self.table_title.get((link["page"], link["anchor"]))
            if title is not None:
                target = title.rpartition(" / ")[2]
            return f"{name} → [{target}]({self.href(page, link)})"
        return f"[{name}]({self.href(page, link)})"

    def type(self, type_name, enumeration=None, values=None) -> str:
        if enumeration and enumeration in self.enumerations:
            return f"[{code(enumeration)}]({ENUMERATIONS}#{self.enumerations[enumeration]})"
        text = code(type_name) if type_name else ""
        if values:
            listed = ", ".join(code(v) for v in values)
            text = f"{text}: {listed}" if text else listed
        return text

    def meaning(self, row: dict) -> str:
        note = row.get("note")
        if note is None:
            return ""
        parts = []
        if row.get("common_meaning"):
            parts.append(
                f"{row['common_meaning'].strip()} [→ Identificazione]({COMMON_FILE}#{IDENTIFICATION})"
            )
        elif note.get("meaning"):
            parts.append(note["meaning"].strip())
        if note.get("values"):
            parts.append("Valori del profilo: " + ", ".join(code(v) for v in note["values"]) + ".")
        if note.get("issues"):
            parts.append(f"[⚠ Incongruenza]({ISSUES}#{self.issue_of.get(note['path'], '')})")
        return " ".join(parts)

    def example(self, row: dict) -> str:
        example = row.get("example")
        if example is None:
            return ""
        text = code(example["value"])
        if example.get("file"):
            text += f" *({example['file'].rpartition('/')[2]})*"
        return text

    def card(self, row: dict) -> str:
        return row["card"] + (f" · scelta {row['choice']}" if row.get("choice") else "")

    def sources(self, row: dict) -> str:
        note = row.get("note")
        return ", ".join(source(s) for s in note["sources"]) if note else ""

    def table_facts(self, table: dict) -> str:
        if table.get("group") is not None:
            facts = [table["description"].rstrip(".")] if table.get("description") else []
        else:
            first = f"Linee guida §{table['section']}"
            if table.get("section_title"):
                first += f" «{table['section_title']}»"
            facts = [first + f", Tabella {table['table']}"]
        if table.get("xsd_type"):
            facts.append(f"Tipo dell'XSD {code(table['xsd_type'])}")
        return ". ".join(facts) + "."

    def issue_sources(self, issue: dict) -> str:
        return ", ".join(f"{source(s)}, {code(s['field'])}" for s in issue["sources"])


def nav_yaml(data: dict) -> str:
    entries = [{p["title"]: p["file"]} for p in data["pages"]]
    entries += [{"Enumerazioni": ENUMERATIONS}, {"Incongruenze": ISSUES}]
    return yaml.safe_dump({"nav": entries}, allow_unicode=True, sort_keys=False, width=100)


# ----------------------------------------------------------------------- generazione


def load_bundle(path: Path) -> dict:
    try:
        data = yaml.safe_load(path.read_text(encoding="utf-8"))
    except (OSError, yaml.YAMLError) as exc:
        raise BundleError(f"{path}: bundle non leggibile ({exc})") from exc
    if not isinstance(data, dict):
        raise BundleError(f"{path}: il bundle non è un oggetto YAML")
    missing = [k for k in REQUIRED if k not in data]
    if missing:
        raise BundleError(f"{path}: chiavi mancanti nel bundle: {', '.join(missing)}")
    return data


def environment() -> Environment:
    return Environment(
        loader=FileSystemLoader(str(TEMPLATES)),
        undefined=StrictUndefined,
        keep_trailing_newline=True,
        autoescape=False,
        trim_blocks=True,
        lstrip_blocks=True,
    )


def render(data: dict) -> dict[str, str]:
    """Nome file → contenuto, in ordine di nome."""
    env = environment()
    fmt = Formatter(data)
    comment = f"{MARKER} · profile-docs {data['profile']} · {data['xsd']}"
    ctx = dict(data=data, fmt=fmt, comment=comment, cell=cell, code=code)
    env.filters.update(cell=cell, code=code)

    def page_of(name: str, **extra) -> str:
        text = env.get_template(name).render(**ctx, **extra)
        # stessa normalizzazione del riferimento: niente righe vuote in coda
        return text.rstrip() + "\n"

    by_kind = {"overview": "index.md.j2", "common": "comuni.md.j2"}
    files = {
        ".nav.yml": env.get_template("nav.yml.j2").render(comment=comment, body=nav_yaml(data)),
        ENUMERATIONS: page_of("enumerazioni.md.j2"),
        ISSUES: page_of("incongruenze.md.j2"),
    }
    for page in data["pages"]:
        files[page["file"]] = page_of(by_kind.get(page["kind"], "pagina.md.j2"), page=page)
    return dict(sorted(files.items()))


def compare(files: dict[str, str], out: Path) -> list[str]:
    problems = []
    existing = {p.name for p in out.iterdir() if p.is_file()} if out.is_dir() else set()
    for name, content in files.items():
        target = out / name
        if name not in existing:
            problems.append(f"{target}: manca")
        elif target.read_text(encoding="utf-8") != content:
            problems.append(f"{target}: diverso dal bundle")
    for name in sorted(existing - files.keys()):
        problems.append(f"{out / name}: in più, non prodotto dal bundle")
    if out.is_dir() and any(p.is_dir() for p in out.iterdir()):
        problems.append(f"{out}: contiene sottocartelle non prodotte dal bundle")
    return problems


def write(files: dict[str, str], out: Path) -> None:
    if out.exists():
        shutil.rmtree(out)
    out.mkdir(parents=True)
    for name, content in files.items():
        (out / name).write_text(content, encoding="utf-8", newline="\n")


def all_pairs() -> list[tuple[Path, Path]]:
    pairs = []
    for bundle in sorted(DATA.glob("*/*/site.yaml")):
        profile, version = bundle.parent.parent.name, bundle.parent.name
        pairs.append((bundle, DOCS / profile / version))
    return pairs


def main(argv=None) -> int:
    parser = argparse.ArgumentParser(description=__doc__.split("\n")[0])
    parser.add_argument("bundle", nargs="?", type=Path)
    parser.add_argument("out", nargs="?", type=Path)
    parser.add_argument("--all", action="store_true", help="tutti i bundle di data/profili/")
    parser.add_argument("--check", action="store_true", help="confronta senza scrivere")
    args = parser.parse_args(argv)

    if args.all == bool(args.bundle):
        parser.error("indicare <bundle> <cartella> oppure --all")
    if args.bundle and not args.out:
        parser.error("manca la cartella di destinazione")
    pairs = all_pairs() if args.all else [(args.bundle, args.out)]
    if args.all and not pairs:
        print(f"nessun bundle in {DATA}", file=sys.stderr)
        return 1

    problems = []
    if args.all:
        # una cartella di versione con pagine generate ma senza bundle è un errore (D3)
        covered = {out for _, out in pairs}
        for profile in sorted({b.parent.parent.name for b, _ in pairs}):
            for folder in sorted((DOCS / profile).glob("*/")):
                if folder.is_dir() and folder not in covered:
                    problems.append(f"{folder}: cartella di versione senza bundle in {DATA}")
    for bundle, out in pairs:
        try:
            files = render(load_bundle(bundle))
        except BundleError as exc:
            problems.append(str(exc))
            continue
        if args.check:
            found = compare(files, out)
            problems += found
            if not found:
                print(f"OK {out}")
        else:
            write(files, out)
            print(f"scritto {out} ({len(files)} file)")

    for p in problems:
        print(f"ERRORE {p}", file=sys.stderr)
    if problems and args.check:
        print(
            "Le pagine dei profili si rigenerano dal bundle: "
            "python scripts/generate_profile_pages.py --all",
            file=sys.stderr,
        )
    return 1 if problems else 0


if __name__ == "__main__":
    sys.exit(main())
