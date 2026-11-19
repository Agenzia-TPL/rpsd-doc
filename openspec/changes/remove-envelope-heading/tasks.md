# Tasks — remove-envelope-heading

Nessun task fa push, apre PR o tocca le impostazioni GitHub senza approvazione di Franco.

## 1. Template e pagine

- [x] 1.1 In `templates/profili/index.md.j2` togliere `## Busta` e la riga `Elementi: …` (D1). Verifica: `grep -rn -i busta templates/` non trova nulla.
- [x] 1.2 Rigenerare con `python scripts/generate_profile_pages.py --all`. Verifica: `git diff --stat` tocca solo `docs/netex/5.0.0/index.md` e `docs/siri/1.0.5/index.md`; `grep -rn -i "busta\|#busta" docs/` non trova nulla (D2).
- [x] 1.3 Annotare in `CONTRIBUTING.md`, sezione «Pagine dei profili NeTEx e SIRI», che le Panoramiche differiscono di proposito dal Markdown di riferimento di rpsd-tools (D3). Verifica: rilettura.

## 2. Verifica finale

- [x] 2.1 `zensical build --strict` senza avvisi e controlli di `pr.yml` in locale (`check_navigation`, `check_conventions`, `check_urls origin/main`, `check_versions --site site`, `generate_profile_pages --all --check`, `test_conventions`, `test_versions`, `test_generate_profile_pages`). Verifica: tutti a zero errori.
- [x] 2.2 Controllo delle Panoramiche rese di NeTEx 5.0.0 e SIRI 1.0.5: nessun «Busta», tabelle PublicationDelivery, CompositeFrame e ServiceDelivery presenti con la riga della fonte, indice a destra coerente. Verifica: HTML costruito.

## Workflow follow-up

- Commit sul branch `remove-envelope-heading`: template e CONTRIBUTING, poi pagine rigenerate con trailer `Generato-da: rpsd-tools 0.6.0` (oppure un unico commit con il trailer).
- Push, PR e merge solo con approvazione di Franco; poi `/opsx:archive`.
