# Spec Delta — profile-docs

## Purpose

Defines the reference pages of each NeTEx and SIRI profile version: one page per frame or service with field tables, common structures, enumerations and the inconsistencies between guidelines and XSD, generated from a data bundle committed in the repository.

## ADDED Requirements

### Requirement: One page per frame and per service
Each profile version SHALL document every NeTEx frame of the Italian profile and every SIRI functional service of the Italian profile on its own page.

#### Scenario: NeTEx frames
- **WHEN** a reader opens the sidebar of NeTEx profile 5.0.0
- **THEN** there is one page each for GeneralFrame, ServiceCalendarFrame, ResourceFrame, SiteFrame, ServiceFrame, TimetableFrame, FareFrame and MobilityServiceFrame

#### Scenario: SIRI services
- **WHEN** a reader opens the sidebar of SIRI profile 1.0.5
- **THEN** there is one page each for SIRI-VM, SIRI-ET, SIRI-SX, SIRI-FM and SIRI-PT

### Requirement: Generated profile pages
The pages of each profile version SHALL be generated from a data bundle committed in the repository, and the committed pages SHALL match that bundle.

#### Scenario: Pages out of date
- **WHEN** a pull request changes the bundle of a profile version without regenerating its pages, or changes a generated page without changing the bundle
- **THEN** the check on the pull request fails and names the version folder

#### Scenario: Bundle changes
- **WHEN** the committed bundle changes and the pages are regenerated
- **THEN** the page diff corresponds to the bundle diff and nothing else

#### Scenario: Repeated generation
- **WHEN** the pages are generated twice from the same bundle
- **THEN** the two outputs are byte-identical

### Requirement: Field table per object
Each frame or service page SHALL document every object of the profile in its own table listing, for each field cited by the guidelines, its cardinality from the XSD, type, example, meaning and source section of the guidelines.

#### Scenario: Nested object
- **WHEN** a reader opens the TimetableFrame page
- **THEN** the ServiceJourney table links to the table of its passing times, and the XSD fields not cited by the guidelines are listed in a collapsed box "Altri campi dell'XSD"

### Requirement: Stable anchors
Each object table and each inconsistency SHALL have an anchor derived from the object path or the inconsistency id, not from the table number of the guidelines.

#### Scenario: Link through the current alias
- **WHEN** a reader follows a link to an object table of the overview page through `netex/corrente/`, for example `netex/corrente/#publicationdelivery`
- **THEN** they land on the same table under the current version folder

#### Scenario: Link to a frame table
- **WHEN** a reader follows a link to an object table of a frame page with the explicit version, for example `netex/5.0.0/timetable-frame/#vehiclejourneys-servicejourney`
- **THEN** they land on that table, and the anchor stays the same in later profile versions that keep the object

### Requirement: Published inconsistencies
Each profile version SHALL have a page listing the inconsistencies between the guidelines, the XSD and the examples, and every field affected by one SHALL link to its entry.

#### Scenario: Field with an inconsistency
- **WHEN** a reader follows the "⚠ Incongruenza" link of a field
- **THEN** the inconsistencies page opens at the entry for that field
