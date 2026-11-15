# Design — restructure-site-sections

## Context

Motivazione e perimetro: `proposal.md`. Requisiti: `specs/site-navigation/spec.md` e `specs/content-conventions/spec.md`.

Stato attuale (`main` dopo `add-profile-versioning`):

- **Navigazione**: `docs/.nav.yml` elenca cinque tab (Home, NeTEx, SIRI, Indicatori, Guida operativa), esplicitamente e senza `"*"`. Ogni sezione ha `index.md` e un `.nav.yml` con `index.md` + `"*"`. NeTEx e SIRI elencano invece la sola versione corrente.
- **Home**: `docs/index.md` è un segnaposto con il callout `note` "Sito in costruzione".
- **Percorsi generati**: in `generated-paths.txt` ogni riga è un prefisso. `check_conventions.py` applica le regole:
  - G1: front matter `generato: true` e `generato_da` nelle cartelle generate;
  - G2: nessuna pagina dichiarata generata fuori da esse;
  - G3: trailer `Generato-da` sui commit che toccano le cartelle generate.

  `docs/contratti/` è elencata per intero.
- **Controlli in CI** (`pr.yml`):
  - `check_navigation.py` confronta i tab con una lista fissa (`EXPECTED_TABS`) e verifica il tab attivo sulla home e sull'indice di ogni sezione;
  - `check_urls.py` verifica che nessun URL pubblicato sparisca senza redirect;
  - `test_conventions.py` prova le regole G1–G3.

## Goals / Non-Goals

**Goals**
- I nove tab nell'ordine della spec, ciascuno con una pagina d'ingresso, verificati in CI come gli attuali cinque.
- Una sola regola, verificabile, su cosa è redazionale e cosa è generato nella sezione Contratti, che regga anche il primo contratto generato senza nuove eccezioni.
- Nessun URL già pubblicato rotto.

**Non-Goals**
- Contenuti delle pagine nuove: restano "da completare" (proposal, Fuori scope).
- Generazione dei contratti e `.nav.yml` di contratto: li produrrà `rpsd-tools`.
- Stile e template della home.

## Decisions

### D1 — Rapsodia: home alla radice, pagine in `docs/rapsodia/`

La home resta `docs/index.md`, cioè l'URL `/`, che non cambia. Le pagine del tab vanno in `docs/rapsodia/` (`progetto.md`, `glossario.md`, `novita.md`), con URL `/rapsodia/<pagina>/`. Nel `.nav.yml` della radice il tab Rapsodia è un gruppo con `index.md` e le tre pagine elencate per percorso, così compaiono piatte nella sidebar e non come sottosezione.

*Alternative scartate*
- **Pagine alla radice (`/progetto/`, `/glossario/`)**: mescola le pagine del tab con le cartelle delle altre sezioni.
- **Home in `docs/rapsodia/index.md` con redirect da `/`**: la radice del sito diventerebbe un redirect.

*Da verificare in apply*: che awesome-nav in Zensical accetti nel `.nav.yml` della radice un gruppo con `index.md` più pagine di una sottocartella. L'anteprima del change 5 ha usato con successo un gruppo `Home: [index.md, Panoramica: panoramica]`. Se le pagine per percorso non funzionano, il ripiego è `rapsodia` come sottocartella con un proprio `.nav.yml`.

### D2 — Una cartella per ogni nuovo tab, con la convenzione esistente

Le nuove cartelle sono `docs/architettura/`, `docs/modello-dati/`, `docs/dashboard/` e `docs/contratti/`. Ognuna ha `index.md` e `.nav.yml` con `index.md` + `"*"`, come Indicatori e Guida.

**Architettura** ha in più tre pagine: `core.md` (titolo "Core (A+D)"), `app.md` ("App (B)") e `iot.md` ("IoT (C)"), elencate in quest'ordine prima di `"*"`.

- La pagina Core ha una sezione "Moduli funzionali": una tabella con colonne *Modulo*, *Cosa fa* e *Repository*. In questo change non ha righe: un callout `note` dice che l'elenco è da completare.
- Nessun nome di modulo, descrizione o URL di repository viene scritto senza fonte (regola di progetto "never invent content"). Elenco e link arrivano con il change dei contenuti.

### D3 — Indice dei contratti redazionale, cartelle dei contratti generate

In `generated-paths.txt`, `docs/contratti/` diventa `docs/contratti/*/`. Il `*` vale un solo segmento di percorso: ogni sottocartella di `docs/contratti/` è generata, mentre `docs/contratti/index.md` e `docs/contratti/.nav.yml` sono redazionali.

`load_generated_paths` / `is_generated` passano dal confronto per prefisso a un confronto segmento per segmento in cui `*` vale un segmento qualsiasi. Le righe senza `*` mantengono la semantica di prefisso, quindi i percorsi già elencati non cambiano comportamento. G3 (`git log -- <pathspec>`) usa direttamente il pathspec `docs/contratti/*/`, che git interpreta come glob.

