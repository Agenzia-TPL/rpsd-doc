# Proposal — add-generated-profile-pages

## Why

`rpsd-tools profile-docs generate` produce ora, per il profilo NeTEx 5.0.0 e il profilo SIRI 1.0.5, un bundle di dati (`site.yaml`) con tutte le tabelle per frame e per servizio, le strutture comuni, le enumerazioni e le incongruenze fra linee guida 5T e XSD, con ancore stabili (change `add-profile-site-bundle` di rpsd-tools, 18/11/2026). Le cartelle `docs/netex/5.0.0/` e `docs/siri/1.0.5/` contengono ancora solo il segnaposto «Sezione in preparazione». Il 16/11/2026 Franco ha deciso che le pagine si producono in rpsd-doc, con template Jinja del sito, dal bundle committato in `data/`, e che le incongruenze si pubblicano finché la piattaforma non va in produzione.

Fonte: `openspec/brief-pagine-profilo-da-rpsd-tools.md`.

## What Changes

- **Bundle committato**: `site.yaml` del NeTEx in `data/profili/netex/5.0.0/` e del SIRI in `data/profili/siri/1.0.5/`, copiati da rpsd-tools. Il commit porta il trailer `Generato-da: rpsd-tools <versione>` preso da `generator` del bundle (oggi `rpsd-tools 0.6.0`).
- **Template Jinja** in `templates/profili/`: Panoramica, pagina di frame o servizio, Strutture comuni, Enumerazioni, Incongruenze, `.nav.yml`. Riproducono la forma del Markdown di riferimento di rpsd-tools: tabelle in cascata, riquadro chiuso «Altri campi dell'XSD», ancore `{#…}` del bundle, front matter `generato: true` e `generato_da`.
- **Script** `scripts/generate_profile_pages.py <bundle> <cartella>`: legge il bundle, applica i template, sostituisce per intero la cartella della versione. Deterministico. Con `--check` confronta senza scrivere; gira in CI su ogni PR.
- **Pagine generate**: `docs/netex/5.0.0/` (Panoramica, 8 frame, Strutture comuni, Enumerazioni, Incongruenze) e `docs/siri/1.0.5/` (Panoramica, SIRI-VM, -ET, -SX, -FM, -PT, Riferimenti alla corsa, Enumerazioni, Incongruenze) al posto del segnaposto.
- **`generated-paths.txt`**: aggiunti `docs/netex/*/` e `docs/siri/*/`. Da qui in poi ogni commit su quelle cartelle porta il trailer.
- **Avviso sulle versioni non correnti**: nessun lavoro nuovo. Il brief (punto 5) chiede di metterlo nel template, ma l'override `overrides/main.html` del change `add-profile-versioning` lo aggiunge già a ogni pagina sotto `<profilo>/<versione>/`, generata o no. Si verifica solo che valga anche per le pagine generate.
- **Documenti di progetto**: design §3 (lo strumento non è `rpsd-profile-gen` ma il bundle di `rpsd-tools profile-docs` più lo script di rpsd-doc; il motore dei template è in rpsd-doc) e seed §3, §4.5, §5 (change 6 e 7 ridotti alla parte redazionale; questo change inserito prima).

Il contenuto è **generato**; i template, lo script, i controlli e i documenti di progetto sono **infrastruttura del sito**. Nessuna pagina redazionale nuova.

### Decisioni prese qui (proposte del brief, da confermare in revisione)

- Una sola change per NeTEx e SIRI, perché il meccanismo è lo stesso (brief, decisione aperta 1).
- Il ResourceFrame resta una pagina sola: si prova sul sito e, se è scomoda, si riporta a Franco senza dividerla (decisione aperta 2).
- Nessun callout «Novità Rapsodia» o «Obbligatorio per KPI»: il bundle non ha i dati (decisione aperta 3).

## Capabilities

### New Capabilities
- `profile-docs`: pagine dei profili NeTEx e SIRI per versione. In questa change entrano dal seed §4.5 solo *One page per frame and per service* (scenario SIRI adattato, vedi sotto) e, come chiede il seed §5, un requisito analogo a *Generated catalog*. **Requisiti aggiunti rispetto al seed**: tabelle dei campi per oggetto, ancore stabili, pagina delle incongruenze. I requisiti del seed *Uniform page structure*, *Extensions are distinguishable*, *Runnable examples* e *Fundamentals* restano alle change 6–7 (parte redazionale) o a change successive.

**SIRI-SM**: lo scenario *SIRI services* del seed lo elencava, ma il profilo italiano del 5T non lo descrive. Le linee guida SIRI IT 1.0.5 lo citano solo nell'elenco dei servizi dello standard CEN (cap. 3); il profilo italiano (cap. 5) descrive VM, ET, SX, FM e PT. La spec segue il profilo 5T e il seed è stato corretto.

### Modified Capabilities
_Nessuna._ `content-conventions` (*Generated pages are identifiable*) e `profile-versioning` (*Non-current version notice*, *Sidebar shows the current version*) coprono già il comportamento; cambiano solo i percorsi elencati in `generated-paths.txt`.

## Impact

- Nuovi: `data/profili/`, `templates/profili/`, `scripts/generate_profile_pages.py`, test dello script.
- Modificati: `docs/netex/5.0.0/`, `docs/siri/1.0.5/`, `generated-paths.txt`, `.github/workflows/pr.yml` (passo di confronto pagine/bundle), `CONTRIBUTING.md`, `README.md`, `rpsd-doc-site-design.md`, `openspec/seed.md`, `CLAUDE.md`.
- Dipendenze: Jinja2 e PyYAML sono già in `requirements.in`.
- Peso: circa 1,2 MB di bundle e 500 KB di Markdown in più nel repository.

## Out of scope

- Alias `corrente/<pagina>/` per le pagine di frame e servizio: oggi `corrente` reindirizza solo la Panoramica (design D4).

- Pagine redazionali «Informazioni generali» di NeTEx e SIRI (introduzione, concetti, esempi commentati): change 6 e 7 ridotte.
- Tabella delle versioni con date e differenze in `docs/netex/index.md` e `docs/siri/index.md`: manca la fonte.
- Callout riservati alimentati dai requisiti degli indicatori: richiede una change di rpsd-tools.
- Qualsiasi modifica a rpsd-tools e `data.yaml` (non serve al sito).
- Contratti e regole di validazione (secondo step).
