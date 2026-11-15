## ADDED Requirements

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
