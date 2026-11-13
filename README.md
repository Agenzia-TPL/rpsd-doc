# rpsd-doc

Sito di documentazione di Rapsodia: profili NeTEx e SIRI italiani, indicatori
ART (Delibera ART 53/2024) e, in un secondo step, una sezione per contratto di
servizio. Generatore: [Zensical](https://zensical.org/docs/), con la
configurazione in `mkdocs.yml`. Design completo: `rpsd-doc-site-design.md`.

Per scrivere o modificare contenuti: regole e controlli in [CONTRIBUTING.md](CONTRIBUTING.md).

## Requisiti

- Python 3.13 (versione in `.python-version`)
- Nessuna toolchain Node

## Installazione

```bash
python3.13 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

`requirements.txt` blocca tutte le dipendenze (dirette e transitive). Per
aggiornarle: modificare `requirements.in`, installarlo in un `.venv` pulito e
rigenerare il lock con `pip freeze > requirements.txt` (mantenendo la riga di
intestazione). Ogni aggiornamento di Zensical è deliberato: ripetere lo spike
prima di adottarlo.

## Build

Comando unico, dalla radice del repository:

```bash
zensical build --strict
```

Il sito viene scritto in `site/`. In modalità strict il build fallisce su
qualsiasi warning, compresi i link a pagine o anchor inesistenti; l'errore
indica file, riga e link. Attenzione: anche un build fallito scrive `site/`,
quindi conta solo il codice di uscita.

Anteprima locale con ricaricamento automatico:

```bash
zensical serve
```

Non usare `mkdocs build`/`mkdocs serve` né `zensical new` (creerebbe
`zensical.toml`; nella fase 1 la configurazione resta in `mkdocs.yml`).

## Navigazione

La navigazione è definita per directory con file `.nav.yml` (formato awesome-nav,
integrato in Zensical); `mkdocs.yml` non contiene `nav`.

- `docs/.nav.yml` definisce i **tab di primo livello** e il loro ordine:
  Home, NeTEx, SIRI, Indicatori, Guida operativa. È un elenco esplicito, senza `"*"`:
  una cartella nuova in `docs/` non diventa un tab finché non viene aggiunta qui.
- Ogni cartella di sezione e sottosezione ha il **proprio `.nav.yml`**, con un titolo
  (se diverso dal nome della cartella) e un `nav` che elenca le voci da tenere in un
  ordine preciso e **termina con `"*"`**:

  ```yaml
  title: Titolo nella sidebar   # facoltativo
  nav:
    - index.md
    - pagina-da-mettere-prima.md
    - "*"                       # tutto il resto, in ordine alfabetico
  ```

  Senza `"*"` le pagine non elencate vengono pubblicate ma **non compaiono** nella
  sidebar, senza alcun avviso.
- Per aggiungere una sottosezione basta creare la cartella con le pagine e il suo
  `.nav.yml`: non serve toccare `mkdocs.yml` né il `.nav.yml` del livello superiore.
- Eccezione: `docs/netex/.nav.yml` e `docs/siri/.nav.yml` elencano solo la versione
  corrente del profilo, senza `"*"` (vedi CONTRIBUTING.md, "Profili versionati").

Nota: finché le sezioni contengono solo `index.md`, il loro `"*"` non trova nulla;
per non bloccare il build strict `mkdocs.yml` imposta temporaneamente
`logs.no_matches: info` (vedi il `TODO` in `mkdocs.yml` e `openspec/seed.md` §5).

## Spike delle funzioni di rendering

La cartella `spike/` contiene pagine di prova non normative, una per funzione
di rendering richiesta (XML annotato, varianti a tab, formule, diagrammi
Mermaid, ricerca in italiano). Usano la stessa configurazione del sito
(`spike/mkdocs.yml` eredita da `mkdocs.yml`) ma **non** fanno parte del sito
pubblicato. Esito delle verifiche: `spike/REPORT.md`; bozze di issue per
Zensical (da aprire solo con approvazione): `spike/ISSUES-zensical.md`.

```bash
python scripts/spike.py                 # build strict delle pagine di prova
python scripts/spike.py --scale         # + 400 pagine generate, tempo ≤ 60 s, controllo sidebar (anche pagina a tre livelli)
python scripts/check_broken_link.py     # verifica che il build strict fallisca su link e anchor rotti
python scripts/check_new_subsection.py  # verifica che una sottosezione nuova compaia senza modificare la configurazione
zensical serve -f spike/mkdocs.yml      # anteprima delle pagine di prova (dopo python scripts/spike.py)
```

## Integrazione continua e pubblicazione

I workflow sono in `.github/workflows/` e partono solo quando il repository è su
GitHub:

| Workflow | Quando | Cosa fa |
|---|---|---|
| `pr.yml` | ogni pull request | job `build`: `zensical build --strict` del sito, `python scripts/check_navigation.py` (tab), `python scripts/check_conventions.py --commits origin/<base>` (convenzioni di contenuto, vedi CONTRIBUTING.md), `python scripts/check_urls.py origin/<base>` (URL stabili) e `python scripts/check_versions.py --site site --commits origin/<base>` (versioni dei profili); job `spike`: `python scripts/spike.py --scale` (400 pagine, limite 60 s, sidebar), `python scripts/check_broken_link.py`, `python scripts/check_new_subsection.py`, `python scripts/test_conventions.py` e `python scripts/test_versions.py` (prove dei controlli). Un errore in uno dei due job fa fallire il controllo della PR, obbligatorio per il merge su `main` |
| `deploy.yml` | push su `main` (e avvio manuale) | job `build`: build strict e caricamento di `site/` come artifact di Pages; job `deploy`: pubblicazione su GitHub Pages. Se il build fallisce, `deploy` non parte e il sito pubblicato resta invariato |

Per riprodurre i controlli in locale:

```bash
zensical build --strict
python scripts/check_navigation.py
python scripts/check_conventions.py --commits origin/main
python scripts/check_urls.py origin/main
python scripts/check_versions.py --site site --commits origin/main
python scripts/spike.py --scale
python scripts/check_broken_link.py
python scripts/check_new_subsection.py
python scripts/test_conventions.py
python scripts/test_versions.py
```

### Passi manuali su GitHub (riservati a Franco)

Nessuno di questi passi è automatizzato e ognuno richiede un'approvazione esplicita.
Stato al 13 novembre 2026: tutti eseguiti (repository `Agenzia-TPL/rpsd-doc` pubblico,
Pages da GitHub Actions, `main` protetto, URL impostati, primo run verificato in
`spike/REPORT.md`). Restano qui come riferimento per un eventuale nuovo repository.

1. Creare il repository remoto e fare il primo push di `main`.
2. In *Settings → Pages* impostare come sorgente **GitHub Actions**.
3. In *Settings → Branches* proteggere `main` richiedendo i controlli
   "Build strict del sito" e "Spike (scala, sidebar, link rotti)" di `pr.yml`
   prima del merge.
4. Sostituire in `mkdocs.yml` i segnaposto `site_url` e `repo_url` (marcati `TODO`)
   con l'URL pubblico del sito e del repository.
5. Al primo run, controllare in CI il tempo di build riportato da
   `scripts/spike.py --scale` (limite 60 s sul runner `ubuntu-latest`).
