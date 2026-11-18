# Design — add-generated-profile-pages

## Context

Motivazione e perimetro: `proposal.md`. Requisiti: `specs/profile-docs/spec.md`. Fonte: `openspec/brief-pagine-profilo-da-rpsd-tools.md`.

Stato attuale:

- `docs/netex/5.0.0/` e `docs/siri/1.0.5/` hanno solo `index.md` (segnaposto) e `.nav.yml` (`index.md` + `"*"`). I `.nav.yml` di `docs/netex/` e `docs/siri/` elencano la sola versione corrente e restano invariati.
- `overrides/main.html` aggiunge l'avviso sulle versioni non correnti a ogni pagina sotto `<profilo>/<versione>/`, leggendo `extra.profili` di `mkdocs.yml`. `check_versions.py` lo verifica (V6) sul sito costruito.
- `check_conventions.py` applica G1–G4, L1, C1, S1 sui percorsi di `generated-paths.txt`; G3 chiede il trailer `Generato-da: rpsd-tools <versione>` sui commit che li toccano. `check_versions.py` V2 non ammette pagine fuori dalle cartelle di versione salvo `docs/<profilo>/index.md` (vincolo per le change 6–7, non per questa).
- `mkdocs.yml` ha già `attr_list`, `admonition`, `pymdownx.details`, `md_in_html`. Jinja2 e PyYAML sono in `requirements.in`.
- In rpsd-tools il renderer di riferimento è `packages/rpsd-core/src/rpsd_core/profile_docs/render.py`; lo schema del bundle è `contracts/profile-data.schema.json`. Il Markdown di riferimento, reso dallo stesso `site.yaml`, ha già passato `zensical build --strict` e i controlli G1, G2, G4, L1, C1, S1 in una copia del repository.

## Goals / Non-Goals

**Goals**
- Pagine di NeTEx 5.0.0 e SIRI 1.0.5 generate in rpsd-doc dal bundle committato, con lo stesso contenuto del Markdown di riferimento.
- Rigenerazione deterministica, verificata in CI.

**Non-Goals**
- Pagine redazionali, tabella delle versioni, callout riservati, modifiche a rpsd-tools (vedi proposal).
- Cambiare la forma delle tabelle rispetto al riferimento: la prima versione la riproduce; ritocchi d'impaginazione in change successive.

## Decisions

### D1 — Percorsi

- Bundle: `data/profili/<profilo>/<versione>/site.yaml` (`netex/5.0.0`, `siri/1.0.5`), cioè la proposta del brief. Il primo commento `# GENERATED — DO NOT EDIT …` resta.
- Template: `templates/profili/` (`index.md.j2`, `pagina.md.j2` per frame e servizio, `comuni.md.j2`, `enumerazioni.md.j2`, `incongruenze.md.j2`, `nav.yml.j2`, macro di tabella in `_tabella.md.j2`). Sottocartella `profili/` perché `templates/` servirà anche al catalogo indicatori e ai contratti.
- Pagine: stessi nomi file del riferimento (`resource-frame.md`, `siri-vm.md`, `common.md`, `enumerations.md`, `issues.md`, …): fissano gli URL, che sono stabili. Il nome di ogni pagina viene da `pages[].file` del bundle, non dal template.

Alternativa scartata: `data/` senza `profili/`. Il catalogo indicatori metterà lì altri dati.

### D2 — Script

`scripts/generate_profile_pages.py <bundle> <cartella> [--check]`:

1. carica il bundle con `yaml.safe_load`; verifica le chiavi richieste dallo schema (`pages`, `issues`, `enumerations`, `generator`, `version`, …) ed esce con errore se mancano. Non dipende da rpsd-tools né dal suo JSON Schema: la validazione completa resta a rpsd-tools;
2. rende ogni file in memoria con un `jinja2.Environment(loader=FileSystemLoader("templates/profili"), undefined=StrictUndefined, keep_trailing_newline=True, autoescape=False)`; `StrictUndefined` fa fallire la generazione se un template usa un dato assente;
3. senza `--check`: svuota la cartella e scrive i file; con `--check`: confronta l'insieme dei file e il contenuto, stampa i file diversi, mancanti o in più, ed esce con 1.

