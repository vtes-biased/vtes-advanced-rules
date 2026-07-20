# Classification calibration — worked examples

Structure borrowed from the `strategist` agent's calibration corpus
(`codex-of-the-damned/.claude/references/strategist/calibration.md`): **general lessons**
are the operating heuristics, **worked examples** are thin anchors. When a grading round
turns up a generalizable correction, promote it into the lessons and leave only the
specific verdict below. The file thickens at the top and stays short at the bottom.

Seed answers are drawn from sections **1.8** and **3.5**, which are drafted and reviewed —
their footnotes fix the correct label for the rulings they cite. Everything below with a
`[cited]` marker is a known answer, not a guess.

## General lessons

**Read for the principle, not the vocabulary.** The section a ruling *mentions* and the
section it *teaches* are often different. `Heidelberg Castle.3` ("cannot be used before
damage inflicted after action resolution: this is still during the action") names damage
and combat, but what it teaches is when the action window closes — chapter 2 timing, with
4.4 secondary at most.

**Template rulings recur; label the template.** One wording — "Cannot be used if the
vampire cannot attempt to block the action (eg. {Daring the Dawn})" — appears on at least
10 cards spread across 7 chunks (`{Black Sunrise}`, `{Coterie Tactics}`, `{Eluding the
Arms of Morpheus}`, `{Eternal Vigilance}`, `{Guard Duty}`, …). No classifier sees more than
a few. Consistency comes from reading the *template* the same way every time, not from
comparing copies. When a ruling reads like boilerplate, ask what the boilerplate is about
and label that.

**The P/E line is about generality of the statement, not of the card.** `{Champion}`'s "the
action fails but was not blocked; cards depending on a block cannot be played" is a
card-specific ruling that *states* the general rule for the "fails" template — that is P,
even though it lives on one card. Reserve E for rulings that only make sense once you
already know the principle.

**Cost, lock and payment ride along with other sections.** A ruling about what happens to a
cost when something is canceled belongs to 1.7 *and* to whatever did the canceling. These
are the most commonly under-labeled rulings in the corpus.

**"Even if / except / unless" clauses usually mark a second section.** They are where a
ruling reaches past its home section into another mechanic. `.44 Magnum`'s "even if the
bearer changes" is what makes it a 4.10 ruling and not only a 1.2 one.

## Worked examples

### Multi-label

**R0001** `.44 Magnum.1` — "Provides only one maneuver each combat, even if the bearer
changes."
→ `1.2,4.10` `P`
The canonical multi-label case. 1.2 owns the "each combat" periodicity template; 4.10 owns
"each combat" *on equipment*, which is exactly what the bearer-change clause tests. Either
label alone loses half the ruling. Taxonomy names the template in both sections — when two
codes both claim a ruling in their own scope line, that is not ambiguity to resolve, it is
two labels.

**R0449** `Daring the Dawn.2` — "The damage is applied if the action reaches resolution,
even if it ends before combat (eg. {Mirror Walk}, {Change of Target}, {Red Herring}) or has
no effect (eg. because cost cannot be paid)."
→ `3.5,3.4` `P` [cited — 3.5.1]
Teaches two principles at once: *reaching resolution* (3.5.1) and *successful vs. having an
effect* (3.4). The "or has no effect" clause is the tell.

**R0589** `Enkil Cog.1` — "If locked to take an action and the action is canceled as it is
played (not if it is canceled after…), it stays locked and the minion can choose to take an
action again or let the Cog effect be lost."
→ `3.5,1.7` `E` [cited — 3.5.4]
3.5 primary (canceled actions), 1.7 secondary: the point is a cost locked into *another*
effect is not refunded. A classifier labeling this 3.5 alone strips it from the costs
extract, where it is load-bearing. 5.2 (lock/unlock) is defensible as a third — locking
here is a cost, not a state change, so it is the weakest of the three.

**R0299** `Chain of Command.2` — "If a commanded vampire is burned (eg. {Daring the Dawn}),
he is not brought back to the crypt."
→ `6.2,5.4` `E`
Temporary control (6.2) meeting minion burning (5.4). Neither section alone would surface
it.

### Single-label

**R0450** `Daring the Dawn.3` — "The damage is not applied if the action is canceled before
resolution (eg. {Tangle Atropos' Hand}, {The Kiss of Ra})."
→ `3.5` `E` [cited — 3.5.4]
Sibling of R0449 but genuinely single: it illustrates only the canceled-action principle.
Note the pair — adjacent rulings on one card can differ in label count. Do not carry a
label across lines out of momentum.

**R0313** `Champion.4` — "[REACTION] The action fails but was not blocked. Cards depending
on a block (eg. {Mirror Image}, {Freak Drive}) cannot be played."
→ `3.5` `E` [cited — 3.5.1]
Arguably P (it states the "fails" template's consequence), but §3.5.1 uses `{Champion}` in
its `e.g.` list. Both defensible, neither moves a number: default E, move on.

### The announcement template

**R1287** `Pandora's Whisper.1` — "The card to retrieve must be announced when declaring
the action."
→ `3.1,1.14` `E`
The corpus's second high-frequency template (`{Carlotta Giovanni}`, `{Sudario Refraction}`,
`{Jack of Both Sides}`, ~4 in 111). 3.1 owns what is fixed at announcement; 1.14 owns cards
announced from hand for later. **Both codes, in that order, every time** — round 1 left this
unanchored and the two passes were free to split it three ways.

Note the variant: `{Jack of Both Sides}.2` adds "but is not discarded if the action fails …
must be in hand before replacement" — that extra clause earns a third code (1.9), but the
announcement half stays labelled the same way.

**R0156** `Black Sunrise.2` — "[QUI] Cannot be used if the vampire cannot attempt to block
the action (eg. {Daring the Dawn})."
→ `3.3` `E`
The template case. Nine or more near-identical siblings exist in other chunks; every one
must land on 3.3. It is about when a block attempt is impossible — blocking (3.3), not
stealth/intercept (3.2) and not lock/unlock (5.2), even on cards whose own effect is
unlocking. **Label the ruling, not the card it sits on.**

**R0003** `Aaron's Feeding Razor.1` — "The effect is not optional."
→ `1.1` `P`
Short rulings can still be P. Mandatory-vs-optional is 1.1's named scope, and §1.1's stub
already cites this exact ruling.

### C — argued, with the note that makes it legitimate

**R0002** `419 Operation.1` — "You can burn the edge to burn the card if it has no counter."
→ `-` `C` `mechanics of this card's own counter/edge interaction; no section principle —
not 6.5, which is about the Edge as a resource, not cards that consume it`
Note the shape: says what it *is* about, and names the section it might have gone to and
why it did not. That second half is what separates an argued C from a shrug.

**Anti-example — what a rejected C looks like:**
`R0002  -  C  card-specific` — this is the failure this rule exists to prevent. It records
no reasoning, cannot be audited, and is indistinguishable from having skipped the ruling.

### C at the thin end — general but worthless

**R0793** `Great Symposium.1` — "Search the crypt for only one Kiasyd, not any number."
→ `-` `C` `reads the singular in this card's own search clause. Generalises only to "the
singular means one", which fails non-obviousness — any judge knows it. No transfer beyond
this card's search`
**This is the case round 1 got wrong**, and the reason the C test changed. It *can* be
phrased as a general rule, so the old "statable without naming the card?" test absorbed it.
Both new tests reject it: it changes no other card's ruling (transfer), and it tells a
fluent judge nothing (non-obviousness). Generality is necessary, not sufficient.

### G — a real principle with no section to hold it

**R0143** `Betrayer.3` — "Is cumulative; multiple Betrayers each turn."
→ `1.2` `G` `cumulative/stacking effects: nothing owns "multiple instances of an effect
stack". 1.2 owns periodicity templates and is nearest, but does not claim stacking`
**Note the codes on a G.** This is usable 1.2 material *and* gap evidence; the codes column
keeps it in 1.2's extract while the role records the gap. A bare `-` would force a choice
between hiding the gap and losing the ruling — the failure both round-1 passes objected to.
Use `-` only when nothing comes close.

**A closed gap is not a gap.** `Dreams of the Sphinx.3` ("cards that are not replaced count
against the hand size") was round 1's flagship G and the evidence that created **6.9**. Now
that 6.9 exists and its scope line names "what counts against hand size", that ruling is
`6.9,1.9` `P` — not G. When a gap closes, its rulings become ordinary members of the new
section. Check the taxonomy before flagging G; it grows.

Contrast `Elder Library.1` ("if there is another copy in play, it enters contest without
modifying the hand size") — same vocabulary as 6.9, but the content is contesting (1.13),
which *does* have a home. **Shared vocabulary is not a shared gap.** Both passes in both
rounds got this right unprompted; it is the control proving 6.9 is not a grep artifact.

### Tension — rulings that pull against each other

**R0533** `Draba.3` — "Can be played on a minion with no or negative stealth, in which case
it has no effect."
→ `3.2` `E` `!TENSION:no-effect-plays  playable although it will do nothing; the
prohibition cases point the other way`

**R0195** `Blood Fury.6` — the opponent "cannot play prevention cards (eg. for cycling)."
→ `1.1` `E` `!TENSION:no-effect-plays  a prohibition bars playing even for zero effect —
the inverse of the Draba case`

Same question — *may you play a card that will accomplish nothing?* — answered opposite ways
by different mechanisms. Neither ruling is wrong, and neither is C: both are good examples
in their own sections. But a drafter meeting only one will state an over-broad rule.

**Both keep their normal labels and stay in their own extracts.** The tag is additive; the
slug is what brings them together later. You will not see the partner ruling — it is in
another chunk — so name the topic, not the pair. `{Dust Up}.3` and `{Veiled Sight}.1` belong
to this same slug.

This is also the standing answer to "these two rulings contradict": **do not resolve it, and
do not let it push you to C.** Flag it and move on; adjudication is a later pass with both
rulings in hand.

### General rule entries

**R2599** `G00061|Cancel an action.2` — "Can only cancel minion cards played from the hand
in the normal fashion (eg. not weapons played via {Disguised Weapon}…)."
→ `1.8,3.5` `P` [cited — 3.5.4]
`G000xx` ids are general rule entries, not card rulings: no card is doing the work, so they
state principles directly. **Almost always P, essentially never C.** Where the same wording
also appears on a card, label both the same way — entry `P`, card copy `E`.

### Boundary cases

**R0261** `Bundi.4` — "Cannot be used with a strike card that reads 'Strike: make a hand
strike.' but can be used with 'strike: make a weapon strike'… the strike is still
considered a hand strike (ie. can be chosen if {Immortal Grapple} has been played)."
→ `4.3` `E`
Reads card-specific, but it settles what a printed formula means, so it decides every card
carrying that formula. **Not C** — and note this is not an exception to the transfer test
but an *instance* of it: a genuine template ruling transfers by construction.

**The limiter (added round 2 — this example was over-applied).** "Turns on wording" is not
enough; nearly every ruling turns on some wording, and round 2 found this example rescuing
8-10 rulings from C on its own. A template ruling must satisfy **both**:

1. **Recurrence** — the wording is a *printed formula appearing on multiple cards*
   ("strike: make a hand strike", "each combat", "announced when the action is declared").
   If you cannot name or confidently expect sibling cards printing the same formula, it is
   not a template — it is this card's own sentence.
2. **Aboutness** — the ruling settles what the *formula* means, not how this card's
   particular effect resolves.

`Great Symposium.1` fails both: "only one Kiasyd" is not a printed formula recurring across
cards, and the ruling is about this card's own search. Apply the two tests before reaching
for this example.

**R0701** `Follow the Blood.2` — "Is played after resolution, but still during the action.
Cards and effects played 'after resolution' (eg. {Freak Drive}) can be played before it,
but not after."
→ `2.3,2.4` `P`
2.3 owns "after resolution"; 2.4 owns ordering among simultaneous effects. The ruling does
both. Tempting to file under 3.4 (resolution) — resist: this is about the *window*, not
about success.

## Grading history

**Round 1 (2026-07-20)** — two independent opus passes over the same 111-ruling stratified
sample (`calib-sample.tsv`), compared with `compare-runs.py`. Not owner-graded: the runs
were graded against each other, on the principle that agreement between two agents given
identical instructions estimates the drift to expect across the 18-way fan-out.

Agreement: **91.0%** shared at least one code (the extract-membership floor, which predicts
false negatives), **96.4%** agreed on absorbed-vs-excluded, 93.7% on primary code, 70.3% on
the exact code set. Role mix A: P34/E72/C3/G2. B: P28/E74/C5/G4.

Verdicts:
- **The C rate was broken, not the corpus.** 92-96% coverage, ~3% C. Both passes diagnosed
  it unprompted and identically: "when torn, add the label" (meant for choosing *codes*)
  was read as "prefer absorbing", and combined with "C must be argued" made C unreachable.
  → contract now scopes that rule explicitly and replaces the C test with transfer +
  non-obviousness. `Great Symposium.1` promoted to a worked example above.
- **G could not carry codes** — the strongest shared objection, raised independently by
  both. → fixed in contract and taxonomy; `Dreams of the Sphinx.3` rewritten to show it.
- **6.9 confirmed and added.** Both cited the same deciding rulings and both rejected the
  planted `Elder Library` control. Scope set to hand size + draw/discard + discard phase as
  one code (see taxonomy for why one and not two).
- **The announcement template was unanchored** — flagged by both. → anchored above.
- **P/E guidance was repeated in three files** — flagged by both as attention spent where
  the contract says not to. → trimmed here; contract keeps the single statement.
- Watch-list gaps raised but not acted on (sect-as-trait, cumulative/stacking, minion-phase
  action ordering, 3.7.4 overload) → recorded in `taxonomy.md`, decided at Phase 4.

Not yet known: the corpus's true absorption rate. Round 1 could not measure it because the
instrument was biased. Round 2 re-runs the same sample against the fixed contract.

**Round 2 (2026-07-20)** — same sample, same method, contract as fixed above.

Agreement improved across the board: identical code set 70.3% → **84.7%**, same role
85.6% → **91.9%**, extract-membership floor 91.0% → **93.7%**, primary code 93.7% → 94.6%.
Absorbed/not dipped 96.4% → 94.6%, as expected once exclusion became a real decision.
Role mix A2: P21/E80/C6/G4 (91.0%). B2: P24/E75/C5/G7 (89.2%). All G's carried codes.

Verdicts:
- **The fix worked on G, not on C.** Coverage fell ~4 points, but tracing the flips shows
  almost all of them went *into G* (the watch-list gaps, now flaggable because G carries
  codes) and the reverse flips were the 6.9 rulings correctly leaving the gap pile. **C
  counts were flat: 3→6 and 5→5.** The C rate is still suppressed.
- **Cause, diagnosed identically by both passes:** the asymmetry frame sat above the ⚠ that
  scoped it and outweighed it. "The ⚠ patches the rule but not the frame" (A2); "it fixes
  the letter, not the pull" (B2). → contract restructured into two explicitly independent
  judgments, absorption decided first and in isolation.
- **`Bundi.4` was over-applied** — B2 estimates it rescued 8-10 rulings from C single-
  handedly, doing more work than both C tests and in the opposite direction. → limiter added
  (recurrence + aboutness), and reframed as an instance of transfer rather than a rival to it.
- **Two instruction defects found, both mine, both would have split the 18-way run:** the
  contract's C-note paragraph was duplicated with divergent instructions, and this file still
  taught `Dreams of the Sphinx.3` as the flagship G *after* 6.9 was added to hold it. Caught
  independently by both passes. → paragraph deduplicated; G example replaced with
  `Betrayer.3`, plus an explicit "a closed gap is not a gap" lesson.
- **Tension mechanism added** (`!TENSION:<slug>`), asked for by three separate passes and by
  the owner independently. Contradictory-polarity rulings keep their normal labels and are
  co-located by slug for a later adjudication pass.
- Watch-list gaps got their second confirmation (cumulative/stacking, sect-as-trait,
  minion-phase ordering) but **no new members** — so still watch-list, not sections.
- New candidate, not acted on: card-conferred status "when played" vs "by an effect in play"
  (`Vidal Jarbeaux.8`), single instance in both rounds.

Open and deliberately unresolved: **the corpus's true C rate.** Two rounds have not measured
it, because both were run against instruments that leaned against C. The round-3 fix is in
place; whether to spend another round measuring a diagnostic-only number, or to proceed to
production and let Phase 4.5 section review catch over-absorption, is the owner's call.
