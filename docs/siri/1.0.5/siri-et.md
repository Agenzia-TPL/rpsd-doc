---
generato: true
generato_da: rpsd-tools 0.8.0
---
<!-- GENERATED — DO NOT EDIT · profile-docs siri-it · siri@v2.2.1 -->

# SIRI-ET (Estimated Timetable)

Orari stimati e consuntivati delle corse (linee guida §5.3).

## EstimatedTimetableDelivery {#estimatedtimetabledelivery}

Linee guida §5.3.3 «EstimatedTimetableDelivery», Tabella 5. Tipo dell'XSD `EstimatedTimetableDeliveryStructure`.

| Campo | Cardinalità | Tipo | Esempio | Significato (5T) | Fonte |
|---|---|---|---|---|---|
| `ResponseTimestamp` | 1..1 | `xsd:dateTime` | `2023-02-15T10:26:03+01:00` | Data e ora di generazione del file [⚠ Incongruenza](issues.md#5-siri-estimatedtimetabledelivery-siri-responsetimestamp) | §5.3.3, Tab. 5 |
| `SubscriberRef` | 0..1 · scelta 1 | `ParticipantRefStructure` | `NAP` | Identifica il NAP-BIP | §5.3.3, Tab. 5 |
| `SubscriptionRef` | 0..1 · scelta 1 | `SubscriptionRefStructure` | `0001` | Identifica la sottoscrizione | §5.3.3, Tab. 5 |
| [`EstimatedJourneyVersionFrame`](#estimatedjourneyversionframe) | 1..n | `EstimatedVersionFrameStructure` |  |  |  |

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

### EstimatedJourneyVersionFrame {#estimatedjourneyversionframe}

Linee guida §5.3.3 «EstimatedTimetableDelivery», Tabella 6. Tipo dell'XSD `EstimatedVersionFrameStructure`.

| Campo | Cardinalità | Tipo | Esempio | Significato (5T) | Fonte |
|---|---|---|---|---|---|
| `RecordedAtTime` | 1..1 | `xsd:dateTime` | `2023-02-15T10:29:59+01:00` | Istante di acquisizione dell’informazione. | §5.3.3, Tab. 6 |
| [`EstimatedVehicleJourney`](#estimatedjourneyversionframe-estimatedvehiclejourney) | 1..n | `EstimatedVehicleJourneyStructure` |  |  | §5.3.3, Tab. 6 |

??? note "Altri campi dell'XSD"

    | Campo | Cardinalità | Tipo |
    |---|---|---|
    | `VersionRef` | 0..1 | `VersionCodeType` |
    | `EstimatedServiceJourneyInterchange` | 0..n | `EstimatedServiceJourneyInterchangeStructure` |

#### EstimatedVehicleJourney {#estimatedjourneyversionframe-estimatedvehiclejourney}

Linee guida §5.3.3 «EstimatedTimetableDelivery», Tabella 6. Tipo dell'XSD `EstimatedVehicleJourneyStructure`.

| Campo | Cardinalità | Tipo | Esempio | Significato (5T) | Fonte |
|---|---|---|---|---|---|
| `LineRef` | 1..1 | `LineRefStructure` | `IT:ITC1:Line:busATS:4` | Riferimento alla linea che il mezzo sta esercendo | §5.3.3, Tab. 6 |
| `DirectionRef` | 1..1 | `DirectionRefStructure` | `inbound` | Indica la direzione della corsa Valori del profilo: `inbound`, `outbound`, `clockwise`, `anticlockwise`. | §5.3.3, Tab. 6 |
| [`FramedVehicleJourneyRef`](common.md#framedvehiclejourneyref) | 0..1 · scelta 2 | `FramedVehicleJourneyRefStructure` |  |  | §5.3.3, Tab. 6 |
| `ExtraJourney` | 0..1 · scelta 3 | `xsd:boolean` | `true` | Indica se la corsa è aggiuntiva rispetto al servizio previsto [⚠ Incongruenza](issues.md#6-siri-estimatedtimetabledelivery-siri-estimatedjourneyversionframe-siri-estimatedvehiclejourney-siri-extrajourney) | §5.3.3, Tab. 6 |
| `Cancellation` | 0..1 · scelta 3 | `xsd:boolean` | `false` | Indica se la corsa è stata cancellata | §5.3.3, Tab. 6 |
| `JourneyPatternRef` | 0..1 | `JourneyPatternRefStructure` | `IT:ITC1:ServiceJourneyPattern:busATS:4_01A` | Percorso che il mezzo sta esercendo | §5.3.3, Tab. 6 |
| `PublishedLineName` | 0..n | `NaturalLanguageStringStructure` | `4` | Testo che riporta il nome della linea come comunicato all’utenza (ad esempio tramite i pannelli degli autobus) | §5.3.3, Tab. 6 |
| `OperatorRef` | 0..1 | `OperatorRefStructure` | `IT:ITC1:Operator:12345678911:busATS:11` | Riferimento all’azienda a cui appartiene il mezzo in servizio | §5.3.3, Tab. 6 |
| `JourneyNote` | 0..n | `NaturalLanguageStringStructure` | `Corsa regolare` *(SIRI_ET.xml)* | [⚠ Incongruenza](issues.md#6-siri-estimatedtimetabledelivery-siri-estimatedjourneyversionframe-siri-estimatedvehiclejourney-siri-journeynote) | §5.3.3, Tab. 6 |
| `VehicleRef` | 0..1 | `VehicleRefStructure` | `IT:ITC1:Vehicle:busATS:ZZ998ZZ` | Riferimento al veicolo che svolge la corsa | §5.3.3, Tab. 6 |
| `RecordedCalls` | 0..1 |  |  |  |  |
| [`RecordedCalls / RecordedCall`](#estimatedjourneyversionframe-estimatedvehiclejourney-recordedcalls-recordedcall) | 1..n | `RecordedCallStructure` |  |  | §5.3.3, Tab. 6 |
| `EstimatedCalls` | 0..1 |  |  |  |  |
| [`EstimatedCalls / EstimatedCall`](#estimatedjourneyversionframe-estimatedvehiclejourney-estimatedcalls-estimatedcall) | 1..n | `EstimatedCallStructure` |  | Dedicata a specificare gli orari programmati e stimati di arrivo del mezzo alle prossime fermate (nel caso l’operatore possegga un previsore) [⚠ Incongruenza](issues.md#6-siri-estimatedtimetabledelivery-siri-estimatedjourneyversionframe-siri-estimatedvehiclejourney-siri-estimatedcalls-siri-estimatedcall) | §5.3.3, Tab. 6 |

??? note "Altri campi dell'XSD"

    | Campo | Cardinalità | Tipo |
    |---|---|---|
    | `RecordedAtTime` | 0..1 | `xsd:dateTime` |
    | `DatedVehicleJourneyRef` | 0..1 | `DatedVehicleJourneyRefStructure` |
    | `DatedVehicleJourneyIndirectRef` | 0..1 | `DatedVehicleJourneyIndirectRefStructure` |
    | `EstimatedVehicleJourneyCode` | 0..1 | `EstimatedVehicleJourneyCodeType` |
    | `JourneyPatternName` | 0..1 | `NaturalLanguageStringStructure` |
    | `VehicleMode` | 0..n | [`VehicleModesEnumeration`](enumerations.md#vehiclemodesenumeration) |
    | `RouteRef` | 0..1 | `RouteRefStructure` |
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
    | `ProductCategoryRef` | 0..1 | `ProductCategoryRefStructure` |
    | `ServiceFeatureRef` | 0..n | `ServiceFeatureRefStructure` |
    | `VehicleFeatureRef` | 0..n | `VehicleFeatureRefStructure` |
    | `VehicleJourneyName` | 0..n | `NaturalLanguageStringStructure` |
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
    | `Monitored` | 0..1 | `xsd:boolean` |
    | `MonitoringError` | 0..1 | `xsd:NMTOKENS` |
    | `InCongestion` | 0..1 | `xsd:boolean` |
    | `InPanic` | 0..1 | `xsd:boolean` |
    | `PredictionInaccurate` | 0..1 | `xsd:boolean` |
    | `PredictionInaccurateReason` | 0..1 | [`PredictionInaccurateReasonEnumeration`](enumerations.md#predictioninaccuratereasonenumeration) |
    | `DataSource` | 0..1 | `xsd:string` |
    | `ConfidenceLevel` | 0..1 | [`QualityIndexEnumeration`](enumerations.md#qualityindexenumeration) |
    | `VehicleLocation` | 0..1 | `LocationStructure` |
    | `LocationRecordedAtTime` | 0..1 | `xsd:dateTime` |
    | `Bearing` | 0..1 | `AbsoluteBearingType` |
    | `ProgressRate` | 0..1 | [`ProgressRateEnumeration`](enumerations.md#progressrateenumeration) |
    | `Velocity` | 0..1 | `VelocityType` |
    | `EngineOn` | 0..1 | `xsd:boolean` |
    | `Occupancy` | 0..1 | [`OccupancyEnumeration`](enumerations.md#occupancyenumeration) |
    | `Delay` | 0..1 | `DurationType` |
    | `ProgressStatus` | 0..n | `NaturalLanguageStringStructure` |
    | `VehicleStatus` | 0..1 | [`VehicleStatusEnumeration`](enumerations.md#vehiclestatusenumeration) |
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
    | `IsCompleteStopSequence` | 0..1 | `xsd:boolean` |
    | `JourneyRelations` | 0..1 | `JourneyRelationsStructure` |
    | `Extensions` | 0..1 | `ExtensionsStructure` |

##### RecordedCalls / RecordedCall {#estimatedjourneyversionframe-estimatedvehiclejourney-recordedcalls-recordedcall}

Linee guida §5.3.3 «EstimatedTimetableDelivery», Tabella 6. Tipo dell'XSD `RecordedCallStructure`.

| Campo | Cardinalità | Tipo | Esempio | Significato (5T) | Fonte |
|---|---|---|---|---|---|
| `StopPointRef` | 1..1 | `StopPointRefStructure` | `IT:ITC1:ScheduledStopPoint:busATS:059642` | Riferimento alla fermata più recente | §5.3.3, Tab. 6 |
| `VisitNumber` | 0..1 | `VisitNumberType` | `1` | Disambigua la fermata nel caso il mezzo transiti dalla stessa fermata più volte durante la stessa corsa | §5.3.3, Tab. 6 |
| `Order` | 0..1 | `xsd:positiveInteger` | `1` | Ordinale della fermata nella corsa | §5.3.3, Tab. 6 |
| `StopPointName` | 0..n | `NaturalLanguageStringStructure` | `Drosso Cap.` | Testo per descrivere il nome della fermata (come noto all’utenza) | §5.3.3, Tab. 6 |
| `AimedArrivalTime` | 0..1 | `xsd:dateTime` | `2023-02-15T10:38:58+01:00` | Orario teorico di arrivo alla fermata – da orario programmato | §5.3.3, Tab. 6 |
| `ActualArrivalTime` | 0..1 | `xsd:dateTime` | `2023-02-15T10:32:47+01:00` | Orario di arrivo effettivo alla fermata | §5.3.3, Tab. 6 |
| `AimedDepartureTime` | 0..1 | `xsd:dateTime` | `2023-02-15T10:38:58+01:00` | Orario teorico di partenza dalla fermata – da orario programmato | §5.3.3, Tab. 6 |
| `ActualDepartureTime` | 0..1 | `xsd:dateTime` | `2023-02-15T10:32:47+01:00` | Orario di partenza effettivo alla fermata | §5.3.3, Tab. 6 |
| [`RecordedDepartureOccupancy`](#estimatedjourneyversionframe-estimatedvehiclejourney-recordedcalls-recordedcall-recordeddepartureoccupancy) | 0..n | `VehicleOccupancyStructure` |  | [⚠ Incongruenza](issues.md#6-siri-estimatedtimetabledelivery-siri-estimatedjourneyversionframe-siri-estimatedvehiclejourney-siri-recordedcalls-siri-recordedcall-siri-recordeddepartureoccupancy) | §5.3.3, Tab. 6 |

??? note "Altri campi dell'XSD"

    | Campo | Cardinalità | Tipo |
    |---|---|---|
    | `ExtraCall` | 0..1 | `xsd:boolean` |
    | `Cancellation` | 0..1 | `CallCancellation` |
    | `PredictionInaccurate` | 0..1 | `xsd:boolean` |
    | `PredictionInaccurateReason` | 0..1 | [`PredictionInaccurateReasonEnumeration`](enumerations.md#predictioninaccuratereasonenumeration) |
    | `Occupancy` | 0..1 | [`OccupancyEnumeration`](enumerations.md#occupancyenumeration) |
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
    | `ExpectedArrivalTime` | 0..1 | `xsd:dateTime` |
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
    | `DeparturePlatformName` | 0..1 | `NaturalLanguageStringStructure` |
    | `DepartureStatus` | 0..1 | [`CallStatusEnumeration`](enumerations.md#callstatusenumeration) |
    | `DepartureCancellationReason` | 0..1 | `NaturalLanguageStringStructure` |
    | `DepartureProximityText` | 0..1 | `NaturalLanguageStringStructure` |
    | `DepartureBoardingActivity` | 0..1 | [`DepartureBoardingActivityEnumeration`](enumerations.md#departureboardingactivityenumeration) |
    | `DepartureStopAssignment` | 0..n | `StopAssignmentStructure` |
    | `DepartureFormationAssignment` | 0..n | `FormationAssignmentStructure` |
    | `DepartureOrientationRelativeToQuay` | 0..n | `VehicleOrientationRelativeToQuay` |
    | `RecordedDepartureCapacities` | 0..n | `PassengerCapacityStructure` |
    | `DepartureOperatorRefs` | 0..n | `OperatorRefStructure` |
    | `AimedHeadwayInterval` | 0..1 | `PositiveDurationType` |
    | `ExpectedHeadwayInterval` | 0..1 | `PositiveDurationType` |
    | `ActualHeadwayInterval` | 0..1 | `PositiveDurationType` |
    | `Extensions` | 0..1 | `ExtensionsStructure` |

###### RecordedDepartureOccupancy {#estimatedjourneyversionframe-estimatedvehiclejourney-recordedcalls-recordedcall-recordeddepartureoccupancy}

Linee guida §5.3.3 «EstimatedTimetableDelivery», Tabella 6. Tipo dell'XSD `VehicleOccupancyStructure`.

| Campo | Cardinalità | Tipo | Esempio | Significato (5T) | Fonte |
|---|---|---|---|---|---|
| `OccupancyPercentage` | 0..1 | `PercentageType` | `50` | Percentuale di occupazione del mezzo dopo la partenza dalla fermata indicata | §5.3.3, Tab. 6 |
| `AlightingCount` | 0..1 | `NumberOfPassengers` | `5` | Numero di passeggeri scesi dal mezzo alla fermata | §5.3.3, Tab. 6 |
| `BoardingCount` | 0..1 | `NumberOfPassengers` | `3` | Numero di passeggeri saliti sul mezzo alla fermata | §5.3.3, Tab. 6 |
| `OnboardCount` | 0..1 | `NumberOfPassengers` | `20` | Numero di passeggeri presenti sul mezzo dopo la partenza dalla fermata indicata | §5.3.3, Tab. 6 |
| `PushchairsOnboardCount` | 0..1 | `NumberOfPassengers` | `1` | Numero di sedili estraibili usati sul mezzo dopo la partenza dalla fermata indicata | §5.3.3, Tab. 6 |
| `WheelchairsOnboardCount` | 0..1 | `NumberOfPassengers` | `2` | Numero di posti per carrozzine disabili usati sul mezzo dopo la partenza dalla fermata indicata [⚠ Incongruenza](issues.md#6-siri-estimatedtimetabledelivery-siri-estimatedjourneyversionframe-siri-estimatedvehiclejourney-siri-recordedcalls-siri-recordedcall-siri-recordeddepartureoccupancy-siri-wheelchairsonboardcount) | §5.3.3, Tab. 6 |
| `TotalNumberOfReservedSeats` | 0..1 | `NumberOfPassengers` | `1` | Numero posti riservati usati sul mezzo dopo la partenza dalla fermata indicata | §5.3.3, Tab. 6 |

??? note "Altri campi dell'XSD"

    | Campo | Cardinalità | Tipo |
    |---|---|---|
    | `CompoundTrainRef` | 0..1 | `CompoundTrainRefStructure` |
    | `TrainRef` | 0..1 | `TrainRefStructure` |
    | `TrainInCompoundTrainRef` | 0..1 | `TrainInCompoundTrainRefStructure` |
    | `TrainElementRef` | 0..1 | `TrainElementRefStructure` |
    | `TrainComponentRef` | 0..1 | `TrainComponentRefStructure` |
    | `EntranceToVehicleRef` | 0..1 | `EntranceToVehicleRefStructure` |
    | `FareClass` | 0..1 | [`FareClassEnumeration`](enumerations.md#fareclassenumeration) |
    | `PassengerCategory` | 0..1 | `NaturalLanguageStringStructure` |
    | `OccupancyLevel` | 0..1 | [`OccupancyEnumeration`](enumerations.md#occupancyenumeration) |
    | `SpecialPlacesOccupied` | 0..1 | `NumberOfPassengers` |
    | `PramsOnboardCount` | 0..1 | `xsd:nonNegativeInteger` |
    | `BicycleOnboardCount` | 0..1 | `xsd:nonNegativeInteger` |
    | `GroupReservation` | 0..n | `GroupReservationStructure` |

##### EstimatedCalls / EstimatedCall {#estimatedjourneyversionframe-estimatedvehiclejourney-estimatedcalls-estimatedcall}

Linee guida §5.3.3 «EstimatedTimetableDelivery», Tabella 6. Tipo dell'XSD `EstimatedCallStructure`.

| Campo | Cardinalità | Tipo | Esempio | Significato (5T) | Fonte |
|---|---|---|---|---|---|
| `StopPointRef` | 1..1 | `StopPointRefStructure` | `IT:ITC1:ScheduledStopPoint:busATS:3` | Riferimento alla fermata alla prossima che verrà raggiunta dal mezzo | §5.3.3, Tab. 6 (occorrenza 2) |
| `VisitNumber` | 0..1 | `VisitNumberType` | `1` | Disambigua la fermata nel caso il mezzo transiti dalla stessa fermata più volte durante la stessa corsa | §5.3.3, Tab. 6 (occorrenza 2) |
| `Order` | 0..1 | `xsd:positiveInteger` | `3` | Ordinale della fermata nella corsa | §5.3.3, Tab. 6 (occorrenza 2) |
| `StopPointName` | 0..n | `NaturalLanguageStringStructure` | `Plava` | Testo per descrivere il nome della fermata (come noto all’utenza) | §5.3.3, Tab. 6 (occorrenza 2) |
| `AimedArrivalTime` | 0..1 | `xsd:dateTime` | `2023-03-17T08:55:00+01:00` | Orario teorico di arrivo alla fermata – da orario programmato | §5.3.3, Tab. 6 (occorrenza 2) |
| `ExpectedArrivalTime` | 0..1 · scelta 2 | `xsd:dateTime` | `2023-03-17T08:56:00+01:00` | Orario di arrivo stimato alla fermata | §5.3.3, Tab. 6 |
| `AimedDepartureTime` | 0..1 | `xsd:dateTime` | `2023-03-17T08:55:00+01:00` | Orario teorico di partenza dalla fermata – da orario programmato [⚠ Incongruenza](issues.md#6-siri-estimatedtimetabledelivery-siri-estimatedjourneyversionframe-siri-estimatedvehiclejourney-siri-estimatedcalls-siri-estimatedcall-siri-aimeddeparturetime) | §5.3.3, Tab. 6 |
| `ExpectedDepartureTime` | 0..1 · scelta 3 | `xsd:dateTime` | `2023-03-17T08:56:00+01:00` | Orario stimato di partenza dalla fermata | §5.3.3, Tab. 6 |

??? note "Altri campi dell'XSD"

    | Campo | Cardinalità | Tipo |
    |---|---|---|
    | `ExtraCall` | 0..1 | `xsd:boolean` |
    | `Cancellation` | 0..1 | `CallCancellation` |
    | `PredictionInaccurate` | 0..1 | `xsd:boolean` |
    | `PredictionInaccurateReason` | 0..1 | [`PredictionInaccurateReasonEnumeration`](enumerations.md#predictioninaccuratereasonenumeration) |
    | `Occupancy` | 0..1 | [`OccupancyEnumeration`](enumerations.md#occupancyenumeration) |
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
    | `LatestExpectedArrivalTime` | 0..1 | `xsd:dateTime` |
    | `ExpectedArrivalPredictionQuality` | 0..1 | `PredictionQualityStructure` |
    | `ArrivalPredictionUnknown` | 0..1 | [`EmptyType`](enumerations.md#emptytype) |
    | `ArrivalStatus` | 0..1 | [`CallStatusEnumeration`](enumerations.md#callstatusenumeration) |
    | `ArrivalCancellationReason` | 0..1 | `NaturalLanguageStringStructure` |
    | `ArrivalProximityText` | 0..1 | `NaturalLanguageStringStructure` |
    | `ArrivalPlatformName` | 0..1 | `NaturalLanguageStringStructure` |
    | `ArrivalBoardingActivity` | 0..1 | [`ArrivalBoardingActivityEnumeration`](enumerations.md#arrivalboardingactivityenumeration) |
    | `ArrivalStopAssignment` | 0..n | `StopAssignmentStructure` |
    | `ArrivalFormationAssignment` | 0..n | `FormationAssignmentStructure` |
    | `ArrivalOrientationRelativeToQuay` | 0..n | `VehicleOrientationRelativeToQuay` |
    | `ArrivalOperatorRefs` | 0..n | `OperatorRefStructure` |
    | `ProvisionalExpectedDepartureTime` | 0..1 | `xsd:dateTime` |
    | `EarliestExpectedDepartureTime` | 0..1 | `xsd:dateTime` |
    | `ExpectedDeparturePredictionQuality` | 0..1 | `PredictionQualityStructure` |
    | `DeparturePredictionUnknown` | 0..1 | [`EmptyType`](enumerations.md#emptytype) |
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