*Alternativa scartata*: elencare in `generated-paths.txt` ogni contratto man mano che viene generato. Così un contratto generato ma non ancora elencato non sarebbe protetto.

### D4 — Il segnaposto `esempio`: eccezione dichiarata

`docs/contratti/esempio/index.md` è scritto a mano, ma sta in un percorso generato. Viene dichiarato in `generated-paths.txt` con una riga di esclusione: `!docs/contratti/esempio/  # segnaposto, da togliere col primo contratto generato`.

Le regole del controllo:

- un percorso escluso con `!` non è generato per G1, G2 e G3 (quest'ultima tramite il pathspec `:(exclude)` di git);
- una nuova regola **G4** richiede che ogni pagina in un percorso escluso abbia `segnaposto: true` nel front matter. A quel punto la pagina deve anche mostrare un callout `warning` "Contratto segnaposto", che il controllo cerca nel sorgente;
- una pagina scritta a mano in un'altra cartella di contratto continua a fallire G1 (scenario della spec).

Quando arriva il primo contratto generato, la riga `!` e la cartella `esempio/` si tolgono nello stesso change. `/contratti/esempio/` sparisce senza redirect, per scelta di Franco: `check_urls.py` lo segnalerà, e in quel change va aggiunta un'eccezione esplicita o un redirect verso l'indice dei contratti. La decisione si prende lì.

*Alternative scartate*
- **Committare il segnaposto con il trailer `Generato-da`**: dichiarerebbe una generazione mai avvenuta.
- **Non creare la cartella**: Franco vuole vedere la forma della sezione con un contratto.

### D5 — Pagine segnaposto

Le pagine nuove senza contenuto usano il callout `note` "Sezione in preparazione", come le sezioni già pubblicate. Dove la pagina ha una struttura (Architettura, Core), i titoli di sezione ci sono e il testo è "_da completare_".

La home (`docs/index.md`) perde il callout "Sito in costruzione" e diventa l'indice del sito. Contiene:

- la frase su Rapsodia, già pubblicata nel `README.md`, che riformula `openspec/config.yaml`;
- un elenco di link, uno per tab, con una riga di descrizione ciascuno, ricavata dal design §1 e dalla proposta.

Le schede (`grid cards`) restano al change dei contenuti. Nessun contenuto del progetto (obiettivi, partner) entra in questo change.

### D6 — Controlli

`check_navigation.py`:

- `EXPECTED_TABS` diventa la lista dei nove tab;
- `PAGES` (pagina → tab attivo atteso) aggiunge `architettura/`, `modello-dati/`, `dashboard/`, `contratti/` e una pagina di `rapsodia/`, che deve rendere attivo il tab Rapsodia;
- `/` deve rendere attivo Rapsodia.

Per lo scenario "sezione senza contenuto" basta che ogni tab abbia un `index.html` costruito: il controllo verifica che la pagina esista.

`test_conventions.py` aggiunge casi per D3 e D4:

- indice dei contratti redazionale accettato;
- pagina a mano in un contratto non dichiarato rifiutata;
- segnaposto senza `segnaposto: true` rifiutato;
- riga senza `*` con semantica invariata.

### D7 — Larghezza della barra dei tab

Con nove tab la barra può non entrare nella larghezza disponibile. Si verifica sul sito costruito, con Chrome headless a 1300 px e a 1024 px (sotto i 1220 px Material e Zensical nascondono i tab e usano il menu laterale).

Se a 1300 px i tab non entrano, si riportano le opzioni a Franco senza scegliere: etichette più brevi oppure meno tab. Non si aggiunge CSS personalizzato.

## Risks / Trade-offs

- **[Le pagine per percorso nel gruppo della radice non sono supportate da awesome-nav in Zensical]** → prova all'inizio dell'apply; ripiego indicato in D1.
- **[Glob in `generated-paths.txt` interpretato diversamente da script e git]** → `*` limitato a un segmento e senza altri metacaratteri; caso di prova dedicato in `test_conventions.py`.
- **[Il segnaposto viene dimenticato quando arriva il primo contratto]** → il commento sulla riga `!` e la regola G4 lo rendono visibile. Il design §5.2 annota che `esempio` va tolto.
- **[Nove tab affollano la testata]** → D7.
- **[Disallineamento tra design, seed e spec]** → gli stessi task aggiornano design §4.1, §4.2, §4.4, §5.2 e §6, e il seed (elenco dei change, requisiti `overview` del change 5).

## Migration Plan

Nessuna migrazione di URL: gli URL esistenti (`/`, `/netex/…`, `/siri/…`, `/indicatori/`, `/guida/`) restano invariati. Gli URL nuovi vengono solo aggiunti.

Rollback: revert del merge. Gli URL nuovi spariscono, e `check_urls.py` lo segnalerebbe solo in un change successivo.

## Open Questions

- Le descrizioni di una riga per tab nella home sono riformulate dal design. Franco le rivede in PR. Non cambiano la struttura.
