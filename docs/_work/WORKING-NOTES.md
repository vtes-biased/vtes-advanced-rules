# Extended Rules — working notes

State record and open-items list for `docs/extended-rules.md`. The production pipeline
is finished and its machinery was deleted in the 2026-07-21 cleanup (everything remains
recoverable from git history before that commit). This file is no longer a pipeline
checklist; it is the project's state, its open work, and the notes that keep future
sessions from re-deriving settled things.

## Where things stand (2026-07-21)

- **The document is complete**: 64 sections, 6 chapters, ~750 footnotes, all drafted,
  assembled, and corrected by the owner-adjudicated whole-document pass (R-017, 118
  edits) plus phantom-citation and footnote-verification fixes.
- **`docs/extended-rules.md` is the sole source of truth. Edit it directly.** The
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
- `phase8-inbox.md` — open work queue: drafter-raised objections and card-text-vs-ruling
  conflicts (see Open items).
- `phantom-id-audit.md` — citation forensics for the ~35 reference IDs absent from the
  pinned database; disposition table, deliberate leftover markers, ⚠ rules flags.
- `drafter-contract.md` — the style contract the document was written to. Judge any
  edit's style against this, not against taste.

## Open items

1. **Appendix A (wording-template glossary) and Appendix B (card index)** — the two
   TODO stubs at the end of the document, and the highest-remaining-value navigation
   work (they are the intended lookup path for trait names like Scarce/Sterile/[FLIGHT]
   buried in §5.7.6, and for card names generally).
2. **phase8-inbox.md triage** — 3 live objections: §1.2 vs §1.15 on whether
   "(limited)" binds the action or the minion-per-round (rulebook says minion for
   additional strikes); §4.3's {Rigor Mortis} counterexample to §1.1's
   cannot-names-cards vs cannot-names-outcome test; §1.11 wanting §1.8's "retrieve
   cards played" clause scoped to canceled cards. Plus 34 card-text-vs-ruling conflicts
   drafters flagged rather than silently resolving.
3. **Known defects, identified and accepted as pending:** 12 compression candidates
   over 70 prose lines (1.13, 1.8, 2.4, 2.5, 3.3, 3.7.6, 4.3, 4.5, 5.2, 5.7, 6.2, 6.5 —
   §1.6 at 48 lines is the accepted density benchmark); the dangling term "futility"
   (§1.1/§1.8/§1.9/§4.2 cross-reference it as though §1.6 defines it — verify whether
   the R-017 pass already cured this); heading style drift ("&" vs "and": §4.5/§5.7/§6.9
   vs §6.1; §4.7 should match the game term capitalization "Strike: Combat Ends").
4. **Two ⚠ rules checks left over from the phantom audit.** The phantom citations
   themselves are gone (2026-07-21: three linked to their live originals, eleven
   removed — final disposition in `phantom-id-audit.md`), but two document claims
   formerly supported by retracted rulings still need a real rules check: {Arika}
   (§5.2 — surviving rulings look reversed, one tagged [REVERSAL] ANK 20250121) and
   {Archon Investigation} (§3.3 — possible timing change).
5. **Pending owner decision:** add a routing line in §2.1.3 pointing to §2.4.4
   (triggered-by-block precedence — an expert reader looked for it in §2.1 and it lives
   under §2.4.4's literal title; proposed 2026-07-21, not yet approved).
6. **tensions.md consistency sweep** — use the slugs as a one-time seed checklist for a
   cross-section consistency pass (offered, undecided).
7. **Upstream data gap:** 48 reference IDs cited in `rulings.yaml` have no entry in
   `references.yaml` (~3.5%). An upstream hole in vtes-biased/vtes-rulings, not a
   drafting error — do not "fix" by deleting citations. One restoration request is
   pending upstream (vtes-biased/vtes-rulings#8, `ANK 20210309-3`).

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
