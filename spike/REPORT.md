# Report dello spike — bootstrap-site

Data: 13 novembre 2026 · Zensical **0.1.1** (zensical-ui 0.0.42) · Python **3.13.3** · Linux

Lo spike verifica su Zensical i requisiti della capability `site-platform`
(`openspec/changes/bootstrap-site/specs/site-platform/spec.md`). Riferimento per la
decisione: design del sito §2.1 e decisione aperta n. 1 del §10.

## Come è stato verificato

- **CI locale**: comandi dei workflow eseguiti in locale (`zensical build --strict`,
  `scripts/spike.py --scale`, `scripts/check_broken_link.py`), gli stessi che girano in `pr.yml`.
- **Browser**: Chrome headless pilotato con Playwright (strumento usato solo per la verifica,
  fuori dal repository), con controlli sul DOM e screenshot in schema chiaro e scuro.
- **Ispezione**: lettura dei workflow e `actionlint` 1.7.12 senza errori.
- **GitHub** (aggiunto dopo l'archive, 13 novembre 2026): primi run dei workflow sul
  repository https://github.com/Agenzia-TPL/rpsd-doc, vedi "Verifica su GitHub" in fondo.

## Esito per scenario

| Requisito | Scenario | Esito | Verifica |
|---|---|---|---|
| Reproducible build | Clean build | ✅ | CI locale: clone pulito, `pip install -r requirements.txt` (lock completo, 11 pacchetti `==`), `zensical build --strict` senza warning |
| Reproducible build | Broken internal link | ✅ | CI locale: `check_broken_link.py`; il build strict esce con 1 e indica per ogni caso `file:riga:colonna`, il link e "page does not exist" / "anchor does not exist". Controllo inverso (`--no-broken`) fallisce come previsto |
| Automated deployment | Merge to main | ✅ | GitHub, 13 novembre 2026: il push su `main` ha avviato `deploy.yml` (run 43417096737), build strict e pubblicazione riusciti; sito online su https://agenzia-tpl.github.io/rpsd-doc/ senza passi manuali |
| Automated deployment | Failing build | ✅ per meccanismo | `deploy` ha `needs: build` e l'upload segue il build. Su GitHub il primo run (43415137989) si è fermato nel job `build` prima dell'upload (Pages non ancora attivo) e non ha pubblicato nulla. Un build strict fallito su `main` non è stato provato di proposito; Zensical scrive `site/` anche quando fallisce, ma il deploy non dipende dalla cartella |
| Pull request preview check | Pull request with an error | ✅ | Protezione di `main` con i due controlli di `pr.yml` obbligatori (impostata il 13 novembre 2026). PR di prova `report-ci`: entrambi i controlli eseguiti sulla PR (dettaglio sotto). Un exit ≠ 0 in uno dei due job fa fallire il controllo e blocca il merge |
| Annotated XML examples | Annotated NeTEx fragment | ✅ | Browser: XML evidenziato, i 3 marcatori `<!-- (n)! -->` diventano annotazioni che si aprono con la propria spiegazione, il testo copiato non contiene marcatori. Nota: resta uno spazio a fine riga dove c'era il commento (bozza di issue 3) |
| Alternative example variants | Minimal and complete variant | ✅ | Browser: tab "Minimale"/"Completo" si alternano, l'URL della pagina non cambia |
| Mathematical formulas | Indicator formula | ✅ | Browser: MathJax compone la formula inline e quella in blocco; nessun sorgente LaTeX visibile |
| Diagrams from text | Flow diagram | ✅ | Browser: flowchart e sequence diagram resi come SVG e leggibili in schema chiaro e scuro |
| Italian interface and search | Search for an Italian term | ⚠️ **parziale** | Browser: la ricerca di "perspicuità" trova la pagina e il termine è evidenziato all'apertura (`search.json` con `lang: ["it"]`). **Ma la finestra di ricerca è in inglese** ("Search", "Close search", "Filters", "1 result"): stringhe fisse nel JavaScript del tema, non traducibili da configurazione. Limitazione nota e voluta da Zensical (issue [#16](https://github.com/zensical/zensical/issues/16), avviso nella documentazione). Accettata da Franco come limite noto |
| Scale | Large section | ✅ | CI locale: 400 pagine generate, build strict pulito (`--clean`) in **2,2 s** (limite concordato 60 s, da confermare sul runner GitHub). Sidebar: controllo automatico (`check_sidebar.py`) e browser: dalla sezione `funzioni/` sono visibili 5 link e nessuno verso `scala/`; da `scala/` 401 link e nessuno verso `funzioni/` |

## Interfaccia in italiano: dettaglio

Con `theme.language: it` sono in italiano etichette di navigazione, indice, toggle dello
schema colori, pulsante "Cerca", "Copia"/"Copiato", titolo del permalink ("Link permanente",
impostato in `mkdocs.yml`). Restano in inglese:

| Stringa | Dove | Rimedio |
|---|---|---|
| "Search", "Close search", "Filters", "N result(s)" | finestra di ricerca | nessuno da configurazione; localizzazione rinviata da Zensical per scelta (issue #16): nessuna issue da aprire |
| "Tabs" | `aria-label` dei tab di navigazione | traduzione mancante nel tema; bozza di issue 2 |
| "Could not copy to clipboard" | errore della copia | traduzione mancante nel tema; bozza di issue 2 |
| "Made with Zensical" | footer | si toglie con `extra.generator: false` (stessa opzione di Material): da decidere nella revisione grafica |

## Differenze rispetto a Material for MkDocs

- Ricerca: modulo integrato con interfaccia propria (dialogo in shadow DOM); la lingua viene da
  `theme.language`, non dall'opzione `lang` del plugin.
- Pulsante di copia: `button.md-code__button[data-md-type=copy]` invece di `button.md-clipboard`
  (rilevante per eventuali CSS o test futuri).
- Validazione: link e anchor rotti sono errori in strict per default; in Material il default
  sugli anchor non fa fallire il build (va aggiunto `validation.anchors: warn` in caso di piano B).
- `theme.variant: classic` è specifico di Zensical (Material lo ignora).
- `INHERIT` e `-f/--config-file` funzionano come in MkDocs.

## Osservazioni per i change successivi

- **Peso delle pagine**: con `navigation.tabs` ogni pagina contiene nell'HTML la navigazione di
  tutte le sezioni (circa 150 KB per pagina con 400 pagine in una sezione; 62 MB per lo spike
  completo). Lo schermo mostra solo la sezione attiva, quindi lo scenario è soddisfatto, ma per
  il change 2 (`add-directory-navigation`) conviene valutare `navigation.prune`, documentata da
  Zensical e presente anche in Material.
- **Ricerca**: trova la pagina anche con forme vicine ("inoltrata", "inoltrare" per "inoltrate"),
  probabilmente per corrispondenza di prefisso; lo stemming italiano non è documentato.
- **Tempo di build**: 2,2 s per 400 pagine lascia ampio margine per le pagine generate dei
  contratti (secondo step).

## Raccomandazione

**Confermare Zensical.** Tutti gli scenari verificabili localmente sono soddisfatti tranne la
localizzazione della finestra di ricerca, accettata come limite noto. Da ricontrollare a ogni
aggiornamento di Zensical e comunque **entro fine febbraio 2027**, la data di uscita del piano B
fissata nel design §2.1. Gli scenari di deploy e del controllo sulle PR vanno confermati al primo
run su GitHub, dopo i passi manuali del README.

## Verifica su GitHub

| Verifica | Esito |
|---|---|
| Deploy da push su `main` | ✅ run 43417096737: build strict 21 s, pubblicazione 9 s |
| Sito online | ✅ https://agenzia-tpl.github.io/rpsd-doc/ con `lang="it"`; le pagine dello spike non sono pubblicate (`/funzioni/` → 404) |
| Protezione di `main` | ✅ controlli obbligatori "Build strict del sito" e "Spike (scala, sidebar, link rotti)"; push forzati e cancellazione bloccati |
| Controlli sulla PR di prova `report-ci` | in corso |
