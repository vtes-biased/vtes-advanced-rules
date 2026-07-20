# VTES Extended Rules

> **Status: DRAFT — structure agreed; sections 1.8 and 3.5 drafted and reviewed; all
> other sections are stubs. `⚠ REVIEW` marks points needing judge confirmation.**

## About this document

This document supplements the [VTES rulebook](https://www.vekn.net/rulebook). It collects
the general principles, corner cases and non-obvious interactions established by thirty
years of rulings, organized by game mechanic. The base rulebook tells you how to play;
this document tells you how the rules behave under pressure.

It is written for judges and advanced players: it assumes full fluency with the base
rules and terminology, and favors precision over accessibility.

**Conventions:**

- Card names appear in braces: `{Abbot}`.
- Discipline and card type symbols appear in brackets: `[pot]`, `[POT]`, `[ACTION]`.
- Statements derived from rulings carry footnote markers. Footnotes list the ruling
  reference IDs (e.g. `[LSJ 20090411]`), which resolve to URLs via
  [references.yaml](../rulings/references.yaml), and name the card or group under which
  the ruling is recorded in [rulings.yaml](../rulings/rulings.yaml).
- Card-specific rulings are quoted as examples where they illustrate a general
  principle. Pure one-card text interpretations remain in the rulings database.

---

## 1. Cards

### 1.1 Card text and the rules
<!-- Card text overrides the rulebook; "cannot" is absolute; mandatory vs. optional
effects ("the effect is not optional" — {Aaron's Feeding Razor}); golden rules. -->

### 1.2 Wording templates and periodicity
<!-- "each combat" / "each turn" (= each player's turn, G00014) / "once per game"
(G00030) / "this round" / "since your last turn" (G00010); "would" vs. "when" vs.
"after". -->

### 1.3 Card types and multi-type cards
<!-- Locquipments (G00047); reflex cards (G00060); clan equipment (G00013). -->

### 1.4 Representation and placeholders
<!-- A card representing something else loses its printed text entirely, including
"unique" ({Agent of Power}, {Absimiliard's Army}); no contest. -->

### 1.5 Abilities vs. cards
<!-- Abilities are not card plays; abilities usable in torpor (G00027) or while
locked (G00039/G00040); abilities reusable where cards are not ({Forest of
Shadows}, {General Perfidio Díos}). -->

### 1.6 Requirements
<!-- Play vs. keep; requirements ignored on abnormal entry (diablerie, {Bima});
requirements when taking control of in-play cards. -->

### 1.7 Costs and payment
<!-- Costs paid at resolution; cost vs. "burn blood to" effects (G00065); X costs
(G00032); arithmetic order ({The Ankara Citadel, Turkey}); pool/blood/life. -->

### 1.8 Playing and canceling a card

**Base rules.** A card is played by announcing its effects and showing it; it goes to
the ash heap (or into play) upon resolution. Action cards are temporarily out of play
between the moment they are played and their resolution. Effects that cancel a card
"as it is played", and wake effects, are the only effects allowed during the
"as played" window — even drawing to replace comes after. A canceled card has no
effect but is still considered played. A canceled action card costs nothing and the
minion does not lock; a canceled non-action card is paid as normal; a canceled strike
card forces the minion to choose a strike again.

#### 1.8.1 The "as played" window

When a card is played, a window opens before anything else happens — before even the
replacement draw. The only effects usable in this window are effects that apply to the
card "as it is played" (cancellations chief among them) and wake effects.[^c1]

- No card is drawn during the window, so a card-drawing effect ({The Barrens},
  {Dreams of the Sphinx}) cannot be used to dig for a cancellation.[^c2]
- A wake can be played in the window — typically to enable a reaction-speed
  cancellation such as {Bliss} or {Ophidian Gaze} — but a reaction that unlocks the
  minion "to attempt to block" is not a wake and cannot be played there.[^c3]
- An effect that applies to a card "as it is played" must be used immediately, before
  any other Methuselah has the opportunity to use a cancellation of their own.[^c4]
- A few cancellation effects are usable "even when there is no action in progress"
  (e.g. [tem] {Rewind Time}, [OBE] {Treat the Sick Mind}). The allowance is strictly
  theirs: it does not let a wake be played outside an action to enable them, and it
  does not extend to combat — they cannot be used during combat.[^c19]

**What can be canceled:** only cards played from the hand in the normal fashion.[^c5]
A card put in play or played by another effect cannot be canceled as it is played:
a weapon via {Disguised Weapon}, an ally via {Piper} or [PRE] {The Summoning}, a
political action card retained via {Charming Lobby}, a card played "as if from your
hand" via {Shadow Court Satyr}.[^c6] The same restriction applies to master
cancellation ({Sudden Reversal}).[^c5] An out-of-turn master is played in the normal
fashion and can be canceled.[^c7]

#### 1.8.2 A canceled card has still been played

Cancellation voids the card's effect, not the fact of its play. Consequences:

- Once-per limits attached to *playing* are consumed. The same minion cannot play the
  same action modifier or reaction card again during the action. A card whose text
  forbids playing more than one per period is locked out: a canceled
  {Immortal Grapple} still forbids playing another one that round.[^c8]
- Effects that trigger on or count card plays still apply: {Infernal Familiar} gains
  its counter even if the frenzy card is canceled; {Dabbler} counts canceled cards;
  a reaction canceled as it is played still denies {Perfectionist} its blood; an
  action canceled mid-course still counts as "one of the next X actions" for
  [OBF] {Veil the Legions}.[^c9]
- The card's own effect is not applied at all, including secondary effects: a
  canceled [CEL] {Infernal Pursuit} applies nothing and draws a single
  replacement.[^c10]
- Limits granted by a *canceled effect* are not consumed: if a limited effect (a
  bleed modifier, an additional strike) is canceled, the limit is not triggered and
  another limited effect can be used.[^c11]

#### 1.8.3 Costs of canceled cards

- A canceled action card costs nothing, and the acting minion does not lock
  (see [3.5.4](#354-canceled-actions) for the retry).
- A canceled non-action card is paid as normal. This includes blood costs put on the
  card by other effects: a strike card carrying a {Terror Frenzy} cost is paid even
  if the strike card is canceled.[^c12]
- If paying for the cancellation itself ousts a Methuselah, the oust is resolved
  before the canceled play finishes resolving. Once a bleed card is canceled, it is
  too late for the target to play reactions to the bleed.[^c13]

#### 1.8.4 Replacement of canceled cards

- Cards are not replaced during the "as played" window; all replacement happens
  after it closes.[^c1]
- A "do not replace until..." clause (or an alternate replacement such as
  {Steely Tenacity}) on a canceled card is canceled with it: the card is replaced
  normally.[^c14]

#### 1.8.5 Canceled strikes

- If a strike is canceled, the minion chooses a strike again — possibly another copy
  of the very same strike card: combat cards carry no once-per-action limit.[^c15]
- If an effect *modifying* a strike is canceled, the strike itself stands and
  resolves in its default form: {Target Retainer} canceled, the strike resolves
  against the opposing minion.[^c16]

#### 1.8.6 Canceled master cards

- A canceled Trifle grants no additional master phase action.[^c17]
- A canceled out-of-turn master still counts as the one out-of-turn master its
  Methuselah may play against that master phase, and still reduces that Methuselah's
  next master phase actions by one. The earlier ruling sparing the master phase
  action ([LSJ 20070309-2]) is reverted by the current rulebook.[^c18]

#### References

[^c1]: [LSJ 20061207] [LSJ 20061013] [RBK playing-a-card] — group "Cancel" (G00058).
[^c2]: [RTR 20040501] — recorded on {The Admonitions} and others.
[^c3]: [LSJ 20021011] — group "Cancel as a reaction" (G00062).
[^c4]: [LSJ 20100728] [LSJ 20090213] — {Veil of Darkness}, {Andrew Stuart}.
[^c5]: [RTR 20001020] — groups G00058/G00061, {Sudden Reversal}, {Asguresh}.
[^c6]: [ANK 20201229] — {The Summoning}; [LSJ 20090113-3] — {Charming Lobby};
    {Shadow Court Satyr}.
[^c7]: [LSJ 20031201] — {Vox Senis}.
[^c8]: [ANK 20190104] [LSJ 19980212] [RBK cancel-a-card] — group "Cancel" (G00058);
    [ANK 20200525-2] — {Immortal Grapple}.
[^c9]: [LSJ 20000424] — {Infernal Familiar}; [ANK 20220411] — {Dabbler};
    [LSJ 20070330] — {Perfectionist}; [ANK 20210124] — {Veil the Legions}.
[^c10]: [LSJ 20021022] — {Infernal Pursuit}.
[^c11]: [LSJ 20030224] — group "Cancel" (G00058); [LSJ 20100206] — {Asguresh}.
[^c12]: [RBK cancel-a-card]; [PIB 20121031] — {Target Hand} et al.
[^c13]: [LSJ 20050607] [LSJ 20050608] — {Spying Mission}.
[^c14]: [LSJ 20011023] [LSJ 20080630] — group "Cancel" (G00058), {Asguresh}.
[^c15]: [RBK cancel-a-card] [LSJ 20090818] — {Supernatural Resistance};
    [LSJ 20100206] — {Asguresh}, {Death Seeker}.
[^c16]: [ANK 20200311] — {Target Retainer}.
[^c17]: [LSJ 20090126] [ANK 20170124] [RBK trifle] — {Sudden Reversal}, {Wash}.
[^c18]: [LSJ 20070309-2] — {Wash}; [RBK master-phase] [RBK master-cards].
[^c19]: [PIB 20120808] [LSJ 20080618] — group "Cancel with no action" (G00063).

### 1.9 Replacement
<!-- When replacement happens; G00020 Action not replaced; "do not replace until"
stacking; drawing into an empty library. -->

### 1.10 Burn, remove from game, shuffle back
<!-- "When burned" triggers vs. removal ({Abandoning the Flesh}); G00056; G00002
(crypt/library separation, owner's zones). -->

### 1.11 The ash heap
<!-- Played vs. put there ({Epikasta Rigatos}: only cards *played* are retrieved);
owner vs. controller. -->

### 1.12 Cards on cards
<!-- G00028: host leaves play, hosted cards burn; {Capuchin}. -->

### 1.13 Contests
<!-- Unique cards and titles; self-contest; effects while contested; what is
remembered after; G00003 Circle. -->

### 1.14 Set-aside and announced cards
<!-- {Charming Lobby}, {Concealed Weapon}: in hand at announcement, not revealed,
not yet "played"; temporarily out-of-play cards do not burn. -->

---

## 2. Timing and Sequencing

### 2.1 Effect windows overview
<!-- Map of the windows and who has the impulse in each. -->

### 2.2 "As the action is announced" effects
<!-- G00052: must precede all regular modifiers/reactions. -->

### 2.3 "After resolution" effects
<!-- G00006/G00007; ordering chosen by acting player; blood hunt interaction. -->

### 2.4 Simultaneous effects and ordering
<!-- Controller chooses own order; unlock phase ordering (G00025); cost and benefit
simultaneous ({Villein}). -->

### 2.5 Duration and persistence of effects
<!-- "Until end of X"; "for the rest of the game" persists through state changes
({Lay Low}); effects lose track of cards in hidden zones. -->

---

## 3. Actions and Politics

### 3.1 Announcement and targets
<!-- Fixed at announcement vs. chosen at resolution; directed vs. undirected;
G00036 Directed at a card. -->

### 3.2 Stealth and intercept
<!-- Only when needed; persistence for the action's duration. -->

### 3.3 Blocking
<!-- Declaration sequence; declining is final; blocking locks; stolen blockers;
block when target vanished. -->

### 3.4 Resolution: success, failure and effect
<!-- Success vs. having an effect ({Nose of the Hound}); hunt success requires
blood gain (G00004); "successful resolution" ({Abactor}). -->

### 3.5 Action repetition (NRA) and canceled actions

**Base rules.** A minion cannot perform an action with the same *named* action card
more than once each turn, even if they unlock. A minion cannot perform the action
provided by the same *copy* of a card in play (including the minion's own card text)
more than once each turn, even if they unlock. The same minion cannot play the same
action modifier or reaction card more than once during a single action. If an action
card is canceled, the minion does not lock, pays nothing, and can play the same
action card again.

The first two rules are the **NRA (Non-Repeatable Action)** rule — a tournament rule
since 1998, part of the rulebook since the 2002 Camarilla Edition. NRA restricts
*card-provided* actions only: rulebook-provided actions are not subject to it
(see [3.5.2](#352-what-is-the-same-action)).

#### 3.5.1 Performing an action: reaching resolution

An action counts as *performed* once it **reaches resolution** — whether it resolves
successfully, is blocked, or is brought to an unsuccessful end by an effect.
Performing an action is what consumes the card name or copy under NRA, and what arms
card effects that forbid repeating "the same action" ({Obedience},
{Red Herring}).[^n1]

Effects that stop an action use one of three templates, with different
consequences:[^n2]

- **"The action fails."** The action resolves unsuccessfully, as if it had been
  blocked, except there is no blocker and no combat. It reached resolution. The end
  of the action otherwise proceeds normally — action modifiers and reactions can
  still be played if their text does not refer to a blocked action. {Freak Drive}
  illustrates the boundary: after a failed action it can be played neither at
  superior (the action was not blocked) nor at inferior (the action was not
  successful).[^n3] Any card whose text makes an action fail uses this template —
  e.g. [val] {Hide the Heart}, {Champion}, or {Secret Passage} burned to make the
  action fail.[^n4] The older templating "the action ends (unsuccessfully)" is
  equivalent to "fails": e.g. {Red Herring} (whose text also extends its lockout to
  *all* vampires you control — card text overrides).[^n5]
- **"End the action"**, on an action that is blocked: the action is over
  *immediately*. Combat does not happen and no further action modifier or reaction
  of any kind can be played — not even end-of-action effects. It reached
  resolution. {Obedience} is the reference (its text spells out the lockout: "The
  acting vampire cannot perform the same action this turn"); {Krassimir}'s ability,
  which ends his own action when blocked before block resolution, was likewise
  ruled to reach resolution.[^n6]
- **"Cancel the action."** The action never reached resolution: it is *not*
  performed (see [3.5.4](#354-canceled-actions)).

> **Mistemplate:** {The Kiss of Ra} reads "the current action is ended (without
> combat)" while *canceling* the block attempt — so the action it ends is not
> blocked. It has been ruled equivalent to a cancellation, and the Rules Director
> acknowledged the wording as a templating error to be corrected to "fails" on
> reprint. Until then it follows the cancellation rules of
> [3.5.4](#354-canceled-actions).[^n7]

#### 3.5.2 What is "the same action"

NRA needs no identity test beyond the card's name or copy, and it does not reach
**rulebook-provided actions** (bleed, hunt, equip, employ, recruit, leave torpor,
rescue, diablerie): a minion who manages to unlock may attempt those again freely,
successful or not — hunt repeatedly, or retry a failed rescue from torpor.

Action *identity* matters instead for card effects that forbid repeating "the same
action" ({Obedience}, {Red Herring}) or that otherwise hinge on it
({Change of Target}). For those:

- A rulebook-provided action is never "the same" as a card-provided action, however
  similar their effects.[^n9]
- Two rulebook-provided actions are the same if they share the action *type and its
  target(s)*. Equipping from another minion targets the *equipment*: going for the
  same equipment card again is the same action.[^n10]
- Actions provided by cards in play are the same only through the same *copy*:
  another copy of a same-named card in play provides a different action.[^n8]

The identity of the *acting minion* matters too:

- {Malleable Visage} does not change the acting minion for NRA purposes.[^n11]
- A burned ally or retainer brought back ({Compel the Spirit}) is a new minion, not
  bound by the actions of its previous incarnation.[^n12]
- Repetition is tracked per turn and per minion across the whole turn — including
  designed repetition: {Quincy, The Trapper} must perform the same action in two
  different turns, and tracking it (with tokens if players agree) is the
  controller's burden.[^n13]

#### 3.5.3 Repetition of action modifiers and reactions

The once-per-action limit on action modifiers and reaction cards is *per minion*:
different minions can each play a copy of the same card on the same action
({Cloak the Gathering}, {Mask of a Thousand Faces}, {Suppressing Fire}...), and
[AUS] {Sins of the Cauchemar} can be played by several minions even with no block
attempt made.[^n14] A canceled play still consumes the minion's once-per-action
allowance (see [1.8.2](#182-a-canceled-card-has-still-been-played)).

#### 3.5.4 Canceled actions

Action cancellation reaches every action card type — including employ retainer,
recruit ally and political action cards — but only cards played from the hand in
the normal fashion ([1.8.1](#181-the-as-played-window)).[^n19]

A canceled action was never performed:

- The minion does not lock, pays nothing, and is free to attempt the same action
  again — including with the very same action card.[^n15]
- Effects contingent on the action reaching resolution never happen: {Daring the
  Dawn}'s "as the action resolves" damage is not applied if the action is canceled
  mid-course.[^n16]
- But the cards played during it were still played ([1.8.2](#182-a-canceled-card-has-still-been-played)),
  and costs locked into *other* effects are not refunded: a minion who locked
  {Enkil Cog} for an extra action keeps the Cog locked if the action is canceled as
  it is played, and may either take an action again or let the Cog's grant
  lapse.[^n17]

**Mid-course cancellation.** {Tangle Atropos' Hand} (and currently {The Kiss of Ra},
see the mistemplate note in [3.5.1](#351-performing-an-action-reaching-resolution))
cancels an action *after* announcement, during its course. The action has not
reached resolution: it is effectively canceled and the same minion may undertake the
same action again — **unless** the action had already been blocked and then
continued (e.g. via [PRO] {Form of Mist}), in which case it may not be
reattempted.[^n18]

#### 3.5.5 Canceled blocks and canceled combats

- A canceled block attempt is neither successful nor unsuccessful — it is simply
  canceled.[^n20]
- When *combat* is canceled after a successful block ({Crypt's Sons}, {Venenation}),
  the action remains blocked and the blocking minion remains locked. {Mask of a
  Thousand Faces} cannot continue the action (there was no unsuccessful block), but
  continue-as-if-unblocked effects ({Crypt's Sons}, {Momentary Delay}) can. Reaction
  cards pertaining to the canceled combat ({Obedience}) cannot be played once it is
  canceled.[^n21]

#### References

[^n1]: [LSJ 20070709] [RTR 20180719] [ANK 20211015] — {Obedience}, {Change of
    Target} and others.
[^n2]: [RTR 20180719] [ANK 20211015] — Rules Director statements on the
    fail/end/cancel templates.
[^n3]: [RTR 20180719]; [LSJ 20041022] [ANK 20221205] — {Hide the Heart}.
[^n4]: [RTR 20180719] [ANK 20211015] — recorded on each card using the template.
[^n5]: [LSJ 20070709] [ANK 20221011-2] — {Red Herring}.
[^n6]: [RTR 20180719] [ANK 20170105] [ANK 20200207] — {Obedience};
    [LSJ 20011202-2] — {Krassimir}.
[^n7]: [ANK 20211015] [ANK 20210124] [LSJ 20090220] [LSJ 20070709] —
    {The Kiss of Ra}.
[^n8]: [LSJ 20080725] — {Obedience}; [RBK].
[^n9]: [LSJ 20060522] [LSJ 20060824] [LSJ 20080725] [LSJ 20090617] — {Obedience};
    [ANK 20180817] [PIB 20110915-2] — {Muricia's Call}, {The Summoning} (playing
    the retainer/ally directly later the same turn is not the same action).
[^n10]: [RTR 19950509] [LSJ 20080710] [ANK 20200502] — {Obedience}, {Change of
    Target}.
[^n11]: [LSJ 20011023] [RTR 20020501] — {Malleable Visage}.
[^n12]: [LSJ 20010627] — {Compel the Spirit}.
[^n13]: [ANK 20170202] — {Quincy, The Trapper}.
[^n14]: [ANK 20200515] — {Cloak the Gathering} and others; [LSJ 19990611] —
    {Sins of the Cauchemar}.
[^n15]: [LSJ 20020801] [LSJ 19980212] [RBK cancel-a-card] — group "Cancel an
    action" (G00061); [LSJ 20060425] — {React with Conviction}.
[^n16]: [ANK 20220401] [ANK 20211015] [ANK 20210124] — {Daring the Dawn}.
[^n17]: [LSJ 20081213-1] [ANK 20210124] — {Enkil Cog}.
[^n18]: [LSJ 20070709] [LSJ 20090220] [ANK 20210124] [ANK 20211015] —
    {Tangle Atropos' Hand}, {The Kiss of Ra}.
[^n19]: [RTR 20001020] [ANK 20200813-2] — group "Cancel an action" (G00061).
[^n20]: [LSJ 20110419] — {Crocodile's Tongue}.
[^n21]: [LSJ 20080611] [ANK 20210131] [LSJ 20010803-2] [ANK 20181003]
    [ANK 20220127] — {Crypt's Sons}, {Venenation}, {Bear-Baiting}.

### 3.6 Continue as if unblocked
<!-- {Form of Mist} and friends: modifiers stay in effect; no new block chance for
those who declined; per-block effects provided again on a second block
([LSJ 20010814-2] family); lost if a new combat is queued. -->

### 3.7 The action types in detail
<!-- One subsection per rulebook action: bleed; hunt (G00004, G00064); equip;
employ retainer; recruit ally; political action — including the full referendum
machinery: procedure & timing, votes vs. ballots (G00021, G00022), automatic
passing, {Charming Lobby}; leave torpor; rescue; diablerie & blood hunt. -->

### 3.8 Actions provided by cards and titles
<!-- G00035, G00042; NRA identity (see 3.5.2). -->

---

## 4. Combat

### 4.1 Sequence and rounds
### 4.2 Range
<!-- Setting range is exclusive ({Omael Kuman}). -->
### 4.3 Strikes
### 4.4 Damage
<!-- Property inheritance; strength base vs. bonus; environmental (G00017);
retainer damage (G00016). -->
### 4.5 Prevention and immunity
<!-- G00033, G00026; no carry-over; unpreventable vs. dodge. -->
### 4.6 Dodge
### 4.7 Strike: Combat Ends
### 4.8 Presses
### 4.9 End of round, end of combat, new combat
<!-- G00007; effects lost when new combat queued. -->
### 4.10 Weapons and equipment in combat
<!-- G00045/G00046/G00050; {.44 Magnum} "each combat". -->

---

## 5. Minions and Their States

### 5.1 Vampires
<!-- Capacity changes retroactive ({Orun}); circles (G00003); merge; creation
(G00054). -->
### 5.2 Lock and unlock
<!-- Wakes are not unlocks; G00005 scope; unlocking the unlocked triggers nothing. -->
### 5.3 Torpor
<!-- G00027; wounded; rescue/leave costs. -->
### 5.4 Burning minions
<!-- Who burned them; trophies; burn vs. removal. -->
### 5.5 Allies
<!-- Life vs. blood; "as a vampire" (G00011, G00018); {War Ghoul} limits. -->
### 5.6 Retainers
<!-- G00016, G00029; bearer. -->
### 5.7 Special minion classes and traits
<!-- Ghouls (G00044); animals (G00019); Imbued; slaves; Black Hand (G00012);
Red List; Scarce (G00043); True Brujah (G00041); infernal. -->
### 5.8 Titles
<!-- Contest, dormancy; sect changes ({Writ of Acceptance}); G00038, G00034,
G00037. -->

---

## 6. Methuselahs and the Game

### 6.1 Owner vs. controller
<!-- Cards return to owner's zones; control defines who acts and pays. -->
### 6.2 Taking control of minions
<!-- G00001 Temporary control; controller ousted; mid-action steals ({Temptation}). -->
### 6.3 Taking control of cards in play
<!-- Requirements don't apply; locquipments (G00047). -->
### 6.4 Leaving and re-entering play
<!-- What is remembered; G00008. -->
### 6.5 Pool, the Edge and ousting
<!-- Gain vs. loss vs. payment; {419 Operation}; G00015. -->
### 6.6 Master phase
<!-- Trifles; G00031; out-of-turn masters (see 1.8.6). -->
### 6.7 Influence phase and the crypt
### 6.8 Events and Gehenna
<!-- G00009. -->

---

## Appendix A. Glossary of wording templates

## Appendix B. Index of cited cards
