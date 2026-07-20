# Phase 4.5 — section review findings

68 opus reviewers (64 sections, 3 C-pile shards, 1 structural), 525 findings.

**Read the caveat in WORKING-NOTES before triaging by severity.** Every unit
returned `coherent-with-issues` and none returned zero findings, so the volume is
inflated and the severity labels are not reliable for triage. The *content* was
spot-verified as largely sound; the calibration was not.

Machine-readable: `review-findings.json`.

## structural

### [high] scope-drift

Q1 ANSWERED — 3.7.4 is not two sections, it is three topics under one code, and only the smallest of them is the employ/recruit action. Cluster A (13 rulings, one ANK 20180517 wording template): a minion that 'cannot act the turn recruited' may still USE its abilities, including lock-to-use abilities — R0247, R0535, R0566, R0766, R0773, R1501, R1521, R1777, R1944 verbatim, plus R1922/R2001/R0285/R0014 as variants. This is 1.5's principle (ability use is not an action) with a 5.2 lock cross-ref; notably NONE of the 13 carries 1.5 as a code, only three carry 5.2. Cluster B (6): whether a minion entering play may ACT that turn — R0928, R1243, R1313, R1767, R1761, R0978. 5.5's scope line already says 'allies acting'. Cluster C (17, the largest and most general): a card effect that puts an ally/retainer into play is NOT an employ/recruit action, so action-keyed cost reductions (R1314, R2521), stealth modifiers (R2017, currently stranded in the G pile), cancellation of a played card (R1317, R2520), the NRA (R1315, R1207, R1765) and the action's requirements/costs (R1766, R1761) all fail to attach — while non-action-keyed reductions and abilities DO attach (R1688, R2151, R2300, R2522, R1044). Cluster D (8, the actual action): R0948, R1206, R1779, R1998, R2127, R2155, R2305, R2600, R0762. 3.7.4's scope line ('recruitment specifics, acting the turn recruited') names A and B and never names C at all, which is why 44 rulings piled into a sub-sub-section.

**Recommendation:** Confirm the standing hypothesis: SCOPE-LINE SPLIT, no new code. The seam is between the ACTION (C+D) and the MINION STATE (A+B). (1) 3.7.4 keeps C+D and gets scope words for C, which it currently lacks: 'employ/recruit actions; and entry into play by a card effect rather than by the action — action-keyed effects (cost reductions naming an action, stealth modifiers, cancel-a-played-card, the NRA) do not attach to non-action entry, while effects keyed to the recruiting minion do. Cross-ref 1.6 for requirements under abnormal entry.' Re-home R2017 here. (2) Cluster B moves to 5.5/5.6, whose scope lines already claim allies acting and retainer employ/bearer; drop 'acting the turn recruited' from 3.7.4's scope line. (3) Cluster A's principle moves to 1.5 with a 5.2 cross-ref. No reclassification of the 44 is required if the drafter is told the seam — the codes stay, the scope lines and the section boundary change.

*Rulings (45):* R0014, R0247, R0285, R0535, R0566, R0766, R0773, R1501, R1521, R1777, R1922, R1944, R2001, R0928, R1243, R1313, R1767, R1761, R0978, R0405, R1044, R1207, R1314, R1315, R1316, R1317, R1688, R1765, R1766, R1778, R2151, R2300, R2520, R2521, R2522, R2017, R0762, R0948, R1206, R1779, R1998, R2127, R2155, R2305, R2600

### [high] duplicate-template

Q5 ANSWERED — no-effect-plays is not one adjudicable question. It is three, and its size is an artifact of merging them. (a) PERMISSIVE DEFAULT: a card may be played, or an action taken, knowing it will accomplish nothing — R0533, R2087, R1459, R0269, R0018, R0936, R0986, R1637, R1296, and the combat-vocabulary instances R1368, R1545, R1612, R1971, R1805, R1814. (b) NAMED-OBJECT PROHIBITION: a card whose text names an object it acts on cannot be played when no such object exists — R0170, R0195, R0205, R0224, R0280, R0730, R1623, R0458, R1487, R0737, R1815, R0251, R0254, R0233, and the eight-copy prevention template R0774, R0833, R0856, R1634, R1646, R1647, R1671, R1736. (c) SUCCESS WITHOUT EFFECT: whether a no-effect action still resolves successfully and still locks the actor — R0228, R0278, R0714, R0735, R1715, R1023, and the genuine outlier R1958 ({Veil of Darkness}, a no-effect action that does NOT lock). (a) and (b) do not contradict each other: they are the two sides of one rule whose deciding distinction is 'a requirement to play' versus 'mere futility' — i.e. 1.6, not 1.1, even though 20 of the 46 were filed 1.1 first. (c) is a different question entirely and is 3.4's own scope line. Separately, the standalone `prevention-without-damage` slug (R0065 vs R0082) is the SAME adjudication as (b)'s prevention template and is currently being resolved in isolation from its eight sibling rulings.

**Recommendation:** Split the slug into three files before drafting: no-effect-permissive, no-effect-required-object, and no-effect-success (the last is 3.4's, not a tension). Merge `prevention-without-damage` (R0065, R0082) into the required-object file with R0774/R0833/R0856/R1634/R1646/R1647/R1671/R1736 — ten rulings, one template, one answer. Sections that must agree before any of them is drafted: 1.6 (requirement-to-play — the deciding section, and the one that should own the a/b boundary), 3.4 (success vs. effect — owns (c)), 1.1 (card-text 'cannot' as absolute — currently over-claiming this pile), 4.5 (prevention requires damage), 4.6 (dodge that accomplishes nothing), 4.3, 3.2, and 1.8. Note that 1.8 is ALREADY DRAFTED and reviewed and states nothing about no-effect plays — it is the natural owner of the permissive default, so adopting (a) there means a light edit to reviewed text, which is the user's call, not the drafter's.

*Rulings (47):* R0533, R2087, R1459, R0269, R0018, R0936, R0986, R1637, R1296, R1368, R1545, R1612, R1971, R1805, R1814, R0170, R0195, R0205, R0224, R0280, R0730, R1623, R0458, R1487, R0737, R1815, R0251, R0254, R0233, R0774, R0833, R0856, R1634, R1646, R1647, R1671, R1736, R0065, R0082, R0228, R0278, R0714, R0735, R1715, R1958, R1023, R0465

### [medium] over-absorbed

Q1, second defect — the single largest cross-chunk over-absorption in the unit. Thirteen rulings sharing one wording ('He/she can lock to use his/her ability the turn he/she is recruited', nine of them verbatim, most citing the same [ANK 20180517] blanket ruling) were each absorbed as P or E across seven chunks. No classifier could see the other twelve. Under the no-exhaustive-card-lists rule this is one principle plus at most three 'e.g.' cards; the other ten are database material. Two of the thirteen were even labelled P (R1501, R1521), so a drafter reading the extract will find the same sentence offered as a general principle twice on two unremarkable ally cards.

**Recommendation:** Keep one P (R1501 or R1521) and two variants that show the principle is not confined to 'lock to use' — R1922 (burn a life for a press) and R2001 ({War Ghoul} lock-and-burn) — and re-role the remaining ten to C with the note 'duplicate of the ANK 20180517 acting-the-turn-recruited template'. Do this as an explicit drafter instruction in the 3.7.4 extract rather than silently, so the count drop is traceable. R0014 and R0285 are not duplicates (werewolf burn, diablerie trigger) and should be judged on their own.

*Rulings (13):* R0247, R0535, R0566, R0766, R0773, R1501, R1521, R1777, R1944, R1922, R2001, R0285, R0014

### [medium] thin-section

Q2 ANSWERED — 6.8 should be dropped, not folded into 6.6. Two independent facts kill it. First, 6.8 appears exactly once in the whole 2,605-ruling classification output, and even on that one row it is the SECOND code: R2544 is labelled `1.6,6.8`, so no ruling in the corpus names 6.8 as its primary. Second, R2544's text — 'the other Gehenna cards in play requirement is only checked when playing the card' — is a verbatim instance of 1.6's scope line (requirements to play vs. requirements to keep) with Gehenna as the incidental subject; it teaches nothing about events or Gehenna as a mechanic. The 'events' half of the scope line is worse off than the Gehenna half: grepping the flat corpus for the event card type returns zero rulings. The only other Gehenna-mentioning rulings are R0477 (a {Delaying Tactics} retrieval question) and R1236 (a capacity comparison), neither of which is about event or Gehenna mechanics.

**Recommendation:** Delete code 6.8. R2544 is already correctly coded 1.6 and needs no reclassification — it becomes a 1.6 example. Do not fold into 6.6: nothing in R2544 concerns the master phase, and moving it there would import a requirements-timing rule into a phase-structure section. If the finished document needs to say anything about events or Gehenna at all, it is one cross-referenced sentence in 1.6, not a heading. Renumber 6.9 to 6.8 or leave the gap, at the user's preference — the taxonomy is a routing key, not the table of contents.

*Rulings (3):* R2544, R0477, R1236

### [medium] misfiled

Q4, first half — five of the ten G survivors are not homeless any more; they are stale labels written against the pre-expansion taxonomy and never revisited. R1733, R1734 and R1985 all carry notes that explicitly cite 'sect as a trait (watch-list)' as their missing topic — but that watch-list item was PROMOTED to 5.9 and deliberately rescoped from sect to traits generally on 2026-07-20. 5.9's scope line now claims exactly what they teach: 'traits as things effects read and write... whether a changed trait counts as the trait for other cards' requirements and triggers'. R1733 ({Stolen Police Cruiser} equippable by a non-Anarch, effect suppressed) and R1985 ({Vivienne Géroux} is not Anarch for {Anarch Manifesto}) are trait-as-a-gate; R1734 (equipping it is not 'an action requiring an Anarch') is trait-keyed effect matching. This matters more than the count suggests: coverage.tsv shows 5.9 at 24 P against only 4 E — the section is starved of examples, and these are three. R2017 is homed by the 3.7.4 scope widening recommended above. R2483 ({Vidal Jarbeaux}.8) is not a live gap either: the taxonomy already adjudicated it as a watch-list item with the verdict 'Still a single instance after the full corpus. Do not create; 1.6 is nearest' — that decision has simply not been written back to the row.

**Recommendation:** Re-code R1733, R1734 and R1985 to 5.9 with roles E (R1733 keeps 1.6 and R1734 keeps 3.7.3 as secondaries). Re-code R2017 to 3.7.4/E once the scope line claims non-action entry. Re-code R2483 to 1.6/E per the taxonomy's own recorded verdict, and strike it from the watch list so it is not re-proposed a third time. This takes the G pile from 10 to 5 with no new sections and no judgment calls beyond ones already made.

*Rulings (5):* R1733, R1734, R1985, R2017, R2483

### [low] recoverable-C

Q4, second half — the mirror defect the question asks about is present, in one clear case and two marginal ones. R1930 ({Unity}.1, 'you can cut however you want') has the exact Phase 3 defect: its own note concedes 'rare mechanic, nothing in the taxonomy claims deck-cutting procedure', which is the homeless-alone reasoning the taxonomy's own lesson names — G requires general AND homeless. It fails the transfer test outright: no other card in the corpus makes a Methuselah cut a library, so it changes how you would rule on nothing. It is C. R2069 ({Platinum Protocol}.2, placing a corruption counter gives no opportunity to steal it) is marginal: it can be stated generally as 'a counter placed on a minion is not equipment and is not stealable', but that fails non-obviousness for a judge fluent in the rules, and if it is kept its nearest owner is 1.12 (counters on hosts), not the 4.10 its note names — 4.10 is about stealing equipment in combat, not about what counts as stealable. R0161 ({Blade Clot}.1) is now half-resolved: the stacking half is owned by 1.15 as its note says, and the residue ('rescue by an older vampire burns all clot counters') is a single-card mechanic, so the row should stop being G. As for clustering: no, the survivors do not form an ownable topic. R0122 (apply modifiers before an inherent floor) and R2468 (a discipline-choice card counts as the discipline it was played as) are the two genuine general singletons, and they are unrelated to each other and to everything else in the pile.

**Recommendation:** Re-role R1930 to C with a transfer-test note. Re-role R0161 to C on the residue, since 1.15 already carries its general half. For R2069, either re-role to C on non-obviousness or move the near-miss code from 4.10 to 1.12 — do not leave it pointing at 4.10. Handle R0122 and R2468 as scope-line widenings rather than sections, matching the 2026-07-20 pattern: 1.7 (or 1.2) gains 'modifier arithmetic against an inherent floor or minimum — apply modifiers first, then the floor' and 1.3 gains 'cards printed with a discipline choice count as the discipline they were played as, for all purposes'. Neither justifies a code.

*Rulings (3):* R1930, R2069, R0161

## 1.1

### [high] duplicate-template

Thirty of the 55 rows are verbatim or near-verbatim recurrences of ten wording templates, each carrying the same ruling reference across cards from different chunks; the section as filed reads as ~11 distinct principles inflated to 55 entries.

**Recommendation:** Collapse each cluster to one principle plus at most three "e.g." cards and return the rest to the database. The clusters, keyed by shared reference: (1) "The effect is not optional" [RTR 19980707]/[LSJ 19980722] — R0003, R0058, R0325, R0588, R2041; keep {Aaron's Feeding Razor} and {Enchanted Marionette}. (2) "The opponent cannot play [for] prevention cards (eg. for cycling)" [LSJ 20050628] — R0195, R0205, R0224, R0458, R1680; keep {Blood Fury} plus R1487 {Rigor Mortis} as the non-prevention variant of the same rule, drop the other four. (3) "Cannot be used if there is no damage to prevent" [LSJ 20001114] — R0774, R0833, R0856; keep R0856 {Hidden Strength} (it adds "X cannot be negative"). (4) "Cannot be used if there is no equipment to steal/destroy" [RTR 19980928] — R0170, R0280, R0730, and R0251 on the same reference; keep one. (5) "Can be played against a vampire with no blood" [RTR 20010711] — R0018, R0269; keep one. (6) "Paying for the equipment found is not optional… she is ousted" [RTR 19941109]/[RTR 20010710] — R1458, R1953; keep one. (7) "The cost to rescue from torpor is reduced even if paid by the rescuee. This is not optional." [LSJ 20020304-2] — R2213, R2353; keep one. (8) "The vampire need not attempt to block nor play further reaction cards: that is merely an option" [TOM 19951129] — R0627, R0708, R1993; keep one (all three are secondary, so one cross-reference suffices). (9) "does not force the minion to strike with it" [LSJ 19971215] — R0226, R0258; keep one. (10) mandatory effects must be applied before passing the opportunity to play effects [LSJ 20100723] — R0414, R2376; keep one. Cluster (1) is additionally all-P: only the consolidated statement should be P, the survivors are E.

*Rulings (30):* R0003, R0058, R0325, R0588, R2041, R0195, R0205, R0224, R0458, R1680, R0774, R0833, R0856, R0170, R0280, R0730, R0251, R0018, R0269, R1458, R1953, R2213, R2353, R0627, R0708, R1993, R0226, R0258, R0414, R2376

### [high] misfiled

Three rulings about discharging a mandatory ACTION obligation are filed in 1.1, two of them as PRIMARY, but 3.9 was created specifically to own them and names these exact cases in its scope line.

**Recommendation:** Reassign R1066 ({Lunatic Eruption}.2, "If the minion it is on has entered combat and unlocks, he is free to take any other action") and R2393 ({Phillipe Rigaud}.1, "he is not 'stuck', he is free to take any other legal action") to 3.9 as PRIMARY, keeping 1.1 as secondary at most; R2394 ("as long as there is an opportunity for diablerie, he must attempt it, even if he did so already and unlocked") likewise. The taxonomy's 3.9 rationale cites discharge ({Cry Wolf}.2) and the stuck-and-cannot-act outcome ({Change of Target}.8, {Elen Kamjian}.3) as its two named sub-topics — R1066 and R2393 are further instances of exactly those, and 3.9 is a 7-ruling section that cannot afford to lose them. 1.1 owns mandatory EFFECTS ("the effect is not optional", "the press is mandatory"); it does not own mandatory ACTIONS.

*Rulings (3):* R1066, R2393, R2394

### [medium] scope-drift

The membership contains two topics with a clean seam: mandatory-vs-optional effects (the section's stated core) and a second, larger cluster on whether a card may be played when it has no valid target or no effect — a topic 1.1's scope line does not name and which contains an unresolved internal contradiction.

**Recommendation:** Decide the seam before drafting. On one side of it: "cannot be played if there is nothing to act on" (R0170, R0251, R0254, R0280, R0730, R0737, R0774, R0833, R0856, R0233, R0465). On the other: "may be played even though it will do nothing" (R0018, R0269, R0986, R1023). The prevention-cycling cluster (R0195 et al., R1487) sits with the first group. As written these two polarities would make a drafter write contradictory sentences — this is the `no-effect-plays` tension the contract anticipates, and no ruling here states the discriminator (target-selection requirement vs. effect futility). Either give 1.1 an explicit second sub-heading with that discriminator stated, or move the whole no-target cluster to 1.6 (requirements to play) and leave 1.1 with mandatory/optional and card-text reading. Do not draft it as one undifferentiated section.

*Rulings (17):* R0170, R0233, R0251, R0254, R0280, R0465, R0730, R0737, R0774, R0833, R0856, R0018, R0269, R0986, R1023, R0195, R1487

### [medium] over-absorbed

Three rulings are P/E in 1.1 but are pure single-card text interpretations that fail the transfer test — they change how you rule on no other card.

**Recommendation:** Re-role to C. R1973 {Victim of Habit}.1: "You can lock the card to remove less than three copies, but then the prey does not burn pool" — the whole content is the lock/three-copies/burn arithmetic printed on that one card. R1294 {Path of Death and the Soul}.2: "If you fail to find a Discipline card, you still get the blood" — reads the independence of two clauses on one card; the general form ("clauses are independent unless conditioned") is true, generic and useless, exactly the {Great Symposium}.1 failure mode the contract names. R0465 {Deep Cover Agent}.2: "The burn option can only be used if you do not control a ready Seraph (no matter the presence or absence of a valid target)" — names a specific card's specific gating condition; keep it only if the drafter needs a third "e.g." for the no-effect cluster, otherwise C.

*Rulings (3):* R1973, R1294, R0465

### [medium] missing-topic

1.1's scope line leads with "card text overriding rulebook" and "'cannot' absolute", but not one ruling in the membership states either rule; the section's headline principle has no supporting material.

**Recommendation:** Warn the drafter that the card-text-trumps-rules principle and the specific-over-general reading rule will have to be written from the rulebook with no ruling footnote behind them, or cited to [RBK] anchors. The nearest things present are indirect: R0195's cluster ("cannot" blocks even a no-effect play for cycling) and R1026 ({Legacy of Caine}.4, "cannot gain blood" redirects hunt blood to the bank) — both are consequences of "cannot" being absolute rather than statements of it. Only R0146 ({Big Game}.1, "that minion" vs. "this minion") is genuinely about reading card text, and one ruling will not carry a sub-topic.

### [low] misfiled

R1087 {Major Boon}.2 is PRIMARY in 1.1 but its principle is that pool loss from a card effect is not a bleed, which belongs to bleed/pool.

**Recommendation:** Move to 3.7.1 (bleed) or 6.5 (pool loss distinctions) as PRIMARY; 1.1 has no claim on the card-effect-vs-bleed distinction. Its sibling R1088 {Major Boon}.3 ("after the first is burned, 'you' are no longer the Methuselah burning pool") is a genuine card-text-reading ruling and should stay, ideally with a 1.15 cross-reference since it also decides whether multiple copies stack.

*Rulings (1):* R1087

## 1.10

### [high] duplicate-template

R0159 ({The Black Throne}.1) and R1374 ({Provision of the Silsila}.1) are the SAME ruling text under the SAME reference [PIB 20150512], differing only by a typo ("or" vs "of"): "Can be used even if the target is burned or if the contract is burned when the target leaves the ready region (eg. {Priority Contract})." Two chunks transcribed the same contract-card boilerplate independently.

**Recommendation:** Collapse to one entry. Keep R0159 as the single "e.g." ({The Black Throne}); drop R1374 to the rulings database. Note that neither is PRIMARY here — the principle (a contract effect survives the burn of its target or of itself) is persistence-of-effect material, so the merged entry belongs primarily in 2.5 with 1.10 as the cross-reference it already is.

*Rulings (2):* R0159, R1374

### [medium] misfiled

R1481 ({Riddle Phantastique}.1) and R1558 ({Secret Horde}.1) are filed P/PRIMARY in 1.10, but 1.12's scope line claims this exact case in these exact words: "counter-count conventions on entry (a card entering with X=0 counters burns immediately) and burn thresholds keyed to another value (eg. vandal counters vs. a location's blood cost)". The classifiers matched the surface word "burns" rather than the principle (golden rule 3). R2184 ({Dominique}.1, the vandal-counter/blood-cost case) is the second half of that same scope line and is correctly here only as secondary — which shows the intended routing.

**Recommendation:** Move R1481 and R1558 to 1.12 as PRIMARY, demoting 1.10 to secondary (or dropping it — 1.10 owns what a burn *does*, not what triggers one). Leave R2184 as is. This also removes the counter-driven self-burn cluster, which is the only place 1.10's membership reads as a second topic.

*Rulings (3):* R1481, R1558, R2184

### [medium] duplicate-template

Independent of where they are filed, R1481 ("If put into play with no counters, it burns immediately") and R1558 ("If put into play with no counters (X=0), it burns immediately") are one sentence written twice, from consecutive rulings [LSJ 20070307] and [LSJ 20070308]. Under the no-exhaustive-card-lists rule these are one principle, not two examples.

**Recommendation:** State the principle once and cite one card — {Secret Horde} (R1558) is the better "e.g." because its text makes the X=0 case explicit. Drop R1481 to the database, or keep it only if the drafter wants a second card to show the convention is not X-specific.

*Rulings (2):* R1481, R1558

### [medium] duplicate-template

R0009 ({Abandoning the Flesh}.2, "will not trigger the {Soul Gem of Etrius} since the vampire is removed from the game instead of being burned") and R1682 ({Soul Gem of Etrius}.2, "does not trigger if the bearer is removed from the game") are the same interaction stated from each end. Both are E/PRIMARY, so the section currently carries the same fact twice as two separate examples.

**Recommendation:** Keep R1682 as the single "e.g." — it states the rule from the triggering card's side and so generalises to any when-burned trigger. Drop R0009 to the database. Pair the surviving entry with R0017 ({Absimiliard's Army}.3, burned first *then* removed, so the trigger does fire) and R0347 ({Charnas the Imp}.3, ousted controller = removed, not burned): those three are the section's genuine polarity pair and are worth all three.

*Rulings (2):* R0009, R1682

### [medium] over-absorbed

Two E rows teach nothing transferable. R0127 ({Bauble}.1): "If it is burned by another mean than its effect, the weapon is not burned" — self-referential to {Bauble}'s own text and, as written, self-contradictory; it fails the transfer test and would be better carried by R1528/R1581 (a burn-conditional rider does not fire when the burn does not occur), which state the same idea generally. R1683 ({Soul Gem of Etrius}.3): "Functions even if the bearer (now burned) was prohibited from using equipments (eg. because of {Drawing Out the Beast})" — a two-named-card interaction whose real content is that a triggered effect is not an ability *use*, which 1.5 already owns.

**Recommendation:** Reclassify R0127 as C (note: {Bauble} self-burn condition; fails transfer, and the wording warrants a !WORDING flag). Reclassify R1683 as C with 1.5 as the near-miss code, or move it to 1.5 as secondary if the drafter wants a worked case there. Neither should consume an "e.g." slot in 1.10.

*Rulings (2):* R0127, R1683

### [low] thin-section

"Crypt/library separation" is one of the three sub-topics named in 1.10's own scope line, and R2537 (G00002|From ash heap to deck.1) is the only ruling that states it. R0968 ({Kaymakli Fragment}.2) is adjacent (continuous effects stop tracking cards shuffled back into the crypt) but is really a persistence ruling and sits here as secondary. The drafter will have one general-rule entry and no illustration.

**Recommendation:** Expect a one-sentence sub-topic and do not pad it. R2537 is a G-entry stating the rule directly, which is adequate prose material on its own; cross-reference 1.9 (empty crypt) and 6.7 rather than hunting for examples. If Phase 4.5 revisits the scope lines, consider whether crypt/library separation is better owned by 6.7.

*Rulings (2):* R2537, R0968

### [low] misfiled

R1129 ({Masquerade Endangered}.1, secondary): "Multiple copies may be played by different Methuselahs after a single action, but all would be burned during the vampire's next unlock phase." The teachable content is that multiple copies each resolve rather than being capped — 1.15's territory. The word "burned" here is only the card's own duration expiring, which is not what 1.10 is about.

**Recommendation:** Drop the 1.10 code and let 1.15 own it. Low confidence weight because it is a secondary row and costs the drafter only a glance, but it is one of the rows most likely to be misread as a burn ruling.

*Rulings (1):* R1129

## 1.11

### [high] duplicate-template

Eight rows are byte-identical copies of the same LSJ 20070808-1 boilerplate ("'continue as if unblocked' moves the action card from the ash heap ... to limbo"), spread across eight cards and multiple chunks. They are all `secondary` here (their true owner is 3.6 continue-as-if-unblocked), and they teach 1.11 exactly one fact: a blocked action's action card sits in the ash heap and can be moved back out. Eight copies of one sentence is 21% of the section's membership carrying one datum.

**Recommendation:** Keep ONE representative in 1.11's extract as the cross-reference anchor (R0039 {Ambulance} — the plain-vanilla copy with no discipline prefix) and drop the other seven from this section. The drafter states the fact once in 1.11 with a cross-ref to 3.6; 3.6 keeps whichever copies it needs for its own "e.g.".

*Rulings (8):* R0039, R0308, R0430, R0694, R0719, R1593, R1872, R1879

### [medium] duplicate-template

One principle — a card that resolves out of the ash heap has no effect if it has been removed from the ash heap before that resolution — appears five times. Four are the identical ANK 20220805 template ("Goes to the ash heap when played, if it has been removed when <trigger>, it has no effect": R0101 referendum passes, R0454/R1139 vampire blocks, R0763 action succeeds); R0571 {Echo of Harmonies} states the same rule with {Delaying Tactics} as the remover. Only the trigger clause varies, which is a per-card detail, not a distinct principle.

**Recommendation:** Keep R1139 {Melange} (already PRIMARY) as the template statement plus R0571 as the second "e.g." (it is the one that names the removal mechanism rather than just the trigger). Drop R0101, R0454, R0763 from 1.11's extract.

*Rulings (5):* R0101, R0454, R0763, R1139, R0571

### [medium] over-absorbed

Three rows are P/E in 1.11 but are pure readings of one card's own text and fail the transfer test. R2202 {Epikasta Rigatos}.1 "Can only retrieve a card played during that same action" is a restatement of Epikasta's own timing clause. R1532 {The Sargon Fragment}.2 "any copy of the named card in the ash heap can be fetched" generalises only to "the singular names any copy", the exact useless-generality pattern the C test was rewritten to exclude. R1618 {Shambling Hordes}.1 ("can choose not to remove a minion from his or her ash heap and thus burn the Shambling Hordes") is an optional-upkeep-cost reading of that one card; whatever is general in it belongs to 1.7, not to the ash heap.

**Recommendation:** Reclassify all three C (near-miss code 1.11; R1618 near-miss 1.7). None changes how a judge rules on any other card. Note that R2202's companion R2203 {Epikasta Rigatos}.2 is the genuinely general one and should stay.

*Rulings (3):* R2202, R1532, R1618

### [low] misfiled

R1303 {Père Lachaise, France}.2 "The crypt card on it is out of play and should be face down" is filed E/PRIMARY in 1.11, but it says nothing about the ash heap — it is about the state of a card placed ON a location, i.e. cards-on-cards and out-of-play status.

**Recommendation:** Move PRIMARY to 1.12 (cards on cards), with 1.14 (temporarily out-of-play cards) as the secondary; keep 1.11 only if the drafter wants the retrieval-destination cross-ref. Its sibling R1302 ("need only be in your ash heap; need not be one you first controlled") is the real 1.11 ruling and stays.

*Rulings (1):* R1303

### [low] duplicate-template

R0977 {Khazar's Diary} and R1354 {Pressing Flesh} are the same ruling (same references: LSJ 20010627, ANK 20181129) stated twice: targeting another Methuselah's ash heap does not make the action directed. The principle itself is 3.1's (directed vs. undirected announcement), not 1.11's; 1.11's stake is only the incidental "any ash heap, including an opponent's" fact, which overlaps R1302.

**Recommendation:** Keep one (R0977, the fuller wording) as 1.11's cross-reference for "retrieval effects may reach any player's ash heap" and drop R1354 here; both remain correctly filed under 3.1 as PRIMARY.

*Rulings (2):* R0977, R1354

### [low] duplicate-template

R0478 {Delaying Tactics}.5 and R0602 {The Erciyes Fragments}.2 are the same interaction recorded from each end: Delaying Tactics catches the political action card before it burns, so a card played from Erciyes Fragments returns to its owner's hand. One entry plus the interaction named covers both.

**Recommendation:** Keep R0478 (the general statement, already PRIMARY) and drop R0602 from 1.11's extract; the Erciyes side is the "e.g." inside R0478's own parenthesis.

*Rulings (2):* R0478, R0602

### [low] duplicate-template

Both are P/PRIMARY and both state the section's central rule identically — only cards played the normal way can be retrieved; cards put into play by another effect cannot (R2203 {Epikasta Rigatos}.2 naming {Concealed Weapon}/{Charming Lobby}, R2332 {Marthe Dizier}.1 in the abstract). Two P rows asserting one principle risks the drafter writing it twice.

**Recommendation:** Not a removal — keep both, but mark R2332 as the P (prose) and R2203 as E (it carries the two "e.g." cards). R0570 {Echo of Harmonies}.4 and R2333 (canceled-as-played still counts as played) are distinct facets of the same rule and should sit alongside as the boundary cases.

*Rulings (2):* R2203, R2332

### [low] thin-section

The taxonomy scope line promises two sub-topics — retrieval (played vs. put there) and "owner vs. controller for retrieval". The first is richly served; the second rests on two rows, only one of which is really about it: R1302 (need only be in YOUR ash heap, need not be a vampire you first controlled) and R2170 {The Capuchin} (burns to his original owner's ash heap, breaking control effects), which is primarily a 6.1/6.2 ruling appearing here as a cross-reference. Nothing in the membership covers what becomes of an ash heap when its owner is ousted, or which player's ash heap a card played by a non-owner lands in.

**Recommendation:** Flag to the drafter that the owner-vs-controller half of 1.11 will be one sentence built on R1302 with R2170 as its illustration, and that it should lean on a cross-reference to 6.1 rather than attempt independent coverage. Do not treat the absence as a classification defect — the corpus appears genuinely to lack these rulings.

*Rulings (2):* R1302, R2170

## 1.12

### [medium] duplicate-template

Six rows state the same principle — a host leaving play or being burned takes its hosted cards with it. R2563 (G00028 "Cards holding cards.1": "If it leaves play, the card on it is burned") is the general entry and already says it in full; R1142 ("Any cards on the target minion are burned"), R1419 ("Blood, equipments and other cards on the initial target are burned"), R0144 ("If the vampire chosen for Betrayer is burned, so is Betrayer") and R2169 ("If he burns, he looses all cards and counters on him") are the same sentence on four different cards. Under the no-exhaustive-lists rule this is one principle with at most three e.g. cards, not six entries.

**Recommendation:** Draft the prose from R2563. Keep R1483 {Righteous Aura} as the lead example because it alone adds the timing refinement ("the card is burned before the vampire leaves the ready region", e.g. under {Banishment}), and keep at most one of R1142/R1419 as the minion-replacement instance. R0144 and R2169 are better used in their other sections (R0144's contest and control-change clauses belong to 1.13/6.2; R2169 is a 6.4 leaves-and-re-enters ruling) and need not appear as separate 1.12 examples. Also note R0144 is labelled P PRIMARY here but only restates R2563 on one card — it is an E at best.

*Rulings (6):* R2563, R1142, R1419, R0144, R1483, R2169

### [medium] duplicate-template

R1175 {Mokolé Blood}.1 and R1628 {Shilmulo Tarot}.2 are byte-identical, including their reference lists: "If there is another copy in play, the cards are put on it before it enters contest. [ANK 20221028] [LSJ 20090428-1]". Two chunks classified the same boilerplate independently and both landed here as E/secondary.

**Recommendation:** Keep exactly one as the "e.g." (either; {Storage Annex}-family hosts are the more recognisable case, so {Mokolé Blood} R1175 is fine) and drop the other from 1.12's extract. The principle — hosted cards migrate to the surviving copy rather than being lost when the host enters contest — is worth one sentence cross-referenced to 1.13.

*Rulings (2):* R1175, R1628

### [medium] over-absorbed

R1739 {Storage Annex}.3 is E/PRIMARY but is a pure interpretation of Storage Annex's own text: "The card on it goes to the controller's hand, regardless of where the new card comes from (eg. {Agaitas, The Scholar of Antiquities} face-up cards)." The qualifier "regardless of where the new card comes from" only has meaning inside Storage Annex's put-a-card-on-it/take-the-old-one mechanism; no other card's ruling changes because of it. Fails the transfer test.

**Recommendation:** Reclassify to C with a note (nearest 1.12). R1737 {Storage Annex}.1 already carries the transferable Storage Annex content for this section — hosted card follows the host when stolen, and returns to the OWNER's ash heap or library — so nothing is lost.

*Rulings (1):* R1739

### [low] duplicate-template

R1481 {Riddle Phantastique}.1 ("If put into play with no counters, it burns immediately") and R1558 {Secret Horde}.1 ("If put into play with no counters (X=0), it burns immediately") are the same template on two cards — this is the counter-count-on-entry convention the 1.12 scope line was widened to claim. Both are filed P/secondary, so the ruling pair the scope line exists for reaches the drafter only as cross-references.

**Recommendation:** Treat these as one principle with one e.g. card. Prefer R1558 {Secret Horde}, whose "(X=0)" makes the X-cost origin of the zero explicit, and cite R1481 only if a second card is wanted. The drafter should state this as prose in 1.12 despite both rows being secondary.

*Rulings (2):* R1481, R1558

### [low] misfiled

R0957 {Jar of Skin Eaters}.4 — "{Ghoul Retainer} is not the bearer so he can use the Jar even if it has no counter on it" — is a ruling about who counts as the bearer of an equipment and a retainer's use of it. Its only contact with 1.12 is the incidental phrase "no counter on it"; it teaches nothing about cards or counters on hosts.

**Recommendation:** Drop from 1.12's extract. 5.6 (retainers striking/using, bearer) or 1.5 (ability use vs. card play) should own it. Secondary row, so this costs the drafter only a discard.

*Rulings (1):* R0957

### [low] misfiled

R1605 {Shadow Court Satyr}.4 — "If the combat card is moved, the Satyr cannot use it as if played from your hand anymore, even if it was moved on him (eg. {Weighted Walking Stick})" — turns entirely on the Satyr's own play-as-if-from-hand mechanism. It is a one-card interpretation, and its 1.12 content is only that a hosted card can be relocated.

**Recommendation:** Drop from 1.12 (secondary row). The section's real Shadow Court Satyr material is R1607 ("The card put on him is not into play"), which states the in-play-status principle and should carry that sub-topic alone.

*Rulings (1):* R1605

### [low] thin-section

The game status of a hosted card rests on a single ruling. R1607 ("The card put on him is not into play") is the only row establishing that hosted cards are not in play, and nothing in the membership says what follows from that — whether a hosted card can be targeted, whether it counts for uniqueness or card-type effects, or what happens to hosted cards when the host merely changes state (goes to torpor, becomes locked) rather than leaving play. R1737 is the only row on destination zones.

**Recommendation:** Flag for the drafter: state the not-in-play principle from R1607 and the owner-determines-destination rule from R1737, then cross-reference rather than trying to fill the gap. If judge confirmation is wanted on host-state-change vs. host-leaves-play, this is where a ⚠ REVIEW mark belongs.

*Rulings (2):* R1607, R1737

## 1.13

### [high] scope-drift

Nine rulings (20% of the section) are about Blood Brothers CIRCLE membership and contain no contest content at all. The seam is clean: sub-topics 'self-contest', 'a contested card is out of play', 'entering contest', and 'what is remembered after' all turn on contest mechanics; the circle rulings turn on vampire grouping/identity and never mention contesting. They are here only because the 1.13 scope line says 'vampire circles & same-name vampires'. Read end to end, R2538 ('a vampire with no circle designation is in his own unique circle'), R2236/R2238 (created vampires are each in their own circle of one) and R2373 (Inner Circle title != Blood Brothers circle) are indistinguishable from 5.7 special-minion-trait material. Same-name-vampire rulings (R0890, R2259, R1696, R1697) DO belong here, because sameness of name is what drives contest; circle designation does not.

**Recommendation:** Move the circle-designation rulings to 5.7 (special minion classes & traits, which already owns Blood Brothers) and narrow the 1.13 scope line to 'same-name vampires' only. If the drafter prefers to keep them, they must be written as an explicitly labelled sub-section that cross-references 5.7 rather than being woven into contest prose — otherwise the section states two unrelated rules under one heading.

*Rulings (9):* R2538, R2125, R2371, R2126, R2372, R1943, R2236, R2238, R2373

### [high] duplicate-template

Eight rulings are the SAME sentence from the SAME ruling reference [LSJ 20080526], spread across eight cards and (evidently) many chunks: 'His "as he enters play" ability can be used before he enters contest if there is another one in play' (R2114 Anarch Convert, R2204 Erlik, R2247 Inez Villagrande, R2396 Porphyrion, R2427 Seterpenre, R2473 Verbruch, R2475 Victor Pelletier; R2192 Dr. Solomon Grey is the same template with a cost instead of an ability). The style rules cap this at one principle plus 1-3 'e.g.' cards, so seven of these are database-only. The chunks also split the role arbitrarily on identical text: R2114/R2396/R2427/R2473 are P, R2204/R2247/R2475/R2192 are E. R2040 (Wormwood.2) is the only row that actually STATES the ordering principle ('the excess blood drains off before entering contest and before playing "as played/as he enters play" effects') and it is filed here only as secondary.

**Recommendation:** Promote R2040 to the principle-carrying row for this sub-topic (entry ordering: pay/place, then as-enters effects, then contest). Keep at most three examples — suggest R2114 (Anarch Convert, which adds 'this is not self-contesting'), R2192 (Dr. Solomon Grey, showing the cost variant) and R2475 or R2204 (which add the 'not after' clarification). Drop the remaining five from the extract.

*Rulings (9):* R2114, R2192, R2204, R2247, R2396, R2427, R2473, R2475, R2040

### [medium] duplicate-template

Within the circle cluster, one statement is repeated six times and a second three times. R2538 (G00003|Circle.1), R2125 (Angelo.1) and R2371 (New Blood.1) are the same sentence verbatim ('a vampire with no circle designation is in his own unique circle of one', all [LSJ 20020609]); R2126, R2372 and R1943 repeat the follow-on ('two uncontrolled Angelos/New Bloods are in different circles, so you have to choose one'). R2236 and R2238 are word-for-word identical to each other on two sibling cards (Hermana Hambrienta Mayor/Menor).

**Recommendation:** Keep R2538 as the P row (it is the general rule entry and is prime prose material per the contract), R2126 or R2372 as the single 'e.g.' for the choose-one consequence, and one of R2236/R2238 for created vampires. Drop the other five wherever this sub-topic ends up landing.

*Rulings (8):* R2538, R2125, R2371, R2126, R2372, R1943, R2236, R2238

### [medium] duplicate-template

R1175 (Mokolé Blood.1) and R1628 (Shilmulo Tarot.2) are identical text with identical references ([ANK 20221028] [LSJ 20090428-1]): 'If there is another copy in play, the cards are put on it before it enters contest.' R0577 (Elder Library.1, same [ANK 20221028]) is the same ruling's other half: the card enters contest without its ongoing effect applying. All three teach one principle — a card entering contest still resolves its entry placement, but is out of play for ongoing effects.

**Recommendation:** State the principle once and keep two examples: R0577 (ongoing effect suppressed) and one of R1175/R1628 (entry placement still happens). Drop the other.

*Rulings (3):* R1175, R1628, R0577

### [medium] over-absorbed

Both are pure interpretations of Jimmy Dunn's own printed trigger. R2262 ('If a non-contesting second copy of Jimmy enters play, the first Jimmy won't burn himself') fails transfer outright — it affects no other card, and the general point it gestures at is already carried better by R0890 (Illusions of the Kindred.7: an illusionary vampire is considered different for all purposes, citing Jimmy Dunn by name as the example). R2261 is labelled P/PRIMARY, which risks a drafter stating a general 1.13 principle out of a card-specific trigger question: the sentence is 'the acting vampire is not considered to be "burning" the first Jimmy', which reads as Jimmy-specific text interpretation.

**Recommendation:** Reclassify R2262 as C (subsumed by R0890). Keep R2261 only for its transferable nugget — a card that leaves play through contest is not burned BY anyone — and file that under 5.4 (who burned them / trophies), demoting 1.13 to secondary and the role to E.

*Rulings (2):* R2261, R2262

### [medium] over-absorbed

R2373 (New Blood.3) is 'Cannot choose to be part of the "Inner Circle" and get the title. The Inner Circle title and a Blood Brothers circle are different things.' This is a name-collision disambiguation between two unrelated game terms. It has no contest content, and it changes how you would rule on no other card — it fails the transfer test.

**Recommendation:** Reclassify as C with 5.7 as the near-miss code. If anything survives into prose, it is a parenthetical in the Blood Brothers material, not a contest rule.

*Rulings (1):* R2373

### [low] duplicate-template

R0492 (Descent into Darkness.5) and R1009 (Lay Low.2) are the identical sentence with the identical anchor reference [RTR 20000501]: 'will remember all effects that had been applied to him, just as contested vampires do. This includes gained or lost titles.' Both are secondary here, and both are borrowing 1.13 as the analogy rather than teaching it — the rule they state belongs to 6.4 (leaving and re-entering play).

**Recommendation:** Keep one (R0492) as the cross-reference showing what a contested vampire remembers; drop R1009 as a duplicate. R1408 (The Rack.4, 'tracks the target if it leaves the game by contesting') is the better in-section evidence that a card returning from contest is the same card.

*Rulings (2):* R0492, R1009

### [low] duplicate-template

Three The Rack rulings for what is at most two principles. R1405 ('may not select a new target just for falling out of contention') and R1406 ('will not target a new copy of the same vampire if the original is burned or yielded') both state that a targeting effect's target is fixed and a new copy is a different card. R1405 is the more card-bound of the two — 'falling out of contention' is The Rack's own targeting vocabulary. R1408 is a different and genuinely useful principle (a card returning from contest is the SAME card, so tracking effects resume).

**Recommendation:** Keep R1406 as the example for 'a new copy is not the old card' and R1408 for 'contest return preserves identity'. Drop R1405 as a duplicate of R1406.

*Rulings (3):* R1405, R1406, R1408

### [low] missing-topic

The membership has no ruling on the contest PROCEDURE itself: when yielding is decided, who may yield, what happens if neither player yields, or the pool cost of contesting. Everything present is downstream of a contest already existing (what effects do while contested, what is remembered after, what happens on entry). R1322 (yielding Political Seizure) and R2435 (Sonja Blue) touch yielding only incidentally.

**Recommendation:** Expect the section's opening paragraph to be un-footnotable from the rulings corpus and to cite the rulebook ([RBK …]) for the procedure instead. Flag for the drafter so the absence is not read as a coverage failure.

## 1.14

### [high] duplicate-template

Ten rulings across at least eight chunks are the same sentence — "The card to retrieve must be announced when declaring the action" — and nine of them cite the identical single ruling [LSJ 20010627]. R2171 (Carlotta Giovanni) is the same principle under the older [LSJ 19970922]. This is one principle (ash-heap retrieval names its target at announcement, not at resolution), not ten examples, and the style rule caps illustration at 1-3 cards.

**Recommendation:** Keep R1531 ({Sargon Fragment, The}) as the card-provided-action case and R2395 ({Pochtli}) as the vampire-ability case — two cards spanning the two ways the effect arises. Drop the remaining eight to C in the extract, or at minimum mark them as redundant copies so the drafter does not mistake volume for weight. Cite [LSJ 20010627] once in the footnote; it is a single ruling, and a footnote listing nine cards would itself violate the no-exhaustive-lists rule.

*Rulings (10):* R0363, R0754, R1287, R1531, R1537, R2027, R2195, R2382, R2395, R2171

### [medium] duplicate-template

A second recurring template: a card named from hand must be in hand at the moment the naming card is played, before that card is replaced, and need not be shown (may be set apart face down). R0383 {Concealed Weapon} and R0514 {Disguised Weapon} are verbatim identical with overlapping refs ([LSJ 19991207] [ANK 20180925-2]); R0336 {Charming Lobby} is the political-action variant of the same sentence; R0332, R0949 and R0769 are the "must be in hand before replacing" half without the face-down clause. The chunks also split the role inconsistently — R0514 is P and its verbatim twin R0383 is E.

**Recommendation:** Treat as ONE principle with two clauses (in-hand-at-play-before-replacement; not-shown/set-apart). Keep R0514 {Disguised Weapon} as the weapon example and R0336 {Charming Lobby} as the political-action example — R0336 additionally carries the unique cancel/fail clause ("If the action is canceled or failed, the political action card stays in hand"), which no other ruling here supplies and which should drive prose, not sit as an example. Drop R0383 as a verbatim duplicate of R0514.

*Rulings (6):* R0383, R0514, R0336, R0332, R0949, R0769

### [medium] duplicate-template

R0105 {Baal's Bloody Talons} and R0362 {Cleave} are word-for-word identical ("The weapon does not burn if it is temporarily out of play (eg. {Kerrie}, {Dagger})") from the same ruling [LSJ 20100211-2], and both are labelled PRIMARY/P. They are the entire evidentiary base for 1.14's "temporarily out-of-play" half, so the duplication also disguises how thin that sub-topic is.

**Recommendation:** Keep one as the P statement of the principle (R0105 is the cleaner instance — R0362 carries a trailing sentence about ordering effects at end of action that belongs to 2.4). Verify R0362's ordering clause reaches 2.4; if it is not coded there, that clause is a silent loss.

*Rulings (2):* R0105, R0362

### [medium] misfiled

R0604 {Erciyes Fragments, The}.4 — "The card on it cannot be discarded or burned to satisfy another effect (eg. {Tension in the Ranks})" — is filed PRIMARY here, but a card placed ON a card in play is the scope of 1.12 (cards on cards), not of set-aside/announced cards. The principle it teaches is that a hosted card is not in any zone that discard/burn effects can reach, which is 1.12's territory; 1.14 owns cards named from hand and held aside for the same effect's own later use.

**Recommendation:** Reassign PRIMARY to 1.12, retaining 1.14 as a secondary cross-reference. The two sections should cross-reference rather than both narrate hosted-card zone status.

*Rulings (1):* R0604

### [medium] missing-topic

1.14's scope line claims two sub-topics — "cards announced from hand for later" and "temporarily out-of-play cards" — but after de-duplication the second is supported by exactly two rulings: R0105/R0362 (weapon out of play does not burn) and R1639 {Siphon}.3, which is the only ruling in the whole section that names the limbo zone ("it is in limbo (not in the ash heap) when resolving"). There is no ruling at all on the status questions a judge actually asks about set-aside cards: whether a set-aside card counts against hand size, whether it can be targeted, stolen or discarded by an opponent effect while set aside, or where it goes if the naming card leaves play. Only R0336 covers the cancel/fail return path, and only for the {Charming Lobby} political-action case.

**Recommendation:** Flag to the drafter that the set-aside-status sub-topic will be thin and mostly unsourced. Two concrete gaps to check against the database before drafting: (a) hand-size treatment of set-aside cards — 6.9 owns hand size and may hold the relevant ruling; (b) the general fate of set-aside cards when the naming card is canceled beyond R0336's single instance. If nothing exists, the section should state the limbo principle from R1639 and cross-reference rather than pad.

*Rulings (2):* R1639, R0336

### [low] misfiled

R1974 {Victim of Habit}.2 — "Once the prey is ousted, the chosen card does not change, but the effect can be used on the new prey" — is PRIMARY here, but the principle is persistence of a locked-in choice across a game-state change (prey shift on ousting), which is 2.5 (duration & persistence) with a 6.5 ousting component. The card named by {Victim of Habit} is a naming, not a card set aside from hand, so it does not exercise 1.14's mechanic.

**Recommendation:** Reassign PRIMARY to 2.5, keep 1.14 secondary if the drafter wants the naming-is-fixed cross-reference. Low severity: it is one ruling and the code carries no dependent cluster.

*Rulings (1):* R1974

### [low] role-error

R1639 {Siphon}.3 is labelled E, but it is the only ruling in the section that states the underlying zone concept ('limbo', explicitly distinguished from the ash heap) rather than illustrating it. Every other candidate for stating the set-aside principle is a duplicate of a template. Reported only because the section is short of P material, not because P/E is worth churn on its own.

**Recommendation:** Promote to P so the drafter sees it as prose material for the limbo/temporarily-out-of-play paragraph. No reclassification of codes needed.

*Rulings (1):* R1639

## 1.15

### [high] duplicate-template

Five rulings are the identical [ANK 20200515] sentence "Multiple copies can be played by different minions on the same action" spread across five cards ({Blanket of Night}, {Cloak the Gathering}, {Inspire Greatness}, {Mask of a Thousand Faces}, {Suppressing Fire}) and multiple chunks. They are one ruling, not five examples. The chunks also disagreed on role placement: R0934/R1125/R1775 are PRIMARY here while R0165/R0366 are secondary, despite word-for-word identical text — a direct violation of golden rule 5 (identical rulings, identical labels) that is only visible with the section assembled.

**Recommendation:** Collapse to a single principle entry — "a per-action play limit binds the minion, not the action: different minions may each play their own copy" — with e.g. {Cloak the Gathering} and {Suppressing Fire}. Drop the other three from the extract. Note also that this template's centre of gravity is the per-minion/per-action limit, so the drafter should check whether it is better stated in 1.2 (periodicity templates) with a cross-reference from 1.15 rather than duplicated in both.

*Rulings (5):* R0165, R0366, R0934, R1125, R1775

### [high] duplicate-template

Five rulings all carry the single reference [LSJ 19980225] and say the same thing in near-identical words: "Burn pool effects are cumulative" (R0022), "Burn blood effects are cumulative" (R0073, R0273, R1522), "The cost is cumulative if they are multiple copies in play" (R0048). All five are labelled P, so the extract hands the drafter five copies of one prose statement.

**Recommendation:** Keep R0022 (or R0073) as the single P stating the default — repeated burn-pool/burn-blood requirements from multiple sources are cumulative — and at most one further card as "e.g.". Drop the remaining three. Under the no-exhaustive-card-lists rule, four vampires whose only content is the same one-line general ruling are not four examples.

*Rulings (5):* R0022, R0073, R0273, R1522, R0048

### [medium] duplicate-template

Five rulings teach the same principle — each copy of a card in play exerts its own effect and imposes its own cost — with no distinguishing sub-case between them: {Betrayer} (pay 1 pool per Betrayer), {First Tradition} (two copies = burn 4 pool), {Frontal Assault} ("they stack"), {Judgment: Camarilla Segregation} ("one must pay for each of them (they stack)"), {Kindred Society Games} (two copies = 2 blood to unlock).

**Recommendation:** Keep R0143 {Betrayer} (the taxonomy's own canonical case, and the only one that adds a wrinkle — the per-copy cost applies even when the same vampire is the betrayer in each copy) plus R0989 {Kindred Society Games} (adds per-copy independence on the follow-on effect). Fold R0677, R0740, R0963 into the database; their references can ride the same footnote if the drafter wants the citation weight.

*Rulings (5):* R0143, R0677, R0740, R0963, R0989

### [medium] duplicate-template

R1020 {Leech} and R1401 {Putrescent Servitude} are the same ruling [ANK 20180111] recorded twice, each naming the other card: "Does not stack with similar effects to provide superior [POT] (eg. {Putrescent Servitude})" / "(eg. {Leech})". Both are P, so the drafter receives the same sentence twice.

**Recommendation:** Keep one (either) as the P stating that discipline-granting effects from different cards do not combine to yield the superior level, citing both cards in the one "e.g.".

*Rulings (2):* R1020, R1401

### [medium] misfiled

R1716 {Spying Mission}.4 is PRIMARY in 1.15 but its content is action-resolution, not stacking: "The bleed it is played on is considered unsuccessful." The only stacking-adjacent clause — "Previous Spying Missions won't trigger during that action" — is a statement about this one card's own trigger condition interacting with its own effect, which fails the transfer test (it changes how you rule on no other card).

**Recommendation:** Move PRIMARY to 3.4 (success vs. effect) or 3.7.1 (bleed), with 1.15 dropped entirely rather than kept as secondary. If the drafter wants a non-cumulative-trigger example, R1266 {Orun}.1 ("will only burn one if he successfully bleeds for more than 2") states it cleanly without the resolution content attached.

*Rulings (1):* R1716

### [low] scope-drift

R1124 {Mask of a Thousand Faces}.11 is filed here as secondary, but neither clause is about cumulation. "The masking vampire can play a modifier already played by the masked minion" is 3.10 (changing the acting minion); "He cannot use a limited effect if a limited effect has already been used on the action" is the once-per-action limited-effect rule, which 1.2 owns.

**Recommendation:** Drop the 1.15 code. Its PRIMARY (3.10) is correct and nothing in 1.15's prose would be written from this row. Low severity because it is a secondary row and costs only tokens; flagged because the drafter reading the extract may mistake the limited-effect clause for a stacking rule.

*Rulings (1):* R1124

### [low] thin-section

The section's cross-card non-stacking sub-topic — two DIFFERENT cards granting a similar effect that does not combine — rests entirely on a single ruling ([ANK 20180111]) recorded on two cards. Every other non-stacking row here (R1028 {Legacy of Pander}, R1267 {Orun} votes, R1543 {Scorn of Adonis}, R1836 {Temptation}, R2191 {Dr. Morrow}, R2264 {Kahina}) is about multiple copies of the SAME card or multiple counters of the same kind. Once the Leech/Putrescent pair collapses to one entry (see above), the drafter has exactly one ruling for that half of the "does not stack with similar effects" scope line.

**Recommendation:** Tell the drafter to state the cross-card non-stacking rule narrowly (discipline-level grants from distinct cards) rather than as a general claim, or to cross-reference rather than assert. Do not expand the section on this evidence; the same-card and counter-count sub-topics are well populated and should carry the section's weight.

*Rulings (2):* R1020, R1401

## 1.2

### [high] duplicate-template

The single largest block in 1.2 is one template arriving fifteen times from many chunks: 'this ability/action may be used only once per <period>', where only the period varies (turn, your turn, master phase, minion phase, unlock, action, bleed, referendum). R2130 'cannot perform the action provided by his ability twice in the same turn', R2158 'cannot perform his special action twice in the same turn, even to fetch different cards', R2283 'can only perform the action provided by her ability once per turn' and R2527 'ability can be used only once per master phase' are the same sentence four times. No classifier could see this from inside 145 lines; the drafter receiving all fifteen will be tempted to write fifteen sentences, which the no-exhaustive-lists rule forbids.

**Recommendation:** Write ONE principle from R2549 (G00014, 'once each turn' means once during each player's turn) and enumerate the periodicity units in prose. Keep exactly three 'e.g.' cards, chosen because each adds a wrinkle the bare template lacks: R2530 {Maila} ('once during each of your turns' — the contrast that makes R2549 non-trivial), R2375 {Owain Evans} (limit survives a change of control during the unlock phase), R2116 {Andre LeRoux} (per-event limits recur across multiple events in one turn). Drop the rest to the ruling database as 'e.g.' overflow; specifically R2130, R2158, R2283, R2527, R0286, R1250, R1311, R2400 add nothing to the template.

*Rulings (15):* R2549, R2130, R2158, R2283, R2527, R2530, R2400, R2375, R2351, R0412, R2116, R0286, R1250, R1311, R2062

### [high] over-absorbed

Beyond being duplicates, these five fail the contract's non-obviousness test outright: they restate a limit printed on the card. R0286 'the effect to burn a hostage counter can be done only once per turn' and R2158 'he cannot perform his special action twice in the same turn' tell a judge fluent in the rulebook nothing they did not already know from reading the card. They are P/E here but teach no principle beyond 'the printed words mean what they say'.

**Recommendation:** Re-role to C with a note ('restates the card's own printed periodicity; fails non-obviousness'), keeping 1.2 as the near-miss code. This is subtractive only — R2549 already carries the principle they would have illustrated, so nothing is lost from the extract.

*Rulings (5):* R2130, R2158, R2283, R2527, R0286

### [medium] duplicate-template

The inverse-polarity twin of the finding above, also arriving five times across chunks: 'an ability with no stated limit may be used repeatedly'. R2330 {Maris Streck} 'can use her ability multiple times each action' and R2196 {Edith Blount} 'may burn a blood to give {Enid Blount} stealth multiple times each action' are the same rule; R2415 {Santaleous} and R2243 {Hukros} restate it for cancellation and for accumulation.

**Recommendation:** State it as the corollary of the periodicity principle in the same paragraph — absence of a periodicity clause means no limit — with one 'e.g.' (R2330 {Maris Streck}) and at most one contrast case (R2360 {Nahir}, which adds that 'each master phase' scales with the number of master phase actions rather than being once per turn). R2196, R2415, R2243 to C.

*Rulings (5):* R2196, R2330, R2360, R2415, R2243

### [medium] duplicate-template

Four rulings, three of them sharing the reference [ANK 20230316], say that a periodicity limit attaches to the card and not to the effect, so a second copy grants a second use: R0042 {Amulet of Temporal Perception} 'a second copy allows a second use in the same turn', R2580 (G00045) '...in the same combat', R2581 (G00046) '...in the same round'. R2062 {Haqim's Law: Retribution} '(multiple Haqim's Law: Retribution can each be used once)' is the same rule again. Split across chunks, this reads as three or four rules keyed to different periods; it is one rule with the period as a free variable.

**Recommendation:** One sentence — the limit is per card, not per effect, whatever the period — citing R2580/R2581 as the general entries and R0042 as the single 'e.g.'. Note the overlap with 1.15 (multiple copies each exerting their effect): cross-reference rather than restate. R2062 is redundant here.

*Rulings (4):* R0042, R2580, R2581, R2062

### [medium] duplicate-template

'Ability usable only once per referendum' appears four times, twice as general entries (R2574 G00039 unconditional, R2575 G00040 non-locking) and twice on cards (R2199 {Ellison Humboldt}, R2351 {Michael Luther}). R2199 is a verbatim restatement of R2574 with no added content.

**Recommendation:** Keep R2574 as the prose (it also carries the locked/torpor scope) and R2351 {Michael Luther} as the sole 'e.g.', since it alone adds the non-obvious part — unlocking mid-referendum does not reset the limit. R2199 to C; R2575 is a scope variant of R2574 and should be merged into the same sentence, not given its own.

*Rulings (4):* R2199, R2351, R2574, R2575

### [medium] duplicate-template

Two verbatim-duplicate triples in the optional-maneuver/press sub-topic. First: 'the optional maneuver cannot be used if the strike cannot be used (eg. {Hidden Lurker})', identical wording and identical reference [LSJ 20021028] in R0468 {Deer Rifle}, R1865 {Tinglestripe} and R2559 (G00024). Second: 'the press/maneuver can only be used during the current round', identical wording and identical reference [TOM 19960521] in R0556 {Dust to Dust}, R1467 {Resist Earth's Grasp} and R1484 {Rigor Mortis}.

**Recommendation:** First template: R2559 (G00024) as the P, R0468 {Deer Rifle} as the one 'e.g.', R1865 to C. Second template: keep one card only — R1484 {Rigor Mortis} — and drop R0556 and R1467, which are the same [TOM 19960521] ruling repeated. Note R1865 is currently roled P while being a pure card copy of the G00024 general entry.

*Rulings (6):* R0468, R1865, R2559, R0556, R1467, R1484

### [medium] scope-drift

The membership contains two topics that share a scope line but not a principle. Topic A (~45 rows) is periodicity: how often an effect may be used. Topic B (~11 rows) is trigger-and-condition wording: what makes a trigger fire. R0052 {Anathema} 'will not burn a vampire for entering combat with zero blood: there must be an actual blood loss' (trigger is an event, not a state), R0607 {Escaped Mental Patient} "'if he does so' only applies if his own effect is used directly" and R0679 {Flaming Candle} 'is not burned if another effect makes the vampire burn 1 blood' (a self-referential condition reads only its own card's effect) are one genuinely valuable principle that has nothing to do with periodicity. The seam falls cleanly between them.

**Recommendation:** Not a reclassification — both sides are in 1.2's stated scope. Tell the drafter to write 1.2 as two explicit subsections: periodicity limits, and trigger/condition wording. The second is currently the stronger material per ruling and will be buried if merged into the once-per-X mass. R0607/R0679/R0052 together support a stated principle ('a condition referring to the card's own effect is not satisfied by another effect producing the same event'); R0607 or R0679 alone would be a card note.

*Rulings (11):* R0051, R0052, R0607, R0676, R0679, R1510, R0076, R2117, R2118, R2549, R2545

### [medium] misfiled

R0621 {Ex Nihilo} 'any effect that would give more blood to the vampire is a gain of blood, so does not apply (eg. {Heidelberg Castle, Germany})' is filed P/PRIMARY in 1.2 but teaches the gain-vs-move-blood distinction, not a periodicity or trigger-wording template. Nothing in it turns on 'each combat', 'once per X', a duration, or a would/when/after window.

**Recommendation:** Reassign PRIMARY to 1.7 (costs & payment — pool/blood distinctions), which owns the gain/put/transfer vocabulary. If a template angle is wanted, 1.2 can stay as a secondary code, but it should not be the section drafting from this ruling.

*Rulings (1):* R0621

### [medium] recoverable-C

R0113 {Bamba} 'you only fetch one discipline card in total, not one in each of hand, library and ash heap' is roled E but is a pure reading of one card's sentence. It generalises only to 'the singular in card text means one' — which is precisely the example the taxonomy names as the archetypal C (`Great Symposium.1`) when explaining that generality is necessary but not sufficient. It fails transfer: no other card is ruled differently because of it.

**Recommendation:** Re-role to C with 1.2 retained as the near-miss code. If the drafter wants the underlying point at all, it belongs as a clause in the trigger-wording subsection, not as a Bamba example.

*Rulings (1):* R0113

### [low] misfiled

Three secondary rows have no template or periodicity content and read as stray cross-references. R0531 {Draba} 'effectively gives a -X stealth modifier to the action' is a stealth mechanic (3.2). R2445 {T.J.} 'must be unlocked with at least 2 blood to use his ability' is a cost/requirement to use an ability (1.7, or 1.5). R2433 {Sonja Blue} "'block as an ally' only affects the 'who can block this action' check" is blocking eligibility (3.3/5.5).

**Recommendation:** Drop the 1.2 code on all three. Being secondary rows they are cheap, but each will land in 1.2's extract as noise the drafter must read and discard, and none of them is about wording periodicity. R2445 is the weakest — its only tie to 1.2 is the [RBK wording-templates] reference on the line, not the ruling's content.

*Rulings (3):* R0531, R2445, R2433

### [low] misfiled

R0076 {Archon Investigation} 'must be played before action resolution, before any modifier or reaction played as the action would be successful' is P/PRIMARY in 1.2, and R2118 {Andre LeRoux}.3 states the same rule from the other side ('only modifiers and reactions that can be played when the action/bleed would be successful can be played after it'). The principle taught is the ordering of a timing window, which is chapter 2 material; 1.2 owns the semantics of the phrase 'would', not the sequencing consequence. The two also duplicate each other.

**Recommendation:** Move PRIMARY on R0076 to 2.1 (effect windows / sequencing), keeping 1.2 secondary. Have the drafter state the window rule once from R2118, with R0076 or R2117 as the single 'e.g.' — not both, since {Andre LeRoux}.2 (R2117) exists only to say it behaves 'like {Spying Mission}'.

*Rulings (3):* R0076, R2118, R2117

### [low] thin-section

Three of the templates named explicitly in 1.2's scope line are supported by almost nothing. 'Since your last turn' has exactly one row, the general entry R2545, with no card example at all. 'Once per game' has two (R0671 {Filchware's Pawn Shop}, R2565 G00030 'burning the card for a vote is not considered playing it'). 'Each combat' has R0001 {.44 Magnum} plus the R2580 general entry. By contrast 'once per turn/action/referendum' is over-supplied fourfold.

**Recommendation:** Flag to the drafter that these three sub-topics will be one sentence each, sourced from the general entries, with no worked example available — that is the correct outcome, not a hole to fill by padding. R0001 ('provides only one maneuver each combat, even if the bearer changes') pairs naturally with R2375 {Owain Evans} ('even if control changes'): both say a periodicity limit tracks the card across a change of holder, which is worth stating once as a shared principle rather than twice.

*Rulings (4):* R2545, R0671, R2565, R0001

## 1.3

### [high] duplicate-template

Six rulings are the SAME sentence with the same citation [PIB 20150924-2]: "Card with multiple types (eg. Combat/Action Modifier) are considered of the type they are played as, not both." R2094 (Adana de Sforza), R2176 (Conrad Adoula), R2255 (Jane Sims), R2370 (Nergal), R2411 (Rex), R2422 (Scout Youngwood) differ only in the vampire whose ability keys off card type and in whether the parenthetical reads Combat/Action Modifier or Reaction/Action Modifier. All six are labelled P PRIMARY, so six chunks each independently promoted the same sentence to prose. R2240 (Horrock, same citation) is not a duplicate — it extends the rule to discipline choices ([pro]/[obf]) — and R2234 (Henry Taylor, [LSJ 20031221]) is an independent application.

**Recommendation:** Keep ONE as the P that states the principle, plus at most two "e.g." cards showing the two polarities — suggest R2094 (Combat/Action Modifier) and R2176 (Reaction/Action Modifier). Keep R2240 separately as the discipline-choice extension and R2234 as the eligibility application. Demote R2255, R2370, R2411, R2422 to C (they transfer nothing beyond the sentence already stated). This alone is 4 of the section's 36 rows.

*Rulings (8):* R2094, R2176, R2255, R2370, R2411, R2422, R2240, R2234

### [high] duplicate-template

The "cost reduction applies to equipments that are locations" rule is filed five times. R1851 (Therbold Realty) and R2324 (Marie Faucigny) are verbatim identical down to the same example — "The reduction applies to equipments that are locations (eg. {Palatial Estate})" — differing only in citation date ([LSJ 20080107] vs [LSJ 20080109]). R2535 (Regina Blake) is the same rule phrased as paying rather than reducing, also citing [LSJ 20080107]/[LSJ 20080114]. R2071/R2072 (British Museum) restate it with the useful addition that the card type is checked IN HAND. Both R1851 and R2071 are P, so the drafter receives two competing prose statements of one rule.

**Recommendation:** Keep R2071 as the P — it is the only one that states the operative mechanism (type checked in hand, not in play), which is what makes the whole cluster true. Keep one of R1851/R2324 as the single "e.g.". Demote the remaining three to C; per the style rule these are one principle with one example, not five examples.

*Rulings (5):* R1851, R2324, R2535, R2071, R2072

### [medium] duplicate-template

Four rulings all citing [LSJ 20050315] say a named vampire "can equip with an equipment that is a location when in play": R2201 (Enkidu), R2231 (Helen Fairchild), R2306 (Lorrie Dunsirn) are word-for-word identical, and R2156 (Beast, the Leatherface of Detroit) is the same plus a genuine extra clause. The three identical ones are secondary rows, which is mitigating, but they are still three copies of one sentence landing in one extract.

**Recommendation:** Keep R2156 only — it is strictly more informative, carrying the nuance that the vampire cannot get there by playing the card normally "as it is an action card", which is the actual teaching point (the ability reads the in-play type, the card play reads the hand type). Drop R2201/R2231/R2306 from 1.3; they add nothing R2156 does not say.

*Rulings (4):* R2156, R2201, R2231, R2306

### [medium] misfiled

R0822 (Hand of Conrad.1) — "The minion cannot use the discipline provided if some effect prevents him to use the equipment (eg. {Drawing Out the Beast})" — is labelled P PRIMARY in 1.3 but says nothing about card types, multi-type cards, locquipments, reflex or clan equipment. Its principle is that an ability granted BY a card is unavailable when use of that card is blocked, i.e. the grant is not independent of its source. That is 1.5 territory (abilities vs. cards, when an ability may be used) and it is the only row in the section with no type question in it at all.

**Recommendation:** Move to 1.5 as PRIMARY. If a cross-reference is wanted it is to 4.10 (equipment in combat, since {Drawing Out the Beast} is the cited blocker), not to 1.3. As a P it is actively harmful here: it invites the 1.3 drafter to write a paragraph the section does not own.

*Rulings (1):* R0822

### [medium] duplicate-template

R0517 (Disputed Territory.2) and R0528 (Dominate Kine.1) are the identical sentence — "If used to steal an equipment representing a location, it can be placed on any minion controlled by the new controller" — with the identical citation [RTR 19960112], and that citation is also the source of the general entry R2582 (Locquipments.1), which states the same rule card-independently. Three copies of one general-entry rule. R0518 (Disputed Territory.3) is a distinct and worthwhile refinement (no move when control "changes" to the same Methuselah).

**Recommendation:** Keep R2582 as the P — the general entry is the right home and the contract explicitly prefers it. Keep R0518, which teaches something R2582 does not. Drop R0517 and R0528 from 1.3; they are secondary here and their PRIMARY home (6.3, where equipment/locations go on a control change) already carries the point.

*Rulings (4):* R2582, R0517, R0528, R0518

### [low] duplicate-template

R1772 (Sunset Strip, Hollywood.3) and R2082 (Shard, London, The.5) are the same sentence with the same two citations, in the same order-insensitive pair: "Can reduce the cost of an action card even if it is not played as an action (ie. a retainer played with {Pack Alpha})". Both are secondary rows. Beyond the duplication, the principle is about a card's type persisting when it is played through some other mode — real 1.3 content, but the cost machinery is 1.7.

**Recommendation:** Keep one (either; they are interchangeable) as an "e.g." illustrating that the printed card type survives an unusual play mode, and confirm 1.7 holds the cost-reduction half. Low severity because both are secondary and cost only tokens.

*Rulings (2):* R1772, R2082

### [low] over-absorbed

R0221 (Body Bag.1) is E PRIMARY but is a pure one-card reading of Body Bag's own text: "Can be equipped by a non-Anarch and would still count as a haven, although the rest of his effect does not apply." The clause "the rest of his effect does not apply" is card-specific bookkeeping that transfers to nothing. The generalisable half — that a non-Anarch may equip despite the requirement — is a requirements rule, not a type rule.

**Recommendation:** Demote to C with 1.6 as the nearest section (requirements to play vs. to keep). If any part is kept it belongs in 1.6, not 1.3; the "still counts as a haven" phrasing is what pulled it here and that is surface vocabulary, not the principle it teaches.

*Rulings (1):* R0221

### [low] thin-section

The taxonomy scope line for 1.3 names four sub-topics — locquipments, reflex cards, clan equipment, multi-type cards. Locquipments draw roughly 15 rulings and multi-type roughly 8, but reflex has exactly ONE ruling (R2597) and clan equipment exactly ONE (R2548). Worse, R2597 is not really about the reflex card type: it says any frenzy card that targets/selects/affects the minion when played is considered played on the minion — a targeting rule that happens to live on the G00060|Reflex general entry. So the drafter has effectively zero material on what a REFLEX card actually is or when it may be played.

**Recommendation:** Tell the drafter these two sub-topics will be one sentence each, not subsections, and expect the section to be locquipment-dominated. If reflex-card timing matters to the document, the material is not in this extract and a targeted search of chapter 2 codes would be needed. Flag for Phase 4.5 alongside the existing 6.8-is-starved note.

*Rulings (2):* R2597, R2548

### [low] other

R1589 (Shackles of Enkidu.6, "Are still considered as an equipment after they are 'activated'") and R2075 (Enhanced Coagulant.3, "Once used, it becomes a typeless card and cannot be used as a weapon anymore") give OPPOSITE answers to the same question — does a card retain its type after being used/activated? Neither carries a !TENSION tag, because each classifier saw only its own chunk. Read together they are not a contradiction but the section's most interesting pair: the type change is governed by the card's own text, not by a general rule about activation.

**Recommendation:** Keep both and present them as a deliberate contrast rather than two isolated examples. This is the one place in 1.3 where the duplication problem inverts — two rulings that look card-specific in isolation become a principle when co-located. No reclassification needed; this is a note for the drafter.

*Rulings (2):* R1589, R2075

## 1.4

### [high] over-absorbed

Four of the section's fourteen rows are {Illusions of the Kindred} (R0888, R0889, R0890, R0892), and three of them are pure internal card-text interpretation rather than representation principles. R0888 ("if the illusionary vampire does not enter combat, then they are removed from the game at the end of the current action") and R0892 ("if the card drawn is an imbued, the imbued would briefly come into play, become incapacitated, and then be removed from the game") are lifecycle mechanics of this one card's own text and fail the transfer test — no other card is ruled differently because of them. R0889 (burned in combat → ash heap instead of removed) is likewise this card's removal clause losing to a burn, filed here as secondary. Only R0890 ("even if they have the same name as a vampire in play, the illusionary vampire is considered different for all purposes") teaches 1.4's actual scope line (name lookups, no contest for placeholders). Leaving all four in gives the drafter the impression that a whole sub-topic exists where there is one datum plus three card notes.

**Recommendation:** Recode R0888 and R0892 as C (nearest code 2.5 for R0888's end-of-action removal). Drop R0889 from 1.4's membership entirely (it is already secondary; its real home is 1.10/5.4). Keep only R0890 from this card, and promote it to the PRIMARY 1.4 slot for the name-lookup/no-contest principle.

*Rulings (3):* R0888, R0892, R0889

### [medium] misfiled

The {Bima} pair is about a card hosted on another card, not about representation. R0147 ("the discipline needs not be announced when Bima is played; the replacement card can be used if it is a discipline") is announcement/replacement timing — 1.9, or 3.1 for the not-fixed-at-announcement half. R0148 ("'that Discipline' refers to the card on Bima; if the card is no longer there, then the effect cannot be used") is the general cards-on-cards principle that an effect referring to a hosted card stops functioning when the host loses it — that is 1.12. Neither card is standing in for something else, so neither exercises 1.4's "loses printed text / name lookup" principle. Together they are 2 of 14 rows pulling the section toward a second, unrelated topic.

**Recommendation:** Move both to 1.12 (cards on cards); add 1.9 as a second code on R0147 for the replacement-card clause. If 1.12's drafter finds them too Bima-specific, R0147 in particular is a defensible C.

*Rulings (2):* R0147, R0148

### [medium] duplicate-template

R0379 ({Compel the Spirit}: "cannot be used if the ally in the ash heap was representing something else while in play (eg. {Khazar's Diary (Endless Night)})") and R1357 ({Pressing Flesh}: "a card burned while representing something else (eg. an ally raised by {Khazar's Diary (Endless Night)}) is not a valid target") are the same wording template on the same underlying case — a card that was a placeholder is not retrievable/targetable as the thing it printed. R1698 ({Spell of Life}) is the informative counterpart, not a third copy: it gives the opposite outcome for a vampire card representing a mummy. Written as three entries this reads as a card list; written as one principle plus its exception it is a complete sub-section.

**Recommendation:** Keep R0379 as the stated principle and cite {Khazar's Diary (Endless Night)} allies once as the e.g.; carry R1698 as the contrasting case (a vampire card representing a mummy is still a vampire card in the ash heap, so {Possession} works and {Compel the Spirit} does not). Drop R1357 to database-only — it is the same sentence on a second targeting card and adds no new distinction.

*Rulings (3):* R0379, R1357, R1698

### [low] misfiled

R1303 ({Père Lachaise, France}: "the crypt card on it is out of play and should be face down") is a set-aside/out-of-play convention (1.14), or cards-on-cards (1.12). The crypt card is not representing anything — it is being stored. Its only tie to 1.4 is that it contrasts with R0016's face-up placeholder convention. Filed as secondary, so this is conservative-side low severity.

**Recommendation:** Drop from 1.4; file under 1.14 (temporarily out-of-play cards) with 1.12 as the alternate. Only retain it here if the drafter explicitly writes the face-up/face-down convention, in which case it is a cross-reference, not membership.

*Rulings (1):* R1303

### [low] thin-section

Two sub-topics named in 1.4's own scope line rest on a single datum each. "No contest for placeholders" appears only as a trailing clause of R0016 ("they do not contest"), reinforced obliquely by R0890; if R0890 is demoted or the Illusions cluster is pruned, the drafter has one sentence. Likewise R1426 ({Reality Mirror}: "cannot be used to bypass restrictions (like Clan restriction or any other play restriction)") is the section's only statement that representation does not launder requirements — a real principle, but co-owned by 1.6, and alone in 1.4.

**Recommendation:** Expect 1.4 to be short. Write the no-contest rule from R0016 plus R0890 as its single worked case and cross-reference 1.13 rather than trying to build a sub-section; treat R1426 as a one-line cross-reference to 1.6 rather than its own paragraph.

*Rulings (3):* R0016, R0890, R1426

## 1.5

### [high] duplicate-template

Fourteen rows — 30% of the section — are the single template "this ability can be used while locked and/or in torpor", recurring across cards with (in several cases) byte-identical wording and identical reference sets. R2378 (Pariah) and R2464 (Tori Longwood) are verbatim copies of each other and of the general entry R2562 (G00027|Ability usable in torpor), all three citing [LSJ 20011022] [LSJ 20100902-2]. R2355 (Montano), R2383 (Paul Forrest) and R2461 (Toby) are three verbatim copies of "can be used while locked or in torpor", all citing [ANK 20220705] [LSJ 20100705]. No classifier could see this from inside its chunk; every one of them labelled it correctly and consistently, which is exactly why the redundancy survived.

**Recommendation:** Keep R2562 (the G00027 general entry) as the P that states the rule, plus at most two examples — R2355 covers locked-and-torpor in one card, R1090 (Make an Example, [PIB 20150720] [RTR 19941109]) covers locked-only with the oldest citation trail. Let the other eleven stay in the rulings database; they add citations, not content. If the drafter wants breadth of citation, footnote the extra reference IDs under the single principle rather than promoting extra "e.g." cards.

*Rulings (14):* R2562, R2378, R2464, R2321, R2329, R2355, R2383, R2461, R0624, R1090, R1200, R2331, R2440, R0410

### [high] duplicate-template

Twelve rows are the template "this ability may be used more than once per action / per turn". Read together they are not twelve examples but three distinct sub-rules with heavy duplication inside each: (a) unrestricted reuse within one action — R0404, R2177, R2196, R2216, R2330, R2344, R2415, seven copies of the same statement; (b) reuse gated on re-unlocking, because the ability locks its bearer — R0722 ("it must be unlocked by some method, of course") and R2243 ("at the rate of one each unlock"); (c) reuse keyed to the number of phase windows available — R2263 (multiple discard phase actions) and R2360 (multiple master phase actions). Sub-rule (a) is currently absorbing seven rows for one sentence.

**Recommendation:** Keep one representative per sub-rule: R0404 (Corpse Minion, the cleanest general statement, [TOM 19960109]) for (a); R0722 (Forest of Shadows) for (b); R2263 or R2360 for (c). Keep R2374 (Osric Vladislav) as the one qualified case — reuse permitted "but only if he is acting and stealth is needed" — since it is the only row showing the limit is read off the ability's own conditions. Drop R2177, R2196, R2216, R2330, R2344, R2415 to C: R2196 in particular is unusable as written, since it names a second card ({Enid Blount}) and states nothing the template does not.

*Rulings (12):* R0404, R0722, R2177, R2196, R2216, R2243, R2263, R2330, R2344, R2360, R2374, R2415

### [medium] duplicate-template

Six rows carry the identical boilerplate "[REACTION] Can be used only when reactions can be used (unlocked or with a wake effect). It does not count as playing a reaction card. [LSJ 20070403] [LSJ 20070413]" across Champion, Discern, Donate, Hide, Surge, and (with a variant clause) Vigilance. All six are labelled P/PRIMARY, so the extract hands the drafter six statements of one principle. R1975 (Vigilance) is the only one that differs: "[1 CONVICTION] ... when reactions can be used (during an action)", i.e. the Imbued conviction-power form where the lock/wake condition does not apply.

**Recommendation:** Keep one of the five identical rows as the P — R0310 (Champion) is as good as any — and keep R1975 as the single variant example, since the "during an action" phrasing is the only place the extract shows that the requirement tracks the reaction *window*, not the unlocked state per se. Send the other four to C. This cluster pairs naturally with R1242 (No Secrets From the Magaji: an ability grant "is not a wake") as the contrapositive; cross-reference rather than expand.

*Rulings (6):* R0310, R0513, R0529, R0858, R1776, R1975

### [medium] missing-topic

The lock half of the section has nine card examples and no principle. Torpor has a general entry (R2562 = G00027|Ability usable in torpor) that states the rule with no card doing the work; the parallel "an ability may be used while its bearer is locked" has no general-entry row and no P — every locked row (R0624, R1090, R1200, R2331, R2440, R0410) is an E on a named card. A drafter writing from this extract will state the torpor rule from a rule and the lock rule by induction from six cards, which is where over-broad or under-broad phrasing gets introduced. Separately, the section's headline principle ("ability use is not a card play") is evidenced only on the cost side — R1529 (Safe Passage: additional cost does not apply to reaction powers) and R1563 (Secure Haven: no additional cost for using effects of cards already in play) — with nothing on whether effects that cancel or prevent *card plays* reach ability use. R0547 (Drum of Xipe Totec) is the only row touching ability prevention and it comes at it from the equipment side.

**Recommendation:** Flag both gaps to the drafter rather than reclassifying anything. For the lock rule, note that no general entry exists and the prose must be induced from the examples — worth a ⚠ REVIEW marker. For cancellation/prevention of ability use, check whether the relevant rulings landed in 1.8 (playing & canceling) as PRIMARY and never got 1.5 as a secondary code; if so, that is a routing loss 1.5 cannot recover from its own extract.

*Rulings (6):* R0624, R1090, R1200, R2331, R2440, R2562

### [low] recoverable-C

Two rows read as one-card text interpretations rather than illustrations of a 1.5 principle. R1273 (Ossian.3): "The Auspex [aus] special applies to whatever the current action is, not just to his special enter combat action" — this resolves an ambiguity created by Ossian having two printed abilities on the same card; it changes no ruling on any other card. R1603 (Shadow Court Satyr.2): "Can choose to use any single discipline effect of a split discipline card, each time he uses it" — the transferable core (the branch of a split-discipline card is chosen fresh at each use) is real but is a reading-card-text point, closer to 1.1 than to abilities-vs-cards. Both are marginal, not clear errors.

**Recommendation:** Treat R1273 as C on the transfer test unless the drafter wants to state "abilities printed on the same card are independent in scope" as a rule — in which case it needs a second instance, and there is none in this extract. Leave R1603 where it is or move it to 1.1; either way do not spend an "e.g." slot on it.

*Rulings (2):* R1273, R1603

### [low] misfiled

R0993 (Kiss of Ra.1, secondary): "Can be played by an acting vampire in torpor." This is about playing a *card* while in torpor, which is the opposite side of the distinction 1.5 exists to draw — the section's principle is that ability use is not a card play, and every other torpor row here is an ability. Its natural owner is 5.3 (torpor: what is usable in torpor). It is filed secondary, so this is a low-confidence call and the row is defensible as a deliberate contrast case.

**Recommendation:** Leave it in the extract only if the drafter intends an explicit contrast sentence ("abilities are usable in torpor by default; card plays are not, unless the card says so"). Otherwise it belongs to 5.3 alone and should be a cross-reference, not membership.

*Rulings (1):* R0993

## 1.6

### [high] duplicate-template

The 'requirement-faker' vampire cluster (Mata Hari / Vidal Jarbeaux / Vlad Tepes class) contributes ~45 rows to 1.6, of which 27 are three sentences of verbatim boilerplate repeated across 13 different vampires. Template A1 [ANK 20190228], 11 copies: 'When playing a card requiring X, he is treated as such for all effects of the card, and only them, including duration effects. He is not treated as such for effects the card has from being in play' (R2214 Gem Ghastly, R2273 Kemintiri, R2296 Lisandro Giovanni, R2337 Mata Hari, R2386 Petaniqua, R2391 Philip van Vermeer IV, R2450 Tatiana Stepanova, R2474 Victor Gerard, R2476 Vidal Jarbeaux, R2488 Vlad Tepes, R2510 Winterlich). Template A2 [LSJ 20050119], 11 copies: 'ability does not let him fulfill card requirements if they are not played normally, like when using {Piper}' (R2215, R2298, R2343, R2388, R2392, R2451, R2487, R2490, R2512, R2531, R2534). Template A3 [LSJ 20050225], 5 copies: 'You can still use the burn options of cards with a requirement he could meet when you play them, but does not meet while in play' (R2297, R2342, R2387, R2486, R2511). No chunk could see this; each agent saw one or two copies and labelled them P/E in good faith.

**Recommendation:** Collapse to one principle with two named vampires. State the faker rule once — the ability substitutes for the requirement only for the effects of the card played, including its duration effects, and never for what the card does from being in play — citing {Mata Hari} and {Vidal Jarbeaux}. Keep R2337 + R2476 for A1, R2343 for A2 (abnormal entry does not invoke the faker ability), R2342 for A3. Drop the other 24 to C/database. Vlad Tepes is worth keeping only as the title-specific worked example (see the title-sub-template finding), not as a fourth copy of A1.

*Rulings (27):* R2214, R2273, R2296, R2337, R2386, R2391, R2450, R2474, R2476, R2488, R2510, R2215, R2298, R2343, R2388, R2392, R2451, R2487, R2490, R2512, R2531, R2534, R2297, R2342, R2387, R2486, R2511

### [high] duplicate-template

'Requirements do not apply when taking control of a card already in play.' [TOM 19960226-1] appears 12 times, byte-identical, on 12 different cards ({Art of Love}, {Book of Going Forth by Night}, {Far Mastery}, {Legend of the Leopard}, {Lure of the Serpent}, {Malkavian Time Auction}, {Putrescent Servitude}, {Reality Mirror}-adjacent, {Restructure}, {Revelation of Ecstasy}, {Set's Call}, {Spirit Marionette}, {Transfusion}). This is the clearest cross-chunk drift signal in the unit: nine copies were filed as `secondary` to 1.6 (correctly deferring to 6.3, whose scope line literally reads 'Taking control of cards in play: requirements don't apply'), but three — R1032, R1069, R1099 — were made PRIMARY 1.6 by their chunks. Identical text, contradictory primaries.

**Recommendation:** Resolve to 6.3 PRIMARY for all twelve, 1.6 secondary. 1.6 should carry one cross-reference sentence ('requirements are checked on play; taking control of a card already in play is not a play — see 6.3') and no card list. Re-file R1032, R1069, R1099 to match the other nine.

*Rulings (12):* R0085, R0237, R0651, R1032, R1069, R1099, R1400, R1469, R1473, R1579, R1702, R1884

### [medium] duplicate-template

An eleven-ruling 'a card cannot be played where it would do nothing' family sits in 1.6, and it is both a duplicate template and a probable seam. Five are verbatim identical [LSJ 20001114]: 'Cannot be used if there is no damage to prevent' (R1634 {Sideslip}, R1646 {Skin of Night}, R1647 {Skin of Rock}, R1671 {Soak}, R1736 {Stonestrength}). Six more are the same principle on other objects: R1623 {Shattering Blow} 'no equipment to destroy', R1991 {Vulture's Buffet} 'no minion or retainer in any ash heap', R1923 {Undue Influence} 'no vampire in the uncontrolled region', R1046 {Liquidation} 'less than 7 cards in your library', R1738 {Storage Annex} 'only card in your hand', R1715 {Spying Mission} 'cannot increase an unsuccessful bleed of zero'. Note the same PRIMARY/secondary drift: the five prevention copies are all secondary, but R1623, R1046, R1738, R1991 were made PRIMARY 1.6. Separately, this is arguably not 'requirements' at all — a requirement is a printed prerequisite (clan, discipline, capacity, title), whereas 'there must be something for the card to act on' is a playability question owned by 1.8 (already drafted) and flagged in calibration as the `no-effect-plays` topic.

**Recommendation:** Decide the seam first: if 1.8 owns no-effect plays, move all eleven there and leave 1.6 a cross-reference. If 1.6 keeps them, they are ONE principle with three examples — keep R1671 {Soak} (or any one prevention card), R1991 {Vulture's Buffet}, R1738 {Storage Annex} — and the other eight go to the database. Either way the four PRIMARY assignments must be reconciled with the five secondary ones.

*Rulings (11):* R1634, R1646, R1647, R1671, R1736, R1623, R1046, R1738, R1923, R1991, R1715

### [medium] duplicate-template

Six rulings state one rule: a card placed on a minion that cannot legally bear it is burned. Four share the reference [LSJ 19980831] — R1517 {Rowan Ring}.5 and R2037 {Wooden Stake}.1 are word-for-word identical including the trailing 'The "does not unlock as normal" effect still applies', R1584 {Shackles of Enkidu}.1 is the same minus that clause, R0837 {Heidelberg Castle}.2 is the same rule stated from the placing card's side. R1954 {Vast Wealth}.4 ('burned without cost') and R0873 {Horrid Reality}.2 ('if the weapon retrieved has requirements the vampire does not meet, then it is burned') add the two useful riders — no cost refund, and the requirement itself as the disqualifier.

**Recommendation:** One principle, two examples. Keep R0873 {Horrid Reality} (requirement-based disqualification, the case actually about requirements) and R1954 {Vast Wealth} (burned without cost). Cite {Wooden Stake} inline as the e.g. for the 'residual in-play effect still applies' rider via R2037 only if the drafter needs it; drop R1517, R1584, R0837.

*Rulings (6):* R1517, R1584, R2037, R0837, R1954, R0873

### [medium] duplicate-template

The requirement-to-play vs. requirement-to-use distinction — the strongest material in the section — is carried by four copies of one [LSJ 20030607] template: R0025 {Agate Talisman} 'capacity less than 4, although they cannot lock it to get a vote', R0163 {Blade of Enoch} 'capacity less than 6, although he cannot use it to strike', R1553 {Seal of Veddartha} 'capacity less than 6: he cannot use it to bleed but the disciplines bonus applies', R0422 {The Crusader Sword} 'can be equipped by a minion who cannot use it'. R0623 {Exile} is the same shape on a lock-cost. R1268 {Orun}.3 is the only ruling in the unit about a capacity requirement CHANGING after the fact.

**Recommendation:** Keep two: R1553 {Seal of Veddartha} (best — shows which parts of the card still work and which do not) and R0422 {The Crusader Sword} (the bare statement of the split). Drop R0025, R0163, R0623 to the database. R1268 is not a duplicate and must be kept — see the thin-section finding.

*Rulings (6):* R0025, R0163, R0422, R1553, R1268, R0623

### [medium] duplicate-template

Eleven further small templates, each recurring 2-5 times across chunks. (a) 'Only requires one clan or the other (Tremere/Tremere antitribu)' [ANK 20190203] x5: R0469, R0486, R1330, R1450, R1687. (b) 'Can be used to meet one (not both) of the Discipline requirements of a multi-Discipline card' x3: R0912, R0920, R2244. (c) 'The requirements and cost of the ally/retainer do not count as requirements nor cost for the action (eg. {CrimethInc.})' [LSJ 20100725] x3: R0950, R1208, R1766. (d) 'Requirements need not be met; inferior discipline version; X is zero' [LSJ 20071015] x2: R0378, R1355. (e) 'ability works on allies recruited in a non-standard way (eg. {Piper})' [ANK 20210913] x3 + R1688: R2300, R2423, R2522. (f) 'not equipped but merely put into play (eg. {Alastor}) → the equip-triggered clause does not fire; it does if equipped (eg. {Magic of the Smith})' [LSJ 20090506] x2: R0915, R1629 (R0842/R0843 {Helicopter} are the same rule again). (g) 'applies when equipping in a non-normal way' [PIB 20150105-2] x2: R2444, R2462. (h) 'burn option can be used if all your infernal vampires are in torpor' [LSJ 20091203] x2: R1938, R1967. (i) 'A card requiring a Baron is a card requiring an Anarch' x3: R0750, R2414, R2572. (j) 'can meet a title requirement even if the sect does not exist anymore' [LSJ 20050124] x3: R2274, R2482, R2494. (k) 'does not get the title's votes for the subsequent referendum' [ANK 20231221] x2: R2481, R2493; plus 'meeting a title requirement implies the underlying sect' x3: R2480, R2491, R2277; and 'Cannot play cards requiring a Baron' [PIB 20151116] x2: R2153, R2154.

**Recommendation:** Keep exactly one representative per template and drop the rest. Suggested keepers: (a) R0469, (b) R0920, (c) R1766, (d) R0378, (e) R2300, (f) R1629, (g) R2462, (h) R1938, (i) R2572 (the general entry G00037 — always prefer the general entry over its card copies, per the contract), (j) R2482, (k) R2480 (which already bundles the title sub-rules into one dense ruling). That is 11 kept, 25 returned to the database. R2480 {Vidal Jarbeaux}.5 is the single best title ruling in the unit and can carry the whole title sub-topic on its own.

*Rulings (36):* R0469, R0486, R1330, R1450, R1687, R0912, R0920, R2244, R0950, R1208, R1766, R0378, R1355, R2300, R2423, R2522, R1688, R0915, R1629, R2444, R2462, R1938, R1967, R0750, R2414, R2572, R2274, R2482, R2494, R2481, R2493, R2480, R2491, R2277, R2153, R2154

### [medium] over-absorbed

Eight rulings are P/E but restate one card's own text or one card's private mechanics. R2508 {White Lily}.1 is P PRIMARY and reads in full 'Requirements need to be met.' — it states no principle, it answers one card's question; R1206 {Muricia's Call}.1 ('Requirements must be met to employ the retainer') and R1284 {Pack Alpha}.1 ('Requirements (clan, discipline) apply') are the same non-content on two more cards. R0045 {Ananasi Vampirephile}.2 ('Can use {Pack Alpha} to put a retainer requiring [ani] in play') is a two-card worked example of R1284 and adds nothing. R1103 {Malleable Visage}.2 ('Requires a ready, unlocked vampire') restates the card line. R1624 {Shattering Crescendo}.1 ('Requires to have the second in hand to play it') fails transfer — no other card has this requirement. R0585 {Emerald Legionnaire}.2 is a four-clause compound every clause of which is Emerald Legionnaire specific ('does not require a ready Harbinger, the pool cost of the new one is not paid, the new one can act this turn and can use his ability to bring another one immediately'). R2276 {Kemintiri}.5 ('Does not enable you to play master cards, it only enables her to play certain minion cards') is a reading of Kemintiri's own text scope, and it sits beside R2477 {Vidal Jarbeaux}.2 ('can meet the requirements for his controller to play any card, including Master cards') — the pair teaches nothing except that the two cards are worded differently.

**Recommendation:** Recode all eight C. Retain at most R1284 {Pack Alpha} as the single e.g. for the default ('requirements apply unless the effect says otherwise'), since the section needs one positive instance to anchor the negative cases. R2477 {Vidal Jarbeaux}.2 stays — it is the general statement that the faker ability is not restricted to minion cards; R2276 is only its card-specific counterpoint.

*Rulings (8):* R2508, R1206, R1284, R0045, R1103, R1624, R0585, R2276

### [low] misfiled

Three rulings have no requirements content. R1684 {Soul Gem of Etrius}.4 ('if the drawn vampire B is younger and would be put into play with Gem but is burned instead (self-contesting), then the Gem activates again, drawing a new vampire C and comparing his capacity to B's capacity') is about re-activation and capacity comparison — it mentions no requirement at all and belongs to 1.13 contests / 6.7 crypt, not 1.6. R1715 {Spying Mission}.3 is a bleed-timing and burn-condition ruling belonging to 3.7.1 (its only 1.6-adjacent clause, 'cannot be used to increase an unsuccessful bleed of zero', is the no-effect-play family covered above). R0706 {Force of Will}.3 ('{Mask of a Thousand Faces} cannot be used to take over, since it requires an unlocked vampire and the action requires a locked one') is PRIMARY 1.6 but is the textbook case for 3.10, whose scope line reads 'eligibility keyed to what the substitute could independently have done'.

**Recommendation:** R1684 → C, or 1.13 secondary. R1715 → 3.7.1 PRIMARY, drop from 1.6. R0706 → 3.10 PRIMARY, 1.6 secondary (it is a legitimate cross-reference here, just not this section's to own). All three are low-cost: R1684 and R1715 are already `secondary` rows, so the damage is extract padding rather than a lost ruling.

*Rulings (3):* R1684, R1715, R0706

### [low] thin-section

1.6's scope line promises three sub-topics; one is nearly unevidenced. 'Requirements to play vs. to keep' is well covered (R2544 G00009 {Require Gehenna} states it generally — 'the "other Gehenna cards in play" requirement is only checked when playing the card'; R1911 {Undead Persistence}.3 shows a requirement re-checked on a second play; R2299 {Lisandro Giovanni}.4 shows a faker ability lapsing outside play). 'Abnormal entry ignores requirements' is over-covered. But 'capacity/discipline requirement changes' — a requirement's satisfaction changing after cards are already in play — rests on R1268 {Orun}.3 alone ('the capacity bonus applies to cards played before the Orun was played'). No ruling addresses the converse: a capacity or discipline REDUCTION after a card requiring it is already in play. The drafter will have one data point and will be tempted to generalise from it in both directions.

**Recommendation:** Flag for the drafter: state the retroactive-satisfaction rule from R1268 narrowly (a later capacity gain validates cards already played) and mark the reverse case ⚠ REVIEW rather than inferring symmetry. If Phase 4 wants this covered, the rulings likely live under 5.1 (capacity changes) rather than 1.6 — worth a targeted check of 5.1's membership for a ruling that belongs here as a secondary.

*Rulings (4):* R1268, R2544, R1911, R2299

## 1.7

### [high] duplicate-template

The ANK 20210226 boilerplate "The burn blood effect is not reduced by effects that reduce the cost of the card (eg. {X}). The card cannot be played if the minion cannot afford to burn the blood." appears 13 times, verbatim except for the parenthetical card, spread across 13 chunks — and every single copy is labelled P/PRIMARY, so 13 rulings all claim to STATE the same principle. R2605 (G00065|Burn blood for effect.1) is the general-rule entry saying exactly this with no card doing the work; the other 12 are card copies that under the contract should be E.

**Recommendation:** Keep R2605 as the single P (it is the general entry and its wording is the rule verbatim). Demote the 12 card copies to E and carry at most three as "e.g." — suggest R1600 {Shadow Boxing} (action modifier), R0099 {Aura Absorption} (reaction), R1359 {Preternatural Evasion} (pairs with R1358, which supplies the when-is-it-burned half). Drop the remaining nine to the database. Draft the principle alongside its converse pair R2194 ({Dragos}: a burn-blood effect on a combat card is not a cost) and R1845 ({Terror Frenzy}: an additional-cost effect DOES stack with cost reductions) — together those three are the whole cost-vs-burn-blood distinction.

*Rulings (13):* R2605, R0099, R0636, R0696, R0821, R1112, R1113, R1286, R1359, R1420, R1533, R1578, R1600

### [high] duplicate-template

{The Line}, {Powerbase: Tshwane}, {Sunset Strip, Hollywood}, {The Shard, London} and {Eccentric Billionaire} are the same lock-to-reduce-cost card printed four/five times, and each contributed near-verbatim rulings for four sub-templates: (a) "Can be locked to reduce the cost at any point before resolution, from when the action is announced to just before the cost is paid" = R1042/R1345/R2079 plus the older phrasing R0565/R1770; (b) "Can reduce the cost of an action card even if it is not played as an action (ie. a retainer played with {Pack Alpha})" = R1044/R1347/R1772/R2082; (c) "Can be used to allow to play cards which cost could not be paid otherwise" = R1346/R2080/R1771; (d) "The cost reduction applies to minion cards, they are also played by the Methuselah" = R1344/R2078. Seventeen rulings carrying four principles.

**Recommendation:** Four principles, one exemplar each. (a) keep R1345 and cite R1771 {Sunset Strip} only where the exception bites (it must be locked at ANNOUNCEMENT when the card is otherwise unaffordable — that is a genuine refinement of the same rule, not a duplicate). (b) keep R1347, drop the other three; it is the same rule as R1285 {Pack Alpha}.2 and R1688 {Soul of the Earth}.2, so state it once as "reductions keyed to a card's cost apply however the card is played" and contrast with R1314/R2133, which say reductions keyed to an ACTION do not. (c) keep R2080. (d) keep R1344. Retain R1045 and R2081 separately — they are the ally/blood-cost edge, not copies.

*Rulings (18):* R0565, R1042, R1345, R1770, R2079, R1044, R1347, R1772, R2082, R1346, R1771, R2080, R1344, R2078, R1045, R2081, R1043, R1285

### [medium] duplicate-template

Five byte-identical rulings — "If it is canceled, any blood cost (eg. {Terror Frenzy}) has to be paid. [PIB 20121031]" — on {Target Hand}, {Target Head}, {Target Leg}, {Target Retainer}, {Target Vitals}, one per card in the same cycle. All five are secondary here (1.8 presumably owns them), so 1.7 is carrying five copies of one cross-reference.

**Recommendation:** Keep one (R1804 {Target Head}) as the cross-reference to 1.8's canceled-card-still-pays rule; the other four are the same card cycle and add nothing. Note the co-located R2416 ({Santaleous}.2) and R1798-adjacent R0504 ({The Diamond Thunderbolt}.3) state the same principle from the canceling side — 1.7 should cross-ref 1.8 rather than restate it.

*Rulings (5):* R1800, R1804, R1807, R1810, R1813

### [medium] duplicate-template

"A vampire with no blood can still block, they burn what they can. [LSJ 19970707]" appears verbatim three times (R0074 {Archon}, R0274 {Camarilla Exemplary}, R1523 {Sabbat Priest}), and R2187 ({Dónal O'Connor}.1) is the same rule reworded from a different source. Four rulings, one principle: a blood cost imposed on blocking does not gate the block; you pay what you can.

**Recommendation:** Keep R1523 as the P statement and one card as the "e.g."; drop the other two verbatim copies. Keep R2188 separately — it adds real content (the blood is burned immediately on a successful block, regardless of whether combat begins) and is not a duplicate. This whole sub-cluster (R0709, R0711, R1036, R1529, R1842, R1935, R2187, R2188) is costs imposed on blocking; it is legitimately 1.7 but should be drafted as one paragraph cross-referencing 3.3, not as eight separate points.

*Rulings (5):* R0074, R0274, R1523, R2187, R2188

### [medium] duplicate-template

The taxonomy's widened 1.7 scope line ("effects naming an amount the target may not hold (steal/transfer templates take what is there)") is illustrated six times. R1159 {Minion Tap}.2 and R1979 {Villein}.3 are verbatim identical ("If the target has less blood at resolution than the amount announced, you take what you can"); R1849 {Theft of Vitae}.1 and R1866 {Tongue of the Serpent}.1 are verbatim identical ("Can target a minion with less blood [or life] than the amount stolen"); R1752 {Succubus}.1 is the same rule again. Two wordings, five cards.

**Recommendation:** One principle, two examples: keep R1979 {Villein} (announced-amount template) and R1849 {Theft of Vitae} (targeting template, and it covers the life case). Drop R1159, R1866, R1752. Keep R1781 {Sword of Nuln}.1 separately — it teaches the non-obvious half (partial payment is made but does NOT achieve the effect), which none of the others state.

*Rulings (6):* R1159, R1979, R1849, R1866, R1752, R1781

### [medium] over-absorbed

Four consecutive {Nergal} rulings (R2366-R2369) are P/E in 1.7, all four citing the single reference [LSJ 20091021-2], and three of them are pure interpretations of that one vampire's once-per-turn pay-ability: "he can choose whether or not to use his ability", "his ability is not considered used for the action (even if it was announced)", "his ability is not considered used for the turn". Nothing about when Nergal's ability counts as spent transfers to any other card. R2504 ({Watenda}.1, "The cost he pays takes into account any cost modification that applies for the opposing minion") is likewise unintelligible away from Watenda.

**Recommendation:** Keep R2366 only — "an ability that funds a cost must be used at the moment the cost is actually paid (at resolution), not at announcement" is a real timing principle and pairs with R0565/R1345 on the other side. Reclassify R2367, R2368, R2369 and R2504 as C; per the contract's own C test they fail transfer, and per the style rules they are one-card text interpretations that stay in the database.

*Rulings (5):* R2366, R2367, R2368, R2369, R2504

### [medium] duplicate-template

{Kindred Segregation} and {Peace Treaty} generate the same two rulings each, from the same source pair. R0985/R1295 are the same rule ([RTR 20010710]: only the POOL cost must be paid to keep the card; blood costs need not be repaid) applied to allies and to weapons. R0987/R1297 are the same rule again ([ANK 20190724]: you may elect to burn a card with no pool cost rather than 'pay zero').

**Recommendation:** State each principle once with one card. Keep R0985 {Kindred Segregation} (it carries the ally/blood-cost case explicitly) and R0987 for the pay-zero-is-still-a-choice point; drop R1295 and R1297, or cite {Peace Treaty} as a bare second 'e.g.' without a second footnoted statement. R0988 (Imbued have a pool cost to recruit of zero) is a genuine third case and should stay.

*Rulings (4):* R0985, R1295, R0987, R1297

### [low] duplicate-template

Residual exact-duplicate pairs and triples, each carrying one principle across two or three cards. Cost arithmetic order (R0064 {The Ankara Citadel} and R1853 {Thin-Blooded Seer} are verbatim identical, both P/PRIMARY, both citing RTR 20070707). X-is-zero on cards put into play without being played (R0378 {Compel the Spirit} and R1355 {Pressing Flesh} verbatim identical; R1763 {Summon History} the same rule). Affordability gate (R0618 {The Eternals of Sirius} and R1978 {Villein} verbatim). Card-provided action does not carry the rulebook action's default blood cost (R0778 {Go Anarch} and R0832 {Healing Touch} verbatim). Reduction is visible to other effects reading a card's cost (R2160 {Black Cat} and R2249 {Ivan Krenyenko} verbatim). Reduction applies to equipment that is a location (R1851 {Therbold Realty} and R2324 {Marie Faucigny} verbatim; R2535 {Regina Blake} the same). Allies have life not blood and cannot pay blood costs (R0368, R1843, and R1045 as the acting-as-a-vampire variant).

**Recommendation:** Keep one per pair: R1853, R0378, R1978, R0778, R2160, R1843. For X-is-zero, lead with the general entry R2567 (G00032|Cost X.1, "X can be zero") and cite R0378 as the e.g. For the location-equipment reduction, lead with the general entry R2584 (G00047|Locquipments.3) — but that is 1.3's material, so 1.7 should cross-reference 1.3 and keep at most one e.g. rather than three footnoted statements.

*Rulings (18):* R0064, R1853, R0378, R1355, R1763, R2567, R0618, R1978, R0778, R0832, R2160, R2249, R1851, R2324, R2535, R2584, R0368, R1843

### [low] misfiled

R2250 ({Jaggedy Andy}.1, "If he goes to torpor and their controller cannot discard two cards, they discard as many as they can") is P/E and PRIMARY in 1.7, but a forced discard is not a cost and no payment occurs. It was pulled in on the surface resemblance to pay-what-you-can (R1781, R1848, R1660), which is the exact failure golden rule 3 warns about.

**Recommendation:** Move to 6.9 (hand, draw & discard), which owns discard mechanics and 'which card may be discarded'. If 1.7 wants the pay-what-you-can-generalises point at all, it should cross-reference rather than own this ruling.

*Rulings (1):* R2250

### [low] misfiled

Four secondary rows carry no cost or payment content. R0503 ({The Diamond Thunderbolt}.2) and R1422 ({React with Conviction}.2) are a matched pair about how far a cancellation reaches into a {Corruption} action — that is 1.8's scope-of-cancellation question, and the cost half is already carried by R0504. R0996 ({The Kiss of Ra}.4, "The action was still taken (eg. counts against {Enkil Cog})") is about an action having been taken, with no cost mentioned. R2184 ({Dominique}.1, "If a location costs X blood, it would take X vandal counters to burn it") uses cost only as a reference value, and the taxonomy's 1.12 scope line explicitly claims it ("burn thresholds keyed to another value (eg. vandal counters vs. a location's blood cost)").

**Recommendation:** Drop R0503, R1422 and R0996 from 1.7 (1.8 and 3.4/3.5 own them as PRIMARY and the drafter needs no cost-side cross-reference). Drop R2184 to 1.12 per its own scope line. These are conservative calls on secondary rows, but none of the four would give a 1.7 drafter anything to write.

*Rulings (4):* R0503, R1422, R0996, R2184

### [low] over-absorbed

Three rulings that are P/E here but read as one-card text interpretation. R0120 ({Banshee Ironwail}.1, "Triggering the burn blood effect does not force the minion to strike with the weapon") decouples one weapon's own two clauses. R1060 ({Loving Agony}.6, "The blood to unlock can be paid until the end of combat, including after other effects that are played at the end of round") is a window specific to that card's optional unlock. R1695 ({Spell of Life}.1, "The copies you burn need not be ones you control") is an interpretation of one card's burn clause.

**Recommendation:** Reclassify as C, or at minimum do not footnote them as principles. R1060 is arguably 4.9 material (end-of-round vs end-of-combat windows) if any section wants it; R1695 has no owner and is fine in the database. Low confidence on R1695 — if the drafter wants a 'costs paid in cards need not be yours' line it is the only evidence, but one instance is not a principle.

*Rulings (3):* R0120, R1060, R1695

### [low] missing-topic

Two sub-topics a 1.7 drafter will reach for and find nothing. (1) No ruling addresses the floor on cost reduction — whether a reduction below zero is capped at zero and whether it ever produces a gain. R2567 ("X can be zero") is adjacent but is about variable costs, not about reductions overshooting, and the section is otherwise dense with reduction rulings (R1344-R1347, R2078-R2082, R2160, R2249, R1851). (2) There is no general-rule entry stating the base rule for WHEN a cost is paid; the section must induce it from card instances (R1358 blood burned when playing the card, R1658 additional cost paid at the same time as the normal cost, R2467 additional cost not paid if the action does not succeed, R0709 blocking cost paid when the action begins to resolve).

**Recommendation:** Flag for the drafter: the when-is-a-cost-paid opening paragraph will have to be synthesised from card examples with no general-entry footnote available, and any statement about reductions hitting zero is currently unsupported by any ruling in this membership. Do not manufacture either from the base rulebook without marking it — this is a place for ⚠ REVIEW.

*Rulings (4):* R2567, R1358, R1658, R2467

## 1.8

### [high] duplicate-template

Five verbatim copies of the 'library-search card cannot be used during the as-played window' template (Admonitions, The Barrens, Dreams of the Sphinx, Erciyes Fragments, Fragment of the Book of Nod), all citing the identical reference [RTR 20040501] — and the general entry R2593 (G00058|Cancel.1) already states the principle in full AND names two of the five cards itself. Cross-chunk drift is visible in the roles too: R0023 and R0124 are labelled P while R0543/R0601/R0733 with byte-identical text are labelled E, violating golden rule 5 (identical rulings must get identical labels).

**Recommendation:** Draft from R2593 as the P (it states 'Cards are not replaced during the "as played" window. The cancelation must be played immediately: no other effects can be used, except for wakes'). Keep at most two of the five card copies as the 'e.g.' — {The Barrens} and {Dreams of the Sphinx}, since R2593 already cites them. Return R0023, R0601, R0733 to the database as C.

*Rulings (6):* R0023, R0124, R0543, R0601, R0733, R2593

### [high] duplicate-template

The 'Target' strike-modifier cycle contributes five byte-identical rulings — 'If it is canceled, any blood cost (eg. {Terror Frenzy}) has to be paid.' [PIB 20121031] — on Target Hand, Target Head, Target Leg, Target Retainer and Target Vitals. These are one card cycle with one shared wording template, not five examples. The same principle (a canceled card's cost is still paid) is independently stated by R0504 and R2416 and refined by R2505.

**Recommendation:** State the principle from R2416 ({Santaleous}: 'the cost of the canceled card must still be paid') and R0504 ('Any bids made are paid. Any counters burned are still burned'), then cite the Target cycle ONCE as a single 'e.g.' — the cycle is one template, so name it as such rather than enumerating members. Drop four of R1800/R1804/R1807/R1810/R1813 to C.

*Rulings (8):* R1800, R1804, R1807, R1810, R1813, R0504, R2416, R2505

### [high] duplicate-template

Eight rulings all teach the single principle 'a card put into play by an effect was not played in the normal fashion and therefore cannot be canceled as it is played'. R2599 (G00061) states it generally. R1759 and R2145 restate it verbatim for masters and minions respectively (both [RTR 20001020]). Worse, R1317, R1768 and R2520 are three copies of the identical ally sub-case ({Piper}, {The Summoning}, {Zhenga}), two of them sharing reference [ANK 20201229] and both naming {Louhi} as the failed canceller.

**Recommendation:** Keep R2599 as the P. Keep R1759 (master-side) and ONE of the three ally cases as the 'e.g.' pair; R1606 ({Shadow Court Satyr}) earns its place separately because it carries the genuine exception ('except if it is part of the card effect'). Drop R2145, and two of R1317/R1768/R2520, to C. R0931 ({Inscription}) is a distinct enough sub-case (card burned off a host) to keep, but should carry 1.12 as a secondary.

*Rulings (8):* R2599, R1759, R2145, R1606, R2520, R1317, R1768, R0931

### [medium] duplicate-template

Four copies of the 'Do Not Replace Until clause is canceled with the card, which is then replaced normally' rule, three of them citing the same [LSJ 20011023]. All four are labelled P, so four separate rulings all claim to state the same principle — the drafter receives one sentence four times.

**Recommendation:** Keep R2594 (G00058|Cancel.2) as the P; it is the general entry and is the only one that also covers the alternate-replacement case ({Steely Tenacity}). R2143 is a duplicate of R2594 including the {Steely Tenacity} clause — drop it. Keep at most one card instance as an 'e.g.'

*Rulings (4):* R2594, R0502, R1423, R2143

### [medium] duplicate-template

Six further two-member template pairs, each a single wording appearing on two cards: canceled Trifle grants no extra master phase action (R1760/R2006, shared ref [LSJ 20090126]); opponent may wake as the card is played (R0463/R1378, shared ref [ANK 20231028]); the effect must apply before anyone can play another cancellation (R1960/R2121, identical text, shared refs [LSJ 20100728] [LSJ 20090213]); canceling a strike means another strike is chosen (R0459/R2142, shared ref [LSJ 20100206]); canceling a limited effect does not trigger the limit (R2144/R2596, shared ref [LSJ 20030224]); cancels reach cards played at end of round (R0240/R0460).

**Recommendation:** Collapse each pair to one 'e.g.'. For the limited-effect pair prefer the general entry R2596 over R2144. For the strike pair prefer R0459 (it carries the [RBK cancel-a-card] anchor). The R1960/R2121 pair is the only evidence in the whole section for cancellation-priority ordering, so keep one and see the 'missing' finding below.

*Rulings (12):* R1760, R2006, R0463, R1378, R1960, R2121, R0459, R2142, R2144, R2596, R0240, R0460

### [medium] over-absorbed

R2415 ({Santaleous}.1) — 'Can use his ability to cancel a master card multiple times each turn' — teaches nothing about playing or canceling. It is a periodicity reading of one vampire's own card text; the fact that the ability happens to cancel masters is incidental. It fails the transfer test: no other card is ruled differently because of it.

**Recommendation:** Reclassify C with a note, or at most 1.5/1.2 as a near-miss code. Note that R2416 ({Santaleous}.2) is a legitimate 1.8 P and should stay — only .1 is the over-absorption.

*Rulings (1):* R2415

### [medium] other

R2369 ({Nergal}.4: 'If a card he plays is cancelled as it played and no cost is paid, his ability is not considered used for the turn') and R2478 ({Vidal Jarbeaux}.3: 'If a card he plays is canceled as it is played, he is still considered having used the requirement, if any') answer the same question — does a canceled play consume the enabling resource? — with opposite-looking answers. Neither carries a !TENSION tag, because neither classifier could see the other. A drafter working from this extract will write one sentence and be contradicted by the other ruling.

**Recommendation:** Co-locate these two for adjudication before drafting. The reconciling rule is probably 'a requirement is spent on announcement, a per-turn ability is spent on payment', but that distinction is not stated anywhere in the membership and must be confirmed rather than inferred.

*Rulings (2):* R2369, R2478

### [low] misfiled

Three secondary rows whose principle is owned elsewhere and which add nothing to 1.8. R1052 ({Lost in Translation}) is about the ordering of effect windows within an action resolution ('before any modifier or reaction played "as the action/bleed would be successful"'), which is 2.3/3.4, not the as-played window. R2114 ({Anarch Convert}) is about entering a contest and self-contest — 1.13. R2504 ({Watenda}.1, 'takes into account any cost modification that applies for the opposing minion') is a cost-arithmetic rule — 1.7; only its sibling R2505 ('pays any pool cost in blood') has a cancellation angle.

**Recommendation:** Drop all three from 1.8's extract. Each is presumably correctly PRIMARY elsewhere, so nothing is lost. Conservative note: R2504 is the weakest of the three claims to removal, since it sits beside a genuine 1.8 ruling on the same card.

*Rulings (3):* R1052, R2114, R2504

### [low] missing-topic

The section is thin on cancellation priority: what happens when more than one player wants to cancel, or when a cancel card is itself canceled. The only evidence is a single two-member template (R1960/R2121, 'the effect needs to be applied before anyone has an opportunity to play another cancellation effect') plus R2593's 'the cancelation must be played immediately'. There is no ruling at all on canceling a cancel card, and none on the seating/impulse order for competing cancels.

**Recommendation:** Flag to the drafter that this sub-topic rests on one wording and cannot be stated broadly. Either mark it ⚠ REVIEW or state it narrowly as a property of the two named abilities rather than as a general priority rule.

*Rulings (3):* R1960, R2121, R2593

### [low] other

A drafting trap rather than a classification defect. R0338 ({Charming Lobby}) says a political action played from hand via that card 'cannot be canceled as it is played', while R0572 ({Echo of Harmonies}) says the retained political action 'can be canceled as it is played'. R0337 supplies the reconciling mechanism — under Charming Lobby the card is considered played only at successful resolution, so no as-played window ever opens — but the three sit far apart in the extract and the connection is easy to miss.

**Recommendation:** Keep all three; they are correctly filed. Note in the extract that R0337 is the explanation for R0338, so the drafter states the timing rule ('when the card counts as played determines whether an as-played window exists') rather than two card-specific exceptions.

*Rulings (3):* R0337, R0338, R0572

## 1.9

### [high] misfiled

Homonym seam: three rulings use "replacement effect" in the *minion-burn* sense (an effect that replaces a vampire's burning), not the *card-replacement* sense 1.9 owns. R0331 {Charigger, The Axe} "His replacement effect triggers before effects depending on the minion burning (eg. {Soul Gem of Etrius})"; R2167 {Byzar} "His ability is a replacement effect. It prevents any effect triggering after the vampire burns... but still allows burn conditions to be met"; R0835 {Heaven's Gate} "Can be played before another replacement effect triggers (eg. {Charigger, The Axe})". None concerns drawing a card to replace one played. This is the {Elder Library} failure mode the taxonomy records as its control case (shared vocabulary is not shared scope), and R0331 and R2167 are PRIMARY here, so 1.9's extract is currently the only place a drafter meets them.

**Recommendation:** Re-home all three: PRIMARY 5.4 (burning minions - what a burn-replacement does to burn-triggered effects vs. burn conditions), secondary 2.4 (ordering of competing replacement triggers, which is what R0331/R0835 turn on). Drop the 1.9 code entirely; there is no card-replacement content to cross-reference.

*Rulings (3):* R0331, R2167, R0835

### [high] duplicate-template

One ruling ([ANK 20181208], verbatim "Replace the action card (if any) before playing it") accounts for 12 of the 60 rows - 20% of the section - across 12 cards and many chunks. The general entry R2588 (G00052|Modifier as announced) states it; the other eleven are identical card copies adding nothing. Cross-chunk drift shows in the roles: the general entry is filed secondary while ten card copies are PRIMARY, and the copies split P/E arbitrarily (R0069/R0137/R1353/R1633/R1650/R1722 as P, R0703/R1461/R1981/R2022/R2032 as E) for identical text, against golden rule 5.

**Recommendation:** Keep R2588 (general entry) as the P stating the rule, plus at most two e.g. cards - suggest R0069 {Approximation of Loyalty} and R1353 {Predator's Transformation} for the [ACTION MODIFIER] instance. Mark the remaining nine C so the drafter is not handed eleven copies of one sentence, and give R2588 primary standing in 1.9 so the general entry anchors the prose.

*Rulings (12):* R2588, R0069, R0137, R0703, R1353, R1461, R1633, R1650, R1722, R1981, R2022, R2032

### [medium] duplicate-template

Five rulings teach one principle - cards an effect requires you to supply must already be in hand before the replacement draw for the card that demanded them. R0171 {Blessing of the Beast} and R0769 {Gift of Proteus} are the same [PIB 20150428] wording on two cards; R0332 {Charming Lobby} and R0949 {Jack of Both Sides} are the same [RTR 19991001]/[LSJ 20101210] wording ("must be in hand before replacing the X"); R0271 {Call the Wild Hunt} is the same rule stated negatively ("cannot use any animals drawn to replace the ones you are discarding as further discards").

**Recommendation:** State once as a principle ("a card that must be supplied from hand is supplied before its demander is replaced; you cannot feed an effect with its own replacement draw") with two e.g. cards - R0332 {Charming Lobby} for the announced-target template and R0271 {Call the Wild Hunt} for the discard-count template. Leave R0171, R0769, R0949 in the database.

*Rulings (5):* R0171, R0769, R0332, R0949, R0271

### [medium] duplicate-template

Four copies of [LSJ 20011023]/[LSJ 20080630]: canceling a card also cancels its "do not replace until" clause (or alternate-replacement clause) and the card is replaced normally. R2594 is the general entry (G00058|Cancel.2); R0502 {The Diamond Thunderbolt}, R1423 {React with Conviction} and R2143 {Asguresh} are card copies. R1423 is PRIMARY while the general entry and the other two copies are secondary - the same primary/secondary inconsistency as the ANK 20181208 cluster.

**Recommendation:** Keep R2594 (general entry) as the P and R2143 {Asguresh} as the single e.g. - it is the fullest wording, covering the alternate-replacement case and not just do-not-replace-until. Drop R0502 and R1423; both are covered verbatim and 1.8 already owns the cancellation side.

*Rulings (4):* R2594, R0502, R1423, R2143

### [medium] scope-drift

Three copies of [PIB 20121031] "you do not get to see the card drawn as replacement" ({Revelations}, {Vaticination}, {Sergei Voshkov}). Beyond the duplication, the taxonomy's 2026-07-20 scope-line widening explicitly gave default VISIBILITY of replacement draws to 6.9, not 1.9 - yet R1479 sits here as PRIMARY.

**Recommendation:** Move the principle to 6.9 as PRIMARY, keeping one 1.9 cross-reference row (R1479 {Revelations}) so 1.9 cross-refs rather than restates. Drop R1957 and R2426 as redundant copies.

*Rulings (3):* R1479, R1957, R2426

### [medium] duplicate-template

Three copies of [ANK 20180318] on non-replaced cards counting against hand size: R0544 {Dreams of the Sphinx} (one of 6.9's two founding cases per the taxonomy), R1137 {The Meddling of Semsith}, R2227 {Hagar Stone} (phrased as "effectively reduces the hand size"). All three are correctly secondary here, so this is a size problem rather than a misfile.

**Recommendation:** Keep exactly one as 1.9's pointer into 6.9 - R0544, since 6.9 is already anchored on it - and drop R1137 and R2227 from 1.9's extract. 1.9 should cross-reference 6.9 for hand-size consequences, not carry three instances of it.

*Rulings (3):* R0544, R1137, R2227

### [low] duplicate-template

R1136 {The Meddling of Semsith} and R2226 {Hagar Stone} are byte-identical [LSJ 20070320-1] text ("The 'do not replace' effect stacks with whatever 'do not replace' clause the card itself has, so that the longest one wins out"), both P PRIMARY. Consistently labelled, but two rows for one sentence.

**Recommendation:** Keep R1136 as the P and drop R2226. Add 1.15 as a secondary code - this is a stacking-with-a-cap rule of exactly the shape 1.15 was created for, so the stacking section should see it.

*Rulings (2):* R1136, R2226

### [low] other

Unflagged tension on batch vs. sequential replacement that the drafter will hit head-on. R2124 {Angelica} ("The cards must all be burned at once. No further burning can be done once they're replaced"), R2413 {Ruxandra} ("must all be discarded at once, then replaced") and R0400 {Constant Revolution} ("all discarded at once (no replace)") say the whole set is committed before any replacement; R0926 {Infernal Pursuit.4} says the opposite for its case ("If multiple cards are replaced, replace and discard one by one"). None carries a !TENSION tag.

**Recommendation:** Group these four for adjudication before drafting (slug e.g. batch-vs-sequential-replacement). The likely resolution is that commit-then-replace governs effects that consume cards while one-by-one governs draw-then-discard effects - but that has to be settled, not guessed by the drafter.

*Rulings (4):* R0926, R2124, R2413, R0400

### [low] over-absorbed

Two rows are E but read as pure single-card interpretation. R2010 {Waste Management Operation} "If the library is empty and the hand not full, you draw immediately after using it" - the conditional is a property of this one card's refill effect and changes no other card's ruling. R1018 {Learjet} "The additional replacement is optionnal, you get to see the normal replacement before you decide to draw the additional card" - the choice sequence is Learjet's own wording, not a template. (R1017, the other Learjet row, does transfer - it states when a delayed replacement pulls its rider along - so keep that one.)

**Recommendation:** Reclassify R2010 and R1018 as C with 1.9 as the near-miss code; neither survives the transfer test. Note this empties the empty-library sub-topic - see the missing-topic finding.

*Rulings (2):* R2010, R1018

### [low] missing-topic

1.9's scope line claims "empty library" as a sub-topic, but the only membership row touching it is R2010 {Waste Management Operation}, itself a C candidate above. No ruling here states what happens when a replacement draw cannot be made because the library is empty. The empty-crypt half of the same scope-line widening, by contrast, has two clean rulings (R0131 {Bear-Baiting}, R0887 {Illusions of the Kindred}).

**Recommendation:** Flag to the drafter that the empty-library paragraph must be written from the rulebook with no ruling support, or dropped in favour of a cross-reference. Worth a targeted grep of the C pile for empty-library rulings absorbed elsewhere before concluding it is a genuine corpus gap.

*Rulings (1):* R2010

## 2.1

### [high] duplicate-template

Five PRIMARY rows are verbatim copies of one ruling — "Can only be played by the controller of the acting minion. [LSJ 19990425]" — on {Blanket of Night}, {Empowering the Puppet King}, {Inspire Greatness}, {Siren's Lure} and {Veil the Legions}. Same text, same single reference, five chunks, five separate absorptions. Under the no-exhaustive-card-lists rule this is one principle with e.g., not five examples. Compounding it, all five are role E: nobody states the principle, so the drafter is asked to induce prose from five identical illustrations.

**Recommendation:** Collapse to one principle sentence ("action modifiers may only be played by the controller of the acting minion") with two e.g. cards — keep R0164 {Blanket of Night} and R1641 {Siren's Lure} (the disciplined/[MEL] variant, which shows the rule is not limited to plain action modifiers). Re-role the kept anchor P. Reclassify R0587, R0932, R1961 to C with note "duplicate of [LSJ 19990425] acting-minion-controller template".

*Rulings (5):* R0164, R0587, R0932, R1641, R1961

### [high] duplicate-template

Four rows are verbatim copies of the {Spying Mission} template — "Must be played before action resolution, ie. before any modifier or reaction played 'as the action/bleed would be successful' are played. It cannot be played after a {Spying Mission} on the vampire triggers. [LSJ 19980105]" — on {Deflection}, {Lost in Translation}, {My Enemy's Enemy} and {Redirection}. All four are bleed-redirection cards teaching the same window boundary from one ruling.

**Recommendation:** Keep R0472 {Deflection} as the named example — it is the archetype of the wording template and is already PRIMARY-filed elsewhere, so it survives as a cross-reference either way. State the boundary once in 2.1 prose (redirection closes before the "would be successful" window opens) and cross-reference 3.7.1. Reclassify R1052, R1210, R1440 to C as template duplicates.

*Rulings (4):* R0472, R1052, R1210, R1440

### [medium] duplicate-template

Three secondary rows carry the same [LSJ 20070403]/[LSJ 20070413] Imbued-power ruling: "[REACTION] Can be used only when reactions can be used ... It does not count as playing a reaction card." on {Hide}, {Surge} and {Vigilance}. The principle (a reaction-timed ability is not a reaction card play) belongs primarily to 1.5 abilities-vs-cards; 2.1 needs at most one copy as the timing-side cross-reference. Note R1975 {Vigilance} states the window as "(during an action)" where the other two say "(unlocked or with a wake effect)" — a real wording divergence in otherwise identical text.

**Recommendation:** Keep one (R0858 {Hide}) as the 2.1 cross-reference; drop R1776 and R1975 from this section's extract. Flag the R1975 parenthetical divergence for the 1.5 drafter — the two phrasings are not equivalent and one of them is probably the paraphrase.

*Rulings (3):* R0858, R1776, R1975

### [medium] duplicate-template

Three further template pairs, each pair being one ruling printed on two cards: R2396/R2427 {Porphyrion}/{Seterpenre} — "His 'as he enters play' ability can be used before he enters contest" [LSJ 20080526]; R2064/R2134 {Haqim's Law: Retribution}/{Anu Diptinatpa} — "Cannot be used during combat" [ANK 20231124]; R0841/R1054 {Heidelberg Castle, Germany}/{Louvre, Paris} — usable between two actions during another Methuselah's turn [ANK 20210608]. Each pair shares one reference date, confirming a single ruling duplicated onto linked cards.

**Recommendation:** Keep one card per pair: R2396 {Porphyrion} (and it is 1.13 material primarily — retain here only as cross-reference), R0841 {Heidelberg Castle, Germany} (already the anchor for the between-actions window and reused by R1645). Reclassify R2427, R1054 as duplicates. See the separate finding on R2064/R2134.

*Rulings (6):* R2396, R2427, R2064, R2134, R0841, R1054

### [medium] over-absorbed

R2064 {Haqim's Law: Retribution}.3 and R2134 {Anu Diptinatpa}.1 are both PRIMARY E on the bare text "Cannot be used during combat" / "Her ability cannot be used during combat". As written these state only that one specific ability's window excludes combat. They fail the transfer test — knowing this changes no ruling on any other card, because the exclusion is a fact about those abilities, not about combat as a window. There is no stated reason to generalize from.

**Recommendation:** Reclassify both to C with note "bare card-specific ability window; fails transfer — 2.1 nearest". If the drafter wants the general point (abilities without a combat-usable window cannot be used during combat), R1121 {Mask of a Thousand Faces}.8 already states it in transferable form and is a better anchor.

*Rulings (2):* R2064, R2134

### [low] role-error

Identical ruling text received different roles across chunks: R1440 {Redirection} is P while R1052 {Lost in Translation} and R1210 {My Enemy's Enemy} are E, and R0472 {Deflection} is P-secondary. This is golden rule 5 (identical rulings, identical labels) failing across chunk boundaries. P/E is low-stakes individually, but the inconsistency is the visible signature of the duplication in the finding above.

**Recommendation:** Resolve as part of the {Spying Mission} template dedupe: one surviving row, role P. No separate action needed if that dedupe is applied.

*Rulings (4):* R1440, R1052, R1210, R0472

### [low] misfiled

R2235 {Hermana Hambrienta Mayor}.1 and R2237 {Hermana Hambrienta Menor}.1 are the same ruling on two printings of one character: excess blood drains off before the enters-play ability forces a burn. The content is influence/capacity mechanics with an ordering wrinkle, not an effect-window question; 2.1's extract gains nothing it can write prose from. Both are secondary rows, so the primary filing may well be correct.

**Recommendation:** Drop from 2.1's extract. The ordering point, if kept at all, belongs to 2.4 (simultaneous effects, controller ordering) or 5.1 (capacity); dedupe to one card either way.

*Rulings (2):* R2235, R2237

### [low] missing-topic

For a section titled "effect windows overview: impulse, who may act when", nothing in the membership addresses the impulse order itself — who gets the opportunity first when several non-acting Methuselahs want to respond, or how a window closes once all pass. R2376 {Owain Evans} is the closest (mandatory effects discharge before the impulse passes) and it approaches the question only obliquely. The drafter will have to carry the core impulse mechanic entirely from the rulebook with no ruling support, which will make the section's opening thin relative to its four well-supplied sub-topics.

**Recommendation:** Expect to write the impulse-order paragraph from [RBK] alone and cite it as such. Worth a targeted grep of the C pile and of 2.4/2.3 for any impulse-order ruling that was routed elsewhere before accepting the gap as real.

*Rulings (3):* R2376, R2558, R2602

### [low] other

Structural note rather than a defect: the strongest and most quotable material in 2.1 is a single coherent sub-topic — atomicity, i.e. that a resolving effect offers no window inside itself. R0836 {Heidelberg Castle, Germany}.1 states the underlying rule outright ("all effects are instantaneous except for actions and certain combat effects") and R0110, R1121, R1645, R1837, R1945 are its illustrations across five different resolution contexts (torpor assignment, referendum/combat, queued combat, control change, damage step). This is a seam, but it is a subsection seam, not a section split — 2.1's charter covers it.

**Recommendation:** Draft 2.1 with an explicit atomicity subsection anchored on R0836, citing two of the five illustrations (R1837 {Temptation} for control change and R1945 {Vagabond Mystic} for the damage step give the widest spread). Do not split to a new code.

*Rulings (6):* R0836, R0110, R1121, R1645, R1837, R1945

## 2.2

### [high] duplicate-template

13 of the 30 rows are a single verbatim ANK 20190425 sentence — "Cards and effects that are played 'as the action is announced' must be played before playing 'regular' action modifier or reaction cards" — stamped onto 12 different cards plus its general entry. All 13 are PRIMARY and 11 are P, so the extract hands the drafter the same sentence twelve times over as if it were twelve principles. This is exactly the cross-chunk drift the review exists to catch: no single classifier could see the other copies.

**Recommendation:** Keep R2587 (G00052|Modifier as announced.1) as the P source — it is the general entry and it is the only copy that names the contrast card ({Conditioning}), which is what makes it prose-ready. Keep at most 2-3 card copies as the "e.g." spread across discipline families, e.g. R0702 {Force of Personality} [PRE], R1632 {Shroud Mastery} [NEC], R0861 {Hide} [1 CONVICTION] (the Imbued copy shows the rule is not discipline-bound). Demote the remaining 9 to C/database. Secondarily, the surviving card copies should be E, not P — a card copy of a general entry illustrates the principle, it does not state it (contract, "General rule entries").

*Rulings (13):* R2587, R0068, R0136, R0702, R0861, R1352, R1460, R1632, R1649, R1721, R1980, R2020, R2031

### [high] duplicate-template

A second verbatim template, ANK 20181208 "Replace the action card (if any) before playing it", appears 9 times (8 cards + general entry). It also shows PRIMARY/secondary drift on identical text: R2032 and R2588 are PRIMARY in 2.2 while the seven other identical copies are secondary — golden rule 5 (identical rulings, identical labels) broken across chunks. It further mixes P and E arbitrarily on the same sentence (R0069 P vs R0703 E).

**Recommendation:** Keep R2588 (general entry) as the single P statement and one card copy as the "e.g."; drop the other 7 to C/database. Also reconcile the primary code: this sentence is a replacement-timing rule (1.9) observed inside the as-announced window, so pick one owner for all copies — 1.9 PRIMARY with 2.2 secondary, or the reverse — rather than leaving the same sentence split both ways.

*Rulings (9):* R2588, R0069, R0137, R0703, R1461, R1633, R1650, R1722, R2032

### [medium] misfiled

Both state the same template about the OPPOSITE end of the action timeline: "Must be played before action resolution, ie. before any modifier or reaction played 'as the action/bleed would be successful'... cannot be played after a {Spying Mission} on the vampire triggers." Nothing here concerns the "as the action is announced" window that defines 2.2; it is a deadline keyed to the pre-resolution window. R1823 {Telepathic Misdirection} is PRIMARY here, which is a genuine misfile; R0076 {Archon Investigation} is secondary and is the more forgivable cross-reference.

**Recommendation:** Move to 2.1 (generic sequencing / who may act when) or 3.4 (resolution), with 2.2 kept only as a secondary cross-reference contrasting the two windows. They are also the same template as each other: keep one, most likely R1823 since it spells the rule out more fully.

*Rulings (2):* R1823, R0076

### [medium] misfiled

{Andrew Stuart}.1 — "His ability needs to be applied before anyone has an opportunity to play another cancellation effect (eg. {Direct Intervention})" — is filed E PRIMARY in 2.2 but says nothing about action announcement. Its principle is that an automatic cancellation applies before an optional cancellation gets a window, which is cancellation ordering.

**Recommendation:** Reassign PRIMARY to 1.8 (playing & canceling a card), which owns what cancellation reaches and when. Drop 2.2 entirely, or keep it only as secondary.

*Rulings (1):* R2121

### [medium] recoverable-C

{Car Bomb}.1 — "Is to be used when the action is announced." — is E PRIMARY but is a bare statement of which window one specific card occupies. It fails transfer: it changes how you rule on {Car Bomb} and no other card, and it does not even assert the ordering rule 2.2 is about. As an "e.g." it illustrates nothing the ANK 20190425 copies do not illustrate better.

**Recommendation:** Reclassify C, nearest code 2.2. If the drafter wants a non-modifier example of the window, R2052 {Yoruba Shrine} (acting player gets the as-announced window first) carries an actual principle and should be preferred.

*Rulings (1):* R0282

### [low] misfiled

{Concoction of Vitality}.1 — "Can be used after declaring an action using a discipline (eg. {Govern the Unaligned})" — is E PRIMARY in 2.2, but the point is that the discipline requirement is checked at announcement so the boost may follow, not that as-announced effects precede regular modifiers. It reads as a requirement-timing ruling that happens to mention announcement.

**Recommendation:** Move PRIMARY to 1.6 (requirements to play vs. to keep) or 2.1; retain 2.2 as secondary at most.

*Rulings (1):* R0388

### [low] thin-section

Once the two boilerplate blocks are deduplicated, 2.2 rests on roughly four distinct rulings. Two sub-topics a judge would expect are essentially unevidenced: ordering AMONG several as-announced effects held by different players (only R2052 {Yoruba Shrine}, and only for the acting player's priority), and whether/when the announcement window closes — i.e. whether an as-announced effect can still be played once a regular modifier has been played. R2093 {Unleashing the Bestial Soul} (opponent may wake as the card is played, before its effects apply) is a reasonable secondary but is about the as-played window generally, not action announcement.

**Recommendation:** Flag to the drafter that 2.2 will be short and should lean on cross-references (1.8 for the as-played window, 2.1 for the wider sequencing, 2.4 for simultaneous-effect ordering) rather than being padded with further copies of the two templates. If the window-closing question matters, it is a candidate ⚠ REVIEW point rather than something the corpus answers.

*Rulings (2):* R2052, R2093

## 2.3

### [high] duplicate-template

Eleven rulings carry byte-identical boilerplate — "Modifiers and reactions that can be used at the end/after an action can still be used afterwards" with the same reference triple [LSJ 20041022] [RTR 20180719] [ANK 20221205] — spread across at least eight chunks. Three trivial surface variants exist: bare (R0314 Champion, R0634 Faerie Wards, R0672 Final Loosening, R0859 Hide, R1395 Purification), "If the action fails," prefix (R0283 Car Bomb, R0495 Detect Authority, R0862 Hide the Heart, R1096 Malkavian Derangement, R1539 Scobax), and "after combat" (R0595 Ensconced). All three state one principle: the post-resolution window survives the action ending, whether by failure or by combat. Under the no-exhaustive-card-lists rule this is one sentence of prose, not eleven entries.

**Recommendation:** Keep three: R0314 (bare form), R0283 (failed-action form), R0595 (after-combat form). Demote the other eight to C — they add no distinct fact and the reference set is identical. Note that the same template is also split P/E arbitrarily across the eleven (R0283/R0862/R1096 are E, the rest P), confirming these were labelled blind of each other.

*Rulings (11):* R0283, R0314, R0495, R0595, R0634, R0672, R0859, R0862, R1096, R1395, R1539

### [high] duplicate-template

Three further ANK-sourced boilerplates recur with no per-card content. (a) "Cards and effects that can be played 'after resolution' (and only them) can be played after it" — R0281 Capitalist, R0295 Cavalier, R1306 Perfectionist, R1551 Scrying of Secrets, R1903 Truth of a Thousand Lies, R1976 Vigilance, all [ANK 20190113]/[ANK 20190425]. (b) "The acting player decides the order of (and can play other) 'after resolving the action' effects" — R0447 The Damned, R0574 Ecstasy, R1888 Travelers Obey the Tenets, R2430 Shemti, all [ANK 20180206], four verbatim copies. (c) "Can be played after action resolution to use a reaction card (eg. {Fast Reaction} after combat)" — R0628 Eyes of Argus, R0710 Forced Awakening, R1262 On the Qui Vive, R1994 Wake with Evening's Freshness, all [LSJ 20091123]; these are four wake cards saying the identical thing about the wake template.

**Recommendation:** (a) keep R0281 and R0295 — they differ usefully in what the intervening effect is (gain blood vs unlock) — and drop the other four to C. (b) keep exactly one, R0447; the other three are the same sentence with a different card name. (c) keep R1994 (Wake with Evening's Freshness is the canonical wake card) and drop the other three; this is a wake-template fact, so the surviving entry should be cross-referenced from the wake/reaction section rather than restated.

*Rulings (14):* R0281, R0295, R1306, R1551, R1903, R1976, R0447, R0574, R1888, R2430, R0628, R0710, R1262, R1994

### [medium] other

Two variants of the same opening sentence give opposite ordering rules, and a drafter reading this extract would write a contradiction. Variant B (R2541 the G00006 general entry "Modifier after resolution", plus R0527 Domain of Evernight, R0656 Fata Amria, R0713 Forced March) says "Is played after resolution, but still during the action. Action modifiers and effects that can be played 'after resolution' can be played BEFORE OR AFTER it" [LSJ 19981028] [ANK 20190425]. Variant B' (R0701 Follow the Blood, R1184 Momentary Delay) says the same first sentence then "can be played BEFORE IT, BUT NOT AFTER" [LSJ 19981028] [LSJ 20100206-2]. Same primary reference, opposite conclusion. No classifier could see this from inside a chunk; neither variant carries a !TENSION tag.

**Recommendation:** Treat as an adjudication item before drafting, not a classification fix. Keep R2541 (the general entry, authoritative P) plus one card example, and keep R0701 or R1184 as the exception case, but the drafter must be told explicitly whether B' is a genuine card-class exception (both are modifiers that end the action's modifier window) or a stale wording. Drop the redundant members of B: R0527, R0656, R0713 are three verbatim copies of the general entry.

*Rulings (6):* R2541, R0527, R0656, R0713, R0701, R1184

### [medium] duplicate-template

Four smaller template clusters. (a) "Is played after all combats are handled" — R2542 (G00007 general entry), R0734 Freak Drive, R0292 Cats' Guidance, with R0087 Art of Memory restating it in different words. (b) "Is used after combat effectively ends and can be order[ed] against other cards and effects played after combat" [ANK 20230314] — R1191 Monster, R1375 Provision of the Silsila, R1601 Shadow Boxing, three verbatim copies that cite each other as the example. (c) "The gain blood effect is applied after combat ends, no combat card can be played afterwards. The acting player chooses the order of after-combat effects" — R0744 Games of Instinct and R1536 Save Face, identical sentence, different reference. (d) The action-ends-immediately negative case — R0322 Change of Target, R0351 Claiming the Body, R0994 Kiss of Ra, all secondary here and all the same sentence.

**Recommendation:** (a) keep R2542 as the P and R0734 as the e.g.; C the rest. (b) keep one, R1375, and let the prose name the other two as the ordering partners rather than as separate entries. (c) keep R0744. (d) keep one (R0322) as the boundary cross-reference to 3.5, which owns the fail/end templates as PRIMARY; the other two add nothing.

*Rulings (12):* R0292, R0734, R2542, R0087, R1191, R1375, R1601, R0744, R1536, R0322, R0351, R0994

### [medium] over-absorbed

Four Spying Mission rulings are filed here, all secondary, and all are about the window BEFORE resolution closing, not the post-resolution window 2.3 owns. R1719: "Is played when a bleed would be successful, before resolution." R1713: "played if you know the bleed is successful, after you would normally play reactions and action modifiers." R1717 and R1718 are pure two-card interactions keyed to that timing — "{Archon Investigation} cannot be played after a Spying Mission is burned for +2 bleed" and "{Mask of a Thousand Faces} cannot be played after playing a superior Spying Mission" — which is exactly the pure card-pair interpretation the style rules leave in the database. Carrying four rulings off one card into a section it is only adjacent to is the single largest single-card presence in 2.3.

**Recommendation:** Keep R1719 only, as the boundary marker naming where 2.3's window opens; its natural PRIMARY is 2.1/3.4. Drop R1713 to C (it restates R1719 with vaguer wording), and R1717/R1718 to C — R1718 additionally belongs to 3.10 if it is kept anywhere, since the operative fact is about {Mask of a Thousand Faces} substituting the actor.

*Rulings (4):* R1713, R1717, R1718, R1719

### [low] misfiled

R1764 {Summon Soul}.1 — "Is removed from play as part of the resolution, it cannot be retrieved by {Shroudsight}" — is about what removal-as-part-of-resolution does to retrieval, not about what may be played after resolution or how post-resolution effects order. It touches 2.3 only through the word "resolution". It is also a two-card interaction (Summon Soul / Shroudsight) with no transfer.

**Recommendation:** Remove from 2.3. Nearest owner is 1.11 (ash heap retrieval, played vs put there) or 1.10; if it survives there at all it is arguably C on the transfer test.

*Rulings (1):* R1764

### [low] duplicate-template

Three rulings make the same point about the blood hunt referendum being part of the resolution and therefore inside the pre-"after resolution" window: R0007 {Abactor} ("cards played 'after a successful action' or 'after resolution' must be played after the referendum; {Heidelberg Castle, Germany} cannot be used before"), R0839 {Heidelberg Castle, Germany}.4 (the same fact from the other card's side), R1498 {Ritual of the Bitter Rose} ("can be played after a diablerie, before the blood hunt"). R0007 and R0839 are a reciprocal pair describing one interaction.

**Recommendation:** Keep R0007 as the statement and R1498 as the contrasting e.g. (a card that DOES fit in the diablerie-to-blood-hunt gap); drop R0839 as the mirror of R0007. All three should remain PRIMARY-owned by 3.7.8; 2.3 carries them as the worked case of "resolution is not over until the embedded referendum resolves".

*Rulings (3):* R0007, R0839, R1498

## 2.4

### [high] duplicate-template

Eight rulings are one end-of-round / "when the combat would end" ordering template; seven of them carry the identical reference triple [LSJ 20021113] [ANK 20191219] [ANK 20180910-1] and say verbatim "Can be played before or after effects that are played at the end of the round or 'when the combat would end' (eg. {Telepathic Tracking}). Can be played before or after {Psyche!}" (R0510 Disarm, R1393 Pulled Fangs, R1744 Street Cred, R1817 Taste of Vitae, R1455 Relentless Reaper, R1384 Psyche!.6, R1828 Telepathic Tracking.4).

**Recommendation:** Write one principle: cards in the end-of-round / end-of-combat window are mutually orderable by their player, with the {Psyche!} vs {Telepathic Tracking} asymmetry as the one exception. Keep R1826 (Telepathic Tracking.2 — the only ruling that carries real content, the non-commutative case), plus R1384 (Psyche!.6) and one of R0510/R1817 as the "either order" e.g. Drop the remaining five to database-only; they add no distinct fact.

*Rulings (8):* R0510, R1384, R1393, R1455, R1744, R1817, R1826, R1828

### [high] duplicate-template

Six rulings are the "Is played after resolution, but still during the action" template. Four are word-for-word identical with the same references [LSJ 19981028] [ANK 20190425] (R0527 Domain of Evernight, R0656 Fata Amria, R0713 Forced March, R2541 the G00006 general entry); two are the contrasting variant "…can be played before it, but not after" [LSJ 20100206-2] (R0701 Follow the Blood, R1184 Momentary Delay).

**Recommendation:** Keep R2541 (the G00006 general entry — prime prose material per the contract) plus exactly one of R0701/R1184 to carry the asymmetric variant. Drop the three card copies of the identical wording. Note also that this template's principle is window membership ("after resolution" effects), which 2.3 owns; 2.4 should cross-reference 2.3 rather than restate it.

*Rulings (6):* R0527, R0656, R0713, R2541, R0701, R1184

### [medium] duplicate-template

Four byte-identical rulings, same single reference [ANK 20180206]: "The acting player decides the order of (and can play other) 'after resolving the action' effects." (R0447 The Damned, R0574 Ecstasy, R1888 Travelers Obey the Tenets, R2430 Shemti).

**Recommendation:** This is the clearest statement of 2.4's own principle in the whole membership, so keep it as P prose — but sourced once. Keep R0447 and cite the other three cards only if an "e.g." is wanted at all; the style rule caps at three and here zero cards are needed, since the sentence names no card.

*Rulings (4):* R0447, R0574, R1888, R2430

### [medium] scope-drift

About sixteen rows (mostly `secondary`) are not about who orders simultaneous effects but about WHICH WINDOW a card belongs to — the "after resolution" window (2.3) and the end-of-combat / after-combat window (4.9). Their 2.4 content reduces to the single clause "and either order is allowed". Read end to end the section has a visible seam: 2.4-proper material (controller chooses order, unlock-phase ordering, cost-and-benefit simultaneity, simultaneous triggers) on one side, window-membership rulings on the other.

**Recommendation:** Keep them in the extract (they are legitimate secondary cross-references), but the drafter should state ordering-within-a-window once as a general rule and cross-reference 2.3 and 4.9 for what the windows are, rather than writing a paragraph per window. Flagging so the drafter does not mistake the volume for a sub-topic.

*Rulings (16):* R0527, R0656, R0701, R0713, R1184, R2541, R0510, R1384, R1393, R1455, R1744, R1817, R1191, R1601, R0744, R1536

### [medium] misfiled

R0865 (Hide the Heart.4) is P/PRIMARY here but teaches nothing about simultaneous effects: "Sequencing applies. For example, if another Methuselah is targeted by the action, they must declare if they attempt or decline to block before you can play Hide the Heart." That is the general impulse/sequencing rule plus the block-declaration point.

**Recommendation:** Reassign primary to 2.1 (effect windows, who may act when), with 3.3 (block declaration sequence) as secondary. Keep 2.4 only as a third code if at all.

*Rulings (1):* R0865

### [medium] duplicate-template

Cost-and-benefit simultaneity: R0617 (Eternals of Sirius), R1158 (Minion Tap) and R1977 (Villein) are the same ruling under reference [LSJ 20020620] — "Pay the cost at the same time you gain pool from it, you do not get ousted in between." R1525 (Sabbat Threat) and R0846 (Herald of Topheth) are adjacent but distinct (choosing to gain before paying; oust resolved before burn-triggered effects).

**Recommendation:** Keep R1158 (Minion Tap — the ruling names the cost sources explicitly, so it is the richest) as the e.g., mention {Villein} in passing at most, drop R0617. Keep R1525 and R0846 separately: they are different facts, not copies.

*Rulings (5):* R0617, R1158, R1977, R1525, R0846

### [medium] duplicate-template

Three rulings share the reference triple [ANK 20210627] [ANK 20211207] [ANK 20220116] and the same two-clause structure — "If the action is blocked, no other effect can be used before resolving the delayed effect. However, effects that trigger at the same moment are still applied and ordered by the acting Methuselah" (R1150 Millicent Smith, R1170 Mirror Walk, R1931 Unleash Hell's Fury). R0121 (Banshee Ironwail.2) is the same ANK 20210627 family from the other side.

**Recommendation:** One principle — a delayed on-block effect resolves before any further effect, but genuinely co-triggering effects are still ordered by the acting Methuselah. Keep R1931 (the most complete: it also states that modifiers may be played after) plus R1150 as the second e.g.; drop R1170. Keep R0121 as the separate reversal note it is.

*Rulings (4):* R1150, R1170, R1931, R0121

### [low] duplicate-template

Eight further pairs of the same template, each pair sharing wording and references: torpor-window priority R0035/R0462 [RTR 20010710]; range-setting priority R1724/R1740 [PIB 20120214]; after-combat blood gain R0744/R1536; "used after combat effectively ends… ordered against other after-combat effects" R1191/R1601 [ANK 20230314]; "a limited bleed modifier can be played before or after" R1337/R1404 [LSJ 20100218] (and R1402 is the same shape for a limited additional strike); the mirrored replacement-effect ordering R0331/R0835 [ANK 20230816]; "replaced before unlocking cards, other unlock effects cannot be ordered before" R1327/R2560 (with R1094 Malkavian Dementia teaching the same not-orderable-at-start-of-unlock principle).

**Recommendation:** Keep one per pair: R0462 (states the window-equivalence explicitly), R1740 or R1724 (one only, and note 4.2 owns range-setting exclusivity — cross-reference rather than restate), R0744, R1191, R1337 (one limited-modifier example covers R1404 and R1402), R0835, and R2560 (the G00025 general entry) with R1094 as the contrasting cannot-be-ordered case.

*Rulings (16):* R0035, R0462, R1724, R1740, R0744, R1536, R1191, R1601, R1337, R1404, R1402, R0331, R0835, R1327, R2560, R1094

### [low] over-absorbed

R0054 (Anathema.4) is E/PRIMARY but is a pure one-card trigger interpretation: "Does not trigger if the vampire is burned by aggravated damage during damage resolution." It states when one specific card's trigger fails to fire; it changes how you rule on no other card and names no orderable pair of effects.

**Recommendation:** Reclassify C with 5.4 or 4.4 as the near-miss code. It fails the transfer test.

*Rulings (1):* R0054

### [low] misfiled

R0056 (Anathema.6) is P/PRIMARY in 2.4 but its principle is non-stacking: "Multiple Anathemas don't multiply the pool gain." Sequential resolution is the mechanism, not the lesson; 1.15 (cumulative & stacking, added on exactly this kind of evidence) owns the lesson.

**Recommendation:** Make 1.15 primary and 2.4 secondary. It is a good worked example of how ordering causes later copies to fizzle, so it should stay visible to this section.

*Rulings (1):* R0056

### [low] missing-topic

The section has no general-rule entry stating its own base rule. The only two G000xx rows present (R2541 G00006, R2560 G00025) are window-membership rulings, not ordering rulings. Ordering ACROSS Methuselahs is also thin: only R0035/R0462 (acting minion first in the going-to-torpor window) and R2358 (Mustafa — first to act has priority, last has final say) touch it, and no ruling states the general turn-order fallback for simultaneous effects controlled by different Methuselahs.

**Recommendation:** The drafter will have to source 2.4's core statement from the rulebook sequencing rules ([RBK sequencing], cited in R0865) rather than from a ruling, and should expect the cross-Methuselah ordering paragraph to rest on R2358 plus R0462 alone. Not a taxonomy gap — a warning that this part of the section will be thin on citations.

*Rulings (3):* R0035, R0462, R2358

## 2.5

### [high] duplicate-template

Four crypt cards carry the same boilerplate verbatim: 'When playing a card requiring <trait>, she is treated as such for all effects of the card, and only them, including duration effects. She is not treated as such for effects the card has from being in play.' R2337 (Mata Hari), R2391 (Philip van Vermeer IV), R2450 (Tatiana Stepanova) are word-for-word identical apart from the trait named; R2386 (Petaniqua) is the same sentence with 'meeting the requirements' substituted for the trait. Three of the four cite the same ruling [ANK 20190228]. This is one principle (a trait granted for playing a card covers that card's duration effects but not its in-play effects), not four examples.

**Recommendation:** Keep R2337 (Mata Hari.2) as the single canonical statement of the principle plus R2338 (Mata Hari.3) as the worked when-played-vs-in-play illustration on contracts. Drop R2391, R2450, R2386 from 2.5's extract; they remain in the database and, if 1.6 wants them, belong there. Per the no-exhaustive-card-lists rule the drafter should write the template once and cite one or two cards.

*Rulings (5):* R2337, R2391, R2450, R2386, R2338

### [high] duplicate-template

Rowan Ring and Wooden Stake carry two identical wording templates, both sourced to the same ruling [LSJ 19980831]: (a) 'If placed on a minion that cannot have equipment, the X is burned. The "does not unlock as normal" effect still applies' (R1517 / R2037) and (b) 'The "does not unlock as normal" effect continues to apply if the X is burned or moved' (R1518 / R2038). Four rows for two principles. Roles are also inconsistent for identical text: R1518 is E while R2038 is P, and R1517 is PRIMARY while its twin R2037 is secondary.

**Recommendation:** Keep the Rowan Ring pair (R1517, R1518) as the 'e.g.' and drop R2037/R2038 from the extract, or vice versa — one card, not two. The drafter should state it once as: an effect the card imposes on entry survives the card's own burn or removal.

*Rulings (5):* R1517, R1518, R2037, R2038, R1512

### [medium] other

Unflagged contradiction on the same wording template. R1518/R2038 state the 'does not unlock as normal' effect continues to apply after the source card is burned or moved. R1512 (Rotschreck.10) states 'The "does not unlock as normal" effect stops if Rotschreck is burned or removed.' Same phrase, opposite persistence outcome, no !TENSION tag on any of the three rows. A drafter working from this extract would write contradictory sentences.

**Recommendation:** Co-locate these three for adjudication before drafting (a !TENSION slug such as does-not-unlock-persistence). The reconciling distinction is likely equipment-imposed-on-entry vs. an ongoing in-play effect, but that distinction is not stated in any of the three rulings and must be settled, not inferred, before it becomes prose.

*Rulings (3):* R1512, R1518, R2038

### [medium] duplicate-template

R0311 (Champion.2) and R0594 (Ensconced.1) are byte-identical apart from the discipline bracket: 'The action still continues until the end of combat. The acting minion stays the same, effects applied during the action still applies during combat.' Both cite [LSJ 20070217]. Roles diverge on identical text — R0311 is E, R0594 is P. Both are secondary in 2.5.

**Recommendation:** Keep one (R0594, since its P role matches the principle statement) and drop the other from 2.5's extract. Note that the sentence's centre of gravity is combat continuation rather than duration; 2.5 needs at most one copy as a cross-reference for 'effects applied during the action still apply during combat'.

*Rulings (2):* R0311, R0594

### [medium] duplicate-template

R0169 (Blessing of Chaos.1) and R2471 (Valerius Maior, Hell's Fool.1) are the same sentence: 'The prohibition to play certain cards applies from the moment [the vampire/he] attempts to block until the end of the action, even if he fails to block.' Both cite [LSJ 20080818]. R2471 is PRIMARY, R0169 secondary.

**Recommendation:** Keep R2471 as the single instance; drop R0169 from 2.5's extract. One principle — a block-triggered prohibition runs from the block attempt to end of action regardless of whether the block succeeds — with one 'e.g.'.

*Rulings (2):* R0169, R2471

### [medium] scope-drift

A cluster filed PRIMARY in 2.5 is really about requirements checked at play and not maintained thereafter, which taxonomy 1.6 explicitly claims ('requirements to play vs. to keep'). R0389 (Concordance: 'continues to apply even if the vampire stops being Infernal'), R0423 (Cry Wolf: 'ability continues to apply fully if he is not a werewolf'), R1144 (Mental Maze: 'can be played if the requirement was met at the time of block'), R1818 (Taste of Vitae: 'can be played if the opponent was burned'). The Mata Hari family (R2337 etc.) is correctly secondary here, showing the classifiers did know 1.6 owns this — the PRIMARY assignments are the inconsistent ones.

**Recommendation:** Do not move them out of 2.5's extract — the persistence half is genuine 2.5 material — but the drafter should state the requirement-snapshot rule once in 1.6 and have 2.5 cross-reference it rather than restate it, per the cross-reference-don't-repeat rule. Flag the PRIMARY/secondary inconsistency so 1.6's extract also receives R0389 and R0423.

*Rulings (5):* R0389, R0423, R1144, R1818, R2337

### [medium] over-absorbed

Both Eternal Mask rows are pure one-card mechanics. R0611: 'You still cannot burn it if the vampire that was brought back was burned and later returned to play' — this is entirely about The Eternal Mask's own self-burn condition and the identity of the specific vampire it named; it changes how you rule on no other card (fails transfer). R0613 ('If The Eternal Mask is burned by something else than its own effect (including when the vampire it is on is burned), the vampire that has been brought back is unaffected') is closer to a general point about effects surviving their source, but that principle is already carried by R2452 (Tegyrius allegiance counters persist when he leaves play) and R1518/R2038.

**Recommendation:** Reclassify R0611 as C with a note ('The Eternal Mask self-burn condition; fails transfer — no other card reads this state; nearest 2.5'). R0613 may stay as an E but should not be the card the drafter builds the source-independence principle on — R2452 is the cleaner statement.

*Rulings (2):* R0611, R0613

### [low] over-absorbed

Two single-line card interpretations sitting as E/PRIMARY. R1818 (Taste of Vitae.4) is the whole ruling: 'Can be played if the opponent was burned.' — it names no template and teaches only that this card's target reference is read at play. R0454 (Darksight.1) 'Goes to the ash heap when played, if it has been removed when the vampire blocks, it has no effect' is a statement about one card's own zone behaviour that a judge fluent in the rulebook would already derive (fails non-obviousness).

**Recommendation:** Candidates for C, or at minimum should not be promoted into prose. If 2.5 wants an example of 'condition read at play, not re-checked', R0482 (Derange.2, 'the clan is set when the card is played') and R1095 (Malkavian Dementia.3, 'no difference if the target changes clan afterwards') are the stronger pair.

*Rulings (2):* R1818, R0454

### [low] thin-section

Two of 2.5's named sub-topics are nearly unevidenced. 'Effects losing track of hidden cards' rests on R0968 (Kaymakli Fragment.2, crypt shuffle-back) with only partial support from R2169 (Capuchin.1, 'all cards and effects lose track of him' after burn). 'For the rest of the game' rests on R1010 (Lay Low.3) alone. Meanwhile the duration-of-an-action and persistence-past-source-leaving-play sub-topics are heavily over-supplied.

**Recommendation:** Tell the drafter these two paragraphs will be one-ruling paragraphs and should be written thin rather than padded, or folded into neighbours (losing-track into 1.9/6.4 vocabulary; 'for the rest of the game' into the leaving-and-re-entering-play discussion alongside R0115/R0116). No taxonomy change — this is a drafting-thinness warning, not a gap.

*Rulings (3):* R0968, R2169, R1010

## 3.1

### [high] duplicate-template

The single ruling [LSJ 20090324] — "an action targeting an equipment/location is directed at the Methuselah controlling it, not the minion it is on" — appears eleven times under 3.1, nine of them near-verbatim card copies of the same sentence (R0070 Arcanum Investigator, R0382 Conceal, R0796 Gremlins, R1051 Loss, R1364 Principia Discordia, R2131 Annazir, R2583 Locquipments.2, plus the location variant R0781 Goblinism / R0827 Haunt). R2571 (G00036|Directed at a card) is the general entry that already states the rule outright, and R0497/R0010 are the consumer side (intercept cards that therefore do not trigger). Nine of these are labelled P, which will hand the drafter nine near-identical prose candidates for one sentence.

**Recommendation:** Keep R2571 as the P statement of the rule. Keep at most two card examples — R0382 {Conceal} (equipment, the canonical case) and R0827 {Haunt} (location, showing the undirected-if-you-control-it corollary). Keep R0497 {Detect Authority} once as the reverse-side illustration (intercept keyed to the minion does not apply). Drop the remaining copies to C, or leave them as codes-only cross-refs; do not carry R0070, R0796, R1051, R1364, R2131, R2583, R0781 into the extract as P.

*Rulings (12):* R2571, R0070, R0382, R0781, R0796, R0827, R1051, R1364, R2131, R2583, R0497, R0010

### [high] duplicate-template

"The card to retrieve must be announced when declaring the action" [LSJ 20010627] recurs ten times with essentially identical wording across ten different cards spread over many chunks (Clio's Kiss, Gear Up, Pandora's Whisper, Sargon Fragment, Scarlet Lore, Whispers from the Dead, Drozodny, Patrizia Giovanni, Pochtli, and R2171 Carlotta Giovanni under an older ref [LSJ 19970922]). No copy adds anything the others do not; they differ only in whether the action comes from a card or a vampire's ability.

**Recommendation:** This is one clause of the announcement principle ("a card retrieved by an action is named at declaration"), not ten examples. Keep R0363 {Clio's Kiss} as the card-provided-action example and R2195 {Drozodny} as the ability-provided-action example — that difference is the only thing the set collectively teaches. Send the other eight to C. Merge the surviving prose with the {Sargon Fragment}/{Charming Lobby} "must be in hand before replacement" strand rather than stating it twice.

*Rulings (10):* R0363, R0754, R1287, R1531, R1537, R2027, R2195, R2382, R2395, R2171

### [medium] duplicate-template

"This is not a directed action, even when targeting another Methuselah's ash heap" [LSJ 20010627] [ANK 20181129] appears five times verbatim, with identical reference pairs, on {Daemonic Possession}, {The Eternal Mask}, {Ghost-Eater}, {Khazar's Diary} and {Pressing Flesh}. Roles drift across the copies (R0756 and R0977 are P, the other three E) purely because different chunks saw different cards.

**Recommendation:** State the principle once — another Methuselah's ash heap is not a card in play, so acting on it does not make the action directed — and cite one example, e.g. {Daemonic Possession} (R0437). Drop R0612, R0756, R0977, R1354 to C. Note the seam with R2571: the general rule is "directed at a card in play = directed at its controller", and the ash-heap set is the negative boundary of that same rule, so it should be one paragraph, not two.

*Rulings (5):* R0437, R0612, R0756, R0977, R1354

### [medium] duplicate-template

The "undirected if you control the target, directed at the target's controller otherwise" template is filed nine times. R1457 {Renewed Vigor} and R2208 {Eurayle Gelasia Mylonas} are word-for-word identical under the same ref [PIB 20121210]; R2109 {Ambrosio Luis Monçada} and R2529 {Evan Klein} are word-for-word identical under the same ref [LSJ 20030214-2] ("Actions from minions of the same controller targeting him are undirected, so they are not affected by his ability"). R1212, R1835, R1068, R0908 and R1258 restate the same rule with different vocabulary.

**Recommendation:** One principle: directedness is determined by whether the target is controlled by another Methuselah, evaluated per action. Keep R1258 {Of Noble Blood} or R1457 {Renewed Vigor} as the plain statement, and keep exactly one of the R2109/R2529 pair as the example of the practical consequence (an ability keyed to directed actions does not fire against your own minions). Drop the remaining seven to C or to codes-only. Do not keep both {Ambrosio} and {Evan Klein} — they are the same ruling.

*Rulings (9):* R1212, R1457, R2208, R1835, R1068, R0908, R1258, R2109, R2529

### [medium] duplicate-template

The "named card must be in hand at announcement, before the announcing card is replaced, and need not be shown (may be set apart face down)" template recurs nine times: {Blessing of the Beast} R0171 and {Gift of Proteus} R0769 (identical), {Charming Lobby} R0332/R0336, {Jack of Both Sides} R0949, {Concealed Weapon} R0383 and {Disguised Weapon} R0514 (identical, same refs [LSJ 19991207] [ANK 20180925-2]), plus R1531 and R1755. Four of these are PRIMARY here even though the load-bearing content splits between 1.9 (replacement ordering) and 6.9 (default non-visibility of a named card).

**Recommendation:** Keep this as ONE paragraph in 3.1 stating the announcement half — cards named as part of announcement must exist in hand at announcement — with a cross-reference to 1.9 for the before-replacement ordering and to 6.9 for the need-not-be-shown half, per the style rule that sections cross-reference rather than repeat. Keep R0336 {Charming Lobby.5} (the fullest statement, including what happens on cancel/fail) and one of R0383/R0514 as the face-down example. Drop the other seven.

*Rulings (9):* R0171, R0769, R0332, R0949, R0336, R0383, R0514, R1531, R1755

### [medium] duplicate-template

The chosen-at-declaration vs chosen-at-resolution axis is the section's most important sub-topic and it is over-populated on both poles. Resolution side: R0973 {Keystone Kine} and R2068 {The Platinum Protocol} are verbatim identical under the same refs [ANK 20240706] [LSJ 20080608], joined by R2084, R1083, R1638. Declaration side: R1390 {Public Trust}, R2083 {Break the Bonds.1}, R0674 {Fire Dance}, R0097 {Ashur Tablets}. Nine rulings for a rule whose only real content is "read the card: some targets are fixed at announcement, some at resolution, and the difference decides what a target-protection or target-change effect can reach".

**Recommendation:** This one deserves prose plus a paired example, which is the strongest teaching device in the section: keep R2083 and R2084 ({Break the Bonds}, same card, one clause fixed at declaration and the other at resolution) as the anchor, and add R0674 {Fire Dance} for the declaration side. Drop R0973/R2068 to one at most, and drop R1083, R1638, R1390, R0097. R0097 {Ashur Tablets} in particular is a three-copies-in-play mechanism specific to that card and is a candidate C rather than an example.

*Rulings (9):* R0973, R2068, R2084, R1083, R1638, R1390, R2083, R0674, R0097

### [medium] duplicate-template

Multi-target directedness is filed seven times. R1625 {Shepherd's Innocence} and R2011 {Wave of Insanity} share the wording "Is directed at all Methuselah controlling [a qualifying card]" and the refs [LSJ 20080809-1] [RTR 20081119]; R0390 {Condemn the Sins of the Father} and R1692 {Sowing Dissension} say the same thing again. R0326 {Chanjelin Ward} and R2446 {Talley} are the same ruling from the blocker's side ("applies if any one target would be enough to enable the effect"), both under [RTR 20081119].

**Recommendation:** One principle with two clauses — an action with several targets is directed at every Methuselah controlling one of them, and a reactive effect keyed to being targeted fires if any single target qualifies. Keep R1692 {Sowing Dissension} for the first clause and one of R0326/R2446 for the second. Keep R2021 {Weigh the Heart.2} only if the drafter wants the corollary about choosing a minion under one of several target Methuselahs; otherwise drop it too. Drop R1625, R2011, R0390 and whichever of the Chanjelin/Talley pair is not kept.

*Rulings (7):* R1625, R2011, R0390, R1692, R0326, R2446, R2021

### [medium] misfiled

The "a steal/transfer effect may name a target holding less than the announced amount; you take what is there" family is here five times, and two of them (R1637 {Siphon.1}, R1979 {Villein.3}) are PRIMARY to 3.1. Taxonomy 1.7 claims this explicitly in its scope line: "effects naming an amount the target may not hold (steal/transfer templates take what is there)". R0522 {Diversion}, R0530 {Donnybrook} and R0537 {Drain Essence} are correctly secondary here and are also a verbatim template triple under one ref [RTR 20010711].

**Recommendation:** Move R1637 and R1979 to 1.7 as PRIMARY, leaving them in 3.1 only as secondary cross-refs. 3.1's legitimate share of this topic is the one-sentence rule that target legality is judged at announcement independently of whether the announced amount is available — cite one card, not five. Keep at most one of R0522/R0530/R0537 as the "e.g.".

*Rulings (5):* R1637, R1979, R0522, R0530, R0537

### [medium] over-absorbed

Three rulings labelled E/P teach nothing transferable. R0145 {Betrayer.5}: "If you have a choice (more than one of your uncontrolled vampires is controlled by the other Methuselah), you still have to choose just one of them to be the Betrayer" — this is the taxonomy's own {Great Symposium} case, generalising only to "the singular in card text means one", which the C-test section names as true, general and useless. R1351 {Predator's Transformation.1}: "Any directed action that ends up burning an ally counts as a directed action burning an ally (eg. {Horseshoes})" is a condition-matching ruling for one card's trigger and fails transfer. R0077 {Archon Investigation.3}: "Targets the bleeding vampire (eg. costs one more against {Secure Haven}, cannot be played on {Mimir})" identifies what one specific card targets rather than teaching how targeting is determined.

**Recommendation:** Reclassify all three as C with the near-miss code 3.1. R0145's companion R0141 {Betrayer.1} ("the affected Methuselah is named when the card is played") already carries the only generalisable content on that card.

*Rulings (3):* R0145, R1351, R0077

### [medium] missing-topic

Two sub-topics that 3.1's scope line implies are essentially unrepresented. (1) What happens when a target chosen at announcement becomes invalid, leaves play, or changes controller before resolution: only R0914 {Incriminating Videotape} touches it, and only for a stolen equipment whose fixed target does not follow the new controller. 3.3 owns "block when target vanished" but nothing owns the announcement side. (2) The rule that an action cannot be announced at all without a legal target: R2569 (G00034, a general entry — "it cannot be played without a valid target") is the only clean statement and it is filed here as secondary, supported only by R2083 {Break the Bonds.1} ("There must be an uncontrolled vampire").

**Recommendation:** Flag both to the drafter as thin. Promote R2569 to a PRIMARY-weight row for 3.1 — as a general entry it is prime prose material and it is currently the section's sole authority for a rule the section must state. For sub-topic (1), the drafter should expect to write from R0914 alone plus a cross-reference to 3.3 and 3.5, and mark any broader claim ⚠ REVIEW rather than generalise from one card.

*Rulings (3):* R0914, R2569, R2083

### [low] duplicate-template

Three further small verbatim clusters. (a) "Does not ignore the normal prey, predator or target restrictions" [ANK 20180623] on R0157 {Black Sunrise}, R1556 {Second Tradition: Domain} and R1569 {Sense the Savage Way} — three copies of one sentence. (b) "If some minions cannot be targeted because of another effect, the action will simply have no effect on the things it cannot target" [RTR 20080808] on R0575 {Edged Illusion} and R2256 {Jaroslav Pascek} — identical. (c) "must be announced as part of the terms of the action" [RTR 20111202] on R1416 {Ravnos Carnival} and R2465 {Travis Miller} — identical.

**Recommendation:** Keep one ruling from each cluster: R1556 for (a), R0575 for (b), R1416 for (c). Cluster (b) is worth prose in its own right — an untargetable subset does not invalidate the announcement, the action simply has no effect there — and pairs naturally with R2569, so state it once and cite one card.

*Rulings (7):* R0157, R1556, R1569, R0575, R2256, R1416, R2465

### [low] misfiled

R2202 {Epikasta Rigatos.1} — "Can only retrieve a card played during that same action" — is a scope restriction on one vampire's retrieval ability, not a statement about what is fixed at announcement or about directedness. It rode in on the {Clio's Kiss} retrieval-template cluster but says something different from it.

**Recommendation:** Low priority since it is secondary here. If its PRIMARY is 1.11 (ash heap retrieval) it is fine to leave the cross-ref; if 3.1 is its PRIMARY it should move to 1.11 or become C, since the ruling changes no other card's handling.

*Rulings (1):* R2202

## 3.10

### [medium] duplicate-template

Four rulings across four chunks are the same wording template: a card whose text keys on "the acting minion/vampire" reads the *substituted* designation, so it fires (or is barred) on the substitute rather than the original. R1343 {Powerbase: Savannah} "takes into account effects that change who is considered the acting vampire in combat"; R0660 {FBI Special Affairs Division} "does not trigger if the ally is considered the acting minion"; R1257 {Obedience} "cannot be played if the opponent is not the acting vampire, for example if a slave took his place"; R1599 {Shadow Boxing} "cannot be used by a Slave that entered combat instead of the acting minion". One principle, four instances. Note also the cross-chunk role drift: R1343 was labelled P while the three identical-in-kind rulings were labelled E.

**Recommendation:** State once in prose: an effect that reads "the acting minion" reads the current designation, including a substituted one — both for triggering and for legality of play. Keep two "e.g." cards spanning the two polarities: R1257 {Obedience} (barred because the substitute is now the actor) and R0660 {FBI Special Affairs Division} (trigger suppressed). Drop R1343 and R1599 to the example pool or leave them in the database; do not list four cards. Cross-reference 5.9 for the general "effects read and write traits" rule instead of restating it.

*Rulings (4):* R1343, R0660, R1257, R1599

### [medium] missing-topic

Nothing in the membership says what happens to the *replaced* minion. The only trace is R1102's parenthetical ("for purposes of the No Repeat Actions rule") and R1117's aside ("not counting blood spent"). No ruling here covers whether the original actor stays locked, whether it is credited with having taken the action for NRA/once-per-turn purposes, or what becomes of costs it already paid. A second silent sub-topic: substitution relative to an already-declared block or an already-resolved stealth/intercept exchange — R1117 covers reactions already *played* as an eligibility bar, but not the state of a block in progress.

**Recommendation:** Flag both to the drafter as thin. The replaced-minion state can probably be written from R1102 + R1117's parenthetical plus a cross-reference to 3.5 (NRA) and 1.7 (costs already paid); if it cannot, mark it ⚠ REVIEW rather than inventing a rule. Do not manufacture prose for the block-in-progress case — there is no ruling for it.

*Rulings (2):* R1102, R1117

### [low] duplicate-template

R0467 ({Deep Song}.2) and R1215 ({Nar-Sheptha}.2) are the same ruling stated reciprocally on the two cards it concerns — same reference [ANK 20211022], same rule (a later effect changing the acting minion in combat supersedes an earlier one), each naming the other card as the example. Both are P/PRIMARY here, so the extract presents one rule as two principles.

**Recommendation:** Merge into a single sentence with both reference IDs in one footnote. This is also 5.9's "later effect governs, earlier resurfaces if the later lapses" rule on the acting-minion trait — state it as the acting-minion instance and cross-reference 5.9 rather than deriving it independently. R1214 ({Nar-Sheptha} burned → designation reverts for the rest of combat) is the useful companion and should be kept, since it supplies the "earlier resurfaces" half.

*Rulings (2):* R0467, R1215

### [low] over-absorbed

Both are single instances of principles already stated by stronger rows in the same section, and both are two-card interactions rather than transferable rules. R0706: "{Mask of a Thousand Faces} cannot be used to take over, since it requires an unlocked vampire and the action requires a locked one" — a direct application of R1117's eligibility rule to one specific card pair. R2063: "If used by a Banu Haqim and another takes the action over with {Mask}, they cannot use it again" — a direct application of R1124's already-stated "cannot use a limited effect if a limited effect has already been used on the action".

**Recommendation:** Keep at most one as the "e.g." illustrating eligibility — R0706 is the clearer of the two because the lock-state conflict makes the eligibility test concrete. Leave R2063 in the database; R1124 already states its rule generally, and the ruling adds only the card pairing.

*Rulings (2):* R0706, R2063

## 3.2

### [high] duplicate-template

Draba (R0531-R0534) and Night Terrors (R2085-R2088) carry four VERBATIM-identical rulings each, with the same ruling references — a 4x2 duplicate block that is 8 of the section's 38 rows (21%). R0531/R2085 share [RTR 20030519], R0533/R2087 share [LSJ 20021211], R0534/R2088 share [ANK 20200607], R0532/R2086 share [ANK 20190628]. A drafter reading the extract will see each principle twice and may mistake the repetition for two independent lines of authority.

**Recommendation:** Collapse to one card as the worked example — keep Draba (R0531-R0534, the older/denser reference set) and demote the Night Terrors four to C or to a bare '(same for {Night Terrors})' parenthetical. Note that the four principles themselves are distinct and all belong in 3.2: the -X stealth modifier framing, playable by a non-blocker, playable with no effect, and the declare-block-first ordering.

*Rulings (8):* R0531, R0532, R0533, R0534, R2085, R2086, R2087, R2088

### [medium] other

Unresolved tension on the section's central question — may a stealth/intercept modifier be added before it is needed? One group says yes unconditionally: R1459 {Repulsion} 'can be used even if the stealth is not currently needed', R1312 {Phased Motion Detector} 'grants intercept even if the bearer is not blocking yet', R0532/R2086 'can be played by a minion who is not attempting to block', R1920 {Under Siege} 'even if the vampire is already unlocked', R0533/R2087 'can be played on a minion with no or negative stealth, in which case it has no effect'. The other says no: R1126 {Mask of a Thousand Faces} 'cannot be used if no stealth is needed yet', R0649 {Familial Bond} 'cannot be played if intercept is not required (rules 6.2.2)', R2374 {Osric Vladislav} 'only if he is acting and stealth is needed'. Written naively these produce contradictory sentences.

**Recommendation:** Adjudicate before drafting. The reconciliation is almost certainly that the default is permissive (play freely, even to no effect) and the prohibitions come from the individual cards' own conditional wording ('if needed' / rulebook 6.2.2 requirement clauses) — but that has to be decided and stated, not left implicit. This cluster deserves a !TENSION slug (no-effect-plays) grouped for a single ruling.

*Rulings (10):* R1459, R1312, R0532, R2086, R1920, R1126, R0649, R2374, R0533, R2087

### [medium] duplicate-template

Three verbatim copies of the sect-change template, all citing [ANK 20190416]: R1160 {Ministry}, R1373 {Protection Racket}, R2454 {Teresita, The Godmother} — 'The additional intercept is gained or lost if the acting vampire changes sect during the action'. Two are filed secondary (fine as cross-refs) but R2454 is PRIMARY here, which risks 3.2 restating a principle 5.9 owns.

**Recommendation:** Keep ONE as the 3.2 example of intercept persistence being re-evaluated mid-action, and cross-reference 5.9 (traits & trait-change precedence, which per the taxonomy was created precisely for this 'later effect governs, and it re-reads mid-action' rule) rather than restating it. R2454 should be secondary here with 5.9 primary.

*Rulings (3):* R1160, R1373, R2454

### [medium] duplicate-template

Three verbatim copies of 'Can be played when failing to block because of stealth: it is still declining to block', all citing [ANK 20211003]: R0473 {Deflection}, R1211 {My Enemy's Enemy}, R1441 {Redirection}. All three are correctly secondary here, but the principle they teach is a blocking-sequence fact (3.3: what counts as declining to block), not a stealth/intercept-addition fact. 3.2 only needs the consequence.

**Recommendation:** Keep at most one in 3.2's extract as the pointer that failing on stealth is not a distinct state, and let 3.3 carry the principle. Do not write three e.g. cards for one wording.

*Rulings (3):* R0473, R1211, R1441

### [medium] misfiled

R1725 {Starshell Grenade Launcher}.1 — 'Using the Launcher to reduce stealth does not force the minion to strike with it if he blocks' — is PRIMARY 3.2 but teaches nothing about stealth or intercept. Stealth reduction is merely the ability that was used; the rule is that exercising an equipment's non-strike ability does not commit the bearer to striking with that weapon.

**Recommendation:** Reassign primary to 4.10 (weapons & equipment in combat), or 4.3 (choosing strikes); 3.2 secondary at most. Contrast R1726, the same card's other ruling, which IS 3.2 material (how often stealth may be reduced in one action).

*Rulings (1):* R1725

### [low] duplicate-template

Five rulings all resolve to the same principle — how many times per action an intercept/stealth-modifying ability may be used is fixed by that card's own wording template. R1311 {Phased Motion Detector} 'only once during each action' [RBK wording-templates], R2123 {Angelica} 'once per action if she needs intercept', R2344 {Matteus} 'multiple times during the same action', R2374 {Osric Vladislav} 'more than once during an action', R1726 {Starshell} 'multiple times in the same action if the bearer manages to unlock'. Five e.g. cards for one principle exceeds the 1-3 style rule.

**Recommendation:** Keep two contrasting examples — one once-per-action ({Phased Motion Detector}, which already cites the rulebook wording-template anchor) and one repeatable ({Matteus}) — and cross-reference 1.2, which owns periodicity templates. Drop the rest to the database or leave them unused in the example pool.

*Rulings (5):* R1311, R2123, R2344, R2374, R1726

### [low] recoverable-C

R0234 {Bonding}.2 — '[DOM] Cannot be used to increase the stealth of a non-bleed action' — is a pure reading of that card's own scoping clause. It fails non-obviousness: a bonus written onto a bleed does not apply to other actions is something any judge fluent in the rulebook already knows, and it fails transfer in any useful sense.

**Recommendation:** Demote to C. If the drafter wants the general point at all it is a one-clause aside under 1.2 (wording scope), not a 3.2 example.

*Rulings (1):* R0234

### [low] missing-topic

Nothing in the membership addresses the asymmetry between stealth and intercept as quantities: stealth is added once against the action and stands against every would-be blocker, while intercept is per-minion and must be re-paid by a second blocker. Nor is there any ruling on whether excess stealth or intercept carries over to a subsequent block attempt on the same action. The scope line's 'persistence during the action' is currently served only by the sect-change trio and R2320 {Marciana Giovanni}.2 ('for the duration of the action').

**Recommendation:** Flag for the drafter: this sub-topic will have to be written from the rulebook ([RBK who-may-attempt-to-block] is already cited by R2123) rather than from rulings. Also check 3.3's and 3.6's memberships — a ruling covering it may have been filed there and not cross-coded here.

## 3.3

### [high] duplicate-template

35 of the 117 rows (30% of the section, all PRIMARY) are four boilerplate wordings from the "unlock/wake a minion to block" card family, each repeated verbatim on 5-12 different cards with a single shared reference. The classifiers could not see the duplication from inside their chunks; as membership this reads as an exhaustive card list, which the style rules forbid.

**Recommendation:** Collapse to four principle statements, each with at most three "e.g." cards, and let the remaining ~25 rulings stay in the database. Suggested keepers: (a) "an unlock/wake effect may be used by a minion that is already attempting to block" — R1554 {Second Tradition: Domain} (the only copy that spells out the locked-vampire case), R0816 {Guardian Vigil}, R1177 {The Mole}; (b) "such an effect cannot be used at all if the minion is barred from attempting to block (eg. {Daring the Dawn})" — R0810 {Guard Duty}, R1555, R2067; (c) "unlocking to block does not override the prey/predator/target restriction on who may block" — R0811 {Guard Duty}, R1900 {Trophy: Domain}; (d) "the block attempt and the resulting combat still happen even if the unlock removes the action's target (eg. {Ambush})" — R0812 {Guard Duty}, R0408 {Coterie Tactics}. Note that {Guard Duty}, {Under Siege}, {Trophy: Domain}, {Second Tradition: Domain} and {Sense the Savage Way} each carry three of the four templates, so one or two cards can anchor all four.

*Rulings (35):* R0155, R0581, R0816, R1177, R1228, R1263, R1425, R1554, R1567, R1693, R1694, R1921, R0156, R0406, R0582, R0614, R0810, R1555, R1568, R1899, R1917, R2067, R0158, R0408, R0616, R0812, R1557, R1570, R1901, R1919, R0157, R0615, R0811, R1900, R1918

### [high] duplicate-template

Three more wordings account for another 16 rows: the block-declaration sequencing template ("if another Methuselah is the target, he must declare whether he attempts or declines to block before X can be played", 6 identical PRIMARY rows plus R0865 as a near-variant), the stealth-failure template ("can be played when failing to block because of stealth: it is still declining to block", 5 rows on one reference [ANK 20211003]), and the wake-effect template ("the vampire need not attempt to block nor play further reaction cards: that is merely an option", 4 rows all labelled P on one reference [TOM 19951129]).

**Recommendation:** Keep one statement of each with 1-3 e.g. cards: sequencing — R0865 {Hide the Heart} (it is the only copy carrying [RBK sequencing], so it anchors the rule to the rulebook) plus R0534 {Draba} (adds the used-vs-played distinction the others lack); stealth-failure — R0473 {Deflection} plus R1824 {Telepathic Misdirection}; wake-optionality — a single instance, R1993 {Wake with Evening's Freshness}, since all four are the same sentence on the same ruling. R0627/R0708/R1261 add nothing. Note this template is arguably 5.2's (waking does not compel a block) and could be a cross-reference rather than prose here.

*Rulings (16):* R0534, R0697, R0880, R1227, R1541, R2088, R0865, R0473, R1053, R1211, R1441, R1824, R0627, R0708, R1261, R1993

### [medium] scope-drift

Eight secondary rows are two "continue as if unblocked" templates repeated across {Shadow Body}, {Shadow Boxing}, {Those Who Endure Judge}, {Toreador's Bane} and {Torrent} — five copies of "Methuselahs that had declined to block do not get another opportunity to block" and three of "all action modifiers and reaction cards are still in effect, even those pertaining to a successful block", all on [ANK 20190116] / [RTR 19941109]. 3.6 explicitly owns this topic ("per-block effects provided again on second block; re-block opportunities"), and R0561 {Eagle's Sight}.2 already gives 3.3 its own hook into it.

**Recommendation:** Cross-referencing 3.6 is legitimate, but eight copies is bulk. Keep one of each wording as the cross-reference (R1858 and R1857, both on {Those Who Endure Judge}, so a single card carries both halves) and drop the other six from 3.3's extract. The drafter should state the declined-block consequence in 3.3 in one sentence and point to 3.6 for the rest.

*Rulings (8):* R1591, R1596, R1857, R1858, R1869, R1870, R1876, R1877

### [medium] misfiled

Three rulings state the same rule about ordering effects that fire on a successful block: an effect that resolves at the moment of the block must resolve before any other effect may be used, while effects triggering at the same moment are all applied and ordered by the acting Methuselah ([ANK 20210627] [ANK 20211207] [ANK 20220116] on all three). That is 2.4's principle (simultaneous effects & ordering; controller chooses order), not 3.3's declaration sequence. R0121 {Banshee Ironwail}.2 is filed PRIMARY here.

**Recommendation:** Re-primary R0121 to 2.4 with 3.3 secondary, and treat R1150/R1931 the same way. They are also a duplicate set: keep R1931 {Unleash Hell's Fury}.1 as the worked example (it is the fullest wording and names both polarities) and let R1150 {Millicent Smith} stay in the database. R0121 is additionally worth keeping for its "REVERSAL of earlier rulings" flag.

*Rulings (3):* R0121, R1150, R1931

### [medium] over-absorbed

Six rows carry P/E but are pure one-card text interpretations that transfer to no other card. R1078 {Madness Network}.4 is a burn condition on one card ("attempt to block the action to burn the Madness Network"). R0071 {Archon}.1 reads Archon's own text ("regardless of which action the Archon was taking"). R2198 {Edward Vignes}.1 is "his ability cannot be used if the action is blocked" — one card's ability. R1183 {Momentary Delay}.5 turns on "if the other conditions are met" on that card. R1139 {Melange}.2 is about the card being in the ash heap, not about blocking at all. R1934 {Unleash Hell's Fury}.4 is the interaction of one card's text with {Faceless Night}.

**Recommendation:** Recover to C. R0071 and R1078 are the two that matter — both are PRIMARY here and would otherwise reach the drafter as blocking material. The general rule behind R0071 (a blocker pays the block's blood cost regardless of the action) is better carried by the template cluster in the next finding.

*Rulings (6):* R1078, R0071, R2198, R1183, R1139, R1934

### [medium] other

Two rulings in this section pull against each other on whether a declared block attempt can be withdrawn. R0631 {Faceless Night}.1: "a minion attempting to block before it is played cannot back out", reinforced by R1123 {Mask of a Thousand Faces}.10 ("a minion attempting to block before is still attempting to block after"). R1842 {Tenebrous Form}.1: "a minion previously attempting to block can resign his attempt and pay no blood". A drafter writing 3.3's irrevocability rule from this membership would write contradictory sentences.

**Recommendation:** Adjudicate before drafting. The likely reconciliation is that the attempt persists but a blood cost keyed to blocking is not paid once the block cannot succeed — but that is not what either wording says, so it needs a judge ruling rather than a drafter's inference. Mark the resolved statement with the section's irrevocability principle and cite both cards.

*Rulings (3):* R0631, R1842, R1123

### [medium] missing-topic

3.3's scope line leads with "block declaration sequence", but nothing in the 117 rows states the base sequence itself: the order in which Methuselahs get the chance to declare, that only one minion may block, or that a minion may make only one block attempt per action. Everything present is sequencing *relative to a card play* (R0534's template) or *implicit* declination (R0075 {Archon Investigation}, R0471 {Deflection}). The drafter will have to source the spine of the section from the rulebook with no ruling support.

**Recommendation:** Flag for the drafter that 3.3's opening paragraph must be written from [RBK sequencing] (reachable via R0865 {Hide the Heart}.4, the only row in the section citing it) rather than from the extract, and that no footnote will back it. Also check whether "who may block" rulings landed primarily in 3.2 — this section only ever states that restriction negatively, via R0560/R0637/R2132.

*Rulings (3):* R0075, R0471, R0534

### [low] misfiled

Two small clusters sit closer to other sections. (a) The blood-cost-of-blocking template "a vampire with no blood can still block, they burn what they can" [LSJ 19970707] appears four times (R0074, R0274, R1523, plus the R2187 {Dónal O'Connor} variant), with R2188 adding the timing ("immediately upon successfully blocking, regardless of whether combat begins"). The principle — an effect naming an amount the target may not hold takes what is there — is 1.7's, explicitly per its scope line. (b) "The maneuver can only be used if the block is successful, and only in the resulting (block-induced) combat; it does not carry over to a follow-up combat" recurs three times (R0808, R0817, R1348) and is about which combat a rider attaches to, which is 4.9/4.2 material.

**Recommendation:** Cluster (a): keep one copy in 3.3 as an E on the block-cost point — R2187 {Dónal O'Connor}.1 is the clearest — and make 1.7 the primary owner of the template. Cluster (b): keep R0808 {Guard Dogs} only, as a cross-reference; R0817 and R1348 are the same sentence on other cards.

*Rulings (8):* R0074, R0274, R1523, R2187, R2188, R0808, R0817, R1348

## 3.4

### [high] duplicate-template

The section's core principle — an unblocked action whose target has become illegal is successful but has no effect (and must still be paid) — is present 14 times across three near-identical wordings: the LSJ 20070411/20090514 'if the target unlocks' template (R0040 Ambush, R0328 Charge of the Buffalo, R0686 Fleetness, R1092 Make the Misere, R1245 Nose of the Hound, R1363 Principia Discordia, plus the variants R2054 Young Bloods and R0824 Harass), the ANK 20181121 'not unlocked anymore when it resolves ... must be paid' template (R0089 Art's Traumatic Essence, R1151 Mind Numb, R1707 Spirit Marionette.6), and the target-removed-by-another-effect cases (R2000 War Ghoul, R2003 Warsaw Station, R1839 Temptation.8). Under the no-exhaustive-lists rule this is one principle with at most three 'e.g.' cards, not fourteen entries.

**Recommendation:** Draft one principle sentence covering both halves (successful, no effect, cost still paid). Keep R0040 {Ambush} as the canonical unlock case, R1707 {Spirit Marionette} for the must-still-pay rider, and R2003 {Warsaw Station} for target-removed-by-another-effect. Leave the remaining eleven in the database; drop them from the extract so the drafter is not tempted to enumerate.

*Rulings (14):* R0040, R0328, R0686, R1092, R1245, R1363, R2054, R0824, R0089, R1151, R1707, R2000, R2003, R1839

### [high] misfiled

The [RTR 20010711] 'can target a minion holding less than the amount named' template is filed here — four of the seven as PRIMARY — but taxonomy 1.7's scope line explicitly claims it: 'effects naming an amount the target may not hold (steal/transfer templates take what is there)'. R0522 {Diversion} '[tha] can target a vampire with no blood', R0530 {Donnybrook} 'can target a minion with less than 2 blood or life', R0537 {Drain Essence}, R1019 {Leech} are pure legality-of-target + amount-taken rulings; R1159 {Minion Tap}.2 'you take what you can' and R1024 {Legacy of Caine}.2 'stealing zero blood' and R0770 {Gift of Proteus}.2 'if there are less cards available ... all of them are put on the Gift' are the same rule on other resources. None of them turns on success-vs-effect; they turn on cost/amount arithmetic.

**Recommendation:** Reassign PRIMARY to 1.7 (3.1 as secondary for the targeting-legality half). If any stays visible to 3.4 it should be one cross-reference only. Within 1.7 this is again one template: keep {Drain Essence} and {Minion Tap} as the 'e.g.' pair.

*Rulings (7):* R0522, R0530, R0537, R1019, R1159, R1024, R0770

### [medium] duplicate-template

Fifteen rulings on hunt success, eleven of them the byte-identical [LSJ 20050720-2] string 'A hunt is not successful if no blood is gained, even if the hunt action is still successful' (R0046, R0667, R0729, R0898, R0910, R1130, R1468, R1675, R1754, R1786, R1996), plus R0878 {Hunger Moon} as a paraphrase and R1856 {Thirst} / R1894 {Triole's Revenge} as consequences. Taxonomy 3.7.2 explicitly owns 'hunt success requires gain'; all eleven are correctly `secondary` here, but eleven copies of one sentence bloat 3.4's extract for zero added signal. R0876 {Hospital Food} is the odd one: it is P PRIMARY in 3.4 while stating the same 3.7.2 rule from the other side ('the action is successful even if no blood is gained').

**Recommendation:** Keep at most one hunt row visible to 3.4 as the cross-reference illustrating that 'the action succeeded' and 'the effect happened' are separate predicates, and cross-reference 3.7.2 for the rest. Re-point R0876 to PRIMARY 3.7.2.

*Rulings (15):* R0046, R0667, R0729, R0878, R0898, R0910, R1130, R1468, R1675, R1754, R1786, R1996, R0876, R1856, R1894

### [medium] scope-drift

There is a seam. On one side sits the outcome topic the scope line names — success vs. effect, 'successful but no effect', what is read at resolution (R0040-family, R1854, R2068, R0549). On the other sits a pure sequencing topic: the 'when the action/bleed would be successful' window and what may or may not be played after it — the six {Spying Mission} rulings (R1713-R1719), the three {Andre LeRoux} rulings (R2117, R2118, R2120), R1822 {Telepathic Counter}, R1086 {Major Boon}, R0507 {Dis Pater}, and the three [LSJ 19980105] copies R1210 / R1440 / R1823. That is ~15 rulings whose content is ordering of effect windows, i.e. chapter 2 material (2.1 'who may act when', 2.3 'after resolution'). It is defensible to keep here because the window is defined by success, but the drafter should be told it is a second sub-topic, not more of the first.

**Recommendation:** Do not re-code, but structure 3.4 as two explicit sub-topics: (a) success vs. effect at resolution, (b) the 'would be successful' window and its closure. Cross-reference 2.1/2.3 from (b) rather than restating window mechanics. Within (b), the [LSJ 19980105] triple R1210/R1440/R1823 is one template — keep one.

*Rulings (15):* R1713, R1714, R1715, R1717, R1718, R1719, R2117, R2118, R2120, R1822, R1086, R0507, R1210, R1440, R1823

### [medium] misfiled

Three rulings are here on shared vocabulary rather than shared principle — exactly the failure the taxonomy's own 'shared vocabulary is not a shared gap' control warns about. R0658 {Fata Amria}.3 and R1971 {Vengeance of Samiel}.2 are the identical [LSJ 20030902-2] string 'Does not prevent the opponent from dodging, the dodge just has no effect' — that is dodge scope, 4.6, and the words 'no effect' are the only tie to 3.4. R2585 (G00050 'Improve weapon before resolution') defines 'before resolution' as 'after strikes have been declared but before they resolve' — that is strike resolution, 4.3 / 4.10, not action resolution; a general-rule entry landing in the wrong chapter is worse than a card ruling doing so, because general entries are prime prose material.

**Recommendation:** Drop all three from 3.4's extract. R0658 and R1971 to 4.6 (and they are one template — keep one). R2585 to 4.3 with 4.10 secondary.

*Rulings (3):* R0658, R1971, R2585

### [medium] over-absorbed

{Spying Mission} contributes six P/E rows (R1713-R1719) and {Andre LeRoux} three more, for one principle. Several are pure one-card readings. R1715: 'Once in play, it must be burned on the next successful bleed against the same Methuselah, it cannot be used to increase an unsuccessful bleed of zero' — the burn-on-next-bleed clause is Spying Mission's own card text and transfers to nothing. R1714: 'No reaction can be played afterwards to make the bleed unsuccessful and "beat" the Spying Mission' restates R1713/R1719 with no new content. R1718 and R2120 are pairwise card-vs-card adjudications ({Mask of a Thousand Faces} after Spying Mission; LeRoux after Spying Mission) that follow mechanically once the window rule is stated.

**Recommendation:** Keep R1719 as the principle statement ('played when a bleed would be successful, before resolution') and R1717 as the one worked consequence ('{Archon Investigation} cannot be played after'). Re-role R1715 and R1714 to C. R1718 and R2120 can stay as unused example pool but should not become prose.

*Rulings (4):* R1714, R1715, R1718, R2120

### [low] misfiled

R1779 {Swarm}.2 — 'If the action to employ the Swarm is blocked, the Swarm goes on the acting minion immediately, before combat, if any' — is E PRIMARY here but concerns an employ-retainer action that was blocked, i.e. what a specific card does on failure. It is not about success-vs-effect or resolution wording, and 3.7.4 explicitly owns employ/recruit action specifics.

**Recommendation:** Reassign PRIMARY to 3.7.4. Given it is one card's placement rule, C is also defensible.

*Rulings (1):* R1779

### [low] recoverable-C

Three P/E rows are card-text readings that teach nothing a judge could carry to another card. R1757 {Sudario Refraction}.3 is card machinery throughout: 'if no copy of a named card is in the ash heap upon resolution ... the effect still resolves for the other copies and the acting Methuselah discards 3 cards'. R2198 {Edward Vignes}.1, 'His ability cannot be used if the action is blocked', is a bare restatement of that card's timing and fails non-obviousness. R0794 {Great Symposium}.2, 'The search can fail, you still get to distribute 3 blood', names the card's own quantity and is a sibling of the ruling the classifier contract already cites as the C archetype.

**Recommendation:** Re-role all three to C. If the drafter wants the underlying idea — a partly-impossible effect resolves for the parts that are possible — R0575 {Edged Illusion} / R2256 {Jaroslav Pascek} ('the action will simply have no effect on the things it cannot target') already state it generally and are the better anchors.

*Rulings (3):* R1757, R2198, R0794

### [low] missing-topic

Nothing in the membership states the base rule in general terms. Every P is a card-attached instance: the closest is R0004 {Abactor}.1, which defines '"successful resolution" means the action must not be blocked and the vampire must have gained blood' — but that is Abactor's own compound condition, not the general definition. There is no general-rule (G000xx) entry and no card-free statement of what makes an action successful, when resolution occurs, or the relationship between 'resolves', 'succeeds' and 'has an effect'. The drafter has abundant material for the exceptions and no anchor for the opening paragraph.

**Recommendation:** Flag to the drafter that 3.4's opening definition must be written from the rulebook (via rulebook2024/content.md, [RBK …] footnote) rather than from a ruling, and check whether a G-entry on action resolution exists elsewhere in the corpus that was routed to 3.1 or 3.5.

*Rulings (2):* R0004, R0089

## 3.5

### [high] duplicate-template

Nineteen rows are the SAME sentence — "The action has reached resolution, so is subject to NRA (Non Repeatable Action) rules" — carrying the same reference pair [RTR 20180719] [ANK 20211015] on nineteen different cards across many chunks. This is 17% of the section's entire membership restating one rule. No classifier could see the scale of it; the drafter receiving the raw extract will see nineteen identical lines and cannot tell they are one principle.

**Recommendation:** Collapse to ONE principle statement plus at most three e.g. cards chosen to span the distinct triggers, not the distinct cards: an action-ending modifier (R0316 {Change of Target}), a reaction that makes the action fail (R0315 {Champion}), and a vampire ability (R2281 {Krassimir}). Note in the extract that the remaining 16 are the identical template so the drafter does not mine them. Keep R0995/R1797 ({The Kiss of Ra}, {Tangle Atropos' Hand}) OUT of this collapse — they are the negative pole ("has NOT reached resolution") and are the contrast the principle needs.

*Rulings (19):* R0151, R0284, R0315, R0316, R0496, R0596, R0635, R0673, R0860, R0863, R1097, R1251, R1389, R1396, R1432, R1540, R1559, R1942, R2281

### [high] duplicate-template

Sixteen rows are the "action ends unsuccessfully immediately, no other action modifier or reaction can be played afterwards" template ([RTR 20180719] [ANK 20200207]), with two combat-flavoured variants (R0187, R0252: "combat begins immediately"). Same defect class as the NRA template: one rule, sixteen cards.

**Recommendation:** One principle — an action that ENDS closes the window immediately — with three e.g. cards: R1796 {Tangle Atropos' Hand} (cancel), R1169 {Mirror Walk} (ends on block, and it already carries the useful negative list {Freak Drive}/slave rule/{Sowing Dissension}), and R0252 {Brujah Frenzy} for the combat-begins variant. Draft this template back-to-back with the "fails" template below — the contrast between ended (nothing playable after) and failed (end-of-action effects still playable) is the substantive content, and it is currently buried under 24 duplicate rows.

*Rulings (16):* R0150, R0187, R0219, R0252, R0322, R0351, R0771, R0994, R1089, R1143, R1169, R1172, R1256, R1369, R1622, R1796

### [medium] duplicate-template

Eight rows are the "if the action fails, modifiers and reactions that can be used at the end/after an action can still be used afterwards" template ([LSJ 20041022] [RTR 20180719] [ANK 20221205]). Filed PRIMARY on some cards (R0495, R1539, R1941) and secondary on others (R0283, R0314, R0862) for identical text — cross-chunk drift on the same wording.

**Recommendation:** One principle plus two e.g. cards; R1173 {Mistaken Identity} and R0495 {Detect Authority} suffice. Drop the other six from the extract.

*Rulings (8):* R0283, R0314, R0495, R0862, R1096, R1173, R1539, R1941

### [medium] duplicate-template

The three sameness-test rulings are triplicated verbatim across {Change of Target}, {Obedience} and {Red Herring}: rulebook actions are not the same as card-provided actions (R0317/R1252/R1433), rulebook actions differ by target and equip-from-minion targets the equipment (R0318/R1253/R1434), and actions from different cards in play are not the same even at equal name (R0319/R1254/R1435). Nine rows, three principles. Note R0319 states it as "different cards in play are not the same" while R1254/R1435 state "not the same if the card is not the same" — same rule, and the drafter should not mistake the phrasing gap for a distinction.

**Recommendation:** Keep exactly one copy of each of the three principles and cite a single card for the set (R0316/R0317/R0318 {Change of Target} is the natural anchor, since it also carries the reached-resolution and action-ended rows). These three ARE the definitional core of the section's sameness test and should become prose, not e.g. — but as three sentences, not nine.

*Rulings (9):* R0317, R1252, R1433, R0318, R1253, R1434, R0319, R1254, R1435

### [medium] duplicate-template

Six more principles each arrive as an exact duplicated pair across two cards: damage applies if the action reached resolution even if it ended (R0449 {Daring the Dawn} = R0704 {Force of Will}); damage does not apply if canceled before resolution (R0450 = R0705); canceled action may be re-attempted unless it was blocked-then-continued (R0995 {The Kiss of Ra} = R1797 {Tangle Atropos' Hand}); the action was still taken for counting effects (R0996 = R1798); canceled combat leaves the action blocked and {Mask of a Thousand Faces} unusable (R0133 {Bear-Baiting} = R1969 {Venenation}); a would-be-successful block still triggers its effect even if the action ended (R0021 {Aching Beauty} = R1932 {Unleash Hell's Fury}). Each pair also drifted on role/centrality: R0133 is P PRIMARY but its twin R1969 is E secondary; R0021 is P PRIMARY but its twin R1932 is E secondary.

**Recommendation:** Keep one of each pair as the principle and the other as its single e.g. Cite {Tangle Atropos' Hand} and {The Kiss of Ra} together for the cancel pair since the document will want the blocked-then-continued exception spelled out once. The R0133/R1969 pair overlaps 3.6 (continue as if unblocked) — cross-reference rather than restate.

*Rulings (12):* R0449, R0704, R0450, R0705, R0995, R1797, R0996, R1798, R0133, R1969, R0021, R1932

### [medium] misfiled

"Multiple copies can be played by different minions on the same action" ([ANK 20200515]) appears three times identically — {Blanket of Night}, {Mouthpiece}, {Zapaderin} — all P/E PRIMARY in 3.5. This is a limit on repeating a CARD PLAY within one action, not on repeating an ACTION. 3.5 owns the No Repeated Action rule; nothing here touches reached-resolution, sameness of actions, or cancellation.

**Recommendation:** Reroute to 1.15 (cumulative & stacking: multiple copies each exerting their effect) with 1.2 as secondary; keep at most a cross-reference from 3.5. If retained anywhere in 3.5's extract it should be one row, not three.

*Rulings (3):* R0165, R1201, R2057

### [medium] misfiled

{Major Boon}.2 — "Cannot be played in succession. The loss from the play of a Major Boon is due to a card effect, not a bleed. So a second cannot be played to Boon the first" — is filed here on the surface word "cannot be played in succession". The principle it actually teaches is that a card-effect pool loss is not a bleed, which is 3.7.1 / 6.5. It says nothing about repeating an action, reached resolution, or cancellation.

**Recommendation:** Drop from 3.5's extract; 3.7.1 (bleed) primary, 6.5 secondary. This is the exact 'filed by surface resemblance' failure golden rule 3 warns about.

*Rulings (1):* R1087

### [medium] missing-topic

Two gaps the drafter will hit. (a) Nineteen rulings say an action 'is subject to NRA rules' but not one ruling in the section STATES what the NRA rule is — per-minion or per-Methuselah, what 'attempt' means, whether a different minion may take the action. R0153 {Black Forest Base}.1 ('cannot be attempted twice even if the first attempt was blocked and failed') is the closest thing to a statement of the rule, and it is filed E. The rule itself will have to come from the rulebook, not from this extract. (b) Canceled BLOCKS, named explicitly in 3.5's scope line, are supported by exactly one ruling: R0421 {Crocodile's Tongue}.1 ('the canceled block isn't successful or unsuccessful. It is simply canceled'). Canceled combats by contrast have five.

**Recommendation:** Flag to the drafter that the NRA statement needs an [RBK] citation, and that the canceled-block sub-topic rests on a single ruling — either write it thin and honest around R0421, or fold it into the canceled-combat discussion rather than giving it its own paragraph.

*Rulings (2):* R0153, R0421

### [low] misfiled

Three secondary rows have no 3.5 hook at all. R0571 {Echo of Harmonies}.5 is about the political action card's presence in the ash heap at resolution ({Delaying Tactics}) — 1.11 / 2.5. R0598 {Enticement}.2 is about losing the Edge mid-action — 6.5 / 3.7.1. R2368 {Nergal}.3 is about an ability not counting as used when the cost cannot be paid — 1.5 / 1.7. None concerns repetition, resolution-reached, or a canceled action.

**Recommendation:** Remove from 3.5's extract. Low severity because all three are secondary and presumably sound under their PRIMARY code — this is extract noise, not a lost ruling.

*Rulings (3):* R0571, R0598, R2368

### [low] over-absorbed

Four rows restate a principle already stated generally elsewhere in the membership, with nothing card-transferable added. R0435 {Dabbler}.1 is the whole ruling: "Cannot be used if the action is canceled" — a bare instance of R2598's "if an action is canceled, it is not performed", failing both the transfer and non-obviousness tests. R1422 {React with Conviction}.2 names one specific interaction ("If used to cancel a {Corruption} action... the corruption counters are not burned") of the same rule. R2046 and R2048 are two rows on the same card saying the same thing by two mechanisms — the acting minion not being ready after combat, and getting out of torpor immediately — both reducing to "the action ends and no referendum is conducted".

**Recommendation:** Treat R0435 as C. Keep at most one of R2046/R2048 (R2046 is the more general statement). R1422 is usable as the single e.g. for 'cancellation undoes the cost' if the drafter wants one, but it should not sit alongside R0593 {Enrage} and R2077 {Mobile HQ} as three separate examples of the same point.

*Rulings (4):* R0435, R1422, R2046, R2048

## 3.6

### [high] duplicate-template

Four verbatim boilerplate templates, replicated onto every card that grants continuation, account for 59 of the 108 rows (55%): 'all action modifiers and reaction cards are still in effect' (16 copies), 'Methuselahs that had declined to block do not get another opportunity' (16), 'cannot continue after a combat resulting from a successful action' (12), 'moves the action card from the ash heap to limbo' (15). Each is one principle, not 12-16 examples.

**Recommendation:** Treat these as four principle sentences in prose, not as an example pool. The continuation-granting cards are interchangeable illustrations, so cite at most {Form of Mist}, {Mirror Image} and {Momentary Delay} (or {Crypt's Sons}) once for the whole cluster and let the remaining 13 cards (Ambulance, Chameleon's Colors, Flow Within the Mountain, Foresee, Morphean Blow, Peacemaker, Shadow Body, Shadow Boxing, Those Who Endure Judge, Toreador's Bane, Torrent, Wamukota) stay in the rulings database. Note the ash-heap/limbo template (D) is the only one of the four that is non-obvious and deserves its own paragraph; the others compress to two or three sentences.

*Rulings (59):* R0036, R0305, R0428, R0691, R0716, R0724, R1163, R1179, R1194, R1298, R1590, R1595, R1857, R1869, R1876, R2500, R0037, R0306, R0429, R0692, R0717, R0725, R1164, R1180, R1195, R1299, R1591, R1596, R1858, R1870, R1877, R2501, R0038, R0307, R0693, R0718, R0726, R1165, R1181, R1196, R1592, R1597, R1871, R1878, R0039, R0308, R0430, R0694, R0719, R0727, R1166, R1182, R1197, R1300, R1593, R1598, R1872, R1879, R2502

### [high] duplicate-template

A second template pair — 'X can only be used if the block is successful, and only in the resulting (block-induced) combat; it does not carry over to a follow-up combat' (10 copies) and 'X is provided again if a second block happens on the same action' (12 copies) — recurs across 12 reaction cards spanning many chunks. The only variation is what X is (maneuver, damage prevention, strike: combat ends, strike restriction, equipment restriction).

**Recommendation:** State this once as a single scoping principle: an effect a reaction card provides on a successful block is scoped to that block instance — it applies only in the block-induced combat, and is provided afresh if the action continues and is blocked again. The variation in X is exactly the material for the 1-3 'e.g.' slots: keep one maneuver card ({Guard Dogs} or {Instinctive Reaction}), {Precognition} for prevention, and {Night Terrors} for strike: combat ends. Drop the other nine cards. R0630 ({Eyes of the Beast}) and R0815 ({Guardian Vigil}.2) are the same rule in reworded form and add nothing.

*Rulings (22):* R0134, R0808, R0817, R0937, R1549, R1662, R1709, R2060, R2089, R2091, R0135, R0809, R0938, R1350, R1550, R1663, R1710, R2061, R2090, R2092, R0630, R0815

### [medium] scope-drift

Two wordings of one rule — 'if the combat continues or a new combat occurs, the continue-as-if-unblocked effect is lost' and 'effects that end combat and then do something else after combat (including continuing the action as if unblocked) will be lost, except for unlock effects' — carry the same reference pair [LSJ 19980109] [RTR 20020501] but were filed inconsistently: the first is PRIMARY on five rows (R0309, R0695, R1167, R1198, R1594) and secondary on three (R0728, R1873, R1880), while the second, which is the more general statement, is secondary on all ten.

**Recommendation:** Pick one owner and be consistent. 4.9 explicitly claims 'effects lost when new combat queued', so the general form belongs there as PRIMARY and 3.6 should carry it as a single cross-reference sentence ('a queued or continuing combat destroys the continuation effect — see 4.9') rather than as five PRIMARY prose rulings. If the project prefers 3.6 to own it, make R0653/R1380/R2102 etc. PRIMARY here too; the current split will make both drafters write the same paragraph.

*Rulings (18):* R0309, R0695, R1167, R1198, R1594, R1873, R1880, R0728, R0653, R0698, R0828, R0849, R1380, R1453, R1825, R2102, R2251, R2327

### [medium] scope-drift

Within the block-scoped-effect template, the identical 'does not carry over to a follow-up combat (eg. {Psyche!})' sentence is PRIMARY-in-3.6 on seven rows and secondary on three, and its role label flips between P (R0937, R1549, R2060, R2089, R2091) and E (R1662, R1709) for the same text. Classic cross-chunk drift on one wording.

**Recommendation:** Harmonise. The forward-looking half ('does not carry over to a follow-up combat') is really 4.9/4.1 material — the block-induced combat ended — while the 'provided again on a second block' half is squarely 3.6's scope line. Filing the first as secondary here (as R0134/R0808/R0817 already do) and the second as PRIMARY would make the section consistent and stop 3.6 and 4.9 both claiming the {Psyche!} follow-up case.

*Rulings (10):* R0937, R1549, R1662, R1709, R2060, R2089, R2091, R0134, R0808, R0817

### [medium] over-absorbed

{Gift of Proteus}.2 is a pure one-card interpretation of that card's own counter mechanic: 'At action resolution, the number of cards declared must be put on the card. If there are less cards available ... then all of them are put on the Gift.' Continuation is mentioned only as an incidental reason fewer cards exist; the ruling teaches nothing about continuing as if unblocked.

**Recommendation:** Drop from 3.6 (it is already secondary here, so the cost is only extract noise). If it teaches anything transferable it is 1.7's 'effect naming an amount the target may not hold' template, not 3.6; otherwise C.

*Rulings (1):* R0770

### [low] recoverable-C

{Forced Awakening}.4 ('The vampire needs not pay a blood if he successfully blocks, even if the action continues as if unblocked') is scoped to Forced Awakening's own blood-payment clause, and it is a singleton — no other card in the section shows the same template, unlike its sibling R0712 which pairs with R2035 ({WMRH Talk Radio}) and is therefore genuinely general.

**Recommendation:** Demote to C, or at most keep as a bare cross-reference example under the principle that a condition already satisfied by a successful block stays satisfied through continuation. Keep R0712 + R2035 as the general pair ('effects do not consider blocks made before the card was played'), which is the transferable rule here.

*Rulings (1):* R0711

### [low] missing-topic

The section states two things that a drafter will have to reconcile and has no ruling that does it: the core template says 'all action modifiers and reaction cards are still in effect' after continuation, while {Eagle's Sight}.2 and {Falcon's Eye}.3 say an intercept bonus 'only applies to one block attempt' and another is needed. Nothing in the membership states the general boundary — which added values persist onto the second block attempt (stealth, action modifiers) and which are consumed by the block attempt they were played for.

**Recommendation:** Flag for the drafter as a known thin spot: 3.6 will need one sentence distinguishing effects that persist for the action's duration from per-block-attempt values that are spent, with 3.2 as the cross-reference. Also absent: the blocker's lock state after a continued action (R1969 covers it only for the canceled-combat case). No new classification work implied — this is a gap in the corpus, not a misfiling.

*Rulings (4):* R0561, R0638, R0036, R0305

## 3.7.1

### [high] duplicate-template

Five rows are the SAME sentence with the SAME two references — "A limited bleed modifier can be played before or after. [LSJ 20100218] [RTR 20180511-2]" — spread over five cards and five different chunks (R0375 {Command of the Beast}, R0523 {Divine Image}, R1035 {Leverage}, R1337 {Power of One}.2, R1404 {Quicksilver Contemplation}.2). They are one principle about the "limited" bleed-modifier template, not five examples, and the style rule caps illustrations at three. The cross-chunk drift is also visible in the role column: three were labelled E and two (R1337, R1404) P for byte-identical text.

**Recommendation:** Collapse to one principle statement of the limited-bleed-modifier timing rule, keeping at most two "e.g." cards (suggest {Command of the Beast} and {Power of One} — different disciplines, both [DOM]/[pot]/[pre] coverage); demote R0523, R1035, R1404 to C or leave them in the database. The rulings that actually add content to this same principle are R0721 (bonus lost mid-action stops counting against the limit) and R0720 (a modifier played where it can have no effect still counts / does not count) — those, not the five clones, should carry the section's prose.

*Rulings (7):* R0375, R0523, R1035, R1337, R1404, R0721, R0720

### [medium] duplicate-template

Two more identical-wording pairs recur across chunks. (a) "Can only be used during a bleed action. [ANK 20171023] [RTR 19941109]" appears verbatim on R0392 {Confusion} and R1336 {Power of One}.1 — same text, same two refs. (b) The "acting bleeding minion" restriction appears as R2065 {Haqim's Law: Retribution}.4 ("Can only be used by an acting bleeding minion") and R2135 {Anu Diptinatpa}.2 ("Her ability can only be used on an acting bleeding minion"), both citing the identical [ANK 20220502].

**Recommendation:** Keep one card per template: one of R0392/R1336 for the "only during a bleed action" restriction, one of R2065/R2135 for the "acting bleeding minion" restriction. Note that (b) is arguably a 1.5 principle (an ability requiring its bearer to be the participant) applied to bleed — cross-reference 1.5 rather than restating it here.

*Rulings (4):* R0392, R1336, R2065, R2135

### [medium] over-absorbed

Two P/E rows are pure one-card arithmetic or pronoun-resolution with no transferable content. R2119 {Andre LeRoux}.4: "He can use his ability on his own bleed to get (-1 +2) = +1 bleed" — the entire ruling is the sum of one card's two numbers. R2398 {Prejudice}.2: "He is the one to get the bleed bonus" — this only says which of two minions on one card receives the bonus; it changes no ruling on any other card. Both fail the transfer test.

**Recommendation:** Reclassify R2119 and R2398 as C with a note (single-card arithmetic / single-card referent resolution, nearest section 3.7.1). Neither belongs in the drafter's extract.

*Rulings (2):* R2119, R2398

### [medium] misfiled

Four rows are mandatory-action rulings that happen to name a bleed; 3.9 (added on exactly this evidence — the taxonomy cites R2525 {Elen Kamjian}.2 and R2526 {Elen Kamjian}.3 by name as 3.9's founding sub-topics) owns them. Nothing in "she is free to take any action" (R2524), "another bleed action does not count as the bleed her ability forces" (R2525) or "she is stuck and cannot act" (R2526) teaches a bleed rule; substitute any other action type and the rulings are unchanged. R1704 {Spirit Marionette}.3 is the same shape (a card-provided bleed discharges the obligation), with slightly more bleed content.

**Recommendation:** Drop R2524-R2526 from 3.7.1's membership entirely — they are correctly PRIMARY in 3.9 and here they only pad the bleed extract. R1704 may stay as a cross-reference if the drafter wants an example of a bleed performed by playing a card; if not, drop it too. 3.7.1 should cross-reference 3.9 for mandatory bleeds rather than carry the rulings.

*Rulings (4):* R2524, R2525, R2526, R1704

### [medium] missing-topic

Given a section titled "Bleed", the fundamentals are absent from the membership. There is no ruling on the base bleed action itself (bleed at 1, prey only, effects allowing a non-prey or cross-table bleed), none on what a successful bleed does (target burns pool, and the pool-loss-vs-burn distinction that 6.5 half-owns), and none on the mechanics of redirection beyond R0470's target-validity rule — nothing on what a redirected bleed carries over (announced modifiers, stealth/intercept, whether the new target is now "the target of the action"). The only statement that a bleed reduced to zero is no longer successful arrives as a secondary row on one card (R2120 {Andre LeRoux}.5).

**Recommendation:** Expect the drafter to source these from the rulebook rather than the extract, and flag the redirection sub-topic in particular: {Deflection}-style redirection is named in 3.7.1's scope line but the extract supplies only R0470, R0472, R1161, R1304 and R0721, none of which state what survives the redirect. Promote R2120 to a PRIMARY 3.7.1 row so the "bleed reduced to zero is not a successful bleed" principle is visible to the drafter.

### [low] over-absorbed

Three further rows are marginal absorptions I would defend only weakly. R0965 {Justicar Retribution}.1 ("Counts the bleed amount that each vampire would have when attempting to bleed his prey") is a measurement rule internal to one card's text. R1372 {Protected Resources}.3 ("If you perform a bleed action that resolves as a bleed for 0, you don't burn your Protected Resources") is a corollary of R1371, which already states the general point. R1138 {Melange}.1 is a card-specific burn-timing window; its general content is 2.1 material, not bleed.

**Recommendation:** Demote R0965 and R1372 to C (R1371 alone carries the Protected-Resources principle: limiting pool burned is not modifying the bleed amount). For R1138, either C or reprimary to 2.1 with 3.7.1 as secondary.

*Rulings (3):* R0965, R1372, R1138

### [low] scope-drift

Roughly a third of the section is not about bleed as a mechanic but about WHEN a bleed-modifying card may be played and whether it counts against the one-modifier limit. That is timing (2.1) and template semantics (1.2) wearing bleed vocabulary — R1301 {Pentex Loves You!}.1 says so explicitly ("the ability to increase bleed is treated as an action modifier: it can be used at any time during the action"). This is the seam in the membership: modifier-timing on one side, bleed amount/target/redirection (R0470, R0472, R1161, R1304, R0866, R1370-R1372) on the other.

**Recommendation:** Not a split — the two halves are close enough for one section — but the drafter should state the modifier-timing half as an application of the 2.x windows with a cross-reference, not re-derive it, and should keep the bleed-specific half (target validity, redirection, reduction, pool-burn limiting) as the section's spine. The de-duplication above shrinks the timing half from ten rulings to about three, which fixes most of the imbalance on its own.

*Rulings (10):* R0375, R0392, R0523, R1035, R1301, R1336, R1337, R1404, R0720, R0721

## 3.7.2

### [high] duplicate-template

Thirteen rulings are the SAME sentence citing the SAME reference [LSJ 20050720-2] — "A hunt is not successful if no blood is gained, even if the hunt action is still successful" — each filed here as P/PRIMARY on a different card (Anarch Free Press, Festivo dello Estinto, Foul Blood, Hunger Moon, Immaculate Vitae, Inbase Discotek, Masquerade Endangered, Restricted Vitae, Songs of the Distant Vitae, Succulent Vitae, Tainted Vitae, Wanderer's Counsel, XTC-Laced Blood). R0878 is the same ruling paraphrased in Hunger Moon's own terms. This is 35% of the section's membership stating one principle thirteen times, and thirteen P labels invite a drafter to write it thirteen times or to build a card list — the exact thing the no-exhaustive-lists rule forbids.

**Recommendation:** Collapse to one P statement of the principle (a hunt action can resolve successfully while the hunt itself is not successful; effects keyed to "successful hunt" do not fire when zero blood is gained) plus at most three "e.g." cards. Keep R0878 {Hunger Moon} (shows the consequence stated in the card's own terms), R1856 {Thirst} (the converse framing: the hunt must be successful to avoid the effect), and one blood-quality card such as R1786 {Tainted Vitae}. The remaining ten stay in the rulings database.

*Rulings (13):* R0046, R0667, R0729, R0878, R0898, R0910, R1130, R1468, R1675, R1754, R1786, R1996, R2044

### [high] other

Direct contradiction inside the section on where hunt-bonus blood comes from, all four rows P/PRIMARY and all citing [RTR 20030519]. R0666 {Festivo dello Estinto} and R0909 {Inbase Discotek, Frankfurt} read "the hunt bonus applies to non-standard hunt actions, it comes from the blood bank NOT from the target of the hunt". The two general-rule entries R2539 (G00004|Hunt bonus) and R2604 (G00064|Special Hunt Action) read "Blood comes FROM THE TARGET of the hunt" and add a second reference [RTR 20180511]. A drafter working from this extract cannot write the sentence; whichever way they guess, half the section's own evidence says the opposite.

**Recommendation:** Adjudicate before drafting. The extra [RTR 20180511] on the two general entries suggests a 2018 ruling revised the 2003 one and the card-level copies were never updated; verify against the original references and the current rulings database. Whatever the resolution, draft from the general entries (R2539/R2604) as the P source and mark the sentence ⚠ REVIEW until confirmed. Consider tagging the four rows !TENSION:hunt-bonus-blood-source so the conflict is not silently averaged away.

*Rulings (4):* R0666, R0909, R2539, R2604

### [medium] duplicate-template

Three verbatim copies of "Cannot choose to target a vampire when using another non-standard hunt action (eg. {Abactor})" [LSJ 20090606], on {Legacy of Caine}, {Week of Nightmares} and {Kyoko Shinsegawa}, all E/PRIMARY. One principle, three identical entries.

**Recommendation:** Keep one as the "e.g." — R1027 {Legacy of Caine} is the clearest carrier since the card is the archetypal blood-stealing hunt. State the principle once (a card granting a hunt action defines its own targeting; the right to name a vampire as hunt target does not travel to other special hunt actions) and drop the other two. Note this pairs with R2018 {Week of Nightmares}.1, which is the permissive side of the same rule and is worth keeping as the contrast case.

*Rulings (3):* R1027, R2019, R2286

### [medium] duplicate-template

Two smaller template repeats. (a) "The effect only applies to the default hunt action provided by the rulebook" appears as R1741 {Strained Vitae Supply} [PIB 20120204] and R2245 {Igo the Hungry} [PIB 20150820-2] — same rule, two cards. (b) The steal-what-is-there rule appears twice with inconsistent roles: R1024 {Legacy of Caine}.2 "hunting on a target that has no blood to steal … will simply have no effect, stealing zero blood" as E, and R2285 {Kyoko Shinsegawa}.4 "cannot steal more blood than the target has" as P.

**Recommendation:** For (a) keep R2245 {Igo the Hungry} as the single "e.g." — it names the contrast card {Loki's Gift} explicitly — and cross-reference rather than repeat on R1741. For (b) keep one; the general rule ("effects naming an amount the target may not hold take what is there") is explicitly owned by 1.7 per its scope line, so 3.7.2 should cross-reference 1.7 and keep at most R1024 as the hunt-flavoured illustration, not restate the principle as P.

*Rulings (4):* R1741, R2245, R1024, R2285

### [medium] over-absorbed

Five of the section's 37 rows are {Kyoko Shinsegawa} (R2282-R2286), more than any other card. Three of them are near-duplicates of principles already carried elsewhere in the section (R2285 duplicates R1024; R2286 duplicates R1027/R2019) and R2283 "She can only perform the action provided by her ability once per turn" [PIB 20121112] is a periodicity reading of one card's text with no hunt content at all. The risk is a section written around one vampire.

**Recommendation:** Keep R2282 (a card-granted action is a hunt action and receives hunt bonuses — the load-bearing one) and R2284 (a special hunt ability may pick among other granted hunt actions). Drop R2285 and R2286 as duplicates. R2283 is correctly marked secondary and belongs to 1.2 (periodicity, "once each turn"); it need not appear in 3.7.2's extract at all.

*Rulings (5):* R2282, R2283, R2284, R2285, R2286

### [medium] other

R1894 {Triole's Revenge} — "he still burns if the benefit of the hunt is reduced to zero" [TOM 19951212-3] — sits adjacent in the extract to thirteen rulings saying a hunt yielding no blood is not successful. Read side by side these produce contradictory sentences: one says zero blood gained means the hunt failed, the other says zero benefit still counts. The reconciliation (Triole's keys on the hunt ACTION, not on a successful hunt) is not stated anywhere in the membership.

**Recommendation:** Either drop R1894 or keep it deliberately as the worked contrast that makes the action-vs-hunt distinction concrete, and write the distinction explicitly: "successful hunt action" and "successful hunt" are different conditions, and each card must be read for which one it names. Tag !TENSION:hunt-success-vs-action-success. Note R1894 also carries the only blocking-related statement in the section.

*Rulings (3):* R1894, R0046, R0667

### [low] misfiled

Two rows whose principle is owned elsewhere. R0047 {The Anarch Free Press}.2 "Using it for the hunt bonus does not make the hunt an action 'requiring an Anarch'" [ANK 20220317] is P/PRIMARY here but teaches a requirements rule — taking a card's bonus does not import that card's requirements into the action — which is 1.6. R2378 {Pariah}.2 "His ability still applies when in torpor" is correctly marked secondary but has no hunt content; it is 1.5/5.3 material.

**Recommendation:** Reassign R0047's primary to 1.6 with 3.7.2 as secondary (it is a fine cross-reference, just not a hunt principle). Leave R2378 as a secondary or drop it from the extract; do not let it pull the drafter into writing about torpor here.

*Rulings (2):* R0047, R2378

### [low] missing-topic

The membership is entirely about (a) hunt success requiring blood gain and (b) non-standard/special hunt actions and hunt bonuses. Nothing in it states the base rulebook hunt action itself — that it is an undirected action, that it is blockable (implied only in passing by R1894), the default amount gained, or what happens when the hunter is at or over capacity (touched by exactly one card-specific ruling, R2402 {Rabbat}). There is also no ruling on hunt-value REDUCTION as distinct from bonuses, though R1048 {Loki's Gift} shows the corpus knows the distinction exists.

**Recommendation:** The drafter must source the base-hunt-action paragraph from the rulebook ([RBK …]) rather than from rulings, and should expect the capacity-overflow and hunt-reduction sub-topics to be thin or absent. Flag those two as ⚠ REVIEW rather than inventing a principle from R2402, which on its own is a single-card reading.

## 3.7.3

### [high] duplicate-template

Two interlocking boilerplate templates account for 9 of 40 rows (22% of the section) across only 5 cards — the Beast/Enkidu/Helen Fairchild/Howler/Lorrie Dunsirn 'cannot use equipment' minions. Template A, verbatim on 5 cards with identical refs [LSJ 20050315] [LSJ 20010210]: 'He/She cannot attempt an action to equip (or employ), nor strike to steal an equipment (or retainer).' Template B, verbatim on 4 of the same 5 cards with ref [LSJ 20050315]: 'He/She can equip with an equipment that is a location when in play.' These are one principle with two halves, not nine data points, and 8 of the 9 are PRIMARY or otherwise land squarely in 3.7.3's extract.

**Recommendation:** Keep R2155 (the fullest wording — covers equip, employ and strike-to-steal in one line) plus R2201 as the location-equipment counterexample, and one more at most. Drop R2200/R2230/R2241/R2305 and R2156/R2231/R2306 to C. Separately, template B's principle is a card-type point — a locquipment is a location while in play, so an equipment prohibition does not reach it — which 1.3 owns; it should be a cross-reference from 3.7.3 to 1.3, not 3.7.3 prose.

*Rulings (9):* R2155, R2200, R2230, R2241, R2305, R2156, R2201, R2231, R2306

### [high] duplicate-template

The bare 'This is an "equip action"' template recurs on six cards across chunks, five of them citing the identical single reference [TOM 19960130]: Children of Stone.1, Jack of Both Sides.1, Magic of the Smith.1, Sleight of Hand.1, Lambach.1, plus Bloodstone.1 ('It's still an equip action'). Four are labelled P, so four separate rulings each claim to state the section's principle — the drafter receives the same one-sentence statement five times with nothing to distinguish the cases.

**Recommendation:** Keep R1081 (Magic of the Smith) as the canonical P for 'a card that puts equipment into play via an action provides an equip action', plus R0948 (Jack of Both Sides) because it adds a real second sub-case — the same card provides an equip action or an employ action depending on what it fetches — and R0218 (Bloodstone) because it draws the downstream consequence (the action can be modified by {The British Museum, London}). Drop R0348, R1657, R2288 to C as identical restatements.

*Rulings (6):* R0348, R0948, R1081, R1657, R2288, R0218

### [medium] duplicate-template

The 'equipped vs. merely put into play' template recurs verbatim on three cards under one reference [LSJ 20090506] — Incriminating Videotape.2, Mokolé Blood.2, Shilmulo Tarot.3 all read 'If it is not equipped but merely put into play (eg. {Alastor}), it does not get X. It does is if it is equipped (eg. {Magic of the Smith}).' R0680 (Flaming Candle.2) is the same distinction from the other direction. All four are PRIMARY or E in this section.

**Recommendation:** This is the section's best principle — an on-equip trigger fires only on an actual equip action, not on an effect that puts the card into play — so keep it, but as one principle with two examples: R0915 and R0680 (which shows the converse: a card already in play can still be put into play by a non-equip effect). Drop R1176 and R1629 to C; they are word-for-word R0915 with a different payload.

*Rulings (4):* R0915, R1176, R1629, R0680

### [medium] duplicate-template

'His/Her ability applies when equipping in a non-normal way' recurs verbatim on three cards under the single reference [PIB 20150105-2] — Synner-G.1, Topaz.1, Vulture.1, differing only in the parenthetical card ({Pier 13, Port of Baltimore} twice, {Concealed Weapon} once). R0438 (Dagger.1) is the same principle applied to an equipment's own on-equip search.

**Recommendation:** Keep R2462 (Topaz.1) as the single 'e.g.', optionally with R0438 since it shows the trigger on the equipment rather than on the equipper. Drop R2444 and R2498 to C. Note for the drafter: this template and the [LSJ 20090506] template above are the two halves of one rule and should be written together — a non-normal equip is still an equip; being put into play is not.

*Rulings (4):* R2444, R2462, R2498, R0438

### [medium] misfiled

Both Lucian rulings are P/PRIMARY in 3.7.3 but neither concerns an equip action. R2310 is explicit that it is a combat rule — 'The stolen equipment cannot be used until the next round' with reference [RBK steal-equipment] — and R2309 ('Cannot attempt to steal a piece of equipment that he is prohibited from having') governs a strike to steal, not an action. 3.7.3's scope line is 'equip from hand/minion; equipment movement actions'; a strike is neither.

**Recommendation:** Reassign both to 4.10 (weapons & equipment in combat) as PRIMARY — 4.10 explicitly owns 'stolen/destroyed mid-combat'. R2309 may keep 1.6 as secondary (a prohibition on holding blocks the acquisition). 3.7.3 should cross-reference 4.10 rather than carry these. The same seam runs through the template-A rulings above, whose 'nor strike to steal' clause is 4.10 material embedded in a 3.7.3 sentence.

*Rulings (2):* R2309, R2310

### [medium] over-absorbed

Shackles of Enkidu.2 is E/PRIMARY but is a pure disambiguation of one card's own noun phrase: "'The shackled minion' refers to the minion the card is placed upon (not the Gangrel the card is put on with the equip action)." It resolves which of two minions a single card's text means. It fails transfer — no other card is ruled differently because of it — and reaches nothing about equip actions beyond the fact that one occurred.

**Recommendation:** Reclassify C with a note that it is a referent-disambiguation on {Shackles of Enkidu} alone; nearest section 3.7.3. Leave it in the rulings database.

*Rulings (1):* R1585

### [low] misfiled

Both NRA PAC rulings are filed here (R1248 PRIMARY) but the principle each teaches is about the duration and persistence of an in-play effect, not about equipping. R1248 — 'Does not affect equip actions performed prior to its arrival in play' — states that an ongoing effect does not reach events that predate it. R1249 — minions who equipped while it was in play still fail to unlock 'regardless of whether NRA PAC is still in play or not' — states that a locked-in consequence survives the source leaving play. 'Equip action' is only the trigger these two rules happen to attach to.

**Recommendation:** Move R1248 to 2.5 (duration & persistence) as PRIMARY with 3.7.3 secondary; R1249 to 2.5 with 5.2 (lock & unlock) secondary. If either is kept in 3.7.3 at all, keep only R1249 and only as a cross-reference.

*Rulings (2):* R1248, R1249

### [low] duplicate-template

The No-Repeated-Action template arrives here three times verbatim, on {Change of Target}, {Obedience} and {Red Herring}, with identical references [RTR 19950509] [LSJ 20080710] [ANK 20200502]: 'Actions without card (provided by the rulebook) can be repeated if they have different targets. Equipping from a minion targets the equipments: if one equipment is the same, the action is the same.' All three are secondary rows whose PRIMARY is presumably 3.5, so this is correctly a cross-reference — but the drafter of 3.7.3 needs the sentence once, not three times.

**Recommendation:** Keep one (R0318) as 3.7.3's cross-reference to 3.5 and drop the 3.7.3 secondary code from R1253 and R1434. No change to their PRIMARY filing. Low severity because secondary rows are cheap by contract; flagged because three identical copies in a 40-row extract is exactly the cross-chunk drift signature.

*Rulings (3):* R0318, R1253, R1434

### [low] recoverable-C

Reg Driscoll.2 — 'You may move all or none the equipment he gets to just one minion, but you cannot split' — is E/PRIMARY but reads as an interpretation of one ability's own distribution wording. Transfer is weak: no other card's ruling changes because of it. It is borderline rather than clear-cut, since 'an effect moving several equipment moves them to a single destination' is statable generally, but nothing else in this membership supports that as a template.

**Recommendation:** Reclassify C with a note (nearest 3.7.3), unless a later pass finds a second card with the same all-or-none movement wording, in which case it becomes the second leg of a real principle. R2407 (Reg Driscoll.1) should be kept regardless — its point that a location-equipment cannot be moved while in play is general and links to 1.3.

*Rulings (1):* R2408

### [low] missing-topic

Nothing in the 40 rows covers the base mechanics of the equip action itself. There is no ruling on when the equipment's pool cost is paid, on what happens to the card when the equip action is blocked, or on whether the equip action is targeted at the equipping minion for stealth/intercept purposes (R1940 {Unlicensed Taxicab} touches stealth but only for the equipment's own bonus). The membership is entirely about which effects count as equip actions, which triggers fire, and who may not equip — the sub-topic 'what an equip action is procedurally' is unrepresented.

**Recommendation:** Warn the drafter that 3.7.3's opening paragraph will have to be written from the rulebook ([RBK] citation) rather than from rulings, and that R1954 ({Vast Wealth}.4 — illegal placement burns the equipment without cost) is the only membership row that touches cost/legality at all. If the section stays this thin procedurally, consider whether it survives as its own heading or folds into 3.7 with a cross-reference to 4.10.

## 3.7.4

### [high] duplicate-template

Twelve of the 44 rows (27% of the section) are one ANK 20180517 wording. Nine are verbatim identical — "He/She can lock to use his/her ability the turn he/she is recruited" (R0247 Brigitte Gebauer, R0535 Draeven Softfoot, R0566 Eccentric Billionaire, R0766 Gianna di Canneto, R0773 Giulia Giovanni Abruzzina, R1501 Rom Gypsy, R1521 Saatet-ta, R1777 Survivalist, R1944 Vagabond Mystic) — and three are same-ruling variants on the same reference (R0285 Carlton Van Wyk "can use his ability to burn a vampire...the turn she is recruited", R1922 Underbridge Stray "can burn 1 life to give a minion a press the turn he is recruited", R2001 War Ghoul "can use its ability to lock and burn...the turn it is recruited"). They all state a single principle: the recruited-this-turn restriction bars taking ACTIONS, not using abilities — including abilities whose cost is locking. This is exactly the exhaustive-card-list failure the style rules forbid.

**Recommendation:** State the principle once (the restriction on a newly recruited minion is on acting, not on ability use; locking as an ability cost is not acting) and cite at most three cards spanning the sub-cases: one plain lock-to-use case (R0247 or R1501), R1922 (burn-life ability, no lock), and R2001 (lock-and-burn). Drop the remaining nine to the database. Cross-reference 1.5 (ability use is not a card play / not an action), which is where the principle actually lives; 3.7.4 should carry only the recruit-turn instance.

*Rulings (12):* R0247, R0535, R0566, R0766, R0773, R1501, R1521, R1777, R1944, R0285, R1922, R2001

### [medium] scope-drift

The membership splits cleanly at a seam the taxonomy watch list already predicted ("3.7.4 is overloaded — its scope line mixes the employ/recruit actions with 'acting the turn recruited', which is a minion-state fact"). This unit confirms it with a hard boundary. Side A — the ACTION and its non-normal substitutes: what counts as an employ/equip action (R0948, R1314 Piper "this is not an action, so cost reductions referring to an action do not apply", R2521 Zhenga), which effects attach to recruiting vs. to the action (R1688, R2151, R2300, R2522), requirements/cost of the recruited card vs. of the action (R1206, R1766, R1761), replacement timing (R0405), whose disciplines are read (R1316). Side B — WHAT A FRESHLY RECRUITED MINION MAY DO: the 12-ruling ANK 20180517 pile, plus R1313/R1767 ("the ally cannot act this turn"), R0928/R1243 ("can act the turn it is recruited" does not reach an opponent's turn), R0978 (wraiths can act the turn put into play). Side B is a state fact about allies and retainers, not a fact about the action, and half of it is really 1.5.

**Recommendation:** Do not create a new code — split the scope line at Phase 4.5 as the watch list proposes. Keep 3.7.4 for the action (announcement, cost, requirements, cancellation, and the non-normal-recruitment substitutes). Move the "acting/using abilities the turn recruited" material to 5.5/5.6 with a cross-reference from 3.7.4, or state it once in 1.5. The drafter should not be asked to write both topics under one heading.

*Rulings (13):* R0247, R0928, R1243, R1313, R1767, R1761, R0978, R1314, R1315, R1316, R2151, R2521, R0405

### [medium] duplicate-template

Four rulings state the same thing about effects keyed to recruiting rather than to the action: R2300 Little Tailor of Prague and R2522 Kuyén are word-for-word identical ("His ability works on allies recruited in a non-standard way (eg. {Piper})", same refs ANK 20210913 / LSJ 20090116); R2151 Baba Yaga ("applies when she recruits or employs...in a non-normal way") and R1688 Soul of the Earth ("Reduction applies to allies or retainers recruited in a non-normal way") are the same principle in different words.

**Recommendation:** One principle with a two-sided statement, which is the section's best material: an effect keyed to the recruit/employ EVENT applies however the minion arrived, while an effect keyed to the ACTION does not (the counterpole is already present as R1314 Piper.2 and R2521 Zhenga.3). Keep R2300 and R1688 as the "e.g." for the first pole and R1314/R2521 for the second; drop R2522 (identical to R2300) and R2151.

*Rulings (4):* R2300, R2522, R2151, R1688

### [medium] duplicate-template

Three rulings are the same wording on the same two references [LSJ 20050315] [LSJ 20010210]: R2127 Angelo ("cannot attempt an action to employ a retainer, nor strike to steal a retainer"), R2155 The Beast and R2305 Lorrie Dunsirn (both "cannot attempt an action to equip or employ, nor strike to steal an equipment or retainer"). They teach one thing — a printed prohibition on equipping/employing also blocks acquiring by strike — which is a card-restriction reading rule, not a recruitment rule.

**Recommendation:** Keep one (R2155, the fuller wording covering both equip and employ) as an "e.g."; drop R2127 and R2305. Consider whether 1.1 ("cannot" absolute; reading card text) or 5.7 is the better owner, with 3.7.4 and 3.7.3 carrying cross-references rather than three copies.

*Rulings (3):* R2127, R2155, R2305

### [medium] over-absorbed

Three rows are pure single-card text interpretation. R1998 War Ghoul.1 — "If you have no other allies and no retainers in play when it is recruited, then you burn it" — is the resolution of War Ghoul's own printed cost and changes no other card's ruling (fails transfer). R1778 Swarm.1 — "the vampire receiving the Swarm does not get to move the Swarm on to a new target" — turns entirely on Swarm's own move-on text. R1779 Swarm.2 — "the Swarm goes on the acting minion immediately, before combat" — likewise resolves Swarm's own blocked-employ text.

**Recommendation:** Reclassify all three as C with a transfer-test note. R1778 and R1779 are the only rulings in the section touching the blocked/failed employ action, so if the drafter wants that sub-topic it must be sourced from the rulebook, not from Swarm.

*Rulings (3):* R1998, R1778, R1779

### [low] duplicate-template

Three further exact pairs. R1313 Piper.1 and R1767 The Summoning.3 both say the recruited ally cannot act this turn, on identical refs [LSJ 20080630] [RTR 20180303]. R0928 Infernal Servitor.1 and R1243 Nocturn.1 are verbatim identical on [ANK 20200813-3]. R1207 Muricia's Call.2 and R1765 The Summoning.1 are verbatim identical on [ANK 20180817] ("Does not prevent the acting vampire from playing the retainer/ally directly this turn if he unlocks (not the same action)").

**Recommendation:** Keep one of each pair. Note that the R1207/R1765 pair, together with R1315 Piper.3 ("does not count as performing the action to recruit this ally in respect to section 3 of the rules"), is NRA material: 3.5 owns the sameness question and is already drafted, so 3.7.4 should cross-reference it rather than restate it.

*Rulings (6):* R1313, R1767, R0928, R1243, R1207, R1765

### [low] role-error

Cross-chunk inconsistency on identical text, which golden rule 5 forbids. R1501 Rom Gypsy and R1521 Saatet-ta are marked P while nine word-for-word-identical siblings are marked E. R1313 Piper.1 is P while R1767 The Summoning.3, the same statement on the same references, is E.

**Recommendation:** Cosmetic given P/E is explicitly low-stakes, and it resolves itself once the duplicate sets are collapsed. Reported only as corroborating evidence that these sets were labelled independently across chunks with no shared reading.

*Rulings (4):* R1501, R1521, R1313, R1767

### [low] missing-topic

Two sub-topics of the employ/recruit action have no general ruling. (1) What happens when the action is blocked or fails — where the ally/retainer card goes, and whether the cost is refunded — is represented only by R1779, a Swarm-specific ruling. (2) Nothing states whether an ally or retainer enters play locked or unlocked, which is the premise the whole ANK 20180517 pile depends on (they all turn on the minion being able to lock).

**Recommendation:** Flag both to the drafter as rulebook-sourced rather than ruling-sourced. The second is load-bearing: the section cannot state the "lock to use an ability the turn recruited" principle without first fixing the entry state, and no ruling in the corpus supplies it.

*Rulings (1):* R1779

## 3.7.5

### [high] duplicate-template

The "automatically passing referendum" rule is filed 12 times across at least 8 chunks, all tracing to the same reference pair [PIB 20150105] [LSJ 19980107]. Four of them (R0333 Charming Lobby.2, R0432 Cryptic Rider.1, R0500 Dia de los Muertos.1, R1098 Malkavian Rider Clause.1) are byte-identical sentences; R0084/R0945/R1997/R2557 are the identical short form "Cannot be used during a referendum that is automatically passing"; R0520/R1403 are the same rule phrased as "cannot be burned". This is one principle with three micro-variants, not 12 examples, and violates the no-exhaustive-card-lists rule by an order of magnitude.

**Recommendation:** Keep three: R2557 (G00022|Vote change — the general rule entry, states the rule with no card doing the work, P), R0333 (the full-form statement including the "effects that operate on the number of votes passed by have no effect" clause), and R1988 (Voter Captivation.3 — the only one teaching the complementary after-window plus the X=0 corollary). Optionally R0433 as the "can be used after" contrast if the drafter wants the boundary shown on a second card. Demote the remaining 8 to C or leave them as unused example pool; they add no wording the kept three do not carry.

*Rulings (12):* R0333, R0432, R0500, R1098, R0084, R0945, R1997, R2557, R0520, R1403, R0433, R1988

### [high] duplicate-template

The "effect is applied after the referendum effects are applied, including any oust and pool gained from it" template recurs 8 times, six of them from the single ruling [LSJ 20090115-2] (R1889 Treachery.1, R0819 Guru.1, R2141 Armin Brenner.1, R2189 Donald Cargill.1, R2190 Donald Cargill.2, R2315 Lutz von Hohenzollern.1), plus R2316 and R2417 restating the same ordering. R2141/R2189/R2315 are word-for-word identical ("His ability is applied after the referendum effects are applied, including any oust and pool gained from it") on three different vampires.

**Recommendation:** Keep three: R1889 (states the rule on the pool-burn template), and the R2190/R2316 pair, which is the only non-obvious content in the cluster — the ability still applies when the *predator* is ousted by the referendum (R2190) but not when the *controller* is ousted (R2316, explicitly a reversal of prior rulings). Drop R0819, R2141, R2189, R2315, R2417 as redundant restatements.

*Rulings (8):* R1889, R0819, R2141, R2189, R2315, R2417, R2190, R2316

### [medium] other

R1889 and R1890 are both P/PRIMARY on the same card and state opposite rules. R1889 (Treachery.1): "The pool is burned after the referendum effects are applied, including any oust and pool gained from it" [LSJ 20090115-2]. R1890 (Treachery.2): "The pool is burned when the votes are tallied, before applying the referendum effects" [RTR 20010710]. A drafter receiving both as principle-stating rows will write a contradictory sentence about when referendum-keyed pool costs are paid.

**Recommendation:** Adjudicate before drafting. The dates suggest the 2009 LSJ ruling supersedes the 2001 RTR one; if so R1890 should be demoted (superseded, C) and 3.7.5 states the after-effects rule with R1889 as its anchor. If the distinction is real, the section must say which template each applies to. Mark ⚠ REVIEW if unresolved — this is exactly the kind of point that needs judge confirmation.

*Rulings (2):* R1889, R1890

### [medium] duplicate-template

Five further exact-duplicate cross-chunk pairs, each the same sentence and the same reference filed on two cards: R0474/R1829 ("May be played before, during, or after votes and ballots have been cast" [LSJ 19980130]); R0479/R1830 ("The results are not tallied (eg. {Scorn of Adonis} or {Bribes} have no effect)" [LSJ 20010209]); R1965/R2157 ("Modifiers and reactions can be played during and after the referendum" [LSJ 20081202-2]); R0264/R1174 ("Each Methuselah must decide how much pool/blood to burn during the resolution... there can be some give and take", the only difference being pool vs blood); R0343/R0845 (ally "as a vampire" may call a referendum / use {Charming Lobby} [RTR 20020501]).

**Recommendation:** Keep one of each pair — R0474, R0479, R1965, R0264 — and drop the twin. For R0343/R0845 the principle is the ally "as a vampire" template, which 5.5 owns; keep at most one here as a cross-reference and let 5.5 carry it. R0264/R1174 also want a cross-reference to 2.4 (simultaneous choices with give-and-take), which is where their real content lives.

*Rulings (10):* R0474, R1829, R0479, R1830, R1965, R2157, R0264, R1174, R0343, R0845

### [medium] over-absorbed

Four {Yawp Court} rulings, all secondary, restate one principle — the referendum is only conducted if the acting minion is still ready when the action would resolve — through four different ways of removing him: not ready after combat (R2046), leaves torpor immediately via {Warsaw Station} (R2048), {Rotschreck} sends him to torpor (R2049), and end-of-combat ordering (R2050). R2049 in particular is a pure three-card interaction ("the Sabbat vampire takes 2 damage (combat ends before torpor)") that teaches nothing about referendum procedure; its content is 4.7 strike-combat-ends timing.

**Recommendation:** Keep R2046 as the single statement of the principle. Demote R2049 to C or refile under 4.7. R2050's real content is 4.9 (end-of-round vs. when-combat-would-end ordering) and it is already secondary here — fine as a cross-reference but not as 3.7.5 material. R2048 is redundant with R2046.

*Rulings (4):* R2046, R2048, R2049, R2050

### [medium] misfiled

R1690 ({Soul Stealing}.2) and R1788 ({Taking the Skin: Minion}.2) are the same template ruling filed twice: "If the minion is burned because of a referendum or as a side-effect of the action, this does not count as the acting minion burning him." The principle is about attribution of a burn — who counts as having burned a minion — and 5.4 ("who burned them; combat vs. non-combat burns; trophies/bounties on burns") owns it outright. "Referendum" appears only as one item in a list of causes; nothing here teaches referendum procedure.

**Recommendation:** Drop both from 3.7.5. They are secondary rows so the loss is contained, but they will pad the extract with material the drafter must read and discard, and they are also a duplicate pair that 5.4 should collapse to one.

*Rulings (2):* R1690, R1788

### [medium] other

Two rulings say game state relevant to a referendum is fixed when terms are chosen — R1291 ({Parity Shift}.4, "changes in pool during the referendum (after terms are chosen) do not affect the outcome") and R1480 ({Revolutionary Council}.1, "unlocked Anarchs are chosen when choosing terms. They still count if they get locked during the vote"). R0525 ({Domain Challenge}.1) says the opposite for its card: "Locked minions are counted after the referendum is completed." A drafter will not be able to state one rule from these three without an explicit distinction.

**Recommendation:** This is a genuine tension the section must resolve in prose: terms fix the *designated targets* at announcement, but an effect whose text counts a quantity at resolution counts it then. State the distinction explicitly with R1480 and R0525 as the contrasting pair, rather than letting the drafter pick whichever it read first.

*Rulings (3):* R1291, R1480, R0525

### [low] over-absorbed

Three rows are pure one-card interpretations. R0101 ({Aura of Invincibility}.2): "Goes to the ash heap when played, if it has been removed when the referendum passes, it has no effect" — this is entirely about that card's own put-into-play mechanism and fails transfer. R0100 (same card) is close behind: that a failed referendum means the card's effect does not happen is what a rulebook-fluent judge already assumes (non-obviousness). R0478 ({Delaying Tactics}.5) is a two-card interaction — "if it was played from {The Erciyes Fragments}, it is still returned into its owner's hand" — whose transferable content, retrieval ordering vs. burning, belongs to 1.11.

**Recommendation:** Demote R0101 and R0478 to C (R0478 with 1.11 as the near-miss code). R0100 is borderline; keep it only if the drafter needs a stated example that a referendum's failure aborts the card's whole effect, otherwise C.

*Rulings (3):* R0101, R0100, R0478

### [low] misfiled

R2600 (G00061|Cancel an action.3, "Can be used to cancel all action cards, including employ retainer, recruit ally and political action") mentions political actions only as one item in an enumeration; its principle is the scope of action cancellation, owned by 3.5/1.8. R0477 ({Delaying Tactics}.4) and R0570 ({Echo of Harmonies}.4) are both about what a retrieval effect can reach in the ash heap — 1.11 material — rather than about referendum procedure.

**Recommendation:** Drop R2600 from 3.7.5; 3.5 already owns it and it is a general entry that section will carry. Leave R0477 and R0570 only if 3.7.5 chooses to state the fate of the political action card during and after the referendum as a sub-topic (see R2314, which is the cleanest statement of the limbo rule); otherwise let 1.11 own all three retrieval rulings and cross-reference.

*Rulings (3):* R2600, R0477, R0570

### [low] missing-topic

The taxonomy scope line for 3.7.5 reads "automatic pass/fail", but all 12 automatic-referendum rulings in the membership concern automatic PASSING. There is no ruling anywhere in this section about a referendum that automatically fails, nor about ties or a referendum resolving with no votes cast. Likewise the basic announcement sequence — when the referendum begins relative to the action, who sets terms and in what order — is only visible indirectly through R0265 ("cannot be used before the terms are set") and R2465. The document will be thin on both.

**Recommendation:** Flag for the drafter: state the automatic-fail and tie cases from the rulebook with a ⚠ REVIEW if no ruling supports them, and open the section with the procedural skeleton (announce, set terms, cast votes and ballots, tally, apply effects) derived from the rulebook rather than expecting the extract to supply it. Check whether automatic-fail rulings were routed to 3.7.6 instead.

*Rulings (2):* R0333, R2557

## 3.7.6

### [high] duplicate-template

Six rulings on three cards (Arishat, Kateline Nadasdy, Sundown) are two verbatim wording templates repeated three times each, and each copy carries the identical reference ID, proving they are the same ruling recorded three times. Template 1 = 'ability applies to Priscus votes and ballots' [LSJ 19971001] (R2138, R2270, R2437). Template 2 = 'ability to force a vampire to abstain can cancel the votes and ballots of the vampire' [LSJ 20100311] (R2139, R2271, R2438). The three cards were split across chunks so no classifier could see the triplication.

**Recommendation:** Collapse to two rulings, one per template. Keep R2138 (Arishat) for 'a forced-abstain effect reaches the Priscus sub-referendum too' and R2139 (Arishat) for 'forcing abstention cancels votes AND ballots already cast'; drop R2270/R2437 and R2271/R2438 to C. Draft as one principle — an effect that acts on a vampire's voting acts on both its votes and its Priscus ballot — with {Arishat} as the single e.g. card.

*Rulings (6):* R2138, R2270, R2437, R2139, R2271, R2438

### [high] scope-drift

A second, unrelated topic has accreted: the pool consequences of a referendum that has already passed. These rulings say nothing about votes or ballots — they are about allocating and accounting pool loss/gain from a vote's effect. The seam is clean: R1041 ('Can allocate more points than a Methuselah has pool'), R1429/R1430 (Reckless Agitation allocation limits), R0665 ('Do not vote if the cost ousts you'), R1321 ('Gaining pool does not count as a negative loss'), R1542 (Scorn of Adonis applies retroactively to no-votes), R2550 (simultaneous ousts, victory points and the 6 pool). None of them turn on how a vote is cast, who may cast, or votes vs. ballots.

**Recommendation:** Move the PRIMARY rows out of 3.7.6: R1041, R1429, R1430 and R0665 to 6.5 (pool payment/oust timing), with R1542 to 3.7.5 (when effects may be played during the referendum). Leave R1321 and R2550 as secondary cross-references only if 6.5 already holds them as PRIMARY. 3.7.6 should cross-reference 6.5 for vote effects rather than absorb them.

*Rulings (7):* R1041, R1429, R1430, R0665, R1321, R1542, R2550

### [medium] duplicate-template

Six further verbatim pairs, each pair identical in wording AND reference IDs, each pair split across chunks so both copies were filed independently: bonus-vs-conditional votes (R1014 Leadership Vacuum / R1325 Political Struggle, both [ANK 20211009][LSJ 20040518-2]); 'Priscus ballots are not taken into account' (R1015 / R1326, both [ANK 20211009][LSJ 20041025]); 'Playable on an abstaining vampire: it does not force them to vote, but restricts their choice if they do' (R0983 Kindred Coercion / R0984 Kindred Manipulation, both [RTR 19991001][LSJ 20030828]); 'votes and ballots must be cast on the same side' (R2217 Genevieve / R2224 Gratiano, both [RBK gaining-votes][LSJ 20051113-2]); 'Can allocate more points than a Methuselah has pool' (R1041 / R1430, both [LSJ 20020819]); 'May be played before, during, or after votes and ballots have been cast' (R0474 Delaying Tactics / R1829 Telepathic Vote Counting, both [LSJ 19980130]).

**Recommendation:** Keep one of each pair and drop the twin to C: R1014, R1015, R0983, R2217, R1041 (or its 6.5 replacement), R0474. Note that R1015/R1326 are the card-level echo of the general entry R2556 (G00021 'Reduce votes': the Priscii sub-referendum is not affected) — draft R2556 as the P and cite one card as the e.g., not two.

*Rulings (12):* R1014, R1325, R1015, R1326, R0983, R0984, R2217, R2224, R1041, R1430, R0474, R1829

### [medium] over-absorbed

Three P/E rows are pure single-card text readings. R1429: 'Cannot allocate 6 points to a single Methuselah, nor any point to yourself. Cannot be played if there is only one opponent left' — this is arithmetic on {Reckless Agitation}'s own printed distribution clause; it changes no ruling on any other card (fails transfer). R1080: 'the acting vampire gains one blood if he does not abstain, as he can only vote in agreement with himself' — a tautology about {Madrigal}'s own gain clause. R1830: 'The results are not tallied (eg. {Scorn of Adonis} or {Bribes} have no effect)' — a consequence of {Telepathic Vote Counting}'s own 'the referendum is not resolved' text, and obvious to a fluent judge.

**Recommendation:** Re-role R1429, R1080 and R1830 to C with notes citing the transfer test. Keep R1079 (Madrigal.1), which does teach generally: an effect keyed to how a vampire voted reads the final disposition of the votes at tally time, not the disposition when the effect was played.

*Rulings (3):* R1429, R1080, R1830

### [low] role-error

Byte-identical ruling texts received different roles in different chunks, violating the contract's golden rule 5 ('identical rulings must get identical labels'). 'applies to Priscus votes and ballots' is E on R2138 and R2270 but P on R2437; 'can cancel the votes and ballots of the vampire' is E on R2139 but P on R2271 and R2438. Low stakes on its own (P vs E is explicitly cheap), but it is the diagnostic signal that the cross-chunk duplication above went undetected.

**Recommendation:** No churn needed if the duplicate-template collapse above is applied — the surviving copy's role is the only one that matters. Flagged as evidence, not as work.

*Rulings (8):* R2138, R2270, R2437, R2139, R2271, R2438, R0982, R0983

### [low] thin-section

The scope line claims 'bonus vs. conditional votes' as a sub-topic, but the entire evidence for it is one wording template appearing twice (R1014, R1325) plus one oblique card case (R1061, Loyalist votes 'silenced' when the bearer's votes are changed). After deduplication the drafter has a single sentence and no independent second source for what is, on the scope line, a first-class distinction. Nothing in the membership explains what makes a vote conditional rather than bonus beyond the four cards named inside R1014's own text.

**Recommendation:** Flag for the drafter: state the bonus/conditional distinction from R1014 and expect to write it thin, or check whether rulings on {Sundown}, {Aura of Invincibility} or {Eze, The Demon Prince} were classified elsewhere (5.8 titles is the likely destination) and should be pulled in as secondary before drafting.

*Rulings (3):* R1014, R1325, R1061

## 3.7.7

### [high] duplicate-template

Eight rulings are the same boilerplate from the same source ruling [ANK 20181017] — "Is not the default action, no blood is paid for the rescue / to leave torpor" — filed across eight different cards ({Healing Touch}, {Lord of Serenity}, {Rapid Healing}, {Recure of the Homeland}, {Resume the Coil}, {Root of Vitality}, {Sense Vitality}, {Warding the Beast}) in several chunks. They are one principle, not eight examples: a card that grants its own leave-torpor or rescue action supplies a distinct action, so the default action's blood cost is not paid. The style rule caps this at one principle plus 1-3 "e.g." cards.

**Recommendation:** State the principle once as P and keep at most three cards as "e.g.". Recommended keeps: R1470 {Resume the Coil} (its wording covers both the leave-torpor and rescue variants in one line, so it anchors the general statement), R1410 {Rapid Healing} (paired with R1411, which independently establishes that such a card IS a "leave torpor" action — the two together carry the whole rule), and one discipline-varied third, R0832 {Healing Touch} [OBE]. Demote R1050, R1431, R1502, R1571, R2002 to C (identical restatement of an already-carried ruling; adds no transfer beyond the card name) and let them stay in the rulings database. Also normalise the role: exactly one P, the rest E — currently six P and two E on identical text.

*Rulings (8):* R0832, R1050, R1410, R1431, R1470, R1502, R1571, R2002

### [high] misfiled

{Warsaw Station}.3 teaches nothing about leave-torpor or rescue actions. Its content is (a) a post-resolution effect applies after the action resolves and after any referendum concludes, and (b) a trait-keyed effect reads the trait at the moment of application, not at announcement ("If the acting vampire is not a Nosferatu anymore at that point, he does not unlock"). Neither is a torpor-action rule; the row is here only because the card's other rulings are.

**Recommendation:** Move to 2.3 (after-resolution modifiers / ordering of post-resolution effects) as PRIMARY, with 5.9 (trait read at application time; the later trait governs) as secondary. Remove from 3.7.7 entirely — it is not even a useful cross-reference for a drafter writing this section.

*Rulings (1):* R2005

### [medium] scope-drift

The two remaining {Warsaw Station} rows are about a card effect removing a vampire from torpor mid-action, not about the leave-torpor or rescue ACTIONS whose cost and payer this section owns. R2003's principle is "an action can succeed and still have no effect" (the diablerie target is no longer in torpor); R2004's is "the action ends and cannot be continued" when its precondition evaporates. Both are chapter-3 action-resolution rules that happen to use torpor as the trigger.

**Recommendation:** Refile R2003 with 3.4 (success vs. having an effect) PRIMARY and 3.7.8 (diablerie) secondary; refile R2004 with 3.5 (fail/end templates, action ends) PRIMARY. Either may remain in 3.7.7 as secondary, but neither should be PRIMARY here — as PRIMARY they invite the drafter to open a "leaving torpor without an action" sub-topic that the section's scope line does not claim and that has no other members.

*Rulings (2):* R2003, R2004

### [medium] duplicate-template

R2213 {Frondator} and R2353 {Miriam Benyona} are word-for-word identical ("The cost to rescue from torpor is reduced even if paid by the rescuee. This is not optional."), both labelled P, both citing [LSJ 20020304-2]. R0297 {Cavalier}.3 is the same principle stated from the other side ("Applies even if the vampire it's on is not the one paying the cost (eg. rescuing from torpor)"). Three rulings, one rule: a rescue-cost reduction attaches to the rescue, not to the payer, and is mandatory.

**Recommendation:** Keep R2213 as the single P stating the rule (it carries the extra [PIB 20110918] reference and the "not optional" clause) and R0297 as the one "e.g." showing the reduction applying when the bearer is not the payer. Demote R2353 to C — a verbatim second copy on another card adds no transfer. Note that the "not optional" half is a real second beat (a reduction cannot be declined to keep a higher cost) and should survive into the prose; do not let the deduplication drop it.

*Rulings (3):* R2213, R2353, R0297

### [medium] missing-topic

The section has no ruling stating the base rules it exists to organise. Every cost ruling here is negative ("is NOT the default action"), so nothing on record states what the default action costs, who pays it, or who may take it. Likewise the rule that blocking a vampire leaving torpor gives the blocker a diablerie opportunity appears only by implication, through three cards that negate it: R0757 {Ghoul Escort} (blocked leave-torpor produces no combat), R0324 {Change of Target} and R1171 {Mirror Walk} (blocker gets no diablerie opportunity). The affirmative rule has no owning ruling in the membership.

**Recommendation:** Flag for the drafter that 3.7.7's spine must come from the rulebook ([RBK] footnotes) rather than from rulings: the default leave-torpor and rescue action costs and payer, and the block-becomes-diablerie-opportunity rule. The three block rulings above then read correctly as exceptions to a stated rule rather than as a floating cluster. Also worth a cross-reference to 3.7.8 (diablerie) and 3.3 (blocking) rather than restating either. Sub-topics with no ruling at all and no obvious rulebook anchor — whether the vampire leaves torpor locked or unlocked, and whether another methuselah's minion may be the rescue target — will be thin or absent; do not manufacture prose for them.

*Rulings (3):* R0757, R0324, R1171

## 3.7.8

### [high] duplicate-template

Eight rulings all teach the same single point — there is a window after the diablerie resolves and before the blood hunt referendum, and effects may be played in it. Three of them are byte-for-byte identical: R0540 (Draught of the Soul.3), R1691 (Soul Stealing.3) and R1789 (Taking the Skin: Minion.3) are all '[ACTION MODIFIER] If played on a diablerie, can be played before or after getting a Discipline card (if any), but must be played before the Blood Hunt.' with the same reference [RTR 19991206]. R1498 (Ritual of the Bitter Rose.1) and R1653 (Slake the Thirst.3) are a second identical pair ('Can be played after a diablerie, before the blood hunt', both [ANK 20201228]). Under the no-exhaustive-lists rule this is one principle with at most three 'e.g.' cards, not eight entries.

**Recommendation:** Keep R0839 (Heidelberg Castle.4) as the P — it is the only row that states the underlying rule ('the Blood Hunt is part of the action although it is independent from it'). Keep exactly one of the [RTR 19991206] trio (R0540) and one of the [ANK 20201228] pair (R1498) as the 'e.g.' cards. Keep R1898 (Trophy: Diablerie.1) separately, since it adds the distinct point that the trophy can be retrieved in time to protect the vampire in that same referendum. Demote R1691, R1789, R1653 to C (redundant copy of an already-carried template) and drop R1324 (Political Struggle.2) to a cross-reference — its 'votes gained before the blood hunt referendum' is the same ordering fact seen from 3.7.6.

*Rulings (8):* R0540, R1691, R1789, R1498, R1653, R0839, R1324, R1898

### [high] misfiled

R0399 (Consignment to Duat.2), R0431 (Cryptic Mission.1) and R1753 (Succubus.2) are all filed PRIMARY in 3.7.8 but contain no diablerie and no blood hunt. All three say a directed action that burns an ally 'counts as a Ⓓ action burning an ally (eg. Trophies, {Predator's Transformation})', all three carry the same reference [ANK 20220507], and R0399/R0431 are word-for-word identical. The classifiers appear to have routed on the token 'Trophies' — but 3.7.8's scope claims only 'trophies for diablerie', while 5.4 explicitly owns 'trophies/bounties on burns' and 'combat vs. non-combat burns'. Compounding the misfile, the three are one template, so even in the right section they are one entry.

**Recommendation:** Move all three to 5.4 as PRIMARY (secondary 5.5 for the ally-life aspect), and keep only one — R0399 — as the carried instance; the other two become C as duplicate copies. Remove 3.7.8 from all three entirely: no drafter of the diablerie section can use them.

*Rulings (3):* R0399, R0431, R1753

### [medium] duplicate-template

R0008 (Abandoning the Flesh.1), R0095 (Ashes to Ashes.5) and R1445 (Reform Body.3) are the identical sentence 'Cannot be played when burned as a result of a Blood Hunt referendum', all tracing to [LSJ 20070417]. The principle is real and belongs here — the blood-hunt burn is not a burn these save-yourself effects can answer — but it is one principle, and three cards is already the ceiling with no headroom for the drafter to add a fourth if a better example exists.

**Recommendation:** State the principle once in prose and cite at most two of the three; R1445 (Reform Body.3, the only PRIMARY row and the one carrying two references) is the natural keeper alongside R0008. Demote R0095 to C as a duplicate copy. Note that R1443 (Reform Body.1) already covers the adjacent 'no blood hunt is called on an unsuccessful diablerie' point, so the two Reform Body rows should be drafted as one paragraph, not two.

*Rulings (3):* R0008, R0095, R1445

### [medium] duplicate-template

R0186 (Blood Brother Ambush.1), R0324 (Change of Target.9) and R1171 (Mirror Walk.4) are the same template three times: when a torpor-leaving action is blocked the blocker gets an opportunity to commit diablerie, and each of these cards removes that opportunity. All three are filed secondary, which is defensible as cross-reference, but the underlying rule they presuppose is stated by none of them — the section will otherwise carry three illustrations of a principle it never states.

**Recommendation:** Keep one (R0324, Change of Target.9, the clearest wording) as the 'e.g.'; the other two add nothing. More importantly, the drafter needs the positive rule — 'a blocker of a leave-torpor action may commit diablerie on the blocked vampire' — written out from 3.7.7 and cross-referenced here, since no ruling in this membership states it directly.

*Rulings (3):* R0186, R0324, R1171

### [medium] misfiled

R1897 (Trophy: Chosen.1) — 'If the recipient of the Trophy chooses to burn it, there is no other effect. He does not unlock and does not gain the four blood.' — is filed E/PRIMARY in 3.7.8 but mentions neither diablerie nor blood hunt. It is an interpretation of one card's own either/or text, listing the specific benefits (unlock, four blood) that card forgoes. It fails the transfer test: no other card is ruled differently because of it.

**Recommendation:** Reclassify as C with 5.4 as the nearest section (trophies on burns). If it is kept at all, it belongs in 5.4, not in the diablerie section — 3.7.8's trophy scope is 'trophies for diablerie', which is R1898 (Trophy: Diablerie.1), not the trophy family generally.

*Rulings (1):* R1897

### [medium] missing-topic

The section has no ruling that describes the diablerie resolution itself — what the diablerist gains and in what order. The only trace of it in the whole membership is a subordinate clause inside the duplicated action-modifier template ('before or after getting a Discipline card (if any)'), and the negative statements R1443 ('the diablerist gets nothing from the victim') and R2163 ('blood and equipment stay on him'). A drafter writing 3.7.8 from this extract can describe when the diablerie fails and what happens afterwards, but cannot state the success path: capacity gain, the discipline card, what happens to the victim's blood and equipment on success, or where the blood hunt sits relative to those steps.

**Recommendation:** Flag 3.7.8 as needing rulebook-sourced prose for the diablerie resolution sequence rather than ruling-derived prose. Also check whether rulings on the success path were absorbed elsewhere (5.1 capacity changes, 5.4 burning minions) and should carry 3.7.8 as a secondary code — this is the shape of a cross-chunk loss, not necessarily a genuine corpus gap.

*Rulings (3):* R0540, R1443, R2163

### [low] role-error

R2394 (Phillipe Rigaud.2) is PRIMARY in 3.7.8, but its content is a mandatory-action rule — 'As long as there is an opportunity for diablerie, he must attempt it, even if he did so already and unlocked' — that is, the obligation is not discharged by having performed it once. Its two companions on exactly this question, R2393 (Phillipe Rigaud.1, the not-stuck rule) and R1926 (Undying Thirst.1), are correctly filed here only as secondary with 3.9 owning them. The three should not be split across primaries.

**Recommendation:** Swap R2394's codes so 3.9 is primary and 3.7.8 secondary, matching R2393 and R1926. Note the pair R2393/R2394 is also a direct instance of 3.9's two named sub-topics (discharge, and the stuck-or-not outcome), so 3.9's drafter needs both.

*Rulings (3):* R2394, R2393, R1926

### [low] recoverable-C

R0053 (Anathema.3) — 'Diablerie does not trigger Anathema' — is E/PRIMARY but is a bare negative about one card's trigger condition. Nothing in the wording states why diablerie fails to trigger it, so it transfers to no other card and gives the drafter no principle to attach it to. Contrast R0005 (Abactor.2), which makes the same kind of negative statement but grounds it in a rule ('this is not a diablerie'), and is therefore usable.

**Recommendation:** Reclassify as C with 3.7.8 as the near-miss code. Keep R0005 and R1428 (Rebirth.1) as the carried instances of the 'X is not a diablerie action, so diablerie-keyed effects do not apply' principle — between them they already cover both {Amaranth} and {Abactor}.

*Rulings (1):* R0053

## 3.8

### [medium] misfiled

A three-ruling cluster is about playing multiple copies of a CARD on one action, not about actions PROVIDED by cards — the one real seam in the section. R0569 ({Echo of Harmonies}) and R1125 ({Mask of a Thousand Faces}) are the same wording verbatim ("Multiple copies can be played by different minions/vampires on the same action"), R1129 ({Masquerade Endangered}) is the same template with "different Methuselahs after a single action". None of these cards provides an action; the principle is a per-copy play limit scoped to the action rather than to the player. A drafter writing 3.8 would have no sentence to attach them to; a drafter writing 1.15 would.

**Recommendation:** Move all three out of 3.8 to 1.15 (cumulative & stacking / per-copy plays), with 1.2 as secondary for the periodicity wording. Note the contrast with R0480 ({Delaying Tactics}.7), which superficially resembles them but genuinely belongs in 3.8 because it concerns referendums provided by copies of a card IN PLAY — keep R0480 here.

*Rulings (3):* R0569, R1125, R1129

### [medium] duplicate-template

The core 3.8 principle — one providing source yields one action, so multiple copies yield multiple actions, and unlocking lets the same minion take each — arrives five times. R0072 ({Archon}.2) and R1831 ({Templar}.1) are character-for-character identical ("Each copy of this card provides its own action: if the vampire manage to unlock during the minion phase, he can perform the action more than once (once per copy)."), both labelled P PRIMARY, both citing [RTR 20030519]. R2570 (G00035 "Provide multiple actions") states the same rule as a general entry. R2130 ({Annazir}.2) and R2158 ({Bindusara}.1) are the converse half of the same template ("cannot perform the action provided by his ability twice in the same turn").

**Recommendation:** Keep R2570 as the prose (it is the general entry and states the rule with no card doing the work), one of R0072/R1831 as the "e.g." for the multiple-copies direction, and one of R2130/R2158 as the "e.g." for the single-source direction. The remaining two stay in the database. Do not write both {Archon} and {Templar} into the document — that is a two-card list of one ruling. Suggested keeps: R2570 + R0072 + R2158 ({Bindusara}'s "even to fetch different cards" clause is the more informative of the converse pair).

*Rulings (5):* R0072, R1831, R2570, R2130, R2158

### [low] duplicate-template

R0956 ({Jar of Skin Eaters}.3) and R0966 ({Karavalanisha Vrana}.1) are verbatim identical ("The provided action ends with no effect if the acting minion does not possess the equipment when the action resolves. It is still considered successful if not blocked."), same reference [RTR 19960221], both P secondary. One principle, two copies.

**Recommendation:** Keep one as the "e.g." for the equipment-provided-action-loses-its-source rule; drop the other. Note that both are secondary here and their principal home is 3.4 (successful but no effect) — 3.8 needs at most one of them as a cross-reference.

*Rulings (2):* R0956, R0966

### [low] misfiled

R1347 ({Powerbase: Tshwane}.4, "Can reduce the cost of an action card even if it is not played as an action (ie. a retainer played with Pack Alpha)") is about cost reduction attaching to a card rather than to the action it is played as. It is the converse subject of 3.8: a card that is NOT an action, not an action provided by a card. Its sibling R1417 ({Ravnos Carnival}.3, "cannot be used to pay for the cost of a cardless action or of an action provided by a card in play") does belong here, which is probably what dragged R1347 along.

**Recommendation:** Drop R1347 from 3.8 and let 1.7 (costs & payment) own it. R1417 alone carries the 3.8-relevant point that card-provided and cardless actions are not "action cards" for cost purposes.

*Rulings (1):* R1347

### [low] thin-section

After removing the misfiles and collapsing the duplicate templates, 3.8 has roughly ten distinct points, and one of the two sub-topics the taxonomy scope line promises is supported by a single ruling. "Contested title = no action" rests entirely on R2577 (G00042), with no card instance illustrating it and nothing on dormant or yielded titles (5.8 vocabulary, no 3.8 ruling). The section's strongest surviving material is instead the "what kind of action is a provided action" thread — R0823 ({Haqim's Law: Judgment}, inherits sect requirements), R2377 ({Pariah}, card-provided undirected hunts), R0344 ({Charming Lobby}, a political action that is not a political action card), R1433 ({Red Herring}, rulebook actions are not the same as card actions).

**Recommendation:** Draft 3.8 around the provided-action-inherits-properties thread as the spine, with multiple-copies as the second sub-topic, and treat the contested-title point as a one-line cross-reference into 5.8 rather than a heading of its own. Flag for Phase 4.5 whether the title half of the scope line is worth keeping in 3.8's title at all.

*Rulings (4):* R2577, R0823, R2377, R0344

## 3.9

### [high] other

Unresolved tension on whether a card-provided action of the required type discharges a mandatory-action obligation. R1704 (Spirit Marionette.3): 'The mandatory bleed can be performed by playing a card (eg. {Computer Hacking}).' R2525 (Elen Kamjian.2): 'Another bleed action (eg. {Flurry of Action}) does not count as the bleed action her ability forces her to take.' As written these are directly contradictory and a drafter working from this extract would state one and silently drop the other. The taxonomy scope line for 3.9 currently encodes only the Elen side ('a different effect granting the same action type does NOT satisfy a distinct obligation'), which would lose R1704 entirely.

**Recommendation:** Adjudicate before drafting 3.9. The likely reconciling distinction is that a card whose effect IS the action ({Computer Hacking} bleeds as the action taken) discharges the obligation, whereas a card granting an ADDITIONAL separate action ({Flurry of Action}) creates a second action that leaves the obligation intact. If confirmed, the section should state that rule explicitly with both cards as the contrasting pair, and the 3.9 scope line in taxonomy.md should be widened from the Elen-only phrasing. If not confirmed, one of the two rulings must be flagged !WORDING. Do not let the drafter resolve this implicitly.

*Rulings (2):* R1704, R2525

### [medium] duplicate-template

Same wording template, same underlying ruling, both labelled P PRIMARY. R0424 (Cry Wolf.2): 'If he unlocks after having performed his mandatory action, he's free to take any action.' R2524 (Elen Kamjian.1): 'If she unlocks after having performed her mandatory bleed, she is free to take any action.' Identical sentence differing only in pronoun and in naming the action type, and both cite the same reference [LSJ 20090226] (Elen adds [ANK 20211009-2]).

**Recommendation:** Keep one as the P that states the discharge principle -- prefer R0424 (Cry Wolf.2), whose wording is already generic ('his mandatory action', not 'her mandatory bleed'). Demote R2524 to the 'e.g.' slot or fold it into the same footnote, carrying its extra [ANK 20211009-2] reference. One sentence of prose, not two.

*Rulings (2):* R0424, R2524

### [medium] duplicate-template

Same wording template across two cards and two chunks, both labelled P PRIMARY. R1065 (Lunatic Eruption.1): 'The mandatory attack action must be taken before any non-mandatory actions.' R1703 (Spirit Marionette.2): 'The mandatory bleed action must be performed before any non-mandatory actions.' One ordering rule instantiated on two action types; neither adds a qualification the other lacks.

**Recommendation:** State the ordering rule once at the general level ('a mandatory action must be taken before any non-mandatory action in the minion phase') with both cards cited in a single footnote as the e.g. pair. This is within the 1-3 cards budget, so both can be named, but they must not become two separate principles.

*Rulings (2):* R1065, R1703

### [medium] missing-topic

The extract has no ruling on whether an ATTEMPTED but unsuccessful mandatory action discharges the obligation. R0323 covers the case where the action is prevented outright ('If the card prevents the acting minion from performing a mandatory action, he is stuck and cannot act'), and R1926 covers what creates a choice of obligations, but nothing here says what happens when the mandatory action is announced and then blocked, canceled, or fails to resolve. That is the intersection with 3.5 (NRA & canceled actions, already drafted) and is the first question a judge will actually be asked.

**Recommendation:** Flag to the drafter that 3.9 will be thin on this point and should cross-reference 3.5 rather than invent an answer. If a ruling on it exists in the corpus it is filed under 3.5 or 3.3 and should be pulled in as a secondary; worth a targeted grep before drafting.

*Rulings (2):* R0323, R1926

### [low] thin-section

After the two duplicate-template merges above, 3.9 reduces to roughly four distinct principles (obligation creation, ordering, discharge, stuck-and-cannot-act) across five cards, with one of those four (discharge) currently unresolved. The section is real -- it clears the multi-sub-topic bar the taxonomy set for it -- but it is at the floor.

**Recommendation:** No action on membership; the rulings here are correctly filed and none should be recovered to C. Note for Phase 4.5 that 3.9 may read better as a subsection under 3.1 or alongside 3.10 than as a standalone heading, on the same 'may not survive as its own heading' basis already recorded for 6.8. Decide at assembly, not now.

*Rulings (11):* R0323, R0424, R1065, R1067, R1122, R1703, R1704, R1926, R2524, R2525, R2526

## 4.1

### [high] duplicate-template

Three rulings are the SAME wording template on three cards, verbatim, with the same single reference [ANK 20181101]: 'Can be played by a minion of a Methuselah not involved in the current combat' ({Bliss}, {Martyr's Resilience}, {Nosferatu Putrescence}). Two are secondary, one PRIMARY — no classifier could see the other copies. This is one principle (a [COMBAT]/[REACTION] card's player need not be a party to the combat), not three examples.

**Recommendation:** Collapse to one entry. Keep R1247 ({Nosferatu Putrescence}) as the PRIMARY carrier since it is already PRIMARY, and cite at most one more as 'e.g.'; drop the third from the extract. Note also that this principle is about who may PLAY a card during combat, not about the combat script — consider whether 1.5 or 2.1 should own it and 4.1 merely cross-reference (see the related finding on R2507/R2509).

*Rulings (3):* R0174, R1108, R1247

### [high] duplicate-template

R0403 ({Coordinate Attacks}) and R0919 ({Infection}) are byte-identical rulings with the same reference [RTR 20030519]: 'Must be played after the presses are handled and can be played if the round ends prematurely.' Filed once as secondary and once as PRIMARY across different chunks.

**Recommendation:** Keep one as the 'e.g.' for the principle 'the end-of-round window falls after the press step and remains available when the round ends prematurely'. Keep R0919 (already PRIMARY); reduce R0403 to a cross-reference or drop it from the extract. The principle itself is good 4.1 script material and should be stated as prose, with the card as a single illustration.

*Rulings (2):* R0403, R0919

### [medium] misfiled

R2507 ({Watenda}) and R2509 ({White Lily}) are the same template on two cards, same reference [ANK 20221021]: 'Can only use his/her ability when he is in combat himself.' The taxonomy's 1.5 scope line names this case verbatim — 'abilities whose use requires the bearer to be *personally* a participant (eg. in combat themselves, not merely combat occurring)' — so 1.5 owns the principle, not 4.1.

**Recommendation:** Both are secondary rows here, so this is not a routing loss; but 4.1's drafter should not write this principle. Cross-reference 1.5 rather than restating. If either is to be kept in 4.1's extract at all, keep one, not both. Note these pull against R0174/R1108/R1247 (card play by a non-participant is fine; ability use by a non-participant is not) — that contrast is a real teaching point but it belongs to 1.5, which owns the ability-vs-card-play distinction.

*Rulings (2):* R2507, R2509

### [medium] misfiled

R1152 ({Mind of the Wilds}) is PRIMARY in 4.1 but teaches 'a minion prohibited from striking ends the combat' — that is strike selection (4.3) and end-of-combat (4.9), not the round script, what resets between rounds, or combat outside actions. It is the only membership row about the consequence of an inability to strike, so it has no neighbours here to be drafted alongside.

**Recommendation:** Reassign PRIMARY to 4.3 (choosing strikes) with 4.9 secondary; keep 4.1 only if a cross-reference is wanted. As it stands it is an orphan sub-topic that will produce a one-sentence stub in 4.1.

*Rulings (1):* R1152

### [low] over-absorbed

R0939 ({Internal Recursion}) is PRIMARY/E on the strength of five words — 'Is played before the combat begins.' Read as written it states only when one card is played and transfers nothing; the general point (a window exists between a successful block and the start of combat) is carried better by R0063 ({Angel of Berlin}), 'May be played after a block is successful before combat begins', which names the block that opens the window.

**Recommendation:** Keep R0063 as the illustration of the block-to-combat-start window and demote R0939 to C (fails transfer: it fixes one card's slot without identifying the window). If the drafter prefers to keep both, they are one principle with one 'e.g.', not two.

*Rulings (2):* R0939, R0063

### [low] missing-topic

4.1's scope line claims three things; 'what resets between rounds' has zero rulings in the membership. Nothing here says which effects are round-scoped and re-arm at the start of the next round, which persist for the combat, or how the round boundary is drawn. The closest rows (R1260 on range for the round, R0403/R0919 on the post-press window) touch the boundary without stating what crosses it.

**Recommendation:** Tell the drafter this sub-topic will be thin and check whether the material was routed to 4.2 (range for round vs. combat), 4.8 (presses, current round only) or 4.10 ('once per combat/round' on equipment) — all three own a per-round reset in their scope lines. If it all lives there, 4.1 should cross-reference and drop the claim from its own prose rather than manufacture a section on it.

### [low] duplicate-template

Three rulings state the same principle in different words: a combat begun outside a normal action designates who acts first — R0179 ({Blissful Agony}) 'the opponent goes first', R1821 ({Taunt the Caged Beast}) 'the prey goes first (for declaring maneuvers, strikes, presses)', R2532 ({The Guardian}) 'the opponent is the acting minion and play their combat effects first'. Not identical wording, so this is at the style limit rather than over it.

**Recommendation:** No routing change. Flagging so the drafter states this once as prose and treats the three as the 'e.g.' pool at the 1-3 cap — R1821 is the most informative (it enumerates maneuvers/strikes/presses) and R2532 adds the acting-minion consequence; R0179 is the droppable one if a third is not needed.

*Rulings (3):* R0179, R1821, R2532

## 4.10

### [high] duplicate-template

The "current damage" definition is filed three times as P PRIMARY on three different cards with word-for-word identical text and the identical single reference [RTR 19980623]: Concealed Weapon.2, Illegal Search and Seizure.1, Machine Blitz.1. These are not three rulings, they are one Rules Team Ruling recorded on the three cards that use the phrase. Three P rows will push the drafter toward stating the same principle three times or toward an exhaustive card list of every card that reads "current damage".

**Recommendation:** Keep R1071 (Machine Blitz.1) as the single P — it carries the fullest wording ("by the bearer against a generic opponent at the appropriate range"). Demote R0384 and R0883 to E, or drop them to C entirely, and cite the cards as "e.g. {Concealed Weapon}, {Illegal Search and Seizure}". Keep R0385 (Concealed Weapon.3) as the separate corollary — that strength and other in-play bonuses are excluded from the limit is a genuinely distinct rule, not a copy.

*Rulings (4):* R0384, R0883, R1071, R0385

### [high] duplicate-template

"Using the equipment's non-strike function does not force the minion to strike with it" appears three times on three cards, all citing the same ruling [LSJ 19971215]: Banshee Ironwail (burn-blood effect), Starshell Grenade Launcher (stealth reduction), Talbot's Chainsaw (enter-combat action / damage prevention). One principle, three surfaces.

**Recommendation:** State it once as prose — a weapon's non-strike function is independent of the choice of strike — and keep two "e.g." cards at most; {Talbot's Chainsaw} and {Starshell Grenade Launcher} give the widest spread (action vs. stealth). Demote the third to C. R1780 (Sword of Judgment: additional strike granted even if the weapon's own strike is unused) is the same family seen from the other direction and can serve as the contrast case rather than a fourth copy.

*Rulings (4):* R0120, R1725, R1792, R1780

### [medium] duplicate-template

"Does not burn / does not inflict damage if combat ends before the strike resolves" recurs on Dragon's Breath Rounds, Grenade and Jar of Skin Eaters, all citing the same reference set [LSJ 20001127-2] [LSJ 19981006] (two also [LSJ 20010806-1]). Three copies of one timing rule about self-burning weapon strikes.

**Recommendation:** Keep one as the stated principle — R0536 or R0798 — with "e.g." naming at most two of the three; drop the remaining copies to C. Pair it with R1665 ({Smoke Grenade} still burns if combat continues or a new combat begins) as the deliberate contrast, since that one is the only member carrying new information. Note the principle itself is shared with 4.7/4.9 and should cross-reference rather than restate the strike-combat-ends timing.

*Rulings (4):* R0536, R0798, R0958, R1665

### [medium] duplicate-template

"The minion cannot use the discipline / maneuver provided by the equipment if some effect prevents him from using the equipment (eg. {Drawing Out the Beast})" is recorded verbatim on Drum of Xipe Totec.1 and Hand of Conrad.1, both citing [RTR 20010710], and both marked P.

**Recommendation:** Keep one as P (either will do; {Hand of Conrad} is the cleaner discipline-granting case), demote the other to E or C. R2559 (G00024, optional maneuver unusable when the strike is unusable) is the general-entry statement of the neighbouring rule and should carry the prose; R1683 ({Soul Gem of Etrius} functions even though the bearer was prohibited from using equipment) is the genuine exception and is worth keeping as the one counter-example.

*Rulings (4):* R0547, R0822, R2559, R1683

### [medium] recoverable-C

R0775 (Glaser Rounds.1) is labelled P PRIMARY but is a pure restatement of one card's own timing: "Must wait until the second time a given gun is used in a given combat to play it." It affects no card other than {Glaser Rounds} and does not change how a judge would rule elsewhere — it fails the transfer test outright, and as a P it invites the drafter to build prose around a single card.

**Recommendation:** Reclassify to C with a note ("{Glaser Rounds} play-timing keyed to its own card text; fails transfer"), nearest code 4.10. If anything is salvaged, it is the per-gun counting of "a given gun is used", which belongs with the once-per-combat cluster (R2580/R2581) rather than as a standalone principle.

*Rulings (1):* R0775

### [medium] misfiled

R2024 (Weighted Walking Stick.2, "Full damage is applied if there are any counter left, even just 1") is filed 4.10 PRIMARY, but the principle it teaches is that a counter-gated effect is flat and does not scale with the counter count — which taxonomy 1.15 explicitly claims ("flat effects that do not scale with counter count"), with 1.12 owning the counter bookkeeping. As filed it reads as a one-card interpretation of the Walking Stick's token mechanism.

**Recommendation:** Move R2024's primary to 1.15 (or 1.12) with 4.10 as secondary. R2023 is already correctly secondary here and should stay that way — its point (token not burned when damage is reduced or not inflicted, contrary to prevented damage) is 1.12 counter bookkeeping plus 4.5 prevention, not weapons-in-combat.

*Rulings (2):* R2024, R2023

### [low] duplicate-template

R2580 (G00045, once per combat) and R2581 (G00046, once per round) are two general entries with the same sentence differing only in the period word: "A second copy allows a second use in the same combat/round." Both are P PRIMARY. They are one rule about copies, parameterised by periodicity.

**Recommendation:** Merge into a single prose statement covering both periods; keep both ids as footnote references on that one sentence rather than writing two near-identical paragraphs. R0001 ({.44 Magnum}: one maneuver each combat even if the bearer changes) is the correct third leg here — it is the only ruling stating that the per-combat limit tracks the weapon, not the wielder — so it should not be lost among the copies.

*Rulings (3):* R2580, R2581, R0001

### [low] missing-topic

4.10's scope line names "stolen/destroyed mid-combat", but the membership only covers destruction and contest: R0764 (weapon burned after being committed as a strike) and R0515 (unique weapon contested by {Disguised Weapon}). Nothing covers a weapon being taken control of mid-combat, and only R0001 touches what happens to a once-per-combat allowance when the bearer changes. The document will be thin exactly where its own scope line promises coverage.

**Recommendation:** Flag for the drafter: either sweep 6.2/6.3 (taking control of cards in play) for a mid-combat weapon-transfer ruling to cross-reference, or narrow 4.10's scope line to drop "stolen" and keep "destroyed/contested mid-combat", which the corpus does support. R0515 and R0764 together do state a real sub-principle worth prose — a weapon that becomes unavailable after being chosen as the strike makes that strike have no effect — so keep both; they are two directions on one rule, not duplicates.

*Rulings (3):* R0515, R0764, R0001

### [low] scope-drift

A weapon-damage-classification sub-cluster sits at the edge of 4.10 and belongs mostly to 4.4: R0970 ({Kerrie} ranged damage is weapon damage, modifiable by melee-weapon-damage effects) is PRIMARY here, while R1793, R1226 and R1074 are correctly secondary. The seam is real but shallow — it is a cross-reference boundary, not a section split.

**Recommendation:** No reclassification needed for the secondary rows. Consider whether R0970's primary should be 4.4 (it is a statement about what counts as weapon damage, which 4.4 owns) with 4.10 secondary; it pairs naturally with R0043 ({Anachronism}: weapons providing ranged strikes are ranged weapons), which is correctly 4.10 as a definitional rule. Whichever way it goes, 4.10 should cross-reference 4.4 here rather than restate damage rules.

*Rulings (4):* R0970, R1793, R1226, R1074

## 4.2

### [high] duplicate-template

22 of 56 rows (39% of the section) are one boilerplate wording carrying the identical reference pair [RTR 19970630] [ANK 20180720]: 'no other effect can be used to reset the range, but other pre-range effects can be played afterwards'. Every one is labelled P/PRIMARY, so the extract hands the drafter 22 statements of the same principle across 22 cards. This is the cross-chunk drift the review exists to catch — no classifier could see 21 copies from inside its own 145 lines, and each dutifully labelled its copy P.

**Recommendation:** Collapse to ONE principle paragraph with three 'e.g.' cards chosen to cover the three real variants the wording hides, not three arbitrary cards: (1) R1229 {Neutral Guard} — the canonical bare range-setter; (2) R0902 {Immortal Grapple} — the 'next round's range' polarity (only R0790, R0902, R1002 carry it); (3) R1723 {Squirrel Balance} or R0745 {Gang Tactics} — the 'if blocked' conditional variant (only these two). The 'Skip the determine range step' clause appears in 8 of the 22 and should be stated in the prose, not attached to a card. Demote the remaining ~19 to C or leave them in the database; they add no information beyond card identity.

*Rulings (22):* R0044, R0245, R0329, R0369, R0745, R0772, R0790, R0869, R0902, R0941, R1002, R1220, R1229, R1260, R1566, R1615, R1666, R1723, R1802, R2076, R2168, R2350

### [high] duplicate-template

A second 8-row template, all carrying [PIB 20120214]: 'If another effect also sets the range, the first to resolve has priority'. Critically, this is not a separate topic from the 22-row template above — it is the other half of the SAME principle (range-setting exclusivity, plus what happens when two setters collide). Drafted from the extract as-is, the section would state one rule twice under two headings. The rows also drift on role for byte-identical text: R1230 and R0090 are P while R1724 and R1740 are E.

**Recommendation:** Merge into the same paragraph as the exclusivity rule — one sentence: the first range-setting effect to resolve has priority; later ones cannot reset. Keep TWO 'e.g.' rows, and prefer the pair that names each other so the ordering is legible: R1230 {Neutral Guard} and R0090 {Asanbonsam Ghoul} (their texts cite each other as resolving before/after). Drop the other six. Normalise the P/E drift to P on whichever survives; do not spend adjudication time on the rest since P/E is low-stakes and they are being cut anyway.

*Rulings (8):* R0090, R0746, R0791, R0903, R1003, R1230, R1724, R1740

### [medium] duplicate-template

The five {Target Hand}/{Target Head}/{Target Leg}/{Target Retainer}/{Target Vitals} rulings are one wording under [LSJ 20080409], repeated verbatim across the five cards of a single card cycle: played during the Strike phase even if a strike was committed during Determine Range, and unplayable once the strike can no longer be chosen. All five are filed here as secondary, which is the right role — the principle is a strike-timing rule that 4.3 should own — but five copies of a card cycle is precisely the exhaustive card list the style rules forbid.

**Recommendation:** Keep ONE as the cross-reference example (R1801 {Target Head}, since R1802 already anchors that card in this section) and drop the other four. In 4.2 this should be at most a cross-reference to 4.3 noting that committing to a strike during Determine Range does not move the strike card's own play window; the substantive rule belongs to 4.3.

*Rulings (5):* R1799, R1801, R1806, R1808, R1811

### [medium] over-absorbed

A cluster of pure one-card range-effectiveness statements absorbed as P/E. R0599 {Entombment} is the entire ruling text 'Only effective at close range.'; R1514 {Rowan Ring} 'Only usable at close range.'; R1489 {Riposte} 'The damage is only dealt if the strike was resolved at close range.'; R0225 {Bollix} 'Does not protect from weapons if played at long range.'; R1332 {Potio Martyrium} 'The damage does not depend on range.' Each states only what range its own card works at. They fail BOTH C tests: no transfer (none changes how you rule on a different card) and non-obviousness (a judge fluent in the rulebook already knows hand strikes and close-range effects do not reach at long range). This is the one-card-interpretation error the contract names as the most common over-absorption.

**Recommendation:** Demote R0599, R1514, R1489 and R0225 to C. If the drafter wants the general observation at all, it is one clause — an effect tied to a strike applies only at the range at which that strike is effective — with a single 'e.g.', for which R1489 {Riposte} is the most instructive because it turns on where the strike RESOLVED rather than where it was chosen. R1332 should move to 4.4 (see the misfiled finding) rather than being kept here.

*Rulings (5):* R0599, R1514, R1489, R0225, R1332

### [medium] over-absorbed

Five rows — nearly 9% of the section — are {Sniper Rifle}. R1666 is a copy of the 22-row exclusivity template. Of the remainder, R1669 ('if a Slave locks to enter combat instead of a blocked minion, the opponent cannot use the Rifle to set the range') is a card-plus-situation interpretation that fails transfer, and R1667 ('the bearer is not committed to use it if he or she uses another effect to set the range') is close to a restatement that an optional ability is optional. Drafted as-is, a reader would take 4.2 for {Sniper Rifle} documentation rather than a section on range.

**Recommendation:** Cut to two. Keep R1670 — the ability may only be used if the weapon was equipped at the time of the block, which is a genuinely transferable rule about when a block-triggered condition is checked (and generalises past this card). Keep R1668 — a new combat queued by {Psyche!} does not restore the once-per-combat range-setting ability, which is real 4.9 interaction material and should be cross-referenced there. Demote R1669 to C; drop R1666 with the rest of the template; R1667 is C unless the drafter explicitly wants the 'optional setter is not committed' clause, in which case state it in prose without the card.

*Rulings (5):* R1666, R1667, R1668, R1669, R1670

### [medium] missing-topic

The taxonomy scope line for 4.2 claims three things: 'determine range; range-setting exclusivity; range for round vs. combat'. Exclusivity is over-covered (30 of 56 rows). The other two have essentially no ruling. Nothing in the membership establishes the baseline mechanics of the determine-range step itself — that the default is close range, who maneuvers and in what order, how competing maneuvers resolve. And 'range for round vs. combat' is only glanced at obliquely, via the three 'next round's range' template rows (R0790, R0902, R1002) and R1668's new-combat case; no ruling states the persistence rule directly. Note that optional-maneuver semantics is deliberately owned by 1.2, so part of this thinness is by design — but the round-vs-combat persistence boundary is 4.2's own and is unevidenced.

**Recommendation:** Tell the drafter these two sub-topics will have to be written from the rulebook with [RBK] citations rather than from rulings, and that the persistence rule (a set range governs the round; a new combat resets it) is supported only inferentially by R0902/R1668. Flag it as a place where ⚠ REVIEW may be warranted rather than letting the section's shape be dictated by where the rulings happen to pile up.

### [low] misfiled

R1332 {Potio Martyrium} ('The damage does not depend on range') is filed P/E PRIMARY in 4.2, but its principle is a property of the damage, not of range determination: damage that is not strike damage is inflicted irrespective of range. 4.4 owns damage properties and environmental damage. R0263 {Burst of Sunlight} teaches the same rule from the same side ('damage done to the striking minion is environmental, it is inflicted regardless of the range') and is already correctly filed here only as secondary with its primary elsewhere — which is the treatment R1332 should have had.

**Recommendation:** Move R1332's primary to 4.4, keeping 4.2 as a secondary cross-reference at most. In 4.2 the point is a one-line cross-reference — range gates strike effectiveness, not damage from non-strike sources — pointing at 4.4. R0263 needs no change; it is a correct secondary and is the better 'e.g.' of the two if the drafter wants one here.

*Rulings (2):* R1332, R0263

### [low] duplicate-template

R1282 {Outside the Hourglass} and R2016 {Weather Control} are the same wording under the same reference [ANK 20170930]: both minions may play prevention and non-prevention pre-range effects before mending, and simultaneous pre-range damage is prevented and mended together. Both are correctly filed as secondary, so the cost is small, but the drafter receives the rule twice.

**Recommendation:** Keep R1282 {Outside the Hourglass} as the single 'e.g.' and drop R2016. The rule is primarily prevention/damage material (4.5/4.4); in 4.2 it should appear only as the observation that the pre-range window admits damage and prevention plays, cross-referenced onward rather than restated.

*Rulings (2):* R1282, R2016

## 4.3

### [high] duplicate-template

The [RTR 19960112] boilerplate "Must be played before strike resolution and damage prevention in order to affect the current strike (can be played after both strikes have been chosen)" recurs verbatim on seven cards (Blood Agony, Body Arsenal, Bone Spur, Chiropteran Marauder, Claws of the Dead, Spirit Claws, Wolf Claws) across multiple chunks, and the same rule is stated card-independently by the general entry G00050|Improve weapon before resolution.1 ("'Before resolution' means after strikes have been declared but before they resolve") and again by Backstab.1. Nine rulings, one principle.

**Recommendation:** Draft the principle from R2585 (the general entry, P) and cite at most two "e.g." cards — suggest R0185 {Blood Agony} (strength modifier) and R2036 {Wolf Claws} (damage modifier) to show both polarities. Downgrade R0220, R0235, R0349, R0359, R1700 to C (identical wording, no incremental content). Keep R0107 {Backstab} only if the drafter wants a non-[dis]-modifier instance; otherwise C.

*Rulings (9):* R0185, R0220, R0235, R0349, R0359, R1700, R2036, R2585, R0107

### [high] duplicate-template

Five verbatim copies of the [LSJ 20080409] "Target X" boilerplate — "Is played during the Strike phase even if you commit to a strike in the Determine Range phase (eg. {Thrown Gate}). Cannot be played if the strike cannot be chosen anymore during the Strike phase (eg. {Immortal Grapple})" — on Target Hand, Target Head, Target Leg, Target Retainer and Target Vitals. All five are PRIMARY E; this is exactly the exhaustive card list the style rules forbid.

**Recommendation:** Keep ONE as the example — R1811 {Target Vitals} (the most commonly seen) — and state the principle in prose: strike-modifier cards are played in the Strike phase even when the strike was committed during Determine Range, and cannot be played once the strike is no longer choosable. Mark R1799, R1801, R1806, R1808 as C (duplicate of R1811).

*Rulings (5):* R1799, R1801, R1806, R1808, R1811

### [high] duplicate-template

Two mirror-image templates state one principle: a maneuver provided by a strike card is unavailable when the minion cannot strike. [LSJ 20001126] "The opponent cannot play or use the maneuver from a strike (eg. {.44 Magnum}, {Thrown Gate}), since they cannot strike" appears verbatim on Fast Reaction.3, Hidden Lurker.5 and Lapse.1; [LSJ 20021028] "The optional maneuver cannot be used if the strike cannot be used (eg. {Hidden Lurker})" appears on Deer Rifle.4, Tinglestripe.1 and the general entry G00024|Weapon with optional maneuver.1. Six rulings, one rule, split across two wordings so no chunk could see the collapse.

**Recommendation:** Write one principle from R2559 (the general entry, P), with {Hidden Lurker} (R0853) as the prohibition-side "e.g." and one weapon (R0468 {Deer Rifle} or R1865 {Tinglestripe}) as the maneuver-side "e.g.". C the remaining three.

*Rulings (6):* R0655, R0853, R1004, R0468, R1865, R2559

### [medium] duplicate-template

Blood Fury and Soul Burn carry literally identical ruling text under identical references: R0193/R1677 are both "A weapon strike done with first strike is unaffected (unless Soul Burn is used with first strike too)" [LSJ 20040928], and R0194/R1679 are both "Only nullify the weapon damage when it resolves..." [ANK 20170519]. Two rulings' worth of content occupying four PRIMARY E slots.

**Recommendation:** Keep R1677 and R1679 ({Soul Burn}, the card the text actually names) as the examples; C the {Blood Fury} copies R0193 and R0194 as same-effect duplicates.

*Rulings (4):* R0193, R1677, R0194, R1679

### [medium] duplicate-template

"You cannot play another strike card to serve as the hand strike for X" [LSJ 20010627] appears identically on Lucky Blow.3 and Scorpion's Touch.2; Bundi.4 (R0261) is the same question answered with the useful nuance ("strike: make a hand strike" cannot be nested, but "strike: make a weapon strike" can, and the result is still a hand strike).

**Recommendation:** Draft the principle from R0261 {Bundi} — it is the only one of the three that carries the distinction — and keep at most one of R1064/R1547 as a second "e.g.". C the other.

*Rulings (3):* R1064, R1547, R0261

### [medium] duplicate-template

"If used to cancel a strike, another strike is chosen" recurs on Death Seeker.1 and Asguresh.1 (both [LSJ 20100206]); Supernatural Resistance.1 states the same rule with the added fact that the same strike may be chosen again. All three are secondary here (primary presumably 1.8), so this is a cross-reference block, not section content.

**Recommendation:** Carry only R1773 {Supernatural Resistance} into 4.3 as the "e.g." for the cancel-a-strike → re-choose rule (it is strictly the most informative), cross-reference 1.8 for the cancellation mechanics, and drop R0459 and R2142 from this extract.

*Rulings (3):* R0459, R2142, R1773

### [medium] duplicate-template

"Can be played on a strike that does no damage, even a dodge or a combat ends, but has no effect in that case" is verbatim on Target Head.5 and Target Vitals.4 [RTR 19960221]; Lucky Blow.1 states the same [RTR 19960221] rule generically ("Adding damage to strikes which are not damage dealing strikes will not deal damage"). Related: R0291 {Catatonic Fear} and R1059 {Loving Agony} are a second verbatim pair ("Is a damage dealing strike and can be modified by effects like {Target Vitals} or {Dam the Heart's River}").

**Recommendation:** State once, from R1062, that damage add-ons attach to any strike but only bite on damage-dealing strikes; keep R1814 as the "e.g." and C R1805. For the converse pair keep R0291 {Catatonic Fear} and C R1059. Consider whether the damage-add-on rule is 4.4's to state, with 4.3 cross-referencing.

*Rulings (3):* R1805, R1814, R1062

### [medium] over-absorbed

Three PRIMARY rows are bare one-card text classifications that transfer nowhere. Veiled Sight.2 is the complete sentence "[CHI] The strike is not ranged." and Compress.2 is "[thn], [THN] Not a hand strike." — each states one card's strike type and changes how you rule on no other card. Veiled Sight.1 ("the strike can be used on a minion with no blood") is not a strike rule at all: it is the steal-template principle the taxonomy explicitly assigns to 1.7 ("effects naming an amount the target may not hold").

**Recommendation:** Recode R1964 and R0381 as C (pure card-text classification; nearest 4.3). Move R1963 to 1.7 as its primary, or C it — it does not belong in the strikes section.

*Rulings (3):* R1964, R0381, R1963

### [medium] missing-topic

4.3's scope line claims "first strike" and "additional strikes", but no ruling in the membership states either rule. First strike appears only as a modifier inside other cards' rulings (R0193, R1546, R1751, R2059) and additional strikes only as timing/mandatoriness edge cases (R0844, R1456, R1487, R1780, R2066, R2564). Nothing covers the ordering of multiple first strikes, whether a first strike may itself be answered, how many additional strikes a minion may take, or the ordering of several additional strikes. Nothing covers the default strike either.

**Recommendation:** The drafter will have to write the first-strike and additional-strike core rules from the rulebook with no ruling support, or cross-reference. Flag both sub-topics for a Phase 4 rulebook-sourced paragraph rather than expecting the extract to carry them.

### [low] duplicate-template

Four further two-to-three card pairs of one template each: (a) R0955 {Jar of Skin Eaters} / R1792 {Talbot's Chainsaw}, both [LSJ 19971215] "using the action does not force the minion to strike with it"; (b) R0844 {Hell-for-Leather} / R1402 {Quickness}, verbatim "A limited additional strike can be played before or after" [LSJ 20001206] [ANK 20211124]; (c) R0167 {Blessed Blade} / R1366 {Projectile}, verbatim-parallel "a minion who maneuvers with a weapon may still use X to strike with that weapon as his initial strike" [LSJ 20050304]; (d) R1456 {Renegade Garou}, R2304 {Lorrie Dunsirn}, R0558 {Dust Up}, all "the additional strike is mandatory / not optional".

**Recommendation:** Keep one card per template: R0955, R1402, R1366, and R1456 (or R2304, which adds the press). C or drop the rest from the extract — each pair is one sentence of prose plus one "e.g.".

*Rulings (9):* R0955, R1792, R0844, R1402, R0167, R1366, R1456, R2304, R0558

### [low] misfiled

Escaped Mental Patient.4 ("If his strike resolves, he cannot be saved from burning with eg. {Heaven's Gate} or {Left for Dead}") and .2 ("'If he does so' only applies if his own effect is used directly") are secondary rows whose content is the reading of one card's self-burn clause, not a strike rule. .3 (R0608) does carry a real strike-resolution fact and should stay.

**Recommendation:** Low priority since both are secondary and their primary code carries them, but drop R0609 and R0607 from 4.3's extract so the drafter is not tempted to build a strike-resolution paragraph out of one ally's burn trigger.

*Rulings (2):* R0609, R0607

## 4.4

### [high] duplicate-template

49 rulings are one principle. 44 carry the byte-identical sentence "Additional damage inherits all of the properties of the base damage. [TOM 19960225]" and 5 more carry its narrower restatement "The additional damage is the same type as the strike's damage. [RTR 19970630]" — the same rule seen from the aggravated/type angle. Every one cites the same one or two references; not one adds a card-specific twist. This is a single sentence of prose plus an "e.g.", but it is 32% of the section's membership and will drown the drafter.

**Recommendation:** Collapse to one principle statement citing [TOM 19960225] + [RTR 19970630], with three e.g. cards chosen to span the templates: R0913 {Increased Strength} (generic +N damage aim), R1812 {Target Vitals} (aggravated-inheritance case, and the card every other ruling in the section uses as its probe), R0776 {Glaser Rounds} (equipment/weapon-damage case). Keep R1745 {Strike at the True Flesh} only if the drafter wants a fourth; the remaining ~45 stay in the rulings database. Note the P/E split within this identical set is arbitrary (28 P vs 16 E) — see the role-error finding.

*Rulings (49):* R0166, R0172, R0183, R0190, R0202, R0208, R0223, R0257, R0294, R0327, R0330, R0360, R0380, R0440, R0457, R0461, R0557, R0723, R0776, R0807, R0831, R0944, R0976, R1000, R1013, R1055, R1063, R1104, R1132, R1148, R1217, R1333, R1397, R1538, R1544, R1655, R1730, R1784, R1785, R1795, R1907, R1916, R1970, R2026, R0443, R0913, R1745, R1803, R1812

### [high] duplicate-template

28 rulings assert nothing but "this card's damage is environmental", almost all citing [RTR 19970630] or [LSJ 19970801]. They fall into three wording templates that recur across cards: bare "Damage is environmental" (R0130, R0139, R0175, R0393, R0415, R1398, R1859, R2014, R2045, R2431 …), "Damage done to the bearer is environmental" on backfiring equipment (R0154 {Black Gloves}, R0227 {Bomb}, R0797 {Grenade}, R2028 {White Phosphorus Grenade}, R2058 {Zip Gun}), and "Damage done to the striking minion is environmental" on defensive reactions (R0222 {Body of Sun}, R0244 {Breath of the Dragon}, R0263 {Burst of Sunlight}, R1334 {Pounce}). None teaches anything the template does not already teach.

**Recommendation:** State the template rule once — damage from a card effect or ability that is not a minion's strike is environmental, whoever it lands on — and cite the general entries as the prose backbone: R2552 (G00017 Environmental damage) for its properties and R2551 (G00016 Retainer doing damage) for the retainer case. Give three e.g. spanning the distinct sources: R0797 {Grenade} (equipment backfire), R0263 {Burst of Sunlight} (defensive reaction against the striker), R2428 {Shemti} (vampire ability). Keep the contrast trio R0287 {Catatonic Fear}, R1056 {Loving Agony}, R1281 {Outside the Hourglass} — "done by the vampire, NOT environmental" — as the counter-example, since that boundary is the only non-obvious part. Drop the rest.

*Rulings (28):* R0130, R0139, R0154, R0175, R0196, R0222, R0227, R0239, R0244, R0263, R0272, R0393, R0415, R0541, R0797, R0992, R1334, R1398, R1859, R2014, R2045, R2058, R2095, R2385, R2412, R2428, R2431, R2551

### [medium] duplicate-template

A second environmental template recurs independently across five cards and was labelled PRIMARY P/E every time: an effect that counts or keys off "damage inflicted" by a minion does not count environmental damage — R0197 {Blood of Acid}, R0509 {Disarm}, R1391 {Pulled Fangs}, R1476 {Revelation of Wrath}, R1885 {Transfusion}. R1219 {Necrosis} ("the environmental damage is not strike damage, {Target Vitals} does not add to it") and R1223 {Nephandus} ("damage reduction does not apply to environmental damage") are the same rule stated from the modifier and reduction side.

**Recommendation:** One principle — environmental damage is not inflicted by any minion and is invisible to effects that add to, count, or reduce a minion's damage — with two e.g.: R1391 {Pulled Fangs} (which usefully covers retainer damage in the same breath) and R1219 {Necrosis} (the {Target Vitals} probe). Cross-reference 4.5 for R1223 rather than restating. The other four stay in the database.

*Rulings (7):* R0197, R0509, R1391, R1476, R1885, R1219, R1223

### [medium] misfiled

R0441 {Dam the Heart's River}.1 — "The opponent is the one affected by frenzy (eg. for {Blade of Enoch})" — is filed PRIMARY E in 4.4 but says nothing about damage. It resolves who the card's frenzy clause targets; the word "damage" does not appear.

**Recommendation:** Remove from 4.4. It is a pure one-card reading of a second clause on the card (fails transfer — no other card has this wording), so C is the right verdict; if it is kept at all, 5.3 (torpor/frenzy states) is nearer than 4.4. The card's other four rulings (R0442-R0445) are correctly here.

*Rulings (1):* R0441

### [medium] over-absorbed

Four PRIMARY P/E rows are one-card text readings that teach nothing transferable. R0895 {Ilomba}.1 — "His effect applies to each point of damage (eg. if 3 damage is done to him, the minion it is on burns 3)" — reads Ilomba's own per-damage trigger. R1613 {Shadow of the Wolf}.1 — "The +1 damage only applies to the additional strike" — reads which of that card's two clauses the bonus attaches to. R1782 {Sword of Nuln}.2 — "Aggravated damage are not healed by default, so they are not doubled" — applies the known aggravated rule to one card's doubling clause (fails non-obviousness). R2348 {Merrill Molitor}.1 — "The damage he treats as normal is handled before any aggravated damage being treated as aggravated" — orders one vampire's own special text against itself.

**Recommendation:** Reclassify all four as C with 4.4 as the near-miss code. If any is retained, R0895 is the only defensible one and belongs in 1.15 (per-point triggers scaling with the amount), not 4.4. Note R2349 {Merrill Molitor}.2 is a genuine member — it is the inherits-properties template again — so the card is not wholly excluded.

*Rulings (4):* R0895, R1613, R1782, R2348

### [medium] over-absorbed

Five rulings from the single card {Nephandus} sit in 4.4, four of them PRIMARY, and three of them are about damage REDUCTION, which 4.5 (prevention & immunity) owns: R1224 "applies to unpreventable damage", R1225 "additional damage provided by Aim cards is not reduced separately", R1226 "damage done by a weapon is reduced if wielded by the opposing minion". One card supplying five P/E rows to a section is the shape of over-absorption even when each row is individually defensible.

**Recommendation:** Keep R1222 and R1223 in 4.4 — they are the strike-damage-vs-environmental boundary and genuinely belong to the damage-classification topic this section owns. Move R1224, R1225, R1226 to 4.5 as PRIMARY (they are already secondary-shaped material about what reduction reaches), and cross-reference rather than repeat, per the style rule.

*Rulings (5):* R1225, R1226, R1224, R1222, R1223

### [low] duplicate-template

Four rulings state the same rule — adding damage to a strike that does not deal damage produces no damage: R0442 {Dam the Heart's River}, R1062 {Lucky Blow}, R1513 {Rowan Ring} ("Adding damage to the Ring strike will not deal damage"), and R1278 {Oubliette} ("Does not inflict damage, eg. does not benefit from {Target Vitals}"). R0442 and R1062 are word-for-word identical with the same reference [RTR 19960221].

**Recommendation:** One sentence, one e.g. Keep R0442 {Dam the Heart's River} as the P (it is also the card the rest of the section uses as its probe) plus R1278 {Oubliette} as the e.g. on the receiving-strike side. Drop R1062 and R1513.

*Rulings (4):* R0442, R1062, R1513, R1278

### [low] role-error

Byte-identical ruling texts received different roles in different chunks, which is the cross-chunk drift golden rule 5 exists to prevent. "Additional damage inherits all of the properties of the base damage." is P 28 times and E 16 times (e.g. R0166 P vs R0440 E). "Damage is environmental. [RTR 19970630]" is P on R0130/R0139/R0393 and E on R0175/R0196/R1398. Flagging for the record only — P vs E is explicitly low-stakes and both land in the same extract.

**Recommendation:** No reclassification needed. Mentioned because it is corroborating evidence for the two duplicate-template findings above: it confirms the copies were labelled in isolation with no awareness of each other, so the drafter should treat the whole set as one item rather than assuming the P-labelled ones were selected.

*Rulings (6):* R0166, R0440, R0130, R0175, R0393, R0196

### [low] thin-section

Two of 4.4's scope-line sub-topics are thin. "Strength set vs. bonus" rests on two cards only — R0605 {Erosion} and R1874/R1875 {Torn Signpost}, plus R0385 {Concealed Weapon} as a secondary — though those rulings are strong and mutually consistent (a set overwrites the base, later sets win, +X adds to the new base). More notably, nothing in the membership states how damage is APPLIED once inflicted: no ruling covers blood loss vs. life loss, the torpor/burn threshold, or what happens to damage in excess of what the minion can take. The nearest are R2164 {Byzar}.2 and R0054 {Anathema}.4, which both assume excess-damage-is-lost without stating it.

**Recommendation:** Expect the section to be short on strength-setting; the three {Erosion}/{Torn Signpost} rulings state the rule completely and no further material exists in the corpus. For damage application, the drafter will have to cite the rulebook directly rather than a ruling — flag [RBK] sourcing for that paragraph, or accept a cross-reference to 5.3/5.5 and 4.5 rather than a thin standalone paragraph.

*Rulings (4):* R0605, R1874, R1875, R0385

## 4.5

### [high] duplicate-template

39 of the 92 rows (42% of the section) are three boilerplate sentences, each repeated verbatim across many cards and every copy carrying the same single reference. Template A, 'Cannot be used if there is no damage to prevent' [LSJ 20001114], appears 17 times (R0082, R0579, R0774, R0833, R0856, R0917, R1109, R1452, R1462, R1500, R1634, R1646, R1647, R1671, R1736, R1913, R1928). Template B, 'Prevents up to X damage, it can be used to prevent less' [RTR 20041202], appears 14 times (R0066, R0078, R0081, R0207, R0715, R0855, R0971, R1110, R1237, R1447, R1463, R1672, R1749, R1914). Template C, 'Unused prevention does not carry over' [LSJ 20001114], appears 8 times (R0083, R1111, R1449, R1464, R1648, R1673, R1735, R1915). These are one ruling each, recorded once per card that bears the wording template — not 39 examples. Left as-is the extract will read to a drafter as if the 'prevent up to X' rule needs fourteen citations.

**Recommendation:** Collapse to three prose sentences with one shared exemplar card. {Armor of Vitality} (R0081/R0082/R0083), {Resilience} (R1462/R1463/R1464), {Soak} (R1671/R1672/R1673) and {Undead Persistence} (R1913/R1914/R1915) each carry all three templates in one card, so a single 'e.g.' serves all three sentences. Keep {Soak} (R1671, R1672, R1673) as the primary e.g.; add {Hidden Strength} R0855/R0856 as the second, since its X+1 wording is the one non-trivial variant ('X can be higher than strictly needed', 'X cannot be negative'), and {Kevlar Vest} R0971 as the third, being the only conditional-scope variant ('from gun strikes'). Demote the remaining ~33 copies to C. Note for the drafter: no G000xx general-rule entry exists for any of the three, unlike the immune/aggravated rules, so the prose must be synthesized from the card copies.

*Rulings (39):* R0082, R0579, R0774, R0833, R0856, R0917, R1109, R1452, R1462, R1500, R1634, R1646, R1647, R1671, R1736, R1913, R1928, R0066, R0078, R0081, R0207, R0715, R0855, R0971, R1110, R1237, R1447, R1463, R1672, R1749, R1914, R0083, R1111, R1449, R1464, R1648, R1673, R1735, R1915

### [medium] duplicate-template

Two templates that DO have general-rule entries are nevertheless carried three to four times each in card copies. 'Immune means damage is not inflicted, even if non-preventable or outside combat' is R2561 (G00026|Immune to damage, correctly P) plus identical copies on {Bloodform} R0216, {Ignore the Searing Flames} R0881 and {Helena} R2233 — all four labelled P, so four rows all claim to state the same principle. 'Cannot be used to prevent aggravated damage, even if the minion treats them as normal damage' is R2568 (G00033|Prevent non-aggravated, P) plus {Flesh of Marble} R0687 and {Resilience} R1465. Per the contract's general-rule-entry rule the general entry is P and the card copies are E, which is not what happened.

**Recommendation:** Keep R2561 as the prose source for immunity and demote R0216/R0881/R2233 to a single 'e.g.' (R0216 {Bloodform} reads most cleanly), the other two to C. Keep R2568 as the prose source for the aggravated restriction with R0687 {Flesh of Marble} as its 'e.g.' — R0687 is worth keeping over R1465 because it pairs with R0688, which adds the genuinely separate rule that the preventing vampire chooses which damage goes unprevented. Drop R1465.

*Rulings (7):* R0216, R0881, R2233, R2561, R0687, R1465, R2568

### [medium] over-absorbed

Four rulings are P/E in 4.5 but are pure one-card text interpretations that fail the transfer test. R2174 {Carolina Vález}: 'She is immune to unlock damage from allies like {Abyssal Hunter} and {Wendell Delburton}' — names her, names the two allies, changes no ruling on any other card. R2175 {Chaundice}: 'Can use her ability to prevent 4 damage on a single strike' — the general point (a per-round prevention allotment may be spent on one strike, or split) is already carried by R0067, R0079 and R0972; this row adds only her number. R0012 {Ablative Skin}: 'Cannot be used to prevent damage that cannot be prevented by cards that require Fortitude' — a bridging clause about how Ablative Skin's own non-discipline text is read against Fortitude restrictions. R0270 {Call the Wild Hunt}: 'Does not render immune to a previously-played Frenzy card' — a single-card interaction with one other card.

**Recommendation:** Relabel all four C with 4.5 as the near-miss code. R2175 in particular is the clearest case: it is the same principle as R0067/R0079/R0972 restated with a card-specific quantity, so it is both over-absorbed and a duplicate.

*Rulings (4):* R2174, R2175, R0012, R0270

### [medium] misfiled

Three rows are PRIMARY in 4.5 but teach another section's principle. R0176 {Blissful Agony}.2 — 'Damage is inflicted even against a dodge. A strike: combat ends ends combat before damage is applied, as will a combatant going to torpor during first strike' — this is dodge scope (4.6) and Strike: Combat Ends timing (4.7); prevention is not mentioned at all. R1108 {Martyr's Resilience}.2 — 'Can be played by a minion of a Methuselah not involved in the current combat' — this is who may play a combat card (4.1), a fact about combat participation, not about prevention; note the taxonomy's 1.5 scope line explicitly claims the mirror-image rule. R1504 {Rötschreck}.2 — 'Can only be played after declaration of a strike, before resolution. It can be played before or after the opponent's strike is announced' — a pure play-window rule for a strike-modifying card (4.3, or 2.1); its sibling R1506, which IS about damage effectiveness, is correctly filed here only as secondary.

**Recommendation:** Repoint R0176 PRIMARY to 4.6 with 4.7 secondary; R1108 PRIMARY to 4.1; R1504 PRIMARY to 4.3. All three may keep 4.5 as a secondary cross-reference. R0413 {The Coven}.1 (locking a location during damage resolution vs. while healing or preventing destruction) is the same shape but arrives as secondary, so I would leave it — it does fix the boundary of the damage-resolution window, which 4.5 needs.

*Rulings (3):* R0176, R1108, R1504

### [medium] duplicate-template

The 'wounded' sub-topic that 4.5's scope line claims is a single ruling text, [LSJ 20090622-2], recorded four times: {Coma} R0374, {Rowan Ring} R1516, {Rabbat, The Sewer Goddess} R2403, {Seren Sukardi} R2425. Every copy says the same thing — the opponent is wounded, and if they play {Undying Tenacity} they go to torpor after combat. Three of the four are labelled P, so the extract presents four independent-looking statements of one rule.

**Recommendation:** Keep one — R1516 {Rowan Ring} reads best because it states the antecedent ('If the strike is inflicted') that the others assume — plus at most one more, and demote the rest to C. Warn the drafter that this sub-topic has exactly one source ruling behind it: the section can state the wounded/Undying Tenacity rule but has no material to develop it, and may be better handled as a cross-reference to 5.3 torpor.

*Rulings (4):* R0374, R1516, R2403, R2425

### [low] duplicate-template

Five smaller template clusters, each one rule recorded on several cards. (a) Block-induced-combat prevention: {Beast Meld} R0134 and {Precognition} R1348+R1349 are the same two LSJ rulings [20010813] [20010819-2] split across two cards — R0134 states both halves in one row, R1348/R1349 state them separately; R1350 adds the genuinely distinct re-block rule. (b) Pre-range mending: {Outside the Hourglass} R1282 and {Weather Control} R2016 are word-for-word the same [ANK 20170930] ruling. (c) Range-effectiveness of prevention: {Bollix} R0225, {Rötschreck} R1506 and {Rowan Ring} R1514 all say a prevention/protection effect does not apply where the damage is not effective at the current range. (d) Splitting a prevention allotment across strikes in a round: {Apparition} R0067, {Armor of Caine's Fury} R0079, {Kevlar Vest} R0972 (plus over-absorbed R2175). (e) Self-inflicted weapon damage not covered by a protection effect: {Blood Fury} R0191, {Blood Rage} R0204, {Soul Burn} R1678, all [LSJ 19980216].

**Recommendation:** Keep R0134 (states both halves) plus R1350 for the re-block rule and demote R1348/R1349 to C; keep R1282 and drop R2016; keep R1506 and R1514 and drop R0225; keep R0079 (cleanest statement: '2 damage per round, from any strike') plus R0972 as the gun-specific variant and demote R0067; keep one of R0191/R0204/R1678 — R0191 {Blood Fury} — and demote the other two. Cluster (e) is at the style-rule cap of three already, so it is the least urgent.

*Rulings (15):* R0134, R1348, R1349, R1350, R1282, R2016, R0225, R1506, R1514, R0067, R0079, R0972, R0191, R0204, R1678

### [low] role-error

Identical template text received different roles in different chunks, which is the cross-chunk drift signature the contract's golden rule 5 targets. 'Cannot be used if there is no damage to prevent' is P on R0917, R1452, R1462, R1500 but E on R0082, R0579, R0774 and ten others — 4 P against 13 E for one sentence. Separately, R0905 {Improvised Flamethrower} is labelled P PRIMARY but states a Flamethrower-specific self-burn trigger ('the Flamethrower will burn and inflict damage'); the transferable content it carries is the prevented-is-still-inflicted contrast, which is E material at most.

**Recommendation:** Low priority, and P vs E is explicitly low-stakes, so do not churn the whole set — but if the templates are collapsed per the first finding the surviving exemplar should be P for the prose sentence and E for the card copy, which resolves this automatically. Demote R0905 to E. Note that R0905 and R2023 {Weighted Walking Stick} ('if the damage is reduced or not inflicted, the corresponding token is not burned, contrary to prevented damage') together carry a real principle the section needs — prevented damage was still inflicted, whereas immune/reduced damage was not — so keep both under the immunity prose rather than under prevention.

*Rulings (8):* R0917, R1452, R1462, R1500, R0082, R0579, R0774, R0905

### [low] missing-topic

Two sub-topics the scope line claims are thin. First, 'unpreventable': nothing here explains what makes damage unpreventable or how the wording operates — R1514 {Rowan Ring} asserts prevention cannot be used against it, R1224 {Nephandus} says reduction still applies to it, and R2561 says immunity still beats it, but no ruling states the rule itself. Second, the exception to the 17-copy 'no damage to prevent' template rests on exactly two rulings: R0065 {Apparition} ('can be played at any time in combat, even if there is no damage to prevent yet') and R0248 {Brother's Blood} ('can be played even if there is no damage yet'). The drafter must state a rule and its exception where the exception has two instances and the rule has seventeen — that asymmetry is an artifact of the recording convention, not of the corpus, and if the templates are collapsed first the two sides become comparably weighted.

**Recommendation:** Flag to the drafter that 'unpreventable' must be defined from the rulebook rather than from these rulings, and that the lingering-vs-instantaneous prevention distinction (R0065, R0200 {Blood of Acid}, R1905 {Tunnel Runner}) is the axis that actually explains the exception — R0200 and R1905 are the same [ANK 20200517-2] ruling reaching opposite outcomes on timing, and are the most valuable pair in the section. Keep both.

*Rulings (4):* R1224, R1514, R0065, R0248

## 4.6

### [high] duplicate-template

Twelve rows are two verbatim boilerplate sentences stating the same single principle — a strike whose damage is not delivered by the strike itself is unaffected by a dodge. Eight are byte-identical ("Does not prevent the opponent from dodging, the dodge just has no effect." [LSJ 20030902-2] [LSJ 20060808-1]) and four are byte-identical ("Damage is inflicted even against a dodge. A 'strike: combat ends' ends combat before damage is applied, as will a combatant going to torpor during first strike." [RTR 19941109]...[ANK 20200422]), the fourth being the general entry G00017|Environmental damage. Spread across many chunks, no classifier could see the pile.

**Recommendation:** Write one principle. Cite R2552 (G00017|Environmental damage.1) as the rule statement — it is the general entry and needs no card. Keep at most two "e.g." cards: R0372 {Collapse the Arches} for the eight-copy wording and R0394 {Conscripted Statue} for the four-copy wording. The remaining nine (R0559, R0564, R0658, R1368, R1545, R1612, R1971, R0451, R1860) stay in the rulings database; they add no new fact.

*Rulings (12):* R0372, R0559, R0564, R0658, R1368, R1545, R1612, R1971, R2552, R0394, R0451, R1860

### [high] duplicate-template

Ten rows all state 4.6's core principle — a dodge negates the whole strike including its supplementary effects — on ten different cards. Three of them (R0290 {Catatonic Fear} "If the strike is dodged, no damage is done", R1058 {Loving Agony}, R1490 {Riposte}, all citing [LSJ 19980526] [RTR 20041202]) additionally fail the non-obviousness test: that a dodged strike inflicts no damage is base rulebook, not a ruling.

**Recommendation:** State the principle once, then "e.g." no more than three. Best three because each shows a different kind of supplementary effect: R1576 {Serpent's Numbing Kiss} (card placement plus lock), R0177 {Blissful Agony} (a queued new combat), and R0682 {Flash Grenade} — which is the most valuable because it marks the boundary: the lock effect is dodged but the card still burns. Drop R1193, R2073, R1515, R1277 as redundant, and drop R0290, R1058, R1490 as restatements of the rulebook.

*Rulings (10):* R1193, R1576, R2073, R0682, R1515, R0177, R1277, R0290, R1058, R1490

### [medium] duplicate-template

Four rows are one sentence verbatim on four cards: "If the opponent dodges this strike, his weapons are unaffected and do damage this round." [LSJ 20040928] — {Blood Fury}, {Blood Rage}, {Personal Scourge}, {Soul Burn}. One wording template (a strike that disables the opponent's weapons), four labels where one plus an "e.g." would do.

**Recommendation:** Fold into the supplementary-effects principle as a single named case with one example, R0192 {Blood Fury}. Drop R0203, R1308, R1676.

*Rulings (4):* R0192, R0203, R1308, R1676

### [medium] duplicate-template

R0236 {Bonecraft} and R0690 {Fleshcraft} are the identical sentence with the identical reference: "The rest of the effect applies if the damage is prevented, it does not if it is dodged." [LSJ 19990106-2]. This is the most valuable pair in the section — it is the prevention-vs-dodge distinction, which is 4.6's sharpest boundary against 4.5 — but it is one ruling recorded twice.

**Recommendation:** Keep as a stated principle (prevention stops the damage, a dodge stops the strike) with one example, R0690 {Fleshcraft}, and a cross-reference to 4.5 rather than a repeat. Drop R0236.

*Rulings (2):* R0236, R0690

### [medium] other

The extract hands the drafter two statements about environmental damage and dodges that read as contradictory. R2552 (G00017|Environmental damage.1) and its copies say "Damage is inflicted even against a dodge"; R1218 {Necrosis} says "[THN] If the strike is dodged, environmental damage is not applied." No row in the section states the reconciling boundary (environmental damage arising from an already-resolved source vs. environmental damage delivered as part of the dodged strike).

**Recommendation:** The drafter must state the boundary explicitly rather than pick a side, and R1218 is the ruling that forces it — keep it and place it adjacent to R2552 in the prose. Flag as a tension for adjudication if the two cannot be reconciled from the ruling text alone; consider a ⚠ REVIEW marker.

*Rulings (5):* R1218, R2552, R0394, R0451, R1860

### [medium] missing-topic

The section is entirely about what a dodge does or does not reach after the fact. Nothing here covers: (a) a general statement of the dodge itself — there is no G000xx|Dodge entry in the membership, so the section rests wholly on the rulebook; (b) "cannot be dodged" / undodgeable strike wording as a template; (c) dodge against multiple or additional strikes (does one dodge answer one strike); (d) dodge interaction with maneuvers and presses. First strike is touched by exactly one row, R1751 {Stutter-Step}.2, on a card with unique dual hand-strike/dodge text.

**Recommendation:** Warn the drafter that 4.6 will be thin outside the supplementary-effects principle and must open by citing the rulebook for what a dodge is. If "cannot be dodged" wording exists in the corpus, it was likely absorbed by 4.3 or 1.1 — worth a targeted grep before drafting so the section does not ship without its exclusion template.

### [low] role-error

Identical text received split roles across chunks, the signature of cross-chunk drift. The eight-copy wording is P on R0372, R0559, R0564 but E on R0658, R1368, R1545, R1612, R1971. The four-copy wording is P on all three card copies (R0394, R0451, R1860) while the general entry R2552 that should carry the P is filed secondary.

**Recommendation:** Low stakes per the contract and not worth reclassifying, but note it as confirmation of the duplicate-template findings above rather than as independent evidence. If anything is changed, make R2552 the P and demote the card copies to E per the general-rule-entries rule in the contract.

*Rulings (12):* R0372, R0559, R0564, R0658, R1368, R1545, R1612, R1971, R0394, R0451, R1860, R2552

### [low] misfiled

R0558 {Dust Up}.2 — "the additional strike is not optional: you cannot play it for the dodge only if you already played it for a (limited) additional strike this round" — teaches nothing about the scope of a dodge. It is a once-per-round restriction on a card that happens to offer a dodge as one of its modes.

**Recommendation:** Conservative call since it is filed here as secondary and its PRIMARY is presumably sound, but the drafter of 4.6 has no use for it. 4.3 (additional strikes) or 1.2 (periodicity, "this round") owns it.

*Rulings (1):* R0558

## 4.7

### [high] duplicate-template

Nine rulings are the same wording template — a card that burns itself when used as a strike "does not burn if combat ends before it resolves (eg. if the opponent uses a 'strike: combat ends')" — carrying the identical reference set [LSJ 20001127-2] [LSJ 20010806-1] [LSJ 19981006]. R0229 Bomb, R0958 Jar of Skin Eaters, R2013 Waxen Poetica and R2029 White Phosphorus Grenade are word-for-word identical; R0580 Elixir of Distillation and R0536 Dragon's Breath Rounds are the same sentence minus the parenthetical; R0608 Escaped Mental Patient is the same rule stated on an ally. Under the no-exhaustive-card-lists rule this is one principle with 'e.g.' plus one to three cards, not nine examples. There is one genuine nuance buried in the set worth preserving: R0685 Flash Grenade and R1664 Smoke Grenade say the card STILL burns when the opponent also plays a strike: combat ends, because those burn on use rather than on resolution — the opposite polarity from the other seven.

**Recommendation:** Draft one principle — an unresolved strike pays none of its costs and produces none of its effects, so a self-burning weapon or ally is not burned — and keep exactly two 'e.g.' cards on opposite polarities: {Bomb} (R0229, burns on resolution, so not burned) and {Flash Grenade} (R0685, burns on use, so burned even against a strike: combat ends). Demote the remaining seven (R0536, R0580, R0608, R0958, R1664, R2013, R2029) to C — they add no principle the two keepers do not already carry, and each is a pure one-card restatement.

*Rulings (9):* R0229, R0536, R0580, R0608, R0685, R0958, R1664, R2013, R2029

### [medium] duplicate-template

One boilerplate paragraph appears verbatim five times: "Damage is inflicted even against a dodge. A 'strike: combat ends' ends combat before damage is applied, as will a combatant going to torpor during first strike" with the identical four-reference set [RTR 19941109] [TOM 19951216] [PIB 20140324] [ANK 20200422]. R2552 is the general rule entry G00017|Environmental damage.1; R0176 Blissful Agony, R0394 Conscripted Statue, R0451 Darkling Trickery and R1860 Thoughts Betrayed are the same text pasted onto four cards. All five are secondary here (their primary home is the environmental-damage rule in 4.4), so 4.7 needs the statement once as a cross-reference, not five times.

**Recommendation:** Keep R2552 (the G00017 general entry) as 4.7's single carrier of this point and cite it as a cross-reference to 4.4; drop R0176, R0394, R0451 and R1860 from the 4.7 extract entirely. They remain correctly filed under their primary code.

*Rulings (5):* R2552, R0176, R0394, R0451, R1860

### [medium] duplicate-template

A second family restates the same underlying rule as the burn family, only for non-burn consequences of the unresolved strike: R0452 Darkness Within (blood not removed), R1178 Molotov Cocktail (not put on the minion), R1515 Rowan Ring (opponent avoids the effect, ring stays), R0940 Internal Recursion (blocking vampire does not unlock), R0524 Dog Pack (opponent's already-declared strike has no effect). Five cards, one rule — the strike never resolves, so nothing it would have done happens. Filed as five separate P/E rows this reads to a drafter as five things to say.

**Recommendation:** Fold this family into the same principle as the burn family and keep at most one 'e.g.' from it — R1178 {Molotov Cocktail} is the strongest, because its wording adds a real qualifier the others lack (the strike stays unresolved 'even if combat continues thanks to another effect like {Relentless Reaper}'), which is the non-obvious part. Demote R0452, R1515 and R0940 to C: each is a pure one-card interpretation of that card's own printed effect, and R0524 is Dog Pack-specific timing better served by a cross-reference.

*Rulings (5):* R0452, R1178, R1515, R0940, R0524

### [medium] missing-topic

The taxonomy scope line for 4.7 is "timing vs. damage; first strike interaction", but no ruling in the membership states the base rule itself — that a strike: combat ends ends combat upon its own resolution, before the opposing strike resolves. Every row is a downstream consequence observed on a particular card. First-strike interaction is likewise present only obliquely: R0765 Gianna di Canneto mentions in passing "or if combat ends due to first strike aggravated damage", and R2552's boilerplate mentions "a combatant going to torpor during first strike". Nothing covers the case a judge actually gets asked about: a strike: combat ends declared against an opponent who has first strike, and whether the first-striking opponent's damage lands before combat ends.

**Recommendation:** Flag to the drafter that 4.7's opening statement of the rule and its first-strike sub-topic must be written from the rulebook (the strike sequence) rather than from ruling evidence, and mark the first-strike ordering claim with the project's ⚠ REVIEW marker until a judge confirms it. Also consider pulling in whichever chapter-4.3 rulings own first-strike ordering as a cross-reference rather than leaving the sub-topic empty.

*Rulings (3):* R0765, R2552, R1509

### [low] misfiled

R1679 Soul Burn.4 — "Only nullify the weapon damage when it resolves, an opponent can successfully use {Rötschreck} after declaring a strike with {Ivory Bow}" — never mentions a strike: combat ends and is not about one. It is about when Soul Burn's nullification takes effect relative to a combat-ending card played after strike declaration. It is a secondary row, so the cost is only extract noise, but it will read to a 4.7 drafter as an off-topic case.

**Recommendation:** Drop the 4.7 code from R1679; its content belongs to 4.9 (effects lost when combat ends early) or 4.10 (weapon damage value), whichever holds its primary.

*Rulings (1):* R1679

### [low] duplicate-template

R0060 and R0062 are the same Anesthetic Touch ruling split across two entries: R0060 "Does not end combat as a strike; it ends combat after strike resolution" and R0062 "Does not end combat until after strike resolution, so the damage can be prevented or healed as normal". The second is the first plus its immediate consequence. Both are P and both are PRIMARY, so the drafter receives one point as two prose candidates.

**Recommendation:** Keep R0062 as the P (it states the rule and its consequence together) and demote R0060 to E, or merge the two when drafting. R0061 (dodge does not prevent the later combat end) is a distinct point and should stay. Low stakes — no reclassification needed if the drafter reads them together.

*Rulings (2):* R0060, R0062

## 4.8

### [high] duplicate-template

36 of 64 rulings (56%) are one wording template — 'The press can only be used during the current round.' — all citing the single ruling [TOM 19960521], spread across effectively every chunk. This is one principle, not 36 examples, and the style rule caps it at 1-3 'e.g.' cards.

**Recommendation:** Collapse to one prose statement ('a press provided by a card is usable only in the round that card was played') with three e.g. cards chosen to cover the wording variants: R0901 {Immortal Grapple} for the bare template, R0304 {Chameleon's Colors} for the 'optional press' variant (it feeds the mandatory/optional sub-topic below), and R0556 {Dust to Dust} for 'press and maneuver' (cross-ref 4.2). Add R1910 {Undead Persistence} as the multi-round edge case ('only provides one press for the current round, not the ones after'). The remaining 32 stay in the rulings database.

*Rulings (36):* R0030, R0041, R0106, R0108, R0215, R0230, R0304, R0370, R0371, R0499, R0519, R0556, R0789, R0857, R0901, R0916, R0961, R0999, R1001, R1128, R1149, R1310, R1335, R1467, R1484, R1614, R1616, R1630, R1728, R1731, R1863, R1864, R1883, R1906, R1950, R2025

### [high] scope-drift

A 13-ruling cluster is a second topic with its own seam: end-of-round effect ordering ('Must be played after the presses are handled and can be played if the round ends prematurely', [RTR 20030519]). Its principle is where end-of-round effects sit in the round script and that they still resolve when the round ends prematurely — presses appear only as the anchor landmark. That is 4.9 (end of round / combat) or 4.1 (the round script), not 4.8 (presses: current round only; press priority).

**Recommendation:** Move the cluster to 4.9, leaving at most a cross-reference in 4.8 fixing the press step's position in the round. Note the classifiers were themselves split on this: R0403, R0508, R1127, R1272, R1392, R1455, R1475 were filed PRIMARY here while the identically-worded R0919, R1382, R1743, R1816, R1827 were filed secondary — cross-chunk drift on the same sentence. R1631 {Shoulder Drop} ('before any other pair of strikes and before the press step') is strike sequencing, 4.3 primary, and follows the same cluster out.

*Rulings (13):* R0403, R0508, R0919, R1127, R1272, R1382, R1392, R1455, R1475, R1743, R1816, R1827, R1631

### [medium] duplicate-template

A third template, 8 rulings on 8 crypt cards, all citing [PIB 20150121]: 'His/Her ability to get/give a press can only be used during the press step.' Together with the two clusters above, 56 of 64 rulings (87.5%) in 4.8 are three wording templates.

**Recommendation:** One sentence — a vampire ability granting a press is usable only during the press step — with two e.g. cards covering both polarities: R2096 {Aeron} (get a press, for oneself) and R2185 {Don Caravelli} (give a press, to another minion). Drop the other six.

*Rulings (8):* R2096, R2185, R2292, R2335, R2389, R2399, R2457, R2472

### [medium] missing-topic

'Press priority', one of the two topics 4.8's scope line names, rests on a single ruling (R1886 {Trap}: the provided press must be handled first; another press cannot be used to continue if there is already one). R1887 {Trap} covers the adjacent point that a minion barred from pressing can still provide presses. Nothing in the membership covers who presses when both minions have a press available, or how a press interacts with effects that end combat (4.7 crossover).

**Recommendation:** Flag to the drafter that press priority will be thin: it can be stated from R1886 alone but cannot be illustrated beyond {Trap}/{Boxed In}. Either write it narrowly as a {Trap}-anchored rule or check whether the both-minions-press and press-vs-combat-ends cases are owned by 4.1/4.7 and cross-reference rather than leaving a gap.

*Rulings (2):* R1886, R1887

### [low] role-error

Identical wordings received split roles across chunks, violating the contract's 'identical rulings must get identical labels'. In the [TOM 19960521] template 32 rows are P and 4 (R1149, R1906, R1950, R2025) are E; in the [PIB 20150121] template 4 rows are E and 4 (R2335, R2389, R2399, R2457) are P.

**Recommendation:** Cosmetic only, and P/E is explicitly low-stakes — but since both templates collapse to one principle plus 2-3 examples anyway, resolve by making the retained e.g. cards E and the single prose statement P. No reclassification effort warranted beyond that.

*Rulings (8):* R1906, R1950, R2025, R1149, R2335, R2389, R2399, R2457

### [low] other

A genuine third sub-topic is present but scattered and easy to miss: whether a press is mandatory or optional. R1791 {Talbot's Chainsaw} ('the press is mandatory') and R2304 {Lorrie Dunsirn} ('her press and additional strike are mandatory') are both filed secondary, while the optional side survives only inside the [TOM 19960521] template rows (R0304, R1149, R1467 say 'the optional press').

**Recommendation:** Keep this as a named sub-topic of 4.8 rather than letting it dissolve into the template collapse: presses provided by a card are mandatory unless the card says otherwise, e.g. R1791 {Talbot's Chainsaw} (mandatory) vs R0304 {Chameleon's Colors} (optional). Preserving R1791 and R2304 through the dedup is the point.

*Rulings (5):* R1791, R2304, R0304, R1149, R1467

## 4.9

### [high] duplicate-template

The single largest cluster in the section: one principle -- 'an effect that ends combat loses its own after-combat riders when the combat continues or a new combat is queued; unlock effects are the exception' -- is present 23 times. Ten rows are the VERBATIM abstract statement, character-for-character, on ten different cards with identical refs [LSJ 19980109] [RTR 20020501] (R0653 Fast Reaction.1, R0698 Follow the Alpha.1, R0828 Haven Hunting.1, R0849 Hidden Lurker.1, R1380 Psyche!.2, R1453 Relentless Reaper.2, R1825 Telepathic Tracking.1, R2102 Akram.1, R2251 Jalal Sayad.1, R2327 Marie-Pierre.3) -- all ten labelled PRIMARY. Thirteen more are per-card instantiations of the same sentence ('If the combat continues or a new combat begins, <this card's rider> does not happen'), also nearly all PRIMARY. Under the no-exhaustive-lists rule this is one paragraph of prose plus at most three e.g. cards; 20 of the 23 are pure repetition that a drafter must read and discard.

**Recommendation:** Keep ONE copy of the abstract statement as the prose source -- R1380 (Psyche!.2), the canonical carrier. Keep R2102 (Akram.1) as the one showing a minion ABILITY, not a card, triggers the same loss. Then keep at most three instantiations chosen for contrast value, not for coverage: R1665 (Smoke Grenade.2 -- still burns) vs R0683 (Flash Grenade.2 -- burns but its lock effect is lost) vs R1511 (Roetschreck.9 -- partial survival: card placed, no torpor, but 'does not unlock as normal' persists). Those three draw the boundary of what survives. Demote the remaining ~18 to C.

*Rulings (23):* R0653, R0698, R0828, R0849, R1380, R1453, R1825, R2102, R2251, R2327, R0289, R0683, R1031, R1057, R1192, R1204, R1276, R1491, R1511, R1575, R1665, R0884, R1190

### [high] duplicate-template

Second large cluster: 'Cannot be used to start a new combat if there is already a pending combat queued' [RTR 20020501] appears verbatim on ten cards/abilities (R0180, R0654, R0699, R0829, R0850, R0886, R1318, R1381, R2103, R2252), plus three near-identical restatements from the other direction (R0885 Illusions of the Kindred.2 'no other combat can be queued afterwards', R1642 Siren's Lure.2, R1643 Siren's Lure.3). Thirteen rulings for the rule 'at most one combat may be queued at a time'. PRIMARY/secondary is also assigned inconsistently across identical text (R0180 PRIMARY vs R1318 secondary).

**Recommendation:** State the one-queued-combat rule once. Keep R1381 ({Psyche!}) as the canonical e.g., R2103 ({Akram}) to show abilities are bound by the same limit, and R1643 ({Siren's Lure}) because it states the complementary half (no other queueing effect may be used until the queued combat begins). Demote the other ten to C.

*Rulings (13):* R0180, R0654, R0699, R0829, R0850, R0886, R1318, R1381, R2103, R2252, R0885, R1642, R1643

### [medium] duplicate-template

The end-of-round window is stated 16 times. Two interleaved templates: 'Must be played after the presses are handled and can be played if the round ends prematurely' [RTR 20030519] on eight cards (R0508, R1382, R1392, R1455, R1475, R1743, R1816, R1827), and 'Can be played before or after effects that are played at the end of the round or "when the combat would end"' [LSJ 20021113] [ANK 20191219] [ANK 20180910-1] on six more (R0510, R1384, R1393, R1744, R1817, R1828). R1127 (Masochism.1) and R1272 (Ossian.2) are the same after-presses rule applied to triggered effects rather than card plays -- the only two rows in the set that add anything.

**Recommendation:** One paragraph: the end-of-round window opens after presses are resolved, survives a round that ends prematurely, and its occupants are mutually orderable. Keep R1816 ({Taste of Vitae}) and R0510 ({Disarm}) as the e.g. pair, plus R1272 ({Ossian}) to show the rule governs triggered effects too, not only card plays. Demote the other 13. Cross-reference 4.8 for presses rather than restating.

*Rulings (16):* R0508, R1382, R1392, R1455, R1475, R1743, R1816, R1827, R0510, R1384, R1393, R1744, R1817, R1828, R1127, R1272

### [medium] duplicate-template

'If the combat continues or a new combat begins, the "action continues as if unblocked" effect is lost' appears verbatim on seven cards (R0309 Chameleon's Colors.6, R0695 Flow Within the Mountain.5, R1167 Mirror Image.5, R1198 Morphean Blow.7, R1594 Shadow Body.5, R1873 Toreador's Bane.5, R1880 Torrent.5), with R0728 (Form of Mist.5) the same rule phrased as '"After combat ends" effect cannot be used'. All eight are labelled P -- eight copies of one sentence claiming to be the prose statement. PRIMARY assignment drifted across chunks on identical text: R1873, R1880 and R0728 are PRIMARY while the four identical rows R0309, R0695, R1167, R1198, R1594 are secondary. This is also a specialisation of the finding above, and continue-as-if-unblocked is 3.6's topic.

**Recommendation:** Collapse to a single cross-reference: 4.9 states that after-combat riders are lost and points to 3.6 for the continue-as-if-unblocked case. Keep R0728 ({Form of Mist}) as the one e.g. -- 3.6's scope line already names it -- and demote the other seven. Companion rows R1871/R1878 ('an action cannot continue as if unblocked after a combat resulting from a successful action') are also a matched pair and belong to 3.6, not here.

*Rulings (8):* R0309, R0695, R1167, R1198, R1594, R1873, R1880, R0728

### [medium] duplicate-template

The [RTR 19970630] family states one contrast 13 times: the unlock half of a strike effect resolves BEFORE combat ends (so it survives continuation), while the rest of the effect resolves AFTER combat ends (so it is lost). Seven rows carry the unlock half (R0231, R0232, R0562, R1085, R1140, R1141, R1203) and six the after-combat half (R0288 Catatonic Fear.2, R1145 Mercy for the Weak.1, R1488 Riposte.1, R1574 Serpent's Numbing Kiss.1, R1929 Unholy Penance.1, R2328 Mariel Lady Thunder.1). Every row is the same sentence with a different card's rider substituted in.

**Recommendation:** One paragraph stating the before/after split, since it is what makes 'except for unlock effects' in the main principle intelligible. Keep R1203 ({Mummify}) as the single best e.g. -- it carries BOTH halves in one ruling ('the unlock effect takes place before the end of combat, the rest of the effect takes place after') -- plus R1140/R1141 ({Meld with the Land}) if a second is wanted. Demote the remaining ten.

*Rulings (13):* R0231, R0232, R0562, R1085, R1140, R1141, R1203, R0288, R1145, R1488, R1574, R1929, R2328

### [medium] duplicate-template

'Does not burn if combat ends before it resolves' with the identical ref triple [LSJ 20001127-2] [LSJ 20010806-1] [LSJ 19981006] on five cards: R0580 (Elixir of Distillation.1), R0798 (Grenade.2), R2013 (Waxen Poetica.1), R2029 (White Phosphorus Grenade.2), R1664 (Smoke Grenade.1). One principle -- a card whose cost is paid on resolution is not paid if combat ends first -- filed five times, twice as PRIMARY and three times as secondary.

**Recommendation:** Keep R0798 ({Grenade}, the clearest: neither burns nor inflicts damage) and R1664 ({Smoke Grenade}) for its contrast case (still burns against a simultaneous strike: combat ends, but not against {Roetschreck}). Demote R0580, R2013, R2029. Note this principle sits closer to 4.7 (strike: combat ends) than 4.9; cross-reference rather than duplicate the paragraph.

*Rulings (5):* R0580, R0798, R2013, R2029, R1664

### [medium] duplicate-template

Three further small identical-wording sets. (a) 'Cannot start a new combat if the opponent is not ready / is going to torpor': R0181 (Blissful Agony.7), R1021 (Left for Dead.1), R1319 (Pocket Out of Time.2), R1379 (Psyche!.1) -- four copies of one requirement. (b) 'When ending combat, cards that are played at the end of round/combat can still be played (eg. {Taste of Vitae}, {Disarm})' -- R0034 (Alpha Glint.1), R0583 (Elysium: The Arboretum.1), R0749 (Garibaldi-Meucci Museum.1) are character-identical with identical refs [RTR 20001020] [LSJ 20001024], all three P PRIMARY. (c) R1216 (Nar-Sheptha.3) and R1412 (Raptor.1) are the same sentence word for word.

**Recommendation:** (a) keep R1379 ({Psyche!}) and R1021 ({Left for Dead}, the ally case), demote the other two. (b) keep exactly one -- R0583 -- and demote R0034 and R0749. (c) keep R1412, demote R1216.

*Rulings (9):* R0181, R1021, R1319, R1379, R0034, R0583, R0749, R1216, R1412

### [medium] over-absorbed

Three rows are P/E but teach nothing transferable. R2112 (Amelia, The Blood Red Tears.3) is 'In the case of {Free Fight}, the last opposing minion burns the blood' -- a two-card interaction naming both cards, affecting no third card; fails transfer. R1489 (Riposte.2) is 'The damage is only dealt if the strike was resolved at close range' -- a reading of Riposte's own printed text, and not an end-of-combat statement at all. R2049 (Yawp Court.5) walks through a specific {Roetschreck}-vs-{Yawp Court} board state; whatever is general in it ('combat ends before torpor', referendum after all combats) is already stated abstractly by its own sibling R2050.

**Recommendation:** Reclassify R2112 and R1489 as C. R1489's only general content ('the strike must have resolved') belongs to 4.3 if kept anywhere. Reclassify R2049 as C, noting R2050 as the surviving general statement.

*Rulings (3):* R2112, R1489, R2049

### [medium] other

A wording discrepancy only visible with the section assembled. For {Disarm} and {Pulled Fangs} the ruling says end-of-round cards 'Can be played before or after [CEL] {Psyche!}' (R0510, R1393). For {Street Cred} and {Taste of Vitae} the same template ends 'Can be played AFTER [CEL] {Psyche!}' (R1744, R1817) -- same card class, same ref triple [LSJ 20021113] [ANK 20191219] [ANK 20180910-1], different permission. Meanwhile R1383 (Psyche!.5) and R1826 (Telepathic Tracking.2) say 'would end' replacement effects cannot be played after {Psyche!} at all. A drafter reading only R0510 and only R1744 would write two different rules.

**Recommendation:** Do not let the drafter collapse these four into one sentence. Route all six to a single tension file (slug: psyche-end-of-round-ordering) for adjudication before drafting; the likely resolution is that end-of-round cards are freely orderable around {Psyche!} while 'when combat would end' REPLACEMENT effects are one-way, and the {Street Cred}/{Taste of Vitae} wording is an imprecision -- but that needs confirming, not assuming.

*Rulings (6):* R0510, R1393, R1744, R1817, R1383, R1826

### [low] misfiled

Two secondary rows have no end-of-combat content. R0293 (Cats' Guidance.2) is 'Cannot be played if the vampire is in torpor' -- a torpor/ability-usability rule; the combat mention is only the scenario that put him there. R1490 (Riposte.3) is 'If the strike is dodged, no damage is done' -- squarely 4.6's scope (a dodge cancels the whole strike including supplementary effects).

**Recommendation:** Drop both from 4.9. R0293 belongs to 5.3 (or 1.5); R1490 belongs to 4.6, which already owns the principle. Low severity: both are secondary rows and are presumably correctly PRIMARY elsewhere, so this only trims the extract.

*Rulings (2):* R0293, R1490

### [low] missing-topic

4.9's scope line names three distinct windows -- 'when combat would end' vs 'at end of combat' vs 'after combat' -- but no ruling in the membership states their canonical ORDER as a single sequence. Everything is pairwise and card-attached ('X can be played before or after Y'). The closest are R2325 (Marie-Pierre.1: 'would end'/'about to end' cards precede after-combat abilities), R2050 (Yawp Court.6: applied after end-of-round and 'would end' cards, damage between two combats), and R1375 (Provision of the Silsila.2: after-combat effects are mutually orderable). No general-rule entry (G000xx) anchors the section at all.

**Recommendation:** Tell the drafter this section's spine must be synthesised from pairwise rulings rather than quoted. R2325 + R2050 + R1375 are the three load-bearing rows for the sequence presses -> end-of-round -> 'would end' replacements -> end-of-combat -> after-combat; mark the assembled ordering with an explicit review flag, since no single ruling states it.

*Rulings (3):* R2325, R2050, R1375

## 5.1

### [high] duplicate-template

The `[MERGED] Is <sect>. If the base version was the one in play, it changes sect as it is merged. If it had an anarch token, it is burned. [ANK 20180524]` sentence appears verbatim on 19 separate crypt cards, plus R2449 (Tariq) as a reworded 20th. These 20 rows are 38% of section 5.1's entire membership and carry exactly one rule between them. All 20 are PRIMARY, so the drafter receives them as core material and will see a wall of identical sentences. This is one principle plus an 'e.g.', not 20 examples, and the style rule forbids exhaustive card lists.

**Recommendation:** Collapse to one principle statement — 'merging with the advanced card sets the vampire's sect to the advanced card's sect, and burns any anarch token' — with three e.g. cards spanning the variants: R2222 {Goratrix} (sect change + anarch token burned), R2178 {Dancin' Dana} (sect change, no token clause), and R2516 {Yazid Tamari} (multi-trait result: Anarch Black Hand Seraph, and it carries a second reference [LSJ 20031121-3]). Demote the other 17 to C. Keep R2449 {Tariq, The Silent} only if the drafter wants the 'in whatever way' phrasing, which is the most general wording in the cluster.

*Rulings (20):* R2162, R2178, R2218, R2222, R2232, R2254, R2290, R2307, R2322, R2323, R2347, R2390, R2410, R2418, R2439, R2458, R2514, R2516, R2517, R2449

### [medium] over-absorbed

Nine of 52 rows are {Dual Form} or its interactions (R0028, R0548-R0555). Several are pure one-card text interpretation and fail the transfer test. R0553 — 'If they are more than two Dual Forms of the same vampires, all the others are burned when one leaves the ready region, whatever chain they form' — describes a chain topology no other card produces. R0554 — 'If more than one go to torpor at the same time (eg. from {Edged Illusion}), the controller chooses which one they keep' — is Dual Form's own pair-resolution rule. R0552 (one of the pair leaves → the other burns, and that burn does not cascade back) is the card's printed mechanic restated. R0550 and R0551 enumerate which traits Dual Form copies and in what order, which changes no ruling on any other card.

**Recommendation:** Demote R0553 and R0554 to C outright (no transfer). Keep at most one of R0550/R0551/R0552 as the single Dual Form 'e.g.' — R0550 is the best candidate since 'only clan, sect, capacity and disciplines are copied; titles and other traits are not' is the closest to a general statement about what a copy effect carries. R0028 {Agent of Power} is a second illustration of the snapshot rule R0549 already states; prefer R0549 and demote R0028. Retain R0548 (capacity floor of one) and R0555 (permanent reduction survives into the uncontrolled region) — both are genuinely general and R0555 pairs with R0115.

*Rulings (6):* R0553, R0554, R0552, R0550, R0551, R0028

### [medium] duplicate-template

Four further exact-duplicate pairs, each split across chunks and each teaching a single rule. (a) R0302 {Chameleon} and R1033 {Legendary Vampire} are the identical sentence 'Cannot be used on a vampire who merged last turn: merging is not entering play' — and were labelled P and E respectively, violating golden rule 5. (b) R0826 {Hatchling} and R1418 {Raw Recruit} are the identical sentence 'The created vampire is not unique', both citing the same reference [LSJ 20100221]. (c) R2235 {Hermana Hambrienta Mayor} and R2237 {Hermana Hambrienta Menor} are word-for-word identical, same reference [LSJ 20051126]. (d) R2447 and R2448 are the same {Tariq, The Silent} ruling recorded on the base and advanced crypt ids, differing only in 'merged with the advanced/base version'.

**Recommendation:** Keep one of each pair and demote the other to C: keep R0302 (with R1131 {Masquerade Enforcement} as the second e.g. for the 'merging is not X' family), keep R0826, keep R2235, keep R2447. This collapses 8 rows to 4 with no loss of content. For (a), fix the label mismatch by making the survivor P — 'merging is not entering play' is the principle itself.

*Rulings (8):* R0302, R1033, R0826, R1418, R2235, R2237, R2447, R2448

### [medium] misfiled

R0354 {Clan Impersonation}.3 — 'When removed, the vampire goes back to its underlying clan' — is filed PRIMARY in 5.1, but 5.1's scope is capacity, uniqueness, merge, vampire creation and crypt card identity. None of those claims clan. This is verbatim 5.9's scope: 'temporary override vs. permanent change… the earlier resurfaces if the later lapses'. 5.9 was added late (2026-07-20) and this ruling is one of the instances that justified it.

**Recommendation:** Reassign PRIMARY to 5.9. 5.1 is not a defensible secondary either — nothing about clan reversion bears on capacity, uniqueness, merge or crypt identity.

*Rulings (1):* R0354

### [low] scope-drift

After the boilerplate collapse, the surviving merge rulings are still substantially about sect — a trait — and 5.9 owns trait change. None of the [MERGED] rows carries 5.9 as a co-code (all are PRIMARY 5.1 only), so a 5.1 drafter will end up writing sect rules that 5.9 also has to state. Separately, R0355 (clan inappropriate for title → benefit lost, yields if contested) and R0356 (most recent clan-change effect takes precedence) sit here as secondaries but are pure 5.8 and 5.9 material respectively; they add nothing a 5.1 drafter can use.

**Recommendation:** Add 5.9 as a co-code on the surviving merge/sect e.g. rulings so both extracts see them, and let 5.1 state only the merge-mechanics fact ('merging rewrites the vampire's traits to the advanced card's, and burns an anarch token') with a cross-reference to 5.9 for the trait-precedence rule. Drop R0355 and R0356 from 5.1's extract.

*Rulings (7):* R2222, R2347, R2410, R2449, R2162, R0355, R0356

### [low] missing-topic

5.1's scope names 'merge (advanced)' and the section has 20+ rulings on what merging *changes*, but not one ruling on the merge procedure itself — when a vampire may merge, what it costs, whether the base card must already be in play, or what becomes of the two cards afterwards. R2528 ('can be merged with {Theo Bell (ADV)} if you get to control one, eg. {Graverobbing}') and R1022 ({Legacy} burn option usable when all unmerged advanced vampires are in torpor) are the only rows that touch acquisition at all, and both are oblique.

**Recommendation:** Flag to the drafter that the merge sub-topic will be thin on procedure and must lean on the rulebook rather than on rulings. Worth a targeted sweep of the C pile and of 6.7 (influence phase & crypt) for merge-timing rulings that may have been filed there as transfer/influence material.

*Rulings (2):* R2528, R1022

### [low] role-error

The 19 identical [MERGED] rows split exactly 10 E / 9 P with no textual difference between them whatsoever. P vs E is low-stakes on its own, but a clean 10/9 split on byte-identical text is the clearest available measurement of cross-chunk drift and is worth recording as calibration evidence even though it needs no correction beyond the collapse in the first finding.

**Recommendation:** No separate action — resolved by collapsing the cluster. Record the split in the phase-3 quality notes as a drift datapoint: identical text reached opposite role labels in different chunks, confirming golden rule 5 is not self-enforcing across a fan-out.

*Rulings (19):* R2162, R2178, R2218, R2222, R2232, R2254, R2290, R2307, R2516, R2517, R2322, R2323, R2347, R2390, R2410, R2418, R2439, R2458, R2514

## 5.2

### [high] duplicate-template

Five rulings are byte-identical in wording AND reference set — 'His/Her ability can be used while locked or in torpor. [ANK 20220705] [LSJ 20100705]' on Maris Streck, Montano, Paul Forrest, Sundown and Toby (Montano adds only 'to provide stealth'). This is a single principle (a vampire's printed ability is not a card play and needs no unlocked state) recurring across five crypt cards in five different chunks, each labelled independently. R0410 {Courier} ('needs not be unlocked to let you look at a card') is the same principle on a retainer. Under 'no exhaustive card lists' this is one sentence plus one 'e.g.', not seven entries.

**Recommendation:** Collapse to one prose statement in 5.2 cross-referencing 1.5 (which owns 'ability use is not a card play; abilities usable in torpor/while locked' and is the more central owner of all five). Keep {Montano} as the single e.g. — it is the only one whose text names what the ability does — and optionally {Courier} to show the rule reaches retainers. Drop R2331, R2383, R2440, R2461 from 5.2's extract entirely.

*Rulings (7):* R2331, R2355, R2383, R2440, R2461, R0410, R2105

### [high] duplicate-template

Eleven rulings restate one pair of principles about unlock effects and combat continuation, most of them citing the same [RTR 20020501]. Positive form ('the vampire still unlocks if an effect continues the combat or begins a new combat') appears verbatim on {Bond with the Mountain} R0232, {Earth Meld} R0562, {Majesty} R1085, {Meld with the Land} R1141, and in variant form on {Loving Agony} R1057. Negative form ('if the combat continues or a new combat begins, the effect does not apply') appears on {Flash Grenade} R0683 and {Rötschreck} R1511; R0682 is the same negative on a dodge. R0231/R1140 are a third near-duplicate pair ('the unlock effect takes place before the end of combat' / 'when the strike resolves'). No drafter needs five cards to say the same thing once.

**Recommendation:** Write three sentences with one e.g. each: (1) an unlock effect that has already resolved is not undone by continued or new combat — e.g. {Earth Meld}; (2) an effect conditioned on combat ending does not apply when combat continues — e.g. {Flash Grenade} (R0683, which also carries the 'it still burns' wrinkle); (3) the unlock resolves at the strike, before combat ends — e.g. {Bond with the Mountain} R0231. Keep R0684 ({Flash Grenade}.3, re-locks after combat) as a genuinely distinct fact. Drop R0562-or-R1085-or-R1141 duplicates, R1057, R1140 from the extract. Cross-reference 4.9 rather than restating it.

*Rulings (11):* R0232, R0562, R1085, R1141, R1057, R0683, R1511, R0682, R0231, R1140, R0684

### [high] duplicate-template

Two identical-wording clusters on the unlock-to-block template. R0812 {Guard Duty}.3, R1557 {Second Tradition: Domain}.4 and R1570 {Sense the Savage Way}.4 are the same sentence with the same single reference [LSJ 20090514]: 'The block attempt and subsequent combat still happen if the action lacks a suitable target because of the unlock (eg. {Ambush}).' R1554 and R1567 are likewise the same sentence with the same reference [ANK 20181122-2]: 'Can be used by a vampire who is already attempting to block.' Five rows, two principles, three cards.

**Recommendation:** State each principle once. Keep {Guard Duty} R0812 as the e.g. for the lost-target case and {Second Tradition: Domain} R1554 for the already-attempting-to-block case. Drop R1557, R1570, R1567 from 5.2's extract.

*Rulings (5):* R0812, R1557, R1570, R1554, R1567

### [medium] duplicate-template

Four locations carry the same 'lock to reduce the cost' timing template: {Eccentric Billionaire} R0565 and {Sunset Strip} R1770 say 'when the action is announced or when the cost is paid' [LSJ 20090705]; {The Line} R1042 and {The Shard} R2079 say 'at any point before resolution, from when the action is announced to just before the cost is paid' [ANK 20230620]. Same mechanic, four cards, and the two phrasings do not obviously describe the same window — the first names two discrete points, the second a continuous span. R1771 {Sunset Strip}.2 adds the one non-duplicated fact (if the card is otherwise unaffordable the lock must happen at announcement).

**Recommendation:** One principle with one e.g. — use {The Line} R1042 as the wording (the later ANK ruling and the broader statement) and keep R1771 as the affordability wrinkle. Drop R0565, R1770, R2079. Flag the two phrasings for the drafter to reconcile: if they are the same window, say so once; if not, that is a real tension worth a sentence.

*Rulings (5):* R0565, R1770, R1042, R2079, R1771

### [medium] duplicate-template

{Deed the Heart's Desire}.1, {Psalm of the Damned}.1 and {Unleashing the Bestial Soul}.1 are the identical sentence with the identical single reference [ANK 20231028]: 'An opponent can play a reaction to wake as the card is played, before its effects apply.' Three chunks each labelled the same boilerplate separately.

**Recommendation:** One statement (the wake window opens in the 'as played' window, before the card's effects apply) with one e.g. — keep {Unleashing the Bestial Soul} R2093, the only one filed PRIMARY here. Drop R0463 and R1378. Cross-reference 1.8, which owns the 'as played' window, rather than restating it.

*Rulings (3):* R0463, R1378, R2093

### [medium] duplicate-template

{Gianna di Canneto}.3, {Giulia Giovanni Abruzzina}.2 and {Survivalist}.1 are the identical sentence with the identical reference [ANK 20180517]: 'He/She can lock to use his/her ability the turn he/she is recruited.' All three are filed secondary here, correctly — 3.7.4 owns 'acting the turn recruited'.

**Recommendation:** Keep at most one as a cross-reference example and drop the other two from 5.2's extract; the principle belongs in 3.7.4 and 5.2 should cross-reference, not repeat. Note the trio also confirms the taxonomy's own watch-list concern that 3.7.4 is overloaded with minion-state facts.

*Rulings (3):* R0766, R0773, R1777

### [medium] duplicate-template

'Can be played by a locked vampire' recurs verbatim on {Cloak the Gathering} [OBF] R0365, {Echo of Harmonies} [MEL] R0568 and {Mouthpiece} [DOM] R1200, three of them sharing [LSJ 19980210]; R1090 {Make an Example} is the same statement on a political action. One principle — an action modifier or action card imposes no unlocked requirement unless its text says so — illustrated four times across four disciplines.

**Recommendation:** One sentence, one or two e.g. — {Cloak the Gathering} and {Make an Example} (to show it covers political actions too). Drop R0568 and R1200. Do NOT fold R1153 {Mind Rape} into this group: 'can be played ON a locked vampire' is the converse (target eligibility, not actor state) and is a separate, keepable fact.

*Rulings (5):* R0365, R0568, R1200, R1090, R1153

### [medium] duplicate-template

{Champion}.1, {Discern}.1 and {Donate}.1 are the identical two-sentence boilerplate with the identical reference pair [LSJ 20070403] [LSJ 20070413]: '[REACTION] Can be used only when reactions can be used (unlocked or with a wake effect). It does not count as playing a reaction card.' Three chunks, three identical labels.

**Recommendation:** One statement — the reaction-timing window is a state requirement independent of whether a reaction card is played — with a single e.g. ({Champion}). Drop R0513 and R0529. Pairs naturally with R1242 {No Secrets From the Magaji} and R1656 {The Sleeping Mind}, which carry the genuinely distinct wake-vs-unlock content.

*Rulings (3):* R0310, R0513, R0529

### [medium] duplicate-template

The 'acting on a minion already in the target state' family is represented eight times. Verbatim duplicates: R0050 {Anarch Troublemaker} 'Can lock a vampire that is already locked' and R0250 {Brujah Debate} 'Can lock a locked Brujah'. Same principle on the unlock side: R1920 {Under Siege}.4 (intercept even if already unlocked), R0777 {Glutton} (unlock a ready Ishtarri), R0657 {Fata Amria} (burn at unlock even if already unlocked), R1947 {Vampiric Disease}.2 (unlocking an already unlocked vampire does not trigger). Eight rows for what the scope line already names as one sub-topic, 'unlocking the unlocked'.

**Recommendation:** State once that locking a locked minion and unlocking an unlocked minion are legal and are not no-ops for cost/trigger purposes, then keep the three that add something the bare statement does not: R1947 (the trigger does NOT fire — the informative counter-case), R1235 {Nightmares upon Nightmares} (deliberate lock-then-Infernal-unlock sequencing) and R2209 {Eze} (mandatory unlock applies even when already unlocked). Drop R0050-or-R0250 (keep one at most), R0777, R1920.

*Rulings (8):* R0050, R0250, R1920, R1947, R0777, R1235, R2209, R0657

### [low] over-absorbed

Three rulings labelled E here fail the transfer test — they only affect situations involving their own card. R1519 {Ruins of Charizel}.1: 'Only works when unlocking minions using their Infernal ability (eg. not with {Path of Evil Revelations} nor {Metro Underground})' is a reading of one card's trigger clause. R0623 {Exile}.1: 'You may lock Orun cards the vampire has even if they're not Laibon' is a reading of one card's Orun clause. R2070 {Revelation of the Serpent}.1: 'Cannot be used to unlock if the target is ousted by the bleed' is about the oust removing the target, which 6.5 owns, not about lock/unlock.

**Recommendation:** Reclassify R1519 and R0623 as C (pure one-card text interpretation; they stay in the rulings database). Re-file R2070's primary to 6.5 (oust timing and consequences) with 5.2 secondary at most. None of the three should reach the drafted section.

*Rulings (3):* R1519, R0623, R2070

### [low] misfiled

Four PRIMARY/near-PRIMARY filings whose principle is owned elsewhere. R2445 {T.J.}.1 'Must be unlocked with at least 2 blood' and R0866 {Hide the Heart}.5 'you need to be unlocked' both cite [RBK wording-templates] and both teach how a state-requirement clause in card text is read — that is 1.2 (wording templates) or 1.6 (requirements), with 5.2 only supplying the vocabulary; R2445 is currently P PRIMARY here. R1573 {Seraph's Second}.1 (unlock a vampire who just resolved an action to become Black Hand) is a trait-timing ruling — 5.9 — exactly parallel to R2005 {Warsaw Station}.3 (Nosferatu checked at the post-resolution unlock), which is correctly filed here as secondary. R0049 {Anarch Revolt}.2 (condition checked at the END of the unlock phase, not continuously during it) is P PRIMARY in 5.2 but teaches nothing about locking or unlocking — it is an evaluation-window rule (2.5).

**Recommendation:** Move R2445's primary to 1.2/1.6 keeping 5.2 secondary; move R1573's primary to 5.9 keeping 5.2 secondary (it should mirror R2005, not lead 5.2); move R0049's primary to 2.5. Retain them in 5.2's extract as secondaries so nothing is lost, but they should not drive 5.2's prose.

*Rulings (4):* R2445, R0866, R1573, R0049

### [low] duplicate-template

R0117 {Banishment}.4 and R0491 {Descent into Darkness}.4 share [LSJ 20060908] and state the same thing about a minion re-entering play: 'The vampire and all cards on them come back unlocked' / 'All cards on the vampire come back unlocked.' R0117 is strictly richer — it adds the load-bearing qualifier 'This is not unlocking (ie. for {Anima Gathering}, {Vampiric Disease}).'

**Recommendation:** Keep R0117 as the sole e.g.; drop R0491. The 'comes back unlocked but that is not an unlock' distinction is one of 5.2's better prose candidates and pairs with R1947 {Vampiric Disease}.2 — cross-reference 6.4 (leaving and re-entering play) rather than restating it.

*Rulings (2):* R0117, R0491

### [low] missing-topic

Three rulings depend on the phrase 'ready, unlocked minion' ({Brujah Frenzy}.4, {Malleable Visage}.2, {Glutton}.1) but no ruling in the section's 113 rows defines the ready / unlocked / locked / torpid vocabulary or explains why card text says 'ready, unlocked' rather than just 'unlocked'. 5.2 is the section that must state it (5.3 owns torpor as a state, not the readiness vocabulary), and the drafter will have to write it from the rulebook with no ruling support. Also unrepresented: any ruling on what a locked minion may still do as a target or participant, beyond R0511's single 'locked vampires can still vote'.

**Recommendation:** Flag to the drafter that the opening paragraph of 5.2 — the state vocabulary — must be sourced from the rulebook ([RBK] footnote) rather than from a ruling, and that the 'locked minions remain valid targets/participants' point rests on {Disarming Presence} R0511 alone.

*Rulings (3):* R0254, R1103, R0777

## 5.3

### [high] duplicate-template

The single largest cluster in 5.3 is one general rule entry restated on eleven vampires. R2562 (G00027 "Ability usable in torpor") IS the principle; R2173 Carmine Giovanni, R2267 Karif al Numair, R2302 Lord Tremere, R2378 Pariah, R2464 Tori Longwood, R2329 Mariel, R2503 Wamukota all carry the identical reference pair [LSJ 20011022] [LSJ 20100902-2] and say nothing the general entry does not ("His ability applies when he is in torpor."). R2321 Marciana is the same template on a different ref. A parallel family sits under R2574 (G00039 "Unconditional referendum ability"): R2355 Montano, R2383 Paul Forrest, R2461 Toby are word-for-word "can be used while locked or in torpor" on [ANK 20220705] [LSJ 20100705]. Fourteen rows, two principles.

**Recommendation:** Draft from the two general entries (R2562, R2574) as the P prose. Keep at most three "e.g." cards total, chosen for variety of ability TYPE rather than count: R2302 Lord Tremere (unlock), R2503 Wamukota or R2329 Mariel (end combat), R2359 Nahir (hand-size bonus — the only one that is not a minion-facing ability and so genuinely extends the rule). Drop the remaining nine to C/database.

*Rulings (14):* R2562, R2173, R2267, R2302, R2329, R2378, R2464, R2503, R2321, R2574, R2355, R2383, R2461, R2359

### [high] duplicate-template

Five rows are the same parenthetical boilerplate on one reference [LSJ 20090622-2]: "the opponent is wounded (if they play {Undying Tenacity}, they go to torpor after combat)" — R0374 Coma, R0600 Entombment, R1516 Rowan Ring, R2403 Rabbat, R2425 Seren Sukardi. Two of them (R2403, R2425) are additionally marked P, so the wounded principle risks being stated in the document in the voice of a specific vampire's strike.

**Recommendation:** State the wounded/delayed-torpor rule once from R0091 (Ashes to Ashes.1), which actually articulates it — the torpor trigger can be interrupted while the unlock, blood gain and wounding still occur. Keep one of the five as the "e.g." (R0374 Coma reads most cleanly) and demote R0600, R1516, R2403, R2425. Correct R2403/R2425 from P to E if they are retained at all.

*Rulings (6):* R0374, R0600, R1516, R2403, R2425, R0091

### [medium] duplicate-template

Six further exact-duplicate pairs/triples that no single classifier could see. (1) "Can be used by a vampire in torpor" on [LSJ 20020416]: R0173 Bliss, R1107 Martyr's Resilience, R1246 Nosferatu Putrescence, R1534 Save Face — four identical rows, and inconsistently roled (R1534 P, the other three E, same sentence). (2) "The vampire can play cards which are not usable by vampires going to torpor" on [LSJ 19970303]: R1909 Undead Persistence.1 and R1925 Undying Tenacity.1 — identical. (3) "Can be used when the vampire is in torpor" on [PIB 20150522]: R0189 Blood Doll and R1972 Vessel — identical; R1407 The Rack.3 is the same rule but strictly richer (adds the not-controlled limit). (4) "Cannot be used to enter combat with a vampire on his way to torpor" on [LSJ 20100604-1]: R0181 Blissful Agony.7 and R0852 Hidden Lurker.4 — identical. (5) "The stolen minion returns to his previous controller even if he is in torpor (but stays in torpor)" on [LSJ 20010119]: R1157 Mind Rape.5 and R1834 Temptation.3 — identical, and 6.2 owns the principle anyway.

**Recommendation:** One entry per family with 1-2 "e.g." cards: keep R0173 (+ optionally R1534) for combat-cards-from-torpor; keep R1909 only (R1925 is the same sentence on the sister card); keep R1407 The Rack over R0189/R1972 since it carries the extra limit; keep R0852 only; keep one of R1157/R1834 as a cross-reference to 6.2. Roughly nine rows leave the extract.

*Rulings (13):* R0173, R1107, R1246, R1534, R1909, R1925, R0189, R1972, R1407, R0181, R0852, R1157, R1834

### [medium] duplicate-template

The "burn option can be used if all your vampires with [mal] are in torpor" ruling [LSJ 20091203] appears three times verbatim (R0123 Barrenness, R0619 Evil Eye, R0586 Emergency Powers, the last with Seraph substituted for [mal]). R0871 High Orun.2 is filed alongside them but reaches the OPPOSITE result — "cannot be used if control a Laibon with three Orun, even if they are in torpor" — because its condition reads control rather than readiness. Presented as four peers this will read to a drafter as a contradiction.

**Recommendation:** Keep one of R0123/R0619/R0586 as the "e.g." and state the principle once (a torpid vampire is still controlled but not ready, so which of the two a card's condition names decides the outcome). Either use R0871 deliberately as the contrasting second example or drop it — it is otherwise a pure {High Orun} counter-condition interpretation that fails transfer.

*Rulings (4):* R0123, R0619, R0586, R0871

### [medium] misfiled

Two secondary rows contain no torpor content at all. R0093 (Ashes to Ashes.3) is entirely about a diablerie attempt failing and another {Amaranth} being playable — the principle is diablerie/repetition. R1483 (Righteous Aura.1) is about a hosted card burning before its bearer leaves the ready region, and its own example is {Banishment}, not torpor.

**Recommendation:** Drop both from 5.3's extract. R0093 belongs to 3.7.8 (diablerie) with 3.5 for the repeat-attempt half; R1483 belongs to 1.12 (cards on cards / host leaves play) with 6.4. Neither adds anything a 5.3 drafter would use.

*Rulings (2):* R0093, R1483

### [low] misfiled

R1610 and R1611 ({Shadow Court Satyr}) are marked PRIMARY in 5.3, but the principle they teach is that an ally has no torpor state — an effect that would send it to torpor burns it instead (R1610), and aggravated damage costs it a life without torpor (R1611). That is a statement about allies, and a 5.3 drafter can only use it as a negative aside.

**Recommendation:** Make 5.5 (Allies) the primary owner of both and keep 5.3 as secondary. Same treatment for R1029 (Legacy of Power.1), already correctly secondary here.

*Rulings (2):* R1610, R1611

### [low] over-absorbed

R0678 (Flames of Insurrection.1) — "If two Anarchs are in combat and both go to torpor, both controllers can benefit from the effect" — is a reading of one card's distributive wording under a simultaneous-torpor edge case. It fails the transfer test: no other card's ruling changes because of it, and the torpor content is incidental to the question of whether one trigger fires twice.

**Recommendation:** Reclassify C with 1.15 (cumulative & stacking) as the near-miss code, or route it to 1.15 as primary if the drafter there wants a simultaneity example. It should not consume a slot in 5.3.

*Rulings (1):* R0678

### [low] missing-topic

5.3's scope line names "wounded" as a sub-topic, but the corpus reaching this section only ever mentions wounded inside the {Undying Tenacity} boilerplate (R0374 family) and one clause of R0091. Nothing here states what the wounded state does on its own, and nothing covers how torpor is entered (damage vs. running out of blood) or how a torpid vampire interacts with being targeted or blocked. The membership is rich on "what still works in torpor" and thin to empty on "how you get there and what wounded means".

**Recommendation:** Expect the wounded and entering-torpor passages to rest on the rulebook rather than on rulings; the drafter should cite [RBK] there and not go looking for ruling support that this extract does not contain. Worth confirming at Phase 4.5 that no wounded-specific rulings were routed to 4.4/4.5 and never cross-coded here.

*Rulings (2):* R0091, R0374

## 5.4

### [high] duplicate-template

Nine rulings — a quarter of the whole section — are the same ANK 20220507 boilerplate: "If it burns an ally as a result, this counts as a Ⓓ action burning an ally (eg. Trophies, {Predator's Transformation})". R0246/R0399/R0431/R0875/R0960/R1659 are near-verbatim identical; R0020 ("a directed action burning an ally"), R0974 ("counts as a Ⓓ action burning the ally", LSJ 20080608) and R1753 ("if she steals a life from an ally and it burns") are the same principle with cosmetic variation. Under the no-exhaustive-card-lists rule this is ONE principle with three examples, not nine.

**Recommendation:** State once as prose: an ally burned as a consequence of a directed action counts as burned by that action, for trophies and equivalent triggers. Keep three "e.g." cards spanning the mechanism variants — R0246 {Brick Laying} (damage), R0431 {Cryptic Mission} (used on an ally), R1753 {Succubus} (life steal). Drop R0020, R0399, R0875, R0960, R0974, R1659 to C; they add no distinct fact.

*Rulings (9):* R0020, R0246, R0399, R0431, R0875, R0960, R0974, R1659, R1753

### [high] duplicate-template

Eight rulings carry two verbatim-repeated attribution templates. Template 1 ([COMBAT] "If a minion is burned in combat, his opponent his always considered to have burned him", LSJ 20090922) appears identically on R0538 {Draught of the Soul}, R1689 {Soul Stealing}, R1787 {Taking the Skin: Minion}. Template 2 ([ACTION MODIFIER] "burned because of a referendum or as a side-effect of the action ... does not count as the acting minion burning him") appears identically on R0539, R1690, R1788 — the same three cards. R0188 {Blood Brother Ambush} and R0395 {Conscripted Statue} are the same rule restated from the burning card's side ("the vampire playing it is not considered having burned a minion ... but the opponent is"). All eight are three cards' worth of copy-paste, and five of the six template rows are labelled PRIMARY, so each will arrive at the drafter as its own candidate paragraph.

**Recommendation:** Collapse to two prose statements — combat burns are always attributed to the opponent; referendum and side-effect burns are not attributed to the acting minion — sourced from R1788 (the richest copy: four references and the fullest example list) and R1787. Keep R0188 as the one "e.g." for the played-card-does-not-attribute variant. Demote R0538, R0539, R1689, R1690, R0395 to C as redundant copies.

*Rulings (8):* R0538, R1689, R1787, R0539, R1690, R1788, R0188, R0395

### [medium] duplicate-template

R0008 {Abandoning the Flesh} and R0095 {Ashes to Ashes} are the identical sentence with the identical reference: "Cannot be played when burned as a result of a Blood Hunt referendum. [LSJ 20070417]". Both are filed PRIMARY in 5.4, so the drafter receives the same rule twice as two independent principles.

**Recommendation:** Keep one (R0008) as the example; drop R0095 to C. Also worth a cross-reference note: the operative fact is a property of the blood hunt burn, so 3.7.8 should own the rule and 5.4 should cite it rather than restate it.

*Rulings (2):* R0008, R0095

### [medium] duplicate-template

R1265 {Orgy of Blood} ("Can be used by a vampire going to torpor or about to be burned") and R1477 {Revelation of Wrath} ("Can be played by a vampire going to torpor. Can be played by a vampire who is about to burn") are the same template. Both are secondary rows, so this is minor, but they are also arguably not 5.4's rule at all — the principle is that a minion on its way out of play is still in play and may still act, which is a timing/state fact.

**Recommendation:** Keep one (R1477, which states both halves explicitly) as a single "e.g." if 5.4 wants a sentence on the still-in-play window; drop the other. Confirm the primary owner is 5.3 or chapter 2 and let 5.4 cross-reference rather than restate.

*Rulings (2):* R1265, R1477

### [medium] over-absorbed

Two rows teach nothing that transfers. R1214 {Nar-Sheptha}.1 — "If burned in combat, her effect ceases immediately and the acting minion returns to normal for the rest of the combat" — is entirely about Nar-Sheptha's own ongoing effect; the only generalisable residue ("burning the source ends its ongoing effect") is 2.5 duration/persistence, not 5.4, and it is not stated here. R0552 {Dual Form}.5 — "If one of the pair leaves the ready region, the other is burned. That burning of the other won't cause the first to burn" — is a pure reading of Dual Form's paired-card mechanic and affects no other card, failing the transfer test outright.

**Recommendation:** R1214 (PRIMARY, E) should be C with 2.5 as the near-miss code. R0552 is a secondary row so 5.4 is not its owner, but it should not appear in this extract either — it is card interpretation, not a burn principle.

*Rulings (2):* R1214, R0552

### [low] role-error

R0168 {Blessed Resilience}.1 — "Only a controlled vampire can be burned from play. Uncontrolled and contested vampires do not qualify" — is labelled E, but it names no card behaviour and states a general precondition on burning outright. It is the natural opening sentence of the section, and the only row here that defines what is eligible to be burned at all.

**Recommendation:** Relabel P. Low stakes per the contract, but flagged because a drafter scanning for prose material would otherwise pass over the section's most load-bearing general statement.

*Rulings (1):* R0168

### [low] missing-topic

Two of the four topics named in 5.4's scope line have no ruling. (a) "trophies/bounties on burns" — trophies appear only as the trigger mentioned inside the R0020-family boilerplate, and bounties appear nowhere; there is no ruling on how a trophy is awarded, who receives it, or what qualifies. (b) "burn vs. removal of minions" — nothing addresses removal from game as distinct from burning; R0979 {Khazar's Diary} touches destination (ash heap) only. There is also no ruling on burning a torpid vampire, a routine judge question, though 5.3 may own it.

**Recommendation:** Flag to the drafter that these subsections will be thin or unsupported. Before writing, check whether trophy/bounty rulings were routed to 3.7.8 (diablerie & blood hunt) and whether removal-vs-burn went to 1.10; if so, 5.4 should cross-reference. If neither extract has them, the corpus genuinely lacks them and the scope line is over-claimed.

## 5.5

### [high] duplicate-template

The "an ally has life, not blood, he cannot pay" principle recurs seven times across six chunks, twice as literally identical text with identical references. R0864 (Hide the Heart.3) and R1843 (Tenebrous Form.2) are word-for-word the same ruling — "An ally has life, not blood, he cannot pay. [LSJ 20050216] [ANK 20190701]" — and both are labelled P PRIMARY. R0368 (allies "cannot use the provided action as they have no blood to pay with"), R2207 ("Allies have no blood, they cannot take directed actions against him"), R1815/R2074 ("Cannot be played/used against an ally" — blood-drinking cards), and R0985 (blood-cost allies kept by paying 0 pool) are the same rule seen from different card angles.

**Recommendation:** Keep ONE P statement of the rule — allies have life, not blood, so they cannot pay blood costs and are not valid targets for effects that take blood from the target. Cite R0864/R1843 as the joint authority, and use at most three "e.g." cards: one blood-cost-to-play case ({Hide the Heart} or {Tenebrous Form}, not both), one target-side case ({Taste of Vitae}), and R0985 as the cost-substitution wrinkle. The remaining four stay in the database.

*Rulings (7):* R0864, R1843, R0368, R2207, R1815, R2074, R0985

### [high] over-absorbed

Nine of 51 rows in 5.5 are {Shadow Court Satyr} (R1602, R1603, R1605-R1611). Four of those teach nothing beyond the Satyr's own unique "put a combat card on him and play it as if from hand" mechanic. R1605: "If the card combat card is moved, the Satyr cannot use it as if played from your hand anymore, even if it was moved on him" — the subject is the Satyr's printed mechanism. R1607: "The card put on him is not into play." R1606: "The card on him cannot be canceled as it is played when he plays it as if from your hand." R1603 ("Can choose to use any single discipline effect of a split discipline card, each time he uses it") is about the Satyr's fixed single discipline level, not about allies. None of these change how you rule on any other card — they fail the transfer test.

**Recommendation:** Demote R1605 (currently E PRIMARY), R1606, R1607 and R1603 to C with a note that they are {Shadow Court Satyr} mechanism interpretations. Retain R1602 (single-discipline allies cannot use multi-discipline effects), R1608 (an ally acting "as a vampire" may play any card, not only discipline cards — a REVERSAL worth recording), R1609 (cannot commit diablerie), R1610/R1611 (torpor-inflicting effects burn the ally instead) as the "as a vampire" sub-topic. Even then, use at most one or two Satyr rows as the "e.g." and let G00011/G00018 carry the prose.

*Rulings (4):* R1605, R1606, R1607, R1603

### [medium] over-absorbed

Three consecutive rows are all {FBI Special Affairs Division} trigger-condition interpretations: does the card fire when the ally is saved by {Left for Dead} (R0659), when the ally is the acting minion (R0660), when the ally burns by himself at end of combat (R0661). All three are E PRIMARY. These read the trigger clause of one card; they do not change how a judge rules on any other card, and 5.5's principle (what allies are) is not what they teach.

**Recommendation:** Demote R0659 and R0661 to C ({FBI Special Affairs Division} trigger scope; fails transfer). R0660 is the only one with a general residue — an ally can be the acting minion in combat — and if kept, it belongs as a cross-reference under "allies acting", not as three parallel examples of one card's trigger.

*Rulings (3):* R0659, R0660, R0661

### [medium] duplicate-template

R1221 ({Nephandus}) and R1271 ({Ossian}) are identical text with the identical reference: "His life total can exceed his starting life capacity (it is the case for all allies). [ANK 20171109]". Both are P PRIMARY. The ruling itself parenthesises the generalisation, so it is one principle recorded twice on two cards.

**Recommendation:** Keep one as the P statement of "an ally's life is not capped by its starting life" and cite both card entries in the single footnote. Do not give the document two examples of a rule that states itself.

*Rulings (2):* R1221, R1271

### [medium] duplicate-template

R0343 ({Charming Lobby}.12: "If played by an ally 'as a vampire', they can call a referendum listed on a political action card in hand") and R0845 ({Herald of Topheth}.1: "Can use {Charming Lobby} to call a referendum 'as a vampire'") are the same ruling, same reference [RTR 20020501], recorded once on the card and once on the ally. They are mirror images, not two examples.

**Recommendation:** Keep R0343 as the general statement (an ally acting "as a vampire" may call a referendum from a political action card in hand) with {Herald of Topheth} named as the e.g. Drop R0845 as a separate entry; one footnote covers both records.

*Rulings (2):* R0343, R0845

### [medium] missing-topic

5.5's scope line claims "ally limits", but no ruling in the membership addresses a limit on allies — nothing on per-methuselah ally caps, unique allies, or contested allies. The closest row is R1998 ({War Ghoul} requires another ally or retainer in play), which is a recruitment precondition, not a limit. The drafter will have a scope-line heading with no material behind it.

**Recommendation:** Either confirm the corpus genuinely has no ally-limit rulings (in which case strike "ally limits" from the 5.5 scope line at Phase 4.5, or fold it into 1.13 contests) or run a targeted grep before drafting. Flagging it now so the drafter does not invent a sub-section from an empty extract.

### [low] misfiled

R2174 ({Carolina Vález}.1: "She is immune to unlock damage from allies like {Abyssal Hunter} and {Wendell Delburton}") is filed here as secondary, but the principle is about a vampire's immunity to a damage type, not about anything allies are or do — the allies are only the incidental source. It teaches nothing that would land in a section about life vs. blood or acting "as a vampire".

**Recommendation:** Drop from 5.5's extract. 4.5 (prevention & immunity) or 5.2 (lock/unlock) should own it as PRIMARY. Low severity because it is a secondary row and costs the drafter only a shrug.

*Rulings (1):* R2174

### [low] recoverable-C

R2423 ({Sébastien Goulet}.1: "His ability works on allies recruited in a non-standard way (eg. {Piper})") is E PRIMARY but reads the trigger wording of one vampire's ability. The general residue — "recruited" covers non-standard recruitment routes — is already carried better by R1999 ({War Ghoul}.2: "regardless of how it did come into play"), which states it as a rule.

**Recommendation:** Demote to C, or keep only as the second e.g. under R1999's principle. Do not give it its own prose beat.

*Rulings (1):* R2423

## 5.6

### [medium] missing-topic

5.6's scope line claims three sub-topics (employ/bearer, retainers striking or damaging, retainers surviving bearer) but only 'striking or damaging' has any membership. Not one ruling in the section addresses what happens to a retainer when its bearer leaves play, goes to torpor, is burned, or changes controller, and nothing addresses the employ/bearer attachment relationship itself (R2127 mentions employing only as an Angelo restriction). Retainer life totals, retainer counters, and retainer-as-cards-on-a-host are likewise absent — those are presumably sitting in 1.12 and 3.7.4, but 5.6 as delivered cannot cross-reference what it never saw.

**Recommendation:** Before drafting, sweep 1.12 (cards on cards / host leaves play), 3.7.4 (employ retainer action) and 5.4 (burning minions) for rulings on retainer survival and bearer attachment, and either pull them into 5.6's extract or accept that 5.6 becomes a short combat-focused section that cross-references those sections for everything else. If nothing turns up, 5.6 may be better folded as a sub-topic than kept as its own heading.

### [medium] thin-section

Half the PRIMARY membership is a single card. R0759, R0760 and R0761 are all {Ghoul Retainer} filed as P, and R0957 ({Jar of Skin Eaters}) is an example of R0759's rule. Three P rows on one card invites the drafter to state the section's principles in that card's vocabulary ('the Ghoul is not the bearer', 'the Ghoul uses weapon as if making the strike') rather than as a rule about retainers.

**Recommendation:** Draft from the two general-rule entries (R2551 retainer damage is environmental with the retainer as source; R2564 a striking retainer gains no additional strikes from its employer) as the prose, then state the weapon-use rule once — a retainer wielding equipment is not its bearer, and its use of the weapon resolves all side effects but is not a strike — citing {Ghoul Retainer} plus {Jar of Skin Eaters} (R0957) as the e.g. pair. R0761 (ammo cards, {Magazine}, {Scattershot}) is the narrowest of the three and should be demoted to E or dropped from the prose entirely.

*Rulings (4):* R0759, R0760, R0761, R0957

### [medium] over-absorbed

R1712 ({Spiritual Protector}.2) is 'Does not restrict the ability of retainers to use equipment.' — a negative statement about the scope of one card's restriction. It teaches nothing about retainers; it teaches what {Spiritual Protector} does not do. It fails the transfer test: no other card's adjudication changes because of it.

**Recommendation:** Reclassify to C with a note ('scope of {Spiritual Protector}'s equipment restriction; fails transfer — nearest 5.6'). If the drafter wants the underlying fact that retainers may use equipment, that is already carried by R0759/R0760/R0957 and does not need this row.

*Rulings (1):* R1712

### [low] over-absorbed

R1617 ({Shadow Twin}.1) is '[OBT] has no additional effect on a retainer.' — a statement about which part of one card's superior text can apply, not a rule about retainers. As written it is unusable as an 'e.g.' because the reader cannot tell what the additional effect was without the card in hand.

**Recommendation:** Reclassify to C with a note ('scope of {Shadow Twin}'s superior effect; fails transfer'). Lower confidence than R1712 — if a drafter can extract a general 'discipline-keyed strike bonuses do not apply when the target is a retainer' rule from it, keep it as E, but it should not survive as PRIMARY on its own.

*Rulings (1):* R1617

### [low] misfiled

Two secondary rows contribute nothing to 5.6's principle. R2127 ({Angelo}.3, 'cannot attempt an action to employ a retainer, nor strike to steal a retainer') is a restriction belonging to Angelo, correctly owned by 3.7.4 or 5.7; it appears in 5.6 only because the word 'retainer' occurs. R0563 ({Earthshock}.1, 'can be used at long range to target a retainer, even if their employer has flight') is a Flight interaction owned by 5.7, with the retainer incidental.

**Recommendation:** Drop both from 5.6's extract; they add reading cost without adding a sentence the drafter could write. Conservative call — both are secondary and the cost of leaving them is a few tokens, so treat this as cleanup rather than a correction. R0497 and R0277, by contrast, are legitimate secondary cross-references and should stay: R0497 carries the transferable point that an action targeting a retainer does not target the minion, and R0277 the point that an effect sourced from a retainer outlives the retainer's burning.

*Rulings (2):* R2127, R0563

## 5.7

### [high] duplicate-template

Four rulings are the same template: a Gargoyle slave locks to enter combat INSTEAD of the blocked/blocking minion, and effects keyed to the original minion behave accordingly. R1183 (a Momentary Delay may still be used by the substituting slave), R1599 (Shadow Boxing cannot be used BY the substituting slave), R1669 (the opponent cannot use Sniper Rifle to set range) and R1257 (Obedience cannot be played because the slave took his place) all restate one rule: the substitute is the combatant, and only effects whose conditions the substitute independently meets apply. Three of them even share the same ruling window (ANK 20200114/20200115). This is also the section's seam: it is a combat/actor-substitution mechanic that shares only the word 'slave' with the rest of 5.7.

**Recommendation:** State once as a single principle in 5.7 with a cross-reference to 3.10 (changing the acting minion) and 4.1. Keep R1669 and R1599 as the 'e.g.' pair — they show the two polarities (an opponent effect blocked, and an effect the substitute cannot itself use). Leave R1183 and R1257 in the database, or carry R1257 only if 3.10 wants it as PRIMARY.

*Rulings (4):* R1183, R1599, R1669, R1257

### [high] duplicate-template

Four identical-text pairs survived the fan-out because no classifier could see both copies. R1938 (Unleash Hell's Fury.8) and R1967 (Veneficti.1) are the SAME sentence with the SAME reference [LSJ 20091203]: 'The burn option can be used if all your infernal vampires are in torpor.' R0266 (Cadet.1) and R1209 (Mustajib.1) are the same sentence with the same reference [LSJ 20070322]: 'The target vampire is not Black Hand if he is not Sabbat.' R0892 (Illusions of the Kindred.9) and R1685 (Soul Gem of Etrius.5) are the same ruling [LSJ 20060323] on an Imbued pulled from the crypt by an effect. R1205 (Murder of Crows.1) is the card copy of general entry R2554 (G00019 Animal.1), same two references, correctly labelled E/P per the contract but adding nothing beyond it.

**Recommendation:** Collapse each pair to one entry. Keep R1938 OR R1967 (either; one 'e.g.'), keep R0266 OR R1209, keep R1685 (the richer of the pair — it states the uncontrolled-region vs incapacitated-region outcome), and drop R1205 in favour of the general entry R2554. Net: four rulings out of the extract, no principle lost.

*Rulings (8):* R1938, R1967, R0266, R1209, R0892, R1685, R1205, R2554

### [medium] misfiled

Two PRIMARY rows teach a principle another section explicitly owns. R1292 ({Patagia: Flaps Allowing Limited Flight}.1, 'Can only be used when the vampire its on is in combat himself') is verbatim the principle 1.5's scope line was widened to claim ('abilities whose use requires the bearer to be *personally* a participant'); Flight is incidental vocabulary. R0978 ({Khazar's Diary}.2, 'Wraiths minions can act the turn they are put into play') is an exception to the acting-the-turn-recruited restriction, which is 3.7.4's scope line; 'Wraith' is not even in 5.7's class list.

**Recommendation:** Re-PRIMARY R1292 to 1.5 (5.7 secondary at most). Re-PRIMARY R0978 to 3.7.4, with 5.5 secondary. Neither leaves the corpus.

*Rulings (2):* R1292, R0978

### [medium] over-absorbed

Two PRIMARY/E rows are pure one-card text interpretation. R0425 ({Cry Wolf}.3, 'If you manage to unlock it during the unlock phase, it does not need to burn') is a timing quirk of one card's own self-burn clause — it fails transfer, since no other card's ruling changes. R0080 ({Armor of Terra}.1, 'Can be used by a non-slave Gargoyle') just reads that card's requirement as not demanding slave status; a judge reading the card already knows it.

**Recommendation:** Recoverable-C both. If R0080 is kept at all, it belongs under 1.6 (requirements) as a near-miss C with a note, not as a 5.7 example.

*Rulings (2):* R0425, R0080

### [low] duplicate-template

R0389 ({Concordance}.1, 'Once played, it continues to apply even if the vampire stops being Infernal') and R0423 ({Cry Wolf}.1, 'His ability continues to apply fully if he is not a werewolf') are the same principle on two different class traits: an effect that required the trait at the time it applied survives the trait lapsing. Both are correctly secondary here, so the cost is low, but a drafter reading 5.7 alone would be tempted to write the rule twice — once under Infernal, once under werewolves.

**Recommendation:** Treat as one principle owned by 5.9 (trait-change precedence) or 2.5 (persistence); 5.7 should cross-reference rather than restate it, citing at most one of the two.

*Rulings (2):* R0389, R0423

### [low] misfiled

Two secondary rows land in 5.7 on vocabulary rather than principle. R0271 ({Call the Wild Hunt}.2) is about discarding X animal CARDS from hand and not using replacement draws as further discards — a discard/replacement mechanic (6.9 / 1.9); nothing about animals as a minion class. R0014 ({Abomination}.1, 'Can be played by burning a werewolf that has been recruited the same turn') is about the same-turn-recruitment restriction not covering being burned as a cost — 3.7.4 — with 'werewolf' incidental.

**Recommendation:** Conservative call since both are secondary: drop the 5.7 code from R0271 outright (it gains 5.7 nothing), and keep R0014's 5.7 code only if the drafter wants a werewolf example, since its real home is 3.7.4 alongside R0978.

*Rulings (2):* R0271, R0014

### [low] scope-drift

5.7 ('special minion classes & traits') and 5.9 ('traits & trait-change precedence') overlap on the section's two best prose anchors. R2479 ({Vidal Jarbeaux}.4) defines what IS a vampire trait (titles, Red List, Flight) versus what is not (mortal, unlocked, older) — that is a general trait taxonomy, 5.9's foundation. R2547 (G00012 Black Hand) is half class definition ('not a title') and half precedence ('not lost if the vampire changes sect'). Left as-is, both sections will state the trait taxonomy.

**Recommendation:** No reclassification needed, but flag for the drafter: 5.7 states the class list and what each class means; 5.9 owns what a trait IS and what happens when one changes. R2479 should appear in both extracts with 5.9 writing the definition and 5.7 citing it.

*Rulings (2):* R2479, R2547

### [low] thin-section

Of the twelve classes 5.7's scope line names, Red List has ZERO rulings in the section (only a passing mention inside R2479's trait list), and True Brujah (R2576), Scarce (R2578), Sterile (R0268) and werewolves have exactly one usable ruling each. The section's real mass is Imbued, Gargoyle slaves, Infernal, and ally subtypes. Nothing here covers Imbued Convictions or Virtues either, beyond R1356 mentioning their loss.

**Recommendation:** Tells the drafter where 5.7 will be thin: write the well-evidenced sub-topics as prose and reduce the singletons to a single list-style paragraph rather than a subsection each. Do not open a Red List heading with no ruling behind it.

*Rulings (4):* R2479, R2576, R2578, R0268

## 5.8

### [high] duplicate-template

Forty of the 93 rows (43% of the section) are one byte-identical sentence with one identical reference: "Keeps his/her title and votes if he/she changes sects. [LSJ 20010714]", recorded on 40 different crypt cards. This is a single principle — a title printed on the crypt card is intrinsic to the vampire and survives a sect change, unlike a title granted by a library card — and the extract as it stands will hand the drafter forty copies of it.

**Recommendation:** Collapse to one principle entry plus at most two "e.g." cards. Keep R2152 ({The Baron} — an Anarch-title case, and the card that also anchors the Baron/name rulings) and R2272 ({Kemintiri}, whose adjacent rulings R2274/R2277 already develop the same requirement machinery); optionally R2108 ({Ambrogino Giovanni}) as an independent case. Reclassify the remaining ~37 to C with the note "duplicate of the LSJ 20010714 printed-title-survives-sect-change template; kept in the rulings database". The drafter should state the rule against the crypt-card-title wording template and contrast it with R2497 ({Vlad Tepes}.10) where a title gained from a library card goes dormant instead.

*Rulings (40):* R2108, R2113, R2129, R2140, R2149, R2150, R2152, R2172, R2179, R2186, R2210, R2228, R2246, R2253, R2265, R2269, R2272, R2278, R2287, R2289, R2313, R2317, R2318, R2336, R2345, R2354, R2362, R2364, R2365, R2405, R2409, R2421, R2429, R2441, R2442, R2459, R2460, R2469, R2513, R2518

### [high] duplicate-template

A second template recurs twelve times: "If the target changes sect to a sect inappropriate for his title, he loses its benefit until his sect is appropriate. He immediately yields the title if it is contested or he receives a new one. [LSJ 20060904]" — seven verbatim sect copies (R0669, R0742, R0780, R0943, R1280, R1437, R2043), two clan-substituted copies (R0355, R0484), and two rewordings for the specific sect-removal cards (R0641, R0645). Every one is labelled P PRIMARY, so twelve rulings each claim to state the same principle.

**Recommendation:** Keep R1240 ({No Confidence}.2) as the P — it is the only row that actually defines the operative term ("'loses the benefit' means he gets no vote, is not considered titled, and yields the title immediately if it would contest") and it carries the rulebook anchor [RBK 6-vampire-sects]. Keep R0355 or R0484 as the one "e.g." that shows the rule is trait-general rather than sect-specific (clan substituted for sect — this is also the row that ties 5.8 to 5.9), and R0641 ({Fall of the Camarilla}) as the mass-effect case. Send the other nine to C as template duplicates.

*Rulings (12):* R0669, R0742, R0780, R0943, R1280, R1437, R2043, R0355, R0484, R0641, R0645, R1240

### [medium] duplicate-template

"A card requiring a Baron (eg. {Open War}) is a card requiring an Anarch" appears five times with the same reference pair [LSJ 20050128] [LSJ 20080603]: once as the general rule entry R2572 (G00037|Require a Baron) and four times as card copies (R0419, R0750, R1341, R2414), all four labelled P PRIMARY. Per the contract's general-rule-entry rule the card copies should be E at most, and four of them are three too many.

**Recommendation:** Keep R2572 as the P (it is the general entry and is currently only a secondary row here — promote it to the section's prose source), one card copy as the "e.g.", and R0367 ({Club Illusion}.1, "does not make the action an action requiring an Anarch") as the negative boundary case. The remaining three card copies go to C.

*Rulings (6):* R2572, R0419, R0750, R1341, R2414, R0367

### [medium] duplicate-template

The "vampire who meets any title requirement" cluster ({Vlad Tepes}, {Vidal Jarbeaux}, {Kemintiri}) duplicates three distinct sub-principles two-to-three times each, split across cards so no classifier could see it: (a) meeting a title requirement implies the underlying sect — R2480, R2491, R2277; (b) meeting a title requirement for a political action does not grant that title's votes for the referendum — R2481, R2493 (verbatim identical, same reference [ANK 20231221]); (c) a title requirement can be met even after the sect ceases to exist — R2482, R2494, R2274 (all three verbatim, same references [LSJ 20050124] [ANK 20230503]); plus (d) the controller chooses how the requirement is met — R2480, R2492.

**Recommendation:** Consolidate on one exemplar card. R2480 ({Vidal Jarbeaux}.5) is the densest single row — it carries (a), (c)'s companion, (d), and the once-each constraint — so keep it as P and R2481 as the votes rule, with {Vlad Tepes} rows dropped to C as the same rulings recorded on a second card. Keep R2274 or R2482 (not both) for the defunct-sect point. R2495 is a usable single "e.g." of the whole cluster; the rest are duplicates.

*Rulings (10):* R2480, R2491, R2277, R2481, R2493, R2482, R2494, R2274, R2492, R2495

### [medium] scope-drift

The membership contains two adjacent but distinguishable topics: (1) titles as a minion state — acquiring, contesting, yielding, dormancy, title-granted votes/capacity/actions, which is 5.8's stated scope; and (2) how card *requirements* read titles — Baron implies Anarch, a title requirement implies its sect, requirements survive the sect's destruction, a vampire named "Baron" is not a Baron. Cluster (2) is roughly 15 rows and its principle is a requirements principle, which 1.6 owns; 5.8's scope line never claims it. The seam is clean, so this is a drafting risk rather than a misfile: without a decision the same material gets written twice or falls between the two sections.

**Recommendation:** Decide the boundary before drafting rather than at assembly. Recommended split: 1.6 states how requirements read titles and sects (with the Baron/Anarch template and the meets-any-title cards as its examples), and 5.8 cross-references it in one line per the "cross-reference rather than repeat" rule. If the drafter prefers to keep it in 5.8, then 1.6's extract needs the cross-reference instead — but not both.

*Rulings (15):* R2572, R0419, R0750, R1341, R2414, R0367, R2480, R2491, R2482, R2494, R2274, R2495, R2569, R2153, R2154

### [medium] misfiled

R0891 ({Illusions of the Kindred}.8, "If the illusionary vampire has a title, they can use the votes even if there is another instance of the title in play") is filed E PRIMARY in 5.8, but the principle it teaches is that a placeholder/representation does not contest — which the taxonomy assigns explicitly to 1.4 ("no contest for placeholders"). Filed here, it reads as a title-contest exception and risks the drafter stating a title-specific rule for what is a representation rule.

**Recommendation:** Move PRIMARY to 1.4, keep 5.8 as secondary so the titles drafter still sees it when writing the contest paragraph.

*Rulings (1):* R0891

### [low] over-absorbed

R1322 ({Political Seizure}.1, "If you yield the Political Seizure, the location it was contesting does not come into play under your control") is E PRIMARY but fails both C tests. It is a statement about one card's own contest behaviour; generalised it becomes "if you yield a contest you do not gain the contested card", which any judge fluent in the rulebook already knows, and it transfers to no other card. It is also a card-contest ruling rather than a title ruling.

**Recommendation:** Reclassify C with a note naming 1.13 as the near miss; 5.8 already has R2183 and R2577 covering title contests with more content.

*Rulings (1):* R1322

### [low] duplicate-template

Three small verbatim pairs remain. R2239 ({Horatio Ballard}) and R2346 ({Maxwell}) are the same sentence with the same reference [LSJ 20030202] (an ability granting a title cannot be used once the vampire is off-sect). R2153 ({The Baron}) and R2154 ({Baron Dieudonne}) are both "Cannot play cards requiring a Baron. [PIB 20151116]" — the same name-is-not-a-title point. R2220 ({Gerald Windham}, "gives him votes but no title") and R2515 ({Xeper}, "Is not titled; if he gets a title his additional votes are added") state the same votes-are-not-a-title principle.

**Recommendation:** Keep one of each pair as the "e.g.": R2239, R2153, and R2515 (the richest of the three, since it also covers stacking with a later-acquired title). Send R2346, R2154 and R2220 to C as duplicates. Note the second pair is the mirror of the Baron/Anarch template in finding 3 and should be drafted next to it.

*Rulings (6):* R2239, R2346, R2153, R2154, R2220, R2515

### [low] role-error

Two cross-chunk role inconsistencies on identical text, in violation of golden rule 5. R2513 ({Xaviar}) and R2518 ({Zayyat}) are labelled E while the other 38 byte-identical copies of the same sentence are P. Separately, the four Baron/Anarch card copies (R0419, R0750, R1341, R2414) are P while the general rule entry stating the same rule (R2572) sits here only as a secondary row — the contract says the general entry is the P and the card copies are E.

**Recommendation:** Low stakes on its own and mostly dissolved by the consolidation in findings 1 and 3; fix as a side effect of those. Worth recording only as evidence that the fan-out did drift on identical text, which is a signal for other sections carrying the same templates.

*Rulings (6):* R2513, R2518, R0419, R0750, R1341, R2414

### [low] missing-topic

Two sub-topics named in 5.8's scope line have essentially no rulings. Acquisition: nothing here explains how a title is gained or that title cards grant a title distinct from a printed one — R2497 (dormancy) and R2268 ({Karsh}, "Imperator is a unique Camarilla title worth 3 votes, the same as the one granted by {Imperator}") are the only touches. Contest mechanics: only R2183 (cost is vampire blood, not pool), R2268 (card-granted and printed titles are the same title for contest) and R2577 (contested title-providing card is turned face down, its action unusable). Nothing covers whether city-keyed titles (Prince of A vs Prince of B) contest, who yields and when, or what a yielded title leaves behind.

**Recommendation:** Flag to the drafter that acquisition and contest-resolution will have to be written from the rulebook with [RBK] footnotes rather than from rulings, and that the corpus supports the sect/clan-appropriateness and requirements material far more heavily than the section's own headline topics. Not evidence for a taxonomy change — the rulings simply do not exist.

*Rulings (4):* R2183, R2268, R2497, R2577

## 5.9

### [high] duplicate-template

Six rulings are one verbatim boilerplate spread across six cards in different chunks: "Is a change of the actual sect. A temporary effect overriding the sect has precedence and if it does, this card burns (eg. {Writ of Acceptance})." R0668 (Field Training), R0741 (Galaric's Legacy), R0779 (Go Anarch), R1436 (Red Question) are word-identical; R0942 (Into the Fire) and R1279 (Out of the Frying Pan) are the same template minus the burn clause. All six carry the same single reference [LSJ 20100811], which confirms they are one ruling recorded six times, not six rulings. All six are labelled P, so the drafter receives six copies of the same principle statement.

**Recommendation:** State the principle once — a permanent sect change is subordinate to any temporary override in effect, and a card whose only function was that permanent change burns when overridden — and cite two cards: {Field Training} (burn clause present) plus {Into the Fire} (override without burn, showing the burn is card-specific, not part of the rule). Mark R0741, R0779, R1436, R1279 as absorbed duplicates that stay in the database.

*Rulings (6):* R0668, R0741, R0779, R1436, R0942, R1279

### [high] duplicate-template

{Fall of the Camarilla} and {Fall of the Sabbat} are mirror cards and their rulings are word-for-word identical with only the sect name swapped, across three pairs: R0639/R0643 (.1, "Cards that change a vampire's sect to X can still be played, but he becomes Independent"), R0640/R0644 (.2, the temporary-override-precedence statement), R0642/R0646 (.4, "An impersonator (eg. {Vlad Tepes}) can still play cards requiring X or an X title"). Each pair shares identical reference sets ([LSJ 20040519]; [LSJ 20080510][LSJ 20100811][ANK 20190619]; [LSJ 20050124][ANK 20230503]). Six rows carrying three facts.

**Recommendation:** Keep only the Camarilla side (R0639, R0640, R0642) and note in the prose that {Fall of the Sabbat} is the mirror case. Drop R0643, R0644, R0646 from the extract. Note also that R0640 overlaps heavily with R2042 ({Writ of Acceptance}.2), which states the same most-recent-override-governs rule and shares two of its three references — R2042 is the cleaner P for the general rule because it also covers the case where the underlying trait changes beneath a live override; R0640 then adds only the Fall-specific redirect-to-Independent wrinkle.

*Rulings (6):* R0639, R0643, R0640, R0644, R0642, R0646

### [medium] over-absorbed

Two rows are pure one-card trait statements that teach no precedence principle and are the section's clearest over-absorption. R0847 ({Herald of Topheth}.3) is the entire ruling text "Cannot play Anarch cards." — a bare statement of one minion's sect, with no effect changing anything and nothing that transfers to another card. R0800 ({Grey Thorne}.2) is "Is not Anarch (eg. does not benefit from {Anarch Manifesto, An})." — again a statement of one card's own trait; whatever generality it has ([RBK allies], allies have no sect) is a claim about allies, not about trait-change precedence.

**Recommendation:** Reclassify R0847 as C (fails transfer: affects only {Herald of Topheth}; and non-obvious fails too — it is a restatement of the card's own sect). Reclassify R0800 as C with 5.5 as the near-miss code, or file it to 5.5 (Allies) if the drafter wants an "allies and sect" line there; it does not belong in 5.9 either way.

*Rulings (2):* R0847, R0800

### [medium] duplicate-template

Three rulings are one template on three cards, all citing the same single reference [ANK 20190416]: R1160 ({Ministry}.1) and R1373 ({Protection Racket}.1) are word-identical ("The additional intercept is gained or lost if the acting vampire changes sect during the action (eg. with {The Red Question} or {Mask of a Thousand Faces})"), and R2454 ({Teresita, The Godmother}.1) is the same sentence with the subject changed. This is the section's best sub-topic — a continuous effect keyed to a trait re-evaluates when the trait changes mid-action — and it is the one place the membership risks reading as three separate facts.

**Recommendation:** State it once as the re-evaluation principle and cite one or two cards, e.g. {Ministry} and {Teresita, The Godmother} (the second shows the effect belongs to a different minion than the one whose trait changed, which is the non-obvious half). Drop R1373 as a duplicate.

*Rulings (3):* R1160, R1373, R2454

### [medium] duplicate-template

{Clan Impersonation} and {Derange} produce two more mirror pairs. R0356/R0487 are word-identical including the same typo ("takes precedenced") and the same reference [LSJ 20021209] — the clan-precedence rule recorded twice. R0353/R0483 are the same negative fact recorded twice ("Does not change the sect" / "Does not change the sect of the target"), both [RTR 20201130]. All four are P.

**Recommendation:** Keep R0487 ({Derange}.7) as the clan instance — the taxonomy's own §5.9 rationale already names it as the deciding clan evidence — and keep one of R0353/R0483 for the separate and genuinely useful point that clan and sect are independent traits (an effect writing one does not write the other). Drop the other two as duplicates.

*Rulings (4):* R0356, R0487, R0353, R0483

### [medium] missing-topic

After deduplication the section rests on roughly 12 distinct facts, and the trait axis is overwhelmingly sect: one clan pair (R0487) and three secondary acting-minion rows are the only non-sect evidence. The taxonomy scoped 5.9 to traits generally precisely so the drafter would not write a sect-specific rule — but the extract as it stands supplies almost nothing else to generalize from. Two concrete sub-topics have no ruling at all: (a) what happens when two temporary overrides are live and the EARLIER one lapses first — R0640 and R2042 only cover a single override lapsing back to the underlying trait, and R2453 ({Tegyrius, Vizier}.2) covers a continuous override surviving an underlying change, but nothing covers unwinding a stack; (b) traits other than sect, clan and acting-minion (Black Hand, Red List, Scarce, title-derived traits) being written by an effect and read by another.

**Recommendation:** Flag to the drafter that the general statement of 5.9 must be written from sect evidence and explicitly generalized, with {Derange}/{Clan Impersonation} and {Deep Song}/{Nar-Sheptha} carried as the proof that the rule is trait-agnostic. Mark the stacked-override-lapse case with ⚠ REVIEW rather than inventing an answer, and cross-reference 5.7 and 5.8 for the traits 5.9 has no rulings on.

*Rulings (3):* R0640, R2042, R2453

### [low] duplicate-template

The three acting-minion rows are all `secondary` (correctly — 3.10 owns them), but R0467 ({Deep Song}.2) and R1215 ({Nar-Sheptha}.2) are the two halves of a single ruling [ANK 20211022] recorded on both cards, and they state the same fact from opposite ends. R1343 ({Powerbase: Savannah}.1) is a distinct point (an effect reading the acting-minion designation respects prior changes to it).

**Recommendation:** Keep one of R0467/R1215 as the 5.9 cross-reference showing the later-governs rule holds on a third trait, and keep R1343 as the reads-the-trait half. This is a low-severity cleanup only — as secondary rows they cost the drafter little, and their value here is precisely that they prove the rule is not sect-specific.

*Rulings (3):* R0467, R1215, R1343

### [low] recoverable-C

R1438 ({The Red Question}.3, "Does not make the action an action that 'makes this vampire anarch' (eg. {CrimethInc.} cannot be played)") is labelled P but is close to a two-card interaction. Its general content — a card whose effect writes a trait is not thereby an action described as writing that trait — is real but narrow, and the only situation it is known to affect is the {Red Question}/{CrimethInc.} pairing.

**Recommendation:** Keep it, but as E rather than P, subordinate to the trait-vs-requirement line already carried by R0642 ({Vlad Tepes} impersonator). If the drafter finds no second instance, demote to C rather than giving it a sentence of its own — one worked example of "reads the trait vs. names the action" is enough.

*Rulings (1):* R1438

## 6.1

### [high] duplicate-template

Four rows are the byte-identical sentence "Can only be played by the controller of the acting minion." carrying the identical reference [LSJ 19990425] (R0567 Echo of Harmonies, R0587 Empowering the Puppet King, R0851 Hidden Lurker, R2056 Zapaderin), three of them PRIMARY. That is 22% of the section's membership spent on one sentence, against a style rule of one principle plus one to three "e.g." cards. R2078 (Shard, London: "they are also played by the Methuselah") and R1580 (Set's Call: "The acting vampire's controller is the one who makes the choices") state the same underlying rule from adjacent angles.

**Recommendation:** Draft one principle — a minion-card effect is played by the controller of the acting minion, who also makes any choices the effect calls for — sourced from R1580 as the P. Keep at most two of the four identical rows as the "e.g." (R0851 {Hidden Lurker} and R0567 {Echo of Harmonies} are the clearest); demote R0587 and R2056 to database-only. Cite R2078 only if the drafter wants the cost-reduction wrinkle.

*Rulings (6):* R0567, R0587, R0851, R2056, R2078, R1580

### [medium] duplicate-template

R1012 ({Lay Low}) and R0118 ({Banishment}) are the same ruling restated — both trace to [ANK 20200408-2] and both say the vampire goes to its last permanent controller's uncontrolled region (which may not be the owner), is removed from the game if that controller is ousted, and survives the owner's oust. R1012 is PRIMARY/P, R0118 is secondary/P; the section needs only one.

**Recommendation:** Keep R1012 as the P stating the rule (its wording is the fuller of the two, covering both the oust-of-controller and oust-of-owner branches). Drop R0118 from 6.1's extract, or carry it only as a one-word "e.g. {Banishment}" alongside; do not let the drafter write the rule twice.

*Rulings (2):* R1012, R0118

### [medium] thin-section

After deduplication 6.1 holds roughly eleven distinct teachings, and the scope line's second clause — "control defines actor/payer" — has no ruling covering the *payer* at all. Nothing in the membership addresses who pays a cost when actor and card-controller differ, and nothing addresses the ownership of the library/hand a card is drawn to or discarded from (only the ash-heap direction is covered, by R2099/R0979/R1737). The section also contains no G000xx general-rule entry, so every statement must be induced from card rulings.

**Recommendation:** Flag for the drafter that the payer half of 6.1 will have to be written from the rulebook and cross-referenced to 1.7 rather than from rulings, and that the zone-ownership half rests entirely on ash-heap examples. If a later pass finds payer rulings sitting in 1.7 or 6.5, route copies here as secondary.

*Rulings (3):* R1580, R2099, R1012

### [low] over-absorbed

R1409 ({The Rack}) is card-specific: "If the target is stolen, the new controller chooses if the vampires gains blood during The Rack controllers unlock phase" turns entirely on The Rack's own optional blood-gain and its own controller's unlock phase. Its only transferable content — a stolen card's choices belong to the new controller — is already carried, more generally, by R1737 ({Storage Annex}).

**Recommendation:** Treat as C for 6.1's purposes (it is only `secondary` here, so the cost is small). If the general point is wanted, state it once from R1737 and cross-reference 6.3.

*Rulings (1):* R1409

## 6.2

### [high] duplicate-template

The 'ousted Methuselah ends the control relationship' rule occupies 5 of 32 rows across two verbatim-identical wordings. R2536 (G00001|Temporary control.1) and R0031 (Ailing Spirit.1) are the SAME sentence word for word ('If one is ousted while having temporary control of a minion, the minion is removed from the game. [LSJ 20081105]'), and R1156 (Mind Rape.4), R1708 (Spirit Marionette.7) and R1833 (Temptation.2) are the SAME sentence word for word ('The stolen minion is removed from the game when he should return to a Methuselah who has been ousted. [ANK 20181110]'). All five are the one principle seen from its two ends: temporary controller ousted, and permanent controller ousted. Four of the five are labelled P, so on current labels a drafter is handed the same principle stated four times.

**Recommendation:** Draft ONE principle from R2536 (the G00001 general entry, correctly P) covering both directions, with at most one card 'e.g.' per direction — R0031 {Ailing Spirit} for the temporary-controller side and R1833 {Temptation} for the permanent-controller side. Demote R0031 to E (the contract's 'general entry P, card copy E' rule). Drop R1156 and R1708 to C/database: they add no wording variation whatsoever. Note that R2381 ({Parmenides}: 'If the owner is ousted before Parmenides comes back, the predator keeps control of him indefinitely') and R1012 ({Lay Low}.5) are the genuinely non-redundant members of this cluster — they state the CONTRARY outcome (control survives the oust) and are what makes the principle non-trivial; keep both and draft the rule as the pair of outcomes, not as one repeated line.

*Rulings (5):* R2536, R0031, R1156, R1708, R1833

### [medium] duplicate-template

R1157 (Mind Rape.5) and R1834 (Temptation.3) are the same sentence verbatim: 'The stolen minion returns to his previous controller even if he is in torpor (but stays in torpor). [LSJ 20010119]' — same ruling reference, same wording, two cards, two chunks.

**Recommendation:** Keep one row as the 'e.g.' — R1834 {Temptation}, since {Temptation} already anchors several other 6.2 principles and concentrating the examples on it reduces the card count in the drafted prose. Send R1157 to C/database.

*Rulings (2):* R1157, R1834

### [medium] duplicate-template

R1966 (Velvet Tongue.1) and R2419 (Sarrasine.2) are the same sentence verbatim: 'Putting a corruption counter on a minion does not give you an opportunity to steal it. [ANK 20200925] [ANK 20211105]' — the corruption-counter wording template, labelled E and P respectively for the same text.

**Recommendation:** Keep one (R2419 {Sarrasine} or R1966 {Velvet Tongue}, either works) as a single 'e.g.' on the point that the control change happens only when the card's own trigger fires, not when a counter is placed. Send the other to C. Also settle the P/E split: identical text should not carry different roles, though this is low-stakes on its own.

*Rulings (2):* R1966, R2419

### [medium] misfiled

R2528 ({Theo Bell}.1, secondary) — 'Can be merged with {Theo Bell (ADV)} if you get to control one (eg. {Graverobbing})' — teaches a merge-eligibility rule, not a taking-control rule. Its subject is 5.1 (vampires: merge/advanced); the control clause is only the incidental route by which the ADV copy arrives, and {Graverobbing} pulls a card from an ash heap rather than taking control of a minion in play.

**Recommendation:** Drop from 6.2. 5.1 owns merge; 1.11 (ash heap, owner vs controller for retrieval) is the secondary if one is wanted. Nothing in 6.2's scope line (temporary control, steals mid-action/combat, controller ousted) claims it, and leaving it here invites the drafter to open a merge sub-topic 6.2 cannot support on one ruling.

*Rulings (1):* R2528

### [low] misfiled

R0242 ({Brainwash}.1, secondary) is about which movements a transfer prohibition blocks and about a vampire reaching capacity and becoming controlled out of the uncontrolled region. That is influence-phase/uncontrolled-region material (6.7); the phrase 'can become controlled' is the uncontrolled-to-controlled transition, not one Methuselah taking control of another's minion, which is what 6.2 owns.

**Recommendation:** Drop from 6.2, file under 6.7 (influence phase & crypt). If any part deserves a 6.2 cross-reference it is only 'Brainwash stays on it (if {Banishment} is used, the effect resumes)', which is 6.4 (leaving & re-entering play) rather than 6.2.

*Rulings (1):* R0242

### [low] misfiled

R2000 ({War Ghoul}.3) is PRIMARY here, but the transferable content is 3.4's principle stated almost verbatim: 'The action will have no effect but is still successful if unblocked and must then be paid.' The steal is only the occasion; the rule being taught is success-without-effect and that cost is still owed.

**Recommendation:** Move the primary to 3.4 (resolution, success & effect) and keep 6.2 as secondary for the narrow point that a target may use an ability in response to a steal attempt and thereby empty it. As it stands 6.2 would draft a success/effect rule that 3.4 also drafts, against the cross-reference-rather-than-repeat style rule.

*Rulings (1):* R2000

### [low] missing-topic

Nothing in the membership answers the first question a judge actually gets about a steal: what state the minion arrives in and what comes with it. There is no ruling on whether the minion arrives locked or unlocked, whether the new controller may act with it immediately (R1154 {Mind Rape}.2 fixes only WHEN the taking may happen, not what may then be done), and none on whether attached equipment, retainers and blood/counters travel with it. R1409 and R1520 touch the adjacent question of whose choice/whose turn an in-play effect keys to after a control change, but not the arrival state itself.

**Recommendation:** Flag for the drafter that 6.2 will be thin here and that the gap is real rather than a classification loss. The attachments half is probably owned by 6.3 (taking control of cards in play, 'where equipment/locations go') and should be handled by cross-reference; the lock-state and may-it-act-now half has no owner and should either be stated from the base rules with no footnote or marked '⚠ REVIEW'.

*Rulings (3):* R1154, R1409, R1520

## 6.3

### [high] duplicate-template

Twelve rulings — 48% of the entire section — are byte-identical boilerplate: "Requirements do not apply when taking control of a card already in play. [TOM 19960226-1]", all from the same 1996 ruling, and all twelve were labelled P/PRIMARY. Twelve independent chunks each saw one copy and each promoted it to a principle-stating row; no chunk could see it was the same sentence twelve times. This is one sentence of prose, not twelve.

**Recommendation:** Collapse to one P plus at most three "e.g." cards; demote the other eight to C (or drop them from the extract). Suggested keepers, chosen for span of card type and mechanism: {Spirit Marionette} (R1702, [OBE] minion-control template), {New Management} (R1232, in-play card control, and it anchors R1233/R0518 below), {Far Mastery} (R0651). The remaining nine (R0085, R0237, R0516, R0739, R1400, R1469, R1473, R1579, R1884) carry no information the kept three do not. Note that no G000xx general entry exists for this rule, so one card copy must carry the P.

*Rulings (12):* R0085, R0237, R0516, R0651, R0739, R1232, R1400, R1469, R1473, R1579, R1702, R1884

### [medium] duplicate-template

Three rulings state the same locquipment rule from the same source [RTR 19960112]: R2582 (G00047|Locquipments.1) is the general-rule entry — "May be put on any minion if the controller changes. If the new controller has no minions, it is burned" — and R0517 ({Disputed Territory}) and R0528 ({Dominate Kine}) are verbatim card copies of its first clause. The general entry is filed as `secondary` while both card copies are PRIMARY, inverting the contract's rule that a general entry is the prose and the card copy the example.

**Recommendation:** Make R2582 the PRIMARY P for this principle in 6.3 — it is the only row carrying the burn-if-no-minions half of the rule, which both card copies drop. Keep one card copy as the "e.g." (R0517 {Disputed Territory}, since R0518 already extends it) and demote R0528 {Dominate Kine} to C as a pure duplicate.

*Rulings (3):* R2582, R0517, R0528

### [medium] other

Two rulings in this section give opposite answers to "what happens to an attached card's chosen target when the card changes controller". R1101 ({Malkavian Time Auction}.3) is stated as a general rule: "If an equipment, retainer or location on a minion changes controller, the new controller chooses a new target they control for them. [LSJ 20030606]". R0914 ({Incriminating Videotape}.1) says the opposite for a card whose text names a minion: "The target is chosen when the card is played, and does not change. If stolen, the chosen minion is unable to block the new possessor." A drafter reading only this extract will write a contradictory sentence. The reconciliation is probably that R1101 governs the bearer (which minion the card sits on) while R0914 governs a target written into the card's own effect — but neither row says so, and no !TENSION tag links them.

**Recommendation:** Adjudicate before drafting and state the distinction explicitly in the section: bearer re-designation follows the new controller, an effect-target fixed at play does not. If the distinction does not hold on inspection, one of the two is wrong and should be flagged !WORDING rather than drafted around. R0914 is `secondary` here and legitimately primary elsewhere (3.1 announcement/targets), so keep it as a cross-reference either way.

*Rulings (2):* R0914, R1101

### [low] role-error

R1737 ({Storage Annex}.1) is labelled P but is written entirely as a card-specific narrative — "If it is stolen, the card on it goes with it and the new controller will be able to take it in hand. The card is returned to the owner's ash heap or library if it would be moved to an ash heap or library." It is recoverable, not C: it carries two general rules (a hosted card follows its host on a control change; a card leaving play goes to its OWNER's zones regardless of who controls it). But as a P it invites the drafter to state a Storage-Annex-shaped principle, and its second clause is 6.1 (owner vs. controller) material that 6.3 does not own.

**Recommendation:** Demote to E under the hosted-card-follows-host principle, and add 6.1 as a second code so the owner-vs-controller clause reaches the section that owns it. Pair it with R1588 ({Shackles of Enkidu}.5) and R2206 ({Ethan Locke}.2), which teach the same follows-the-host rule for a minion-attached card and a stolen master card respectively — one principle, those three as the e.g. pool, not three separate statements.

*Rulings (1):* R1737

### [low] misfiled

R2161 ({Black Cat}.2) is about a minion whose presence modifies the pool cost of equipment moving on and off her — "if that equipment is transferred to another minion, then it regains its normal pool value... if a piece of equipment moves onto her, its effective pool cost is lowered by 1." The principle is cost recalculation on equipment movement, not control of a card in play; movement between minions is not necessarily a control change at all.

**Recommendation:** 1.7 (costs & payment — when a cost modifier attaches and detaches) should own it, with 3.7.3 as the alternate. It is filed here as `secondary` so this is a low-cost drop; if 1.7 already holds it as PRIMARY, remove it from 6.3's extract rather than leaving a cost ruling in a control section.

*Rulings (1):* R2161

### [low] missing-topic

Nothing in the 25 rows addresses the duration or reversion of control over a card in play. Every ruling here treats the transfer as permanent; there is no ruling on what happens when a temporary control effect lapses (does the card return to the original controller, and in what state — counters, lock status, bearer?), nor on whether taking control of a card in play triggers any "when played" effect on it. The section will be thin exactly where 6.2 has a rich temporary-control story for minions and 6.3 has none for cards.

**Recommendation:** Flag for the drafter that the reversion sub-topic has no ruling support in this extract, and cross-reference 6.2 (temporary control of minions) and 6.4 (what cards remember) rather than inventing a rule. If Phase 4 wants it covered, it needs a targeted search of the database outside this section's membership.

## 6.4

### [high] duplicate-template

"Effects targeting a card resume if and when it returns to play" is one ruling filed on three cards. R0493 (Descent into Darkness.6) and R1408 (The Rack.4) carry the identical reference pair [LSJ 20010809-2] [LSJ 20010809-3] — they are literally the same ruling recorded twice, and both are labelled PRIMARY. R1010 (Lay Low.3) states the same rule scoped to "for the rest of the game" effects; R1407 is The Rack's near-duplicate on the not-controlled case.

**Recommendation:** Draft one principle — ongoing effects pointed at a card are suspended, not lost, while it is out of play, and resume on its return — citing {The Rack} as the worked example (it is the card the rulings were actually issued against) plus at most one of {Descent into Darkness}/{Lay Low}. Demote R1010 and R1407 to database-only; keep R0493 as a secondary cross-reference from the Descent block rather than a PRIMARY.

*Rulings (4):* R0493, R1408, R1010, R1407

### [high] duplicate-template

The "contract" cluster is four rows carrying only two distinct rulings. R0159 ({The Black Throne}.1) and R1374 ({Provision of the Silsila}.1) are verbatim identical — same sentence, same typo ("is burned of if"), same reference [PIB 20150512]. R0160 and R1365 ({Priority Contract}.1) are likewise one ruling, both [ANK 20180129-2]. Three of the four are PRIMARY or E-PRIMARY, so the drafter receives them as four separate examples.

**Recommendation:** Collapse to a single principle: an effect keyed to a card leaving the ready region fires regardless of the route out — burn, or the controller being ousted — and fires even if the triggering card itself is burned in the same event. Cite {The Black Throne} and {Priority Contract} as the two e.g. cards; drop R1374 and R1365 to database-only.

*Rulings (4):* R0159, R1374, R0160, R1365

### [medium] duplicate-template

R0492 (Descent into Darkness.5) and R1009 (Lay Low.2) are word-for-word identical — "will remember all effects that had been applied to him, just as contested vampires do. This includes gained or lost titles." — and share the reference [RTR 20000501]. Both are P PRIMARY, so both will present themselves to the drafter as prose-source for the same sentence.

**Recommendation:** Keep one as the prose statement (R0492 is the fuller citation, [RTR 20000501] [LSJ 20060908]) and let {Lay Low} be a bare "e.g." mention alongside {Descent into Darkness}. This is the section's headline rule; it needs one sentence, not two.

*Rulings (2):* R0492, R1009

### [medium] over-absorbed

R0129 ({Bauble}.3) is P PRIMARY but is a pure one-card interpretation: "Still cannot be burned if the target equipment was burned and somehow returned to play." The "still cannot be burned" clause reads only against Bauble's own printed restriction, and "somehow returned to play" is hedged enough that it fixes no general rule. It also fails transfer — no other card's adjudication changes. Worse, as PRIMARY P it invites the drafter to state a persistence rule that contradicts R1329 and R0377, which establish that a card passing out of play through the ash heap returns as a new object.

**Recommendation:** Reclassify to C (nearest 6.4), or at minimum demote from P to E and from PRIMARY to secondary so it cannot seed a principle. If retained, it needs a !TENSION flag against the new-object rule in R1329/R0377.

*Rulings (1):* R0129

### [medium] thin-section

"Permanents not replaced" is named as half of 6.4's scope line, but R2543 (G00008|Permanent not replaced.1, "Is not replaced until the condition is met, even if it is burned") is the only ruling in the section touching it — and it is a general entry with no card behind it. Every other row in the membership is about leaving and re-entering play.

**Recommendation:** Flag to the drafter that this sub-topic will be a single unillustrated sentence. Either pull the replacement-timing rulings from 1.9 as cross-references for at least one worked example, or move the sub-topic wholly into 1.9 (which already owns "do not replace until") and narrow 6.4's scope line to leaving and re-entering play.

*Rulings (1):* R2543

### [low] duplicate-template

"Merging is not entering play" appears three times: R0302 ({Chameleon}.1) and R1033 ({Legendary Vampire}.1) are word-for-word identical, and R1131 ({Masquerade Enforcement}.1, "does not affect merging") is the same rule from the other direction. All three are secondary, so the cost is low, but the drafter will see three rows for one clause.

**Recommendation:** One clause in the entering-play discussion — merging an advanced vampire onto its base is not entering play — with a single e.g. card. Note that R1131's natural primary is 5.1 (merge), so it need not appear in 6.4's extract at all.

*Rulings (3):* R0302, R1033, R1131

### [low] duplicate-template

R1135 ({The Meddling of Semsith}.2) and R1155 ({Mind Rape}.3) are the same template — an in-play effect card is removed and its effect cancelled when the Methuselah who played it is ousted. Both are correctly secondary here (their principle is 6.2/6.5 territory), so this is low cost, but they should not both survive into 6.4's prose.

**Recommendation:** Handle in 6.2/6.5 and cross-reference from 6.4 with one card, not two. R1155 additionally carries a rules-reversal note ("rulings before 2008-11-19 have been reversed") that makes it the better single citation if one is kept.

*Rulings (2):* R1135, R1155

### [low] over-absorbed

Two rows are pure single-card mechanics that teach nothing transferable. R2098 ({Agaitas}.2) is entirely about Agaitas's own prey-library mechanism — "you cannot draw in your prey's library until you control Agaitas anew" adjudicates no other card. R0490 (Descent into Darkness.3, "If played by an ally, the ally can never come back") turns on Descent's specific return condition being unavailable to allies.

**Recommendation:** Both are already secondary, so the harm is bounded — but neither should reach the page. Reclassify to C, or explicitly mark them database-only in the extract so the drafter does not mine them for examples.

*Rulings (2):* R2098, R0490

## 6.5

### [high] duplicate-template

Six sets of verbatim-identical ruling text, each set carrying identical reference IDs, arrived in 6.5 from different chunks and were each labelled independently. This is one principle per set, not 13 entries.

**Recommendation:** Collapse each set to one keeper plus at most one 'e.g.' partner. (1) R0149 {Bima}.3 and R0846 {Herald of Topheth}.2 are word-for-word identical, both [LSJ 20080512] ('If it uses its last life to pay for an action... the oust is resolved before resolving effects triggered by the fact that the Bima/Herald burns') — keep R0846 (already PRIMARY), drop R0149. (2) R0059 {Ancient Influence}.1 and R1451 {Reins of Power}.1 are identical, both [ANK 20180813], and both merely restate R1321 {Poison Pill}.2 from the other side — keep R1321 as the P, keep ONE of R0059/R1451 as the 'e.g.', drop the other. (3) R0160 {The Black Throne}.2 and R1365 {Priority Contract}.1 are the same ruling, both [ANK 20180129-2] ('contract effect can be used when a minion leaves the ready region because his controller is ousted') — keep R1365. (4) R1458 {Repo Man}.1 and R1953 {Vast Wealth}.3 are identical, both [RTR 19941109] [RTR 20010710] — keep one; both are secondary here and primarily 1.7 material anyway. (5) R0617 {The Eternals of Sirius}.1 and R1977 {Villein}.1 are the same ruling, both [LSJ 20020620] ('pay the cost at the same time you gain pool, you do not get ousted in between') — keep R1977 as the P, and keep R0618 as its genuine contrast case (must be able to pay to play). (6) R1156 {Mind Rape}.4 and R1833 {Temptation}.2 are identical, both [ANK 20181110] — keep one.

*Rulings (13):* R0149, R0846, R0059, R1451, R1321, R0160, R1365, R1458, R1953, R0617, R1977, R1156, R1833

### [medium] duplicate-template

Three verbatim copies of the same vote-title ability timing ruling ([LSJ 20090115-2]) on Armin Brenner, Donald Cargill and Lutz von Hohenzollern, filed separately.

**Recommendation:** R2141, R2189 and R2315 are the identical sentence 'His ability is applied after the referendum effects are applied, including any oust and pool gained from it' with the same single reference. Keep ONE as the template statement (R2315 {Lutz von Hohenzollern} is the canonical bearer). The other two rows carry no new information. Do keep R2190 and R2316 — they are the two genuine variants (ability still applies when the PREDATOR is ousted; ability does not apply when the bearer's OWN controller is ousted) and together they make the distinction the drafter needs. Note R2316 is flagged as a reversal of previous rulings, so it should be drafted as current law with the reversal not mentioned.

*Rulings (5):* R2141, R2189, R2315, R2190, R2316

### [medium] over-absorbed

The Life Boon cluster is four PRIMARY rows plus a cross-reference, all interpreting one card's private victory-point-reservation mechanic — the exact shape the taxonomy already rejected for Monocle of Clarity and Extremis Boon.

**Recommendation:** Demote R1037, R1039 and R1040 to C. R1037 ('the various Boons reserve a series of victory points, rather than competing with each other for a single victory point') fails transfer — no other card reserves victory points, so it changes no ruling elsewhere. R1039 ('The Boon is not burned until a total of one victory point has been awarded') is pure card-text bookkeeping. R1040 keys entirely on Life Boon's award clause. Keep R1038 only if the drafter can restate its general half — that a Methuselah may be required to pay more pool than she holds, and that the shortfall is a real quantity rather than being capped at her pool — which is a genuine 6.5 pool-accounting point; otherwise it is C too. R1289 {Parity Shift}.2 is a legitimate secondary cross-reference and can stay, but it should not be the peg for a Life Boon paragraph.

*Rulings (5):* R1037, R1039, R1040, R1038, R1289

### [medium] over-absorbed

Five rows on The Rising, of which three are conditional readings of that card's own trigger clause rather than general pool/oust principles.

**Recommendation:** Keep R1493 ('Anything that would increase the pool amount is considered gaining pool') — it is one of the section's two anchor definitions, paired with R1320. Keep R1496 ('When ousting their prey, Methuselahs decide if they gain the VP before or after gaining the pool'), which is a real and transferable oust-sequencing rule. Demote R1494 and R1495 to C or collapse them into a single 'e.g.' under R1496: both turn on The Rising's own 'if they have the edge or a VP beforehand' condition, and the pair exists only to distinguish {Kindred Spirits} from {The unnamed} for that one card. R1497 ({Off Kilter}'s additional pool cannot be gained if you do not have a VP) is a third instance of the same conditional and should not be a separate row.

*Rulings (5):* R1494, R1495, R1497, R1493, R1496

### [medium] misfiled

A six-row family on 'what happens to a card or minion in play when its controller is ousted' sits at the seam with 6.4 and 6.2, and R1155 is PRIMARY here for a fact 6.2's scope line explicitly claims.

**Recommendation:** This is one template — a card controlled by an ousted Methuselah is REMOVED FROM THE GAME, not burned — with several bearers. Treat it as one principle in 6.5 with a cross-reference to 6.4, and let 6.4/6.2 own the mechanics. Specifically: R1155 {Mind Rape}.3 should not be PRIMARY 6.5; 6.2 names 'controller ousted' in its scope and Mind Rape is a control-stealing card, so 6.2 (or 6.4) should own it with 6.5 as secondary. R1156 and R1833 (stolen minion returning to an ousted Methuselah) are correctly secondary here and belong to 6.2 as PRIMARY. R1012 {Lay Low}.5 is correctly secondary. For the 6.5 paragraph itself keep at most R0347 {Charnas the Imp} (the cleanest statement of removed-not-burned, which matters because burn triggers do not fire) and R1135 {The Meddling of Semsith} (effect cancelled as well as card removed) as the two 'e.g.' cards. Note R1621 {Shatter the Gate}.1 pulls the other way — counters stay active after the acting Methuselah is ousted — and is worth keeping precisely as the boundary case; the drafter should reconcile it explicitly rather than state the removal rule unqualified.

*Rulings (6):* R1155, R1135, R0347, R1012, R1156, R1833

### [medium] missing-topic

Withdrawal and victory-point award mechanics — both named in 6.5's scope line — are effectively unattested in the membership.

**Recommendation:** There is no ruling in this extract on the withdrawal rule itself: when a Methuselah may withdraw, what she scores, how withdrawal interacts with the ousting chain. Withdrawal appears only obliquely in R1848 {Thanks for the Donation} (yielding a contest) and as a Poison Pill side effect in R0059/R1451. Likewise, victory-point mechanics are represented almost entirely by the Life Boon cluster, which this review recommends cutting — after that, only R1496 and R2550 remain, and nothing covers game end, timeout scoring, or the basic VP award. The drafter should expect to write both paragraphs from the rulebook with few or no footnotable rulings, and should be warned rather than left to discover it. R2550 (general entry G00015, multiple simultaneous ousts: everyone whose prey is ousted scores a VP even if ousted themselves, but only survivors take the 6 pool) is the single strongest VP ruling present and should anchor that paragraph.

*Rulings (4):* R1848, R0059, R1451, R1037

### [low] over-absorbed

Four marginal rows whose general content is thin enough that they will cost the drafter more to read than to use.

**Recommendation:** Candidates for C, or at least for not being cited. R1844 {Tension in the Ranks}.1 ('Pool is not paid when an imbued is incapacitated') is an imbued-specific exception to one card's pool-payment clause — 5.7 territory, and it fails transfer. R2229 {Hector Trelane}.1 turns on that vampire's own ability plus a bloodhunt burn; its home is 5.4/3.7.8 and it teaches 6.5 nothing. R1525 {Sabbat Threat}.1 is a one-card ordering trick ('gain pool from the Edge before burning it'). R2242 {Hrothulf}.1 ('Only burns the Edge if the action is successful') is a reading of that card's action text and is arguably a 3.4 success-vs-effect reminder a fluent judge already knows. None of these is severe; flagging them so the drafter does not mistake volume for coverage.

*Rulings (4):* R1844, R2229, R1525, R2242

## 6.6

### [medium] missing-topic

6.6's scope claims four sub-topics (master phase actions, trifles, out-of-turn masters, masters on minions) but the membership only reaches three of them obliquely and is very thin: 11 rows, 6 PRIMARY, and the trifle material is entirely about what happens when a trifle is CANCELED (R1760, R2006, R2007). There is no ruling establishing the master phase action economy itself — one master card per master phase, a trifle granting an additional action, what does or does not consume an action — and none on WHEN an out-of-turn master may be played (the window / what counts as being played 'against' a given master phase); only the per-phase COUNT limit is covered (R1377, R2443, R2008). Masters-on-minions is represented by two rulings, both on the same narrow point (the bearer's controller chooses whether to use the effect: R0620, R2566), with nothing on where such cards go, what happens when the host leaves play, or who pays their upkeep (the last presumably owned by 1.12, but the drafter will find the seam empty).

**Recommendation:** Warn the drafter that 6.6 must be written substantially from the rulebook baseline rather than from rulings: the section's spine (master phase action count, trifle bonus, out-of-turn window) has no ruling support in the corpus, and the rulings only supply the edge cases hanging off that spine. If a Phase 4.5 review is looking for sections that may not survive as their own heading, 6.6 belongs on that list alongside 6.8 — though unlike 6.8 it has enough distinct edge cases (cancellation accounting, per-phase vs per-action ability periodicity, bearer's choice) to justify keeping it.

*Rulings (4):* R2007, R2006, R1760, R1377

### [low] duplicate-template

R1760 ({Sudden Reversal}.2) and R2006 ({Wash}.1) are word-for-word identical — 'If used to cancel a Trifle, the target does not get an extra Master Phase Action from the canceled Trifle' — and share the same [LSJ 20090126] [RBK trifle] references. They are the same template on two master-cancel cards. R2008 ({Wash}.3) is the complementary half of the same principle in the opposite direction: canceling an out-of-turn master still spends that Methuselah's out-of-turn slot.

**Recommendation:** Write one principle, not two entries: canceling a master card does not unwind the master phase accounting — a canceled trifle's extra action never arrives, and a canceled out-of-turn master still consumes the once-per-master-phase allowance. Cite {Wash} as the single 'e.g.' (it carries all three facets: R2006, R2007, R2008) and fold {Sudden Reversal} (R1760) into the same footnote rather than giving it its own sentence. Both are `secondary` rows so no reclassification is needed; this is a drafting instruction.

*Rulings (3):* R1760, R2006, R2008

### [low] role-error

R2443 ({Synesios}.2) is marked P but does not state a principle — it applies the existing one-out-of-turn-master-per-master-phase limit to a single card's ability ('His ability do not allow his owner to play more than one Master: Out of Turn between two master phases'). R1377 ({Proxy Kissed}.2) is also P and carries the same limit, but earns it: it adds genuinely transferable timing content (a master played during your influence phase counts against your NEXT master phase). Two P rows on the same limit risks the drafter stating it twice.

**Recommendation:** Treat R1377 as the P for the out-of-turn limit and its timing, and demote R2443 to E (or drop it to the example pool unused). R2443 is close to C on the non-obviousness test — a card ability that lets you play an out-of-turn master obviously does not raise the per-phase cap — but it is defensible as an 'ability grants access, not an extra allowance' example, so E rather than C.

*Rulings (2):* R2443, R1377

### [low] misfiled

R2566 (G00031 'Master on vampire who can use it': the vampire's controller chooses to use the effect or not) and R0620 ({Ex Nihilo}.1: the controller chooses between paying the blood or burning the vampire) are correctly in 6.6 under its 'masters on minions' scope line, but their actual principle — an effect on a card you control is optional unless the wording makes it mandatory, and the BEARER's controller is the one who chooses — transfers far beyond master cards and is 1.1 material (mandatory vs optional effects; reading card text), with the who-chooses half touching 6.1. As a general rule entry, R2566 is the prose seed for that principle and it will be lost to 1.1 if it only ever appears in the 6.6 extract.

**Recommendation:** Add 1.1 as a co-code on R2566 and R0620 so the 1.1 drafter sees them; keep 6.6 as primary. R0620 should also be E rather than P — it is the named-card instance of R2566's rule, not a separate principle.

*Rulings (2):* R2566, R0620

## 6.7

### [medium] duplicate-template

The [RTR 20180303] batch is one template: 'a vampire/card influenced out mid-phase — does its ability apply to the ongoing influence phase?'. R2122 (Angela Preston) and R2384 (Paul "Sixofswords29" Moreton) are near-verbatim identical ('When he/she is influenced out, her/his ability can be used during the ongoing influence phase') and carry the same single reference. R2248 (Ingrid Rossler) is the negative pole of the same template (bonus transfers do NOT apply), and R0591 (Ennoia's Theater) is the same window question on an in-play card. Four PRIMARY rows for what is one rule with a positive and a negative case.

**Recommendation:** State one principle — an ability that becomes available mid-influence-phase can be used for the remainder of that phase, but an effect modifying the *number of transfers* is fixed for the phase and does not retroactively apply. Keep R2122 (or R2384, not both) as the positive e.g. and R2248 as the contrasting e.g.; drop the third to the database. R0591 can be folded in as the 'any moment during the phase' clause or kept as a third e.g. at most.

*Rulings (4):* R2122, R2384, R2248, R0591

### [medium] duplicate-template

Four rulings all answer 'may this card be played / this ability used when the uncontrolled region does not hold a qualifying vampire?'. R1923 (Undue Influence, 'cannot be played with no vampire in the uncontrolled region') and R2291 (Lázár Dobrescu, 'cannot use his special ability if his controller has no vampires in her uncontrolled region') are the same rule stated twice on two cards. R2083 (Break the Bonds, 'there must be an uncontrolled vampire') is a third instance, its only distinct content being 'chosen upon declaration' — which is 3.1 material and where it is already filed as secondary. R1674 (Social Ladder) is the informative counter-case: the card may be played with no *older* vampire available, because that clause describes the effect and not a play requirement.

**Recommendation:** One principle tied to the wording template: a card requiring a target in the uncontrolled region cannot be played with the region empty, but a clause that merely describes what the effect does to the region is not a requirement. Keep R1923 and R1674 as the contrasting pair. R2291 and R2083 add nothing to 6.7 (R2083 stays in 3.1).

*Rulings (4):* R1923, R2291, R2083, R1674

### [medium] scope-drift

The 'what a vampire keeps across the uncontrolled region' cluster is split inconsistently between 6.7 and 6.4. R0115 (Banishment.2 — capacity-changing cards do not apply while uncontrolled, extra blood does not drain off) and R1852 (Thicker than Blood.1 — keeps cards and blood) are PRIMARY here, while R0116 (Banishment.3 — remembers all effects, titles, continuous effects) and R0117 (Banishment.4 — comes back unlocked, and that is not unlocking) are only secondary, i.e. owned by 6.4/5.2. These are the same principle and, as filed, two drafters will each receive half of it and both will write it.

**Recommendation:** Decide ownership once. Recommended: 6.4 owns memory across leaving and re-entering play generally; 6.7 owns the uncontrolled region as a zone and the influence-phase window, and cross-references. That means moving R0115 and R1852 to 6.4-PRIMARY with 6.7 secondary. If the opposite call is made, R0116 must become 6.7-PRIMARY. Either way, all six should sit on one side with the other as cross-reference.

*Rulings (6):* R0115, R1852, R0116, R0117, R1011, R0118

### [medium] missing-topic

The section is titled 'Influence phase & crypt' but the crypt half has no rulings at all, and the influence phase's own mechanics are unrepresented. Nothing here covers: the transfer allowance itself (how many transfers, the early-turn allowance, limits on transfers to one vampire); influencing non-vampire crypt cards; crypt replacement after a vampire is influenced out; or what happens to transfers/uncontrolled vampires when a Methuselah is ousted. Every ruling in the membership is either a bonus/forgone transfer (R0591, R2248, R2295) or an uncontrolled-region state question.

**Recommendation:** Flag to the drafter that the transfer and crypt mechanics must be written from the rulebook with [RBK] footnotes rather than from rulings, since the corpus supplies none. If nothing substantive can be written for the crypt-as-zone half, consider whether 6.7's scope line should shed 'crypt' at Phase 4.5 (1.9 already claims the empty-crypt case).

### [low] duplicate-template

R0118 (Banishment.5) and R1011 (Lay Low.4) state exactly the same rule from the same source [RTR 20000501]: a vampire leaving play under a temporary control effect goes to its *last permanent controller's* uncontrolled region. R1011 is already secondary so the cost is small, but both are labelled P and a drafter reading the extract sees the principle asserted twice.

**Recommendation:** Keep R0118 as the P statement (it also carries the ousting consequence, 'removed from the game when the controller is ousted'). Cite R1011 only if a second e.g. is wanted; otherwise it stays in the database.

*Rulings (2):* R0118, R1011

### [low] recoverable-C

R1049 (Loner.1) is PRIMARY/E but is a reading of one card's own condition: 'Only considers the minions controlled during the influence phase. It does not care if minions you no longer control acted this turn.' The wording 'It does not care if minions you no longer control acted this turn' is an interpretation of Loner's specific text, not a transferable rule about the influence phase — it changes how you rule on no other card.

**Recommendation:** Reclassify C with 6.7 as the near-miss code, unless the drafter wants it as the single e.g. for a general 'conditions are evaluated against the game state at the moment the card checks them' statement — but that principle is not 6.7's and no other ruling here supports it.

*Rulings (1):* R1049

### [low] recoverable-C

R1376 (Proxy Kissed.1) is PRIMARY/E on the strength of a parenthetical: 'Can be played on a vampire who already has a Proxy Kissed (and was moved to uncontrolled and re-influenced).' The rule being stated is about one card's own once-per-vampire restriction; the uncontrolled round-trip is incidental colour and the general point it gestures at is already covered by R0116/R1852.

**Recommendation:** Reclassify C with 6.7 as near-miss, or at most demote to a non-cited example. Do not let it occupy an 'e.g.' slot that R0115/R1852 fill better.

*Rulings (1):* R1376

## 6.9

### [high] duplicate-template

The "cards that are not replaced count against the hand size" rule is recorded three times in near-identical wording, twice with the identical reference pair. R0544 (Dreams of the Sphinx.3) is "Cards that are not replaced count against the hand size. [ANK 20180318]"; R1137 (Meddling of Semsith.4) is the same sentence plus a parenthetical, with [ANK 20180318] [ANK 20231229]; R2227 (Hagar Stone.2) states the same rule from the other side ("the 'do not replace' effect effectively reduces the hand size") with the same [ANK 20180318] [ANK 20231229] pair. All three are labelled P PRIMARY, so the drafter receives three copies of one principle presented as three principles. R2420 (Sascha Vykos) is the same rule again as a one-card restatement ("When using his ability to draw, discard afterwards").

**Recommendation:** Keep R0544 as the P that states the rule (it is the taxonomy's own deciding ruling for 6.9's existence). Demote R1137 to E — its {Raptor} parenthetical is the one thing the set adds, showing successive non-replacements accumulating — and keep R2227 as the second e.g. because it states the converse framing (a do-not-replace effect as a de facto hand-size reduction). Drop R2420 to C: it is Sascha Vykos's own draw ability with no transfer beyond the rule R0544 already states.

*Rulings (4):* R0544, R1137, R2227, R2420

### [medium] duplicate-template

The default-visibility sub-topic is six rulings expressing two rules. R1957 (Vaticination.1) "You do not get to see the card drawn as replacement. [PIB 20121031]" and R2426 (Sergei Voshkov.1) "When using his ability, you do not get to see the card drawn as replacement. [ANK 20211020] [PIB 20121031]" are the same sentence resting on the same ruling reference; R1956 (Vast Wealth.6) "You do not show cards when you search" is the search-side twin. R1018 and R2466 both turn on seeing the hand before/without the replacement card, and R0098 is the explicit-show exception.

**Recommendation:** State one principle — replacement draws and library searches are private by default, and only text that says to show does otherwise — with R1957 and R1956 as the two e.g. cards and R0098 as the exception example. Fold R2426 into R1957 (same reference, no new content). R1018 and R2466 are legitimately about the timing of an unreplaced/optional replacement rather than visibility; if the drafter keeps them, cross-reference 1.9 rather than listing both.

*Rulings (6):* R1957, R2426, R1956, R1018, R2466, R0098

### [medium] duplicate-template

"Discard the whole set first, replace afterwards" recurs on five cards. R0400 (Constant Revolution.1) "The cards are all discarded at once (no replace)"; R2413 (Ruxandra.1) "The cards must all be discarded at once, then replaced" — these two are the same sentence. R0271 (Call the Wild Hunt.2) is the same rule stated as its consequence (you cannot feed replacement draws back in as further discards); R0664 (Feline Saboteur.1) and R2404 (Rachel Brandywine.1) are per-card resolution orders that instantiate it.

**Recommendation:** Keep R2413 (or R0400 — they are interchangeable) as the P stating the rule, with R0271 as the e.g. that shows why it matters. R0664 is a bare recitation of one card's three-step resolution order and transfers nothing once the general rule is stated — send it to C. R2404 adds a genuinely separate beat (shuffle-back happens after all discards and redraws) so keep it, but as an E on the general rule rather than as its own P.

*Rulings (5):* R0400, R2413, R0271, R0664, R2404

### [medium] misfiled

R0868 (High Aye.1) "The discard effect happens after action resolution (and all combats, if any)" is filed P PRIMARY in 6.9, but the principle it teaches is when a card's effect resolves relative to the action and any combat it provokes — that is 2.3 ("after resolution"/"after combat" modifiers). The fact that the effect in question happens to be a discard is the surface, not the principle. Filing it here invites the drafter to write a discard-specific timing rule that is actually the general post-resolution ordering rule.

**Recommendation:** Move to 2.3 as PRIMARY; retain 6.9 as a secondary cross-reference at most. 6.9 should cross-reference 2.3 for when a discard effect lands rather than restate it.

*Rulings (1):* R0868

### [medium] over-absorbed

R2098 (Agaitas, The Scholar of Antiquities.2) is E PRIMARY but is entirely Agaitas's own mechanism: "If Agaitas is burned while cards owned by your prey are still face-up in front of you, you can still play and discard them as normal, but you cannot draw in your prey's library until you control Agaitas anew." Drawing from a prey's library and holding face-up cards owned by another Methuselah is a mechanic no other card produces, so it fails the transfer test — it changes how you rule on no other card. What little is general in it (cards keep their owner; the owner's zone is where they go) is 6.1's, not 6.9's.

**Recommendation:** Reclassify C with 6.1 as the near-miss code. R2097 (Agaitas.1, additional draws are not subject to his ability) is worth keeping only if the drafter can state it as the general rule that an ability modifying "your draw" does not reach draws granted by other cards; if not, it is C for the same reason.

*Rulings (1):* R2098

### [low] duplicate-template

R1758 (Sudario Refraction.4) "If the library is empty and the hand is not full, you draw the returned cards up to hand size before discarding at random" and R2010 (Waste Management Operation.1) "If the library is empty and the hand not full, you draw immediately after using it" are one rule on two cards: cards returned to an empty library are drawn immediately to refill the hand.

**Recommendation:** One sentence with R2010 as the single e.g.; R1758's extra clause (discard at random happens after the refill) can be a subordinate note on the same entry rather than a second ruling.

*Rulings (2):* R1758, R2010

### [low] misfiled

R2359 (Nahir.1) "The hand size is still +X if Nahir is in torpor" is P PRIMARY here, but the rule it applies is the torpor rule about which abilities keep functioning (5.3, or 1.5 on ability use not being a card play), not anything about the hand. Read as a 6.9 principle it says nothing more than "a hand-size bonus persists while its source persists", which fails non-obviousness.

**Recommendation:** Move PRIMARY to 5.3 and keep 6.9 as secondary. If 6.9 wants a persistence example, R1134 ({The Meddling of Semsith} still reducing hand size after its target is ousted) already serves and is the stronger case.

*Rulings (1):* R2359

### [low] role-error

R0927 (Infernal Pursuit.5) "Effects that make you discard (eg. {Nicomedes}) are subject to Infernal Pursuit" is labelled P, i.e. it would become prose stating a 6.9 principle. As written it states a fact about one card's scope, not a general rule; the general form (a modifier keyed to "discard" applies to discards from any source, not only the card's own) is not what the text says.

**Recommendation:** Demote to E under the draw/discard-mechanics principle, alongside R0923 which is the genuine P for that sub-topic ("the card you discard need not be one of the cards that you just drew").

*Rulings (1):* R0927

### [low] missing-topic

Three sub-topics a drafter would expect to cover in 6.9 have no ruling in the membership. (1) Discarding as a cost or as a voluntary act — every ruling here is about a forced or effect-driven discard; nothing addresses whether or when a Methuselah may discard at will. (2) The baseline itself — no ruling touches the default hand size or the mandatory nature of drawing back up at end of turn, so the prose will have to lean entirely on the rulebook. (3) Who chooses which card is discarded when another Methuselah forces the discard — R0923 fixes that the discarder chooses among their own hand, but nothing covers a card that directs the choice.

**Recommendation:** Flag to the drafter that these three will be written from the rulebook with no ruling support, and that the section should cross-reference 1.7 for discard-as-cost rather than attempt to own it. Also note the standing seam with 1.9: roughly a third of this membership (R0544, R1137, R2227, R2466, R1018, R2010, R1758) turns on replacement timing, which 1.9 owns; 6.9 should keep only the hand-size consequence and cross-reference.

## C-00

### [medium] recoverable-C

Two different cards ({Consignment to Duat}, {Gregory Winter}) carry the same ruling — an effect that takes/removes blood may target a vampire holding none — issued under the same reference [RTR 20010711]. The corpus itself proves transfer: one rule, two cards, dropped independently by two chunks. Taxonomy widened 1.7 on 2026-07-20 for precisely this class ('effects naming an amount the target may not hold (steal/transfer templates take what is there)'). The notes reason card-by-card and so cannot see that the same rule was applied twice.

**Recommendation:** Recover both as E under 1.7 (secondary 1.6). They are the paired 'e.g.' cards for the principle that targeting language never carries an implicit requirement that the target hold the resource the effect names; the effect simply takes what is there. Two cards is exactly the 1-3 example budget, so no exhaustive-list risk.

*Rulings (2):* R0398, R0795

### [medium] recoverable-C

{Brainwash}.2's note addresses only the crypt-position targeting mechanic and never engages the ruling's second half: 'In case multiple copies of the same vampire are subject to different effects, the controller must track them, but they can do it secretly.' That is a general rule about hidden state — who bears the tracking obligation for identical cards under divergent effects, and that the tracking need not be public — and 2.5's scope line already claims it verbatim ('effects losing track of hidden cards').

**Recommendation:** Recover as P under 2.5, secondary 6.7. Drafters of 2.5 need this: it is the only ruling in the shard stating who must track divergent state across identical cards and that the record may be kept secret. The card-specific crypt-position half stays in the database; the tracking sentence is the transferable part.

*Rulings (1):* R0243

### [low] recoverable-C

{Gemini's Mirror}.1 — 'Does not protect the minion's equipment, retainers, or any other cards on him. Just him and his blood.' The note calls this card-specific 'protection-scope wording', but the boundary it draws (an effect naming a minion reaches the minion and its blood, not the cards hosted on it) is the standing default that 1.12 exists to state, and it governs any effect worded at a minion.

**Recommendation:** Recover as E under 1.12 (secondary 5.6). One sentence of 1.12 prose with this as the cited example; do not expand into a list of protection cards.

*Rulings (1):* R0755

### [low] recoverable-C

{The Diamond Thunderbolt}.4 — a cancel effect 'will not extend temporary change of control effects when they expire.' The note dismisses this as following from what a cancel card does, but the underlying rule — cancellation reaches card plays, not the natural lapse of an ongoing duration — is a boundary judges are asked about and is not stated by the rulebook. 1.8's scope line already owns 'what cancellation does/reaches'.

**Recommendation:** Recover as E under 1.8 (secondary 2.5, which owns duration expiry). Note that 1.8 is already drafted and reviewed, so this is a candidate for a light edit at most, not a rewrite — route it to the extract and let the Phase 4.5 pass decide whether it earns a clause.

*Rulings (1):* R0505

### [low] recoverable-C

{Ashur Tablets}.1 — 'Can be played with no card in the ash heap.' The note's non-obviousness argument is defensible, but this is the positive side of the live no-effect-plays question the contract names as a standing tension slug, and it pairs instructively with R0119/R0128 in the same shard: a card with a printed target requirement cannot be played without a legal target, while a card whose effect merely operates on a zone may be played into an empty one.

**Recommendation:** Recover as E under 1.8 (secondary 1.11), tagged !TENSION:no-effect-plays. Lowest-confidence of the five — if the 1.8 drafter finds the distinction already carried by the drafted text, drop it again.

*Rulings (1):* R0096

### [low] other

Two rows state opposite outcomes for the same condition on adjacent ruling dates: {Council of Seraphim}.1 'The burn option cannot be used if all your Seraph are in torpor' [LSJ 20091204] versus {Deep Cover Agent}.1 'The burn option can be used if all your Seraphs are in torpor' [LSJ 20091203]. Both were correctly dropped as C, so there is no document impact, but neither classifier could see the other and so neither tagged the conflict. If these are two different cards with genuinely different text the pair is fine; if one is a transcription error the database carries a wrong ruling.

**Recommendation:** No document action. Raise as a database-integrity check for the vtes-rulings maintainers: verify both card texts and the two originals. If the wording turns out to be garbled, the surviving row may warrant a !WORDING tag rather than reclassification.

*Rulings (2):* R0409, R0464

## C-01

### [high] recoverable-C

Five Mask of a Thousand Faces / Madness Network rulings were dropped as "specific to Mask's own masking mechanic" — but §3.10 (changing the acting minion) was created after classification on Mask.3, and these rulings sit squarely inside its published scope line. §3.10 currently rests on 4 rulings; this is a silent loss of most of the section's evidence base. R1076 (non-Malkavian cannot use Mask to assume a Malkavian's out-of-turn action) and R1115 (cannot take over an action granted by an equipment the masked minion has, even if the masking vampire has the same equipment) are the scope line's "eligibility keyed to what the substitute could independently have done", and R1076 is on a different card, which is transfer demonstrated rather than argued. R1119 (may mask after blocks declined when the masked minion was unblockable, even though the masking minion does not benefit) is the "which effects carry over" rule, and it pairs with R1115 to draw the line: state already applied to the action carries; the action's card-granted source does not. R1118 fixes a window §3.10 does not currently state (after a block is declared, before block resolution).

**Recommendation:** Recover R1076 and R1119 as §3.10 E, and R1115 as §3.10 E (it is the counter-case that bounds R1119). R1118 as §3.10 E if the drafter wants the timing window; otherwise leave it. Leave R1114 and R1120 as C — R1114 restates the ordinary controller-plays-action-modifiers rule (and duplicates R1199 on Mouthpiece, same LSJ 19990425), and R1120 restates Mask's own unlocked requirement. Recovering 3 respects the 1-3 example rule; do not recover all six.

*Rulings (4):* R1119, R1076, R1115, R1118

### [medium] recoverable-C

Six rulings across five cards state one template — an effect naming an amount the target cannot supply or cannot hold is still legal, and simply takes/moves what is there. §1.7's scope line was widened on 2026-07-20 to claim exactly this ("effects naming an amount the target may not hold (steal/transfer templates take what is there)"), so the widened scope currently has no rulings from this shard to draft from. R0998 (a strike to steal 2 blood may be used on a minion holding less than 2) is the cleanest instance of the source side. R0959 (Jar the Soul on an empty vampire attempts to burn blood and fails, and does not convert to damage) supplies the resolution consequence — the effect does not substitute a different one. R0840 (Heidelberg may move more blood than the target can hold; the excess goes to the blood bank) is the destination-side mirror the scope line does not yet cover. Notes rejecting these as "fails transfer" are contradicted by the fact that four distinct cards produced the same answer, three of them on the same RTR 20010711.

**Recommendation:** Recover R0998 as §1.7 E and R0959 as §1.7 E (source side and its resolution consequence). Recover R0840 as §1.7 E only if the drafter wants the capacity-cap mirror; it is the weakest on non-obviousness. Leave R0907, R1361 and R1362 as C — they are duplicate instances of the same template and the style rule caps examples at three.

*Rulings (6):* R0998, R0959, R0840, R0907, R1361, R1362

### [medium] recoverable-C

R1427 (Reanimated Corpse brought back with X=0 has no pathos counter and burns immediately) restates §1.12's scope line almost verbatim — "counter-count conventions on entry (a card entering with X=0 counters burns immediately)" — yet its note reads "fails transfer — specific to this card's counter type; nearest 1.12". The scope widening postdates classification. R1339 (Church of the Order of St. Blaise may add a counter to a zero-counter Powerbase: Barranquilla before it burns) is the same section's burn-threshold sub-topic and pulls against R1427's "burns immediately": one says the zero-counter burn is instant, the other says there is a window to intervene. That apparent conflict is exactly the kind of thing a §1.12 drafter must resolve and cannot resolve if both rulings stayed in the database.

**Recommendation:** Recover R1427 as §1.12 E. Recover R1339 as §1.12 E carrying a !TENSION:zero-counter-burn-window tag so the pair is adjudicated together rather than each being read alone.

*Rulings (2):* R1427, R1339

### [low] other

The taxonomy's rejected-candidates record states "the 2 auction rulings are all Extremis Boon — single-card topics". This shard contains auction/bidding-procedure rulings on two further cards: R0877 (Hostile Takeover — open-format bidding, the player who played the card conducts it) and R1100 (Malkavian Time Auction — bidding continues until nobody bids; you do not participate). The stated ground for rejection is therefore factually wrong: bidding spans at least three cards. This is a record-accuracy issue, not a recovery — the C verdicts on both rulings are defensible on non-obviousness, and two thin idiosyncratic procedures do not clear the two-sub-topic bar §6.9 and §1.15 were held to.

**Recommendation:** Correct the rejection note in taxonomy.md to say auctions were rejected for thinness and idiosyncrasy across three cards, not for being a single-card topic. Leave both rulings C. Do not create a section; if a future pass surfaces more bidding rulings, the corrected record is what a reviewer would need to reassess.

*Rulings (2):* R0877, R1100

## C-02

### [medium] recoverable-C

Le Dinh Tho.1 ("When using his ability, you do not get to see the card drawn as replacement") is a direct instance of the default-visibility rule that 6.9's scope line explicitly claims: "default VISIBILITY of card manipulation (library searches and replacement draws are not shown)". The classifier's note says "no general rule about replacement visibility transfers elsewhere" — but that is precisely the rule the taxonomy widened 6.9 to own, and it transfers to every effect that replaces a card. The classifier plausibly worked against the pre-widening scope line; against the current taxonomy the drop is wrong.

**Recommendation:** Recover as 6.9, role E (the concrete worked case for the visibility default; the principle prose likely comes from elsewhere in 6.9's extract). Nearest secondary code 1.9.

*Rulings (1):* R2293

### [medium] recoverable-C

A recurring wording template — an ability conditioned on combat/bleeding is read as requiring the BEARER personally to be the participant — was dropped five times in this shard alone. R2212 and R2352 are literally the same sentence with the same reference ([ANK 20221021]) on two different cards, which marks it as a template rather than card text. 1.5's scope line was widened on Phase 3 evidence to claim exactly this: "abilities whose use requires the bearer to be *personally* a participant (eg. in combat themselves, not merely combat occurring)". R2212's own note even names 1.5 as nearest while calling the reading "obvious" — a reading the Rules Director had to issue on at least three cards. R2033 (Winged Second) is the non-obvious member: the "Second" does the fighting yet the minion is not in combat, so neither its own nor its retainers' combat abilities fire — that transfers to any stand-in/representation entity.

**Recommendation:** Recover R2033 as 1.5, role E (secondary 1.4, representation/placeholders). Recover ONE of R2212/R2352 as 1.5 role E for the plain "in combat herself" case; leave the rest C — style rule caps examples at three, so the remaining copies correctly stay in the database.

*Rulings (5):* R2033, R2212, R2352, R1604, R2397

### [low] recoverable-C

Three rulings on the same question — WHO may play a given card into an action or combat — were dropped with three mutually incompatible accounts of the default. R1774 (Suppressing Fire, "only by the controller of the acting minion") is called a card-specific restriction; R1882 (Touch of Clarity, playable by a non-acting ready unlocked minion of the acting minion's controller) is called "the standard action-modifier default"; R1535 (Save Face, playable by a minion of an uninvolved Methuselah) is called "reads the absence of a restriction literally". These cannot all be the baseline. The rulebook default is that action modifiers come from the acting minion, so R1882's eligibility template (ready + unlocked + non-acting + same controller) is an exception whose constraints the rulebook does not spell out, and it transfers to every card worded that way.

**Recommendation:** Recover R1882 as 2.1 ("who may act when"), role E, secondary 1.8. Leave R1774 and R1535 as C but consider a !TENSION:who-may-play-a-card tag so a later pass adjudicates the three together; whichever way it resolves, the drafter of 2.1 should see at least one of them.

*Rulings (3):* R1882, R1774, R1535

