# Design — add-overview-pages

## Context

Motivazione: `proposal.md`. Oggi `docs/index.md` è una tabella di undici voci, senza front matter. Il tab Rapsodia (`docs/.nav.yml`) raggruppa home, `rapsodia/progetto.md`, `rapsodia/glossario.md`, `rapsodia/novita.md`, tutte segnaposto. `docs/guida/.nav.yml` elenca `index.md` e poi `"*"`. `mkdocs.yml` ha già `attr_list`, `md_in_html`, `pymdownx.snippets` e il plugin `redirects` (usato solo per gli alias `corrente/`); non ha `pymdownx.emoji`. Le versioni correnti dei profili stanno in `extra.profili`, controllate da `check_versions.py` (V1–V7). `check_navigation.py` controlla i tab su un elenco fisso di pagine, che include `rapsodia/progetto/`. `check_conventions.py` legge il glossario da una costante `GLOSSARY` (regola S1). `check_urls.py` fa fallire la PR se un URL pubblicato non è più servito come pagina o redirect.

## Goals / Non-Goals

**Goals:** home in solo Markdown, con funzioni presenti sia in Zensical sia in Material; ristrutturazione pulita, senza redirect né note per pagine che non hanno mai avuto contenuto; nessun dato scritto in due posti senza un controllo.

**Non-Goals:** template, CSS o blocchi HTML; contenuto del progetto e del glossario.

## Decisions

