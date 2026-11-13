# Design — add-profile-versioning

## Context

Motivazione e perimetro: `proposal.md`. Requisiti: `specs/profile-versioning/spec.md` (seed §4.4 senza modifiche).

Stato attuale: `docs/netex/` e `docs/siri/` contengono solo `index.md` segnaposto e un `.nav.yml` con `nav: [index.md, "*"]`. Plugin `redirects` attivo con `redirect_maps` vuoto. Nessun override del template. I controlli girano nei job obbligatori "Build strict del sito" e "Spike (scala, sidebar, link rotti)" di `pr.yml`; `check_urls.py` garantisce già che nessun URL pubblicato sparisca.

### Verifiche fatte in fase di proposta (13 novembre 2026, Zensical 0.1.1)

Prova su un sito usa e getta con NeTEx 5.0.0 (precedente) e 5.1.0 (corrente):

| Punto | Esito |
|---|---|
| `theme.custom_dir` con `main.html` che estende `base.html` e ridefinisce `block content` chiamando `super()` | Funziona |
| Motore dei template | **Non è Jinja2**: `page.url.split("/")` fallisce ("string has no method named split"). Funzionano filtri e operatori comuni a Jinja2: `dictsort`, slicing (`page.url[:n]`), `length`, concatenazione `~`, `super()` |
| Lettura di `config.extra` dal template | Funziona |
| Avviso su pagina di versione non corrente | Presente su `netex/5.0.0/` e `netex/5.0.0/frame/resourceframe/`, assente su `netex/5.1.0/…` e `netex/`; link alla corrente corretto (`base_url`) |
| Pagine non elencate nella sidebar | Costruite e pubblicate senza warning |
| `redirect_maps: netex/corrente/index.md: netex/5.1.0/index.md` | `netex/corrente/` rimanda a `../5.1.0/` |

## Goals / Non-Goals

**Goals**
- Un solo punto da aggiornare per stato e versione corrente, con controlli che segnalano ogni incoerenza.
- Pubblicare una nuova versione senza modificare i file delle versioni precedenti.
- Ogni scenario di `profile-versioning` verificato in CI, anche quello con due versioni (che sul sito reale ancora non esiste) tramite prove su fixture.

**Non-Goals**
- Contenuti dei profili; alias per singola pagina; scelta della granularità delle versioni.

## Decisions

### D1. Metadati in `mkdocs.yml` (`extra.profili`)

```yaml
extra:
  profili:
    netex:
      titolo: NeTEx
      corrente: "5.0.0"
      versioni:
        "5.0.0": corrente
    siri:
      titolo: SIRI
      corrente: "1.0.5"
      versioni:
        "1.0.5": corrente
```

Stati ammessi: `corrente`, `precedente`, `ritirata` (requisito *Version list*). È l'unico punto letto dal template (D3) ed è la fonte dei controlli (D6).
*Alternativa scartata*: file YAML separato (il template legge solo `config.extra`).

### D2. Struttura delle cartelle e pagine

- `docs/<profilo>/<versione>/index.md`: pagina indice della versione, titolo "Profilo NeTEx 5.0.0" / "Profilo SIRI 1.0.5" e callout `note` "Sezione in preparazione". Ogni cartella di versione ha un `.nav.yml` con `nav: [index.md, "*"]` (convenzione di `site-navigation`).
- `docs/<profilo>/index.md`: pagina elenco versioni, redazionale. Callout `note` per il testo introduttivo da scrivere con le fonti, poi la tabella:

  | Versione | Stato | Date | Differenze rispetto alla versione precedente |
  |---|---|---|---|
  | [5.0.0](5.0.0/index.md) | corrente | _da completare_ | _da completare_ |

  Formato fisso della prima colonna (`[<versione>](<versione>/index.md)`), letto dal controllo D6.
- Nessuna pagina sotto `docs/<profilo>/` fuori da una cartella di versione, salvo `index.md` e `.nav.yml` (requisito *One directory per profile version*).

