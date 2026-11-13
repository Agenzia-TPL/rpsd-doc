# Spec Delta — site-platform

## Purpose

Defines how the rpsd-doc site is built, checked and published, and which rendering features its pages can rely on (annotated XML, tabbed variants, formulas, diagrams, Italian search) at the expected size.

## ADDED Requirements

### Requirement: Reproducible build
The site SHALL build from a clean checkout with a single documented command, using dependency versions pinned in the repository.

#### Scenario: Clean build
- **WHEN** a contributor installs the pinned dependencies and runs the build command on a clean checkout
- **THEN** the site is produced with no errors and no warnings in strict mode

#### Scenario: Broken internal link
- **WHEN** a page links to another page or anchor that does not exist
- **THEN** the strict build fails and names the page and the broken link

### Requirement: Automated deployment
The site SHALL be published to its public URL automatically when the main branch changes, and only when the strict build succeeds.

#### Scenario: Merge to main
- **WHEN** a change is merged into the main branch and the strict build passes
- **THEN** the published site reflects the change without manual steps

#### Scenario: Failing build
- **WHEN** the strict build fails on the main branch
- **THEN** the published site is left unchanged

### Requirement: Pull request preview check
Every pull request SHALL be built in strict mode before it can be merged.

#### Scenario: Pull request with an error
- **WHEN** a pull request introduces a build error
- **THEN** the check on the pull request fails

### Requirement: Annotated XML examples
Pages SHALL be able to show XML code blocks with syntax highlighting, a copy button and numbered inline annotations that explain individual lines.

#### Scenario: Annotated NeTEx fragment
- **WHEN** a reader opens a page containing an annotated XML block
- **THEN** the XML is highlighted, each annotation marker opens its explanation, and the copied text contains no annotation markers

### Requirement: Alternative example variants
Pages SHALL be able to present alternative variants of the same example as tabs.

#### Scenario: Minimal and complete variant
- **WHEN** a page offers a "Minimale" and a "Completo" variant of an example
- **THEN** the reader can switch between them without leaving the page

### Requirement: Mathematical formulas
Pages SHALL render mathematical formulas written in LaTeX notation, inline and as display blocks.

#### Scenario: Indicator formula
- **WHEN** a page contains the formula of an indicator
- **THEN** the formula is rendered as typeset mathematics, not as source text

### Requirement: Diagrams from text
Pages SHALL render diagrams written as Mermaid source.

#### Scenario: Flow diagram
- **WHEN** a page contains a Mermaid flowchart or sequence diagram
- **THEN** the diagram is rendered as a graphic in both light and dark colour schemes

### Requirement: Italian interface and search
The site interface SHALL be in Italian and full-text search SHALL find Italian content.

#### Scenario: Search for an Italian term
- **WHEN** a reader searches for a word that appears in a page body
- **THEN** the page is listed in the results and the match is highlighted on the page

### Requirement: Scale
The site SHALL remain usable and build in acceptable time with at least 400 pages.

#### Scenario: Large section
- **WHEN** the site contains a section with 400 pages
- **THEN** the build completes within the agreed time limit and the sidebar shows only the current section's pages
