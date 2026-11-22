# overview Specification

## Purpose

Defines the pages that present the site and the Rapsodia project to a reader: the home page, the description of the project and the changelog of the site.

## Requirements

### Requirement: Landing page
The home page SHALL state in one screen what Rapsodia is and who the site is for, and SHALL link to each main section.

#### Scenario: First visit
- **WHEN** a reader opens the home page
- **THEN** they see a one-sentence description, one entry point per main section, and the current versions of the NeTEx and SIRI profiles

### Requirement: Site changelog
The site SHALL list its releases in reverse chronological order, each with its version number, its date and the changes it includes.

#### Scenario: New profile version documented
- **WHEN** the documentation of a new profile version is published in a release
- **THEN** the row of that release has its version number and date and names the profile version among its changes

### Requirement: Latest versions on the home page
The home page SHALL show the most recent entries of the site changelog after the section entry points, with a link to the full changelog page.

#### Scenario: Bottom of the home page
- **WHEN** a reader scrolls past the section entry points on the home page
- **THEN** they see the latest site versions, identical to the top of the Release del sito page, and a link to that page
