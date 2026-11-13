# Tasks — add-directory-navigation

Lavoro sul branch locale `add-directory-navigation`. Se uno scenario di `site-navigation` non è soddisfacibile con Zensical, fermarsi e riportarlo. Nessun push, PR o modifica di impostazioni GitHub senza approvazione esplicita di Franco.

## 1. Plugin e navigazione della radice

- [x] 1.1 Aggiungere a `mkdocs.yml` `plugins: [search, awesome-nav]` senza opzioni (design D1); verifica: `zensical build --strict` senza warning e `site/search.json` con `lang: ["it"]`
- [x] 1.2 Scrivere `docs/.nav.yml` con i cinque tab nell'ordine del design D2, senza `"*"`; verifica: build strict senza warning. Nota dall'apply: Zensical ignora in silenzio le voci che puntano a cartelle inesistenti (il build non fallisce); il tab mancante è intercettato da `check_navigation.py` (task 3.1)

## 2. Sezioni segnaposto

- [x] 2.1 Creare `docs/netex/`, `docs/siri/`, `docs/indicatori/`, `docs/guida/` con `index.md` segnaposto (titolo della sezione + admonition `info` "Sezione in preparazione", nessun testo di dominio) e `.nav.yml` con `nav: [index.md, "*"]` (design D3–D4); verifica: build strict senza warning e una pagina per sezione in `site/`. Nota dall'apply: richiede `logs.no_matches: info` per `awesome-nav` (design D1, temporaneo, `TODO` in `mkdocs.yml` e `openspec/seed.md` §5)

## 3. Controlli automatici

- [x] 3.1 Scrivere `scripts/check_navigation.py` (design D5): tab esatti e nell'ordine richiesto, unico tab attivo corretto per la home e per ciascuna sezione; verifica: OK sul sito costruito e FALLITO se in una copia temporanea si inverte l'ordine di due tab in `docs/.nav.yml` — scenario *Reader on any page*
- [x] 3.2 Scrivere `scripts/check_new_subsection.py` (design D5): sottosezione aggiunta in una copia temporanea di `docs/guida/`, presente nella sidebar con il titolo del suo `.nav.yml`, `mkdocs.yml` invariato; verifica: OK, e FALLITO se nella copia si toglie `"*"` dal `.nav.yml` di `guida/` — scenario *New subsection*
- [x] 3.3 Aggiungere `spike/docs/navigazione/` con due rami e una pagina al terzo livello, ciascuna cartella con il proprio `.nav.yml` secondo la convenzione D3; estendere `scripts/check_sidebar.py` con il caso della pagina profonda (antenati espansi, ramo fratello chiuso); verifica: `python scripts/spike.py --scale` verde e controllo visivo nel browser (schermata della pagina profonda) — scenario *Deep page*
- [x] 3.4 Aggiornare `.github/workflows/pr.yml`: `python scripts/check_navigation.py` nel job `build` dopo il build, `python scripts/check_new_subsection.py` nel job `spike`, nomi dei job invariati; verifica: `actionlint` senza errori e comandi dei due job eseguiti in locale nello stesso ordine con esito positivo

## 4. Documentazione

- [x] 4.1 Aggiungere al README la sezione "Navigazione" (design D6) e i nuovi comandi di controllo; verifica: i comandi citati esistono e girano come scritti

## 5. Verifica finale

- [x] 5.1 Build finale da clone pulito del branch: `zensical build --strict`, `python scripts/check_navigation.py`, `python scripts/spike.py --scale`, `python scripts/check_broken_link.py`, `python scripts/check_new_subsection.py`; controllo nel browser delle pagine toccate (home, le quattro sezioni, pagina profonda dello spike) in schema chiaro; verifica: tutti i comandi con l'esito atteso, nessun warning, tab e sidebar come da spec
- [x] 5.2 Commit sul branch `add-directory-navigation` (nessun push); verifica: `git status` pulito

## Workflow follow-up

- `/opsx:verify`, poi `/opsx:archive` con il riepilogo di come è stato verificato ciascun requisito.
- Con approvazione di Franco: push del branch, PR verso `main` (i controlli obbligatori girano sulla PR), merge e verifica del sito pubblicato.
