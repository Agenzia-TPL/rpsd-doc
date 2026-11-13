#!/usr/bin/env python3
"""Controlli sulle versioni dei profili NeTEx e SIRI (capability profile-versioning).

Fonte: `extra.profili` in mkdocs.yml (versione corrente e stato di ogni versione).

Regole (design del change add-profile-versioning, D6):
  V1  metadati: una sola versione corrente, dichiarata tra le versioni; stati ammessi
  V2  cartelle: una cartella docs/<profilo>/<versione>/ con index.md per ogni versione
      dichiarata, nessuna cartella di versione non dichiarata, nessuna pagina fuori
      dalle cartelle di versione salvo docs/<profilo>/index.md
  V3  sidebar: docs/<profilo>/.nav.yml elenca index.md e la sola versione corrente, senza "*"
  V4  alias: redirect_maps porta <profilo>/corrente/ alla versione corrente
  V5  elenco versioni: docs/<profilo>/index.md ha una riga per versione, con link e stato
  V6  (con --site DIR) avviso su tutte e sole le pagine delle versioni non correnti
  V7  (con --commits BASE) i commit che modificano una versione non corrente hanno il
      trailer "Errata: <motivo>"

Uso: python scripts/check_versions.py [--site DIR] [--commits BASE] [--root DIR]
"""
from __future__ import annotations

import argparse
import re
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT / "scripts"))
from check_conventions import Problem  # noqa: E402
from spike import load_config  # noqa: E402

STATES = {"corrente", "precedente", "ritirata"}
VERSION_DIR = re.compile(r"^\d+\.\d+\.\d+$")
TABLE_ROW = re.compile(r"^\|\s*\[([^\]]+)\]\(([^)\s]+)\)\s*\|\s*([^|]*?)\s*\|")
TO_COMPLETE = "_da completare_"
NOTICE_CLASS = "avviso-versione"
ERRATA = "Errata"


def profiles(config: dict) -> dict:
    return ((config.get("extra") or {}).get("profili") or {})


def redirect_maps(config: dict) -> dict:
    for item in config.get("plugins", []):
        if isinstance(item, dict) and "redirects" in item:
            return dict((item["redirects"] or {}).get("redirect_maps") or {})
    return {}


# --------------------------------------------------------------------------- V1–V5


def check_metadata(config: dict) -> list[Problem]:
    problems = []
    if not profiles(config):
        problems.append(Problem("V1", "mkdocs.yml", "extra.profili assente o vuoto"))
    for name, prof in profiles(config).items():
        versions = {str(k): str(v) for k, v in (prof.get("versioni") or {}).items()}
        current = str(prof.get("corrente", ""))
        where = f"mkdocs.yml extra.profili.{name}"
        bad = {v: s for v, s in versions.items() if s not in STATES}
        if bad:
            problems.append(Problem("V1", where, f"stati non ammessi {bad} (ammessi: {', '.join(sorted(STATES))})"))
        currents = [v for v, s in versions.items() if s == "corrente"]
        if current not in versions:
            problems.append(Problem("V1", where, f"versione corrente {current!r} non dichiarata tra le versioni"))
        if currents != [current]:
            problems.append(Problem("V1", where, f"le versioni con stato 'corrente' sono {currents}, "
                                                 f"deve essere solo {current!r}"))
    return problems


def check_folders(root: Path, config: dict) -> list[Problem]:
    problems = []
    for name, prof in profiles(config).items():
        base = root / "docs" / name
        declared = {str(v) for v in (prof.get("versioni") or {})}
        for v in sorted(declared):
            if not (base / v / "index.md").exists():
                problems.append(Problem("V2", f"docs/{name}/{v}/", "cartella della versione dichiarata assente "
                                                                    "o senza index.md"))
        for d in sorted(p for p in base.iterdir() if p.is_dir()) if base.exists() else []:
            if VERSION_DIR.match(d.name) and d.name not in declared:
                problems.append(Problem("V2", f"docs/{name}/{d.name}/", "cartella di versione non dichiarata "
                                                                         "in extra.profili"))
        for page in sorted(base.rglob("*.md")) if base.exists() else []:
            rel = page.relative_to(base)
            if rel.as_posix() == "index.md":
                continue
            if rel.parts[0] not in declared:
                problems.append(Problem("V2", page.relative_to(root).as_posix(),
                                        "pagina fuori dalle cartelle di versione: ogni pagina di profilo sta "
                                        f"sotto docs/{name}/<versione>/"))
    return problems


