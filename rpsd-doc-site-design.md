# rpsd-doc — Design del Sito di Documentazione Rapsodia

> Documento di progettazione per il repository `rpsd-doc`.
> Versione: 0.3 — 11 novembre 2026 (sostituisce la 0.2; la 0.1 è di marzo 2026)
> Autore: Franco (con supporto Claude)
> Stato: Bozza per revisione

## 0. Cosa cambia

### Dalla v0.2 alla v0.3

- **Stack deciso: Zensical**, con Docusaurus come piano B e criteri di uscita espliciti (§2.1).
- **Profili NeTEx e SIRI versionati per percorso** (`netex/<versione>/`, `siri/<versione>/`): ogni versione del profilo è una cartella congelata (§2.3, §4.2).
- **Sezione Contratti confermata come direzione ma spostata al secondo step**: la generazione dal config parte quando il modello del config è consolidato (§5).
- **Regole di validazione**: collocazione (catalogo generale o solo nel contratto) da decidere dopo il consolidamento del config; in entrambi i casi le pagine di contratto sono autosufficienti (§4.2).
- **Documentazione dbt**: pubblicata come sito separato e collegata dalla parte generale, non importata (§4.4).

### Dalla v0.1 alla v0.2

| Tema | v0.1 | v0.2 |
|------|------|------|
| Generatore | MkDocs Material | **Zensical** (successore, stesso team); `mkdocs.yml` mantenuto come formato di configurazione nella prima fase |
| Contratti di servizio | Assenti | Nuova sezione **Contratti**: un mini-sito per contratto, interamente generato dal config |
| NeTEx / SIRI | Profilo + pagine "strutture per indicatori ART" + validazione descrittiva | Profilo (generale) + regole di validazione e parametri **per contratto** |
| Indicatori | Catalogo ART unico | Definizione ART **agnostica rispetto al contratto** (generale) + **declinazione per contratto** (soglie, penali, scostamenti) |
| Origine dei contenuti | Tutto scritto a mano | Distinzione netta tra pagine **redazionali** e pagine **generate** (config → `rpsd-tools` → `rpsd-doc`) |
| Navigazione | `nav` monolitico in `mkdocs.yml` | Navigazione per directory (`.nav.yml`), così aggiungere un contratto non tocca la configurazione del sito |
| Versioning | `mike` | Niente `mike`: versioni di profilo per percorso, versione e validità esplicite nelle pagine di contratto |
| Visibilità | Tutto pubblico | Predisposizione per contratti riservati (secondo step) |

Gli obiettivi e le tre audience (§1) restano quelli della v0.1.


## 1. Obiettivi del sito

Il sito `rpsd-doc` è la documentazione ufficiale del progetto Rapsodia.

| Audience | Cosa cerca | Dove lo trova |
|----------|-----------|---------------|
| **Aziende TPL** (Imprese Affidatarie) | Cosa devo trasmettere per il *mio* contratto, con quali regole, e come vengono calcolati i *miei* indicatori | Sezione **Contratti** (punto di ingresso), con rimandi a profili e regole |
| **Agenzie TPL** (Enti Affidanti) | Significato degli indicatori, parametri contrattuali, processo di approvazione | **Indicatori**, **Contratti**, **Guida operativa** |
| **Team tecnico / sviluppatori** | Profili, catalogo regole, definizioni formali | **NeTEx**, **SIRI**, **Validazione**, **Indicatori** |

Principio organizzativo: la parte generale dice **cosa esiste** (profili, regole, definizioni ART); la parte di contratto dice **cosa si applica** (quali dataset, quali regole con quali parametri, quali indicatori con quali soglie). La parte di contratto non ridefinisce nulla: seleziona, parametrizza e, dove serve, dichiara gli scostamenti.

Poiché l'Allegato G rimanda a `rpsd-doc` come Documentazione Tecnica Integrativa, le pagine di contratto hanno valore di riferimento per le Aziende: richiedono **URL stabili**, **versione e data di validità esplicite** e un **changelog**.


## 2. Stack tecnologico

### 2.1 Valutazione: Material for MkDocs o Zensical

Stato dei fatti a novembre 2026:

