# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## What this repository is

A **writing project**, not a software project: it produces `docs/extended-rules.md`, a
judge-level companion to the [VTES rulebook](https://www.vekn.net/rulebook) that
synthesizes ~2,605 individual rulings into general principles organized by game mechanic.
There is no build, no test suite, no package. The deliverable is one Markdown file.

**The document is complete** — 64 sections in 6 chapters, ~750 footnotes, drafted,
assembled, and corrected through an owner-adjudicated whole-document pass. The project is
in maintenance mode: remaining work is polish (Appendices A/B, the open items in
`docs/_work/WORKING-NOTES.md`) and keeping the document true as rulings evolve upstream.

**`docs/extended-rules.md` is the sole source of truth. Edit it directly.** The
generation pipeline (classification chunks, extracts, section drafts, `assemble.py`) was
retired and deleted on 2026-07-21; it survives only in git history. Do not resurrect it.

## docs/_work — the reference shelf

What remains under `docs/_work/` is deliberately kept reference material, not pipeline
scaffolding:

- `WORKING-NOTES.md` — **read this first**: current state, open items, maintenance
  workflow, compressed project history.
- `owner-rulings.md` — **the highest authority in this project.** Binding rules calls by
  Lionel, each verified against printed card text. Outranks the rulings database's
  paraphrases and any other analysis. Read it before touching any section it covers.
- `classification.tsv` — canonical ruling→section labels: 2,605 rows,
  `id<TAB>codes<TAB>P|E|C|G<TAB>note`.
- `rulings-flat.tsv` — the flattened rulings snapshot those `R####` ids key to. Frozen,
  and older than the pinned submodule (upstream de-duplicated afterwards) — see
  `phantom-id-audit.md` before assuming a cited ID exists upstream.
- `taxonomy.md` — the 64 section codes (chapter 6 skips 8, deliberately not renumbered)
  with the rationale for every added code and the rejected candidates. Authoritative for
  the code list; read it before proposing a new section.
- `tensions.md` — adjudicated contradictory-polarity ruling groups; candidate seed for a
  future consistency sweep.
- `phase8-inbox.md` — open work queue: drafter-raised objections and card-text-vs-ruling
  conflicts awaiting triage.
- `phantom-id-audit.md` — citation forensics for reference IDs absent from the pinned
  database: disposition table, deliberately retained markers, two ⚠ rules flags.
- `drafter-contract.md` — the style contract the document was written to. Judge edits
  against this, not against taste.

Verification and post-update maintenance run through the **rulemonger agent**
(`.claude/agents/rulemonger.md`): it is deliberately detached from `docs/_work/` and
works from the document plus the citable sources; it reports findings and exact edits
rather than editing the document itself.

## Source data (outside this repo)

The document cites, but does not contain, the rulings database. Both sources are **git
submodules** — run `git submodule update --init` on a fresh clone:

- `vtes-rulings/` ([vtes-biased/vtes-rulings](https://github.com/vtes-biased/vtes-rulings))
  — the database is at `vtes-rulings/rulings/`: `rulings.yaml` (keyed by
  `<card_id>|<card_name>` or by group `G#####|<name>`), `groups.yaml`, `references.yaml`
  (ruling ID → URL).
- `rulebook2024/` ([GiottoVerducci/rulebook2024](https://github.com/GiottoVerducci/rulebook2024))
  — `content.md` is the base 2024 rulebook, verbatim with `vekn.net/rulebook` anchors.
  This is the citable rulebook (`[RBK …]` footnotes).

Submodules pin a commit: the rulings database moves upstream, so `cd vtes-rulings && git
pull` (then commit the new pointer here) when rulings need refreshing — then have the
rulemonger map the changed rulings to affected sections (the document's footnotes are the
ruling→section index).
- Card text for verification: `https://api.krcg.org/card/<id-or-name>`, key `card_text`.
- Rules-change history gist (when a rule changed or was reverted) — URL in
  `WORKING-NOTES.md`.

Ruling reference prefixes are Rules Directors and sources: `TOM`, `SFC`, `JON`, `LSJ`,
`PIB`, `ANK` (successive directors), `RTR` (Rules Team Ruling), `RBK` (rulebook anchor).

### The `vtes` skill — read it first, cite the sources

The `vtes` skill (`~/.claude/skills/vtes/`) provides game terminology plus
`references/*.md`. These files are **deliberately condensed for agent consumption** —
note-form digests that are far cheaper to read than the originals. Use them as the
default first read for orientation, terminology, and locating which rule governs a
question.

They are digests, not source texts, so nothing quoted from them may land in the document.
Once you know what you're looking for, get the wording from the citable source:

- `vtes-rules.md` (35KB) — condensed rules digest. For anything that reaches the page,
  quote `rulebook2024/content.md` (~4× longer, verbatim, with rulebook anchors).
- `judges-guide-v2.md` (35KB) — despite the name, this is the *Tournament Conduct &
  Infraction Guide*: penalties, judge procedure, infraction categories. Tournament
  conduct rather than rules interactions, so mostly out of scope here.
- `tournament-rules.md`, `game_terms.json` (multilingual terms), `code-of-ethics.md`,
  `rules-feedback.md`, `judges-guide.md` (v1, legacy).

(The skill's file-size table lists pre-condensation sizes, e.g. 128KB for `vtes-rules.md`;
the actual files are the smaller ones above.)

## Style rules for the document

These were validated by the user; deviating from them is a regression.

- Mechanics-first, 6 chapters, judge-level terse prose. Precision over accessibility;
  full fluency with the base rules is assumed. §1.6 is the accepted density benchmark.
- **No exhaustive card lists.** Tie a rule to its wording template, then give "e.g." plus
  one to three cards.
- Be synthetic: cross-reference other sections rather than repeating, and merge redundant
  subsections.
- Card names in braces `{Abbot}`; disciplines and card types in brackets `[pot]`, `[POT]`,
  `[ACTION]`.
- Every derived statement carries a footnote. **Footnote conventions (since 2026-07-21):**
  one inline marker per footnote — its first occurrence only; all definitions live in a
  single `## References` section at the end of the document (no per-section blocks);
  labels are section-prefixed (`[^4-4-1]`) and unique document-wide; ruling IDs in a
  definition are markdown links to their `references.yaml` URLs and `[RBK anchor]` links
  to `https://www.vekn.net/rulebook#anchor`, e.g.
  `[^c1]: [LSJ 20061207](https://…) [RBK playing-a-card](https://www.vekn.net/rulebook#playing-a-card) — group "Cancel" (G00058).`
  IDs with no URL (phantoms, upstream holes) stay as plain unlinked labels — do not
  delete them; see `docs/_work/phantom-id-audit.md`.
- Pure one-card text interpretations stay in the rulings database and do not enter this
  document.
- `⚠ REVIEW` marks a point that still needs judge confirmation.
- For anything deeper, the full style contract is `docs/_work/drafter-contract.md`.

## Domain gotchas already established

- Rulebook actions are **not** subject to the No Repeated Action rule — only card
  name/copy rules are. Sameness matters only for card effects (`{Obedience}`,
  `{Red Herring}`, `{Change of Target}`).
- `rulings.yaml` wording sometimes paraphrases the original ruling. Verify against actual
  card text and, when it matters, the original ruling (VEKN forum posts are fetchable;
  LSJ Google Groups archives are not practical).
- `owner-rulings.md` settles its points: do not re-derive, soften, or `⚠ REVIEW` them.

## Tooling

Python work on the YAML files uses `.venv/bin/python` (create the venv with `pyyaml` if
absent). The `vtes-rulings` repo has its own `make test`
(`black`/`ruff`/`yamllint`/`check_rulings.py`) — run it there, not here, if you touch that
database.

**awk gotcha when matching section codes.** `awk -v C="3.10"` creates a *strnum*, which
compares numerically equal to `"3.1"` — so a naive `a[i]==C` silently folds section 3.1
into 3.10. This produced a wrong count once already. Match codes via array subscripts
(always string keys) or force string context (`a[i] "" == C ""`). The same trap applies to
any `3.7.x` vs `3.7` comparison.

**Verify field indices after `join`.** `join` shifts columns (`1=key`, then file1's
remaining fields, then file2's), so an index copied from a pre-join script reads the wrong
column and quietly reports zero violations. Print one joined row and count before trusting
any validation built on it.