def nav_targets(nav: list) -> list[str]:
    out = []
    for item in nav or []:
        if isinstance(item, dict):
            out.extend(str(v) for v in item.values())
        else:
            out.append(str(item))
    return out


def check_sidebar_nav(root: Path, config: dict) -> list[Problem]:
    import yaml
    problems = []
    for name, prof in profiles(config).items():
        current = str(prof.get("corrente", ""))
        path = root / "docs" / name / ".nav.yml"
        where = f"docs/{name}/.nav.yml"
        if not path.exists():
            problems.append(Problem("V3", where, "assente"))
            continue
        targets = [t.rstrip("/") for t in nav_targets((yaml.safe_load(path.read_text(encoding="utf-8")) or {}).get("nav"))]
        if any("*" in t for t in targets):
            problems.append(Problem("V3", where, "contiene \"*\": la sidebar deve mostrare solo la versione corrente"))
        versions = [t for t in targets if VERSION_DIR.match(t)]
        if versions != [current]:
            problems.append(Problem("V3", where, f"versioni in sidebar {versions}, deve esserci solo {current!r}"))
        if "index.md" not in targets:
            problems.append(Problem("V3", where, "manca index.md (elenco versioni)"))
    return problems


def check_alias(config: dict) -> list[Problem]:
    maps = redirect_maps(config)
    problems = []
    for name, prof in profiles(config).items():
        key, expected = f"{name}/corrente/index.md", f"{name}/{prof.get('corrente')}/index.md"
        if maps.get(key) != expected:
            problems.append(Problem("V4", "mkdocs.yml redirect_maps", f"{key} deve puntare a {expected} "
                                                                     f"(trovato: {maps.get(key)!r})"))
    return problems


def check_version_list(root: Path, config: dict, notes: list[str] | None = None) -> list[Problem]:
    problems = []
    for name, prof in profiles(config).items():
        path = root / "docs" / name / "index.md"
        where = f"docs/{name}/index.md"
        if not path.exists():
            problems.append(Problem("V5", where, "pagina elenco versioni assente"))
            continue
        text = path.read_text(encoding="utf-8")
        rows = {}
        for line in text.splitlines():
            m = TABLE_ROW.match(line.strip())
            if m:
                rows[m.group(1).strip()] = (m.group(2), m.group(3).strip())
        for v, state in (prof.get("versioni") or {}).items():
            v, state = str(v), str(state)
            if v not in rows:
                problems.append(Problem("V5", where, f"manca la riga della versione {v}"))
                continue
            link, listed = rows[v]
            if link.rstrip("/") not in (f"{v}/index.md", v):
                problems.append(Problem("V5", where, f"la riga {v} deve linkare {v}/index.md (trovato {link})"))
            if listed != state:
                problems.append(Problem("V5", where, f"stato della versione {v}: '{listed}' nella tabella, "
                                                     f"'{state}' in extra.profili"))
        for v in rows:
            if v not in {str(x) for x in (prof.get("versioni") or {})}:
                problems.append(Problem("V5", where, f"riga della versione {v} non dichiarata in extra.profili"))
        if notes is not None and TO_COMPLETE in text:
            notes.append(f"{where}: {text.count(TO_COMPLETE)} campi \"{TO_COMPLETE}\"")
    return problems


# --------------------------------------------------------------------------- V6


