# Proposal — remove-envelope-heading

## Why

La Panoramica di ogni versione di profilo (NeTEx 5.0.0, SIRI 1.0.5) raggruppa le prime tabelle sotto il titolo «Busta», seguito dalla frase «Elementi: `…`». Il termine non è nelle linee guida 5T: viene dal renderer di riferimento di rpsd-tools ed è stato ripreso nel template di rpsd-doc dal change `add-generated-profile-pages`. Le linee guida NeTEx descrivono quelle tabelle in §5.1.2 «Tag comuni» (PublicationDelivery, Tabella 3) e §5.1.3 «Contenuto informativo» (CompositeFrame, Tabella 4); le SIRI in «Tag comuni – ServiceDelivery» di ogni servizio. Il sito non deve introdurre termini che le fonti non usano (CLAUDE.md, «Never invent content»). Decisione di Franco del 19/11/2026: togliere il titolo raggruppante (opzione 2).

## What Changes

- Template della Panoramica (`templates/profili/index.md.j2`): tolti il titolo «Busta» e la frase «Elementi: …». Le tabelle PublicationDelivery, CompositeFrame (NeTEx) e ServiceDelivery (SIRI) restano titoli di secondo livello, con le loro ancore e la riga della fonte («Linee guida §…, Tabella …»).
- Pagine rigenerate: `docs/netex/5.0.0/index.md` e `docs/siri/1.0.5/index.md`. Nessun'altra pagina cambia.
- Il confronto con il Markdown di riferimento di rpsd-tools ammette d'ora in poi questa differenza.

Contenuto **generato** (via template); nessuna pagina redazionale, nessuna modifica all'infrastruttura. Implementa il design del sito §3 (pagine di profilo generate) senza modificarlo.

## Capabilities

### New Capabilities
_Nessuna._

### Modified Capabilities
_Nessuna._ La spec `profile-docs` non nomina il raggruppamento; nessun requisito cambia (`skip_specs: true`).

## Impact

- `templates/profili/index.md.j2`, `docs/netex/5.0.0/index.md`, `docs/siri/1.0.5/index.md`.
- Nessun URL cambia; le ancore `#publicationdelivery`, `#compositeframe`, `#servicedelivery` restano. Sparisce solo l'ancora implicita `#busta` del titolo, mai linkata da altre pagine.

## Out of scope

- Correzione del renderer di riferimento di rpsd-tools: si segnala là come change separata.
- Altri titoli o testi fissi dei template: si rivedono solo se emerge lo stesso problema.
