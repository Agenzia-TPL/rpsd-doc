# Design — update-profile-bundles-0-8-0

## Context

Vedi proposal.md, «Why». Le pagine di `docs/netex/5.0.0/` e `docs/siri/1.0.5/` sono generate. `scripts/generate_profile_pages.py` le produce dal bundle `site.yaml` con i template di `templates/profili/` e copia `generator` del bundle nel campo `generato_da` del front matter. `CONTRIBUTING.md`, «Pagine dei profili NeTEx e SIRI», chiede di committare insieme bundle e pagine, con il trailer `Generato-da: rpsd-tools <versione>` preso da `generator`. Il checkout di rpsd-tools (`../rpsd-tools`) è su `main` ed è pulito.

## Goals / Non-Goals

**Goals:**
- Bundle uguali, byte per byte, a quelli che `v0.8.0` produce, e riproducibili.
- Un diff delle pagine che contiene solo le differenze attese.

**Non-Goals:**
- Toccare template, script o il checkout di lavoro di rpsd-tools.

## Decisions

### D1 — Generare da un worktree di rpsd-tools sul tag `v0.8.0`
I bundle si generano da `git worktree add <scratch>/rpsd-tools-v0.8.0 v0.8.0`, con `uv sync --all-packages` e `uv run rpsd-tools profile-docs generate profiles/netex-it|profiles/siri-it --out <dir>`.
- *Perché:* il `main` di rpsd-tools resta com'è, e il generatore è proprio quello del tag.
- *Alternativa scartata:* `git checkout v0.8.0` nel checkout principale. Sposta il branch di lavoro di un altro repo, e va poi rimesso su `main`.

### D2 — Riproducibilità verificata prima della copia
Si genera due volte, in due processi separati e in due cartelle di output diverse, e si confronta con `cmp`. Si confrontano anche le dimensioni con quelle del brief (1 039 126 byte per il NeTEx, 263 491 per il SIRI). Si copia in `data/` solo se le due esecuzioni coincidono.
- *Perché:* è il motivo della change. Se non coincidono ci si ferma e si segnala a Franco, senza commit.

### D3 — Diff delle pagine come controllo di accettazione
Dopo la rigenerazione, il diff atteso è questo:
- in tutti i file delle due cartelle di versione, solo la riga `generato_da`;
- in `docs/netex/5.0.0/resource-frame.md`, in più, righe della tabella spostate.

Per controllare la tabella si confrontano le righe ordinate, prima e dopo: devono coincidere (`diff <(sort old) <(sort new)` dà solo `generato_da`). Qualunque altra differenza blocca il commit finché non è capita.

### D4 — Nessuna release del sito in questa change
La decisione aperta del brief si risolve fuori dalla change: una release è un commit «Release X.Y.Z» con una sua PR (CONTRIBUTING, «Release del sito»). Per chi legge cambia solo l'ordine di una tabella, quindi la raccomandazione è di farla entrare nella prossima release. Franco può comunque chiedere una 0.1.1 subito dopo il merge.

### D5 — Un solo commit generato
Bundle e pagine vanno in un commit con il trailer `Generato-da: rpsd-tools 0.8.0`. Gli artefatti OpenSpec e la rimozione del brief superato vanno in un commit separato: non toccano percorsi generati e non hanno bisogno del trailer.

## Risks / Trade-offs

- [Le due generazioni non coincidono] → stop, nessun commit, segnalazione a rpsd-tools (D2).
- [Il diff delle pagine va oltre quello atteso, per esempio perché `uv sync` risolve una dipendenza diversa da quella fissata nel lock] → stop. Si confronta il bundle con quello atteso dal brief (70 e 2 righe diverse) prima di procedere.
- [Il worktree resta nello scratchpad] → alla fine si rimuove con `git worktree remove`.

## Migration Plan

Il merge su `main` non pubblica niente: il sito pubblicato cambia al prossimo tag di release. Per tornare indietro basta un revert del commit generato.
