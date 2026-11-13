# Proposal — add-profile-versioning

## Why

I profili italiani NeTEx e SIRI evolvono per versioni, e ogni contratto dichiara la versione di profilo di ciascun dataset (design §2.3). Il sito deve quindi documentare più versioni insieme, per percorso, senza duplicare il resto del sito e senza toccare le pagine delle versioni precedenti quando ne esce una nuova. Il change 4 del seed prepara questa struttura prima che arrivino le pagine di profilo (change 6–7).

## What Changes

- Metadati delle versioni di profilo in un unico punto, `mkdocs.yml` (`extra.profili`): per NeTEx e SIRI la versione corrente e lo stato di ogni versione documentata (corrente, precedente, ritirata).
- Cartelle di versione `docs/netex/5.0.0/` e `docs/siri/1.0.5/`, ciascuna con una pagina indice segnaposto.
- `docs/netex/index.md` e `docs/siri/index.md` diventano le pagine elenco versioni: tabella con versione, link, stato, date e sintesi delle differenze. **Date e differenze restano "da completare"** finché le linee guida non sono in `sources/` (scelta di Franco).
- Avviso automatico in testa a ogni pagina di una versione non corrente, con stato e link alla versione corrente, prodotto da un override del template a partire dai metadati: le pagine congelate non si modificano.
- Sidebar di NeTEx e SIRI limitata alla versione corrente (`.nav.yml` di sezione senza `"*"`).
- Alias `netex/corrente/` e `siri/corrente/` verso la versione corrente (plugin `redirects`).
- Controlli in CI: coerenza tra metadati, cartelle, `.nav.yml`, alias ed elenco versioni; avviso presente su tutte e sole le pagine non correnti; versioni non correnti congelate (un commit che le modifica deve dichiararsi errata). Prove con due versioni documentate.

## Capabilities

### New Capabilities
- `profile-versioning`: una cartella per versione di profilo, versioni che coesistono, elenco versioni, avviso sulle versioni non correnti, sidebar sulla versione corrente, alias della corrente. Requisiti presi **così come sono** dal seed §4.4.

### Modified Capabilities
_Nessuna._ Il comportamento di `site-navigation` resta valido: la regola "ogni `.nav.yml` di sezione termina con `"*"`" aveva già l'eccezione prevista per `netex/` e `siri/`.

## Riferimenti al design

Implementa `rpsd-doc-site-design.md`:
- **§2.3** — versioning per percorso: una cartella congelata per versione, `netex/index.md` e `siri/index.md` redazionali con elenco versioni, sidebar sulla sola versione corrente, avviso sulle versioni non correnti, alias `netex/corrente/` via `redirects`.
- **§4.2 e §4.3** — struttura `netex/<versione>/`, `siri/<versione>/`; le sezioni NeTEx e SIRI espongono in sidebar la sola versione corrente.
- **§2.1** — "override del template", punto dello spike rimasto da verificare: verificato qui.

## Tipo di intervento

**Infrastruttura del sito** (metadati, override del template, navigazione, controlli) e **contenuto redazionale minimo**: le due pagine elenco versioni e due pagine indice di versione, con i soli dati certi (numero di versione e stato) e i campi da completare marcati come tali. Nessun contenuto generato.

## Decisioni prese in fase di proposta

- **Campi da completare**: date e sintesi delle differenze marcate "_da completare_" nella tabella delle versioni; nessun dato inventato (scelta di Franco). Il controllo le elenca senza fallire.
- **Avviso tramite override del template**, non scritto nelle pagine: quando una versione diventa non corrente basta aggiornare i metadati, le sue pagine restano invariate.
- **Errata sulle versioni congelate**: un commit che modifica una versione non corrente deve avere il trailer `Errata: <motivo>`, sullo stesso schema del trailer per le cartelle generate.
- **Scheletro minimo**: per ogni versione solo la pagina indice; le sottocartelle (introduzione, fondamentali, frame, servizi, esempi) arrivano con i change 6–7.

Nessun requisito aggiunto rispetto al seed §4.4.

## Fuori scope

- Contenuti dei profili (change 6–7) e testo introduttivo sugli standard nelle pagine elenco versioni (richiede le fonti).
- **Granularità delle cartelle di versione** (decisione aperta 2e del design §10 e seed §5): resta aperta; con una sola versione per profilo non cambia nulla in questo change.
- Alias per le singole pagine della versione corrente (`netex/corrente/frame/...`): il requisito chiede un URL indipendente dalla versione che porti alla versione corrente; l'alias copre la pagina indice. I contratti linkano sempre la versione esplicita (design §2.3).
- Operazioni su GitHub senza approvazione esplicita.

## Impact

- File modificati: `mkdocs.yml` (`theme.custom_dir`, `extra.profili`, `redirect_maps`), `docs/netex/index.md`, `docs/siri/index.md`, `docs/netex/.nav.yml`, `docs/siri/.nav.yml`, `.github/workflows/pr.yml`, `CONTRIBUTING.md`, `README.md`.
- File nuovi: `overrides/main.html`, `docs/netex/5.0.0/index.md`, `docs/siri/1.0.5/index.md` (con `.nav.yml`), `scripts/check_versions.py`, `scripts/test_versions.py`.
- URL nuovi: `/netex/5.0.0/`, `/siri/1.0.5/`, `/netex/corrente/`, `/siri/corrente/`.
- Dipendenze: nessuna nuova (PyYAML è già nel lock come dipendenza di Zensical).
