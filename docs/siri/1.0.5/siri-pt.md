---
generato: true
generato_da: rpsd-tools 0.8.0
---
<!-- GENERATED — DO NOT EDIT · profile-docs siri-it · siri@v2.2.1 -->

# SIRI-PT (Production Timetable)

Programmato del giorno operativo (linee guida §5.6).

## ProductionTimetableDelivery {#productiontimetabledelivery}

Linee guida §5.6.3 «ProductionTimetableDelivery», Tabella 20. Tipo dell'XSD `ProductionTimetableDeliveryStructure`.

| Campo | Cardinalità | Tipo | Esempio | Significato (5T) | Fonte |
|---|---|---|---|---|---|
| `ResponseTimestamp` | 1..1 | `xsd:dateTime` | `2021-04-13T09:00:00+01:00` | Data e ora di generazione del file [⚠ Incongruenza](issues.md#20-siri-productiontimetabledelivery-siri-responsetimestamp) | §5.6.3, Tab. 20 |
| `SubscriberRef` | 0..1 · scelta 1 | `ParticipantRefStructure` | `NAP` | Identifica il NAP-BIP | §5.6.3, Tab. 20 |
| `SubscriptionRef` | 0..1 · scelta 1 | `SubscriptionRefStructure` | `0001` | Identifica la sottoscrizione | §5.6.3, Tab. 20 |
| `ValidUntil` | 0..1 | `xsd:dateTime` | `2023-02-15T09:00:00+01:00` | Data e ora di fine validità della programmazione alterata | §5.6.3, Tab. 20 |
| [`DatedTimetableVersionFrame`](#datedtimetableversionframe) | 0..n | `DatedTimetableVersionFrameStructure` |  |  |  |

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
    | `ShortestPossibleCycle` | 0..1 | `PositiveDurationType` |
    | `DefaultLanguage` | 0..1 | `xsd:language` |
    | `Extensions` | 0..1 | `ExtensionsStructure` |

### DatedTimetableVersionFrame {#datedtimetableversionframe}

Linee guida §5.6.3 «ProductionTimetableDelivery», Tabella 21. Tipo dell'XSD `DatedTimetableVersionFrameStructure`.

| Campo | Cardinalità | Tipo | Esempio | Significato (5T) | Fonte |
|---|---|---|---|---|---|
| `RecordedAtTime` | 1..1 | `xsd:dateTime` | `2023-03-17T08:41:07` | Istante di generazione della corsa modificata. | §5.6.3, Tab. 21 |
| `LineRef` | 1..1 | `LineRefStructure` | `IT:ITC1:Line:busATS:4` | Riferimento alla linea a cui appartiene la corsa modificata | §5.6.3, Tab. 21 |
| `DirectionRef` | 1..1 | `DirectionRefStructure` | `inbound` | Direzione della corsa modificata Valori del profilo: `inbound`, `outbound`, `clockwise`, `anticlockwise`. | §5.6.3, Tab. 21 |
| `JourneyPatternRef` | 0..1 | `JourneyPatternRefStructure` | `IT:ITC1:ServiceJourneyPattern:busATS:4_01A` | Percorso della corsa modificata | §5.6.3, Tab. 21 |
| `VehicleMode` | 0..n | [`VehicleModesEnumeration`](enumerations.md#vehiclemodesenumeration) | `bus` | Tipo veicolo che esercisce la corsa modificata | §5.6.3, Tab. 21 |
| `PublishedLineName` | 0..n | `NaturalLanguageStringStructure` | `4` | Testo che riporta il nome della linea come comunicato all’utenza (ad esempio tramite i pannelli degli autobus) | §5.6.3, Tab. 21 |
| `OperatorRef` | 0..1 | `OperatorRefStructure` | `IT:ITC1:Operator:12345678911:busATS:11` | Riferimento all’azienda che esercisce la corsa modificata | §5.6.3, Tab. 21 |
| [`DatedVehicleJourney`](#datedtimetableversionframe-datedvehiclejourney) | 0..n | `DatedVehicleJourneyStructure` |  |  | §5.6.3, Tab. 21 |

??? note "Altri campi dell'XSD"

    | Campo | Cardinalità | Tipo |
    |---|---|---|
    | `VersionRef` | 0..1 | `VersionRefStructure` |
    | `ValidityPeriod` | 0..1 | `TimetableValidityPeriod` |
    | `ShortestPossibleCycle` | 0..1 | `PositiveDurationType` |
    | `JourneyPatternName` | 0..1 | `NaturalLanguageStringStructure` |
    | `RouteRef` | 0..1 | `RouteRefStructure` |
    | `GroupOfLinesRef` | 0..1 | `GroupOfLinesRefStructure` |
    | `DirectionName` | 0..n | `NaturalLanguageStringStructure` |
    | `ExternalLineRef` | 0..1 | `LineRefStructure` |
    | `BrandingRef` | 0..1 | `BrandingRefStructure` |
    | `Branding` | 0..1 | `BrandingStructure` |
    | `ProductCategoryRef` | 0..1 | `ProductCategoryRefStructure` |
    | `ServiceFeatureRef` | 0..n | `ServiceFeatureRefStructure` |
    | `VehicleFeatureRef` | 0..n | `VehicleFeatureRefStructure` |
    | `OriginDisplay` | 0..n | `NaturalLanguageStringStructure` |
    | `DestinationDisplay` | 0..n | `NaturalLanguageStringStructure` |
    | `LineNote` | 0..n | `NaturalLanguagePlaceNameStructure` |
    | `FirstOrLastJourney` | 0..1 | [`FirstOrLastJourneyEnumeration`](enumerations.md#firstorlastjourneyenumeration) |
    | `HeadwayService` | 0..1 | `xsd:boolean` |
    | `Monitored` | 0..1 | `xsd:boolean` |
    | `RemovedDatedVehicleJourney` | 0..n | `RemovedDatedVehicleJourneyStructure` |
    | `ServiceJourneyInterchange` | 0..n | `ServiceJourneyInterchangeStructure` |
    | `RemovedServiceJourneyInterchange` | 0..n | `RemovedServiceJourneyInterchangeStructure` |
    | `Extensions` | 0..1 | `ExtensionsStructure` |

#### DatedVehicleJourney {#datedtimetableversionframe-datedvehiclejourney}

Linee guida §5.6.3 «ProductionTimetableDelivery», Tabella 21. Tipo dell'XSD `DatedVehicleJourneyStructure`.

| Campo | Cardinalità | Tipo | Esempio | Significato (5T) | Fonte |
|---|---|---|---|---|---|
| [`FramedVehicleJourneyRef`](common.md#framedvehiclejourneyref) | 0..1 · scelta 1 | `FramedVehicleJourneyRefStructure` | `IT:ITC1:ServiceJourney:busATS:001_01_01A` | Identificativo della corsa programmata che viene modificata [⚠ Incongruenza](issues.md#21-siri-productiontimetabledelivery-siri-datedtimetableversionframe-siri-datedvehiclejourney-siri-framedvehiclejourneyref) | §5.6.3, Tab. 21 |
| `JourneyNote` | 0..n | `NaturalLanguageStringStructure` | `Corsa deviata con capolinea modificato` | Descrizione della modifica del servizio e le eventuali cause | §5.6.3, Tab. 21 |
| `Monitored` | 0..1 | `xsd:boolean` | `true` | Presenza di AVM sul mezzo che esercisce la corsa modificata | §5.6.3, Tab. 21 |
| `VehicleRef` | 0..1 | `VehicleRefStructure` | `IT:ITC1:Vehicle:busATS:ZZ998ZZ` | Riferimento al veicolo che svolge la corsa modificata | §5.6.3, Tab. 21 |
| `DatedCalls` | 1..1 |  |  |  |  |
| [`DatedCalls / DatedCall`](#datedtimetableversionframe-datedvehiclejourney-datedcalls-datedcall) | 2..n | `DatedCallStructure` |  | Dedicata a specificare gli orari programmati della corsa modificata | §5.6.3, Tab. 21 |

??? note "Altri campi dell'XSD"

    | Campo | Cardinalità | Tipo |
    |---|---|---|
    | `DatedVehicleJourneyCode` | 0..1 | `DatedVehicleJourneyCodeType` |
    | `VehicleJourneyRef` | 0..1 | `VehicleJourneyRefStructure` |
    | `ExtraJourney` | 0..1 | `xsd:boolean` |
    | `Cancellation` | 0..1 | `xsd:boolean` |
    | `JourneyPatternRef` | 0..1 | `JourneyPatternRefStructure` |
    | `JourneyPatternName` | 0..1 | `NaturalLanguageStringStructure` |
    | `VehicleMode` | 0..n | [`VehicleModesEnumeration`](enumerations.md#vehiclemodesenumeration) |
    | `RouteRef` | 0..1 | `RouteRefStructure` |
    | `PublishedLineName` | 0..n | `NaturalLanguageStringStructure` |
    | `GroupOfLinesRef` | 0..1 | `GroupOfLinesRefStructure` |
    | `DirectionName` | 0..n | `NaturalLanguageStringStructure` |
    | `ExternalLineRef` | 0..1 | `LineRefStructure` |
    | `BrandingRef` | 0..1 | `BrandingRefStructure` |
    | `Branding` | 0..1 | `BrandingStructure` |
    | `OriginRef` | 0..1 | `JourneyPlaceRefStructure` |
    | `OriginName` | 0..n | `NaturalLanguagePlaceNameStructure` |
    | `OriginShortName` | 0..n | `NaturalLanguagePlaceNameStructure` |
    | `DestinationDisplayAtOrigin` | 0..n | `NaturalLanguagePlaceNameStructure` |
    | `Via` | 0..n | `ViaNameStructure` |
    | `DestinationRef` | 0..1 | `DestinationRefStructure` |
    | `DestinationName` | 0..n | `NaturalLanguageStringStructure` |
    | `DestinationShortName` | 0..n | `NaturalLanguagePlaceNameStructure` |
    | `OriginDisplayAtDestination` | 0..n | `NaturalLanguagePlaceNameStructure` |
    | `OperatorRef` | 0..1 | `OperatorRefStructure` |
    | `ProductCategoryRef` | 0..1 | `ProductCategoryRefStructure` |
    | `ServiceFeatureRef` | 0..n | `ServiceFeatureRefStructure` |
    | `VehicleFeatureRef` | 0..n | `VehicleFeatureRefStructure` |
    | `VehicleJourneyName` | 0..n | `NaturalLanguageStringStructure` |
    | `PublicContact` | 0..1 | `SimpleContactStructure` |
    | `OperationsContact` | 0..1 | `SimpleContactStructure` |
    | `OriginDisplay` | 0..n | `NaturalLanguageStringStructure` |
    | `DestinationDisplay` | 0..n | `NaturalLanguageStringStructure` |
    | `LineNote` | 0..n | `NaturalLanguagePlaceNameStructure` |
    | `FirstOrLastJourney` | 0..1 | [`FirstOrLastJourneyEnumeration`](enumerations.md#firstorlastjourneyenumeration) |
    | `HeadwayService` | 0..1 | `xsd:boolean` |
    | `TrainBlockPart` | 0..n | `TrainBlockPartStructure` |
    | `BlockRef` | 0..1 | `BlockRefStructure` |
    | `CourseOfJourneyRef` | 0..1 | `CourseOfJourneyRefStructure` |
    | `TrainNumbers` | 0..1 |  |
    | `JourneyParts` | 0..1 |  |
    | `TrainElements` | 0..1 |  |
    | `Trains` | 0..1 |  |
    | `CompoundTrains` | 0..1 |  |
    | `JourneyRelations` | 0..1 | `JourneyRelationsStructure` |
    | `Extensions` | 0..1 | `ExtensionsStructure` |

##### DatedCalls / DatedCall {#datedtimetableversionframe-datedvehiclejourney-datedcalls-datedcall}

Linee guida §5.6.3 «ProductionTimetableDelivery», Tabella 21. Tipo dell'XSD `DatedCallStructure`.

| Campo | Cardinalità | Tipo | Esempio | Significato (5T) | Fonte |
|---|---|---|---|---|---|
| `StopPointRef` | 1..1 | `StopPointRefStructure` | `IT:ITC1:ScheduledStopPoint:busATS:059642` | Riferimento alla fermata di transito della corsa modificata | §5.6.3, Tab. 21 |
| `VisitNumber` | 0..1 | `VisitNumberType` | `1` | Disambigua la fermata nel caso il mezzo transiti dalla stessa fermata più volte durante la stessa corsa | §5.6.3, Tab. 21 |
| `Order` | 0..1 | `xsd:positiveInteger` | `1` | Ordinale della fermata nella corsa | §5.6.3, Tab. 21 |
| `StopPointName` | 0..n | `NaturalLanguageStringStructure` | `Drosso Cap.` | Testo per descrivere il nome della fermata (come noto all’utenza) | §5.6.3, Tab. 21 |
| `ExtraCall` | 0..1 · scelta 1 | `xsd:boolean` | `false` | Indica se la fermata sia aggiuntiva rispetto a quelle previste nella pianificazione NeTEx [⚠ Incongruenza](issues.md#21-siri-productiontimetabledelivery-siri-datedtimetableversionframe-siri-datedvehiclejourney-siri-datedcalls-siri-datedcall-siri-extracall) | §5.6.3, Tab. 21 |
| `Cancellation` | 0..1 · scelta 1 | `xsd:boolean` | `false` | Indica se la fermata fosse presente nella pianificazione NeTEx e sia stata soppressa (o sostituita da altra fermata) – In alternativa a ExtraCall | §5.6.3, Tab. 21 |
| `AimedArrivalTime` | 0..1 | `xsd:dateTime` | `2023-02-15T10:39:58+01:00` | Orario teorico di arrivo alla fermata – da orario programmato modificato | §5.6.3, Tab. 21 |
| `ArrivalBoardingActivity` | 0..1 | [`ArrivalBoardingActivityEnumeration`](enumerations.md#arrivalboardingactivityenumeration) | `boarding` | Indica se la fermata (in fase di arrivo) sia di salita, discesa o transito Valori del profilo: `alighting`, `noAlighting`, `passThru`. [⚠ Incongruenza](issues.md#21-siri-productiontimetabledelivery-siri-datedtimetableversionframe-siri-datedvehiclejourney-siri-datedcalls-siri-datedcall-siri-arrivalboardingactivity) | §5.6.3, Tab. 21 |
| `AimedDepartureTime` | 0..1 | `xsd:dateTime` | `2023-02-15T10:38:58+01:00` | Orario teorico di partenza dalla fermata – da orario programmato modificato | §5.6.3, Tab. 21 |
| `DepartureBoardingActivity` | 0..1 | [`DepartureBoardingActivityEnumeration`](enumerations.md#departureboardingactivityenumeration) | `boarding` | Indica se la fermata (in fase di partenza) sia di salita, discesa o transito | §5.6.3, Tab. 21 |

??? note "Altri campi dell'XSD"

    | Campo | Cardinalità | Tipo |
    |---|---|---|
    | `TimingPoint` | 0..1 | `xsd:boolean` |
    | `BoardingStretch` | 0..1 | `xsd:boolean` |
    | `RequestStop` | 0..1 | `xsd:boolean` |
    | `OriginDisplay` | 0..n | `NaturalLanguageStringStructure` |
    | `DestinationDisplay` | 0..n | `NaturalLanguageStringStructure` |
    | `CallNote` | 0..n | `NaturalLanguageStringStructure` |
    | `ArrivalPlatformName` | 0..1 | `NaturalLanguageStringStructure` |
    | `ArrivalStopAssignment` | 0..n | `PlannedStopAssignmentStructure` |
    | `ArrivalFormationAssignment` | 0..n | `FormationAssignmentStructure` |
    | `ArrivalOperatorRefs` | 0..n | `OperatorRefStructure` |
    | `DeparturePlatformName` | 0..1 | `NaturalLanguageStringStructure` |
    | `DepartureStopAssignment` | 0..n | `PlannedStopAssignmentStructure` |
    | `DepartureFormationAssignment` | 0..n | `FormationAssignmentStructure` |
    | `DepartureOperatorRefs` | 0..n | `OperatorRefStructure` |
    | `AimedLatestPassengerAccessTime` | 0..1 | `xsd:dateTime` |
    | `AimedHeadwayInterval` | 0..1 | `PositiveDurationType` |
    | `TargetedInterchange` | 0..n | `TargetedInterchangeStructure` |
    | `FromServiceJourneyInterchange` | 0..n | `FromServiceJourneyInterchangeStructure` |
    | `ToServiceJourneyInterchange` | 0..n | `ToServiceJourneyInterchangeStructure` |
    | `Extensions` | 0..1 | `ExtensionsStructure` |
