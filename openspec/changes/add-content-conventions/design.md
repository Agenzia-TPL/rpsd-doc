# Design — add-content-conventions

## Context

Motivazione e perimetro: `proposal.md`. Requisiti: `specs/content-conventions/spec.md` (seed §4.3 senza modifiche).

Stato attuale: `docs/` contiene la home e quattro sezioni segnaposto, tutte redazionali, con callout `info` "Sito in costruzione" / "Sezione in preparazione". Nessuna pagina generata, nessun glossario. I controlli esistenti sono script Python in `scripts/` richiamati da `pr.yml` nei job "Build strict del sito" e "Spike (scala, sidebar, link rotti)", entrambi obbligatori per il merge su `main`.

### Verifiche fatte in fase di proposta (13 novembre 2026, Zensical 0.1.1)

| Punto | Esito | Fonte |
|---|---|---|
| Plugin `redirects` | Integrato; opzioni ammesse solo `enabled` e `redirect_maps` (mappa stringa → stringa) | codice (`zensical/config.py`) |
| Pagina di redirect | Generata all'URL vecchio (`guida/vecchia/index.html`) con `meta refresh`, `link rel=canonical` e script che conserva l'anchor; build strict senza warning | prova |
| Front matter personalizzato (`generato`, `generato_da`) | Accettato, non compare nella pagina | prova |

## Goals / Non-Goals

**Goals**
- Ogni requisito di `content-conventions` verificato da un controllo automatico che fallisce con un messaggio che dice cosa correggere.
- Ogni controllo provato su casi conformi e non conformi, in CI.
- Una sola fonte per l'elenco delle cartelle generate.

**Non-Goals**
- Rigenerazione delle pagine in CI (richiede `rpsd-tools`).
- Verifica del *significato* dei callout (es. che un campo marcato "Obbligatorio per KPI" lo sia davvero): resta alla revisione; il controllo verifica la forma.

## Decisions

### D1. Elenco delle cartelle generate: `generated-paths.txt`

File nella radice, un percorso per riga, commenti con `#`:

```
docs/indicatori/catalogo/
docs/indicatori/matrice/
docs/contratti/      # secondo step
docs/validazione/    # secondo step, solo ipotesi B
```

Letto da tutti i controlli; un percorso non ancora esistente è ammesso. `CLAUDE.md` e `CONTRIBUTING.md` rimandano a questo file.
*Alternativa scartata*: elenco nel codice dello script (due fonti da tenere allineate con `CLAUDE.md`).

**Matrice**: `docs/indicatori/matrice/index.md` invece di `docs/indicatori/matrice.md` (design del sito §6), perché il requisito vuole le pagine generate in cartelle che contengono solo pagine generate. L'URL pubblicato è lo stesso (`/indicatori/matrice/`). Aggiornati design del sito §6 e `CLAUDE.md`.

### D2. Pagine generate (`scripts/check_conventions.py`, regole G1–G3)

- **G1** — ogni file `.md` sotto un percorso generato ha nel front matter `generato: true` e `generato_da` non vuoto (es. `generato_da: rpsd-tools 0.3.0`). Gli altri campi del design §3.1 (id contratto, versione config, data) sono ammessi ma non richiesti qui: dipendono dal tipo di pagina.
- **G2** — ogni file `.md` con `generato: true` sta sotto un percorso generato (niente pagine miste o generate fuori posto).
- **G3** (solo sulle PR, opzione `--commits <base>`) — ogni commit non di merge in `<base>..HEAD` che modifica un file sotto un percorso generato (qualunque tipo, anche `.nav.yml`) deve avere il trailer `Generato-da: rpsd-tools <versione>`. Il messaggio di errore elenca commit e file e spiega che si modificano i dati in `data/` e si rigenera, non le pagine. I commit di merge sono esclusi perché portano modifiche già controllate altrove.
  Lettura del trailer: `git log --format=%(trailers:key=Generato-da,valueonly)`.
  *Alternative scartate*: etichetta sulla PR, prefisso del branch (scelta di Franco).

Il front matter è letto con un parser minimale (righe `chiave: valore` tra `---`), senza dipendenze: i valori usati sono scalari.

### D3. Lunghezza delle pagine redazionali (regola L1)

