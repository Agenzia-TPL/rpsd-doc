# Proposal — add-overview-pages

## Why

La home attuale (`docs/index.md`) è una tabella con tutte le pagine e le sezioni del sito. Franco vuole una home sul modello di <https://pydantic.dev/docs/>: una frase introduttiva, schede di ingresso alle sezioni, le versioni correnti dei profili e in fondo le ultime versioni del sito. Decisioni di Franco del 20–22/11/2026 sul tab Rapsodia: niente pagina Progetto (il testo sul progetto va nella home), «Novità del sito» diventa «Release del sito», il glossario passa in Guida operativa. Sono i requisiti *Landing page* e *Site changelog* del change 5 del seed (`overview`), più un requisito nuovo sulle ultime versioni in home.

## What Changes

- **Home** (`docs/index.md`), solo Markdown, front matter `hide: [navigation, toc]`, in quest'ordine:
  1. titolo e una frase su cos'è Rapsodia e per chi è il sito;
  2. posto per il testo sul progetto (obiettivi, consorzio, partner): si scrive quando ci sono le fonti, non in questo change;
  3. griglia di schede (`<div class="grid cards" markdown>`), una per sezione da Architettura in avanti: Architettura, NeTEx, SIRI, Indicatori, Modello dati, Dashboard, Guida operativa, Contratti. Nessuna scheda Rapsodia: la home è la pagina del tab Rapsodia. Ogni scheda ha un'icona accanto al titolo e in fondo il link «Vai alla sezione»; le schede NeTEx e SIRI riportano la versione corrente (5.0.0, 1.0.5);
  4. «Release del sito»: le ultime voci del changelog del sito e il link alla pagina completa.
- **Pagina Progetto tolta**: `rapsodia/progetto.md` eliminata, senza redirect.
- **Novità → Release del sito**: `rapsodia/novita.md` sostituita da `rapsodia/release.md`, senza redirect. La pagina elenca le modifiche al sito dalla più recente, ricavate dalle change archiviate.
- **Glossario in Guida operativa**: `rapsodia/glossario.md` spostata in `guida/glossario.md`, senza redirect. Il tab Rapsodia resta con home e Release del sito. La regola S1 (*Linkable glossary*) non cambia; si aggiorna solo il percorso nel controllo e in CONTRIBUTING.
- **URL stabili solo per pagine con contenuto**: il requisito *Stable URLs* di `content-conventions` esclude le pagine pubblicate solo come segnaposto (titolo e avviso «Sezione in preparazione»). `scripts/check_urls.py` non segnala più gli URL di quelle pagine. Le tre pagine del tab Rapsodia sono segnaposto: spariscono senza redirect e senza lasciare voci in `mkdocs.yml` (decisione di Franco del 22/11/2026).
- **Regola V8** in `scripts/check_versions.py`: la home deve linkare la versione corrente di ogni profilo dichiarata in `extra.profili`, che altrimenti resterebbe indietro al cambio di versione.
- **Design del sito e seed** aggiornati secondo le nuove decisioni (tab Rapsodia, glossario, URL stabili), senza note su ciò che non esiste più.

Contenuto **redazionale** più infrastruttura (controlli di CI `check_urls.py`, `check_versions.py`, `check_navigation.py`, `check_conventions.py`); nessun contenuto generato. Implementa il design del sito §4.2 («la home è l'indice del sito: cos'è Rapsodia e un ingresso per ogni sezione»), che questo change aggiorna per il tab Rapsodia.

Fonti dei testi (nessun testo inventato):
- cos'è Rapsodia: la frase della home attuale;
- per chi è il sito: le tre audience del design §1 (Aziende TPL, Agenzie TPL, team tecnico);
- descrizioni delle schede: la colonna «Cosa contiene» della home attuale;
- versioni correnti dei profili: `extra.profili` in `mkdocs.yml`;
- voci di Versioni: le change archiviate in `openspec/changes/archive/` (data, nome, scopo dalla proposal).

## Capabilities

### New Capabilities
- `overview`: pagine di presentazione del sito e del progetto. In questo change i requisiti *Landing page* e *Site changelog* del seed §4.6, così come sono scritti, e un requisito **non presente nel seed**: *Latest versions on the home page* (aggiunto al seed da questo change).

### Modified Capabilities
- `content-conventions`: *Stable URLs* non si applica alle pagine pubblicate solo come segnaposto.

*Home page* di `site-navigation` resta valido (`hide: [navigation]` nasconde la sidebar, non i tab); *Linkable glossary* resta valido (il glossario cambia solo percorso).

## Impact

- Pagine: `docs/index.md`; eliminata `docs/rapsodia/progetto.md`; spostate `docs/rapsodia/novita.md` → `docs/rapsodia/release.md` e `docs/rapsodia/glossario.md` → `docs/guida/glossario.md`.
- Navigazione: `docs/.nav.yml` (tab Rapsodia).
- Configurazione: `mkdocs.yml`, estensione `pymdownx.emoji` per le icone delle schede, nella forma di Material accettata anche da Zensical; nessun redirect nuovo.
- CI: `scripts/check_urls.py` e `scripts/test_conventions.py` (segnaposto), `scripts/check_versions.py` e `scripts/test_versions.py` (V8), `scripts/check_navigation.py` (pagine controllate), `scripts/check_conventions.py` e `scripts/test_conventions.py` (percorso del glossario).
- Documentazione: `CONTRIBUTING.md` («URL stabili», «Profili versionati», «Glossario e sigle»), `rpsd-doc-site-design.md`, `openspec/seed.md`.
- URL: `rapsodia/progetto/`, `rapsodia/novita/`, `rapsodia/glossario/` non sono più serviti (erano segnaposto); nuovi `rapsodia/release/` e `guida/glossario/`.

## Out of scope

- Testo sul progetto (seed §4.6 *Project overview*), Architettura e Core (*Architecture by subsystem*, *Core functional modules*): servono le fonti in `sources/`.
- Contenuto del glossario: il requisito *Glossary* passa nel seed da `overview` a `operational-guide` (change 9), con le fonti.
- Tooltip sulle sigle (`abbr` + `content.tooltips`): provato il 22/11/2026, scartato da Franco.
- Template personalizzati, CSS o HTML scritto a mano oltre al contenitore delle schede.
- Contratti in evidenza come ingresso per le Aziende (design §4.2, secondo step): in home, fra le schede e Release del sito, una sezione «Contratti monitorati» ripresa dall'elenco generato dei contratti (mai copiata a mano, solo contratti pubblici). Si aggiunge con il primo contratto generato, quando sparisce il segnaposto `esempio`; fino ad allora basta la scheda Contratti (decisione di Franco del 22/11/2026).
