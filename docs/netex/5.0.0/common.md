---
generato: true
generato_da: rpsd-tools 0.8.0
---
<!-- GENERATED — DO NOT EDIT · profile-docs netex-it · netex-it-lev5@cecb0cd -->

# Strutture comuni

Strutture usate in più punti del profilo, raggruppate per argomento. La descrizione unica di ogni campo è ricavata dalle note delle linee guida elencate nella colonna Fonte. Le righe dei frame che usano una struttura rimandano qui e tengono la nota del loro contesto.

## Identificazione {#identificazione}

Descrizione unica degli attributi comuni a tutti gli oggetti, riportata nelle loro tabelle.

| Campo | Significato |
|---|---|
| `@id` | Identificativo |
| `@version` | Versione |

## Validità

### ValidBetween {#validbetween}

Struttura contenente le condizioni di validità temporale dell'elemento. Tipo dell'XSD `ValidBetween_VersionStructure`.

| Campo | Cardinalità | Tipo | Esempio | Significato (5T) | Fonte |
|---|---|---|---|---|---|
| `FromDate` | 0..1 | `xsd:dateTime` | `2021-01-01T00:00:00.000+02:00` | Data inizio validità | §5.1.3, Tab. 4, §5.2.3.4.4, Tab. 21, §5.2.3.5.2, Tab. 36, §5.2.3.6, Tab. 37, §5.2.3.7, Tab. 38, §5.2.6.2, Tab. 67, §5.2.7.5, Tab. 74, §5.2.7.10, Tab. 79 |
| `ToDate` | 0..1 | `xsd:dateTime` | `2021-12-31T23:59:59.999+02:00` | Data fine validità | §5.1.3, Tab. 4, §5.2.3.4.4, Tab. 21, §5.2.3.5.2, Tab. 36, §5.2.3.6, Tab. 37, §5.2.3.7, Tab. 38, §5.2.6.2, Tab. 67, §5.2.7.5, Tab. 74, §5.2.7.10, Tab. 79 |

