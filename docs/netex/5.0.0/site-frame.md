---
generato: true
generato_da: rpsd-tools 0.6.0
---
<!-- GENERATED — DO NOT EDIT · profile-docs netex-it · netex-it-lev5@cecb0cd -->

# SiteFrame

Luoghi, fermate e parcheggi (linee guida §5.2.4).

## SiteFrame {#siteframe}

Linee guida §5.2.4 «SiteFrame», Tabella 41. Tipo dell'XSD `SiteFrameL5_VersionStructure`.

| Campo | Cardinalità | Tipo | Esempio | Significato (5T) | Fonte |
|---|---|---|---|---|---|
| `@id` | 1..1 | `xsd:normalizedString` | `epd:IT:ITC1:SiteFrame_EU_PI_STOP:ita` | Identificativo [→ Identificazione](common.md#identificazione) | §5.2.4, Tab. 41 |
| `@version` | 0..1 | `xsd:normalizedString` | `1` | Versione [→ Identificazione](common.md#identificazione) | §5.2.4, Tab. 41 |
| [`TypeOfFrameRef`](common.md#typeofframeref) | 0..1 | `TypeOfFrameRefStructure` |  |  |  |
| [`topographicPlaces`](#topographicplaces-topographicplace) | 0..1 | `topographicPlaces_RelStructure` |  |  |  |
| [`stopPlaces`](#stopplaces-stopplace) | 0..1 | `stopPlacesL5_RelStructure` |  |  |  |
| [`parkings`](#parkings-parking) | 0..1 | `parkingsL2_RelStructure` |  |  |  |

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
    | `groupsOfStopPlaces` | 0..1 | `groupsOfStopPlaces_RelStructure` |
    | `pointsOfInterest` | 0..1 | `pointsOfInterest_RelStructure` |
    | `tariffZones` | 0..1 | `tariffZonesStructure` |

### topographicPlaces / TopographicPlace {#topographicplaces-topographicplace}

Linee guida §5.2.4.1 «topographicPlaces», Tabella 42. Tipo dell'XSD `TopographicPlace_VersionStructure`.

| Campo | Cardinalità | Tipo | Esempio | Significato (5T) | Fonte |
|---|---|---|---|---|---|
| `@id` | 1..1 | `xsd:normalizedString` | `IT:ITC1:TopographicPlace:trenoFS:milanocentrale` | Identificativo [→ Identificazione](common.md#identificazione) | §5.2.4.1, Tab. 42 |
| `@version` | 0..1 | `xsd:normalizedString` | `1` | Versione [→ Identificazione](common.md#identificazione) | §5.2.4.1, Tab. 42 |
| `Descriptor` | 1..1 | `TopographicPlaceDescriptor_VersionedChildStructure` |  |  |  |
| `Descriptor / Name` | 1..1 | `MultilingualString` | `MILANO CENTRALE F.S.` | Nome completo dello topographicPlace | §5.2.4.1, Tab. 42 |

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
    | `ShortName` | 0..1 | `MultilingualString` |
    | `Description` | 0..1 | `MultilingualString` |
    | `PurposeOfGroupingRef` | 0..1 | `PurposeOfGroupingRefStructure` |
    | `PrivateCode` | 0..1 | `PrivateCodeStructure` |
    | `members` | 0..1 | `PlaceObjectMembers` |
    | `Centroid` | 0..1 | `CentroidStructure` |
    | `gml:Polygon` | 0..1 | `gml:T_Polygon` |
    | `placeTypes` | 0..1 | `placeTypes_Structure` |
    | `IsoCode` | 0..1 | `xsd:string` |
    | `TopographicPlaceType` | 0..1 | [`TopographicPlaceTypeEnumeration`](enumerations.md#topographicplacetypeenumeration) |
    | `PostCode` | 0..1 | `xsd:normalizedString` |
    | `CountryRef` | 0..1 | `CountryRefStructure` |
    | `otherCountries` | 0..1 | `otherCountries_RelStructure` |
    | `ParentTopographicPlaceRef` | 0..1 | `ParentTopographicPlaceRefStructure` |
    | `containedIn` | 0..1 | `containedIn_RelStructure` |

### stopPlaces / StopPlace {#stopplaces-stopplace}

Linee guida §5.2.4.2 «stopPlaces», Tabella 43. Tipo dell'XSD `StopPlaceL5_VersionStructure`.

| Campo | Cardinalità | Tipo | Esempio | Significato (5T) | Fonte |
|---|---|---|---|---|---|
| `@id` | 1..1 | `xsd:normalizedString` | `IT:ITC1:StopPlace:busATS:001` | Identificativo [→ Identificazione](common.md#identificazione) | §5.2.4.2, Tab. 43 |
| `@version` | 0..1 | `xsd:normalizedString` | `1` | Versione [→ Identificazione](common.md#identificazione) [⚠ Incongruenza](issues.md#43-netex-siteframe-netex-stopplaces-netex-stopplace-version) | §5.2.4.2, Tab. 43 |
| `Name` | 0..1 | `MultilingualString` | `Terminal Torino Corso Bolzano` | Nome completo dello stop place | §5.2.4.2, Tab. 43 |
| `ShortName` | 0..1 | `MultilingualString` | `Torino Corso Bolzano` | Nome breve dello stop place | §5.2.4.2, Tab. 43 |
| `PrivateCode` | 0..1 | `PrivateCodeStructure` | `001` | Identificativo univoco dello stop place | §5.2.4.2, Tab. 43 |
| `Centroid` | 0..1 | `CentroidStructure` |  | Posizione dello StopPlace | §5.2.4.2, Tab. 43 |
| `AccessModes` | 0..1 | [`AccessModeListOfEnumerations`](enumerations.md#accessmodelistofenumerations) | `foot` | Modalità di accesso allo stop place | §5.2.4.2, Tab. 43 |
| `ParentSiteRef` | 0..1 | `ParentSiteRefStructure` | `IT:ITC1:StopPlace:busATS:000MI` | Contiene un eventuale riferimento ad uno stop place “padre” | §5.2.4.2, Tab. 43 |
| `levels` | 0..1 | `levelsL5_RelStructure` |  |  |  |
| [`levels / Level`](#stopplaces-stopplace-levels-level) | 0..n · scelta 1 | `LevelL5_VersionStructure` |  | [⚠ Incongruenza](issues.md#43-netex-siteframe-netex-stopplaces-netex-stopplace-netex-levels-netex-level) | §5.2.4.2, Tab. 43 |
| `entrances` | 0..1 | `entrancesL5_RelStructure` |  |  |  |
| [`entrances / Entrance`](#stopplaces-stopplace-entrances-entrance) | 0..n · scelta 1 | `SiteEntranceL5_VersionStructure` |  | [⚠ Incongruenza](issues.md#43-netex-siteframe-netex-stopplaces-netex-stopplace-netex-entrances-netex-entrance) | §5.2.4.2, Tab. 43 |
| `TransportMode` | 0..1 | [`VehicleModeEnumeration`](enumerations.md#vehiclemodeenumeration) | `bus` | Modalità di trasporto primaria associata allo stop place [⚠ Incongruenza](issues.md#43-netex-siteframe-netex-stopplaces-netex-stopplace-netex-transportmode) | §5.2.4.2, Tab. 43 |
| `StopPlaceType` | 1..1 | [`StopTypeEnumeration`](enumerations.md#stoptypeenumeration) | `onstreetBus` | Tipologia dello stop place | §5.2.4.2, Tab. 43 |
| [`quays`](#stopplaces-stopplace-quays-quay) | 0..1 | `quaysL5_RelStructure` |  |  | §5.2.4.2, Tab. 43 |
| [`accessSpaces`](#stopplaces-stopplace-accessspaces-accessspace) | 0..1 | `accessSpacesL5_RelStructure` |  |  | §5.2.4.2, Tab. 43 |
| [`pathLinks`](#stopplaces-stopplace-pathlinks-sitepathlink) | 0..1 | `sitePathLinksL5_RelStructure` |  |  | §5.2.4.2, Tab. 43 |

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
    | `PurposeOfGroupingRef` | 0..1 | `PurposeOfGroupingRefStructure` |
    | `members` | 0..1 | `PlaceObjectMembers` |
    | `gml:Polygon` | 0..1 | `gml:T_Polygon` |
    | `placeTypes` | 0..1 | `placeTypes_Structure` |
    | `Url` | 0..1 | `xsd:anyURI` |
    | `Image` | 0..1 | `xsd:anyURI` |
    | `PostalAddress` | 0..1 | `PostalAddress_VersionStructure` |
    | `RoadAddress` | 0..1 | `RoadAddressStructure` |
    | `AccessibilityAssessment` | 0..1 | `AccessibilityAssessmentStructure` |
    | `alternativeNames` | 0..1 | `alternativeNamesStructure` |
    | `CrossRoad` | 0..1 | `MultilingualString` |
    | `Landmark` | 0..1 | `MultilingualString` |
    | `Covered` | 0..1 | [`CoveredEnumeration`](enumerations.md#coveredenumeration) |
    | `Gated` | 0..1 | [`GatedEnumeration`](enumerations.md#gatedenumeration) |
    | `Lighting` | 0..1 | [`LightingEnumeration`](enumerations.md#lightingenumeration) |
    | `facilities` | 0..1 | `siteFacilities_RelStructure` |
    | `TopographicPlaceRef` | 0..1 | `TopographicPlaceRefStructure` |
    | `TopographicPlaceView` | 0..1 | `TopographicPlaceViewStructure` |
    | `additionalTopographicPlaces` | 0..1 | `topographicPlaceRefs_RelStructure` |
    | `Locale` | 0..1 | `LocaleStructure` |
    | `OrganisationRef` | 0..1 | `OrganisationRefStructure` |
    | `AuthorityRef` | 0..1 | `AuthorityRefStructure` |
    | `OperatorRef` | 0..1 | `OperatorRefStructure` |
    | `PublicCode` | 0..1 | `xsd:normalizedString` |
    | `AirSubmode` | 0..1 | [`AirSubmodeEnumeration`](enumerations.md#airsubmodeenumeration) |
    | `BusSubmode` | 0..1 | [`BusSubmodeEnumeration`](enumerations.md#bussubmodeenumeration) |
    | `CoachSubmode` | 0..1 | [`CoachSubmodeEnumeration`](enumerations.md#coachsubmodeenumeration) |
    | `FunicularSubmode` | 0..1 | [`FunicularSubmodeEnumeration`](enumerations.md#funicularsubmodeenumeration) |
    | `MetroSubmode` | 0..1 | [`MetroSubmodeEnumeration`](enumerations.md#metrosubmodeenumeration) |
    | `TramSubmode` | 0..1 | [`TramSubmodeEnumeration`](enumerations.md#tramsubmodeenumeration) |
    | `TelecabinSubmode` | 0..1 | [`TelecabinSubmodeEnumeration`](enumerations.md#telecabinsubmodeenumeration) |
    | `RailSubmode` | 0..1 | [`RailSubmodeEnumeration`](enumerations.md#railsubmodeenumeration) |
    | `WaterSubmode` | 0..1 | [`WaterSubmodeEnumeration`](enumerations.md#watersubmodeenumeration) |
    | `SnowAndIceSubmode` | 0..1 | [`SnowAndIceSubmodeEnumeration`](enumerations.md#snowandicesubmodeenumeration) |
    | `OtherTransportModes` | 0..1 | [`VehicleModeListOfEnumerations`](enumerations.md#vehiclemodelistofenumerations) |
    | `tariffZones` | 0..1 | `tariffZoneRefs_RelStructure` |
    | `BorderCrossing` | 0..1 | `xsd:boolean` |
    | `unlocalisedEquipments` | 0..1 | `explicitEquipments_RelStructure` |
    | `Weighting` | 0..1 | [`InterchangeWeightingEnumeration`](enumerations.md#interchangeweightingenumeration) |
    | `StopPlaceWeight` | 0..1 | [`StopPlaceWeightEnumeration`](enumerations.md#stopplaceweightenumeration) |

#### levels / Level {#stopplaces-stopplace-levels-level}

Linee guida §5.2.4.2 «stopPlaces», Tabella 43. Tipo dell'XSD `LevelL5_VersionStructure`.

| Campo | Cardinalità | Tipo | Esempio | Significato (5T) | Fonte |
|---|---|---|---|---|---|
| `@id` | 1..1 | `xsd:normalizedString` | `IT:ITC1:Level:busATS:0001_Lvl_UG0` | Identificativo [→ Identificazione](common.md#identificazione) | §5.2.4.2, Tab. 43 (occorrenza 2) |
| `@version` | 0..1 | `xsd:normalizedString` | `1` | Versione [→ Identificazione](common.md#identificazione) [⚠ Incongruenza](issues.md#43-netex-siteframe-netex-stopplaces-netex-stopplace-netex-levels-netex-level-version) | §5.2.4.2, Tab. 43 (occorrenza 2) |
| `Name` | 0..1 | `MultilingualString` | `Ground` | Nome completo del livello | §5.2.4.2, Tab. 43 (occorrenza 2) |
| `PublicCode` | 0..1 | `xsd:normalizedString` | `G` | Codice pubblico del livello che permette ai passeggeri di identificarlo univocamente | §5.2.4.2, Tab. 43 |

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
    | `ShortName` | 0..1 | `MultilingualString` |
    | `Description` | 0..1 | `MultilingualString` |
    | `PublicUse` | 0..1 | `xsd:boolean` |
    | `RelativeLevelOrder` | 0..1 | `xsd:integer` |
    | `AccessibilityAssessment` | 0..1 | `AccessibilityAssessmentL5Structure` |
    | `AllAreasWheelchairAccessible` | 0..1 | `xsd:boolean` |

#### entrances / Entrance {#stopplaces-stopplace-entrances-entrance}

Linee guida §5.2.4.2 «stopPlaces», Tabella 43. Tipo dell'XSD `SiteEntranceL5_VersionStructure`.

| Campo | Cardinalità | Tipo | Esempio | Significato (5T) | Fonte |
|---|---|---|---|---|---|
| `@id` | 1..1 | `xsd:normalizedString` | `IT:ITC1:Entrance:busATS:Entrata001` | Identificativo [→ Identificazione](common.md#identificazione) | §5.2.4.2, Tab. 43 (occorrenza 3) |
| `@version` | 0..1 | `xsd:normalizedString` | `1` | Versione [→ Identificazione](common.md#identificazione) [⚠ Incongruenza](issues.md#43-netex-siteframe-netex-stopplaces-netex-stopplace-netex-entrances-netex-entrance-version) | §5.2.4.2, Tab. 43 (occorrenza 3) |
| `Centroid` | 0..1 | `CentroidStructure` |  |  |  |
| `Centroid / Location` | 1..1 | `LocationStructure` |  | Posizione della Entrance | §5.2.4.2, Tab. 43 |
| [`PostalAddress`](common.md#postaladdress) | 0..1 | `PostalAddress_VersionStructure` |  | Indirizzo della Entrance [⚠ Incongruenza](issues.md#43-netex-siteframe-netex-stopplaces-netex-stopplace-netex-entrances-netex-entrance-netex-postaladdress) | §5.2.4.2, Tab. 43 |
| [`AccessibilityAssessment`](common.md#accessibilityassessment) | 0..1 | `AccessibilityAssessmentL5Structure` |  |  |  |
| `Gated` | 0..1 | [`GatedEnumeration`](enumerations.md#gatedenumeration) | `gatedArea` | Indica la presenza di un accesso controllato | §5.2.4.2, Tab. 43 |
| `LevelRef` → [Level](#stopplaces-stopplace-levels-level) | 0..1 | `LevelRefStructure` | `IT:ITC1:Level:busATS:001_Lvl_G0` | Riferimento al Level della Entrance | §5.2.4.2, Tab. 43 |
| `IsExternal` | 0..1 | `xsd:boolean` | `true` | Indica se la Entrance è in comunicazione con l’esterno | §5.2.4.2, Tab. 43 |
| `IsEntry` | 0..1 | `xsd:boolean` | `true` | Indica se la Entrance è un’entrata | §5.2.4.2, Tab. 43 |
| `IsExit` | 0..1 | `xsd:boolean` | `false` | Indica se la Entrance è un’uscita | §5.2.4.2, Tab. 43 |
| `PublicCode` | 0..1 | `xsd:normalizedString` | `TO-Bolzano` | Codice pubblico dello stop place che permette ai passeggeri di identificarlo univocamente | §5.2.4.2, Tab. 43 (occorrenza 2) |

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
    | `Name` | 0..1 | `MultilingualString` |
    | `ShortName` | 0..1 | `MultilingualString` |
    | `Description` | 0..1 | `MultilingualString` |
    | `AccessModes` | 0..1 | [`AccessModeListOfEnumerations`](enumerations.md#accessmodelistofenumerations) |
    | `Covered` | 0..1 | [`CoveredEnumeration`](enumerations.md#coveredenumeration) |
    | `Lighting` | 0..1 | [`LightingEnumeration`](enumerations.md#lightingenumeration) |
    | `placeEquipments` | 0..1 | `placeEquipments_RelStructure` |
    | `Label` | 0..1 | `MultilingualString` |
    | `EntranceType` | 0..1 | [`EntranceEnumeration`](enumerations.md#entranceenumeration) |
    | `Width` | 0..1 | `LengthType` |
    | `Height` | 0..1 | `LengthType` |
    | `DroppedKerbOutside` | 0..1 | `xsd:boolean` |
    | `DropOffPointClose` | 0..1 | `xsd:boolean` |

#### quays / Quay {#stopplaces-stopplace-quays-quay}

Linee guida §5.2.4.2.1 «quays», Tabella 44. Tipo dell'XSD `QuayL5_VersionStructure`.

| Campo | Cardinalità | Tipo | Esempio | Significato (5T) | Fonte |
|---|---|---|---|---|---|
| `@id` | 1..1 | `xsd:normalizedString` | `IT:ITC1:Quay:busATS:001` | Identificativo [→ Identificazione](common.md#identificazione) [⚠ Incongruenza](issues.md#44-netex-siteframe-netex-stopplaces-netex-stopplace-netex-quays-netex-quay-id) | §5.2.4.2.1, Tab. 44 |
| `@version` | 0..1 | `xsd:normalizedString` | `1` | Versione [→ Identificazione](common.md#identificazione) [⚠ Incongruenza](issues.md#44-netex-siteframe-netex-stopplaces-netex-stopplace-netex-quays-netex-quay-version) | §5.2.4.2.1, Tab. 44 |
| `Name` | 0..1 | `MultilingualString` | `Capolinea Autostradale` | Nome completo del quay | §5.2.4.2.1, Tab. 44 |
| `Description` | 0..1 | `MultilingualString` | `Capolinea Autostradale - TO-MI` | Descrizione testuale libera del quay | §5.2.4.2.1, Tab. 44 |
| `Centroid` | 0..1 | `CentroidStructure` |  |  | §5.2.4.2.1, Tab. 44 |
| [`AccessibilityAssessment`](common.md#accessibilityassessment) | 0..1 | `AccessibilityAssessmentL5Structure` |  |  |  |
| `Covered` | 0..1 | [`CoveredEnumeration`](enumerations.md#coveredenumeration) | `covered` | Indica la presenza di copertura | §5.2.4.2.1, Tab. 44 |
| `Lighting` | 0..1 | [`LightingEnumeration`](enumerations.md#lightingenumeration) | `wellLit` | Indica la presenza di illuminazione [⚠ Incongruenza](issues.md#44-netex-siteframe-netex-stopplaces-netex-stopplace-netex-quays-netex-quay-netex-lighting) | §5.2.4.2.1, Tab. 44 |
| `LevelRef` → [Level](#stopplaces-stopplace-levels-level) | 0..1 | `LevelRefStructure` | `IT:ITC1:Level:busATS:001_Lvl_G0` | Riferimento ad un’entità Level | §5.2.4.2.1, Tab. 44 |
| `placeEquipments` | 0..1 | `placeEquipments_RelStructure` |  | Riferimento alla dotazione dei quays | §5.2.4.2.1, Tab. 44 |
| `placeEquipments / EscalatorEquipmentRef` → [EscalatorEquipment](resource-frame.md#equipments-escalatorequipment) | 0..n | `EscalatorEquipmentRefStructure` | `IT:ITC1:EscalatorEquipment:busATS:001` | Riferimento ai sistemi sollevatori (vedi par. 5.2.3.4.3) | §5.2.4.2.1, Tab. 44 |
| `placeEquipments / LiftEquipmentRef` → [LiftEquipment](resource-frame.md#equipments-liftequipment) | 0..n | `LiftEquipmentRefStructure` | `IT:ITC1:LiftEquipments:busATS:2` | Riferimento alla presenza di ascensori (5.2.3.4.7) | §5.2.4.2.1, Tab. 44 |
| `placeEquipments / LiftCallEquipmentRef` → [LiftCallEquipment](resource-frame.md#equipments-liftcallequipment) | 0..n | `LiftCallEquipmentRefStructure` | `IT:ITC1:LiftCallEquipment:busATS:001` | Riferimento ai sistemi di chiamata degli ascensori (vedi par. 5.2.3.4.6). [⚠ Incongruenza](issues.md#44-netex-siteframe-netex-stopplaces-netex-stopplace-netex-quays-netex-quay-netex-placeequipments-netex-liftcallequipmentref) | §5.2.4.2.1, Tab. 44 |
| `placeEquipments / RampEquipmentRef` → [RampEquipment](resource-frame.md#equipments-rampequipment) | 0..n | `RampEquipmentRefStructure` | `IT:ITC1:RampEquipment:busATS:001` | Riferimento alle dotazioni delle rampe (vedi par. 5.2.3.4.11). | §5.2.4.2.1, Tab. 44 |
| `placeEquipments / RoughSurfaceRef` → [RoughSurface](resource-frame.md#equipments-roughsurface) | 0..n | `RoughSurfaceRefStructure` | `IT:ITC1:RoughSurface:busATS:001` | Riferimento alla tipologia di superficie di accesso alle fermate (vedi par. 5.2.3.4.12). | §5.2.4.2.1, Tab. 44 |
| `placeEquipments / StaircaseEquipmentRef` → [StaircaseEquipment](resource-frame.md#equipments-staircaseequipment) | 0..n | `StaircaseEquipmentRefStructure` | `IT:ITC1:StaircaseEquipment:busATS:001` | Riferimento alle dotazioni delle scale (vedi par. 5.2.3.4.14). | §5.2.4.2.1, Tab. 44 |
| `placeEquipments / TicketingEquipment` | 0..n | `TicketingEquipment_VersionStructure` |  | Struttura equivalente a quella del par. 5.2.3.4.15 | §5.2.4.2.1, Tab. 44 |
| `Label` | 0..1 | `xsd:normalizedString` | `TO-MI` | Breve stringa associata al quay | §5.2.4.2.1, Tab. 44 |
| `entrances` | 0..1 | `entrancesL5_RelStructure` |  |  |  |
| `entrances / EntranceRef` → [Entrance](#stopplaces-stopplace-entrances-entrance) | 0..n · scelta 1 | `EntranceRefStructure` | `IT:ITC1:Entrance:busATS:Entrata002` | Riferimento alle entrate del Quay | §5.2.4.2.1, Tab. 44 |
| `QuayType` | 0..1 | [`QuayTypeEnumeration`](enumerations.md#quaytypeenumeration) | `busStop` | Tipologia del quay | §5.2.4.2.1, Tab. 44 |

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
    | `ShortName` | 0..1 | `MultilingualString` |
    | `PurposeOfGroupingRef` | 0..1 | `PurposeOfGroupingRefStructure` |
    | `PrivateCode` | 0..1 | `PrivateCodeStructure` |
    | `members` | 0..1 | `PlaceObjectMembers` |
    | `gml:Polygon` | 0..1 | `gml:T_Polygon` |
    | `placeTypes` | 0..1 | `placeTypes_Structure` |
    | `Url` | 0..1 | `xsd:anyURI` |
    | `Image` | 0..1 | `xsd:anyURI` |
    | `PostalAddress` | 0..1 | `PostalAddress_VersionStructure` |
    | `RoadAddress` | 0..1 | `RoadAddressStructure` |
    | `AccessModes` | 0..1 | [`AccessModeListOfEnumerations`](enumerations.md#accessmodelistofenumerations) |
    | `alternativeNames` | 0..1 | `alternativeNamesStructure` |
    | `CrossRoad` | 0..1 | `MultilingualString` |
    | `Landmark` | 0..1 | `MultilingualString` |
    | `Gated` | 0..1 | [`GatedEnumeration`](enumerations.md#gatedenumeration) |
    | `AllAreasWheelchairAccessible` | 0..1 | `xsd:boolean` |
    | `Length` | 0..1 | `LengthType` |
    | `Width` | 0..1 | `LengthType` |
    | `PublicCode` | 0..1 | `xsd:normalizedString` |
    | `PlateCode` | 0..1 | `xsd:normalizedString` |
    | `destinations` | 0..1 | `destinationDisplayViews_RelStructure` |
    | `CompassBearing` | 0..1 | `xsd:float` |
    | `PlatformHeight` | 0..1 | `LengthType` |
    | `ParentQuayRef` | 0..1 | `QuayRefStructure` |

#### accessSpaces / AccessSpace {#stopplaces-stopplace-accessspaces-accessspace}

Linee guida §5.2.4.2.2 «accessSpaces», Tabella 45. Tipo dell'XSD `AccessSpaceL5_VersionStructure`.

| Campo | Cardinalità | Tipo | Esempio | Significato (5T) | Fonte |
|---|---|---|---|---|---|
| `@id` | 1..1 | `xsd:normalizedString` | `IT:ITC1:Quay:busATS:001` | Identificativo [→ Identificazione](common.md#identificazione) [⚠ Incongruenza](issues.md#45-netex-siteframe-netex-stopplaces-netex-stopplace-netex-accessspaces-netex-accessspace-id) | §5.2.4.2.2, Tab. 45 |
| `@version` | 0..1 | `xsd:normalizedString` | `1` | Versione [→ Identificazione](common.md#identificazione) [⚠ Incongruenza](issues.md#45-netex-siteframe-netex-stopplaces-netex-stopplace-netex-accessspaces-netex-accessspace-version) | §5.2.4.2.2, Tab. 45 |
| `Name` | 0..1 | `MultilingualString` | `Mezzanino` | Nome completo del AccessSpace | §5.2.4.2.2, Tab. 45 |
| `Description` | 0..1 | `MultilingualString` | `Mezzanino` | Descrizione testuale libera del AccessSpace | §5.2.4.2.2, Tab. 45 |
| `Centroid` | 0..1 | `CentroidStructure` |  |  | §5.2.4.2.2, Tab. 45 |
| [`AccessibilityAssessment`](common.md#accessibilityassessment) | 0..1 | `AccessibilityAssessmentL5Structure` |  |  |  |
| `Covered` | 0..1 | [`CoveredEnumeration`](enumerations.md#coveredenumeration) | `covered` | Indica la presenza di copertura | §5.2.4.2.2, Tab. 45 |
| `Lighting` | 0..1 | [`LightingEnumeration`](enumerations.md#lightingenumeration) | `wellLit` | Indica la presenza di illuminazione [⚠ Incongruenza](issues.md#45-netex-siteframe-netex-stopplaces-netex-stopplace-netex-accessspaces-netex-accessspace-netex-lighting) | §5.2.4.2.2, Tab. 45 |
| `LevelRef` → [Level](#stopplaces-stopplace-levels-level) | 0..1 | `LevelRefStructure` | `IT:ITC1:Level:busATS:001_Lvl_G0` | Riferimento ad un’entità Level | §5.2.4.2.2, Tab. 45 |
| `placeEquipments` | 0..1 | `placeEquipments_RelStructure` |  | Riferimento alla dotazione dei accessSpaces | §5.2.4.2.2, Tab. 45 |
| `placeEquipments / EscalatorEquipmentRef` → [EscalatorEquipment](resource-frame.md#equipments-escalatorequipment) | 0..n | `EscalatorEquipmentRefStructure` | `IT:ITC1:EscalatorEquipment:busATS:001` | Riferimento ai sistemi sollevatori (vedi par. 5.2.3.4.3) | §5.2.4.2.2, Tab. 45 |
| `placeEquipments / LiftEquipmentRef` → [LiftEquipment](resource-frame.md#equipments-liftequipment) | 0..n | `LiftEquipmentRefStructure` | `IT:ITC1:LiftEquipments:busATS:2` | Riferimento alla presenza di ascensori (5.2.3.4.7) | §5.2.4.2.2, Tab. 45 |
| `placeEquipments / LiftCallEquipmentRef` → [LiftCallEquipment](resource-frame.md#equipments-liftcallequipment) | 0..n | `LiftCallEquipmentRefStructure` | `IT:ITC1:LiftCallEquipment:busATS:001` | Riferimento ai sistemi di chiamata degli ascensori (vedi par. 5.2.3.4.6). [⚠ Incongruenza](issues.md#45-netex-siteframe-netex-stopplaces-netex-stopplace-netex-accessspaces-netex-accessspace-netex-placeequipments-netex-liftcallequipmentref) | §5.2.4.2.2, Tab. 45 |
| `placeEquipments / RampEquipmentRef` → [RampEquipment](resource-frame.md#equipments-rampequipment) | 0..n | `RampEquipmentRefStructure` | `IT:ITC1:RampEquipment:busATS:001` | Riferimento alle dotazioni delle rampe (vedi par. 5.2.3.4.11). | §5.2.4.2.2, Tab. 45 |
| `placeEquipments / RoughSurfaceRef` → [RoughSurface](resource-frame.md#equipments-roughsurface) | 0..n | `RoughSurfaceRefStructure` | `IT:ITC1:RoughSurface:busATS:001` | Riferimento alla tipologia di superficie di accesso alle fermate (vedi par. 5.2.3.4.12). | §5.2.4.2.2, Tab. 45 |
| `placeEquipments / StaircaseEquipmentRef` → [StaircaseEquipment](resource-frame.md#equipments-staircaseequipment) | 0..n | `StaircaseEquipmentRefStructure` | `IT:ITC1:StaircaseEquipment:busATS:001` | Riferimento alle dotazioni delle scale (vedi par. 5.2.3.4.14). | §5.2.4.2.2, Tab. 45 |
| `placeEquipments / TicketingEquipment` | 0..n | `TicketingEquipment_VersionStructure` |  | Struttura equivalente a quella del par. 5.2.3.4.15 | §5.2.4.2.2, Tab. 45 |
| `entrances` | 0..1 | `entrancesL5_RelStructure` |  |  |  |
| `entrances / EntranceRef` → [Entrance](#stopplaces-stopplace-entrances-entrance) | 0..n · scelta 1 | `EntranceRefStructure` | `IT:ITC1:Entrance:busATS:Entrata001` | Riferimento alle entrate del accessSpaces [⚠ Incongruenza](issues.md#45-netex-siteframe-netex-stopplaces-netex-stopplace-netex-accessspaces-netex-accessspace-netex-entrances-netex-entranceref) | §5.2.4.2.2, Tab. 45 |
| `AccessSpaceType` | 0..1 | [`AccessSpaceTypeEnumeration`](enumerations.md#accessspacetypeenumeration) | `passage` | Tipologia del accessSpaces [⚠ Incongruenza](issues.md#45-netex-siteframe-netex-stopplaces-netex-stopplace-netex-accessspaces-netex-accessspace-netex-accessspacetype) | §5.2.4.2.2, Tab. 45 |

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
    | `ShortName` | 0..1 | `MultilingualString` |
    | `PurposeOfGroupingRef` | 0..1 | `PurposeOfGroupingRefStructure` |
    | `PrivateCode` | 0..1 | `PrivateCodeStructure` |
    | `members` | 0..1 | `PlaceObjectMembers` |
    | `gml:Polygon` | 0..1 | `gml:T_Polygon` |
    | `placeTypes` | 0..1 | `placeTypes_Structure` |
    | `Url` | 0..1 | `xsd:anyURI` |
    | `Image` | 0..1 | `xsd:anyURI` |
    | `PostalAddress` | 0..1 | `PostalAddress_VersionStructure` |
    | `RoadAddress` | 0..1 | `RoadAddressStructure` |
    | `AccessModes` | 0..1 | [`AccessModeListOfEnumerations`](enumerations.md#accessmodelistofenumerations) |
    | `alternativeNames` | 0..1 | `alternativeNamesStructure` |
    | `CrossRoad` | 0..1 | `MultilingualString` |
    | `Landmark` | 0..1 | `MultilingualString` |
    | `Gated` | 0..1 | [`GatedEnumeration`](enumerations.md#gatedenumeration) |
    | `AllAreasWheelchairAccessible` | 0..1 | `xsd:boolean` |
    | `Label` | 0..1 | `xsd:normalizedString` |
    | `Length` | 0..1 | `LengthType` |
    | `Width` | 0..1 | `LengthType` |
    | `PassageType` | 0..1 | [`PassageTypeEnumeration`](enumerations.md#passagetypeenumeration) |
    | `ParentAccessSpaceRef` | 0..1 | `AccessSpaceRefStructure` |

#### pathLinks / SitePathLink {#stopplaces-stopplace-pathlinks-sitepathlink}

Linee guida §5.2.4.2.3 «pathLinks», Tabella 46. Tipo dell'XSD `PathLinkL5_VersionStructure`.

| Campo | Cardinalità | Tipo | Esempio | Significato (5T) | Fonte |
|---|---|---|---|---|---|
| `@id` | 1..1 | `xsd:normalizedString` | `IT:ITC1:Quay:busATS:001` | Identificativo [→ Identificazione](common.md#identificazione) [⚠ Incongruenza](issues.md#46-netex-siteframe-netex-stopplaces-netex-stopplace-netex-pathlinks-netex-sitepathlink-id) | §5.2.4.2.3, Tab. 46 |
| `@version` | 0..1 | `xsd:normalizedString` | `1` | Versione [→ Identificazione](common.md#identificazione) [⚠ Incongruenza](issues.md#46-netex-siteframe-netex-stopplaces-netex-stopplace-netex-pathlinks-netex-sitepathlink-version) | §5.2.4.2.3, Tab. 46 |
| `Distance` | 0..1 | `LengthType` | `10` | Lunghezza in metri dell’arco | §5.2.4.2.3, Tab. 46 |
| `gml:LineString` | 0..1 | `gml:T_LineString` | `<gml:posList>10.8375021270454 45.7996993338911 10.8427924483546 45.8039389496581</gml:posList>` | Rappresentazione secondo lo standard GML della polilinea che descrive la geometria dell’arco | §5.2.4.2.3, Tab. 46 |
| `From` | 1..1 | `PathLinkEndStructure` |  |  |  |
| `From / PlaceRef` | 1..1 | `PlaceRefStructure` | `IT:ITC1:Entrance:busATS:Entrata001` | Identificativo della Entrance o del Quay o dell’AccessSpace in cui inizia l’arco. | §5.2.4.2.3, Tab. 46 |
| `To` | 1..1 | `PathLinkEndStructure` |  |  |  |
| `To / PlaceRef` | 1..1 | `PlaceRefStructure` | `IT:ITC1:Entrance:busATS:Entrata001` | Identificativo della Entrance o del Quay o dell’AccessSpace in cui finisce l’arco. | §5.2.4.2.3, Tab. 46 |
| [`AccessibilityAssessment`](common.md#accessibilityassessment) | 0..1 · scelta 1 | `AccessibilityAssessmentL5Structure` |  |  | §5.2.4.2.3, Tab. 46 |

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
    | `AccessibilityAssessmentRef` | 0..1 | `AccessibilityAssessmentRefStructure` |
    | `AccessModes` | 0..1 | [`AccessModeListOfEnumerations`](enumerations.md#accessmodelistofenumerations) |
    | `Covered` | 0..1 | [`CoveredEnumeration`](enumerations.md#coveredenumeration) |
    | `Gated` | 0..1 | [`GatedEnumeration`](enumerations.md#gatedenumeration) |
    | `Lighting` | 0..1 | [`LightingEnumeration`](enumerations.md#lightingenumeration) |
    | `NumberOfSteps` | 0..1 | `xsd:nonNegativeInteger` |
    | `AllowedUse` | 0..1 | [`PathDirectionEnumeration`](enumerations.md#pathdirectionenumeration) |
    | `Transition` | 0..1 | [`TransitionEnumeration`](enumerations.md#transitionenumeration) |
    | `Gradient` | 0..1 | `xsd:integer` |
    | `GradientType` | 0..1 | [`GradientEnumeration`](enumerations.md#gradientenumeration) |
    | `TiltAngle` | 0..1 | `xsd:integer` |
    | `TiltType` | 0..1 | [`TiltTypeEnumeration`](enumerations.md#tilttypeenumeration) |
    | `AccessFeatureType` | 0..1 | [`AccessFeatureEnumeration`](enumerations.md#accessfeatureenumeration) |
    | `PassageType` | 0..1 | [`PassageTypeEnumeration`](enumerations.md#passagetypeenumeration) |
    | `TactileWarningStrip` | 0..1 | [`TactileWarningStripEnumeration`](enumerations.md#tactilewarningstripenumeration) |
    | `TactileGuidingStrip` | 0..1 | `xsd:boolean` |
    | `LevelRef` | 0..1 | `LevelRefStructure` |
    | `placeEquipments` | 0..1 | `placeEquipments_RelStructure` |

### parkings / Parking {#parkings-parking}

Linee guida §5.2.4.3 «Parkings», Tabella 47. Tipo dell'XSD `ParkingL2_VersionStructure`.

| Campo | Cardinalità | Tipo | Esempio | Significato (5T) | Fonte |
|---|---|---|---|---|---|
| `@id` | 1..1 | `xsd:normalizedString` | `IT:ITC1:Parking:parcheggiTorino:p:Porta_Nuova` | Identificativo [→ Identificazione](common.md#identificazione) | §5.2.4.3, Tab. 47 |
| `@version` | 0..1 | `xsd:normalizedString` | `1` | Versione [→ Identificazione](common.md#identificazione) [⚠ Incongruenza](issues.md#47-netex-siteframe-netex-parkings-netex-parking-version) | §5.2.4.3, Tab. 47 |
| `Name` | 0..1 | `MultilingualString` | `Parcheggio Porta Nuova` | Nome completo del parcheggio | §5.2.4.3, Tab. 47 |
| `ShortName` | 0..1 | `MultilingualString` | `Porta Nuova` | Nome breve del parcheggio | §5.2.4.3, Tab. 47 |
| `Centroid` | 0..1 | `CentroidStructure` |  |  | §5.2.4.3, Tab. 47 |
| `gml:Polygon` | 0..1 | `gml:T_Polygon` |  |  | §5.2.4.3, Tab. 47 |
| `OperatorRef` → [Operator](resource-frame.md#organisations-operator) | 0..1 | `OperatorRefStructure` | `IT:ITC1:Operator:parcheggiTorino:parcheggiTorino` | Riferimento all’operatore | §5.2.4.3, Tab. 47 |
| [`entrances`](#parkings-parking-entrances-parkingentranceforvehicles) | 0..1 | `siteEntrances_RelStructure` |  |  | §5.2.4.3, Tab. 47 |
| `ParkingType` | 0..1 | [`ParkingTypeEnumeration`](enumerations.md#parkingtypeenumeration) | `parkAndRide` | Tipologia di parcheggio | §5.2.4.3, Tab. 47 |
| `ParkingVehicleTypes` | 0..1 | [`ParkingVehicleListOfEnumerations`](enumerations.md#parkingvehiclelistofenumerations) | `car` | Tipologia di mezzi ammessi nel parcheggio [⚠ Incongruenza](issues.md#47-netex-siteframe-netex-parkings-netex-parking-netex-parkingvehicletypes) | §5.2.4.3, Tab. 47 |
| `ParkingLayout` | 0..1 | [`ParkingLayoutEnumeration`](enumerations.md#parkinglayoutenumeration) | `roadside` | Disposizione dell’area di parcheggio | §5.2.4.3, Tab. 47 |
| `PrincipalCapacity` | 0..1 | `xsd:integer` | `80` | Stalli ordinari disponibili | §5.2.4.3, Tab. 47 |
| `TotalCapacity` | 0..1 | `xsd:integer` | `100` | Stalli totali disponibili | §5.2.4.3, Tab. 47 |
| `ProhibitedForHazardousMaterials` | 0..1 | `xsd:boolean` | `true` | Limitazioni per materiali pericolosi | §5.2.4.3, Tab. 47 |
| `RechargingAvailable` | 0..1 | `xsd:boolean` | `true` | Disponibilità punti di ricarica elettrica | §5.2.4.3, Tab. 47 |
| `Secure` | 0..1 | `xsd:boolean` | `true` | Parcheggio sorvegliato | §5.2.4.3, Tab. 47 |
| `ParkingReservation` | 0..1 | [`ParkingReservationEnumeration`](enumerations.md#parkingreservationenumeration) | `reservationAllowed` | Possibilità di prenotare il parcheggio | §5.2.4.3, Tab. 47 |
| [`parkingProperties`](#parkings-parking-parkingproperties-parkingproperties) | 0..1 | `parkingProperties_RelStructure` |  |  | §5.2.4.3, Tab. 47 |

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
    | `Covered` | 0..1 | `xsd:string` |
    | `ParentSiteRef` | 0..1 | `ParentSiteRefStructure` |
    | `ParkingPaymentProcess` | 0..1 | [`ParkingPaymentProcessListOfEnumerations`](enumerations.md#parkingpaymentprocesslistofenumerations) |

#### entrances / ParkingEntranceForVehicles {#parkings-parking-entrances-parkingentranceforvehicles}

Linee guida §5.2.4.3.1 «entrances», Tabella 48. Tipo dell'XSD `ParkingEntranceForVehicles_VersionStructure`.

| Campo | Cardinalità | Tipo | Esempio | Significato (5T) | Fonte |
|---|---|---|---|---|---|
| `@id` | 1..1 | `xsd:normalizedString` | `IT:ITC1:ParkingEntranceForVehicles:parcheggiTorino:pefv:Porta_Nuova_EntrataVeicoli1` | Identificativo [→ Identificazione](common.md#identificazione) [⚠ Incongruenza](issues.md#48-netex-siteframe-netex-parkings-netex-parking-netex-entrances-netex-parkingentranceforvehicles-id) | §5.2.4.3.1, Tab. 48 |
| `@version` | 0..1 | `xsd:normalizedString` | `1` | Versione [→ Identificazione](common.md#identificazione) [⚠ Incongruenza](issues.md#48-netex-siteframe-netex-parkings-netex-parking-netex-entrances-netex-parkingentranceforvehicles-version) | §5.2.4.3.1, Tab. 48 |
| `Centroid` | 0..1 | `CentroidStructure` |  |  | §5.2.4.3.1, Tab. 48 |
| [`PostalAddress`](common.md#postaladdress) | 0..1 | `PostalAddress_VersionStructure` |  |  | §5.2.4.3.1, Tab. 48 |
| `IsEntry` | 0..1 | `xsd:boolean` | `true` | Accesso utilizzato come ingresso | §5.2.4.3.1, Tab. 48 |
| `IsExit` | 0..1 | `xsd:boolean` | `false` | Accesso utilizzato come uscita | §5.2.4.3.1, Tab. 48 |

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
    | `PublicCode` | 0..1 | `xsd:normalizedString` |
    | `Label` | 0..1 | `MultilingualString` |
    | `EntranceType` | 0..1 | [`EntranceEnumeration`](enumerations.md#entranceenumeration) |
    | `IsExternal` | 0..1 | `xsd:boolean` |
    | `Width` | 0..1 | `LengthType` |
    | `Height` | 0..1 | `LengthType` |

#### parkingProperties / ParkingProperties {#parkings-parking-parkingproperties-parkingproperties}

Linee guida §5.2.4.3.2 «parkingProperties», Tabella 49. Tipo dell'XSD `ParkingProperties_VersionStructure`.

| Campo | Cardinalità | Tipo | Esempio | Significato (5T) | Fonte |
|---|---|---|---|---|---|
| `@id` | 1..1 | `xsd:normalizedString` | `IT:ITC1:ParkingProperties:parcheggiTorino:pc1` | Identificativo [→ Identificazione](common.md#identificazione) [⚠ Incongruenza](issues.md#49-netex-siteframe-netex-parkings-netex-parking-netex-parkingproperties-netex-parkingproperties-id) | §5.2.4.3.2, Tab. 49 |
| `@version` | 0..1 | `xsd:normalizedString` | `1` | Versione [→ Identificazione](common.md#identificazione) [⚠ Incongruenza](issues.md#49-netex-siteframe-netex-parkings-netex-parking-netex-parkingproperties-netex-parkingproperties-version) | §5.2.4.3.2, Tab. 49 |
| [`spaces`](#parkings-parking-parkingproperties-parkingproperties-spaces-parkingcapacity) | 0..1 | `parkingCapacities_RelStructure` |  |  | §5.2.4.3.2, Tab. 49 |

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

##### spaces / ParkingCapacity {#parkings-parking-parkingproperties-parkingproperties-spaces-parkingcapacity}

Linee guida §5.2.4.3.2 «parkingProperties», Tabella 50. Tipo dell'XSD `ParkingCapacity_VersionStructure`.

| Campo | Cardinalità | Tipo | Esempio | Significato (5T) | Fonte |
|---|---|---|---|---|---|
| `@id` | 1..1 | `xsd:normalizedString` | `IT:ITC1:ParkingCapacity:parcheggiTorino:pcauto` | Identificativo [→ Identificazione](common.md#identificazione) [⚠ Incongruenza](issues.md#50-netex-siteframe-netex-parkings-netex-parking-netex-parkingproperties-netex-parkingproperties-netex-spaces-netex-parkingcapacity-id) | §5.2.4.3.2, Tab. 50 |
| `@version` | 0..1 | `xsd:normalizedString` | `1` | Versione [→ Identificazione](common.md#identificazione) [⚠ Incongruenza](issues.md#50-netex-siteframe-netex-parkings-netex-parking-netex-parkingproperties-netex-parkingproperties-netex-spaces-netex-parkingcapacity-version) | §5.2.4.3.2, Tab. 50 |
| `ParkingUserType` | 0..1 | [`ParkingUserEnumeration`](enumerations.md#parkinguserenumeration) | `registered` | Categoria di utenti che usufruiscono degli stalli indicati | §5.2.4.3.2, Tab. 50 |
| `ParkingVehicleType` | 0..1 | [`ParkingVehicleEnumeration`](enumerations.md#parkingvehicleenumeration) | `car` | Tipologia di mezzo ammesso negli stalli indicati | §5.2.4.3.2, Tab. 50 |
| `ParkingStayType` | 0..1 | [`ParkingStayEnumeration`](enumerations.md#parkingstayenumeration) | `midTerm` | Tipo di permanenza dell’utente che può usare gli stalli | §5.2.4.3.2, Tab. 50 |
| `NumberOfSpaces` | 0..1 | `xsd:nonNegativeInteger` | `100` | Numero stalli parcheggio | §5.2.4.3.2, Tab. 50 |
| `NumberOfSpacesWithRechargePoint` | 0..1 | `xsd:nonNegativeInteger` | `10` | Numero stalli parcheggio con postazione ricarica elettrica | §5.2.4.3.2, Tab. 50 |

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
