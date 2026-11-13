# Proposal — add-content-conventions

## Why

Le convenzioni trasversali del sito (pagine generate mai toccate a mano, lunghezza massima, URL stabili, callout con significato fisso, glossario linkabile) oggi sono solo scritte nel design e in `CLAUDE.md`. Dai change 4–9 arrivano i contenuti e, con `rpsd-tools`, le pagine generate: se le regole non sono controllate in CI, le violazioni si accumulano e diventano costose da correggere. Il change 3 del seed le rende verificabili prima che arrivino i contenuti.

## What Changes

- Controlli in CI sulle pull request, uno per requisito di `content-conventions`:
  - **pagine generate**: front matter obbligatorio (`generato: true`, `generato_da`) e cartelle che contengono solo pagine generate; una PR fallisce se un suo commit modifica una cartella generata senza il trailer `Generato-da: rpsd-tools …`, con un messaggio che rimanda ai dati sorgente;
  - **lunghezza**: le pagine redazionali oltre 1500 parole vengono segnalate con il numero di parole;
  - **URL stabili**: plugin `redirects`; il build della PR deve servire ogni URL pubblicato su `main`, come pagina o come redirect;
  - **callout**: solo note, tip, warning, example, danger con titolo "Obbligatorio per KPI", info con titolo "Novità Rapsodia";
  - **glossario**: al primo uso in una pagina, ogni sigla del glossario deve essere un link alla sua voce.
- Elenco delle cartelle generate in un unico file letto dai controlli.
- Prove dei controlli (casi conformi e non conformi) eseguite in CI.
- `CONTRIBUTING.md` con le regole di scrittura, linkato dal README.
- Le pagine segnaposto passano dal callout `info` al callout `note` (oggi `info` è ammesso solo con titolo "Novità Rapsodia").

## Capabilities

### New Capabilities
- `content-conventions`: pagine generate riconoscibili, limite di lunghezza, URL stabili, callout coerenti, glossario linkabile. Requisiti presi **così come sono** dal seed §4.3.

### Modified Capabilities
_Nessuna._

## Riferimenti al design

Implementa `rpsd-doc-site-design.md`:
- **§3 e §3.1** — una pagina è redazionale o generata, mai mista; le cartelle generate si sovrascrivono per intero; la generazione arriva via PR; front matter `generato: true`.
- **§8** — convenzioni di scrittura: massimo 1500 parole, admonition con significato fisso, glossario linkabile, ID e URL stabili con `redirects`, pagine generate riconoscibili.
- **§2.1** — plugin `redirects` (tenuto per la stabilità degli URL).

## Tipo di intervento

**Infrastruttura del sito** (controlli, configurazione, documentazione per chi contribuisce). Unica modifica a contenuti esistenti: il tipo di callout delle cinque pagine segnaposto. Nessun contenuto generato e nessun contenuto di dominio.

## Decisioni prese in fase di proposta (scelte di Franco)

- **Modifiche manuali alle cartelle generate**: riconosciute dal trailer di commit `Generato-da: rpsd-tools <versione>`, che `rpsd-tools` dovrà aggiungere. Quando `rpsd-tools` esisterà si potrà aggiungere in CI la rigenerazione dai dati come controllo più forte.
- **Glossario**: in questo change solo il controllo, provato con termini fittizi; il glossario con le definizioni arriva nel change 5, quando ci saranno i documenti sorgente. Fino ad allora il controllo non trova sigle e passa.
- **"Come contribuire"**: `CONTRIBUTING.md` nel repository, non una pagina del sito.

## Punto da confermare in revisione

- **Matrice indicatori × dataset.** Il requisito *Generated pages are identifiable* chiede che una pagina generata stia in una cartella che contiene solo pagine generate. Il design §6 e `CLAUDE.md` prevedono invece `docs/indicatori/matrice.md`, nella cartella `indicatori/` che contiene anche pagine redazionali (`delibera/`). Proposta: `docs/indicatori/matrice/index.md`, che produce **lo stesso URL** (`/indicatori/matrice/`). Il change aggiorna di conseguenza design §6 e `CLAUDE.md`; nessuna pagina esiste ancora.

Nessun requisito aggiunto rispetto al seed §4.3.

## Fuori scope

- Il glossario e le sue voci (change 5).
- La generazione delle pagine e `rpsd-tools` stesso; il controllo per rigenerazione.
- Tag per dataset e codice indicatore (design §8), plugin `tags`: arrivano con le pagine generate.
- Controlli su lingua e tono: non verificabili in modo affidabile, restano regole in `CONTRIBUTING.md`.
- Operazioni su GitHub: push e PR solo con approvazione esplicita. La protezione di `main` non cambia (i nuovi controlli girano dentro i job già obbligatori).

## Impact

- File modificati: `mkdocs.yml` (plugin `redirects`), `.github/workflows/pr.yml`, `README.md`, `docs/**/index.md` segnaposto (callout), `rpsd-doc-site-design.md` §6 e `CLAUDE.md` (percorso della matrice).
- File nuovi: `scripts/check_conventions.py`, `scripts/test_conventions.py`, `scripts/check_urls.py`, `generated-paths.txt`, `CONTRIBUTING.md`.
- Dipendenze: nessuna nuova (solo libreria standard Python; `redirects` è integrato in Zensical). Con il piano B servirebbe il pacchetto `mkdocs-redirects`.
- Processo: ogni commit di `rpsd-tools` che tocca cartelle generate deve portare il trailer.
