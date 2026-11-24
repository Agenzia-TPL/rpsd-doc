# Proposal — update-profile-bundles-0-8-0

## Why

I bundle `data/profili/netex/5.0.0/site.yaml` e `data/profili/siri/1.0.5/site.yaml` vengono da rpsd-tools 0.6.0 (change `add-generated-profile-pages`, 18/11/2026). Fino alla 0.7.0 `profile-docs generate` ordinava i sostituti di un `substitutionGroup` secondo l'indirizzo in memoria degli oggetti di xmlschema: lo stesso tag poteva dare un `site.yaml` diverso a ogni esecuzione. La correzione (`fix-profile-docs-determinism`, PR #17 di rpsd-tools, 23/11/2026) ordina i sostituti alfabeticamente dopo l'elemento ed è nella release **0.8.0** (tag `v0.8.0`, 24/11/2026). È la prima release da cui il bundle si rigenera sempre uguale. Il tag `v0.7.0` non la contiene. Con la 0.8.0 le pagine dei profili si riproducono dal tag di una release.

Nome della change: il brief proponeva `update-profile-bundles-0.8.0`, ma OpenSpec non accetta punti nel nome; si usa `update-profile-bundles-0-8-0`.

## What Changes

- I due `site.yaml` sono sostituiti da quelli generati da rpsd-tools `v0.8.0`. Rispetto agli attuali:
  - NeTEx 5.0.0, 70 righe diverse: `generator: rpsd-tools 0.8.0`, più l'ordine dei riferimenti alle attrezzature in una tabella del ResourceFrame. Sono le stesse righe, messe in ordine alfabetico dopo `EquipmentRef`.
  - SIRI 1.0.5, 2 righe diverse: solo `generator`.
  - Restano uguali campi, tabelle, ancore e incongruenze, con gli stessi `id`.
- Pagine rigenerate con `python scripts/generate_profile_pages.py --all`:
  - `generato_da: rpsd-tools 0.8.0` nel front matter di tutte le pagine di NeTEx 5.0.0 e SIRI 1.0.5;
  - l'ordine delle righe in quella tabella di `docs/netex/5.0.0/resource-frame.md`.
- Si rimuove `openspec/brief-pagine-profilo-da-rpsd-tools.md`, già eseguito con `add-generated-profile-pages` e ormai superato. Il brief di questa change si rimuove prima dell'archiviazione.

Tipo di contenuto: solo **generato** (bundle in `data/` e pagine delle cartelle di versione). Nessuna pagina redazionale cambia, e nemmeno template, script, `generated-paths.txt` o infrastruttura. La change applica il design del sito §3 (pagine di profilo generate da rpsd-tools) senza modificarlo. NeTEx 5.0.0 e SIRI 1.0.5 sono le versioni correnti, quindi l'aggiornamento non è un'errata.

## Capabilities

### New Capabilities
_Nessuna._

### Modified Capabilities
_Nessuna._ Nessun requisito di `profile-docs` o di `profile-versioning` cambia: le pagine restano generate dal bundle con il trailer `Generato-da`. Per questo `skip_specs: true`.

## Impact

- `data/profili/netex/5.0.0/site.yaml`, `data/profili/siri/1.0.5/site.yaml`.
- Le pagine generate in `docs/netex/5.0.0/` e `docs/siri/1.0.5/`. Il contenuto per chi legge cambia solo nell'ordine delle righe di una tabella di `resource-frame.md`.
- URL e ancore restano uguali.
- Il commit porta il trailer `Generato-da: rpsd-tools 0.8.0` (controllo G3 in CI).
- Release del sito: la change non comprende una release. Il sito pubblicato cambia solo al prossimo tag `vX.Y.Z`. Franco decide dopo il merge se fare subito una patch 0.1.1 o aspettare la prossima release (vedi design, D4).

## Out of scope

- Modifiche a rpsd-tools: la release 0.8.0 è già fatta.
- Il callout «Obbligatorio per KPI» nei requisiti degli indicatori, che richiede una change di rpsd-tools.
- Le pagine redazionali «Informazioni generali» (change 6 e 7 ridotte).
- La release del sito.
