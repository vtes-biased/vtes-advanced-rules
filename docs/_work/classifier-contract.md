# Classifier contract — Phase 3

The operating contract for the 18 classification agents. Self-contained by design: an
agent working from this file plus `taxonomy.md`, `calibration.md` and its own chunk needs
nothing else. Do not send agents off to read the `vtes` skill or the rulebook — 18 agents
independently choosing what to read is 18 chances to drift.

## What you are doing and why it matters

You classify rulings against the 60 section codes in `taxonomy.md`. The labels are not the
deliverable. They build the per-section extracts that a later agent uses as the raw
material for drafting that section of the document.

So the bar is not "is this label defensible". It is:

> **Will the agent drafting §4.4 receive every ruling it needs to write §4.4?**

Your work splits into **two independent judgments**, and they must not contaminate each
other:

**Judgment 1 — does this ruling belong in the document at all?** Decided ONLY by the C
tests below. It has no default and no thumb on the scale. `C` and absorbed are equally
respectable outcomes, and "I'm not sure" is never a reason to absorb.

**Judgment 2 — given that it belongs, which sections should see it?** Here, and only here,
the errors are asymmetric: a missing code is a silent permanent loss (the drafter never
sees the ruling), an extra code costs a few tokens (the drafter shrugs and moves on). **So
when genuinely torn between two sections, add both.**

⚠ Calibration rounds 1 and 2 both found agents carrying judgment 2's asymmetry into
judgment 1, absorbing marginal rulings because "an extra label is cheap". It is cheap — for
codes. It is not cheap for absorption: every strained absorption pads 60 extracts with
material the drafters must read and discard. Round 1 drove coverage to 92-96% and the C
rate to ~3% on this error alone; the instrument measured the instruction, not the corpus.
**Decide judgment 1 first, in isolation, before you think about codes at all.**

## Golden rules

1. **Classify the ruling as written, not the card as you remember it.** You are labeling
   the text in front of you. Do not reason from recalled card behavior, and do not
   "correct" a ruling that looks wrong — `rulings.yaml` sometimes paraphrases the original,
   and that is not yours to fix. If the wording seems mistaken or self-contradictory, label
   what it says and flag it in the note.
2. **Multi-label is the default posture, not an escape hatch.** Up to 3 codes, most central
   first. Many rulings genuinely teach two sections: a canceled-strike ruling is 1.8 *and*
   4.3; a torpor-rescue vote is 3.7.7 *and* 3.7.5. Forcing one code discards a true signal.
3. **Read for the principle, not the surface.** The failure mode is filing a ruling under
   the section it superficially resembles rather than the one whose principle it teaches. A
   ruling mentioning combat is not automatically chapter 4 — a ruling about *when a combat
   card may be played* is timing (chapter 2).
4. **C must be argued, never defaulted.** See below. C is a verdict you reach, not the box
   you tick when nothing obvious fits.
5. **Identical rulings must get identical labels.** The same ruling text recurs across many
   cards (one wording appears on 10 cards spread over 7 chunks). If a ruling looks generic
   and template-like, label it on its principle — you cannot see the other copies, so
   consistency has to come from reading the text the same way every time.
6. **Never leave a ruling unlabeled.** Every input line produces exactly one output line.

## Output format

One tab-separated line per input ruling, same order as the input:

```
<id><TAB><codes><TAB><role><TAB><note>
```

- **`id`** — `R####`, copied exactly.
- **`codes`** — 1-3 section codes, comma-separated, no spaces, **most central first**
  (`3.5,1.7`). Literal `-` for C, and for G only when no section comes close.
  If a defensible 4th code existed, name it in the note — the cap drops it silently
  otherwise.
- **`role`** — describes the ruling's relation to its *primary* (first) code:
  - `P` — states or directly applies the section's general principle (becomes prose).
  - `E` — a usable example of that principle on a specific card (becomes an "e.g.").
  - `C` — pure one-card text interpretation; teaches nothing general.
  - `G` — teaches something general, but **no section owns it**. Codes column is `-`.
- **`note`** — **required for C and G**. Otherwise optional: use it for a topic hint or a
  flag on wording that looks wrong.

**P vs E is low-stakes — do not agonise.** Coverage counts them together and both land in
the same extract; the label is a hint about intended use, not a judgment. **When torn,
choose E.** A false P can push a drafter into stating an over-broad principle; a false E
just sits unused in the example pool.

Emit nothing but these lines — no preamble, no summary, no markdown fences.

## The C and G rules — the important distinction

When no section fits, you must say **which kind** of not-fitting it is. These look identical
from inside a single ruling and mean opposite things downstream:

- **C** — *"nothing here worth carrying into the document."* Correct and expected: pure
  card interpretations stay in the rulings database by design, and the corpus has a
  substantial natural ceiling of them. **C is a normal outcome, not a failure.**
