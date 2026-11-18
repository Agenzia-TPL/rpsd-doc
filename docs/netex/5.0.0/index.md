---
generato: true
generato_da: rpsd-tools 0.6.0
---
<!-- GENERATED — DO NOT EDIT · profile-docs netex-it · netex-it-lev5@cecb0cd -->

# Profilo italiano NeTEx

- Linee guida 5.0.0: «Linee guida compilazione NeTEx IT v.5.0.0.docx»
    - Linee guida compilazione NeTEx IT v.5.0.0.docx (versione 5.0.0, provided)
    - Linee guida compilazione NeTEx IT v.5.0.1.pdf (versione 5.0.1, published)
- XSD: `netex-it-lev5@cecb0cd`
- Note del profilo riviste da Franco il 2026-11-11

La cardinalità è quella dell'XSD: l'obbligatorietà non fa parte del profilo (linee guida, §2.2.4). Il significato è quello dato dalle linee guida; i campi dell'XSD che le linee guida non citano sono nel riquadro chiuso sotto ogni tabella.

## Pagine del profilo

- [GeneralFrame](general-frame.md): Linee guida §5.2.1.
- [ServiceCalendarFrame](service-calendar-frame.md): Calendario di esercizio (linee guida §5.2.2).
- [ResourceFrame](resource-frame.md): Organizzazioni, attrezzature e veicoli (linee guida §5.2.3).
- [SiteFrame](site-frame.md): Luoghi, fermate e parcheggi (linee guida §5.2.4).
- [ServiceFrame](service-frame.md): Rete, linee, fermate programmate e percorsi (linee guida §5.2.5).
- [TimetableFrame](timetable-frame.md): Corse e coincidenze (linee guida §5.2.6).
- [FareFrame](fare-frame.md): Tariffe e titoli di viaggio (linee guida §5.2.7).
- [MobilityServiceFrame](mobility-service-frame.md): Servizi di mobilità condivisa (linee guida §5.2.8).
- [Strutture comuni](common.md)
- [Enumerazioni](enumerations.md)
- [Incongruenze](issues.md)

## Busta

Elementi: `netex:PublicationDelivery`, `netex:CompositeFrame`.

## PublicationDelivery {#publicationdelivery}

Linee guida §5.1.2 «Tag comuni», Tabella 3. Tipo dell'XSD `PublicationDeliveryStructure`.

| Campo | Cardinalità | Tipo | Esempio | Significato (5T) | Fonte |
|---|---|---|---|---|---|
| `PublicationTimestamp` | 1..1 | `xsd:dateTime` | `2021-01-01T12:00:00.000+02:00` | Data e ora di generazione del file (cfr. par. 4.1) [⚠ Incongruenza](issues.md#3-netex-publicationdelivery-netex-publicationtimestamp) | §5.1.2, Tab. 3 |
| `ParticipantRef` | 1..1 | `xsd:normalizedString` | `RAP` | Identifica il mittente del file | §5.1.2, Tab. 3 |
| `Description` | 0..1 | `MultilingualString` | `Esempio di profilo italiano del NeTEx` | Descrive il contenuto del file | §5.1.2, Tab. 3 |

??? note "Altri campi dell'XSD"

    | Campo | Cardinalità | Tipo |
    |---|---|---|
    | `@version` | 0..1 | `xsd:NMTOKEN` |
    | `PublicationRequest` | 0..1 | `PublicationRequestStructure` |
    | `dataObjects` | 0..1 | `dataObjectsStructure` |

## CompositeFrame {#compositeframe}

Linee guida §5.1.3 «Contenuto informativo», Tabella 4. Tipo dell'XSD `CompositeFrame_VersionStructure`.

| Campo | Cardinalità | Tipo | Esempio | Significato (5T) | Fonte |
|---|---|---|---|---|---|
| `@id` | 1..1 | `xsd:normalizedString` | `epd:IT:ITC1:CompositeFrame_EU_PI_STOP_OFFER:ita` | Identificativo [→ Identificazione](common.md#identificazione) | §5.1.3, Tab. 4 |
| `@version` | 0..1 | `xsd:normalizedString` | `1` | Versione [→ Identificazione](common.md#identificazione) | §5.1.3, Tab. 4 |
| [`ValidBetween`](common.md#validbetween) | 0..1 | `ValidBetween_VersionStructure` |  |  |  |
| [`TypeOfFrameRef`](common.md#typeofframeref) | 0..1 | `TypeOfFrameRefStructure` |  |  |  |
| [`codespaces`](#codespaces-codespace) | 0..1 | `codespaces_RelStructure` |  |  |  |
| `FrameDefaults` | 0..1 | `FrameDefaultsStructure` |  |  |  |
| `FrameDefaults / DefaultCodespaceRef` | 0..1 | `CodespaceRefStructure` |  |  |  |
| `FrameDefaults / DefaultCodespaceRef / @ref` | 0..1 | `xsd:normalizedString` | `ita` | Sigla della lingua del profilo | §5.1.3, Tab. 4 |
| `FrameDefaults / DefaultLocale` | 0..1 | `LocaleStructure` |  |  | §5.1.3, Tab. 4 |
| `FrameDefaults / DefaultLocale / TimeZone` | 0..1 | `xsd:normalizedString` | `Europe/Rome` | Time zone del dato | §5.1.3, Tab. 4 |

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
    | `Description` | 0..1 | `MultilingualString` |
    | `BaselineVersionFrameRef` | 0..1 | `BaselineVersionFrameRefStructure` |
    | `prerequisites` | 0..1 | `prerequisites_RelStructure` |
    | `contentValidityConditions` | 0..1 | `contentValidityConditions_RelStructure` |
    | `frames` | 0..1 | `frames_RelStructure` |

### codespaces / Codespace {#codespaces-codespace}

Linee guida §5.1.3 «Contenuto informativo», Tabella 4. Tipo dell'XSD `CodespaceStructure`.

| Campo | Cardinalità | Tipo | Esempio | Significato (5T) | Fonte |
|---|---|---|---|---|---|
| `@id` | 1..1 | `xsd:normalizedString` | `ita` | Identificativo [→ Identificazione](common.md#identificazione) | §5.1.3, Tab. 4 |
| `Xmlns` | 1..1 | `xsd:NMTOKEN` | `ita` | Namespace del profilo | §5.1.3, Tab. 4 |
| `XmlnsUrl` | 0..1 | `xsd:anyURI` | `www.ita.it` | Url a cui è reperibile la documentazione del profilo | §5.1.3, Tab. 4 |
| `Description` | 0..1 | `MultilingualString` | `Italian Profile` | Campo descrittivo del profilo | §5.1.3, Tab. 4 |
