# Brief: pubblicare le pagine dei profili NeTEx e SIRI generate da rpsd-tools

Input per `/opsx:propose` in rpsd-doc. Raccoglie quello che rpsd-tools produce per la documentazione dei profili, come diventa pagine del sito e cosa resta da decidere qui. Stato al 16 novembre 2026, con le decisioni prese da Franco lo stesso giorno.

## Decisioni già prese (Franco, 16/11/2026)

1. **Le pagine si producono in rpsd-doc, con i template del sito.** rpsd-tools fornisce i dati, cioè il bundle YAML, e rpsd-doc li trasforma in Markdown con template Jinja in `templates/`, eseguiti da uno script di rpsd-doc. Così le pagine dei profili seguono le stesse convenzioni delle altre (callout, avvisi, glossario) e l'impaginazione cambia senza rilasciare rpsd-tools. È il flusso del §3.1 del design, con una differenza: il motore che esegue i template è uno script di rpsd-doc, non rpsd-tools.
2. **Il bundle si committa in rpsd-doc**, in `data/`, così ogni versione pubblicata è riproducibile e il diff del bundle spiega il diff delle pagine.
3. **Le incongruenze si pubblicano.** Il sito deve anche mostrarle finché la piattaforma non va in produzione; poi si risolvono con il 5T e la pagina si toglie.

Il Markdown che rpsd-tools genera oggi (`profile-docs generate`) resta come riferimento e anteprima: mostra un'impaginazione già verificata sul sito, ma rpsd-doc non lo copia.

## Da dove arriva

In rpsd-tools il comando `profile-docs generate` scrive la documentazione del profilo italiano partendo da due fonti: l'XSD della versione e le note delle linee guida del 5T, mappate riga per riga e riviste da Franco. Scrive i dati (il bundle `site.yaml` e i dati completi `data.yaml`) e, da quei dati, un Markdown di riferimento.

Due change di rpsd-tools hanno dato all'output la forma attuale:

| Change | Cosa ha fatto | PR |
|---|---|---|
| `profile-docs-by-frame` | Pagine per frame NeTEx e servizio SIRI al posto delle pagine per tipo XSD: una tabella per oggetto, in cascata, sul modello dell'Excel di Franco e del profilo nordico di Entur. Front matter e `.nav.yml` per questo sito | Agenzia-TPL/rpsd-tools#2 |
| `add-profile-common-structures` | Pagina «Strutture comuni» sul modello del framework di Entur, con una descrizione unica ricavata dalle note del 5T | Agenzia-TPL/rpsd-tools#3, impilata sulla #2 |

Le due PR non sono ancora su `main` di rpsd-tools e la release che le contiene non è ancora fatta. Finché non c'è, `generator` del bundle riporta `rpsd-tools 0.6.0`. Non è un problema: il sito non è in produzione. Il brief da cui sono partite le due change e le analisi stanno in rpsd-tools, in `openspec/changes/archive/2026-11-16-profile-docs-by-frame/` e `…-add-profile-common-structures/`.

## Il bundle

Il bundle è `site.yaml`, scritto da `profile-docs generate` accanto alle pagine di riferimento (change `add-profile-site-bundle` di rpsd-tools, del 18/11/2026):

```bash
uv sync --all-packages
uv run rpsd-tools profile-docs generate profiles/netex-it --out <cartella>
uv run rpsd-tools profile-docs generate profiles/siri-it  --out <cartella>
```

Il formato è il JSON Schema `contracts/profile-data.schema.json` di rpsd-tools. Le chiavi che servono al sito sono:
- `pages`: pagine, in ordine, con `file` e `title`, e per ognuna le tabelle in cascata (`anchor`, `title`, `level`, `parent`, `group`, `description`, `xsd_type`, `section`, `table`), con le righe (`field`, `card`, `type`, `enumeration`, `values`, `example`, `note`, `common_meaning`, `link`) e gli `other_fields`;
- `identification`, `enumerations` (solo quelle usate dalle pagine, con `anchor`), `issues` e `text_issues`;
- `title`, `xsd`, `guidelines`, `version`, `review`, `generator`.

Ogni incongruenza ha un `id` stabile: è l'ancora della sua riga in `issues.md` e la destinazione del link «⚠ Incongruenza» delle pagine. Le incongruenze della stessa nota condividono l'id. `site.yaml` pesa circa 950 KB per il NeTEx e 250 KB per il SIRI.

Accanto c'è `data.yaml`: lo stesso formato con in più `types`, i record di ogni tipo XSD per gli agenti (4,3 e 3,4 MB). Al sito non serve. Un test di rpsd-tools rende il Markdown di riferimento dal solo `site.yaml` e lo confronta con quello generato: è la garanzia che ai template non manca nessun dato.

