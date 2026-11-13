# XML annotato

!!! warning "Pagina di prova — contenuto non normativo"

    Frammento solo strutturale, senza campi né vincoli del profilo italiano.

Scenario: *Annotated NeTEx fragment*.

``` xml
<PublicationDelivery version="1.0"> <!-- (1)! -->
  <PublicationTimestamp>2026-01-01T00:00:00</PublicationTimestamp> <!-- (2)! -->
  <dataObjects> <!-- (3)! -->
    <GeneralFrame id="prova:GeneralFrame:1" version="1"/>
  </dataObjects>
</PublicationDelivery>
```

1.  Prima annotazione: elemento radice del documento di prova.
2.  Seconda annotazione: marca temporale di prova.
3.  Terza annotazione: contenitore dei frame.

## Da verificare

- il codice XML è evidenziato
- ciascuno dei tre marcatori si apre e mostra la propria spiegazione
- il testo copiato con il pulsante di copia non contiene marcatori né commenti `<!-- (n)! -->`
