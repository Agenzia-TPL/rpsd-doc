# Design — bootstrap-site

## Context

Motivazione e perimetro: vedi `proposal.md`. Requisiti: `specs/site-platform/spec.md` (seed §4.1 senza modifiche).

Stato attuale: la cartella non è un repository git e contiene solo `CLAUDE.md`, `rpsd-doc-site-design.md` e `openspec/`. Vincoli rilevanti:

- Zensical in beta 0.x, configurazione in `mkdocs.yml` (fase 1); niente `zensical new` (creerebbe `zensical.toml`); si usano solo `zensical serve` e `zensical build --strict`, mai `mkdocs`.
- Solo funzioni presenti sia in Zensical sia in Material for MkDocs (reversibilità, design §2.1).
- Nessuna operazione su GitHub: i workflow si scrivono ma non si eseguono lì.
- Nessun contenuto inventato: le pagine di prova non documentano il profilo.
- Le opzioni vanno confrontate con la documentazione Zensical prima di scriverle (CLAUDE.md). Se Zensical non supporta qualcosa che serve a uno scenario, l'apply si ferma e lo riporta.

### Verifiche fatte in fase di proposta (13 novembre 2026)

Fonti: documentazione Zensical consultata tramite Context7 (`context7.com/zensical/docs`; la home di zensical.org/docs non è leggibile senza JavaScript) = **doc**; prova con Zensical 0.1.1 su Python 3.13 in un ambiente usa e getta, fuori dal repo = **prova**. Ciò che resta da verificare nel browser è marcato ⚠️ e confluisce nei task dello spike.

