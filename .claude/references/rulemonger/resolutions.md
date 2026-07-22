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
- **The drafting corpus diverges from the pinned database.** `docs/_work/rulings-flat.tsv`
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
document now carries three genuinely-open ⚠ markers (§2.2 as-announced stealth,
§4.9.1 end-of-round full order, §5.9.2 lapsed-override). Batches applied 2026-07-21:
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
in the cleanup commit — `docs/extended-rules.md` is now the sole source of truth, stated
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
the assembled `docs/extended-rules.md`**: the R-017 edits (E1–E118) and all
footnote-verification fixes live only in the assembled file, while WORKING-NOTES still
declares `assemble.py` (which rebuilds from sections/) the source of truth — one
re-assembly silently reverts everything (verified: E5's "additionally caps each
requirement" is in extended-rules.md, absent from sections/5.8.md). Owner must either
retire assemble.py/sections/ or back-port. (b) CLAUDE.md and the task pipeline's
self-description are stale ("drafting has not started beyond the two pilots") — this
mis-premised the audit itself. Note-level: §4.1.4 is a pointer-only numbered heading;
unlock-phase content split §2.4.5/§5.2.2 while other phases live in ch. 6 (cross-refs
cover it); §5.7.6 packs Scarce/Sterile/True Brujah/Flight into one unheaded paragraph
(Appendix A/B, still TODO, are the intended lookup path). Do not re-propose rejected
taxonomy candidates (Monocle question-cards, Extremis Boon auctions, events/Gehenna,
card-conferred status) absent new evidence.
**Sources:** docs/extended-rules.md (full read, 4,804 lines); docs/_work/taxonomy.md;
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
**Sources:** pinned `references.yaml`; upstream HEAD; `docs/_work/rulings-flat.tsv`
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

### R-012 — §1.6.5 {Repulsion} [OBE] sentence states the opposite of its ruling  [OPEN]
**Position (proposed, evidence firm):** [LSJ 20011214-2]: "[OBE] **Can** be used even if
the stealth is not currently needed." The document said "cannot be played when the
stealth is not needed". The correct rule is the duration-grant escape (see General
lessons). Rewrite §1.6.5 with three families + the immediate/duration split.
**Sources:** {Repulsion} card text ([OBE] puts card in play, standing +1 stealth);
[LSJ 20011214-2]; [LSJ 20010315] {Apparition}; [LSJ 20100527] {Brother's Blood}.

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
