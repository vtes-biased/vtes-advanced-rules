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
  G2 ADV, `201326|Sundown` = G3 ADV, `200758|Karsh` = G3 ADV — [MERGED] tags where
  the ability is merged-only). Keys use the printed name; the id disambiguates. Do not
  propose "(advanced version only)" annotations in ruling text and do not flag
  plain-name keys on ADV ids as defects. Name-based lookups being ambiguous is by
  design — resolve by id: before filing "mis-stamped boilerplate" or "printing lacks
  this text" upstream, fetch the record's OWN id from KRCG — the Sundown, Valerius and
  Ivan flags all changed shape on the id-level check (2026-07-21, phase8-inbox triage).
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
  The same applies when upstream re-cites a rule to a rulebook anchor
  ([RBK recruit-ally] replacing [LSJ 20080630] [RTR 20180303] on the Piper/Summoning
  cannot-act rule, upstream 1a49949): cite the anchor, drop the superseded IDs (R-030);
  keep or relink a deleted ID only where the deleted post itself was the rule's source
  (R-028).
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
- **Read the whole thread — Rules Directors correct themselves downthread.**
  LSJ 20100604-1's later "My mistake. Neither can be used to enter combat with a
  non-ready minion." superseded his first answer; reading only the first answer
  produced a wrong inverted-paraphrase claim against the database (owner-corrected
  2026-07-22, R-027(3)).
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
- **Quote the working tree, and re-grep every residual-defect claim immediately
  before reporting (2026-07-22).** The adjudication queue's Q2/Q3 items quoted
  content and line numbers that matched HEAD while the working tree had moved on —
  Q3's "residual defect" (§3.9.3 meta-commentary) had already been deleted by the
  owner's own polish pass. When the tree is dirty, state which state a quote comes
  from.

## Resolutions

### R-031 — Atomicity/deduplication pass: one rule, one home; cross-refs culled  [SETTLED 2026-07-22]
**Position:** Owner-directed document-wide pass, applied 2026-07-22. Doctrine (now in
CLAUDE.md, drafter-contract, playbook): every rule has exactly one normative home — the
section a judge would look it up in first; the default toward other sections' rules is
silence; a `§` pointer survives only where its absence risks a wrong ruling. Executed:
766 shared-citation footnote pairs classified (57 DUP / 109 PARTIAL), 104 clusters
resolved — duplicate statements deleted or trimmed to minimal-premise-plus-pointer, 41
footnotes retired (714 → 673) with all orphaned ruling IDs and example cards folded into
the home definitions (ID census 1,133 before and after — nothing lost). Then a 463-entry
cross-reference audit against the misreading test: 185 navigation refs removed
(§-refs 554 → 353; Appendix A's 163 template-to-section entries are structural and
exempt). Do not re-report the resulting deliberate gaps as `gap` findings: a section
silent on a rule whose home is elsewhere, or carrying a bare ownership pointer
("X is §Y's"), is the intended architecture. Residuals deliberately left: 26 cited
pointer sentences (pointer + own footnote) flagged DELETE by the audit but deferred —
removing them needs per-case marker rehoming; 10 same-paragraph double-citations noted
as citation hygiene. Both lists reproducible from the sweep recipe below.
**Sources:** session scratchpad sweep (pairmap/clusters/refcull), owner approval of the
batch-1 calibration and blanket delegation for the rest, 2026-07-22.

