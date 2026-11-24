---
generato: true
generato_da: rpsd-tools 0.8.0
---
<!-- GENERATED — DO NOT EDIT · profile-docs netex-it · netex-it-lev5@cecb0cd -->

# MobilityServiceFrame

Servizi di mobilità condivisa (linee guida §5.2.8).

## MobilityServiceFrame {#mobilityserviceframe}

Linee guida §5.2.8 «MobilityServiceFrame», Tabella 80. Tipo dell'XSD `MobilityServiceFrame_VersionStructure`.

| Campo | Cardinalità | Tipo | Esempio | Significato (5T) | Fonte |
|---|---|---|---|---|---|
| `@id` | 1..1 | `xsd:normalizedString` | `epd:IT:ITC1:MobilityServiceFrame_EU_PI_MOBILITY:BikeSharing:ita` | Identificativo [→ Identificazione](common.md#identificazione) | §5.2.8, Tab. 80 |
| `@version` | 0..1 | `xsd:normalizedString` | `1` | Versione [→ Identificazione](common.md#identificazione) | §5.2.8, Tab. 80 |
| [`fleets`](#fleets-fleet) | 0..1 | `fleets_RelStructure` |  |  |  |
| [`modesOfOperation`](#modesofoperation-vehiclesharing) | 0..1 | `modesOfOperation_RelStructure` |  |  |  |
| [`mobilityServices`](#mobilityservices-vehiclesharingservice) | 0..1 | `mobilityServices_RelStructure` |  |  |  |
| [`mobilityServiceConstraintZones`](#mobilityserviceconstraintzones-mobilityserviceconstraintzone) | 0..1 | `mobilityServiceConstraintZones_RelStructure` |  |  |  |

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

### fleets / Fleet {#fleets-fleet}

Linee guida §5.2.8.1 «fleets», Tabella 81. Tipo dell'XSD `Fleet_VersionStructure`.

| Campo | Cardinalità | Tipo | Esempio | Significato (5T) | Fonte |
|---|---|---|---|---|---|
| `@id` | 1..1 | `xsd:normalizedString` | `IT:ITC1:Fleet:BikeSharingTorino:fleet:1` | Identificativo [→ Identificazione](common.md#identificazione) | §5.2.8.1, Tab. 81 |
| `@version` | 0..1 | `xsd:normalizedString` | `1` | Versione [→ Identificazione](common.md#identificazione) | §5.2.8.1, Tab. 81 |
| [`ValidBetween`](common.md#validbetween) | 0..1 | `ValidBetween_VersionStructure` |  | Struttura contente le condizioni di validità temporale [⚠ Incongruenza](issues.md#81-netex-mobilityserviceframe-netex-fleets-netex-fleet-netex-validbetween) | §5.2.8.1, Tab. 81 |
| `members` | 0..1 | `vehicles_RelStructure` |  | Riferimenti a tutti i veicoli che fanno parte della flotta | §5.2.8.1, Tab. 81 |
| `members / VehicleRef` → [Vehicle](resource-frame.md#vehicles-vehicle) | 1..n | `VehicleRefStructure` | `IT:ITC1:Vehicle:BikeSharingTorino:VE:01` | Riferimento al veicolo | §5.2.8.1, Tab. 81 |
| `OperatorRef` → [Operator](resource-frame.md#organisations-operator) | 0..1 | `OperatorRefStructure` | `IT:ITC1:Operator:BikeSharing:BikeSharing` | Riferimento al veicolo | §5.2.8.1, Tab. 81 |

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

### modesOfOperation / VehicleSharing {#modesofoperation-vehiclesharing}

Linee guida §5.2.8.2 «modesOfOperation», Tabella 82. Tipo dell'XSD `VehicleSharing_VersionStructure`.

| Campo | Cardinalità | Tipo | Esempio | Significato (5T) | Fonte |
|---|---|---|---|---|---|
| `@id` | 1..1 | `xsd:normalizedString` | `IT:ITC1:VehicleSharing:BikeSharingTorino:VS:1` | Identificativo [→ Identificazione](common.md#identificazione) | §5.2.8.2, Tab. 82 |
| `@version` | 0..1 | `xsd:normalizedString` | `1` | Versione [→ Identificazione](common.md#identificazione) | §5.2.8.2, Tab. 82 |
| [`submodes`](#modesofoperation-vehiclesharing-submodes-submode) | 0..1 | `submodes_RelStructure` |  |  |  |

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

#### submodes / Submode {#modesofoperation-vehiclesharing-submodes-submode}

Linee guida §5.2.8.2 «modesOfOperation», Tabella 82. Tipo dell'XSD `Submode_VersionStructure`.

| Campo | Cardinalità | Tipo | Esempio | Significato (5T) | Fonte |
|---|---|---|---|---|---|
| `@id` | 1..1 | `xsd:normalizedString` | `IT:ITC1:Submode:BikeSharingTorino:submode:1` | Identificativo [→ Identificazione](common.md#identificazione) | §5.2.8.2, Tab. 82 |
| `@version` | 0..1 | `xsd:normalizedString` | `1` | Versione [→ Identificazione](common.md#identificazione) | §5.2.8.2, Tab. 82 |
| `TransportMode` | 1..1 | [`AllModesL4Enumeration`](enumerations.md#allmodesl4enumeration) | `bicycle` | Modalità di trasporti | §5.2.8.2, Tab. 82 |
| `SelfDriveSubmode` | 1..1 | [`SelfDriveSubmodeL4Enumeration`](enumerations.md#selfdrivesubmodel4enumeration) | `hireCycle` | Proprietà del veicolo [⚠ Incongruenza](issues.md#82-netex-mobilityserviceframe-netex-modesofoperation-netex-vehiclesharing-netex-submodes-netex-submode-netex-selfdrivesubmode) | §5.2.8.2, Tab. 82 |

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

### mobilityServices / VehicleSharingService {#mobilityservices-vehiclesharingservice}

Linee guida §5.2.8.3 «mobilityServices», Tabella 83. Tipo dell'XSD `VehicleSharingService_VersionStructure`.

| Campo | Cardinalità | Tipo | Esempio | Significato (5T) | Fonte |
|---|---|---|---|---|---|
| `@id` | 1..1 | `xsd:normalizedString` | `IT:ITC1:VehicleSharingService:BikeSharingTorino:VSS:1` | Identificativo [→ Identificazione](common.md#identificazione) | §5.2.8.3, Tab. 83 |
| `@version` | 0..1 | `xsd:normalizedString` | `1` | Versione [→ Identificazione](common.md#identificazione) | §5.2.8.3, Tab. 83 |
| `VehicleSharingRef` → [VehicleSharing](#modesofoperation-vehiclesharing) | 1..1 | `VehicleSharingRefStructure` |  |  |  |
| `VehicleSharingRef / @ref` → [VehicleSharing](#modesofoperation-vehiclesharing) | 1..1 | `xsd:normalizedString` | `IT:ITC1:VehicleSharing:BikeSharingTorino:VS:1` | Id della modalità del servizio [⚠ Incongruenza](issues.md#83-netex-mobilityserviceframe-netex-mobilityservices-netex-vehiclesharingservice-netex-vehiclesharingref-ref) | §5.2.8.3, Tab. 83 |
| `VehicleSharingRef / @version` → [VehicleSharing](#modesofoperation-vehiclesharing) | 0..1 | `xsd:normalizedString` | `1` | Versione della modalità del servizio [⚠ Incongruenza](issues.md#83-netex-mobilityserviceframe-netex-mobilityservices-netex-vehiclesharingservice-netex-vehiclesharingref-version) | §5.2.8.3, Tab. 83 |
| `FloatingVehicles` | 0..1 | `xsd:boolean` | `false` | Veicolo in free floating | §5.2.8.3, Tab. 83 |
| [`fleets`](#mobilityservices-vehiclesharingservice-fleets-fleetref) | 0..1 | `fleetRefs_RelStructure` |  |  |  |

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

#### fleets / FleetRef {#mobilityservices-vehiclesharingservice-fleets-fleetref}

Linee guida §5.2.8.3 «mobilityServices», Tabella 83. Tipo dell'XSD `FleetRefStructure`.

| Campo | Cardinalità | Tipo | Esempio | Significato (5T) | Fonte |
|---|---|---|---|---|---|
| `@ref` | 1..1 | `xsd:normalizedString` | `IT:ITC1:Fleet:BikeSharingTorino:fleet:1` | Riferimento alla flotta [⚠ Incongruenza](issues.md#83-netex-mobilityserviceframe-netex-mobilityservices-netex-vehiclesharingservice-netex-fleets-netex-fleetref-ref) | §5.2.8.3, Tab. 83 |
| `@version` | 0..1 | `xsd:normalizedString` | `1` | Versione [→ Identificazione](common.md#identificazione) | §5.2.8.3, Tab. 83 |

??? note "Altri campi dell'XSD"

    | Campo | Cardinalità | Tipo |
    |---|---|---|
    | `@nameOfRefClass` | 0..1 | `xsd:Name` |
    | `@created` | 0..1 | `xsd:dateTime` |
    | `@changed` | 0..1 | `xsd:dateTime` |
    | `@modification` | 0..1 | [`ModificationEnumeration`](enumerations.md#modificationenumeration) |
    | `@versionRef` | 0..1 | `xsd:normalizedString` |

### mobilityServiceConstraintZones / MobilityServiceConstraintZone {#mobilityserviceconstraintzones-mobilityserviceconstraintzone}

Linee guida §5.2.8.4 «mobilityServiceConstraintZones», Tabella 84. Tipo dell'XSD `MobilityServiceConstraintZone_VersionStructure`.

| Campo | Cardinalità | Tipo | Esempio | Significato (5T) | Fonte |
|---|---|---|---|---|---|
| `@id` | 1..1 | `xsd:normalizedString` | `IT:ITC1:MobilityServiceConstraintZone:BikeSharingTorino:msc:1` | Identificativo [→ Identificazione](common.md#identificazione) | §5.2.8.4, Tab. 84 |
| `@version` | 0..1 | `xsd:normalizedString` | `1` | Versione [→ Identificazione](common.md#identificazione) | §5.2.8.4, Tab. 84 |
| `gml:Polygon` | 0..1 | `gml:T_Polygon` |  | Geometria della zona | §5.2.8.4, Tab. 84 |
| `VehicleSharingServiceRef` → [VehicleSharingService](#mobilityservices-vehiclesharingservice) | 0..1 | `VehicleSharingServiceRefStructure` |  |  |  |
| `VehicleSharingServiceRef / @ref` → [VehicleSharingService](#mobilityservices-vehiclesharingservice) | 1..1 | `xsd:normalizedString` | `IT:ITC1:VehicleSharingService:BikeSharingTorino:VSS:1` | Id della modalità del servizio [⚠ Incongruenza](issues.md#84-netex-mobilityserviceframe-netex-mobilityserviceconstraintzones-netex-mobilityserviceconstraintzone-netex-vehiclesharingserviceref-ref) | §5.2.8.4, Tab. 84 |
| `VehicleSharingServiceRef / @version` → [VehicleSharingService](#mobilityservices-vehiclesharingservice) | 0..1 | `xsd:normalizedString` | `1` | Versione della modalità del servizio [⚠ Incongruenza](issues.md#84-netex-mobilityserviceframe-netex-mobilityserviceconstraintzones-netex-mobilityserviceconstraintzone-netex-vehiclesharingserviceref-version) | §5.2.8.4, Tab. 84 |

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
    | `Centroid` | 0..1 | `CentroidStructure` |
