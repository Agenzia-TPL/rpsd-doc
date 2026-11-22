# Spec Delta

## MODIFIED Requirements

### Requirement: Automated deployment
The site SHALL be published to its public URL automatically when a release tag is pushed, and only when the release check and the strict build succeed.

#### Scenario: Release tag pushed
- **WHEN** a release tag is pushed, the release check passes and the strict build passes
- **THEN** the published site reflects the content of that release without manual steps

#### Scenario: Merge to main
- **WHEN** a change is merged into the main branch and no release tag is pushed
- **THEN** the published site is left unchanged

#### Scenario: Failing build
- **WHEN** the strict build fails for a release tag
- **THEN** the published site is left unchanged
