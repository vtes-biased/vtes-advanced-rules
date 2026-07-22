# Advanced Rules — working notes

State record and open-items list for `docs/advanced-rules.md`. The production pipeline
is finished and its machinery was deleted in the 2026-07-21 cleanup (everything remains
recoverable from git history before that commit). This file is no longer a pipeline
checklist; it is the project's state, its open work, and the notes that keep future
sessions from re-deriving settled things.

## Where things stand (2026-07-21)

- **The document is complete**: 64 sections, 6 chapters, ~750 footnotes, all drafted,
  assembled, and corrected by the owner-adjudicated whole-document pass (R-017, 118
  edits) plus phantom-citation and footnote-verification fixes.
- **`docs/advanced-rules.md` is the sole source of truth. Edit it directly.** The
  assembly pipeline (`assemble.py` + `sections/`) was retired and deleted: it had
  diverged from the corrected document, and one re-run would have silently reverted
  every applied fix (rulemonger finding R-022).
- **Reference convention (changed 2026-07-21):** one inline marker per footnote (first
  occurrence only); all definitions consolidated in a single `## References` section at
  the end of the document (no per-section blocks); ruling reference IDs are markdown
  links to their `references.yaml` URLs, `[RBK anchor]` links to
  `https://www.vekn.net/rulebook#anchor`. IDs with no URL (phantoms, upstream holes)
  stay as plain labels.
- Final classification over 2,605 rulings: P 1074 / E 1299 / C 227 / G 5, coverage
  91.1%. 60% of the corpus is template duplication — that is why the document
  compresses as hard as it does.

## What lives in docs/_work now (reference shelf)

- `owner-rulings.md` — **the highest authority in this project.** Lionel's binding
  rules calls, each verified against printed card text. Outranks the rulings database's
  paraphrases and any analysis file. Read before touching any section it covers.
- `classification.tsv` — canonical ruling→section labels, 2,605 rows,
  `id<TAB>codes<TAB>P|E|C|G<TAB>note`.
- `rulings-flat.tsv` — the flattened rulings snapshot the `R####` ids key to. Frozen,
  and generated from a database snapshot OLDER than the pinned submodule (upstream
  later de-duplicated); consequences documented in `phantom-id-audit.md`.
- `taxonomy.md` — the 64 section codes with the rationale for every addition and the
  rejected candidates. Authoritative for the code list.
- `tensions.md` — the adjudicated contradictory-polarity slugs (including the RESOLVED
  mandatory-action-satisfaction call). Candidate seed checklist for a consistency
  sweep (offered, not yet decided).
- `review.md` — candidate questions for an upstream Rules Director review (one entry
  as of 2026-07-22: the Edge-steal / mid-action-burn question). The diablerie-window,
  override-lapse and torpor-combat entries were closed by owner adjudication 2026-07-22
  (rulemonger R-027); the "inverted paraphrase" flag on LSJ 20100604-1 was our own
  misread — LSJ corrected himself downthread — and is withdrawn.
- `phantom-id-audit.md` — citation forensics for the ~35 reference IDs absent from the
  pinned database; disposition table, deliberate leftover markers, ⚠ rules flags.
- `drafter-contract.md` — the style contract the document was written to. Judge any
  edit's style against this, not against taste.

## Open items

1. **Appendix A (wording-template glossary) — DONE, owner-approved 2026-07-22**: ~150
   alphabetical entries, each one gloss plus its governing section link. Harvest notes:
   [FLIGHT] is treated in §4.2.4 (not §5.7.6); Red List has no document treatment to
   index. Appendix B (card index) was dropped by owner decision 2026-07-21.
2. **Known defects — cleared 2026-07-22.** "Futility" is now defined where it lives
   (§1.6.5 opens "Futility is no bar by default"); heading drift fixed (§4.5/§5.7/§6.9
   "&" → "and", anchors updated; §4.7 → "Strike: Combat Ends"). Compression:
   re-measured under the uniform 120-column wrap (2026-07-22) — every flagged section
   now measures 38–52 non-blank lines, all below the §1.6 benchmark itself (63); the
   compression defect list is empty. The whole document was rewrapped to 120 columns
   (2026-07-22; keep new edits inside it).
