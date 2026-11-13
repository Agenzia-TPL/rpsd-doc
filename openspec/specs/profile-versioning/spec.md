# profile-versioning Specification

## Purpose

Defines how the documentation of the Italian NeTEx and SIRI profiles is versioned by path: one frozen directory per profile version, a version list per profile, notices on non-current versions, and a version-independent URL for the current one.

## Requirements

### Requirement: One directory per profile version
The documentation of each NeTEx and SIRI profile version SHALL live under a path that contains the version identifier.

#### Scenario: Current NeTEx profile
- **WHEN** a reader opens the ResourceFrame page of NeTEx profile 5.0.0
- **THEN** the URL contains `netex/5.0.0/`

### Requirement: Versions coexist
Publishing a new profile version SHALL leave the pages of previous versions online and unchanged.

#### Scenario: New profile version published
- **WHEN** the documentation of a new NeTEx profile version is added
- **THEN** every URL of the previous version still resolves to the same content

### Requirement: Version list
Each profile section SHALL have a landing page listing the documented versions with their status (corrente, precedente, ritirata), dates and a summary of differences.

#### Scenario: Reader looks for an older version
- **WHEN** a reader opens the NeTEx landing page
- **THEN** every documented version is listed with a link to its pages and its status

### Requirement: Non-current version notice
Every page of a non-current profile version SHALL show a notice that it is not the current version, with a link to the current one.

#### Scenario: Page of a previous version
- **WHEN** a reader opens a page under a non-current version
- **THEN** a notice at the top states the version status and links to the current version

### Requirement: Sidebar shows the current version
The sidebar of a profile section SHALL list the pages of the current version only.

#### Scenario: Two versions documented
- **WHEN** two NeTEx profile versions are documented
- **THEN** the sidebar lists the current version's pages, and the other version is reachable from the version list

### Requirement: Alias for the current version
Each profile section SHALL offer a version-independent URL that leads to the current version.

#### Scenario: Link from the operational guide
- **WHEN** a reader follows a link to `netex/corrente/`
- **THEN** they land on the current NeTEx profile version
