---
generato: true
generato_da: rpsd-tools 0.8.0
---
<!-- GENERATED — DO NOT EDIT · profile-docs netex-it · netex-it-lev5@cecb0cd -->

# ResourceFrame

Organizzazioni, attrezzature e veicoli (linee guida §5.2.3).

## ResourceFrame {#resourceframe}

Linee guida §5.2.3 «ResourceFrame», Tabella 12. Tipo dell'XSD `ResourceFrameL4_VersionStructure`.

| Campo | Cardinalità | Tipo | Esempio | Significato (5T) | Fonte |
|---|---|---|---|---|---|
| `@id` | 1..1 | `xsd:normalizedString` | `epd:IT:ITC1:ResourceFrame_EU_PI_COMMON:ita` | Identificativo [→ Identificazione](common.md#identificazione) | §5.2.3, Tab. 12 |
| `@version` | 0..1 | `xsd:normalizedString` | `1` | Versione [→ Identificazione](common.md#identificazione) | §5.2.3, Tab. 12 |
| [`TypeOfFrameRef`](common.md#typeofframeref) | 0..1 | `TypeOfFrameRefStructure` |  |  |  |
| `responsibilitySets` | 0..1 | `responsibilitySetsL2_RelStructure` |  |  |  |
| [`responsibilitySets / ResponsibilitySet`](#responsibilitysets-responsibilityset) | 1..n | `ResponsibilitySetL2_VersionStructure` |  |  | §5.2.3.1, Tab. 13 |
| [`organisations`](#organisations-authority) | 0..1 | `organisationsL3Structure` |  |  |  |
| [`organisations`](#organisations-travelagent) | 0..1 | `organisationsL3Structure` |  |  |  |
| [`organisations`](#organisations-operator) | 0..1 | `organisationsL3Structure` |  |  |  |
| [`groupsOfOperators`](#groupsofoperators-groupofoperators) | 0..1 | `groupsOfOperatorsStructure` |  |  |  |
| [`equipments`](#equipments-communicationservice) | 0..1 | `equipmentsL2_RelStructure` |  |  |  |
| [`equipments`](#equipments-cyclestorageequipment) | 0..1 | `equipmentsL2_RelStructure` |  |  |  |
| [`equipments`](#equipments-escalatorequipment) | 0..1 | `equipmentsL2_RelStructure` |  |  |  |
| [`equipments`](#equipments-headingsign) | 0..1 | `equipmentsL2_RelStructure` |  |  |  |
| [`equipments`](#equipments-helppointequipment) | 0..1 | `equipmentsL2_RelStructure` |  |  |  |
| [`equipments`](#equipments-liftcallequipment) | 0..1 | `equipmentsL2_RelStructure` |  |  |  |
| [`equipments`](#equipments-liftequipment) | 0..1 | `equipmentsL2_RelStructure` |  |  |  |
| [`equipments`](#equipments-luggagelockerequipment) | 0..1 | `equipmentsL2_RelStructure` |  |  |  |
| [`equipments`](#equipments-passengerinformationequipment) | 0..1 | `equipmentsL2_RelStructure` |  |  |  |
| [`equipments`](#equipments-passengersafetyequipment) | 0..1 | `equipmentsL2_RelStructure` |  |  |  |
| [`equipments`](#equipments-rampequipment) | 0..1 | `equipmentsL2_RelStructure` |  |  |  |
| [`equipments`](#equipments-roughsurface) | 0..1 | `equipmentsL2_RelStructure` |  |  |  |
| [`equipments`](#equipments-shelterequipment) | 0..1 | `equipmentsL2_RelStructure` |  |  |  |
| [`equipments`](#equipments-staircaseequipment) | 0..1 | `equipmentsL2_RelStructure` |  |  |  |
| [`equipments`](#equipments-ticketingequipment) | 0..1 | `equipmentsL2_RelStructure` |  |  |  |
| [`equipments`](#equipments-ticketvalidatorequipment) | 0..1 | `equipmentsL2_RelStructure` |  |  |  |
| [`equipments`](#equipments-wheelchairvehicleequipment) | 0..1 | `equipmentsL2_RelStructure` |  |  |  |
| [`vehicleTypes`](#vehicletypes-vehicletype) | 0..1 | `vehicleTypesL2Structure` |  |  |  |
| [`vehicleTypes`](#vehicletypes-train) | 0..1 | `vehicleTypesL2Structure` |  |  |  |
| [`vehicleModels`](#vehiclemodels-vehiclemodel) | 0..1 | `vehicleModelsStructure` |  |  |  |
| [`vehicles`](#vehicles-vehicle) | 0..1 | `vehiclesL4Structure` |  |  |  |
| [`vehicleModelProfiles`](#vehiclemodelprofiles-cyclemodelprofile) | 0..1 | `vehicleModelProfilesStructure` |  |  |  |
| [`vehicleModelProfiles`](#vehiclemodelprofiles-carmodelprofile) | 0..1 | `vehicleModelProfilesStructure` |  |  |  |

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
    | `dataSources` | 0..1 | `dataSources_RelStructure` |
    | `typesOfValue` | 0..1 | `typesOfValue_RelStructure` |

### responsibilitySets / ResponsibilitySet {#responsibilitysets-responsibilityset}

Linee guida §5.2.3.1 «responsibilitySets», Tabella 13. Tipo dell'XSD `ResponsibilitySetL2_VersionStructure`.

| Campo | Cardinalità | Tipo | Esempio | Significato (5T) | Fonte |
|---|---|---|---|---|---|
| `@id` | 1..1 | `xsd:normalizedString` | `IT:ITC1:ResponsibilitySet:busATS:JourneyAccounting:1A` | Identificativo [→ Identificazione](common.md#identificazione) | §5.2.3.1, Tab. 13 (occorrenza 2) |
| `@version` | 0..1 | `xsd:normalizedString` | `1` | Versione [→ Identificazione](common.md#identificazione) | §5.2.3.1, Tab. 13 |
| `roles` | 1..1 | `rolesL2Structure` |  |  |  |
| [`roles / ResponsibilityRoleAssignment`](#responsibilitysets-responsibilityset-roles-responsibilityroleassignment) | 1..n | `ResponsibilityRoleAssignmentL2Structure` |  | Validità temporale del frame [⚠ Incongruenza](issues.md#13-netex-resourceframe-netex-responsibilitysets-netex-responsibilityset-netex-roles-netex-responsibilityroleassignment) | §5.2.3.1, Tab. 13 |

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
    | `PrivateCode` | 0..1 | `PrivateCodeStructure` |

#### roles / ResponsibilityRoleAssignment {#responsibilitysets-responsibilityset-roles-responsibilityroleassignment}

Linee guida §5.2.3.1 «responsibilitySets», Tabella 13. Tipo dell'XSD `ResponsibilityRoleAssignmentL2Structure`.

| Campo | Cardinalità | Tipo | Esempio | Significato (5T) | Fonte |
|---|---|---|---|---|---|
| `@id` | 0..1 | `xsd:normalizedString` | `IT:ITC1:busATS:ResponsibilityRoleAssignment:JourneyAccounting:1A:Affidante"` | Identificativo [→ Identificazione](common.md#identificazione) | §5.2.3.1, Tab. 13 (occorrenza 3) |
| `@version` | 0..1 | `xsd:normalizedString` | `1` | Versione [→ Identificazione](common.md#identificazione) | §5.2.3.1, Tab. 13 (occorrenza 2) |
| `StakeholderRoleType` | 0..1 | [`StakeholderRoleTypeListOfEnumerations`](enumerations.md#stakeholderroletypelistofenumerations) | `Control` | Riferimento alla tipologia di ruolo contrattuale | §5.2.3.1, Tab. 13 |
| `ResponsibleOrganisationRef` | 0..1 | `ResponsibleOrganisationRefStructure` | `IT:ITC1:busATS:Authority:AMP` | Riferimento all’organizzazione che ha uno specifico ruolo contrattuale | §5.2.3.1, Tab. 13 |
| `ResponsiblePartRef` | 0..1 | `ResponsiblePartRefStructure` | `IT:ITC1:busATS:JourneyAccounting:1A` | Riferimento al contratto di servizio (definito nel GeneralFrame) | §5.2.3.1, Tab. 13 |

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
    | `ResponsibilitySetRef` | 0..1 | `ResponsibilitySetRefStructure` |
    | `Description` | 0..1 | `MultilingualString` |
    | `DataRoleType` | 0..1 | [`DataRoleTypeListOfEnumerations`](enumerations.md#dataroletypelistofenumerations) |
    | `ResponsibleAreaRef` | 0..1 | `ResponsibleAreaRefStructure` |

### organisations / Authority {#organisations-authority}

Linee guida §5.2.3.2.1 «Authority», Tabella 14. Tipo dell'XSD `Authority_VersionStructure`.

| Campo | Cardinalità | Tipo | Esempio | Significato (5T) | Fonte |
|---|---|---|---|---|---|
| `@id` | 1..1 | `xsd:normalizedString` | `IT:ITC1:Authority:busATS:AMP` | Identificativo [→ Identificazione](common.md#identificazione) | §5.2.3.2.1, Tab. 14 |
| `@version` | 0..1 | `xsd:normalizedString` | `1` | Versione [→ Identificazione](common.md#identificazione) | §5.2.3.2.1, Tab. 14 |
| `Name` | 0..1 | `MultilingualString` | `Agenzia Mobilità Piemontese` | Nome che identifica l’ente | §5.2.3.2.1, Tab. 14 |
| `ShortName` | 0..1 | `MultilingualString` | `AMP` | Nome sintetico dell’ente | §5.2.3.2.1, Tab. 14 |
| [`ContactDetails`](common.md#contactdetails) | 1..1 | `ContactDetailsStructure` |  | Informazioni di contatto del referente valorizzate come descritto al paragrafo 4.3. | §5.2.3.2.1, Tab. 14 |
| `OrganisationType` | 1..1 | [`OrganisationTypeListOfEnumerations`](enumerations.md#organisationtypelistofenumerations) | `authority` | Descrive la tipologia di ente | §5.2.3.2.1, Tab. 14 |
| `Address` | 0..1 | `PostalAddress_VersionStructure` |  | Indirizzo dell’ente secondo la logica descritta al paragrafo 4.4. | §5.2.3.2.1, Tab. 14 |

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
    | `PublicCode` | 0..1 | `xsd:normalizedString` |
    | `CompanyNumber` | 0..1 | `xsd:normalizedString` |
    | `LegalName` | 0..1 | `MultilingualString` |
    | `alternativeNames` | 0..1 | `alternativeNamesStructure` |
    | `Description` | 0..1 | `MultilingualString` |

### organisations / TravelAgent {#organisations-travelagent}

Linee guida §5.2.3.2.2 «TravelAgent», Tabella 15. Tipo dell'XSD `TravelAgent_VersionStructure`.

| Campo | Cardinalità | Tipo | Esempio | Significato (5T) | Fonte |
|---|---|---|---|---|---|
| `@id` | 1..1 | `xsd:normalizedString` | `IT:ITC1:TravelAgent:busATS:11` | Identificativo [→ Identificazione](common.md#identificazione) | §5.2.3.2.2, Tab. 15 |
| `@version` | 0..1 | `xsd:normalizedString` | `1` | Versione [→ Identificazione](common.md#identificazione) | §5.2.3.2.2, Tab. 15 |
| `Name` | 0..1 | `MultilingualString` | `Autostradale S.r.l.` | Nome che identifica il rivenditore | §5.2.3.2.2, Tab. 15 |
| `ShortName` | 0..1 | `MultilingualString` | `Autostradale` | Nome sintetico del rivenditore | §5.2.3.2.2, Tab. 15 |
| [`ContactDetails`](common.md#contactdetails) | 1..1 | `ContactDetailsStructure` |  | Informazioni di contatto del referente valorizzate come descritto al paragrafo 4.3. | §5.2.3.2.2, Tab. 15 |
| `OrganisationType` | 1..1 | [`OrganisationTypeListOfEnumerations`](enumerations.md#organisationtypelistofenumerations) | `operator` | Descrive la tipologia di rivendita Valori del profilo: `authority`, `facilityOperator`, `operator`. [⚠ Incongruenza](issues.md#15-netex-resourceframe-netex-organisations-netex-travelagent-netex-organisationtype) | §5.2.3.2.2, Tab. 15 |
| `Address` | 0..1 | `RestrictedPostalAddress_VersionStructure` |  | Indirizzo dell’ente secondo la logica descritta al paragrafo 4.4. | §5.2.3.2.2, Tab. 15 |

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
    | `PublicCode` | 0..1 | `xsd:normalizedString` |
    | `PrivateCode` | 0..1 | `PrivateCodeStructure` |
    | `CompanyNumber` | 0..1 | `xsd:normalizedString` |
    | `LegalName` | 0..1 | `MultilingualString` |
    | `TradingName` | 0..1 | `MultilingualString` |
    | `alternativeNames` | 0..1 | `alternativeNamesStructure` |
    | `Description` | 0..1 | `MultilingualString` |
    | `CountryRef` | 0..1 | `CountryRefStructure` |
    | `PrimaryMode` | 0..1 | [`VehicleModeEnumeration`](enumerations.md#vehiclemodeenumeration) |
    | `departments` | 0..1 | `departments_RelStructure` |

### organisations / Operator {#organisations-operator}

Linee guida §5.2.3.2.3 «Operator», Tabella 16. Tipo dell'XSD `OperatorL2_VersionStructure`.

| Campo | Cardinalità | Tipo | Esempio | Significato (5T) | Fonte |
|---|---|---|---|---|---|
| `@id` | 1..1 | `xsd:normalizedString` | `IT:ITC1:Operator:metroATMMILANO:ATMMILANO` | Identificativo [→ Identificazione](common.md#identificazione) | §5.2.3.2.3, Tab. 16 |
| `@version` | 0..1 | `xsd:normalizedString` | `1` | Versione [→ Identificazione](common.md#identificazione) | §5.2.3.2.3, Tab. 16 |
| `PrivateCode` | 0..1 | `PrivateCodeStructure` | `ATMMilano` | Codice aziendale dell’operatore | §5.2.3.2.3, Tab. 16 |
| `Name` | 0..1 | `MultilingualString` | `ATMMilano` | Nome che identifica l’operatore | §5.2.3.2.3, Tab. 16 |
| `ShortName` | 0..1 | `MultilingualString` | `ATMMilano` | Nome sintetico dell’operatore | §5.2.3.2.3, Tab. 16 |
| `LegalName` | 0..1 | `MultilingualString` | `ATMMilano` | Denominazione legale dell’operatore | §5.2.3.2.3, Tab. 16 |
| `TradingName` | 0..1 | `MultilingualString` | `ATMMilano` | Denominazione commerciale dell’operatore | §5.2.3.2.3, Tab. 16 |
| [`ContactDetails`](common.md#contactdetails) | 1..1 | `ContactDetailsStructure` |  | Informazioni di contatto del referente aziendale valorizzate come descritto al paragrafo 4.3. | §5.2.3.2.3, Tab. 16 |
| `OrganisationType` | 1..1 | [`OrganisationTypeListOfEnumerations`](enumerations.md#organisationtypelistofenumerations) | `operator` | Descrive la tipologia di operatore Valori del profilo: `authority`, `facilityOperator`, `operator`. [⚠ Incongruenza](issues.md#16-netex-resourceframe-netex-organisations-netex-operator-netex-organisationtype) | §5.2.3.2.3, Tab. 16 |
| `Address` | 0..1 | `RestrictedPostalAddress_VersionStructure` |  | Indirizzo dell’ente secondo la logica descritta al paragrafo 4.4. | §5.2.3.2.3, Tab. 16 |
| `departments` | 0..1 | `departments_RelStructure` |  | Struttura contenente i reparti aziendali | §5.2.3.2.3, Tab. 16 |
| [`departments / Department`](#organisations-operator-departments-department) | 0..n · scelta 1 | `Department_VersionStructure` |  | Struttura del singolo reparto aziendale | §5.2.3.2.3, Tab. 16 |

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
    | `PublicCode` | 0..1 | `xsd:normalizedString` |
    | `CompanyNumber` | 0..1 | `xsd:normalizedString` |
    | `alternativeNames` | 0..1 | `alternativeNamesStructure` |
    | `Description` | 0..1 | `MultilingualString` |
    | `CountryRef` | 0..1 | `CountryRefStructure` |
    | `PrimaryMode` | 0..1 | [`VehicleModeEnumeration`](enumerations.md#vehiclemodeenumeration) |

#### departments / Department {#organisations-operator-departments-department}

Linee guida §5.2.3.2.3 «Operator», Tabella 16. Tipo dell'XSD `Department_VersionStructure`.

| Campo | Cardinalità | Tipo | Esempio | Significato (5T) | Fonte |
|---|---|---|---|---|---|
| `@id` | 1..1 | `xsd:normalizedString` | `IT:ITC1:Department:metroATMMILANO:FERROVIARIO_17_17` | Identificativo [→ Identificazione](common.md#identificazione) | §5.2.3.2.3, Tab. 16 (occorrenza 2) |
| `@version` | 0..1 | `xsd:normalizedString` | `1` | Versione [→ Identificazione](common.md#identificazione) | §5.2.3.2.3, Tab. 16 (occorrenza 2) |
| `Name` | 0..1 | `MultilingualString` | `Ferroviario` | Nome che identifica il reparto | §5.2.3.2.3, Tab. 16 (occorrenza 2) |
| `ShortName` | 0..1 | `MultilingualString` | `Ferroviario` | Nome sintetico il reparto | §5.2.3.2.3, Tab. 16 (occorrenza 2) |
| `Description` | 0..1 | `MultilingualString` | `Ferroviario` | Descrizione del reparto | §5.2.3.2.3, Tab. 16 |
| `PrivateCode` | 0..1 | `PrivateCodeStructure` | `Ferroviario` | Codice aziendale del reparto | §5.2.3.2.3, Tab. 16 (occorrenza 2) |

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
    | `units` | 0..1 | `organisationalUnitRefs_RelStructure` |

### groupsOfOperators / GroupOfOperators {#groupsofoperators-groupofoperators}

Linee guida §5.2.3.3 «groupsOfOperators - GroupOfOperators», Tabella 17. Tipo dell'XSD `GroupOfOperators_VersionStructure`.

| Campo | Cardinalità | Tipo | Esempio | Significato (5T) | Fonte |
|---|---|---|---|---|---|
| `@id` | 1..1 | `xsd:normalizedString` | `IT:ITC1:GroupOfOperators:busATS:Consortium:RP` | Identificativo [→ Identificazione](common.md#identificazione) | §5.2.3.3, Tab. 17 |
| `@version` | 0..1 | `xsd:normalizedString` | `1` | Versione [→ Identificazione](common.md#identificazione) | §5.2.3.3, Tab. 17 |
| `Name` | 0..1 | `MultilingualString` | `Consorzio Piemonte` | Nome che identifica il consorzio | §5.2.3.3, Tab. 17 |
| `ShortName` | 0..1 | `MultilingualString` | `CRP` | Nome sintetico del consorzio | §5.2.3.3, Tab. 17 |
| `Description` | 0..1 | `MultilingualString` | `Consorzio Piemonte` | Descrizione testuale del consorzio | §5.2.3.3, Tab. 17 |
| `PrivateCode` | 0..1 | `PrivateCodeStructure` | `CRP` | Codice del consorzio | §5.2.3.3, Tab. 17 |
| `members` | 0..1 | `operatorRefs_RelStructure` |  | Riferimenti a tutti gli Operatori che fanno parte del consorzio (vedi paragrafo 5.2.3.2.2) [⚠ Incongruenza](issues.md#17-netex-resourceframe-netex-groupsofoperators-netex-groupofoperators-netex-members) | §5.2.3.3, Tab. 17 |
| `members / OperatorRef` → [Operator](#organisations-operator) | 1..n | `OperatorRefStructure` | `IT:ITC1:Operator:busATS:11` | Riferimento ad un operatore (vedi paragrafo 5.2.3.2.2) | §5.2.3.3, Tab. 17 |

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

### equipments / CommunicationService {#equipments-communicationservice}

Linee guida §5.2.3.4.1 «CommunicationService», Tabella 18. Tipo dell'XSD `CommunicationService_VersionStructure`.

| Campo | Cardinalità | Tipo | Esempio | Significato (5T) | Fonte |
|---|---|---|---|---|---|
| `@id` | 1..1 | `xsd:normalizedString` | `IT:ITC1:CommunicationService:busATS:001` | Identificativo [→ Identificazione](common.md#identificazione) | §5.2.3.4.1, Tab. 18 |
| `@version` | 0..1 | `xsd:normalizedString` | `1` | Versione [→ Identificazione](common.md#identificazione) | §5.2.3.4.1, Tab. 18 |
| `ServiceList` | 1..1 | [`CommunicationServiceListOfEnumerations`](enumerations.md#communicationservicelistofenumerations) | `freeWifi audioEntertainment` | Nome che identifica il consorzio Valori del profilo: `audioEntertainment`, `businessServices`, `freeWifi`, `internet`, `mobileCoverage`, `phone`, `postOffice`, `publicWifi`, `videoEntertainment`. | §5.2.3.4.1, Tab. 18 |

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
    | `PrivateCode` | 0..1 | `PrivateCodeStructure` |
    | `PublicCode` | 0..1 | `PrivateCodeStructure` |
    | `Image` | 0..1 | `xsd:anyURI` |
    | `TypeOfEquipmentRef` | 0..1 | `TypeOfEquipmentRefStructure` |
    | `Description` | 0..1 | `MultilingualString` |
    | `Note` | 0..1 | `MultilingualString` |
    | `infoLinks` | 0..1 | `infoLinks_RelStructure` |
    | `OutOfService` | 0..1 | `xsd:boolean` |

### equipments / CycleStorageEquipment {#equipments-cyclestorageequipment}

Linee guida §5.2.3.4.2 «CycleStorageEquipment», Tabella 19. Tipo dell'XSD `CycleStorageEquipment_VersionStructure`.

| Campo | Cardinalità | Tipo | Esempio | Significato (5T) | Fonte |
|---|---|---|---|---|---|
| `@id` | 1..1 | `xsd:normalizedString` | `IT:ITC1:CycleStorageEquipments:busATS:1` | Identificativo [→ Identificazione](common.md#identificazione) | §5.2.3.4.2, Tab. 19 |
| `@version` | 0..1 | `xsd:normalizedString` | `1` | Versione [→ Identificazione](common.md#identificazione) | §5.2.3.4.2, Tab. 19 |
| `NumberOfSpaces` | 0..1 | `xsd:integer` | `5` | Numero di biciclette che possono essere parcheggiate o trasportate. | §5.2.3.4.2, Tab. 19 |
| `CycleStorageType` | 0..1 | [`CycleStorageEnumeration`](enumerations.md#cyclestorageenumeration) | `racks` | Tipo di fissaggio delle biciclette [⚠ Incongruenza](issues.md#19-netex-resourceframe-netex-equipments-netex-cyclestorageequipment-netex-cyclestoragetype) | §5.2.3.4.2, Tab. 19 |
| `Cage` | 0..1 | `xsd:boolean` | `true` | Sistema di parcheggio o trasporto chiuso | §5.2.3.4.2, Tab. 19 |
| `Covered` | 0..1 | `xsd:boolean` | `false` | Sistema di parcheggio o trasporto coperto | §5.2.3.4.2, Tab. 19 |

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
    | `PrivateCode` | 0..1 | `PrivateCodeStructure` |
    | `PublicCode` | 0..1 | `PrivateCodeStructure` |
    | `Image` | 0..1 | `xsd:anyURI` |
    | `TypeOfEquipmentRef` | 0..1 | `TypeOfEquipmentRefStructure` |
    | `Description` | 0..1 | `MultilingualString` |
    | `Note` | 0..1 | `MultilingualString` |
    | `infoLinks` | 0..1 | `infoLinks_RelStructure` |
    | `OutOfService` | 0..1 | `xsd:boolean` |

### equipments / EscalatorEquipment {#equipments-escalatorequipment}

Linee guida §5.2.3.4.3 «EscalatorEquipment», Tabella 20. Tipo dell'XSD `EscalatorEquipment_VersionStructure`.

| Campo | Cardinalità | Tipo | Esempio | Significato (5T) | Fonte |
|---|---|---|---|---|---|
| `@id` | 1..1 | `xsd:normalizedString` | `IT:ITC1:EscalatorEquipment:busATS:escalatore` | Identificativo [→ Identificazione](common.md#identificazione) | §5.2.3.4.3, Tab. 20 |
| `@version` | 0..1 | `xsd:normalizedString` | `1` | Versione [→ Identificazione](common.md#identificazione) | §5.2.3.4.3, Tab. 20 |
| `Width` | 0..1 | `LengthType` | `2.0` | Larghezza apparato | §5.2.3.4.3, Tab. 20 |
| `Height` | 0..1 | `LengthType` | `1.0` | Altezza apparato | §5.2.3.4.3, Tab. 20 |
| `PassengersPerMinute` | 0..1 | `xsd:integer` | `2` | Numero di passeggeri trasportabili al minuto [⚠ Incongruenza](issues.md#20-netex-resourceframe-netex-equipments-netex-escalatorequipment-netex-passengersperminute) | §5.2.3.4.3, Tab. 20 |
| `RelativeWeighting` | 0..1 | `xsd:integer` | `100` | Peso trasportabile | §5.2.3.4.3, Tab. 20 |
| `SafeForGuideDog` | 0..1 | `xsd:boolean` | `true` | Sicuro per i cani guida | §5.2.3.4.3, Tab. 20 |
| `Depth` | 0..1 | `LengthType` | `1.0` | Profondità gradini | §5.2.3.4.3, Tab. 20 |
| `NumberOfSteps` | 0..1 | `xsd:positiveInteger` | `50` | Numero di gradini | §5.2.3.4.3, Tab. 20 |
| `StepHeight` | 0..1 | `LengthType` | `0.20` | Altezza gradini | §5.2.3.4.3, Tab. 20 |
| `StepColourContrast` | 0..1 | `xsd:boolean` | `true` | Gradini con colori ad alto contrasto | §5.2.3.4.3, Tab. 20 |
| `StepCondition` | 0..1 | [`StepConditionEnumeration`](enumerations.md#stepconditionenumeration) | `even` | Tipo di superficie del gradino | §5.2.3.4.3, Tab. 20 |
| `HandrailType` | 0..1 | [`HandrailEnumeration`](enumerations.md#handrailenumeration) | `bothSides` | Presenza corrimano sui lati | §5.2.3.4.3, Tab. 20 |
| `TactileWriting` | 0..1 | `xsd:boolean` | `true` | Presenza di scritte in Braille | §5.2.3.4.3, Tab. 20 |
| `StairRamp` | 0..1 | [`StairRampEnumeration`](enumerations.md#stairrampenumeration) | `luggage` | Presenza di rampe aggiuntive distinte per tipologia | §5.2.3.4.3, Tab. 20 |
| `TactileActuators` | 0..1 | `xsd:boolean` | `true` | Presenza di bottoni con scritte in Braille | §5.2.3.4.3, Tab. 20 |
| `DogsMustBeCarried` | 0..1 | `xsd:boolean` | `true` | Necessità di portare i cani in braccio per la loro sicurezza | §5.2.3.4.3, Tab. 20 |
| `EnergySaving` | 0..1 | `xsd:boolean` | `true` | Presenza di sistemi di risparmio energetico | §5.2.3.4.3, Tab. 20 |
| `EscalatorWithLanding` | 0..1 | `xsd:boolean` | `true` | Presenza di piattaforma al termine dell’apparato | §5.2.3.4.3, Tab. 20 |
| `MonitoringRemoteControl` | 0..1 | `xsd:boolean` | `false` | Presenza di sistemi di controllo a distanza | §5.2.3.4.3, Tab. 20 |

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
    | `PrivateCode` | 0..1 | `PrivateCodeStructure` |
    | `PublicCode` | 0..1 | `PrivateCodeStructure` |
    | `Image` | 0..1 | `xsd:anyURI` |
    | `TypeOfEquipmentRef` | 0..1 | `TypeOfEquipmentRefStructure` |
    | `Description` | 0..1 | `MultilingualString` |
    | `Note` | 0..1 | `MultilingualString` |
    | `infoLinks` | 0..1 | `infoLinks_RelStructure` |
    | `OutOfService` | 0..1 | `xsd:boolean` |
    | `DirectionOfUse` | 0..1 | [`DirectionOfUseEnumeration`](enumerations.md#directionofuseenumeration) |
    | `StepLength` | 0..1 | `LengthType` |
    | `HandrailHeight` | 0..1 | `LengthType` |
    | `LowerHandrailHeight` | 0..1 | `LengthType` |
    | `TopEnd` | 0..1 | `StairEndStructure` |
    | `BottomEnd` | 0..1 | `StairEndStructure` |

### equipments / HeadingSign {#equipments-headingsign}

Linee guida §5.2.3.4.4 «HeadingSign», Tabella 21. Tipo dell'XSD `HeadingSign_VersionStructure`.

| Campo | Cardinalità | Tipo | Esempio | Significato (5T) | Fonte |
|---|---|---|---|---|---|
| `@id` | 1..1 | `xsd:normalizedString` | `IT:ITC1:HeadSign:busATS:1` | Identificativo [→ Identificazione](common.md#identificazione) | §5.2.3.4.4, Tab. 21 |
| `@version` | 0..1 | `xsd:normalizedString` | `1` | Versione [→ Identificazione](common.md#identificazione) | §5.2.3.4.4, Tab. 21 |
| [`ValidBetween`](common.md#validbetween) | 0..1 | `ValidBetween_VersionStructure` |  |  |  |
| `PlaceName` | 1..1 | `MultilingualString` | `Capolinea` | Destinazione descritta testualmente | §5.2.3.4.4, Tab. 21 |

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
    | `Name` | 0..1 | `MultilingualString` |
    | `PrivateCode` | 0..1 | `PrivateCodeStructure` |
    | `PublicCode` | 0..1 | `PrivateCodeStructure` |
    | `Image` | 0..1 | `xsd:anyURI` |
    | `TypeOfEquipmentRef` | 0..1 | `TypeOfEquipmentRefStructure` |
    | `Description` | 0..1 | `MultilingualString` |
    | `Note` | 0..1 | `MultilingualString` |
    | `infoLinks` | 0..1 | `infoLinks_RelStructure` |
    | `OutOfService` | 0..1 | `xsd:boolean` |
    | `Height` | 0..1 | `LengthType` |
    | `Width` | 0..1 | `LengthType` |
    | `HeightFromFloor` | 0..1 | `LengthType` |
    | `Placement` | 0..1 | `MultilingualString` |
    | `BrandGraphic` | 0..1 | `xsd:anyURI` |
    | `SignGraphic` | 0..1 | `xsd:anyURI` |
    | `MachineReadable` | 0..1 | `xsd:boolean` |
    | `AsBraille` | 0..1 | `xsd:boolean` |
    | `AudioTriggerMethod` | 0..1 | [`AudioTriggerMethodEnumeration`](enumerations.md#audiotriggermethodenumeration) |
    | `PrintedPresentation` | 0..1 | `PrintPresentationStructure` |
    | `Contrast` | 0..1 | `xsd:decimal` |
    | `FontSize` | 0..1 | [`FontSizeEnumeration`](enumerations.md#fontsizeenumeration) |
    | `LineRef` | 0..1 | `LineRefStructure` |
    | `FlexibleLineRef` | 0..1 | `LineRefStructure` |
    | `LineName` | 0..1 | `MultilingualString` |
    | `TransportMode` | 0..1 | [`AllVehicleModesOfTransportEnumeration`](enumerations.md#allvehiclemodesoftransportenumeration) |
    | `TransportSubmode` | 0..1 | `TransportSubmodeStructure` |
    | `LineMap` | 0..1 | `xsd:anyURI` |
    | `DirectionRef` | 0..1 | `DirectionRefStructure` |
    | `DirectionName` | 0..1 | `MultilingualString` |
    | `DestinationDisplayRef` | 0..1 | `DestinationDisplayRefStructure` |
    | `LinePublicCode` | 0..1 | `xsd:normalizedString` |

### equipments / HelpPointEquipment {#equipments-helppointequipment}

Linee guida §5.2.3.4.5 «HelpPointEquipment», Tabella 22. Tipo dell'XSD `HelpPointEquipment_VersionStructure`.

| Campo | Cardinalità | Tipo | Esempio | Significato (5T) | Fonte |
|---|---|---|---|---|---|
| `@id` | 1..1 | `xsd:normalizedString` | `IT:ITC1:HelpPointEquipment:busATS:001` | Identificativo [→ Identificazione](common.md#identificazione) | §5.2.3.4.5, Tab. 22 |
| `@version` | 0..1 | `xsd:normalizedString` | `1` | Versione [→ Identificazione](common.md#identificazione) | §5.2.3.4.5, Tab. 22 |
| `Phone` | 0..1 | `xsd:boolean` | `true` | Indica la presenza di servizio telefonico | §5.2.3.4.5, Tab. 22 |
| `StopRequestButton` | 0..1 | `xsd:boolean` | `true` | Indica la presenza di tasto per la richiesta della fermata | §5.2.3.4.5, Tab. 22 |

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
    | `PrivateCode` | 0..1 | `PrivateCodeStructure` |
    | `PublicCode` | 0..1 | `PrivateCodeStructure` |
    | `Image` | 0..1 | `xsd:anyURI` |
    | `TypeOfEquipmentRef` | 0..1 | `TypeOfEquipmentRefStructure` |
    | `Description` | 0..1 | `MultilingualString` |
    | `Note` | 0..1 | `MultilingualString` |
    | `infoLinks` | 0..1 | `infoLinks_RelStructure` |
    | `OutOfService` | 0..1 | `xsd:boolean` |
    | `Fixed` | 0..1 | `xsd:boolean` |
    | `AccessibilityAssessment` | 0..1 | `AccessibilityAssessmentStructure` |
    | `HeightFromGround` | 0..1 | `LengthType` |
    | `InductionLoop` | 0..1 | `xsd:boolean` |
    | `InductionLoopSign` | 0..1 | `xsd:boolean` |
    | `StopRequestTimeout` | 0..1 | `xsd:duration` |

### equipments / LiftCallEquipment {#equipments-liftcallequipment}

Linee guida §5.2.3.4.6 «LiftCallEquipment», Tabella 23. Tipo dell'XSD `LiftCallEquipment_VersionStructure`.

| Campo | Cardinalità | Tipo | Esempio | Significato (5T) | Fonte |
|---|---|---|---|---|---|
| `@id` | 1..1 | `xsd:normalizedString` | `IT:ITC1:LiftCallEquipment:busATS:001` | Identificativo [→ Identificazione](common.md#identificazione) | §5.2.3.4.6, Tab. 23 |
| `@version` | 0..1 | `xsd:normalizedString` | `1` | Versione [→ Identificazione](common.md#identificazione) | §5.2.3.4.6, Tab. 23 |
| `SafeForGuideDog` | 0..1 | `xsd:boolean` | `true` | Indica se sia sicuro per i cani guida | §5.2.3.4.6, Tab. 23 |
| `BrailleButtons` | 0..1 | `xsd:boolean` | `true` | Indica la presenza di tasto di chiamata con scritte in Braille | §5.2.3.4.6, Tab. 23 |
| `AudioAnnouncements` | 0..1 | `xsd:boolean` | `true` | Indica la presenza di annunci audio | §5.2.3.4.6, Tab. 23 |

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
    | `PrivateCode` | 0..1 | `PrivateCodeStructure` |
    | `PublicCode` | 0..1 | `PrivateCodeStructure` |
    | `Image` | 0..1 | `xsd:anyURI` |
    | `TypeOfEquipmentRef` | 0..1 | `TypeOfEquipmentRefStructure` |
    | `Description` | 0..1 | `MultilingualString` |
    | `Note` | 0..1 | `MultilingualString` |
    | `infoLinks` | 0..1 | `infoLinks_RelStructure` |
    | `OutOfService` | 0..1 | `xsd:boolean` |
    | `Width` | 0..1 | `LengthType` |
    | `Height` | 0..1 | `LengthType` |
    | `DirectionOfUse` | 0..1 | [`DirectionOfUseEnumeration`](enumerations.md#directionofuseenumeration) |
    | `PassengersPerMinute` | 0..1 | `xsd:integer` |
    | `RelativeWeighting` | 0..1 | `xsd:integer` |
    | `CallButtonHeight` | 0..1 | `LengthType` |
    | `RaisedButtons` | 0..1 | `xsd:boolean` |
    | `GroundMarkAlignedWithButton` | 0..1 | `xsd:boolean` |
    | `MagneticInductionLoop` | 0..1 | `xsd:boolean` |
    | `DoorOrientation` | 0..2 | [`CompassBearing8Enumeration`](enumerations.md#compassbearing8enumeration) |
    | `MonitoringRemoteControl` | 0..1 | `xsd:boolean` |

### equipments / LiftEquipment {#equipments-liftequipment}

Linee guida §5.2.3.4.7 «LiftEquipment», Tabella 24. Tipo dell'XSD `LiftEquipment_VersionStructure`.

| Campo | Cardinalità | Tipo | Esempio | Significato (5T) | Fonte |
|---|---|---|---|---|---|
| `@id` | 1..1 | `xsd:normalizedString` | `IT:ITC1:LiftEquipments:busATS:1` | Identificativo [→ Identificazione](common.md#identificazione) | §5.2.3.4.7, Tab. 24 |
| `@version` | 0..1 | `xsd:normalizedString` | `1` | Versione [→ Identificazione](common.md#identificazione) | §5.2.3.4.7, Tab. 24 |
| `WheelchairPassable` | 0..1 | `xsd:boolean` | `true` | Indica se sia utilizzabile con sedia a rotelle | §5.2.3.4.7, Tab. 24 |
| `RaisedButtons` | 0..1 | `xsd:boolean` | `true` | Indica la presenza di tasti in rilievo | §5.2.3.4.7, Tab. 24 |
| `BrailleButtons` | 0..1 | `xsd:boolean` | `true` | Indica la presenza di tasto di chiamata con scritte in Braille | §5.2.3.4.7, Tab. 24 |
| `AlarmButton` | 0..1 | `xsd:boolean` | `true` | Indica la presenza di tasto di emergenza [⚠ Incongruenza](issues.md#24-netex-resourceframe-netex-equipments-netex-liftequipment-netex-alarmbutton) | §5.2.3.4.7, Tab. 24 |
| `AudioAnnouncements` | 0..1 | `xsd:boolean` | `true` | Indica la presenza di annunci audio | §5.2.3.4.7, Tab. 24 |
| `ReachedFloorAnnouncement` | 0..1 | [`ReachedFloorAnnouncementEnumeration`](enumerations.md#reachedfloorannouncementenumeration) | `visualAndAudioAndTactile` | Indica la presenza di annunci di raggiungimento del piano specificando la tipologia | §5.2.3.4.7, Tab. 24 |

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
    | `PrivateCode` | 0..1 | `PrivateCodeStructure` |
    | `PublicCode` | 0..1 | `PrivateCodeStructure` |
    | `Image` | 0..1 | `xsd:anyURI` |
    | `TypeOfEquipmentRef` | 0..1 | `TypeOfEquipmentRefStructure` |
    | `Description` | 0..1 | `MultilingualString` |
    | `Note` | 0..1 | `MultilingualString` |
    | `infoLinks` | 0..1 | `infoLinks_RelStructure` |
    | `OutOfService` | 0..1 | `xsd:boolean` |
    | `Width` | 0..1 | `LengthType` |
    | `Height` | 0..1 | `LengthType` |
    | `DirectionOfUse` | 0..1 | [`DirectionOfUseEnumeration`](enumerations.md#directionofuseenumeration) |
    | `PassengersPerMinute` | 0..1 | `xsd:integer` |
    | `RelativeWeighting` | 0..1 | `xsd:integer` |
    | `SafeForGuideDog` | 0..1 | `xsd:boolean` |
    | `Depth` | 0..1 | `LengthType` |
    | `MaximumLoad` | 0..1 | `WeightType` |
    | `WheelchairTurningCircle` | 0..1 | `LengthType` |
    | `InternalWidth` | 0..1 | `LengthType` |
    | `InternalHeight` | 0..1 | `LengthType` |
    | `HandrailType` | 0..1 | [`HandrailEnumeration`](enumerations.md#handrailenumeration) |
    | `HandrailHeight` | 0..1 | `LengthType` |
    | `LowerHandrailHeight` | 0..1 | `LengthType` |
    | `TactileWriting` | 0..1 | `xsd:boolean` |
    | `CallButtonHeight` | 0..1 | `LengthType` |
    | `DirectionButtonHeight` | 0..1 | `LengthType` |
    | `TactileGroundFloorButton` | 0..1 | `xsd:boolean` |
    | `GroundMarkAlignedWithButton` | 0..1 | `xsd:boolean` |
    | `ThroughLoader` | 0..1 | `xsd:boolean` |
    | `MirrorOnOppositeSide` | 0..1 | `xsd:boolean` |
    | `Attendant` | 0..1 | `xsd:boolean` |
    | `Automatic` | 0..1 | `xsd:boolean` |
    | `ExternalFloorSelection` | 0..1 | `xsd:boolean` |
    | `TactileActuators` | 0..1 | `xsd:boolean` |
    | `AccousticAnnouncements` | 0..1 | `xsd:boolean` |
    | `MagneticInductionLoop` | 0..1 | `xsd:boolean` |
    | `SignageToLift` | 0..1 | `xsd:boolean` |
    | `SuitableForCycles` | 0..1 | `xsd:boolean` |
    | `ButtonsHeight` | 0..1 | `LengthType` |

### equipments / LuggageLockerEquipment {#equipments-luggagelockerequipment}

Linee guida §5.2.3.4.8 «LuggageLockerEquipment», Tabella 25. Tipo dell'XSD `LuggageLockerEquipment_VersionStructure`.

| Campo | Cardinalità | Tipo | Esempio | Significato (5T) | Fonte |
|---|---|---|---|---|---|
| `@id` | 1..1 | `xsd:normalizedString` | `IT:ITC1:LuggageLockerEquipments:busATS:1` | Identificativo [→ Identificazione](common.md#identificazione) | §5.2.3.4.8, Tab. 25 |
| `@version` | 0..1 | `xsd:normalizedString` | `1` | Versione [→ Identificazione](common.md#identificazione) | §5.2.3.4.8, Tab. 25 |
| `NumberOfLockers` | 0..1 | `xsd:integer` | `5` | Numero di spazi | §5.2.3.4.8, Tab. 25 |
| `LockerWidth` | 0..1 | `LengthType` | `50.0` | Larghezza spazi | §5.2.3.4.8, Tab. 25 |
| `LockerHeight` | 0..1 | `LengthType` | `100.0` | Altezza spazi | §5.2.3.4.8, Tab. 25 |
| `LockerDepth` | 0..1 | `LengthType` | `50.0` | Profondità spazi | §5.2.3.4.8, Tab. 25 |
| `LockerType` | 0..1 | [`LockerTypeEnumeration`](enumerations.md#lockertypeenumeration) | `visualAndAudioAndTactile` | Indica la tipologia di spazio Valori del profilo: `bikeCarriage`, `bikeRack`, `leftLuggageOffice`, `lockers`, `oversizeLockers`. [⚠ Incongruenza](issues.md#25-netex-resourceframe-netex-equipments-netex-luggagelockerequipment-netex-lockertype) | §5.2.3.4.8, Tab. 25 |
| `LockingType` | 0..1 | [`LockingTypeEnumeration`](enumerations.md#lockingtypeenumeration) | `key` | Indica la tipologia di serratura dello spazio | §5.2.3.4.8, Tab. 25 |

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
    | `PrivateCode` | 0..1 | `PrivateCodeStructure` |
    | `PublicCode` | 0..1 | `PrivateCodeStructure` |
    | `Image` | 0..1 | `xsd:anyURI` |
    | `TypeOfEquipmentRef` | 0..1 | `TypeOfEquipmentRefStructure` |
    | `Description` | 0..1 | `MultilingualString` |
    | `Note` | 0..1 | `MultilingualString` |
    | `infoLinks` | 0..1 | `infoLinks_RelStructure` |
    | `OutOfService` | 0..1 | `xsd:boolean` |
    | `WheelchairAccepted` | 0..1 | `xsd:boolean` |
    | `BlindAccessible` | 0..1 | `xsd:boolean` |

### equipments / PassengerInformationEquipment {#equipments-passengerinformationequipment}

Linee guida §5.2.3.4.9 «PassengerInformationEquipment», Tabella 26. Tipo dell'XSD `PassengerInformationEquipment_VersionStructure`.

| Campo | Cardinalità | Tipo | Esempio | Significato (5T) | Fonte |
|---|---|---|---|---|---|
| `@id` | 1..1 | `xsd:normalizedString` | `IT:ITC1:PassengerInformationEquipments:busATS:1` | Identificativo [→ Identificazione](common.md#identificazione) | §5.2.3.4.9, Tab. 26 |
| `@version` | 0..1 | `xsd:normalizedString` | `1` | Versione [→ Identificazione](common.md#identificazione) | §5.2.3.4.9, Tab. 26 |
| `PassengerInformationFacilityList` | 0..1 | [`PassengerInformationFacilityListOfEnumerations`](enumerations.md#passengerinformationfacilitylistofenumerations) | `passengerInformationDisplay realTimeConnections stopAnnouncements` | Tipolgia di sisteam [⚠ Incongruenza](issues.md#26-netex-resourceframe-netex-equipments-netex-passengerinformationequipment-netex-passengerinformationfacilitylist) | §5.2.3.4.9, Tab. 26 |

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
    | `PrivateCode` | 0..1 | `PrivateCodeStructure` |
    | `PublicCode` | 0..1 | `PrivateCodeStructure` |
    | `Image` | 0..1 | `xsd:anyURI` |
    | `TypeOfEquipmentRef` | 0..1 | `TypeOfEquipmentRefStructure` |
    | `Description` | 0..1 | `MultilingualString` |
    | `Note` | 0..1 | `MultilingualString` |
    | `infoLinks` | 0..1 | `infoLinks_RelStructure` |
    | `OutOfService` | 0..1 | `xsd:boolean` |
    | `Fixed` | 0..1 | `xsd:boolean` |
    | `LogicalDisplayRef` | 0..1 | `LogicalDisplayRefStructure` |
    | `StopPlaceRef` | 0..1 | `StopPlaceRefStructure` |
    | `SiteComponentRef` | 0..1 | `SiteComponentRefStructure` |
    | `PassengerInformationEquipmentList` | 0..1 | [`PassengerInformationEquipmentListOfEnumerations`](enumerations.md#passengerinformationequipmentlistofenumerations) |
    | `TypeOfPassengerInformationEquipmentRef` | 0..1 | `TypeOfPassengerInformationEquipmentRefStructure` |
    | `LowCounterAccess` | 0..1 | `xsd:boolean` |
    | `HeightOfLowCounter` | 0..1 | `LengthType` |
    | `InductionLoops` | 0..1 | `xsd:boolean` |
    | `TactileInterfaceAvailable` | 0..1 | `xsd:boolean` |
    | `AudioInterfaceAvailable` | 0..1 | `xsd:boolean` |
    | `DisabledPriority` | 0..1 | `xsd:boolean` |
    | `WheelchairSuitable` | 0..1 | `xsd:boolean` |
    | `AccessibilityInfoFacilityList` | 0..1 | [`AccessibilityInfoFacilityListOfEnumerations`](enumerations.md#accessibilityinfofacilitylistofenumerations) |

### equipments / PassengerSafetyEquipment {#equipments-passengersafetyequipment}

Linee guida §5.2.3.4.10 «PassengerSafetyEquipment», Tabella 27. Tipo dell'XSD `PassengerSafetyEquipment_VersionStructure`.

| Campo | Cardinalità | Tipo | Esempio | Significato (5T) | Fonte |
|---|---|---|---|---|---|
| `@id` | 1..1 | `xsd:normalizedString` | `IT:ITC1:PassengerSafetyEquipments:busATS:1` | Identificativo [→ Identificazione](common.md#identificazione) | §5.2.3.4.10, Tab. 27 |
| `@version` | 0..1 | `xsd:normalizedString` | `1` | Versione [→ Identificazione](common.md#identificazione) | §5.2.3.4.10, Tab. 27 |
| `Cctv` | 0..1 | `xsd:boolean` | `true` | Presenza di telecamere a circuito chiuso | §5.2.3.4.10, Tab. 27 |
| `PanicButton` | 0..1 | `xsd:boolean` | `true` | Presenza di tasti di emergenza | §5.2.3.4.10, Tab. 27 |
| `SosPanel` | 0..1 | `xsd:boolean` | `true` | Presenza di tasti per richiedere aiuto [⚠ Incongruenza](issues.md#27-netex-resourceframe-netex-equipments-netex-passengersafetyequipment-netex-sospanel) | §5.2.3.4.10, Tab. 27 |

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
    | `PrivateCode` | 0..1 | `PrivateCodeStructure` |
    | `PublicCode` | 0..1 | `PrivateCodeStructure` |
    | `Image` | 0..1 | `xsd:anyURI` |
    | `TypeOfEquipmentRef` | 0..1 | `TypeOfEquipmentRefStructure` |
    | `Description` | 0..1 | `MultilingualString` |
    | `Note` | 0..1 | `MultilingualString` |
    | `infoLinks` | 0..1 | `infoLinks_RelStructure` |
    | `OutOfService` | 0..1 | `xsd:boolean` |
    | `Fixed` | 0..1 | `xsd:boolean` |
    | `MobilePhoneCoverage` | 0..1 | `xsd:boolean` |
    | `HeightOfSosPanel` | 0..1 | `LengthType` |
    | `Lighting` | 0..1 | [`LightingEnumeration`](enumerations.md#lightingenumeration) |
    | `AudioAnnouncements` | 0..1 | `xsd:boolean` |
    | `AcousticAnnouncements` | 0..1 | `xsd:boolean` |
    | `AudioAnnouncementType` | 0..1 | [`AudioAnnouncementTypeEnumeration`](enumerations.md#audioannouncementtypeenumeration) |
    | `AudioAnnouncementsTrigger` | 0..1 | [`AudioTriggerMethodEnumeration`](enumerations.md#audiotriggermethodenumeration) |

### equipments / RampEquipment {#equipments-rampequipment}

Linee guida §5.2.3.4.11 «RampEquipment», Tabella 28. Tipo dell'XSD `RampEquipment_VersionStructure`.

| Campo | Cardinalità | Tipo | Esempio | Significato (5T) | Fonte |
|---|---|---|---|---|---|
| `@id` | 1..1 | `xsd:normalizedString` | `IT:ITC1:RampEquipments:busATS:1` | Identificativo [→ Identificazione](common.md#identificazione) | §5.2.3.4.11, Tab. 28 |
| `@version` | 0..1 | `xsd:normalizedString` | `1` | Versione [→ Identificazione](common.md#identificazione) | §5.2.3.4.11, Tab. 28 |
| `HandrailType` | 0..1 | [`HandrailEnumeration`](enumerations.md#handrailenumeration) | `bothSides` | Presenza corrimano sui lati [⚠ Incongruenza](issues.md#28-netex-resourceframe-netex-equipments-netex-rampequipment-netex-handrailtype) | §5.2.3.4.11, Tab. 28 |
| `TactileGuidanceStrips` | 0..1 | `xsd:boolean` | `true` | Presenza di cammino tattile [⚠ Incongruenza](issues.md#28-netex-resourceframe-netex-equipments-netex-rampequipment-netex-tactileguidancestrips) | §5.2.3.4.11, Tab. 28 |
| `VisualGuidanceBands` | 0..1 | `xsd:boolean` | `true` | Presenza di guide visuali | §5.2.3.4.11, Tab. 28 |
| `SuitableForCycles` | 0..1 | `xsd:boolean` | `true` | Adatto al transito delle biciclette | §5.2.3.4.11, Tab. 28 |
| `RestStopDistance` | 0..1 | `LengthType` | `10.0` | Distanza massima fra due livelli | §5.2.3.4.11, Tab. 28 |
| `SafetyEdge` | 0..1 | [`SafetyEdgeEnumeration`](enumerations.md#safetyedgeenumeration) | `bothSides` | Presenza di bordi rialzati | §5.2.3.4.11, Tab. 28 |
| `TurningSpace` | 0..1 | [`RampTurningSpacePositionEnumeration`](enumerations.md#rampturningspacepositionenumeration) | `botton` | Presenza di spazio per manovrare [⚠ Incongruenza](issues.md#28-netex-resourceframe-netex-equipments-netex-rampequipment-netex-turningspace) | §5.2.3.4.11, Tab. 28 |

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
    | `PrivateCode` | 0..1 | `PrivateCodeStructure` |
    | `PublicCode` | 0..1 | `PrivateCodeStructure` |
    | `Image` | 0..1 | `xsd:anyURI` |
    | `TypeOfEquipmentRef` | 0..1 | `TypeOfEquipmentRefStructure` |
    | `Description` | 0..1 | `MultilingualString` |
    | `Note` | 0..1 | `MultilingualString` |
    | `infoLinks` | 0..1 | `infoLinks_RelStructure` |
    | `OutOfService` | 0..1 | `xsd:boolean` |
    | `Width` | 0..1 | `LengthType` |
    | `Height` | 0..1 | `LengthType` |
    | `DirectionOfUse` | 0..1 | [`DirectionOfUseEnumeration`](enumerations.md#directionofuseenumeration) |
    | `PassengersPerMinute` | 0..1 | `xsd:integer` |
    | `RelativeWeighting` | 0..1 | `xsd:integer` |
    | `SafeForGuideDog` | 0..1 | `xsd:boolean` |
    | `Length` | 0..1 | `LengthType` |
    | `MaximumLoad` | 0..1 | `WeightType` |
    | `Gradient` | 0..1 | `xsd:positiveInteger` |
    | `GradientType` | 0..1 | [`GradientEnumeration`](enumerations.md#gradientenumeration) |
    | `Pedestal` | 0..1 | `xsd:boolean` |
    | `HandrailHeight` | 0..1 | `LengthType` |
    | `LowerHandrailHeight` | 0..1 | `LengthType` |
    | `TactileWriting` | 0..1 | `xsd:boolean` |
    | `Temporary` | 0..1 | `xsd:boolean` |

### equipments / RoughSurface {#equipments-roughsurface}

Linee guida §5.2.3.4.12 «RoughSurface», Tabella 29. Tipo dell'XSD `RoughSurface_VersionStructure`.

| Campo | Cardinalità | Tipo | Esempio | Significato (5T) | Fonte |
|---|---|---|---|---|---|
| `@id` | 1..1 | `xsd:normalizedString` | `IT:ITC1:RoughSurface:busATS:001` | Identificativo [→ Identificazione](common.md#identificazione) | §5.2.3.4.12, Tab. 29 |
| `@version` | 0..1 | `xsd:normalizedString` | `1` | Versione [→ Identificazione](common.md#identificazione) | §5.2.3.4.12, Tab. 29 |
| `SurfaceType` | 1..1 | [`SurfaceTypeEnumeration`](enumerations.md#surfacetypeenumeration) | `roughSurface` | Tipologia di superficie [⚠ Incongruenza](issues.md#29-netex-resourceframe-netex-equipments-netex-roughsurface-netex-surfacetype) | §5.2.3.4.12, Tab. 29 |

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
    | `PrivateCode` | 0..1 | `PrivateCodeStructure` |
    | `PublicCode` | 0..1 | `PrivateCodeStructure` |
    | `Image` | 0..1 | `xsd:anyURI` |
    | `TypeOfEquipmentRef` | 0..1 | `TypeOfEquipmentRefStructure` |
    | `Description` | 0..1 | `MultilingualString` |
    | `Note` | 0..1 | `MultilingualString` |
    | `infoLinks` | 0..1 | `infoLinks_RelStructure` |
    | `OutOfService` | 0..1 | `xsd:boolean` |
    | `Width` | 0..1 | `LengthType` |
    | `Height` | 0..1 | `LengthType` |
    | `DirectionOfUse` | 0..1 | [`DirectionOfUseEnumeration`](enumerations.md#directionofuseenumeration) |
    | `PassengersPerMinute` | 0..1 | `xsd:integer` |
    | `RelativeWeighting` | 0..1 | `xsd:integer` |
    | `SafeForGuideDog` | 0..1 | `xsd:boolean` |
    | `VisualContrast` | 0..1 | `xsd:boolean` |
    | `SuitableForCycles` | 0..1 | `xsd:boolean` |

### equipments / ShelterEquipment {#equipments-shelterequipment}

Linee guida §5.2.3.4.13 «SheltherEquipment», Tabella 30. Tipo dell'XSD `ShelterEquipment_VersionStructure`.

| Campo | Cardinalità | Tipo | Esempio | Significato (5T) | Fonte |
|---|---|---|---|---|---|
| `@id` | 1..1 | `xsd:normalizedString` | `IT:ITC1:SheltherEquipments:busATS:1` | Identificativo [→ Identificazione](common.md#identificazione) | §5.2.3.4.13, Tab. 30 |
| `@version` | 0..1 | `xsd:normalizedString` | `1` | Versione [→ Identificazione](common.md#identificazione) | §5.2.3.4.13, Tab. 30 |
| `Seats` | 0..1 | `xsd:nonNegativeInteger` | `50` | Numero di posti a sedere | §5.2.3.4.13, Tab. 30 |
| `WheelchairAreaWidth` | 0..1 | `LengthType` | `1` | Ampiezza dello spazio per la sedia a rotella | §5.2.3.4.13, Tab. 30 |
| `WheelchairAreaLength` | 0..1 | `LengthType` | `0.8` | Lunghezza dello spazio per la sedia a rotella | §5.2.3.4.13, Tab. 30 |
| `AirConditioned` | 0..1 | `xsd:boolean` | `true` | Presenza di condizionamento dell’aria | §5.2.3.4.13, Tab. 30 |

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
    | `PrivateCode` | 0..1 | `PrivateCodeStructure` |
    | `PublicCode` | 0..1 | `PrivateCodeStructure` |
    | `Image` | 0..1 | `xsd:anyURI` |
    | `TypeOfEquipmentRef` | 0..1 | `TypeOfEquipmentRefStructure` |
    | `Description` | 0..1 | `MultilingualString` |
    | `Note` | 0..1 | `MultilingualString` |
    | `infoLinks` | 0..1 | `infoLinks_RelStructure` |
    | `OutOfService` | 0..1 | `xsd:boolean` |
    | `Width` | 0..1 | `LengthType` |
    | `Length` | 0..1 | `LengthType` |
    | `StepFree` | 0..1 | `xsd:boolean` |
    | `SmokingAllowed` | 0..1 | `xsd:boolean` |
    | `Heated` | 0..1 | `xsd:boolean` |
    | `Enclosed` | 0..1 | `xsd:boolean` |
    | `DistanceFromNearestKerb` | 0..1 | `LengthType` |

### equipments / StaircaseEquipment {#equipments-staircaseequipment}

Linee guida §5.2.3.4.14 «StaircaseEquipment», Tabella 31. Tipo dell'XSD `StaircaseEquipment_VersionStructure`.

| Campo | Cardinalità | Tipo | Esempio | Significato (5T) | Fonte |
|---|---|---|---|---|---|
| `@id` | 1..1 | `xsd:normalizedString` | `IT:ITC1:StaircaseEquipment:busATS:001` | Identificativo [→ Identificazione](common.md#identificazione) | §5.2.3.4.14, Tab. 31 |
| `@version` | 0..1 | `xsd:normalizedString` | `1` | Versione [→ Identificazione](common.md#identificazione) | §5.2.3.4.14, Tab. 31 |
| `SafeForGuideDog` | 0..1 | `xsd:boolean` | `true` | Indica se la scala sia sicura per cani guida [⚠ Incongruenza](issues.md#31-netex-resourceframe-netex-equipments-netex-staircaseequipment-netex-safeforguidedog) | §5.2.3.4.14, Tab. 31 |
| `NumberOfSteps` | 0..1 | `xsd:positiveInteger` | `5` | Indica il numero degli scalini | §5.2.3.4.14, Tab. 31 |
| `HandrailType` | 0..1 | [`HandrailEnumeration`](enumerations.md#handrailenumeration) | `bothSides` | Indica la presenza del corrimano e la sua posizione | §5.2.3.4.14, Tab. 31 |
| `TactileWriting` | 0..1 | `xsd:boolean` | `true` | Indica la presenza di cartelli con indicazioni in Braille | §5.2.3.4.14, Tab. 31 |

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
    | `PrivateCode` | 0..1 | `PrivateCodeStructure` |
    | `PublicCode` | 0..1 | `PrivateCodeStructure` |
    | `Image` | 0..1 | `xsd:anyURI` |
    | `TypeOfEquipmentRef` | 0..1 | `TypeOfEquipmentRefStructure` |
    | `Description` | 0..1 | `MultilingualString` |
    | `Note` | 0..1 | `MultilingualString` |
    | `infoLinks` | 0..1 | `infoLinks_RelStructure` |
    | `OutOfService` | 0..1 | `xsd:boolean` |
    | `Width` | 0..1 | `LengthType` |
    | `Height` | 0..1 | `LengthType` |
    | `DirectionOfUse` | 0..1 | [`DirectionOfUseEnumeration`](enumerations.md#directionofuseenumeration) |
    | `PassengersPerMinute` | 0..1 | `xsd:integer` |
    | `RelativeWeighting` | 0..1 | `xsd:integer` |
    | `Depth` | 0..1 | `LengthType` |
    | `StepHeight` | 0..1 | `LengthType` |
    | `StepLength` | 0..1 | `LengthType` |
    | `StepColourContrast` | 0..1 | `xsd:boolean` |
    | `StepCondition` | 0..1 | [`StepConditionEnumeration`](enumerations.md#stepconditionenumeration) |
    | `HandrailHeight` | 0..1 | `LengthType` |
    | `LowerHandrailHeight` | 0..1 | `LengthType` |
    | `StairRamp` | 0..1 | [`StairRampEnumeration`](enumerations.md#stairrampenumeration) |
    | `TopEnd` | 0..1 | `StairEndStructure` |
    | `BottomEnd` | 0..1 | `StairEndStructure` |
    | `ContinuousHandrail` | 0..1 | `xsd:boolean` |
    | `WithoutRiser` | 0..1 | `xsd:boolean` |
    | `SpiralStair` | 0..1 | `xsd:boolean` |
    | `NumberOfFlights` | 0..1 | `xsd:integer` |
    | `flights` | 0..1 | `stairFlights_RelStructure` |

### equipments / TicketingEquipment {#equipments-ticketingequipment}

Linee guida §5.2.3.4.15 «TicketingEquipment», Tabella 32. Tipo dell'XSD `TicketingEquipment_VersionStructure`.

| Campo | Cardinalità | Tipo | Esempio | Significato (5T) | Fonte |
|---|---|---|---|---|---|
| `@id` | 1..1 | `xsd:normalizedString` | `IT:ITC1:TicketingEquipment:busATS:001` | Identificativo [→ Identificazione](common.md#identificazione) | §5.2.3.4.15, Tab. 32 |
| `@version` | 0..1 | `xsd:normalizedString` | `1` | Versione [→ Identificazione](common.md#identificazione) | §5.2.3.4.15, Tab. 32 |
| `NumberOfMachines` | 0..1 | `xsd:integer` | `5` | Indica il numero degli apparati di vendita | §5.2.3.4.15, Tab. 32 |
| `NumberOfTills` | 0..1 | `xsd:integer` | `5` | Indica il numero degli sportelli di vendita | §5.2.3.4.15, Tab. 32 |
| `PaymentMethods` | 0..1 | [`PaymentMethodListOfEnumerationsL2`](enumerations.md#paymentmethodlistofenumerationsl2) | `cash cheque` | Indica le modalità di pagamento accettate [⚠ Incongruenza](issues.md#32-netex-resourceframe-netex-equipments-netex-ticketingequipment-netex-paymentmethods) | §5.2.3.4.15, Tab. 32 |
| `TicketTypesAvailable` | 0..1 | [`TicketTypeListOfEnumerations`](enumerations.md#tickettypelistofenumerations) | `carnet promotion` | Indica i tipi di biglietti vendibili | §5.2.3.4.15, Tab. 32 |
| `AudioInterfaceAvailable` | 0..1 | `xsd:boolean` | `true` | Indica la disponibilità di guida vocale [⚠ Incongruenza](issues.md#32-netex-resourceframe-netex-equipments-netex-ticketingequipment-netex-audiointerfaceavailable) | §5.2.3.4.15, Tab. 32 |
| `WheelchairSuitable` | 0..1 | `xsd:boolean` | `true` | Indica se l’apparato di vendita è accessibile stando seduti su sedia a rotelle | §5.2.3.4.15, Tab. 32 |

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
    | `PrivateCode` | 0..1 | `PrivateCodeStructure` |
    | `PublicCode` | 0..1 | `PrivateCodeStructure` |
    | `Image` | 0..1 | `xsd:anyURI` |
    | `TypeOfEquipmentRef` | 0..1 | `TypeOfEquipmentRefStructure` |
    | `Description` | 0..1 | `MultilingualString` |
    | `Note` | 0..1 | `MultilingualString` |
    | `infoLinks` | 0..1 | `infoLinks_RelStructure` |
    | `OutOfService` | 0..1 | `xsd:boolean` |
    | `Fixed` | 0..1 | `xsd:boolean` |
    | `VehicleModes` | 0..1 | [`AllModesListOfEnumerations`](enumerations.md#allmodeslistofenumerations) |
    | `TicketMachines` | 0..1 | `xsd:boolean` |
    | `HeightOfMachineInterface` | 0..1 | `LengthType` |
    | `TicketingFacilityList` | 0..1 | [`TicketingFacilityListOfEnumerations`](enumerations.md#ticketingfacilitylistofenumerations) |
    | `TicketingServiceFacilityList` | 0..1 | [`TicketingServiceFacilityListOfEnumerations`](enumerations.md#ticketingservicefacilitylistofenumerations) |
    | `TicketOffice` | 0..1 | `xsd:boolean` |
    | `TicketCounter` | 0..1 | `xsd:boolean` |
    | `QueueManagement` | 0..1 | [`QueueManagementEnumeration`](enumerations.md#queuemanagementenumeration) |
    | `ScopeOfTicketsAvailable` | 0..1 | [`ScopeOfTicketListOfEnumerationsL2`](enumerations.md#scopeofticketlistofenumerationsl2) |
    | `LowCounterAccess` | 0..1 | `xsd:boolean` |
    | `HeightOfLowCounter` | 0..1 | `LengthType` |
    | `InductionLoops` | 0..1 | `xsd:boolean` |
    | `TactileInterfaceAvailable` | 0..1 | `xsd:boolean` |
    | `DisabledPriority` | 0..1 | `xsd:boolean` |

### equipments / TicketValidatorEquipment {#equipments-ticketvalidatorequipment}

Linee guida §5.2.3.4.16 «TicketValidatorEquipment», Tabella 33. Tipo dell'XSD `TicketValidatorEquipment_VersionStructure`.

| Campo | Cardinalità | Tipo | Esempio | Significato (5T) | Fonte |
|---|---|---|---|---|---|
| `@id` | 1..1 | `xsd:normalizedString` | `IT:ITC1:TicketingEquipment:busATS:001` | Identificativo [→ Identificazione](common.md#identificazione) | §5.2.3.4.16, Tab. 33 |
| `@version` | 0..1 | `xsd:normalizedString` | `1` | Versione [→ Identificazione](common.md#identificazione) | §5.2.3.4.16, Tab. 33 |
| `TicketValidatorType` | 0..1 | [`TicketValidatorListOfEnumerations`](enumerations.md#ticketvalidatorlistofenumerations) | `contactless magnetic` | Indica le modalità di validazione possibili [⚠ Incongruenza](issues.md#33-netex-resourceframe-netex-equipments-netex-ticketvalidatorequipment-netex-ticketvalidatortype) | §5.2.3.4.16, Tab. 33 |
| `AudioValidationFeedback` | 0..1 | `xsd:boolean` | `true` | Indica la presenza di feedback vocale | §5.2.3.4.16, Tab. 33 |
| `VisualValidationFeedback` | 0..1 | `xsd:boolean` | `true` | Indica la presenza di feedback visivo | §5.2.3.4.16, Tab. 33 |

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
    | `PrivateCode` | 0..1 | `PrivateCodeStructure` |
    | `PublicCode` | 0..1 | `PrivateCodeStructure` |
    | `Image` | 0..1 | `xsd:anyURI` |
    | `TypeOfEquipmentRef` | 0..1 | `TypeOfEquipmentRefStructure` |
    | `Description` | 0..1 | `MultilingualString` |
    | `Note` | 0..1 | `MultilingualString` |
    | `infoLinks` | 0..1 | `infoLinks_RelStructure` |
    | `OutOfService` | 0..1 | `xsd:boolean` |
    | `Fixed` | 0..1 | `xsd:boolean` |
    | `TactileValidationFeedback` | 0..1 | `xsd:boolean` |
    | `ValidationGuidance` | 0..1 | `MultilingualString` |

### equipments / WheelchairVehicleEquipment {#equipments-wheelchairvehicleequipment}

Linee guida §5.2.3.4.17 «WheelchairVehicleEquipment», Tabella 34. Tipo dell'XSD `WheelchairVehicleEquipment_VersionStructure`.

| Campo | Cardinalità | Tipo | Esempio | Significato (5T) | Fonte |
|---|---|---|---|---|---|
| `@id` | 1..1 | `xsd:normalizedString` | `IT:ITC1:TicketingEquipment:busATS:001` | Identificativo [→ Identificazione](common.md#identificazione) | §5.2.3.4.17, Tab. 34 |
| `@version` | 0..1 | `xsd:normalizedString` | `1` | Versione [→ Identificazione](common.md#identificazione) | §5.2.3.4.17, Tab. 34 |
| `HasWheelchairSpaces` | 0..1 | `xsd:boolean` | `true` | Indica se siano presenti spazi per sedia a rotelle. | §5.2.3.4.17, Tab. 34 |
| `WidthOfAccessArea` | 0..1 | `LengthType` | `0.8` | Indica la larghezza dello spazio di accesso per la sedia a rotelle. | §5.2.3.4.17, Tab. 34 |
| `LengthOfAccessArea` | 0..1 | `LengthType` | `1` | Indica la lunghezza dello spazio di accesso per la sedia a rotelle. | §5.2.3.4.17, Tab. 34 |
| `HeightOfAccessArea` | 0..1 | `LengthType` | `1` | Indica l’altezza dello spazio di accesso per la sedia a rotelle. | §5.2.3.4.17, Tab. 34 |
| `WheelchairTurningCircle` | 0..1 | `LengthType` | `1` | Indica il raggio di rotazione per la sedia a rotelle. | §5.2.3.4.17, Tab. 34 |
| `CompanionSeat` | 0..1 | `xsd:boolean` | `true` | Indica se sia presente un posto a sedere accanto alla sedia a rotelle. | §5.2.3.4.17, Tab. 34 |

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
    | `PrivateCode` | 0..1 | `PrivateCodeStructure` |
    | `PublicCode` | 0..1 | `PrivateCodeStructure` |
    | `Image` | 0..1 | `xsd:anyURI` |
    | `TypeOfEquipmentRef` | 0..1 | `TypeOfEquipmentRefStructure` |
    | `Description` | 0..1 | `MultilingualString` |
    | `Note` | 0..1 | `MultilingualString` |
    | `infoLinks` | 0..1 | `infoLinks_RelStructure` |
    | `OutOfService` | 0..1 | `xsd:boolean` |
    | `Fixed` | 0..1 | `xsd:boolean` |
    | `Units` | 0..1 | `xsd:integer` |
    | `VehicleTypeRef` | 0..1 | `VehicleTypeRefStructure` |
    | `EquipmentRef` | 0..1 | `EquipmentRefStructure` |
    | `AccessVehicleEquipmentRef` | 0..1 | `AccessVehicleEquipmentRefStructure` |
    | `AssistanceServiceRef` | 0..1 | `AssistanceServiceRefStructure` |
    | `CommunicationServiceRef` | 0..1 | `CommunicationServiceRefStructure` |
    | `CycleStorageEquipmentRef` | 0..1 | `CycleStorageEquipmentRefStructure` |
    | `EntranceEquipmentRef` | 0..1 | `EntranceEquipmentRefStructure` |
    | `EscalatorEquipmentRef` | 0..1 | `EscalatorEquipmentRefStructure` |
    | `HeadingSignRef` | 0..1 | `HeadingSignRefStructure` |
    | `HelpPointEquipmentRef` | 0..1 | `HelpPointEquipmentRefStructure` |
    | `LiftCallEquipmentRef` | 0..1 | `LiftCallEquipmentRefStructure` |
    | `LiftEquipmentRef` | 0..1 | `LiftEquipmentRefStructure` |
    | `LuggageLockerEquipmentRef` | 0..1 | `LuggageLockerEquipmentRefStructure` |
    | `PassengerInformationEquipmentRef` | 0..1 | `PassengerInformationEquipmentRefStructure` |
    | `PassengerSafetyEquipmentRef` | 0..1 | `PassengerSafetyEquipmentRefStructure` |
    | `RampEquipmentRef` | 0..1 | `RampEquipmentRefStructure` |
    | `RoughSurfaceRef` | 0..1 | `RoughSurfaceRefStructure` |
    | `ShelterEquipmentRef` | 0..1 | `ShelterEquipmentRefStructure` |
    | `StaircaseEquipmentRef` | 0..1 | `StaircaseEquipmentRefStructure` |
    | `TicketValidatorEquipmentRef` | 0..1 | `TicketValidatorEquipmentRefStructure` |
    | `TicketingEquipmentRef` | 0..1 | `TicketingEquipmentRefStructure` |
    | `WheelchairVehicleRef` | 0..1 | `WheelchairVehicleRefStructure` |
    | `AccessibilityAssessment` | 0..1 | `AccessibilityAssessmentL5Structure` |
    | `NumberOfWheelchairAreas` | 0..1 | `xsd:nonNegativeInteger` |

### vehicleTypes / VehicleType {#vehicletypes-vehicletype}

Linee guida §5.2.3.5.1 «Sottostruttura VehicleType», Tabella 35. Tipo dell'XSD `VehicleTypeL2_VersionStructure`.

| Campo | Cardinalità | Tipo | Esempio | Significato (5T) | Fonte |
|---|---|---|---|---|---|
| `@id` | 1..1 | `xsd:normalizedString` | `IT:ITC1:VehicleType:busATS:001` | Identificativo [→ Identificazione](common.md#identificazione) [⚠ Incongruenza](issues.md#35-netex-resourceframe-netex-vehicletypes-netex-vehicletype-id) | §5.2.3.5.1, Tab. 35 |
| `@version` | 0..1 | `xsd:normalizedString` | `1` | Versione [→ Identificazione](common.md#identificazione) [⚠ Incongruenza](issues.md#35-netex-resourceframe-netex-vehicletypes-netex-vehicletype-version) | §5.2.3.5.1, Tab. 35 |
| `PrivateCode` | 0..1 | `PrivateCodeStructure` | `001` | Codice aziendale univoco della tipologia di veicolo | §5.2.3.5.1, Tab. 35 |
| `FuelType` | 0..1 | [`FuelTypeEnumeration`](enumerations.md#fueltypeenumeration) | `diesel` | Tipo di alimentazione del veicolo | §5.2.3.5.1, Tab. 35 |
| `EuroClass` | 0..1 | `xsd:normalizedString` | `Euro5` | Classe Euro del veicolo | §5.2.3.5.1, Tab. 35 |
| `capacities` | 0..1 | `capacities_RelStructure` |  |  | §5.2.3.5.1, Tab. 35 |
| [`capacities / PassengerCapacity`](common.md#passengercapacity) | 1..n | `PassengerCapacity_VersionStructure` |  |  |  |
| `LowFloor` | 0..1 | `xsd:boolean` | `true` | Determina se la tipologia di veicolo sia dotata o meno di pianale ribassato. | §5.2.3.5.1, Tab. 35 |
| `HasLiftOrRamp` | 0..1 | `xsd:boolean` | `True` | Determina se la tipologia di veicolo sia dotata o meno di sollevatore o di scivolo per sedie a rotelle | §5.2.3.5.1, Tab. 35 |
| `Length` | 0..1 | `LengthType` | `18` | Lunghezza totale del veicolo | §5.2.3.5.1, Tab. 35 |

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
    | `SelfPropelled` | 0..1 | `xsd:boolean` |
    | `HasHoist` | 0..1 | `xsd:boolean` |
    | `Width` | 0..1 | `LengthType` |
    | `Height` | 0..1 | `LengthType` |
    | `Weight` | 0..1 | `WeightType` |

### vehicleTypes / Train {#vehicletypes-train}

Linee guida §5.2.3.5.2 «Sottostruttura Train», Tabella 36. Tipo dell'XSD `TrainL2_VersionStructure`.

| Campo | Cardinalità | Tipo | Esempio | Significato (5T) | Fonte |
|---|---|---|---|---|---|
| `@id` | 1..1 | `xsd:normalizedString` | `IT:ITC1:Train:trenoFS:1` | Identificativo [→ Identificazione](common.md#identificazione) | §5.2.3.5.2, Tab. 36 |
| `@version` | 0..1 | `xsd:normalizedString` | `1` | Versione [→ Identificazione](common.md#identificazione) | §5.2.3.5.2, Tab. 36 |
| [`ValidBetween`](common.md#validbetween) | 0..1 | `ValidBetween_VersionStructure` |  |  | §5.2.3.5.2, Tab. 36 |
| `Name` | 0..1 | `MultilingualString` | `Torino - Milano` | Nome della composizione | §5.2.3.5.2, Tab. 36 |
| `ShortName` | 0..1 | `MultilingualString` | `Torino - Milano` | Nome breve della composizione | §5.2.3.5.2, Tab. 36 |
| `Description` | 0..1 | `MultilingualString` | `E 2 2 2 2 2 2 R 1 1 X` | Descrizione della composizione | §5.2.3.5.2, Tab. 36 |
| `PrivateCode` | 0..1 | `PrivateCodeStructure` | `TM1` | Codice aziendale della composizione | §5.2.3.5.2, Tab. 36 |
| `capacities` | 0..1 | `capacities_RelStructure` |  |  |  |
| [`capacities / PassengerCapacity`](common.md#passengercapacity) | 1..n | `PassengerCapacity_VersionStructure` |  | Definizione dei posti disponibili del treno completo [⚠ Incongruenza](issues.md#36-netex-resourceframe-netex-vehicletypes-netex-train-netex-capacities-netex-passengercapacity) | §5.2.3.5.2, Tab. 36, §5.2.3.5.2, Tab. 36 |
| `SelfPropelled` | 0..1 | `xsd:boolean` | `True` | Indica se l’alimentazione è autonoma | §5.2.3.5.2, Tab. 36 |
| `FuelType` | 0..1 | [`FuelTypeEnumeration`](enumerations.md#fueltypeenumeration) | `electricity` | Tipo di alimentazione del veicolo | §5.2.3.5.2, Tab. 36 |
| `TrainSize` | 0..1 | `TrainSizeStructure` |  | [⚠ Incongruenza](issues.md#36-netex-resourceframe-netex-vehicletypes-netex-train-netex-trainsize) | §5.2.3.5.2, Tab. 36 |
| `TrainSize / NumberOfCars` | 0..1 | `xsd:nonNegativeInteger` | `6` | Numero di componenti | §5.2.3.5.2, Tab. 36 |
| `TrainSize / TrainSizeType` | 0..1 | [`TrainSizeEnumeration`](enumerations.md#trainsizeenumeration) | `normal` | Lunghezza del treno [⚠ Incongruenza](issues.md#36-netex-resourceframe-netex-vehicletypes-netex-train-netex-trainsize-netex-trainsizetype) | §5.2.3.5.2, Tab. 36 |
| `facilities` | 0..1 | `serviceFacilitiesL2_RelStructure` |  |  |  |
| [`facilities / ServiceFacilitySetRef`](#vehicletypes-train-facilities-servicefacilitysetref) | 0..n · scelta 1 | `ServiceFacilitySetRefStructure` | `IT:ITC1:ServiceFacilitySet:trenoFS:1` | riferimento alla ServiceFacilitySet | §5.2.3.5.2, Tab. 36 |
| `components` | 0..1 | `trainComponents_RelStructure` |  |  |  |
| [`components / TrainComponent`](#vehicletypes-train-components-traincomponent) | 1..n | `TrainComponent_VersionStructure` |  | Elenco dei vagoni componenti del treno [⚠ Incongruenza](issues.md#36-netex-resourceframe-netex-vehicletypes-netex-train-netex-components-netex-traincomponent) | §5.2.3.5.2, Tab. 36 |

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
    | `EuroClass` | 0..1 | `xsd:normalizedString` |
    | `LowFloor` | 0..1 | `xsd:boolean` |
    | `HasLiftOrRamp` | 0..1 | `xsd:boolean` |
    | `HasHoist` | 0..1 | `xsd:boolean` |
    | `Length` | 0..1 | `LengthType` |
    | `Width` | 0..1 | `LengthType` |
    | `Height` | 0..1 | `LengthType` |
    | `Weight` | 0..1 | `WeightType` |

#### facilities / ServiceFacilitySetRef {#vehicletypes-train-facilities-servicefacilitysetref}

Linee guida §5.2.3.5.2 «Sottostruttura Train», Tabella 36. Tipo dell'XSD `ServiceFacilitySetRefStructure`.

| Campo | Cardinalità | Tipo | Esempio | Significato (5T) | Fonte |
|---|---|---|---|---|---|
| `@version` | 0..1 | `xsd:normalizedString` | `1` | Versione [→ Identificazione](common.md#identificazione) [⚠ Incongruenza](issues.md#36-netex-resourceframe-netex-vehicletypes-netex-train-netex-facilities-netex-servicefacilitysetref-version) | §5.2.3.5.2, Tab. 36 |

??? note "Altri campi dell'XSD"

    | Campo | Cardinalità | Tipo |
    |---|---|---|
    | `@nameOfRefClass` | 0..1 | `xsd:Name` |
    | `@created` | 0..1 | `xsd:dateTime` |
    | `@changed` | 0..1 | `xsd:dateTime` |
    | `@modification` | 0..1 | [`ModificationEnumeration`](enumerations.md#modificationenumeration) |
    | `@versionRef` | 0..1 | `xsd:normalizedString` |
    | `@ref` | 1..1 | `xsd:normalizedString` |

#### components / TrainComponent {#vehicletypes-train-components-traincomponent}

Linee guida §5.2.3.5.2 «Sottostruttura Train», Tabella 36. Tipo dell'XSD `TrainComponent_VersionStructure`.

| Campo | Cardinalità | Tipo | Esempio | Significato (5T) | Fonte |
|---|---|---|---|---|---|
| `@id` | 1..1 | `xsd:normalizedString` | `IT:ITC1:TrainComponent:trenoFS:1` | Identificativo [→ Identificazione](common.md#identificazione) | §5.2.3.5.2, Tab. 36 (occorrenza 2) |
| `@version` | 0..1 | `xsd:normalizedString` | `1` | Versione [→ Identificazione](common.md#identificazione) | §5.2.3.5.2, Tab. 36 (occorrenza 2) |
| `@order` | 1..1 | `xsd:integer` | `1` | Ordinale del vagone nella composizione | §5.2.3.5.2, Tab. 36 |
| `Label` | 0..1 | `MultilingualString` | `Carriage K` | Etichetta del componente | §5.2.3.5.2, Tab. 36 |
| `Description` | 0..1 | `MultilingualString` | `Front Carriage 1st Class` | Descrizione del componente | §5.2.3.5.2, Tab. 36 (occorrenza 2) |
| [`TrainElement`](#vehicletypes-train-components-traincomponent-trainelement) | 1..1 | `TrainElement_VersionStructure` |  | Descrive i dettagli del componente | §5.2.3.5.2, Tab. 36 |

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

##### TrainElement {#vehicletypes-train-components-traincomponent-trainelement}

Linee guida §5.2.3.5.2 «Sottostruttura Train», Tabella 36. Tipo dell'XSD `TrainElement_VersionStructure`.

| Campo | Cardinalità | Tipo | Esempio | Significato (5T) | Fonte |
|---|---|---|---|---|---|
| `@id` | 1..1 | `xsd:normalizedString` | `IT:ITC1:TrainElement:trenoFS:1_01` | Identificativo [→ Identificazione](common.md#identificazione) | §5.2.3.5.2, Tab. 36 (occorrenza 3) |
| `@version` | 0..1 | `xsd:normalizedString` | `1` | Versione [→ Identificazione](common.md#identificazione) | §5.2.3.5.2, Tab. 36 (occorrenza 3) |
| `Name` | 0..1 | `MultilingualString` | `Carriage K` | Nome dell’elemento | §5.2.3.5.2, Tab. 36 (occorrenza 2) |
| `TrainElementType` | 0..1 | [`TrainElementTypeEnumeration`](enumerations.md#trainelementtypeenumeration) | `carriage` | Tipologia di carrozza | §5.2.3.5.2, Tab. 36 |
| `FareClasses` | 0..1 | [`FareClassListOfEnumerations`](enumerations.md#fareclasslistofenumerations) | `firstClass` | Classe del vagone | §5.2.3.5.2, Tab. 36 |

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

### vehicleModels / VehicleModel {#vehiclemodels-vehiclemodel}

Linee guida §5.2.3.6 «VehicleModels», Tabella 37. Tipo dell'XSD `VehicleModel_VersionStructure`.

| Campo | Cardinalità | Tipo | Esempio | Significato (5T) | Fonte |
|---|---|---|---|---|---|
| `@id` | 1..1 | `xsd:normalizedString` | `IT:ITC1:VehicleModel:busATS: 01"` | Identificativo [→ Identificazione](common.md#identificazione) | §5.2.3.6, Tab. 37 |
| `@version` | 0..1 | `xsd:normalizedString` | `1` | Versione [→ Identificazione](common.md#identificazione) | §5.2.3.6, Tab. 37 |
| [`ValidBetween`](common.md#validbetween) | 0..1 | `ValidBetween_VersionStructure` |  |  | §5.2.3.6, Tab. 37 |
| `Name` | 0..1 | `MultilingualString` | `BUS Extraurbano Modello 1` | Nome del modello | §5.2.3.6, Tab. 37 |
| `Description` | 0..1 | `MultilingualString` | `BUS Extraurbano Modello 1` | Descrive in modo esteso il modello | §5.2.3.6, Tab. 37 |
| `Manufacturer` | 0..1 | `MultilingualString` | `RCBD` | Descrive il produttore del modello | §5.2.3.6, Tab. 37 |
| `VehicleTypeRef` → [VehicleType](#vehicletypes-vehicletype) | 0..1 · scelta 1 | `VehicleTypeRefStructure` | `IT:ITC1:VehicleType:busATS:001` | Riferimento al corrispondente VehicleType (vedi paragrafo 5.2.3.5). [⚠ Incongruenza](issues.md#37-netex-resourceframe-netex-vehiclemodels-netex-vehiclemodel-netex-vehicletyperef) | §5.2.3.6, Tab. 37 |

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
    | `TrainRef` | 0..1 | `TrainRefStructure` |

### vehicles / Vehicle {#vehicles-vehicle}

Linee guida §5.2.3.7 «Vehicles», Tabella 38. Tipo dell'XSD `VehicleL4_VersionStructure`.

| Campo | Cardinalità | Tipo | Esempio | Significato (5T) | Fonte |
|---|---|---|---|---|---|
| `@id` | 1..1 | `xsd:normalizedString` | `IT:ITC1:Vehicle:busATS:ZZ998ZZ` | Identificativo [→ Identificazione](common.md#identificazione) | §5.2.3.7, Tab. 38 |
| `@version` | 0..1 | `xsd:normalizedString` | `1` | Versione [→ Identificazione](common.md#identificazione) | §5.2.3.7, Tab. 38 |
| [`ValidBetween`](common.md#validbetween) | 0..1 | `ValidBetween_VersionStructure` |  |  | §5.2.3.7, Tab. 38 |
| `Name` | 0..1 | `MultilingualString` | `Bus ZZ998ZZ` | Nome del veicolo | §5.2.3.7, Tab. 38 |
| `ShortName` | 0..1 | `MultilingualString` | `001` | Nome sintetico del veicolo | §5.2.3.7, Tab. 38 |
| `RegistrationNumber` | 0..1 | `xsd:normalizedString` | `ZZ998ZZ` | Numero di targa del veicolo | §5.2.3.7, Tab. 38 |
| `OperationalNumber` | 0..1 | `xsd:normalizedString` | `ZZZZZZZZZZZZZZZZ1` | Numero di telaio del veicolo | §5.2.3.7, Tab. 38 |
| `PrivateCode` | 0..1 | `PrivateCodeStructure` | `001` | Matricola aziendale del veicolo | §5.2.3.7, Tab. 38 |
| `OperatorRef` → [Operator](#organisations-operator) | 0..1 | `OperatorRefStructure` | `IT:ITC1:Operator:busATS:11` | Riferimento all’operator proprietario del veicolo (cfr. paragrafo 5.2.3.2.2) | §5.2.3.7, Tab. 38 |
| `VehicleTypeRef` → [VehicleType](#vehicletypes-vehicletype) | 0..1 · scelta 1 | `VehicleTypeRefStructure` | `IT:ITC1:VehicleType:busATS:001` | Riferimento al corrispondente VehicleType (paragrafo 5.2.3.5). [⚠ Incongruenza](issues.md#38-netex-resourceframe-netex-vehicles-netex-vehicle-netex-vehicletyperef) | §5.2.3.7, Tab. 38 |
| `actualVehicleEquipments` | 0..1 | `equipmentsL2_RelStructure` |  |  | §5.2.3.7, Tab. 38 |
| `actualVehicleEquipments / CommunicationServiceRef` → [CommunicationService](#equipments-communicationservice) | 0..n | `CommunicationServiceRefStructure` | `IT:ITC1:CommunicationService:busATS:002` | Riferimento ai sistemi di comunicazione (vedi par. 5.2.3.4.1) | §5.2.3.7, Tab. 38 |
| `actualVehicleEquipments / CycleStorageEquipmentRef` → [CycleStorageEquipment](#equipments-cyclestorageequipment) | 0..n | `CycleStorageEquipmentRefStructure` | `IT:ITC1:CycleStorageEquipments:busATS:1` | Riferimento ai sistemi di trasporto delle biciclette (vedi par. 5.2.3.4.2) | §5.2.3.7, Tab. 38 |
| `actualVehicleEquipments / HeadingSignRef` → [HeadingSign](#equipments-headingsign) | 0..n | `HeadingSignRefStructure` | `IT:ITC1:HeadSign:busATS:1` | Riferimento agli ascensori e sollevatori per l’accesso al veicolo (vedi par. 5.2.3.4.4) | §5.2.3.7, Tab. 38 |
| `actualVehicleEquipments / HelpPointEquipmentRef` → [HelpPointEquipment](#equipments-helppointequipment) | 0..n | `HelpPointEquipmentRefStructure` | `IT:ITC1:HelpPointEquipment:busATS:002` | Riferimento ai sistemi di supporto ai passeggeri (vedi par. 5.2.3.4.5) | §5.2.3.7, Tab. 38 |
| `actualVehicleEquipments / LiftEquipmentRef` → [LiftEquipment](#equipments-liftequipment) | 0..n | `LiftEquipmentRefStructure` | `IT:ITC1:LiftEquipments:busATS:1` | Riferimento agli ascensori e sollevatori per l’accesso al veicolo (vedi par. 5.2.3.4.7) | §5.2.3.7, Tab. 38 |
| `actualVehicleEquipments / LuggageLockerEquipmentRef` → [LuggageLockerEquipment](#equipments-luggagelockerequipment) | 0..n | `LuggageLockerEquipmentRefStructure` | `IT:ITC1:LuggageLockerEquipments:busATS:1` | Riferimento al sistema di stoccaggio di bagagli e biciclette (vedi par. 5.2.3.4.8) | §5.2.3.7, Tab. 38 |
| `actualVehicleEquipments / PassengerInformationEquipmentRef` → [PassengerInformationEquipment](#equipments-passengerinformationequipment) | 0..n | `PassengerInformationEquipmentRefStructure` | `IT:ITC1:PassengerInformationEquipments:busATS:1` | Riferimento ai sistemi di infomobilità all’utenza (vedi par. 5.2.3.4.9) | §5.2.3.7, Tab. 38 |
| `actualVehicleEquipments / PassengerSafetyEquipmentRef` → [PassengerSafetyEquipment](#equipments-passengersafetyequipment) | 0..n | `PassengerSafetyEquipmentRefStructure` | `IT:ITC1:PassengerSafetyEquipments:busATS:1` | Riferimento ai sistemi di sicurezza per l’utenza (vedi par. 5.2.3.4.10) | §5.2.3.7, Tab. 38 |
| `actualVehicleEquipments / RampEquipmentRef` → [RampEquipment](#equipments-rampequipment) | 0..n | `RampEquipmentRefStructure` | `IT:ITC1:RampEquipments:busATS:1` | Riferimento alle rampe di accesso per l’utenza (vedi par. 5.2.3.4.11) | §5.2.3.7, Tab. 38 |
| `actualVehicleEquipments / ShelterEquipmentRef` → [ShelterEquipment](#equipments-shelterequipment) | 0..n | `ShelterEquipmentRefStructure` | `IT:ITC1:SheltherEquipments:busATS:1` | Riferimento ai sistemi di protezione per l’utenza (vedi par. 5.2.3.4.13) [⚠ Incongruenza](issues.md#38-netex-resourceframe-netex-vehicles-netex-vehicle-netex-actualvehicleequipments-netex-shelterequipmentref) | §5.2.3.7, Tab. 38 |
| `actualVehicleEquipments / TicketingEquipmentRef` → [TicketingEquipment](#equipments-ticketingequipment) | 0..n | `TicketingEquipmentRefStructure` | `IT:ITC1:TicketingEquipments:busATS:002` | Riferimento ai sistemi di emissione dei titoli di viaggio (vedi par. 5.2.3.4.15) | §5.2.3.7, Tab. 38 |
| `actualVehicleEquipments / TicketValidatorEquipmentRef` → [TicketValidatorEquipment](#equipments-ticketvalidatorequipment) | 0..n | `TicketValidatorEquipmentRefStructure` | `IT:ITC1:TicketValidatorEquipments:busATS:1` | Riferimento ai sistemi di validazione dei titoli di viaggio (vedi par. 5.2.3.4.16) [⚠ Incongruenza](issues.md#38-netex-resourceframe-netex-vehicles-netex-vehicle-netex-actualvehicleequipments-netex-ticketvalidatorequipmentref) | §5.2.3.7, Tab. 38 |
| `actualVehicleEquipments / WheelchairVehicleRef` | 0..n | `WheelchairVehicleRefStructure` | `IT:ITC1:WheelchairVehicleEquipment:busATS:1` | Riferimento ai sistemi per l’accesso ai veicoli con sedia a rotelle (vedi par. 5.2.3.4.17) | §5.2.3.7, Tab. 38 |

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
    | `TrainRef` | 0..1 | `TrainRefStructure` |
    | `CarModelProfileRef` | 0..1 | `CarModelProfileRefStructure` |
    | `CycleModelProfileRef` | 0..1 | `CycleModelProfileRefStructure` |

### vehicleModelProfiles / CycleModelProfile {#vehiclemodelprofiles-cyclemodelprofile}

Linee guida §5.2.3.8.2 «CarModelProfile», Tabella 39. Tipo dell'XSD `CycleModelProfile_VersionStructure`.

| Campo | Cardinalità | Tipo | Esempio | Significato (5T) | Fonte |
|---|---|---|---|---|---|
| `@id` | 1..1 | `xsd:normalizedString` | `IT:ITC1:CycleModelProfile:BikeSharingTorino:vehicleType:Bike01` | Identificativo [→ Identificazione](common.md#identificazione) | §5.2.3.8.2, Tab. 39 |
| `@version` | 0..1 | `xsd:normalizedString` | `1` | Versione [→ Identificazione](common.md#identificazione) | §5.2.3.8.2, Tab. 39 |
| `ChildSeat` | 0..1 | [`ChildSeatEnumeration`](enumerations.md#childseatenumeration) | `olderChild` | Tipo di seggiolino | §5.2.3.8.2, Tab. 39 |
| `Battery` | 0..1 | `xsd:boolean` | `false` | Presenza pedalata assistita | §5.2.3.8.2, Tab. 39 |
| `Lamps` | 0..1 | `xsd:boolean` | `true` | Presenza luci | §5.2.3.8.2, Tab. 39 |
| `Pump` | 0..1 | `xsd:boolean` | `true` | Presenza pompa pneumatici | §5.2.3.8.2, Tab. 39 |
| `Basket` | 0..1 | `xsd:boolean` | `true` | Presenza cestino | §5.2.3.8.2, Tab. 39 |
| `Lock` | 0..1 | `xsd:boolean` | `true` | Presenza lucchetto | §5.2.3.8.2, Tab. 39 |

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
    | `NumberOfGears` | 0..1 | `xsd:nonNegativeInteger` |
    | `IsPortable` | 0..1 | `xsd:boolean` |
    | `Helmet` | 0..1 | `xsd:boolean` |

### vehicleModelProfiles / CarModelProfile {#vehiclemodelprofiles-carmodelprofile}

Linee guida §5.2.3.8.2 «CarModelProfile», Tabella 40. Tipo dell'XSD `CarModelProfile_VersionStructure`.

| Campo | Cardinalità | Tipo | Esempio | Significato (5T) | Fonte |
|---|---|---|---|---|---|
| `@id` | 1..1 | `xsd:normalizedString` | `IT:ITC1:CarModelProfile:CarSharingTorino:vehicleModel:Car01` | Identificativo [→ Identificazione](common.md#identificazione) | §5.2.3.8.2, Tab. 40 |
| `@version` | 0..1 | `xsd:normalizedString` | `1` | Versione [→ Identificazione](common.md#identificazione) | §5.2.3.8.2, Tab. 40 |
| `ChildSeat` | 0..1 | [`ChildSeatEnumeration`](enumerations.md#childseatenumeration) | `olderChild` | Tipo di seggiolino | §5.2.3.8.2, Tab. 40 |
| `Seats` | 0..1 | `xsd:nonNegativeInteger` | `4` | Numero posti disponibili | §5.2.3.8.2, Tab. 40 |
| `Doors` | 0..1 | `xsd:nonNegativeInteger` | `5` | Numero porte | §5.2.3.8.2, Tab. 40 |
| `Transmission` | 0..1 | [`TransmissionEnumeration`](enumerations.md#transmissionenumeration) | `automatic` | Tipologia cambio | §5.2.3.8.2, Tab. 40 |
| `CruiseControl` | 0..1 | `xsd:boolean` | `true` | Presenza cruise control | §5.2.3.8.2, Tab. 40 |
| `SatNav` | 0..1 | `xsd:boolean` | `true` | Presenza navigatore satellitare | §5.2.3.8.2, Tab. 40 |
| `AirConditioning` | 0..1 | `xsd:boolean` | `true` | Presenza aria condizionata | §5.2.3.8.2, Tab. 40 |
| `Convertible` | 0..1 | `xsd:boolean` | `false` | Mezzo cabrio | §5.2.3.8.2, Tab. 40 |
| `UsbPowerSockets` | 0..1 | `xsd:boolean` | `true` | Presenza presa usb | §5.2.3.8.2, Tab. 40 |
| `WinterTyres` | 0..1 | `xsd:boolean` | `false` | Presenza gomme invernali | §5.2.3.8.2, Tab. 40 |
| `Chains` | 0..1 | `xsd:boolean` | `true` | Presenza catene da neve | §5.2.3.8.2, Tab. 40 |
| `TrailerHitch` | 0..1 | `xsd:boolean` | `true` | Presenza gancio traino | §5.2.3.8.2, Tab. 40 |
| `RoofRack` | 0..1 | `xsd:boolean` | `true` | Presenza barre porta pacchi | §5.2.3.8.2, Tab. 40 |
| `CycleRack` | 0..1 | `xsd:boolean` | `false` | Presenza barre porta bici | §5.2.3.8.2, Tab. 40 |
| `SkiRack` | 0..1 | `xsd:boolean` | `false` | Presenza barre porta sci | §5.2.3.8.2, Tab. 40 |

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
    | `NumberOfGears` | 0..1 | `xsd:nonNegativeInteger` |
