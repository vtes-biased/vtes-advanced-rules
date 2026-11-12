# Rulemonger memory

Maintained by the rulemonger agent; adjudicated by the owner. This file — not any
conversation — is the agent's accumulated judgment. Two layers, maintained by
*promotion*: when a case teaches something general, the lesson moves up to General
lessons and the case entry stays thin, pointing at it.

**Supersession discipline (binding):** one entry per question, forever. A reversal or
refinement rewrites the entry's Position in place and records the old stance in its
History line. Never a second entry contradicting an earlier one. `SETTLED` entries are
binding on future sessions; challenging one requires a finding that names it
("challenges R-###") with new evidence, and only the owner flips it. R-numbers are
stable (other files cite them); a merged entry leaves a one-line pointer.

Entry format:

```
### R-001 — <one-line question>  [SETTLED | OPEN]
**Position:** <the binding answer, stated as the rule>
**Sources:** [LSJ 20061207], {Card} / group "Name" (G#####), [RBK anchor]
**History:** <only if the position ever changed: date, prior stance, what flipped it>
```

## General lessons

### Sources and verification

- **Fetch the original, and read all of it** (the {Annabelle Triabell} original exposed
  an inverted DB paraphrase, R-024(c); [ANK 20210124] reversed R-020). Rules Directors
  correct themselves downthread — LSJ 20100604-1's "My mistake. Neither can be used to
  enter combat with a non-ready minion." was missed once and produced a false
  inverted-paraphrase claim (R-027(3)). An RD post's embedded images are part of the
  ruling: Ankha's "Queued combats" FAQ (#114683) flow chart settles what its text leaves
  contradictory; HTML-to-text drops it — grep the post for `<img` (2026-11-09).
- **Cite only the archive, usenet.krcg.org** (`/t/<thread>/#mN`; BGG `/t/bgg-<id>/`;
  VEKN forum `/t/vekn-<thread>/`) — owner, 2026-11-11. Upstream refuses Google Groups and
  BGG links (0e06daf); relink a phantom by finding the RD's post in the archive (R-028).
- **The owner's rules-qa yields to a Rules Director ruling** (owner, 2026-11-11). Where
  no ruling settles a point, his call enters the document marked *(reading)*. Do not
  re-raise a rules-qa line against a ruled point (R-027(5)).
- **A wrong-citation finding requires a targeted `grep -A4 "|<Card>:"` coming back
  empty**, never a batch scan. Date IDs ([RTR 19951110]) are shared across unrelated
  cards, and a `head`-truncated batch produced a false wrong-citation on [^1-15-4]
  ({Scorn of Adonis} carries the ruling verbatim; 2026-07-21).
- **Resolve by id, not name.** ADV-only rulings sit on the ADV card's own record — that
  IS the printing marker (owner policy, 2026-07-22; e.g. `201422|Valerius Maior`,
  `200649|Ivan Krenyenko`, `201326|Sundown`, `200758|Karsh`, [MERGED] where merged-only).
  Do not propose "(advanced version only)" annotations or flag plain-name keys on ADV
  ids. Before filing "mis-stamped" or "printing lacks this text" upstream, fetch the
  record's own id: the Sundown, Valerius and Ivan flags all changed shape on that check.
- **KRCG `text` omits the burn-option icon** — check the `burn_option` field. {Legacy}
  nearly produced a false "stale ruling" filing for [LSJ 20091203].
- **An ID absent from the pinned DB is not a retraction.** Recover from submodule
  history (`git log -S "<string>" -- rulings/`), read the deletion commit, fetch the
  original from the pre-deletion `references.yaml`. Common cause: upstream deletes
  rulings a reprint folded into card text ({Extortion} [LSJ 20010725], {Pack Alpha}
  [LSJ 20051207], {White Lily} [LSJ 20080702-3]) or re-cites to a rulebook anchor ([RBK
  recruit-ally] for Piper/Summoning, upstream 1a49949). Then cite the card text,
  surviving group or anchor and drop the ID — except where the deleted post itself is
  the rule's source: relink it (R-028). G00031's deletion (e13882a, a bot commit
  mislabeled "Adding cards to group") looks accidental (R-003).
