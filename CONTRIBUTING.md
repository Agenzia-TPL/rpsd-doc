# Come contribuire a rpsd-doc

Regole per chi scrive o modifica il sito. Ogni regola è verificata in CI sulle pull
request, quando possibile, e rimanda alla fonte: design del sito
(`rpsd-doc-site-design.md`), requisiti (`openspec/specs/`) o `CLAUDE.md`.

## Lingua e tono

Contenuti in italiano; i nomi propri degli standard (frame, delivery, nomi degli
elementi) restano in inglese. Tono tecnico ma accessibile (design §8).

## Pagine redazionali e pagine generate

Una pagina è **o redazionale o generata, mai mista** (design §3).

- Le cartelle generate sono elencate in [`generated-paths.txt`](generated-paths.txt).
  Sono scritte da `rpsd-tools` a partire dai dati in `data/` e dai template in
  `templates/`, e vengono sovrascritte per intero a ogni generazione.
- **Non si modificano a mano.** Per cambiare una pagina generata si cambiano i dati
  sorgente (o il template) e si rigenera.
- Ogni pagina generata dichiara nel front matter `generato: true` e lo strumento che
  l'ha prodotta (`generato_da: rpsd-tools <versione>`).
- Ogni commit che tocca una cartella generata porta il trailer
  `Generato-da: rpsd-tools <versione>`, aggiunto da `rpsd-tools`. Una PR con un
  commit senza trailer su quelle cartelle fallisce.
- In `generated-paths.txt` un `*` vale un solo segmento di percorso:
  `docs/contratti/*/` vuol dire "ogni cartella di contratto". L'indice
  `docs/contratti/index.md` resta quindi **redazionale**: è l'elenco dei contratti e si
  scrive a mano.
- Un **segnaposto** scritto a mano dentro un percorso generato è ammesso solo se è
  dichiarato in `generated-paths.txt` con una riga che inizia con `!` (oggi
  `!docs/contratti/esempio/`). Le sue pagine hanno `segnaposto: true` nel front matter
  e il callout `!!! warning "Contratto segnaposto"`. Il segnaposto `esempio` si toglie,
  insieme alla sua riga, quando arriva il primo contratto generato.

Controllo: `scripts/check_conventions.py` (regole G1, G2, G3, G4).

### Pagine dei profili NeTEx e SIRI

Le cartelle di versione `docs/netex/<versione>/` e `docs/siri/<versione>/` sono
generate. I dati vengono da `rpsd-tools profile-docs generate` (bundle `site.yaml`);
l'impaginazione è dei template di questo repository, in `templates/profili/`, applicati
da `scripts/generate_profile_pages.py`.

Per aggiornare un profilo:

1. in un checkout di rpsd-tools: `uv run rpsd-tools profile-docs generate
   profiles/netex-it --out <cartella>` (o `profiles/siri-it`);
2. copiare `<cartella>/netex-it/site.yaml` in `data/profili/netex/<versione>/site.yaml`
   (`data.yaml` non serve al sito);
3. `python scripts/generate_profile_pages.py --all`;
4. committare bundle e pagine insieme, con il trailer
   `Generato-da: rpsd-tools <versione>` preso dalla chiave `generator` del bundle.

Una modifica ai template si committa con le pagine rigenerate. Se cambia le pagine di
una versione non corrente è un'errata e porta anche il trailer `Errata: <motivo>`.

Controllo: `python scripts/generate_profile_pages.py --all --check` fallisce se le
pagine committate non corrispondono al bundle.

I template partono dal Markdown di riferimento di rpsd-tools ma possono discostarsene
di proposito. Differenze volute oggi: la Panoramica non ha il titolo «Busta» né la
riga «Elementi: …», che le linee guida 5T non usano (change `remove-envelope-heading`).

## Lunghezza

Una pagina redazionale non supera **1500 parole** (design §8). Il conteggio esclude
front matter e blocchi di codice: gli esempi XML non sono prosa. Oltre il limite, la
pagina va divisa.

Controllo: `scripts/check_conventions.py` (regola L1).

## Callout

Insieme fisso di callout con significato fisso (spec `content-conventions`):

| Callout | Titolo | Uso |
|---|---|---|
| `note` | libero | nota |
| `tip` | libero | suggerimento |
| `warning` | libero | attenzione |
| `example` | libero | esempio |
| `danger` | **"Obbligatorio per KPI"** (solo questo) | campo la cui assenza impedisce il calcolo di un indicatore |
| `info` | **"Novità Rapsodia"** (solo questo) | campo o struttura aggiunti al profilo italiano per gli indicatori ART |

Sintassi: `!!! tipo "Titolo"` (o `???` / `???+` per i callout richiudibili). Altri
tipi non sono ammessi; i due titoli riservati non si usano con altri tipi.

Controllo: `scripts/check_conventions.py` (regola C1). Il controllo verifica la
forma; l'uso corretto (per esempio che un campo sia davvero obbligatorio per un KPI)
resta alla revisione.

## Glossario e sigle

- Il glossario è `docs/guida/glossario.md`, nella Guida operativa. Ogni sigla è un titolo con anchor
  esplicito e classe `sigla`:

  ```markdown
  ### PdE {#pde .sigla}
  ```

