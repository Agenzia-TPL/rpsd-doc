## MODIFIED Requirements

### Requirement: Top-level sections
The site SHALL expose its main sections as top-level tabs in this order: Rapsodia, Architettura, NeTEx, SIRI, Indicatori, Modello dati, Dashboard, Guida operativa, Contratti.

#### Scenario: Reader on any page
- **WHEN** a reader is on any page
- **THEN** the tabs are visible and the tab of the current section is marked as active

## ADDED Requirements

### Requirement: Every section has a landing page
Each top-level section SHALL have a landing page at the root of its URL path, including sections whose content is not yet published.

#### Scenario: Section without content yet
- **WHEN** a reader opens the tab of a section whose content is not yet published
- **THEN** a landing page with the section title and a notice that the content is being prepared is shown, not an error page

#### Scenario: Home page
- **WHEN** a reader opens the site root
- **THEN** the landing page of the Rapsodia section is shown and the Rapsodia tab is marked as active
