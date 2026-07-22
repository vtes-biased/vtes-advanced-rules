# Rulemonger memory

Maintained by the rulemonger agent; adjudicated by the owner. This file — not any
conversation — is the agent's accumulated judgment. Two layers, maintained by
*promotion*: when a case teaches something general, the lesson moves up to General
lessons and the case entry stays thin, pointing at it.

**Supersession discipline (binding):** one entry per question, forever. A reversal or
refinement rewrites the entry's Position in place and records the old stance in its
History line. Never a second entry contradicting an earlier one. `SETTLED` entries are
binding on future sessions; challenging one requires a finding that names it
("challenges R-###") with new evidence, and only the owner flips it.

Entry format:

```
### R-001 — <one-line question>  [SETTLED | OPEN]
**Position:** <the binding answer, stated as the rule>
**Sources:** [LSJ 20061207], {Card} / group "Name" (G#####), [RBK anchor]
**History:** <only if it ever changed: date, prior stance, what flipped it>
```

## General lessons

- **Equipment, ally, retainer and political action cards are action-card subtypes
  (owner ruling, 2026-07-22).** Playing any of them from hand is playing an action
  card, so a bar like {Beast, The Leatherface of Detroit}'s "Beast cannot play action
  cards" reaches an equipment card — including a locquipment such as
  {Palatial Estate}. The Beast ruling's stated reason ("not by playing the card
  normally as it is an action card") is CORRECT as written; the proposed reword was
  reverted out of vtes-rulings PR #10. The document already agrees (§1.3.1 Beast
  sentence; §1.3.2 "a retainer employed through {Pack Alpha} is still an action
  card"). Do not re-flag this wording.
- **ADV-only rulings sit on the ADV card's record — that IS the printing marker
  (owner policy, 2026-07-22).** The advanced version of a vampire is another card with
  its own id; a ruling that applies only to the advanced text belongs on that record
  (e.g. `201422|Valerius Maior, Hell's Fool` = G4 ADV, `200649|Ivan Krenyenko` =
  G2 ADV). Keys use the printed name; the id disambiguates. Do not propose "(advanced
  version only)" annotations in ruling text and do not flag plain-name keys on ADV ids
  as defects. Name-based lookups being ambiguous is by design — resolve by id.
- **The drafting corpus diverges from the pinned database.** `docs/_work/rulings-flat.tsv` (retired to git history 2026-07-22)
  was generated from a pre-pin snapshot of the rulings DB. 35 of 1,166 reference IDs cited
  in the document do not exist in the pinned `references.yaml` (nor upstream HEAD). When a
  footnote cites an ID or group absent from the pinned DB, do not assume retraction:
  recover it from the submodule's git history (`git log -S "<string>" -- rulings/`), read
  the deletion commit, and fetch the original URL from the pre-deletion `references.yaml`.
  G00031's deletion (upstream e13882a, a bot commit mislabeled "Adding cards to group")
  looks accidental, and the original ruling survives on the VEKN forum.
- **Group consolidation can drop per-card specifics.** When TOM 19960521 was consolidated
  into G00096 "Optional press", {Dust to Dust}'s "press **and maneuver** can only be used
  during the current round" lost its maneuver half. When a group ruling reads narrower
  than the document's claim, check the per-card historical expansion (flat TSV or KRCG
  API) before calling the claim over-broad.
- **Scope each general sentence to its evidence** (owner's drafting caution, F1
  adjudication 2026-07-21): when a principle is evidenced only in one phase/context,
  word the sentence so that scoping is visible; do not let a rewrite silently narrow a
  genuinely general principle either. State the general rule only where exemplars from
  more than one context exist elsewhere in the section.
- **Mode discipline held under pressure:** a coordinator relay of owner adjudications is
  direction for work, but does not flip `Mode: FINDINGS-ONLY`. Deliverable in that case:
  hunts done, memory updated, exact ready-to-apply edit text in the report, document
  untouched.
- **Upstream deletes rulings that reprints folded into card text.** [LSJ 20010725]
  ({Extortion}: "Usable by a locked vampire"), [LSJ 20051207] ({Pack Alpha}) and
  [LSJ 20080702-3] ({White Lily}: "requirements and cost apply as normal") were all
  deleted because the current card text now prints the rule. Before treating a deleted ID
  as a retraction, fetch the card: if the text carries the rule, cite card text or a
  surviving group ruling (e.g. G00131 [LSJ 20100303] "Requirements apply") and drop the ID.
- **Cost gates, triggered burn does not.** "Burn X blood *to attempt to block*"
  ({Tenebrous Form} [OBT], G00088) is a cost: an empty vampire cannot attempt. "Any
  vampire attempting to block … burns 1 blood" ({Camarilla Exemplary}) is a triggered
  consequence: an empty vampire blocks and burns what it has. {Unleash Hell's Fury}
  states both sides in one ruling [LSJ 19970707] [ANK 20230226]. Same cost-vs-effect
  discriminator as §1.7.4's burn-blood-for-effect family.
- **Cancels: standing abilities pre-empt, card plays are answerable.** A cancellation
  from an ability in play applies before anyone may respond ({Andrew Stuart}
  [LSJ 20100728] [LSJ 20090213]); a cancellation that is itself a card play opens its
  own "as played" window and can be canceled there ({Sudden Reversal} on
  {Direct Intervention}). Never state "cancels resolve first" flat.
- **"As if from your hand" = a normal, cancelable play.** {Persistent Echo},
  {The Erciyes Fragments} print it; [RTR 20040501] presupposes Erciyes plays are
  cancelable as played; {Echo of Harmonies} parallel [LSJ 20100426]. "Cancellation
  reaches only plays from hand" is under-inclusive without it.
- **Cancellation propagates downward only.** Canceling a strike cancels the card's whole
  effect [RBK cancel-a-card]; canceling a maneuver cancels the press it provides
  [ANK 20230114] but never the strike that provided the maneuver, which cannot be
  changed [LSJ 20050228-3] [ANK 20230111] (all under {Rigor Mortis}).
- **Member-card keys where a group record holds the ruling are a recurring footnote
  defect.** The drafter sometimes keyed a group ruling to the group's *member* names
  (found 2026-07-22: [^4-6-8] G00109 members, [^4-5-1] G00154 members, [^4-3-12] G00091
  members, [^1-6-22] a G00122 member) even though sibling footnotes key the same group
  correctly ([^1-6-23] → G00154). When one footnote shows the pattern, grep the other
  footnotes citing the same IDs; the fix is R-009's (key the group, DB name verbatim,
  typos included). Footnote merges also carry old strays forward — check the pre-merge
  label in git history before blaming the merge.