??? note "Altri campi dell'XSD"

    | Campo | Cardinalità | Tipo |
    |---|---|---|
    | `@nameOfClass` | 0..1 | `xsd:Name` |
    | `@id` | 0..1 | `xsd:normalizedString` |
    | `@dataSourceRef` | 0..1 | `xsd:normalizedString` |
    | `@created` | 0..1 | `xsd:dateTime` |
    | `@changed` | 0..1 | `xsd:dateTime` |
    | `@modification` | 0..1 | [`ModificationEnumeration`](enumerations.md#modificationenumeration) |
    | `@version` | 0..1 | `xsd:normalizedString` |
    | `@status` | 0..1 | [`StatusEnumeration`](enumerations.md#statusenumeration) |
    | `@responsibilitySetRef` | 0..1 | `xsd:normalizedString` |

## Accessibilità

### AccessibilityAssessment {#accessibilityassessment}

Tipo dell'XSD `AccessibilityAssessmentL5Structure`.

| Campo | Cardinalità | Tipo | Esempio | Significato (5T) | Fonte |
|---|---|---|---|---|---|
| `@id` | 0..1 | `xsd:normalizedString` | `IT:ITC1:QuayAccessibilityAssignment:busATS:001` | Identificativo | §5.2.4.2.1, Tab. 44 (occorrenza 2), §5.2.4.2.2, Tab. 45 (occorrenza 2), §5.2.4.2.3, Tab. 46 (occorrenza 2), §5.2.6.1, Tab. 66 |
| `@version` | 0..1 | `xsd:normalizedString` | `1` | Versione | §5.2.4.2.1, Tab. 44 (occorrenza 2), §5.2.4.2.2, Tab. 45 (occorrenza 2), §5.2.4.2.3, Tab. 46 (occorrenza 2), §5.2.6.1, Tab. 66 |
| `MobilityImpairedAccess` | 1..1 | [`LimitationStatusEnumeration`](enumerations.md#limitationstatusenumeration) | `true` | Indica se l'elemento (pensilina o banchina, piano, corsa) sia accessibile o meno a disabili motori. | §5.2.4.2, Tab. 43, §5.2.4.2.1, Tab. 44, §5.2.4.2.2, Tab. 45, §5.2.4.2.3, Tab. 46, §5.2.6.1, Tab. 66 |
| [`limitations / AccessibilityLimitation`](#accessibilitylimitation) | 1..n | `AccessibilityLimitationL5Structure` |  |  | §5.2.4.2, Tab. 43, §5.2.4.2.1, Tab. 44, §5.2.4.2.2, Tab. 45, §5.2.4.2.3, Tab. 46, §5.2.6.1, Tab. 66 |
| [`suitabilities / Suitability`](#suitability) | 1..n | `SuitabilityStructure` |  |  | §5.2.4.2, Tab. 43, §5.2.4.2.1, Tab. 44, §5.2.4.2.2, Tab. 45, §5.2.4.2.3, Tab. 46 |

??? note "Altri campi dell'XSD"

    | Campo | Cardinalità | Tipo |
    |---|---|---|
    | `@nameOfClass` | 0..1 | `xsd:Name` |
    | `@dataSourceRef` | 0..1 | `xsd:normalizedString` |
    | `@created` | 0..1 | `xsd:dateTime` |
    | `@changed` | 0..1 | `xsd:dateTime` |
    | `@modification` | 0..1 | [`ModificationEnumeration`](enumerations.md#modificationenumeration) |
    | `@status` | 0..1 | [`StatusEnumeration`](enumerations.md#statusenumeration) |
    | `ValidBetween` | 0..1 | `ValidBetween_VersionStructure` |
    | `alternativeTexts` | 0..1 | `alternativeTextsStructure` |

### AccessibilityLimitation {#accessibilitylimitation}

Tipo dell'XSD `AccessibilityLimitationL5Structure`.

| Campo | Cardinalità | Tipo | Esempio | Significato (5T) | Fonte |
|---|---|---|---|---|---|
| `WheelchairAccess` | 1..1 | [`LimitationStatusEnumeration`](enumerations.md#limitationstatusenumeration) | `true` | Indica l’accessibilità con sedia a rotelle | §5.2.4.2, Tab. 43, §5.2.4.2.1, Tab. 44, §5.2.4.2.2, Tab. 45, §5.2.4.2.3, Tab. 46, §5.2.6.1, Tab. 66 |
| `StepFreeAccess` | 0..1 | [`LimitationStatusEnumeration`](enumerations.md#limitationstatusenumeration) | `Partial` | Indica la presenza di gradini | §5.2.4.2, Tab. 43, §5.2.4.2.1, Tab. 44, §5.2.4.2.2, Tab. 45, §5.2.4.2.3, Tab. 46, §5.2.6.1, Tab. 66 |
| `StairFreeAccess` | 0..1 | [`LimitationStatusEnumeration`](enumerations.md#limitationstatusenumeration) | `Partial` | Indica la presenza di scale | §5.2.4.2, Tab. 43, §5.2.4.2.1, Tab. 44, §5.2.4.2.2, Tab. 45, §5.2.4.2.3, Tab. 46, §5.2.6.1, Tab. 66 |
| `EscalatorFreeAccess` | 0..1 | [`LimitationStatusEnumeration`](enumerations.md#limitationstatusenumeration) | `False` | Indica la presenza di scale mobili | §5.2.4.2, Tab. 43, §5.2.4.2.1, Tab. 44, §5.2.4.2.2, Tab. 45, §5.2.4.2.3, Tab. 46, §5.2.6.1, Tab. 66 |
| `LiftFreeAccess` | 0..1 | [`LimitationStatusEnumeration`](enumerations.md#limitationstatusenumeration) | `True` | Indica la presenza di ascensori | §5.2.4.2, Tab. 43, §5.2.4.2.1, Tab. 44, §5.2.4.2.2, Tab. 45, §5.2.4.2.3, Tab. 46, §5.2.6.1, Tab. 66 |
| `RampFreeAccess` | 0..1 | [`LimitationStatusEnumeration`](enumerations.md#limitationstatusenumeration) | `True` | Indica la presenza di rampe | §5.2.4.2, Tab. 43, §5.2.4.2.1, Tab. 44, §5.2.4.2.2, Tab. 45, §5.2.4.2.3, Tab. 46, §5.2.6.1, Tab. 66 |
| `LevelAccessIntoVehicle` | 0..1 | [`LimitationStatusEnumeration`](enumerations.md#limitationstatusenumeration) | `True` | Indica la presenza di piattaforma a livello del veicolo | §5.2.4.2, Tab. 43, §5.2.4.2.1, Tab. 44, §5.2.4.2.2, Tab. 45, §5.2.4.2.3, Tab. 46, §5.2.6.1, Tab. 66 |
| `AudibleSignalsAvailable` | 0..1 | [`LimitationStatusEnumeration`](enumerations.md#limitationstatusenumeration) | `True` | Indica la presenza di segnali audio | §5.2.4.2, Tab. 43, §5.2.4.2.1, Tab. 44, §5.2.4.2.2, Tab. 45, §5.2.4.2.3, Tab. 46, §5.2.6.1, Tab. 66 |
| `VisualSignsAvailable` | 0..1 | [`LimitationStatusEnumeration`](enumerations.md#limitationstatusenumeration) | `False` | Indica la presenza di segnali visuali | §5.2.4.2, Tab. 43, §5.2.4.2.1, Tab. 44, §5.2.4.2.2, Tab. 45, §5.2.4.2.3, Tab. 46, §5.2.6.1, Tab. 66 |
| `TactileGuidanceAvailable` | 0..1 | [`LimitationStatusEnumeration`](enumerations.md#limitationstatusenumeration) | `False` | Indica la presenza di percorsi tattili | §5.2.4.2, Tab. 43, §5.2.4.2.1, Tab. 44, §5.2.4.2.2, Tab. 45, §5.2.4.2.3, Tab. 46, §5.2.6.1, Tab. 66 |
| `GuideDogAccess` | 0..1 | [`LimitationStatusEnumeration`](enumerations.md#limitationstatusenumeration) | `False` | Indica la possibilità di accesso da parte dei cani guida | §5.2.4.2, Tab. 43, §5.2.4.2.1, Tab. 44, §5.2.4.2.2, Tab. 45, §5.2.4.2.3, Tab. 46, §5.2.6.1, Tab. 66 |

??? note "Altri campi dell'XSD"

    | Campo | Cardinalità | Tipo |
    |---|---|---|
    | `@nameOfClass` | 0..1 | `xsd:Name` |
    | `@id` | 0..1 | `xsd:normalizedString` |
    | `@dataSourceRef` | 0..1 | `xsd:normalizedString` |
    | `@created` | 0..1 | `xsd:dateTime` |
    | `@changed` | 0..1 | `xsd:dateTime` |
    | `@modification` | 0..1 | [`ModificationEnumeration`](enumerations.md#modificationenumeration) |
    | `@version` | 0..1 | `xsd:normalizedString` |
    | `@status` | 0..1 | [`StatusEnumeration`](enumerations.md#statusenumeration) |

### Suitability {#suitability}

Tipo dell'XSD `SuitabilityStructure`.

| Campo | Cardinalità | Tipo | Esempio | Significato (5T) | Fonte |
|---|---|---|---|---|---|
| `MobilityNeed` | 0..1 · scelta 1 | [`MobilityEnumeration`](enumerations.md#mobilityenumeration) | `assistedWheelchair` | Indica l’adeguatezza della struttura a specifiche esigenze degli utenti | §5.2.4.2, Tab. 43, §5.2.4.2.1, Tab. 44, §5.2.4.2.2, Tab. 45, §5.2.4.2.3, Tab. 46 |
| `Excluded` | 0..1 | `xsd:boolean` | `false` | Indica l’esclusione della specifica esigenza | §5.2.4.2, Tab. 43, §5.2.4.2.1, Tab. 44, §5.2.4.2.2, Tab. 45, §5.2.4.2.3, Tab. 46 |
| `NeedRanking` | 0..1 | `xsd:integer` | `1` | Indica la priorità della specifica esigenza | §5.2.4.2, Tab. 43, §5.2.4.2.1, Tab. 44, §5.2.4.2.2, Tab. 45, §5.2.4.2.3, Tab. 46 |
| `Suitable` | 1..1 | [`SuitableEnumeration`](enumerations.md#suitableenumeration) | `suitable` | Indica l’adeguatezza alla specifica esigenza | §5.2.4.2, Tab. 43, §5.2.4.2.1, Tab. 44, §5.2.4.2.2, Tab. 45, §5.2.4.2.3, Tab. 46 |

??? note "Altri campi dell'XSD"

    | Campo | Cardinalità | Tipo |
    |---|---|---|
    | `@nameOfClass` | 0..1 | `xsd:Name` |
    | `@id` | 0..1 | `xsd:normalizedString` |
    | `@dataSourceRef` | 0..1 | `xsd:normalizedString` |
    | `@created` | 0..1 | `xsd:dateTime` |
    | `@changed` | 0..1 | `xsd:dateTime` |
    | `@modification` | 0..1 | [`ModificationEnumeration`](enumerations.md#modificationenumeration) |
    | `@version` | 0..1 | `xsd:normalizedString` |
    | `@status` | 0..1 | [`StatusEnumeration`](enumerations.md#statusenumeration) |
    | `PsychosensoryNeed` | 0..1 | [`PsychosensoryNeedEnumeration`](enumerations.md#psychosensoryneedenumeration) |
    | `MedicalNeed` | 0..1 |  |
    | `EncumbranceNeed` | 0..1 | [`EncumbranceEnumeration`](enumerations.md#encumbranceenumeration) |

## Tipo di frame

### TypeOfFrameRef {#typeofframeref}

Tipo dell'XSD `TypeOfFrameRefStructure`.

| Campo | Cardinalità | Tipo | Esempio | Significato (5T) | Fonte |
|---|---|---|---|---|---|
| `@ref` | 1..1 | `xsd:normalizedString` | `epip:EU_PI_LINE_OFFER` | Tipologia di frame | §5.1.3, Tab. 4, §5.2.1, Tab. 5, §5.2.2, Tab. 7, §5.2.3, Tab. 12, §5.2.4, Tab. 41, §5.2.5, Tab. 51, §5.2.6, Tab. 65 |
| `@version` | 0..1 | `xsd:normalizedString` | `1` | Versione del Frame | §5.1.3, Tab. 4, §5.2.4, Tab. 41, §5.2.5, Tab. 51, §5.2.6, Tab. 65 |
| `@versionRef` | 0..1 | `xsd:normalizedString` | `1` | Versione del Frame | §5.2.1, Tab. 5, §5.2.2, Tab. 7, §5.2.3, Tab. 12 |

??? note "Altri campi dell'XSD"

    | Campo | Cardinalità | Tipo |
    |---|---|---|
    | `@nameOfRefClass` | 0..1 | `xsd:Name` |
    | `@created` | 0..1 | `xsd:dateTime` |
    | `@changed` | 0..1 | `xsd:dateTime` |
    | `@modification` | 0..1 | [`ModificationEnumeration`](enumerations.md#modificationenumeration) |

## Veicoli

### PassengerCapacity {#passengercapacity}

Tipo dell'XSD `PassengerCapacity_VersionStructure`.

| Campo | Cardinalità | Tipo | Esempio | Significato (5T) | Fonte |
|---|---|---|---|---|---|
| `@id` | 1..1 | `xsd:normalizedString` | `IT:ITC1:PassengerCapacity:001` | Identificativo | §5.2.3.5.1, Tab. 35 (occorrenza 2) |
| `TotalCapacity` | 0..1 | `xsd:nonNegativeInteger` | `60` | Numero totale di posti. | §5.2.3.5.1, Tab. 35, §5.2.3.5.2, Tab. 36 |
| `SeatingCapacity` | 0..1 | `xsd:nonNegativeInteger` | `55` | Numero totale di posti a sedere. | §5.2.3.5.1, Tab. 35, §5.2.3.5.2, Tab. 36 |
| `StandingCapacity` | 0..1 | `xsd:nonNegativeInteger` | `3` | Numero totale di posti in piedi. | §5.2.3.5.1, Tab. 35, §5.2.3.5.2, Tab. 36 |
| `SpecialPlaceCapacity` | 0..1 | `xsd:nonNegativeInteger` | `1` | Numero totale di posti a sedere per utenti disabili. | §5.2.3.5.1, Tab. 35, §5.2.3.5.2, Tab. 36 |
| `WheelchairPlaceCapacity` | 0..1 | `xsd:nonNegativeInteger` | `1` | Numero totale di posti dedicati per sedie a rotelle. | §5.2.3.5.1, Tab. 35, §5.2.3.5.2, Tab. 36 |

??? note "Altri campi dell'XSD"

    | Campo | Cardinalità | Tipo |
    |---|---|---|
    | `@nameOfClass` | 0..1 | `xsd:Name` |
    | `@dataSourceRef` | 0..1 | `xsd:normalizedString` |
    | `@created` | 0..1 | `xsd:dateTime` |
    | `@changed` | 0..1 | `xsd:dateTime` |
    | `@modification` | 0..1 | [`ModificationEnumeration`](enumerations.md#modificationenumeration) |
    | `@version` | 0..1 | `xsd:normalizedString` |
    | `@status` | 0..1 | [`StatusEnumeration`](enumerations.md#statusenumeration) |
    | `@responsibilitySetRef` | 0..1 | `xsd:normalizedString` |
    | `ValidBetween` | 0..1 | `ValidBetween_VersionStructure` |
    | `alternativeTexts` | 0..1 | `alternativeTextsStructure` |
    | `keyList` | 0..1 | `keyListStructure` |
    | `BrandingRef` | 0..1 | `BrandingRefStructure` |
    | `FareClass` | 0..1 | `xsd:normalizedString` |
    | `PushchairCapacity` | 0..1 | `xsd:nonNegativeInteger` |

## Presentazione

### Presentation {#presentation}

Tipo dell'XSD `PresentationStructure`.

| Campo | Cardinalità | Tipo | Esempio | Significato (5T) | Fonte |
|---|---|---|---|---|---|
| `Colour` | 0..1 | `ColourValueType` | `FF2000` | Colore della linea (per infomobilità) | §5.2.5.4.1, Tab. 55, §5.2.5.4.2, Tab. 56 |

??? note "Altri campi dell'XSD"

    | Campo | Cardinalità | Tipo |
    |---|---|---|
    | `ColourName` | 0..1 | `xsd:normalizedString` |
    | `ColourSystem` | 0..1 | `xsd:normalizedString` |
    | `BackgroundColour` | 0..1 | `ColourValueType` |
    | `BackgroundColourName` | 0..1 | `xsd:normalizedString` |
    | `TextColour` | 0..1 | `ColourValueType` |
    | `TextColourName` | 0..1 | `xsd:normalizedString` |
    | `TextFont` | 0..1 | `xsd:normalizedString` |
    | `TextFontName` | 0..1 | `xsd:normalizedString` |
    | `TextLanguage` | 0..1 | `xsd:language` |
    | `infoLinks` | 0..1 | `infoLinks_RelStructure` |

## Contatti e indirizzi

### ContactDetails {#contactdetails}

Informazioni di contatto del referente. Tipo dell'XSD `ContactDetailsStructure`.

| Campo | Cardinalità | Tipo | Esempio | Significato (5T) | Fonte |
|---|---|---|---|---|---|
| `Email` | 0..1 | `xsd:normalizedString` | `luigi.milano@atm.it` | Indirizzo email ufficiale di contatto | §4.3, Tab. 1 |
| `Phone` | 0..1 | `xsd:normalizedString` | `+39-02-453502` | Numero di telefono di contatto | §4.3, Tab. 1 |
| `Url` | 0..1 | `xsd:anyURI` | `www.atm.it` | Indirizzo web di riferimento dell’azienda o nel caso di provider di servizi di mobilità (TravelAgent) url del e-commerce | §4.3, Tab. 1 |

### PostalAddress {#postaladdress}

Tipo dell'XSD `PostalAddress_VersionStructure`.

| Campo | Cardinalità | Tipo | Esempio | Significato (5T) | Fonte |
|---|---|---|---|---|---|
| `CountryName` | 0..1 | `MultilingualString` | `Italia` | Stato | §4.4, Tab. 2 |
| `Street` | 0..1 | `MultilingualString` | `piazza Castello 1` | Indirizzo (eventualmente completo di civico). | §4.4, Tab. 2 |
| `Town` | 0..1 | `MultilingualString` | `Milano` | Comune | §4.4, Tab. 2 |
| `PostCode` | 0..1 | `xsd:normalizedString` | `20121` | Codice di Avviamento Postale. | §4.4, Tab. 2 |

??? note "Altri campi dell'XSD"

    | Campo | Cardinalità | Tipo |
    |---|---|---|
    | `@nameOfClass` | 0..1 | `xsd:Name` |
    | `@id` | 1..1 | `xsd:normalizedString` |
    | `@dataSourceRef` | 0..1 | `xsd:normalizedString` |
    | `@created` | 0..1 | `xsd:dateTime` |
    | `@changed` | 0..1 | `xsd:dateTime` |
    | `@modification` | 0..1 | [`ModificationEnumeration`](enumerations.md#modificationenumeration) |
    | `@version` | 0..1 | `xsd:normalizedString` |
    | `@status` | 0..1 | [`StatusEnumeration`](enumerations.md#statusenumeration) |
    | `@responsibilitySetRef` | 0..1 | `xsd:normalizedString` |
    | `ValidBetween` | 0..1 | `ValidBetween_VersionStructure` |
    | `alternativeTexts` | 0..1 | `alternativeTextsStructure` |
    | `keyList` | 0..1 | `keyListStructure` |
    | `BrandingRef` | 0..1 | `BrandingRefStructure` |
    | `Name` | 0..1 | `MultilingualString` |
    | `ShortName` | 0..1 | `MultilingualString` |
    | `Description` | 0..1 | `MultilingualString` |
    | `PurposeOfGroupingRef` | 0..1 | `PurposeOfGroupingRefStructure` |
    | `PrivateCode` | 0..1 | `PrivateCodeStructure` |
    | `members` | 0..1 | `PlaceObjectMembers` |
    | `Centroid` | 0..1 | `CentroidStructure` |
    | `gml:Polygon` | 0..1 | `gml:T_Polygon` |
    | `placeTypes` | 0..1 | `placeTypes_Structure` |
    | `CountryRef` | 0..1 | `CountryRefStructure` |
    | `HouseNumber` | 0..1 | `xsd:normalizedString` |
    | `BuildingName` | 0..1 | `MultilingualString` |
    | `AddressLine1` | 0..1 | `MultilingualString` |
    | `AddressLine2` | 0..1 | `MultilingualString` |
    | `Suburb` | 0..1 | `MultilingualString` |
    | `PostCodeExtension` | 0..1 | `xsd:normalizedString` |
    | `PostalRegion` | 0..1 | `xsd:normalizedString` |
    | `Province` | 0..1 | `MultilingualString` |
    | `RoadAddressRef` | 0..1 | `RoadAddressRefStructure` |