- **Group vs per-card records: check both directions.** Consolidation can drop a
  per-card specific (G00096 lost {Dust to Dust}'s "and maneuver", R-005); a per-card
  record can keep a wording the group corrects ({Eccentric Billionaire} vs G00130 "from
  announcement to just before the cost is paid"; {Festivo dello Estinto}'s "from the
  blood bank" vs G00121, R-021(b)). Before calling a claim over-broad or two records
  contradictory, read the group, the per-card history and the card text.
- **Group rulings keyed to member cards are a recurring footnote defect** ([^4-6-8]
  G00109, [^4-5-1] G00154, [^4-3-12] G00091, [^1-6-22] G00122; 2026-07-22). When one
  footnote shows it, grep every footnote citing the same IDs; fix per R-009. Merges
  carry old strays forward — check the pre-merge label before blaming the merge.
- **A *(reading)* claims "no official ruling" only after `content.md` and
  `rulings.yaml` (groups included) are searched.** Four reading sentences carried an
  official half (2026-11-10: G00130 + {The Line}, [RBK crypt-cards], [RBK
  6-vampire-sects]/[RBK other-vampire-sects], LSJ 20021008). Split: official part
  unmarked with its citation, marker on the remainder; the footnote still names its card
  or group.
- **RTR IDs carry the ruling's own date, else the publication date** (RTR 20180719 at a
  post titled 19-07-2018; RTR 20191031 a newsletter). Same-day ANK IDs: bare-then-`-2`
  and `-1`/`-2` are both conformant.
- **Quote the working tree; re-grep every residual-defect claim right before
  reporting** (2026-07-22: a quoted HEAD "defect" was already gone from the tree,
  R-030). Say which state a quote comes from when the tree is dirty.
- **Before minting a footnote label, grep inline and definition forms** — definitions
  are ordered by first use (a collision near [^1-2-14], 2026-07-22).
- **{Card} tokens must resolve under krcg.js's nameToImage slug** (leading "The":
  {The Louvre, Paris}); braces are for card names only — cycle names unbraced (R-024).

### Drafting and architecture

- **One rule, one home; silence elsewhere is intended** (owner-directed dedup pass,
  R-031; doctrine in CLAUDE.md, drafter contract, playbook). A section silent on a rule
  homed elsewhere, or carrying a bare "X is §Y's" pointer, is not a `gap`. Cross-reference
  density is at its ceiling (owner: "too much? already", R-022): no new navigational
  refs without evidence a reader failed to find a rule.
- **A cross-reference is a promise — read the target before deleting a local
  statement in its favor.** §1.13.5 said "§5.7 owns Blood Brothers" while §5.7 had no
  circles material.
- **Scope each general sentence to its evidence** (owner, 2026-07-21): evidence from one
  phase or context is worded as such (R-001); a rewrite must not silently narrow a
  genuinely general principle either. State the general rule only where exemplars from
  more than one context exist.
- **A coordinator relay of owner adjudications does not flip `Mode: FINDINGS-ONLY`:**
  deliver hunts, memory and ready-to-apply edit text; the document stays untouched.

### Rules doctrine (settled readings that recur)