- **Before declaring a citation wrong, grep the specific record.** A date-based ID
  ([RTR 19951110]) is shared by unrelated rulings under several cards, and batch lookups
  piped through `head` can truncate before the relevant record prints. This produced a
  false wrong-citation on [^1-15-4] (2026-07-21, W-cycle): {Scorn of Adonis} carries its
  own [RTR 19951110] ruling verbatim (rulings.yaml ~2561) — the batch output was cut
  before it appeared. Rule: a wrong-citation finding requires a targeted
  `grep -A4 "|<Card>:"` on the cited record coming back empty, never just a batch scan.
- **A delayed replacement is simply absent at the moment of play.** Effects tied to the
  play resolve then, without it ({Troglodytia} [ANK 20180512] sees less; {Agaitas}
  [LSJ 20020718] fires not at all); effects keyed to the replacement itself wait for it
  ({Learjet} [PIB 20110718]). And delayed-replacement clauses govern only normal plays —
  "put into play in a special way … replaced immediately" ({Baseball Bat}
  [LSJ 20080702-2]), even mid-action.
- **At contest entry: enter-play effects resolve pre-contest, standing effects never
  apply.** "The cards are put on it before it enters contest" ({Mokolé Blood},
  {Shilmulo Tarot} [ANK 20221028] [LSJ 20090428-1]) is about the INCOMING copy's own
  enter-play effect; {Elder Library} "enters contest without modifying the hand size"
  [ANK 20221028]. §1.12.2 had misread the Mokolé ruling as moving cards to the other
  copy — no source says that.
