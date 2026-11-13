# Proposal — add-directory-navigation

## Why

Oggi il sito ha una sola pagina e nessuna navigazione dichiarata: Zensical costruisce il menu dalla struttura delle cartelle, senza ordine né titoli controllati. I change di contenuto (4–9) e, nel secondo step, i contratti generati hanno bisogno di una navigazione stabile in cui una sezione o una sottosezione si aggiunge creando una cartella, senza toccare `mkdocs.yml` (design §4.3). Il change 2 del seed la mette in piedi prima che arrivino i contenuti.

## What Changes

- Navigazione per directory con file `.nav.yml` (formato awesome-nav, supportato nativamente da Zensical) e plugin `awesome-nav` dichiarato in `mkdocs.yml`; nessun `nav` in `mkdocs.yml`.
- `docs/.nav.yml` che definisce i tab di primo livello nell'ordine Home, NeTEx, SIRI, Indicatori, Guida operativa.
- Sezioni `docs/netex/`, `docs/siri/`, `docs/indicatori/`, `docs/guida/` con una pagina segnaposto "Sezione in preparazione" ciascuna (nessun contenuto di dominio) e il proprio `.nav.yml`, che include automaticamente le sottocartelle future.
- Plugin `search` dichiarato esplicitamente accanto ad `awesome-nav` (con `plugins:` presente, Material disattiverebbe la ricerca se non elencata; per Zensical è indifferente).
- Controlli automatici: ordine e stato attivo dei tab sul sito costruito, aggiunta di una sottosezione senza modifiche alla configurazione, sidebar di una pagina a tre livelli (antenati espansi, rami fratelli chiusi) nello spike. Integrati in `pr.yml`.
- README: breve sezione su come aggiungere pagine e sezioni.

## Capabilities

### New Capabilities
- `site-navigation`: tab di primo livello, navigazione definita per directory, sidebar limitata al contesto corrente. Requisiti presi **così come sono** dal seed §4.2.

### Modified Capabilities
_Nessuna._ `site-platform` non cambia: lo scenario *Large section* (sidebar della sola sezione corrente) resta valido e continua a essere verificato.

## Riferimenti al design

Implementa `rpsd-doc-site-design.md`:
- **§2.2** — componente Navigazione: `awesome-nav` con `.nav.yml` per directory; `navigation.expand` resta disattivato.
- **§4.1** — tab di primo livello del primo step: Home | NeTEx | SIRI | Indicatori | Guida operativa.
- **§4.3** — navigazione per directory: la radice elenca i tab; aggiungere una cartella non richiede modifiche a `mkdocs.yml` né alle altre sezioni.

## Tipo di intervento

**Infrastruttura del sito**, più quattro pagine redazionali segnaposto (solo titolo e "Sezione in preparazione"), che i change 4–9 sostituiscono. Nessun contenuto generato.

## Decisioni prese in fase di proposta

- **Pagine segnaposto pubblicate** per le quattro sezioni, così i tab sono visibili subito (scelta di Franco).
- **`navigation.prune` non adottato per ora** (scelta di Franco): con prune le pagine fuori da una sezione grande si alleggeriscono molto (da 152 KB a 34 KB nella prova con 400 pagine), ma i rami chiusi della sidebar diventano link invece di espandersi sul posto. Si rivaluta quando arrivano le sezioni generate (catalogo indicatori, contratti).

- **`navigation.sections` tolto** (deciso in apply, scelta di Franco): con la feature i gruppi di secondo livello restano sempre aperti e il requisito *Sidebar limited to the current context* non è soddisfatto. Modifica al design del sito §2.2 (design D7).

Nessun requisito aggiunto rispetto al seed §4.2.

## Fuori scope

- Struttura versionata di NeTEx e SIRI (`netex/5.0.0/`, `siri/1.0.5/`), elenco versioni e sidebar limitata alla versione corrente: change 4 (`profile-versioning`). In quel change il `.nav.yml` di `netex/` e `siri/` elencherà esplicitamente la sola versione corrente.
- Contenuti di Home/Panoramica e delle sezioni: change 5–9. L'aggiunta di `panoramica/` sotto il tab Home richiederà di elencarla nel `.nav.yml` della radice (file di navigazione, non configurazione del sito).
- Tab Contratti e Validazione: secondo step.
- `navigation.prune`, stile della navigazione, override del template.
- Operazioni su GitHub: push del branch e PR solo con approvazione esplicita.

## Impact

- File modificati: `mkdocs.yml` (sezione `plugins`, feature `navigation.sections` tolta), `rpsd-doc-site-design.md` (§2.2), `.github/workflows/pr.yml`, `README.md`, `scripts/check_sidebar.py`.
- File nuovi: `docs/.nav.yml`, `docs/{netex,siri,indicatori,guida}/index.md` e `.nav.yml`, pagine di prova a tre livelli in `spike/docs/`, script di controllo in `scripts/`.
- Dipendenze: nessuna nuova per Zensical (awesome-nav è integrato). In caso di piano B con Material servirebbe il pacchetto `mkdocs-awesome-nav`.
- URL pubblicati nuovi: `/netex/`, `/siri/`, `/indicatori/`, `/guida/`. Sono stabili: i change successivi ne sostituiscono il contenuto, non il percorso.
