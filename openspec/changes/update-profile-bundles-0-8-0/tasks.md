# Tasks — update-profile-bundles-0-8-0

Nessun task fa push, apre PR o tocca le impostazioni GitHub senza l'approvazione di Franco. Si lavora sul branch `update-profile-bundles-0-8-0`.

## 1. Generazione dei bundle da rpsd-tools v0.8.0

- [x] 1.1 Creare un worktree di `../rpsd-tools` sul tag `v0.8.0` nello scratchpad ed eseguire `uv sync --all-packages` (D1). Verifica: `git -C <worktree> describe --tags` dà `v0.8.0`, e il checkout principale di rpsd-tools resta su `main` pulito.
- [x] 1.2 Generare NeTEx (`profiles/netex-it`) e SIRI (`profiles/siri-it`) due volte, in due cartelle di output distinte (D2). Verifica: `cmp` sui due `site.yaml` di ciascun profilo non trova differenze, `generator` è `rpsd-tools 0.8.0` e le dimensioni sono 1 039 126 e 263 491 byte.
- [x] 1.3 Confrontare i bundle generati con quelli di `data/profili/`. Verifica: le righe diverse sono 70 per il NeTEx (`generator` e l'ordine dei riferimenti alle attrezzature dopo `EquipmentRef`) e 2 per il SIRI (solo `generator`). Se c'è altro, fermarsi e chiedere a Franco.

## 2. Bundle e pagine

- [x] 2.1 Copiare i due `site.yaml` in `data/profili/netex/5.0.0/` e `data/profili/siri/1.0.5/`, poi rigenerare con `python scripts/generate_profile_pages.py --all`. Verifica: `--all --check` passa.
- [x] 2.2 Controllare il diff delle pagine (D3). Verifica: `git diff` tocca solo `docs/netex/5.0.0/` e `docs/siri/1.0.5/`; fuori da `resource-frame.md` cambia solo `generato_da`; in `resource-frame.md` le righe ordinate di prima e dopo differiscono solo per `generato_da`; `grep -rn "rpsd-tools 0.6.0" docs data` non trova nulla.
- [x] 2.3 Fare il commit di bundle e pagine con il trailer `Generato-da: rpsd-tools 0.8.0`, senza attribuzioni AI (D5). Verifica: `python scripts/check_conventions.py --commits origin/main` passa.

## 3. Pulizia dei brief

- [x] 3.1 Rimuovere `openspec/brief-pagine-profilo-da-rpsd-tools.md` e farne il commit insieme agli artefatti della change, senza trailer, perché non tocca percorsi generati. Verifica: `git ls-files openspec/brief-*` non lo elenca più.
- [x] 3.2 Rimuovere il worktree di rpsd-tools (`git -C ../rpsd-tools worktree remove …`). Verifica: `git -C ../rpsd-tools worktree list` mostra solo il checkout principale.

## 4. Verifica finale

- [x] 4.1 Eseguire `zensical build --strict` e, in locale, i controlli di `pr.yml`: `check_conventions --commits origin/main`, `check_urls origin/main`, `check_versions --site site`, `check_navigation`, `check_release`, `generate_profile_pages --all --check` e i test degli script. Verifica: nessun avviso e zero errori.
- [x] 4.2 Controllare le pagine rese `netex/5.0.0/resource-frame/` e un campione di pagine SIRI 1.0.5 nell'HTML costruito. Verifica: la tabella del ResourceFrame ha le stesse righe in ordine alfabetico dopo `EquipmentRef`, e ancore e indice a destra sono invariati.

## Workflow follow-up

- Push, PR e merge solo con l'approvazione di Franco.
- Dopo il merge: rimuovere `openspec/brief-aggiorna-bundle-profili-0.8.0.md` (oggi non tracciato) e fare `/opsx:archive`.
- Release del sito: Franco decide se fare subito una 0.1.1 o aspettare la prossima release (design D4).