- **D1 — Otto schede, nessuna per Rapsodia.** Le «main sections» del requisito *Landing page* sono i tab da Architettura in avanti (decisione di Franco). La home è la pagina del tab Rapsodia, quindi una scheda Rapsodia porterebbe a sé stessa.
- **D2 — Ordine della home.** Titolo → frase introduttiva → testo sul progetto (assente finché non ci sono le fonti; nessun segnaposto visibile) → schede → «Versioni». Frase introduttiva: «Rapsodia è la piattaforma di monitoraggio del trasporto pubblico locale delle Agenzie TPL lombarde; questo sito ne raccoglie la documentazione per le Aziende TPL, le Agenzie TPL e il team tecnico.» (home attuale + design §1).
- **D3 — Schede a griglia, forma a lista, con icone.** `<div class="grid cards" markdown>` con una voce di lista per scheda: icona `:material-…:{ .lg .middle }` e titolo in grassetto, `---`, una frase dalla colonna «Cosa contiene» della home attuale, in fondo `[:material-arrow-right: Vai alla sezione](…)`. È lo schema documentato da Material e da Zensical. Icone (scelte da Franco il 22/11/2026 su anteprima): Architettura `sitemap-outline`, NeTEx `timetable`, SIRI `bus-clock`, Indicatori `chart-line`, Modello dati `database-outline`, Dashboard `view-dashboard-outline`, Guida operativa `book-open-variant`, Contratti `file-sign`.
- **D3b — `pymdownx.emoji` in `mkdocs.yml`.** `emoji_index: material.extensions.emoji.twemoji`, `emoji_generator: material.extensions.emoji.to_svg`: è la forma di Material, che Zensical 0.1.1 accetta (verificato con build strict: le icone sono rese in SVG inline). La stessa configurazione vale quindi per entrambi i generatori. Alternativa scartata: `zensical.extensions.emoji`, che non funzionerebbe con Material.
- **D4 — Versioni dei profili nelle schede.** Riga «Versione corrente: [5.0.0](netex/5.0.0/index.md)» nella scheda NeTEx, «[1.0.5](siri/1.0.5/index.md)» in SIRI. Link alla cartella di versione, non all'alias `corrente/` (redirect, non verificato dal build strict come link a file).
- **D5 — Regola V8.** `check_versions.py`: per ogni profilo di `extra.profili`, `docs/index.md` linka `<profilo>/<corrente>/index.md` e nessuna cartella di versione non corrente. Test in `test_versions.py`. Già in `pr.yml`.
- **D6 — Pagina Versioni.** `git mv rapsodia/novita.md rapsodia/versioni.md`, titolo «Versioni». Una tabella `Data | Area | Modifica`, una riga per change archiviata e integrata in `main`, dalla più recente: data in grassetto, area con icona (Profili, Struttura, Convenzioni, Navigazione, Sito; elenco in CONTRIBUTING), scopo riassunto dalla proposal. Formato a tabella scelto da Franco il 22/11/2026. «Versione» del sito = una change archiviata: oggi non ci sono tag di rilascio, e l'archivio è l'unica fonte datata delle modifiche.
- **D7 — Ultime righe in home con snippets.** In `versioni.md` l'intestazione della tabella e le 3 righe più recenti stanno fra due marcatori di sezione di `pymdownx.snippets` (`<!-- --8<-- [start:recenti] -->` … `[end:recenti]`); la home le include con `--8<-- "docs/rapsodia/versioni.md:recenti"` sotto il titolo «Versioni» e chiude con il link alla pagina. `pymdownx.snippets` toglie i marcatori anche dalla pagina stessa, quindi la tabella completa non si spezza (verificato con build strict: una tabella di 7 righe nella pagina, una di 3 in home).
- **D8 — Pagine tolte o spostate, senza redirect.** `rapsodia/progetto.md` eliminata; `rapsodia/novita.md` → `rapsodia/versioni.md` e `rapsodia/glossario.md` → `guida/glossario.md` con `git mv`; nessuna voce in `redirect_maps`. È possibile perché sono segnaposto (D11). Il glossario entra nella sidebar di Guida operativa tramite `"*"`, senza toccare `guida/.nav.yml`. Tab Rapsodia: `index.md`, `rapsodia/versioni.md`.
- **D9 — Controlli che citano i vecchi percorsi.** `check_navigation.py`: `rapsodia/progetto/index.html` sostituita da `rapsodia/versioni/index.html` (tab Rapsodia attivo); `check_conventions.py`: `GLOSSARY = "docs/guida/glossario.md"`, con i link d'esempio dei test e di CONTRIBUTING (`../guida/glossario.md#pde`).
- **D11 — Eccezione ai segnaposto in `check_urls.py`.** Un URL presente in BASE e assente nella copia corrente non è un errore se in BASE la sua pagina Markdown è un segnaposto: dopo il front matter contiene solo il titolo `#` e il callout `!!! note "Sezione in preparazione"` con il suo testo. Il controllo si fa sui sorgenti di BASE già estratti da `export_revision`, mappando l'URL al file (`x/` → `docs/x.md` o `docs/x/index.md`). Le pagine di sezione come `netex/index.md`, che hanno l'avviso più una tabella, non sono segnaposto e restano protette. Testata in `scripts/test_conventions.py`, accanto ai casi esistenti di *Stable URLs*. Il messaggio finale elenca a parte gli URL tolti perché segnaposto. Alternativa scartata: un elenco di URL rimossi dichiarati a mano, da mantenere e che resta come residuo nel repo.
- **D12 — Seed e design del sito riallineati.** Il seed (§4.6 `overview`, tabella dei change, *Stable URLs* in §4.3) e il design del sito (§0 nuova voce datata, §3, §4.2, albero delle cartelle, §8 URL stabili, §9) si correggono nel testo, come se le decisioni ci fossero da subito, con la sola voce datata in §0 che le registra.
- **D10 — `hide: [navigation, toc]`.** Nasconde sidebar e indice a destra, non i tab. Effetto: dalla home la pagina Versioni si raggiunge dal link in fondo, non dalla sidebar.

## Risks / Trade-offs

- [Il testo sul progetto, quando arriva, spinge le schede sotto la prima schermata, contro *Landing page* «in one screen»] → testo breve (poche righe); se non basta, si rivede il requisito.
- [Otto schede più la sezione Versioni: la home non sta tutta in una schermata] → il requisito chiede in una schermata solo frase e ingressi; Versioni sta sotto le schede per scelta.
- [Snippets con marcatori di sezione da spostare a ogni nuova voce] → regola in CONTRIBUTING; il build strict fallisce se la sezione manca.
- [Versioni dei profili scritte in due posti] → V8.

## Open Questions

- Testo della voce di Versioni: si può riprendere la prima frase del «Why» della proposal o riassumerla. Non cambia struttura né task; si decide alla revisione della pagina.
