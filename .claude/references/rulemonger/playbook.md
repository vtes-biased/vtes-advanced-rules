# Rulemonger playbook

The mechanical craft: where every source lives, how to look things up, and how to
verify a claim end-to-end. Static reference — lived experience goes in
`resolutions.md`, not here.

## Source map

| Source | Location | Role |
|---|---|---|
| Advanced rules (the document) | `docs/advanced-rules.md` | Under review. ~4,800 lines, 6 chapters, 2 appendices (appendices still TODO). |
| 2024 rulebook, verbatim | `rulebook2024/content.md` | The citable base rules. Headings carry `vekn.net/rulebook` anchors. |
| Rulings database | `vtes-rulings/rulings/rulings.yaml` | ~2,605 curated rulings. May paraphrase originals. |
| Reference URLs | `vtes-rulings/rulings/references.yaml` | Ruling reference ID → original URL. |
| Card groups | `vtes-rulings/rulings/groups.yaml` | Group ID (`G#####|Name`) → member cards, with per-card symbol annotations. |
| Card text | `curl -s "https://api.krcg.org/card/<id-or-name>"` | JSON; the text is under key `card_text`. URL-encode names. |
| Rulings canon | `.claude/references/rulemonger/canon.md` | Verbatim cache of the document's most-cited rulings (discipline in its header). Check its index when a question touches a listed ID. |
| VTES skill digests | `~/.claude/skills/vtes/references/` | Locators only (golden rule 1). `vtes-rules.md` (rules digest), `judges-guide-v2.md` (tournament conduct & infractions — mostly out of scope), `tournament-rules.md`, `game_terms.json`. |

Both source repos are git submodules pinned to a commit. If they look empty:
`git submodule update --init`. A submodule bump changes the ground truth under the
document — after one, the maintenance sweep (below) is due.

## Data formats

**`rulings.yaml`** — top-level keys `<card_id>|<Card Name>:` (VEKN CSV ids) or
`G#####|<Group name>:`, each holding a list of ruling strings. Every ruling ends with
one or more reference IDs in brackets. Disciplines/types appear as `[pot]`/`[POT]`/
`[ACTION]`, card names as `{Abbot}`:

```yaml
100006|Abbot:
  - The +1 intercept applies to actions directed at cards controlled by the
    controller. It does not apply to actions directed at other Methuselahs. [LSJ 20061222]
```

**`references.yaml`** — one line per reference: `LSJ 20061207: https://groups.google.com/...`.
ID grammar: `<SOURCE> <YYYYMMDD>[-n]` where the suffix disambiguates same-day rulings.
Sources are successive Rules Directors and institutions: `TOM`, `SFC`, `JON`, `LSJ`,
`PIB`, `ANK`, plus `RTR` (Rules Team Ruling) and `RBK` (rulebook).

**`groups.yaml`** — `G#####|<name>:` then `card_id|Card Name: '<symbols>'` members.

## Lookup recipes

```sh
# A card's rulings block (anchor on the pipe and colon to avoid substring hits):
grep -n -A20 '|Abbot:' vtes-rulings/rulings/rulings.yaml

# Every ruling citing a reference ID, and its URL:
grep -n 'LSJ 20061207' vtes-rulings/rulings/rulings.yaml vtes-rulings/rulings/references.yaml

# A group's membership:
grep -n -A30 'G00058|' vtes-rulings/rulings/groups.yaml

# Card text (never trust memory — fetch):
curl -s "https://api.krcg.org/card/Abbot" | python3 -c 'import json,sys; print(json.load(sys.stdin)["card_text"])'

# Rulebook passage for [RBK playing-a-card]: anchors are kebab-case headings.
grep -n -i 'Playing a Card' rulebook2024/content.md
```

Grep-first is usually enough; for structured queries over the YAML, create a venv with
`pyyaml` (`python3 -m venv .venv && .venv/bin/pip install pyyaml`) — there is no
standing one.

## The document's footnote grammar

Every derived statement carries a footnote. Footnotes live in a `#### References`
block at the end of each section:

```
[^1-1-5]: [PIB 20150418] [ANK 20210309-3] — {Third Tradition: Progeny}, group "Master on vampire who can use it" (G00031).
```

- Label: section-prefixed and unique document-wide (`[^1-1-5]`, `[^3-7-2-5]`). The two
  pilot sections (1.8 and 3.5) predate the convention and use `[^c1..c19]`, `[^n1..n21]`.
