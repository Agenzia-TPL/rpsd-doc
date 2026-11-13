#!/usr/bin/env python3
"""Controlli sulle convenzioni di contenuto (capability content-conventions).

Regole (design del change add-content-conventions):
  G1  ogni pagina sotto un percorso generato dichiara `generato: true` e `generato_da`
  G2  ogni pagina con `generato: true` sta sotto un percorso generato
  G3  (con --commits BASE) ogni commit non di merge in BASE..HEAD che tocca un percorso
      generato ha il trailer "Generato-da: rpsd-tools <versione>"
  L1  le pagine redazionali non superano 1500 parole
  C1  i callout usano solo i tipi ammessi; danger e info solo con i titoli riservati
  S1  al primo uso in una pagina, ogni sigla del glossario è un link alla sua voce
      (esclusi titoli, titoli dei callout e codice)

I percorsi generati sono in generated-paths.txt.

Uso: python scripts/check_conventions.py [--commits BASE] [--root DIR]
"""
from __future__ import annotations

import argparse
import re
import subprocess
import sys
from dataclasses import dataclass
from pathlib import Path

MAX_WORDS = 1500
GLOSSARY = "docs/panoramica/glossario.md"
TRAILER = "Generato-da"
GENERATOR = "rpsd-tools"

FREE_CALLOUTS = {"note", "tip", "warning", "example"}
RESERVED_CALLOUTS = {"danger": "Obbligatorio per KPI", "info": "Novità Rapsodia"}


# --------------------------------------------------------------------------- utilità


def load_generated_paths(root: Path) -> list[str]:
    """Prefissi (relativi alla radice, con / finale) delle cartelle generate."""
    paths = []
    for line in (root / "generated-paths.txt").read_text(encoding="utf-8").splitlines():
        line = line.split("#", 1)[0].strip()
        if line:
            paths.append(line if line.endswith("/") else line + "/")
    return paths


def is_generated(rel: str, prefixes: list[str]) -> bool:
    return any(rel.startswith(p) for p in prefixes)


def pages(root: Path) -> list[tuple[str, str]]:
    """(percorso relativo alla radice, testo) di ogni pagina .md sotto docs/."""
    return [(p.relative_to(root).as_posix(), p.read_text(encoding="utf-8"))
            for p in sorted((root / "docs").rglob("*.md"))]


def split_front_matter(text: str) -> tuple[dict[str, str], str, int]:
    """Front matter (chiave: valore scalari), corpo, numero di righe del front matter."""
    lines = text.splitlines(keepends=True)
    if not lines or lines[0].strip() != "---":
        return {}, text, 0
    for i in range(1, len(lines)):
        if lines[i].strip() in ("---", "..."):
            meta = {}
            for raw in lines[1:i]:
                if ":" in raw and not raw.startswith((" ", "\t", "#")):
                    key, value = raw.split(":", 1)
                    meta[key.strip()] = value.strip().strip("'\"")
            return meta, "".join(lines[i + 1:]), i + 1
    return {}, text, 0


FENCE = re.compile(r"^\s*(`{3,}|~{3,})")


def mask_code_blocks(body: str) -> list[str]:
    """Righe del corpo con i blocchi di codice recintati sostituiti da righe vuote."""
    out, fence = [], None
    for line in body.splitlines():
        m = FENCE.match(line)
        if fence is None:
            if m:
                fence = m.group(1)
                out.append("")
            else:
                out.append(line)
        else:
            if m and m.group(1)[0] == fence[0] and len(m.group(1)) >= len(fence) and line.strip() == m.group(1):
                fence = None
            out.append("")
    return out


@dataclass
class Problem:
    rule: str
    where: str
    message: str

    def __str__(self) -> str:
        return f"[{self.rule}] {self.where}: {self.message}"


# --------------------------------------------------------------------------- G1, G2


def check_generated_pages(root: Path) -> list[Problem]:
    prefixes = load_generated_paths(root)
    problems = []
    for rel, text in pages(root):
        meta, _, _ = split_front_matter(text)
        declared = meta.get("generato", "").lower() == "true"
        if is_generated(rel, prefixes):
            if not declared or not meta.get("generato_da"):
                problems.append(Problem("G1", rel, "pagina in una cartella generata senza `generato: true` "
                                                   "e `generato_da` nel front matter"))
        elif declared:
            problems.append(Problem("G2", rel, "pagina dichiarata generata fuori dalle cartelle generate "
                                               "(generated-paths.txt): una pagina è redazionale o generata, mai mista"))
    return problems


