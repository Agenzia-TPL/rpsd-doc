# Tasks — bootstrap-site

Regola generale: le opzioni di `mkdocs.yml` sono già state confrontate con la documentazione Zensical (tabella "Verifiche" in design.md); ogni opzione non in tabella va confrontata con https://zensical.org/docs/ prima di scriverla. Se uno scenario di `site-platform` non è soddisfacibile con Zensical, fermarsi e riportarlo (nessun aggiramento). Nessun task fa push, apre PR o tocca impostazioni GitHub.

## 1. Repository e ambiente

- [ ] 1.1 `git init -b main`, commit iniziale dei file esistenti (CLAUDE.md, design, `openspec/`, `.claude/`), poi `git switch -c bootstrap-site`; verifica: `git branch` mostra `main` e `bootstrap-site` attivo, `git remote` vuoto
- [ ] 1.2 Creare `.gitignore` con `.venv/`, `site/`, `.cache/`, `spike/site/`, `spike/docs/scala/`, `spike/docs/assets/` (`spike/mkdocs.yml` invece è committato); verifica: `git status` dopo i passi successivi non mostra questi percorsi
- [ ] 1.3 Fissare Python 3.13 in `.python-version`, creare `.venv/`, scrivere `requirements.in` con `zensical==0.1.1` (o una successiva solo dopo aver ripetuto le verifiche del design), installarlo e produrre `requirements.txt` con `pip freeze` (tutte le versioni `==`); verifica: in un `.venv` nuovo `pip install -r requirements.txt` riesce e `zensical --version` stampa la versione bloccata

## 2. Configurazione del sito e build strict

- [ ] 2.1 Scrivere `mkdocs.yml` secondo design D3 (`theme.name: material` + `variant: classic`, lingua `it`, palette chiaro/scuro, feature senza `navigation.expand`, estensioni con `toc.permalink_title: Link permanente`, nessun blocco `validation`, nessuna voce `plugins: search`, segnaposto `TODO` per `site_url`/`repo_url`, nessun `nav`); verifica: `zensical build --strict` senza warning e nessuna opzione fuori dalla tabella "Verifiche" senza un riscontro sulla doc Zensical
- [ ] 2.2 Aggiungere `docs/assets/javascripts/mathjax.js` (schema della doc Zensical) e in `extra_javascript` il file e `https://unpkg.com/mathjax@3/es5/tex-mml-chtml.js`; verifica: i file compaiono in `site/` dopo il build
- [ ] 2.3 Scrivere `docs/index.md` segnaposto ("sito in costruzione", nessun contenuto di dominio); verifica: `zensical build --strict` termina con exit 0 e nessun warning, `site/index.html` ha `lang="it"`
- [ ] 2.4 Scrivere `README.md` con installazione (`python -m venv .venv`, `pip install -r requirements.txt`), comando unico `zensical build --strict`, anteprima `zensical serve`, comandi dello spike e passi manuali GitHub riservati a Franco; verifica: eseguire i comandi del README su un clone pulito (`git clone` locale in una dir temporanea) senza errori né warning — scenario *Clean build*

## 3. Spike: pagine di prova per le funzioni di rendering

- [ ] 3.1 Scrivere `spike/mkdocs.yml` (`INHERIT: ../mkdocs.yml`, `site_name`, `docs_dir: docs`, `site_dir: site`) e `scripts/spike.py` (design D4: copia `docs/assets/` in `spike/docs/assets/`, lancia `zensical build --strict -f spike/mkdocs.yml`); verifica: con il solo `spike/docs/index.md` il build riesce, produce `spike/site/` con `lang="it"` e lancia lo stesso comando dalla radice e da un'altra directory
- [ ] 3.2 `spike/docs/funzioni/xml-annotato.md`: blocco XML neutro con 3 annotazioni numerate e avviso "Pagina di prova"; verifica nel browser (`zensical serve -f spike/mkdocs.yml`), **bloccante**: XML evidenziato, ogni marcatore `<!-- (n)! -->` diventa un'annotazione cliccabile che apre la sua spiegazione, testo copiato col pulsante incollato in un file senza marcatori; se fallisce, provare il marcatore senza commento e riportare l'esito prima di proseguire — scenario *Annotated NeTEx fragment*
- [ ] 3.3 `spike/docs/funzioni/varianti.md`: tab "Minimale" e "Completo" dello stesso esempio; verifica: passaggio tra i tab senza cambio di URL di pagina — scenario *Minimal and complete variant*
- [ ] 3.4 `spike/docs/funzioni/formule.md`: formula inline e in blocco (rapporto generico, non un indicatore ART); verifica: nel browser formula tipografata, nessun sorgente LaTeX visibile — scenario *Indicator formula*
- [ ] 3.5 `spike/docs/funzioni/diagrammi.md`: un flowchart e un sequence diagram Mermaid; verifica: entrambi resi come grafica in schema chiaro e scuro (toggle) — scenario *Flow diagram*
- [ ] 3.6 `spike/docs/funzioni/ricerca.md` con termini italiani presenti solo lì (accentato e flesso); verifica: interfaccia in italiano (etichette di ricerca, tema; le stringhe rimaste in inglese vanno annotate per il report), `spike/site/search.json` con `lang: ["it"]`, la ricerca dei termini elenca la pagina e il termine è evidenziato all'apertura; annotare se la ricerca di una forma flessa diversa trova la pagina (stemming) — scenario *Search for an Italian term*