| Punto | Esito | Fonte |
|---|---|---|
| CLI: `build` con `-f/--config-file`, `-c/--clean`, `-s/--strict`; `--version`; `serve`; `new` | Esistono | prova (`--help`) |
| Link a pagina o anchor inesistente con `--strict` | Rilevati **di default**, senza blocco `validation`; l'output nomina `file:riga:colonna`, evidenzia il link e dice "page does not exist" / "anchor does not exist"; exit 1 | doc + prova |
| Build strict fallito | Scrive comunque `site/` | prova |
| `INHERIT` + `-f` lanciato da un'altra directory | Funziona; `docs_dir`/`site_dir` relativi al file di configurazione figlio; tema e lingua ereditati | prova |
| `theme.language: it` | `lang="it"` e interfaccia in italiano; restano in inglese "Permanent link" (titolo del permalink `toc`), l'etichetta "Tabs" e il messaggio di errore della copia | prova |
| Ricerca | Modulo integrato, attivo di default; la lingua deriva da `theme.language` (non dall'opzione `lang` del plugin); `search.json` ha `lang: ["it"]`. Stemming italiano non documentato | doc + prova |
| `search.highlight` | Documentata: evidenzia le occorrenze dopo il click sul risultato | doc |
| `navigation.tabs/sections/indexes/expand` | Documentate; `navigation.expand` esiste, quindi ometterla ha effetto | doc |
| `content.code.copy`, `content.tabs.link` | Accettate dal build, testi "Copia"/"Copiato" presenti; non trovate nelle pagine consultate ⚠️ | prova |
| `content.code.annotate` | Documentata con marcatore `# (1)!`; il marcatore in commento XML `<!-- (1)! -->` arriva nell'HTML come commento evidenziato e la trasformazione è lato browser ⚠️ | doc + prova |
| `pymdownx.tabbed` (`alternate_style`), fence `mermaid`, `pymdownx.arithmatex` (`generic`) + MathJax | Snippet della doc identici a Material; HTML con `tabbed-set tabbed-alternate`, `pre.mermaid`, `span.arithmatex` | doc + prova |
| Mermaid in schema scuro | Non documentato ⚠️ | — |
| `theme.variant` | Novità Zensical: `classic` conserva l'aspetto di Material, `modern` cambia l'aspetto con la stessa struttura HTML | doc |
| `theme.palette` con toggle | Sintassi documentata (icone `lucide/*`) | doc |

## Goals / Non-Goals

**Goals**
- Un `mkdocs.yml` che sia già la configurazione definitiva di tema ed estensioni per la parte generale.
- Ogni scenario di `site-platform` verificabile: in CI quando possibile, altrimenti con una verifica manuale documentata nel report dello spike.
- Le pagine di prova usano esattamente la configurazione del sito, non una copia mantenuta a mano.

**Non-Goals**
- Navigazione del sito (`.nav.yml`, awesome-nav, ordine dei tab): change 2.
- Stile personalizzato (`extra.css`), override del template, plugin `tags`/`glightbox`/`redirects`.

## Decisions

### D1. Dipendenze: `requirements.txt` completamente bloccato

`requirements.in` contiene la sola dipendenza diretta (`zensical==0.1.1`, ultima pubblicata alla proposta; se all'apply ne è uscita una successiva si valuta il changelog e si ripetono le verifiche della tabella); `requirements.txt` è il freeze completo (dirette e transitive, `==`) prodotto da un `.venv` pulito con `pip freeze`. CI e contributori installano solo da `requirements.txt`.
*Alternative*: solo `zensical==x` (transitive libere → build non riproducibile, cfr. issue #932 citata nel design); `pip-tools`/`uv lock` (strumento in più; rinviabile).
Python **3.13** fissato in `.python-version` e usato dal workflow. Il freeze di prova contiene: `click`, `Jinja2`, `Markdown`, `MarkupSafe`, `pathspec`, `Pygments`, `pymdown-extensions`, `PyYAML`, `tomli`, `zensical`, `zensical-ui`: le estensioni `pymdownx` arrivano con Zensical, non serve dichiararle.

### D2. Comando di build unico

`zensical build --strict` dalla radice, documentato nel README. Lo scenario *Broken internal link* è coperto dal comportamento di default di Zensical (vedi tabella): **nessun blocco `validation`** in `mkdocs.yml`, per non introdurre chiavi il cui significato differisce tra Zensical e Material.
*Nota per il piano B*: in Material il default sugli anchor non fa fallire `--strict`; in caso di passaggio a Material va aggiunto `validation.anchors: warn`.

### D3. `mkdocs.yml`

- `site_name`, `site_url` e `repo_url` segnaposto con commento `# TODO: fissare alla creazione del repo remoto`. `docs_dir: docs`, nessun `nav`.
- `theme.name: material` (accettato da Zensical e necessario alla reversibilità) con `theme.variant: classic`, così l'aspetto coincide con quello che si avrebbe con Material.
- `theme.language: it`; `theme.palette` con due schemi (chiaro `default`, scuro `slate`) e toggle con la sintassi della doc Zensical, necessario per lo scenario Mermaid in entrambi gli schemi.
- `theme.features`: `navigation.tabs`, `navigation.sections`, `navigation.indexes`, `search.highlight`, `content.code.copy`, `content.code.annotate`, `content.tabs.link`. **`navigation.expand` assente** (design §2.2).
- `markdown_extensions`: `admonition`, `pymdownx.details`, `attr_list`, `md_in_html`, `toc` con `permalink: true` e `permalink_title: Link permanente` (altrimenti resta il titolo inglese), `pymdownx.highlight` (con `anchor_linenums`), `pymdownx.inlinehilite`, `pymdownx.snippets`, `pymdownx.superfences` con fence personalizzato `mermaid`, `pymdownx.tabbed` con `alternate_style`, `pymdownx.arithmatex` con `generic: true`.
- Formule: MathJax caricato via `extra_javascript` con lo schema della doc Zensical: file di configurazione locale `docs/assets/javascripts/mathjax.js` (delimitatori e ri-composizione al cambio pagina) + `https://unpkg.com/mathjax@3/es5/tex-mml-chtml.js`, come da design §2.1. *Alternativa*: KaTeX (più leggero, ma il design indica MathJax). Il caricamento da CDN è accettato: il sito è pubblico e non ha requisiti offline.
- Mermaid: nessun JavaScript aggiunto; il fence `mermaid` (snippet della doc) produce `pre.mermaid` che il tema rende nel browser. Il comportamento in schema scuro non è documentato e si verifica nello spike.
- Ricerca: modulo integrato, **nessuna voce `plugins: search`** e nessuna opzione `lang` (la lingua viene da `theme.language`). Lo scenario chiede che una parola presente nel corpo sia trovata ed evidenziata (`search.highlight`); lo stemming italiano non è richiesto e non è documentato: la pagina di prova verifica anche una forma flessa e il risultato va nel report.

### D4. Spike separato dal sito pubblicato

Struttura:

```
spike/
├── docs/
│   ├── index.md
│   ├── funzioni/            # committato: una pagina per funzione
│   │   ├── xml-annotato.md
│   │   ├── varianti.md
│   │   ├── formule.md
│   │   ├── diagrammi.md
│   │   └── ricerca.md
│   ├── scala/               # GENERATO da scripts/gen_scale_pages.py, ignorato da git
│   └── assets/              # COPIATO da docs/assets/ da scripts/spike.py, ignorato da git
└── mkdocs.yml               # committato: INHERIT: ../mkdocs.yml + site_name, docs_dir, site_dir
```

`spike/mkdocs.yml` contiene solo `INHERIT: ../mkdocs.yml`, `site_name` di prova, `docs_dir: docs` e `site_dir: site` (relativi al file, quindi `spike/docs` e `spike/site`). Lo spike eredita così tema ed estensioni del sito senza copie da mantenere (comportamento verificato, vedi tabella). `scripts/spike.py` copia `docs/assets/` in `spike/docs/assets/` (servono i percorsi di `extra_javascript`) e lancia `zensical build --strict -f spike/mkdocs.yml`.
*Alternative scartate*: copia testuale di `mkdocs.yml` generata da script (più fragile, non più necessaria); pagine in `docs/_spike/` con esclusione dal deploy (finirebbero nell'indice di ricerca del sito pubblico).

Contenuto delle pagine di prova: ciascuna porta in testa un avviso "Pagina di prova — contenuto non normativo". L'XML usa solo un frammento strutturale (`PublicationDelivery` / `dataObjects` / un frame vuoto) senza vincoli o campi del profilo italiano; la formula è un rapporto generico, non un indicatore ART; i diagrammi sono un flowchart e un sequence diagram con nodi neutri. Ogni pagina elenca in fondo cosa verificare a mano (checklist dello scenario).

Pagina per scenario:

| Pagina | Scenario | Verifica |
|---|---|---|
| `xml-annotato.md` | Annotated NeTEx fragment | blocco `xml` con 3 annotazioni `<!-- (1)! -->`: evidenziazione, apertura annotazioni, testo copiato senza marcatori (incollato e confrontato). Verifica **nel browser e bloccante**: se i marcatori in commento XML non diventano annotazioni, si prova il marcatore senza commento e, se neppure quello funziona, lo scenario è non soddisfatto |
| `varianti.md` | Minimal and complete variant | tab "Minimale" / "Completo" con lo stesso esempio |
| `formule.md` | Indicator formula | formula inline `\( … \)` e blocco `$$ … $$`; HTML contiene MathJax renderizzato, non il sorgente |
| `diagrammi.md` | Flow diagram | flowchart + sequence diagram, controllati in schema chiaro e scuro |
| `ricerca.md` | Search for an Italian term | parola italiana con accento e una flessa (es. "validità", "trasmesse") presenti solo in questa pagina |

### D5. Scala: 400 pagine e limite di 60 s

`scripts/gen_scale_pages.py` scrive 400 pagine Markdown deterministiche (titolo, alcuni paragrafi, una tabella, un blocco di codice, link alla pagina precedente/successiva) in `spike/docs/scala/`, ripulendo la cartella a ogni esecuzione. `scripts/spike.py --scale` genera, costruisce e misura il tempo di `zensical build --strict --clean -f spike/mkdocs.yml` (cache svuotata dall'opzione `--clean`; tempo a orologio dell'intero processo), fallendo se supera **60 s** (valore concordato, vedi proposal). Il tempo misurato è riportato in output e nel report.
Sidebar: con `navigation.tabs` le sezioni `funzioni/` e `scala/` diventano tab distinti; la verifica è che una pagina di `funzioni/` non mostri in sidebar le pagine di `scala/`. Il controllo è automatico (lo script cerca nell'HTML di `funzioni/xml-annotato/index.html` l'assenza di link a `scala/`) più una verifica visiva.

### D6. Controllo del link rotto

`scripts/check_broken_link.py` copia `spike/docs` in una directory temporanea, aggiunge una pagina con un link a una pagina inesistente e una seconda con un anchor inesistente, costruisce in strict (`INHERIT` dalla configurazione dello spike) e **si aspetta il fallimento**: exit ≠ 0 e, nell'output ripulito dai codici colore ANSI, il percorso `pagina.md:riga` di ciascuna pagina, il link e i messaggi "page does not exist" e "anchor does not exist". Fallisce se il build riesce o se il messaggio non li nomina. Così lo scenario negativo è verificabile in CI senza committare una pagina rotta.

### D7. Workflow GitHub Actions

- `.github/workflows/pr.yml` — `on: pull_request`; job `build`: setup Python dalla `.python-version`, `pip install -r requirements.txt`, `zensical build --strict`; job `spike`: `scripts/spike.py --scale` e `scripts/check_broken_link.py`. Il fallimento di un job fa fallire il check della PR.
- `.github/workflows/deploy.yml` — `on: push` su `main` (+ `workflow_dispatch`); job `build` come sopra, poi `actions/upload-pages-artifact`; job `deploy` con `needs: build`, `environment: github-pages`, `actions/deploy-pages`; `permissions` minime (`contents: read`, `pages: write`, `id-token: write`); `concurrency` per non sovrapporre deploy. Se `build` fallisce, il job si interrompe prima dell'upload e `deploy` non parte: il sito pubblicato resta invariato. Non ci si affida all'assenza di `site/`, che Zensical scrive anche quando il build strict fallisce.
- Azioni referenziate per tag di versione major.
*Alternativa*: `gh-deploy`/branch `gh-pages` (scarta: è un comando `mkdocs`, e il deploy da artifact non riscrive un branch).

Il design §6 nomina solo `deploy.yml`; il file per le PR è un'aggiunta necessaria al requisito *Pull request preview check*.

Passi che restano a Franco (nel README, non nei task): creare il repo remoto, impostare Pages su "GitHub Actions", proteggere `main` richiedendo i check di `pr.yml`, fissare `site_url`/`repo_url`.

### D8. Git locale

`git init -b main`, primo commit con i file già presenti (`CLAUDE.md`, design, `openspec/`, `.claude/`), poi `git switch -c bootstrap-site` per il lavoro del change. Nessun remote.

## Risks / Trade-offs

- [Un'opzione di Material non è supportata o si comporta diversamente in Zensical] → verifica sulla documentazione Zensical prima di scriverla; se blocca uno scenario, stop e report (possibile piano B).
- [Una release successiva di Zensical cambia il default della validazione o il formato dei messaggi] → D6 lo intercetta in CI a ogni PR; aggiornamenti di versione solo deliberati.
- [Annotazioni nei commenti XML non trasformate dal tema] → verificabile solo nel browser; esito bloccante per *Annotated NeTEx fragment* (possibile piano B).
- [Build strict fallito lascia `site/` parziale] → il deploy dipende dall'esito del job, non dai file presenti (D7).
- [`INHERIT` cambia comportamento in una release 0.x] → lo spike fallirebbe subito; ripiego sulla copia testuale della configurazione.
- [MathJax/Mermaid da CDN non disponibili] → impatto solo sul rendering lato browser; registrato come trade-off accettato.
- [Tempo di build misurato in locale diverso da CI] → il limite di 60 s è vincolante sul runner `ubuntu-latest`; in locale si misura e si riporta, la conferma in CI arriva al primo run su GitHub.
- [Scenari di deploy non eseguibili senza GitHub] → verifica per ispezione dei workflow (e `actionlint` se disponibile via pip/binario, senza Node); dichiarato nel report.
- [Freeze delle transitive vincola anche dipendenze non usate] → aggiornamento deliberato rigenerando il freeze da `requirements.in`.

## Migration Plan

Nessuna migrazione: il sito non esiste. Rollback: eliminare il branch `bootstrap-site`. Se lo spike fallisce su un punto bloccante, il change resta non archiviato e si apre la valutazione del piano B.

## Open Questions

- Se all'apply è disponibile una versione di Zensical successiva alla 0.1.1, la si adotta solo dopo aver ripetuto le verifiche della tabella.