# --------------------------------------------------------------------------- G3


def git(root: Path, *args: str) -> str:
    return subprocess.run(["git", *args], cwd=root, capture_output=True, text=True, check=True).stdout


def check_commits(root: Path, base: str) -> list[Problem]:
    prefixes = load_generated_paths(root)
    try:
        git(root, "rev-parse", "--verify", f"{base}^{{commit}}")
    except subprocess.CalledProcessError:
        return [Problem("G3", base, "riferimento base non trovato (serve la cronologia completa: fetch-depth 0)")]
    shas = git(root, "log", "--no-merges", "--format=%H", f"{base}..HEAD", "--", *prefixes).split()
    problems = []
    for sha in shas:
        trailer = git(root, "log", "-1", f"--format=%(trailers:key={TRAILER},valueonly)", sha).strip()
        if trailer.startswith(GENERATOR):
            continue
        files = git(root, "diff-tree", "--no-commit-id", "--name-only", "-r", sha, "--", *prefixes).split()
        subject = git(root, "log", "-1", "--format=%s", sha).strip()
        problems.append(Problem(
            "G3", f"commit {sha[:7]} \"{subject}\"",
            f"modifica a mano file generati ({', '.join(files)}). Le pagine generate non si modificano: "
            f"cambiare i dati sorgente in data/ (o i template) e rigenerare con {GENERATOR}, "
            f"che aggiunge il trailer \"{TRAILER}: {GENERATOR} <versione>\""))
    return problems


# --------------------------------------------------------------------------- L1

HTML_COMMENT = re.compile(r"<!--.*?-->", re.S)
LINK_URL = re.compile(r"\]\([^)]*\)")
ATTR_LIST = re.compile(r"\{[^}]*\}")
CALLOUT_TYPE = re.compile(r"^(\s*)(?:!!!|\?\?\?\+?)\s+[\w-]+(?:\s+[\w-]+)*")
WORD = re.compile(r"[^\W_]+(?:['’][^\W_]+)*")


def count_words(text: str) -> int:
    _, body, _ = split_front_matter(text)
    prose = "\n".join(mask_code_blocks(HTML_COMMENT.sub(" ", body)))
    prose = LINK_URL.sub("]", prose)
    prose = ATTR_LIST.sub(" ", prose)
    prose = "\n".join(CALLOUT_TYPE.sub(r"\1", line) for line in prose.splitlines())
    return len(WORD.findall(prose))


def check_length(root: Path, report: list[str] | None = None) -> list[Problem]:
    prefixes = load_generated_paths(root)
    problems = []
    for rel, text in pages(root):
        if is_generated(rel, prefixes):
            continue
        words = count_words(text)
        if report is not None:
            report.append(f"{rel}: {words} parole")
        if words > MAX_WORDS:
            problems.append(Problem("L1", rel, f"{words} parole, oltre il limite di {MAX_WORDS}: "
                                               "dividere la pagina"))
    return problems


# --------------------------------------------------------------------------- C1

CALLOUT = re.compile(r'^\s*(?:!!!|\?\?\?\+?)\s+([\w-]+)((?:\s+[\w-]+)*)\s*(?:"([^"]*)")?\s*$')


def check_callouts(root: Path) -> list[Problem]:
    problems = []
    for rel, text in pages(root):
        _, body, offset = split_front_matter(text)
        for n, line in enumerate(mask_code_blocks(body), start=offset + 1):
            m = CALLOUT.match(line)
            if not m:
                continue
            kind, title = m.group(1), m.group(3)
            where = f"{rel}:{n}"
            if kind in RESERVED_CALLOUTS:
                if title != RESERVED_CALLOUTS[kind]:
                    problems.append(Problem("C1", where, f"il callout `{kind}` si usa solo con il titolo "
                                                         f"\"{RESERVED_CALLOUTS[kind]}\" (trovato: {title!r})"))
            elif kind in FREE_CALLOUTS:
                for reserved_kind, reserved_title in RESERVED_CALLOUTS.items():
                    if title == reserved_title:
                        problems.append(Problem("C1", where, f"il titolo \"{reserved_title}\" è riservato al "
                                                             f"callout `{reserved_kind}`"))
            else:
                allowed = ", ".join(sorted(FREE_CALLOUTS | set(RESERVED_CALLOUTS)))
                problems.append(Problem("C1", where, f"tipo di callout `{kind}` non ammesso (ammessi: {allowed})"))
    return problems


