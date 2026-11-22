# Tasks — add-site-releases

Nessun task fa push, crea tag, apre PR o tocca le impostazioni GitHub senza approvazione di Franco.

## 1. Controllo della release

- [x] 1.1 Scrivere `scripts/check_release.py` con le regole R1–R4 (D3) e `scripts/test_release.py` su un repository git temporaneo: tabella valida, tabella vuota, versione malformata, versioni non decrescenti, data non valida, marcatori `recenti` assenti o con più di 3 righe, tag non annotato, tag fuori da `main`, tag diverso dalla prima riga. Verifica: `python scripts/test_release.py` passa.
- [x] 1.2 Aggiungere a `pr.yml` `check_release.py` (senza `--tag`) e `test_release.py`. Verifica: lettura del workflow; i due comandi a zero errori in locale.

## 2. Pagina «Release del sito»

- [x] 2.1 Portare `docs/rapsodia/release.md` al formato `Versione | Data | Novità` senza righe, con i marcatori `recenti` attorno all'intestazione e il testo introduttivo aggiornato (D4, D6). Verifica: `zensical build --strict` senza avvisi; home e pagina mostrano la tabella vuota; `python scripts/check_release.py` a zero errori.
- [x] 2.2 Riscrivere CONTRIBUTING «Release del sito»: numerazione, formato della riga e icone delle aree, procedura (PR `release-X.Y.Z`, merge, tag annotato con il messaggio di D5, push con approvazione), quando proporre una release, controllo `check_release.py`. Verifica: rilettura; l'esempio di riga passa `check_release.py` in un file di prova.

## 3. Pubblicazione ai tag

- [x] 3.1 Modificare `.github/workflows/deploy.yml`: trigger su tag `v*` e avvio manuale, checkout con `fetch-depth: 0`, `check_release.py --tag "$GITHUB_REF_NAME"` prima del build, commento di testa aggiornato (D2). Verifica: `check_release.py --tag` su un tag di prova locale (non pushato) passa con la riga giusta e fallisce senza; YAML valido (`python -c "import yaml; yaml.safe_load(open(...))"`).
- [x] 3.2 Aggiornare la tabella dei workflow nel README (`deploy.yml`: push di un tag `v*`). Verifica: rilettura.

## 4. Design del sito e seed

- [x] 4.1 `rpsd-doc-site-design.md`: voce datata in §0, paragrafo «Release del sito» in §2.3 (D8), piano di implementazione (§9) con le release. Verifica: rilettura.
- [x] 4.2 `openspec/seed.md`: *Automated deployment* (§4.1) e *Site changelog* (§4.6) uguali alle spec modificate, nuova capability `site-releases` nella tabella delle capability e sezione §4.9 con i suoi requisiti, riga 5c `add-site-releases` nel piano dei change. Verifica: rilettura; testo dei requisiti identico alle spec delta.

## 5. Verifica finale

- [x] 5.1 `zensical build --strict` senza avvisi e controlli di `pr.yml` in locale, compresi `check_release.py` e `test_release.py`. Verifica: tutti a zero errori.
- [x] 5.2 Controllo delle pagine costruite: «Release del sito» con la sola intestazione `Versione | Data | Novità`, home con la stessa intestazione nella sezione in fondo (Python-Markdown aggiunge una riga vuota a una tabella senza righe: stato intermedio mai pubblicato, sparisce con la 0.1.0). Verifica: HTML costruito.

## Workflow follow-up

- Commit sul branch `add-site-releases`; push, PR e merge con approvazione di Franco. Dopo il merge il sito pubblicato non cambia.
- `/opsx:archive` su `archive-add-site-releases`, con PR.
- Con approvazione di Franco: regola di deploy `v*` sull'ambiente `github-pages` al posto di `main` (D7).
- PR «Release 0.1.0» (branch `release-0.1.0`) con la riga della release. Bozza delle novità da rivedere con Franco:
  - Sito: piattaforma Zensical con build strict, navigazione a tab, convenzioni dei contenuti controllate in CI, release del sito;
  - Profili: versioni di NeTEx e SIRI per percorso; pagine di NeTEx 5.0.0 e SIRI 1.0.5 (frame e servizi, strutture comuni, enumerazioni, incongruenze);
  - Struttura: tab Rapsodia, Architettura, Modello dati, Dashboard, Contratti; home con schede delle sezioni; glossario nella Guida operativa.
- Con approvazione di Franco: tag annotato `v0.1.0` sul commit di merge e push; verifica della run di Deploy e del sito pubblicato.
