# Tasks — add-generated-profile-pages

Regola generale: nessun contenuto di dominio scritto a mano; tutto viene dal bundle. Nessun task fa push, apre PR o tocca le impostazioni GitHub.

## 1. Bundle

- [x] 1.1 In un checkout di rpsd-tools (`../rpsd-tools`, `main` con `add-profile-site-bundle`) eseguire `uv sync --all-packages` e `profile-docs generate` per `profiles/netex-it` e `profiles/siri-it` in due cartelle dello scratchpad. Verifica: ogni cartella ha `site.yaml` e il Markdown di riferimento elencato nel brief.
- [x] 1.2 Copiare i due `site.yaml` in `data/profili/netex/5.0.0/` e `data/profili/siri/1.0.5/` (D1), senza ancora committarli. Verifica: `generator`, `version` e `xsd` corrispondono al brief (`rpsd-tools 0.6.0`, `netex-it-lev5@cecb0cd`, `siri@v2.2.1`).

## 2. Template e script

- [x] 2.1 Scrivere `scripts/generate_profile_pages.py` (D2): caricamento e controllo delle chiavi, rendering con `StrictUndefined`, scrittura che sostituisce la cartella, `--check`, `--all`. Verifica: `--help` e uscita con errore su bundle senza `pages`.
- [x] 2.2 Scrivere i template in `templates/profili/` sul modello di `render.py` di rpsd-tools (D1, D4): Panoramica, pagina di frame/servizio, Strutture comuni, Enumerazioni, Incongruenze, `.nav.yml`, macro di tabella. Verifica: generazione dei due bundle senza errori.
- [x] 2.3 Confrontare con `diff -r` l'output dei template con il Markdown di riferimento del task 1.1 (D5). Verifica: differenze solo nel marcatore di testa; ogni altra corretta o riportata a Franco.
- [x] 2.4 Scrivere `scripts/test_generate_profile_pages.py` con il bundle minimo di D5. Verifica: il test passa; due generazioni dallo stesso bundle sono identiche byte per byte.

## 3. Pagine, percorsi generati e controlli

- [x] 3.1 Aggiungere `docs/netex/*/` e `docs/siri/*/` a `generated-paths.txt`, con commento (D7). Verifica: `python scripts/test_conventions.py` passa.
- [x] 3.2 Generare `docs/netex/5.0.0/` e `docs/siri/1.0.5/` con `--all`. Verifica: il segnaposto non c'è più; `--all --check` esce con 0; modificando a mano una riga di una pagina, `--check` esce con 1 e nomina il file (poi ripristino).
- [x] 3.3 Aggiungere a `.github/workflows/pr.yml` il passo `python scripts/generate_profile_pages.py --all --check` e il test dello script (D3). Verifica: rilettura del diff; comandi eseguiti in locale.
- [x] 3.4 Aggiornare `CONTRIBUTING.md` (come aggiornare un bundle e rigenerare; le pagine dei profili sono generate; cambio di template su versione non corrente = errata) e `README.md` (nuovo controllo). Verifica: i comandi citati esistono e funzionano.

## 4. Documenti di progetto

- [x] 4.1 Aggiornare `rpsd-doc-site-design.md` §3 (tabella delle origini: bundle di `rpsd-tools profile-docs` + script di rpsd-doc al posto di `rpsd-profile-gen`; per i profili il motore dei template è in rpsd-doc) e §6 (`data/profili/`, `templates/profili/`), con una voce in §0. Verifica: `grep -n rpsd-profile-gen rpsd-doc-site-design.md` non trova nulla.
- [x] 4.2 Aggiornare `openspec/seed.md`: §3 (questa change prima della 6; 6 e 7 ridotte a «Informazioni generali» redazionali), §4.5 (scenario SIRI senza SIRI-SM, se Franco conferma; requisiti aggiunti), §5 (punto change 6–7 risolto). Le modifiche ai requisiti si riportano a Franco. Verifica: `openspec validate add-generated-profile-pages --strict`.
- [x] 4.3 Aggiornare `CLAUDE.md` (percorsi generati: `docs/netex/<versione>/`, `docs/siri/<versione>/`; bundle in `data/profili/`). Verifica: rilettura del diff.

## 5. Verifica finale

- [x] 5.1 `zensical build --strict` senza warning; tutti i controlli di `pr.yml` in locale (`check_navigation`, `check_conventions`, `check_urls origin/main`, `check_versions --site site`, `generate_profile_pages --all --check`, `test_conventions`, `test_versions`, `test_generate_profile_pages`). Verifica: tutti a zero errori.
- [x] 5.2 Controllo delle pagine rese con Chrome headless: sidebar di NeTEx 5.0.0 (otto frame più Panoramica, Strutture comuni, Enumerazioni, Incongruenze) e di SIRI 1.0.5; in TimetableFrame il link da ServiceJourney ai passing times e il riquadro «Altri campi dell'XSD»; un link «⚠ Incongruenza» che apre `issues.md` alla voce giusta; un'ancora della Panoramica tramite `netex/corrente/` (alias solo della Panoramica, design D4); ricerca di un nome di campo. Verifica: tutto come da spec.
- [x] 5.3 Provare lo scorrimento di ResourceFrame e `issues.md` del NeTEx e misurare il tempo di build. Verifica: esito riportato a Franco, senza dividere le pagine.

## Workflow follow-up

- Revisione di Franco, poi due commit sul branch `add-generated-profile-pages` (D7): infrastruttura, poi bundle e pagine con trailer `Generato-da: rpsd-tools 0.6.0`.
- Push, PR e merge solo con approvazione esplicita di Franco.
- `/opsx:archive` dopo il merge.
