# Proposal — restructure-site-sections

## Why

Rivedendo l'anteprima del change 5 (`add-overview-pages`), Franco ha deciso una struttura diversa da quella del design: la home non è più "Home + Panoramica" ma un indice del progetto, l'architettura diventa una sezione a sé organizzata per sottosistemi, e modello dati, dashboard e contratti diventano tab di primo livello. Va fatto **prima** dei change di contenuto (5–9), perché decide dove stanno le pagine e quali URL vengono pubblicati, e gli URL sono stabili. Questo change fissa **solo la struttura**: i contenuti arrivano dopo.

## What Changes

- **BREAKING (navigazione)**: i tab di primo livello diventano, in quest'ordine:
  **Rapsodia | Architettura | NeTEx | SIRI | Indicatori | Modello dati | Dashboard | Guida operativa | Contratti**.
  Cambiano il nome di un tab (Home → Rapsodia) e il numero dei tab (da 5 a 9). Nessun URL già pubblicato cambia o sparisce.
- **Rapsodia** (ex Home, `docs/index.md` più `docs/rapsodia/`): la pagina d'ingresso fa da indice del sito. La sezione contiene le pagine *Il progetto*, *Glossario* e *Novità del sito*, come segnaposto "da completare".
- **Architettura** (`docs/architettura/`): sostituisce la "Panoramica" del design. Contiene una pagina d'ingresso con la definizione generale e una pagina per ciascuno dei tre sottosistemi: **Core (A+D)**, **App (B)**, **IoT (C)**. La pagina Core ha lo spazio per l'elenco dei moduli funzionali (rpsd-config, rpsd-ingest, …): breve descrizione e link al repository GitHub di ciascuno. In questo change ogni pagina ha la struttura e "da completare".
- **NeTEx, SIRI, Indicatori, Guida operativa**: invariati.
- **Modello dati** (`docs/modello-dati/`): tab nuovo, con pagina segnaposto. Pagina redazionale con link alla documentazione dbt (design §4.4); il contenuto arriva dopo.
- **Dashboard** (`docs/dashboard/`): tab nuovo, con pagina segnaposto.
- **Contratti** (`docs/contratti/`): tab nuovo, anticipato rispetto al secondo step per scelta di Franco.
  - `docs/contratti/index.md` diventa **redazionale**: è l'elenco dei contratti. Il design lo prevedeva generato.
  - Ogni cartella di contratto `docs/contratti/<id>/` resta **generata**.
  - Un contratto segnaposto `esempio` (`/contratti/esempio/`), con "da completare", finché `rpsd-tools` non genera il primo contratto reale.
- **Regole sui percorsi generati**: `generated-paths.txt` e il controllo `check_conventions.py` distinguono l'indice dei contratti, redazionale, dalle cartelle dei contratti, generate. Il segnaposto `esempio` è dichiarato come eccezione temporanea (design D4).
- **Documenti di progetto allineati**:
  - design del sito §4.1, §4.2, §4.4, §5.2, §6;
  - seed: elenco dei change e requisiti `overview` del change 5;
  - `CLAUDE.md` e `openspec/config.yaml` (percorsi generati, Contratti non più "fuori scope" come sezione).

## Capabilities

### New Capabilities
_Nessuna._ I requisiti sui contenuti di Rapsodia, Architettura e Modello dati restano alla capability `overview` del change 5, che il seed riformula su questa struttura.

### Modified Capabilities
- `site-navigation`: il requisito *Top-level sections* cambia elenco e ordine dei tab. Si aggiunge un requisito: ogni tab ha una pagina d'ingresso anche quando la sezione non ha ancora contenuti.
- `content-conventions`: il requisito *Generated pages are identifiable* ammette una pagina indice redazionale in una sezione le cui sottocartelle sono generate (l'elenco dei contratti), e un segnaposto dichiarato in un percorso generato.

## Riferimenti al design

Modifica `rpsd-doc-site-design.md`:
- **§4.1** tab di primo livello;
- **§4.2** parte generale: Home/Panoramica sostituita da Rapsodia e Architettura;
- **§4.4** modello dati come tab;
- **§5.2** `contratti/index.md` redazionale;
- **§6** struttura del repository.

Il resto del design (§5, sezione Contratti come mini-sito generato) non cambia: questo change ne anticipa solo il punto di ingresso.

## Tipo di intervento

**Infrastruttura del sito** (navigazione, controlli sui percorsi generati) più **pagine redazionali segnaposto**: titolo, struttura delle sezioni e "da completare". Nessun contenuto di dominio e nessun contenuto generato. Il contratto `esempio` è un segnaposto, non un contratto generato.

## Decisioni prese in fase di proposta (Franco)

- Il tab Indicatori resta un tab a sé.
- Il tab dell'architettura si chiama **Architettura**.
- Contratti: indice scritto a mano, contratti generati; segnaposto con id `esempio`. Si accetta che l'URL `/contratti/esempio/` sparisca quando arriva il primo contratto reale (vedi design D4).
- Il tab **Dashboard** va dopo Modello dati.

## Fuori scope

- **Contenuti** di tutte le pagine nuove: testo del progetto, glossario, novità, definizione dell'architettura, descrizioni dei moduli e link ai repository, strati del modello dati, link dbt, dashboard. Arrivano con il change 5 (riformulato) e con le fonti fornite da Franco.
- **Home "da vetrina"** con template HTML personalizzato: si resta su Markdown standard.
- Generazione dei contratti, schema del bundle, `templates/`, `data/`: secondo step.
- Tab Validazione: secondo step, solo ipotesi B.
- Push, PR e impostazioni GitHub: solo con approvazione esplicita.

## Impact

- **File modificati**:
  - `docs/.nav.yml`, `docs/index.md`;
  - `generated-paths.txt`, `scripts/check_conventions.py`, `scripts/test_conventions.py`;
  - i controlli dei tab in `scripts/`;
  - `rpsd-doc-site-design.md`, `openspec/seed.md`, `CLAUDE.md`, `openspec/config.yaml`, `README.md`/`CONTRIBUTING.md` (dove elencano le sezioni).
- **File nuovi**: `docs/rapsodia/`, `docs/architettura/`, `docs/modello-dati/`, `docs/dashboard/`, `docs/contratti/` (con `esempio/`), ciascuno con `index.md` e `.nav.yml`.
- **URL pubblicati nuovi**:
  - `/rapsodia/…`;
  - `/architettura/…`;
  - `/modello-dati/`;
  - `/dashboard/`;
  - `/contratti/`, `/contratti/esempio/`.

  Tutti stabili salvo `/contratti/esempio/`, temporaneo per scelta.
- **Rischio**: nove tab possono non entrare in una riga su schermi stretti; va verificato nel sito costruito (design D6).