### D3. Avviso sulle versioni non correnti: override del template

`theme.custom_dir: overrides` e `overrides/main.html`:

```jinja
{% extends "base.html" %}
{% block content %}
  {% for nome, profilo in (config.extra.profili or {})|dictsort %}
    {% for versione, stato in profilo.versioni|dictsort %}
      {% set prefisso = nome ~ "/" ~ versione ~ "/" %}
      {% if page.url[:prefisso|length] == prefisso and versione != profilo.corrente %}
        <div class="admonition warning avviso-versione"> … stato, link alla corrente … </div>
      {% endif %}
    {% endfor %}
  {% endfor %}
  {{ super() }}
{% endblock %}
```

Solo costrutti comuni a Zensical e Jinja2 (vedi verifiche), quindi funziona anche con Material. Il callout usa il tipo `warning` (ammesso dalla regola C1 di `content-conventions`); il titolo indica lo stato ("Versione precedente del profilo" / "Versione ritirata del profilo").
*Alternativa scartata*: scrivere l'avviso nelle pagine quando la versione diventa non corrente: modificherebbe pagine congelate.

### D4. Sidebar e alias

- `docs/<profilo>/.nav.yml`: `nav: [index.md, "Profilo <corrente>": <corrente>]`, **senza `"*"`**: le altre versioni sono pubblicate ma raggiungibili solo dalla pagina elenco versioni (requisito *Sidebar shows the current version*).
- `redirect_maps`: `<profilo>/corrente/index.md: <profilo>/<corrente>/index.md`. Aggiornata quando cambia la versione corrente.

### D5. Pubblicare una nuova versione (procedura, in `CONTRIBUTING.md`)

1. Creare `docs/<profilo>/<nuova>/` (pagine nuove; quelle della versione precedente non si toccano).
2. In `extra.profili`: `corrente` = nuova; nuova → `corrente`, precedente → `precedente`.
3. Aggiornare `docs/<profilo>/.nav.yml` e la voce `corrente` di `redirect_maps`.
4. Aggiungere la riga alla tabella di `docs/<profilo>/index.md` e aggiornare lo stato della precedente.

I controlli D6 falliscono se uno dei passi manca.

### D6. Controlli: `scripts/check_versions.py`

Legge `mkdocs.yml` con PyYAML (già nel lock), ignorando i tag `!!python/name`.

- **V1** metadati: per ogni profilo, `corrente` è tra le versioni, ha stato `corrente` ed è l'unica; stati solo tra `corrente`, `precedente`, `ritirata`.
- **V2** cartelle: ogni versione dichiarata ha la sua cartella con `index.md`; ogni cartella di versione (nome `N.N.N`) è dichiarata; nessuna pagina sotto `docs/<profilo>/` fuori dalle cartelle di versione, salvo `index.md`.
- **V3** sidebar: `docs/<profilo>/.nav.yml` contiene `index.md` e la sola cartella della versione corrente, nessun `"*"`.
- **V4** alias: `redirect_maps` contiene `<profilo>/corrente/index.md: <profilo>/<corrente>/index.md`.
- **V5** elenco versioni: la tabella di `docs/<profilo>/index.md` ha una riga per ogni versione dichiarata, con link alla sua cartella e stato uguale ai metadati. I campi "_da completare_" vengono contati e stampati, senza far fallire.
- **V6** (`--site DIR`, sito costruito): ogni pagina HTML sotto una versione non corrente contiene l'avviso con il link alla corrente; nessuna pagina della versione corrente o fuori dalle versioni lo contiene.
- **V7** (`--commits BASE`): ogni commit non di merge in `BASE..HEAD` che modifica file di una versione non corrente (secondo i metadati di HEAD) ha il trailer `Errata: <motivo>`. Il messaggio ricorda che una versione congelata si cambia solo per errata e che una revisione del profilo è una nuova cartella.

### D7. Prove: `scripts/test_versions.py`

