# Design — add-directory-navigation

## Context

Motivazione e perimetro: `proposal.md`. Requisiti: `specs/site-navigation/spec.md` (seed §4.2 senza modifiche).

Stato attuale (dopo `bootstrap-site`): `mkdocs.yml` senza `plugins` e senza `nav`; feature del tema `navigation.tabs`, `navigation.sections`, `navigation.indexes`, senza `navigation.expand`; `docs/` contiene solo `index.md` e `assets/`. Lo spike (`spike/mkdocs.yml`) eredita la configurazione con `INHERIT`. `scripts/check_sidebar.py` verifica già, sullo spike, che la sezione attiva contenga solo le proprie pagine.

### Verifiche fatte in fase di proposta (13 novembre 2026)

Fonti: codice di Zensical 0.1.1 (`zensical/config.py`) = **codice**; documentazione Zensical via Context7 = **doc**; prova con Zensical 0.1.1 su un sito usa e getta con le cinque sezioni, pagine a tre livelli e Chrome headless = **prova**.

| Punto | Esito | Fonte |
|---|---|---|
| `awesome-nav` in Zensical | Integrato (scoperta, parsing YAML e risoluzione in Rust); si attiva con la sola presenza in `plugins`; nessun pacchetto da installare | codice |
| Opzioni del plugin | Ammesse solo `enabled`, `filename` (default `.nav.yml`), `logs`; ogni altra opzione è rifiutata | codice |
| Pattern nei `.nav.yml` | Il glob `"*"` in coda aggiunge le voci non elencate (pagine e sottocartelle); niente extglob | prova + design §2.1 |
| `title` e `nav` nel `.nav.yml` di una sottocartella | Titolo e ordine della sottosezione rispettati | prova |
| Tab | Con `docs/.nav.yml` a cinque voci: tab nell'ordine dichiarato, tab della sezione corrente marcato attivo (`md-tabs__item--active`) | prova |
| Pagina a tre livelli | Antenati espansi, ramo fratello chiuso, sidebar della sola sezione corrente | prova (browser) |
| Sottocartella nuova con `.nav.yml` | Compare nella sidebar dopo il rebuild **solo se** il `.nav.yml` del livello superiore termina con `"*"`; se elenca le voci una per una viene costruita ma non compare | prova |
| `plugins: [search, awesome-nav]` | Ricerca attiva (`search.json` con `lang: ["it"]`); dichiarare `search` non cambia nulla in Zensical | prova |
| `navigation.prune` | Documentato; pagine fuori dalla sezione grande da 152 KB a 34 KB; rami chiusi resi come link. Non adottato (proposal) | doc + prova |

## Goals / Non-Goals

**Goals**
- Una convenzione unica per i `.nav.yml`, che i change 4–9 e la generazione dei contratti possano seguire senza decisioni caso per caso.
- Ogni scenario di `site-navigation` verificato in CI, non solo a vista.

**Non-Goals**
- Navigazione per versione di profilo (change 4), contenuti (change 5–9), sezione Contratti (secondo step).

## Decisions

### D1. Plugin dichiarati in `mkdocs.yml`

```yaml
plugins:
  - search
  - awesome-nav
```

`search` è elencato esplicitamente per reversibilità: in MkDocs/Material la presenza di `plugins` disattiva i plugin di default non elencati. Nessuna opzione per `awesome-nav` (i default `filename: .nav.yml` vanno bene). Nessuna modifica a `requirements.txt`.
*Piano B*: con Material va aggiunto a `requirements.in` il pacchetto `mkdocs-awesome-nav`.

### D2. `.nav.yml` della radice: i tab

```yaml
nav:
  - Home: index.md
  - NeTEx: netex
  - SIRI: siri
  - Indicatori: indicatori
  - Guida operativa: guida
```

Elenco esplicito, **senza** `"*"`: l'ordine dei tab è un requisito, e una cartella nuova in radice non deve diventare un tab per caso. Aggiungere un tab (es. Contratti nel secondo step) significa aggiungere una riga qui, non toccare `mkdocs.yml`.
*Alternativa scartata*: `nav` in `mkdocs.yml` (contraddice il requisito *Navigation defined per directory*).
Home resta una voce singola; quando il change 5 aggiungerà `panoramica/`, la voce diventerà una sezione (`- Home: [index.md, panoramica]` o equivalente) con una modifica a questo file.

