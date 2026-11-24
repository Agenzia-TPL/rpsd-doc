---
generato: true
generato_da: rpsd-tools 0.8.0
---
<!-- GENERATED — DO NOT EDIT · profile-docs siri-it · siri@v2.2.1 -->

# Strutture comuni

Strutture usate in più punti del profilo, raggruppate per argomento. La descrizione unica di ogni campo è ricavata dalle note delle linee guida elencate nella colonna Fonte. Le righe dei frame che usano una struttura rimandano qui e tengono la nota del loro contesto.

## Riferimenti alla corsa

### FramedVehicleJourneyRef {#framedvehiclejourneyref}

Tipo dell'XSD `FramedVehicleJourneyRefStructure`.

| Campo | Cardinalità | Tipo | Esempio | Significato (5T) | Fonte |
|---|---|---|---|---|---|
| `DataFrameRef` | 1..1 | `DataFrameRefStructure` | `2023-03-17` | Data di effettuazione della corsa programmata. | §5.2.3, Tab. 3, §5.3.3, Tab. 6, §5.4.3, Tab. 9 |
| `DatedVehicleJourneyRef` | 1..1 | `DatedVehicleJourneyCodeType` | `IT:ITC1:ServiceJourney:busATS:001_01_01A` | Identificativo della corsa programmata esercita dal veicolo. | §5.2.3, Tab. 3, §5.3.3, Tab. 6 |
