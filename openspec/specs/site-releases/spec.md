# site-releases Specification

## Purpose

Defines how the rpsd-doc site is released: how releases are numbered, how a release is marked in the repository and how it is kept consistent with the «Release del sito» page that readers see.

## Requirements

### Requirement: Release numbering
Every release of the site SHALL have a version number of the form X.Y.Z, greater than the version of the previous release.

#### Scenario: Valid release list
- **WHEN** the «Release del sito» page lists its releases
- **THEN** every version has the form X.Y.Z and the versions decrease from the first row to the last

#### Scenario: Release out of order
- **WHEN** a pull request adds a release whose version is not greater than the previous one
- **THEN** the check on the pull request fails and names the version

### Requirement: Release tag matches the changelog
A release SHALL be published only from an annotated tag vX.Y.Z on a commit of the main branch whose «Release del sito» page lists X.Y.Z as its first row.

#### Scenario: Tag consistent with the page
- **WHEN** the tag v0.1.0 is pushed on a commit of main whose release page starts with 0.1.0
- **THEN** the release check passes

#### Scenario: Tag not matching the page
- **WHEN** a tag is pushed whose version is not the first row of the release page, or that points to a commit outside main
- **THEN** the release check fails, names the mismatch and the site is not published
