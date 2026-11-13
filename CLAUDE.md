# rpsd-doc — Context for Claude Code

## What this repo is
Static documentation site for the Rapsodia project, built with Zensical
(config kept in mkdocs.yml). Documents the Italian NeTEx/SIRI profiles, the
ART indicators and, in a later step, one section per service contract.

## Key documents
- rpsd-doc-site-design.md — full site design (read before any change)
- openspec/seed.md — change plan and requirements for OpenSpec
- openspec/config.yaml — OpenSpec project context and rules

## Workflow
- All work goes through OpenSpec: /opsx:propose → review → /opsx:apply → /opsx:archive
- One change per branch
- Never push, create remote branches, open PRs or change GitHub settings
  without explicit approval from Franco

## Versioned profiles
- docs/netex/<version>/ and docs/siri/<version>/ hold one frozen copy per profile
  version. Never edit a non-current version except for errata. A new profile
  version is a new folder, not an edit of the existing one.

## Hand-written vs generated
- NEVER edit by hand: docs/indicatori/catalogo/, docs/indicatori/matrice.md and,
  once they exist (second step), docs/contratti/ and docs/validazione/.
  They are produced by rpsd-tools from data files in data/ using templates/.

## Conventions
- Language: Italian (content), English (technical terms from standards)
- Indicator codes, rule ids, contract ids and published URLs are stable
- General pages carry no contract thresholds and no tender-annex references
- Max 1500 words per hand-written page
- Use only features supported by both Zensical and Material for MkDocs (phase 1)
- Never invent content: every field, constraint or rule must come from a source
  document; if a source is missing, stop and ask

## Source documents
Not yet in the repo. Will be added under sources/ before content changes (5–9):
Linee guida compilazione NeTEx IT v5.0.0, Linee guida compilazione SIRI IT v1.0.5,
Delibera ART 53/2024 Allegato A, rapsodia-context.md.

## Zensical
- Use the zensical CLI only: `zensical serve`, `zensical build --strict`.
  Never run `mkdocs serve` or `mkdocs build`.
- Do NOT run `zensical new`: it creates zensical.toml. In phase 1 the
  configuration lives in mkdocs.yml (see rpsd-doc-site-design.md §2.1).
- Work inside a Python virtual environment (.venv/). .gitignore must include
  .venv/, site/, .cache/
- Zensical reference docs: https://zensical.org/docs/ — check them before
  assuming a Material for MkDocs feature or plugin option works the same way.