`unittest`. Fixture con NeTEx 5.0.0 (precedente) e 5.1.0 (corrente), costruita davvero con Zensical a partire da `mkdocs.yml` e `overrides/` reali:
- *Current NeTEx profile*: la pagina ResourceFrame di prova è servita sotto `netex/5.1.0/`.
- *New profile version published*: rispetto al sito con la sola 5.0.0 nessun URL della 5.0.0 sparisce (`check_urls.compare`) e i sorgenti della 5.0.0 sono invariati.
- *Reader looks for an older version*: la pagina elenco versioni linka entrambe con lo stato giusto (V5).
- *Page of a previous version*: avviso con stato e link alla 5.1.0 sulle pagine della 5.0.0, assente sulla 5.1.0 (V6).
- *Two versions documented*: la sidebar della sezione NeTEx contiene pagine della 5.1.0 e nessuna della 5.0.0 (riuso di `check_sidebar`).
- *Link from the operational guide*: `netex/corrente/` rimanda alla 5.1.0.
- Casi non conformi per V1–V5 e V7 (corrente non dichiarata, cartella non dichiarata, `"*"` nel `.nav.yml`, alias errato, riga mancante, commit senza `Errata`).

### D8. CI

- Job "Build strict del sito": `python scripts/check_versions.py --site site --commits "origin/${GITHUB_BASE_REF}"` dopo il build.
- Job "Spike (scala, sidebar, link rotti)": `python scripts/test_versions.py`.
- Nomi dei job invariati.

### D9. Effetti su spike e script esistenti (aggiunta in apply)

L'override del template e gli alias hanno effetti su ciò che costruisce copie del sito:
- **Spike**: con `INHERIT`, `custom_dir` è relativo al file figlio, quindi `spike/mkdocs.yml` ridefinisce `theme.custom_dir: ../overrides` (le mappe si uniscono). Gli alias ereditati puntano a pagine che lo spike non ha, e un redirect verso una pagina inesistente è un warning (il build strict fallisce): lo spike ridefinisce quindi `plugins` con `redirect_maps` vuoto. Con `INHERIT` la **lista** dei plugin viene sostituita, non unita (verificato: senza ripeterla `awesome-nav` sparisce e `check_sidebar.py` fallisce), per cui lo spike ripete la lista completa e `scripts/spike.py` verifica a ogni esecuzione che coincida con quella di `mkdocs.yml`, salvo `redirect_maps`.
- **Copie temporanee del sito** (`check_urls.py`, `check_new_subsection.py`, `check_broken_link.py`, prove di `test_conventions.py`): copiavano solo `mkdocs.yml` e `docs/`. Ora usano tutte `copy_site_sources()` di `scripts/spike.py`, con l'elenco unico `SITE_SOURCES = ["mkdocs.yml", "docs", "overrides"]`; `check_urls.py` estrae dalla revisione base solo i sorgenti che lì esistono.
- La prova di `test_conventions.py` sullo spostamento di pagina non presuppone più `redirect_maps` vuoto.

## Risks / Trade-offs

- [Il motore dei template di Zensical non è Jinja2 e potrebbe cambiare] → template limitato a costrutti comuni; le prove D7 costruiscono il sito reale e falliscono se l'avviso sparisce.
- [Override del template: Zensical potrebbe cambiare i blocchi di `base.html`] → stesso presidio; l'override tocca un solo blocco (`content`).
- [Metadati in `mkdocs.yml`: cambiare la versione corrente tocca la configurazione] → accettato; è un evento raro e ogni passo dimenticato è segnalato da V1–V5.
- [Il trailer `Errata` si può scrivere a mano] → intercetta l'errore involontario; la revisione della PR resta.
- [Date e differenze da completare pubblicate così] → marcate in modo esplicito e conteggiate dal controllo; si completano quando le fonti sono nel repository.

## Migration Plan

`docs/netex/index.md` e `docs/siri/index.md` cambiano contenuto (da segnaposto a elenco versioni) ma non URL. Nessun URL esistente sparisce.
