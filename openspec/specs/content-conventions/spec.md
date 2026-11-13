# content-conventions Specification

## Purpose

Defines the cross-cutting rules every page of the rpsd-doc site follows — generated versus hand-written pages, page length, stable URLs, callout meanings and glossary links — and how they are enforced by checks on the repository.

## Requirements

### Requirement: Generated pages are identifiable
Every generated page SHALL declare in its metadata that it is generated and by which tool, and SHALL live in a directory that contains only generated pages.

#### Scenario: Hand edit of a generated page
- **WHEN** a pull request not produced by the generation tool modifies a file in a generated directory
- **THEN** the check on the pull request fails and explains that the source data must be changed instead

### Requirement: Page length limit
Hand-written pages SHALL NOT exceed 1500 words.

#### Scenario: Oversized page
- **WHEN** a hand-written page exceeds 1500 words
- **THEN** the check reports the page and its word count

### Requirement: Stable URLs
A published page URL SHALL keep resolving after the page is moved or renamed.

#### Scenario: Page moved
- **WHEN** a published page is moved to a new path
- **THEN** the old URL redirects to the new one

### Requirement: Consistent callouts
Pages SHALL use a fixed set of callout types with fixed meanings: note, tip, warning, danger "Obbligatorio per KPI", example, info "Novità Rapsodia".

#### Scenario: Field required for an indicator
- **WHEN** a page documents a field whose absence prevents the calculation of an indicator
- **THEN** the field is marked with the danger callout titled "Obbligatorio per KPI"

### Requirement: Linkable glossary
Each glossary term SHALL have its own anchor, and pages SHALL link domain acronyms to the glossary on first use.

#### Scenario: Acronym in a page
- **WHEN** a page uses the acronym "PdE" for the first time
- **THEN** it links to the "PdE" entry of the glossary
