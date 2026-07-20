# Phase 3 runbook — the 18-way production classification

Self-sufficient. If you are picking this up in a fresh context, read `WORKING-NOTES.md`
first (mandate + pipeline state), then this file. You do not need anything else.

## What this phase does

Classifies all 2,605 rulings against the 61 section codes, producing the per-section
extracts that Phase 5/6 drafting is built from. 18 agents, one per chunk, ~145 rulings each.

## Preconditions (verify before launching)

```sh
cd /Users/lpanhaleux/Developer/vtes-advanced-rules/docs/_work
ls chunk-??            # 18 files, chunk-00 … chunk-17
ls class/              # must exist; must be EMPTY (else you are re-running — see below)
wc -l chunk-* | tail -1   # 2605 total
diff <(cat chunk-*) rulings-flat.tsv && echo "chunks are an exact partition"
```

The four input files every agent reads — `classifier-contract.md`, `taxonomy.md`,
`calibration.md`, and its own `chunk-NN` — must be unchanged from the calibrated versions.
**If you edit any of them, the calibration no longer describes the instrument.** Small
fixes are fine; anything touching the C tests, the two-judgments framing, or the role
definitions means re-running calibration (see `calibration.md` → Grading history for how).

## Model and orchestration

- **Sonnet** for all 18 (volume work; opus is reserved for calibration and Phase 4.5 review).
- 18 concurrent agents is a multi-agent fan-out. The `Workflow` tool is the natural vehicle
  but **requires the user's explicit opt-in** ("use a workflow" / "ultracode"). Without
  that, use the `Agent` tool directly — several per message, they run concurrently.
- Cost estimate: ~20-30k tokens per agent, **~400-500k total**.

## The agent prompt (use verbatim, substituting NN)

> You are a classification agent for the VTES Extended Rules project. Work in the repo at
> /Users/lpanhaleux/Developer/vtes-advanced-rules.
>
> Read these four files, in this order, before doing anything:
> 1. docs/_work/classifier-contract.md — your operating contract. Follow it exactly.
> 2. docs/_work/taxonomy.md — the section codes and role definitions.
> 3. docs/_work/calibration.md — worked examples showing the expected standard.
> 4. docs/_work/chunk-NN — your input: ~145 rulings, one per line.
>
> Classify EVERY line of chunk-NN according to the contract. Write your output to:
> docs/_work/class/chunk-NN.tsv
>
> Output format, one tab-separated line per input ruling, same order as input:
> `<id><TAB><codes><TAB><role><TAB><note>`
>
> Emphasis (all detailed in the contract — this does not replace reading it):
> - Two INDEPENDENT judgments. First: does this ruling belong in the document at all?
>   Decided only by the C tests, no default, no thumb on the scale. Second, and only then:
>   which sections should see it — there, when torn between sections, add both codes.
> - C is a normal, expected outcome. Do not strain to absorb.
> - G means genuinely general but homeless; G and C may both carry codes (nearest section).
> - C and G both require a note.
> - Note-field tags where they apply: `!TENSION:<slug>`, `!WORDING`, `!DROPPED:<code>`.
> - Every input line produces exactly one output line.
>
> Do NOT read any other files. Do not consult the vtes skill, the rulebook, or the rulings
> database — you are deliberately self-contained. Classify the ruling text as written.
>
> After writing the file, return a SHORT report (not the classifications): counts of
> P/E/C/G, how many multi-labelled, any taxonomy gaps you marked G and whether they
> cluster, any `!TENSION` slugs you coined, and anything in the contract or calibration
> file that was ambiguous or unhelpful.

## Validation (run after all 18 return)

```sh
cd /Users/lpanhaleux/Developer/vtes-advanced-rules/docs/_work
# every chunk produced a file, with the right number of lines
for n in $(seq -w 0 17); do
  want=$(wc -l < chunk-$n); got=$(wc -l < class/chunk-$n.tsv 2>/dev/null || echo 0)
  [ "$want" = "$got" ] || echo "MISMATCH chunk-$n: want $want got $got"
done
# ids present, in order, no dupes, none lost
diff <(cat class/chunk-*.tsv | cut -f1 | sort) <(cut -f1 rulings-flat.tsv | sort) \
  && echo "all 2605 ids accounted for"
# field count must be 4 everywhere
cat class/chunk-*.tsv | awk -F'\t' 'NF!=4 {print FILENAME" line "NR": "NF" fields"}'
# every C and G carries a note
cat class/chunk-*.tsv | awk -F'\t' '($3=="C"||$3=="G") && length($4)<15 {print "thin note: "$0}'
# codes must all exist in the taxonomy
cat class/chunk-*.tsv | cut -f2 | tr ',' '\n' | grep -v '^-$' | sort -u \
  | while read c; do grep -q "^- $c " taxonomy.md || echo "UNKNOWN CODE: $c"; done
```

A failed chunk is cheap to redo — relaunch that one agent with the same prompt. Do not
hand-patch output files; the point is that the labels are the agents' judgments.

## Then

- **Phase 4** — aggregate to `coverage.tsv`. Report P+E / C / G **separately**. Coverage is
  diagnostic, NOT a target (see the amended mandate in `WORKING-NOTES.md`). The G pile is
  the only evidence that justifies adding sections; a clustered G pile means expand there, a
  near-empty one with low coverage means the corpus's true ceiling — do nothing.
- **Collect `!TENSION` slugs** into `tensions.md`, grouped by slug, for a cross-section
  adjudication pass. These are contradictory-polarity rulings that must be resolved together
  or a drafter meeting only one will state an over-broad rule.
- **Phase 4.5** — per-SECTION review (opus), never per-chunk. Cross-chunk drift and
  per-section completeness are invisible on the chunk axis: one boilerplate wording recurs on
  10 cards across 7 chunks. This pass is also the safety net for over-absorption, which no
  classifier can see from inside its own 145 lines.

## Watch list — expected trouble, do not treat as surprises

- **C rate.** If it comes back ~5% with ~90% coverage, the untested round-3 fix did not
  work. That is a finding about the instrument, not about the corpus, and it must NOT
  trigger taxonomy expansion.
- **Candidate gaps on the watch list** (`taxonomy.md`): cumulative/stacking effects, sect as
  a trait, minion-phase action ordering, card-conferred status when-played vs in-play. Each
  has 1-2 confirmations from calibration. Phase 4 counts decide them; do not pre-empt.
- **3.7.4 is overloaded** — its scope line mixes the employ/recruit actions with "acting the
  turn recruited". Expect a pile-up; candidate for a scope-line split, not a new code.
