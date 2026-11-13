# rpsd-doc — Seed per OpenSpec

> Derivato da `rpsd-doc-site-design.md` v0.3 (11 novembre 2026).
> Copre il **primo step** (parte generale). Il secondo step (contratti, regole di validazione, contratti riservati) è solo elencato: si specifica quando il modello del config è consolidato.

Come usarlo:

1. `openspec init` nel repo `rpsd-doc`, poi incolla il blocco del §1 in `openspec/config.yaml`.
2. Copia `rpsd-doc-site-design.md` nella radice del repo: è il riferimento che il config cita.
3. Per ogni change del §3, nell'ordine: `/opsx:propose <nome>` passando come descrizione il testo del change e i requisiti del §4 indicati. I requisiti sono già in formato delta (`## ADDED Requirements`), quindi la bozza generata va solo rivista.
4. `/opsx:apply`, verifica, `/opsx:archive`. Le spec consolidate finiscono in `openspec/specs/<capability>/spec.md`.

Nota sulla lingua: requisiti e scenari sono in inglese perché il formato OpenSpec si appoggia alle parole chiave SHALL/MUST e WHEN/THEN; non ho verificato se la validazione accetta equivalenti italiani. Il contenuto del sito resta in italiano.


## 1. `openspec/config.yaml`

```yaml
schema: spec-driven

context: |
  rpsd-doc is the static documentation site of Rapsodia, a public-transport (TPL)
  monitoring platform for the Lombardy transport agencies. The site documents the
  Italian NeTEx and SIRI profiles, the ART quality indicators (Delibera ART 53/2024)
  and, in a later step, one section per service contract.

  Full design: rpsd-doc-site-design.md (repo root). Read it before proposing a change.

  Tech stack:
  - Generator: Zensical (pinned version), configuration kept in mkdocs.yml
  - Navigation: per-directory .nav.yml files (awesome-nav), no nav in mkdocs.yml
  - Plugins in use: search, tags, glightbox, redirects, awesome-nav
  - Not used by decision: mike, macros, git-revision-date-localized, gen-files
  - Hosting: GitHub Pages, deployed by GitHub Actions
  - Python tooling only; no Node toolchain
  - Fallback generator if Zensical fails the spike: Docusaurus

  Content rules:
  - Site content is in Italian; terms that are proper names of the standards
    (frame, delivery, element names) stay in English
  - A page is either hand-written or generated, never both. Generated directories
    are overwritten as a whole by rpsd-tools and are never edited by hand
  - NeTEx and SIRI profile docs are versioned by path: docs/netex/<version>/,
    docs/siri/<version>/. A new profile version is a new folder
  - General pages carry no contract thresholds and no tender-annex references
  - Indicator codes, rule ids, contract ids and published URLs are stable
  - Hand-written pages are at most 1500 words

  Out of scope for now (second step, blocked on the rpsd-config data model):
  docs/contratti/, the validation rule catalog, restricted contracts.

rules:
  proposal:
    - State which sections of rpsd-doc-site-design.md the change implements
    - State whether the change touches hand-written content, generated content, or site infrastructure
  specs:
    - Write requirements as observable behavior of the built site or of the build, checkable by a reader or by CI
    - One SHALL or MUST per requirement; at least one WHEN/THEN scenario each
    - Keep generator-specific mechanics (plugin options, template code) in design.md
  design:
    - Use only features available in both Zensical and Material for MkDocs unless the proposal justifies otherwise
  tasks:
    - End every change with a strict build (`zensical build --strict`) and a check of the rendered pages touched
    - Never include tasks that push, open PRs or change repository settings on GitHub without explicit approval
```


## 2. Capability

| Capability (`openspec/specs/…`) | Contenuto |
|---|---|
| `site-platform` | Build, deploy, configurazione, funzioni di rendering richieste |
| `site-navigation` | Tab, sidebar, navigazione per directory |
| `content-conventions` | Regole trasversali: lingua, lunghezza, admonition, pagine generate, URL stabili |
| `profile-versioning` | Versioni dei profili NeTEx/SIRI per percorso |
| `profile-docs` | Struttura e template delle pagine di profilo (frame NeTEx, servizi SIRI) |
| `overview` | Home, panoramica, glossario, modello dati con link alla documentazione dbt |
| `indicator-catalog` | Delibera, catalogo delle definizioni ART, matrice indicatori × dataset |
| `operational-guide` | Guida per Aziende e Agenzie, funzionamento della validazione, FAQ |

Secondo step, da non specificare ora: `contracts`, `validation-rules`, `restricted-contracts`, `doc-generation` (interfaccia bundle ↔ `rpsd-tools`).


## 3. Change, nell'ordine