Determinismo: ordine solo da liste del bundle (mai da insiemi o dict non ordinati), nessuna data di generazione nel front matter (la data cambierebbe l'output a ogni esecuzione; la versione del generatore basta a ricostruire), fine riga `\n`, UTF-8.

Front matter scritto dal template:
```
---
generato: true
generato_da: <generator del bundle>
---
<!-- GENERATED — DO NOT EDIT · profile-docs <profilo> · <xsd> -->
```

Senza argomenti posizionali (`--all`) lo script percorre ogni `data/profili/*/*/site.yaml` e la cartella `docs/<profilo>/<versione>/` corrispondente: è la forma usata in CI.

### D3 — Controllo in CI

Nuovo passo in `pr.yml`, dopo il build: `python scripts/generate_profile_pages.py --all --check`. Copre gli scenari *Pages out of date*. Un bundle senza cartella, o una cartella di versione con pagine generate senza bundle, è un errore.

Le versioni non correnti sono congelate (V7, trailer `Errata:`). Un cambio di template che modifica le pagine di una versione non corrente si tratta come errata e porta il trailer `Errata:`; si annota in `CONTRIBUTING.md`. Alternativa scartata: template per versione, inutile finché c'è una sola versione per profilo.

### D4 — Ancore e link

Le ancore sono quelle del bundle (`anchor` delle tabelle, `anchor` delle enumerazioni, `id` delle incongruenze); il template non ne calcola. I link sono relativi alla cartella della versione (`timetable-frame.md#…`, `issues.md#…`), quindi restano validi dentro ogni cartella di versione.

L'alias `corrente` (change `add-profile-versioning`) reindirizza solo la Panoramica (`netex/corrente/` → `netex/5.0.0/`) e conserva l'ancora: un link `netex/corrente/#publicationdelivery` funziona, uno a `netex/corrente/timetable-frame/#…` no, perché quella pagina non esiste. Deciso con Franco il 18/11/2026: lo scenario si limita alla Panoramica; i link alle tabelle dei frame usano l'indirizzo con la versione. Gli alias `corrente/<pagina>/` per ogni pagina generata, se serviranno (guida operativa, change 9), sono un change successivo. Il campo `link` delle righe arriva già risolto dal bundle.

Ancore di riga in `issues.md` con HTML in linea `<a id="…"></a>`, come nel riferimento: è HTML grezzo supportato da Zensical e Material.

### D5 — Fedeltà al riferimento

Il test `scripts/test_generate_profile_pages.py` usa un bundle minimo scritto a mano (una pagina, due tabelle in cascata, un campo con incongruenza, un'enumerazione) e verifica: front matter, ancore, riquadro «Altri campi dell'XSD», link all'incongruenza, output identico in due esecuzioni, `--check` che fallisce dopo una modifica.

Per il bundle reale, in fase di apply si confronta l'output con il Markdown di riferimento generato da un checkout di rpsd-tools alla stessa versione (`diff -r`). Le differenze ammesse sono solo nel marcatore di testa; ogni altra si corregge nel template o si riporta a Franco. Il confronto non entra in CI: richiederebbe rpsd-tools.

### D6 — Avviso sulle versioni non correnti

Nessun template: `overrides/main.html` copre già ogni pagina della cartella. Si verifica con `check_versions.py --site site` (V6). Duplicarlo nel template produrrebbe due avvisi.

### D7 — `generated-paths.txt`

Si aggiungono `docs/netex/*/` e `docs/siri/*/`. `docs/netex/index.md`, `docs/siri/index.md` e i `.nav.yml` di `docs/netex/` e `docs/siri/` restano redazionali (stanno nella cartella del profilo, non sotto `*/`). `data/` non è in `generated-paths.txt` (contiene dati, non pagine), ma il commit del bundle porta comunque il trailer.

Ordine dei commit: (1) script, template, test, controlli e documenti; (2) bundle e pagine generate, con il trailer. Così G3 non chiede il trailer a commit che toccano anche file redazionali.

## Risks / Trade-offs

- **Pagine lunghe** (ResourceFrame circa 99 KB, `issues.md` del NeTEx circa 169 KB) → si verificano build, ricerca e scorrimento nel sito; la divisione in sottopagine si riporta a Franco, non si decide qui.
- **Release di rpsd-tools non ancora fatta**: `generator` riporta `rpsd-tools 0.6.0` anche se il bundle viene da PR non rilasciate → accettato dal brief, il sito non è in produzione; alla release si rigenera.
- **Deriva fra template di rpsd-doc e riferimento di rpsd-tools** → il confronto di D5 si ripete a ogni nuovo bundle; i ritocchi voluti si annotano.
- **S1 (glossario) su pagine generate**: le sigle del glossario nelle note del 5T devono essere link al primo uso. Il riferimento passa S1 oggi; se il glossario cresce (change 5) le pagine generate possono fallire S1 → si valuta allora se escludere i percorsi generati da S1.
- **Peso del repository**: circa 1,7 MB per versione fra bundle e pagine; accettabile.