# --------------------------------------------------------------------------- S1

GLOSSARY_ENTRY = re.compile(r"^#{1,6}\s+(.+?)\s*\{([^}]*)\}\s*$")
HEADING = re.compile(r"^\s{0,3}#{1,6}\s")
INLINE_CODE = re.compile(r"`+[^`]*`+")
LINK = re.compile(r"\[([^\]]*)\]\(([^)\s]+)(?:\s+\"[^\"]*\")?\)")


def glossary_terms(root: Path) -> list[tuple[str, str]] | None:
    """(sigla, anchor) delle voci marcate .sigla; None se il glossario non esiste."""
    path = root / GLOSSARY
    if not path.exists():
        return None
    terms = []
    for line in mask_code_blocks(split_front_matter(path.read_text(encoding="utf-8"))[1]):
        m = GLOSSARY_ENTRY.match(line)
        if not m:
            continue
        attrs = m.group(2).split()
        anchor = next((a[1:] for a in attrs if a.startswith("#")), None)
        if ".sigla" in attrs and anchor:
            terms.append((m.group(1).strip(), anchor))
    return terms


def check_glossary(root: Path, notes: list[str] | None = None) -> list[Problem]:
    terms = glossary_terms(root)
    if terms is None:
        if notes is not None:
            notes.append(f"glossario {GLOSSARY} assente: nessuna sigla da controllare")
        return []
    if notes is not None:
        notes.append(f"glossario: {len(terms)} sigle ({', '.join(t for t, _ in terms) or 'nessuna'})")
    problems = []
    for rel, text in pages(root):
        if rel == GLOSSARY:
            continue
        _, body, offset = split_front_matter(text)
        # Titoli di pagina e righe di apertura dei callout esclusi: lì un link non viene reso.
        lines = ["" if HEADING.match(line) or CALLOUT.match(line)
                 else INLINE_CODE.sub(lambda m: " " * len(m.group(0)), line)
                 for line in mask_code_blocks(body)]
        prose = "\n".join(lines)
        links = [(m.start(1), m.end(1), m.start(2), m.end(2), m.group(2)) for m in LINK.finditer(prose)]
        for term, anchor in terms:
            target = re.compile(r"glossario(?:\.md|/|/index\.md)?#" + re.escape(anchor) + r"$")
            for occ in re.finditer(r"(?<!\w)" + re.escape(term) + r"(?!\w)", prose):
                pos = occ.start()
                if any(us <= pos < ue for _, _, us, ue, _ in links):
                    continue  # occorrenza dentro un URL, non nel testo
                link = next((lk for lk in links if lk[0] <= pos < lk[1]), None)
                if link is None or not target.search(link[4]):
                    line_no = prose.count("\n", 0, pos) + offset + 1
                    problems.append(Problem("S1", f"{rel}:{line_no}", f"primo uso della sigla \"{term}\" non "
                                                                      f"linkato alla voce del glossario "
                                                                      f"(…/glossario.md#{anchor})"))
                break
    return problems


# --------------------------------------------------------------------------- main


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument("--commits", metavar="BASE", help="controlla anche i commit BASE..HEAD (regola G3)")
    parser.add_argument("--root", type=Path, default=Path(__file__).resolve().parent.parent)
    parser.add_argument("--verbose", action="store_true", help="stampa il conteggio parole di ogni pagina")
    args = parser.parse_args()
    root = args.root.resolve()

    lengths: list[str] = []
    notes: list[str] = []
    results = {
        "pagine generate (G1, G2)": check_generated_pages(root),
        "lunghezza (L1)": check_length(root, lengths),
        "callout (C1)": check_callouts(root),
        "glossario (S1)": check_glossary(root, notes),
    }
    if args.commits:
        results[f"commit su cartelle generate (G3, {args.commits}..HEAD)"] = check_commits(root, args.commits)

    if args.verbose:
        print("\n".join(lengths))
    for note in notes:
        print(note)
    failed = False
    for name, problems in results.items():
        print(f"{name}: {'OK' if not problems else f'{len(problems)} problemi'}")
        for p in problems:
            print(f"  - {p}")
        failed |= bool(problems)
    print("Controllo convenzioni: " + ("FALLITO" if failed else "OK"))
    return 1 if failed else 0


if __name__ == "__main__":
    sys.exit(main())