- **G** — *"there is something general here, but nobody planned a home for it."* The ruling
  teaches a real principle; the taxonomy is short a section.

### Deciding C

The earlier test — *"could a judge state this as a rule without naming the card?"* — was
too weak: almost anything can be phrased generally. `Great Symposium.1` ("search the crypt
for only one Kiasyd, not any number") generalises to "the singular in card text means one",
which is true, general, and useless. Generality is necessary but not sufficient; the
question is **value**. Two tests, either one sufficient to make it C:

1. **Transfer.** Does this ruling change how you would rule on a *different* card? If the
   only situations it affects involve this card, it is C — however generally you can
   phrase it.
2. **Non-obviousness.** Would a judge fluent in the rulebook already know this? If yes, it
   is a reminder restating known rules, not a ruling that teaches. C.

Reaching C by these tests is a *positive finding*. Do not strain to absorb a ruling.

### Deciding G, and G's codes

G means the ruling passes both tests above — it genuinely teaches something transferable
and non-obvious — but no section's scope claims it.

**G may carry codes.** List the nearest partially-owning sections: `1.9` + role `G` reads
"the core is homeless, but 1.9 touches it". Use `-` only when nothing comes close. This
matters: a ruling that is mostly homeless but partly 1.9 material must not have to choose
between hiding the gap and vanishing from 1.9's extract. Both calibration passes hit this
independently and it was their strongest shared objection.

Getting C vs G wrong corrupts the number the project steers by. Both are subtractive, but
only G justifies adding sections. A lazy C hides a real gap; a G used as a synonym for "I'm
not sure" invents gaps that aren't there.

**Every C and every G carries a note.** For C: what the ruling *is* about, and which test it
failed. Not `C  card-specific` — that is the shrug this rule exists to prevent. Write:

```
C   {419 Operation} edge-burn interaction with its own counter mechanism; fails transfer —
    affects no other card. Nearest was 6.5, but that owns the Edge as a resource, not cards
    consuming it
```

**C may also carry codes**, same as G: name the near-miss section rather than burying it in
prose. `6.5` + role `C` reads "excluded, but 6.5 came closest" — which lets a later pass
measure how marginal the exclusions were. Use `-` when nothing came close.

For G: name the missing topic in words that would work as a section title. If you cannot
write either sentence, you have not finished reading the ruling.

## Note-field tags

Three tags may appear at the START of a note. They are greppable, aggregated by later
passes, and each solves a problem the note field otherwise buries in prose.

**`!TENSION:<topic-slug>`** — this ruling appears to pull against another on the same
question. Classify it into its natural section as normal; the tag is *additional*, not a
substitute for a label. The **slug is the co-location key**: you cannot see the other
ruling (it is probably in another agent's chunk), so name the shared topic in a stable
kebab-case phrase and a later pass groups every ruling carrying that slug into one file for
adjudication. Reuse a slug from `calibration.md` if one fits; otherwise coin a clear one.

```
3.2   E   !TENSION:no-effect-plays  may be played where it will have no effect; the
          prohibition cases point the other way
```

Use it when two rulings would make a drafter write contradictory sentences. Do NOT use it
for a ruling you merely found hard.

**`!WORDING`** — the ruling's own text looks mistaken, self-contradictory, or garbled. You
still label it exactly as written (golden rule 1); the tag records the doubt so a later pass
can check it against the card text and the original ruling.

**`!DROPPED:<code>`** — a 4th (or 5th) code was defensible but the 3-code cap forced it out.
Without the tag the cap discards it silently.

Tags may combine: `!TENSION:no-effect-plays !DROPPED:1.8 …prose…`

## General rule entries

Some ids carry `G000xx|<name>` instead of a card id — these are *general rule entries*, not
card rulings (`G00058|Cancel`, `G00061|Cancel an action`, `G00064|Special Hunt Action`).
They state rules directly, with no card doing the work. They are **almost always `P`, and
essentially never `C`**: a general entry that failed the transfer test would not exist. They
belong in the corpus and are prime prose material.

Watch for duplicates: the same wording often appears both on a card and on its general
entry. Label both identically — the general entry as `P`, the card copy usually as `E`.

## Scope note

Sections **1.8** (playing/canceling) and **3.5** (NRA/canceled actions) are already
written. Keep classifying into them normally — their extracts are used to verify the pass,
and calibration answers are drawn from them.

## Do not

- Do not read other files (the vtes skill, the rulebook, the rulings database). You are
  self-contained; 18 agents choosing their own reading is 18 sources of drift.
- Do not "fix" a ruling whose wording looks wrong. Label what it says, flag it in the note.
- Do not leave any input line without an output line.
- Do not strain to absorb. C is a normal, expected outcome.
