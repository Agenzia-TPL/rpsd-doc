---
generato: true
generato_da: rpsd-tools 0.6.0
---
<!-- GENERATED — DO NOT EDIT · profile-docs netex-it · netex-it-lev5@cecb0cd -->

# ServiceCalendarFrame

Calendario di esercizio (linee guida §5.2.2).

## ServiceCalendarFrame {#servicecalendarframe}

Linee guida §5.2.2 «ServiceCalendarFrame», Tabella 7. Tipo dell'XSD `ServiceCalendarFrameL2_VersionStructure`.

| Campo | Cardinalità | Tipo | Esempio | Significato (5T) | Fonte |
|---|---|---|---|---|---|
| `@id` | 1..1 | `xsd:normalizedString` | `epd:IT:ITC1:ServiceCalendarFrame_EU_PI_CALENDAR:ita` | Identificativo [→ Identificazione](common.md#identificazione) | §5.2.2, Tab. 7 |
| `@version` | 0..1 | `xsd:normalizedString` | `1` | Versione [→ Identificazione](common.md#identificazione) | §5.2.2, Tab. 7 |
| [`TypeOfFrameRef`](common.md#typeofframeref) | 0..1 | `TypeOfFrameRefStructure` |  |  |  |
| [`ServiceCalendar`](#servicecalendar) | 0..1 | `ServiceCalendarL2Structure` |  |  |  |

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

### ServiceCalendar {#servicecalendar}

Linee guida §5.2.2.1 «ServiceCalendar», Tabella 8. Tipo dell'XSD `ServiceCalendarL2Structure`.

| Campo | Cardinalità | Tipo | Esempio | Significato (5T) | Fonte |
|---|---|---|---|---|---|
| `@id` | 0..1 | `xsd:normalizedString` | `IT:ITC1:DayType:busATS:annuale12345` | Identificativo [→ Identificazione](common.md#identificazione) | §5.2.2.1, Tab. 8 |
| `@version` | 0..1 | `xsd:normalizedString` | `1` | Versione [→ Identificazione](common.md#identificazione) | §5.2.2.1, Tab. 8 |
| `Name` | 0..1 | `MultilingualString` | `Calendario ordinario valido tutto l'anno` | Nome completo del calendario di servizio | §5.2.2.1, Tab. 8 |
| `ShortName` | 0..1 | `MultilingualString` | `Annuale` | Nome breve del calendario di servizio | §5.2.2.1, Tab. 8 |
| `FromDate` | 0..1 | `xsd:date` | `2021-01-01` | Data di inizio del calendario di servizio nel formato YYYY-MM-DD | §5.2.2.1, Tab. 8 |
| `ToDate` | 0..1 | `xsd:date` | `2021-12-31` | Data di fine del calendario di servizio nel formato YYYY-MM-DD | §5.2.2.1, Tab. 8 |
| [`dayTypes`](#servicecalendar-daytypes-daytype) | 0..1 | `dayTypesL2Structure` |  |  | §5.2.2.1, Tab. 8 |
| [`operatingPeriods`](#servicecalendar-operatingperiods-uicoperatingperiod) | 0..1 | `operatingPeriodsStructure` |  |  | §5.2.2.1, Tab. 8 |
| [`dayTypeAssignments`](#servicecalendar-daytypeassignments-daytypeassignment) | 0..1 | `dayTypeAssignments_RelStructure` |  |  | §5.2.2.1, Tab. 8 |

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
    | `keyList` | 0..1 | `keyListStructure` |
    | `BrandingRef` | 0..1 | `BrandingRefStructure` |
    | `operatingDays` | 0..1 | `operatingDays_RelStructure` |

#### dayTypes / DayType {#servicecalendar-daytypes-daytype}

Linee guida §5.2.2.1.1 «dayTypes», Tabella 9. Tipo dell'XSD `DayTypeL2Structure`.

| Campo | Cardinalità | Tipo | Esempio | Significato (5T) | Fonte |
|---|---|---|---|---|---|
| `@id` | 1..1 | `xsd:normalizedString` | `IT:ITC1:DayType:busATS:annuale12345` | Identificativo [→ Identificazione](common.md#identificazione) | §5.2.2.1.1, Tab. 9 |
| `@version` | 0..1 | `xsd:normalizedString` | `1` | Versione [→ Identificazione](common.md#identificazione) | §5.2.2.1.1, Tab. 9 |
| `Name` | 0..1 | `MultilingualString` | `Calendario annuale` | Nome completo del tipo di giornata | §5.2.2.1.1, Tab. 9 |
| `ShortName` | 0..1 | `MultilingualString` | `Annuale12345` | Nome breve del tipo di giornata | §5.2.2.1.1, Tab. 9 |
| `Description` | 0..1 | `MultilingualString` | `Annuale Lun Ven` | Descrizione testuale libera del tipo di giornata | §5.2.2.1.1, Tab. 9 |
| `PrivateCode` | 0..1 | `PrivateCodeStructure` | `12345` | Identificativo univoco del tipo di giornata | §5.2.2.1.1, Tab. 9 |
| [`properties`](#servicecalendar-daytypes-daytype-properties-propertyofday) | 0..1 |  |  |  |  |

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
    | `EarliestTime` | 0..1 | `binding_friendly_time` |
    | `DayLength` | 0..1 | `xsd:duration` |
    | `timebands` | 0..1 |  |

##### properties / PropertyOfDay {#servicecalendar-daytypes-daytype-properties-propertyofday}

Linee guida §5.2.2.1.1 «dayTypes», Tabella 9. Tipo dell'XSD `PropertyOfDayStructure`.

| Campo | Cardinalità | Tipo | Esempio | Significato (5T) | Fonte |
|---|---|---|---|---|---|
| `DaysOfWeek` | 0..1 | [`DaysOfWeekListOfEnumerations`](enumerations.md#daysofweeklistofenumerations) | `Monday Tuesday Wednesday Thursday Friday` | Identifica i giorni della settimana. È possibile inserire fino a 7 valori. Valori del profilo: `Monday`, `Tuesday`, `Wednesday`, `Thursday`, `Friday`, `Saturday`, `Sunday`. [⚠ Incongruenza](issues.md#9-netex-servicecalendarframe-netex-servicecalendar-netex-daytypes-netex-daytype-netex-properties-netex-propertyofday-netex-daysofweek) | §5.2.2.1.1, Tab. 9 |
| `HolidayTypes` | 0..1 | [`HolidayTypesListOfEnumerations`](enumerations.md#holidaytypeslistofenumerations) | `NotHoliday` | Indica se si tratta di giorni festivi o feriali. [⚠ Incongruenza](issues.md#9-netex-servicecalendarframe-netex-servicecalendar-netex-daytypes-netex-daytype-netex-properties-netex-propertyofday-netex-holidaytypes) | §5.2.2.1.1, Tab. 9 |

??? note "Altri campi dell'XSD"

    | Campo | Cardinalità | Tipo |
    |---|---|---|
    | `Name` | 0..1 | `MultilingualString` |
    | `Description` | 0..1 | `MultilingualString` |
    | `WeeksOfMonth` | 0..1 | [`WeeksOfMonthListOfEnumerations`](enumerations.md#weeksofmonthlistofenumerations) |
    | `MonthOfYear` | 0..1 | `xsd:gMonth` |
    | `DayOfMonth` | 0..1 | `xsd:gDay` |
    | `DayOfYear` | 0..1 | `xsd:gMonthDay` |
    | `CountryRef` | 0..1 | `CountryRefStructure` |
    | `Seasons` | 0..1 | [`SeasonsListOfEnumerations`](enumerations.md#seasonslistofenumerations) |
    | `Crowding` | 0..1 | [`CrowdingEnumeration`](enumerations.md#crowdingenumeration) |

#### operatingPeriods / UicOperatingPeriod {#servicecalendar-operatingperiods-uicoperatingperiod}

Linee guida §5.2.2.1.2 «operatingPeriods», Tabella 10. Tipo dell'XSD `UicOperatingPeriod_VersionStructure`.

| Campo | Cardinalità | Tipo | Esempio | Significato (5T) | Fonte |
|---|---|---|---|---|---|
| `@id` | 1..1 | `xsd:normalizedString` | `IT:ITC1:UicOperatingPeriod:busATS:annuale12345` | Identificativo [→ Identificazione](common.md#identificazione) | §5.2.2.1.2, Tab. 10 |
| `@version` | 0..1 | `xsd:normalizedString` | `1` | Versione [→ Identificazione](common.md#identificazione) | §5.2.2.1.2, Tab. 10 |
| `FromDate` | 1..1 | `xsd:dateTime` | `2021-01-04T00:00:00` | data di inizio validità del periodo calendariale | §5.2.2.1.2, Tab. 10 |
| `ToDate` | 1..1 | `xsd:dateTime` | `2021-01-10T23:59:59` | data di fine validità del periodo calendariale | §5.2.2.1.2, Tab. 10 |
| `ValidDayBits` | 1..1 | `xsd:normalizedString` | `1111100` | Giorni di validità | §5.2.2.1.2, Tab. 10 |

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
    | `keyList` | 0..1 | `keyListStructure` |
    | `BrandingRef` | 0..1 | `BrandingRefStructure` |
    | `Name` | 0..1 | `MultilingualString` |
    | `DaysOfWeek` | 0..1 | [`DaysOfWeekListOfEnumerations`](enumerations.md#daysofweeklistofenumerations) |

#### dayTypeAssignments / DayTypeAssignment {#servicecalendar-daytypeassignments-daytypeassignment}

Linee guida §5.2.2.1.3 «dayTypeAssignments», Tabella 11. Tipo dell'XSD `DayTypeAssignmentStructure`.

| Campo | Cardinalità | Tipo | Esempio | Significato (5T) | Fonte |
|---|---|---|---|---|---|
| `@id` | 0..1 | `xsd:normalizedString` | `IT:ITC1:DayTypeAssignment:busATS:2021-01-04_12345` | Identificativo [→ Identificazione](common.md#identificazione) | §5.2.2.1.3, Tab. 11 |
| `@version` | 0..1 | `xsd:normalizedString` | `1` | Versione [→ Identificazione](common.md#identificazione) | §5.2.2.1.3, Tab. 11 |
| `@order` | 0..1 | `xsd:integer` | `1` | Ordine di visualizzazione del DayTypeAssignment | §5.2.2.1.3, Tab. 11 |
| `OperatingPeriodRef` | 0..1 · scelta 1 | `OperatingPeriodRefStructure` | `IT:ITC1:UicOperatingPeriod:busATS:annuale12345` | Eventuale riferimento alll’OperatingPeriod | §5.2.2.1.3, Tab. 11 |
| `DayTypeRef` → [DayType](#servicecalendar-daytypes-daytype) | 1..1 | `DayTypeRefStructure` | `IT:ITC1:DayType:busATS:annuale12345` | Riferimento al DayType | §5.2.2.1.3, Tab. 11 |

??? note "Altri campi dell'XSD"

    | Campo | Cardinalità | Tipo |
    |---|---|---|
    | `@nameOfClass` | 0..1 | `xsd:Name` |
    | `@dataSourceRef` | 0..1 | `xsd:normalizedString` |
    | `@created` | 0..1 | `xsd:dateTime` |
    | `@changed` | 0..1 | `xsd:dateTime` |
    | `@modification` | 0..1 | [`ModificationEnumeration`](enumerations.md#modificationenumeration) |
    | `@status` | 0..1 | [`StatusEnumeration`](enumerations.md#statusenumeration) |
    | `ServiceCalendarRef` | 0..1 | `ServiceCalendarRefStructure` |
    | `Date` | 0..1 | `xsd:date` |
    | `isAvailable` | 0..1 | `xsd:boolean` |
