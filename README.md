# rpsd-doc

Sito di documentazione di Rapsodia: profili NeTEx e SIRI italiani, indicatori
ART (Delibera ART 53/2024) e, in un secondo step, una sezione per contratto di
servizio. Generatore: [Zensical](https://zensical.org/docs/), con la
configurazione in `mkdocs.yml`. Design completo: `rpsd-doc-site-design.md`.

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

## Spike delle funzioni di rendering

La cartella `spike/` contiene pagine di prova non normative, una per funzione
di rendering richiesta (XML annotato, varianti a tab, formule, diagrammi
Mermaid, ricerca in italiano). Usano la stessa configurazione del sito
(`spike/mkdocs.yml` eredita da `mkdocs.yml`) ma **non** fanno parte del sito
pubblicato. Esito delle verifiche: `spike/REPORT.md`; bozze di issue per
Zensical (da aprire solo con approvazione): `spike/ISSUES-zensical.md`.

```bash
python scripts/spike.py                 # build strict delle pagine di prova
python scripts/spike.py --scale         # + 400 pagine generate, tempo ≤ 60 s, controllo sidebar
python scripts/check_broken_link.py     # verifica che il build strict fallisca su link e anchor rotti
zensical serve -f spike/mkdocs.yml      # anteprima delle pagine di prova (dopo python scripts/spike.py)
```

## Integrazione continua e pubblicazione

I workflow sono in `.github/workflows/` e partono solo quando il repository è su
GitHub:

| Workflow | Quando | Cosa fa |
|---|---|---|
| `pr.yml` | ogni pull request | job `build`: `zensical build --strict` del sito; job `spike`: `python scripts/spike.py --scale` (400 pagine, limite 60 s, controllo sidebar) e `python scripts/check_broken_link.py`. Un errore in uno dei due job fa fallire il controllo della PR |
| `deploy.yml` | push su `main` (e avvio manuale) | job `build`: build strict e caricamento di `site/` come artifact di Pages; job `deploy`: pubblicazione su GitHub Pages. Se il build fallisce, `deploy` non parte e il sito pubblicato resta invariato |

Per riprodurre i controlli in locale:

```bash
zensical build --strict
python scripts/spike.py --scale
python scripts/check_broken_link.py
```

### Passi manuali su GitHub (riservati a Franco)

Nessuno di questi passi è automatizzato e ognuno richiede un'approvazione esplicita:

1. Creare il repository remoto e fare il primo push di `main`.
2. In *Settings → Pages* impostare come sorgente **GitHub Actions**.
3. In *Settings → Branches* proteggere `main` richiedendo i controlli
   "Build strict del sito" e "Spike (scala, sidebar, link rotti)" di `pr.yml`
   prima del merge.
4. Sostituire in `mkdocs.yml` i segnaposto `site_url` e `repo_url` (marcati `TODO`)
   con l'URL pubblico del sito e del repository.
5. Al primo run, controllare in CI il tempo di build riportato da
   `scripts/spike.py --scale` (limite 60 s sul runner `ubuntu-latest`).
