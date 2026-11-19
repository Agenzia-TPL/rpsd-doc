# Design — remove-envelope-heading

## Context

Motivazione: `proposal.md`. `templates/profili/index.md.j2` scrive, dopo l'elenco delle pagine, `## Busta`, una riga `Elementi: <roots>.` e le tabelle di `page.tables` (livello 2 nel bundle). Il titolo viene dal renderer di rpsd-tools (`render.py`, `overview`), non dal bundle.

## Goals / Non-Goals

**Goals:** nessun termine estraneo alle linee guida nella Panoramica; tabelle e ancore invariate.

**Non-Goals:** cambiare il bundle o rpsd-tools; aggiungere testo nuovo al posto del titolo.

## Decisions

- **D1 — Togliere titolo e frase, non sostituirli.** Le tabelle sono già titoli di secondo livello, allo stesso livello di «Pagine del profilo», e ognuna dice la sezione e la tabella delle linee guida da cui viene. Alternativa scartata: usare il titolo del §5.1 («Lo schema NeTEx_publication.xsd»), che richiederebbe un dato per profilo assente dal bundle o un testo fisso per profilo nel template.
- **D2 — Ancora `#busta`.** Sparisce. `grep` su `docs/` e `templates/` non trova link verso di essa; `check_urls` controlla gli URL di pagina, non le ancore, e passa.
- **D3 — Differenza voluta dal riferimento di rpsd-tools.** Il confronto `diff -r` di `add-generated-profile-pages` D5 accetta d'ora in poi questa differenza nelle due Panoramiche; si annota in `CONTRIBUTING.md`.
- **D4 — Versioni non correnti.** Oggi c'è una sola versione per profilo, corrente: nessun trailer `Errata:` necessario.

## Risks / Trade-offs

- Il Markdown di riferimento di rpsd-tools e le pagine del sito divergono finché rpsd-tools non toglie lo stesso titolo → differenza documentata, segnalata a rpsd-tools.
