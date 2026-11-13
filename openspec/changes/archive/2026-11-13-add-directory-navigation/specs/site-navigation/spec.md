# Spec Delta — site-navigation

## Purpose

Defines how readers move through the rpsd-doc site: the top-level sections shown as tabs, the sidebar of the current section, and how navigation is declared per directory so that new sections need no site configuration change.

## ADDED Requirements

### Requirement: Top-level sections
The site SHALL expose its main sections as top-level tabs in this order: Home, NeTEx, SIRI, Indicatori, Guida operativa.

#### Scenario: Reader on any page
- **WHEN** a reader is on any page
- **THEN** the tabs are visible and the tab of the current section is marked as active

### Requirement: Navigation defined per directory
The navigation of a section SHALL be defined by files inside that section's directory, so that adding a section or a subsection requires no change to the site configuration file.

#### Scenario: New subsection
- **WHEN** a directory with pages and its own navigation file is added under an existing section
- **THEN** it appears in the sidebar after a rebuild, with no edit to the site configuration

### Requirement: Sidebar limited to the current context
The sidebar SHALL show the pages of the current section with only the branch of the current page expanded.

#### Scenario: Deep page
- **WHEN** a reader opens a page three levels deep
- **THEN** its ancestors are expanded and sibling branches are collapsed