def check_site_notices(site: Path, config: dict) -> list[Problem]:
    problems = []
    for name, prof in profiles(config).items():
        current = str(prof.get("corrente", ""))
        for v in (prof.get("versioni") or {}):
            v = str(v)
            pages = sorted((site / name / v).rglob("*.html"))
            if not pages:
                problems.append(Problem("V6", f"{site.name}/{name}/{v}/", "nessuna pagina costruita"))
            for page in pages:
                html = page.read_text(encoding="utf-8")
                rel = page.relative_to(site).as_posix()
                has = NOTICE_CLASS in html
                if v == current and has:
                    problems.append(Problem("V6", rel, "avviso di versione non corrente su una pagina della corrente"))
                if v != current:
                    if not has:
                        problems.append(Problem("V6", rel, f"pagina della versione {v} senza avviso di versione "
                                                           "non corrente"))
                    elif not re.search(rf'href="[^"]*/{re.escape(name)}/{re.escape(current)}/"', html):
                        problems.append(Problem("V6", rel, f"l'avviso non linka la versione corrente {current}"))
        index = site / name / "index.html"
        if index.exists() and NOTICE_CLASS in index.read_text(encoding="utf-8"):
            problems.append(Problem("V6", f"{name}/index.html", "avviso di versione sulla pagina elenco versioni"))
    return problems


# --------------------------------------------------------------------------- V7


def git(root: Path, *args: str) -> str:
    return subprocess.run(["git", *args], cwd=root, capture_output=True, text=True, check=True).stdout


def check_frozen(root: Path, config: dict, base: str) -> list[Problem]:
    frozen = [f"docs/{name}/{v}/" for name, prof in profiles(config).items()
              for v in (prof.get("versioni") or {}) if str(v) != str(prof.get("corrente"))]
    if not frozen:
        return []
    try:
        git(root, "rev-parse", "--verify", f"{base}^{{commit}}")
    except subprocess.CalledProcessError:
        return [Problem("V7", base, "riferimento base non trovato (serve la cronologia completa: fetch-depth 0)")]
    problems = []
    for sha in git(root, "log", "--no-merges", "--format=%H", f"{base}..HEAD", "--", *frozen).split():
        if git(root, "log", "-1", f"--format=%(trailers:key={ERRATA},valueonly)", sha).strip():
            continue
        files = git(root, "diff-tree", "--no-commit-id", "--name-only", "-r", sha, "--", *frozen).split()
        subject = git(root, "log", "-1", "--format=%s", sha).strip()
        problems.append(Problem(
            "V7", f"commit {sha[:7]} \"{subject}\"",
            f"modifica una versione di profilo non corrente ({', '.join(files)}). Le versioni non correnti sono "
            f"congelate: si modificano solo per errata, con il trailer \"{ERRATA}: <motivo>\"; una revisione del "
            "profilo è una nuova cartella di versione"))
    return problems


# --------------------------------------------------------------------------- main


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument("--site", type=Path, help="sito costruito da controllare (regola V6)")
    parser.add_argument("--commits", metavar="BASE", help="controlla anche i commit BASE..HEAD (regola V7)")
    parser.add_argument("--root", type=Path, default=ROOT)
    args = parser.parse_args()
    root = args.root.resolve()
    config = load_config(root / "mkdocs.yml")

    notes: list[str] = []
    results = {
        "metadati (V1)": check_metadata(config),
        "cartelle di versione (V2)": check_folders(root, config),
        "sidebar sulla versione corrente (V3)": check_sidebar_nav(root, config),
        "alias della versione corrente (V4)": check_alias(config),
        "elenco versioni (V5)": check_version_list(root, config, notes),
    }
    if args.site:
        results["avviso sulle versioni non correnti (V6)"] = check_site_notices(args.site.resolve(), config)
    if args.commits:
        results[f"versioni congelate (V7, {args.commits}..HEAD)"] = check_frozen(root, config, args.commits)

    for name, prof in profiles(config).items():
        print(f"{prof.get('titolo', name)}: corrente {prof.get('corrente')}, versioni {dict(prof.get('versioni') or {})}")
    for note in notes:
        print(f"da completare: {note}")
    failed = False
    for label, problems in results.items():
        print(f"{label}: {'OK' if not problems else f'{len(problems)} problemi'}")
        for p in problems:
            print(f"  - {p}")
        failed |= bool(problems)
    print("Controllo versioni: " + ("FALLITO" if failed else "OK"))
    return 1 if failed else 0


if __name__ == "__main__":
    sys.exit(main())
