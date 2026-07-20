# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## What this repository is

A **writing project**, not a software project: it produces `docs/extended-rules.md`, a
judge-level companion to the [VTES rulebook](https://www.vekn.net/rulebook) that
synthesizes ~2,605 individual rulings into general principles organized by game mechanic.
There is no build, no test suite, no package. The deliverable is one Markdown file.

Classification is complete: all 2,605 rulings are labelled against the taxonomy
(`docs/_work/classification.tsv`). Drafting has not started beyond the two pilot sections.

## Working files and pipeline

`docs/_work/` holds the machinery for producing the document; it is scaffolding, not
output.

**It is tracked deliberately and is meant to be deleted.** Everything under `_work/` is
in-flight tooling — kept in git only so mid-pipeline state survives across iterations
(the Phase 3 classification output in particular is thousands of agent judgments that
cost real work to reproduce). When the document is finished, remove `docs/_work/`
wholesale in a cleanup commit. Do not treat its presence as a sign it should be
maintained, and do not let it accumulate anything the final document depends on.

- `WORKING-NOTES.md` — **read this first.** It is compaction insurance: the mandate,
  the validated style constraints, and a phase-by-phase pipeline checklist with current
  state. Update the phase checkboxes as work completes.
- `classification.tsv` — **the canonical output of the classification pipeline and the
  input to every later phase.** 2,605 rows, `id<TAB>codes<TAB>P|E|C|G<TAB>note`, one per
  ruling. Read THIS, not `class/chunk-*.tsv`, which is the superseded per-agent record.
- `taxonomy.md` — the **64 live** section codes (`1.1` … `6.9`; chapter 6 skips 8, which
  was deleted and deliberately not renumbered) every ruling is classified against, plus
  the P/E/C/G role definitions (Principle / Example / not-worth-carrying /
  Gap-with-no-owning-section). **Authoritative for the code list**, and it records why
  each added code was added and which candidates were rejected — read it before
  proposing a new section.
- `review-findings.md` / `.json` — the Phase 4.5 per-section review: 525 findings from 68
  opus reviewers. **Carries a calibration caveat that must be read before use** — the pass
  produced to a quota, so volume is inflated and severity labels carry no signal. The
  `duplicate-template` findings are its real value: 60% of the corpus is template
  redundancy, which is the single biggest determinant of the finished document's length.
- `phase3-runbook.md`, `phase5-runbook.md` — self-sufficient runbooks for the two phases
  that are easy to get wrong from a cold start.
- `coverage.tsv` — per-section membership (P / E / P+E / G-nearest), regenerated from
  `classification.tsv`. Coverage is DIAGNOSTIC, not a target; see the mandate.
- `tensions.md` — contradictory-polarity rulings grouped by `!TENSION` slug. A drafter
  who meets only one side of a pair will state an over-broad rule, so resolve each slug
  as a unit before drafting the owning section. The `no-effect-plays` slug is large (46).
- `rulings-flat.tsv` — all rulings flattened, one per line:
  `R####<TAB><card_id>|<Card Name>.<n><TAB>ruling text with [REF IDs]`.
- `chunk-00` … `chunk-17`, `class/chunk-NN.tsv` — the Phase 3 inputs and their raw
  per-agent output. Kept as the immutable record of what each agent judged; **stale for
  the 275 rulings the Phase 4b recheck revised.** `recheck-NN` / `reclass/recheck-NN.tsv`
  are that recheck's input and output (output carries two extra fields, `KEEP|CHANGE`
  and a reason).
- `classifier-contract.md` — the operating contract for the classification agents: the
  two independent judgments (absorb-or-not, then which sections), golden rules, output
  format, the C/G tests, and the note-field tags. Agents are self-contained (contract +
  taxonomy + calibration + own chunk, nothing else).
- `phase3-runbook.md` — **how to run the 18-way production classification.** Written to
  be self-sufficient from a cold start: preconditions, the verbatim agent prompt, model
  choice, validation commands, and the known trouble spots.
- `calib-sample.tsv`, `calib-run-{A,B,A2,B2}.tsv`, `compare-runs.py` — the calibration
  evidence. Two rounds of two independent opus passes over the same 111 rulings, graded
  against each other; `compare-runs.py` reports the agreement metrics.
- `calibration.md` — worked examples anchoring the pass, seeded from the drafted
  sections 1.8 and 3.5 where the correct labels are already fixed by their footnotes.
  Maintained by *promotion*: generalizable corrections move up into "General lessons",
  case verdicts stay thin.

Later phases write `docs/_work/extracts/<sec>.md` and `docs/_work/sections/<sec>.md`
before assembly into `docs/extended-rules.md`.

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
pull` (then commit the new pointer here) when rulings need refreshing.
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
  full fluency with the base rules is assumed.
- **No exhaustive card lists.** Tie a rule to its wording template, then give "e.g." plus
  one to three cards.
- Be synthetic: cross-reference other sections rather than repeating, and merge redundant
  subsections.
- Card names in braces `{Abbot}`; disciplines and card types in brackets `[pot]`, `[POT]`,
  `[ACTION]`.
- Every derived statement carries a footnote. Footnotes live in a `#### References` block
  at the end of each section and list the ruling reference IDs plus the card or group the
  ruling is recorded under, e.g.
  `[^c1]: [LSJ 20061207] [RBK playing-a-card] — group "Cancel" (G00058).`
  Footnote labels must be **unique document-wide**: the pilot sections used `^c1..c19` and
  `^n1..n21`; new sections use section-prefixed labels like `[^4-4-1]`.
- Pure one-card text interpretations stay in the rulings database and do not enter this
  document.
- `⚠ REVIEW` marks a point that still needs judge confirmation.

**Sections 1.8 (playing/canceling) and 3.5 (NRA/canceled actions) are drafted and
reviewed.** Use them as style exemplars; do not rewrite them (light edits only if a
review pass demands it). Everything else is an HTML-comment stub sketching intended
content.

## Domain gotchas already established

- Rulebook actions are **not** subject to the No Repeated Action rule — only card
  name/copy rules are. Sameness matters only for card effects (`{Obedience}`,
  `{Red Herring}`, `{Change of Target}`).
- `rulings.yaml` wording sometimes paraphrases the original ruling. Verify against actual
  card text and, when it matters, the original ruling (VEKN forum posts are fetchable;
  LSJ Google Groups archives are not practical).

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
