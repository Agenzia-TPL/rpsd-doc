#!/usr/bin/env python3
"""Controlli sulle release del sito (capability site-releases).

Fonte: la tabella di docs/rapsodia/release.md («Release del sito»).

Regole (design del change add-site-releases, D3):
  R1  formato: intestazione | Versione | Data | Novità |; ogni riga ha versione **X.Y.Z**,
      data «G mmm AAAA» (mesi abbreviati in italiano) e novità non vuote
  R2  ordine: versioni strettamente decrescenti dall'alto, date non crescenti
  R3  home: marcatori `recenti` presenti, con dentro l'intestazione e le prime
      min(3, righe) righe della tabella
  R4  (con --tag vX.Y.Z) tag annotato, su un commit raggiungibile dal branch principale,
      e X.Y.Z è la prima riga della pagina nel commit del tag

Una tabella senza righe è valida (prima della prima release).

Uso: python scripts/check_release.py [--tag vX.Y.Z] [--main origin/main] [--root DIR]
"""
from __future__ import annotations

import argparse
import datetime
import re
import subprocess
import sys
from dataclasses import dataclass
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT / "scripts"))
from check_conventions import Problem  # noqa: E402

RELEASE = "docs/rapsodia/release.md"
RECENT = 3
HEADER = re.compile(r"^\|\s*Versione\s*\|\s*Data\s*\|\s*Novità\s*\|$")
SEPARATOR = re.compile(r"^\|(\s*:?-{3,}:?\s*\|){3}$")
ROW = re.compile(r"^\|(.*)\|(.*)\|(.*)\|$")
VERSION = re.compile(r"^\*\*(\d+)\.(\d+)\.(\d+)\*\*$")
DATE = re.compile(r"^(\d{1,2}) (\w{3}) (\d{4})$")
MONTHS = ["gen", "feb", "mar", "apr", "mag", "giu", "lug", "ago", "set", "ott", "nov", "dic"]
TAG = re.compile(r"^v(\d+\.\d+\.\d+)$")
START, END = "--8<-- [start:recenti]", "--8<-- [end:recenti]"


@dataclass
class Release:
    version: tuple[int, int, int]
    date: datetime.date | None
    line: int

    @property
    def label(self) -> str:
        return ".".join(map(str, self.version))


def parse(text: str) -> tuple[list[Release], list[Problem], list[str]]:
    """(release, problemi R1, righe della tabella con i marcatori) dal testo della pagina."""
    lines = text.splitlines()
    problems: list[Problem] = []
    header = next((i for i, line in enumerate(lines) if HEADER.match(line.strip())), None)
    if header is None:
        return [], [Problem("R1", RELEASE, "intestazione '| Versione | Data | Novità |' assente")], []
    if header + 1 >= len(lines) or not SEPARATOR.match(lines[header + 1].strip()):
        problems.append(Problem("R1", f"{RELEASE}:{header + 2}", "riga di separazione della tabella assente"))
    releases = []
    block = [lines[header - 1]] if header > 0 and START in lines[header - 1] else []
    block.append(lines[header])
    for i in range(header + 1, len(lines)):
        raw = lines[i].strip()
        if START in raw or END in raw:
            block.append(raw)
            continue
        if not raw.startswith("|"):
            break
        block.append(raw)
        if i == header + 1:
            continue  # separatore
        where = f"{RELEASE}:{i + 1}"
        m = ROW.match(raw)
        cells = [c.strip() for c in m.groups()] if m else []
        if len(cells) != 3:
            problems.append(Problem("R1", where, "la riga deve avere tre celle: versione, data, novità"))
            continue
        v = VERSION.match(cells[0])
        if not v:
            problems.append(Problem("R1", where, f"versione {cells[0]!r}: attesa **X.Y.Z**"))
            continue
        date = None
        d = DATE.match(cells[1])
        if d and d.group(2) in MONTHS:
            try:
                date = datetime.date(int(d.group(3)), MONTHS.index(d.group(2)) + 1, int(d.group(1)))
            except ValueError:
                pass
        if date is None:
            problems.append(Problem("R1", where, f"data {cells[1]!r}: attesa «G mmm AAAA», es. 22 nov 2026"))
        if not cells[2]:
            problems.append(Problem("R1", where, "novità vuote"))
        releases.append(Release(tuple(int(x) for x in v.groups()), date, i + 1))
    return releases, problems, block


