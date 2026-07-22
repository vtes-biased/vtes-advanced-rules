# Findings — {Arika} claim in §5.2.2 (WORKING-NOTES open item 3, phantom-audit ⚠)

Sweep date: 2026-07-22. Scope: the §5.2.2 unlock-phase-condition sentence and footnote
[^5-2-7]; the {Arika} ruling state post-[ANK 20250121].

## F-arika-1 — §5.2.2 states the reversed (dead) Arika rule  [stale] [blocking]

**Where:** §5.2.2, lines 2867–2869:

> A condition on what a Methuselah controls during that phase is checked when the phase
> ends: meeting it earlier does not help, acquiring the object later does not excuse it,
> e.g. {Anarch Revolt}, {Arika} ([§2.5](#25-duration-and-persistence)).[^5-2-7]

Footnote (line 4598):

> [^5-2-7]: [LSJ 20080106](https://groups.google.com/g/rec.games.trading-cards.jyhad/c/q4s1P6ozsW8/m/N9wEQl5sgTgJ) [ANK 20200629](https://www.vekn.net/forum/rules-questions/78700-arika-special-order?start=6#100211) [ANK 20220503](https://www.vekn.net/forum/rules-questions/39040-re-ex-nihilo-can-i-choose-to-burn-my-minion#105161) — {Anarch Revolt}, {Arika}, {Drink the Blood of Ahriman}.

**Evidence:**

- {Arika} card text (KRCG 200135): "If Arika is ready during your prey's unlock phase,
  your prey chooses which locations he or she keeps in play. For each location he or she
  controls, your prey burns 1 pool or burns the location. +2 bleed."
- The "acquiring later does not excuse it" half was the retracted [LSJ 19990405]
  ("Arika's prey cannot end her unlock phase if she controls a location that she hasn't
  burned a pool for, even if she gained control of that location during that unlock
  phase") — quoted verbatim in the VEKN thread and answered by Ankha (Rules Director,
  21 Jan 2025 13:38, = [ANK 20250121]): **"This ruling is also REVERSED."**
  (https://www.vekn.net/forum/rules-questions/79080-nightmares-upon-nightmares?start=6#113567,
  fetched 2026-07-22.)
- Same post series, 13:30, the doctrine: **'"For each ... do something" should be
  resolved as a whole, and only once. This means that when you decide to resolve this
  effect, you consider the minions in play at that moment. This is a REVERSAL of the
  ruling above.'** (reversing Ankha's own earlier {Nightmares upon Nightmares} ruling
  that an ally gained mid-phase must still be locked or discarded for). Also:
  **"NB: Conditional effects (eg. Anarch Revolt) are different as they cannot be
  resolved if the condition is not met."**
- Pinned DB, `200135|Arika`: "The effect only triggers once each unlock phase. Any
  Locations put into play after the effect is resolved are unaffected until their
  Methuselah's next unlock phase. [REVERSAL] [ANK 20250121]" — same text under
  `101285|Nightmares upon Nightmares` (minions).
- `100055|Anarch Revolt` [LSJ 20080106] survives unreversed: "If a Methuselah controls
  no ready Anarch by the end of the unlock phase, they must burn 1 pool, even if they
  had a ready Anarch at some point during the unlock phase." Card text: "A Methuselah
  not controlling a ready Anarch burns 1 pool during their unlock phase."
- [ANK 20200629] survives ("Arika's prey can use a location during her unlock phase
  before burning it") but supports no clause of the current sentence.
- [ANK 20220503] is the {Ex Nihilo}/{Drink the Blood of Ahriman} burn-blood-or-burn-card
  free-choice reversal ("No, you can choose between both options. This is a REVERSAL.")
  — it supports no clause of this sentence either; it is correctly cited at [^1-7-25],
  [^2-4-12], [^6-6-7].

**Analysis:** The sentence fuses two models. The Anarch Revolt half (conditional effect,
checked at end of phase, meeting it earlier does not help) stands — [LSJ 20080106] is
live and Ankha's NB expressly carves conditional effects out of the reversal. The Arika
half ("acquiring the object later does not excuse it") is the reversed [LSJ 19990405]
rule: since [ANK 20250121], the "for each" tax resolves once, over the locations in play
at that moment, and later-acquired locations are untouched until the next unlock phase.
A judge applying the sentence as written would misrule the Arika case in exactly the
direction the Rules Director reversed. The §2.5 cross-reference fits the corrected text
even better (§2.5.2's snapshot-at-resolution principle, {Annabelle Triabell}).

**Proposed fix (exact edit, ready to apply):**

Body, §5.2.2 — old string:

```
 A condition on what a Methuselah
controls during that phase is checked when the phase ends: meeting it earlier does not help,
acquiring the object later does not excuse it, e.g. {Anarch Revolt}, {Arika} ([§2.5](#25-duration-and-persistence)).[^5-2-7]
```

new string:

```
 A condition on what a Methuselah
controls during that phase is checked when the phase ends: meeting it earlier does not
help, e.g. {Anarch Revolt}.[^5-2-7] A "for each" unlock-phase effect instead resolves once,
as a whole, over the objects in play at that moment: objects acquired after it resolves are
unaffected until the Methuselah's next unlock phase, e.g. {Arika}, {Nightmares upon
Nightmares} ([§2.5](#25-duration-and-persistence)).[^5-2-30]
```

References section — old string:

```
[^5-2-7]: [LSJ 20080106](https://groups.google.com/g/rec.games.trading-cards.jyhad/c/q4s1P6ozsW8/m/N9wEQl5sgTgJ) [ANK 20200629](https://www.vekn.net/forum/rules-questions/78700-arika-special-order?start=6#100211) [ANK 20220503](https://www.vekn.net/forum/rules-questions/39040-re-ex-nihilo-can-i-choose-to-burn-my-minion#105161) — {Anarch Revolt}, {Arika}, {Drink the Blood of Ahriman}.
```

new string (two definitions; [^5-2-30] is the next free label in the family, max in use
is [^5-2-29], and first-use ordering puts it here):

```
[^5-2-7]: [LSJ 20080106](https://groups.google.com/g/rec.games.trading-cards.jyhad/c/q4s1P6ozsW8/m/N9wEQl5sgTgJ) — {Anarch Revolt}.
[^5-2-30]: [ANK 20250121](https://www.vekn.net/forum/rules-questions/79080-nightmares-upon-nightmares?start=6#113567) — {Arika}, {Nightmares upon Nightmares}.
```

Dropped citations, deliberately: [ANK 20200629] (live but supports a claim the document
does not make — re-add to [^5-2-30] only if the owner wants a "the prey may still use a
location before burning it" clause); [ANK 20220503]/{Drink the Blood of Ahriman}
(supports burn-choice freedom, not end-of-phase checking; correctly cited elsewhere).

## F-arika-2 — [ANK 20220503] in [^5-2-7] supports no clause of the sentence  [wrong-citation] [minor]

Folded into F-arika-1's footnote edit; recorded separately so it is not lost if the
owner rewords F-arika-1 differently. Evidence in F-arika-1.

## Note — general-doctrine hook (owner's call, no edit proposed)  [gap] [note]

[ANK 20250121] states a general doctrine beyond the unlock phase: "for each ..." and
"X, where X is ..." effects are strictly equivalent, resolve once as a whole, and
"effects in VTES cannot be interrupted during resolution" (exceptions only where a card
prints one, e.g. {Psyche!} vs {Rötschreck}). The document states uninterruptibility only
for diablerie (§3.7.8) and mend/burn-to-prevent sequences; whether §1.7/§2.4.6 should
carry the general statement is an owner drafting decision, not a defect.

## Adjudication question

Post-[ANK 20250121], does {Arika}'s location tax still bind locations the prey acquires
later in the same unlock phase (old end-of-phase model), or does it resolve once over
the locations in play at that moment, leaving later acquisitions untouched until the
next unlock phase? **Recommended answer:** the latter — the reversal is explicit, on the
record, and mirrored under {Nightmares upon Nightmares}; apply the split-sentence edit
above, keeping {Anarch Revolt}'s end-of-phase check, which the same post expressly
preserves for conditional effects.
