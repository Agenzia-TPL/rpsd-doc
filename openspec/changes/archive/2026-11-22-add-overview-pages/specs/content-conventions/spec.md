# Spec Delta

## MODIFIED Requirements

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
