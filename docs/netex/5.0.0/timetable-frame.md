---
generato: true
generato_da: rpsd-tools 0.6.0
---
<!-- GENERATED — DO NOT EDIT · profile-docs netex-it · netex-it-lev5@cecb0cd -->

# TimetableFrame

Corse e coincidenze (linee guida §5.2.6).

## TimetableFrame {#timetableframe}

Linee guida §5.2.6 «TimeTableFrame», Tabella 65. Tipo dell'XSD `TimetableFrameL5_VersionStructure`.

| Campo | Cardinalità | Tipo | Esempio | Significato (5T) | Fonte |
|---|---|---|---|---|---|
| `@id` | 1..1 | `xsd:normalizedString` | `epd:IT:ITC1:TimetableFrame_EU_PI_TIMETABLE:ita` | Identificativo [→ Identificazione](common.md#identificazione) | §5.2.6, Tab. 65 |
| `@version` | 0..1 | `xsd:normalizedString` | `1` | Versione [→ Identificazione](common.md#identificazione) | §5.2.6, Tab. 65 |
| [`TypeOfFrameRef`](common.md#typeofframeref) | 0..1 | `TypeOfFrameRefStructure` |  |  |  |
| [`vehicleJourneys`](#vehiclejourneys-servicejourney) | 0..1 | `vehicleJourneysL5Structure` |  |  |  |
| [`typesOfService`](#typesofservice-typeofservice) | 0..1 | `typesOfService_RelStructure` |  |  |  |
| [`journeyInterchanges`](#journeyinterchanges-servicejourneyinterchange) | 0..1 | `journeyInterchanges_RelStructure` |  |  |  |

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
    | `groupsOfServices` | 0..1 | `groupsOfServices_RelStructure` |
    | `trainNumbers` | 0..1 | `trainNumbers_RelStructure` |
    | `journeyPartCouples` | 0..1 | `journeyPartCouples_RelStructure` |
    | `vehicleTypes` | 0..1 | `vehicleTypesStructure` |

### vehicleJourneys / ServiceJourney {#vehiclejourneys-servicejourney}

Linee guida §5.2.6.1 «VehicleJourneys», Tabella 66. Tipo dell'XSD `ServiceJourneyL5_VersionStructure`.

| Campo | Cardinalità | Tipo | Esempio | Significato (5T) | Fonte |
|---|---|---|---|---|---|
| `@id` | 1..1 | `xsd:normalizedString` | `IT:ITC1:ServiceJourney:busATS:001_01_01A` | Identificativo [→ Identificazione](common.md#identificazione) | §5.2.6.1, Tab. 66 |
| `@version` | 0..1 | `xsd:normalizedString` | `1` | Versione [→ Identificazione](common.md#identificazione) | §5.2.6.1, Tab. 66 |
| [`ValidBetween`](common.md#validbetween) | 0..1 | `ValidBetween_VersionStructure` |  | Validità delle corse | §5.2.6.1, Tab. 66 |
| `Name` | 0..1 | `MultilingualString` | `Corsa 1 Torino – Milano` | Nome della corsa | §5.2.6.1, Tab. 66 |
| `ShortName` | 0..1 | `MultilingualString` | `Corsa 1 TO- MI` | Nome breve della corsa | §5.2.6.1, Tab. 66 |
| `Description` | 0..1 | `MultilingualString` | `Corsa 1 Torino - Milano` | Descrizione libera della corsa | §5.2.6.1, Tab. 66 |
| `PrivateCode` | 0..1 | `PrivateCodeStructure` | `Corsa 1` | Nome aziendale della corsa | §5.2.6.1, Tab. 66 |
| `Distance` | 0..1 | `LengthType` | `60000` | Lunghezza in Km della corsa | §5.2.6.1, Tab. 66 |
| `TransportMode` | 0..1 | [`AllVehicleModesOfTransportEnumeration`](enumerations.md#allvehiclemodesoftransportenumeration) | `bus` | Tipo di trasporto [⚠ Incongruenza](issues.md#66-netex-timetableframe-netex-vehiclejourneys-netex-servicejourney-netex-transportmode) | §5.2.6.1, Tab. 66 |
| [`AccessibilityAssessment`](common.md#accessibilityassessment) | 0..1 | `AccessibilityAssessmentL5Structure` |  |  |  |
| [`journeyAccountings`](#vehiclejourneys-servicejourney-journeyaccountings-journeyaccounting) | 0..1 | `journeyAccountings_RelStructure` |  | Elenco di contratti [⚠ Incongruenza](issues.md#66-netex-timetableframe-netex-vehiclejourneys-netex-servicejourney-netex-journeyaccountings) | §5.2.6.1, Tab. 66 |
| `DepartureTime` | 0..1 | `binding_friendly_time` | `06:54:00Z` | Ora di partenza della corsa | §5.2.6.1, Tab. 66 |
| `JourneyDuration` | 0..1 | `xsd:duration` | `PT1H51M0S` | Durata della corsa | §5.2.6.1, Tab. 66 |
| `dayTypes` | 0..1 | `dayTypes2Structure` | `IT:ITC1:DayType:busATS:annuale12345` | Riferimento al calendario di validità [⚠ Incongruenza](issues.md#66-netex-timetableframe-netex-vehiclejourneys-netex-servicejourney-netex-daytypes) | §5.2.6.1, Tab. 66 |
| `JourneyPatternView` | 0..1 | `JourneyPatternViewStructure` |  |  |  |
| `JourneyPatternView / JourneyPatternRef` | 0..1 | `JourneyPatternRefStructure` | `IT:ITC1:ServiceJourneyPattern:busATS:001_01A` | Riferimento a percorso | §5.2.6.1, Tab. 66 |
| `VehicleTypeRef` → [VehicleType](resource-frame.md#vehicletypes-vehicletype) | 0..1 · scelta 1 | `VehicleTypeRefStructure` | `IT:ITC1:VehicleType:busATS:001` | Riferimento a tipo veicolo che effettua la corsa | §5.2.6.1, Tab. 66 |
| `TrainRef` → [Train](resource-frame.md#vehicletypes-train) | 0..1 · scelta 1 | `TrainRefStructure` | `IT:ITC1:Train:trenoFS:1` | Riferimento a treno che effettua la corsa | §5.2.6.1, Tab. 66 |
| `OperatorRef` → [Operator](resource-frame.md#organisations-operator) | 0..1 | `OperatorRefStructure` | `IT:ITC1:Operator:trenoFS:TI` | Riferimento a Operator | §5.2.6.1, Tab. 66 |
| `LineView` | 0..1 · scelta 2 | `LineViewStructure` |  |  |  |
| `LineView / LineRef` → [Line](service-frame.md#lines-line) | 0..1 | `LineRefStructure` | `IT:ITC1:Line:busATS:TO-MI` | Riferimento alla linea | §5.2.6.1, Tab. 66 |
| `FlexibleLineView` | 0..1 · scelta 2 | `FlexibleLineViewStructure` |  |  |  |
| `FlexibleLineView / FlexibleLineRef` → [FlexibleLine](service-frame.md#lines-flexibleline) | 0..1 | `LineRefStructure` | `IT:ITC1:Line:busATS:TO-MI_a_chiamata` | Riferimento alla linea a chiamata | §5.2.6.1, Tab. 66 |
| `PublicCode` | 0..1 | `xsd:normalizedString` | `Corsa 1` | Nome pubblico della corsa | §5.2.6.1, Tab. 66 |
| [`passingTimes`](#vehiclejourneys-servicejourney-passingtimes-timetabledpassingtime) | 1..1 | `passingTimes_RelStructure` |  | Elenco di passaggi in fermata | §5.2.6.1, Tab. 66 |
| `facilities` | 0..1 | `serviceFacilitiesL2_RelStructure` |  |  |  |
| [`facilities / ServiceFacilitySet`](#vehiclejourneys-servicejourney-facilities-servicefacilityset) | 0..n · scelta 1 | `ServiceFacilitySetL2_VersionStructure` |  |  | §5.2.6.1, Tab. 66 |
| [`FlexibleServiceProperties`](#vehiclejourneys-servicejourney-flexibleserviceproperties) | 0..1 | `FlexibleServicePropertiesL2_VersionStructure` |  |  | §5.2.6.1, Tab. 66 |

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
    | `TypeOfServiceRef` | 0..1 | `TypeOfServiceRefStructure` |
    | `noticeAssignments` | 0..1 | `noticeAssignments_RelStructure` |
    | `DepartureDayOffset` | 0..1 | `xsd:integer` |
    | `ServiceJourneyPatternRef` | 1..1 | `ServiceJourneyPatternRefStructure` |
    | `LineRef` | 0..1 | `LineRefStructure` |
    | `FlexibleLineRef` | 0..1 | `LineRefStructure` |
    | `DirectionType` | 0..1 | [`DirectionTypeEnumeration`](enumerations.md#directiontypeenumeration) |
    | `trainNumbers` | 0..1 | `trainNumberRefs_RelStructure` |
    | `parts` | 0..1 | `journeyParts_RelStructure` |
    | `TrainSize` | 0..1 | `TrainSizeStructure` |

#### journeyAccountings / JourneyAccounting {#vehiclejourneys-servicejourney-journeyaccountings-journeyaccounting}

Linee guida §5.2.6.1 «VehicleJourneys», Tabella 66. Tipo dell'XSD `JourneyAccounting_VersionStructure`.

| Campo | Cardinalità | Tipo | Esempio | Significato (5T) | Fonte |
|---|---|---|---|---|---|
| `@id` | 0..1 | `xsd:normalizedString` | `IT:ITC1:JourneyAccounting:busATS:001_01_01A_1A` | Identificativo [→ Identificazione](common.md#identificazione) | §5.2.6.1, Tab. 66 (occorrenza 2) |
| `@version` | 0..1 | `xsd:normalizedString` | `1` | Versione [→ Identificazione](common.md#identificazione) | §5.2.6.1, Tab. 66 (occorrenza 2) |
| `Name` | 0..1 | `MultilingualString` | `Contratto Piemonte` | Nome del contratto | §5.2.6.1, Tab. 66 (occorrenza 2) |
| `SupplyContractRef` | 0..1 | `SupplyContractRefStructure` | `IT:ITC1:JourneyAccounting:busATS:1A` | Riferimento al contratto | §5.2.6.1, Tab. 66 |
| `Partial` | 0..n | `xsd:boolean` | `true` | Booleano per indicare se il contratto copre solo parte della corsa | §5.2.6.1, Tab. 66 |
| `Distance` | 0..1 | `DistanceType` | `30000` | Lunghezza della corsa coperta dal contratto | §5.2.6.1, Tab. 66 (occorrenza 2) |

??? note "Altri campi dell'XSD"

    | Campo | Cardinalità | Tipo |
    |---|---|---|
    | `@nameOfClass` | 0..1 | `xsd:Name` |
    | `@dataSourceRef` | 0..1 | `xsd:normalizedString` |
    | `@created` | 0..1 | `xsd:dateTime` |
    | `@changed` | 0..1 | `xsd:dateTime` |
    | `@modification` | 0..1 | [`ModificationEnumeration`](enumerations.md#modificationenumeration) |
    | `@status` | 0..1 | [`StatusEnumeration`](enumerations.md#statusenumeration) |
    | `validityConditions` | 0..1 | `validityConditionsL2Structure` |
    | `ValidBetween` | 0..n | `ValidBetween_VersionStructure` |
    | `alternativeTexts` | 0..1 | `alternativeTextsStructure` |
    | `keyList` | 0..1 | `keyListStructure` |
    | `BrandingRef` | 0..1 | `BrandingRefStructure` |
    | `Description` | 0..1 | `MultilingualString` |
    | `AccountedObjectRef` | 0..1 | `AccountedObjectRefStructure` |
    | `OrganisationRef` | 0..1 | `OrganisationRefStructure` |
    | `AccountingCode` | 0..1 | `xsd:normalizedString` |
    | `AccountingType` | 0..1 | [`JourneyAccountingEnumeration`](enumerations.md#journeyaccountingenumeration) |
    | `Duration` | 0..1 | `xsd:duration` |

#### passingTimes / TimetabledPassingTime {#vehiclejourneys-servicejourney-passingtimes-timetabledpassingtime}

Linee guida §5.2.6.1 «VehicleJourneys», Tabella 66. Tipo dell'XSD `TimetabledPassingTimeStructure`.

| Campo | Cardinalità | Tipo | Esempio | Significato (5T) | Fonte |
|---|---|---|---|---|---|
| `@id` | 0..1 | `xsd:normalizedString` | `IT:ITC1:TimetabledPassingTime:busATS:001_01_01A:passingTimes:01` | Identificativo [→ Identificazione](common.md#identificazione) | §5.2.6.1, Tab. 66 (occorrenza 3) |
| `@version` | 0..1 | `xsd:normalizedString` | `1` | Versione [→ Identificazione](common.md#identificazione) | §5.2.6.1, Tab. 66 (occorrenza 3) |
| `StopPointInJourneyPatternRef` → [StopPointInJourneyPattern](service-frame.md#journeypatterns-servicejourneypattern-pointsinsequence-stoppointinjourneypattern) | 1..1 | `StopPointInJourneyPatternRefStructure` | `IT:ITC1:StopPointInJourneyPattern:busATS:001_01A_1` | Riferimento a fermata | §5.2.6.1, Tab. 66 |
| `ArrivalTime` | 0..1 | `binding_friendly_time` | `06:08:00` | Ora di arrivo in fermata | §5.2.6.1, Tab. 66 |
| `DepartureTime` | 0..1 | `binding_friendly_time` | `06:08:00` | Ora di partenza dalla fermata | §5.2.6.1, Tab. 66 (occorrenza 2) |

??? note "Altri campi dell'XSD"

    | Campo | Cardinalità | Tipo |
    |---|---|---|
    | `@nameOfClass` | 0..1 | `xsd:Name` |
    | `@dataSourceRef` | 0..1 | `xsd:normalizedString` |
    | `@created` | 0..1 | `xsd:dateTime` |
    | `@changed` | 0..1 | `xsd:dateTime` |
    | `@modification` | 0..1 | [`ModificationEnumeration`](enumerations.md#modificationenumeration) |
    | `@status` | 0..1 | [`StatusEnumeration`](enumerations.md#statusenumeration) |
    | `ArrivalDayOffset` | 0..1 | `xsd:integer` |
    | `DepartureDayOffset` | 0..1 | `xsd:integer` |
    | `Headway` | 0..1 | `HeadwayIntervalStructure` |

#### facilities / ServiceFacilitySet {#vehiclejourneys-servicejourney-facilities-servicefacilityset}

Linee guida §5.2.6.1 «VehicleJourneys», Tabella 66. Tipo dell'XSD `ServiceFacilitySetL2_VersionStructure`.

| Campo | Cardinalità | Tipo | Esempio | Significato (5T) | Fonte |
|---|---|---|---|---|---|
| `@id` | 1..1 | `xsd:normalizedString` | `IT:ITC1:ServiceFacilitySet:trenoFS:1` | Identificativo [→ Identificazione](common.md#identificazione) | §5.2.6.1, Tab. 66 (occorrenza 4) |
| `@version` | 0..1 | `xsd:normalizedString` | `1` | Versione [→ Identificazione](common.md#identificazione) | §5.2.6.1, Tab. 66 (occorrenza 4) |
| `AssistanceFacilityList` | 0..1 | [`AssistanceFacilityListOfEnumerations`](enumerations.md#assistancefacilitylistofenumerations) | `boardingAssistance` | Struttura di assistenza Valori del profilo: `boardingAssistance`, `conductor`, `information`, `none`, `other`, `personalAssistance`, `wheechairAssistance`, `wheelchairUse`. [⚠ Incongruenza](issues.md#66-netex-timetableframe-netex-vehiclejourneys-netex-servicejourney-netex-facilities-netex-servicefacilityset-netex-assistancefacilitylist) | §5.2.6.1, Tab. 66 |
| `CateringFacilityList` | 0..1 | [`CateringFacilityListOfEnumerations`](enumerations.md#cateringfacilitylistofenumerations) | `buffet` | Strutture di catering | §5.2.6.1, Tab. 66 |
| `FareClasses` | 0..1 | [`FareClassListOfEnumerations`](enumerations.md#fareclasslistofenumerations) | `firstClass` | Classe Valori del profilo: `businessClass`, `economyClass`, `firstClass`, `preferente`, `premiumClass`, `secondClass`, `standardClass`, `thirdClass`, `turista`, `unknown`. | §5.2.6.1, Tab. 66 |
| `MobilityFacilityList` | 0..1 | [`MobilityFacilityListOfEnumerations`](enumerations.md#mobilityfacilitylistofenumerations) | `stepFreeAccess` | Strutture per lo spostamento [⚠ Incongruenza](issues.md#66-netex-timetableframe-netex-vehiclejourneys-netex-servicejourney-netex-facilities-netex-servicefacilityset-netex-mobilityfacilitylist) | §5.2.6.1, Tab. 66 |
| `NuisanceFacilityList` | 0..1 | [`NuisanceFacilityListOfEnumerations`](enumerations.md#nuisancefacilitylistofenumerations) | `mobilePhoneFreeZone` | Strutture specifiche | §5.2.6.1, Tab. 66 |
| `PassengerCommsFacilityList` | 0..1 | [`PassengerCommsFacilityListOfEnumerations`](enumerations.md#passengercommsfacilitylistofenumerations) | `publicWifi` | Strutture per la comunicazione Valori del profilo: `audioEntertainment`, `businessServices`, `freeWifi`, `internet`, `postBox`, `postOffice`, `powerSupplySockets`, `publicWifi`, `telephone`, `unknown`. [⚠ Incongruenza](issues.md#66-netex-timetableframe-netex-vehiclejourneys-netex-servicejourney-netex-facilities-netex-servicefacilityset-netex-passengercommsfacilitylist) | §5.2.6.1, Tab. 66 |
| `PassengerInformationFacilityList` | 0..1 | [`PassengerInformationFacilityListOfEnumerations`](enumerations.md#passengerinformationfacilitylistofenumerations) | `nextStopIndicator` | Strutture per informazioni | §5.2.6.1, Tab. 66 |
| `SanitaryFacilityList` | 0..1 | [`SanitaryFacilityL2ListOfEnumerations`](enumerations.md#sanitaryfacilityl2listofenumerations) | `toilet` | Strutture sanitarie Valori del profilo: `babyChange`, `none`, `other`, `shoeShiner`, `shower`, `washingAndChangeFacilities`, `wheelchairAccessToilet`, `wheelchairBabyChange`. | §5.2.6.1, Tab. 66 |
| `TicketingServiceFacilityList` | 0..1 | [`TicketingServiceFacilityListOfEnumerations`](enumerations.md#ticketingservicefacilitylistofenumerations) | `purchase` | Strutture per rilascio biglietti Valori del profilo: `cardTopUp`, `collection`, `excessFares`, `exchange`, `other`, `purchase`, `refund`, `renewal`, `reservations`. [⚠ Incongruenza](issues.md#66-netex-timetableframe-netex-vehiclejourneys-netex-servicejourney-netex-facilities-netex-servicefacilityset-netex-ticketingservicefacilitylist) | §5.2.6.1, Tab. 66 |
| `AccommodationAccessList` | 0..1 | [`AccommodationAccessListOfEnumerations`](enumerations.md#accommodationaccesslistofenumerations) | `reservation` | Strutture per accesso | §5.2.6.1, Tab. 66 |
| `AccommodationFacilityList` | 0..1 | [`AccommodationFacilityListOfEnumerations`](enumerations.md#accommodationfacilitylistofenumerations) | `couchette` | Tipo di posto | §5.2.6.1, Tab. 66 |
| `CouchetteFacilityList` | 0..1 | [`CouchetteFacilityListOfEnumerations`](enumerations.md#couchettefacilitylistofenumerations) | `C2` | Strutture letto | §5.2.6.1, Tab. 66 |
| `LuggageCarriageFacilityList` | 0..1 | [`LuggageCarriageFacilityListOfEnumerations`](enumerations.md#luggagecarriagefacilitylistofenumerations) | `baggageStorage` | Strutture per bagagli Valori del profilo: `baggageStorage`, `baggageVan`, `cyclesAllowed`, `cyclesAllowedInCarriage`, `cyclesAllowedInVan`, `cyclesAllowedWithReservation`, `extraLargeLuggageRacks`, `luggageRacks`, `noBaggageStorage`, `noCycles`. [⚠ Incongruenza](issues.md#66-netex-timetableframe-netex-vehiclejourneys-netex-servicejourney-netex-facilities-netex-servicefacilityset-netex-luggagecarriagefacilitylist) | §5.2.6.1, Tab. 66 |

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
    | `AccessibilityInfoFacilityList` | 0..1 | [`AccessibilityInfoFacilityListOfEnumerations`](enumerations.md#accessibilityinfofacilitylistofenumerations) |
    | `AccessibilityToolList` | 0..1 | [`AccessibilityToolListOfEnumerations`](enumerations.md#accessibilitytoollistofenumerations) |
    | `CarServiceFacilityList` | 0..1 | [`CarServiceFacilityListOfEnumerations`](enumerations.md#carservicefacilitylistofenumerations) |
    | `FamilyFacilityList` | 0..1 | [`FamilyFacilitiesListOfEnumerations`](enumerations.md#familyfacilitieslistofenumerations) |
    | `GenderLimitation` | 0..1 | [`GenderLimitationEnumeration`](enumerations.md#genderlimitationenumeration) |
    | `MealFacilityList` | 0..1 | [`MealFacilityListOfEnumerations`](enumerations.md#mealfacilitylistofenumerations) |
    | `MedicalFacilityList` | 0..1 | [`MedicalFacilityListOfEnumerations`](enumerations.md#medicalfacilitylistofenumerations) |
    | `PassengerInformationEquipmentList` | 0..1 | [`PassengerInformationEquipmentEnumeration`](enumerations.md#passengerinformationequipmentenumeration) |
    | `RetailFacilityList` | 0..1 | [`RetailFacilityListOfEnumerations`](enumerations.md#retailfacilitylistofenumerations) |
    | `SafetyFacilityList` | 0..1 | [`SafetyFacilityListOfEnumerations`](enumerations.md#safetyfacilitylistofenumerations) |
    | `TicketingFacilityList` | 0..1 | [`TicketingFacilityListOfEnumerations`](enumerations.md#ticketingfacilitylistofenumerations) |
    | `VehicleAccessFacilityList` | 0..1 | [`VehicleAccessFacilityListOfEnumerations`](enumerations.md#vehicleaccessfacilitylistofenumerations) |
    | `BoardingPermission` | 0..1 | [`BoardingPermissionEnumeration`](enumerations.md#boardingpermissionenumeration) |
    | `BookingProcessFacilityList` | 0..1 | [`BookingProcessFacilityListOfEnumerations`](enumerations.md#bookingprocessfacilitylistofenumerations) |
    | `GroupBookingFacility` | 0..1 | [`GroupBookingEnumeration`](enumerations.md#groupbookingenumeration) |
    | `ServiceReservationFacilityList` | 0..1 | [`ServiceReservationFacilityListOfEnumerations`](enumerations.md#servicereservationfacilitylistofenumerations) |
    | `UicProductCharacteristicList` | 0..1 | [`UicProductCharacteristicListOfEnumerations`](enumerations.md#uicproductcharacteristiclistofenumerations) |
    | `UicTrainRate` | 0..1 | [`UicRateTypeEnumeration`](enumerations.md#uicratetypeenumeration) |
    | `accommodations` | 0..1 | `accommodations_RelStructure` |

#### FlexibleServiceProperties {#vehiclejourneys-servicejourney-flexibleserviceproperties}

Linee guida §5.2.6.1 «VehicleJourneys», Tabella 66. Tipo dell'XSD `FlexibleServicePropertiesL2_VersionStructure`.

| Campo | Cardinalità | Tipo | Esempio | Significato (5T) | Fonte |
|---|---|---|---|---|---|
| `@id` | 1..1 | `xsd:normalizedString` | `IT:ITC1:FlexibleServiceProperties:busATS:001_01_01A` | Identificativo [→ Identificazione](common.md#identificazione) | §5.2.6.1, Tab. 66 (occorrenza 5) |
| `@version` | 0..1 | `xsd:normalizedString` | `1` | Versione [→ Identificazione](common.md#identificazione) | §5.2.6.1, Tab. 66 (occorrenza 5) |
| `BookingContact` | 0..1 | `ContactDetailsL2Structure` |  |  |  |
| `BookingContact / ContactRef` | 0..1 | `ContactRefStructure` | `IT:ITC1:Operator:busATS:11` | Riferimento all’operatore che gestisce le prenotazioni | §5.2.6.1, Tab. 66 |
| `BookingMethods` | 0..1 | [`BookingMethodListOfEnumerations`](enumerations.md#bookingmethodlistofenumerations) | `atOffice` | Indica i metodi di prenotazione [⚠ Incongruenza](issues.md#66-netex-timetableframe-netex-vehiclejourneys-netex-servicejourney-netex-flexibleserviceproperties-netex-bookingmethods) | §5.2.6.1, Tab. 66 |
| `BookWhen` | 0..1 | [`PurchaseWhenEnumeration`](enumerations.md#purchasewhenenumeration) | `advanceOnly` | Indica quando è possibile effettuare la prenotazione | §5.2.6.1, Tab. 66 |
| `BuyWhen` | 0..1 | [`PurchaseMomentListOfEnumerations`](enumerations.md#purchasemomentlistofenumerations) | `inAdvance` | Indica quando è possibile acquistare il titolo di viaggio della prenotazione | §5.2.6.1, Tab. 66 |
| `LatestBookingTime` | 0..1 | `binding_friendly_time` | `22:00:00+02:00` | Indica l’ora del giorno fino a cui è possibile effettuare la prenotazione. | §5.2.6.1, Tab. 66 |
| `MinimumBookingPeriod` | 0..1 | `xsd:duration` | `PT24H` | Indica il minimo anticipo con cui è possibile effettuare la prenotazione. [⚠ Incongruenza](issues.md#66-netex-timetableframe-netex-vehiclejourneys-netex-servicejourney-netex-flexibleserviceproperties-netex-minimumbookingperiod) | §5.2.6.1, Tab. 66 |
| `MaximumBookingPeriod` | 0..1 | `xsd:duration` | `P7D` | Indica il massimo anticipo con cui è possibile effettuare la prenotazione. [⚠ Incongruenza](issues.md#66-netex-timetableframe-netex-vehiclejourneys-netex-servicejourney-netex-flexibleserviceproperties-netex-maximumbookingperiod) | §5.2.6.1, Tab. 66 |

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
    | `TypeOfFlexibleServiceRef` | 0..1 | `TypeOfFlexibleServiceRefStructure` |
    | `FlexibleServiceType` | 0..1 | [`FlexibleServiceEnumeration`](enumerations.md#flexibleserviceenumeration) |
    | `CancellationPossible` | 0..1 | `xsd:boolean` |
    | `ChangeOfTimePossible` | 0..1 | `xsd:boolean` |
    | `BookingAccess` | 0..1 | [`BookingAccessEnumeration`](enumerations.md#bookingaccessenumeration) |
    | `BookingUrl` | 0..1 | `xsd:anyURI` |
    | `BookingNote` | 0..1 | `MultilingualString` |

### typesOfService / TypeOfService {#typesofservice-typeofservice}

Linee guida §5.2.6.2 «TypeOfServices», Tabella 67. Tipo dell'XSD `TypeOfService_VersionStructure`.

| Campo | Cardinalità | Tipo | Esempio | Significato (5T) | Fonte |
|---|---|---|---|---|---|
| `@id` | 1..1 | `xsd:normalizedString` | `IT:ITC1:TypeOfService:metroATMMILANO:LIN_20` | Identificativo [→ Identificazione](common.md#identificazione) | §5.2.6.2, Tab. 67 |
| `@version` | 0..1 | `xsd:normalizedString` | `1` | Versione [→ Identificazione](common.md#identificazione) | §5.2.6.2, Tab. 67 |
| [`ValidBetween`](common.md#validbetween) | 0..1 | `ValidBetween_VersionStructure` |  |  |  |
| `Name` | 0..1 | `MultilingualString` | `Corsa in linea` | Nome del servizio | §5.2.6.2, Tab. 67 |
| `ShortName` | 0..1 | `MultilingualString` | `Corsa` | Nome breve del servizio | §5.2.6.2, Tab. 67 |
| `Description` | 0..1 | `MultilingualString` | `Corsa in linea` | Descrizione del tipo di servizio | §5.2.6.2, Tab. 67 |
| `PrivateCode` | 0..1 | `PrivateCodeStructure` | `LIN_20` | Codice del tipo di servizio | §5.2.6.2, Tab. 67 |

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

### journeyInterchanges / ServiceJourneyInterchange {#journeyinterchanges-servicejourneyinterchange}

Linee guida §5.2.6.3 «JourneyInterchanges», Tabella 68. Tipo dell'XSD `ServiceJourneyInterchange_VersionStructure`.

| Campo | Cardinalità | Tipo | Esempio | Significato (5T) | Fonte |
|---|---|---|---|---|---|
| `@id` | 1..1 | `xsd:normalizedString` | `IT:ITC1:ServiceJourneyInterchange:trenoFS:1` | Identificativo [→ Identificazione](common.md#identificazione) | §5.2.6.3, Tab. 68 |
| `@version` | 0..1 | `xsd:normalizedString` | `1` | Versione [→ Identificazione](common.md#identificazione) | §5.2.6.3, Tab. 68 |
| `FromPointRef` | 1..1 | `ScheduledStopPointRefStructure` | `IT:ITC1:ScheduledStopPoint:trenoFS:milanocentrale` | Riferimento alla fermata di inizio interscambio | §5.2.6.3, Tab. 68 |
| `ToPointRef` | 1..1 | `ScheduledStopPointRefStructure` | `IT:ITC1:ScheduledStopPoint:trenoFS:milanocentrale` | Riferimento alla fermata di fine interscambio | §5.2.6.3, Tab. 68 |
| `FromJourneyRef` | 1..1 | `ServiceJourneyRefStructure` | `IT:ITC1:ServiceJourney:trenoFS:1` | Riferimento alla corsa in arrivo | §5.2.6.3, Tab. 68 |
| `ToJourneyRef` | 1..1 | `ServiceJourneyRefStructure` | `IT:ITC1:ServiceJourney:trenoFS:2` | Riferimento alla corsa in partenza | §5.2.6.3, Tab. 68 |

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
    | `ConnectionRef` | 0..1 | `ConnectionRefStructure` |
    | `StaySeated` | 0..1 | `xsd:boolean` |
    | `CrossBorder` | 0..1 | `xsd:boolean` |
    | `StandardTransferTime` | 0..1 | `xsd:duration` |
    | `FromVisitNumber` | 0..1 | `xsd:nonNegativeInteger` |
    | `ToVisitNumber` | 0..1 | `xsd:nonNegativeInteger` |