- **Equipment, ally, retainer and political action cards are action cards** (owner,
  2026-07-22). {Beast, The Leatherface of Detroit}'s "cannot play action cards" reaches
  equipment, locquipment included ({Palatial Estate}); its ruling's stated reason is
  correct (the reword was reverted out of vtes-rulings PR #10). Do not re-flag.
- **Cost gates; triggered burn does not.** "Burn X blood *to attempt to block*"
  ({Tenebrous Form} [OBT], G00088) is a cost — an empty vampire cannot attempt; "any
  vampire attempting to block … burns 1 blood" ({Camarilla Exemplary}) is a consequence
  — it blocks and burns what it has. {Unleash Hell's Fury} states both [LSJ 19970707]
  [ANK 20230226]. Same discriminator as §1.7.4's burn-for-effect family.
- **Cancellation.** (1) Standing abilities pre-empt; card plays are answerable: an
  in-play cancel applies before responses ({Andrew Stuart} [LSJ 20100728]
  [LSJ 20090213]), a cancel that is a card play opens its own window ({Sudden Reversal}
  on {Direct Intervention}) — never "cancels resolve first" flat. (2) "As if from your
  hand" is a normal, cancelable play ({Persistent Echo}, {The Erciyes Fragments}
  [RTR 20040501], {Echo of Harmonies} [LSJ 20100426]). (3) It propagates downward only:
  canceling a strike cancels the card [RBK cancel-a-card]; canceling a maneuver cancels
  its press [ANK 20230114], never the strike that provided it [LSJ 20050228-3]
  [ANK 20230111] ({Rigor Mortis}). (4) A standing "no effect" bar is not a cancellation
  ({Veil of Darkness}, R-025(e)).
- **A delayed replacement is absent at the moment of play.** Play-tied effects resolve
  without it ({Troglodytia} [ANK 20180512]; {Agaitas} [LSJ 20020718] not at all);
  replacement-keyed effects wait ({Learjet} [PIB 20110718]). Delayed-replacement clauses
  govern normal plays only — special put-into-play replaces immediately ({Baseball Bat}
  [LSJ 20080702-2]).
- **At contest entry: enter-play effects resolve pre-contest, standing effects never
  apply** ({Mokolé Blood}, {Shilmulo Tarot} [ANK 20221028] [LSJ 20090428-1] — the
  incoming copy's own effect; {Elder Library} no hand-size change). §1.12.2 once misread
  Mokolé as moving cards to the other copy.
- **Cards under a departing host: the region model** (owner, 2026-07-21). Cards on a
  host burn when it leaves play — burned, removed, returned, or set aside without
  provision ({Raw Recruit} [LSJ 20100302-2]; {Memory's Fading Glimpse} [SFC 19960919]).
  Torpor, the uncontrolled region and contest are not departures: cards follow the host
  intact ([RBK contested-cards] burns stacked cards only on yield; {Lay Low}). A
  set-aside keeps them only by printing it ({Descent into Darkness} [LSJ 20080816]).
  "Out of play" is a status; the burn keys on the departure event (R-016).
- **Prevention: immediate vs duration-grant.** Immediate "prevent X damage" needs
  unresolved damage (G00154 "Immideate damage prevention", {Armor of Vitality});
  duration grants are playable with none ({Apparition} [LSJ 20010315], {Brother's Blood}
  [LSJ 20100527]); same shape as {Repulsion} [OBE] [LSJ 20011214-2]. Never state the
  prohibition flat (R-012).
- **Absolute values set; "+X" adds.** "Gets 1 vote" ({Legacy of Pander}), "strength of
  2" ({Torn Signpost}) set — copies do not stack, setting can reduce ({Rock Cat} [pot]
  [PIB 20130303]); "+X" adds to the set value [LSJ 20100813]. When a draft calls
  something an "exception", look for an unread template — votes never were one.

## Resolutions

### R-001 — Phase-keyed limits (Nahir/Nonu Dis)  [SETTLED 2026-07-21]
**Position:** An ability whose use *costs a master phase action* is spent per action
({Nahir}: extra MPAs buy extra uses) — evidenced in the master phase only, worded as
such. An ability *framed by a phase* is once per phase however often its occasion
recurs ({Nonu Dis}) — general (unlock {Owain Evans}; referendum G00039/G00040). §1.2.1
is the one home; §6.6.4 a pointer (owner, E113).
**Sources:** [ANK 20191218]; [ANK 20220617]; [LSJ 20040127].

### R-003 — Who uses an optional effect on a card in play  [SETTLED 2026-07-21]
**Position:** The wording names the decider: "this vampire can" → the vampire's current
controller, even on a master card another Methuselah controls ({Perfectionist},
{Corporal Reservoir}); "you may" → the card's controller. Never the flat form. §1.1.1
states it; §6.6.3/§6.2.5 align.
**Sources:** [ANK 20210309-3] original, https://usenet.krcg.org/t/vekn-79065/#m4
(deleted upstream e13882a; restoration filed as vtes-rulings issue #8); [RBK
important-terms-of-the-game]; {The Rack} + [ANK 20200130-2].
**History:** 2026-07-21 — owner's first relayed wording (card's controller decides)
challenged by the recovered original; owner then ruled wording-decides.

### R-004 — The optional markers  [SETTLED 2026-07-21]
**Position:** "may", "can" and printed "optional" ({Renegade Garou}, G00096, G00024).

### R-005 — "Press or maneuver … only during the round"  [SETTLED 2026-07-21]
**Position:** Keep "press or maneuver" (owner). G00096 dropped the maneuver half that
{Dust to Dust}'s per-card [TOM 19960521] carried; cite G00096 with a note on the
expansion. Not over-broad, no ⚠.

### R-006 — Anathema scope  [SETTLED 2026-07-21]
**Position:** Fires on any loss *in combat* however caused — card and ruling are
combat-scoped [RTR 19980623].

### R-009 — Footnote record keys  [SETTLED 2026-07-21]
**Position:** Key the record the ruling is filed under (the group, not member cards);
group and card names exactly as the DB keys them, typos included (G00154 "Immideate";
G00024 "Strikes with optional maneuver"; {The Coven}, {The Ancestor's Talisman}).

### R-010 — Rulebook anchor spelling  [SETTLED 2026-07-21]
**Position:** `important-terms-of-the-game` (not "-in-"), `wording-templates`,
`action-card-or-card-in-play` are all live.

### R-011 — Antitribu and clan requirements  [SETTLED 2026-07-22]
**Position:** A lone clan requirement is NOT met by the antitribu; only a card printing
the pair as alternatives needs one of the two ({Defender of the Haven}, {Derange},
{Ennoia's Theater} [ANK 20190203]). Baron→Anarch stands separately (G00037
[LSJ 20080603] [LSJ 20050128]). §1.6.2 and the glossary state the narrow template.

### R-012 — §1.6.5 no-effect plays: the three-family doctrine  [SETTLED]
**Position (owner, 2026-07-20; revised 2026-11-11):** Futility is no bar by default
({Absorb the Mind}, {Draba}/{Night Terrors} at 0, {Siphon} on an empty target, {Kindred
Segregation}/{Peace Treaty} with no subject, no-effect dodges, forced {Legacy of Caine}
actions). Three families bar the play: (a) missing named object ({Shattering Blow},
{Free States Rant} allocation, {Brujah Frenzy}, {Taste of Vitae} vs allies, empty crypt
G00126); (b) immediate prevention with no damage (G00154) — duration grants exempt; (c)
unneeded stealth/intercept ({Bonding}) — reducing at the floor stays legal. The bar
reaches only the play, and a card adding the unneeded value is barred even if it does
more ({Bonding} [DOM] [TOM 19951109]); standing effects ({Repulsion} [OBE]
[LSJ 20011214-2]) and random-outcome stealth ({Gathii} G00067 [ANK 20231031], the
stealth not gained) are usable. Fixed points: {Blood Fury}/G00141 and {Rigor
Mortis}/G00137 "cannot" bars; {Spying Mission} zero-bleed [PIB 20150612]; {Veil of
Darkness} no-lock (card-specific); {Deep Cover Agent} as printed ([ANK 20240610],
DB-only). §1.6.5 is home; §3.2.1/§3.2.3, §4.5.1, §4.6.4 are instances.
**Sources:** as inline; findings/no-effect-plays.md (git history).
**History:** 2026-11-11 owner: TOM 19951109 governs; the 'whole effect' wording withdrawn.

### R-013 — Torpor and locked minions vs card plays  [SETTLED 2026-07-22]
**Position:** A vampire in torpor performs no action but leaving torpor, cannot block or
play reactions, and plays action modifiers only on his own actions [RBK torpor] ({The
Kiss of Ra} [LSJ 19970325]; not {Make an Example} [RTR 19970306]). Action modifiers have
no unlocked requirement ({Cloak the Gathering} [LSJ 19980210] [RTR 19941109]; {Make an
Example} usable locked [PIB 20150720]). §5.3.2 owns.

### R-014 — §1.7 cost calls (U9, U11)  [SETTLED 2026-07-22]
**Position:** U9 — a fail-to-block cost burns at resolution start; reactions may still
be played and paid for before it [LSJ 19990421]. U11 — cost/gain simultaneity is
between a card's play-cost (whatever imposed it: {Secure Haven} on {Minion Tap}) and
that card's gain [LSJ 20020620].

### R-015 — Repay-to-keep  [SETTLED 2026-07-22]
**Position:** The printed "repaying their pool cost" template on {Kindred
Segregation}/{Peace Treaty}, read by [RTR 20010710] — not a general truth about cost
repayment.

### R-016 — Contest and hosted cards (X-cycle)  [SETTLED 2026-07-22]
**Position:** Governed by the region model (General lessons); [LSJ 20080816] covers only
an effect-caused departure of a contested card on a moved host (§1.13.3, {Descent into
Darkness}). [^2-3-3] holds on [LSJ 20110502] [LSJ 19980105]; [^2-3-6] stands without the
deleted {Voter Captivation} ruling.

### R-017 — Rule ownership map (structural pass, 2026-07-21)  [SETTLED]
**Position:** Homes that bind drafting: named/announced cards §1.14; ousted-removal
§6.5.3; would-be-successful §3.4.3; block-burn §3.3.3; queued combat §4.9.3;
range-setting §4.2.1; lock-to-reduce §1.7.3; simultaneity §1.7.1; oust-order §6.5.2
(incl. oust-first, R-024(g)); ally-acting §5.5.4; unlock-to-block §3.3.1; leave-torpor
diablerie §3.7.7.2; memory/suspension §6.4.1 (capacity §5.1.1); referendum-ability
states §3.7.6.4; periodicity templates §1.2.1; out-of-play weapon burns §1.14.3.
Deliberate dual statements (do not report): immediate-vs-duration prevention
(§1.6.5/§4.5.1); {Repulsion} (§1.6.5/§3.2.3/§4.5.1).
**Sources:** findings/structural-pass.md (git history).

### R-018 — Title-faking: home and caps  [SETTLED]
**Position:** §5.8.3 is the full statement (sect membership, made-up city, per-card
master-card reach); §1.6.4 keeps the Mata Hari template plus a pointer. The
once-per-game caps (each requirement once; each title once; generic "X votes" title
once; a canceled-as-played card still spends the use) are {Vidal Jarbeaux}'s text and
rulings ONLY — never {Vlad Tepes} or {Kemintiri}. Keys: G00069 no-votes, G00070
dead-sect, [LSJ 20050526] under {Mata Hari} for sect membership. A named-title ability
reaches only a closed list naming it, never an open one ({Karl Schrekt}: {Parity Shift}
yes, {Camarilla's Iron Fist} no) — owner 2026-11-11, over his rules-qa 59.14.
**Sources:** {Vidal Jarbeaux} text; [ANK 20211019] [ANK 20200710]; {Vlad Tepes} record;
[LSJ 20050721] (Kemintiri); [ANK 20250410] (Karl Schrekt).

### R-019 — Referendum requires a *ready* acting minion at resolution  [SETTLED]
**Position:** No referendum only if the acting minion is *not ready* (torpor or out of
play) when the action would resolve; "locked" is never the test. §3.7.5.1 owns.
**Sources:** [LSJ 20060902] [ANK 20180910-1] [LSJ 20060903] — {Yawp Court}.

### R-020 — "Fizzle" is a defined term: successful, no effect, and not paid  [SETTLED]
**Position:** An unblocked action whose target became illegal, or whose effect was
prevented, during the action fizzles: it resolves and is successful, but has no effect
and its cost is not paid. An action whose cost can no longer be paid in full at
resolution fizzles too, and the acting minion pays as much as possible. Defined in
§1.6.1; §1.7.5 owns the cost case; §3.4.1, §5.9.3, §6.2.2 use it. Never frame fizzle as
the action failing or ending.
**Sources:** [ANK 20210124] {The Red Question}, original post #101492: "If the action
fizzles because of 1/ or 2/, the action is not paid. If the action fizzles because of
3/, the acting minion must pay as much as possible".
**History:** 2026-11-10 — reversed on payment (was "successful and paid"), read from the
original; [PIB 20121031] ("must then be paid", original not located) superseded; the DB
paraphrases (G00078–G00081, {Harass}, {Sleep of Reason}) invert it — listed for an
upstream issue. Rules-qa 28.7/17.4 "fizzles paid" yielded, 2026-11-11 (R-027(5)).

### R-021 — Canceled-play resource; hunt-bonus blood  [SETTLED]
**Position:** (a) A canceled play spends a use iff the use attached to the play itself
({Vidal Jarbeaux} [ANK 20200710]); not if it attached to an element the cancellation
removed ({Nergal} [LSJ 20091021-2]; §1.5.4). (b) Hunt-amount bonuses take blood from
wherever the hunt does (the target, for steal-hunts: G00004/G00121 [RTR 20030519]
[RTR 20180511]); a "from the blood bank" rider ({Festivo dello Estinto}, {Inbase
Discotek, Frankfurt}) is a separate gain, not hunt blood (G00121). Not a contradiction.

### R-022 — Section architecture  [SETTLED 2026-07-21]
**Position:** The 64-section, 6-chapter architecture is sound. Do not re-propose the
rejected taxonomy candidates (Monocle question-cards, Extremis Boon auctions,
events/Gehenna, card-conferred status) absent new evidence.

### R-023 — Phase-8 inbox triage  [SETTLED 2026-07-22]
**Position:** "(limited)" cap-holder split: a limited bleed effect binds the action, a
limited additional strike binds the minion per round. Upstream: issue #9 + PR #10.

### R-024 — §2 owner review pass (2026-07-22)  [SETTLED]
**Position:** (a) §1.6's as-announced stealth bar reaches the as-announced window; every
stealth card usable there prints its override ({Predator's Transformation}). (b) The
diablerie blood hunt IS part of the action but not of its RESOLUTION: its window takes
diablerie-keyed cards only [ANK 20201228] [RTR 19991206], other after-resolution effects
follow it ({Freak Drive}, rules-qa 88.4); {Heidelberg} never fits; Abactor-type
referendums are inside resolution. (c) {Annabelle Triabell}: the pinned DB paraphrase is
INVERTED against [LSJ 20030811]; the document states the original (a class-addressed
effect applies to members in play when it resolves); filed as vtes-rulings issue #11.
(d) [REACTION] markers belong to imbued powers. (e) Would/about-to precedence is a
general template (§1.2.3, §2.4.1). (f) The between-actions impulse is general (R0841);
between queued combats the after-windows stay shut but other effects fit ({Obedience}
[LSJ 19991025]; {Raptor} [LSJ 20030530]). (g) Oust-first among a resolution's
consequences is general ({Herald of Topheth}/{Bima} [LSJ 20080512]); §6.5.2 owns it in
full. (h) Unlock phase: only MANDATORY effects must finish before passing ({Fame}
[LSJ 20110121]; upstream renamed the key 2026, the post is 2011).
**History:** 2026-07-22 — (b) first ruled "not part of the action at all"; reversed the
same day on re-reading the Heidelberg ruling. 2026-11-11 owner, rules-qa 88.4: (b)'s
window narrowed to diablerie-keyed cards (was every after-resolution effect).

### R-025 — §3 owner review pass (2026-07-22)  [SETTLED]
**Position:** (a) No reader injunctions; state rules declaratively. (b) Unnumbered
"Driving principles" section after About this document. (c) {Incriminating Videotape}:
the choice made at play binds against the NEW bearer [TOM 19960114] [LSJ 20020514].
(d) §3.4.2: terms at announcement; effect-embedded choices, options and state-reads at
resolution ({The Platinum Protocol} [ANK 20240706] [LSJ 20080608]; {Third Tradition:
Progeny} [PIB 20150418]; {Dual Form} [ANK 20170226]). (e) {Veil of Darkness} lives in
§3.4.1 — a standing "no effect" bar is NOT a cancellation [LSJ 20090323]. (f) Mask's
not-needed bar is [OBF]-only [LSJ 20060409]. (h) Block-triggered burns precede every
card and effect ({Truth of Blood} before {Obedience}). (i) Equip-target sameness: "if
any one of them is the same" [ANK 20200502]. (j) Locquipment cannot be moved by
equipment-moving effects, though control can change; Enkidu exception per §1.3.1.
(k) Referendum pool-burn polling: one blood at a time, amounts not locked ({Mob Rule}
[LSJ 20030602]) — the owner's rules-qa 51.5 yielded to it (2026-11-11).
(m) Presses first; end of round and end of combat are ONE shared window, freely
ordered, "would end" replacements before "about to end" effects; "after combat" waits
outside.

### R-026 — Unlock-phase "for each" effects: end-of-phase model reversed  [SETTLED 2026-07-22]
**Position:** [LSJ 19990405] is REVERSED by [ANK 20250121]. A "for each" unlock-phase
effect resolves once, as a whole, over the objects in play then; later arrivals wait for
the next unlock phase ({Arika} locations, {Nightmares upon Nightmares} minions).
Conditional effects keep the end-of-phase check ({Anarch Revolt} [LSJ 20080106]).
§5.2.2 states both halves ([^5-2-30]); the general "resolved as a whole, and only once"
doctrine is homed in §2.1.3 ([^2-1-8]). [ANK 20220503] is burn-choice freedom, not
end-of-phase checking — cited at [^1-7-25], [^2-4-12], [^6-6-7], not [^5-2-7].
**Sources:** https://usenet.krcg.org/t/vekn-79080/#m7

### R-027 — Review-file answers  [SETTLED]
**Position:** (1) **Diablerie blood hunt** — R-024(b). (2) **Two live "is considered"
overrides, later lapses first** — the earlier override governs again; the underlying
trait returns only when none remains. No ruling on record (forum searched); owner call,
footnote-less in §5.9.2. (3) **Torpor combat** — no combat-starting effect reaches a
minion in torpor or on his way there; a queued combat with a torpid combatant does not
happen. The {Hidden Lurker}/{Blissful Agony} [VAL] DB paraphrases are CORRECT
(LSJ 20100604-1, corrected downthread). (4) **Edge steal vs mid-action burn** — the
steal still gets the Edge (RTR 19980623 read literally, over TOM 19951214-2); §6.5.4
carries "the stealer still gets it at resolution". (5) **Rules-digest triage, closed
2026-11-11** — rules-qa yields to a ruling (General lessons). Ruling kept:
stealth/intercept reduction without a block attempt, the take as an equip action,
Bonding [DOM], the Parijat toll, Mask and inherent stealth, switching blockers, the
fizzle cost, the stealing hunt, Rötschreck, Target Vitals, Business Pressure, cards on a
removed minion, Life Boon, Unleash Hell's Fury. Card text or rulebook: Field Training,
the polling stage, 'put … in play' played. Readings: a hunt at full capacity, from-hand
'action requiring X', the diablerie window, Mask and the No Repeated Action rule, the
torpor burn option, a title contested by one's own vampires, a vote after casting.
**Sources:** owner messages 2026-07-22 and 2026-11-11; rules-qa 90.7; LSJ 20100604-1
thread; KRCG {Hand Intervention}, {Sabbat Threat}.
**History:** (3) 2026-07-22 — an earlier same-day finding called those paraphrases
inverted, reading only LSJ's first answer; reversed on the downthread correction. (4)
2026-07-22 — owner lean: a mid-action Edge burn makes the steal fizzle (§3.4), clause
trimmed; 2026-11-10 — restored on rules-qa 90.7 (2026-10-24).

### R-028 — Archon Investigation timing; [LSJ 20070203] re-added  [SETTLED 2026-07-22]
**Position:** Upstream's deletion of [LSJ 20070203] (9f3b7ac) folded it into card text
("after blocks are declined"); no timing change. §3.3.2 stands (late deadline:
[LSJ 19980105] [LSJ 20050422] [ANK 20180531]; implicit decline: [LSJ 20000507],
[ANK 20211003]). [^3-3-8] carries [LSJ 20070203] again with its live URL (owner: "yes
re-add") — relinked-phantom precedent, {Archon Investigation} as historical key.
**Sources:** https://usenet.krcg.org/t/37EYK3FA30k/#m2 (LSJ, 3 Feb 2007)

### R-029 — Mandatory-action satisfaction: the mandating card decides  [SETTLED 2026-07-22]
**Position (owner, 2026-07-20):** The MANDATING effect decides, never the satisfying
card. (1) It **provides** the action ({Elen Kamjian}): only that action counts — "Another
bleed action (eg. {Flurry of Action}) does not count" [ANK 20211009-2]. (2) It
**requires an action of a type** ({Spirit Marionette}): any such action, card plays
included ({Computer Hacking} [LSJ 20021121-2]). (3) Alternatives ({Undying Thirst}
[LSJ 20081213-2]): either branch. Recurrence follows the split: provides → discharged
once, no re-attach on unlock ({Cry Wolf}/{Lunatic Eruption}/{Elen Kamjian}
[LSJ 20090226] [ANK 20200227]); requires → keeps demanding while its condition holds
({Phillipe Rigaud} [ANK 20211010]). §3.9 owns. §3.9.2's "the action need not succeed"
is sound inference from the rulings' uniform "performed" plus ANK 20211010's "once is
enough" — do not re-flag without new evidence.
**Sources:** originals fetched 2026-07-22 (ANK 20211009-2/20211010, ANK 20200227, LSJ
20090226); {Change of Target} [LSJ 19980112]; {Mask of a Thousand Faces} [LSJ 20001113].

### R-030 — tensions.md consistency sweep  [SETTLED 2026-07-22]
**Position:** Consistent; applied. Deliberate deletions (do not re-add): §3.7.3.1's
{Bloodstone} bypass clause, §3.7.4.2's {Web of Knives Recruit} bullet.

### R-031 — Atomicity/deduplication pass  [SETTLED 2026-07-22]
**Position:** Applied document-wide (ID census 1,133 unchanged; Appendix A's
template-to-section entries are structural, exempt). Its silences and bare pointers are
intended, not `gap`. Deferred, not new findings: 26 cited pointer sentences flagged
DELETE (need per-case marker rehoming); 10 same-paragraph double-citations.

### R-032 — "Inflicted" vs "successfully inflicted"  [SETTLED 2026-11-12]
**Position (owner, 2026-11-12):** "Inflicted" = not dodged; prevented (and immunized) damage counts; "(even if
prevented)" is reminder text. "Successfully inflicted" = not dodged, not prevented, not ignored — on every card printing
it. Older cards printing plain "inflicts" that an LSJ ruling reads as "successfully" keep the ruling until reprinted
({Twisting the Knife} LSJ 20010627/20020215, {Blade Clot} LSJ 20080820); LSJ 20040802's general statement describes
that older wording. Without a ruling the text applies ({Haymaker}, *(reading)*, open in review.md). Home §4.5.5.
**Sources:** [RBK damage-resolution]; LSJ 20020215 (FArran2SmSQ #m1); ANK 20171226 (vekn-76349 #m8); ANK 20210324
(vekn-79087 #m12, #m15).

R-002, R-007, R-008: deleted 2026-11-10 (completed work; lessons absorbed above).
