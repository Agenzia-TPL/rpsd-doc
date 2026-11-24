---
generato: true
generato_da: rpsd-tools 0.8.0
---
<!-- GENERATED — DO NOT EDIT · profile-docs netex-it · netex-it-lev5@cecb0cd -->

# GeneralFrame

Linee guida §5.2.1.

## GeneralFrame {#generalframe}

Linee guida §5.2.1 «GeneralFrame», Tabella 5. Tipo dell'XSD `GeneralFrame_VersionStructure`.

| Campo | Cardinalità | Tipo | Esempio | Significato (5T) | Fonte |
|---|---|---|---|---|---|
| `@id` | 1..1 | `xsd:normalizedString` | `epd:IT:ITC1:GeneralFrame_EU_CONTRACTS:ita` | Identificativo [→ Identificazione](common.md#identificazione) | §5.2.1, Tab. 5 |
| `@version` | 0..1 | `xsd:normalizedString` | `1` | Versione [→ Identificazione](common.md#identificazione) | §5.2.1, Tab. 5 |
| [`TypeOfFrameRef`](common.md#typeofframeref) | 0..1 | `TypeOfFrameRefStructure` |  |  |  |
| [`members`](#members-journeyaccounting) | 0..1 | `members_RelStructure` |  |  |  |

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

### members / JourneyAccounting {#members-journeyaccounting}

Linee guida §5.2.1.1 «members», Tabella 6. Tipo dell'XSD `JourneyAccounting_VersionStructure`.

| Campo | Cardinalità | Tipo | Esempio | Significato (5T) | Fonte |
|---|---|---|---|---|---|
| `@id` | 0..1 | `xsd:normalizedString` | `IT:ITC1:JourneyAccounting:busATS:1A` | Identificativo [→ Identificazione](common.md#identificazione) | §5.2.1.1, Tab. 6 |
| `@version` | 0..1 | `xsd:normalizedString` | `1` | Versione [→ Identificazione](common.md#identificazione) | §5.2.1.1, Tab. 6 |
| [`ValidBetween`](common.md#validbetween) | 0..n · scelta 1 | `ValidBetween_VersionStructure` |  | Struttura contente le condizioni di validità temporale [⚠ Incongruenza](issues.md#6-netex-generalframe-netex-members-netex-journeyaccounting-netex-validbetween) | §5.2.1.1, Tab. 6 |
| `Name` | 0..1 | `MultilingualString` | `Contratto Piemonte` | Nome completo del contratto/sovvenzione | §5.2.1.1, Tab. 6 |
| `Description` | 0..1 | `MultilingualString` | `Contratto Piemonte` | Descrizione testuale libera del contratto/sovvenzione | §5.2.1.1, Tab. 6 |
| `OrganisationRef` | 0..1 | `OrganisationRefStructure` | `IT:ITC1:Authority:busATS:AMP` | Riferimento all’organizzazione con la quale è stato stipulato il contratto/sovvenzione | §5.2.1.1, Tab. 6 |
| `AccountingCode` | 0..1 | `xsd:normalizedString` | `CDS0001` | Codice associato al contratto/sovvenzione | §5.2.1.1, Tab. 6 |
| `AccountingType` | 0..1 | [`JourneyAccountingEnumeration`](enumerations.md#journeyaccountingenumeration) | `contract` | Tipologia di contratto/sovvenzione stipulata | §5.2.1.1, Tab. 6 |

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
    | `alternativeTexts` | 0..1 | `alternativeTextsStructure` |
    | `keyList` | 0..1 | `keyListStructure` |
    | `BrandingRef` | 0..1 | `BrandingRefStructure` |
    | `AccountedObjectRef` | 0..1 | `AccountedObjectRefStructure` |
    | `SupplyContractRef` | 0..1 | `SupplyContractRefStructure` |
    | `Partial` | 0..n | `xsd:boolean` |
    | `Distance` | 0..1 | `DistanceType` |
    | `Duration` | 0..1 | `xsd:duration` |
