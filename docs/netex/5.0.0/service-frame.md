---
generato: true
generato_da: rpsd-tools 0.6.0
---
<!-- GENERATED — DO NOT EDIT · profile-docs netex-it · netex-it-lev5@cecb0cd -->

# ServiceFrame

Rete, linee, fermate programmate e percorsi (linee guida §5.2.5).

## ServiceFrame {#serviceframe}

Linee guida §5.2.5 «ServiceFrame», Tabella 51. Tipo dell'XSD `ServiceFrameL5_VersionStructure`.

| Campo | Cardinalità | Tipo | Esempio | Significato (5T) | Fonte |
|---|---|---|---|---|---|
| `@id` | 1..1 | `xsd:normalizedString` | `epd:IT:ITC1:ServiceFrame_EU_PI_NETWORK:ita` | Identificativo [→ Identificazione](common.md#identificazione) | §5.2.5, Tab. 51 |
| `@version` | 0..1 | `xsd:normalizedString` | `1` | Versione [→ Identificazione](common.md#identificazione) | §5.2.5, Tab. 51 |
| [`TypeOfFrameRef`](common.md#typeofframeref) | 0..1 | `TypeOfFrameRefStructure` |  |  |  |
| [`Network`](#network) | 0..1 | `Network_VersionStructure` |  |  |  |
| [`additionalNetworks`](#additionalnetworks-network) | 0..1 | `additionalNetworks_RelStructure` |  |  |  |
| [`routes`](#routes-route) | 0..1 | `routesL2_RelStructure` |  |  |  |
| [`lines`](#lines-flexibleline) | 0..1 | `linesL5_RelStructure` |  |  |  |
| [`lines`](#lines-line) | 0..1 | `linesL5_RelStructure` |  |  |  |
| [`groupsOfLines`](#groupsoflines-groupoflines) | 0..1 | `groupsOfLines_RelStructure` |  |  |  |
| [`destinationDisplays`](#destinationdisplays-destinationdisplay) | 0..1 | `destinationDisplaysL2_RelStructure` |  |  |  |
| [`scheduledStopPoints`](#scheduledstoppoints-scheduledstoppoint) | 0..1 | `scheduledStopPointsL2_RelStructure` |  |  |  |
| [`serviceLinks`](#servicelinks-servicelink) | 0..1 | `serviceLinksL2_RelStructure` |  |  |  |
| [`stopAreas`](#stopareas-stoparea) | 0..1 | `stopAreas_RelStructure` |  |  |  |
| [`tariffZones`](#tariffzones-tariffzone) | 0..1 | `tariffZonesStructure` |  |  |  |
| [`stopAssignments`](#stopassignments-passengerstopassignment) | 0..1 | `stopAssignmentsL2Structure` |  |  |  |
| [`journeyPatterns`](#journeypatterns-servicejourneypattern) | 0..1 | `journeyPatternsL2Structure` |  |  |  |

??? note "Altri campi dell'XSD"

    | Campo | Cardinalità | Tipo |
    |---|---|---|
    | `@nameOfClass` | 0..1 | `xsd:Name` |
    | `@dataSourceRef` | 0..1 | `xsd:normalizedString` |
    | `@created` | 0..1 | `xsd:dateTime` |
    | `@changed` | 0..1 | `xsd:dateTime` |
    | `@modification` | 0..1 | [`ModificationEnumeration`](enumerations.md#modificationenumeration) |
    | `@status` | 0..1 | [`StatusEnumeration`](enumerations.md#statusenumeration) |
    | `@responsibilitySetRef` | 0..1 | `xsd:normalizedString` |
    | `ValidBetween` | 0..1 | `ValidBetween_VersionStructure` |
    | `Name` | 0..1 | `MultilingualString` |
    | `Description` | 0..1 | `MultilingualString` |
    | `BaselineVersionFrameRef` | 0..1 | `BaselineVersionFrameRefStructure` |
    | `codespaces` | 0..1 | `codespaces_RelStructure` |
    | `FrameDefaults` | 0..1 | `FrameDefaultsStructure` |
    | `prerequisites` | 0..1 | `prerequisites_RelStructure` |
    | `contentValidityConditions` | 0..1 | `contentValidityConditions_RelStructure` |
    | `directions` | 0..1 | `directions_RelStructure` |
    | `routePoints` | 0..1 | `routePoints_RelStructure` |
    | `routeLinks` | 0..1 | `routeLinks_RelStructure` |
    | `connections` | 0..1 | `connectionsL2Structure` |
    | `notices` | 0..1 | `notices_RelStructure` |

### Network {#network}

Linee guida §5.2.5.1 «Network», Tabella 52. Tipo dell'XSD `Network_VersionStructure`.

| Campo | Cardinalità | Tipo | Esempio | Significato (5T) | Fonte |
|---|---|---|---|---|---|
| `@id` | 1..1 | `xsd:normalizedString` | `IT:ITC1:Network:metroATMMILANO:20` | Identificativo [→ Identificazione](common.md#identificazione) | §5.2.5.1, Tab. 52 |
| `@version` | 0..1 | `xsd:normalizedString` | `1` | Versione [→ Identificazione](common.md#identificazione) | §5.2.5.1, Tab. 52 |
| [`ValidBetween`](common.md#validbetween) | 0..1 | `ValidBetween_VersionStructure` |  | Struttura contente le condizioni di validità temporale [⚠ Incongruenza](issues.md#52-netex-serviceframe-netex-network-netex-validbetween) | §5.2.5.1, Tab. 52 |
| `Name` | 0..1 | `MultilingualString` | `Rete TPL Metro Milano` | Nome della rete | §5.2.5.1, Tab. 52 |
| `ShortName` | 0..1 | `MultilingualString` | `TPL Metro Milano` | Nome sintetico della rete | §5.2.5.1, Tab. 52 |
| `PrivateCode` | 0..1 | `PrivateCodeStructure` | `Rete TPL Metro Milano OK` | Codice aziendale della rete espresso in formato testo | §5.2.5.1, Tab. 52 |
| `Description` | 0..1 | `MultilingualString` | `Rete TPL Metro Milano OK – 12/12/2020` | Descrizione della rete | §5.2.5.1, Tab. 52 |
| `OperatorRef` → [Operator](resource-frame.md#organisations-operator) | 0..1 · scelta 1 | `OperatorRefStructure` | `ATMMilano` *(Netex_ITA_1.10_EPIP+Level2+KPI-ART_with_versioning_final_lev5.xml)* | Riferimento all’azienda che gestisce la rete TPL | §5.2.5.1, Tab. 52 |

??? note "Altri campi dell'XSD"

    | Campo | Cardinalità | Tipo |
    |---|---|---|
    | `@nameOfClass` | 0..1 | `xsd:Name` |
    | `@dataSourceRef` | 0..1 | `xsd:normalizedString` |
    | `@created` | 0..1 | `xsd:dateTime` |
    | `@changed` | 0..1 | `xsd:dateTime` |
    | `@modification` | 0..1 | [`ModificationEnumeration`](enumerations.md#modificationenumeration) |
    | `@status` | 0..1 | [`StatusEnumeration`](enumerations.md#statusenumeration) |
    | `@responsibilitySetRef` | 0..1 | `xsd:normalizedString` |
    | `alternativeTexts` | 0..1 | `alternativeTextsStructure` |
    | `keyList` | 0..1 | `keyListStructure` |
    | `BrandingRef` | 0..1 | `BrandingRefStructure` |
    | `PurposeOfGroupingRef` | 0..1 | `PurposeOfGroupingRefStructure` |
    | `members` | 0..1 | `lineRefs_RelStructure` |
    | `MainLineRef` | 0..1 | `LineRefStructure` |
    | `TransportMode` | 0..1 | [`AllVehicleModesOfTransportEnumeration`](enumerations.md#allvehiclemodesoftransportenumeration) |
    | `AuthorityRef` | 0..1 | `AuthorityRefStructure` |
    | `groupsOfLines` | 0..1 | `groupsOfLines_RelStructure` |

### additionalNetworks / Network {#additionalnetworks-network}

Linee guida §5.2.5.2 «AdditionalNetworks», Tabella 53. Tipo dell'XSD `Network_VersionStructure`.

| Campo | Cardinalità | Tipo | Esempio | Significato (5T) | Fonte |
|---|---|---|---|---|---|
| `@id` | 1..1 | `xsd:normalizedString` | `IT:ITC1:Network:metroATMMILANO:RETE METRO MILANO_15` | Identificativo [→ Identificazione](common.md#identificazione) | §5.2.5.2, Tab. 53 |
| `@version` | 0..1 | `xsd:normalizedString` | `1` | Versione [→ Identificazione](common.md#identificazione) | §5.2.5.2, Tab. 53 |
| [`ValidBetween`](common.md#validbetween) | 0..1 | `ValidBetween_VersionStructure` |  | Struttura contente le condizioni di validità temporale [⚠ Incongruenza](issues.md#53-netex-serviceframe-netex-additionalnetworks-netex-network-netex-validbetween) | §5.2.5.2, Tab. 53 |
| `Name` | 0..1 | `MultilingualString` | `Rete TPL Metro Milano` | Nome della rete | §5.2.5.2, Tab. 53 |
| `ShortName` | 0..1 | `MultilingualString` | `Rete TPL Metro Milano` | Nome sintetico della rete | §5.2.5.2, Tab. 53 |
| `PrivateCode` | 0..1 | `PrivateCodeStructure` | `Rete TPL Metro Milano` | Codice aziendale della rete espresso in formato testo | §5.2.5.2, Tab. 53 |
| `Description` | 0..1 | `MultilingualString` | `Rete TPL Metro Milano` | Descrizione della rete | §5.2.5.2, Tab. 53 |
| `OperatorRef` → [Operator](resource-frame.md#organisations-operator) | 0..1 · scelta 1 | `OperatorRefStructure` | `IT:ITC1:Operator:metroATMMILANO:ATMMILANO` | Riferimento all’azienda che gestisce la rete TPL | §5.2.5.2, Tab. 53 |

??? note "Altri campi dell'XSD"

    | Campo | Cardinalità | Tipo |
    |---|---|---|
    | `@nameOfClass` | 0..1 | `xsd:Name` |
    | `@dataSourceRef` | 0..1 | `xsd:normalizedString` |
    | `@created` | 0..1 | `xsd:dateTime` |
    | `@changed` | 0..1 | `xsd:dateTime` |
    | `@modification` | 0..1 | [`ModificationEnumeration`](enumerations.md#modificationenumeration) |
    | `@status` | 0..1 | [`StatusEnumeration`](enumerations.md#statusenumeration) |
    | `@responsibilitySetRef` | 0..1 | `xsd:normalizedString` |
    | `alternativeTexts` | 0..1 | `alternativeTextsStructure` |
    | `keyList` | 0..1 | `keyListStructure` |
    | `BrandingRef` | 0..1 | `BrandingRefStructure` |
    | `PurposeOfGroupingRef` | 0..1 | `PurposeOfGroupingRefStructure` |
    | `members` | 0..1 | `lineRefs_RelStructure` |
    | `MainLineRef` | 0..1 | `LineRefStructure` |
    | `TransportMode` | 0..1 | [`AllVehicleModesOfTransportEnumeration`](enumerations.md#allvehiclemodesoftransportenumeration) |
    | `AuthorityRef` | 0..1 | `AuthorityRefStructure` |
    | `groupsOfLines` | 0..1 | `groupsOfLines_RelStructure` |

### routes / Route {#routes-route}

Linee guida §5.2.5.3 «Routes», Tabella 54. Tipo dell'XSD `RouteL2_VersionStructure`.

| Campo | Cardinalità | Tipo | Esempio | Significato (5T) | Fonte |
|---|---|---|---|---|---|
| `@id` | 1..1 | `xsd:normalizedString` | `IT:ITC1:Route:trenoFS:1` | Identificativo [→ Identificazione](common.md#identificazione) | §5.2.5.3, Tab. 54 |
| `@version` | 0..1 | `xsd:normalizedString` | `1` | Versione [→ Identificazione](common.md#identificazione) [⚠ Incongruenza](issues.md#54-netex-serviceframe-netex-routes-netex-route-version) | §5.2.5.3, Tab. 54 |
| `Name` | 0..1 | `MultilingualString` | `Torino-Milano-Verona` | Nome della linea | §5.2.5.3, Tab. 54 |
| `ShortName` | 0..1 | `MultilingualString` | `Torino-Verona` | Nome sintetico della linea | §5.2.5.3, Tab. 54 |

??? note "Altri campi dell'XSD"

    | Campo | Cardinalità | Tipo |
    |---|---|---|
    | `@nameOfClass` | 0..1 | `xsd:Name` |
    | `@dataSourceRef` | 0..1 | `xsd:normalizedString` |
    | `@created` | 0..1 | `xsd:dateTime` |
    | `@changed` | 0..1 | `xsd:dateTime` |
    | `@modification` | 0..1 | [`ModificationEnumeration`](enumerations.md#modificationenumeration) |
    | `@status` | 0..1 | [`StatusEnumeration`](enumerations.md#statusenumeration) |
    | `@responsibilitySetRef` | 0..1 | `xsd:normalizedString` |
    | `ValidBetween` | 0..1 | `ValidBetween_VersionStructure` |
    | `alternativeTexts` | 0..1 | `alternativeTextsStructure` |
    | `keyList` | 0..1 | `keyListStructure` |
    | `BrandingRef` | 0..1 | `BrandingRefStructure` |
    | `Description` | 0..1 | `MultilingualString` |
    | `Distance` | 0..1 | `LengthType` |
    | `PrivateCode` | 0..1 | `PrivateCodeStructure` |
    | `LineRef` | 0..1 | `LineRefStructure` |
    | `FlexibleLineRef` | 0..1 | `LineRefStructure` |
    | `DirectionType` | 0..1 | [`DirectionTypeEnumeration`](enumerations.md#directiontypeenumeration) |
    | `DirectionRef` | 0..1 | `DirectionRefStructure` |
    | `pointsInSequence` | 0..1 | `routePointsInSequence_RelStructure` |
    | `InverseRouteRef` | 0..1 | `RouteRefStructure` |

### lines / FlexibleLine {#lines-flexibleline}

Linee guida §5.2.5.4.1 «FlexibleLine», Tabella 55. Tipo dell'XSD `FlexibleLineL5Structure`.

| Campo | Cardinalità | Tipo | Esempio | Significato (5T) | Fonte |
|---|---|---|---|---|---|
| `@id` | 1..1 | `xsd:normalizedString` | `IT:ITC1:Line:busATS:TO-MI_a_conferma` | Identificativo [→ Identificazione](common.md#identificazione) | §5.2.5.4.1, Tab. 55 |
| `@version` | 0..1 | `xsd:normalizedString` | `1` | Versione [→ Identificazione](common.md#identificazione) [⚠ Incongruenza](issues.md#55-netex-serviceframe-netex-lines-netex-flexibleline-version) | §5.2.5.4.1, Tab. 55 |
| [`ValidBetween`](common.md#validbetween) | 0..1 | `ValidBetween_VersionStructure` |  | Struttura contente le condizioni di validità temporale [⚠ Incongruenza](issues.md#55-netex-serviceframe-netex-lines-netex-flexibleline-netex-validbetween) | §5.2.5.4.1, Tab. 55 |
| `Name` | 1..1 | `MultilingualString` | `Torino - Milano` | Nome della linea | §5.2.5.4.1, Tab. 55 |
| `ShortName` | 0..1 | `MultilingualString` | `TO-MI` | Nome sintetico della linea | §5.2.5.4.1, Tab. 55 |
| `Description` | 0..1 | `MultilingualString` | `Autostradale - Linea Torino - Milano - Servizio a conferma` | Descrizione della linea | §5.2.5.4.1, Tab. 55 |
| `TransportMode` | 0..1 | [`AllVehicleModesOfTransportEnumeration`](enumerations.md#allvehiclemodesoftransportenumeration) | `bus` | Modalità di trasporto della linea [⚠ Incongruenza](issues.md#55-netex-serviceframe-netex-lines-netex-flexibleline-netex-transportmode) | §5.2.5.4.1, Tab. 55 |
| `Url` | 0..1 | `xsd:anyURI` | `https://autostradale.it/it-IT/Torino_Milan` | Pagina web per la linea | §5.2.5.4.1, Tab. 55 |
| `PrivateCode` | 0..1 | `PrivateCodeStructure` | `001` | Codice aziendale della linea espresso in formato testo | §5.2.5.4.1, Tab. 55 |
| `ExternalLineRef` | 0..1 | `ExternalObjectRefStructure` | `IT:ITC1:Line:trenoFS:tovr` | Identificativo della linea sostituita da quella descritta nella struttura Line | §5.2.5.4.1, Tab. 55 |
| `PublicCode` | 0..1 | `xsd:normalizedString` | `001` | Codice pubblico con cui la linea è nota alla clientela | §5.2.5.4.1, Tab. 55 |
| `OperatorRef` → [Operator](resource-frame.md#organisations-operator) | 0..1 · scelta 1 | `OperatorRefStructure` | `IT:ITC1:Operator:busATS:11` | Riferimento all’azienda che opera la linea | §5.2.5.4.1, Tab. 55 |
| `Monitored` | 0..1 | `xsd:boolean` | `true` | Flag che indica se la linea e monitorata con AVL/AVM | §5.2.5.4.1, Tab. 55 |
| `routes` | 0..1 | `routeRefs_RelStructure` |  |  |  |
| `routes / RouteRef` → [Route](#routes-route) | 1..n | `RouteRefStructure` | `IT:ITC1:Route:trenoFS:1` | Riferimento alla rotta (par. 5.2.5.3) [⚠ Incongruenza](issues.md#55-netex-serviceframe-netex-lines-netex-flexibleline-netex-routes-netex-routeref) | §5.2.5.4.1, Tab. 55 |
| [`Presentation`](common.md#presentation) | 0..1 | `PresentationStructure` |  |  |  |
| `RepresentedByGroupRef` | 0..1 | `RepresentedByGroupRefStructure` | `IT:ITC1:GroupOfLines:metroATMMILANO:EXTRAURBANO` | Riferimento al raggruppamento di linee | §5.2.5.4.1, Tab. 55 |

??? note "Altri campi dell'XSD"

    | Campo | Cardinalità | Tipo |
    |---|---|---|
    | `@nameOfClass` | 0..1 | `xsd:Name` |
    | `@dataSourceRef` | 0..1 | `xsd:normalizedString` |
    | `@created` | 0..1 | `xsd:dateTime` |
    | `@changed` | 0..1 | `xsd:dateTime` |
    | `@modification` | 0..1 | [`ModificationEnumeration`](enumerations.md#modificationenumeration) |
    | `@status` | 0..1 | [`StatusEnumeration`](enumerations.md#statusenumeration) |
    | `@responsibilitySetRef` | 0..1 | `xsd:normalizedString` |
    | `alternativeTexts` | 0..1 | `alternativeTextsStructure` |
    | `keyList` | 0..1 | `keyListStructure` |
    | `BrandingRef` | 0..1 | `BrandingRefStructure` |
    | `TransportSubmode` | 0..1 | `TransportSubmodeStructure` |
    | `AuthorityRef` | 0..1 | `AuthorityRefStructure` |
    | `additionalOperators` | 0..1 | `additionalOperators_RelStructure` |
    | `otherModes` | 0..1 |  |
    | `TypeOfLineRef` | 0..1 | `TypeOfLineRefStructure` |
    | `AccessibilityAssessment` | 0..1 | `AccessibilityAssessmentL5Structure` |
    | `allowedDirections` | 0..1 | `allowedDirections_RelStructure` |
    | `noticeAssignments` | 0..1 | `noticeAssignments_RelStructure` |
    | `documentLinks` | 0..1 | `infoLinks_RelStructure` |
    | `FlexibleLineType` | 0..1 | [`FlexibleLineTypeEnumeration`](enumerations.md#flexiblelinetypeenumeration) |
    | `BookingContact` | 0..1 | `ContactDetailsStructure` |
    | `BookingMethods` | 0..1 | [`BookingMethodListOfEnumerations`](enumerations.md#bookingmethodlistofenumerations) |
    | `BookingAccess` | 0..1 | [`BookingAccessEnumeration`](enumerations.md#bookingaccessenumeration) |
    | `BookWhen` | 0..1 | [`PurchaseWhenEnumeration`](enumerations.md#purchasewhenenumeration) |
    | `BuyWhen` | 0..1 | [`PurchaseMomentListOfEnumerations`](enumerations.md#purchasemomentlistofenumerations) |
    | `LatestBookingTime` | 0..1 | `binding_friendly_time` |
    | `MinimumBookingPeriod` | 0..1 | `xsd:duration` |
    | `BookingUrl` | 0..1 | `xsd:anyURI` |
    | `BookingNote` | 0..1 | `MultilingualString` |

### lines / Line {#lines-line}

Linee guida §5.2.5.4.2 «Line», Tabella 56. Tipo dell'XSD `LineL5Structure`.

| Campo | Cardinalità | Tipo | Esempio | Significato (5T) | Fonte |
|---|---|---|---|---|---|
| `@id` | 1..1 | `xsd:normalizedString` | `IT:ITC1:Line:busATS:TO-MI` | Identificativo [→ Identificazione](common.md#identificazione) | §5.2.5.4.2, Tab. 56 |
| `@version` | 0..1 | `xsd:normalizedString` | `1` | Versione [→ Identificazione](common.md#identificazione) [⚠ Incongruenza](issues.md#56-netex-serviceframe-netex-lines-netex-line-version) | §5.2.5.4.2, Tab. 56 |
| [`ValidBetween`](common.md#validbetween) | 0..1 | `ValidBetween_VersionStructure` |  | Struttura contente le condizioni di validità temporale [⚠ Incongruenza](issues.md#56-netex-serviceframe-netex-lines-netex-line-netex-validbetween) | §5.2.5.4.2, Tab. 56 |
| `Name` | 1..1 | `MultilingualString` | `Torino - Milano` | Nome della linea | §5.2.5.4.2, Tab. 56 |
| `ShortName` | 0..1 | `MultilingualString` | `TO-MI` | Nome sintetico della linea | §5.2.5.4.2, Tab. 56 |
| `Description` | 0..1 | `MultilingualString` | `Autostradale - Linea Torino - Milano` | Descrizione della linea | §5.2.5.4.2, Tab. 56 |
| `TransportMode` | 0..1 | [`AllVehicleModesOfTransportEnumeration`](enumerations.md#allvehiclemodesoftransportenumeration) | `bus` | Modalità di trasporto della linea [⚠ Incongruenza](issues.md#56-netex-serviceframe-netex-lines-netex-line-netex-transportmode) | §5.2.5.4.2, Tab. 56 |
| `Url` | 0..1 | `xsd:anyURI` | `https://autostradale.it/it-IT/Torino_Milan` | Pagina web per la linea | §5.2.5.4.2, Tab. 56 |
| `PrivateCode` | 0..1 | `PrivateCodeStructure` | `001` | Codice aziendale della linea espresso in formato testo | §5.2.5.4.2, Tab. 56 |
| `ExternalLineRef` | 0..1 | `ExternalObjectRefStructure` | `IT:ITC1:Line:trenoFS:tovr` | Identificativo della linea sostituita da quella descritta nella struttura Line | §5.2.5.4.2, Tab. 56 |
| `PublicCode` | 0..1 | `xsd:normalizedString` | `001` | Codice pubblico con cui la linea è nota alla clientela | §5.2.5.4.2, Tab. 56 |
| `OperatorRef` → [Operator](resource-frame.md#organisations-operator) | 0..1 · scelta 1 | `OperatorRefStructure` | `IT:ITC1:Operator:busATS:11` | Riferimento all’azienda che opera la linea | §5.2.5.4.2, Tab. 56 |
| `Monitored` | 0..1 | `xsd:boolean` | `true` | Flag che indica se la linea e monitorata con AVL/AVM | §5.2.5.4.2, Tab. 56 |
| `routes` | 0..1 | `routeRefs_RelStructure` |  |  |  |
| `routes / RouteRef` → [Route](#routes-route) | 1..n | `RouteRefStructure` | `IT:ITC1:Route:trenoFS:1` | Riferimento alla rotta (par. 5.2.5.3) [⚠ Incongruenza](issues.md#56-netex-serviceframe-netex-lines-netex-line-netex-routes-netex-routeref) | §5.2.5.4.2, Tab. 56 |
| [`Presentation`](common.md#presentation) | 0..1 | `PresentationStructure` |  |  |  |
| `RepresentedByGroupRef` | 0..1 | `RepresentedByGroupRefStructure` | `IT:ITC1:GroupOfLines:metroATMMILANO:EXTRAURBANO` | Riferimento al raggruppamento di linee | §5.2.5.4.2, Tab. 56 |

??? note "Altri campi dell'XSD"

    | Campo | Cardinalità | Tipo |
    |---|---|---|
    | `@nameOfClass` | 0..1 | `xsd:Name` |
    | `@dataSourceRef` | 0..1 | `xsd:normalizedString` |
    | `@created` | 0..1 | `xsd:dateTime` |
    | `@changed` | 0..1 | `xsd:dateTime` |
    | `@modification` | 0..1 | [`ModificationEnumeration`](enumerations.md#modificationenumeration) |
    | `@status` | 0..1 | [`StatusEnumeration`](enumerations.md#statusenumeration) |
    | `@responsibilitySetRef` | 0..1 | `xsd:normalizedString` |
    | `alternativeTexts` | 0..1 | `alternativeTextsStructure` |
    | `keyList` | 0..1 | `keyListStructure` |
    | `BrandingRef` | 0..1 | `BrandingRefStructure` |
    | `TransportSubmode` | 0..1 | `TransportSubmodeStructure` |
    | `AuthorityRef` | 0..1 | `AuthorityRefStructure` |
    | `additionalOperators` | 0..1 | `additionalOperators_RelStructure` |
    | `otherModes` | 0..1 |  |
    | `TypeOfLineRef` | 0..1 | `TypeOfLineRefStructure` |
    | `AccessibilityAssessment` | 0..1 | `AccessibilityAssessmentL5Structure` |
    | `allowedDirections` | 0..1 | `allowedDirections_RelStructure` |
    | `noticeAssignments` | 0..1 | `noticeAssignments_RelStructure` |
    | `documentLinks` | 0..1 | `infoLinks_RelStructure` |

### groupsOfLines / GroupOfLines {#groupsoflines-groupoflines}

Linee guida §5.2.5.5 «GroupsOfLines», Tabella 57. Tipo dell'XSD `GroupOfLines_VersionStructure`.

| Campo | Cardinalità | Tipo | Esempio | Significato (5T) | Fonte |
|---|---|---|---|---|---|
| `@id` | 1..1 | `xsd:normalizedString` | `IT:ITC1:GroupOfLines:metroATMMILANO:EXTRAURBANO` | Identificativo [→ Identificazione](common.md#identificazione) | §5.2.5.5, Tab. 57 |
| `@version` | 0..1 | `xsd:normalizedString` | `1` | Versione [→ Identificazione](common.md#identificazione) | §5.2.5.5, Tab. 57 |
| [`ValidBetween`](common.md#validbetween) | 0..1 | `ValidBetween_VersionStructure` |  | Struttura contente le condizioni di validità temporale [⚠ Incongruenza](issues.md#57-netex-serviceframe-netex-groupsoflines-netex-groupoflines-netex-validbetween) | §5.2.5.5, Tab. 57 |
| `Name` | 0..1 | `MultilingualString` | `Extraurbano` | Nome del raggruppamento | §5.2.5.5, Tab. 57 |
| `ShortName` | 0..1 | `MultilingualString` | `TPL Gomma Extraurbano` | Nome sintetico del raggruppamento | §5.2.5.5, Tab. 57 |
| `Description` | 0..1 | `MultilingualString` | `Raggruppamento linee extraurbane` | Descrizione del raggruppamento | §5.2.5.5, Tab. 57 |
| `PrivateCode` | 0..1 | `PrivateCodeStructure` | `EXTRAURBANO` | Codice aziendale del raggruppamento espresso in formato testo | §5.2.5.5, Tab. 57 |
| `members` | 0..1 | `lineRefs_RelStructure` |  | Riferimenti alle linee del raggruppamento | §5.2.5.5, Tab. 57 |
| `members / LineRef` → [Line](#lines-line) | 1..n | `LineRefStructure` | `IT:ITC1:Line:metroATMMILANO:1` | Linea che fa parte del raggruppamento | §5.2.5.5, Tab. 57 |

??? note "Altri campi dell'XSD"

    | Campo | Cardinalità | Tipo |
    |---|---|---|
    | `@nameOfClass` | 0..1 | `xsd:Name` |
    | `@dataSourceRef` | 0..1 | `xsd:normalizedString` |
    | `@created` | 0..1 | `xsd:dateTime` |
    | `@changed` | 0..1 | `xsd:dateTime` |
    | `@modification` | 0..1 | [`ModificationEnumeration`](enumerations.md#modificationenumeration) |
    | `@status` | 0..1 | [`StatusEnumeration`](enumerations.md#statusenumeration) |
    | `@responsibilitySetRef` | 0..1 | `xsd:normalizedString` |
    | `alternativeTexts` | 0..1 | `alternativeTextsStructure` |
    | `keyList` | 0..1 | `keyListStructure` |
    | `BrandingRef` | 0..1 | `BrandingRefStructure` |
    | `PurposeOfGroupingRef` | 0..1 | `PurposeOfGroupingRefStructure` |
    | `MainLineRef` | 0..1 | `LineRefStructure` |
    | `TransportMode` | 0..1 | [`AllVehicleModesOfTransportEnumeration`](enumerations.md#allvehiclemodesoftransportenumeration) |

### destinationDisplays / DestinationDisplay {#destinationdisplays-destinationdisplay}

Linee guida §5.2.5.6 «DestinationDisplays», Tabella 58. Tipo dell'XSD `DestinationDisplayL2_VersionStructure`.

| Campo | Cardinalità | Tipo | Esempio | Significato (5T) | Fonte |
|---|---|---|---|---|---|
| `@id` | 1..1 | `xsd:normalizedString` | `IT:ITC1:DestinationDisplay:trenoFS:dest:1` | Identificativo [→ Identificazione](common.md#identificazione) | §5.2.5.6, Tab. 58 |
| `@version` | 0..1 | `xsd:normalizedString` | `1` | Versione [→ Identificazione](common.md#identificazione) [⚠ Incongruenza](issues.md#58-netex-serviceframe-netex-destinationdisplays-netex-destinationdisplay-version) | §5.2.5.6, Tab. 58 |
| [`ValidBetween`](common.md#validbetween) | 0..1 | `ValidBetween_VersionStructure` |  | Struttura contente le condizioni di validità temporale [⚠ Incongruenza](issues.md#58-netex-serviceframe-netex-destinationdisplays-netex-destinationdisplay-netex-validbetween) | §5.2.5.6, Tab. 58 |
| `Name` | 0..1 | `MultilingualString` | `Milano Centrale F.S.` | Nome del pannello informativo | §5.2.5.6, Tab. 58 |
| `ShortName` | 0..1 | `MultilingualString` | `Milano` | Nome sintetico del pannello informativo | §5.2.5.6, Tab. 58 |
| `SideText` | 0..1 | `MultilingualString` | `Milano F.S.` | Testo visualizzato nel pannello informativo laterale | §5.2.5.6, Tab. 58 |
| `FrontText` | 0..1 | `MultilingualString` | `Milano Centrale F.S.` | Testo visualizzato nel pannello informativo frontale | §5.2.5.6, Tab. 58 |
| `PublicCode` | 0..1 | `xsd:normalizedString` | `MIFS_1` | Codice pubblico del pannello informativo | §5.2.5.6, Tab. 58 |

??? note "Altri campi dell'XSD"

    | Campo | Cardinalità | Tipo |
    |---|---|---|
    | `@nameOfClass` | 0..1 | `xsd:Name` |
    | `@dataSourceRef` | 0..1 | `xsd:normalizedString` |
    | `@created` | 0..1 | `xsd:dateTime` |
    | `@changed` | 0..1 | `xsd:dateTime` |
    | `@modification` | 0..1 | [`ModificationEnumeration`](enumerations.md#modificationenumeration) |
    | `@status` | 0..1 | [`StatusEnumeration`](enumerations.md#statusenumeration) |
    | `@responsibilitySetRef` | 0..1 | `xsd:normalizedString` |
    | `alternativeTexts` | 0..1 | `alternativeTextsStructure` |
    | `keyList` | 0..1 | `keyListStructure` |
    | `BrandingRef` | 0..1 | `BrandingRefStructure` |
    | `vias` | 0..1 | `viasStructure` |
    | `variants` | 0..1 | `destinationDisplayVariants_RelStructure` |

### scheduledStopPoints / ScheduledStopPoint {#scheduledstoppoints-scheduledstoppoint}

Linee guida §5.2.5.7 «ScheduledStopPoints», Tabella 59. Tipo dell'XSD `ScheduledStopPointL2_VersionStructure`.

| Campo | Cardinalità | Tipo | Esempio | Significato (5T) | Fonte |
|---|---|---|---|---|---|
| `@id` | 1..1 | `xsd:normalizedString` | `IT:ITC1:ScheduledStopPoint:metroATMMILANO:GIOIA_3699` | Identificativo [→ Identificazione](common.md#identificazione) | §5.2.5.7, Tab. 59 |
| `@version` | 0..1 | `xsd:normalizedString` | `1` | Versione [→ Identificazione](common.md#identificazione) [⚠ Incongruenza](issues.md#59-netex-serviceframe-netex-scheduledstoppoints-netex-scheduledstoppoint-version) | §5.2.5.7, Tab. 59 |
| [`ValidBetween`](common.md#validbetween) | 0..1 | `ValidBetween_VersionStructure` |  | Struttura contente le condizioni di validità temporale [⚠ Incongruenza](issues.md#59-netex-serviceframe-netex-scheduledstoppoints-netex-scheduledstoppoint-netex-validbetween) | §5.2.5.7, Tab. 59 |
| `Name` | 0..1 | `MultilingualString` | `Fermata Linea M2 (metropolitana di Milano)` | Nome della fermata | §5.2.5.7, Tab. 59 |
| `Location` | 1..1 | `LocationStructure` |  | Posizione geografica della fermata | §5.2.5.7, Tab. 59 |
| `TimingPointStatus` | 0..1 | [`TimingPointStatusEnumeration`](enumerations.md#timingpointstatusenumeration) | `True` | Flag che indica se la fermata e temporizzata | §5.2.5.7, Tab. 59 |
| `ShortName` | 0..1 | `MultilingualString` | `GIOIA` | Nome sintetico della fermata | §5.2.5.7, Tab. 59 |
| `Description` | 0..1 | `MultilingualString` | `GIOIA` | Descrizione della fermata | §5.2.5.7, Tab. 59 |
| `PublicCode` | 0..1 | `PrivateCodeStructure` | `GIOIA_3699` | Codice pubblico con cui la fermata è nota alla clientela | §5.2.5.7, Tab. 59 |
| `PrivateCode` | 0..1 | `PrivateCodeStructure` | `GIOIA_3699` | Codice aziendale della fermata espresso in formato testo | §5.2.5.7, Tab. 59 |
| `tariffZones` | 0..1 | `tariffZoneRefs_RelStructure` | `IT:ITC1:TariffZone:metroATMMILANO:015146_64` | Riferimento alle zone tariffarie per la fermata | §5.2.5.7, Tab. 59 |
| `stopAreas` | 0..1 | `stopAreaRefs_RelStructure` | `IT:ITC1:StopArea:metroATMMILANO:GIOIA` | Riferimento alle aree di fermata associate alla fermata | §5.2.5.7, Tab. 59 |
| `StopType` | 0..1 | [`StopTypeEnumeration`](enumerations.md#stoptypeenumeration) | `Vedi elenco` | Tipologia di fermata Valori del profilo: `onstreetBus`, `onstreetTram`, `railStation`, `metroStation`, `busStation`, `coachStation`, `tramStation`, `ferryStop`, `other`. | §5.2.5.7, Tab. 59 |
| `VehicleModes` | 0..1 | [`VehicleModeListOfEnumerations`](enumerations.md#vehiclemodelistofenumerations) | `Vedi elenco` | Modalità di veicolo Valori del profilo: `air`, `bus`, `trolleyBus`, `tram`, `coach`, `rail`, `metro`, `water`, `cableway`, `funicular`, `lift`, `snowAndIce`. | §5.2.5.7, Tab. 59 |

??? note "Altri campi dell'XSD"

    | Campo | Cardinalità | Tipo |
    |---|---|---|
    | `@nameOfClass` | 0..1 | `xsd:Name` |
    | `@dataSourceRef` | 0..1 | `xsd:normalizedString` |
    | `@created` | 0..1 | `xsd:dateTime` |
    | `@changed` | 0..1 | `xsd:dateTime` |
    | `@modification` | 0..1 | [`ModificationEnumeration`](enumerations.md#modificationenumeration) |
    | `@status` | 0..1 | [`StatusEnumeration`](enumerations.md#statusenumeration) |
    | `@responsibilitySetRef` | 0..1 | `xsd:normalizedString` |
    | `alternativeTexts` | 0..1 | `alternativeTextsStructure` |
    | `keyList` | 0..1 | `keyListStructure` |
    | `BrandingRef` | 0..1 | `BrandingRefStructure` |
    | `PointNumber` | 0..1 | `xsd:normalizedString` |
    | `projections` | 0..1 | `pointProjectionsStructure` |
    | `Presentation` | 0..1 | `PresentationStructure` |

### serviceLinks / ServiceLink {#servicelinks-servicelink}

Linee guida §5.2.5.8 «ServiceLinks», Tabella 60. Tipo dell'XSD `ServiceLinkL2_VersionStructure`.

| Campo | Cardinalità | Tipo | Esempio | Significato (5T) | Fonte |
|---|---|---|---|---|---|
| `@id` | 1..1 | `xsd:normalizedString` | `IT:ITC1:ServiceLink:busATV:164136-164138_1` | Identificativo [→ Identificazione](common.md#identificazione) | §5.2.5.8, Tab. 60 |
| `@version` | 0..1 | `xsd:normalizedString` | `1` | Versione [→ Identificazione](common.md#identificazione) [⚠ Incongruenza](issues.md#60-netex-serviceframe-netex-servicelinks-netex-servicelink-version) | §5.2.5.8, Tab. 60 |
| `Name` | 0..1 | `MultilingualString` | `L164136-164138_1` | Nome della tratta | §5.2.5.8, Tab. 60 |
| `Distance` | 0..1 | `LengthType` | `10` | Lunghezza della tratta in metri | §5.2.5.8, Tab. 60 |
| `gml:LineString` | 0..1 | `gml:T_LineString` | `<gml:posList>10.8375021270454 45.7996993338911 10.8427924483546 45.8039389496581</gml:posList>` | Rappresentazione secondo lo standard GML della polilinea che descrive la geometria della tratta | §5.2.5.8, Tab. 60 |
| `FromPointRef` | 1..1 | `ScheduledStopPointRefStructure` | `IT:ITC1:ScheduledStopPoint:busATV:164136` | Riferimento alla fermata di inizio | §5.2.5.8, Tab. 60 |
| `ToPointRef` | 1..1 | `ScheduledStopPointRefStructure` | `IT:ITC1:ScheduledStopPoint:busATV:164138` | Riferimento alla fermata di fine | §5.2.5.8, Tab. 60 |
| `VehicleMode` | 0..1 | [`AllModesEnumeration`](enumerations.md#allmodesenumeration) | `bus` | Modalità di veicolo [⚠ Incongruenza](issues.md#60-netex-serviceframe-netex-servicelinks-netex-servicelink-netex-vehiclemode) | §5.2.5.8, Tab. 60 |

??? note "Altri campi dell'XSD"

    | Campo | Cardinalità | Tipo |
    |---|---|---|
    | `@nameOfClass` | 0..1 | `xsd:Name` |
    | `@dataSourceRef` | 0..1 | `xsd:normalizedString` |
    | `@created` | 0..1 | `xsd:dateTime` |
    | `@changed` | 0..1 | `xsd:dateTime` |
    | `@modification` | 0..1 | [`ModificationEnumeration`](enumerations.md#modificationenumeration) |
    | `@status` | 0..1 | [`StatusEnumeration`](enumerations.md#statusenumeration) |
    | `@responsibilitySetRef` | 0..1 | `xsd:normalizedString` |
    | `ValidBetween` | 0..1 | `ValidBetween_VersionStructure` |
    | `alternativeTexts` | 0..1 | `alternativeTextsStructure` |
    | `keyList` | 0..1 | `keyListStructure` |
    | `BrandingRef` | 0..1 | `BrandingRefStructure` |
    | `projections` | 0..1 | `projections_RelStructure` |

### stopAreas / StopArea {#stopareas-stoparea}

Linee guida §5.2.5.9 «StopAreas», Tabella 61. Tipo dell'XSD `StopArea_VersionStructure`.

| Campo | Cardinalità | Tipo | Esempio | Significato (5T) | Fonte |
|---|---|---|---|---|---|
| `@id` | 1..1 | `xsd:normalizedString` | `IT:ITC1:StopArea:busATV:0001_GARDA` | Identificativo [→ Identificazione](common.md#identificazione) | §5.2.5.9, Tab. 61 |
| `@version` | 0..1 | `xsd:normalizedString` | `1` | Versione [→ Identificazione](common.md#identificazione) [⚠ Incongruenza](issues.md#61-netex-serviceframe-netex-stopareas-netex-stoparea-version) | §5.2.5.9, Tab. 61 |
| [`ValidBetween`](common.md#validbetween) | 0..1 | `ValidBetween_VersionStructure` |  | Condizioni di validità delle StopAreas | §5.2.5.9, Tab. 61 |
| `Name` | 0..1 | `MultilingualString` | `Stazione degli Autobus Garda` | Nome dell’area di fermata | §5.2.5.9, Tab. 61 |
| `ShortName` | 0..1 | `MultilingualString` | `Stazione degli Autobus Garda` | Nome sintetico dell’area di fermata | §5.2.5.9, Tab. 61 |
| `PrivateCode` | 0..1 | `PrivateCodeStructure` | `x0001_GARDA` | Codice aziendale dell’area fermata espresso in formato testo | §5.2.5.9, Tab. 61 |
| `PublicCode` | 0..1 | `xsd:normalizedString` | `x0001_GARDA` | Codice pubblico con cui l’area di fermata è nota alla clientela | §5.2.5.9, Tab. 61 |
| `Description` | 0..1 | `MultilingualString` | `Stazione degli Autobus Garda` | Descrizione dell’area di fermata | §5.2.5.9, Tab. 61 |
| `members` | 0..1 | `pointRefs_RelStructure` |  |  |  |
| `members / ScheduledStopPointRef` → [ScheduledStopPoint](#scheduledstoppoints-scheduledstoppoint) | 1..n | `ScheduledStopPointRefStructure` | `IT:ITC1:ScheduledStopPoint:busATV:164073` | Riferimento alle fermate che fanno parte della Stop Area [⚠ Incongruenza](issues.md#61-netex-serviceframe-netex-stopareas-netex-stoparea-netex-members-netex-scheduledstoppointref) | §5.2.5.9, Tab. 61 |
| `gml:Polygon` | 0..1 | `gml:T_Polygon` |  | Poligono che delimita l’area di fermata | §5.2.5.9, Tab. 61 |

??? note "Altri campi dell'XSD"

    | Campo | Cardinalità | Tipo |
    |---|---|---|
    | `@nameOfClass` | 0..1 | `xsd:Name` |
    | `@dataSourceRef` | 0..1 | `xsd:normalizedString` |
    | `@created` | 0..1 | `xsd:dateTime` |
    | `@changed` | 0..1 | `xsd:dateTime` |
    | `@modification` | 0..1 | [`ModificationEnumeration`](enumerations.md#modificationenumeration) |
    | `@status` | 0..1 | [`StatusEnumeration`](enumerations.md#statusenumeration) |
    | `@responsibilitySetRef` | 0..1 | `xsd:normalizedString` |
    | `alternativeTexts` | 0..1 | `alternativeTextsStructure` |
    | `keyList` | 0..1 | `keyListStructure` |
    | `BrandingRef` | 0..1 | `BrandingRefStructure` |
    | `PurposeOfGroupingRef` | 0..1 | `PurposeOfGroupingRefStructure` |

### tariffZones / TariffZone {#tariffzones-tariffzone}

Linee guida §5.2.5.10 «TariffZones», Tabella 62. Tipo dell'XSD `TariffZone_VersionStructure`.

| Campo | Cardinalità | Tipo | Esempio | Significato (5T) | Fonte |
|---|---|---|---|---|---|
| `@id` | 1..1 | `xsd:normalizedString` | `IT:ITC1:TariffZone:metroATMMILANO:015146_64` | Identificativo [→ Identificazione](common.md#identificazione) | §5.2.5.10, Tab. 62 |
| `@version` | 0..1 | `xsd:normalizedString` | `1` | Versione [→ Identificazione](common.md#identificazione) [⚠ Incongruenza](issues.md#62-netex-serviceframe-netex-tariffzones-netex-tariffzone-version) | §5.2.5.10, Tab. 62 |
| [`ValidBetween`](common.md#validbetween) | 0..1 | `ValidBetween_VersionStructure` |  | Struttura contente le condizioni di validità temporale [⚠ Incongruenza](issues.md#62-netex-serviceframe-netex-tariffzones-netex-tariffzone-netex-validbetween) | §5.2.5.10, Tab. 62 |
| `Name` | 0..1 | `MultilingualString` | `015146` | Nome della zona tariffaria | §5.2.5.10, Tab. 62 |
| `ShortName` | 0..1 | `MultilingualString` | `015146` | Nome sintetico della zona tariffaria | §5.2.5.10, Tab. 62 |
| `Description` | 0..1 | `MultilingualString` | `Milano` | Descrizione della zona tariffaria | §5.2.5.10, Tab. 62 |
| `PrivateCode` | 0..1 | `PrivateCodeStructure` | `015146_64` | Codice aziendale della zona tariffaria espresso in formato testo | §5.2.5.10, Tab. 62 |
| `Centroid` | 0..1 | `CentroidStructure` |  | Centroide della zona tariffaria | §5.2.5.10, Tab. 62 |
| `gml:Polygon` | 0..1 | `gml:T_Polygon` |  | Poligono che delimita la zona tariffaria | §5.2.5.10, Tab. 62 |

??? note "Altri campi dell'XSD"

    | Campo | Cardinalità | Tipo |
    |---|---|---|
    | `@nameOfClass` | 0..1 | `xsd:Name` |
    | `@dataSourceRef` | 0..1 | `xsd:normalizedString` |
    | `@created` | 0..1 | `xsd:dateTime` |
    | `@changed` | 0..1 | `xsd:dateTime` |
    | `@modification` | 0..1 | [`ModificationEnumeration`](enumerations.md#modificationenumeration) |
    | `@status` | 0..1 | [`StatusEnumeration`](enumerations.md#statusenumeration) |
    | `@responsibilitySetRef` | 0..1 | `xsd:normalizedString` |
    | `alternativeTexts` | 0..1 | `alternativeTextsStructure` |
    | `keyList` | 0..1 | `keyListStructure` |
    | `BrandingRef` | 0..1 | `BrandingRefStructure` |
    | `PurposeOfGroupingRef` | 0..1 | `PurposeOfGroupingRefStructure` |
    | `Presentation` | 0..1 | `PresentationStructure` |

### stopAssignments / PassengerStopAssignment {#stopassignments-passengerstopassignment}

Linee guida §5.2.5.11 «stopAssignments», Tabella 63. Tipo dell'XSD `PassengerStopAssignmentL2_VersionStructure`.

| Campo | Cardinalità | Tipo | Esempio | Significato (5T) | Fonte |
|---|---|---|---|---|---|
| `@id` | 1..1 | `xsd:normalizedString` | `IT:ITC1:PassengerStopAssignment:busATV:164146` | Identificativo [→ Identificazione](common.md#identificazione) | §5.2.5.11, Tab. 63 |
| `@version` | 0..1 | `xsd:normalizedString` | `1` | Versione [→ Identificazione](common.md#identificazione) [⚠ Incongruenza](issues.md#63-netex-serviceframe-netex-stopassignments-netex-passengerstopassignment-version) | §5.2.5.11, Tab. 63 |
| `@order` | 1..1 | `xsd:integer` | `1` | Ordine di visualizzazione dell’assegnazione [⚠ Incongruenza](issues.md#63-netex-serviceframe-netex-stopassignments-netex-passengerstopassignment-order) | §5.2.5.11, Tab. 63 |
| `Description` | 0..1 | `MultilingualString` | `Bus Assignment 164146` | Descrizione dell’assegnazione | §5.2.5.11, Tab. 63 |
| `ScheduledStopPointRef` → [ScheduledStopPoint](#scheduledstoppoints-scheduledstoppoint) | 1..1 | `ScheduledStopPointRefStructure` | `IT:ITC1:ScheduledStopPoint:busATV:164146` | Riferimento alla fermata | §5.2.5.11, Tab. 63 |
| `StopPlaceRef` → [StopPlace](site-frame.md#stopplaces-stopplace) | 1..1 | `StopPlaceRefStructure` | `IT:ITC1:StopPlace:busATV:164146` | Riferimento allo StopPlace | §5.2.5.11, Tab. 63 |
| `QuayRef` → [Quay](site-frame.md#stopplaces-stopplace-quays-quay) | 0..1 | `QuayRefStructure` | `IT:ITC1:Quay:busATV:164146` | Riferimento alla pensilina/banchina | §5.2.5.11, Tab. 63 |

??? note "Altri campi dell'XSD"

    | Campo | Cardinalità | Tipo |
    |---|---|---|
    | `@nameOfClass` | 0..1 | `xsd:Name` |
    | `@dataSourceRef` | 0..1 | `xsd:normalizedString` |
    | `@created` | 0..1 | `xsd:dateTime` |
    | `@changed` | 0..1 | `xsd:dateTime` |
    | `@modification` | 0..1 | [`ModificationEnumeration`](enumerations.md#modificationenumeration) |
    | `@status` | 0..1 | [`StatusEnumeration`](enumerations.md#statusenumeration) |
    | `@responsibilitySetRef` | 0..1 | `xsd:normalizedString` |
    | `ValidBetween` | 0..1 | `ValidBetween_VersionStructure` |
    | `alternativeTexts` | 0..1 | `alternativeTextsStructure` |
    | `keyList` | 0..1 | `keyListStructure` |
    | `BrandingRef` | 0..1 | `BrandingRefStructure` |
    | `trainElements` | 0..1 |  |

### journeyPatterns / ServiceJourneyPattern {#journeypatterns-servicejourneypattern}

Linee guida §5.2.5.12 «JourneyPatterns», Tabella 64. Tipo dell'XSD `JourneyPatternL2_VersionStructure`.

| Campo | Cardinalità | Tipo | Esempio | Significato (5T) | Fonte |
|---|---|---|---|---|---|
| `@id` | 1..1 | `xsd:normalizedString` | `IT:ITC1:ServiceJourneyPattern:busATS:001_01A` | Identificativo [→ Identificazione](common.md#identificazione) | §5.2.5.12, Tab. 64 |
| `@version` | 0..1 | `xsd:normalizedString` | `1` | Versione [→ Identificazione](common.md#identificazione) [⚠ Incongruenza](issues.md#64-netex-serviceframe-netex-journeypatterns-netex-servicejourneypattern-version) | §5.2.5.12, Tab. 64 |
| `Name` | 0..1 | `MultilingualString` | `Torino - Milano Andata` | Nome del percorso | §5.2.5.12, Tab. 64 |
| `ShortName` | 0..1 | `MultilingualString` | `TO-MI A` | Nome sintetico del percorso | §5.2.5.12, Tab. 64 |
| `Distance` | 0..1 | `LengthType` | `60000` | Lunghezza del percorso | §5.2.5.12, Tab. 64 |
| `PrivateCode` | 0..1 | `PrivateCodeStructure` | `00101A` | Codice aziendale del percorso espresso in formato testo | §5.2.5.12, Tab. 64 |
| `RouteView` | 0..1 · scelta 1 | `RouteViewL2Structure` |  |  | §5.2.5.12, Tab. 64 |
| `RouteView / VehicleMode` | 0..1 | [`AllModesEnumeration`](enumerations.md#allmodesenumeration) | `Bus` | Modalità veicolare Valori del profilo: `air`, `all`, `bus`, `cableway`, `coach`, `funicular`, `intercityRail`, `metro`, `rail`, `selfDrive`, `snowAndIce`, `tram`, `trolleyBus`, `unknown`, `urbanRail`, `water`. [⚠ Incongruenza](issues.md#64-netex-serviceframe-netex-journeypatterns-netex-servicejourneypattern-netex-routeview-netex-vehiclemode) | §5.2.5.12, Tab. 64 |
| `RouteView / LineRef` → [Line](#lines-line) | 1..1 | `LineRefStructure` | `IT:ITC1:Line:busATS:TO-MI` | Linea | §5.2.5.12, Tab. 64 |
| `Description` | 0..1 | `MultilingualString` | `Milano Lampugnano` | Descrizione del percorso | §5.2.5.12, Tab. 64 |
| `DirectionType` | 0..1 | [`DirectionTypeEnumeration`](enumerations.md#directiontypeenumeration) | `inbound` | Direzione del percorso | §5.2.5.12, Tab. 64 |
| `DirectionView` | 0..1 · scelta 2 | `DirectionViewStructure` |  |  |  |
| `DirectionView / Name` | 0..1 | `MultilingualString` | `Milano Lampugnano` | Riferimento alla descrizione della direzione del percorso | §5.2.5.12, Tab. 64 |
| `DestinationDisplayView` | 0..1 · scelta 3 | `DestinationDisplayView_VersionStructure` |  |  |  |
| `DestinationDisplayView / Name` | 0..1 | `MultilingualString` | `Milano Lampugnano` | Riferimento alla descrizione della destinazione del percorso visualizzata sui pannelli informativi | §5.2.5.12, Tab. 64 |
| `pointsInSequence` | 0..1 | `stopPointsInSequenceL2_RelStructure` |  |  |  |
| [`pointsInSequence / StopPointInJourneyPattern`](#journeypatterns-servicejourneypattern-pointsinsequence-stoppointinjourneypattern) | 2..n | `StopPointInJourneyPatternL2Structure` |  | Riferimento alle fermate del percorso [⚠ Incongruenza](issues.md#64-netex-serviceframe-netex-journeypatterns-netex-servicejourneypattern-netex-pointsinsequence-netex-stoppointinjourneypattern) | §5.2.5.12, Tab. 64 |
| `linksInSequence` | 0..1 | `linksInSequenceL2_RelStructure` |  |  | §5.2.5.12, Tab. 64 |
| [`linksInSequence / ServiceLinkInJourneyPattern`](#journeypatterns-servicejourneypattern-linksinsequence-servicelinkinjourneypattern) | 1..n | `ServiceLinkInJourneyPatternL2Structure` |  | Struttura con la sequenza di archi | §5.2.5.12, Tab. 64 |
| `ServiceJourneyPatternType` | 0..1 | [`ServiceJourneyPatternTypeEnumeration`](enumerations.md#servicejourneypatterntypeenumeration) | `passenger` | Tipologia di percorso [⚠ Incongruenza](issues.md#64-netex-serviceframe-netex-journeypatterns-netex-servicejourneypattern-netex-servicejourneypatterntype) | §5.2.5.12, Tab. 64 |

??? note "Altri campi dell'XSD"

    | Campo | Cardinalità | Tipo |
    |---|---|---|
    | `@nameOfClass` | 0..1 | `xsd:Name` |
    | `@dataSourceRef` | 0..1 | `xsd:normalizedString` |
    | `@created` | 0..1 | `xsd:dateTime` |
    | `@changed` | 0..1 | `xsd:dateTime` |
    | `@modification` | 0..1 | [`ModificationEnumeration`](enumerations.md#modificationenumeration) |
    | `@status` | 0..1 | [`StatusEnumeration`](enumerations.md#statusenumeration) |
    | `@responsibilitySetRef` | 0..1 | `xsd:normalizedString` |
    | `ValidBetween` | 0..1 | `ValidBetween_VersionStructure` |
    | `alternativeTexts` | 0..1 | `alternativeTextsStructure` |
    | `keyList` | 0..1 | `keyListStructure` |
    | `BrandingRef` | 0..1 | `BrandingRefStructure` |
    | `RouteRef` | 0..1 | `RouteRefStructure` |
    | `DirectionRef` | 0..1 | `DirectionRefStructure` |
    | `DestinationDisplayRef` | 0..1 | `DestinationDisplayRefStructure` |

#### pointsInSequence / StopPointInJourneyPattern {#journeypatterns-servicejourneypattern-pointsinsequence-stoppointinjourneypattern}

Linee guida §5.2.5.12 «JourneyPatterns», Tabella 64. Tipo dell'XSD `StopPointInJourneyPatternL2Structure`.

| Campo | Cardinalità | Tipo | Esempio | Significato (5T) | Fonte |
|---|---|---|---|---|---|
| `@id` | 0..1 | `xsd:normalizedString` | `IT:ITC1:StopPointInJourneyPattern:busATS:001_01A_1` | Identificativo [→ Identificazione](common.md#identificazione) | §5.2.5.12, Tab. 64 (occorrenza 2) |
| `@version` | 0..1 | `xsd:normalizedString` | `1` | Versione [→ Identificazione](common.md#identificazione) | §5.2.5.12, Tab. 64 (occorrenza 2) |
| `@order` | 0..1 | `xsd:integer` | `1` | Ordinale dell’arco nel percorso | §5.2.5.12, Tab. 64 |
| [`ValidBetween`](common.md#validbetween) | 0..1 | `ValidBetween_VersionStructure` |  |  | §5.2.5.12, Tab. 64 |
| `ScheduledStopPointRef` → [ScheduledStopPoint](#scheduledstoppoints-scheduledstoppoint) | 1..1 | `ScheduledStopPointRefStructure` | `IT:ITC1:ScheduledStopPoint:busATS:000241` | Riferimento alla fermata | §5.2.5.12, Tab. 64 |

??? note "Altri campi dell'XSD"

    | Campo | Cardinalità | Tipo |
    |---|---|---|
    | `@nameOfClass` | 0..1 | `xsd:Name` |
    | `@dataSourceRef` | 0..1 | `xsd:normalizedString` |
    | `@created` | 0..1 | `xsd:dateTime` |
    | `@changed` | 0..1 | `xsd:dateTime` |
    | `@modification` | 0..1 | [`ModificationEnumeration`](enumerations.md#modificationenumeration) |
    | `@status` | 0..1 | [`StatusEnumeration`](enumerations.md#statusenumeration) |
    | `alternativeTexts` | 0..1 | `alternativeTextsStructure` |
    | `keyList` | 0..1 | `keyListStructure` |
    | `BrandingRef` | 0..1 | `BrandingRefStructure` |
    | `LinkSequenceRef` | 0..1 | `LinkSequenceRefStructure` |
    | `Description` | 0..1 | `MultilingualString` |
    | `OnwardServiceLinkRef` | 0..1 | `ServiceLinkRefStructure` |
    | `ForAlighting` | 0..1 | `xsd:boolean` |
    | `ForBoarding` | 0..1 | `xsd:boolean` |
    | `DestinationDisplayRef` | 0..1 | `DestinationDisplayRefStructure` |
    | `FlexiblePointProperties` | 0..1 | `FlexiblePointPropertiesStructure` |
    | `ChangeOfDestinationDisplay` | 0..1 | `xsd:boolean` |
    | `noticeAssignments` | 0..1 | `noticeAssignments_RelStructure` |
    | `RequestStop` | 0..1 | `xsd:boolean` |
    | `RequestMethod` | 0..1 | [`RequestMethodTypeEnumeration`](enumerations.md#requestmethodtypeenumeration) |
    | `StopUse` | 0..1 | [`StopUseEnumeration`](enumerations.md#stopuseenumeration) |
    | `BookingArrangements` | 0..1 | `BookingArrangementsStructure` |

#### linksInSequence / ServiceLinkInJourneyPattern {#journeypatterns-servicejourneypattern-linksinsequence-servicelinkinjourneypattern}

Linee guida §5.2.5.12 «JourneyPatterns», Tabella 64. Tipo dell'XSD `ServiceLinkInJourneyPatternL2Structure`.

| Campo | Cardinalità | Tipo | Esempio | Significato (5T) | Fonte |
|---|---|---|---|---|---|
| `@id` | 0..1 | `xsd:normalizedString` | `IT:ITC1:ServiceLinkInJourneyPattern:busATS:001_01A` | Identificativo [→ Identificazione](common.md#identificazione) | §5.2.5.12, Tab. 64 (occorrenza 3) |
| `@version` | 0..1 | `xsd:normalizedString` | `1` | Versione [→ Identificazione](common.md#identificazione) | §5.2.5.12, Tab. 64 (occorrenza 3) |
| `@order` | 0..1 | `xsd:integer` | `1` | Ordinale dell’arco nella sequenza | §5.2.5.12, Tab. 64 (occorrenza 2) |
| `ServiceLinkRef` → [ServiceLink](#servicelinks-servicelink) | 1..1 | `ServiceLinkRefStructure` | `IT:ITC1:ServiceLink:busATS:001` | Riferimento all’arco nella sequenza (par. 5.2.5.5) | §5.2.5.12, Tab. 64 |

??? note "Altri campi dell'XSD"

    | Campo | Cardinalità | Tipo |
    |---|---|---|
    | `@nameOfClass` | 0..1 | `xsd:Name` |
    | `@dataSourceRef` | 0..1 | `xsd:normalizedString` |
    | `@created` | 0..1 | `xsd:dateTime` |
    | `@changed` | 0..1 | `xsd:dateTime` |
    | `@modification` | 0..1 | [`ModificationEnumeration`](enumerations.md#modificationenumeration) |
    | `@status` | 0..1 | [`StatusEnumeration`](enumerations.md#statusenumeration) |
    | `Description` | 0..1 | `MultilingualString` |