| # | Change | Cosa fa | Requisiti (§4) |
|---|---|---|---|
| 1 | `bootstrap-site` | Repo, Zensical con versione bloccata, `mkdocs.yml`, tema e lingua, build e deploy via CI. Include lo spike: una pagina di prova per ogni funzione di rendering richiesta | `site-platform` |
| 2 | `add-directory-navigation` | Tab di primo livello e sidebar definite da `.nav.yml` | `site-navigation` |
| 3 | `add-content-conventions` | Controlli in CI sulle convenzioni e pagina "come contribuire" | `content-conventions` |
| 4 | `add-profile-versioning` | Scheletro `netex/5.0.0/`, `siri/1.0.5/`, pagine elenco versioni, avviso sulle versioni non correnti, alias `corrente` | `profile-versioning` |
| 5 | `add-overview-pages` | Home, progetto, architettura, glossario, modello dati | `overview` |
| 6 | `add-netex-profile-docs` | Introduzione, concetti, una pagina per frame, esempi (NeTEx 5.0.0) | `profile-docs` |
| 7 | `add-siri-profile-docs` | Introduzione, concetti, una pagina per servizio, esempi (SIRI 1.0.5) | `profile-docs` |
| 8 | `add-indicator-catalog` | Pagine sulla delibera, catalogo generato, matrice | `indicator-catalog` |
| 9 | `add-operational-guide` | Guida operativa e FAQ | `operational-guide` |

Il change 1 è anche il punto di decisione sullo stack: se uno scenario di `site-platform` non è soddisfacibile con Zensical, si ferma tutto e si valuta il piano B prima dei change successivi.


## 4. Requisiti

### 4.1 `site-platform`

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


### 4.2 `site-navigation`

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


### 4.3 `content-conventions`

## ADDED Requirements

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


### 4.4 `profile-versioning`

## ADDED Requirements

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


### 4.5 `profile-docs`

## ADDED Requirements

### Requirement: One page per frame and per service
Each profile version SHALL document every NeTEx frame of the Italian profile and every SIRI functional service in use on its own page.

#### Scenario: NeTEx frames
- **WHEN** a reader opens the frame list of a NeTEx profile version
- **THEN** there is one page each for GeneralFrame, ServiceCalendarFrame, ResourceFrame, SiteFrame, ServiceFrame, TimetableFrame, FareFrame and MobilityServiceFrame

#### Scenario: SIRI services
- **WHEN** a reader opens the service list of a SIRI profile version
- **THEN** there is one page each for SIRI-PT, SIRI-ET, SIRI-VM, SIRI-SM, SIRI-SX and SIRI-FM

### Requirement: Uniform page structure
Every frame page and every service page SHALL follow the same section structure: role, when it is used, structure with a field table, contained entities, Rapsodia extensions, XML example.

#### Scenario: Field table
- **WHEN** a reader opens the structure section of a frame or service page
- **THEN** each field is listed with type, whether it is mandatory, an example and a description

### Requirement: Extensions are distinguishable
Fields and structures added to the Italian profile for the ART indicators SHALL be visibly marked as Rapsodia extensions.

#### Scenario: Extended field
- **WHEN** a page documents a field introduced by the profile extension
- **THEN** it is marked with the "Novità Rapsodia" callout

### Requirement: Runnable examples
Each profile version SHALL provide complete example files that can be downloaded and that are valid against the schema of that profile version.

#### Scenario: Download and validate
- **WHEN** a reader downloads an example file from the examples section
- **THEN** the file validates against the XSD of the profile version it belongs to

### Requirement: Fundamentals
Each profile version SHALL explain the concepts needed before reading the frame or service pages: overall document structure, identifier conventions, date/time and coordinate formats.

#### Scenario: Identifier convention
- **WHEN** a reader opens the identifier conventions page
- **THEN** the pattern is stated with at least one valid and one invalid example


### 4.6 `overview`

## ADDED Requirements

### Requirement: Landing page
The home page SHALL state in one screen what Rapsodia is and who the site is for, and SHALL link to each main section.

#### Scenario: First visit
- **WHEN** a reader opens the home page
- **THEN** they see a one-sentence description, one entry point per main section, and the current versions of the NeTEx and SIRI profiles

### Requirement: Project and architecture overview
The site SHALL describe the project (goals, consortium, partners) and the high-level architecture with a diagram of the data flow, without implementation detail.

#### Scenario: Architecture page
- **WHEN** a reader opens the architecture page
- **THEN** a diagram shows the flow from the transport operators to the dashboards, with the role of each component in one or two sentences

### Requirement: Glossary
The site SHALL provide an alphabetical glossary of the domain terms used across the site.

#### Scenario: Term lookup
- **WHEN** a reader opens the glossary
- **THEN** terms are in alphabetical order and each has a definition and its own anchor

### Requirement: Data model entry point
The site SHALL describe the layers of the data model and SHALL link to the database documentation generated by dbt, which is published separately.

