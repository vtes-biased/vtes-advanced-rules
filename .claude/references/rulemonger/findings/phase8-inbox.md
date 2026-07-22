# Phase-8 inbox triage — findings (2026-07-21)

Sweep: 35-item wave-2 drafter inbox (content pasted by owner; docs/_work/ not read),
re-checked against the current assembled `docs/extended-rules.md` (post R-017/R-022,
post reference-reformat). Result: 29 CLOSED, 5 EDITs (E1–E6, none blocking severity
beyond E1/E2), 0 OWNER questions, 3 UPSTREAM defects (+2 low-priority annotations).
Three drafter upstream recommendations COUNTERMANDED on evidence (Sundown, Legacy,
The Becoming). Line numbers are current as of this session.

## F-p8i-1 — "(limited)" cap-holder stated action-side only  [over-broad] [blocking]
**Where:** §1.2.1 lines 130–134; §1.15 line 881.
**Evidence:** [RBK additional-strikes] "A minion cannot use more than one card or
effect to gain additional strikes per round of combat." (content.md 1695–1698; glossary
2682–2690 states both caps side by side). [RBK bleed] binds the bleed action
(content.md 947–951). [ANK 20190117-1] {Mask of a Thousand Faces}: "He cannot use a
limited effect (ie. bleed enhancer) if a limited effect has already been used on the
action." [ANK 20220204] {Dust Up}: "you cannot play it for the dodge only if **you**
already played it for a (limited) additional strike this round" (per-minion). The
document's "The limit binds the action (or round), not the minion" would deny the
opposing combatant a limited additional strike — a misrule. §3.7.1 base rules (1552–55)
already state the bleed side correctly; §3.10.1 (2168–70) is ruling-verbatim and fine.
**Proposed fix:** E1 + E2 (exact text in session report). Amend [^1-2-15] to add
[RBK bleed] and [RBK additional-strikes] links.

## F-p8i-2 — §1.1.3 two-branch "cannot" test mispredicts the G00137 template  [gap] [minor]
**Where:** §1.1.3 lines 77–81 ({Rigor Mortis} example sits unexplained in the
names-cards branch).
**Evidence:** {Rigor Mortis} (101636) prints "The opposing minion cannot use any
additional strikes this round" — names neither cards nor an outcome. G00137 "Prohibits
additional strikes" ({Blight}, {Decompose}, {Rigor Mortis}, {Stutter-Step},
{Sympathetic Agony}, {Target Head}): "The affected minion cannot play a card that
provides an additional strike, even if just to benefit from another effect (e.g.
{Acrobatics})." [LSJ 20011214-5]. A judge applying the stated test to another G00137
member would classify "cannot use X" as a barred outcome and misrule. [^1-1-7] already
cites G00137.
**Proposed fix:** E3 — name the template as an adjudicated third family, scoped to
additional strikes only (do not generalize to all "cannot use" wordings; no ruling
supports more).

## F-p8i-3 — [^4-2-9] record key wrong  [wrong-citation] [minor]
**Where:** References, line 4329, supporting §4.2.3 (line 2288–91, Lucian surcharge).
**Evidence:** [LSJ 20090529] is filed under {Jann Berger} (rulings.yaml 200675, the
Thrown Gate arithmetic) and group G00074 "Adding costs to a strike or strike card"
("If an opponent then plays an effect that grants a strike (e.g. {Aid from Bats}),
they pay the additional cost."). It is NOT in the {Lucian, the Perfect} record
(200871: LSJ 20031118 / 20090528-2 / 20090528-2-2 only). Targeted grep performed per
the R-015 lesson. Note: the drafter's "cost of the strike, not of the card" inference
is VERIFIED by these two rulings — no owner check needed.
**Proposed fix:** E4 — record keys → {Jann Berger}, group "Adding costs to a strike
or strike card" (G00074).

## F-p8i-4 — {Valerius Maior} prose example names a printing the clause is not on  [style/stale] [note]
**Where:** §2.5.1 line 1133.
**Evidence:** KRCG 201421 (base G4): no block-prohibition. 201422 (G4 ADV): "If
Valerius attempts to block, the acting minion cannot play action modifier or combat
cards that require [chi] or [obf]." DB record `201422|Valerius Maior, Hell's Fool`
(plain name, ADV id). A name lookup returns the base card without the clause.
Footnote key stays as the DB key (R-009).
**Proposed fix:** E5 — "{Valerius Maior, Hell's Fool (ADV)}" in prose (DB in-text
convention, cf. "{Alan Sovereign (ADV)}").

## F-p8i-5 — {Karsh} prose: title is on the merged form  [style] [note]
**Where:** §5.8.1 line 3264.
**Evidence:** KRCG 200757 (base): no Imperator title. 200758 (G3 ADV): "[MERGED]
Imperator (3 votes)". DB ruling [ANK 20190407] is [MERGED]-tagged.
**Proposed fix:** E6 — "…that merged {Karsh} prints."

## Countermanded drafter claims (do not file upstream)
- **{Sundown} R2437/R2438 are NOT mis-stamped.** DB record is `201326|Sundown` = the
  G3 ADV printing; its [MERGED] text prints "discard a political action card to force
  any vampire to abstain." The drafter checked only base 201325. Document's use of
  {Sundown} as a record key in [^3-7-6-2] is correct.
- **{Legacy} R1022 is NOT stale.** KRCG `burn_option: True` for 101085 — the burn
  option is an icon carried in a separate JSON field, absent from `card_text`.
- **R0138 {The Becoming} needs no retirement.** Printed "0-capacity" + cards-out-of-
  play-while-uncontrolled + the ruled capacity floor ([RTR 19990712] {Dual Form}:
  "A vampire's capacity can never be reduced below one") = exactly the ruling's
  "1-capacity vampire if moved to the uncontrolled region" [LSJ 20090625]. §5.1.1's
  chain is fully sourced.

## UPSTREAM (vtes-rulings database)
1. `101232|Mokolé Blood` ruling 2: garbled — "It does is if it is equipped" →
   "It does get them if it is equipped".
2. `100868|Guardian Vigil`: maneuver rulings carry stale [aus] prefixes
   ([LSJ 20010814-2] [ANK 20181127]; "[aus] The maneuver can only be used…") — current
   printing puts the maneuver on [cel]; [aus] is +1 intercept. Retag.
3. `201422|Valerius Maior, Hell's Fool`: ruling describes ADV-only printed text under
   a plain-name key with no [MERGED]/(ADV) marker — annotate the printing.
4. `200649|Ivan Krenyenko`: same class — [RTR 19941109] presupposes the ADV-only
   "Equipment costs Ivan 2 fewer" text; plain-name key, no marker.
5. (low) `200179|Beast…` ruling 2: "as it is an action card" is loose for printed
   Equipment locquipments like {Palatial Estate}; defensible only under the rulebook's
   "Action Card (or Card in Play)" umbrella — a clarity reword would help.

## Status
Awaiting owner adjudication of E1–E6. All other inbox items CLOSED (verdicts and
evidence in the session report of 2026-07-21).