## Cosa produce oggi il generatore Markdown di rpsd-tools (riferimento per i template)

### NeTEx (`netex-it`, XSD `netex-it-lev5@cecb0cd`, linee guida 5.0.0)

| File | Titolo in `.nav.yml` | Contenuto | Dimensione |
|---|---|---|---|
| `index.md` | Panoramica | Linee guida e XSD, elenco dei frame, tabelle della busta (`PublicationDelivery`, `CompositeFrame`) | 5 KB, 3 tabelle |
| `general-frame.md` | GeneralFrame | §5.2.1 | 4 KB, 2 tabelle |
| `service-calendar-frame.md` | ServiceCalendarFrame | §5.2.2 | 11 KB, 6 tabelle |
| `resource-frame.md` | ResourceFrame | §5.2.3 | 99 KB, 34 tabelle |
| `site-frame.md` | SiteFrame | §5.2.4 | 43 KB, 12 tabelle |
| `service-frame.md` | ServiceFrame | §5.2.5 | 47 KB, 16 tabelle |
| `timetable-frame.md` | TimetableFrame | §5.2.6 | 28 KB, 8 tabelle |
| `fare-frame.md` | FareFrame | §5.2.7 | 56 KB, 28 tabelle |
| `mobility-service-frame.md` | MobilityServiceFrame | §5.2.8 | 13 KB, 7 tabelle |
| `common.md` | Strutture comuni | Identificazione, Validità, Accessibilità, Tipo di frame, Veicoli, Presentazione, Contatti e indirizzi | 16 KB |
| `enumerations.md` | Enumerazioni | Valori dell'XSD delle enumerazioni usate | 27 KB |
| `issues.md` | Incongruenze | Differenze fra linee guida, XSD Lev5 ed esempi | 169 KB |
| `.nav.yml` | — | Sidebar della versione, titoli in italiano | |
| `site.yaml` | — | Il bundle (vedi sopra), da committare in `data/` | 950 KB |
| `data.yaml` | — | Dati completi per gli agenti, non serve al sito | 4,3 MB |

### SIRI (`siri-it`, XSD `siri@v2.2.1`, linee guida 1.0.5)

`index.md` (Panoramica, busta `ServiceDelivery`), `siri-vm.md`, `siri-et.md`, `siri-sx.md`, `siri-fm.md`, `siri-pt.md`, `common.md` (Riferimenti alla corsa), `enumerations.md`, `issues.md`, `.nav.yml`, `site.yaml` e `data.yaml`. La pagina più grande è di 23 KB.

### Forma delle pagine

- **Front matter**, come chiede `CONTRIBUTING.md`, seguito dal marcatore:
  ```
  ---
  generato: true
  generato_da: rpsd-tools 0.6.0
  ---
  <!-- GENERATED — DO NOT EDIT · profile-docs netex-it · netex-it-lev5@cecb0cd -->
  ```
  `.nav.yml`, `site.yaml` e `data.yaml` iniziano con `# GENERATED — DO NOT EDIT …`.
