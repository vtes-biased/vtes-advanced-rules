# Phase 5 runbook — per-section extracts

Self-sufficient. From a cold start read `WORKING-NOTES.md` first (mandate + pipeline
state), then this file. You do not need anything else.

## What this phase does

Turns `classification.tsv` (2,605 labelled rulings) into one **drafting brief per section**
at `docs/_work/extracts/<code>.md`. Phase 6 gives one agent one extract and asks for prose,
so an extract must be everything that agent needs and nothing it must go looking for.

**This phase is MECHANICAL — a script, not a fan-out.** Every input already exists. Do not
spend agent tokens assembling files. The judgment was spent at Phase 4.5/4.6; Phase 5 only
routes it to where the drafter will see it.

## Preconditions

```sh
cd /Users/lpanhaleux/Developer/vtes-advanced-rules/docs/_work
wc -l classification.tsv                 # 2605
cut -f1 classification.tsv | sort | uniq -d | wc -l   # 0 = no dupe ids
ls review-findings.json tensions.md taxonomy.md coverage.tsv
awk -F'\t' '{r[$3]++} END{for(k in r) print k, r[k]}' classification.tsv
# expect: P 1074, E 1299, C 227, G 5
```

64 live codes. **6.8 was deleted at Phase 4.6 and 6.9 was deliberately not renumbered** —
chapter 6 skips 8. Do not "fix" this.

## The extract format

One file per code, `docs/_work/extracts/<code>.md`:

```markdown
# <code> — <the scope line verbatim from taxonomy.md>

Membership: <N> rulings (P <p>, E <e>). Generated from classification.tsv.
Footnote label prefix for this section: [^<code-with-dashes>-N]  (eg. 4.4 -> [^4-4-1])

## Drafting constraints
- Judge-level terse prose, mechanics-first. Full fluency with the base rules is assumed.
- NO exhaustive card lists. Tie the rule to its wording template, then "e.g." + 1-3 cards.
- Be synthetic: cross-reference other sections rather than repeating.
- Card names in braces {Abbot}; disciplines/types in brackets [pot], [POT], [ACTION].
- Every derived statement carries a footnote in a `#### References` block at section end.
- Pure one-card interpretations do NOT enter the document.
- `⚠ REVIEW` marks a point still needing judge confirmation.

## Reviewer notes (Phase 4.5) — READ BEFORE DRAFTING
<every finding from review-findings.json whose unit == this code, each as:
 ### [severity] type
 summary
 **Recommendation:** recommendation
 *Rulings:* ids>

> CALIBRATION CAVEAT. The Phase 4.5 pass produced to a quota: all 68 units returned the
> same middle verdict and none returned zero findings. Volume is inflated and **severity
> labels carry no signal — do not triage by them.** Content was spot-verified as largely
> sound. Treat these as leads to check, not instructions to obey. In particular the
> `duplicate-template` findings are the most valuable thing in this file: they are the one
> defect class no classifier could see, and they are what keeps the section from becoming
> a card list.

## Tensions touching this section
<any block from tensions.md whose ruling ids intersect this section's membership,
 including the RESOLVED ones — a resolved tension is a stated principle, draft it>

## Rulings — PRINCIPLE candidates (P)
| id | card | ruling text |

## Rulings — EXAMPLE candidates (E)
| id | card | ruling text |
```

Ruling text comes from `rulings-flat.tsv` field 3, card from field 2. Keep the `[REF ID]`
tags in the text — the drafter needs them to build footnotes.

## Things that MUST ride along or they are lost

These are decisions already taken that live nowhere in the data. If the script does not
route them, no drafter will reinvent them.

1. **The 3.7.4 seam.** Phase 4.6 split 3.7.4's scope line but deliberately did NOT
   reclassify its 45 rulings. So the data still shows one undifferentiated pile while the
   taxonomy says it is three topics. The 3.7.4 extract must carry the seam explicitly:
   - Cluster A — "may still USE abilities the turn recruited" — is **1.5's principle**, not
     3.7.4's. Nine rulings share `[ANK 20180517]` verbatim.
   - Cluster B — "may an entering minion ACT that turn" — is **5.5/5.6's**.
   - Cluster C — a card effect putting an ally/retainer into play is **not** an
     employ/recruit action, so action-keyed effects do not attach. This is 3.7.4's largest
     and most general topic and its scope line never used to name it.
   - Cluster D — the employ/recruit action itself.
   The full cluster membership is in the 3.7.4 finding in `review-findings.json`.
2. **`no-effect-plays` is three questions, not one** (Phase 4.5 Q5). Do not let a drafter
   meet one polarity and state an over-broad rule. Split before drafting; see tensions.md.
3. **The resolved mandatory-action principle** (tensions.md, RESOLVED section). Adjudicated
   by the owner, not a `⚠ REVIEW`: whether another action of a type discharges a mandatory
   obligation depends on whether the mandating effect PROVIDES the action or merely
   REQUIRES one of that type. Belongs in 3.9's prose.
4. **1.8 and 3.5 are ALREADY DRAFTED AND REVIEWED** in `docs/extended-rules.md`. Generate
   their extracts for reference but mark them **DO NOT DRAFT — style exemplars only**.

## Validation

```sh
cd /Users/lpanhaleux/Developer/vtes-advanced-rules/docs/_work
ls extracts/*.md | wc -l                      # 64
# every P/E ruling reaches at least one extract
grep -ho '^| R[0-9]\{4\}' extracts/*.md | tr -d '| ' | sort -u > /tmp/in-extracts.txt
awk -F'\t' '$3=="P"||$3=="E"{print $1}' classification.tsv | sort -u > /tmp/should.txt
diff /tmp/in-extracts.txt /tmp/should.txt && echo "all P/E rulings routed"
# no extract is empty, and the big ones are not truncated
wc -l extracts/*.md | sort -n | head -3
# every section with Phase 4.5 findings actually carries them
python3 -c "
import json,os
f=json.load(open('review-findings.json'))
units={x['unit'] for x in f if x['unit']!='structural'}
missing=[u for u in units if os.path.exists(f'extracts/{u}.md')
         and 'Reviewer notes' not in open(f'extracts/{u}.md').read()]
print('sections missing reviewer notes:', missing or 'none')"
```

**awk gotcha, it has bitten twice:** `awk -v C="3.10"` makes a strnum that compares equal to
`"3.1"`. Match codes via array subscripts (always string keys) or force string context.
Same trap for `3.7.x` vs `3.7`.

## Then

- **Phase 6** — drafting, one agent per extract → `docs/_work/sections/<code>.md`. That IS
  a fan-out and it is where the model choice matters. 62 sections to draft (64 minus the
  two pilots).
- Footnote labels must be unique document-wide. The pilots used `^c1..c19` and `^n1..n21`;
  every new section uses its own `[^<code>-N]` prefix, which is why the extract states it.
