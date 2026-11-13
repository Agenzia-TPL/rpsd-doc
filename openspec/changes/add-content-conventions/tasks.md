# Tasks — add-content-conventions

Lavoro sul branch locale `add-content-conventions`. Se un requisito non è soddisfacibile con Zensical, fermarsi e riportarlo. Nessun push, PR o modifica di impostazioni GitHub senza approvazione esplicita di Franco.

## 1. Cartelle generate e pagine generate

- [x] 1.1 Creare `generated-paths.txt` (design D1) e aggiornare il percorso della matrice in `rpsd-doc-site-design.md` §6 e in `CLAUDE.md` (`docs/indicatori/matrice/`); verifica: i tre file citano gli stessi percorsi
- [x] 1.2 Scrivere `scripts/check_conventions.py` con lettura di `generated-paths.txt`, parser del front matter e regole G1, G2 e G3 (`--commits <base>`) del design D2; verifica: sul repository attuale G1/G2 passano e G3 su `origin/main..HEAD` passa (nessun commit tocca cartelle generate) — scenario *Hand edit of a generated page*

## 2. Lunghezza, callout, glossario

- [x] 2.1 Aggiungere a `check_conventions.py` la regola L1 (design D3); verifica: tutte le pagine attuali sotto 1500 parole, conteggio stampato — scenario *Oversized page*
- [x] 2.2 Aggiungere la regola C1 (design D5) e cambiare le cinque pagine segnaposto da `info` a `note`; verifica: `check_conventions.py` verde e `zensical build --strict` senza warning — scenario *Field required for an indicator* (forma del callout)
- [x] 2.3 Aggiungere la regola S1 (design D6); verifica: con il glossario assente il controllo lo dichiara e passa — scenario *Acronym in a page*

## 3. URL stabili

- [x] 3.1 Aggiungere a `mkdocs.yml` il plugin `redirects` con `redirect_maps` vuoto; verifica: build strict senza warning
- [x] 3.2 Scrivere `scripts/check_urls.py <base>` (design D4); verifica: `python scripts/check_urls.py main` passa sul branch (nessun URL perso) — scenario *Page moved*

## 4. Prove dei controlli

- [x] 4.1 Scrivere `scripts/test_conventions.py` (design D7) con casi conformi e non conformi per G1, G2, G3, L1, C1, S1 e per lo spostamento di pagina con e senza redirect; verifica: `python scripts/test_conventions.py` verde, e ogni caso non conforme fallisce con il messaggio atteso

## 5. CI e documentazione

- [x] 5.1 Aggiornare `.github/workflows/pr.yml` (design D8: `fetch-depth: 0`, `check_conventions.py --commits`, `check_urls.py` nel job "Build strict del sito"; `test_conventions.py` nel job "Spike"), nomi dei job invariati; verifica: `actionlint` senza errori e comandi eseguiti in locale nello stesso ordine con esito positivo
- [x] 5.2 Scrivere `CONTRIBUTING.md` (design D9) e linkarlo dal README insieme ai nuovi comandi; verifica: ogni regola rimanda a design del sito, seed o `CLAUDE.md`; `check_conventions.py` non si applica a `CONTRIBUTING.md` (fuori da `docs/`)

## 6. Verifica finale

- [ ] 6.1 Da clone pulito del branch: `zensical build --strict`, `check_navigation.py`, `check_conventions.py --commits main`, `check_urls.py main`, `test_conventions.py`, `spike.py --scale`, `check_broken_link.py`, `check_new_subsection.py`; controllo nel browser della home e di una sezione (callout `note`); verifica: tutti i comandi con l'esito atteso, nessun warning
- [ ] 6.2 Commit sul branch `add-content-conventions` (nessun push); verifica: `git status` pulito

## Workflow follow-up

- `/opsx:verify`, poi `/opsx:archive` con il riepilogo di come è stato verificato ciascun requisito.
- Con approvazione di Franco: push del branch, PR verso `main`, merge con controlli verdi e verifica del sito pubblicato.
