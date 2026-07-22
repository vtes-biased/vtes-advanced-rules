# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## What this repository is

A **writing project**, not a software project: it produces `docs/advanced-rules.md`, a
judge-level companion to the [VTES rulebook](https://www.vekn.net/rulebook) that
synthesizes ~2,605 individual rulings into general principles organized by game mechanic.
There is no build, no test suite, no package. The deliverable is one Markdown file.

**The document is complete** — 64 sections in 6 chapters, 714 footnotes, appendix
included, corrected through owner-adjudicated passes and a cross-section consistency
sweep (2026-07-22). The project is in maintenance mode: keep the document true as
rulings evolve upstream, and track the open Rules Director questions in
`docs/_work/review.md`.

**`docs/advanced-rules.md` is the sole source of truth. Edit it directly.** The
generation pipeline (classification chunks, extracts, section drafts, `assemble.py`) was
retired and deleted on 2026-07-21; it survives only in git history. Do not resurrect it.

## Reference files

- `docs/_work/review.md` — the open Rules Director questions (one entry as of
  2026-07-22: the Edge-steal / mid-action-burn question). The rest of the
  production-era reference shelf (WORKING-NOTES, taxonomy, tensions, the
  classification/rulings TSVs, phantom-id-audit) was retired on 2026-07-22 — recover
  any of it from git history.
- `.claude/references/owner-rulings.md` — **the highest authority in this project.**
  Binding rules calls by Lionel, each verified against printed card text. Outranks the
  rulings database's paraphrases and any other analysis. Read it before touching any
  section it covers.
- `.claude/references/drafter-contract.md` — the style contract the document was
  written to. Judge edits against this, not against taste.
- One open upstream item: vtes-biased/vtes-rulings#8 (the accidentally deleted G00031
  record and its `ANK 20210309-3` reference); nothing needed here when it lands.

Verification and post-update maintenance run through the **rulemonger agent**
(`.claude/agents/rulemonger.md`): it works from the document plus the citable sources;
it reports findings and exact edits rather than editing the document itself, and keeps
its memory under `.claude/references/rulemonger/`.

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
- Rules-change history gist (when a rule changed or was reverted):
  https://gist.githubusercontent.com/lionel-panhaleux/a4a9cad2e492af7c45c50a1cea7e6cf6/raw/92a6f169931c08ea3a4ae62ccbf2d6da17bc8970/VTES%2520History%2520of%2520changes.md

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
  to `https://www.vekn.net/rulebook#anchor`, **double-bracketed so the brackets display**
  (since 2026-07-22), e.g.
  `[^c1]: [[LSJ 20061207]](https://…) [[RBK playing-a-card]](https://www.vekn.net/rulebook#playing-a-card) — group "Cancel" (G00058).`
  Definitions are separated by blank lines — kramdown otherwise lazily absorbs the next
  definition as paragraph content (this silently broke all footnotes once). IDs with no
  URL (phantoms, upstream holes) stay as plain unlinked single-bracket labels — do not
  delete them; the audit that settled them (`phantom-id-audit.md`) is in git history.
- Source lines hard-wrap at 120 columns; rewrap the paragraphs you touch.
- Pure one-card text interpretations stay in the rulings database and do not enter this
  document.
- No reader injunctions ("Read the card…", "Read the wording…"): state the rule
  declaratively (owner, 2026-07-22).
- `⚠ REVIEW` marks a point that still needs judge confirmation.
- For anything deeper, the full style contract is `.claude/references/drafter-contract.md`.

## Domain gotchas already established

- Rulebook actions are **not** subject to the No Repeated Action rule — only card
  name/copy rules are. Sameness matters only for card effects (`{Obedience}`,
  `{Red Herring}`, `{Change of Target}`).
- `rulings.yaml` wording sometimes paraphrases the original ruling — and can even invert
  it (the {Annabelle Triabell} record, caught 2026-07-22). Verify against actual card
  text and, when it matters, the original ruling (VEKN forum posts are fetchable; LSJ
  Google Groups posts often work through WebFetch too — try before giving up).
- **Read the whole thread — Rules Directors correct themselves downthread.** LSJ
  20100604-1's later "My mistake. Neither can be used to enter combat with a non-ready
  minion." supersedes his first "Sure. Card text." answer on {Hidden Lurker}; reading
  only the first answer produced a wrong "inverted paraphrase" claim against the
  database (owner-corrected 2026-07-22).
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
