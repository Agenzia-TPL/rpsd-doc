# Proposal — bootstrap-site

## Why

`rpsd-doc` oggi contiene solo il documento di design e la configurazione OpenSpec: non c'è un sito costruibile. Il change 1 del seed mette in piedi la piattaforma (Zensical con versione bloccata, `mkdocs.yml`, tema in italiano, build strict, CI di build e deploy) e fa da **spike**: verifica su Zensical ogni funzione di rendering richiesta. È il punto di decisione sullo stack (design §2.1, seed §3): se uno scenario di `site-platform` non è soddisfacibile, ci si ferma e si valuta il piano B (Docusaurus) prima dei change successivi.

## What Changes

- Repository git locale (`git init`, branch `main` con i file esistenti, branch di lavoro `bootstrap-site`). Nessun remote, nessun push.
- `requirements.txt` con Zensical e tutte le dipendenze transitive bloccate a versione esatta; ambiente in `.venv/`; `.gitignore` con `.venv/`, `site/`, `.cache/` e gli output generati dallo spike.
- `mkdocs.yml` (fase 1, letto da Zensical; niente `zensical.toml`): lingua italiana, schema chiaro/scuro, feature del tema e estensioni Markdown del design §2.2, `navigation.expand` disattivato, nessun `nav`.
- `docs/index.md` minimo (segnaposto "sito in costruzione", senza contenuti di dominio: la home vera è del change 5).
- Spike in `spike/`: una pagina di prova per ogni funzione di rendering richiesta dagli scenari (XML annotato, varianti a tab, formule, Mermaid, ricerca in italiano), più uno script che genera 400 pagine sintetiche per lo scenario di scala. Le pagine di prova sono committate ma **non** pubblicate; le 400 pagine sono generate a ogni esecuzione e non committate.
- Script Python di verifica (link interno rotto → build fallita; tempo di build con 400 pagine ≤ 60 s).
- Workflow GitHub Actions **preparati ma non attivati**: build strict su pull request; build strict + deploy su GitHub Pages su push a `main`, con deploy solo se il build riesce. `site_url`/`repo_url` sono segnaposto marcati `TODO`.
- `README.md` con il comando unico di build e i passi manuali su GitHub che restano a Franco.
- Report dello spike con l'esito di ciascun punto (base per la decisione aperta n. 1 del design §10).

## Capabilities

### New Capabilities
- `site-platform`: build riproducibile, deploy automatico, controllo sulle pull request, funzioni di rendering richieste (XML annotato, varianti a tab, formule, diagrammi Mermaid), interfaccia e ricerca in italiano, scala a 400 pagine. Requisiti presi **così come sono** dal seed §4.1.

### Modified Capabilities
_Nessuna_ (non esistono ancora spec in `openspec/specs/`).

## Riferimenti al design

Implementa `rpsd-doc-site-design.md`:
- **§2.1** — scelta di Zensical, versione bloccata, `mkdocs.yml` in fase 1, spike prima di consolidare (punti: formule arithmatex + MathJax, Mermaid, annotazioni su XML, content tab, ricerca in italiano, tempi di build e sidebar con ~400 pagine).
- **§2.2** — componenti (generatore, hosting GitHub Pages, lingua) ed estensioni/feature del tema, con `navigation.expand` disattivato.
- **§6** — struttura del repository, limitatamente a `mkdocs.yml`, `requirements.txt`, `docs/index.md`, `.github/workflows/`, `README.md`. Le altre cartelle (`templates/`, `data/`, sezioni di `docs/`) arrivano con i rispettivi change.

## Tipo di intervento

**Infrastruttura del sito.** Nessun contenuto redazionale di dominio, nessun contenuto generato da `rpsd-tools`. Le pagine dello spike sono pagine di prova non normative, fuori dal sito pubblicato.

## Decisioni prese in fase di proposta

- **Tempo di build accettabile** (seed §5, scenario *Large section*): **≤ 60 secondi** per il build strict con 400 pagine sul runner GitHub `ubuntu-latest`. Il requisito resta formulato come nel seed ("agreed time limit"); il valore concordato è fissato qui e nel design.
- Pagine di prova committate in `spike/`, escluse dal sito pubblicato; 400 pagine sintetiche generate, non committate.
- `site_url`/`repo_url` segnaposto con `TODO`, da fissare alla creazione del repo remoto.
- `git init` solo locale.

Nessun requisito aggiunto rispetto al seed §4.1.

## Fuori scope

- Qualsiasi operazione su GitHub: creazione del repo remoto, push, PR, abilitazione di Pages con sorgente "GitHub Actions", branch protection che rende obbligatorio il check sulle PR. Sono elencati nel README come passi manuali per Franco; gli scenari *Merge to main*, *Failing build* e *Pull request with an error* sono verificati in questo change solo per ispezione dei workflow e con build locali equivalenti, non su GitHub.
- Navigazione per directory, `.nav.yml`, plugin `awesome-nav` e tab di primo livello del sito (change 2, `site-navigation`).
- Plugin `tags`, `glightbox`, `redirects` e controlli sulle convenzioni (change 3–4, quando servono).
- Override del template e comportamento di `.nav.yml` (punti dello spike del design §2.1 non richiesti dagli scenari di `site-platform`).
- Struttura versionata `netex/`, `siri/` e qualsiasi contenuto di dominio (change 4–9).
- Passaggio a `zensical.toml` (fase 2, design §9).
- Sezione Contratti, regole di validazione, contratti riservati (secondo step).

## Impact

- Nuovi file: `mkdocs.yml`, `requirements.txt`, `.gitignore`, `README.md`, `docs/index.md`, `spike/…`, `scripts/…`, `.github/workflows/…`.
- Dipendenze: Python 3 e Zensical (con le estensioni `pymdown-extensions` che porta con sé); MathJax e Mermaid caricati dal browser. Nessuna toolchain Node.
- Rischio principale: Zensical è in beta 0.x; se un requisito non è soddisfacibile, l'apply si ferma e lo riporta (nessun aggiramento).
