---
generato: true
generato_da: rpsd-tools 0.8.0
---
<!-- GENERATED — DO NOT EDIT · profile-docs siri-it · siri@v2.2.1 -->

# SIRI-SX (Situation Exchange)

Avvisi e perturbazioni del servizio (linee guida §5.4).

## SituationExchangeDelivery {#situationexchangedelivery}

Linee guida §5.4.3 «SituationExchangeDelivery», Tabella 8. Tipo dell'XSD `SituationExchangeDeliveryStructure`.

| Campo | Cardinalità | Tipo | Esempio | Significato (5T) | Fonte |
|---|---|---|---|---|---|
| `ResponseTimestamp` | 1..1 | `xsd:dateTime` | `2023-02-15T10:29:59+01:00` | Data e ora di generazione del file [⚠ Incongruenza](issues.md#8-siri-situationexchangedelivery-siri-responsetimestamp) | §5.4.3, Tab. 8 |
| `SubscriberRef` | 0..1 · scelta 1 | `ParticipantRefStructure` | `NAP` | Identifica il NAP-BIP | §5.4.3, Tab. 8 |
| `SubscriptionRef` | 0..1 · scelta 1 | `SubscriptionRefStructure` | `0001` | Identifica la sottoscrizione | §5.4.3, Tab. 8 |
| `Situations` | 0..1 |  |  |  |  |
| [`Situations / PtSituationElement`](#situations-ptsituationelement) | 0..n | `PtSituationElementStructure` |  |  | §5.4.3, Tab. 9 |

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
    | `PtSituationContext` | 0..1 | `ContextStructure` |
    | `Extensions` | 0..1 | `ExtensionsStructure` |

### Situations / PtSituationElement {#situations-ptsituationelement}

Linee guida §5.4.3 «SituationExchangeDelivery», Tabella 9. Tipo dell'XSD `PtSituationElementStructure`.

| Campo | Cardinalità | Tipo | Esempio | Significato (5T) | Fonte |
|---|---|---|---|---|---|
| `CreationTime` | 1..1 | `xsd:dateTime` | `2023-02-15T10:33:11+01:00` | Istante di creazione dell’informazione. | §5.4.3, Tab. 9 |
| `CountryRef` | 0..1 | [`ifopt:CountryRefStructure`](enumerations.md#ifopt-countryrefstructure) | `it` | Sigla della lingua dei dati trasmessi [⚠ Incongruenza](issues.md#9-siri-situationexchangedelivery-siri-situations-siri-ptsituationelement-siri-countryref) | §5.4.3, Tab. 9 |
| `ParticipantRef` | 0..1 | `ParticipantRefStructure` | `RAP` | Identificativo del RAP mittente | §5.4.3, Tab. 9 |
| `SituationNumber` | 1..1 | `EntryQualifierStructure` | `1` | Identificativo dell’evento | §5.4.3, Tab. 9 |
| `Source` | 1..1 | `SituationSourceStructure` |  |  | §5.4.3, Tab. 9 |
| `Source / Country` | 0..1 | [`ifopt:CountryRefStructure`](enumerations.md#ifopt-countryrefstructure) | `it` | Sigla della nazione di appartenenza del mittente dei dati | §5.4.3, Tab. 9 |
| `Source / SourceType` | 1..1 | [`SituationSourceTypeEnumeration`](enumerations.md#situationsourcetypeenumeration) | `other` | Natura della segnalazione | §5.4.3, Tab. 9 |
| `Source / AgentReference` | 0..1 | `xsd:string` | `GTT` | Identifica l’azienda che ha fornito del dato [⚠ Incongruenza](issues.md#9-siri-situationexchangedelivery-siri-situations-siri-ptsituationelement-siri-source-siri-agentreference) | §5.4.3, Tab. 9 |
| `Progress` | 0..1 | [`WorkflowStatusEnumeration`](enumerations.md#workflowstatusenumeration) | `open` | Indica lo stato dell’evento Valori del profilo: `closed`, `closing`, `draft`, `open`, `pendingApproval`, `published`. | §5.4.3, Tab. 9 |
| [`ValidityPeriod`](#situations-ptsituationelement-validityperiod) | 1..n | `HalfOpenTimestampOutputRangeStructure` |  |  | §5.4.3, Tab. 9 |
| `AlertCause` | 0..1 · scelta 1 | [`AlertCauseEnumeration`](enumerations.md#alertcauseenumeration) | `closedForMaintenance` | Causa sintetica dell’evento Valori del profilo: `unknown`, `miscellaneous`, `technicalProblem`, `march`, `demonstration`, `accident`, `holiday`, `poorWeather`, `closedForMaintenance`, `constructionWork`, `policeActivity`. [⚠ Incongruenza](issues.md#9-siri-situationexchangedelivery-siri-situations-siri-ptsituationelement-siri-alertcause) | §5.4.3, Tab. 9 |
| `Summary` | 0..n | `DefaultedTextStructure` | `Linea 4 limitata` | Descrizione sintetica dell’evento | §5.4.3, Tab. 9 |
| `Description` | 0..n | `DefaultedTextStructure` | `Il 15 Febbraio 2023 dalle 10.00 fino al 16 febbraio alle 10:00 la linea 4 sarà soggetta manutenzione` | Descrizione estesa dell’evento | §5.4.3, Tab. 9 |
| [`Affects`](#situations-ptsituationelement-affects-networks-affectednetwork) | 0..1 | `AffectsScopeStructure` |  |  | §5.4.3, Tab. 9 |
| `Affects / Operators` | 0..1 |  |  |  |  |
| [`Affects / Operators / AffectedOperator`](#situations-ptsituationelement-affects-operators-affectedoperator) | 0..n · scelta 1 | `AffectedOperatorStructure` |  |  | §5.4.3, Tab. 9 |
| `Affects / StopPoints` | 0..1 |  |  |  |  |
| [`Affects / StopPoints / AffectedStopPoint`](#situations-ptsituationelement-affects-stoppoints-affectedstoppoint) | 1..n | `AffectedStopPointStructure` |  |  | §5.4.3, Tab. 9 |
| `Affects / VehicleJourneys` | 0..1 |  |  |  |  |
| [`Affects / VehicleJourneys / AffectedVehicleJourney`](#situations-ptsituationelement-affects-vehiclejourneys-affectedvehiclejourney) | 1..n | `AffectedVehicleJourneyStructure` |  |  | §5.4.3, Tab. 9 |
| `Consequences` | 0..1 | `PtConsequencesStructure` |  |  |  |
| [`Consequences / Consequence`](#situations-ptsituationelement-consequences-consequence) | 1..n | `PtConsequenceStructure` |  |  | §5.4.3, Tab. 9 |

??? note "Altri campi dell'XSD"

    | Campo | Cardinalità | Tipo |
    |---|---|---|
    | `UpdateCountryRef` | 0..1 | [`ifopt:CountryRefStructure`](enumerations.md#ifopt-countryrefstructure) |
    | `UpdateParticipantRef` | 0..1 | `ParticipantRefStructure` |
    | `Version` | 0..1 | `SituationVersion` |
    | `References` | 0..1 | `ReferencesStructure` |
    | `VersionedAtTime` | 0..1 | `xsd:dateTime` |
    | `Verification` | 0..1 |  |
    | `QualityIndex` | 0..1 | [`QualityIndexEnumeration`](enumerations.md#qualityindexenumeration) |
    | `Reality` | 0..1 | [`D2LogicalModel:InformationStatusEnum`](enumerations.md#d2logicalmodel-informationstatusenum) |
    | `Likelihood` | 0..1 | [`D2LogicalModel:ProbabilityOfOccurrenceEnum`](enumerations.md#d2logicalmodel-probabilityofoccurrenceenum) |
    | `Publication` | 0..n | `PublicationStatusType` |
    | `Repetitions` | 0..1 |  |
    | `PublicationWindow` | 0..n | `HalfOpenTimestampOutputRangeStructure` |
    | `UnknownReason` | 0..1 | `xsd:string` |
    | `MiscellaneousReason` | 0..1 | `xsd:NMTOKEN` |
    | `PersonnelReason` | 0..1 | `xsd:NMTOKEN` |
    | `EquipmentReason` | 0..1 | `xsd:NMTOKEN` |
    | `EnvironmentReason` | 0..1 | `xsd:NMTOKEN` |
    | `UndefinedReason` | 0..1 | `xsd:string` |
    | `MiscellaneousSubReason` | 0..1 | `xsd:NMTOKEN` |
    | `PersonnelSubReason` | 0..1 | `xsd:NMTOKEN` |
    | `EquipmentSubReason` | 0..1 | `xsd:NMTOKEN` |
    | `EnvironmentSubReason` | 0..1 | `xsd:NMTOKEN` |
    | `PublicEventReason` | 0..1 | [`D2LogicalModel:PublicEventTypeEnum`](enumerations.md#d2logicalmodel-publiceventtypeenum) |
    | `ReasonName` | 0..n | `NaturalLanguageStringStructure` |
    | `ControlActionRef` | 0..1 | `ControlActionRefStructure` |
    | `Severity` | 0..1 | [`SeverityEnumeration`](enumerations.md#severityenumeration) |
    | `Priority` | 0..1 | `xsd:nonNegativeInteger` |
    | `Sensitivity` | 0..1 | [`SensitivityEnumeration`](enumerations.md#sensitivityenumeration) |
    | `Audience` | 0..1 | [`AudienceEnumeration`](enumerations.md#audienceenumeration) |
    | `ScopeType` | 0..1 |  |
    | `ReportType` | 0..1 | [`ReportTypeEnumeration`](enumerations.md#reporttypeenumeration) |
    | `Planned` | 0..1 | `xsd:boolean` |
    | `Keywords` | 0..1 | `xsd:NMTOKENS` |
    | `SecondaryReasons` | 0..1 |  |
    | `Language` | 0..1 | `xsd:language` |
    | `Detail` | 0..n | `DefaultedTextStructure` |
    | `Advice` | 0..n | `DefaultedTextStructure` |
    | `Internal` | 0..1 | `DefaultedTextStructure` |
    | `Images` | 0..1 |  |
    | `InfoLinks` | 0..1 |  |
    | `PublishingActions` | 0..1 | `ActionsStructure` |
    | `Extensions` | 0..1 | `ExtensionsStructure` |

#### ValidityPeriod {#situations-ptsituationelement-validityperiod}

Linee guida §5.4.3 «SituationExchangeDelivery», Tabella 9. Tipo dell'XSD `HalfOpenTimestampOutputRangeStructure`.

| Campo | Cardinalità | Tipo | Esempio | Significato (5T) | Fonte |
|---|---|---|---|---|---|
| `StartTime` | 1..1 | `xsd:dateTime` | `2023-02-15T10:00:00+01:00` | Istante di creazione dell’informazione. [⚠ Incongruenza](issues.md#9-siri-situationexchangedelivery-siri-situations-siri-ptsituationelement-siri-validityperiod-siri-starttime) | §5.4.3, Tab. 9 |
| `EndTime` | 0..1 | `xsd:dateTime` | `2023-02-16T10:00:00+01:00` | Istante di creazione dell’informazione. [⚠ Incongruenza](issues.md#9-siri-situationexchangedelivery-siri-situations-siri-ptsituationelement-siri-validityperiod-siri-endtime) | §5.4.3, Tab. 9 |

??? note "Altri campi dell'XSD"

    | Campo | Cardinalità | Tipo |
    |---|---|---|
    | `EndTimeStatus` | 0..1 | [`EndTimeStatusEnumeration`](enumerations.md#endtimestatusenumeration) |

#### Affects / Operators / AffectedOperator {#situations-ptsituationelement-affects-operators-affectedoperator}

Linee guida §5.4.3 «SituationExchangeDelivery», Tabella 9. Tipo dell'XSD `AffectedOperatorStructure`.

| Campo | Cardinalità | Tipo | Esempio | Significato (5T) | Fonte |
|---|---|---|---|---|---|
| `OperatorRef` | 0..1 | `OperatorRefStructure` | `IT:ITC1:Operator:12345678911:busATS:11` | Identificativo dell’azienda TPL su cui ha effetto l’evento | §5.4.3, Tab. 9 |
| `OperatorName` | 0..n | `NaturalLanguageStringStructure` | `BusATS` | Nome dell’azienda TPL | §5.4.3, Tab. 9 |

??? note "Altri campi dell'XSD"

    | Campo | Cardinalità | Tipo |
    |---|---|---|
    | `OperatorShortName` | 0..n | `NaturalLanguageStringStructure` |
    | `OperationalUnitRef` | 0..n | `OperationalUnitRefStructure` |
    | `Extensions` | 0..1 | `ExtensionsStructure` |

#### Affects / Networks / AffectedNetwork {#situations-ptsituationelement-affects-networks-affectednetwork}

Linee guida §5.4.3 «SituationExchangeDelivery», Tabella 9.

| Campo | Cardinalità | Tipo | Esempio | Significato (5T) | Fonte |
|---|---|---|---|---|---|
| [`AffectedLine`](#situations-ptsituationelement-affects-networks-affectednetwork-affectedline) | 0..n · scelta 3 | `AffectedLineStructure` |  |  | §5.4.3, Tab. 9 |

??? note "Altri campi dell'XSD"

    | Campo | Cardinalità | Tipo |
    |---|---|---|
    | `AffectedOperator` | 0..n | `AffectedOperatorStructure` |
    | `NetworkRef` | 0..1 | `NetworkRefStructure` |
    | `NetworkName` | 0..n | `NaturalLanguageStringStructure` |
    | `RoutesAffected` | 0..n | `NaturalLanguageStringStructure` |
    | `VehicleMode` | 0..1 | [`VehicleModesOfTransportEnumeration`](enumerations.md#vehiclemodesoftransportenumeration) |
    | `AirSubmode` | 0..1 | [`AirSubmodesOfTransportEnumeration`](enumerations.md#airsubmodesoftransportenumeration) |
    | `BusSubmode` | 0..1 | [`BusSubmodesOfTransportEnumeration`](enumerations.md#bussubmodesoftransportenumeration) |
    | `CoachSubmode` | 0..1 | [`CoachSubmodesOfTransportEnumeration`](enumerations.md#coachsubmodesoftransportenumeration) |
    | `MetroSubmode` | 0..1 | [`MetroSubmodesOfTransportEnumeration`](enumerations.md#metrosubmodesoftransportenumeration) |
    | `RailSubmode` | 0..1 | [`RailSubmodesOfTransportEnumeration`](enumerations.md#railsubmodesoftransportenumeration) |
    | `TramSubmode` | 0..1 | [`TramSubmodesOfTransportEnumeration`](enumerations.md#tramsubmodesoftransportenumeration) |
    | `WaterSubmode` | 0..1 | [`WaterSubmodesOfTransportEnumeration`](enumerations.md#watersubmodesoftransportenumeration) |
    | `TelecabinSubmode` | 0..1 | [`TelecabinSubmodesOfTransportEnumeration`](enumerations.md#telecabinsubmodesoftransportenumeration) |
    | `AccessMode` | 0..1 | [`ifopt:AccessModesEnumeration`](enumerations.md#ifopt-accessmodesenumeration) |
    | `AllLines` | 0..1 | [`EmptyType`](enumerations.md#emptytype) |
    | `SelectedRoutes` | 0..n | `AffectedRouteStructure` |
    | `AffectedSection` | 0..n | `AffectedSectionStructure` |
    | `Extensions` | 0..1 | `ExtensionsStructure` |

##### AffectedLine {#situations-ptsituationelement-affects-networks-affectednetwork-affectedline}

Linee guida §5.4.3 «SituationExchangeDelivery», Tabella 9. Tipo dell'XSD `AffectedLineStructure`.

| Campo | Cardinalità | Tipo | Esempio | Significato (5T) | Fonte |
|---|---|---|---|---|---|
| `LineRef` | 1..1 | `LineRefStructure` | `IT:ITC1:Line:busATS:4` | Identificativo della linea TPL su cui ha effetto l’evento | §5.4.3, Tab. 9 |

??? note "Altri campi dell'XSD"

    | Campo | Cardinalità | Tipo |
    |---|---|---|
    | `AffectedOperator` | 0..n | `AffectedOperatorStructure` |
    | `PublishedLineName` | 0..n | `NaturalLanguageStringStructure` |
    | `Origins` | 0..n | `AffectedStopPointStructure` |
    | `Destinations` | 0..n | `AffectedStopPointStructure` |
    | `Direction` | 0..n | `DirectionStructure` |
    | `Routes` | 0..1 |  |
    | `Sections` | 0..1 |  |
    | `StopPoints` | 0..1 |  |
    | `StopPlaces` | 0..1 |  |
    | `Extensions` | 0..1 | `ExtensionsStructure` |

#### Affects / StopPoints / AffectedStopPoint {#situations-ptsituationelement-affects-stoppoints-affectedstoppoint}

Linee guida §5.4.3 «SituationExchangeDelivery», Tabella 9. Tipo dell'XSD `AffectedStopPointStructure`.

| Campo | Cardinalità | Tipo | Esempio | Significato (5T) | Fonte |
|---|---|---|---|---|---|
| `StopPointRef` | 0..1 | `StopPointRefStructure` | `IT:ITC1:ScheduledStopPoint:busATS:059642` | Identificativo della fermata su cui ha effetto l’evento | §5.4.3, Tab. 9 |
| `StopPointName` | 0..n | `NaturalLanguageStringStructure` | `Drosso Cap.` | Nome della fermata su cui ha effetto l’evento | §5.4.3, Tab. 9 |
| `Location` | 0..1 | `LocationStructure` |  |  | §5.4.3, Tab. 9 |
| `Location / Longitude` | 0..1 · scelta 1 | `LongitudeType` | `7.71378` | Longitudine (WGS84) | §5.4.3, Tab. 9 |
| `Location / Latitude` | 0..1 · scelta 1 | `LatitudeType` | `45.12401` | Latitudine (WGS84) | §5.4.3, Tab. 9 |

??? note "Altri campi dell'XSD"

    | Campo | Cardinalità | Tipo |
    |---|---|---|
    | `PrivateRef` | 0..1 | `xsd:string` |
    | `StopPointType` | 0..1 | [`StopPointTypeEnumeration`](enumerations.md#stoppointtypeenumeration) |
    | `StopPlaceRef` | 0..1 | `ifopt:StopPlaceRefStructure` |
    | `StopPlaceName` | 0..n | `NaturalLanguageStringStructure` |
    | `AffectedModes` | 0..1 | `AffectedModesStructure` |
    | `PlaceRef` | 0..1 | `ZoneRefStructure` |
    | `PlaceName` | 0..n | `NaturalLanguageStringStructure` |
    | `AccessibilityAssessment` | 0..1 | `acsb:AccessibilityAssessmentStructure` |
    | `StopCondition` | 0..n | [`RoutePointTypeEnumeration`](enumerations.md#routepointtypeenumeration) |
    | `ConnectionLinks` | 0..1 |  |
    | `Lines` | 0..1 |  |
    | `Extensions` | 0..1 | `ExtensionsStructure` |

#### Affects / VehicleJourneys / AffectedVehicleJourney {#situations-ptsituationelement-affects-vehiclejourneys-affectedvehiclejourney}

Linee guida §5.4.3 «SituationExchangeDelivery», Tabella 9. Tipo dell'XSD `AffectedVehicleJourneyStructure`.

| Campo | Cardinalità | Tipo | Esempio | Significato (5T) | Fonte |
|---|---|---|---|---|---|
| [`FramedVehicleJourneyRef`](common.md#framedvehiclejourneyref) | 0..1 · scelta 1 | `FramedVehicleJourneyRefStructure` |  |  | §5.4.3, Tab. 9 |
| `FramedVehicleJourneyRef / DatedVehicleJourneyRef` → [DatedVehicleJourney](siri-pt.md#datedtimetableversionframe-datedvehiclejourney) | 1..1 | `DatedVehicleJourneyCodeType` | `IT:ITC1:ServiceJourney:busATS:001_01_01A` | Identificativo della corsa (a consuntivo) esercita dal veicolo su cui ha effetto l’evento | §5.4.3, Tab. 9 |

??? note "Altri campi dell'XSD"

    | Campo | Cardinalità | Tipo |
    |---|---|---|
    | `VehicleJourneyRef` | 0..n | `VehicleJourneyRefStructure` |
    | `DatedVehicleJourneyRef` | 0..n | `DatedVehicleJourneyRefStructure` |
    | `JourneyName` | 0..n | `NaturalLanguageStringStructure` |
    | `Operator` | 0..1 | `AffectedOperatorStructure` |
    | `LineRef` | 0..1 | `LineRefStructure` |
    | `PublishedLineName` | 0..n | `NaturalLanguageStringStructure` |
    | `DirectionRef` | 0..1 | `DirectionRefStructure` |
    | `BlockRef` | 0..1 | `BlockRefStructure` |
    | `TrainNumbers` | 0..1 |  |
    | `JourneyParts` | 0..1 |  |
    | `Origins` | 0..n | `AffectedStopPointStructure` |
    | `Destinations` | 0..n | `AffectedStopPointStructure` |
    | `Route` | 0..n | `AffectedRouteStructure` |
    | `OriginAimedDepartureTime` | 0..1 | `xsd:dateTime` |
    | `DestinationAimedArrivalTime` | 0..1 | `xsd:dateTime` |
    | `OriginDisplayAtDestination` | 0..n | `NaturalLanguagePlaceNameStructure` |
    | `DestinationDisplayAtOrigin` | 0..n | `NaturalLanguagePlaceNameStructure` |
    | `AccessibilityAssessment` | 0..1 | `acsb:AccessibilityAssessmentStructure` |
    | `JourneyCondition` | 0..n | [`ServiceConditionEnumeration`](enumerations.md#serviceconditionenumeration) |
    | `Calls` | 0..1 |  |
    | `Facilities` | 0..1 |  |
    | `Extensions` | 0..1 | `ExtensionsStructure` |

#### Consequences / Consequence {#situations-ptsituationelement-consequences-consequence}

Linee guida §5.4.3 «SituationExchangeDelivery», Tabella 9. Tipo dell'XSD `PtConsequenceStructure`.

| Campo | Cardinalità | Tipo | Esempio | Significato (5T) | Fonte |
|---|---|---|---|---|---|
| [`Period`](#situations-ptsituationelement-consequences-consequence-period) | 0..n | `HalfOpenTimestampOutputRangeStructure` |  |  | §5.4.3, Tab. 9 |
| `Severity` | 0..1 | [`SeverityEnumeration`](enumerations.md#severityenumeration) | `normal` | Gravità dell’evento | §5.4.3, Tab. 9 |
| `Boarding` | 0..1 | `BoardingStructure` |  |  | §5.4.3, Tab. 9 |
| `Boarding / ArrivalBoardingActivity` | 0..1 | [`ArrivalBoardingActivityEnumeration`](enumerations.md#arrivalboardingactivityenumeration) | `noAlighting` | Indica se sia possibile o meno scendere alla fermata su cui agisce l’evento [⚠ Incongruenza](issues.md#9-siri-situationexchangedelivery-siri-situations-siri-ptsituationelement-siri-consequences-siri-consequence-siri-boarding-siri-arrivalboardingactivity) | §5.4.3, Tab. 9 |
| `Boarding / DepartureBoardingActivity` | 0..1 | [`DepartureBoardingActivityEnumeration`](enumerations.md#departureboardingactivityenumeration) | `noBoarding` | Indica se sia possibile o meno salire alla fermata su cui agisce l’evento [⚠ Incongruenza](issues.md#9-siri-situationexchangedelivery-siri-situations-siri-ptsituationelement-siri-consequences-siri-consequence-siri-boarding-siri-departureboardingactivity) | §5.4.3, Tab. 9 |
| `Delays` | 0..1 | `DelaysStructure` |  |  | §5.4.3, Tab. 9 |
| `Delays / DelayType` | 0..1 | [`D2LogicalModel:DelaysTypeEnum`](enumerations.md#d2logicalmodel-delaystypeenum) | `delays` | Specifica il tipo di ritardo | §5.4.3, Tab. 9 |
| `Delays / Delay` | 0..1 | `PositiveDurationType` | `PT10M` | Durata del ritardo causato dall’evento | §5.4.3, Tab. 9 |

??? note "Altri campi dell'XSD"

    | Campo | Cardinalità | Tipo |
    |---|---|---|
    | `Condition` | 0..n | [`ServiceConditionEnumeration`](enumerations.md#serviceconditionenumeration) |
    | `ConditionName` | 0..n | `NaturalLanguageStringStructure` |
    | `Affects` | 0..1 | `AffectsScopeStructure` |
    | `Suitabilities` | 0..1 |  |
    | `Advice` | 0..1 | `PtAdviceStructure` |
    | `Blocking` | 0..1 | `BlockingStructure` |
    | `Casualties` | 0..1 | `CasualtiesStructure` |
    | `Easements` | 0..n | `EasementsStructure` |
    | `Extensions` | 0..1 | `ExtensionsStructure` |

##### Period {#situations-ptsituationelement-consequences-consequence-period}

Linee guida §5.4.3 «SituationExchangeDelivery», Tabella 9. Tipo dell'XSD `HalfOpenTimestampOutputRangeStructure`.

| Campo | Cardinalità | Tipo | Esempio | Significato (5T) | Fonte |
|---|---|---|---|---|---|
| `StartTime` | 1..1 | `xsd:dateTime` | `2023-02-15T10:00:00+01:00` | Inizio delle conseguenze dell’evento | §5.4.3, Tab. 9 (occorrenza 2) |
| `EndTime` | 0..1 | `xsd:dateTime` | `2023-02-16T10:00:00+01:00` | Fine delle conseguenze dell’evento | §5.4.3, Tab. 9 (occorrenza 2) |

??? note "Altri campi dell'XSD"

    | Campo | Cardinalità | Tipo |
    |---|---|---|
    | `EndTimeStatus` | 0..1 | [`EndTimeStatusEnumeration`](enumerations.md#endtimestatusenumeration) |
