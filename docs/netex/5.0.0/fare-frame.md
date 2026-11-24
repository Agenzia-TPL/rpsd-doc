---
generato: true
generato_da: rpsd-tools 0.8.0
---
<!-- GENERATED — DO NOT EDIT · profile-docs netex-it · netex-it-lev5@cecb0cd -->

# FareFrame

Tariffe e titoli di viaggio (linee guida §5.2.7).

## FareFrame {#fareframe}

Linee guida §5.2.7 «FareFrame», Tabella 69. Tipo dell'XSD `FareFrameL4_VersionStructure`.

| Campo | Cardinalità | Tipo | Esempio | Significato (5T) | Fonte |
|---|---|---|---|---|---|
| `@id` | 1..1 | `xsd:normalizedString` | `epd:IT:ITC1:FareFrame_EU_PI_FARE:TPL:ita` | Identificativo [→ Identificazione](common.md#identificazione) | §5.2.7, Tab. 69 |
| `@version` | 0..1 | `xsd:normalizedString` | `1` | Versione [→ Identificazione](common.md#identificazione) | §5.2.7, Tab. 69 |
| [`geographicalUnits`](#geographicalunits-geographicalunit) | 0..1 | `geographicalUnits_RelStructure` |  |  |  |
| [`tariffs`](#tariffs-tariff) | 0..1 | `tariffs_RelStructure` |  |  |  |
| [`validableElements`](#validableelements-validableelement) | 0..1 | `validableElements_RelStructure` |  |  |  |
| [`usageParameters`](#usageparameters-usagevalidityperiod) | 0..1 | `usageParameters_RelStructure` |  |  |  |
| [`usageParameters`](#usageparameters-userprofile) | 0..1 | `usageParameters_RelStructure` |  |  |  |
| [`fareProducts`](#fareproducts-preassignedfareproduct) | 0..1 | `fareProductsL4_RelStructure` |  |  |  |
| [`fareTables`](#faretables-faretable) | 0..1 | `fareTables_RelStructure` |  |  |  |
| [`distributionChannels`](#distributionchannels-distributionchannel) | 0..1 | `distributionChannels_RelStructure` |  |  |  |
| [`typesOfTravelDocuments`](#typesoftraveldocuments-typeoftraveldocument) | 0..1 | `typesOfTravelDocuments_RelStructure` |  |  |  |
| [`salesOfferPackages`](#salesofferpackages-salesofferpackage) | 0..1 | `salesOfferPackages_RelStructure` |  |  |  |
| [`parkingTariffs`](#parkingtariffs-parkingtariff) | 0..1 | `parkingTariffs_RelStructure` |  |  |  |

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
    | `TypeOfFrameRef` | 0..1 | `TypeOfFrameRefStructure` |
    | `BaselineVersionFrameRef` | 0..1 | `BaselineVersionFrameRefStructure` |
    | `codespaces` | 0..1 | `codespaces_RelStructure` |
    | `FrameDefaults` | 0..1 | `FrameDefaultsStructure` |
    | `prerequisites` | 0..1 | `prerequisites_RelStructure` |
    | `contentValidityConditions` | 0..1 | `contentValidityConditions_RelStructure` |
    | `timeUnits` | 0..1 | `timeUnits_RelStructure` |

### geographicalUnits / GeographicalUnit {#geographicalunits-geographicalunit}

Linee guida §5.2.7.1 «geographicalUnits», Tabella 70. Tipo dell'XSD `GeographicalUnit_VersionStructure`.

| Campo | Cardinalità | Tipo | Esempio | Significato (5T) | Fonte |
|---|---|---|---|---|---|
| `@id` | 1..1 | `xsd:normalizedString` | `IT:ITC1:GeographicalUnit:busATS:gu:1` | Identificativo [→ Identificazione](common.md#identificazione) | §5.2.7.1, Tab. 70 |
| `@version` | 0..1 | `xsd:normalizedString` | `1` | Versione [→ Identificazione](common.md#identificazione) | §5.2.7.1, Tab. 70 |
| `Name` | 0..1 | `MultilingualString` | `Unità geografica 1km` | Nome dell’unità geografica | §5.2.7.1, Tab. 70 |
| `Distance` | 0..1 | `LengthType` | `1000` | Valore della distanza | §5.2.7.1, Tab. 70 |

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

### tariffs / Tariff {#tariffs-tariff}

Linee guida §5.2.7.2 «tariffs», Tabella 71. Tipo dell'XSD `Tariff_VersionStructure`.

| Campo | Cardinalità | Tipo | Esempio | Significato (5T) | Fonte |
|---|---|---|---|---|---|
| `@id` | 1..1 | `xsd:normalizedString` | `IT:ITC1:Tariff:busATS:tf:1` | Identificativo [→ Identificazione](common.md#identificazione) | §5.2.7.2, Tab. 71 |
| `@version` | 0..1 | `xsd:normalizedString` | `1` | Versione [→ Identificazione](common.md#identificazione) | §5.2.7.2, Tab. 71 |
| [`geographicalIntervals`](#tariffs-tariff-geographicalintervals-geographicalinterval) | 0..1 | `geographicalIntervals_RelStructure` |  |  |  |
| [`timeIntervals`](#tariffs-tariff-timeintervals-timeinterval) | 0..1 | `timeIntervals_RelStructure` |  |  |  |
| [`fareStructureElements`](#tariffs-tariff-farestructureelements-farestructureelement) | 0..1 | `fareStructureElements_RelStructure` |  |  |  |
| `distanceMatrixElements / DistanceMatrixElementRef` → [DistanceMatrixElement](#tariffs-tariff-distancematrixelements-distancematrixelement) | 0..n · scelta 1 | `DistanceMatrixElementRefStructure` | `IT:ITC1:DistanceMatrixElement:busATS:dm:1` | Riferimento a matrice distanza | §5.2.7.2, Tab. 71 |
| `geographicalIntervals / GeographicalIntervalRef` → [GeographicalInterval](#tariffs-tariff-geographicalintervals-geographicalinterval) | 0..n · scelta 1 | `GeographicalIntervalRefStructure` | `IT:ITC1:GeographicalInterval:busATS:gi:0-5` | Riferimento a intervallo geografico | §5.2.7.2, Tab. 71 |
| [`distanceMatrixElements`](#tariffs-tariff-distancematrixelements-distancematrixelement) | 0..1 | `distanceMatrixElements_RelStructure` |  |  |  |

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

#### geographicalIntervals / GeographicalInterval {#tariffs-tariff-geographicalintervals-geographicalinterval}

Linee guida §5.2.7.2 «tariffs», Tabella 71. Tipo dell'XSD `GeographicalInterval_VersionStructure`.

| Campo | Cardinalità | Tipo | Esempio | Significato (5T) | Fonte |
|---|---|---|---|---|---|
| `@id` | 1..1 | `xsd:normalizedString` | `IT:ITC1:GeographicalInterval:busATS:gi:0-5` | Identificativo [→ Identificazione](common.md#identificazione) | §5.2.7.2, Tab. 71 |
| `@version` | 0..1 | `xsd:normalizedString` | `1` | Versione [→ Identificazione](common.md#identificazione) | §5.2.7.2, Tab. 71 |
| `StartGeographicalValue` | 0..1 | `xsd:decimal` | `0` | Inizio intervallo geografico | §5.2.7.2, Tab. 71 |
| `EndGeographicalValue` | 0..1 | `xsd:decimal` | `5` | Fine intervallo geografico | §5.2.7.2, Tab. 71 |
| `GeographicalUnitRef` → [GeographicalUnit](#geographicalunits-geographicalunit) | 0..1 | `GeographicalUnitRefStructure` | `IT:ITC1:GeographicalUnit:busATS:gu:1` | Riferimento all’unità geografica | §5.2.7.2, Tab. 71 |
| `Description` | 0..1 | `MultilingualString` | `singola corsa` | Descrizione testuale | §5.2.7.2, Tab. 71 |

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
    | `NumberOfUnits` | 0..1 | `xsd:integer` |
    | `IntervalType` | 0..1 | [`IntervalTypeEnumeration`](enumerations.md#intervaltypeenumeration) |

#### timeIntervals / TimeInterval {#tariffs-tariff-timeintervals-timeinterval}

Linee guida §5.2.7.2 «tariffs», Tabella 71. Tipo dell'XSD `TimeInterval_VersionStructure`.

| Campo | Cardinalità | Tipo | Esempio | Significato (5T) | Fonte |
|---|---|---|---|---|---|
| `@id` | 1..1 | `xsd:normalizedString` | `IT:ITC1:TimeInterval:busATS:ti:1` | Identificativo [→ Identificazione](common.md#identificazione) | §5.2.7.2, Tab. 71 |
| `@version` | 0..1 | `xsd:normalizedString` | `1` | Versione [→ Identificazione](common.md#identificazione) | §5.2.7.2, Tab. 71 |
| `Duration` | 0..1 | `xsd:duration` | `PT90M` | Durata | §5.2.7.2, Tab. 71 |

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
    | `StartTime` | 0..1 | `xsd:time` |
    | `EndTime` | 0..1 | `xsd:time` |
    | `DayOffset` | 0..1 | `DayOffsetType` |
    | `MinimumDuration` | 0..1 | `xsd:duration` |

#### fareStructureElements / FareStructureElement {#tariffs-tariff-farestructureelements-farestructureelement}

Linee guida §5.2.7.2 «tariffs», Tabella 71. Tipo dell'XSD `FareStructureElement_VersionStructure`.

| Campo | Cardinalità | Tipo | Esempio | Significato (5T) | Fonte |
|---|---|---|---|---|---|
| `@id` | 1..1 | `xsd:normalizedString` | `IT:ITC1:FareStructureElement:busATS:fse:8` | Identificativo [→ Identificazione](common.md#identificazione) | §5.2.7.2, Tab. 71 |
| `@version` | 0..1 | `xsd:normalizedString` | `1` | Versione [→ Identificazione](common.md#identificazione) | §5.2.7.2, Tab. 71 |
| `fareStructureElementsInSequence / FareStructureElementInSequence` | 1..1 | `FareStructureElementInSequenceStructure` |  |  |  |
| `fareStructureElementsInSequence / FareStructureElementInSequence / @id` | 0..1 | `xsd:normalizedString` | `IT:ITC1:FareStructureElementInSequence:busATS:fseis:8` | Id dell’elemento | §5.2.7.2, Tab. 71 |
| `fareStructureElementsInSequence / FareStructureElementInSequence / @version` | 0..1 | `xsd:normalizedString` | `1` | Versione del tag | §5.2.7.2, Tab. 71 |
| `fareStructureElementsInSequence / FareStructureElementInSequence / @order` | 0..1 | `xsd:integer` | `1` | Ordinale | §5.2.7.2, Tab. 71 |
| [`fareStructureElementsInSequence`](#tariffs-tariff-farestructureelements-farestructureelement-farestructureelementsinsequence-farestructureelementinsequence-genericparameterassignment) | 0..1 | `fareStructureElementsInSequence_RelStructure` |  |  |  |

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
    | `TariffBasis` | 0..1 | [`TariffBasisEnumeration`](enumerations.md#tariffbasisenumeration) |
    | `GeographicalIntervalRef` | 0..1 | `GeographicalIntervalRefStructure` |
    | `geographicalIntervals` | 0..1 | `geographicalIntervals_RelStructure` |
    | `TimeIntervalRef` | 0..1 | `TimeIntervalRefStructure` |
    | `timeIntervals` | 0..1 | `timeIntervals_RelStructure` |
    | `DistanceMatrixElementRef` | 0..1 | `DistanceMatrixElementRefStructure` |
    | `distanceMatrixElements` | 0..1 | `distanceMatrixElements_RelStructure` |

##### fareStructureElementsInSequence / FareStructureElementInSequence / GenericParameterAssignment {#tariffs-tariff-farestructureelements-farestructureelement-farestructureelementsinsequence-farestructureelementinsequence-genericparameterassignment}

Linee guida §5.2.7.2 «tariffs», Tabella 71. Tipo dell'XSD `GenericParameterAssignmentStructure`.

| Campo | Cardinalità | Tipo | Esempio | Significato (5T) | Fonte |
|---|---|---|---|---|---|
| `@id` | 0..1 | `xsd:normalizedString` | `IT:ITC1:GenericParameterAssignment:busATS:gpafs:8` | Identificativo [→ Identificazione](common.md#identificazione) | §5.2.7.2, Tab. 71 |
| `@version` | 0..1 | `xsd:normalizedString` | `1` | Versione [→ Identificazione](common.md#identificazione) | §5.2.7.2, Tab. 71 |
| `@order` | 0..1 | `xsd:integer` | `1` | Ordinale | §5.2.7.2, Tab. 71 |
| `limitations` | 0..1 | `usageParameters_RelStructure` |  |  |  |
| `limitations / UserProfileRef` → [UserProfile](#usageparameters-userprofile) | 0..n · scelta 2 | `UserProfileRefStructure` | `IT:ITC1:UserProfile:busATS:up:1` | Limitazioni – riferimento a profilo utente [⚠ Incongruenza](issues.md#71-netex-fareframe-netex-tariffs-netex-tariff-netex-farestructureelements-netex-farestructureelement-netex-farestructureelementsinsequence-netex-farestructureelementinsequence-netex-genericparameterassignment-netex-limitations-netex-userprofileref) | §5.2.7.2, Tab. 71 |
| `limitations / UsageValidityPeriodRef` → [UsageValidityPeriod](#usageparameters-usagevalidityperiod) | 0..n · scelta 1 | `UsageValidityPeriodRefStructure` | `IT:ITC1:UsageValidityPeriod:busATS:uvp:2` | Limitazioni – riferimento a periodo di validità [⚠ Incongruenza](issues.md#71-netex-fareframe-netex-tariffs-netex-tariff-netex-farestructureelements-netex-farestructureelement-netex-farestructureelementsinsequence-netex-farestructureelementinsequence-netex-genericparameterassignment-netex-limitations-netex-usagevalidityperiodref) | §5.2.7.2, Tab. 71 |
| `validityParameters` | 0..1 | `validityParameters_RelStructure` |  |  |  |
| `validityParameters / OperatorRef` → [Operator](resource-frame.md#organisations-operator) | 0..n | `OperatorRefStructure` | `IT:ITC1:Operator:busATS:11` | Riferimento a operatore di validità | §5.2.7.2, Tab. 71 |
| `validityParameters / LineRef` → [Line](service-frame.md#lines-line) | 0..n | `LineRefStructure` | `IT:ITC1:Line:busATS:TO-MI` | Riferimento a linea di validità | §5.2.7.2, Tab. 71 |
| `validityParameters / TariffZoneRef` → [TariffZone](service-frame.md#tariffzones-tariffzone) | 0..n | `TariffZoneRefStructure` | `IT:ITC1:TariffZone:busATS:TZ:3` | Riferimento a zona tariffaria di validità | §5.2.7.2, Tab. 71 |
| `validityParameters / ScheduledStopPointRef` → [ScheduledStopPoint](service-frame.md#scheduledstoppoints-scheduledstoppoint) | 0..n | `ScheduledStopPointRefStructure` | `IT:ITC1:ScheduledStopPoint:busATS:031109` | Riferimento a fermata di validità | §5.2.7.2, Tab. 71 |
| `validityParameters / ServiceJourneyPatternRef` → [ServiceJourneyPattern](service-frame.md#journeypatterns-servicejourneypattern) | 0..n | `ServiceJourneyPatternRefStructure` | `IT:ITC1:ServiceJourneyPattern:busATS:001_01A` | Riferimento a percorso di validità | §5.2.7.2, Tab. 71 |
| `validityParameters / ServiceJourneyRef` → [ServiceJourney](timetable-frame.md#vehiclejourneys-servicejourney) | 0..n | `ServiceJourneyRefStructure` | `IT:ITC1:ServiceJourney:busATS:001_01_01A` | Riferimento a percorso di validità | §5.2.7.2, Tab. 71 |
| `validityParameters / VehicleTypeRef` → [VehicleType](resource-frame.md#vehicletypes-vehicletype) | 0..n · scelta 1 | `VehicleTypeRefStructure` | `IT:ITC1:VehicleType:busATS:001` | Riferimento a tipo veicolo di validità | §5.2.7.2, Tab. 71 |
| `validityParameters / TrainRef` → [Train](resource-frame.md#vehicletypes-train) | 0..n · scelta 1 | `TrainRefStructure` | `IT:ITC1:Train:trenoFS:1` | Riferimento a treno di validità | §5.2.7.2, Tab. 71 |

??? note "Altri campi dell'XSD"

    | Campo | Cardinalità | Tipo |
    |---|---|---|
    | `@nameOfClass` | 0..1 | `xsd:Name` |
    | `@dataSourceRef` | 0..1 | `xsd:normalizedString` |
    | `@created` | 0..1 | `xsd:dateTime` |
    | `@changed` | 0..1 | `xsd:dateTime` |
    | `@modification` | 0..1 | [`ModificationEnumeration`](enumerations.md#modificationenumeration) |
    | `@status` | 0..1 | [`StatusEnumeration`](enumerations.md#statusenumeration) |
    | `TimeIntervalRef` | 0..1 | `TimeIntervalRefStructure` |
    | `GeographicalIntervalRef` | 0..1 | `GeographicalIntervalRefStructure` |

#### distanceMatrixElements / DistanceMatrixElement {#tariffs-tariff-distancematrixelements-distancematrixelement}

Linee guida §5.2.7.2 «tariffs», Tabella 71. Tipo dell'XSD `DistanceMatrixElement_VersionStructure`.

| Campo | Cardinalità | Tipo | Esempio | Significato (5T) | Fonte |
|---|---|---|---|---|---|
| `@id` | 1..1 | `xsd:normalizedString` | `IT:ITC1:DistanceMatrixElement:busATS:dm:1` | Identificativo [→ Identificazione](common.md#identificazione) | §5.2.7.2, Tab. 71 |
| `@version` | 0..1 | `xsd:normalizedString` | `1` | Versione [→ Identificazione](common.md#identificazione) | §5.2.7.2, Tab. 71 |
| `StartTariffZoneRef` | 1..1 | `TariffZoneRefStructure` | `IT:ITC1:TariffZone:busATS:TZ:1` | Riferimento inizio zona tariffaria | §5.2.7.2, Tab. 71 |
| `EndTariffZoneRef` | 1..1 | `TariffZoneRefStructure` | `IT:ITC1:TariffZone:busATS:TZ:2` | Riferimento fine zona tariffaria | §5.2.7.2, Tab. 71 |

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

### validableElements / ValidableElement {#validableelements-validableelement}

Linee guida §5.2.7.3 «validableElements», Tabella 72. Tipo dell'XSD `ValidableElement_VersionStructure`.

| Campo | Cardinalità | Tipo | Esempio | Significato (5T) | Fonte |
|---|---|---|---|---|---|
| `@id` | 1..1 | `xsd:normalizedString` | `IT:ITC1:ValidableElement:busATS:ve:8` | Identificativo [→ Identificazione](common.md#identificazione) | §5.2.7.3, Tab. 72 |
| `@version` | 0..1 | `xsd:normalizedString` | `1` | Versione [→ Identificazione](common.md#identificazione) | §5.2.7.3, Tab. 72 |
| `Name` | 0..1 | `MultilingualString` | `Biglietto urbano` | Nome | §5.2.7.3, Tab. 72 |
| [`fareStructureElements`](#validableelements-validableelement-farestructureelements-farestructureelementref) | 0..1 | `fareStructureElements_RelStructure` |  |  |  |

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

#### fareStructureElements / FareStructureElementRef {#validableelements-validableelement-farestructureelements-farestructureelementref}

Linee guida §5.2.7.3 «validableElements», Tabella 72. Tipo dell'XSD `FareStructureElementRefStructure`.

| Campo | Cardinalità | Tipo | Esempio | Significato (5T) | Fonte |
|---|---|---|---|---|---|
| `@ref` | 1..1 | `xsd:normalizedString` | `IT:ITC1:FareStructureElement:busATS:fse:8` | Id dell’elemento [⚠ Incongruenza](issues.md#72-netex-fareframe-netex-validableelements-netex-validableelement-netex-farestructureelements-netex-farestructureelementref-ref) | §5.2.7.3, Tab. 72 |
| `@version` | 0..1 | `xsd:normalizedString` | `1` | Versione [→ Identificazione](common.md#identificazione) | §5.2.7.3, Tab. 72 |

??? note "Altri campi dell'XSD"

    | Campo | Cardinalità | Tipo |
    |---|---|---|
    | `@nameOfRefClass` | 0..1 | `xsd:Name` |
    | `@created` | 0..1 | `xsd:dateTime` |
    | `@changed` | 0..1 | `xsd:dateTime` |
    | `@modification` | 0..1 | [`ModificationEnumeration`](enumerations.md#modificationenumeration) |
    | `@versionRef` | 0..1 | `xsd:normalizedString` |

### usageParameters / UsageValidityPeriod {#usageparameters-usagevalidityperiod}

Linee guida §5.2.7.4 «usageParameters», Tabella 73. Tipo dell'XSD `UsageValidityPeriod_VersionStructure`.

| Campo | Cardinalità | Tipo | Esempio | Significato (5T) | Fonte |
|---|---|---|---|---|---|
| `@id` | 1..1 | `xsd:normalizedString` | `IT:ITC1:UsageValidityPeriod:busATS:uvp:1` | Identificativo [→ Identificazione](common.md#identificazione) | §5.2.7.4, Tab. 73 |
| `@version` | 0..1 | `xsd:normalizedString` | `1` | Versione [→ Identificazione](common.md#identificazione) | §5.2.7.4, Tab. 73 |
| `ValidityPeriodType` | 0..1 | [`UsageValidityTypeEnumeration`](enumerations.md#usagevaliditytypeenumeration) | `singleRide` | Tipo di periodo di validità | §5.2.7.4, Tab. 73 |
| `StandardDuration` | 0..1 | `xsd:duration` | `PT90M` | Durata della validità | §5.2.7.4, Tab. 73 |
| `StartDate` | 0..1 | `xsd:date` | `2025-01-01` | Data inizio validità | §5.2.7.4, Tab. 73 |
| `StartTime` | 0..1 | `xsd:time` | `00:00:00` | Ora inizio validità | §5.2.7.4, Tab. 73 |
| `EndDate` | 0..1 | `xsd:date` | `2025-12-31` | Data fine validità | §5.2.7.4, Tab. 73 |
| `EndTime` | 0..1 | `xsd:time` | `23:59:59` | Ora fine validità | §5.2.7.4, Tab. 73 |
| `startOnlyOn` | 0..1 |  |  | Struttura specifica per i parcheggi [⚠ Incongruenza](issues.md#73-netex-fareframe-netex-usageparameters-netex-usagevalidityperiod-netex-startonlyon) | §5.2.7.4, Tab. 73 |
| `startOnlyOn / DayTypeRef` → [DayType](service-calendar-frame.md#servicecalendar-daytypes-daytype) | 1..1 | `DayTypeRefStructure` | `T:ITC1:DayType:parcheggiARaso:annuale123456` | Calendario di apertura dei parcheggi | §5.2.7.4, Tab. 73 |

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

### usageParameters / UserProfile {#usageparameters-userprofile}

Linee guida §5.2.7.4 «usageParameters», Tabella 73. Tipo dell'XSD `UserProfile_VersionStructure`.

| Campo | Cardinalità | Tipo | Esempio | Significato (5T) | Fonte |
|---|---|---|---|---|---|
| `@id` | 1..1 | `xsd:normalizedString` | `IT:ITC1:UserProfile:busATS:up:1` | Identificativo [→ Identificazione](common.md#identificazione) | §5.2.7.4, Tab. 73 |
| `@version` | 0..1 | `xsd:normalizedString` | `1` | Versione [→ Identificazione](common.md#identificazione) | §5.2.7.4, Tab. 73 |
| `UserType` | 0..1 | [`UserTypeEnumeration`](enumerations.md#usertypeenumeration) | `JobSeeker` | Tipo utente [⚠ Incongruenza](issues.md#73-netex-fareframe-netex-usageparameters-netex-userprofile-netex-usertype) | §5.2.7.4, Tab. 73 |
| `MinimumAge` | 0..1 | `xsd:integer` | `11` | Età minima utente | §5.2.7.4, Tab. 73 |
| `MaximumAge` | 0..1 | `xsd:integer` | `65` | Età massima utente | §5.2.7.4, Tab. 73 |

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
    | `MonthDayOnWhichAgeApplies` | 0..1 | `xsd:gMonthDay` |
    | `MinimumHeight` | 0..1 | `LengthType` |
    | `MaximumHeight` | 0..1 | `LengthType` |
    | `LocalResident` | 0..1 | `xsd:boolean` |

### fareProducts / PreassignedFareProduct {#fareproducts-preassignedfareproduct}

Linee guida §5.2.7.5 «fareProducts», Tabella 74. Tipo dell'XSD `PreassignedFareProductL4_VersionStructure`.

| Campo | Cardinalità | Tipo | Esempio | Significato (5T) | Fonte |
|---|---|---|---|---|---|
| `@id` | 1..1 | `xsd:normalizedString` | `IT:ITC1:PreassignedFareProduct:busATS:pfp:1+8` | Identificativo [→ Identificazione](common.md#identificazione) | §5.2.7.5, Tab. 74 |
| `@version` | 0..1 | `xsd:normalizedString` | `1` | Versione [→ Identificazione](common.md#identificazione) | §5.2.7.5, Tab. 74 |
| [`ValidBetween`](common.md#validbetween) | 0..1 | `ValidBetween_VersionStructure` |  |  |  |
| `Name` | 0..1 | `MultilingualString` | `Tariffa parcheggio+corsa urbana` | Nome prodotto tariffario | §5.2.7.5, Tab. 74 |
| `Description` | 0..1 | `MultilingualString` | `Tariffa parcheggio` | Descrizione prodotto tariffario | §5.2.7.5, Tab. 74 |
| `ChargingMomentType` | 0..1 | [`ChargingMomentEnumeration`](enumerations.md#chargingmomentenumeration) | `atEndOfChargePeriod` | Tipologia ChargingMoment [⚠ Incongruenza](issues.md#74-netex-fareframe-netex-fareproducts-netex-preassignedfareproduct-netex-chargingmomenttype) | §5.2.7.5, Tab. 74 |
| [`validityParameterAssignments`](#fareproducts-preassignedfareproduct-validityparameterassignments-genericparameterassignment) | 0..1 | `validityParameterAssignmentsL4_RelStructure` |  |  |  |
| `validableElements` | 0..1 | `validableElements_RelStructure` |  |  |  |
| `validableElements / ValidableElementRef` → [ValidableElement](#validableelements-validableelement) | 0..n · scelta 1 | `ValidableElementRefStructure` | `IT:ITC1:ValidableElement:busATS:ve:1` | Riferimento al validable Element [⚠ Incongruenza](issues.md#74-netex-fareframe-netex-fareproducts-netex-preassignedfareproduct-netex-validableelements-netex-validableelementref) | §5.2.7.5, Tab. 74 |
| `tariffs` | 0..1 | `tariffRefs_RelStructure` |  |  |  |
| `tariffs / ParkingTariffRef` → [ParkingTariff](#parkingtariffs-parkingtariff) | 1..1 | `ParkingTariffRefStructure` | `IT:ITC1:ParkingTariff:parcheggiTorino:pt:1a` | Riferimento alla tariffa del parcheggio | §5.2.7.5, Tab. 74 |

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

#### validityParameterAssignments / GenericParameterAssignment {#fareproducts-preassignedfareproduct-validityparameterassignments-genericparameterassignment}

Linee guida §5.2.7.5 «fareProducts», Tabella 74. Tipo dell'XSD `GenericParameterAssignmentL4Structure`.

| Campo | Cardinalità | Tipo | Esempio | Significato (5T) | Fonte |
|---|---|---|---|---|---|
| `@id` | 0..1 | `xsd:normalizedString` | `IT:ITC1:GenericParameterAssignment:busATS:gpa:2b` | Identificativo [→ Identificazione](common.md#identificazione) | §5.2.7.5, Tab. 74 |
| `@order` | 0..1 | `xsd:integer` | `1` | Ordinale del tag | §5.2.7.5, Tab. 74 |
| `@version` | 0..1 | `xsd:normalizedString` | `1` | Versione [→ Identificazione](common.md#identificazione) | §5.2.7.5, Tab. 74 |
| `limitations` | 0..1 | `usageParameters_RelStructure` |  |  |  |
| `limitations / UsageValidityPeriodRef` → [UsageValidityPeriod](#usageparameters-usagevalidityperiod) | 0..n · scelta 1 | `UsageValidityPeriodRefStructure` | `IT:ITC1:UsageValidityPeriod:busATS:uvp:1` | Riferimento al periodo di validità | §5.2.7.5, Tab. 74 |
| `limitations / UserProfileRef` → [UserProfile](#usageparameters-userprofile) | 0..n · scelta 2 | `UserProfileRefStructure` | `IT:ITC1:UserProfile:busATS:up:1` | Riferimento al profilo utente | §5.2.7.5, Tab. 74 |
| `validityParameters` | 0..1 | `validityParametersL4_RelStructure` |  |  |  |
| `validityParameters / OperatorRef` → [Operator](resource-frame.md#organisations-operator) | 0..n | `OperatorRefStructure` | `IT:ITC1:Operator:busATS:11` | Riferimento all’operatore | §5.2.7.5, Tab. 74 |
| `validityParameters / TariffZoneRef` → [TariffZone](service-frame.md#tariffzones-tariffzone) | 0..n | `TariffZoneRefStructure` | `IT:ITC1:TariffZone:busATS:TZ:1` | Riferimento alla zona tariffaria | §5.2.7.5, Tab. 74 |
| `validityParameters / TrainRef` → [Train](resource-frame.md#vehicletypes-train) | 0..n · scelta 1 | `TrainRefStructure` | `IT:ITC1:Train:metroATMMILANO:LEONARDO` | Riferimento al treno | §5.2.7.5, Tab. 74 |
| `TimeIntervalRef` → [TimeInterval](#tariffs-tariff-timeintervals-timeinterval) | 0..1 | `TimeIntervalRefStructure` | `IT:ITC1:TimeInterval:busATS:ti:1` | Riferimento all’intervallo temporale | §5.2.7.5, Tab. 74 |

??? note "Altri campi dell'XSD"

    | Campo | Cardinalità | Tipo |
    |---|---|---|
    | `@nameOfClass` | 0..1 | `xsd:Name` |
    | `@dataSourceRef` | 0..1 | `xsd:normalizedString` |
    | `@created` | 0..1 | `xsd:dateTime` |
    | `@changed` | 0..1 | `xsd:dateTime` |
    | `@modification` | 0..1 | [`ModificationEnumeration`](enumerations.md#modificationenumeration) |
    | `@status` | 0..1 | [`StatusEnumeration`](enumerations.md#statusenumeration) |
    | `GeographicalIntervalRef` | 0..1 | `GeographicalIntervalRefStructure` |

### fareTables / FareTable {#faretables-faretable}

Linee guida §5.2.7.6 «fareTables», Tabella 75. Tipo dell'XSD `FareTable_VersionStructure`.

| Campo | Cardinalità | Tipo | Esempio | Significato (5T) | Fonte |
|---|---|---|---|---|---|
| `@id` | 1..1 | `xsd:normalizedString` | `IT:ITC1:FareTable:busATS:ft:1` | Identificativo [→ Identificazione](common.md#identificazione) | §5.2.7.6, Tab. 75 |
| `@version` | 0..1 | `xsd:normalizedString` | `1` | Versione [→ Identificazione](common.md#identificazione) | §5.2.7.6, Tab. 75 |
| [`prices`](#faretables-faretable-prices-farestructureelementprice) | 0..1 | `fareStructureElementPrices_RelStructure` |  |  |  |
| `prices / DistanceMatrixElementPriceRef` | 0..n · scelta 3 | `DistanceMatrixElementPriceRefStructure` | `IT:ITC1:DistanceMatrixElement:busATS:dm:1` | Riferimento al DistanceMatrixElementPrice | §5.2.7.6, Tab. 75 |
| [`prices`](#faretables-faretable-prices-geographicalintervalprice) | 0..1 | `fareStructureElementPrices_RelStructure` |  |  |  |

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

#### prices / FareStructureElementPrice {#faretables-faretable-prices-farestructureelementprice}

Linee guida §5.2.7.6 «fareTables», Tabella 75. Tipo dell'XSD `FareStructureElementPrice_VersionStructure`.

| Campo | Cardinalità | Tipo | Esempio | Significato (5T) | Fonte |
|---|---|---|---|---|---|
| `@id` | 1..1 | `xsd:normalizedString` | `IT:ITC1:FareStructureElementPrice:busATS:cep:8` | Identificativo [→ Identificazione](common.md#identificazione) | §5.2.7.6, Tab. 75 (occorrenza 2) |
| `@version` | 0..1 | `xsd:normalizedString` | `1` | Versione [→ Identificazione](common.md#identificazione) | §5.2.7.6, Tab. 75 (occorrenza 2) |
| `Amount` | 0..1 | `xsd:decimal` | `1.70` | Costo tariffa | §5.2.7.6, Tab. 75 |
| `Currency` | 0..1 | `CurrencyType` | `EUR` | Valuta | §5.2.7.6, Tab. 75 |
| `CanBeCumulative` | 0..1 | `xsd:boolean` | `false` | Cumulabilità del titolo | §5.2.7.6, Tab. 75 |
| `FareStructureElementRef` → [FareStructureElement](#tariffs-tariff-farestructureelements-farestructureelement) | 0..1 | `FareStructureElementRefStructure` | `IT:ITC1:FareStructureElement:busATS:fse:8` | Riferimento al FareStructureElement | §5.2.7.6, Tab. 75 |

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
    | `Name` | 0..1 | `MultilingualString` |
    | `Description` | 0..1 | `MultilingualString` |

#### prices / GeographicalIntervalPrice {#faretables-faretable-prices-geographicalintervalprice}

Linee guida §5.2.7.6 «fareTables», Tabella 75. Tipo dell'XSD `GeographicalIntervalPrice_VersionStructure`.

| Campo | Cardinalità | Tipo | Esempio | Significato (5T) | Fonte |
|---|---|---|---|---|---|
| `GeographicalIntervalRef` → [GeographicalInterval](#tariffs-tariff-geographicalintervals-geographicalinterval) | 0..1 | `GeographicalIntervalRefStructure` | `IT:ITC1:GeographicalInterval:busATS:gi:0-5` | Riferimento al GeographicalInterval | §5.2.7.6, Tab. 75 |

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
    | `Description` | 0..1 | `MultilingualString` |
    | `Amount` | 0..1 | `xsd:decimal` |
    | `Currency` | 0..1 | `CurrencyType` |
    | `CanBeCumulative` | 0..1 | `xsd:boolean` |

### distributionChannels / DistributionChannel {#distributionchannels-distributionchannel}

Linee guida §5.2.7.7 «distributionChannels», Tabella 76. Tipo dell'XSD `DistributionChannel_VersionStructure`.

| Campo | Cardinalità | Tipo | Esempio | Significato (5T) | Fonte |
|---|---|---|---|---|---|
| `@id` | 1..1 | `xsd:normalizedString` | `IT:ITC1:DistributionChannel:busATS:dc:1` | Identificativo [→ Identificazione](common.md#identificazione) | §5.2.7.7, Tab. 76 |
| `@version` | 0..1 | `xsd:normalizedString` | `1` | Versione [→ Identificazione](common.md#identificazione) | §5.2.7.7, Tab. 76 |
| `Name` | 0..1 | `MultilingualString` | `Rete di vendita ATS` | Nome canale di distribuzione | §5.2.7.7, Tab. 76 |
| `Description` | 0..1 | `MultilingualString` | `Dettagli rete di vendita ATS` | Descrizione canale di distribuzione | §5.2.7.7, Tab. 76 |
| `DistributionChannelType` | 0..1 | [`DistributionChannelTypeEnumeration`](enumerations.md#distributionchanneltypeenumeration) | `agency` | Tipo canale di distribuzione | §5.2.7.7, Tab. 76 |
| `TravelAgentRef` → [TravelAgent](resource-frame.md#organisations-travelagent) | 0..n · scelta 1 | `TravelAgentRefStructure` | `IT:ITC1:TravelAgent:busATS:11` | Id travel agent | §5.2.7.7, Tab. 76 |
| `PaymentMethods` | 0..1 | [`PaymentMethodListOfEnumerations`](enumerations.md#paymentmethodlistofenumerations) | `cashAndCard` | Metodi di pagamento accettati | §5.2.7.7, Tab. 76 |

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
    | `OperatorRef` | 0..n | `OperatorRefStructure` |

### typesOfTravelDocuments / TypeOfTravelDocument {#typesoftraveldocuments-typeoftraveldocument}

Linee guida §5.2.7.8 «typesOfTravelDocuments», Tabella 77. Tipo dell'XSD `TypeOfTravelDocument_VersionStructure`.

| Campo | Cardinalità | Tipo | Esempio | Significato (5T) | Fonte |
|---|---|---|---|---|---|
| `@id` | 1..1 | `xsd:normalizedString` | `IT:ITC1:TypeOfTravelDocument:busATS:ttd:1` | Identificativo [→ Identificazione](common.md#identificazione) | §5.2.7.8, Tab. 77 |
| `@version` | 0..1 | `xsd:normalizedString` | `1` | Versione [→ Identificazione](common.md#identificazione) | §5.2.7.8, Tab. 77 |
| `HasPhoto` | 0..1 | `xsd:boolean` | `true` | Presenza fotografia | §5.2.7.8, Tab. 77 |
| `MediaType` | 0..1 | [`MediaTypeEnumeration`](enumerations.md#mediatypeenumeration) | `card` | Tipo di media Valori del profilo: `none`, `paperTicket`, `coupon`, `selfPrintPaperTicket`, `smartCard`, `mobileApp`, `licencePlate`, `card`, `mms`, `sms`, `other`. [⚠ Incongruenza](issues.md#77-netex-fareframe-netex-typesoftraveldocuments-netex-typeoftraveldocument-netex-mediatype) | §5.2.7.8, Tab. 77 |
| `MachineReadable` | 0..1 | [`MachineReadableListOfEnumerations`](enumerations.md#machinereadablelistofenumerations) | `chip` | Dettaglio media | §5.2.7.8, Tab. 77 |

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
    | `IsCard` | 0..1 | `xsd:boolean` |
    | `IsSmartCard` | 0..1 | `xsd:boolean` |

### salesOfferPackages / SalesOfferPackage {#salesofferpackages-salesofferpackage}

Linee guida §5.2.7.9 «salesOfferPackages», Tabella 78. Tipo dell'XSD `SalesOfferPackage_VersionStructure`.

| Campo | Cardinalità | Tipo | Esempio | Significato (5T) | Fonte |
|---|---|---|---|---|---|
| `@id` | 1..1 | `xsd:normalizedString` | `IT:ITC1:SalesOfferPackage:busATS:sop:1` | Identificativo [→ Identificazione](common.md#identificazione) | §5.2.7.9, Tab. 78 |
| `@version` | 0..1 | `xsd:normalizedString` | `1` | Versione [→ Identificazione](common.md#identificazione) | §5.2.7.9, Tab. 78 |
| [`distributionAssignments`](#salesofferpackages-salesofferpackage-distributionassignments-distributionassignment) | 0..1 | `distributionAssignments_RelStructure` |  |  |  |
| [`salesOfferPackageElements`](#salesofferpackages-salesofferpackage-salesofferpackageelements-salesofferpackageelement) | 0..1 | `salesOfferPackageElements_RelStructure` |  |  |  |

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

#### distributionAssignments / DistributionAssignment {#salesofferpackages-salesofferpackage-distributionassignments-distributionassignment}

Linee guida §5.2.7.9 «salesOfferPackages», Tabella 78. Tipo dell'XSD `DistributionAssignment_VersionStructure`.

| Campo | Cardinalità | Tipo | Esempio | Significato (5T) | Fonte |
|---|---|---|---|---|---|
| `@id` | 0..1 | `xsd:normalizedString` | `IT:ITC1:DistributionAssignment:busATS:da:1` | Identificativo [→ Identificazione](common.md#identificazione) | §5.2.7.9, Tab. 78 |
| `@version` | 0..1 | `xsd:normalizedString` | `1` | Versione [→ Identificazione](common.md#identificazione) | §5.2.7.9, Tab. 78 |
| `@order` | 0..1 | `xsd:integer` | `1` | Ordinale dell’elemento | §5.2.7.9, Tab. 78 |
| `DistributionChannelRef` → [DistributionChannel](#distributionchannels-distributionchannel) | 1..1 | `DistributionChannelRefStructure` | `IT:ITC1:DistributionChannel:busATS:dc:1` | Riferimento a canale di distribuzione | §5.2.7.9, Tab. 78 |

??? note "Altri campi dell'XSD"

    | Campo | Cardinalità | Tipo |
    |---|---|---|
    | `@nameOfClass` | 0..1 | `xsd:Name` |
    | `@dataSourceRef` | 0..1 | `xsd:normalizedString` |
    | `@created` | 0..1 | `xsd:dateTime` |
    | `@changed` | 0..1 | `xsd:dateTime` |
    | `@modification` | 0..1 | [`ModificationEnumeration`](enumerations.md#modificationenumeration) |
    | `@status` | 0..1 | [`StatusEnumeration`](enumerations.md#statusenumeration) |

#### salesOfferPackageElements / SalesOfferPackageElement {#salesofferpackages-salesofferpackage-salesofferpackageelements-salesofferpackageelement}

Linee guida §5.2.7.9 «salesOfferPackages», Tabella 78. Tipo dell'XSD `SalesOfferPackageElement_VersionStructure`.

| Campo | Cardinalità | Tipo | Esempio | Significato (5T) | Fonte |
|---|---|---|---|---|---|
| `@id` | 0..1 | `xsd:normalizedString` | `IT:ITC1:SalesOfferPackageElement:busATS:sope:1` | Identificativo [→ Identificazione](common.md#identificazione) | §5.2.7.9, Tab. 78 |
| `@version` | 0..1 | `xsd:normalizedString` | `1` | Versione [→ Identificazione](common.md#identificazione) | §5.2.7.9, Tab. 78 |
| `@order` | 0..1 | `xsd:integer` | `1` | Ordinale dell’elemento | §5.2.7.9, Tab. 78 |
| `fareTables` | 0..1 | `fareTables_RelStructure` |  |  |  |
| `fareTables / FareTableRef` → [FareTable](#faretables-faretable) | 0..n · scelta 1 | `FareTableRefStructure` | `IT:ITC1:FareTable:busATS:ft:1` | Riferimento al FareTable | §5.2.7.9, Tab. 78 |
| `TypeOfTravelDocumentRef` → [TypeOfTravelDocument](#typesoftraveldocuments-typeoftraveldocument) | 0..1 | `TypeOfTravelDocumentRefStructure` | `IT:ITC1:TypeOfTravelDocument:busATS:ttd:1` | Riferimento al tipo di biglietto | §5.2.7.9, Tab. 78 |
| `FareProductRef` | 0..1 | `PreassignedFareProductRefStructure` | `IT:ITC1:PreassignedFareProduct:busATS:pfp:1` | Riferimento al prodotto tariffario | §5.2.7.9, Tab. 78 |
| [`prices`](#salesofferpackages-salesofferpackage-salesofferpackageelements-salesofferpackageelement-prices-salesofferpackageprice) | 0..1 | `salesOfferPackagePrices_RelStructure` |  |  |  |

??? note "Altri campi dell'XSD"

    | Campo | Cardinalità | Tipo |
    |---|---|---|
    | `@nameOfClass` | 0..1 | `xsd:Name` |
    | `@dataSourceRef` | 0..1 | `xsd:normalizedString` |
    | `@created` | 0..1 | `xsd:dateTime` |
    | `@changed` | 0..1 | `xsd:dateTime` |
    | `@modification` | 0..1 | [`ModificationEnumeration`](enumerations.md#modificationenumeration) |
    | `@status` | 0..1 | [`StatusEnumeration`](enumerations.md#statusenumeration) |

##### prices / SalesOfferPackagePrice {#salesofferpackages-salesofferpackage-salesofferpackageelements-salesofferpackageelement-prices-salesofferpackageprice}

Linee guida §5.2.7.9 «salesOfferPackages», Tabella 78. Tipo dell'XSD `SalesOfferPackagePrice_VersionStructure`.

| Campo | Cardinalità | Tipo | Esempio | Significato (5T) | Fonte |
|---|---|---|---|---|---|
| `@id` | 1..1 | `xsd:normalizedString` | `IT:ITC1:SalesOfferPackagePrice:busATS:sopp:1a` | Identificativo [→ Identificazione](common.md#identificazione) | §5.2.7.9, Tab. 78 |
| `@version` | 0..1 | `xsd:normalizedString` | `1` | Versione [→ Identificazione](common.md#identificazione) | §5.2.7.9, Tab. 78 |
| [`PricingRule`](#salesofferpackages-salesofferpackage-salesofferpackageelements-salesofferpackageelement-prices-salesofferpackageprice-pricingrule) | 0..1 · scelta 1 | `PricingRule_VersionStructure` |  |  |  |
| [`DiscountingRule`](#salesofferpackages-salesofferpackage-salesofferpackageelements-salesofferpackageelement-prices-salesofferpackageprice-discountingrule) | 0..1 · scelta 1 | `DiscountingRule_VersionStructure` |  |  |  |

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
    | `CappingRulePriceRef` | 0..1 | `CappingRulePriceRefStructure` |
    | `PricingRuleRef` | 0..1 | `PricingRuleRefStructure` |
    | `DiscountingRuleRef` | 0..1 | `DiscountingRuleRefStructure` |

###### PricingRule {#salesofferpackages-salesofferpackage-salesofferpackageelements-salesofferpackageelement-prices-salesofferpackageprice-pricingrule}

Linee guida §5.2.7.9 «salesOfferPackages», Tabella 78. Tipo dell'XSD `PricingRule_VersionStructure`.

| Campo | Cardinalità | Tipo | Esempio | Significato (5T) | Fonte |
|---|---|---|---|---|---|
| `@id` | 1..1 | `xsd:normalizedString` | `IT:ITC1:PricingRule:busATS:sopp:pr1a` | Identificativo [→ Identificazione](common.md#identificazione) | §5.2.7.9, Tab. 78 |
| `@version` | 0..1 | `xsd:normalizedString` | `1` | Versione [→ Identificazione](common.md#identificazione) | §5.2.7.9, Tab. 78 |
| `Factor` | 0..1 | `xsd:decimal` | `1` | Fattore moltiplicativo della tariffa | §5.2.7.9, Tab. 78 |

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
    | `Name` | 0..1 | `MultilingualString` |
    | `Description` | 0..1 | `MultilingualString` |

###### DiscountingRule {#salesofferpackages-salesofferpackage-salesofferpackageelements-salesofferpackageelement-prices-salesofferpackageprice-discountingrule}

Linee guida §5.2.7.9 «salesOfferPackages», Tabella 78. Tipo dell'XSD `DiscountingRule_VersionStructure`.

| Campo | Cardinalità | Tipo | Esempio | Significato (5T) | Fonte |
|---|---|---|---|---|---|
| `@id` | 1..1 | `xsd:normalizedString` | `IT:ITC1:PricingRule:busATS:sopp:pr1a` | Identificativo [→ Identificazione](common.md#identificazione) | §5.2.7.9, Tab. 78 |
| `@version` | 0..1 | `xsd:normalizedString` | `1` | Versione [→ Identificazione](common.md#identificazione) | §5.2.7.9, Tab. 78 |
| `Factor` | 0..1 | `xsd:decimal` | `1` | Fattore moltiplicativo della tariffa | §5.2.7.9, Tab. 78 (occorrenza 2) |
| `DiscountAsPercentage` | 0..1 | `xsd:decimal` |  | Percentuale di sconto [⚠ Incongruenza](issues.md#78-netex-fareframe-netex-salesofferpackages-netex-salesofferpackage-netex-salesofferpackageelements-netex-salesofferpackageelement-netex-prices-netex-salesofferpackageprice-netex-discountingrule-netex-discountaspercentage) | §5.2.7.9, Tab. 78 |

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
    | `Name` | 0..1 | `MultilingualString` |
    | `Description` | 0..1 | `MultilingualString` |
    | `DiscountAsValue` | 0..1 | `xsd:decimal` |
    | `CanBeCumulative` | 0..1 | `xsd:boolean` |

### parkingTariffs / ParkingTariff {#parkingtariffs-parkingtariff}

Linee guida §5.2.7.10 «parkingTariffs», Tabella 79. Tipo dell'XSD `ParkingTariff_VersionStructure`.

| Campo | Cardinalità | Tipo | Esempio | Significato (5T) | Fonte |
|---|---|---|---|---|---|
| `@id` | 1..1 | `xsd:normalizedString` | `IT:ITC1:ParkingTariff:parcheggiTorino:pt:1a` | Identificativo [→ Identificazione](common.md#identificazione) | §5.2.7.10, Tab. 79 |
| `@version` | 0..1 | `xsd:normalizedString` | `1` | Versione [→ Identificazione](common.md#identificazione) | §5.2.7.10, Tab. 79 |
| [`ValidBetween`](common.md#validbetween) | 0..1 | `ValidBetween_VersionStructure` |  |  |  |
| `OperatorRef` → [Operator](resource-frame.md#organisations-operator) | 0..1 | `OperatorRefStructure` |  |  |  |
| `OperatorRef / @ref` → [Operator](resource-frame.md#organisations-operator) | 1..1 | `xsd:normalizedString` | `IT:ITC1:Operator:parcheggiTorino:parcheggiTorino` | Riferimento operatore | §5.2.7.10, Tab. 79 |
| `OperatorRef / @version` → [Operator](resource-frame.md#organisations-operator) | 0..1 | `xsd:normalizedString` | `1` | Versione del tag | §5.2.7.10, Tab. 79 |
| [`timeIntervals`](#parkingtariffs-parkingtariff-timeintervals-timeintervalref) | 0..1 | `timeIntervals_RelStructure` |  |  |  |
| `ParkingStayType` | 0..1 | [`ParkingStayEnumeration`](enumerations.md#parkingstayenumeration) | `midTerm` | Tipologia permanenza | §5.2.7.10, Tab. 79 |
| [`appliesTo`](#parkingtariffs-parkingtariff-appliesto-parkingref) | 0..1 | `parkingRefs_RelStructure` |  |  |  |

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
    | `ParkingUserType` | 0..1 | [`ParkingUserEnumeration`](enumerations.md#parkinguserenumeration) |
    | `ParkingVehicleTypes` | 0..1 | [`ParkingVehicleListOfEnumerations`](enumerations.md#parkingvehiclelistofenumerations) |
    | `parkingChargeBands` | 0..1 | `parkingChargeBands_RelStructure` |

#### timeIntervals / TimeIntervalRef {#parkingtariffs-parkingtariff-timeintervals-timeintervalref}

Linee guida §5.2.7.10 «parkingTariffs», Tabella 79. Tipo dell'XSD `TimeIntervalRefStructure`.

| Campo | Cardinalità | Tipo | Esempio | Significato (5T) | Fonte |
|---|---|---|---|---|---|
| `@ref` | 1..1 | `xsd:normalizedString` | `IT:ITC1:TimeInterval:parcheggiTorino:ti:1min` | Riferimento intervallo temporale | §5.2.7.10, Tab. 79 |
| `@version` | 0..1 | `xsd:normalizedString` | `1` | Versione [→ Identificazione](common.md#identificazione) | §5.2.7.10, Tab. 79 |

??? note "Altri campi dell'XSD"

    | Campo | Cardinalità | Tipo |
    |---|---|---|
    | `@nameOfRefClass` | 0..1 | `xsd:Name` |
    | `@created` | 0..1 | `xsd:dateTime` |
    | `@changed` | 0..1 | `xsd:dateTime` |
    | `@modification` | 0..1 | [`ModificationEnumeration`](enumerations.md#modificationenumeration) |
    | `@versionRef` | 0..1 | `xsd:normalizedString` |

#### appliesTo / ParkingRef {#parkingtariffs-parkingtariff-appliesto-parkingref}

Linee guida §5.2.7.10 «parkingTariffs», Tabella 79. Tipo dell'XSD `ParkingRefStructure`.

| Campo | Cardinalità | Tipo | Esempio | Significato (5T) | Fonte |
|---|---|---|---|---|---|
| `@ref` | 1..1 | `xsd:normalizedString` | `IT:ITC1:Parking:parcheggiTorino:p:Porta_Nuova` | Riferimento al parcheggio | §5.2.7.10, Tab. 79 |
| `@version` | 0..1 | `xsd:normalizedString` | `1` | Versione [→ Identificazione](common.md#identificazione) | §5.2.7.10, Tab. 79 |

??? note "Altri campi dell'XSD"

    | Campo | Cardinalità | Tipo |
    |---|---|---|
    | `@nameOfRefClass` | 0..1 | `xsd:Name` |
    | `@created` | 0..1 | `xsd:dateTime` |
    | `@changed` | 0..1 | `xsd:dateTime` |
    | `@modification` | 0..1 | [`ModificationEnumeration`](enumerations.md#modificationenumeration) |
    | `@versionRef` | 0..1 | `xsd:normalizedString` |
