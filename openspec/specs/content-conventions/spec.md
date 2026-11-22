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
A published page URL SHALL keep resolving after the page is moved or renamed, unless the published page is only a placeholder: a title and the "Sezione in preparazione" notice, with no other content.

#### Scenario: Page moved
- **WHEN** a published page is moved to a new path
- **THEN** the old URL redirects to the new one

#### Scenario: Placeholder page removed
- **WHEN** a page that is published only as a placeholder is removed or moved without a redirect
- **THEN** the URL check passes and the old URL is no longer served

#### Scenario: Page with content removed
- **WHEN** a page whose published version has content beyond the placeholder notice is removed without a redirect
- **THEN** the URL check fails and lists the URL

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

### Requirement: Hand-written index of a generated section
A section whose subdirectories are generated SHALL be allowed to have a hand-written index page at its root, which the checks treat as hand-written.

#### Scenario: Contract list edited by hand
- **WHEN** a pull request not produced by the generation tool modifies the index page of the contracts section
- **THEN** the generated-pages check passes and the page is subject to the hand-written page rules

#### Scenario: Contract folder edited by hand
- **WHEN** a pull request not produced by the generation tool modifies a page inside a contract folder that is not a declared placeholder
- **THEN** the generated-pages check fails

### Requirement: Declared placeholders in generated paths
A placeholder page SHALL be allowed inside a generated path only if it is listed as a placeholder in the repository and marked as a placeholder on the published page.

#### Scenario: Placeholder contract
- **WHEN** the site is built with the placeholder contract `esempio`
- **THEN** the checks pass, and the contract page shows that it is a placeholder to be replaced by a generated contract

#### Scenario: Undeclared hand-written page in a contract folder
- **WHEN** a hand-written page is added to a contract folder that is not listed as a placeholder
- **THEN** the generated-pages check fails
