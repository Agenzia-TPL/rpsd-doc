---
generato: true
generato_da: rpsd-tools 0.6.0
---
<!-- GENERATED — DO NOT EDIT · profile-docs siri-it · siri@v2.2.1 -->

# Profilo italiano SIRI

- Linee guida 1.0.5: «Linee guida compilazione SIRI IT v.1.0.5.docx»
    - Linee guida compilazione SIRI IT v.1.0.5.docx (versione 1.0.5, provided)
    - Linee guida compilazione SIRI IT.pdf (versione 2.0.0, published)
- XSD: `siri@v2.2.1`
- Note del profilo riviste da Franco il 2026-11-11

La cardinalità è quella dell'XSD: l'obbligatorietà non fa parte del profilo (linee guida, §2.2.4). Il significato è quello dato dalle linee guida; i campi dell'XSD che le linee guida non citano sono nel riquadro chiuso sotto ogni tabella.

## Pagine del profilo

- [SIRI-VM (Vehicle Monitoring)](siri-vm.md): Posizione e stato dei veicoli in servizio (linee guida §5.2).
- [SIRI-ET (Estimated Timetable)](siri-et.md): Orari stimati e consuntivati delle corse (linee guida §5.3).
- [SIRI-SX (Situation Exchange)](siri-sx.md): Avvisi e perturbazioni del servizio (linee guida §5.4).
- [SIRI-FM (Facility Monitoring)](siri-fm.md): Stato di parcheggi, stalli di ricarica, bike sharing e sistemi (linee guida §5.5).
- [SIRI-PT (Production Timetable)](siri-pt.md): Programmato del giorno operativo (linee guida §5.6).
- [Strutture comuni](common.md)
- [Enumerazioni](enumerations.md)
- [Incongruenze](issues.md)

## ServiceDelivery {#servicedelivery}

Linee guida §5.2.2 «Tag comuni – ServiceDelivery», Tabella 1.

| Campo | Cardinalità | Tipo | Esempio | Significato (5T) | Fonte |
|---|---|---|---|---|---|
| `ResponseTimestamp` | 1..1 | `xsd:dateTime` | `2023-02-15T10:26:03.010Z` | Data e ora di generazione del file [⚠ Incongruenza](issues.md#1-siri-servicedelivery-siri-responsetimestamp) | §5.2.2, Tab. 1, §5.3.2, Tab. 4, §5.4.2, Tab. 7, §5.5.2, Tab. 10, §5.6.2, Tab. 19 |
| `ProducerRef` | 0..1 | `ParticipantRefStructure` | `RAP_Piemonte` | Identifica il RAP che ha trasmesso il file | §5.2.2, Tab. 1, §5.3.2, Tab. 4, §5.4.2, Tab. 7, §5.5.2, Tab. 10, §5.6.2, Tab. 19 |
| `ResponseMessageIdentifier` | 0..1 | `MessageQualifierStructure` | `1` | Descrive il contenuto del file | §5.2.2, Tab. 1, §5.3.2, Tab. 4, §5.4.2, Tab. 7, §5.5.2, Tab. 10, §5.6.2, Tab. 19 |

??? note "Altri campi dell'XSD"

    | Campo | Cardinalità | Tipo |
    |---|---|---|
    | `@srsName` | 0..1 | `SrsNameType` |
    | `Address` | 0..1 | `EndpointAddress` |
    | `RequestMessageRef` | 0..1 | `MessageRefStructure` |
    | `DelegatorAddress` | 0..1 | `EndpointAddress` |
    | `DelegatorRef` | 0..1 | `ParticipantRefStructure` |
    | `Status` | 0..1 | `xsd:boolean` |
    | `ErrorCondition` | 0..1 |  |
    | `MoreData` | 0..1 | `xsd:boolean` |
    | `IncludedSituationExchangeDelivery` | 0..n | `SituationExchangeDeliveryStructure` |
    | `ProductionTimetableDelivery` | 0..n | `ProductionTimetableDeliveryStructure` |
    | `EstimatedTimetableDelivery` | 0..n | `EstimatedTimetableDeliveryStructure` |
    | `StopTimetableDelivery` | 0..n | `StopTimetableDeliveryStructure` |
    | `StopMonitoringDelivery` | 0..n | `StopMonitoringDeliveryStructure` |
    | `VehicleMonitoringDelivery` | 0..n | `VehicleMonitoringDeliveryStructure` |
    | `ConnectionTimetableDelivery` | 0..n | `ConnectionTimetableDeliveryStructure` |
    | `ConnectionMonitoringFeederDelivery` | 0..n | `ConnectionMonitoringFeederDeliveryStructure` |
    | `ConnectionMonitoringDistributorDelivery` | 0..n | `ConnectionMonitoringDistributorDeliveryStructure` |
    | `GeneralMessageDelivery` | 0..n | `GeneralMessageDeliveryStructure` |
    | `FacilityMonitoringDelivery` | 0..n | `FacilityMonitoringDeliveryStructure` |
    | `SituationExchangeDelivery` | 0..n | `SituationExchangeDeliveryStructure` |
