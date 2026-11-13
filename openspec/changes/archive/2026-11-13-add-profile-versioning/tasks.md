# Tasks — add-profile-versioning

Lavoro sul branch locale `add-profile-versioning`. Se un requisito non è soddisfacibile con Zensical, fermarsi e riportarlo. Nessun dato inventato: date e differenze restano "_da completare_". Nessun push, PR o modifica di impostazioni GitHub senza approvazione esplicita di Franco.

## 1. Metadati e struttura

- [x] 1.1 Aggiungere `extra.profili` a `mkdocs.yml` (design D1) con NeTEx 5.0.0 e SIRI 1.0.5 correnti; verifica: build strict senza warning
- [x] 1.2 Creare `docs/netex/5.0.0/` e `docs/siri/1.0.5/` con `index.md` segnaposto e `.nav.yml` (design D2); verifica: pagine costruite sotto `site/netex/5.0.0/` e `site/siri/1.0.5/` — scenario *Current NeTEx profile*
- [x] 1.3 Riscrivere `docs/netex/index.md` e `docs/siri/index.md` come pagine elenco versioni (design D2), con date e differenze "_da completare_"; verifica: `check_conventions.py` verde (callout ammessi, lunghezza)

## 2. Navigazione, alias, avviso

- [x] 2.1 Aggiornare `docs/netex/.nav.yml` e `docs/siri/.nav.yml` con la sola versione corrente, senza `"*"` (design D4); verifica: `check_navigation.py` verde e sidebar di NeTEx con la sola 5.0.0
- [x] 2.2 Aggiungere a `redirect_maps` gli alias `netex/corrente/` e `siri/corrente/` (design D4); verifica: `site/netex/corrente/index.html` rimanda a `../5.0.0/` — scenario *Link from the operational guide*
- [x] 2.3 Creare `overrides/main.html` e `theme.custom_dir` (design D3); verifica: build strict senza warning, nessun avviso sul sito attuale (tutte le versioni correnti) — scenario *Page of a previous version* (verificato con due versioni nel gruppo 3). Nota dall'apply: adattati spike e script che costruiscono copie del sito (design D9)

## 3. Controlli e prove

- [x] 3.1 Scrivere `scripts/check_versions.py` con le regole V1–V7 (design D6); verifica: verde sul repository e sul sito costruito, con elenco dei campi "_da completare_"
- [x] 3.2 Scrivere `scripts/test_versions.py` (design D7) con la fixture a due versioni costruita con Zensical e i casi non conformi; verifica: tutte le prove verdi, una per scenario del requisito più i casi non conformi di V1–V5 e V7 — scenari *New profile version published*, *Reader looks for an older version*, *Page of a previous version*, *Two versions documented*
- [x] 3.3 Aggiornare `.github/workflows/pr.yml` (design D8), nomi dei job invariati; verifica: `actionlint` senza errori e comandi eseguiti in locale nello stesso ordine con esito positivo

## 4. Documentazione

- [x] 4.1 Aggiornare `CONTRIBUTING.md` (procedura del design D5, trailer `Errata`) e `README.md` (nuovi comandi); verifica: i comandi citati esistono e girano come scritti

## 5. Verifica finale

- [x] 5.1 Da clone pulito del branch: build strict e tutti i controlli e le prove della CI; controllo nel browser di `netex/`, `netex/5.0.0/`, `netex/corrente/` e, sulla fixture a due versioni, di una pagina della versione precedente con l'avviso; verifica: esiti attesi, nessun warning
- [x] 5.2 Commit sul branch `add-profile-versioning` (nessun push); verifica: `git status` pulito

## Workflow follow-up

- `/opsx:verify`, `/opsx:archive` con il riepilogo di come è stato verificato ciascun requisito.
- Con approvazione di Franco: push, PR verso `main`, merge con controlli verdi, verifica del sito.
- Quando le linee guida saranno in `sources/`: completare date e differenze nelle pagine elenco versioni.