- **Tabelle**, una per oggetto, in cascata: TimetableFrame → vehicleJourneys / ServiceJourney → passingTimes / TimetabledPassingTime. Le colonne sono Campo · Cardinalità (dell'XSD) · Tipo · Esempio · Significato (5T) · Fonte (§ e tabella delle linee guida). I campi dell'XSD che le linee guida non citano stanno in un riquadro chiuso, «Altri campi dell'XSD».
- **Link**, tutti relativi alla cartella: alle tabelle figlie, alle tabelle degli oggetti puntati dai `…Ref` anche in altre pagine, a `common.md`, a `enumerations.md` e a `issues.md`.
- **Estensioni Markdown**, tutte già attive in `mkdocs.yml`:
  - `attr_list` per le ancore dei titoli (`### vehicleJourneys / ServiceJourney {#vehiclejourneys-servicejourney}`);
  - `admonition` e `pymdownx.details` per il riquadro chiuso (`??? note "Altri campi dell'XSD"`);
  - HTML in linea (`<a id="…"></a>`) per le ancore delle righe di `issues.md`.
- **Ancore stabili**: derivano dal percorso dell'oggetto, non dal numero della tabella del Word, quindi reggono fra versioni delle linee guida e funzionano anche sotto l'alias `corrente`.

## Dove va nel sito

| Bundle | Pagine |
|---|---|
| `data/profili/netex/5.0.0/` (bundle NeTEx) | `docs/netex/5.0.0/` |
| `data/profili/siri/1.0.5/` (bundle SIRI) | `docs/siri/1.0.5/` |

I percorsi di `data/` sono una proposta. Le pagine generate sostituiscono il segnaposto «Sezione in preparazione» della versione e il suo `.nav.yml` (`index.md` + `"*"`). I `.nav.yml` di `docs/netex/` e `docs/siri/` restano come sono: già puntano a `Profilo 5.0.0: 5.0.0` e `Profilo 1.0.5: 1.0.5`.

## Verifiche già fatte

Il Markdown di rpsd-tools è stato copiato in una copia di rpsd-doc (non nel repository) al posto delle due cartelle. Esiti:
- `zensical build --strict`: nessun avviso;
- `scripts/check_conventions.py`, con `docs/netex/*/` e `docs/siri/*/` aggiunti a `generated-paths.txt`: G1, G2, G4, L1, C1 e S1 tutti OK.

Le pagine prodotte dai template di rpsd-doc dovranno passare gli stessi controlli.

## Cosa fare in rpsd-doc

1. **Bundle in `data/`**: copiare `site.yaml` dei due profili da un checkout di rpsd-tools. Il commit porta il trailer `Generato-da: rpsd-tools <versione>`, preso da `generator` del bundle.
2. **Template Jinja in `templates/`** per Panoramica, pagina di frame o servizio, Strutture comuni, Enumerazioni, Incongruenze e `.nav.yml`, sul modello del Markdown di riferimento:
   - stessa forma delle tabelle;
   - riquadro chiuso «Altri campi dell'XSD»;
   - ancore `{#…}` uguali a quelle del bundle, che sono stabili fra versioni e reggono l'alias `corrente`;
   - front matter `generato: true` e `generato_da`.
3. **Uno script in `scripts/`**, per esempio `generate_profile_pages.py <bundle> <cartella>`, che legge il bundle, applica i template e sostituisce per intero la cartella della versione. Deve essere ripetibile, con lo stesso output dallo stesso bundle, e girare in CI per controllare che le pagine committate corrispondano al bundle.
4. **`generated-paths.txt`**: aggiungere `docs/netex/*/` e `docs/siri/*/`.
5. **Avviso sulle versioni non correnti** (`profile-versioning`): lo aggiunge il template, leggendo lo stato della versione da `extra.profili` in `mkdocs.yml`. Le pagine generate non si toccano a mano, quindi non c'è un altro modo.
6. **Pagina «Informazioni generali»** del NeTEx e del SIRI, scritta a mano sotto `NeTEx` e `SIRI`, fuori dalla cartella della versione: introduzione, concetti ed esempi commentati.
7. **Tabella delle versioni** in `docs/netex/index.md` e `docs/siri/index.md` (date e differenze), se ci sono le fonti.

## Decisioni ancora da prendere qui

1. **Il piano del seed.** Le change 6 e 7 (`add-netex-profile-docs`, `add-siri-profile-docs`) prevedono introduzione, concetti, una pagina per frame o servizio ed esempi. Le pagine per frame e servizio ora vengono dal bundle. Proposta:
   - una change «pagine di profilo generate», per NeTEx e SIRI insieme visto che il meccanismo è lo stesso, che copre i punti 1–5 sopra;
   - le change 6 e 7 ridotte alla parte redazionale (punto 6).

   Va aggiornato anche il §3 del design: lo strumento non è `rpsd-profile-gen` ma il bundle di `rpsd-tools profile-docs` più lo script di rpsd-doc.
2. **Dimensione delle pagine.** La più grande è il ResourceFrame: 34 tabelle, una per attrezzatura, più veicoli e organizzazioni, e 99 KB nel Markdown di riferimento. Non è un problema di build. Va solo provata sul sito: se scorrerla è scomodo, il template può dividerla in sottopagine, per esempio le attrezzature.
3. **Callout riservati.** Il bundle oggi non ha i dati per «Novità Rapsodia» né per «Obbligatorio per KPI» (`CONTRIBUTING.md`). Per il secondo rpsd-tools ha già l'informazione: i requisiti NeTEx e SIRI degli indicatori, in `inputs/requirements.yaml`. Si può chiedere di aggiungerla al bundle in una change successiva di rpsd-tools; per ora resta fuori.

## Fuori scope

- Le modifiche a rpsd-tools: il bundle del sito (`site.yaml`, id delle incongruenze) è arrivato con la change `add-profile-site-bundle`; altre richieste si portano là come change separate.
- La sezione Contratti e le regole di validazione, che sono il secondo step.