### R-030 — tensions.md consistency sweep: run, adjudicated, applied  [SETTLED 2026-07-22]
**Position:** All five tension slugs verified consistent document-wide; every finding
of the no-effect-plays, abnormal-entry, unlock-outlives-source and dedup-and-xref
sweeps was owner-adjudicated and applied 2026-07-22. Notable calls: §3.7.3.1's
{Bloodstone} bypass clause and §3.7.4.2's {Web of Knives Recruit} bullet DELETED;
[^5-5-7] clean-swapped to [RBK recruit-ally] (superseded IDs dropped — the rulebook
now prints the rule; contrast R-028). WORKING-NOTES item 4 closed; tensions.md
retained as history. Display conventions changed same day (owner) — recorded in the
playbook's footnote grammar. Q3 residual (the §3.9.3 "states this in one sentence"
meta-commentary, X1's pattern): MOOT — the owner's own polish pass had deleted it
before adjudication (2026-07-22).
**Sources:** findings files (git history); owner messages 2026-07-22.

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
keeps demanding while its condition holds ({Phillipe Rigaud} [ANK 20211010]). §3.9 owns; consistency sweep 2026-07-22 clean
document-wide. §3.9.2's "the action need
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
**Position:** [LSJ 19990405] is REVERSED — [ANK 20250121], verbatim "This ruling is
also REVERSED". A "for each" unlock-phase effect resolves once, as a whole, over the
objects in play at that moment; objects acquired after it resolves are unaffected
until the next unlock phase ({Arika} locations, {Nightmares upon Nightmares} minions
— identical [REVERSAL] records). Conditional effects keep the end-of-phase check
({Anarch Revolt} [LSJ 20080106]; Ankha's NB in the same post). §5.2.2 states both
halves; the reversal carries [^5-2-30] → [ANK 20250121] (owner: "add a footnote to
the reversal"); [ANK 20220503]/{Drink the Blood of Ahriman} dropped from [^5-2-7]
(burn-choice freedom, not end-of-phase checking; correctly cited at [^1-7-25],
[^2-4-12], [^6-6-7]). The post's general doctrine — '"For each ... do something"
should be resolved as a whole, and only once'; effects cannot be interrupted during
resolution unless a card prints the exception — is stated in §2.1.3
(owner-approved 2026-07-22 in variant placement: proposed for §2.4, but §2.1.3's
atomicity paragraph was the one normative home), carrying [^2-1-8] → [ANK 20250121]
under {Nightmares upon Nightmares}, {Arika}.
**Sources:** [ANK 20250121]
https://www.vekn.net/forum/rules-questions/79080-nightmares-upon-nightmares?start=6#113567;
rulings.yaml `200135|Arika`, `101285|Nightmares upon Nightmares`, `100055|Anarch
Revolt`; findings/arika-5-2.md (git history).

### R-025 — §3 owner review pass (2026-07-22)  [SETTLED]
**Position:** Fifteen owner items adjudicated and applied same day. Binding residue:
(a) style rule — no reader injunctions; state rules declaratively (playbook
conventions; CLAUDE.md). (b) Unnumbered "Driving principles" section after About
this document. (c) {Incriminating Videotape}: the choice made at play persists and
binds against the NEW bearer [TOM 19960114] [LSJ 20020514]. (d) §3.4.2
announcement-vs-resolution: terms at announcement; effect-embedded choices, options
and state-reads at resolution ({The Platinum Protocol} [ANK 20240706]
[LSJ 20080608]; {Third Tradition: Progeny} [PIB 20150418]; {Dual Form}
[ANK 20170226]). (e) {Veil of Darkness} lives in §3.4.1 — a standing "no effect" bar
is NOT a cancellation [LSJ 20090323]. (f) Mask's not-needed bar is [OBF]-only
[LSJ 20060409]. (h) Block-triggered burns precede every card and effect ({Truth of
Blood} completes before {Obedience}). (i) Equip-target sameness: same "if any one of
them is the same" [ANK 20200502]. (j) Locquipment: cannot be moved by effects that
move equipment, though control can change; Enkidu exception per §1.3.1.
(k) Referendum pool-burn polling: one blood at a time, amounts not locked
({Mob Rule} [LSJ 20030602]). (m) §4.9.1 ⚠ closed: presses first; end of round and
end of combat are ONE shared window, freely ordered, "would end" replacements
preceding "about to end" effects; "after combat" waits outside.
**Sources:** as cited per item; session transcript 2026-07-22.
**History (e):** 2026-07-22 — first moved to §3.5.1; owner countermanded same day
(not a cancellation), moved back with the precise wording kept.

### R-024 — §2 owner review pass (2026-07-22)  [SETTLED]
**Position:** Fourteen owner items adjudicated and applied same day. Binding residue:
(a) as-announced stealth ⚠ closed: §1.6's bar reaches the as-announced window; every
stealth card usable there prints its own override ({Predator's Transformation}).
(b) The diablerie blood hunt IS part of the action, though independent of it, and
not part of the RESOLUTION: an after-resolution window precedes the referendum
[ANK 20201228], inside the action, so {Heidelberg} never fits; Abactor-type
referendums are inside resolution — deliberate contrast in §2.3.4. (c) {Annabelle
Triabell}: the pinned DB paraphrase is INVERTED against the original [LSJ 20030811];
the document states the original (a class-addressed effect applies to the members in
play when it resolves). Filed upstream 2026-07-22 as vtes-biased/vtes-rulings
issue #11. (d) [REACTION] ability markers belong to imbued powers (§1.5.1, §2.1.2).
(e) Would/about-to precedence is a general template (§1.2.3, §2.4.1). (f)
Between-actions impulse is general (R0841); between queued combats the after-windows
stay shut but other effects fit ({Obedience} [LSJ 19991025]; {Raptor}
[LSJ 20030530]). (g) Oust-first among a resolution's consequences is the general rule
({Herald of Topheth}/{Bima} [LSJ 20080512] the instance). (h) Unlock phase: only the
MANDATORY effects must finish before passing ({Fame} [LSJ 20010121]). Sweeps same
session: all 1,048 {Card} tokens validated against the krcg.js slug (2 fixes); all
47 body [RBK] refs linked.
**Sources:** as cited per item; session transcript 2026-07-22.
**History:** 2026-07-22 — (b) owner first ruled "not part of the action at all";
reversed later the same day on re-reading the Heidelberg ruling. 2026-07-22 (later)
— (g) placement superseded by the dedup pass (D13, owner-adjudicated): §6.5.2 owns
oust-first in full; §2.4.3's restatement and [^2-4-17] were removed. The rule itself
is unchanged.

### R-023 — Phase-8 inbox triage (2026-07-21)  [SETTLED 2026-07-22]
**Position:** 35 items: 29 closed as already implemented; 5 edits E1–E6
owner-approved verbatim and applied 2026-07-22 (substantive one: the "(limited)"
cap-holder split — a limited bleed effect binds the action, a limited additional
strike binds the minion per round). Three drafter upstream claims countermanded on
evidence (Sundown, Legacy, The Becoming — General lessons); the two
printing-annotation items and the Beast reword withdrawn (owner policy/ruling —
General lessons). Upstream defects reduced to the Mokolé/Shilmulo typo and the
Guardian Vigil [aus]→[cel] retag, filed as issue #9 + PR #10.
**Sources:** findings/phase8-inbox.md (git history); session reports 2026-07-21/22.

### R-017 — Whole-document structural pass (2026-07-21)  [SETTLED]
**Position:** All 118 edits of the pass applied and validated; findings record in
findings/structural-pass.md (git history). Binding residue — ownership decisions
bind future drafting: named/announced cards §1.14; ousted-removal §6.5.3;
would-be-successful §3.4.3; block-burn §3.3.3; queued combat §4.9.3; range-setting
§4.2.1; lock-to-reduce §1.7.3; simultaneity §1.7.1 / oust-order §6.5.2; ally-acting
§5.5.4; unlock-to-block §3.3.1; leave-torpor diablerie §3.7.7.2; memory/suspension
§6.4.1 (capacity §5.1.1); referendum-ability states §3.7.6.4; periodicity templates
§1.2.1; out-of-play weapon burns §1.14.3. Owner-recorded deliberate dual statements
(do not re-report): immediate-vs-duration prevention (§1.6.5/§4.5.1); {Repulsion}
(§1.6.5/§3.2.3/§4.5.1). The three blocking tensions became R-018/R-019/R-020; the
two ⚠ closures R-021. No ⚠ REVIEW markers remain document-wide (last, §5.9.2,
closed by R-027(2)).
**Sources:** findings/structural-pass.md (git history).
**History:** 2026-07-21 — report-only at first; owner adjudicated and the
coordinator applied the batches the same day.

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
**Sources:** as cited; G00121 record quoted in the findings file (git history).

### R-022 — Section-architecture audit (whole document, 2026-07-21)  [SETTLED 2026-07-21]
**Position:** The 64-section, 6-chapter architecture is SOUND — no merge, split,
new-section or reordering recommendation cleared the evidence bar. Owner retired the
generation pipeline (commit 70753f2 + cleanup); docs/advanced-rules.md is the sole
source of truth (CLAUDE.md/WORKING-NOTES rewritten). Binding: cross-reference
density is at its ceiling (owner: "let's not add more … too much? already") — no new
navigational cross-references without evidence of a reader failing to find a rule;
do not re-propose the rejected taxonomy candidates (Monocle question-cards, Extremis
Boon auctions, events/Gehenna, card-conferred status) absent new evidence. Same day
the reference convention moved to a single end-of-document `## References` section
with linked ruling IDs; 11 unlinkable phantom citations removed, 3 relinked.
**Sources:** session record 2026-07-21.

### R-016 — X-cycle (§1.13 items + §§2.1–2.3 sweep, 2026-07-21)  [SETTLED 2026-07-22]
**Position:** X1 — cards on a host that itself enters contest are governed by the
owner's region model (General lessons): contest is not a departure, cards stay with
the host intact, [RBK contested-cards] burns stacked cards only on yield;
[LSJ 20080816] covers only the effect-caused departure of a contested card on a
moved host, and §1.13.3 states exactly that ({Descent into Darkness}). X2 — §1.13.5
moved to §5.7.7 ([^1-13-12] → [^5-7-10]), verified holding. §2.3 markers resolved:
[^2-3-3] holds on [LSJ 20110502] [LSJ 19980105]; [^2-3-6] stands without the
deleted {Voter Captivation} ruling.
**Sources:** [RBK contested-cards]; rulings.yaml {Descent into Darkness}; document
§1.13.3/§6.4.1/Appendix.
**History:** OPEN 2026-07-21 (X1 flagged for owner sourcing); settled 2026-07-22 —
the owner's region model, adjudicated the same day X1 was filed, answers it.

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
wording-decides, applied via E19. Upstream restoration of the deleted ruling
recommended; filed 2026-07-21 as vtes-biased/vtes-rulings issue #8.

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

### R-011 — §1.6.2 "A clan requirement is met by that clan or its antitribu"  [SETTLED 2026-07-22]
**Position:** Wrong as a general rule, and no longer in the document: a lone clan
requirement is NOT met by the antitribu clan; only a card printing the pair as
alternatives needs just one of the two ({Defender of the Haven}, {Derange},
{Ennoia's Theater} [ANK 20190203]). The Baron→Anarch half stands separately (G00037
[LSJ 20080603] [LSJ 20050128]). §1.6.2 and the Appendix state the narrow template.
**Sources:** [ANK 20190203] eight card records; G00037 "Require a Baron"; document
§1.6.2 + glossary, [^1-6-6].
**History:** OPEN 2026-07-21 (narrowing proposed); settled 2026-07-22 — the
owner-adjudicated document states the narrowed template.

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
stand). Verified implemented across 14 units 2026-07-22 — doctrine clean; the six
footnote repairs applied via R-030.
**Sources:** as inline; per-record verification quoted in findings/no-effect-plays.md
(git history).
**History:** 2026-07-21 — opened as "§1.6.5 states the opposite of [LSJ 20011214-2]"
(the pre-rewrite text inverted the Repulsion ruling); the three-families rewrite was
applied and the owner adjudicated the doctrine; flipped SETTLED 2026-07-22.

### R-013 — Torpor and locked minions vs card plays (owner item U2)  [SETTLED 2026-07-22]
**Position:** Per the rulebook: a vampire in torpor can perform no action except
leave torpor, cannot block or play reaction cards, and plays action modifiers during
his own actions only [RBK torpor] — {The Kiss of Ra} on the leave-torpor action
[LSJ 19970325]; not {Make an Example} during another minion's action
[RTR 19970306]. Action modifiers have no unlocked requirement even for non-acting
minions ({Cloak the Gathering} [LSJ 19980210] [RTR 19941109]); {Make an Example} is
an action modifier, not an ability, usable locked [PIB 20150720]. §5.3.2 owns and
states it.
**Sources:** rulebook2024/content.md torpor passage; KRCG {Make an Example};
document §5.3.2.
**History:** OPEN 2026-07-21; settled 2026-07-22 on document verification.

### R-014 — Owner items U1/U3/U5/U6/U8–U13 (§§1.4–1.7)  [SETTLED 2026-07-22]
**Position:** Verification batch, all items applied to the document. Standing calls:
U9 — a cost charged for failing to block burns at resolution start; reactions may
still be *played, and paid for,* before that burn ([LSJ 19990421]; §1.7 states it
verbatim). U11 — the cost/gain simultaneity is between a card's play-cost (whatever
card imposed it, e.g. {Secure Haven} surcharge on {Minion Tap}) and that card's gain
[LSJ 20020620]. U6's refinement (made-up-city is general; only the caps are Vidal's)
became R-018.
**Sources:** as cited inline; document §1.7.
**History:** OPEN 2026-07-21 (proposed edits pending); settled 2026-07-22 on
document verification.

### R-015 — Owner items V1–V5 (§§1.7.5–1.8)  [SETTLED 2026-07-22]
**Position:** Verification batch, all items applied; the reusable lessons (V1/V3/
V4/V5) live in General lessons. V2: repay-to-keep is the printed "repaying their
pool cost" template on {Kindred Segregation}/{Peace Treaty}, read by [RTR 20010710]
— not a general truth about cost repayment. [^1-8-3]'s stray {Veil of Darkness} key
removed (the ruling lives under {Andrew Stuart} only).
**Sources:** as cited inline; document §1.8, [^1-8-3].
**History:** OPEN 2026-07-21; settled 2026-07-22 on document verification.