Pagina redazionale = file `.md` sotto `docs/` non sotto un percorso generato. Conteggio delle parole sul testo dopo aver tolto: front matter, blocchi di codice recintati (``` e ~~~), commenti HTML, URL dei link e marcatori Markdown. Una parola è una sequenza di lettere/cifre (Unicode), con apostrofo interno ammesso. Oltre 1500 parole il controllo fallisce indicando pagina e conteggio.
Motivazione dell'esclusione del codice: gli esempi XML sono richiesti (design §8: "XML sempre annotato") e non sono prosa.

### D4. URL stabili

- `mkdocs.yml`: plugin `redirects` con `redirect_maps` vuoto. Spostare una pagina pubblicata significa aggiungere una riga `vecchio/percorso.md: nuovo/percorso.md`.
- **`scripts/check_urls.py <base>`**: crea un worktree temporaneo di `<base>` (sulla PR, `origin/main`), costruisce in strict sia `<base>` sia la copia corrente e confronta gli insiemi di pagine HTML servite (esclusi `404.html` e gli asset). Ogni URL presente in `<base>` deve esistere nella PR, come pagina o come redirect; altrimenti fallisce elencando gli URL persi e suggerendo la voce di `redirect_maps`.
  *Alternativa scartata*: confronto con la `sitemap.xml` del sito pubblicato (dipende dalla rete e dallo stato del deploy).
- Le pagine dello spike non sono pubblicate e non entrano nel confronto.

### D5. Callout (regola C1)

Riconosciuti `!!! tipo "titolo"`, `??? tipo "titolo"`, `???+ tipo "titolo"` (anche con classi aggiuntive dopo il tipo), fuori dai blocchi di codice. Ammessi:

| Tipo | Titolo |
|---|---|
| `note`, `tip`, `warning`, `example` | libero |
| `danger` | esattamente "Obbligatorio per KPI" |
| `info` | esattamente "Novità Rapsodia" |

I due titoli riservati non possono essere usati con altri tipi. Vale per tutte le pagine di `docs/`, generate comprese (i template di `rpsd-tools` dovranno rispettarla). Le pagine segnaposto passano da `info` a `note`.

### D6. Glossario (regola S1)

- Formato fissato ora, contenuti nel change 5: glossario in `docs/panoramica/glossario.md`; ogni sigla è un titolo con anchor esplicito e classe `sigla` (`attr_list`, già attiva):
  ```markdown
  ### PdE {#pde .sigla}
  ```
- Regola: in ogni altra pagina di `docs/`, la **prima** occorrenza di ciascuna sigla nel testo (esclusi titoli, front matter, blocchi di codice e codice in linea; confronto sensibile alle maiuscole, a parola intera) deve stare nel testo di un link il cui destinatario termina con `glossario.md#<anchor>` o `glossario/#<anchor>`. Le occorrenze successive sono libere.
- Glossario assente: il controllo lo dice e passa (nessuna sigla).
- Solo le voci marcate `.sigla` sono soggette: il requisito parla di sigle di dominio, non di tutti i termini.

### D7. Prove dei controlli: `scripts/test_conventions.py`

`unittest` della libreria standard. Per ogni regola almeno un caso conforme e uno non conforme su fixture in directory temporanee: G1/G2 (front matter mancante, pagina generata fuori posto), G3 (repository git temporaneo con un commit senza trailer e uno con trailer), L1 (1500 e 1501 parole, codice escluso), C1 (tipi e titoli), S1 (prima occorrenza linkata, non linkata, linkata solo dopo, glossario assente), D4 (pagina spostata senza redirect → fallisce; con redirect → passa).

### D8. Integrazione in CI

- Job **"Build strict del sito"**: `actions/checkout` con `fetch-depth: 0`; dopo il build: `python scripts/check_conventions.py --commits origin/${{ github.base_ref }}` (G1–G3, L1, C1, S1) e `python scripts/check_urls.py origin/${{ github.base_ref }}`.
- Job **"Spike (scala, sidebar, link rotti)"**: `python scripts/test_conventions.py`.
- Nomi dei job invariati: la protezione di `main` non va toccata.
- `deploy.yml` invariato.

### D9. `CONTRIBUTING.md`

Regole per chi scrive: pagina redazionale o generata, cartelle generate (rimando a `generated-paths.txt`) e trailer per `rpsd-tools`; limite di 1500 parole; tabella dei callout (D5); glossario e sigle (D6); spostare una pagina con `redirect_maps`; navigazione con `.nav.yml` (rimando al README); come eseguire i controlli in locale. Solo regole già presenti nel design del sito, nel seed o in `CLAUDE.md`: nessuna regola nuova.

## Risks / Trade-offs

- [Il trailer si può scrivere a mano] → il controllo intercetta l'errore involontario, non l'abuso; la revisione della PR resta obbligatoria. Il controllo forte (rigenerazione) arriva con `rpsd-tools`.
- [Doppio build in `check_urls.py`] → qualche secondo in più per PR (build attuale < 1 s).
- [Conteggio parole approssimato] → regola semplice e documentata; il limite serve a segnalare pagine da dividere, non a misurare con precisione.
- [Sigla che compare per la prima volta in una tabella o in un callout] → conta come testo: va linkata lì. Documentato in `CONTRIBUTING.md`.
- [Piano B] → con Material servirebbe il pacchetto `mkdocs-redirects` (stesse opzioni).

## Migration Plan

Nessuna migrazione di URL: le pagine esistenti non si spostano. Il callout delle pagine segnaposto cambia tipo (nessun effetto sugli URL).
