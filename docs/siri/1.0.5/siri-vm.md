---
generato: true
generato_da: rpsd-tools 0.6.0
---
<!-- GENERATED — DO NOT EDIT · profile-docs siri-it · siri@v2.2.1 -->

# SIRI-VM (Vehicle Monitoring)

Posizione e stato dei veicoli in servizio (linee guida §5.2).

## VehicleMonitoringDelivery {#vehiclemonitoringdelivery}

Linee guida §5.2.3 «VehicleMonitoringDelivery», Tabella 2. Tipo dell'XSD `VehicleMonitoringDeliveryStructure`.

| Campo | Cardinalità | Tipo | Esempio | Significato (5T) | Fonte |
|---|---|---|---|---|---|
| `ResponseTimestamp` | 1..1 | `xsd:dateTime` | `2021-04-13T09:00:00+01:00` | Data e ora di generazione del file [⚠ Incongruenza](issues.md#2-siri-vehiclemonitoringdelivery-siri-responsetimestamp) | §5.2.3, Tab. 2 |
| `SubscriberRef` | 0..1 · scelta 1 | `ParticipantRefStructure` | `NAP` | Identifica il NAP-BIP | §5.2.3, Tab. 2 |
| `SubscriptionRef` | 0..1 · scelta 1 | `SubscriptionRefStructure` | `0001` | Identifica la sottoscrizione | §5.2.3, Tab. 2 |
| [`VehicleActivity`](#vehicleactivity) | 0..n | `VehicleActivityStructure` |  |  |  |

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
    | `VehicleActivityCancellation` | 0..n | `VehicleActivityCancellationStructure` |
    | `VehicleActivityNote` | 0..n | `NaturalLanguageStringStructure` |
    | `Extensions` | 0..1 | `ExtensionsStructure` |

### VehicleActivity {#vehicleactivity}

Linee guida §5.2.3 «VehicleMonitoringDelivery», Tabella 3. Tipo dell'XSD `VehicleActivityStructure`.

| Campo | Cardinalità | Tipo | Esempio | Significato (5T) | Fonte |
|---|---|---|---|---|---|
| `RecordedAtTime` | 1..1 | `xsd:dateTime` | `2023-03-17T08:41:07` | Istante di acquisizione dell’informazione. | §5.2.3, Tab. 3 |
| `ItemIdentifier` | 0..1 | `ItemIdentifierType` | `RAP_Piemonte` | RAP che ha inviato il flusso | §5.2.3, Tab. 3 |
| `ValidUntilTime` | 1..1 | `xsd:dateTime` | `2023-03-17T08:41:07` | Data e ora in cui l’informazione contenuta nel flusso sarà da considerare superata e pertanto non più utilizzabile | §5.2.3, Tab. 3 |
| [`MonitoredVehicleJourney`](#vehicleactivity-monitoredvehiclejourney) | 1..1 |  |  |  | §5.2.3, Tab. 3 |

??? note "Altri campi dell'XSD"

    | Campo | Cardinalità | Tipo |
    |---|---|---|
    | `VehicleMonitoringRef` | 0..1 | `VehicleMonitoringRefStructure` |
    | `MonitoringName` | 0..n | `NaturalLanguageStringStructure` |
    | `ProgressBetweenStops` | 0..1 | `ProgressBetweenStopsStructure` |
    | `VehicleActivityNote` | 0..n | `NaturalLanguageStringStructure` |
    | `Extensions` | 0..1 | `ExtensionsStructure` |

#### MonitoredVehicleJourney {#vehicleactivity-monitoredvehiclejourney}

Linee guida §5.2.3 «VehicleMonitoringDelivery», Tabella 3.

| Campo | Cardinalità | Tipo | Esempio | Significato (5T) | Fonte |
|---|---|---|---|---|---|
| `LineRef` | 0..1 | `LineRefStructure` | `IT:ITC1:Line:busATS:4` | Riferimento alla linea che il mezzo sta esercendo | §5.2.3, Tab. 3 |
| `DirectionRef` | 0..1 | `DirectionRefStructure` | `inbound` | Direzione della corsa Valori del profilo: `inbound`, `outbound`, `clockwise`, `anticlockwise`. | §5.2.3, Tab. 3 |
| [`FramedVehicleJourneyRef`](common.md#framedvehiclejourneyref) | 0..1 | `FramedVehicleJourneyRefStructure` |  |  | §5.2.3, Tab. 3 |
| `JourneyPatternRef` | 0..1 | `JourneyPatternRefStructure` | `IT:ITC1:ServiceJourneyPattern:busATS:4_01A` | Percorso che il mezzo sta esercendo | §5.2.3, Tab. 3 |
| `PublishedLineName` | 0..n | `NaturalLanguageStringStructure` | `4` | Testo che riporta il nome della linea come comunicato all’utenza (ad esempio tramite i pannelli degli autobus) | §5.2.3, Tab. 3 |
| `OperatorRef` | 0..1 | `OperatorRefStructure` | `IT:ITC1:Operator:12345678911:busATS:11` | Riferimento all’azienda a cui appartiene il mezzo in servizio | §5.2.3, Tab. 3 |
| `Monitored` | 0..1 | `xsd:boolean` | `true` | Presenza di AVM sul mezzo che esercisce la corsa modificata | §5.2.3, Tab. 3 |
| `MonitoringError` | 0..1 | `xsd:NMTOKENS` | `AVM` | Apparato che rende il monitoraggio della corsa Monitored=“false” | §5.2.3, Tab. 3 |
| `ConfidenceLevel` | 0..1 | [`QualityIndexEnumeration`](enumerations.md#qualityindexenumeration) | `probablyReliable` | Affidabilità delle previsioni Valori del profilo: `probablyReliable`, `reliable`, `unconfirmed`, `veryReliable`. | §5.2.3, Tab. 3 |
| `VehicleLocation` | 0..1 | `LocationStructure` |  | [⚠ Incongruenza](issues.md#3-siri-vehiclemonitoringdelivery-siri-vehicleactivity-siri-monitoredvehiclejourney-siri-vehiclelocation) | §5.2.3, Tab. 3 |
| `VehicleLocation / Longitude` | 0..1 · scelta 1 | `LongitudeType` | `7.71378` | Longitudine (WGS84) | §5.2.3, Tab. 3 |
| `VehicleLocation / Latitude` | 0..1 · scelta 1 | `LatitudeType` | `45.12401` | Latitudine (WGS84) | §5.2.3, Tab. 3 |
| `VehicleLocation / Precision` | 0..1 | `DistanceType` | `5` | Precisione della localizzazione in metri | §5.2.3, Tab. 3 |
| `Bearing` | 0..1 | `AbsoluteBearingType` | `-115` | Direzione del mezzo in movimento (in gradi decimali) misurato rispetto al nord e riferito alla parte frontale del veicolo | §5.2.3, Tab. 3 |
| `Occupancy` | 0..1 | [`OccupancyEnumeration`](enumerations.md#occupancyenumeration) | `full` | Stato occupazionale del veicolo Valori del profilo: `full`, `seatsAvailable`, `standingAvailable`. | §5.2.3, Tab. 3 |
| `Delay` | 0..1 | `DurationType` | `PT128S` | Ritardo del mezzo (rispetto al servizio programmato); nel caso di anticipo il valore è negativo. [⚠ Incongruenza](issues.md#3-siri-vehiclemonitoringdelivery-siri-vehicleactivity-siri-monitoredvehiclejourney-siri-delay) | §5.2.3, Tab. 3 |
| `VehicleStatus` | 0..1 | [`VehicleStatusEnumeration`](enumerations.md#vehiclestatusenumeration) | `offRoute` | Situazione del servizio svolto dal veicolo | §5.2.3, Tab. 3 |
| `VehicleRef` | 0..1 | `VehicleRefStructure` | `IT:ITC1:Vehicle:busATS:ZZ998ZZ` | Riferimento al veicolo che svolge la corsa | §5.2.3, Tab. 3 |
| [`MonitoredCall`](#vehicleactivity-monitoredvehiclejourney-monitoredcall) | 0..1 | `MonitoredCallStructure` |  | Dedicata a specificare gli orari programmati ed effettivi di arrivo del mezzo in fermata (per la fermata corrente o più recente) | §5.2.3, Tab. 3 |

??? note "Altri campi dell'XSD"

    | Campo | Cardinalità | Tipo |
    |---|---|---|
    | `JourneyPatternName` | 0..1 | `NaturalLanguageStringStructure` |
    | `VehicleMode` | 0..n | [`VehicleModesEnumeration`](enumerations.md#vehiclemodesenumeration) |
    | `RouteRef` | 0..1 | `RouteRefStructure` |
    | `GroupOfLinesRef` | 0..1 | `GroupOfLinesRefStructure` |
    | `DirectionName` | 0..n | `NaturalLanguageStringStructure` |
    | `ExternalLineRef` | 0..1 | `LineRefStructure` |
    | `BrandingRef` | 0..1 | `BrandingRefStructure` |
    | `Branding` | 0..1 | `BrandingStructure` |
    | `ProductCategoryRef` | 0..1 | `ProductCategoryRefStructure` |
    | `ServiceFeatureRef` | 0..n | `ServiceFeatureRefStructure` |
    | `VehicleFeatureRef` | 0..n | `VehicleFeatureRefStructure` |
    | `OriginRef` | 0..1 | `JourneyPlaceRefStructure` |
    | `OriginName` | 0..n | `NaturalLanguagePlaceNameStructure` |
    | `OriginShortName` | 0..n | `NaturalLanguagePlaceNameStructure` |
    | `DestinationDisplayAtOrigin` | 0..n | `NaturalLanguagePlaceNameStructure` |
    | `Via` | 0..n | `ViaNameStructure` |
    | `DestinationRef` | 0..1 | `DestinationRefStructure` |
    | `DestinationName` | 0..n | `NaturalLanguageStringStructure` |
    | `DestinationShortName` | 0..n | `NaturalLanguagePlaceNameStructure` |
    | `OriginDisplayAtDestination` | 0..n | `NaturalLanguagePlaceNameStructure` |
    | `VehicleJourneyName` | 0..n | `NaturalLanguageStringStructure` |
    | `JourneyNote` | 0..n | `NaturalLanguageStringStructure` |
    | `PublicContact` | 0..1 | `SimpleContactStructure` |
    | `OperationsContact` | 0..1 | `SimpleContactStructure` |
    | `HeadwayService` | 0..1 | `xsd:boolean` |
    | `OriginAimedDepartureTime` | 0..1 | `xsd:dateTime` |
    | `DestinationAimedArrivalTime` | 0..1 | `xsd:dateTime` |
    | `FirstOrLastJourney` | 0..1 | [`FirstOrLastJourneyEnumeration`](enumerations.md#firstorlastjourneyenumeration) |
    | `FormationCondition` | 0..n | `FormationConditionStructure` |
    | `FacilityConditionElement` | 0..n | `FacilityConditionStructure` |
    | `FacilityChangeElement` | 0..1 | `FacilityChangeStructure` |
    | `SituationRef` | 0..n | `SituationRefStructure` |
    | `ControlActionRef` | 0..1 | `ControlActionRefStructure` |
    | `InCongestion` | 0..1 | `xsd:boolean` |
    | `InPanic` | 0..1 | `xsd:boolean` |
    | `PredictionInaccurate` | 0..1 | `xsd:boolean` |
    | `PredictionInaccurateReason` | 0..1 | [`PredictionInaccurateReasonEnumeration`](enumerations.md#predictioninaccuratereasonenumeration) |
    | `DataSource` | 0..1 | `xsd:string` |
    | `LocationRecordedAtTime` | 0..1 | `xsd:dateTime` |
    | `ProgressRate` | 0..1 | [`ProgressRateEnumeration`](enumerations.md#progressrateenumeration) |
    | `Velocity` | 0..1 | `VelocityType` |
    | `EngineOn` | 0..1 | `xsd:boolean` |
    | `ProgressStatus` | 0..n | `NaturalLanguageStringStructure` |
    | `TrainBlockPart` | 0..n | `TrainBlockPartStructure` |
    | `BlockRef` | 0..1 | `BlockRefStructure` |
    | `CourseOfJourneyRef` | 0..1 | `CourseOfJourneyRefStructure` |
    | `VehicleJourneyRef` | 0..1 | `VehicleJourneyRefStructure` |
    | `AdditionalVehicleJourneyRef` | 0..n | `FramedVehicleJourneyRefStructure` |
    | `DriverRef` | 0..1 | `xsd:normalizedString` |
    | `DriverName` | 0..1 | `xsd:normalizedString` |
    | `TrainNumbers` | 0..1 |  |
    | `JourneyParts` | 0..1 |  |
    | `TrainElements` | 0..1 |  |
    | `Trains` | 0..1 |  |
    | `CompoundTrains` | 0..1 |  |
    | `PreviousCalls` | 0..1 | `PreviousCallsStructure` |
    | `OnwardCalls` | 0..1 | `OnwardCallsStructure` |
    | `IsCompleteStopSequence` | 0..1 | `xsd:boolean` |

##### MonitoredCall {#vehicleactivity-monitoredvehiclejourney-monitoredcall}

Linee guida §5.2.3 «VehicleMonitoringDelivery», Tabella 3. Tipo dell'XSD `MonitoredCallStructure`.

| Campo | Cardinalità | Tipo | Esempio | Significato (5T) | Fonte |
|---|---|---|---|---|---|
| `StopPointRef` | 0..1 | `StopPointRefStructure` | `IT:ITC1:ScheduledStopPoint:busATS:2` | Riferimento alla fermata più recente | §5.2.3, Tab. 3 |
| `VisitNumber` | 0..1 | `VisitNumberType` | `1` | Disambigua la fermata nel caso il mezzo transiti dalla stessa fermata più volte durante la stessa corsa | §5.2.3, Tab. 3 |
| `Order` | 0..1 | `xsd:positiveInteger` | `2` | Ordinale della fermata nella corsa | §5.2.3, Tab. 3 |
| `StopPointName` | 0..n | `NaturalLanguageStringStructure` | `Castello di Mirafiori` | Testo per descrivere il nome della fermata (come noto all’utenza) | §5.2.3, Tab. 3 |
| `VehicleAtStop` | 0..1 | `xsd:boolean` | `true` | Indica se il mezzo sia o meno in fermata (valorizzato a “true” se il mezzo è in fermata) | §5.2.3, Tab. 3 |
| `AimedDepartureTime` | 0..1 | `xsd:dateTime` | `2023-03-17T08:46:00+01:00` | Orario teorico di partenza dalla fermata – da orario programmato | §5.2.3, Tab. 3 |
| `ActualDepartureTime` | 0..1 · scelta 2 | `xsd:dateTime` | `2023-03-17T08:47:00+01:00` | Orario di partenza effettivo alla fermata | §5.2.3, Tab. 3 |

??? note "Altri campi dell'XSD"

    | Campo | Cardinalità | Tipo |
    |---|---|---|
    | `VehicleLocationAtStop` | 0..1 | `LocationStructure` |
    | `ReversesAtStop` | 0..1 | `xsd:boolean` |
    | `PlatformTraversal` | 0..1 | `xsd:boolean` |
    | `SignalStatus` | 0..1 | `xsd:NMTOKEN` |
    | `TimingPoint` | 0..1 | `xsd:boolean` |
    | `BoardingStretch` | 0..1 | `xsd:boolean` |
    | `RequestStop` | 0..1 | `xsd:boolean` |
    | `OriginDisplay` | 0..n | `NaturalLanguageStringStructure` |
    | `DestinationDisplay` | 0..n | `NaturalLanguageStringStructure` |
    | `CallNote` | 0..n | `NaturalLanguageStringStructure` |
    | `FormationCondition` | 0..n | `FormationConditionStructure` |
    | `FacilityConditionElement` | 0..n | `FacilityConditionStructure` |
    | `FacilityChangeElement` | 0..1 | `FacilityChangeStructure` |
    | `SituationRef` | 0..n | `SituationRefStructure` |
    | `ControlActionRef` | 0..1 | `ControlActionRefStructure` |
    | `AimedArrivalTime` | 0..1 | `xsd:dateTime` |
    | `ActualArrivalTime` | 0..1 | `xsd:dateTime` |
    | `ExpectedArrivalTime` | 0..1 | `xsd:dateTime` |
    | `LatestExpectedArrivalTime` | 0..1 | `xsd:dateTime` |
    | `ArrivalStatus` | 0..1 | [`CallStatusEnumeration`](enumerations.md#callstatusenumeration) |
    | `ArrivalCancellationReason` | 0..1 | `NaturalLanguageStringStructure` |
    | `ArrivalProximityText` | 0..1 | `NaturalLanguageStringStructure` |
    | `ArrivalPlatformName` | 0..1 | `NaturalLanguageStringStructure` |
    | `ArrivalBoardingActivity` | 0..1 | [`ArrivalBoardingActivityEnumeration`](enumerations.md#arrivalboardingactivityenumeration) |
    | `ArrivalStopAssignment` | 0..n | `StopAssignmentStructure` |
    | `ArrivalFormationAssignment` | 0..n | `FormationAssignmentStructure` |
    | `ArrivalOrientationRelativeToQuay` | 0..n | `VehicleOrientationRelativeToQuay` |
    | `ArrivalOperatorRefs` | 0..n | `OperatorRefStructure` |
    | `ExpectedDepartureTime` | 0..1 | `xsd:dateTime` |
    | `ProvisionalExpectedDepartureTime` | 0..1 | `xsd:dateTime` |
    | `EarliestExpectedDepartureTime` | 0..1 | `xsd:dateTime` |
    | `ExpectedDeparturePredictionQuality` | 0..1 | `PredictionQualityStructure` |
    | `AimedLatestPassengerAccessTime` | 0..1 | `xsd:dateTime` |
    | `ExpectedLatestPassengerAccessTime` | 0..1 | `xsd:dateTime` |
    | `DepartureStatus` | 0..1 | [`CallStatusEnumeration`](enumerations.md#callstatusenumeration) |
    | `DepartureCancellationReason` | 0..1 | `NaturalLanguageStringStructure` |
    | `DepartureProximityText` | 0..1 | `NaturalLanguageStringStructure` |
    | `DeparturePlatformName` | 0..1 | `NaturalLanguageStringStructure` |
    | `DepartureBoardingActivity` | 0..1 | [`DepartureBoardingActivityEnumeration`](enumerations.md#departureboardingactivityenumeration) |
    | `DepartureStopAssignment` | 0..n | `StopAssignmentStructure` |
    | `DepartureFormationAssignment` | 0..n | `FormationAssignmentStructure` |
    | `DepartureOrientationRelativeToQuay` | 0..n | `VehicleOrientationRelativeToQuay` |
    | `ExpectedDepartureOccupancy` | 0..n | `VehicleOccupancyStructure` |
    | `ExpectedDepartureCapacities` | 0..n | `PassengerCapacityStructure` |
    | `RecordedDepartureOccupancy` | 0..n | `VehicleOccupancyStructure` |
    | `RecordedDepartureCapacities` | 0..n | `PassengerCapacityStructure` |
    | `DepartureOperatorRefs` | 0..n | `OperatorRefStructure` |
    | `AimedHeadwayInterval` | 0..1 | `PositiveDurationType` |
    | `ExpectedHeadwayInterval` | 0..1 | `PositiveDurationType` |
    | `DistanceFromStop` | 0..1 | `DistanceType` |
    | `NumberOfStopsAway` | 0..1 | `xsd:nonNegativeInteger` |
    | `Extensions` | 0..1 | `ExtensionsStructure` |