def check_order(releases: list[Release]) -> list[Problem]:
    problems = []
    for prev, cur in zip(releases, releases[1:]):
        where = f"{RELEASE}:{cur.line}"
        if cur.version >= prev.version:
            problems.append(Problem("R2", where, f"versione {cur.label} non minore della precedente {prev.label}"))
        if prev.date and cur.date and cur.date > prev.date:
            problems.append(Problem("R2", where, f"data della {cur.label} successiva a quella della {prev.label}"))
    return problems


def check_recent(block: list[str]) -> list[Problem]:
    starts = [i for i, line in enumerate(block) if START in line]
    ends = [i for i, line in enumerate(block) if END in line]
    if len(starts) != 1 or len(ends) != 1 or starts[0] > ends[0]:
        return [Problem("R3", RELEASE, "servono un marcatore start:recenti prima dell'intestazione e uno "
                                       "end:recenti dentro la tabella")]
    inside = [line for line in block[starts[0] + 1:ends[0]] if line.startswith("|")]
    rows = len(inside) - 2  # intestazione e separatore
    total = len([line for line in block if line.startswith("|")]) - 2
    expected = min(RECENT, max(total, 0))
    if rows != expected or not inside or not HEADER.match(inside[0]):
        return [Problem("R3", RELEASE, f"fra i marcatori recenti devono esserci l'intestazione e le prime "
                                       f"{expected} righe della tabella (trovate {max(rows, 0)})")]
    return []


def git(root: Path, *args: str) -> subprocess.CompletedProcess:
    return subprocess.run(["git", *args], cwd=root, capture_output=True, text=True)


def check_tag(root: Path, tag: str, main: str) -> list[Problem]:
    m = TAG.match(tag)
    if not m:
        return [Problem("R4", tag, "il ref non è un tag di release vX.Y.Z")]
    if git(root, "cat-file", "-t", f"refs/tags/{tag}").stdout.strip() != "tag":
        return [Problem("R4", tag, "tag assente o non annotato (usare git tag -a)")]
    commit = git(root, "rev-list", "-n", "1", tag).stdout.strip()
    problems = []
    if git(root, "merge-base", "--is-ancestor", commit, main).returncode != 0:
        problems.append(Problem("R4", tag, f"il commit {commit[:7]} non è su {main}"))
    shown = git(root, "show", f"{commit}:{RELEASE}")
    if shown.returncode != 0:
        return problems + [Problem("R4", tag, f"{RELEASE} assente nel commit del tag")]
    releases, _, _ = parse(shown.stdout)
    first = releases[0].label if releases else None
    if first != m.group(1):
        problems.append(Problem("R4", tag, f"la prima riga di {RELEASE} è {first or 'assente'}, "
                                           f"il tag è {m.group(1)}"))
    return problems


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument("--tag", help="tag da pubblicare (regola R4)")
    parser.add_argument("--main", default="origin/main", help="branch principale per R4 (default origin/main)")
    parser.add_argument("--root", type=Path, default=ROOT)
    args = parser.parse_args()
    root = args.root.resolve()

    releases, r1, block = parse((root / RELEASE).read_text(encoding="utf-8"))
    results = {
        "formato (R1)": r1,
        "ordine (R2)": check_order(releases),
        "righe recenti per la home (R3)": check_recent(block) if block else [],
    }
    if args.tag:
        results[f"tag {args.tag} (R4)"] = check_tag(root, args.tag, args.main)

    print(f"Release in {RELEASE}: {', '.join(r.label for r in releases) or 'nessuna'}")
    failed = False
    for label, problems in results.items():
        print(f"{label}: {'OK' if not problems else f'{len(problems)} problemi'}")
        for p in problems:
            print(f"  - {p}")
        failed |= bool(problems)
    print("Controllo release: " + ("FALLITO" if failed else "OK"))
    return 1 if failed else 0


if __name__ == "__main__":
    sys.exit(main())