## 4. Spike: link rotto e scala

- [ ] 4.1 Scrivere `scripts/check_broken_link.py` (design D6) con un caso pagina inesistente e un caso anchor inesistente; verifica: lo script termina con exit 0 solo se il build strict esce con codice ≠ 0 e l'output, ripulito dai codici ANSI, contiene per ciascun caso `pagina.md:riga`, il link e "page does not exist" / "anchor does not exist"; con le pagine rotte rimosse lo script deve fallire — scenario *Broken internal link*
- [ ] 4.2 Scrivere `scripts/gen_scale_pages.py` (400 pagine deterministiche in `spike/docs/scala/`) e l'opzione `--scale` di `scripts/spike.py` con misura del tempo a orologio di `zensical build --strict --clean -f spike/mkdocs.yml` e soglia 60 s; verifica: esecuzione locale riporta il tempo, exit ≠ 0 se > 60 s
- [ ] 4.3 Aggiungere a `--scale` il controllo automatico sulla sidebar (HTML di una pagina di `funzioni/` senza link a `scala/`) e fare la verifica visiva su una pagina di `scala/` e una di `funzioni/`; verifica: controllo verde e sidebar limitata alla sezione corrente — scenario *Large section*

## 5. Workflow CI (preparati, non eseguiti)

- [ ] 5.1 Scrivere `.github/workflows/pr.yml` (design D7: job `build` strict, job `spike` con `--scale` e `check_broken_link.py`); verifica: ispezione e, se installabile senza Node, `actionlint` senza errori; i comandi dei job eseguiti in locale nello stesso ordine riescono — scenario *Pull request with an error* (per ispezione: un errore fa fallire un job)
- [ ] 5.2 Scrivere `.github/workflows/deploy.yml` (push su `main` + `workflow_dispatch`, `build` → `deploy` con `needs`, upload dell'artifact solo dopo il build riuscito, permessi minimi, `concurrency`); verifica: ispezione e `actionlint` se disponibile; `deploy` non può partire se `build` fallisce e nessun passo dipende dalla sola presenza di `site/` — scenari *Merge to main* e *Failing build* (per ispezione)
- [ ] 5.3 Completare il README con la sezione CI e i passi GitHub manuali (repo remoto, Pages su "GitHub Actions", branch protection con i check di `pr.yml`, `site_url`/`repo_url`); verifica: ogni workflow e ogni passo manuale è citato

## 6. Report e verifica finale

- [ ] 6.1 Scrivere `spike/REPORT.md`: versione Zensical e Python, esito di ciascuno scenario (verificato in CI locale / manualmente / solo per ispezione), tempo di build con 400 pagine, discrepanze rispetto a Material, raccomandazione (conferma Zensical o piano B); verifica: ogni scenario della spec ha una riga
- [ ] 6.2 Build finale da clone pulito: `zensical build --strict` del sito, `python scripts/spike.py --scale`, `python scripts/check_broken_link.py`; controllo delle pagine renderizzate toccate (`site/index.html` e le cinque pagine di `spike/site/funzioni/`); verifica: tutti i comandi con exit atteso, nessun warning
- [ ] 6.3 Commit sul branch `bootstrap-site` (nessun push); verifica: `git status` pulito, `git remote` vuoto

## Workflow follow-up

- Revisione del report dello spike da parte di Franco: decisione aperta n. 1 del design §10 (conferma Zensical o piano B).
- Passi GitHub manuali, solo con approvazione esplicita di Franco: repo remoto, Pages, branch protection, primo run dei workflow (conferma in CI del limite di 60 s e degli scenari di deploy).
- `/opsx:verify`, poi `/opsx:archive` con il riepilogo di come è stato verificato ciascun requisito.
