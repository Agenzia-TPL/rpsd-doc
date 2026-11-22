# Proposal — add-site-releases

## Why

Oggi `deploy.yml` pubblica il sito a ogni merge su `main`, e la pagina «Release del sito» ha una riga per ogni change. Chi legge vede quindi un elenco di modifiche tecniche, e il sito pubblicato cambia a ogni PR. Decisione di Franco del 22/11/2026: introdurre le release del sito sul modello di rpsd-tools (commit «Release X.Y.Z» e tag annotato `vX.Y.Z`), pubblicare solo le release e mostrare in «Release del sito» una riga per release. Serve anche al secondo step: le pagine di contratto richiamate dall'Allegato G chiedono versione, data e changelog espliciti (design §1).

## What Changes

- **Numerazione** `X.Y.Z`, come rpsd-tools: sotto la 1.0 la minore cambia per sezioni o contenuti nuovi, la patch per le correzioni.
- **Rilascio**: PR «Release X.Y.Z» che aggiunge la riga della release in `docs/rapsodia/release.md`; dopo il merge, tag annotato `vX.Y.Z` sul commit di `main`, con lo stesso contenuto della riga. Il push del tag lo fa o lo approva Franco ogni volta.
- **Pubblicazione solo alle release** — **BREAKING** per il flusso di lavoro: `deploy.yml` parte al push di un tag `v*` (e a mano su un tag), non più al merge su `main`. Fra due release `main` cambia ma il sito pubblicato resta quello dell'ultima release.
- **Controllo della release** (`scripts/check_release.py`): il deploy fallisce, e il sito resta com'è, se il tag non è `vX.Y.Z`, se non punta a un commit di `main` o se la sua versione non è la prima riga di «Release del sito». Sulle PR lo stesso script controlla il formato della pagina (versioni valide, in ordine decrescente, date valide).
- **Pagina «Release del sito»**: tabella `Versione | Data | Novità`, una riga per release, dalla più recente; le righe attuali (una per change) confluiscono nella **prima release, 0.1.0**, che raccoglie tutto il lavoro fino a questo change compreso. La home continua a mostrare le ultime 3 righe.
- **Impostazione GitHub**: l'ambiente `github-pages` oggi accetta deploy solo da `main`; va aggiunta la regola per i tag `v*`. È una modifica alle impostazioni del repository: solo con approvazione esplicita di Franco.
- **Documentazione**: CONTRIBUTING (procedura di release), README se descrive il deploy, design del sito (§2.3, piano di implementazione), seed (*Automated deployment*, *Site changelog*).

Tocca **infrastruttura** (workflow, controlli di CI, impostazioni GitHub) e **contenuto redazionale** (`release.md`); nessun contenuto generato. Implementa il design del sito §1 (versione e changelog espliciti) e aggiorna §2.3: le release del sito non sono un «versioning di sito» alla `mike`, perché resta pubblicata solo l'ultima.

## Capabilities

### New Capabilities
- `site-releases`: numerazione delle release, procedura (PR, tag annotato) e corrispondenza fra tag e pagina «Release del sito». Requisiti **non presenti nel seed**: *Release numbering*, *Release tag matches the changelog*.

### Modified Capabilities
- `site-platform`: *Automated deployment* pubblica al tag di release, non al cambiamento di `main` (seed §4.1 da aggiornare).
- `overview`: *Site changelog* elenca le release (versione, data, novità) invece delle singole modifiche (seed §4.6 da aggiornare).

## Impact

- CI: `.github/workflows/deploy.yml` (trigger sui tag, controllo della release), `.github/workflows/pr.yml` (formato della pagina), nuovi `scripts/check_release.py` e `scripts/test_release.py`.
- Pagine: `docs/rapsodia/release.md` (nuovo formato, riga 0.1.0); `docs/index.md` invariata (include sempre la sezione `recenti`).
- GitHub: regola di deploy per i tag `v*` nell'ambiente `github-pages`; primo tag `v0.1.0`.
- Documentazione: `CONTRIBUTING.md`, `README.md`, `rpsd-doc-site-design.md`, `openspec/seed.md`.
- Dopo il merge di questo change il sito pubblicato non cambia finché non si pubblica la 0.1.0.

## Out of scope

- Numero di release mostrato in ogni pagina (piè di pagina o testata): non richiesto ora.
- Versioni e validità delle pagine di contratto (secondo step): restano un asse separato, come le versioni dei profili.
- Protezione dei tag (ruleset GitHub) e GitHub Releases come pagine separate: si valutano dopo la prima release.
- Archivio delle release precedenti consultabile online: resta pubblicata solo l'ultima.
