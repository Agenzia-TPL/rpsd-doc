---
generato: true
generato_da: rpsd-tools 0.8.0
---
<!-- GENERATED — DO NOT EDIT · profile-docs siri-it · siri@v2.2.1 -->

# SIRI-FM (Facility Monitoring)

Stato di parcheggi, stalli di ricarica, bike sharing e sistemi (linee guida §5.5).

## FacilityMonitoringDelivery {#facilitymonitoringdelivery}

Linee guida §5.5.3 «FacilityMonitoringDelivery», Tabella 11. Tipo dell'XSD `FacilityMonitoringDeliveryStructure`.

| Campo | Cardinalità | Tipo | Esempio | Significato (5T) | Fonte |
|---|---|---|---|---|---|
| `ResponseTimestamp` | 1..1 | `xsd:dateTime` | `2023-02-15T10:29:59+01:00` | Data e ora di generazione del file [⚠ Incongruenza](issues.md#11-siri-facilitymonitoringdelivery-siri-responsetimestamp) | §5.5.3, Tab. 11 |
| `SubscriberRef` | 0..1 · scelta 1 | `ParticipantRefStructure` | `NAP` | Identifica il NAP-BIP | §5.5.3, Tab. 11 |
| `SubscriptionRef` | 0..1 · scelta 1 | `SubscriptionRefStructure` | `0001` | Identifica la sottoscrizione | §5.5.3, Tab. 11 |
| [`FacilityCondition`](#facilitycondition) | 0..n | `FacilityConditionStructure` |  |  | §5.5.3.1, Tab. 12 |
| [`FacilityCondition`](#facilitycondition-disponibilita-stalli-di-ricarica-dei-parcheggi) | 0..n | `FacilityConditionStructure` |  |  | §5.5.3.2, Tab. 13 |
| [`FacilityCondition`](#facilitycondition-disponibilita-biciclette-del-bike-sharing-station-based) | 0..n | `FacilityConditionStructure` |  |  | §5.5.3.3, Tab. 14 |
| [`FacilityCondition`](#facilitycondition-disponibilita-biciclette-del-bike-sharing-free-floating) | 0..n | `FacilityConditionStructure` |  |  | §5.5.3.4, Tab. 15 |
| [`FacilityCondition`](#facilitycondition-stato-sistemi-di-bigliettazione) | 0..n | `FacilityConditionStructure` |  |  | §5.5.3.5, Tab. 16 |
| [`FacilityCondition`](#facilitycondition-stato-sistemi-di-bordo-veicolo) | 0..n | `FacilityConditionStructure` |  |  | §5.5.3.6, Tab. 17 |
| [`FacilityCondition`](#facilitycondition-stato-sistemi-di-terra-stazione) | 0..n | `FacilityConditionStructure` |  |  | §5.5.3.7, Tab. 18 |

??? note "Altri campi dell'XSD"

    | Campo | Cardinalità | Tipo |
    |---|---|---|
    | `@version` | 0..1 | `VersionString` |
    | `RequestMessageRef` | 0..1 | `MessageRefStructure` |
    | `SubscriptionFilterRef` | 0..1 | `SubscriptionFilterRefStructure` |
    | `DelegatorAddress` | 0..1 | `EndpointAddress` |
    | `DelegatorRef` | 0..1 | `ParticipantRefStructure` |
    | `Status` | 0..1 | `xsd:boolean` |
    | `ErrorCondition` | 0..1 | `ServiceDeliveryErrorConditionStructure` |
    | `ValidUntil` | 0..1 | `xsd:dateTime` |
    | `ShortestPossibleCycle` | 0..1 | `PositiveDurationType` |
    | `DefaultLanguage` | 0..1 | `xsd:language` |
    | `Extensions` | 0..1 | `ExtensionsStructure` |

### FacilityCondition (§5.5.3.1 FacilityCondition – Stato occupazionale dei parcheggi) {#facilitycondition}

Linee guida §5.5.3.1 «FacilityCondition – Stato occupazionale dei parcheggi», Tabella 12. Tipo dell'XSD `FacilityConditionStructure`.

| Campo | Cardinalità | Tipo | Esempio | Significato (5T) | Fonte |
|---|---|---|---|---|---|
| `FacilityRef` | 0..1 · scelta 1 | `FacilityRefStructure` | `IT:ITC1:Parking:parcheggiTorino:p:Porta_Nuova` | Identificativo del parcheggio. | §5.5.3.1, Tab. 12 |
| `FacilityStatus` | 1..1 | `FacilityStatusStructure` |  |  |  |
| `FacilityStatus / Status` | 1..1 | [`FacilityStatusEnumeration`](enumerations.md#facilitystatusenumeration) | `partiallyAvailable` | Stato del parcheggio Valori del profilo: `available`, `notAvailable`, `partiallyAvailable`, `removed`, `unknown`. [⚠ Incongruenza](issues.md#12-siri-facilitymonitoringdelivery-siri-facilitycondition-siri-facilitystatus-siri-status) | §5.5.3.1, Tab. 12 |
| [`MonitoredCounting`](#facilitycondition-monitoredcounting) | 0..n |  |  |  | §5.5.3.1, Tab. 12 |

??? note "Altri campi dell'XSD"

    | Campo | Cardinalità | Tipo |
    |---|---|---|
    | `Facility` | 0..1 | `FacilityStructure` |
    | `FacilityUpdatedPosition` | 0..1 | `LocationStructure` |
    | `SituationRef` | 0..1 | `SituationRefStructure` |
    | `Remedy` | 0..1 | `RemedyStructure` |
    | `MonitoringInfo` | 0..1 | `MonitoringInformationStructure` |
    | `ValidityPeriod` | 0..1 | `HalfOpenTimestampOutputRangeStructure` |
    | `Extensions` | 0..1 | `ExtensionsStructure` |

#### MonitoredCounting (§5.5.3.1 FacilityCondition – Stato occupazionale dei parcheggi) {#facilitycondition-monitoredcounting}

Linee guida §5.5.3.1 «FacilityCondition – Stato occupazionale dei parcheggi», Tabella 12.

| Campo | Cardinalità | Tipo | Esempio | Significato (5T) | Fonte |
|---|---|---|---|---|---|
| `CountingType` | 1..1 | [`CountingTypeEnumeration`](enumerations.md#countingtypeenumeration) | `presentCount` | Tipologia di conteggio Valori del profilo: `availabilityCount`, `outOfOrderCount`, `presentCount`, `reservedCount`. [⚠ Incongruenza](issues.md#12-siri-facilitymonitoringdelivery-siri-facilitycondition-siri-monitoredcounting-siri-countingtype) | §5.5.3.1, Tab. 12 |
| `CountedFeatureUnit` | 0..1 | [`CountedFeatureUnitEnumeration`](enumerations.md#countedfeatureunitenumeration) | `bays` | Tipologia di stallo contato Valori del profilo: `bays`, `otherSpaces`. | §5.5.3.1, Tab. 12 |
| `Count` | 0..1 · scelta 2 | `xsd:integer` | `10` | Numero di stalli contati | §5.5.3.1, Tab. 12 |
| `Percentage` | 0..1 · scelta 2 | `PercentageType` | `5` | Percentuale di stalli contati | §5.5.3.1, Tab. 12 |

??? note "Altri campi dell'XSD"

    | Campo | Cardinalità | Tipo |
    |---|---|---|
    | `TypeOfCountedFeature` | 0..1 | `TypeOfValueStructure` |
    | `Trend` | 0..1 | [`CountingTrendEnumeration`](enumerations.md#countingtrendenumeration) |
    | `Accuracy` | 0..1 | `PercentageType` |
    | `Description` | 0..n | `NaturalLanguageStringStructure` |
    | `CountedItemsIdList` | 0..1 |  |
    | `Extensions` | 0..1 | `ExtensionsStructure` |

### FacilityCondition (§5.5.3.2 FacilityCondition – Disponibilità stalli di ricarica dei parcheggi) {#facilitycondition-disponibilita-stalli-di-ricarica-dei-parcheggi}

Linee guida §5.5.3.2 «FacilityCondition – Disponibilità stalli di ricarica dei parcheggi», Tabella 13. Tipo dell'XSD `FacilityConditionStructure`.

| Campo | Cardinalità | Tipo | Esempio | Significato (5T) | Fonte |
|---|---|---|---|---|---|
| `FacilityRef` | 0..1 · scelta 1 | `FacilityRefStructure` | `IT:ITC1:Parking:StazioniRicaricaTorino:p:Porta_Nuova` | Identificativo del parcheggio. | §5.5.3.2, Tab. 13 |
| `FacilityStatus` | 1..1 | `FacilityStatusStructure` |  |  |  |
| `FacilityStatus / Status` | 1..1 | [`FacilityStatusEnumeration`](enumerations.md#facilitystatusenumeration) | `partiallyAvailable` | Stato del parcheggio Valori del profilo: `available`, `notAvailable`, `partiallyAvailable`, `removed`, `unknown`. [⚠ Incongruenza](issues.md#12-siri-facilitymonitoringdelivery-siri-facilitycondition-siri-facilitystatus-siri-status) | §5.5.3.2, Tab. 13 |
| [`MonitoredCounting`](#facilitycondition-monitoredcounting-facilitycondition-disponibilita-stalli-di-ricarica-dei-parcheggi) | 0..n |  |  |  | §5.5.3.2, Tab. 13 |

??? note "Altri campi dell'XSD"

    | Campo | Cardinalità | Tipo |
    |---|---|---|
    | `Facility` | 0..1 | `FacilityStructure` |
    | `FacilityUpdatedPosition` | 0..1 | `LocationStructure` |
    | `SituationRef` | 0..1 | `SituationRefStructure` |
    | `Remedy` | 0..1 | `RemedyStructure` |
    | `MonitoringInfo` | 0..1 | `MonitoringInformationStructure` |
    | `ValidityPeriod` | 0..1 | `HalfOpenTimestampOutputRangeStructure` |
    | `Extensions` | 0..1 | `ExtensionsStructure` |

#### MonitoredCounting (§5.5.3.2 FacilityCondition – Disponibilità stalli di ricarica dei parcheggi) {#facilitycondition-monitoredcounting-facilitycondition-disponibilita-stalli-di-ricarica-dei-parcheggi}

Linee guida §5.5.3.2 «FacilityCondition – Disponibilità stalli di ricarica dei parcheggi», Tabella 13.

| Campo | Cardinalità | Tipo | Esempio | Significato (5T) | Fonte |
|---|---|---|---|---|---|
| `CountingType` | 1..1 | [`CountingTypeEnumeration`](enumerations.md#countingtypeenumeration) | `availabilityCount` | Tipologia di conteggio Valori del profilo: `availabilityCount`, `outOfOrderCount`, `presentCount`, `reservedCount`. [⚠ Incongruenza](issues.md#12-siri-facilitymonitoringdelivery-siri-facilitycondition-siri-monitoredcounting-siri-countingtype) | §5.5.3.2, Tab. 13 |
| `CountedFeatureUnit` | 0..1 | [`CountedFeatureUnitEnumeration`](enumerations.md#countedfeatureunitenumeration) | `devices` | Tipologia di stallo contato Valori del profilo: `devices`. | §5.5.3.2, Tab. 13 |
| `Count` | 0..1 · scelta 2 | `xsd:integer` | `15` | Numero di stalli contati | §5.5.3.2, Tab. 13 |
| `Percentage` | 0..1 · scelta 2 | `PercentageType` | `5` | Percentuale di stalli contati | §5.5.3.2, Tab. 13 |

??? note "Altri campi dell'XSD"

    | Campo | Cardinalità | Tipo |
    |---|---|---|
    | `TypeOfCountedFeature` | 0..1 | `TypeOfValueStructure` |
    | `Trend` | 0..1 | [`CountingTrendEnumeration`](enumerations.md#countingtrendenumeration) |
    | `Accuracy` | 0..1 | `PercentageType` |
    | `Description` | 0..n | `NaturalLanguageStringStructure` |
    | `CountedItemsIdList` | 0..1 |  |
    | `Extensions` | 0..1 | `ExtensionsStructure` |

### FacilityCondition (§5.5.3.3 FacilityCondition – Disponibilità biciclette del Bike Sharing (Station Based)) {#facilitycondition-disponibilita-biciclette-del-bike-sharing-station-based}

Linee guida §5.5.3.3 «FacilityCondition – Disponibilità biciclette del Bike Sharing (Station Based)», Tabella 14. Tipo dell'XSD `FacilityConditionStructure`.

| Campo | Cardinalità | Tipo | Esempio | Significato (5T) | Fonte |
|---|---|---|---|---|---|
| `FacilityRef` | 0..1 · scelta 1 | `FacilityRefStructure` | `IT:ITC1:Parking:StazioniRicaricaTorino:p:Porta_Nuova` | Identificativo della stazione | §5.5.3.3, Tab. 14 |
| `FacilityStatus` | 1..1 | `FacilityStatusStructure` |  |  |  |
| `FacilityStatus / Status` | 1..1 | [`FacilityStatusEnumeration`](enumerations.md#facilitystatusenumeration) | `partiallyAvailable` | Stato della stazione Valori del profilo: `available`, `notAvailable`, `partiallyAvailable`, `removed`, `unknown`. [⚠ Incongruenza](issues.md#12-siri-facilitymonitoringdelivery-siri-facilitycondition-siri-facilitystatus-siri-status) | §5.5.3.3, Tab. 14 |
| [`MonitoredCounting`](#facilitycondition-monitoredcounting-facilitycondition-disponibilita-biciclette-del-bike-sharing-station-based) | 0..n |  |  |  | §5.5.3.3, Tab. 14 |

??? note "Altri campi dell'XSD"

    | Campo | Cardinalità | Tipo |
    |---|---|---|
    | `Facility` | 0..1 | `FacilityStructure` |
    | `FacilityUpdatedPosition` | 0..1 | `LocationStructure` |
    | `SituationRef` | 0..1 | `SituationRefStructure` |
    | `Remedy` | 0..1 | `RemedyStructure` |
    | `MonitoringInfo` | 0..1 | `MonitoringInformationStructure` |
    | `ValidityPeriod` | 0..1 | `HalfOpenTimestampOutputRangeStructure` |
    | `Extensions` | 0..1 | `ExtensionsStructure` |

#### MonitoredCounting (§5.5.3.3 FacilityCondition – Disponibilità biciclette del Bike Sharing (Station Based)) {#facilitycondition-monitoredcounting-facilitycondition-disponibilita-biciclette-del-bike-sharing-station-based}

Linee guida §5.5.3.3 «FacilityCondition – Disponibilità biciclette del Bike Sharing (Station Based)», Tabella 14.

| Campo | Cardinalità | Tipo | Esempio | Significato (5T) | Fonte |
|---|---|---|---|---|---|
| `CountingType` | 1..1 | [`CountingTypeEnumeration`](enumerations.md#countingtypeenumeration) | `availabilityCount` | Tipologia di conteggio Valori del profilo: `availabilityCount`, `outOfOrderCount`, `presentCount`, `reservedCount`. [⚠ Incongruenza](issues.md#12-siri-facilitymonitoringdelivery-siri-facilitycondition-siri-monitoredcounting-siri-countingtype) | §5.5.3.3, Tab. 14 |
| `CountedFeatureUnit` | 0..1 | [`CountedFeatureUnitEnumeration`](enumerations.md#countedfeatureunitenumeration) | `otherSpaces` | Tipologia di stallo contato Valori del profilo: `bays`, `devices`, `otherSpaces`. [⚠ Incongruenza](issues.md#14-siri-facilitymonitoringdelivery-siri-facilitycondition-siri-monitoredcounting-siri-countedfeatureunit) | §5.5.3.3, Tab. 14 |
| `Count` | 0..1 · scelta 2 | `xsd:integer` | `15` | Numero di stalli contati | §5.5.3.3, Tab. 14 |
| `Percentage` | 0..1 · scelta 2 | `PercentageType` | `5` | Percentuale di stalli contati | §5.5.3.3, Tab. 14 |

??? note "Altri campi dell'XSD"

    | Campo | Cardinalità | Tipo |
    |---|---|---|
    | `TypeOfCountedFeature` | 0..1 | `TypeOfValueStructure` |
    | `Trend` | 0..1 | [`CountingTrendEnumeration`](enumerations.md#countingtrendenumeration) |
    | `Accuracy` | 0..1 | `PercentageType` |
    | `Description` | 0..n | `NaturalLanguageStringStructure` |
    | `CountedItemsIdList` | 0..1 |  |
    | `Extensions` | 0..1 | `ExtensionsStructure` |

### FacilityCondition (§5.5.3.4 FacilityCondition – Disponibilità biciclette del Bike Sharing (Free Floating)) {#facilitycondition-disponibilita-biciclette-del-bike-sharing-free-floating}

Linee guida §5.5.3.4 «FacilityCondition – Disponibilità biciclette del Bike Sharing (Free Floating)», Tabella 15. Tipo dell'XSD `FacilityConditionStructure`.

| Campo | Cardinalità | Tipo | Esempio | Significato (5T) | Fonte |
|---|---|---|---|---|---|
| `Facility` | 0..1 · scelta 1 | `FacilityStructure` |  |  | §5.5.3.4, Tab. 15 |
| `Facility / FacilityClass` | 0..n | [`FacilityCategoryEnumeration`](enumerations.md#facilitycategoryenumeration) | `vehicle` | Tipologia di mezzo | §5.5.3.4, Tab. 15 |
| `Facility / FacilityLocation` | 0..1 | `FacilityLocationStructure` | `IT:ITC1:Operator:12345678911:BikeSharing:BikeSharing` | Gestore della flotta [⚠ Incongruenza](issues.md#15-siri-facilitymonitoringdelivery-siri-facilitycondition-siri-facility-siri-facilitylocation) | §5.5.3.4, Tab. 15 |
| `Facility / FacilityLocation / VehicleRef` | 0..1 | `VehicleRefStructure` | `IT:ITC1:Vehicle:BikeSharingTorino:VE:01` | Identificativo della bicicletta. | §5.5.3.4, Tab. 15 |
| `Facility / FacilityLocation / OperatorRef` | 0..1 | `OperatorRefStructure` | `IT:ITC1:Operator:12345678911:BikeSharing:BikeSharing` *(SIRI_FM.xml)* |  | §5.5.3.4, Tab. 15 |
| `FacilityStatus` | 1..1 | `FacilityStatusStructure` |  |  |  |
| `FacilityStatus / Status` | 1..1 | [`FacilityStatusEnumeration`](enumerations.md#facilitystatusenumeration) | `available` | Disponibilità della bicicletta Valori del profilo: `available`, `notAvailable`, `partiallyAvailable`, `removed`, `unknown`. [⚠ Incongruenza](issues.md#12-siri-facilitymonitoringdelivery-siri-facilitycondition-siri-facilitystatus-siri-status) | §5.5.3.4, Tab. 15 |
| `FacilityUpdatedPosition` | 0..1 | `LocationStructure` |  |  |  |
| `FacilityUpdatedPosition / Longitude` | 0..1 · scelta 1 | `LongitudeType` | `7.71378` | Longitudine (WGS84) [⚠ Incongruenza](issues.md#15-siri-facilitymonitoringdelivery-siri-facilitycondition-siri-facilityupdatedposition-siri-longitude) | §5.5.3.4, Tab. 15 |
| `FacilityUpdatedPosition / Latitude` | 0..1 · scelta 1 | `LatitudeType` | `45.12401` | Latitudine (WGS84) [⚠ Incongruenza](issues.md#15-siri-facilitymonitoringdelivery-siri-facilitycondition-siri-facilityupdatedposition-siri-latitude) | §5.5.3.4, Tab. 15 |

??? note "Altri campi dell'XSD"

    | Campo | Cardinalità | Tipo |
    |---|---|---|
    | `FacilityRef` | 0..1 | `FacilityRefStructure` |
    | `MonitoredCounting` | 0..n |  |
    | `SituationRef` | 0..1 | `SituationRefStructure` |
    | `Remedy` | 0..1 | `RemedyStructure` |
    | `MonitoringInfo` | 0..1 | `MonitoringInformationStructure` |
    | `ValidityPeriod` | 0..1 | `HalfOpenTimestampOutputRangeStructure` |
    | `Extensions` | 0..1 | `ExtensionsStructure` |

### FacilityCondition (§5.5.3.5 FacilityCondition – Stato sistemi di bigliettazione) {#facilitycondition-stato-sistemi-di-bigliettazione}

Linee guida §5.5.3.5 «FacilityCondition – Stato sistemi di bigliettazione», Tabella 16. Tipo dell'XSD `FacilityConditionStructure`.

| Campo | Cardinalità | Tipo | Esempio | Significato (5T) | Fonte |
|---|---|---|---|---|---|
| `FacilityRef` | 0..1 · scelta 1 | `FacilityRefStructure` | `IT:ITC1:TicketingEquipment:busATS:001` | Identificativo dell’apparato | §5.5.3.5, Tab. 16 |
| `FacilityStatus` | 1..1 | `FacilityStatusStructure` |  |  |  |
| `FacilityStatus / Status` | 1..1 | [`FacilityStatusEnumeration`](enumerations.md#facilitystatusenumeration) | `notAvailable` | Stato dell’apparato Valori del profilo: `available`, `notAvailable`, `partiallyAvailable`, `removed`, `unknown`. [⚠ Incongruenza](issues.md#12-siri-facilitymonitoringdelivery-siri-facilitycondition-siri-facilitystatus-siri-status) | §5.5.3.5, Tab. 16 |
| [`Remedy`](#facilitycondition-remedy) | 0..1 | `RemedyStructure` |  |  | §5.5.3.5, Tab. 16 |

??? note "Altri campi dell'XSD"

    | Campo | Cardinalità | Tipo |
    |---|---|---|
    | `Facility` | 0..1 | `FacilityStructure` |
    | `MonitoredCounting` | 0..n |  |
    | `FacilityUpdatedPosition` | 0..1 | `LocationStructure` |
    | `SituationRef` | 0..1 | `SituationRefStructure` |
    | `MonitoringInfo` | 0..1 | `MonitoringInformationStructure` |
    | `ValidityPeriod` | 0..1 | `HalfOpenTimestampOutputRangeStructure` |
    | `Extensions` | 0..1 | `ExtensionsStructure` |

#### Remedy (§5.5.3.5 FacilityCondition – Stato sistemi di bigliettazione) {#facilitycondition-remedy}

Linee guida §5.5.3.5 «FacilityCondition – Stato sistemi di bigliettazione», Tabella 16. Tipo dell'XSD `RemedyStructure`.

| Campo | Cardinalità | Tipo | Esempio | Significato (5T) | Fonte |
|---|---|---|---|---|---|
| `RemedyType` | 0..1 | [`RemedyTypeEnumeration`](enumerations.md#remedytypeenumeration) | `repair` | Tipologia di intervento manutentivo richiesto | §5.5.3.5, Tab. 16 |
| `Description` | 0..n | `NaturalLanguageStringStructure` | `In manutenzione` | Descrizione testuale dell’intervento manutentivo richiesto | §5.5.3.5, Tab. 16 |
| `RemedyPeriod` | 0..1 | `HalfOpenTimestampInputRangeStructure` |  |  | §5.5.3.5, Tab. 16 |
| `RemedyPeriod / StartTime` | 1..1 | `xsd:dateTime` | `2025-08-12T10:30:00+01:00` | Data/ora di inizio dell’intervento manutentivo | §5.5.3.5, Tab. 16 |
| `RemedyPeriod / EndTime` | 0..1 | `xsd:dateTime` | `2025-08-12T11:30:00+01:00` | Data/ora di fine dell’intervento manutentivo | §5.5.3.5, Tab. 16 |

??? note "Altri campi dell'XSD"

    | Campo | Cardinalità | Tipo |
    |---|---|---|
    | `Extensions` | 0..1 | `ExtensionsStructure` |

### FacilityCondition (§5.5.3.6 FacilityCondition – Stato sistemi di bordo veicolo) {#facilitycondition-stato-sistemi-di-bordo-veicolo}

Linee guida §5.5.3.6 «FacilityCondition – Stato sistemi di bordo veicolo», Tabella 17. Tipo dell'XSD `FacilityConditionStructure`.

| Campo | Cardinalità | Tipo | Esempio | Significato (5T) | Fonte |
|---|---|---|---|---|---|
| `FacilityRef` | 0..1 · scelta 1 | `FacilityRefStructure` | `IT:ITC1:HeadSign:busATS:1` | Identificativo dell’apparato | §5.5.3.6, Tab. 17 |
| `FacilityStatus` | 1..1 | `FacilityStatusStructure` |  |  |  |
| `FacilityStatus / Status` | 1..1 | [`FacilityStatusEnumeration`](enumerations.md#facilitystatusenumeration) | `notAvailable` | Stato dell’apparato Valori del profilo: `available`, `notAvailable`, `partiallyAvailable`, `removed`, `unknown`. [⚠ Incongruenza](issues.md#12-siri-facilitymonitoringdelivery-siri-facilitycondition-siri-facilitystatus-siri-status) | §5.5.3.6, Tab. 17 |
| [`Remedy`](#facilitycondition-remedy-facilitycondition-stato-sistemi-di-bordo-veicolo) | 0..1 | `RemedyStructure` |  |  | §5.5.3.6, Tab. 17 |

??? note "Altri campi dell'XSD"

    | Campo | Cardinalità | Tipo |
    |---|---|---|
    | `Facility` | 0..1 | `FacilityStructure` |
    | `MonitoredCounting` | 0..n |  |
    | `FacilityUpdatedPosition` | 0..1 | `LocationStructure` |
    | `SituationRef` | 0..1 | `SituationRefStructure` |
    | `MonitoringInfo` | 0..1 | `MonitoringInformationStructure` |
    | `ValidityPeriod` | 0..1 | `HalfOpenTimestampOutputRangeStructure` |
    | `Extensions` | 0..1 | `ExtensionsStructure` |

#### Remedy (§5.5.3.6 FacilityCondition – Stato sistemi di bordo veicolo) {#facilitycondition-remedy-facilitycondition-stato-sistemi-di-bordo-veicolo}

Linee guida §5.5.3.6 «FacilityCondition – Stato sistemi di bordo veicolo», Tabella 17. Tipo dell'XSD `RemedyStructure`.

| Campo | Cardinalità | Tipo | Esempio | Significato (5T) | Fonte |
|---|---|---|---|---|---|
| `RemedyType` | 0..1 | [`RemedyTypeEnumeration`](enumerations.md#remedytypeenumeration) | `repair` | Tipologia di intervento manutentivo richiesto | §5.5.3.6, Tab. 17 |
| `Description` | 0..n | `NaturalLanguageStringStructure` | `In manutenzione` | Descrizione testuale dell’intervento manutentivo richiesto | §5.5.3.6, Tab. 17 |
| `RemedyPeriod` | 0..1 | `HalfOpenTimestampInputRangeStructure` |  |  | §5.5.3.6, Tab. 17 |
| `RemedyPeriod / StartTime` | 1..1 | `xsd:dateTime` | `2025-08-12T10:30:00+01:00` | Data/ora di inizio dell’intervento manutentivo | §5.5.3.6, Tab. 17 |
| `RemedyPeriod / EndTime` | 0..1 | `xsd:dateTime` | `2025-08-12T11:30:00+01:00` | Data/ora di fine dell’intervento manutentivo | §5.5.3.6, Tab. 17 |

??? note "Altri campi dell'XSD"

    | Campo | Cardinalità | Tipo |
    |---|---|---|
    | `Extensions` | 0..1 | `ExtensionsStructure` |

### FacilityCondition (§5.5.3.7 FacilityCondition – Stato sistemi di terra - stazione) {#facilitycondition-stato-sistemi-di-terra-stazione}

Linee guida §5.5.3.7 «FacilityCondition – Stato sistemi di terra - stazione», Tabella 18. Tipo dell'XSD `FacilityConditionStructure`.

| Campo | Cardinalità | Tipo | Esempio | Significato (5T) | Fonte |
|---|---|---|---|---|---|
| `FacilityRef` | 0..1 · scelta 1 | `FacilityRefStructure` | `IT:ITC1:EscalatorEquipment:busATS:001` | Identificativo dell’apparato | §5.5.3.7, Tab. 18 |
| `FacilityStatus` | 1..1 | `FacilityStatusStructure` |  |  |  |
| `FacilityStatus / Status` | 1..1 | [`FacilityStatusEnumeration`](enumerations.md#facilitystatusenumeration) | `notAvailable` | Stato dell’apparato Valori del profilo: `available`, `notAvailable`, `partiallyAvailable`, `removed`, `unknown`. [⚠ Incongruenza](issues.md#12-siri-facilitymonitoringdelivery-siri-facilitycondition-siri-facilitystatus-siri-status) | §5.5.3.7, Tab. 18 |
| [`Remedy`](#facilitycondition-remedy-facilitycondition-stato-sistemi-di-terra-stazione) | 0..1 | `RemedyStructure` |  |  | §5.5.3.7, Tab. 18 |

??? note "Altri campi dell'XSD"

    | Campo | Cardinalità | Tipo |
    |---|---|---|
    | `Facility` | 0..1 | `FacilityStructure` |
    | `MonitoredCounting` | 0..n |  |
    | `FacilityUpdatedPosition` | 0..1 | `LocationStructure` |
    | `SituationRef` | 0..1 | `SituationRefStructure` |
    | `MonitoringInfo` | 0..1 | `MonitoringInformationStructure` |
    | `ValidityPeriod` | 0..1 | `HalfOpenTimestampOutputRangeStructure` |
    | `Extensions` | 0..1 | `ExtensionsStructure` |

#### Remedy (§5.5.3.7 FacilityCondition – Stato sistemi di terra - stazione) {#facilitycondition-remedy-facilitycondition-stato-sistemi-di-terra-stazione}

Linee guida §5.5.3.7 «FacilityCondition – Stato sistemi di terra - stazione», Tabella 18. Tipo dell'XSD `RemedyStructure`.

| Campo | Cardinalità | Tipo | Esempio | Significato (5T) | Fonte |
|---|---|---|---|---|---|
| `RemedyType` | 0..1 | [`RemedyTypeEnumeration`](enumerations.md#remedytypeenumeration) | `repair` | Tipologia di intervento manutentivo richiesto | §5.5.3.7, Tab. 18 |
| `Description` | 0..n | `NaturalLanguageStringStructure` | `In manutenzione` | Descrizione testuale dell’intervento manutentivo richiesto | §5.5.3.7, Tab. 18 |
| `RemedyPeriod` | 0..1 | `HalfOpenTimestampInputRangeStructure` |  |  | §5.5.3.7, Tab. 18 |
| `RemedyPeriod / StartTime` | 1..1 | `xsd:dateTime` | `2025-08-12T10:30:00+01:00` | Data/ora di inizio dell’intervento manutentivo | §5.5.3.7, Tab. 18 |
| `RemedyPeriod / EndTime` | 0..1 | `xsd:dateTime` | `2025-08-12T11:30:00+01:00` | Data/ora di fine dell’intervento manutentivo | §5.5.3.7, Tab. 18 |

??? note "Altri campi dell'XSD"

    | Campo | Cardinalità | Tipo |
    |---|---|---|
    | `Extensions` | 0..1 | `ExtensionsStructure` |
