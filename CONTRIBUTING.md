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

Controllo: `scripts/check_conventions.py` (regole G1, G2, G3).

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

- Il glossario è `docs/panoramica/glossario.md`. Ogni sigla è un titolo con anchor
  esplicito e classe `sigla`:

  ```markdown
  ### PdE {#pde .sigla}
  ```

- In ogni pagina, il **primo uso** di una sigla del glossario è un link alla sua voce,
  per esempio `[PdE](../panoramica/glossario.md#pde)`. Gli usi successivi sono liberi.
  Contano anche tabelle e callout; non contano titoli e codice.

Controllo: `scripts/check_conventions.py` (regola S1).

## URL stabili

Gli URL pubblicati non cambiano (design §8): codici indicatore, id regola, id
contratto e percorsi delle pagine sono stabili. Se una pagina pubblicata deve essere
spostata o rinominata, si aggiunge in `mkdocs.yml`, sotto
`plugins → redirects → redirect_maps`, una riga:

```yaml
vecchio/percorso.md: nuovo/percorso.md
```

Controllo: `scripts/check_urls.py`, che confronta gli URL della PR con quelli del
branch di destinazione.

## Navigazione

Tab e sidebar sono definiti dai file `.nav.yml` di ogni cartella: vedi la sezione
"Navigazione" del [README](README.md).

## Profili versionati

`docs/netex/<versione>/` e `docs/siri/<versione>/` contengono una copia congelata per
versione di profilo: una versione non corrente non si modifica, salvo errata. Una
nuova versione è una nuova cartella (`CLAUDE.md`, design §2.3).

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
python scripts/test_conventions.py
```

Gli altri controlli della CI sono elencati nel [README](README.md).

## Flusso di lavoro

Ogni modifica passa da OpenSpec (`/opsx:propose` → revisione → `/opsx:apply` →
`/opsx:archive`), un change per branch, e arriva su `main` con una pull request i cui
controlli devono essere verdi.