- In ogni pagina, il **primo uso** di una sigla del glossario è un link alla sua voce,
  per esempio `[PdE](../guida/glossario.md#pde)`. Gli usi successivi sono liberi.
  Contano anche tabelle e testo dei callout; non contano titoli di pagina, titoli dei
  callout (dove un link non viene reso) e codice.

Controllo: `scripts/check_conventions.py` (regola S1).

## URL stabili

Gli URL pubblicati non cambiano (design §8): codici indicatore, id regola, id
contratto e percorsi delle pagine sono stabili. Se una pagina pubblicata deve essere
spostata o rinominata, si aggiunge in `mkdocs.yml`, sotto
`plugins → redirects → redirect_maps`, una riga:

```yaml
vecchio/percorso.md: nuovo/percorso.md
```

Eccezione: una pagina che sul branch di destinazione è **solo un segnaposto** (titolo
e callout `note` «Sezione in preparazione», nient'altro) si può togliere o spostare
senza redirect, perché non ha mai pubblicato contenuto. Una pagina con l'avviso più
altro contenuto (per esempio la tabella delle versioni in `netex/index.md`) non è un
segnaposto e resta protetta.

Controllo: `scripts/check_urls.py`, che confronta gli URL della PR con quelli del
branch di destinazione ed elenca a parte i segnaposto tolti.

## Navigazione

Tab e sidebar sono definiti dai file `.nav.yml` di ogni cartella: vedi la sezione
"Navigazione" del [README](README.md).

## Versioni del sito

`docs/rapsodia/versioni.md` elenca le modifiche al sito in una tabella, dalla più
recente: una riga per ogni change completata e pubblicata, con la data di
archiviazione, l'area e lo scopo ripreso dalla sua proposal.

| Area | Icona |
|---|---|
| Profili | `:material-file-document-multiple-outline:` |
| Struttura | `:material-sitemap-outline:` |
| Convenzioni | `:material-check-decagram-outline:` |
| Navigazione | `:material-compass-outline:` |
| Sito | `:material-rocket-launch-outline:` |

La home mostra l'intestazione e le righe comprese fra i marcatori
`<!-- --8<-- [start:recenti] -->` e `<!-- --8<-- [end:recenti] -->`, incluse con
`pymdownx.snippets`: si scrivono una volta sola. I marcatori stanno fra le righe della
tabella e non la spezzano, perché `pymdownx.snippets` li toglie prima del rendering.

Quando si aggiunge una riga in cima, si sposta il marcatore `end:recenti` in modo che
fra i due marcatori restino l'intestazione e le **tre** righe più recenti.

## Profili versionati

`docs/netex/<versione>/` e `docs/siri/<versione>/` contengono una copia congelata per
versione di profilo (`CLAUDE.md`, design §2.3, spec `profile-versioning`).

- La versione corrente e lo stato di ogni versione (corrente, precedente, ritirata)
  stanno in `mkdocs.yml`, sotto `extra.profili`.
- La sidebar mostra solo la versione corrente; le altre si raggiungono dall'elenco
  versioni in `docs/<profilo>/index.md`.
- Le pagine delle versioni non correnti ricevono in automatico un avviso con il link
  alla versione corrente (override del template in `overrides/main.html`): non si
  scrive a mano.
- `netex/corrente/` e `siri/corrente/` portano alla versione corrente.

**Una versione non corrente non si modifica**, salvo errata: un commit che la tocca
deve avere il trailer `Errata: <motivo>`. Una revisione del profilo è una nuova
cartella.

**Pubblicare una nuova versione** (es. NeTEx 5.1.0 dopo 5.0.0):

1. aggiungere il bundle in `data/profili/netex/5.1.0/` e generare `docs/netex/5.1.0/`
   (sezione "Pagine dei profili NeTEx e SIRI"; la cartella `5.0.0/` non si tocca);
2. in `mkdocs.yml`, `extra.profili.netex`: `corrente: "5.1.0"`, `"5.1.0": corrente`,
   `"5.0.0": precedente`;
3. in `docs/netex/.nav.yml` sostituire la voce della versione con `Profilo 5.1.0: 5.1.0`,
   e in `redirect_maps` far puntare `netex/corrente/index.md` a `netex/5.1.0/index.md`;
4. in `docs/netex/index.md` aggiungere la riga della 5.1.0 e cambiare lo stato della
   5.0.0 in `precedente`;
5. nella home (`docs/index.md`), scheda NeTEx, cambiare «Versione corrente» in
   `[5.1.0](netex/5.1.0/index.md)`.

Se manca un passo, il controllo fallisce indicando quale.

Controllo: `scripts/check_versions.py` (regole V1–V8).

## Contenuti e fonti

Nessun contenuto inventato: ogni campo, vincolo o regola viene da un documento
sorgente. Le pagine generali non riportano soglie contrattuali né riferimenti ad
allegati di gara (`CLAUDE.md`, design §8).

## Controlli in locale

```bash
zensical build --strict
python scripts/check_navigation.py
python scripts/check_conventions.py --commits origin/main
python scripts/check_urls.py origin/main
python scripts/check_versions.py --site site --commits origin/main
python scripts/test_conventions.py
python scripts/test_versions.py
```

Gli altri controlli della CI sono elencati nel [README](README.md).

## Flusso di lavoro

Ogni modifica passa da OpenSpec (`/opsx:propose` → revisione → `/opsx:apply` →
`/opsx:archive`), un change per branch, e arriva su `main` con una pull request i cui
controlli devono essere verdi.