- Before the em-dash: the reference IDs, `[RBK <anchor>]` included.
- After the em-dash: the record keys — the cards `{...}` and/or groups `"..." (G#####)`
  under which the cited rulings are filed in `rulings.yaml`. This is the lookup path.

## Verifying a footnoted statement (the core procedure)

1. Read the sentence carrying the footnote mark; state to yourself exactly what it claims.
2. Parse the footnote: reference IDs + record keys.
3. For each record key, open its block in `rulings.yaml` and find the ruling(s) ending
   in the cited reference IDs. A cited ID absent from the cited record is a
   `wrong-citation` finding.
4. Check support, not topicality: does the ruling text actually establish the sentence
   — its full breadth, including words like "any", "always", "only"? A ruling about one
   card supports a general statement only if the sentence ties it to a wording template
   the ruling exemplifies. Breadth beyond the rulings is an `over-broad` finding.
5. For `[RBK <anchor>]`: find the heading in `rulebook2024/content.md` (kebab-case
   anchor ↔ heading text) and read the verbatim passage.
6. If exact wording is load-bearing and `rulings.yaml` may be paraphrasing: resolve the
   ID in `references.yaml` and fetch the original. `vekn.net/forum` URLs fetch fine, and
   `groups.google.com` archives usually do too (2026-07-22 calibration: 30+ successes in
   one session). Fallbacks: the VEKN rules archive
   (`https://www.vekn.net/history-of-vtes-rules`) hosts the RTR compilations; narkive
   mirrors the usenet groups. Only after those fail, record "unverifiable at source;
   database wording relied on" instead of guessing.
7. If the sentence makes a card-text claim, fetch the card from KRCG and compare.

## Document conventions and style (settled owner decisions — regressions if violated)

- Mechanics-first structure, judge-level terse prose. Precision over accessibility;
  full fluency with the base rules is assumed.
- **No exhaustive card lists.** Tie a rule to its wording template; then "e.g." plus
  one to three cards.
- Synthetic: cross-reference other sections rather than repeat; merged subsections
  over redundant ones.
- Card names in braces `{Abbot}`; disciplines and card types in brackets `[pot]`,
  `[POT]`, `[ACTION]`.
- Every derived statement footnoted (grammar above); labels unique document-wide.
- Pure one-card text interpretations stay in the rulings database — they do not enter
  the document. (Their absence is not a `gap`.)
- `⚠ REVIEW` marks a point awaiting judge confirmation — six exist as of 2026-07-20.
- Sections 1.8 and 3.5 are the drafted-and-reviewed style exemplars: judge deviations
  from their register, not from taste.

## Domain gotchas (established; do not re-derive)

- Rulebook actions are **not** subject to the No Repeated Action rule — only card
  name/copy rules are. Sameness matters only for card effects ({Obedience},
  {Red Herring}, {Change of Target}).
- Chapter 6 skips section 6.8 (deleted, deliberately not renumbered). Not a defect.
- `rulings.yaml` wording can paraphrase the original ruling (see step 6 above).

## Shell gotchas

- **awk strnum trap:** `awk -v C="3.10"` compares numerically equal to `"3.1"`, so a
  naive `a[i]==C` folds section 3.1 into 3.10 (this produced a wrong count once).
  Match section codes as array subscripts (always string keys) or force string
  context: `a[i] "" == C ""`. Same trap for any `x.y` vs `x.y0` pair.
- **`join` shifts columns** (`1=key`, then file1's fields, then file2's). Print one
  joined row and count fields before trusting any check built on it.

## Sweep types

- **Footnote verification** — the core procedure over a chapter's References blocks.
  Most objective pass; parallelizes by chapter.
- **Consistency** — cross-section: contradictions, terminology drift, over-broad
  statements, redundancy that should be a cross-reference.
- **Review markers** — the open `⚠ REVIEW` points: gather every source bearing on the
  question, lay out the tension, propose a resolution for the owner to adjudicate.
- **Maintenance** (after a submodule bump) — diff `rulings.yaml` between the old and
  new pin; map changed/added/removed rulings to sections by searching the document's
  footnotes for their reference IDs and record keys; report affected sections as
  `stale` findings. Re-check `canon.md` entries whose IDs appear in the diff and
  update their Status lines.