3. **Phantom-audit rules checks — CLOSED 2026-07-22.** {Archon Investigation} (§3.3):
   clean — the upstream deletion of [LSJ 20070203] folded the early gate into the
   current printing ("after blocks are declined"); no timing change; record-key repairs
   applied ([^2-2-5], [^1-2-14]) and [LSJ 20070203] re-added to [^3-3-8] with its live
   URL (owner call; R-028). {Arika} (§5.2): confirmed REVERSED by [ANK 20250121]; owner
   confirmed, split-sentence edit applied — {Anarch Revolt} keeps the end-of-phase
   check, the resolves-once model carries the new [^5-2-30] (R-026, findings in
   `.claude/references/rulemonger/findings/arika-5-2.md`).
4. **tensions.md consistency sweep** — use the slugs as a one-time seed checklist for a
   cross-section consistency pass (offered, undecided). Spot-check 2026-07-22: all four
   unresolved slugs already have document treatments; the sweep would only verify
   cross-section consistency of each stated resolution.
5. **Upstream data gap — closed 2026-07-22.** After pulling 241a7e3, zero reference IDs
   cited in `rulings.yaml` are missing from `references.yaml` (1,431 cited / 1,549
   defined) — upstream restored the hole; adding entries now would be dangling. Still
   open upstream: vtes-biased/vtes-rulings#8 (the accidentally deleted G00031 record
   and its `ANK 20210309-3` reference); nothing needed here when it lands.

## Maintenance workflow

- **Verification and rulings-database updates:** the rulemonger agent
  (`.claude/agents/rulemonger.md`), deliberately detached from `docs/_work/` — it works
  from the document plus the citable sources only. It runs FINDINGS-ONLY: it returns
  exact ready-to-apply edits and the main session applies them after owner
  adjudication.
- **Refreshing rulings:** `cd vtes-rulings && git pull`, commit the new submodule
  pointer, then have the rulemonger map changed rulings to affected sections (the
  document's footnotes are the ruling→section index).
- **Corpus queries:** `classification.tsv` joined to `rulings-flat.tsv`. Remember the
  snapshot is stale relative to the pinned database — check `phantom-id-audit.md`
  before trusting an ID exists upstream.
- History of rules changes (when a rule changed or was reverted):
  https://gist.githubusercontent.com/lionel-panhaleux/a4a9cad2e492af7c45c50a1cea7e6cf6/raw/92a6f169931c08ea3a4ae62ccbf2d6da17bc8970/VTES%2520History%2520of%2520changes.md
- Python for the YAML files: `.venv/bin/python` (venv has pyyaml). If touching the
  vtes-rulings database itself, run its own `make test` there.

## How the document was made (compressed history, June–July 2026)

Flatten 2,605 rulings → taxonomy (61 codes, grown to 64 on evidence; 6.8 deleted, not
renumbered) → two-round opus calibration (independent double-pass agreement ~94%) →
18-way sonnet classification (~1.95M tokens, 0 failures) → 275-row recheck → 68-unit
opus section review (quota-inflated: 68/68 produced findings despite "no finding is a
valid result" in capitals; its one durable output: 60% of the corpus is template
duplicates) → per-section extracts → two-wave opus drafting (wave 1 rejected on style,
4× too long; contract gained brevity + mandatory card-text verification; 64/64 drafted,
1,345 card texts verified) → assembly → owner correction pass (R-017).

Durable lessons, kept because they will recur: settle a rules call BEFORE launching an
agent wave (a mid-flight change raced the drafters three times; agents that flag stale
inputs instead of guessing are what saved the run); reviewers produce findings to a
quota unless forced to earn them; classification agents must be self-contained (N
agents choosing their own reading is N chances to drift); the awk strnum trap —
`-v C="3.10"` compares equal to `"3.1"`, so match section codes via string-keyed array
subscripts, and verify field indices after any `join`.
