# Diagrammi

!!! warning "Pagina di prova — contenuto non normativo"

Scenario: *Flow diagram*.

## Flowchart

``` mermaid
flowchart LR
  A[Sorgente] --> B[Elaborazione]
  B --> C{Controllo}
  C -->|esito positivo| D[Pubblicazione]
  C -->|esito negativo| E[Segnalazione]
```

## Sequence diagram

``` mermaid
sequenceDiagram
  participant P as Produttore
  participant S as Sistema
  P->>S: invio
  S-->>P: ricevuta
  S->>S: elaborazione
  S-->>P: esito
```

## Da verificare

- entrambi i diagrammi sono resi come grafica nello schema chiaro
- entrambi i diagrammi sono resi come grafica e leggibili nello schema scuro
