# Design — add-site-releases

## Context

Motivazione: `proposal.md`. Oggi `deploy.yml` parte a ogni push su `main` (più avvio manuale), fa `zensical build --strict` e pubblica su GitHub Pages; il checkout è superficiale. L'ambiente `github-pages` ha una regola di deploy che ammette solo il branch `main` (verificato con `gh api`, 22/11/2026). `main` è protetto: controlli obbligatori, niente force push, nessuna revisione richiesta, amministratori non vincolati. `docs/rapsodia/release.md` ha una tabella `Data | Area | Modifica`, una riga per change, con le ultime 3 righe fra i marcatori `recenti` inclusi dalla home (`pymdownx.snippets`). rpsd-tools fa le release con un commit «Release X.Y.Z» su `main` e un tag annotato `vX.Y.Z` il cui messaggio elenca le novità.

## Goals / Non-Goals

**Goals:** il sito pubblicato cambia solo a una release; tag, pagina e sito pubblicato non possono divergere senza che un controllo fallisca; la procedura è la stessa di rpsd-tools.

**Non-Goals:** più release consultabili online; GitHub Releases; numero di release nelle pagine; automazione del tag (lo crea e lo pusha Franco, o Claude con la sua approvazione).

## Decisions

- **D1 — Procedura di release con PR.** `main` è protetto e i controlli obbligatori valgono per le PR, quindi il commit «Release X.Y.Z» passa da una PR (branch `release-X.Y.Z`) che aggiunge solo la riga in `release.md`. Dopo il merge: `git tag -a vX.Y.Z <commit di merge>` con il messaggio di D5, push del tag. Alternativa scartata: commit diretto su `main` (possibile perché gli amministratori non sono vincolati, ma salterebbe i controlli della PR).
- **D2 — Trigger di `deploy.yml`.** `on: push: tags: ['v*']` e `workflow_dispatch`. Nel job `build`, prima del build: checkout con `fetch-depth: 0` e `python scripts/check_release.py --tag "$GITHUB_REF_NAME"`. Un avvio manuale da un branch fallisce al controllo (il ref non è un tag `vX.Y.Z`): si può ripubblicare solo una release. Il merge su `main` non pubblica più nulla.
- **D3 — `scripts/check_release.py`.** Legge la tabella di `docs/rapsodia/release.md` (stesse convenzioni degli altri script: `Problem`, codici di regola, uscita 1 se ci sono problemi).
  - R1: intestazione `| Versione | Data | Novità |`; ogni riga ha versione `**X.Y.Z**`, data `G mmm AAAA` (mesi abbreviati in italiano) e novità non vuote.
  - R2: versioni strettamente decrescenti dall'alto, date non crescenti.
  - R3: marcatori `recenti` presenti, con dentro l'intestazione e al più le 3 righe più recenti (le prime della tabella).
  - R4 (con `--tag`): il tag ha la forma `vX.Y.Z`, è annotato, punta a un commit raggiungibile da `origin/main` e `X.Y.Z` è la prima riga.
  - Una tabella senza righe è valida (stato prima della prima release).
  Test in `scripts/test_release.py` su un repository git temporaneo (casi conformi e non conformi per R1–R4). Su `pr.yml` si eseguono `check_release.py` (senza `--tag`) e `test_release.py`.
- **D4 — Formato di «Release del sito».** Tabella `Versione | Data | Novità`, dalla più recente. Versione in grassetto, data come oggi (`22 nov 2026`), novità come elementi separati da ` · `, ciascuno preceduto dall'icona della sua area (Profili, Struttura, Convenzioni, Navigazione, Sito: le icone già in CONTRIBUTING). Niente liste o HTML nelle celle: i separatori bastano e restano Markdown puro. La colonna «Area» sparisce: una release tocca più aree.
- **D5 — Messaggio del tag.** Come rpsd-tools: prima riga `rpsd-doc X.Y.Z — <sintesi>`, poi `Novità:` e un elemento per riga, con lo stesso testo della cella «Novità» senza icone. Scritto in CONTRIBUTING con un esempio.
- **D6 — Prima release con la procedura normale.** Questo change porta `release.md` al nuovo formato **senza righe**: le 7 righe per change non hanno più senso come release. La 0.1.0 arriva con la prima PR «Release 0.1.0» dopo il merge e l'archiviazione di questo change, così la procedura viene provata per intero. Lo stato intermedio non viene mai pubblicato, perché dopo il merge il deploy parte solo dai tag. Contenuto della 0.1.0: le change archiviate fino a `add-site-releases`, raggruppate per area (bozza nei task, da rivedere con Franco).
- **D7 — Ambiente `github-pages`.** La regola di deploy passa da «branch `main`» a «tag `v*`» (`gh api` su `environments/github-pages/deployment-branch-policies`). Va fatto dopo il merge di questo change e prima del push di `v0.1.0`; con la sola regola `main` il deploy dal tag verrebbe rifiutato. Modifica alle impostazioni GitHub: solo con approvazione esplicita di Franco.
- **D8 — Release del sito e versioning del design §2.3.** Restano compatibili: il §2.3 esclude un versioning di sito che pubblica più copie del sito; le release pubblicano sempre e solo l'ultima. Si scrive nel §2.3.

## Risks / Trade-offs

- [Correzioni urgenti aspettano una release] → una patch `X.Y.Z+1` è solo una PR con una riga e un tag.
- [Si dimentica di pubblicare: `main` resta avanti rispetto al sito] → accettato: è lo scopo. CONTRIBUTING ricorda di proporre una release dopo l'archiviazione di una change che tocca il sito.
- [Tag pushato per errore su un commit sbagliato] → R4 ferma il deploy; il tag si cancella e si ricrea (con approvazione di Franco).
- [Deploy dal tag rifiutato dall'ambiente] → D7 prima del primo tag; il controllo di fine change lo verifica sulla run di `v0.1.0`.

## Migration Plan

1. Merge di questo change: il sito pubblicato resta quello attuale.
2. Archiviazione del change (PR).
3. Con approvazione di Franco: regola dei tag `v*` sull'ambiente `github-pages` al posto di `main` (D7).
4. PR «Release 0.1.0» con la riga della release; merge.
5. Con approvazione di Franco: tag annotato `v0.1.0` sul commit di merge e push; verifica della run di Deploy e del sito.

Rollback: ripristinare in `deploy.yml` il trigger su `main` e la regola `main` dell'ambiente.

## Open Questions

- Testo della riga 0.1.0 e della sintesi del tag: si scrive nella PR di release, partendo dalla bozza nei task.
