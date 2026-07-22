# Findings — no-effect-plays consistency sweep (§1.6.5 doctrine)

Sweep date: 2026-07-22. Scope: §1.1, §1.6, §1.8, §1.9, §3.1, §3.2, §3.4, §3.7.5, §4.2,
§4.3, §4.5, §4.6, §5.5, Appendix A entries. Canonical form: §1.6.5 (owner adjudication
2026-07-20, R-012).

**Doctrine verdict: clean.** No over-broad statement, no inverted polarity, no divergent
restatement found; all cross-references route to §1.6. The six findings below are
footnote-apparatus repairs (lookup paths / one missing citation), none doctrinal, none
blocking. R-017's deliberate dual statements (§1.6.5/§4.5.1 prevention; {Repulsion} in
§1.6.5/§3.2.3/§4.5.1) were not re-reported.

Status: ADJUDICATED 2026-07-22 (owner: apply) — all seven footnote repairs applied
(F-noeff-1..7). See R-030.

## F-noeff-1 — §3.2.2's "not attempting to block" sentence is uncited; the supporting ruling exists  [unsupported-claim] [minor]
**Where:** §3.2.2, "Such a card may be played by a minion that is not attempting to
block." — inside the [^3-2-3] paragraph.
**Evidence:** [^3-2-3] cites only [RTR 20030519] [LSJ 20021211] — {Draba}, {Night
Terrors}; neither record states the point, and the LSJ 20021211 thread (fetched) does not
address it. The ruling that does: G00104 "Minus stealth" — "Can be played/used any time
during the action before resolution; a block attempt is not required. [LSJ 20020612]"
(rulings.yaml ~4532; members include {Draba}, {Night Terrors}, {Ignis Fatuus},
{Starshell Grenade Launcher}). [LSJ 20020612] is currently cited nowhere in the document;
its URL is in references.yaml (line 622).
**Proposed fix:** replace [^3-2-3] with:
```
[^3-2-3]: [RTR 20030519](https://groups.google.com/g/rec.games.trading-cards.jyhad/c/NOBWXWrd-vA/m/iEOpQp1uhvAJ) [LSJ
    20021211](https://groups.google.com/g/rec.games.trading-cards.jyhad/c/-J07wvmidOA/m/gPQ5ngEZ6HcJ) [LSJ
    20020612](https://groups.google.com/g/rec.games.trading-cards.jyhad/c/sC0pTtJJDj4/m/bD04Jy4pM_cJ) — {Draba},
    {Night Terrors}, group "Minus stealth" (G00104).
```

