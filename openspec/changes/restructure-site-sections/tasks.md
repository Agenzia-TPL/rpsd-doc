# Tasks — restructure-site-sections

Regola generale: solo struttura e segnaposto. Nessun contenuto di dominio senza fonte: dove manca, "_da completare_". Nessun task fa push, apre PR o tocca le impostazioni GitHub.

## 1. Prova di navigazione (D1)

- [x] 1.1 In una cartella di prova nello scratchpad, fuori dal repository, costruire con `zensical build --strict` un `.nav.yml` della radice con il gruppo `Rapsodia: [index.md, rapsodia/progetto.md, rapsodia/glossario.md, rapsodia/novita.md]`. Verificare che le pagine compaiano piatte nella sidebar del tab e che `/` e `/rapsodia/progetto/` rendano attivo il tab Rapsodia. Se non funziona, adottare il ripiego di D1 e annotarlo in design.md.

## 2. Sezioni e pagine segnaposto

- [x] 2.1 Riscrivere `docs/.nav.yml` con i nove tab nell'ordine della spec (Rapsodia, Architettura, NeTEx, SIRI, Indicatori, Modello dati, Dashboard, Guida operativa, Contratti), mantenendo il commento sull'elenco esplicito. Verifica: build strict senza warning.
- [x] 2.2 Creare `docs/rapsodia/` con `progetto.md`, `glossario.md` e `novita.md`, segnaposto con callout `note` "Sezione in preparazione" (D5). Riscrivere `docs/index.md` come indice del sito, senza il callout "Sito in costruzione": frase su Rapsodia dal README, un link per tab con una riga di descrizione. Verifica: ogni link della home funziona nella build strict.
- [x] 2.3 Creare `docs/architettura/` con `index.md` (definizione generale "_da completare_" ed elenco dei tre sottosistemi con link), `core.md`, `app.md`, `iot.md` e `.nav.yml` (index, core, app, iot, `"*"`). `core.md` ha la sezione "Moduli funzionali" con la tabella Modulo / Cosa fa / Repository senza righe e un callout `note` "da completare" (D2). Verifica: sidebar del tab con le quattro voci in ordine.
- [x] 2.4 Creare `docs/modello-dati/` e `docs/dashboard/` con `index.md` segnaposto e `.nav.yml` (`index.md` + `"*"`). Verifica: build strict, tab attivo corretto.
- [x] 2.5 Creare `docs/contratti/index.md`, redazionale: elenco dei contratti con la sola riga del segnaposto `esempio` e il link. Creare `docs/contratti/.nav.yml` (`index.md` + `"*"`) e `docs/contratti/esempio/index.md` con `segnaposto: true` nel front matter e il callout `warning` "Contratto segnaposto". Verifica: `/contratti/` e `/contratti/esempio/` costruiti.

## 3. Percorsi generati e controlli (D3, D4)

- [x] 3.1 Aggiornare `generated-paths.txt`: `docs/contratti/*/` al posto di `docs/contratti/`, più la riga `!docs/contratti/esempio/` con il commento. In `check_conventions.py` gestire `*` (un segmento) ed esclusioni `!` in G1, G2 e G3 (pathspec `:(exclude)`), e aggiungere G4 (`segnaposto: true` e callout "Contratto segnaposto" nei percorsi esclusi). Verifica: `python scripts/check_conventions.py --commits origin/main` senza errori.
- [x] 3.2 Aggiungere a `test_conventions.py` i casi di D6: indice dei contratti redazionale accettato, pagina a mano in un contratto non dichiarato rifiutata, segnaposto senza `segnaposto: true` rifiutato, riga senza `*` invariata. Verifica: `python scripts/test_conventions.py` passa.
- [x] 3.3 Aggiornare `check_navigation.py`: `EXPECTED_TABS` con i nove tab; `PAGES` con `/` e `rapsodia/progetto/` → Rapsodia, e l'indice di architettura, modello-dati, dashboard e contratti → tab corrispondente (D6). Verifica: `python scripts/check_navigation.py` passa sul sito costruito e fallisce se si inverte l'ordine di due tab in `docs/.nav.yml` (prova manuale, poi ripristino).
- [x] 3.4 Aggiornare `CONTRIBUTING.md` (percorsi generati: indice redazionale, segnaposto, G4) e `README.md` (tab elencati, descrizione dei controlli). Verifica: `python scripts/check_conventions.py` passa e i comandi citati esistono.

## 4. Documenti di progetto

- [x] 4.1 Aggiornare `rpsd-doc-site-design.md`: §4.1 (tab), §4.2 (Rapsodia e Architettura al posto di Home/Panoramica, con sottosistemi Core A+D, App B, IoT C), §4.4 (Modello dati come tab), §5.2 (`contratti/index.md` redazionale, segnaposto `esempio`), §6 (struttura di `docs/`); aggiungere una voce in §0 "Cosa cambia". Verifica: nessun riferimento residuo a `panoramica/` (`grep -n panoramica rpsd-doc-site-design.md`).
- [x] 4.2 Aggiornare `openspec/seed.md`: §3 (change 5 riformulato sui contenuti di Rapsodia, Architettura, Modello dati e Dashboard; questo change inserito prima del 5) e §4.6 `overview` (requisiti riferiti alle nuove pagine; l'architettura descritta per sottosistemi e moduli). Le modifiche ai requisiti di `overview` vanno solo riportate a Franco, che le approva. Verifica: `openspec validate restructure-site-sections --strict`.
- [x] 4.3 Aggiornare `CLAUDE.md` (elenco dei percorsi generati: `docs/contratti/<id>/`, indice redazionale) e `openspec/config.yaml` (Contratti: tab e indice presenti, contenuto generato al secondo step). Verifica: rilettura del diff.

## 5. Verifica finale

- [x] 5.1 `zensical build --strict` senza warning; tutti i controlli di `pr.yml` eseguiti in locale (`check_navigation`, `check_conventions --commits origin/main`, `check_urls origin/main`, `check_versions`, `test_conventions`, `test_versions`). Verifica: tutti a zero errori.
- [x] 5.2 Screenshot con Chrome headless di home, Architettura (con Core), Contratti e `contratti/esempio/` a 1300 px, più la testata a 1024 px (D7). Verifica: nove tab leggibili su una riga a 1300 px; se no, riportare le opzioni a Franco senza scegliere.

## Workflow follow-up

- Revisione di Franco, poi commit sul branch `restructure-site-sections`.
- Push, PR e merge solo con approvazione esplicita di Franco.
- `/opsx:archive` dopo il merge.