#### Scenario: Reader with access
- **WHEN** a reader follows the link from the data model page
- **THEN** they reach the dbt documentation, or an access-controlled page if it is not public

### Requirement: Site changelog
The site SHALL list its changes in reverse chronological order.

#### Scenario: New profile version documented
- **WHEN** the documentation of a new profile version is published
- **THEN** the changelog has an entry with the date and the version


### 4.7 `indicator-catalog`

## ADDED Requirements

### Requirement: Regulatory background
The site SHALL explain Delibera ART 53/2024, the minimum quality conditions and the mechanism of minimum levels and penalties, citing measure and paragraph numbers.

#### Scenario: Reader looks for the source of an indicator
- **WHEN** a reader opens an indicator page
- **THEN** the measure of the Delibera that defines it is cited

### Requirement: One page per indicator
Each ART indicator SHALL have its own page with: short definition, regulatory reference, formal definition with formula, calculation and aggregation grain, partition, required data.

#### Scenario: Aggregation grain
- **WHEN** an indicator is aggregated in two stages
- **THEN** the page states both the calculation grain and the aggregation rule explicitly

### Requirement: Contract-agnostic definitions
Indicator pages in the general catalog SHALL NOT contain numeric thresholds, penalty amounts or references to the annexes of a specific tender.

#### Scenario: Threshold defined by the contract
- **WHEN** an indicator's minimum level is set by each contract
- **THEN** the page says that the level is defined per contract and gives no number

### Requirement: Generated catalog
Indicator catalog pages and the catalog summary SHALL be generated from a data file committed in the repository, and the pages SHALL match that file.

#### Scenario: Data file changes
- **WHEN** the committed data file changes and the pages are regenerated
- **THEN** the page diff corresponds to the data diff and nothing else

### Requirement: Indicator to data matrix
The site SHALL provide a matrix showing, for each indicator, which datasets it depends on.

#### Scenario: Reader checks dependencies
- **WHEN** a reader opens the matrix
- **THEN** each indicator row shows, per dataset, whether it is required, optional or not applicable, and links to the indicator page


### 4.8 `operational-guide`

## ADDED Requirements

### Requirement: End-to-end process for operators
The guide SHALL describe the process a transport operator follows from producing the data to receiving the validation outcome, with a sequence diagram.

#### Scenario: Operator reads the process page
- **WHEN** an operator opens the process overview
- **THEN** each step names who acts, what is sent and what comes back

### Requirement: Transmission and formats
The guide SHALL state how data is transmitted and which formats are accepted, with the conditions and limits of each.

#### Scenario: Accepted formats
- **WHEN** an operator opens the formats page
- **THEN** each accepted format is listed with when to use it and its limitations

### Requirement: How validation works
The guide SHALL explain the validation levels, the meaning of each severity and the possible outcomes, without listing contract-specific rules.

#### Scenario: Operator receives a blocking outcome
- **WHEN** an operator reads the validation page
- **THEN** they can tell a blocking outcome from a diagnostic one and what each implies

### Requirement: Guide for agencies
The guide SHALL describe the NeTEx approval workflow and how to read the KPI dashboards.

#### Scenario: Approval workflow
- **WHEN** an agency operator opens the approval page
- **THEN** the steps from reception to approval or change request are described in order

### Requirement: Linkable FAQ
The guide SHALL include frequently asked questions grouped by topic, each with its own anchor.

#### Scenario: Link to an answer
- **WHEN** someone shares the link to a question
- **THEN** the link opens the page at that question


## 5. Punti da decidere prima o durante i change

- **Change 1**: "tempo di build accettabile" va quantificato (scenario *Large section*).
- **Change 4**: granularità delle cartelle di versione (ogni versione adottata da un contratto, o solo major/minor).
- **Change 5**: documentazione dbt pubblica sotto lo stesso dominio o ad accesso controllato.
- **Change 6–7**: confine tra pagine generate da `rpsd-profile-gen` e contenuto redazionale. Se le pagine di frame/servizio sono generate, va aggiunto a `profile-docs` un requisito analogo a *Generated catalog*.
- **Change 8**: origine del file dati del catalogo indicatori finché il config non è consolidato (export del catalogo attuale o file del pilot).
- **Change 9** (o comunque quando ogni sezione con `"*"` nel proprio `.nav.yml` ha almeno una pagina oltre a `index.md`): riportare `logs.no_matches` di `awesome-nav` da `info` a `warning` in `mkdocs.yml`, così un pattern senza corrispondenze torna a bloccare il build strict. Impostato a `info` nel change 2 perché le sezioni segnaposto non hanno altre pagine.
- **Contratto della consegna di aprile 2027**: non coperto da questo seed; se va documentato prima del consolidamento del config serve un change dedicato.