## F-noeff-2 — [^1-6-21] cites [LSJ 20070411] under record keys that do not carry it  [wrong-citation] [minor]
**Where:** References, [^1-6-21] (backs §1.6.5's futility-default sentence).
**Evidence:** [LSJ 20070411] is filed under {CrimethInc.}, {Forced March}, {Harass},
{Instantaneous Transformation}, {Perfectionist}, {Sleep of Reason} and groups
G00078/G00080/G00081 — none of [^1-6-21]'s keys ({Absorb the Mind}, {Call the Lamprey},
{Draba}, {Night Terrors}, {Siphon}, {Kindred Segregation}, {Peace Treaty}). Each named
record was grepped individually: the ID appears in none. The defect predates the D8
footnote merge (old [^1-8-19] had the same key set). The ID's rulings are the
success-riders-on-no-effect-actions family, already correctly cited at [^3-4-1]
({Harass}), [^3-4-4] ({Forced March}, {CrimethInc.}, {Perfectionist}) and [^1-7-2]
(G00078/G00080/G00081). §1.6.5's sentence stays fully supported by the remaining IDs
([RTR 20010710] {Peace Treaty}/{Kindred Segregation}: "Can be called even if there are no
weapons/allies in play"; [RTR 20010711]; [PIB 20110725]; [LSJ 20021211]).
**Proposed fix:** drop the ID; replace [^1-6-21] with:
```
[^1-6-21]: [RTR 20010711](https://groups.google.com/g/rec.games.trading-cards.jyhad/c/GsI1UyH54jU/m/x9LfDZX1vR4J) [LSJ
    20021211](https://groups.google.com/g/rec.games.trading-cards.jyhad/c/-J07wvmidOA/m/gPQ5ngEZ6HcJ) [PIB
    20110725](https://www.vekn.net/forum/rules-questions/6728-announcing-siphon#6740) [RTR
    20010710](https://groups.google.com/g/rec.games.trading-cards.jyhad/c/GsI1UyH54jU/m/x9LfDZX1vR4J) — {Absorb the
    Mind}, {Call the Lamprey}, {Draba}, {Night Terrors}, {Siphon}, {Kindred Segregation}, {Peace Treaty}.
```
(Alternative if the owner wants the ID kept here: add keys {Harass} and groups
G00078/G00080/G00081 — but that duplicates [^1-7-2]/[^3-4-1].)

## F-noeff-3 — [^1-6-22]: [ANK 20200420-3] is filed under G00122, not {Vulture's Buffet}  [wrong-citation] [minor]
**Where:** References, [^1-6-22] (backs §1.6.5's missing-object family).
**Evidence:** rulings.yaml: `102135|Vulture's Buffet` carries only "Is a hunt action.
[ANK 20200421]". The cited ruling lives at G00122 "Targets card in Ash Heap": "Cannot be
played if no target is available in any Methuselah's ash heap. [ANK 20200420-3]"
(~line 4601); {Vulture's Buffet} is a G00122 member. Per R-009, keys name the record the
ruling is filed under. All other [^1-6-22] IDs verified in place ([RTR 19980928] on the
four strike cards + {Brujah Frenzy}'s [RTR 19951110]; [LSJ 20100527] {Storage Annex};
[LSJ 20070901] {Liquidation}; [LSJ 20060623] {Undue Influence}; [LSJ 20010810]
{Free States Rant}; [PIB 20121028] {Taste of Vitae}).
**Proposed fix:** in [^1-6-22]'s key list, replace `{Vulture's Buffet}` with
`group "Targets card in Ash Heap" (G00122)`; final three lines become:
```
    20121028](https://www.vekn.net/forum/rules-questions/39816-ec-2012-can-you-answer-these?start=6#39843) — {Shattering
    Blow}, {Fractured Armament}, {Canine Horde}, {Blessing of Durga Syn}, {Brujah Frenzy}, {Storage Annex},
    {Liquidation}, {Undue Influence}, {Free States Rant}, {Taste of Vitae}, group "Targets card in Ash Heap" (G00122).
```

## F-noeff-4 — [^4-3-12]: two IDs keyed to member cards; one stray key  [wrong-citation] [minor]
**Where:** References, [^4-3-12] (backs §4.3.3's damage-add-on / after-combat-damage /
strike-missing-object sentences).
**Evidence:** [ANK 20170111] and [LSJ 20071011] are filed under {Dam the Heart's River}
("Applies to damage played in combat that are resolved after combat (eg. {Catatonic
Fear})", ~line 789) and — [ANK 20170111] with [PIB 20130319] — under G00091 "Damage after
combat ends" (~line 4493) and {Riposte}; the current keys {Catatonic Fear} and
{Loving Agony} are G00091 members whose own records carry neither ID. {Lucky Blow}'s
record carries none of the five cited IDs at all. Verified in place: [RTR 19960221] and
[PIB 20130319] under {Target Vitals} and {Target Head} ("Can be played on a strike that
does no damage, even a dodge or a combat ends, but has no effect in that case");
[RTR 19980928] under {Talith} ("The 'strike: destroy weapon' cannot be chosen if there is
no weapon to destroy").
**Proposed fix:** replace the key list (last two lines of [^4-3-12]) with:
```
    19980928](https://groups.google.com/g/rec.games.trading-cards.jyhad/c/Xva4_IRavxM/m/F-_fjzTmo88J) — {Target Vitals},
    {Target Head}, {Talith}, {Dam the Heart's River}, group "Damage after combat ends" (G00091).
```

## F-noeff-5 — [^4-5-1] keys are G00154 member cards, not the group record  [wrong-citation] [minor]
**Where:** References, [^4-5-1] (backs §4.5.1's immediate-prevention bar).
**Evidence:** [LSJ 20001114] is filed under G00154 "Immideate damage prevention" ("Cannot
be used if there is no damage to prevent.") and under {Hidden Strength}; the current keys
{Soak}, {Skin of Night}, {Glancing Blow}, {Armor of Vitality}, {Indomitability} are all
G00154 member names whose own records do not carry the ID. [^1-6-23] already keys this
same ID to G00154 correctly (keeping the DB's "Immideate" typo per R-009).
**Proposed fix:** replace [^4-5-1] with:
```
[^4-5-1]: [LSJ 20001114](https://groups.google.com/g/rec.games.trading-cards.jyhad/c/qXSlM7Grq1c/m/cSDoQ9mw0z4J) —
    group "Immideate damage prevention" (G00154).
```
(Optionally add {Hidden Strength}, which carries the ID per-card alongside
[LSJ 20030121].)

## F-noeff-6 — [^4-6-8] keys are G00109 member cards, not the group record  [wrong-citation] [minor]
**Where:** References, [^4-6-8] (backs §4.6.4's cannot-be-dodged rule).
**Evidence:** "Does not prevent the opponent from dodging, the dodge just has no effect.
[LSJ 20030902-2] [LSJ 20060808-1]" is filed under G00109 "Cannot be dodged" (~line 4558)
and, per-card, under {Shadow Feint} only. {Collapse the Arches} has no record in
rulings.yaml at all; {Scorpion Sting} and {Projectile} records carry neither ID (all
three are G00109 members). Body examples ({Scorpion Sting}, {Projectile}) are fine and
unchanged.
**Proposed fix:** replace [^4-6-8] with:
```
[^4-6-8]: [LSJ 20030902-2](https://groups.google.com/g/rec.games.trading-cards.jyhad/c/mgZt4f2LyOg/m/FCeKmePPkxwJ) [LSJ
    20060808-1](https://groups.google.com/g/rec.games.trading-cards.jyhad/c/7oK-hKbOs9g/m/EGeyVt3vfl4J) — group "Cannot
    be dodged" (G00109), {Shadow Feint}.
```

## F-noeff-7 — [^3-4-15] stray key {Spying Mission}  [wrong-citation] [note]
**Where:** References, [^3-4-15] (backs §3.4.3's zero-bleed sentence — a doctrine fixed
point; the sentence itself is correct).
**Evidence:** [PIB 20150612] is filed only under {Andre LeRoux} ("If his ability reduces
a bleed to zero, it is no longer successful and {Spying Mission} cannot be used
afterwards"); the {Spying Mission} record (grepped in full) does not carry it.
**Proposed fix:** replace [^3-4-15] with:
```
[^3-4-15]: [PIB 20150612](https://www.vekn.net/forum/rules-questions/71660-andre-leroux-spying-mission#71685) — {Andre
    LeRoux}.
```

## Per-section verdicts

| Section | Verdict |
|---|---|
| §1.1 | Clean — "cannot"-names-cards vs names-outcome split verified (G00141 [LSJ 20050628] "eg. for cycling"; G00137 [LSJ 20011214-5]; {Legacy of Caine} outcome-cannot). |
| §1.6.5 | Canonical form verbatim-consistent with the adjudicated doctrine; two footnote repairs (F-2, F-3). |
| §1.8 | Clean — no doctrine content (old §1.8.5 duplicate correctly merged away; cycling bar owned by §1.1.3). |
| §1.9 | Clean — §1.9.4 states the empty-crypt bar as §1.6's missing-object family, "not futility"; G00126 verified. |
| §3.1 | Clean — §3.1.3 keeps both polarities (G00034 no-legal-object bar; {Siphon}/[RTR 20010711]/[PIB 20110725] empty-target default). |
| §3.2 | Consistent — §3.2.1 bar + printed waivers, §3.2.2 reduction polarity, §3.2.3 {Repulsion} play-not-effect; one missing citation (F-1). |
| §3.4 | Consistent — fizzle/success split, {Veil of Darkness} per R-025(e), zero-bleed fixed point; one stray key (F-7). |
| §3.7.5 | Clean — {Peace Treaty} no-subject referendum with §1.6 pointer ([RTR 20010710] verified). |
| §4.2 | Clean — {Rötschreck} framed as trigger-unmet vs futility-no-bar, matching [RTR 19980928] [ANK 20211102]. |
| §4.3 | Consistent — {Target Vitals}-on-dodge default and strike-missing-object bar both verified; footnote re-key (F-4). |
| §4.5 | Consistent — immediate vs duration-grant split (deliberate dual statement with §1.6.5, R-017); footnote re-key (F-5). |
| §4.6 | Consistent — §4.6.4 states the permissive default and walls it off from prevention; footnote re-key (F-6). |
| §5.5 | Clean — {Taste of Vitae}/{Enhanced Coagulant} missing-object family ([PIB 20121028] verified); repay-template kept separate. |
| Appendix A | Clean — "playing a card that will do nothing", "prevention (immediate vs standing)", "needed (stealth/intercept)", "cannot", "{Blood Fury} template", "cannot be dodged" all match the canonical form and point at the owning sections. |

Not a gap (by design): {Deep Cover Agent} [ANK 20240610] ("no matter the presence or
absence of a valid target") is a one-card printed-condition interpretation — stays in the
DB per the drafter contract.