- Material for MkDocs termina il supporto il **5 maggio 2027**; fino ad allora solo fix critici e di sicurezza ([release 9.8.0](https://newreleases.io/project/pypi/mkdocs-material/release/9.8.0)). Il collaudo di Regione Lombardia è a fine aprile 2027: partendo con Material il sito andrebbe in esercizio su uno stack a fine vita dopo una settimana.
- Zensical **0.1.0** è uscito il 5 novembre 2026 ed è entrato in beta per tre mesi ([release notes](https://github.com/zensical/zensical/pull/1129)); la beta si chiude quindi prima del collaudo. Resta sulla linea 0.x mentre viene definito il sistema di moduli ([nota di novembre](https://zensical.org/upcoming-changes/)).
- Zensical legge nativamente `mkdocs.yml` ([roadmap](https://zensical.org/about/roadmap/)).
- Compatibilità dei plugin previsti nella v0.1 ([pagina di compatibilità](https://zensical.org/compatibility/plugins/)):

| Plugin v0.1 | Stato in Zensical | Decisione v0.2 |
|-------------|-------------------|----------------|
| `search` | Supportato, attivo di default | Tenuto |
| `tags` | Supportato (alcune impostazioni legacy ignorate) | Tenuto |
| `glightbox` | Supportato (alcune impostazioni ignorate) | Tenuto |
| `redirects` | Supportato | Tenuto (serve per la stabilità degli URL) |
| `awesome-nav` | Supportato (no pattern extglob) | **Aggiunto** (vedi §4.3) |
| `macros` | Supportato, ma con comportamento diverso da MkDocs Macros | **Rimosso**: i valori variabili sono risolti in generazione da `rpsd-tools` |
| `git-revision-date-localized` | Non supportato (pianificato) | **Rimosso**: le pagine generate riportano versione config e data di generazione |
| `mike` | Supportato solo tramite [fork](https://github.com/squidfunk/mike) installabile da GitHub, dichiarato soluzione temporanea in attesa del versioning nativo | **Rimosso**: versioni gestite per percorso (vedi §2.3) |
| `gen-files` | Non supportato; l'indicazione è eseguire gli script di generazione separatamente | Non serve: la generazione è già esterna al build |

**Decisione (11 novembre 2026): Zensical.** Motivi: è un progetto nuovo senza nulla da migrare; l'EOL di Material cade a ridosso del collaudo; resta in Python, senza toolchain Node da mantenere; ha le annotazioni nel codice XML; i due plugin non coperti sono sostituiti da scelte di progetto che servono comunque (generazione esterna al build).

Alternative valutate e scartate: Docusaurus (maturo, versioning nativo, ma Node/React, MDX da disattivare per contenuti pieni di tag XML, v4 con breaking change in arrivo), Sphinx + MyST (Python e governance longeva, ma niente annotazioni nel codice e resa meno curata), Hugo + Hextra/Docsy (template Go da imparare), Astro Starlight (Node, pre-1.0), Antora (versioni per componente e sito da più repository, ma AsciiDoc e UI costosa da personalizzare), ProperDocs + Material (il tema termina comunque a maggio 2027).

**Piano B: Docusaurus.** Si adotta se lo spike fallisce su un punto bloccante oppure se a fine febbraio 2027 la beta di Zensical non è chiusa. Il costo del cambio è contenuto perché la sintassi specifica del generatore vive quasi solo nei template di generazione.

Rischi e mitigazioni:

- *Zensical è in beta e sulla linea 0.x.* Versione bloccata in `requirements.txt`, aggiornamenti deliberati. Esiste un precedente di regressione di compatibilità tra release minori ([issue #932](https://github.com/zensical/zensical/issues/932)).
- *Reversibilità.* Nella prima fase la configurazione resta in `mkdocs.yml` e si usano solo funzioni presenti in entrambi i generatori: fino a maggio 2027 lo stesso repo è costruibile anche con Material. Il passaggio a `zensical.toml` si valuta a beta conclusa.
- *Dipendenza minima dal generatore.* Tutto ciò che è specifico di Rapsodia (contratti, regole, indicatori) è Markdown standard prodotto da `rpsd-tools`: cambiare generatore in futuro non tocca la pipeline dei contenuti.

**Da verificare con uno spike prima di consolidare** (non ho verificato questi punti sulla documentazione di Zensical): formule con `pymdownx.arithmatex` + MathJax, diagrammi mermaid, code annotations su XML, content tabs, ricerca in italiano, override del template, tempi di build e resa della sidebar con ~400 pagine generate, comportamento di `.nav.yml` con Zensical e con Material.

### 2.2 Componenti

| Componente | Scelta | Note |
|-----------|--------|------|
| Generatore | Zensical (versione bloccata) | Configurazione in `mkdocs.yml` nella fase 1 |
| Navigazione | `awesome-nav` (`.nav.yml` per directory) | La cartella di un contratto porta con sé la propria navigazione |
| Generazione contenuti | `rpsd-tools` (`doc-gen`) | Esterna al build; scrive Markdown in `rpsd-doc` |
| Hosting | GitHub Pages | Solo contenuti pubblici (vedi §7) |
| Repository | `rpsd-doc` | |
| Lingua | Italiano | |

Estensioni Markdown e feature del tema restano quelle della v0.1 (admonition, superfences/mermaid, tabbed, highlight con annotazioni, arithmatex, attr_list, toc con permalink; navigation tabs, indexes, search highlight, code copy), con due modifiche: **`navigation.expand` va disattivato**, altrimenti la sidebar della sezione Contratti si apre su tutte le pagine di tutti i contratti; **`navigation.sections` è stato tolto** (change `add-directory-navigation`, novembre 2026), perché rende i gruppi di secondo livello sempre aperti e la sidebar mostrerebbe, per esempio, tutte le pagine di tutti i contratti mentre se ne legge uno.

### 2.3 Versioning

Nel sito convivono più assi di versione indipendenti: il profilo NeTEx, il profilo SIRI, ciascun contratto. `mike` (e in generale il versioning di sito) ne gestisce uno solo: versionare tutto il sito a ogni nuovo profilo NeTEx duplicherebbe anche SIRI, indicatori e contratti che non sono cambiati. Per questo le versioni sono gestite **per percorso**, non per sito.

**Profili NeTEx e SIRI**

- Ogni versione di profilo è una cartella: `netex/5.0.0/…`, `siri/1.0.5/…`. All'uscita di una nuova versione si crea una nuova cartella; quella precedente resta online, congelata.
- `netex/index.md` e `siri/index.md` sono pagine redazionali fuori dalle cartelle di versione: cos'è lo standard, elenco delle versioni documentate con stato (corrente, precedente, ritirata), date e sintesi delle differenze.
- La sidebar mostra solo la versione corrente; le altre si raggiungono dall'elenco versioni. Le pagine di una versione non corrente portano un riquadro di avviso con link alla corrente.
- Si apre una cartella solo per le versioni di profilo effettivamente adottate da almeno un contratto, non per ogni rilascio pubblicato.
- Ogni contratto dichiara la versione di profilo di ciascun dataset e linka le pagine di quella versione: due contratti su versioni diverse di profilo convivono senza ambiguità.
- Le pagine di frame e servizio sono in larga parte generate (`rpsd-profile-gen`), quindi una nuova versione costa una nuova generazione più la revisione delle parti redazionali.
- Un percorso `netex/corrente/` come alias della versione corrente (via `redirects`) è utile per i link dalla guida operativa; i contratti linkano sempre la versione esplicita.

**Contratti** — ogni contratto espone versione del config, data di decorrenza e changelog generato (§5.6).

**Sito** — ogni rilascio è un tag git, quindi lo stato a una certa data è sempre ricostruibile.

Il versioning nativo di Zensical, quando disponibile, non cambia questa impostazione.


## 3. Origine dei contenuti

Regola di base: **una pagina è o redazionale o generata, mai mista.** Le directory generate vengono sovrascritte per intero a ogni esecuzione; nessuno le modifica a mano. Se in una pagina di contratto serve del testo descrittivo (note, motivazione di uno scostamento), quel testo sta nel config, non in `rpsd-doc`.

| Sezione | Origine | Strumento |
|---------|---------|-----------|
| Home, Panoramica, Glossario | Redazionale | — |
| NeTEx / SIRI — introduzione, concetti, esempi commentati | Redazionale | — |
| NeTEx / SIRI — pagine di frame e servizio (per versione di profilo) | Generata da XSD + linee guida 5T, con integrazioni redazionali da definire | `rpsd-profile-gen` |
| Indicatori — delibera, CMQ, penali | Redazionale | — |
| Indicatori — catalogo definizioni | Generata dal config | `rpsd-tools` |
| Modello dati | Pagina redazionale + link alla documentazione dbt | `dbt docs` (sito separato) |
| Guida operativa | Redazionale | — |
| Contratti — tutto (secondo step) | Generata dal config | `rpsd-tools` |
| Regole di validazione (secondo step, collocazione da decidere) | Generata dal config | `rpsd-tools` |

### 3.1 Flusso config → rpsd-tools → rpsd-doc

```
rpsd-config (unica fonte di verità)
      │  export
      ▼
bundle di documentazione (YAML)        ← interfaccia stabile, §3.2
      │  doc-gen (template Jinja)
      ▼
rpsd-doc/docs/…  (Markdown generato + .nav.yml)
      │  PR → revisione → merge → build → deploy
      ▼
sito
```

Scelte proposte:

- **Il bundle è l'interfaccia.** `doc-gen` non legge il DB Django del config: legge un export in YAML. Finché il DB non è definito, il bundle è prodotto dai file di input del pilot; quando il DB sarà disponibile cambia solo l'export. Lo schema del bundle va concordato con Davide.
- **Il bundle è committato in `rpsd-doc`** (`data/`) insieme alle pagine che ne derivano: ogni versione pubblicata è riproducibile e il diff del bundle spiega il diff delle pagine.
- **I template stanno in `rpsd-doc`** (`templates/`), il motore in `rpsd-tools`: l'impaginazione è una scelta del sito e deve poter cambiare senza rilasciare `rpsd-tools`.
- **La generazione arriva via pull request**, mai con push diretto: una modifica a soglie o regole di un contratto è un cambiamento con effetti contrattuali e va riletta.
- Ogni pagina generata porta nel front matter `generato: true`, id contratto, versione config e data di generazione, e in testa un riquadro con versione e decorrenza.

### 3.2 Contenuto del bundle (proposta, da allineare al modello del config)

```yaml
versione_config: "…"
generato_il: 2026-12-15
contratto:
  id: "…"                 # slug stabile, usato nell'URL; non si rinomina
  denominazione: "…"
  ente_affidante: "…"
  impresa_affidataria: "…"
  ambito: "…"             # bacino / lotto
  validita: {dal: …, al: …}
  stato: attivo           # in_preparazione | attivo | concluso
  visibilita: pubblico    # pubblico | riservato
  documenti: [{titolo, riferimento, url}]
dataset:                  # dataset richiesti dal contratto
  - id: netex             # netex | siri-pt | siri-et | siri-vm | siri-fm | siri-sx | …
    profilo: "…"
    versione: "…"
    frequenza: "…"
    modalita_trasmissione: "…"
regole:                   # regole attive, con parametri risolti
  - id: "…"               # id stabile del catalogo
    dataset: [netex]      # più di uno = regola cross-dataset
    severita: bloccante   # bloccante | diagnostica
    parametri: {…}
    indicatori: ["…"]     # indicatori che dipendono dalla regola
indicatori:
  - codice: "…"
    granularita: "…"      # grana di calcolo e di aggregazione, dichiarate
    partizione: "…"
    soglia: …
    penale: {…}
    parametri: {…}
    riferimenti_contrattuali: ["…"]
    scostamenti: "…"      # testo, vuoto se l'indicatore segue la definizione ART
changelog: [{versione, data, modifiche}]
```

Catalogo regole e catalogo indicatori (definizioni generali) arrivano con un bundle analogo, non legato a un contratto.


## 4. Struttura del sito

### 4.1 Tab di primo livello

```
Primo step:    Home | NeTEx | SIRI | Indicatori | Guida operativa
Secondo step:  … | Contratti | (Validazione, se si sceglie il catalogo generale)
```

### 4.2 Parte generale

**Home / Panoramica** — introduzione, progetto, architettura di alto livello, modello dati (§4.4), glossario, changelog del sito. Con il secondo step la home aggiunge una card "Contratti" come ingresso principale per le Aziende.

**NeTEx** e **SIRI** — documentazione dei profili italiani e delle estensioni introdotte con 5T, **una cartella per versione di profilo** (§2.3):

```
netex/
├── index.md              # redazionale: lo standard, elenco versioni, differenze
└── 5.0.0/
    ├── introduzione/     # profilo italiano, estensioni, riferimenti normativi
    ├── fondamentali/     # struttura XML, CompositeFrame, convenzioni ID, formati
    ├── frame/            # una pagina per frame
    └── esempi/
siri/
├── index.md
└── 1.0.5/
    ├── introduzione/
    ├── fondamentali/
    ├── servizi/          # una pagina per servizio
    └── esempi/
```

Rispetto alla v0.1:

- **escono** le sezioni "Strutture per indicatori ART" (`netex/art/`, `siri/art/`): il legame struttura → indicatore è espresso dalla matrice indicatori × dataset e, nel secondo step, dai requisiti dati del contratto;
- **esce** la sezione "Validazione" descrittiva per profilo: nel primo step resta una pagina redazionale nella guida operativa su come funziona la validazione (livelli, severità, esiti).

**Regole di validazione — collocazione da decidere dopo il consolidamento del config.** Due ipotesi:

- *A — solo nel contratto.* Le regole compaiono esclusivamente nelle pagine `dati/` del contratto, descritte per intero. Coerente con un config in cui la regola appartiene al contratto.
- *B — catalogo generale + attivazione nel contratto.* Le regole sono definite una volta, con ID stabile, in un tab Validazione; il contratto le attiva e le parametrizza. Ha senso solo se il config modella la regola come definizione riusabile tra contratti, e in particolare se esiste un nucleo di regole di profilo valide per qualunque NeTEx/SIRI (quelle che il validator applica anche in uso stand alone, senza contratto).

In entrambe le ipotesi vale un vincolo: **la pagina di contratto è autosufficiente**, cioè riporta per ogni regola la descrizione completa con i parametri risolti, senza obbligare l'Azienda a consultare un catalogo. La differenza tra A e B è quindi solo l'esistenza della vista generale, che essendo generata può essere aggiunta in seguito senza toccare le pagine di contratto.

La struttura che segue descrive l'ipotesi B.

```
validazione/
├── index.md          # come funziona: livelli (XSD, regole), severità, esiti
├── netex.md          # regole sul dataset NeTEx (suddivise per frame se numerose)
├── siri-pt.md
├── siri-et.md
├── siri-vm.md
├── siri-fm.md
├── siri-sx.md
├── coerenza.md       # regole di coerenza tra dataset (es. NeTEx ↔ SIRI-PT ↔ SIRI-ET)
└── errori-comuni.md  # redazionale
```

Scheda di una regola (una sezione con anchor per regola, es. `validazione/netex/#<id>`):

| Campo | Contenuto |
|-------|-----------|
| ID | Identificativo stabile dal config |
| Tipo | Obbligatorietà · vincolo di valore/formato · coerenza interna · coerenza tra dataset |
| Ambito | Struttura interessata (percorso nel file) |
| Descrizione | Cosa deve essere vero |
| Parametri | Nome, significato, valore di default (i valori per contratto stanno nel contratto) |
| Implementazione | XPath · SQL · Python |
| Indicatori dipendenti | Link al catalogo indicatori |
| Esempio | Frammento conforme e non conforme |

La distinzione tra regole diagnostiche (qualità del dato, feedback al produttore) e regole bloccanti di contratto è spiegata in `index.md`; la severità effettiva è un attributo dell'attivazione sul contratto.

**Indicatori** — la definizione ART, valida per tutti i contratti.

```
indicatori/
├── delibera/         # redazionale: delibera 53/2024, CMQ, livelli minimi e penali
├── catalogo/
│   ├── index.md      # riepilogo generato
│   └── <codice>.md   # una pagina per indicatore, generata
└── matrice/          # indicatori × dataset, generata (index.md, URL /indicatori/matrice/)
```

La pagina di indicatore generale segue il template v0.1 con due vincoli, coerenti con il catalogo: **nessuna soglia numerica e nessun riferimento ad allegati di gara** (solo normativa valida per tutti i contratti, es. delibera ART 53/2024); granularità di calcolo e di aggregazione sempre dichiarate. In fondo, blocco generato "Contratti che applicano questo indicatore" (vedi §7 per il vincolo sui contratti riservati).

Da decidere: se pubblicare anche gli indicatori base e quelli di qualità/trasmissione del catalogo, o solo gli indicatori ART.

**Guida operativa** — resta generale: processo end-to-end, modalità di trasmissione, formati accettati, risoluzione problemi, guida per le Agenzie, FAQ. **Escono** `frequenze.md` e `checklist.md`: frequenze e requisiti sono per contratto e sono generati nella sezione Contratti.

### 4.3 Navigazione

La navigazione è definita per directory con `.nav.yml`. La radice elenca i tab; le sezioni NeTEx e SIRI espongono nella sidebar la sola versione corrente del profilo. Nel secondo step la sezione Contratti include le sottocartelle con un pattern, e ogni cartella di contratto contiene il proprio `.nav.yml` generato: aggiungere il decimo contratto significa aggiungere una cartella, senza modifiche a `mkdocs.yml` né alle altre sezioni.

### 4.4 Modello dati e documentazione dbt

La documentazione del database prodotta da `dbt docs generate` è un'applicazione statica autonoma (una pagina HTML che legge `manifest.json` e `catalog.json`), con propria navigazione, ricerca e grafo di lineage: non è Markdown e non si può fondere nelle pagine del sito. **Si pubblica come sito separato e si collega**, non si importa.

- `panoramica/modello-dati.md` è una pagina redazionale: livelli del modello (raw, staging, intermediate, mart), convenzioni, e link alla documentazione dbt.
- Se la documentazione dbt può essere pubblica, la CI di `rpsd-transform` la pubblica sotto lo stesso dominio (per esempio `/dbt/`), copiando l'output nel sito dopo il build: stesso indirizzo, interfaccia propria.
- Se non può esserlo, resta su un host ad accesso controllato e la pagina riporta il link per chi ha le credenziali. Da valutare prima di pubblicare: la documentazione dbt espone l'intero progetto, compresi schema raw, modelli di staging e codice SQL.
- Evoluzione possibile: se alle Agenzie serve un dizionario dati delle sole tabelle mart usate dalle dashboard, `rpsd-tools` può generarlo in Markdown da `manifest.json` e `catalog.json`. In quel caso le pagine entrano nel sito come contenuto generato, limitate ai modelli esposti.


## 5. Sezione Contratti (secondo step)

> **Stato**: struttura confermata come direzione. L'implementazione parte quando il modello del config è definito e consolidato, perché tutto il contenuto della sezione deriva dal config. Fino ad allora questa sezione è una proposta e può cambiare con il modello.
>
> **Da chiarire**: come documentare il contratto previsto per la consegna di aprile 2027 se a quella data la generazione dal config non è pronta (§10, punto 2).

"Mini-sito" qui significa una sezione dello stesso sito con un proprio prefisso di URL (`/contratti/<id-contratto>/`), una propria sidebar e una pagina indice, raggiungibile dalla parte generale tramite l'elenco contratti e la card in home. Non è un sito o un dominio separato: è lo stesso build. La separazione fisica entra in gioco solo per i contratti riservati (§7).

### 5.1 Una pagina o un mini-sito?

Una pagina sola per contratto non regge: con una trentina di indicatori e le regole di cinque o sei dataset supererebbe di molto il limite di 1500 parole e non offrirebbe URL puntuali da citare (in un esito di validazione, in una comunicazione all'Azienda, nell'Allegato G). Proposta: **ogni contratto è un mini-sito con struttura identica**, la cui pagina indice è "la pagina del contratto" e contiene già il riepilogo di input e output.

Dimensione attesa: circa 40 pagine per contratto, quindi ~400 con dieci contratti. Sostenibile perché sono tutte generate e la sidebar mostra un contratto alla volta.

### 5.2 Struttura

```
contratti/
├── index.md                    # elenco contratti (generato)
└── <id-contratto>/
    ├── .nav.yml                # generato
    ├── index.md                # scheda del contratto
    ├── documenti.md            # documentazione contrattuale
    ├── dati/                   # INPUT
    │   ├── index.md            # requisiti dati: dataset, versioni, frequenze, trasmissione
    │   ├── netex.md            # regole attive sul NeTEx
    │   ├── siri-pt.md          # solo i dataset richiesti dal contratto
    │   ├── siri-et.md
    │   ├── …
    │   ├── coerenza.md         # regole attive tra dataset
    │   └── esempi.md           # file di esempio conformi al contratto
    ├── indicatori/             # OUTPUT
    │   ├── index.md            # riepilogo: indicatore, soglia, penale, granularità
    │   └── <codice>.md         # indicatore declinato sul contratto
    └── changelog.md
```

`contratti/index.md` è una tabella generata: contratto, ente affidante, impresa affidataria, ambito, validità, stato, versione config. Con dieci contratti basta una tabella ordinabile; i contratti conclusi restano in elenco con il loro stato.

### 5.3 Scheda del contratto (`index.md`)

1. Riquadro di testata: versione config, decorrenza, stato.
2. Dati identificativi: parti, ambito, durata.
3. **Input in sintesi**: tabella dei dataset richiesti (profilo, versione, frequenza) con numero di regole attive per severità, e link a `dati/`.
4. **Output in sintesi**: tabella degli indicatori applicati con soglia e link alla scheda.
5. Ultime modifiche (estratto del changelog).

### 5.4 Input: `dati/`

`dati/index.md` è il data contract leggibile: quali dataset, in quale versione di profilo, con quale frequenza e modalità di trasmissione, e la gerarchia tra i flussi come definita per quel contratto. Sostituisce `frequenze.md` della v0.1.

Le pagine per dataset elencano le **regole attive**, raggruppate per struttura (frame NeTEx, entità SIRI):

| Colonna | Contenuto |
|---------|-----------|
| Regola | ID stabile (con link al catalogo generale, se esiste) |
| Cosa richiede | Descrizione completa con i **parametri già risolti** per il contratto |
| Severità | Bloccante · diagnostica |
| Serve a | Indicatori del contratto che dipendono dalla regola |

Le regole bloccanti la cui violazione impedisce il calcolo di un indicatore sono evidenziate con l'admonition `!!! danger "Obbligatorio per KPI"`. Questa pagina sostituisce la `checklist.md` della v0.1: l'elenco di controllo dell'Azienda coincide con le regole che il validator applica, senza una seconda lista mantenuta a mano.

`esempi.md` pubblica i file NeTEx/SIRI di esempio prodotti dal generatore di `rpsd-tools`, conformi alle regole del contratto e scaricabili.

### 5.5 Output: `indicatori/<codice>.md`

```
# [Codice] — [Nome] · [Contratto]

> Riquadro: versione config, decorrenza

## Definizione
Sintesi + link alla definizione ART nel catalogo generale.

## Applicazione nel contratto
Formula con i parametri del contratto risolti.
Granularità di calcolo e di aggregazione.
Partizione (domanda rilevante / non rilevante, urbano / extraurbano, linea…).

## Soglia e penale
Livello minimo, importi e coefficienti, con riferimento all'allegato contrattuale.

## Parametri
Tabella: parametro | valore | riferimento contrattuale che lo giustifica.

## Scostamenti dalla definizione ART
Presente solo se esistono. Cosa cambia, perché, con quale effetto sul valore.

## Dati necessari
Dataset e regole da cui dipende, con link a dati/ dello stesso contratto.
```

La sezione "Scostamenti" è il punto qualificante: è qui che un indicatore "definito a partire dalla definizione ART" diventa specifico del contratto in modo dichiarato e tracciabile. La definizione generale non viene mai modificata per accogliere il caso di un contratto.

### 5.6 Documenti e changelog

`documenti.md` elenca la documentazione contrattuale (contratto di servizio, allegati su qualità e penali, sistema di monitoraggio, servizi sostitutivi…) con riferimento e link, o file scaricabile se pubblicabile.

`changelog.md` è generato dal bundle: per ogni versione del config che tocca il contratto, data di decorrenza ed elenco delle modifiche a dataset, regole, parametri e soglie.


## 6. Struttura del repository

```
rpsd-doc/
├── mkdocs.yml                  # configurazione (letta da Zensical)
├── requirements.txt            # zensical e plugin, versioni bloccate
├── templates/                  # template Jinja usati da rpsd-tools doc-gen
│   ├── contratto/
│   ├── regole/
│   └── indicatori/
├── data/                       # bundle committati (input della generazione)
│   ├── catalogo/
│   └── contratti/<id-contratto>/bundle.yaml
├── docs/
│   ├── .nav.yml
│   ├── index.md
│   ├── panoramica/             # redazionale (incl. modello-dati.md → link dbt docs)
│   ├── netex/
│   │   ├── index.md            # redazionale: elenco versioni
│   │   └── 5.0.0/              # redazionale + rpsd-profile-gen
│   ├── siri/
│   │   ├── index.md
│   │   └── 1.0.5/
│   ├── indicatori/
│   │   ├── delibera/           # redazionale
│   │   ├── catalogo/           # GENERATO
│   │   └── matrice/            # GENERATO (index.md)
│   ├── guida/                  # redazionale
│   ├── contratti/              # GENERATO — secondo step
│   ├── validazione/            # GENERATO — secondo step, solo ipotesi B
│   └── assets/
│       ├── images/
│       ├── xml/                # esempi generali
│       └── stylesheets/extra.css
├── .github/workflows/deploy.yml
├── CLAUDE.md
└── README.md
```


## 7. Contratti riservati (secondo step)

Un sito statico su GitHub Pages non offre controllo di accesso per pagina, e il contenuto di un contratto riservato non deve comparire né nel sito né nel repository pubblico. La soluzione va definita, ma la struttura deve già permetterla. Vincoli da rispettare da subito:

1. **Cartella di contratto autosufficiente**: tutto ciò che riguarda un contratto sta sotto `contratti/<id>/` e nel suo bundle.
2. **Nessun link scritto a mano dalla parte generale a un contratto.** I soli rimandi generale → contratto sono blocchi generati ("Contratti che applicano questo indicatore"), che `doc-gen` filtra in base alla visibilità. I link contratto → generale sono liberi.
3. **`visibilita` è un attributo del contratto nel config**; `doc-gen` produce separatamente l'insieme pubblico e quello riservato.

Ipotesi per il secondo step, da valutare: repository privato con i soli contratti riservati, build che unisce parte generale pubblica e contratti riservati, pubblicazione su un host con autenticazione (l'infrastruttura di progetto prevede già Keycloak come IAM).


## 8. Convenzioni di scrittura

Restano valide quelle della v0.1 (tono tecnico ma accessibile, termini dello standard in inglese, massimo 1500 parole per pagina, admonition con significato fisso, XML sempre annotato, glossario linkabile). Si aggiungono:

- **ID stabili come anchor e come URL**: ID regola, codice indicatore, id contratto non si rinominano; se necessario si usa `redirects`.
- **Il contratto rimanda, non copia**: le pagine di contratto riportano i valori risolti e linkano la definizione generale.
- **Normativa generale nella parte generale, allegati di gara nel contratto.**
- **Pagine generate riconoscibili**: riquadro di testata con versione config e decorrenza; front matter `generato: true`.
- **Tag** generati per dataset e per codice indicatore, per la navigazione trasversale.


## 9. Piano di implementazione

Allineato alle scadenze di progetto (config con pilot a fine novembre 2026, parte documentale e regole a fine dicembre, collaudo a fine aprile 2027).

**Primo step — Parte generale**

*Fase 0 — Fondamenta (novembre–dicembre 2026)*
1. Spike Zensical sui punti del §2.1; conferma della scelta o passaggio al piano B.
2. Setup repository, `mkdocs.yml`, `.nav.yml`, CI di build e deploy.
3. Struttura versionata di `netex/` e `siri/` con le versioni correnti dei profili.

*Fase 1 — Contenuti (dicembre 2026–marzo 2027)*
4. Home, panoramica, glossario, pagina sul modello dati con link alla documentazione dbt.
5. NeTEx e SIRI: introduzione, concetti, pagine di frame e servizio, esempi.
6. Indicatori: pagine sulla delibera, catalogo delle definizioni, matrice.
7. Guida operativa, incluso il funzionamento della validazione.

*Fase 2 — Verso il collaudo (aprile 2027)*
8. FAQ, revisione complessiva, tag di rilascio.
9. Verifica dello stato di Zensical (uscita dalla beta); valutazione di `zensical.toml`.

**Secondo step — Contratti** (avvio condizionato al consolidamento del modello del config)

10. Schema del bundle concordato con chi sviluppa il config.
11. Decisione sulla collocazione delle regole di validazione (§4.2, ipotesi A o B).
12. `doc-gen` in `rpsd-tools`, template, generazione del primo contratto.
13. Esempi NeTEx/SIRI conformi al contratto; revisione dei contenuti con l'Agenzia.
14. Contratti riservati (§7); ulteriori contratti (solo bundle + generazione).


## 10. Decisioni aperte

| # | Questione | Chi |
|---|-----------|-----|
| 1 | Esito dello spike Zensical; in caso negativo, piano B Docusaurus (§2.1) | Franco |
| 2 | Contratto della consegna di aprile 2027: come documentarlo se la generazione dal config non è pronta (pagine con la stessa struttura prodotte dai file del pilot, forma ridotta, oppure rinvio) | Franco, responsabile |
| 2b | Schema del bundle e copertura da parte del modello del config (in particolare: testo degli scostamenti, changelog, visibilità) — secondo step | Franco, Davide |
| 2c | Regole di validazione: solo nel contratto (A) o catalogo generale + attivazione (B), dopo il consolidamento del config | Franco, Davide |
| 2d | Documentazione dbt: pubblica sotto lo stesso dominio o ad accesso controllato | Franco, responsabile |
| 2e | Granularità delle cartelle di versione dei profili (ogni versione adottata da un contratto, o solo major/minor) | Franco |
| 3 | Template in `rpsd-doc` e motore in `rpsd-tools`, oppure tutto in `rpsd-tools` | Franco |
| 4 | Confine tra `rpsd-profile-gen` e contenuto redazionale nelle pagine di frame/servizio | Franco |
| 5 | Pubblicare indicatori base e di qualità/trasmissione, o solo ART | Franco, responsabile |
| 6 | Quali documenti contrattuali sono pubblicabili come file e quali solo citati | Agenzia |
| 7 | Formule nelle pagine di contratto: con parametri risolti (proposta) o solo rimando alla definizione generale | Franco |
| 8 | Soluzione di hosting per i contratti riservati | — |


## 11. Note per l'implementazione con Claude Code

Suggerimento per il `CLAUDE.md` del repo:

```markdown
# rpsd-doc — Context for Claude Code

## What this repo is
Static documentation site for the Rapsodia project, built with Zensical
(config kept in mkdocs.yml). Documents the Italian NeTEx/SIRI profiles, the
validation rule catalog, the ART indicators, and one section per service contract.

## Versioned profiles
- docs/netex/<version>/ and docs/siri/<version>/ hold one frozen copy per profile
  version. Never edit a non-current version except for errata. A new profile
  version is a new folder, not an edit of the existing one.

## Hand-written vs generated
- NEVER edit by hand: docs/indicatori/catalogo/, docs/indicatori/matrice/ and,
  once they exist (second step), docs/contratti/ and docs/validazione/.
  They are produced by rpsd-tools doc-gen from the bundles in data/ using templates/.
- To change generated content: change the config (source of truth), re-export the
  bundle, re-run doc-gen. To change layout: edit templates/.
- Hand-written pages never link into docs/contratti/<id>/.

## Key files
- mkdocs.yml — site configuration (no nav: navigation lives in .nav.yml files)
- docs/.nav.yml — top-level navigation
- data/ — committed bundles (input of generation)
- templates/ — Jinja templates for generated pages
- rpsd-doc-site-design.md — full site design

## Conventions
- Language: Italian (content), English (technical terms from standards)
- Rule IDs, indicator codes and contract ids are stable: never rename them
- General pages carry no contract thresholds and no tender-annex references
- Max 1500 words per hand-written page
- Use only features supported by both Zensical and Material for MkDocs (phase 1)

## Source documents (in project knowledge)
- Linee guida compilazione NeTEx IT v5.0.0
- Linee guida compilazione SIRI IT v1.0.5
- Delibera ART 53/2024 — Allegato A
- rapsodia-context.md
```