### D3. `.nav.yml` di sezione e di sottosezione: convenzione

Ogni cartella di sezione ha un `.nav.yml` con titolo (se diverso dal nome della cartella) e un `nav` che elenca le voci da ordinare e **termina con `"*"`**:

```yaml
nav:
  - index.md
  - "*"
```

Così una sottocartella nuova, con il proprio `.nav.yml`, compare nella sidebar senza modificare né `mkdocs.yml` né il `.nav.yml` del livello superiore (scenario *New subsection*). Le voci da tenere in un ordine preciso si elencano prima di `"*"`.
Eccezione prevista: i `.nav.yml` di `netex/` e `siri/` nel change 4 elencheranno solo la versione corrente, senza `"*"`, perché la sidebar deve mostrare solo quella (`profile-versioning`).

### D4. Pagine segnaposto

`docs/netex/index.md`, `docs/siri/index.md`, `docs/indicatori/index.md`, `docs/guida/index.md`: titolo della sezione (NeTEx, SIRI, Indicatori, Guida operativa) e un'admonition `info` "Sezione in preparazione", come la home attuale. Nessun testo di dominio. Le cartelle seguono i nomi del design §6.

### D5. Controlli automatici

- **`scripts/check_navigation.py`** (sito costruito, `site/`): per `index.html` e per l'`index.html` di ciascuna sezione verifica che i tab siano esattamente Home, NeTEx, SIRI, Indicatori, Guida operativa in quest'ordine e che l'unico tab attivo sia quello della sezione della pagina. Scenario *Reader on any page*.
- **`scripts/check_new_subsection.py`**: copia `mkdocs.yml` e `docs/` in una directory temporanea, aggiunge `guida/prova-sottosezione/` con due pagine e un `.nav.yml` con `title`, costruisce in strict e verifica che la sidebar della sezione Guida operativa contenga la sottosezione con quel titolo e che `mkdocs.yml` sia invariato (hash). Scenario *New subsection*. Esegue sulla configurazione e sui `.nav.yml` reali del sito.
- **Pagina a tre livelli nello spike**: `spike/docs/navigazione/` con due rami (`ramo-a/livello-2/…`, `ramo-b/…`) e una pagina al terzo livello. `scripts/check_sidebar.py` aggiunge un caso: nella sidebar della pagina profonda gli antenati sono espansi (`aria-expanded="true"` sulle `nav` annidate del percorso) e il ramo fratello è chiuso (`aria-expanded="false"`). Scenario *Deep page*. Verifica visiva nel browser come nel change 1.
- `pr.yml`: `check_navigation.py` nel job `build` dopo il build; `check_new_subsection.py` nel job `spike`. I nomi dei job non cambiano, quindi la protezione di `main` non va toccata.

La pagina profonda sta nello spike perché il sito reale non ha ancora pagine a tre livelli; la struttura dei `.nav.yml` dello spike segue la convenzione D3.

### D6. README

Sezione "Navigazione": la radice definisce i tab; ogni cartella ha il proprio `.nav.yml` che termina con `"*"`; per aggiungere una sottosezione basta creare la cartella con pagine e `.nav.yml`. Le regole complete di scrittura arrivano con la pagina "come contribuire" (change 3).

## Risks / Trade-offs

- [Una cartella creata per errore compare in sidebar per via di `"*"`] → è il comportamento voluto per le sottosezioni; la radice è esplicita, quindi non nascono tab per caso.
- [Le pagine segnaposto vengono indicizzate e linkate] → URL stabili e contenuto neutro; i change successivi ne sostituiscono il testo, non il percorso.
- [Senza `navigation.prune` le pagine crescono con il numero di pagine del sito] → misurato e accettato per ora (proposal); da rivalutare con le sezioni generate.
- [Formato `.nav.yml` interpretato dal Rust di Zensical, non dal plugin originale] → i controlli in CI lo intercettano; prima di un aggiornamento di Zensical si rilancia lo spike.
- [Piano B] → con Material serve `mkdocs-awesome-nav`; i `.nav.yml` usati (voci, titolo, `"*"`) appartengono al formato del plugin originale.

## Migration Plan

Nessuna migrazione: gli URL esistenti (`/`) non cambiano. Rollback: revert del merge.
