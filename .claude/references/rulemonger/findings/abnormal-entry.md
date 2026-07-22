# Findings — cross-section sweep: abnormal-entry-requirements (2026-07-22)

Doctrine swept (owner adjudication 2026-07-20, block B — settled): (1) only "put … in
play" bypasses requirements and costs; equip/recruit/employ invoke the normal machinery;
(2) bypassing requirements does not bypass prohibitions (Heidelberg/Enkidu, R0837);
(3) illegal placement burns without cost refund, imposed effect persists (Wooden Stake);
(4) a card's own on-entry clauses and burn-requirements apply however it entered
(War Ghoul, R1999); (5) played "not in the normal fashion" is still played — loses only
the normal-play window.

Sections swept: §1.6.3/§1.6.4, §1.8, §1.9.3, §3.5.3/§3.5.5, §3.7.3, §3.7.4, §5.5,
§5.6, §6.3, Appendix A ("put … in play", "recruit / employ / equip (keywords)",
"as played window", {Mata Hari} template, "X (cost of X)", "card played (retrieval)").

Sources verified this sweep (KRCG card_text): {Concealed Weapon}, {Piper},
{The Summoning}, {Magic of the Smith} all print "(requirements and cost apply as
normal)"; {Summon History} "put that card in play"; {Compel the Spirit} [NEC] "move it
to your ready region (ignore requirements and cost)"; {Bindusara, Historian of the
Kindred} "put that card in play. (Pay cost as normal.)"; {Horrid Reality} "Do not pay
the cost … if the requirements are not met, it is burned"; {Bloodstone} "Put this
equipment on any minion (this is a +1 stealth Ⓓ action if the minion is controlled by
another Methuselah)" — no cost, no requirement; {War Ghoul} "After this ally enters
play, burn an ally or retainer you control"; {Web of Knives Recruit} "+1 stealth
action. Put this card in play in your uncontrolled region with 3 training counters…";
{Blood Cult Awareness Network} "any action to put a vampire or ghoul in play … gets -1
stealth". Rulings: 100908|Heidelberg Castle, Germany.2 [LSJ 19980831];
102192|Wooden Stake [LSJ 19980831]; G00110, G00131, G00132, G00133, G00094, G00150,
G00151, G00072; {The Summoning}/{Piper} "[PRE] The ally cannot act this turn.
[RBK recruit-ally]"; 101046|Khazar's Diary (Endless Night) [LSJ 20080426];
102165|Web of Knives Recruit [LSJ 20060616-2]; 100703|Far Mastery [TOM 19960226-1];
201446|Vidal Jarbeaux [LSJ 20050119]; ANK 20230408 original fetched (VEKN #107810:
Bloodstone on another Methuselah's minion IS a successful equip action).
Submodule history: upstream 1a49949 "Group equip/employ/recruit action" and 346ee59
(Feb 2025) consolidated the per-card equip/employ/recruit rulings into
G00131/G00132/G00133/G00094 and re-cited the Summoning/Piper cannot-act rulings from
[LSJ 20080630] [RTR 20180303] to [RBK recruit-ally]; {Bloodstone}, {Jack of Both
Sides}, {Muricia's Call} records were dissolved entirely.

Interaction: F-unlock-1 (findings/unlock-outlives-source.md, open) proposes an edit to
the same §1.6.3 lines 339–342 paragraph as F-abn-5's [^1-6-10] repair — merge if both
approved. The Wooden-Stake persistence nuance is NOT re-reported here.

## F-abn-1 — §1.6.3's lead sentence omits the cost half of the bypass and its cost sentence suggests the wrong default  [contradiction] [minor]
**Where:** §1.6.3, lines 330 and 335–337:
> Only "put ... in play" bypasses requirements, e.g. {Summon History}, {Compel the Spirit} [NEC].[^1-6-7]
> …
> Where requirements are bypassed, a required discipline is used at inferior and a cost of X is zero.[^1-6-8] Cost is a
> separate check: {Bindusara, Historian of the Kindred} ignores requirements but pays cost; {Horrid Reality} pays none but
> burns the weapon if requirements are unmet.[^1-6-9]

**Evidence:** Owner doctrine point 1 (block B, settled): "put … in play" bypasses
requirements *and costs*. The document states it that way everywhere else: §3.7.4.2
"Requirements and cost apply as normal under the first and are bypassed under the
second"; Appendix A ""put … in play" — the only wording that bypasses requirements and
cost". §1.6.3 — the canonical home the others point to — is the one place that says
"bypasses requirements" only, and its "Cost is a separate check: {Bindusara} …
pays cost" reads as if cost were unbypassed by default, when Bindusara pays only
because its card prints "(Pay cost as normal.)" (KRCG) and Horrid Reality skips cost
because it prints "Do not pay the cost" (KRCG). A judge reading §1.6.3 alone could
make a {Summon History} fetch pay its printed cost.
**Proposed fix** (lines 330–337, 120-col rewrap):
```
Only "put ... in play" bypasses requirements and cost, e.g. {Summon History}, {Compel the Spirit} [NEC].[^1-6-7]
**Equip**, **recruit** and **employ** invoke the normal machinery, so requirements and cost apply as printed, e.g.
{Concealed Weapon}, {Piper}, {Magic of the Smith}. Such a card has still been played; see
[§1.8](#18-playing-and-canceling-a-card) for what it loses.

Where requirements are bypassed, a required discipline is used at inferior and a cost of X is zero.[^1-6-8] Card text
splits the two checks at will: {Bindusara, Historian of the Kindred} puts in play but prints that cost is paid; {Horrid
Reality} equips paying no cost, and burns the weapon if requirements are unmet.[^1-6-9]
```

## F-abn-2 — §3.7.3.1 uses {Bloodstone} as the "put → bypass" exemplar; Bloodstone is a normal play from hand with nothing to bypass  [unsupported-claim] [minor]
**Where:** §3.7.3.1, lines 1669–1671:
> Being an equip action does not settle requirements and cost. Only the wording "put … in play" bypasses them
> ([§1.6](#16-requirements)): {Bloodstone} puts the equipment on the minion, {Magic of the Smith} prints that requirements
> and cost apply.

**Evidence:** {Bloodstone} (KRCG): "Put this equipment on any minion (this is a +1
stealth Ⓓ action if the minion is controlled by another Methuselah)." — no cost, no
requirement, so there is nothing it could bypass; and the card is itself played from
hand as the action (a normal play). Its "put" wording sets target latitude, not the
§1.6.3 entry template (a card brought in *by another card's effect*). No ruling ever
made it a bypass case: its only rulings — pre-consolidation "It's still an equip
action (eg. It can benefit from {The British Museum, London}…) [LSJ 20050313]
[ANK 20230408]" (deleted into G00094 by upstream 346ee59), G00094 "The type of the
action (equip/employ) does not change regardless of the target" — are about action
type. As written, the sentence teaches "own-text 'put' = bypass", which would misrule
e.g. {Shackles of Enkidu} ("put this card on the opposing minion" — played from hand,
[pot] required, cost paid).
**Proposed fix** (keep the contrast, move Bloodstone to the target-latitude point):
```
Being an equip action does not settle requirements and cost. Only the wording "put … in play" bypasses them
([§1.6](#16-requirements)): {Magic of the Smith} prints that requirements and cost apply. {Bloodstone}'s "put" sets only
where the equipment goes — the card itself is played from hand as normal. A requirement is checked continuously while
the action is in progress, so a trait change mid-action fizzles it — successful if unblocked, but no effect
([§1.6.1](#161-when-a-requirement-is-checked)).
```
Alternative (minimal): delete "{Bloodstone} puts the equipment on the minion, " and
keep only the Magic of the Smith half. Escalate: owner picks wording.

## F-abn-3 — §3.7.4.2 files the BCAN/{Web of Knives Recruit} example under "Neither is an action"; the ruling's ground is action-type mismatch, and WoKR *is* an action  [unsupported-claim] [minor]
**Where:** §3.7.4.2, lines 1741–1745:
> Neither is an action, and effects worded as attaching to an action do not attach:
>
> - Cost reductions naming an action, e.g. {Charisma}, {Erichtho}.[^3-7-4-4]
> - Stealth modifiers on an action, e.g. {Blood Cult Awareness Network} does not reduce the stealth of a {Web of Knives
>   Recruit} action.

**Evidence:** 102165|Web of Knives Recruit: "It is not an action to put a vampire in
play (eg. {Blood Cult Awareness Network} does not give it -1 stealth).
[LSJ 20060616-2]". WoKR (KRCG) is a "+1 stealth action" played from hand — an action,
and not an ally/retainer entry at all (it puts its own card in the uncontrolled
region). BCAN (KRCG) reads "any action to put a vampire or ghoul in play … gets -1
stealth": it misses WoKR because the action's type does not match BCAN's template, not
because there is no action. The bullet contradicts its own frame (it says "a {Web of
Knives Recruit} *action*" inside a list headed "Neither is an action") and does not
belong in the entry-without-the-action section. The counterpart rulings for
put-a-vampire-in-play actions live under {Call the Great Beast} and {Raw Recruit}
("{Blood Cult Awareness Network} gives it -1 stealth" [LSJ 20011212] [LSJ 20060815]).
**Proposed fix:** delete the bullet, and drop
[LSJ 20060616-2](…/YGA7bnOj04Y/m/wOVi6CvB8Z0J) + {Web of Knives Recruit} from
[^3-7-4-4] (remaining IDs [LSJ 20090115-1] [ANK 20170309] — {Piper}(*see F-abn-5:
→ {Zhenga}*) cover the cost-reduction bullet). If the owner wants the WoKR point kept,
its home is the action-to-put-a-vampire-in-play family (§5.7.6 Sterile / BCAN
template), not §3.7.4.2 — escalate placement.

## F-abn-4 — §3.5.5 states cancellation reach as "cards played from the hand", dropping the "as if from your hand" arm the canonical §1.8.2 carries  [contradiction] [minor]
**Where:** §3.5.5, lines 1491–1493:
> Cancel effects reach every action card, including employ retainer, recruit ally and political actions.[^3-5-25] They
> reach only cards played from the hand in the normal fashion, so a weapon equipped via {Disguised Weapon} or an ally
> recruited via {Piper} cannot be canceled ([§1.8](#18-playing-and-canceling-a-card)).[^3-5-26]

**Evidence:** §1.8.2 (canonical): "Cancellation reaches only normal plays … from hand,
or "as if from your hand" where a card says so, e.g. {Persistent Echo}, {The Erciyes
Fragments}". [RTR 20040501] presupposes Erciyes plays are cancelable as played
(recorded general lesson). An Erciyes political card is not played *from the hand*, so
§3.5.5's wording as written would misrule it uncancelable.
**Proposed fix** (line 1491–1493 rewrap):
```
Cancel effects reach every action card, including employ retainer, recruit ally and political actions.[^3-5-25] They
reach only cards played in the normal fashion ([§1.8](#18-playing-and-canceling-a-card), "as if from your hand"
included), so a weapon equipped via {Disguised Weapon} or an ally recruited via {Piper} cannot be canceled.[^3-5-26]
```

## F-abn-5 — Footnote record keys stale against the Feb-2025 upstream consolidation (1a49949, 346ee59)  [stale] [minor]
**Where / Evidence / Fix per footnote** (every filing below verified by targeted grep
on the pinned DB; history recovered from the two commits — none of these IDs was
retracted):

- **[^1-6-10]** — [ANK 20170309-2] is filed under G00150/G00151, not {War Ghoul}
  (102144's only ruling is [PIB 20121031]). Replace the key `{War Ghoul}` with
  `groups "Allies with enter play effects" (G00150) and "Allies that burn an ally when
  entering play" (G00151)`. All other IDs/keys verified sound ({Rowan Ring} carries
  LSJ 19980831 — see unlock-outlives-source sweep).
- **[^5-5-9]** — same re-keying: [RTR 19961113] → G00151, [ANK 20170309-2] →
  G00150/G00151. New tail: `— groups "Allies with enter play effects" (G00150) and
  "Allies that burn an ally when entering play" (G00151), {Sébastien Goulet}.`
  ([ANK 20210913] [LSJ 20090116] verified on {Sébastien Goulet}.)
- **[^5-5-7]** — [LSJ 20080630] and [RTR 20180303] were the citations on
  {Piper}/{The Summoning} "the ally cannot act this turn" until 1a49949 re-cited it to
  [RBK recruit-ally]; in the pinned DB those two IDs support only unrelated rulings
  ({Asguresh}/G00058/G00089 self-replacement cancel; {Abomination}/influence-phase).
  Replacement definition:
  `[^5-5-7]: [RBK recruit-ally](https://www.vekn.net/rulebook#recruit-ally) [LSJ
  20100204](https://groups.google.com/g/rec.games.trading-cards.jyhad/c/o5Xnzc8G774/m/yovVizGngKsJ)
  [LSJ 20080426](https://groups.google.com/g/rec.games.trading-cards.jyhad/c/VIV521VtVfk/m/qQRxntT52F4J)
  — {The Summoning}, {Piper}, group "Put card in play ignoring requirements" (G00110),
  {Khazar's Diary (Endless Night)}.`
  (Keeping the two superseded IDs as historical is the owner's call — R-028 precedent.)
- **[^3-7-4-3]** — [LSJ 20100204] is filed under G00110 only; {Summon History}'s
  record carries neither cited ID. Tail → `— group "Put card in play ignoring
  requirements" (G00110), {Piper}.` ([LSJ 20080803] verified on {Piper}.)
- **[^3-7-3-1]** — {Bloodstone} and {Jack of Both Sides} have no records in the pinned
  DB; {Magic of the Smith}'s record carries no cited ID. [TOM 19960130] is filed under
  G00132, G00133, {Children of Stone}, {Sleight of Hand}, {Vast Wealth}, {Lambach};
  [LSJ 20050313] [ANK 20230408] under G00094. Tail → `— groups "Equip/Employ/Recruit
  action" (G00132) and "Retainers and equipment put on different minion" (G00094),
  {Children of Stone}, {Sleight of Hand}, {Lambach}.`
- **[^1-8-6]** — {Piper}'s record carries no cited ID; [ANK 20201229] is filed under
  {The Summoning} (kept) and G00131. Replace key `{Piper}` with `group
  "Equip/employ/recruit outside of an action" (G00131)`. ([RTR 20001020] verified on
  {Sudden Reversal}; [LSJ 20060530-2] on {Zhenga}; [RTR 20040501] on
  {The Erciyes Fragments}.)
- **[^1-6-14]** — [LSJ 20100725] [LSJ 20100303] [ANK 20180817] are filed under G00131
  (ruling 1) and G00132 (ruling 2); {Jack of Both Sides} and {Muricia's Call} have no
  records; {The Summoning}'s CrimethInc ruling was dissolved by 1a49949. Tail →
  `— groups "Equip/employ/recruit outside of an action" (G00131) and
  "Equip/Employ/Recruit action" (G00132), {Charming Lobby}.` ([ANK 20220704]
  [LSJ 20100819] verified on {Charming Lobby}.)
- **[^3-7-4-1]** — same family: keys {Muricia's Call} (no record), {The Summoning}
  (rulings dissolved) → `— groups "Equip/employ/recruit outside of an action" (G00131)
  and "Equip/Employ/Recruit action" (G00132), {Ghouled}.` ([LSJ 20030520-2] verified
  on {Ghouled}.)
- **[^3-7-4-2]** — key {Jack of Both Sides} (no record) → `group "Equip/Employ/Recruit
  action" (G00132)` ("Is an action of the appropriate type for the chosen card"
  [TOM 19960130]). Other keys untouched.
- **[^3-7-4-6]** — {Piper}'s record carries no cited ID ([ANK 20201229] →
  {The Summoning}, G00131). Tail → `— group "Equip/employ/recruit outside of an
  action" (G00131), {The Summoning}, {Zhenga}.`
- **[^3-7-4-7]** — [LSJ 20080815] and [ANK 20180817] are filed under G00131/G00132
  (also G00133); none of {Piper}, {Muricia's Call}, {The Summoning} carries them. Tail
  → `— groups "Equip/employ/recruit outside of an action" (G00131) and
  "Equip/Employ/Recruit action" (G00132).`
- **[^1-6-16]** — [LSJ 20050119] is filed under {Vidal Jarbeaux} and G00072
  "Impersonating requirements for cards not played normally"; none of the eleven
  listed vampires' own records carries it. Tail → `— group "Impersonating requirements
  for cards not played normally" (G00072), {Vidal Jarbeaux}.`

## F-abn-6 — [^6-3-1]/[^1-6-11]: [TOM 19960226-1] is now on fifteen records, not twelve  [stale] [note]
**Where:** [^6-3-1] "recorded identically on twelve cards; {Far Mastery},
{New Management}, {Spirit Marionette}"; [^1-6-11] enumerates twelve cards + G00013.
**Evidence:** pinned DB carries [TOM 19960226-1] on fifteen records: the twelve of
[^1-6-11] plus {Disputed Territory}, {From a Sinking Ship}, {New Management}.
**Proposed fix:** [^6-3-1] "twelve" → "fifteen"; [^1-6-11] add {Disputed Territory},
{From a Sinking Ship}, {New Management} (or trim to "fifteen cards; e.g." + three —
owner's call under the no-exhaustive-lists sensibility).

## Per-section verdicts

| Section | Verdict |
|---|---|
| §1.6.3 | Doctrine points 1–5 all present; cost-default wording diverges from §3.7.4.2/Appendix (F-abn-1); prohibition sentence verified against Heidelberg.2 [LSJ 19980831]; Wooden Stake nuance already open as F-unlock-1. Keys: F-abn-5/6. |
| §1.6.4 | Clean (Mata-Hari never-on-abnormal-play verified, [LSJ 20050119] G00072/{Vidal Jarbeaux}); key repair only. |
| §1.8.1–1.8.4 | Clean — point 5 canonical home; "as if from your hand" arm present; [^1-8-6] key repair only. |
| §1.9.3 | Clean — Baseball-Bat immediate-replacement rule matches [LSJ 20080702-2]; normal-play scoping intact. |
| §3.5.3 / §3.5.5 | §3.5.3 clean; §3.5.5 "from the hand" under-inclusive vs §1.8.2 (F-abn-4). |
| §3.7.3 | Requirements-vs-prohibitions carried (locked-vs-cannot-have split; burn-if-illegal + no-refund + §1.6 pointer). Bloodstone exemplar wrong side (F-abn-2); [^3-7-3-1] keys (F-abn-5). |
| §3.7.4 | Two-template statement matches doctrine; point 5 restated with §1.8 pointer; NRA/level-setting verified (G00131/G00132/{Piper}/{Ghouled}). WoKR bullet misfiled (F-abn-3); keys (F-abn-5). |
| §5.5 | §5.5.4 keyword split verified ({The Summoning}/{Piper} [RBK recruit-ally]; G00110 can-act; {Khazar's Diary} [LSJ 20080426]); point 4 fully stated (G00150/G00151). [^5-5-7]/[^5-5-9] stale (F-abn-5). |
| §5.6 | Clean — §5.6.5 employ-version rule consistent with §3.7.4.2's basic-version-when-put rule. |
| §6.3 | Clean — requirements-not-checked verified ([TOM 19960226-1] on {Far Mastery} et al.); count note (F-abn-6). |
| Appendix A | Clean — "put … in play", "recruit / employ / equip (keywords)", "as played window", {Mata Hari}, "X (cost of X)", "card played" all state the doctrine exactly. |

Status: ADJUDICATED 2026-07-22 (owner) — F-abn-1 applied; F-abn-2 resolved by DELETING the
{Bloodstone} clause; F-abn-3 resolved by DELETING the WoKR bullet ([^3-7-4-4] re-keyed
G00131/{Zhenga}); F-abn-4 applied; F-abn-5 applied with the clean [^5-5-7] swap (superseded
IDs dropped — rulebook now prints the rule); F-abn-6 applied. See R-030.