- **Cards under a departing host: the region model (owner's, 2026-07-21).** Cards on a
  host burn when the host leaves play — burned, removed from the game, returned to hand/
  library/crypt, or set aside with no printed provision ({Raw Recruit} burns them
  [LSJ 20100302-2]; {Memory's Fading Glimpse} [SFC 19960919]). Torpor, the uncontrolled
  region and contest are not such departures: cards follow the host, out of play but
  intact ([RBK contested-cards] burns stacked cards only on yield; {Lay Low} goes to the
  uncontrolled region, its printed keep-clause merely restating the region rule). A
  set-aside can keep them only by printing it ({Descent into Darkness} "and any other
  cards and counters on them" [LSJ 20080816]). "Out of play" is a status; the burn rule
  keys on the departure event.
- **The prevention/no-effect discriminator is immediate vs duration-grant.** Immediate
  "prevent X damage" cards need unresolved damage (G00154 "Immideate damage prevention",
  member {Armor of Vitality}); cards granting a prevention *ability* for a duration are
  playable with no damage yet ({Apparition} [LSJ 20010315], {Brother's Blood}
  [LSJ 20100527]). Same shape as {Repulsion} [OBE] [LSJ 20011214-2]: duration-granting
  plays escape the not-needed bar. Never state the prohibition side flat.

- **Absolute values set; "+X" adds.** A card granting "X" (a value: {Legacy of Pander}
  "gets 1 vote", {Torn Signpost} "gets a strength of 2") sets it — copies do not stack,
  and setting can *reduce* ({Rock Cat} at [pot], directly ruled: "Sets base strength. It
  can reduce the base strength of a minion" [PIB 20130303]); "+X" effects then add to
  the set value [LSJ 20100813]. When a draft calls something an "exception", check
  whether it is really an unread wording template — votes were never an exception.
- **A cross-reference is a promise — verify the target holds the content.** §1.13.5 said
  "§5.7 owns Blood Brothers" while §5.7 contained no circles material at all. Before
  deleting a local statement in favor of "§X owns this", read §X.
- **Group records supersede stale per-card phrasings — check both directions.** The
  known lesson is that consolidation can *drop* per-card specifics; the reverse also
  holds: a per-card record can retain a superseded wording that the group record
  corrects. {Eccentric Billionaire} still says "at announcement or when the cost is
  paid" while G00130 (same IDs + ANK 20230620) rules "at any point … from announcement
  to just before the cost is paid"; {Festivo dello Estinto}/{Inbase Discotek} retain
  the 2003 "from the blood bank" phrasing that G00121 [RTR 20180511] reconciles
  ("{Festivo dello Estinto} is not blood gained from the hunt" — the card prints the
  bank). Before reporting a contradiction between two records, check whether a group
  record consolidates them and whether the card text itself settles it.

- **LSJ Google Groups posts ARE often fetchable via WebFetch** (2026-07-22: the
  Annabelle Triabell original settled an owner-vs-DB conflict and exposed an inverted
  DB paraphrase). When a DB paraphrase is load-bearing and contested, fetch the
  original before adjudicating — do not stop at "archives are not practical".
- **Before minting a footnote label, grep both its inline and definition forms.**
  Definitions are ordered by first use, not numerically, so the highest label near an
  insertion point is not the highest in the family ([^1-2-15] existed far from
  [^1-2-14]; a new footnote briefly collided, 2026-07-22).
- **{Card} tokens must resolve under krcg.js's nameToImage slug** (leading "The"
  matters: {The Louvre, Paris}, not {Louvre, Paris}); braces are for card names only —
  cycle names stay unbraced. Sweep procedure in R-024.
- **KRCG `card_text` omits the burn-option icon.** The burn option is a separate JSON
  field (`burn_option: true/false`). {Legacy} (101085) looked stripped of its burn
  option in `card_text` and nearly produced a false "stale ruling" upstream filing for
  [LSJ 20091203]. Check the field before calling any burn-option ruling stale.
- **Crypt records are keyed by printing id, not by the name you'd look up.** The DB
  keys advanced printings under the plain name with the ADV id (`201326|Sundown` = G3
  ADV, `201422|Valerius Maior…` = G4 ADV, `200649|Ivan Krenyenko` = G2 ADV,
  `200758|Karsh` = G3 ADV), with [MERGED] tags where the ability is merged-only.
  Before filing "mis-stamped boilerplate" or "printing lacks this text" upstream,
  fetch the record's OWN id from KRCG — the Sundown force-abstain "mis-stamp" and the
  Valerius/Ivan "wrong printing" flags all changed shape on the id-level check
  (2026-07-21, phase8-inbox triage).

## Resolutions

### R-030 — tensions.md consistency sweep: run, adjudicated, applied  [SETTLED 2026-07-22]
**Position:** All five tension slugs verified consistent document-wide (four parallel
sweeps; mandatory-action-satisfaction = R-029 clean pass). Owner calls applied same day:
§1.6.3 placement-effect persistence tied to the printed duration clause with a §2.5.3
pointer (F-unlock-1); §1.6.3 "put … in play" bypasses requirements AND cost, card text
splitting the two checks at will (F-abn-1); §3.7.3.1 {Bloodstone} bypass-exemplar clause
DELETED (F-abn-2 — Bloodstone is a normal play with nothing to bypass; its equip-action
sentence stays); §3.7.4.2 WoKR bullet DELETED, [^3-7-4-4] re-keyed to G00131/{Zhenga}
(F-abn-3); §3.5.5 gains the "as if from your hand" arm (F-abn-4); 22 footnote repairs
applied (F-noeff-1..7, F-abn-5, F-abn-6) — [^5-5-7] clean-swapped to [RBK recruit-ally]
+ live IDs, superseded IDs dropped because the rulebook now prints the rule (contrast
R-028, where the deleted post was the rule's source). dedup-and-xref batch confirmed
adjudicated by the owner; its status line fixed. WORKING-NOTES item 4 closed;
tensions.md retained as history. Display change same day (owner): all linked reference
IDs double-bracketed so brackets render; footnote definitions blank-line-separated
(kramdown lazy-absorption fix); external links open in a new tab via card-links.js.
**Sources:** findings/no-effect-plays.md, findings/abnormal-entry.md,
findings/unlock-outlives-source.md; owner messages 2026-07-22.

### R-029 — Mandatory-action satisfaction: the mandating card decides (provides vs requires)  [SETTLED 2026-07-22]
**Position (owner-adjudicated 2026-07-20; consistency sweep clean 2026-07-22):** Whether
another action of the same type discharges a mandatory-action obligation is decided by
the MANDATING effect, never by the card used to satisfy it. (1) The card **provides**
the action ({Elen Kamjian}): the obligation is to that specific action — "Another bleed
action (eg. {Flurry of Action}) does not count as the bleed action her ability forces
her to take" [ANK 20211009-2]; original confirms ("No, she must bleed using the action
described in her cardtext"). (2) The card **requires an action of a type**
({Spirit Marionette}): any action of that type discharges it, including a card play —
"[OBE] The mandatory bleed can be performed by playing a card (eg. {Computer Hacking})"
[LSJ 20021121-2]. (3) Requires-with-alternatives ({Undying Thirst} [LSJ 20081213-2]):
either branch discharges. {Computer Hacking} vs {Flurry of Action} is NOT the variable.
Recurrence tracks the same split: provides → discharged once, no re-attach on unlock
({Cry Wolf}/{Lunatic Eruption}/{Elen Kamjian} [LSJ 20090226] [ANK 20200227]); requires →
keeps demanding while its condition holds ({Phillipe Rigaud} [ANK 20211010]). §3.9 owns;
sweep 2026-07-22 verified §3.9, §1.1.3, §1.15, §3.7.1.3, §3.7.2.3–.4, §3.7.8.4, §3.10.1,
§6.2.3 and both glossary entries consistent — zero findings. §3.9.2's "the action need
not succeed" is a synthesis from the rulings' uniform "performed" (rulebook usage:
resolved successful OR blocked) plus ANK 20211010's "performing the mandatory action
(provided by the card) once is enough" — inference, sound, do not re-flag without new
evidence.
**Sources:** rulings.yaml {Elen Kamjian}, {Spirit Marionette}, {Undying Thirst},
{Phillipe Rigaud}, {Cry Wolf}, {Lunatic Eruption}, {Change of Target} [LSJ 19980112],
{Mask of a Thousand Faces} [LSJ 20001113]; [RBK minion-phase]; originals fetched
2026-07-22: ANK 20211009-2/20211010 thread, ANK 20200227, LSJ 20090226.

### R-028 — §3.3.2 Archon Investigation timing: clean bill; [LSJ 20070203] re-added  [SETTLED 2026-07-22]
**Position (verified, owner-adjudicated):** the upstream deletion of [LSJ 20070203]
(commit 9f3b7ac, 2025-06-09) was a fold-into-card-text cleanup, not a retraction — the
current printing carries "after blocks are declined" verbatim, and no timing change
occurred (gist checked; late deadline stands on [LSJ 19980105], [LSJ 20050422],
[ANK 20180531]; implicit-decline survives via [LSJ 20000507] and fits [ANK 20211003]).
§3.3.2 stands as written. Record-key repairs applied: [^2-2-5] re-keyed to
{Archon Investigation}/{Lost in Translation}/G00106; [^1-2-14] gained {Major Boon};
[^3-3-8] re-keyed and, per owner call ("yes re-add"), carries [LSJ 20070203] again with
its live URL (https://groups.google.com/g/rec.games.trading-cards.jyhad/c/37EYK3FA30k/m/QynliahgIzQJ)
— relinked-phantom precedent, {Archon Investigation} kept as the historical record key.
WORKING-NOTES open item 3 is closed.
**Sources:** KRCG 100085 card text; rulings.yaml `100085|Archon Investigation`;
submodule history 9f3b7ac; originals fetched for [LSJ 20070203], [LSJ 20000507],
[ANK 20211003]; rules-change gist.

### R-027 — Review-file answers: four owner calls (2026-07-22)  [SETTLED]
**Position (owner-adjudicated 2026-07-22):**
(1) **Diablerie blood hunt** — no upstream question needed; the synthesis is complete:
the blood hunt is part of the action but *not* of its resolution — "immediately"
notwithstanding, an after-resolution window precedes it. §3.7.8.1/§2.3.4 unchanged.
review.md entry removed.
(2) **Two live "is considered" overrides, later lapses first** — the earlier override
resurfaces as governing; the underlying trait returns only when no override remains.
No ruling on record (VEKN forum searched 2026-07-22); owner call, stated footnote-less
in §5.9.2. review.md entry removed.
(3) **Torpor combat — REVERSAL of the 2026-07-22 "inverted paraphrase" finding.** That
finding misread the LSJ 20100604-1 thread: LSJ corrected himself downthread — "My
mistake. Neither can be used to enter combat with a non-ready minion." The
{Hidden Lurker}/{Blissful Agony} [VAL] paraphrases in rulings.yaml are CORRECT. No
combat-starting effect reaches a minion in torpor or on his way there; a queued combat
with a torpid combatant does not happen at all. §4.9.3/§5.3.1 re-corrected 2026-07-22;
nothing was ever filed upstream (verified against the issue/PR list), so nothing to
withdraw. CLAUDE.md gotcha rewritten (read the whole thread; directors self-correct).
review.md entry removed.
(4) **Edge steal vs mid-action burn — KEPT in review.md** (sole remaining entry).
Owner lean: RTR 19980623 likely says only that the holder cannot burn the Edge in
response out of nowhere; an effect that genuinely burns it mid-action should leave the
steal to fizzle per §3.4. Live mechanisms found: {Hand Intervention} ("may burn this
card by burning the Edge" — in-play ability, no timing restriction), {Sabbat Threat}
(burn the Edge to shed threat counters). §6.5.4 trimmed of "the stealer still gets it
at resolution, e.g. {Tereza Rostas}" down to the bare RTR sentence.
**Sources:** owner messages 2026-07-22; rulings.yaml @241a7e3 {Hidden Lurker},
{Blissful Agony}; LSJ 20100604-1 thread; KRCG {Hand Intervention}, {Sabbat Threat};
gh issue/PR list vtes-biased/vtes-rulings.

### R-026 — §5.2.2 Arika unlock-phase tax: end-of-phase model reversed  [SETTLED 2026-07-22]
**Adjudicated 2026-07-22 (owner): reversal confirmed** — the split-sentence edit is
applied to §5.2.2 ({Anarch Revolt} keeps the end-of-phase check on [^5-2-7]; the
resolves-once model carries the new [^5-2-30] → [ANK 20250121], per the owner's
"add a footnote to the reversal").
**Position (proposed, evidence firm):** [LSJ 19990405] (prey cannot end her unlock
phase controlling an un-paid-for location, even one gained mid-phase) is REVERSED —
Ankha, 21 Jan 2025 13:38, verbatim "This ruling is also REVERSED" [ANK 20250121].
Current rule: a "for each" unlock-phase effect resolves once, as a whole, over the
objects in play at that moment; objects acquired after it resolves are unaffected
until the next unlock phase ({Arika} locations, {Nightmares upon Nightmares} minions —
identical [REVERSAL] records). Conditional effects are expressly distinguished and
keep the end-of-phase check ({Anarch Revolt} [LSJ 20080106]; Ankha's NB in the same
post). §5.2.2's sentence states the reversed rule for its Arika half — split it;
exact edit in `findings/arika-5-2.md`. Same edit drops [ANK 20220503]/{Drink the
Blood of Ahriman} from [^5-2-7] (supports burn-choice freedom, not end-of-phase
checking; correctly cited at [^1-7-25], [^2-4-12], [^6-6-7]). New footnote label
[^5-2-30] (family max in use: [^5-2-29]).
**Sources:** [ANK 20250121]
https://www.vekn.net/forum/rules-questions/79080-nightmares-upon-nightmares?start=6#113567
(fetched 2026-07-22; also states the general doctrine '"For each ... do something"
should be resolved as a whole, and only once' and "effects in VTES cannot be
interrupted during resolution"); rulings.yaml `200135|Arika`,
`101285|Nightmares upon Nightmares`, `100055|Anarch Revolt`; {Arika} card text
(KRCG 200135); [ANK 20200629] (live, use-location-before-burning — currently
supports no document claim).

### R-025 — §3 owner review pass (2026-07-22)  [SETTLED]
**Position:** Fifteen owner items adjudicated and applied same day. The rules calls
and notable moves:
(a) **Style rule (binding): no reader injunctions.** "Read the card / the wording /
the possessive…" sentences are banned; state the rule declaratively. Nine instances
removed document-wide (§§1.7, 1.10.1, 3.1.2, 3.1.5, 3.3.3, 3.7.2.1, 3.7.3.1, 3.7.5.3,
4.6.3, 4.7.1, 6.6-influence). Recorded in CLAUDE.md style rules.
(b) **New unnumbered "Driving principles" section** after About this document
(owner-initiated): card text governs; you cannot do what you cannot do (barred in
part = no play, even to cycle); there is no stack; effects that apply, apply.
Pointer-based, no new footnotes.
(c) **{Incriminating Videotape}: the §3.1.1 sentence had the ruling's sense
inverted.** [TOM 19960114] [LSJ 20020514]: the choice made at play persists when the
equipment changes hands and binds against the NEW bearer ("the chosen minion is
unable to block the new possessor"). Now stated that way.
(d) **§3.4.2 recast — announcement vs resolution.** Terms are named at announcement
(§3.1.1); resolution supplies: choices the wording embeds in the effect rather than
the terms ({The Platinum Protocol} "chosen at action resolution (not declaration)"
[ANK 20240706] [LSJ 20080608]; {Break the Bonds} [obf] "chosen upon resolution"),
options exercised then ({Third Tradition: Progeny} [PIB 20150418]), states read then
({Dual Form} [ANK 20170226]). NOTE: owner's review note said "all choices must be
made at announcement" — the cited rulings place effect-embedded choices at
resolution; the recast preserves both and was flagged to the owner. §3.1.2 keeps the
declaration-vs-resolution split ({Break the Bonds} both levels).
(e) **{Veil of Darkness} stays in §3.4.1** (footnote [^3-4-8]): a card voided by a
standing "no effect" bar counts as played but produces no action — no lock, may
repeat, the same action included [LSJ 20090323]. The sentence now says explicitly
"this is not a cancellation"; the imprecise "nullified before the action begins"
phrasing is gone.
**History (e):** 2026-07-22 — first moved to §3.5.1 beside the canceled-action rule;
owner countermanded same day (it is not a cancellation, so it does not belong in the
cancel section) and it moved back with the precise wording kept.
(f) **Not-needed bar on {Mask of a Thousand Faces} is [OBF]-only** (R1126
[LSJ 20060409]); §3.2.1 now says "at [OBF]".
(g) **Unleash-intercept sentence removed** from §3.2.4 as card-specific
([ANK 20211112-2] dropped from [^3-2-6]).
(h) **Block-triggered burns precede every card and effect** — §3.3.3 extended with
{Truth of Blood} (prints "before block resolution"): its discard completes before the
blocker can play {Obedience}; §3.3.4/§2.4.4 own the general delayed-trigger rule.
(i) **Equip-target sameness: "if any one of them is the same"** ([ANK 20200502] — the
equipment tried before {Change of Target} cannot be among the second action's
targets); §3.5.2 aligned with §3.7.3.2.
(j) **Locquipment qualifications:** §3.7.3.2 "cannot be moved BY EFFECTS THAT MOVE
EQUIPMENT, though control can change"; §3.7.3.3 adds the Enkidu locquipment exception
pointing at §1.3.1.
(k) **Referendum pool-burn polling: sequencing does not lock the amounts** — give and
take, one blood at a time, waiting on the others ({Mob Rule} [LSJ 20030602]); §3.7.5.3
now says so.
(l) {Marciana Giovanni, Investigator} name fix was already applied in R-024 — the
owner reviewed a build predating it.
(m) **§4.9.1 ⚠ closed (owner reading of the rulings as they stand):** presses first;
then end of round and end of combat are ONE shared window (identical when no press is
taken and combat is about to end) whose occupants order freely, with a single fixed
point — a "would end" replacement precedes the window's "about to end" effects.
"After combat" effects sit outside, waiting for combat to actually end. The pairwise
rulings ([^4-9-2] [^4-9-5] [^4-9-6]) all fit this model; stated in §4.9.1 without a
marker. One ⚠ REVIEW remains in the document (§5.9.2 lapsed-override).
**Sources:** as cited per item; session transcript 2026-07-22.

### R-024 — §2 owner review pass (2026-07-22)  [SETTLED]
**Position:** Fourteen owner items adjudicated and applied to the document same day.
The binding rules calls:
(a) **As-announced stealth — ⚠ closed.** §1.6's bar on gaining stealth you do not
need DOES reach the as-announced window; every stealth card usable there prints its
own override ({Predator's Transformation} "+1 stealth, even if stealth is not yet
needed"). §2.2 states it; no marker.
(b) **The diablerie blood hunt IS part of the action, though independent of it** —
R0839's phrasing stands ([LSJ 20090722-2] [LSJ 20030618] under {Heidelberg Castle,
Germany}). It is not part of the RESOLUTION: an after-resolution window sits between
the diablerie and the referendum where effects may be played ([ANK 20201228]), but
that window is inside the action, so {Heidelberg} never fits; the referendum itself
takes no action modifiers or reaction cards [RBK the-blood-hunt]. The Abactor-type
referendum (called by the action's own text) is inside resolution — after-resolution
cards FOLLOW it — and the two cases stand as deliberate contrast in §2.3.4. The
convolution is flagged for upstream Rules Director review in docs/_work/review.md.
**History (b):** 2026-07-22 — owner first ruled "not part of the action at all" (§2
review pass); reversed later the same day on re-reading the Heidelberg ruling,
restoring R0839's model. §2.3.4 and §3.7.8.1 re-edited both times.
(c) **{Annabelle Triabell}: the pinned DB paraphrase is INVERTED.** Original
[LSJ 20030811] fetched from Google Groups 2026-07-22 — Q: "does it apply only to
toreadors in play at the moment the card is played?" LSJ: "Yes." The DB record
("applies to all Toreadors, not just the ones in play at the time the action
resolved", R2128) has the polarity backwards. Document now states the original: a
class-addressed effect applies to the members in play when it resolves. Upstream
defect, not yet filed (owner instruction needed).
(d) **[REACTION] ability markers belong to imbued powers** — {Hide}, {Surge},
{Vigilance}, {Champion} are all Power cards; §1.5.1 and §2.1.2 now say so explicitly.
(e) **Would/about-to precedence is a general template:** a replacement effect
("would X … instead") must be played while X is pending and cannot follow an effect
keyed to X happening ("about to"). Template in §1.2.3 (new [^1-2-16]), general form
§2.4.1, burn-replacement alignment §2.4.2; §4.9.1 keeps the combat-specific statement.
(f) **Between-actions and between-combats impulses reframed.** Between actions anyone
may use any non-action-bounded effect (R0841 [ANK 20210608]); §2.1.3 no longer frames
it as a property of "barred during an action" cards. Between queued combats the
after-resolution/after-combat windows stay shut, but the impulse serves other effects:
{Obedience} avoids the queued combat ([LSJ 19991025]), {Raptor}'s per-combat penalty
drops and re-applies ([LSJ 20030530]) — new [^2-3-13]. The combat a block causes IS
the blocked action's resolution (§2.3.3).
(g) **Oust-vs-burn: the general rule is "oust first among a resolution's
consequences"** (owner refinement, 2026-07-22): when one resolution yields an oust
along with other consequences, the oust resolves before the rest — the ally-last-life
mechanics ({Herald of Topheth}/{Bima} [LSJ 20080512]) are the instance, not the rule.
Verified against the original thread: LSJ's "you pay the cost of an action when the
action resolves" (no window between payment and resolution) is verbatim there, which
makes the burn, the pool loss and the oust one resolution bundle; the oust-first
clause itself was not found in the fetched portion of the thread and rests on the DB
paraphrase — unchallenged, and consistent with §6.5.2's cancel-cost case
([LSJ 20050607] [LSJ 20050608]). §2.4.3 leads with the general rule; {Bima} added to
[^2-4-17].
(h) **Unlock phase: only the MANDATORY effects must finish before passing** ({Fame}
[LSJ 20010121]; {Scourge of the Enochians} [ANK 20200508-1]); §2.4.5 now says
"the mandatory ones".
(i) Mask R1121 ("cannot be used during the resolution of an action") removed from
§2.1.3 — it is a window bound, not an atomicity fact; [LSJ 19980825] dropped from
[^2-1-4]. Smaller: {Rewind Time} example added (G00063); {Vagabond Mystic} phrasing;
{The Louvre, Paris} name fixed (body + footnote key form).
**Sweeps (same session):** all 1,048 unique {Card} tokens validated against krcg.js's
nameToImage slug (procedure: lowercase, move leading "the " to suffix, strip
punctuation/accents, HEAD static.krcg.org/card/<slug>.webp) — 2 real defects fixed
({Marciana Giovanni, Investigator}; the {Target} cycle mention unbraced). All 47
unlinked body [RBK …] refs linked ([RBK glossaries]→[RBK 8-glossaries] typo;
5-ending-the-game uses the page-URL form per existing convention).
**Sources:** as cited per item; session transcript 2026-07-22.

### R-023 — Phase-8 inbox triage (2026-07-21)  [SETTLED 2026-07-22]
**Outcome:** Owner approved E1–E6 verbatim; all applied to the document 2026-07-22.
The three countermands (Sundown, Legacy, The Becoming) stand. Upstream defects filed
as vtes-biased/vtes-rulings issue #9 + PR #10 (owner instruction) — reduced to the
Mokolé/Shilmulo typo and the Guardian Vigil [aus]→[cel] retag. Withdrawn: the two
"printing annotation" items (owner policy: ADV rulings sit on the ADV record) and the
Beast reword (owner ruling: equipment/ally/retainer/political cards are action-card
subtypes, so "as it is an action card" is correct — see General lessons for both). phase8-inbox.md deleted from docs/_work (queue fully processed; the
per-item record is findings/phase8-inbox.md).
**Position (proposed):** 35 items: 29 CLOSED (drafter resolutions verified in the
assembled document), 5 edit findings E1–E6 in `findings/phase8-inbox.md` (the
"(limited)" cap-holder split §1.2.1/§1.15 is the substantive one; plus §1.1.3 G00137
template, [^4-2-9] record key, Valerius/Karsh printing markers), 0 owner rules calls,
5 upstream defects (Mokolé Blood typo, Guardian Vigil [aus]→[cel], Valerius/Ivan
printing annotations, Beast wording). Three drafter upstream recommendations
countermanded on evidence (Sundown, Legacy, The Becoming — see General lessons and
the findings file). Hunt-bonus item was already settled by R-021(b). Lucian
strike-surcharge inference verified against [LSJ 20090529] {Jann Berger}/G00074 —
needs only the record-key fix, not an owner ruling.
**Sources:** findings/phase8-inbox.md; session report 2026-07-21.

### R-017 — Whole-document structural pass (2026-07-21)  [SETTLED]
**Position:** Sweep report in `findings/structural-pass.md`. Adjudicated and APPLIED
2026-07-21 (edits E1–E13 + two ⚠ closures, applied by coordinator, validated): the
three blocking tensions (now R-018/R-019/R-020), the title-faking consolidation
(F-struct-7), the §3.5.3 Yawp long-tail trim, and the two ⚠ closures (R-021). The
document now carries one genuinely-open ⚠ marker (§5.9.2 lapsed-override; the §2.2
as-announced-stealth marker was closed by owner ruling 2026-07-22 R-024, and the
§4.9.1 end-of-round full-order marker by owner ruling 2026-07-22 R-025 (m)). Batches applied 2026-07-21:
E1–E13 (blocking), E14–E21 (tensions; F-26 settled R-003; F-25 region model),
E22–E75 (placements P1–P4, clusters D1–D12), E76–E118 (long tail F-15, promises
F-29/F-30, style F-31). Pass COMPLETE: all 118 edits applied and validated
(document 4,858 → 4,804 lines); findings file stands as the record. Owner-recorded deliberate dual
statements (no change, do not re-report): immediate-vs-duration prevention
(§1.6.5/§4.5.1); {Repulsion} in §1.6.5/§3.2.3/§4.5.1. Ownership decisions of the
pass bind future drafting: named/announced cards §1.14; ousted-removal §6.5.3;
would-be-successful §3.4.3; block-burn §3.3.3; queued combat §4.9.3; range-setting
§4.2.1; lock-to-reduce §1.7.3; simultaneity §1.7.1 / oust-order §6.5.2; ally-acting
§5.5.4; unlock-to-block §3.3.1; leave-torpor diablerie §3.7.7.2; memory/suspension
§6.4.1 (capacity §5.1.1); referendum-ability states §3.7.6.4; periodicity templates
§1.2.1 ({Nahir}/{Nonu Dis}, {Owain Evans}); out-of-play weapon burns §1.14.3.
**Sources:** per findings file; key lookups quoted there.
**History:** 2026-07-21 — initial position was report-only/awaiting adjudication;
same day the owner adjudicated the blocking batch and the coordinator applied it.

### R-018 — Title-faking doctrine: where it lives and whose caps  [SETTLED]
**Position:** §5.8.3 is the single full statement (sect membership, made-up city,
per-card master-card reach); §1.6.4 keeps the general Mata-Hari template plus a
pointer line. The once-per-game caps (each requirement once; each title once; generic
"X votes" title once; a canceled-as-played card still spends the use) are {Vidal
Jarbeaux}'s printed text and rulings ONLY — never {Vlad Tepes} or {Kemintiri}.
Record keys: G00069 for the no-votes rule, G00070 for the dead-sect rule,
[LSJ 20050526] under {Mata Hari} for sect membership.
**Sources:** {Vidal Jarbeaux} card text ("only once each game"); [ANK 20211019]
[ANK 20200710] (Vidal); {Vlad Tepes} card text + record (no cap); [LSJ 20050721]
(Kemintiri, no master cards); G00069, G00070.

### R-019 — Referendum requires a *ready* acting minion at resolution  [SETTLED]
**Position:** The action ends and no referendum is conducted only if the acting
minion is *not ready* (torpor or out of play) when the action would resolve. "Locked"
is never the test — the acting minion is normally locked. §3.7.5.1 owns; §3.5.3
keeps the generic ends-if-not-ready sentence + link.
**Sources:** [LSJ 20060902] [ANK 20180910-1] [LSJ 20060903] — {Yawp Court}.

### R-020 — "Fizzle" is a defined term: successful and paid, but no effect  [SETTLED]
**Position:** A requirement-lapse mid-action fizzles the action: it still resolves
and, if unblocked, is successful and its cost paid, but has no effect. Defined once
in §1.6.1 (citing [ANK 20210124], {The Red Question}); §3.4.1, §3.7.3.1, §5.9.3 use
the term and link there. Target-lapse and requirement-lapse produce the SAME outcome;
the genuine contrast is the play-time requirement check, which bars the play itself.
Never frame fizzle as the action failing/ending.
**Sources:** [ANK 20210124] — {The Red Question}: "the action fizzles (is successful
but has no effect)".

### R-021 — Two ⚠ markers closed (canceled-play resource; hunt-bonus blood)  [SETTLED]
**Position:** (a) A canceled play spends a use iff the use attached to the play
itself ({Vidal Jarbeaux} [ANK 20200710]: canceled card was still played); it does not
if it attached to an element the cancellation removed ({Nergal} [LSJ 20091021-2]: no
cost paid → cost reduction never applied; §1.5.4's spent-only-if-it-applies rule).
(b) Hunt-amount bonuses take blood from wherever the hunt takes it (the target, for
steal-hunts: G00004/G00121 [RTR 20030519] [RTR 20180511]); a rider granting blood
"from the blood bank" ({Festivo dello Estinto}, {Inbase Discotek, Frankfurt} — both
print it) is a separate gain, not hunt blood ("{Festivo dello Estinto} is not blood
gained from the hunt", G00121). The per-card blood-bank copies are not a
contradiction.
**Sources:** as cited; G00121 record quoted in the findings file.

### R-022 — Section-architecture audit (whole document, 2026-07-21)  [RESOLVED 2026-07-21]
**Outcome:** Owner retired the pipeline (option a). The corrected document was committed
(70753f2), then `assemble.py`, `sections/`, and all other pipeline machinery were deleted
in the cleanup commit — `docs/advanced-rules.md` is now the sole source of truth, stated
in CLAUDE.md and WORKING-NOTES.md (both rewritten; the stale "drafting has not started"
premise is gone). `docs/_work/` now holds only the reference shelf: WORKING-NOTES,
owner-rulings, classification.tsv, rulings-flat.tsv, taxonomy, tensions,
phase8-inbox, phantom-id-audit, drafter-contract. Note-level items recorded as open
items in WORKING-NOTES (appendices A/B priority confirmed there). Same day, on owner
instruction, a separate pass changed the reference convention: one inline marker per
footnote, definitions consolidated into a single end-of-document `## References`
section, ruling IDs linked to their references.yaml URLs; a follow-up owner call then
removed the 11 unlinkable phantom citations and linked the 3 with live originals.
**Owner call (2026-07-21): cross-reference density is at its ceiling.** The proposed
§2.1.3 → §2.4.4 routing line was declined ("let's not add more cross-references, I
feel we have enough (too much?) already"). Do not propose additional navigational
cross-references without new evidence of a reader actually failing to find a rule.
**Position (proposed):** The 64-section, 6-chapter architecture is SOUND — no merge,
split, new-section or reordering recommendation cleared the evidence bar. G pile is 5
rows, all individually adjudicated; all four tension slugs landed inside existing
boundaries; the R-017 owner+pointer architecture is implemented consistently. Two
process findings instead: (a) **BLOCKING — `docs/_work/sections/*.md` is stale versus
the assembled `docs/advanced-rules.md`**: the R-017 edits (E1–E118) and all
footnote-verification fixes live only in the assembled file, while WORKING-NOTES still
declares `assemble.py` (which rebuilds from sections/) the source of truth — one
re-assembly silently reverts everything (verified: E5's "additionally caps each
requirement" is in advanced-rules.md, absent from sections/5.8.md). Owner must either
retire assemble.py/sections/ or back-port. (b) CLAUDE.md and the task pipeline's
self-description are stale ("drafting has not started beyond the two pilots") — this
mis-premised the audit itself. Note-level: §4.1.4 is a pointer-only numbered heading;
unlock-phase content split §2.4.5/§5.2.2 while other phases live in ch. 6 (cross-refs
cover it); §5.7.6 packs Scarce/Sterile/True Brujah/Flight into one unheaded paragraph
(Appendix A/B, still TODO, are the intended lookup path). Do not re-propose rejected
taxonomy candidates (Monocle question-cards, Extremis Boon auctions, events/Gehenna,
card-conferred status) absent new evidence.
**Sources:** docs/advanced-rules.md (full read, 4,804 lines); docs/_work/taxonomy.md;
coverage.tsv; review-findings.md structural unit; tensions.md; WORKING-NOTES.md;
sections/5.8.md grep.

### R-016 — X-cycle (§1.13 items + §§2.1–2.3 sweep, 2026-07-21)  [OPEN]
**Position:** X1: [LSJ 20080816] ({Descent into Darkness}) covers only effect-caused
departure ("If any card on the vampire was contested, it goes out of the contest until
the vampire comes back") — the contested-host case is NOT settled by it; sentence
narrowed to the ruling, exception flagged for owner sourcing. X2: §5.7 has no circles
content, so move §1.13.5 wholesale to a new §5.7.7 ([^1-13-12] → [^5-7-10]) and
cross-reference from §1.13.1. §2.3 markers: [^2-3-3] holds on [LSJ 20110502]
[LSJ 19980105]; [^2-3-6]'s ordering claim stands without the deleted {Voter Captivation}
ruling (flat R1987 recovered; drop [LSJ 20070327], no ⚠ REVIEW). Sweep found no new
blocking errors; coverage partial (see report).
**Sources:** per report.

All adjudications below: owner, 2026-07-21, relayed via coordinator message
(session: review-and-fix pass on §§1.1–1.3).

### R-001 — §1.2.1 "limit keyed to a phase is spent per window" (Nahir/Nonu Dis)  [SETTLED]
**Position:** Wrong as drafted. An ability whose use *costs a master phase action* is
spent per action (extra master phase actions buy extra uses: {Nahir}); an ability
*framed by a phase* is usable once per that phase however often its occasion recurs
({Nonu Dis}, once per master phase even with several master cards). §1.2.1 owns the
templates. The action-cost side is evidenced only in the master phase — word it as such;
the phase-framed side is general (unlock: {Owain Evans}; referendum: G00039/G00040).
**History:** 2026-07-21 — original position kept two synchronized copies (§1.2.1 and
§6.6.4); the structural pass's final batch trims §6.6.4 to a pointer (owner chose one
owner over two copies, E113).
**Sources:** [ANK 20191218] {Nahir}; [ANK 20220617] {Nonu Dis}; [LSJ 20040127]
{Owain Evans, The Wanderer}; §6.6.4 of the document.

### R-002 — Phantom reference IDs (flat-TSV vs pinned DB divergence)  [SETTLED]
**Position:** Fix only the three in-scope phantoms of §§1.1–1.3 ([LSJ 19980823],
[ANK 20210309-3]/G00031, [PIB 20121112]); the document-wide 35-ID audit is owned by a
separate parallel agent (report-only). See General lessons for the recovery procedure.
**Sources:** pinned `references.yaml`; upstream HEAD; `docs/_work/rulings-flat.tsv` (retired to git history 2026-07-22)
R1791, R2283, R2566.

### R-003 — §1.1.1: who uses an optional effect on a card in play  [SETTLED]
**Position:** The card's wording names the decider — "this vampire can" → the vampire's
current controller, even on a master card another Methuselah played and still controls
({Perfectionist}, {Corporal Reservoir}); "you may" → the card's controller. Never state
the flat form ("the minion's controller decides" or "the card's controller decides").
§1.1.1 states it; §6.6.3 and §6.2.5 (E19) align and link.
**Sources:** [ANK 20210309-3] original at
https://www.vekn.net/forum/rules-questions/79065-master-cards-attached-to-a-stolen-minion#101806
(record deleted upstream in e13882a); [RBK important-terms-of-the-game] (Control);
{The Rack} card text + [ANK 20200130-2].
**History:** 2026-07-21 — owner's first relayed wording (controller-of-the-card)
challenged same session by the recovered original ruling; owner then adjudicated
wording-decides, applied via E19. Upstream restoration of the deleted ruling still
recommended.

### R-004 — §1.1.1 "Only 'may' or 'can' is optional"  [SETTLED]
**Position:** Add "optional" as a third marker: "Only a clause the card marks as
optional — 'may', 'can', 'optional' — is optional." (The word "optional" is printed on
cards: {Renegade Garou}, G00096, G00024.)
**Sources:** {Renegade Garou} card text; groups "Optional press" (G00096), "Strikes with
optional maneuver" (G00024).

### R-005 — §1.2.2 "press or maneuver … only during the round"  [SETTLED]
**Position:** Keep "press or maneuver" (owner's authority). Evidence found supporting the
maneuver half: the per-card record of [TOM 19960521] for {Dust to Dust} read "The press
and maneuver can only be used during the current round"; the maneuver word was dropped in
the G00096 consolidation. Cite G00096 with a prose note pointing at the Dust to Dust
expansion. No ⚠ REVIEW.
**Sources:** [TOM 19960521] — group "Optional press" (G00096); flat TSV R0556; KRCG API
{Dust to Dust} ([THN] "with an optional maneuver").

### R-006 — §1.2.3 Anathema scope  [SETTLED]
**Position:** Say "fires on any loss in combat however caused" — the card and ruling are
combat-scoped.
**Sources:** [RTR 19980623] {Anathema}; card text "reduced to 0 in combat".

### R-007 — §1.3.2 Conrad Adoula anaphora  [SETTLED]
**Position:** Name the [REACTION]/[ACTION MODIFIER] pairing for Conrad; "such a card"
wrongly pointed at [COMBAT]/[ACTION MODIFIER].
**Sources:** [PIB 20150924-2] {Conrad Adoula}; card text.

### R-008 — §1.3.1 Enkidu "may still carry one"  [SETTLED]
**Position:** "may still equip with a locquipment" — matches the ruling's verb and fixes
the antecedent.
**Sources:** [LSJ 20050315] {Enkidu, The Noah}.

### R-009 — Footnote-grammar batch (F8–F10)  [SETTLED]
**Position:** Record keys must name the record the ruling is filed under (groups, not
member cards); strays removed ({Glaser Rounds}/[RTR 19941109] from 1-2-11; {Santaleous}/
[ANK 20200420-2] moves from 1-2-6 to 1-2-3; {Talbot's Chainsaw} from 1-1-2); group names
as in the DB (G00024 = "Strikes with optional maneuver"; keep the DB's "Immideate" typo
in G00154 — it is the lookup key); card name forms follow DB keys ({The Coven},
{The Ancestor's Talisman}).
**Sources:** groups.yaml/rulings.yaml record keys, verified this session.

### R-010 — [RBK important-terms-…] anchor  [SETTLED]
**Position:** The live anchor is `important-terms-of-the-game` (verified:
`id="important-terms-of-the-game"` on vekn.net/rulebook/3-playing-the-game; the "-in-"
variant does not exist there). Standardize on `-of-`. Seven occurrences document-wide;
only line 34 was in §§1.1–1.3 scope — the rest belong to the parallel audit.
`wording-templates` verified live. `action-card-or-card-in-play` is legitimate
(content.md "### Action Card (or Card in Play)").
**Sources:** live vekn.net HTML; rulebook2024/content.md lines 658/701/1184.

### R-011 — §1.6.2 "A clan requirement is met by that clan or its antitribu"  [OPEN]
**Position (proposed, evidence firm):** Wrong as a general rule. [ANK 20190203] covers
only cards that *print both clans* ({Defender of the Haven}, {Derange}, {Ennoia's
Theater}: "Only requires one clan or the other … to be played"). A Brujah antitribu does
not meet a Brujah requirement. Narrow to the printed-pair template. Baron→Anarch half
stands (G00037 [LSJ 20080603] [LSJ 20050128]).
**Sources:** [ANK 20190203] eight card records; G00037 "Require a Baron".

### R-012 — §1.6.5 no-effect plays: the three-family doctrine  [SETTLED]
**Position (owner-adjudicated 2026-07-20, relayed as settled in the 2026-07-22 sweep
direction):** Futility is no bar by default — a card may be played and an action taken
knowing it accomplishes nothing ({Absorb the Mind}, {Draba}/{Night Terrors} at 0,
{Siphon} empty target, {Kindred Segregation}/{Peace Treaty} no-subject referendum,
no-effect dodges, forced {Legacy of Caine} actions). Three families bar the play:
(a) missing named object ({Shattering Blow}, {Free States Rant} point-allocation,
{Brujah Frenzy}, {Taste of Vitae} vs allies, empty crypt G00126); (b) immediate damage
prevention with no damage (G00154) — duration-grant prevention exempt ({Apparition}
[LSJ 20010315], {Brother's Blood} [LSJ 20100527]); (c) unneeded stealth/intercept
({Bonding}) — reducing at the floor stays legal. The bar reaches only the play, and
only a play whose whole effect is the unneeded one ({Repulsion} [OBE] standing effect
unrestricted [LSJ 20011214-2]). Fixed points: {Blood Fury}/G00141 and
{Rigor Mortis}/G00137 "cannot" bars; {Spying Mission} zero-bleed [PIB 20150612];
{Veil of Darkness} no-lock (card-specific); {Deep Cover Agent} printed condition as
printed ([ANK 20240610] — DB-only per the one-card rule). §1.6.5 is the canonical home;
§3.2.1/§3.2.3, §4.5.1, §4.6.4 are its instances (R-017's deliberate dual statements
stand). Verified implemented across 14 units 2026-07-22 — doctrine clean; six footnote
repairs pending in findings/no-effect-plays.md.
**Sources:** as inline; per-record verification quoted in findings/no-effect-plays.md.
**History:** 2026-07-21 — opened as "§1.6.5 states the opposite of [LSJ 20011214-2]"
(the pre-rewrite text inverted the Repulsion ruling); the three-families rewrite was
applied and the owner adjudicated the doctrine; flipped SETTLED 2026-07-22.

### R-013 — Torpor and locked minions vs card plays (owner item U2)  [OPEN]
**Position (proposed):** Rulebook is explicit: "A vampire in torpor can perform no
action except the 'leave torpor' action and cannot block or play reaction cards. They
can play action modifiers during their actions." [RBK torpor]. Action modifiers have no
unlocked requirement even for non-acting minions ({Cloak the Gathering}, {Mouthpiece},
{Inspire Greatness} [LSJ 19980210] [RTR 19941109]); {Make an Example} — an *action
modifier*, not an ability — is usable locked [PIB 20150720] but not by a torpid
non-acting minion [RTR 19970306], matching "during their actions". {The Kiss of Ra} is
the torpid-acting-vampire example [LSJ 19970325]. The doc's "cannot act" also needs the
leave-torpor exception.
**Sources:** rulebook2024/content.md torpor passage; card types via KRCG
({Make an Example} = Action Modifier).

### R-014 — Owner items U1/U3/U5/U6/U8–U13 verified  [OPEN]
**Position:** All confirmed against sources with one pushback (U9: the DB ruling
literally says "He can pay for reactions after declining to block" [LSJ 19990421] — 
propose "played, and paid for," rather than dropping payment) and one refinement (U6:
made-up-city choice is general — {Vlad Tepes} too [PIB 20150306] [PIB 20150307]; only
the once-per-game cap is {Vidal Jarbeaux}'s own card text). U11's scope: the
simultaneity is between a card's play-cost (whatever card imposed it, e.g.
{Secure Haven} surcharge on {Minion Tap}) and that card's gain [LSJ 20020620].
**Sources:** per-item, see session report 2026-07-21 (§§1.4–1.7 review).

### R-015 — Owner items V1–V5 (§§1.7.5–1.8) verified  [OPEN]
**Position:** All five confirmed with evidence; proposed edits in session report
2026-07-21 (§§1.8–1.11 cycle). V1/V3/V4/V5 each promoted a general lesson (see above).
V2: the repay-to-keep rule is the printed "repaying their pool cost" template on
{Kindred Segregation}/{Peace Treaty}, read by [RTR 20010710] ("can be kept by paying
0 pool") — not a general truth about cost repayment. V5: {Masque of Judas} verified as
the maneuver-with-optional-press example ("[aus][obf] Maneuver with an optional press").
Sweep of §§1.9–1.11: clean at sampled depth; §1.8's only extra defect is [^1-8-3]'s
stray record ({Veil of Darkness} — the ruling lives under {Andrew Stuart} only).
**Sources:** per-item in the session report.
