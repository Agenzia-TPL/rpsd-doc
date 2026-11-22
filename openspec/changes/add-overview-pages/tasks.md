# Tasks — add-overview-pages

Nessun task fa push, apre PR o tocca le impostazioni GitHub senza approvazione di Franco.

## 1. Pagine del tab Rapsodia e URL

- [x] 1.1 In `scripts/check_urls.py` escludere gli URL di BASE la cui pagina è un segnaposto (D11); casi aggiunti ai test di *Stable URLs* già presenti in `scripts/test_conventions.py` (eseguito da `pr.yml`, quindi niente `test_urls.py` né modifiche a `pr.yml`): segnaposto tolto (passa), pagina con contenuto tolta (fallisce), pagina di sezione con avviso più tabella tolta (fallisce), più il riconoscimento del segnaposto sul testo. Aggiornare CONTRIBUTING «URL stabili». Verifica: `python scripts/test_conventions.py` e `python scripts/test_versions.py` passano.
- [x] 1.2 Eliminare `docs/rapsodia/progetto.md`; `git mv` di `docs/rapsodia/novita.md` in `docs/rapsodia/release.md` (titolo «Release del sito») e di `docs/rapsodia/glossario.md` in `docs/guida/glossario.md`; aggiornare `docs/.nav.yml` (tab Rapsodia: `index.md`, `rapsodia/release.md`); nessun redirect (D8). Verifica: `python scripts/check_urls.py origin/main` passa e indica i tre URL come segnaposto tolti; nessun redirect nuovo in `mkdocs.yml`.
- [x] 1.3 Aggiornare `scripts/check_navigation.py` (D9: `rapsodia/release/` al posto di `rapsodia/progetto/`). Verifica: `zensical build --strict` e `python scripts/check_navigation.py` a zero errori, glossario nella sidebar di Guida operativa.
- [x] 1.4 Aggiornare il percorso del glossario in `scripts/check_conventions.py`, `scripts/test_conventions.py` e CONTRIBUTING «Glossario e sigle» (D9). Verifica: `python scripts/test_conventions.py` passa; `grep -rn "rapsodia/glossario" scripts CONTRIBUTING.md docs templates` non trova nulla.

## 2. Pagina Release del sito

- [x] 2.1 Scrivere `docs/rapsodia/release.md`: tabella con una riga per change archiviata in `openspec/changes/archive/`, dalla più recente, con data, area e scopo dalla proposal (D6); intestazione e 3 righe più recenti fra i marcatori `recenti` (D7). Aggiungere a CONTRIBUTING come si aggiunge una riga, le aree con le loro icone e come si spostano i marcatori. Verifica: ogni voce corrisponde a una cartella dell'archivio; build strict senza avvisi.

## 3. Home

- [x] 3.1 Riscrivere `docs/index.md`: front matter `hide: [navigation, toc]` (D10), titolo e frase introduttiva (D2), otto schede da Architettura a Contratti (D1, D3) con le versioni dei profili in NeTEx e SIRI (D4), sezione «Release del sito» con l'inclusione `recenti` e il link a `rapsodia/release.md` (D7). Verifica: nessun HTML oltre al `div` delle schede, nessun link a progetto o glossario, `python scripts/check_conventions.py` a zero errori.

- [x] 3.2 Icone nelle schede (D3, D3b): aggiungere `pymdownx.emoji` a `mkdocs.yml`; in ogni scheda icona accanto al titolo e link «Vai alla sezione» in fondo. Verifica: build strict senza avvisi, otto icone SVG nella home costruita, `check_versions` (V8) e `check_conventions` a zero errori.

## 4. Controllo delle versioni in home

- [x] 4.1 Aggiungere la regola V8 a `scripts/check_versions.py` e i casi in `scripts/test_versions.py`: home valida, home con versione non corrente, home senza link alla corrente (D5). Verifica: `python scripts/test_versions.py` passa e `python scripts/check_versions.py` è a zero errori.
- [x] 4.2 In CONTRIBUTING «Profili versionati» aggiungere la home tra i punti da aggiornare al cambio di versione, controllati da V8. Verifica: rilettura.

## 5. Design del sito e seed

- [x] 5.1 Aggiornare `rpsd-doc-site-design.md` (D12): §0 nuova voce datata; §3, §4.2, albero delle cartelle, §8 URL stabili, §9 corretti nel testo; in §4.2 la sezione «Contratti monitorati» della home prevista con il primo contratto generato (proposal, Out of scope). Verifica: `grep -n "progetto.md\|rapsodia/glossario\|novita" rpsd-doc-site-design.md` trova solo la voce di §0.
- [x] 5.2 Aggiornare `openspec/seed.md` (D12): tabella dei change (riga 5), §4.3 *Stable URLs* uguale alla spec modificata, §4.6 `overview` con *Project overview* sulla home e *Latest versions on the home page*, *Glossary* spostato in §4.8 `operational-guide`. Verifica: rilettura; `grep -n "progetto, glossario, novità" openspec/seed.md` non trova nulla.

## 6. Verifica finale

- [x] 6.1 `zensical build --strict` senza avvisi e controlli di `pr.yml` in locale (`check_navigation`, `check_conventions`, `check_urls origin/main`, `check_versions --site site`, `generate_profile_pages --all --check`, `test_conventions`, `test_versions`, `test_generate_profile_pages`). Verifica: tutti a zero errori.
- [x] 6.2 Controllo delle pagine costruite: home senza sidebar né indice, tab Rapsodia attivo, otto schede con link funzionanti, versioni 5.0.0 e 1.0.5, sezione Release del sito uguale alla testa di `rapsodia/release/`; i tre vecchi URL non sono serviti; glossario in Guida operativa; nessun redirect nuovo in `mkdocs.yml`. Verifica: HTML costruito e `zensical serve`.

## Workflow follow-up

- Commit sul branch `add-overview-pages`.
- Push, PR e merge solo con approvazione di Franco.
- Prima di `/opsx:archive`, decidere con Franco se il testo sul progetto (fonti in `sources/`) entra in questa change o in una successiva.
