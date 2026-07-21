# VTES Extended Rules

> **Status: COMPLETE DRAFT — all 64 sections drafted (Phase 6). Not yet consistency-reviewed
> or reference-verified. `⚠ REVIEW` marks points needing judge confirmation.**

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
- A cross-reference to another section is written `§3.5`.
- Statements derived from rulings carry footnote markers; all footnotes are gathered in
  the [References](#references) section at the end of the document. Each lists the ruling
  reference IDs (e.g. `[LSJ 20090411]`) as links to the original ruling, `[RBK …]` as
  links to the [rulebook](https://www.vekn.net/rulebook), and names the card or group
  under which the ruling is recorded in the
  [rulings database](https://github.com/vtes-biased/vtes-rulings).
- Card-specific rulings are quoted as examples where they illustrate a general
  principle. Pure one-card text interpretations remain in the rulings database.

---

## 1. Cards

### 1.1 Card text and the rules

**Base rules.** Where a card contradicts the rules, the card takes precedence. [RBK important-terms-of-the-game]

#### 1.1.1 Mandatory and optional effects

A printed statement of fact applies automatically and its controller has no choice in the
matter, e.g. {Writ of Acceptance}, {Enchanted Marionette}.[^1-1-1] Only a clause the card
marks as optional — "may", "can", "optional" — is optional. {Changeling Skin Mask} carries both: the bearer has [OBF]
whether you want it or not, and burning the card for intercept is your choice.

An ability is mandatory unless the card marks it optional. {Renegade Garou} gets a
mandatory additional strike and an optional maneuver on the same line; {Lorrie Dunsirn}'s
press and additional strike are both mandatory.[^1-1-2]

A cost printed inside an effect is mandatory. {Vast Wealth} equips with the equipment
found and you pay for it even if the payment ousts you; {Serpent's Numbing Kiss} at
superior burns 1 blood.[^1-1-3] A printed cost reduction likewise cannot be declined,
e.g. {Frondator}.

An opportunity is not a compulsion. A card that lets a minion strike with a weapon does
not force the strike, e.g. {Bomb}, {Bundi}; a wake card lets its vampire attempt a block
but never requires it, e.g. {Wake with Evening's Freshness} ([§3.3](#33-blocking)).[^1-1-4]

A choice inside an effect is made when the effect resolves, not when the card is played,
e.g. the "up to 2 blood" on {Third Tradition: Progeny}.[^1-1-5] Who takes or declines an
optional effect on a card in play follows the card's wording, not control of the card: an
effect granted to "this vampire" is used by the vampire — hence by its current controller —
even on a master card another Methuselah played and still controls, e.g. {Perfectionist},
{Corporal Reservoir}.

#### 1.1.2 Applying a mandatory effect

A mandatory effect is applied at its timing point, before its controller passes the
opportunity to play effects, e.g. burning pool to {Anarch Revolt}.[^1-1-6] A player who has
passed that opportunity does not get it back because the effect was overlooked: {The Coven}
still moves to the predator and its controller cannot lock it retroactively.

Where a mandatory choice has no printed default and every player missed it, imposing one
of the choices after the fact is not a remedy, e.g. {Leandro}.

#### 1.1.3 "Cannot"

A "cannot" on a card is absolute. Where it names the cards it forbids, those cards cannot
be played at all, not even for no effect to cycle them: the {Blood Fury} template ("damage
from this strike cannot be prevented by cards requiring Fortitude [for]") stops the
opponent from playing [for] prevention entirely.[^1-1-7] {Rigor Mortis} bars playing an
additional-strike card even for a side benefit, e.g. {Acrobatics} for its dodge.

Where the "cannot" names an outcome instead, the play remains legal and only the outcome
fails. {Charnas the Imp} is immune to damage from its employer, but the employer may still
use effects that would normally damage it.[^1-1-8] A vampire under {Legacy of Caine} who
cannot gain blood still takes the hunt action; the blood he steals goes to the blood
bank.

A card naming an object it acts on cannot be played when no such object exists, e.g.
{Fractured Armament} with no equipment in play; futility alone is no bar. See [§1.6](#16-requirements) for that
distinction.[^1-1-9]

#### 1.1.4 Reading card text

"This minion" is the acting minion, "that minion" the target, e.g. {Big Game}.[^1-1-10]
Such referents are re-read as the effect resolves: two {Major Boon} cannot be burned on
the same bleed, because after the first "you" are no longer the Methuselah burning
pool.

### 1.2 Wording templates: periodicity, duration, triggers

#### 1.2.1 How often an effect may be used

"Once each turn" means once during each player's turn. "Once during each of your turns" is
the narrower form, e.g. {Maila}. Turn, master phase, unlock phase, action, bleed and
referendum all read the same way.[^1-2-1]

A limit keyed to an event is spent per occurrence, and the event can recur in one turn:
{Andre LeRoux} may be used on each successful bleed. An ability whose use costs a master
phase action is likewise spent per action, so extra master phase actions buy extra uses,
e.g. {Nahir}. An ability framed by a phase is spent for that phase: {Nonu Dis} may be used
once per master phase however many master cards are played in it.[^1-2-2]

Absence of a periodicity clause means no limit — {Maris Streck} may use her ability as
often as she can pay for it. A trigger condition is not a limit: {Slake the Thirst} may be
played several times on one blood gain.[^1-2-3]

The limit attaches to the card, not to the effect, so a second copy carries its own use
whatever the period, e.g. {Amulet of Temporal Perception}. See [§1.15](#115-cumulative-and-stacking-effects) for multiple copies
generally.[^1-2-4]

The limit travels with the card, not the holder: {Owain Evans, The Wanderer}'s use is spent
for that unlock phase even if control of him changes during it; a weapon's per-combat
allowance tracks the weapon ([§4.10.2](#4102-once-per-combat-once-per-round)); a spent
referendum ability is not restored by unlocking ([§3.7.5.3](#3753-polling-and-the-tally)).
A minion who takes an action over gets no fresh use of a per-action ability already used on
it.[^1-2-5] Per [§1.15](#115-cumulative-and-stacking-effects) a
once-per-action limit on *playing* a card binds the minion instead.

An effect marked "(limited)" is capped by the rulebook, not the card, and is not optional:
once a limited additional strike has been used this round, the card cannot be played for
its other clause, e.g. {Dust Up} [cel].[^1-2-6] The limit binds the action (or round), not
the minion: a substitute acting minion cannot use a limited effect if one has already been
used on the action ([§3.10.1](#3101-substituting-the-actor-in-an-announced-action)).[^1-2-15]
A canceled use spends no limit, and using a
card's ability through another card plays no card — see [§1.8](#18-playing-and-canceling-a-card) for both.

A referendum ability is usable once per referendum; which states it works from is
[§3.7.6.4](#3764-locked-and-torpid-vampires)'s.[^1-2-7]

Two actions provided by one source are not cross-restrictive; each may be taken once per
turn ([§3.8.1](#381-one-source-one-action)).[^1-2-8]

"Only once in a game" survives the card's return from the ash heap, so a replay effect
cannot bring it back, e.g. {Filchware's Pawn Shop}; burning a card for its votes is not
playing it.[^1-2-9] "Since your last turn" means between the end of your previous turn and
now: that turn does not qualify, the current one does.

#### 1.2.2 Duration of maneuvers and presses

A press or maneuver granted by a strike card is usable only during the round the card was
played, e.g. {Rigor Mortis}.[^1-2-10]

A maneuver granted by a card played on the action serves only the combat resulting from
that action, but a vampire who blocks a second time after the action continues gets the
grant again, e.g. {Eyes of the Beast}.[^1-2-11]

#### 1.2.3 Trigger and condition wording

"Reduced to X" names an event, not a state. {Anathema} does not fire on a vampire that
entered combat already at zero blood, fires on any loss in combat however caused, and does not fire
on diablerie.[^1-2-12]

A condition referring to the card's own effect is not satisfied by another effect producing
the same event: {Escaped Mental Patient} is not burned when another card grants him the
hand strike.[^1-2-13] An "either A or B" condition needs one branch completed in full;
partial progress on both does not combine, e.g. {First Tradition: The Masquerade}.

"When the action/bleed would be successful" is a timing window, not merely a condition
([§3.4.3](#343-the-would-be-successful-window) owns its sequencing).[^1-2-14]

### 1.3 Card types and multi-type cards

#### 1.3.1 Locquipments

An equipment card printed "represents a location and does not count as equipment while in play" is an equipment in hand, library and ash heap; both equipment and location as it is played; and only a location once in play, e.g. {Palatial Estate}.[^1-3-1]

Cost effects reach it under either wording, since the card is checked in hand and is both types at the moment it is played. An effect reducing the cost of locations applies, e.g. {Therbold Realty}; so does one reducing the cost of equipment cards, e.g. {The British Museum, London}.[^1-3-2] See [§1.7](#17-costs-and-payment) for cost reduction.

An effect that reads the type of a card already in play sees only a location. A search for an equipment card finds a locquipment in the library, e.g. {Magic of the Smith}; a search for a location does not, e.g. {Danylo}. An effect that moves "the equipment" after an equip action cannot move it, e.g. {Reg Driscoll}.[^1-3-3]

A vampire who cannot have or use equipment may still equip with a locquipment, e.g. {Enkidu, The Noah}. {Beast, The Leatherface of Detroit} also cannot play action cards, so a card must put it on him, e.g. {Vast Wealth}.[^1-3-4]

On a change of control the locquipment is re-placed or burned like other cards on minions ([§6.3.2](#632-where-the-card-is-placed)); an action targeting one is directed at the Methuselah controlling it ([§3.1.5](#315-directed-actions)).[^1-3-5]

#### 1.3.2 Multi-type cards

A card with two types is of the type it is played as, never both.[^1-3-6] {Adana de Sforza} reduces the cost of a [COMBAT]/[ACTION MODIFIER] card only when it is played as a combat card; {Conrad Adoula} reads a [REACTION]/[ACTION MODIFIER] card only when it is played as a reaction. A card offering a choice of disciplines is of the discipline it was played at, e.g. {Horrock}.

An effect that retrieves or counts cards by type reads the type the card was played as: {Henry Taylor} recovers {Swallowed by the Night} only if it was played as a combat card.

The printed type is unchanged by an unusual play route. A retainer employed through {Pack Alpha} is still an action card, so an effect reducing the cost of action cards applies, e.g. {Sunset Strip, Hollywood}.[^1-3-7]

Conversely, a card that provides an action of some type is not a card of that type. {Charming Lobby} calls a referendum but is not a [POLITICAL ACTION] card, so effects reading political action cards do not see it.

Whether a card keeps its type after being used is settled by its own text, not by a general rule. {Shackles of Enkidu} is still an equipment once it has been moved onto the opposing minion. {Enhanced Coagulant} prints replacement text on use and becomes typeless, so it is no longer a weapon.

#### 1.3.3 Clan equipment and reflex cards

A clan equipment already in play may be taken from the minion carrying it by a minion who does not meet its requirements; the equip-from-minion rulebook action is not a card play, so no requirement is checked. See [§1.6](#16-requirements).[^1-3-8]

A frenzy card that targets, selects, chooses or affects the minion when played counts as played on that minion.[^1-3-9]

### 1.4 Representation and placeholders

**Base rules.** Several cards put a card into play to stand in for something else — a
Master: Discipline card as a 1-capacity Sabbat vampire ({Shock Troops}), a library card as
a ghoul ally ({Absimiliard's Army}), an ash-heap minion as a wraith ally
({Khazar's Diary (Endless Night)}).

The representing card contributes nothing of its own. Its name, card type, cost, clan,
disciplines, text and unique status are all inert; the card is exactly what the effect that
put it there describes, and nothing more.[^1-4-1] An {Agent of Power} put into play by
{Shock Troops} is a non-unique clanless 1-capacity Sabbat vampire with no discipline, and
is not a Master: Discipline card while it is in play.

The placeholder sits in play face up, but anything looking for a card by name ignores the
printed name.[^1-4-2] A card merely stored on another card is out of play and sits face
down instead, e.g. {Père Lachaise, France} ([§1.11](#111-the-ash-heap)).

Placeholders do not contest. The same holds for any minion put into play under a
"does not contest" clause: it is a different card from an identically named minion in play,
for all purposes. {Jimmy Dunn (G2)}'s burn-the-first-Jimmy clause does not fire on an
illusionary Jimmy from {Illusions of the Kindred}.[^1-4-3] See [§1.13](#113-contests) for contesting.

Once the card leaves play it is read as printed again; what it represented is gone. A card
that was an ally in play is not an ally card in the ash heap and cannot be retrieved as one,
e.g. {Compel the Spirit} cannot reach a burned ally raised by
{Khazar's Diary (Endless Night)}.[^1-4-4] The same rule works the other way: a vampire card
that was a mummy ally under {Spell of Life} is a vampire in the ash heap, so {Possession}
reaches it and {Compel the Spirit} does not. No effect targeting a card in the ash
heap reads it as the thing it used to represent.

Standing in for something else does not launder a play restriction. An ability that lets a
minion count as having a required discipline substitutes only for that discipline; clan and
other printed restrictions still apply, e.g. {Reality Mirror}.[^1-4-5] See [§1.6](#16-requirements) for
requirements and requirement-faking.

### 1.5 Abilities and card plays

**Base rules.** Using an ability printed on a card already in play is not playing a card,
and is not taking an action.

#### 1.5.1 Ability use is not a card play

Costs and restrictions that attach to playing a card do not reach ability use. The [obe]
version of {Safe Passage} raises the cost of reaction cards, not of reaction powers.
{Secure Haven}'s surcharge applies to master cards played at the minion, not to using the
effect of a master already in play, e.g. {KRCG News Radio}.[^1-5-1]

An ability marked [REACTION] does not count as playing a reaction card, but it can be used
only when reactions can be used — unlocked, or with a wake effect, e.g. {Champion}. Card
text overrides the unlocked half: {Vigilance} is only usable by a locked imbued, so it
needs no wake and only the reaction window itself — during an action — applies.[^1-5-2] An
effect that merely lets a locked minion block is not a wake ([§5.2.3](#523-wakes-unlocking-and-blocking)).

#### 1.5.2 Locked bearers and torpor

Locking bars acting and blocking; it does not bar ability use. An ability stays usable
while its bearer is locked unless its own text requires the bearer to be unlocked, acting
or blocking, e.g. {Montano}, {Toby}. Where the ability costs a lock, only that
part needs the bearer unlocked: {Courier} lets you look at the card while locked and needs
the lock only to discard it.[^1-5-4]

Torpor bars no ability either: abilities remain usable there, including lock-to-use ones,
e.g. {Montano}, {Mariel, Lady Thunder}.[^1-5-5] Action modifiers are likewise not barred:
they carry no unlocked requirement ([§5.2.1](#521-what-a-lock-prevents)); what a vampire in
torpor can and cannot play is [§5.3.2](#532-what-a-torpid-vampire-can-still-do)'s.

#### 1.5.3 Ability use is not an action

A minion barred from acting may still use its abilities. A recruited ally cannot act the
turn it enters play, but it can use its abilities that turn, including ones that lock it,
e.g. {Draeven Softfoot}, {War Ghoul}. The same holds for a minion influenced out: its
ability is usable during that influence phase.[^1-5-6] See [§3.7.4](#374-employ-retainer-and-recruit-ally) for the recruit action
and [§5.2](#52-locking-and-unlocking) for the lock.

A vampire treated as an ally keeps abilities that let him play discipline-requiring cards,
and uses them on an ally's terms (see [§5.5](#55-allies)).[^1-5-14]

#### 1.5.4 Reuse

An ability may be used any number of times during a single action unless its own text
limits it, e.g. {Corpse Minion}.[^1-5-7] Three limits come from the wording. If use locks
the bearer or its source, it is once per unlock, e.g. {Forest of Shadows}, {Hukros}. If it
is keyed to a phase action, it is once per window available, e.g. {Josef von Bauren}. Any
other condition in the text is rechecked at each use: {Osric Vladislav} may repeat only
while he is acting and stealth is needed.[^1-5-8]

A once-each-turn ability is spent only if it actually applies. {Nergal}'s cost reduction is
not used when the action cannot be paid for even with it, or when the card is canceled as
played and no cost is paid.[^1-5-9]

#### 1.5.5 Timing, participation, prevention

An ability that modifies an action has action-modifier timing: usable at any point during
the action, including after block attempts conclude, e.g. {Pentex(TM) Loves You!},
{Spiridonas}.[^1-5-10]

An ability whose text is framed by combat requires its bearer to be a combatant, not merely
that a combat is occurring, e.g. {Watenda}, {White Lily}.[^1-5-11]

An ability granted by a card in play is unavailable while an effect prevents the bearer
from using that card: {Drawing Out the Beast} stops the vampire using {Drum of Xipe Totec},
so neither the [CEL] nor the maneuver it grants is available.[^1-5-12]

### 1.6 Requirements

#### 1.6.1 When a requirement is checked

A requirement is checked when the card is played and on each later play: {Undead Persistence} cannot be used twice in one combat.[^1-6-1] During an action it is checked continuously; a minion who stops meeting it *fizzles* the action: the action still resolves and, if unblocked, is successful and its cost paid, but it has no effect. One met at the time of the block stands if the acting vampire is later replaced.

A card already in play stays in play when its requirement lapses.[^1-6-2] A trait gained later applies to cards already in play if the card checks for it, e.g. {Orun}'s capacity bonus[^1-6-3], not if it's only checked when the card is played, eg. the discipline level for a retainer like {Raven Spy}.

#### 1.6.2 What counts as meeting a requirement

What "Only usable by ..." restricts depends on whether using the card is the same act as playing it. On a card that is played and resolves — action, action modifier, reaction, combat card — it bars the play: {Regeneration} cannot be played by an untorpid vampire. On a card that goes into play it gates only the conferred ability: a capacity-5 vampire can still equip {Seal of Veddartha} and gains its [dom] and [for] levels, but cannot use its bleed action.[^1-6-4]

Meeting a requirement is not possessing the trait: {Talaq, the Immortal} plays [qui] cards but has no [qui] and gains nothing from cards keyed to having it.[^1-6-5]

A card printing a clan and its antitribu as alternatives needs only one of the two, e.g. {Defender of the Haven}; a lone clan requirement is not met by the antitribu clan. A card requiring a Baron requires an Anarch.[^1-6-6]

#### 1.6.3 Cards entering play abnormally

Only "put ... in play" bypasses requirements, e.g. {Summon History}, {Compel the Spirit} [NEC].[^1-6-7] **Equip**, **recruit** and **employ** invoke the normal machinery, so requirements and cost apply as printed, e.g. {Concealed Weapon}, {Piper}, {Magic of the Smith}. Such a card has still been played; see [§1.8](#18-playing-and-canceling-a-card) for what it loses.

Where requirements are bypassed, a required discipline is used at inferior and a cost of X is zero.[^1-6-8] Cost is a separate check: {Bindusara, Historian of the Kindred} ignores requirements but pays cost; {Horrid Reality} pays none but burns the weapon if requirements are unmet.[^1-6-9]

Bypassing requirements does not bypass prohibitions: {Heidelberg Castle, Germany} cannot move equipment onto {Enkidu, The Noah}. A card placed where it cannot legally sit is burned without cost refund, though an effect it imposed on placement persists, e.g. {Wooden Stake}'s "does not unlock as normal". An ally's on-entry clause fires however it entered, e.g. {War Ghoul}.[^1-6-10]

Taking control of a card in play is not playing it, so requirements do not apply — see [§6.3](#63-taking-control-of-a-card-in-play).[^1-6-11]

A clause firing on equipping does not fire when the card is merely put in play: {Helicopter} comes locked when equipped, unlocked when {Alastor} places it.[^1-6-12] An ability modifying equipping or recruiting does apply to non-normal ones, e.g. {Little Tailor of Prague} with {Piper}. One keyed to the action applies only where there is an action: {Zhenga} triggers on announcing a recruit or employ action, so {Piper}'s actionless recruit is outside her ability, while a non-standard recruit that is an action is not.[^1-6-13]

The requirements and cost of a fetched card are not those of the fetching action: {CrimethInc.} cannot be used off {The Summoning} for an ally requiring an Anarch.[^1-6-14]

#### 1.6.4 Vampires that meet requirements they do not have

{Mata Hari} and her kind are treated as meeting the requirement for all effects of the card played, and only them, including its duration effects — never for what the card does from being in play.[^1-6-15]

The ability operates only on a card played normally, not for a {Piper} recruit or a {Concealed Weapon} equip.[^1-6-16] It operates only where the card prints the requirement, never to match a trait the card merely acts on, e.g. {Sacrifice}.[^1-6-17] It does not operate while the vampire is uncontrolled or in the crypt.[^1-6-18] Controlling such a vampire does not shut off burn options: a card in hand that only she could meet the requirement to play may still be discarded via its burn option.[^1-6-25]

Title requirements are the special case: sect membership, the choice of city, and {Vidal Jarbeaux}'s printed once-per-game caps are [§5.8.3](#583-how-requirements-read-titles)'s.

An ability granting a discipline for playing cards meets one, not both, of a two-discipline requirement, e.g. {Infernal Familiar}, {Grey Thorne}.[^1-6-20]

#### 1.6.5 Playing a card that will do nothing

A card may be played, and an action taken, knowing it will accomplish nothing, e.g. {Absorb the Mind} against a bloodless vampire, {Draba} on a minion already at 0 stealth.[^1-6-21]

Three families bar the play. A card whose text names the object it acts on cannot be played when no such object exists, e.g. {Shattering Blow} with no equipment, {Storage Annex} as the only card in hand, an empty crypt to draw from ([§1.9.4](#194-empty-crypt-hand-size)).[^1-6-22] Immediate damage prevention cannot be played with no damage to prevent, e.g. {Soak} — but a card granting a prevention ability for a duration is not immediate and may be played before any damage, e.g. {Apparition}, {Brother's Blood} ([§4.5](#45-prevention--immunity)).[^1-6-23] Stealth or intercept cannot be gained when not needed, e.g. {Bonding}. Reducing an opposing value already at its floor stays legal.

These bars are on the play only, and only on a play whose whole effect is the unneeded one. A card granting a standing effect may be played before the need exists: {Repulsion} [OBE] may be played though the stealth is not currently needed, and once on the vampire its +1 stealth applies on every action regardless.[^1-6-24]

### 1.7 Costs and payment

#### 1.7.1 When a cost is paid

An action's cost is paid at resolution, not at announcement; any other card burns its cost as it is played.[^1-7-1] An unblocked action is successful and its cost paid even when the effect cannot occur ([§3.4](#34-resolution-success-and-effect)).[^1-7-2]

An additional cost is paid at the same time as the cost it adds to. Where that cost is never reached — the action is blocked or canceled, the referendum fails — nothing is paid.[^1-7-3] A charge incurred per combat is incurred anew if a fresh combat begins: {Blithe Acceptance} burns its blood (or itself) again under {Psyche!}.

A cost charged for failing to block burns when the action begins to resolve, and reactions may still be played, and paid for, before that burn.[^1-7-4] Costs and triggered burns charged on the block itself are [§3.3.3](#333-the-cost-of-blocking)'s; a cost to *attempt* is per attempt and never retroactive, e.g. {Tenebrous Form}.

The cost of playing a card and the gain that card yields happen in one step, so no oust intervenes — even where another card imposed the cost, e.g. {Secure Haven}'s surcharge on a {Minion Tap}. Where paying does oust a player, resolve the oust before the effects that produced it ([§1.1](#11-card-text-and-the-rules), [§6.5](#65-pool-the-edge-and-ousting)).[^1-7-5]

#### 1.7.2 Cost arithmetic

Multiplication and division are applied first, then addition and subtraction.[^1-7-6] The modified cost is the card's cost for every other effect that reads it, and a reduction tied to a minion follows the card onto and off that minion.[^1-7-7] Modifications apply before affordability is checked, but paying from another source leaves the cost itself unchanged.[^1-7-8] Where a reduction and another cost effect could both fire, the controller chooses the order.[^1-7-9]

You must be able to pay the printed cost, even when the card returns more than it costs, e.g. {The Eternals of Sirius}, {Villein}; a reduction that brings the cost within reach makes the play legal.[^1-7-10]

Some cards have a cost of X, chosen by the player when paying. X may be zero, and "X" in the card's own text means the cost paid for that card. A card put into play rather than played has X of zero, whatever the fetching card announced, e.g. {Summon History}.[^1-7-11]

#### 1.7.3 Cost reductions

A "lock to reduce the cost" location may be locked at any point from announcement until just before the cost is paid. When the reduction is what makes the card affordable at all, it must be locked at announcement, e.g. {Sunset Strip, Hollywood}.[^1-7-12]

Read what the reduction is keyed to. A reduction on a card's cost applies however the card reaches play, including a retainer employed by {Pack Alpha}. A reduction keyed to an action does not apply where no action is taken, e.g. {Charisma}.[^1-7-13] A reduction on "cards you play" covers minion cards, which the Methuselah also plays; wording naming pool does not reach a cost paid in vampire blood, and the converse.[^1-7-14] Reductions reaching an equipment that is a location are [§1.3](#13-card-types-and-multi-type-cards)'s.[^1-7-15]

#### 1.7.4 Costs and "burn blood" effects

A "burn X blood" clause inside a card's effect is not a cost. Cost reductions do not touch it, and the card cannot be played if the minion cannot afford the burn, e.g. {Preternatural Evasion}, {Shadow Boxing}.[^1-7-16] An ability sparing a vampire the cost of a class of cards therefore does not spare a burn-blood effect printed on one, e.g. {Dragos} against {Chiropteran Marauder}.[^1-7-17]

An effect that adds to a card's cost is a cost: other reductions apply to it, and it reaches every card in the class it names, including cards played at end of round, e.g. {Terror Frenzy}.[^1-7-18]

#### 1.7.5 Paying what you can

Where a card names an amount to take from a target, take what is there, e.g. {Villein}, {Theft of Vitae}.[^1-7-19] Where the amount is a cost the payer cannot meet, the payment is still made as far as it goes and the effect it was to buy does not happen, e.g. {Sword of Nuln}.[^1-7-20]

A triggered burn does not gate the act, a cost does: an empty vampire blocks through a "vampires blocking … burn 1 blood" effect and burns what it has, but cannot attempt through a cost "to attempt to block", e.g. {Tenebrous Form} ([§3.3.3](#333-the-cost-of-blocking) owns the blocking case).[^1-7-21] An ally has life, not blood, and cannot pay a blood cost at all ([§5.5](#55-allies)). Where the payer chooses the source, choosing an empty one does not discharge the obligation, e.g. {Smiling Jack, The Anarch}.[^1-7-22]

#### 1.7.6 Whose cost, and paid in what

The requirements and cost of a card brought into play by another card are not the fetching action's ([§1.6](#16-requirements), [§3.7.4](#374-employ-retainer-and-recruit-ally)); the fetching card's cost is paid even if the search finds nothing.[^1-7-23] Where a card names who pays, that minion pays, acting or not, e.g. {Alastor}.[^1-7-24] Where a cost may be paid in blood or pool, or a choice of costs is offered, the player playing the card chooses.[^1-7-25]

A card-provided action does not carry the rulebook action's default blood cost, e.g. {Go Anarch}.[^1-7-26] Using an ability of a card in play is not playing a card, so an added cost on card plays does not reach it ([§1.5](#15-abilities-and-card-plays)).[^1-7-27] A canceled card's cost is [§1.8](#18-playing-and-canceling-a-card)'s.[^1-7-28]

The "keep … by repaying their pool cost" template ({Kindred Segregation}, {Peace Treaty}) repays the pool cost only: blood costs are not repaid, and a card with only a blood cost is kept for 0 pool. The controller may instead let the card burn, even where the amount is zero.[^1-7-29]

### 1.8 Playing and canceling a card

#### 1.8.1 The "as played" window

A card played from hand in the normal fashion can be canceled as it is played. The
cancellation must be immediate, and cards are not replaced during the window, so a
library-search master cannot fetch a canceller, e.g. {The Barrens}, {Dreams of the
Sphinx}.[^1-8-1] A wake effect is the one other card playable in the window; a reaction that
unlocks to attempt a block is not.[^1-8-2] A cancellation from an ability in play is
applied before anyone may play a further cancellation, e.g. {Andrew Stuart} pre-empting
{Direct Intervention}. A cancellation that is itself a card play opens its own window and
can be canceled there first — {Sudden Reversal} on the {Direct Intervention}.[^1-8-3]

The window opens on an out-of-turn master, on a combat card played at the end of a round or
"when combat would end", and on a modifier played after the action succeeds, e.g. {Voter
Captivation}.[^1-8-4] A card is cancelable as what it was played as: played with [obe] it
does not require [aus], e.g. {Hide the Mind}, {Iron Heart}.[^1-8-5]

#### 1.8.2 Played, but not in the normal fashion

A card brought into play by another card's effect has still been played. What it lacks is
only the normal-play window: it cannot be canceled as it is played. Cancellation reaches
only normal plays, minion cards and master cards alike — from hand, or "as if from your
hand" where a card says so, e.g. {Persistent Echo}, {The Erciyes Fragments} — not an ally
recruited by {Piper} or a weapon equipped by {Disguised Weapon}.[^1-8-6] Requirements and cost still
apply; see [§1.6](#16-requirements).

An effect that lets a minion *use the ability* of a card plays no card: no window opens, and
it does not consume his own once-per-action limit on that modifier, e.g. {Inscription},
{Shadow Court Satyr}. A cancellation in the used card's own text still applies, e.g. {Target
Vitals}.[^1-8-7]

When a card counts as played fixes when the window is. A political action card played from
hand by {Charming Lobby} counts as played only at successful resolution and so never becomes
cancelable; one retained by {Echo of Harmonies} is played normally and is.[^1-8-8]

#### 1.8.3 A canceled card has still been played

Cancellation stops the effect, not the play. The same reaction or modifier cannot be played
again by that minion, and a card limited to one per round cannot be replayed, e.g. {Immortal
Grapple}.[^1-8-9] Effects that count or retrieve cards played count the canceled one, e.g.
{Dabbler}, {Marthe Dizier}, {Perfectionist}.[^1-8-10]

The cost is still paid unless the canceling card says otherwise. Most say "its cost is not
paid", e.g. {Direct Intervention}; those that do not, do not, e.g. {Santaleous} — including
a blood cost imposed by {Terror Frenzy}.[^1-8-11] Where only part of an effect is canceled,
bids made are still paid and counters burned stay burned.[^1-8-12]

The card is replaced normally, and any "do not replace until" clause or alternate
replacement is canceled with it, e.g. {Steely Tenacity}.[^1-8-13] A canceled limited effect
does not trigger its limit, so another bleed or additional strike remains available; a
canceled Trifle grants no extra master phase action.[^1-8-14]

#### 1.8.4 What a cancellation reaches

Cancellation propagates downward only: canceling an effect cancels what that effect
provides, never the effect that provided it. Canceling a strike cancels the rest of the
strike card's effect, and the striking minion chooses another strike.[^1-8-15] Canceling a
maneuver does not cancel the strike that provided it — and that strike cannot be changed,
e.g. {Aid from Bats} — but does cancel a press the maneuver provides, e.g. the optional
press on {Masque of Judas}'s maneuver.[^1-8-16] Canceling an aim leaves the strike to
resolve on its default target, e.g. {Target Retainer}.[^1-8-17]

A canceled action is not performed and the acting minion stays unlocked, free to attempt it
again — likewise for an action card nullified as it is played, e.g. {Veil of Darkness}. An
action canceled *after* it has been played still counts against a "next X actions"
allowance.[^1-8-18]

#### 1.8.5 Playing for no effect

A card may be played, and an action taken, knowing it will accomplish nothing: a target
holding none of the resource the card acts on is legal, and reducing a value already at its
floor is a legal play, e.g. {Absorb the Mind}, {Draba}.[^1-8-19] Bars on such plays are
requirements, not futility, and belong to [§1.6](#16-requirements); [§3.4](#34-resolution-success-and-effect) covers whether the action succeeds and
locks.

A canceled play spends a use that attached to the play itself: the canceled card was
still played, so {Vidal Jarbeaux} has spent his once-per-game requirement. A use that
attached to an element the cancellation removed is not spent: no cost was paid, so
{Nergal}'s reduction never applied and his once-per-turn ability is not used
([§1.5.4](#154-reuse)).[^1-8-20]

### 1.9 Replacement

**Base rules.** A card played from hand is replaced immediately unless card text says
otherwise, and the draw comes after the "as played" window closes [RBK playing-a-card]
[RBK drawing-cards]. With an empty library you do not draw and play continues.

#### 1.9.1 When the replacement is drawn

The action card is replaced before any action modifier is played on that action.[^1-9-1]

Cards an effect requires you to supply from hand must be in hand at announcement, before
the replacement for the card demanding them is drawn: you cannot feed an effect with its
own replacement draw, e.g. {Charming Lobby}, {Gift of Proteus} ([§1.14.2](#1142-cards-named-from-hand) for naming).[^1-9-2]

An effect that discards or burns a set of cards from hand commits the whole set first and
replaces afterwards, e.g. {Angelica, The Canonicus}, {Call the Wild Hunt}.[^1-9-3] An
effect that repeats a draw-and-discard resolves one card at a time, e.g.
{Infernal Pursuit}.

#### 1.9.2 Delayed replacement

A card printing "do not replace until after this action" is not replaced when the action
is blocked; it is replaced when the action ends, after all combats.[^1-9-4]

A delayed replacement is drawn at the first moment its condition is met, ahead of any
other effect triggering then: before cards unlock ({Port Authority}), before other effects
keyed to the same torpor ({The New Inquisition} ahead of {Fame}), before a queued combat
begins ({Lucky Blow} ahead of {Psyche!}).[^1-9-5] The delay runs to its condition even if
the card has since been burned.

"Do not replace" effects stack with a card's own clause and the longest delay wins (cf.
[§1.15](#115-cumulative-and-stacking-effects)).[^1-9-6] Where two effects each offer a different replacement treatment, the
controller chooses, e.g. {Visit from the Capuchin} against {Steely Tenacity}.

An effect tied to the moment a card is played resolves at that moment, and a delayed
replacement is simply not there yet. That can reduce the effect — {Troglodytia} after
{Wash} sees the hand without the replacement — or negate it entirely:
{Agaitas, The Scholar of Antiquities}' ability applies only as the card is played, so any
delay prevents it. An effect keyed to the replacement itself waits for it, e.g.
{Learjet}.[^1-9-7]

#### 1.9.3 Abnormal entry and cancellation

A "do not replace until after this action" clause governs only a normal play ([§1.8.2](#182-played-but-not-in-the-normal-fashion)). A
card put into play in a special way is replaced immediately, even mid-action, e.g.
{Baseball Bat} played via {Concealed Weapon}; played normally the clause still governs,
even when the card reaches
play by another route during the resulting combat, e.g. {Gift of Bellona}.[^1-9-8] A card
played normally is replaced before its action resolves, so an ally recruited in the normal
fashion can be given cards drawn as its own replacement; one entering play by other means
cannot, e.g. {Corrupt Construction}.

A canceled card is replaced normally, its "do not replace until" or alternate-replacement
clause canceled with it ([§1.8.3](#183-a-canceled-card-has-still-been-played)).[^1-9-9]

#### 1.9.4 Empty crypt, hand size

A card whose effect draws from or moves a card out of a crypt cannot be played when that
crypt is empty — your own for {Illusions of the Kindred}, the blocker's for
{Bear-Baiting}.[^1-9-10] This is [§1.6](#16-requirements)'s missing-object family, not futility.

Cards not yet replaced count against hand size, and an effect that shows you a hand does
not show the card drawn to replace a discard from it. See [§6.9](#69-hand-draw--discard) for both.[^1-9-11]

### 1.10 Burn, removal from the game, and shuffling back

#### 1.10.1 Burn is not removal from the game

Burning a card and removing it from the game are separate events. A "when burned"
trigger does not fire when its object is removed instead: {Soul Gem of Etrius} does
nothing when its bearer is removed by {Golconda: Inner Peace}.[^1-10-1]

Read the printed order of the clauses. Where a card is burned and then removed, the
burn happened and every when-burned trigger fires — an {Absimiliard's Army} ghoul is
burned first, so {Tension in the Ranks} sees it. Cards controlled by an ousted
Methuselah are removed, not burned, so nothing triggers.

Where a card prints removal as its own disposition, an actual burn pre-empts it and the
card goes to the ash heap instead, e.g. an illusionary vampire burned in combat, or a
{Grasp the Ghostly} equipment burned before its pathos counters run out.[^1-10-2]

A card removed as part of resolving its own effect never reaches the ash heap, so
ash-heap retrieval cannot find it, e.g. {Summon Soul} at [NEC].

Cards removed from the game are public.

#### 1.10.2 "Burned" means burned from play

An effect keyed to a card being burned means burned from play, not any route to the ash
heap. A card discarded from hand has not been burned, and neither has an ally card whose
recruit action was blocked; {Resurrection} recovers neither.[^1-10-3]

The same test governs a shuffle-back clause: a card that shuffles into its owner's
library when burned is not shuffled back when it is discarded.

Such a card is burned first and shuffled back second, so other when-burned effects still
apply — {Set's Curse} still puts its ally into play when the minion it burns is
{Kherebutu}.

#### 1.10.3 Effects conditioned on a burn

A card whose effect is conditioned on a burn may be played when that burn will not
happen; see [§1.6](#16-requirements) for the permissive default. The conditioned part simply does not fire.
{Set's Curse} may be played on {Ilomba}, which redirects its own burn, but then nothing
is put into play. {Sacrificial Lamb} gains no blood and moves no equipment if the target
does not burn.[^1-10-4]

A card that burns itself at a stated moment does not burn if that moment is never
reached: {Bomb} used as a strike does not burn if combat ends before the strike resolves,
and a weapon out of play when a burn would apply escapes it ([§1.14.3](#1143-cards-out-of-play)).

A card that burns itself for want of counters is a counter-count question, not a burn
question; see [§1.12](#112-cards-and-counters-on-other-cards) for it.[^1-10-5]

#### 1.10.4 Crypt and library are separate

Crypt cards cannot be put into the library and library cards cannot be put into the
crypt. Continuous effects stop tracking a card shuffled back into the crypt, and any
effect standing on that card is voided ([§2.5](#25-duration-and-persistence)). Where one effect both discards and
shuffles the discards back, resolve all discards and draws first, then shuffle
([§6.9](#69-hand-draw--discard)).[^1-10-6]

An effect does not need the minion it names to remain in play. A contract can still be
used after its target — or the contract card itself — is burned, e.g. {The Black Throne};
a card keyed to what happened in the combat may be played after the minion it measures was
burned, e.g. {Taste of Vitae}; and a prohibition fixed on a card survives even that card's
own trip through the ash heap — {The Eternal Mask} still cannot be burned after its
vampire burned and returned. See [§2.5](#25-duration-and-persistence) for persistence.[^1-10-7]

### 1.11 The ash heap

The ash heap has no order. A player removing or taking cards from an ash heap chooses
them freely, e.g. {Trochomancy}, and the choice is visible to every player even when the
card is then placed face down, e.g. {Maabara}.[^1-11-7]

#### 1.11.1 Retrieval: what counts as played

A retrieval effect worded on "a card played" reaches only cards played the normal way. A
card brought into play by another card's effect is not retrievable by such an effect, e.g.
{Concealed Weapon}, {Charming Lobby}. That card has still been played ([§1.8](#18-playing-and-canceling-a-card)); the two
tests are separate. A card canceled as it is played counts as played and can be retrieved.
The action card of the action itself counts among the cards the acting minion played
during that action, e.g. {The Art of Memory}.[^1-11-1]

Burning a card is not playing it. A card burned from hand for a vote was not played (it is burned, but neither played nor burned from play; [§1.10.2](#1102-burned-means-burned-from-play)), and a
card in play burned by its own text was not played to call the referendum that burned it —
{Echo of Harmonies} cannot retrieve a {National Guard Support} burned that way.[^1-11-2]

#### 1.11.2 The ash heap is read when the effect resolves

A card that goes to the ash heap when played and is referred to later has no effect if it
has been removed from the ash heap before that moment, e.g. {Melange} when the vampire
blocks. A retrieval likewise finds nothing if its target has left the ash heap before the
retrieval resolves, e.g. {Echo of Harmonies} after {Delaying Tactics}.[^1-11-3]

A card diverted before it reaches the ash heap was never there. {Delaying Tactics} returns
the political action card to its owner's hand before it is burned, so a card played from
{The Erciyes Fragments} returns to hand rather than being removed from the game. A
retrieval naming a card in the ash heap cannot be played at all if that card was moved
elsewhere, e.g. {Compel the Spirit}.[^1-11-4]

#### 1.11.3 What a card is in the ash heap

A card in the ash heap is its own printed card, not what it represented in play. A library
card that became a minion in play is not a minion of that type there: {Jake Washington} is
no ally in the ash heap, and an action card that created a vampire leaves no vampire
there. A crypt card in the ash heap is a vampire whatever it represented in play, so a
burned {Spell of Life} mummy can be retrieved by {Possession} but not by
{Compel the Spirit} — and an ally that was represented by a crypt card cannot be retrieved
as an ally. An effect keyed to a card "burned from play" does not reach a card that was
never in play: a discard, or an ally card sent to the ash heap by a blocked recruit action,
does not qualify, e.g. {Resurrection}.[^1-11-5]

#### 1.11.4 Whose ash heap

A burned or discarded card goes to its owner's ash heap. A minion controlled by another
Methuselah passes through its owner's ash heap when burned, breaking all control effects,
e.g. {The Capuchin}; a stolen equipment burned in play returns to its owner's ash heap and
is not removed from the game unless an effect says so, e.g. {Grasp the Ghostly}. A
retrieval worded "your ash heap" means the ash heap you own — it does not matter who first
controlled the card, e.g. {Père Lachaise, France}. Effects may reach any player's ash heap,
and an action targeting one is always undirected ([RBK important-terms-of-the-game]; see [§3.1](#31-announcement-and-targets)
for this).[^1-11-6]

#### 1.11.5 The action card of a blocked action

A blocked action's action card goes to the ash heap. "Continue as if unblocked" moves it
back to limbo, and the action cannot be continued if the card is no longer in the ash heap,
e.g. {Ambulance}, {Foresee}. See [§3.6](#36-continuing-an-action-as-if-unblocked) for this.[^1-11-8]

### 1.12 Cards and counters on other cards

**Base rules.** Burning a card or removing it from the game burns any counters and cards
on it. Moving a minion between regions does not: cards and counters follow the minion and
are out of play while it sits in torpor or in the uncontrolled region.

#### 1.12.1 The host leaving play

A card on a host is burned when the host leaves play, whatever sends it away: burned,
removed from the game, returned to a hand, library or crypt, or set aside with no printed
provision for its cards.[^1-12-1] Cards on the initial target of a card effect burn like
any other, e.g. {Memory's Fading Glimpse} (host to the bottom of the crypt), {Raw Recruit}
(host set aside out of play). Two families of departures keep the cards instead,
out of play but intact: torpor, the uncontrolled region and contest, where they burn only
if the host is yielded or burned; and a set-aside whose own text carries them along, e.g.
{Descent into Darkness} ("this vampire and any other cards and counters on
them").[^1-12-8] A vampire that burns and returns comes back with nothing on it and is a
new minion for every purpose ([§6.4](#64-leaving-and-re-entering-play)).

A hosted card printing its own "burn this card if this vampire is about to leave the ready
region" clause resolves before the move. It burns even under an effect that would otherwise
keep cards on the vampire, e.g. {Righteous Aura} under {Banishment}.[^1-12-2]

Effects the hosted card already produced are not undone when it burns with its host, e.g.
{The Eternal Mask}. Counters it placed elsewhere keep working, e.g. {Tegyrius, Vizier}'s
allegiance counters. See [§2.5](#25-duration-and-persistence) for persistence.[^1-12-3]

#### 1.12.2 Status of a hosted card

A card put on another card is not in play, even where the host's text does not say so, e.g.
{Shadow Court Satyr}.[^1-12-4]

A card on a minion is controlled by that minion's controller, so it stays when the
Methuselah who played it is ousted, e.g. {Anathema}.[^1-12-5] It follows its host on a
change of control, and the new controller may use it. When it would move to an ash heap or
library it goes to the owner's, e.g. {Storage Annex} stolen.

A copy entering play into a contest resolves its enter-play effects before the contest
begins: a second {Mokolé Blood} puts its cards on itself first. A standing effect does not
apply: a second {Elder Library} contests without modifying hand size. See [§1.13.2](#1132-entering-contest) for
entering contest.[^1-12-6]

A retainer using a hosted weapon is not its bearer; see [§5.6](#56-retainers) for that.

#### 1.12.3 Counters on hosts

A card that enters play with zero counters and prints "burn this card when it has no
counters" burns immediately, e.g. {Secret Horde} put into play with X=0.[^1-12-7]

A counter moved onto a master card becomes the counter type that card uses, e.g.
{Goth Band}.

A threshold of counters "equal to the card's cost" reads the number, not the currency:
{Dominique} burns a location that cost X blood with X vandal counters, the same as one
that cost X pool.

### 1.13 Contests

**Base rules.** Contested cards are turned face down and out of play for the contest's
duration; a yielded card is burned. A contested *title* leaves its vampires in play and
acting normally, treated as having no title.

#### 1.13.1 What contests what

A contest needs two cards that are both unique and share a card name, whatever the card
type. The unique mummies made by {Spell of Life} contest each other and a unique vampire
of that name, but never the non-unique {Aabbt Kindred}.[^1-13-1]

A card whose text says it does not contest is treated as a different card for everything
that reads names, not merely spared the contest. Its duplicate title still votes, and an
effect triggered by a second copy of that name does not fire: an illusionary {Jimmy Dunn}
from {Illusions of the Kindred} does not make the real one burn himself. {Jimmy Dunn}'s
own "cannot be contested" works the same way, so a second copy may be influenced
out.[^1-13-2]

You can never choose to contest yourself. A play or choice that would do so is illegal: a
second {Visit from the Capuchin} cannot be played, and {Chain of Command} cannot bring out
two copies of one unique vampire. Where an effect forces the contest instead, the incoming
copy is burned, e.g. two {Parmenides} influenced in one turn.[^1-13-3] Vampires sharing a
name do not share a Blood Brother circle and never contest a circle ([§5.7.7](#577-blood-brother-circles)).

#### 1.13.2 Entering contest

Entry costs, cards placed on the card, and "as this enters play" abilities all resolve
before it enters contest, and only before. {Dr. Solomon Grey} burns his pool first; a
second {Mokolé Blood} collects its cards first; {Anarch Convert} may remove himself from
the game, averting the contest entirely.[^1-13-4]

The copy already in play leaves play when the contest starts, so its "if this leaves play"
clause fires: {Sonja Blue} is removed from the game, handing the contest to the incoming
copy.[^1-13-5]

#### 1.13.3 While contested

A contested card is out of play and nothing printed on it applies. A contested location
gives no hand size, whether printed on it ({Elder Library}) or counted by another card
({Guillaume Giovanni}); {Secure Haven} is not burned when its minion goes to torpor;
{Byzar}'s burn-replacement does not save him from being yielded.[^1-13-6]

A weapon taken into contest mid-combat is unusable by either side, and a strike already
chosen with it has no effect, e.g. {Disguised Weapon}.

An effect elsewhere that reads the contested card is suspended, not ended, and resumes
when the contest resolves, e.g. {Betrayer} naming a vampire who becomes contested. A
contested card carried by a minion that an effect moves out of play drops out of the
contest and re-enters it when the minion returns, e.g. {Descent into Darkness}.[^1-13-7]

Where a title is granted by a card in play, contesting the title turns that card face down
as well, e.g. {Fee Stake: Boston}, {Regent} ([§5.8.1](#581-printed-titles-granted-titles-contests)).[^1-13-8]

#### 1.13.4 After the contest

A card that comes back from contest is the same card: it remembers everything and effects
tracking it resume — {The Rack} gives its chosen vampire blood again
([§6.4.1](#641-set-aside-out-of-play--the-card-remembers-everything) generally; [§3.5](#35-action-repetition-nra-and-canceled-actions) for No Repeated Action).[^1-13-9]

A fresh copy of the same name is a different card, and a choice fixed on a copy that was
burned or yielded does not move to it. {The Rack} does not pick up the new copy, nor may
its controller re-choose merely because the chosen vampire became ineligible.[^1-13-10]

A card that leaves play through a contest is not burned by any minion, so nothing keyed to
a minion burning it applies ([§5.4](#54-burning-minions)).[^1-13-11]

### 1.14 Set-aside and announced cards

#### 1.14.1 When the card is named

An action that moves a named card out of your ash heap names that card when the action is
declared, not at resolution.[^1-14-1] This holds whether the action comes from a card, e.g.
{The Sargon Fragment}, or from a minion's own ability, e.g. {Pochtli}.

A search of your library declares nothing: the card is chosen at resolution, e.g.
{Magic of the Smith}.[^1-14-2] So is a choice belonging to an effect that only triggers
later, e.g. {Ashur Tablets}.

The card providing the current action is not itself available to that action. While it is
resolving it is in limbo — neither in hand nor in the ash heap — so it cannot be named
among the cards it retrieves, e.g. {Siphon}, {Sudario Refraction}.[^1-14-3]

#### 1.14.2 Cards named from hand

A card named from hand must be in hand when the naming card is played, before the
replacement for that card is drawn.[^1-14-4] It need not be shown: you may set it apart
face down, e.g. {Disguised Weapon}, {Charming Lobby}. The same applies where the
naming card takes a count rather than a name, e.g. {Gift of Proteus}.

Naming does not commit the card. If the action is canceled or fails, the named card stays
in hand and is not discarded, e.g. {Jack of Both Sides}. See [§1.8](#18-playing-and-canceling-a-card) for when a card
played this way counts as played; see [§3.5](#35-action-repetition-nra-and-canceled-actions) for cancellation.

A card playable "as if from your hand" is not in hand. An effect requiring a card in hand
cannot reach it: {Charming Lobby} cannot call a referendum off a political action card
held by {Echo of Harmonies}.[^1-14-5] Likewise, an effect that returns the political
action card played to call a referendum finds nothing when the referendum came from a card
in play, e.g. {Delaying Tactics}.

#### 1.14.3 Cards out of play

A card set aside face down under an effect is out of play. It is in no zone that discard
and burn effects reach, so it cannot be discarded or burned to satisfy another effect,
e.g. a card on {The Erciyes Fragments} against {Tension in the Ranks}.[^1-14-6] See [§1.12](#112-cards-and-counters-on-other-cards) for
cards placed on cards in play.

An equipment that is temporarily out of play is not burned by a scheduled burn that applies
while it is out.[^1-14-7] {Kerrie}'s ranged strike turns it face down until the end of the
action ({Dagger} likewise), so {Baal's Bloody Talons}' end-of-round burn misses it;
{Cleave}'s burn lands at the end of the action itself, where the acting Methuselah orders
it against the weapon's return. See [§2.4](#24-simultaneous-effects-and-ordering) for the ordering of the
several effects that resolve at the end of an action.

### 1.15 Cumulative and stacking effects

Multiple copies of the same card in play each exert their own effect and impose their own
cost. Two {Anarch Revolt} burn 2 pool in the unlock phase; two {First Tradition: The
Masquerade} burn 4 pool.[^1-15-1] Burn-pool and burn-blood requirements from any number of
sources are cumulative. Where a card offers an alternative to its cost, taking
that alternative once satisfies every copy — skipping a turn counts against all copies of
{First Tradition: The Masquerade}.

Numeric bonuses from multiple copies add, e.g. {Mass Reality} damage, {Orun}
capacity.[^1-15-2] An absolute value does not add: a card granting "X" rather than "+X"
sets its value, so multiple {Legacy of Pander} give a non-titled Pander 1 vote in total,
and {Torn Signpost} sets strength to 2 or 3 — which can even reduce it, e.g. a 3-strength
{Rock Cat} using it at [pot]. "+X" effects then add to the set value. {Orun} counts its
own copies by its own text: one vote per three. A vote bonus that is
not a title adds to the votes of a title gained later, e.g. {Xeper, Sultan of
Lepers}.

Each copy triggers and resolves on its own. Multiple copies of {Camarilla Exemplary} may
each name the same vampire, and multiple {Courier} each look at and discard a card in
succession.[^1-15-3] Copies attached to one minion are never merged: two {Kindred Society
Games} on a vampire cost 2 blood to unlock and move separately, and stealing a minion under
two {Temptation} burns the counters on only one of them.

An effect conditioned on having *any* counters is flat and does not scale with the count. A
minion with graft counters from {Dr. Morrow, The Skindoctor} gets -1 stealth, not -X
stealth; {Kahina the Sorceress} inflicts 1 damage however many corruption counters the
minion carries.[^1-15-4] The same holds for a trigger tied to an event rather than to a
magnitude: a vampire with several {Orun} burns one on a successful bleed for more than 2,
and each {Scorn of Adonis} costs a given Methuselah at most 1 pool however many "no" votes
that Methuselah casts.

Effects from *different* cards that grant the same discipline do not combine into the
superior level. An ally allowed to play [pot] cards by both {Leech} and {Putrescent
Servitude} still plays only [pot], never [POT].[^1-15-5]

A once-per-action limit on playing a card binds the minion, not the action. Different
minions may each play their own copy on the same action, e.g. {Cloak the Gathering},
{Suppressing Fire}.[^1-15-6] A limited effect binds the action itself; see [§1.2](#12-wording-templates-periodicity-duration-triggers).

Two copies of a card that imposes a mandatory directed action can deadlock the bearer: a
minion under two {Lunatic Eruption} is stuck and cannot act.[^1-15-7] See [§3.9](#39-mandatory-actions).

---

## 2. Timing and Sequencing

### 2.1 Effect windows and impulse

**Base rules.** The impulse is the opportunity to play the next card or effect. The acting
Methuselah plays first and gets the impulse back whenever anyone else uses a card or
effect; the window closes only when every Methuselah passes in turn.

#### 2.1.1 Where the impulse exists

An ability worded "when its controller has the opportunity to play effects" is usable at
every such point, including inside an action.[^2-1-1] Mandatory effects are applied before
their controller passes the impulse (see [§1.1](#11-card-text-and-the-rules) for this).

Permission to play one card outside its usual window opens no window for anything else: a
cancel card usable when there is no action does not thereby allow a wake effect.

#### 2.1.2 Who may play what

Only the acting minion plays action modifiers; only other Methuselahs' ready unlocked
minions play reaction cards. The window runs until resolution, so a modifier may still be
played after all block attempts are concluded.[^2-1-2]

The template "Only usable by a ready vampire other than the acting minion" widens which
minion plays the modifier, not which player. The card is still an action modifier and only
the acting minion's controller may play it, e.g. {Blanket of Night}, {Siren's Lure}.

A reaction card widens its user only as far as its own text goes. {Bliss} is usable by a
vampire not involved in the current combat, which includes a minion of a Methuselah not in
that combat at all.[^2-1-3] A [REACTION] ability is not a reaction card play but still
needs a reaction window; see [§1.5](#15-abilities-and-card-plays) for it.

#### 2.1.3 Effects resolve atomically

All effects are instantaneous except actions and certain combat effects. Nothing may be
played "in response" to an effect, and no window opens between the sub-steps of one
resolving effect, e.g. {Heidelberg Castle, Germany} cannot be locked in response, and
{Mask of a Thousand Faces} cannot be used during a referendum or during combat.[^2-1-4]

So a vampire chosen to go to torpor by {Baltimore Purge} cannot be unlocked between the choice and the torpor
by another effect; a vampire changing controller because of {Temptation} cannot be locked between the unlock
and the change of control; and life cannot be added in the middle of a single damage resolution step
({Vagabond Mystic}).

A card barred "during an action" is usable between two actions, including during another
Methuselah's turn, e.g. {Heidelberg Castle, Germany}; a card printing no such bar is usable
at any impulse, e.g. {Louvre, Paris}. A combat generated by an action modifier is still
part of that action, so no between-actions window opens between two such combats
({Siren's Lure}).[^2-1-5]

#### 2.1.4 Step windows

A card that changes how a step resolves must be played before that step resolves.
{Spirit Claws} affects the current strike only if played before strike resolution;
{Rötschreck} is played after a strike is declared and before resolution, in either strike
order. A card played on a diablerie may come before or after the Discipline card is taken,
but must precede the blood hunt.[^2-1-6]

A lock-to-reduce cost reduction may be applied at any point up to payment ([§1.7.3](#173-cost-reductions)). A card
in play that must be burned on an action is burned before that action resolves
({Melange}).

The "as the action/bleed would be successful" window is the last one before resolution
([§3.4.3](#343-the-would-be-successful-window)); redirection must precede it ([§3.7.1](#371-bleed)).[^2-1-7]

### 2.2 "As the action is announced" effects

**Base rules.** A card worded "only usable as the action is announced" must be played
before any regular action modifier or reaction card [RBK summary-of-the-course-of-an-action].

The window opens once the action card has been played and closes as soon as the first
regular action modifier or reaction card is played, by any player. No as-announced card
may follow it.[^2-2-1]

The timing is a property of the card's wording, not of its card type. Action modifiers,
reaction cards and cards already in play all carry it, e.g. {Car Bomb} [REACTION] and the
location {Yoruba Shrine}. The acting Methuselah has the first opportunity to play in this
window, as everywhere else in the action; see [§2.1](#21-effect-windows-and-impulse) for the general order.[^2-2-2]

The action card is played, and replaced, before the window opens. A card drawn as that
replacement may therefore be played as the action is announced. See [§1.9](#19-replacement) for replacement
timing.[^2-2-3]

Because the action card has already been played, an effect used in the window that
forbids playing cards does not reach it. {Concoction of Vitality} may be burned as the
action is announced even though the action was announced with a card requiring a
discipline, e.g. {Govern the Unaligned}.[^2-2-4]

The other end of the action has its own deadline and it is not this one: cards printed
"before action resolution" are barred once the "would be successful" window opens
([§3.4.3](#343-the-would-be-successful-window)).[^2-2-5]

⚠ REVIEW — an as-announced card is played before any block is attempted, so a player
grants stealth here without knowing whether it is needed. Whether [§1.6](#16-requirements)'s bar on gaining
stealth you do not need reaches this window is unsettled; {Predator's Transformation}
prints "+1 stealth, even if stealth is not yet needed", which suggests it does.

### 2.3 After resolution and after combat

**Base rules.** An action resolves before it ends. Cards keyed "after resolution" or "after
combat" are played in the gap between the two, while the action is still in progress.

#### 2.3.1 The post-resolution window

A card played after resolution is played during the action, not after it.[^2-3-1] Durations
running to the end of the action are still running: a minion taken control of until the end of
the action returns to its controller only once these effects are done, e.g.
{Spirit Marionette}. An oust does not close the window either — with {Last Stand} in
play, post-resolution effects are played before the turn ends. Being played during the
action, such a card can be canceled as it is played, e.g. {Ophidian Gaze} on
{Voter Captivation}.

Once a card keyed to resolution has been played, only cards with that same timing may follow.
Cards keyed to an earlier point — {Deflection}, {Archon Investigation}, {Conditioning} — must
precede it.[^2-3-2] A printed after-success effect on a permanent works the same way and does
not close the window: cards playable after resolution may still be played after
{Perfectionist} gains its blood. The window opens at resolution; the "would be
successful" window is earlier still and cannot follow it ([§3.4.3](#343-the-would-be-successful-window)).[^2-3-3]

Modifiers and reactions usable at the end of or after an action survive a failed action and
survive an intervening combat, e.g. {Champion}, {Car Bomb}, {Ensconced}.[^2-3-4] An action
that *ends* closes the window immediately and nothing may follow, e.g.
{Change of Target}. See [§3.5](#35-action-repetition-nra-and-canceled-actions) for the failed/ended distinction.

Two post-resolution cards put the action back in progress rather than adding to it:
{Follow the Blood} sends the reacting vampire into combat, {Momentary Delay} continues the
action as if unblocked. Other "after resolution" cards may be played before them, not
after.[^2-3-5]

#### 2.3.2 Ordering

The acting player chooses the order of effects played after resolution and after combat, and
may play further cards of that timing between them.[^2-3-6] Cards keyed "after combat" order
freely against one another, e.g. {Provision of the Silsila} and {Monster}.[^2-3-7]

Damage taken after resolution, e.g. {Force of Will}, and blood gained after resolution are
both inside the window; cards usable after resolution may be played before or after
them.[^2-3-8] Blood gained there is a gain like any other and triggers gain-keyed cards, e.g.
{Slake the Thirst}.

A reaction card that unlocks its vampire may be played after resolution to enable another
reaction card, e.g. {Wake with Evening's Freshness} into {Fast Reaction} after
combat.[^2-3-9]

#### 2.3.3 After combat

Cards keyed "after combat" are played once every combat generated by the action has been
handled, e.g. {Freak Drive}, {Cats' Guidance}, {Hay Ride}.[^2-3-10] Where the action resolves
before combat begins, "after resolution" effects wait until that combat ends ([§3.4](#34-resolution-success-and-effect)); the same
holds for a success-conditioned effect from a card played earlier in the action, e.g.
{The Art of Memory}.[^2-3-11]

#### 2.3.4 What resolution includes

An effect embedded in the action's own resolution happens before the window opens. A blood
hunt referendum called by the action's text is part of resolution, so "after resolution" cards
follow it and {Heidelberg Castle, Germany} — which cannot be used during an action — cannot be
used before it.[^2-3-12] A card keyed to the diablerie itself still fits between the diablerie
and the blood hunt, e.g. {Ritual of the Bitter Rose}.

### 2.4 Simultaneous effects and ordering

**Base rules.** When two or more effects apply at the same moment, the acting Methuselah
plays and orders first, then the impulse passes ([RBK sequencing]).

#### 2.4.1 Ordering within a window

The acting Methuselah decides the order of the effects available in a window, and may play
further effects in it before passing.[^2-4-1] Nothing else forces an order: cards playable
at the end of the round or "when the combat would end" may be played before or after one
another,[^2-4-2] and a limited bleed modifier or limited additional strike may be played
before or after an unlimited one.[^2-4-3]

Order is fixed only where a card says so. {Telepathic Tracking} at [AUS] cannot be played
after {Psyche!}; played first, combat continues and {Psyche!} waits for the end of the new
round.[^2-4-4] An effect that reads a value applies after every effect that modifies that
value, e.g. {Protected Resources} after all bleed modifiers.[^2-4-5]

Which window a card belongs to is [§2.3](#23-after-resolution-and-after-combat) and [§4.9](#49-end-of-round-end-of-combat-and-new-combats); ordering runs the same in each
([§2.3.2](#232-ordering), [§4.9.4](#494-after-combat)). An action that ENDS closes
its window at once, leaving nothing to order ([§3.5](#35-action-repetition-nra-and-canceled-actions)).

Across Methuselahs, whoever uses an effect first has priority and whoever uses one last has
the final say. In the "when a vampire should go into torpor" window the acting minion goes
first, and going first can lock the other side out — {Undead Persistence} denies
{Amaranth}, and the reverse.[^2-4-9]

#### 2.4.2 Order is a real choice

Effects resolve one at a time, so a later one can find nothing left to do: a second
{Anathema} is burned unresolved ([§1.15](#115-cumulative-and-stacking-effects)).[^2-4-10] Ordering also dodges a cost or a trigger
— apply a cost reduction before {Jenna Cross}'s surcharge, or burn the last non-Camarilla
vampire before {Judgment: Camarilla Segregation} bills you.[^2-4-11]

Where one effect could attach to any of several simultaneous applications, its controller
chooses which, e.g. {Slake the Thirst}.[^2-4-12] The clauses of a single card resolve in
printed order.[^2-4-13]

A replacement effect triggered by a minion burning resolves before effects that depend on
that burn, but a competing replacement may be played first, per sequencing.[^2-4-14]

#### 2.4.3 Cost and benefit

A cost paid and a benefit gained by the same effect happen at the same time; no oust
intervenes ([§1.7.1](#171-when-a-cost-is-paid)). Where the card offers the choice, take the gain first: gain pool from the
Edge, then burn it to remove {Sabbat Threat}'s counters.[^2-4-16] An oust resolves before
effects triggered by the burn that caused it ([§6.5.2](#652-when-the-oust-resolves)).[^2-4-17]

#### 2.4.4 Delayed effects triggered by a block

When a block triggers a delayed effect, no other effect may be used before it resolves,
e.g. {Millicent Smith, Puritan Vampire Hunter}, {Unleash Hell's Fury}. Effects triggering
at that same moment are still applied and ordered by the acting Methuselah; modifiers may
follow.[^2-4-18]

#### 2.4.5 Unlock phase

Cards unlock at the beginning of the phase, before any effect applied "during" it — so
{Baleful Doll}'s bearer is unlocked and can pay the lock cost.[^2-4-19] Held-back
replacements and control reversions resolve before unlocking and cannot be ordered among
unlock effects ([§1.9.2](#192-delayed-replacement), [§6.2.1](#621-when-the-control-change-happens)).[^2-4-20] Within the phase the
acting Methuselah orders his own effects freely, but must finish them before another
Methuselah gets the impulse.[^2-4-21]

#### 2.4.6 Effects that are not ordered

Some effects are simultaneous, not ordered. Two {Theft of Vitae} strikes net the gain
against the loss; no blood wears off.[^2-4-22] {Deep Song}'s lock and enter-combat are one
moment, and both are lost if the action ends first.[^2-4-23] Damage is prevented in
sequence — acting player first — but all of it is applied at once; see [§4.5](#45-prevention--immunity) for
prevention.[^2-4-24] Where two effects write the same trait, the most recent governs ([§5.9](#59-traits-and-trait-changes)).

### 2.5 Duration and persistence

#### 2.5.1 Effects with a stated duration

An effect granted for the duration of an action runs until the action ends. A combat the
action causes is inside it: the acting minion stays the same and effects applied during the
action still apply there. They also survive an action continuing as if unblocked.[^2-5-1]

An allowance given for one action ends with the action even when the card granting it stays
in play: {Eyes of the Beast}'s maneuver serves only that action though the card sits on the
vampire until the discard phase. Within the action it is not spent by being available —
{Marciana Giovanni, Investigator}'s beneficiary may burn the blood for intercept at any
point. A prohibition triggered by attempting to block runs from the attempt to the end of
the action, whether or not the block succeeds, e.g. {Valerius Maior, Hell's Fool}.[^2-5-2]

#### 2.5.2 Fixed at play versus read continuously

A value a card writes is fixed when the card is played and is not re-read. {Derange} takes
the clan and sect from the acting vampire at play; that vampire changing clan afterwards
does not move it. Counters added later do not change an X already set, e.g. {Leadership
Vacuum}. Removing the card restores the underlying value.[^2-5-3]

An effect whose text reads a trait on an ongoing basis re-reads it, including mid-action:
{Teresita, The Godmother} gains or loses her intercept if the acting vampire changes sect
during the action ([§5.9](#59-traits-and-trait-changes)). A relational referent is re-read at each use — {Victim of Habit}
keeps its named card when the prey is ousted and then works against the new prey.[^2-5-4]

A requirement is checked when the card is played and the effect continues after the vampire
stops meeting it, e.g. {Concordance}, {Cry Wolf}; see [§1.6](#16-requirements) for requirements.[^2-5-5] A trait
granted for playing a card covers that card's duration effects but not what the card does
from being in play ([§1.6](#16-requirements), the {Mata Hari} template).[^2-5-6]

A continuous grant addressed to a class of minions reaches members entering play later and
is not consumed by use, e.g. {Annabelle Triabell}, {Toreador Grand Ball}.[^2-5-7]

#### 2.5.3 Effects outliving their source

An effect already applied stands when its source leaves play. {Tegyrius, Vizier}'s
allegiance counters keep working after he leaves; {Camarilla Vitae Slave} grants its
discipline until the next master phase even if the retainer is burned or stolen.[^2-5-8]

An effect equally outlives the player or minion that produced it: {Shatter the Gate}'s
counters stay active after the acting Methuselah is ousted, and minions that equipped while
{NRA PAC} was in play unlock at end of turn whether or not it still is. A card in play keeps
working while its bearer is in torpor, e.g. {Nahir}'s hand size.[^2-5-9]

A card reaches only what happens after it is played. {Frenzy} does not undo equipment used
earlier in the round; {Kraken's Kiss} does not count damage inflicted before it; gaining or
losing {Sire's Index Finger} does not reach a frenzy card already played.[^2-5-10]

Whether a persistent effect ends with its source is decided by the card's printed duration
clause. {Rowan Ring} and {Wooden Stake} tie "does not unlock as normal" to the victim
remaining in torpor, so it holds after the weapon is burned or moved. {Rötschreck} states it
flatly in its own in-play text, so it ends when that card is burned or removed.[^2-5-11]

An effect naming a card as its object keeps tracking it across a change of bearer or
controller: {Horrid Reality} burns the weapon at end of combat wherever it now sits, and
{Imposing Phantasm} returns the blood even if the opposing minion changed
controller.[^2-5-12]

#### 2.5.4 Leaving play

A minion that goes to the ash heap loses every continuous effect on it, comes back a new
minion, and is lost track of by cards and effects, e.g. {The Capuchin}. Cards shuffled back
into the crypt are lost track of the same way. A minion that changes type loses the
continuous effects attached to its old form, e.g. {Demdemeh}'s retainers.[^2-5-13]

The uncontrolled region suspends rather than erases: cards, counters, titles and continuous
effects — even those worded for the rest of the game — resume on return, e.g. {Banishment}
([§6.4.1](#641-set-aside-out-of-play--the-card-remembers-everything)); suspended capacity modifiers are [§5.1.1](#511-capacity)'s.[^2-5-14]

---

## 3. Actions and Politics

### 3.1 Announcement and targets

#### 3.1.1 What is fixed at announcement

Every term the card calls for is named when the action is declared: the target, the counters spent, the card burned, the affected Methuselah.[^3-1-1] A lock-to-reduce cost reduction is not such a term: it may be applied at any point from announcement until just before the cost is paid ([§1.7.3](#173-cost-reductions)).

A card named as part of the announcement must be in hand at that moment, face down if you wish, and stays in hand if the action is canceled or fails; a card retrieved from your ash heap is named at declaration, while a library search chooses only at resolution. [§1.14](#114-set-aside-and-announced-cards) owns all of these.

A term fixed at announcement is not re-read later. Anarchs chosen while unlocked still count if they lock during the vote, e.g. {Revolutionary Council}; a target chosen when an equipment was played does not follow that equipment to a new controller, e.g. {Incriminating Videotape}.[^3-1-5]

#### 3.1.2 Declaration or resolution

Read the card. Some effects choose their object at declaration, others at resolution, and both can sit on the same card: {Break the Bonds} fixes the uncontrolled vampire at `[pre]` on declaration, the locked minion at `[obf]` on resolution.[^3-1-6] Which one applies decides what a target-protection or target-changing effect can reach.

An effect worded on the action being successful chooses its object then, e.g. {Keystone Kine}; so does a search that need not name what it fetches, e.g. {Magic of the Smith}.[^3-1-7]

#### 3.1.3 Legal targets

An action cannot be announced at all if the card requires an object and no legal one exists.[^3-1-8] But the object need only exist — it need not be able to yield the full effect. A vampire with no blood is a legal choice for a blood-stealing action, and if the target holds less than the announced amount at resolution you take what is there, e.g. {Siphon}, {Villein}.[^3-1-9] See [§1.7](#17-costs-and-payment) for the amount, [§1.6](#16-requirements) for the general no-effect rule.

If some of the intended objects cannot be targeted, the announcement stands and the action simply has no effect on those, e.g. {Edged Illusion}.[^3-1-10]

An effect granting an action or a block does not lift the normal prey, predator and target restrictions; see [§3.3](#33-blocking) for the blocking side.[^3-1-11]

#### 3.1.4 Choosing is targeting

A directed action that chooses, selects or names a minion targets it: protection effects bar it and cost increases apply, e.g. {Spirit Marionette} against {Secure Haven}, and a master card that chooses a vampire pays its extra pool, e.g. {The Rack}. The same test decides whether a frenzy card is played "on" a minion. An action targeting a retainer, equipment or other card on a minion does not target the minion, and neither does a card elsewhere that merely named him.[^3-1-12]

An effect that resolves outside an action targets nothing: an unlock-phase choice reaches a minion under {Secure Haven}, e.g. {Baltimore Purge}.[^3-1-13]

#### 3.1.5 Directed actions

An action directed at a card controlled by another Methuselah is directed at that Methuselah; it is undirected if you control the target.[^3-1-14] So an action against an equipment, retainer or location is directed at the Methuselah controlling it, not at the minion carrying it, e.g. {Conceal}, {Haunt}.[^3-1-15]

Read the reacting card's own wording. {Abbot} grants intercept during actions directed at its controller, so it applies to those; {Detect Authority} requires an action directed at a minion or location, so it does not. An ability keyed to directed actions never fires against actions by its own controller's minions.[^3-1-16]

Acting on another Methuselah's ash heap is not a directed action — the ash heap is not a card in play, e.g. {Daemonic Possession}. Neither is a referendum, so {Secure Haven} gives no protection against a vampire being chosen by one, e.g. {Banishment}.[^3-1-17]

An action with several targets is directed at every Methuselah controlling one of them, e.g. {Sowing Dissension}.[^3-1-18] A reactive effect keyed to being targeted applies if any one target of the action would enable it, e.g. {Chanjelin Ward}; where such an action's effect then names a single minion, that minion must be controlled by one of the target Methuselahs, e.g. {Weigh the Heart}.[^3-1-19]

### 3.2 Stealth and intercept

**Base rules.** Stealth may be added only while the action is being blocked by a minion
with enough intercept to stop it; intercept only by a blocking minion whose intercept is
below the acting minion's stealth. [RBK stealth-and-intercept]

#### 3.2.1 Adding what is not needed

A card that adds stealth or intercept cannot be played when the value is not needed, e.g.
{Bonding}, {Mask of a Thousand Faces}. The restriction reaches an ability that adds it as
well, e.g. {Osric Vladislav}.[^3-2-1] See [§1.6](#16-requirements) for the rule; this is its main instance.

Need is a threshold, not a cap. Once some intercept is needed the minion may take more
than it needs, e.g. {Angelica, The Canonicus}. Printed text waives the restriction where
it says so — "even if intercept is not yet needed", e.g. {Phased Motion Detector},
{Under Siege}.[^3-2-2]

#### 3.2.2 Reducing the opposing value

Reducing is always legal, including against a minion already at 0 or negative, where it
simply has no effect, e.g. {Draba}, {Night Terrors}. Such a card may be played by a minion
that is not attempting to block. Reducing stealth "to 0" is a -X stealth modifier on the
action, X fixed at the time the card is played; stealth added afterwards is added to the
reduced value.[^3-2-3]

#### 3.2.3 The restriction is on the play, not on the effect

A "cannot use it if you do not need it" restriction attaches to playing the card, never to
a continuous effect from a card already in play. {Repulsion} played as an action modifier
for +1 stealth is restricted like any other. Once the [OBE] version is on the vampire, its
standing +1 stealth applies on every action, needed or not.[^3-2-4]

#### 3.2.4 Duration and re-evaluation

Modifications last for the duration of the action [RBK stealth-and-intercept]. An option to
add, granted during the action, likewise stays open until resolution, e.g.
{Marciana Giovanni, Investigator}.[^3-2-5]

Having intercept is not permission to block. {Marciana Giovanni} may lock to grant herself
the option, and may do so from torpor, but still needs a wake to attempt the block. Once a
card is attempting to block, its intercept is modifiable like any minion's, e.g.
{Unleash Hell's Fury}.[^3-2-6]

A bonus conditioned on the action's target is satisfied by any one qualifying target, e.g.
{Talley, The Hound}; "directed at their controller" covers actions directed at cards that
controller owns, e.g. {Abbot}. A bonus conditioned on a trait is re-read if the trait
changes mid-action, e.g. {Ministry} — see [§5.9](#59-traits-and-trait-changes) for that.[^3-2-7]

#### 3.2.5 Who plays it, when, and how often

Action modifiers are the acting Methuselah's to play. A card usable by a vampire other than
the acting minion still requires that vampire be under the same control, e.g.
{Cloak the Gathering}; different minions may each play a copy on the same action
([§1.15](#115-cumulative-and-stacking-effects)).[^3-2-8]

The window does not close when one side passes. Intercept may still be added after the
acting Methuselah declines to add stealth, e.g. {Guardian Vigil}, and playing a modifier
that changes neither value leaves it open, e.g. {Inspire Greatness}. Sequencing puts the
targeted Methuselah's declaration first ([§3.3.2](#332-declaring-and-declining)). Failing
to block for want of intercept is still declining to block ([§3.3](#33-blocking)).[^3-2-9]

How often a stealth or intercept effect may be used is fixed by its own wording: once per
action, e.g. {Phased Motion Detector}; repeatable, e.g. {Matteus, Flesh Sculptor}; once per
unlock where locking is the cost, e.g. {Starshell Grenade Launcher}. See [§1.2](#12-wording-templates-periodicity-duration-triggers) for the wording
templates.[^3-2-10]

### 3.3 Blocking

#### 3.3.1 Who may block

An effect that lets a minion ignore the prey, predator or target restriction reaches only
that check. Every other condition on blocking still applies, including a prior decision not
to block, e.g. {Eagle's Sight} [AUS], {Anneke}.[^3-3-1] It covers one block attempt; if the
action later continues as if unblocked, another is needed ([§3.6](#36-continuing-an-action-as-if-unblocked)).[^3-3-2] Blocking "as an
ally" is the same shape — [§5.5](#55-allies).

The unlock-to-block template ({Guard Duty}, {Second Tradition: Domain}):

- Unusable when that vampire could not attempt to block the action anyway ({Daring the Dawn}).[^3-3-3]
- Unlocking to block does not lift the prey, predator or target restriction.[^3-3-4]
- Usable by a vampire already attempting to block, including a locked one that woke earlier.[^3-3-5]
- If the unlock leaves the action with no suitable target ({Ambush}), the block attempt and the
  resulting combat still happen.[^3-3-6]

#### 3.3.2 Declaring and declining

Sequencing governs the block window: a Methuselah who is not the target must wait until the
targeted Methuselah declares whether he attempts or declines to block. Using a card in play
is bound the same as playing one from hand, e.g. {Hide the Heart} [VAL], {Draba}.[^3-3-7]

Playing a card worded "after blocks are declined" declines the block for its controller, and
a block attempt that already failed against stealth counts as declining for those cards,
e.g. {Archon Investigation}, {Deflection}.[^3-3-8] Waking or unlocking to block compels
nothing: the vampire need not attempt to block nor play further reaction cards.[^3-3-9]

A declared attempt cannot be withdrawn — the minion is still attempting to block after a
stealth modifier lands ({Faceless Night} [OBF]).[^3-3-10] An effect imposing a blood cost to
attempt is the exception: a minion already attempting may resign instead of paying
({Tenebrous Form} [OBT]).[^3-3-11] Locking or taking control of the blocking minion
mid-attempt fails the attempt.[^3-3-12]

Declining belongs to the Methuselah, not to the minion. Taking control of a minion mid-action
does not undo its former controller's declination, and the new controller may block with it
if he has not declined.[^3-3-13] Being made to enter combat with the acting minion is not
blocking ({Brujah Frenzy}); substituting another minion into the block-induced combat leaves
the block standing, so the blocker still locks.[^3-3-14]

#### 3.3.3 The cost of blocking

Read the wording. "Must burn 1 blood to attempt to block" is a cost, so a minion who cannot
pay cannot attempt, e.g. {Dominion}, {Tenebrous Form} ([§5.5](#55-allies) for allies).[^3-3-15] "Vampires
blocking this vampire burn 1 blood" is an automatic effect: an empty vampire still blocks and
burns what it can, e.g. {Archon}, {Dónal O'Connor}. That burn happens immediately on the
successful block, whether or not combat follows.[^3-3-16]

A restriction triggered by attempting to block runs for the duration the card prints, and a
failed attempt does not cut it short ({Blessing of Chaos} [dem]). A cost worded as a state —
"while attempting to block" — stops once the attempt has failed, so it never reaches the
action card's cost ({Libertas}).[^3-3-17]

#### 3.3.4 After the block succeeds

Locking the blocker and entering combat are the two simultaneous consequences of block
resolution, not of the attempt succeeding. Cards timed "before block resolution" fill that
window ({Change of Target}, {Angel of Berlin}). An effect that ends the action or cancels the
block there prevents both consequences ({Clan Loyalty}); canceling only the combat does
not — [§3.5](#35-action-repetition-nra-and-canceled-actions).[^3-3-18]

Effects triggered by the block fire once the block would be successful; ending the action
afterwards does not undo them ({Aching Beauty}, {Unleash Hell's Fury}). An effect that makes
the action resolve as if unblocked instead means no block was successful, so effects
conditioned on a successful block never fire ({Lesser Boon}).[^3-3-19] An effect keyed on a
block does nothing when none occurred ({Spiritual Protector}).[^3-3-20]

A delayed effect triggered by the block resolves before any other card may be used;
simultaneous triggers are ordered normally ([§2.4.4](#244-delayed-effects-triggered-by-a-block)).[^3-3-21] A rider granted for blocking applies only in the block-induced
combat, not in a later one ({Guard Dogs} [ANI], [§4.9](#49-end-of-round-end-of-combat-and-new-combats)).[^3-3-22] Methuselahs who had already
declined get no fresh opportunity when the action continues as if unblocked — [§3.6](#36-continuing-an-action-as-if-unblocked).[^3-3-23]

### 3.4 Resolution, success and effect

**Base rules.** An action that survives all block attempts is successful; its cost is then
paid and its effects take place. [RBK resolve-the-action]

#### 3.4.1 A successful action need not do anything

An unblocked action is successful even when its effect cannot happen. The cost is still
paid.[^3-4-1] The usual causes are a target that no longer qualifies at resolution, e.g.
{Ambush} when the target unlocks, and a target removed or protected by another effect, e.g.
{Warsaw Station}. A stolen target keeps the action pointed at it; the action ends with no
effect only if that target has become illegal, e.g. {Temptation}.

An action provided by an equipment the acting minion no longer bears at resolution ends
with no effect, though still successful if unblocked ([§3.8.3](#383-losing-the-source)).

The target ceasing to qualify does not end the action: block attempts and any resulting
combat happen as normal, e.g. {Coterie Tactics}.[^3-4-3] An acting minion that stops meeting
the action's own requirement fizzles it the same way — successful and paid, but no effect
([§1.6.1](#161-when-a-requirement-is-checked)). Only a requirement unmet when the card is
played bars anything, and what it bars is the play itself ([§1.6](#16-requirements)).

Riders conditioned on the action being successful fire on such an action. {Forced March}
and {Instantaneous Transformation} unlock; {Perfectionist} gains the blood; {Hrothulf}
burns the Edge.[^3-4-4]

Where a card names the effect rather than the success, the effect must actually occur.
{Abactor} calls its blood hunt only after "successful resolution", meaning unblocked *and*
blood gained.[^3-4-5] A hunt is unsuccessful if no blood is gained, though the hunt action
itself succeeded, e.g. {Hospital Food} — as a bleed reduced to zero is unsuccessful on a
successful action ([§3.7.1.2](#3712-reduction-and-pool-burned), [§3.7.2](#372-hunt)).[^3-4-6]

An effect that cannot apply to part of what it names applies to the rest, e.g.
{Edged Illusion} against minions another effect protects, or {Enticement} when the Edge is
gone before resolution.[^3-4-7] (See [§1.7](#17-costs-and-payment) for amounts: a steal or transfer template takes what
is there.)

An action card whose effect is nullified before the action begins produces no action at all:
the vampire does not lock and may act again, e.g. under {Veil of Darkness}.[^3-4-8]
[RBK wording-templates]

#### 3.4.2 What is read at resolution

Choices and values the effect depends on are made at resolution, not at announcement, e.g.
the minion taking the corruption counter from {The Platinum Protocol}, the blood moved by
{Third Tradition: Progeny}, the disciplines copied by {Dual Form}.[^3-4-9] A library search
provided by an action happens only once the action succeeds, e.g. {Magic of the Smith}; an
additional cost imposed on the action is likewise not paid if it fails, e.g.
{Tryphosa}.[^3-4-10]

An effect keyed to the action *reaching* resolution fires even where the action does
nothing, or ends before combat, e.g. {Daring the Dawn}.[^3-4-11]

An action that puts its acting minion into combat resolves first. Effects timed "after
action resolution" wait until that combat ends, e.g. {Strix}.[^3-4-12]

#### 3.4.3 The "would be successful" window

Once all blocks are declined, a card usable "when the action/bleed would be successful" may
be played, e.g. {Spying Mission}, {Andre LeRoux}, {Dis Pater}. After one is played the
action is about to resolve: only other cards with that same timing may follow.[^3-4-13]
Anything that changes or defeats the action — {Deflection}, {Archon Investigation},
{Telepathic Counter} — must be played before that point.[^3-4-14] The post-resolution
windows sequence the same way ([§2.3](#23-after-resolution-and-after-combat)).

A bleed reduced to zero is not successful, so a "would be successful" card cannot then be
used on it.[^3-4-15]

### 3.5 Action repetition (NRA) and canceled actions

**Base rules.** A minion cannot perform an action with the same action card, from hand or in play, more than once each turn, even if it unlocks; a minion cannot bleed more than once each turn. [RBK action-card-or-card-in-play] [RBK bleed]

#### 3.5.1 Reached resolution

The No Repeated Action rule bites once the action reaches resolution. An action that fails, or that is ended by a card or an ability, has reached resolution: the same minion cannot attempt it again this turn, e.g. {Change of Target}, {Champion}, {Krassimir}.[^3-5-1] Being blocked and failing still counts as the attempt. An action continued after a reaction made it fail still fails.

A canceled action has not reached resolution. It is not performed, the minion does not lock, its cost is not paid, and the same minion may attempt the same action again, e.g. {Tangle Atropos' Hand}.[^3-5-2] It may not if the action was blocked and then continued before the cancellation.[^3-5-3]

The action was nonetheless taken, so it counts against effects that count actions, e.g. {Enkil Cog}, {Veil the Legions}.[^3-5-4]

Cancellation undoes the cost of the action: an {Enrage}d vampire canceled mid-action does not burn 2 blood.[^3-5-5] Failure does not — {Mobile HQ, Operation Antigen} stays locked when the action it paid for fails. A minion locked by a card in play to take an action canceled as it is played stays locked, and may act again or let the effect be lost.[^3-5-6]

#### 3.5.2 "The same action"

{Change of Target}, {Obedience} and {Red Herring} forbid repeating "the same action". Two actions are compared as follows.

- Rulebook actions (bleed, hunt, equip, …) are never the same as an action from a card, played or in play.[^3-5-7]
- Two rulebook actions differ if their targets differ. Equipping from a minion targets the equipment: same equipment, same action.[^3-5-8]
- Actions granted by two different cards in play are not the same, even if the cards share a name.[^3-5-9]
- Substituting the acting minion mid-action does not change who took it, e.g. {Malleable Visage}.[^3-5-10]
- A minion that leaves play and returns is a new minion, bound by nothing its previous incarnation did, e.g. {Compel the Spirit}, {Soul Gem of Etrius}.[^3-5-11]
- Putting a card into play, or being made to recruit or employ out of turn, is not performing that card's action, so the normal action is still available, e.g. {Piper}, {Muricia's Call}, {Clandestine Contract}.[^3-5-12]

#### 3.5.3 Ended and failed

An action that **ends** ends immediately. No further action modifier or reaction can be played and no other effect intervenes, e.g. {Mirror Walk}, {Tangle Atropos' Hand}.[^3-5-13] Where the effect starts a combat instead, combat begins immediately with the same window closed, e.g. {Brujah Frenzy}.[^3-5-14]

An action that **fails** also ends, but modifiers and reactions usable at the end of, or after, an action can still be played, e.g. {Detect Authority}, {Mistaken Identity}.[^3-5-15] A failed action was not blocked, so cards requiring a block cannot be played, e.g. {Freak Drive}, {Mirror Image}.[^3-5-16]

Effects scheduled for resolution or later are lost if the action ends first: the lock-and-enter-combat of {Deep Song}, the after-resolution combat of {Siren's Lure}.[^3-5-17] Likewise, an action whose acting minion is not ready when it would resolve simply ends — [§3.7.5.1](#3751-the-referendum-is-part-of-resolution) owns the referendum case.

Damage a card inflicts on its own acting vampire applies if the action reached resolution, even though it ended before combat; it does not apply if the action was canceled, e.g. {Daring the Dawn}, {Force of Will}.[^3-5-18] A block that would have been successful still triggers its effects even if the action ends first ([§3.3.4](#334-after-the-block-succeeds)).[^3-5-19]

#### 3.5.4 Canceled blocks and canceled combats

A canceled block attempt is neither successful nor unsuccessful. It is simply canceled.[^3-5-20]

Canceling the combat that a successful block created leaves the action blocked. The blocking minion stays locked, {Mask of a Thousand Faces} cannot take the action over, and reaction cards pertaining to that combat cannot be played afterwards, e.g. {Venenation}, {Bear-Baiting}.[^3-5-21] An effect that continues the action as if unblocked still works ([§3.6](#36-continuing-an-action-as-if-unblocked)), e.g. {Crypt's Sons}.

#### 3.5.5 Scope of cancellation

A canceled card is still played, so a cancellation does not give back the play: a canceled out-of-turn master still bars another against that master phase ([§6.6](#66-master-phase)).[^3-5-22] But a canceled *limited* effect does not trigger the limit, and another limited effect can be used.[^3-5-23]

Canceling a card that carried a choice returns the choice, and the same choice may be made again — a minion whose strike is canceled must still choose a strike and may play the same card.[^3-5-24]

Cancel effects reach every action card, including employ retainer, recruit ally and political actions.[^3-5-25] They reach only cards played from the hand in the normal fashion, so a weapon equipped via {Disguised Weapon} or an ally recruited via {Piper} cannot be canceled ([§1.8](#18-playing-and-canceling-a-card)).[^3-5-26]

Multiple copies of one action modifier played by different minions on the same action are a stacking question, not a repetition one ([§1.15](#115-cumulative-and-stacking-effects)).

### 3.6 Continuing an action as if unblocked

**Base rules.** A successful block locks the blocker and sends both minions into combat; the
action card is set aside out of play until the action resolves. Once a Methuselah declines
to make further block attempts, that decision is final. [RBK summary-of-the-course-of-an-action]

#### 3.6.1 What continuation restores

Continuation moves the action card from the ash heap, where it went when the action was
blocked, back to limbo. If the action card is not in the ash heap, the action cannot be
continued.[^3-6-1]

All action modifiers and reaction cards played earlier in the action remain in effect,
including those that pertained to the successful block.[^3-6-2]

Methuselahs who had already declined to block get no fresh opportunity. A Methuselah who
had not yet passed may still attempt to block, and a minion who blocked may block
again.[^3-6-3]

An effect that penalises a minion for not blocking ignores blocks made before it was
played, e.g. {Forced Awakening}, {WMRH Talk Radio}.[^3-6-4]

A card whose effect is one block attempt is spent by that attempt; another copy is needed
to attempt the second block, e.g. {Eagle's Sight}, {Falcon's Eye}. Effects that apply for
the duration of the action are not spent this way ([§3.2](#32-stealth-and-intercept), [§3.3](#33-blocking)).[^3-6-5]

#### 3.6.2 When the action cannot be continued

Only a combat induced by a block can be left this way. An action cannot continue as if
unblocked after a combat that resulted from the action succeeding, e.g. {Bum's Rush}.[^3-6-6]

Continuation is an "after combat ends" effect. If the combat continues or a new combat
begins, it is lost, along with other after-combat riders; unlock effects survive. See [§4.9](#49-end-of-round-end-of-combat-and-new-combats) for
this.[^3-6-7]

A combat queued during the action is still part of that action, so a continuation effect
played after that combat ends works normally, e.g. {Form of Mist} after {Psyche!}.[^3-6-8]

No combat need have occurred. Canceling the combat leaves the action blocked and it can
still be continued, e.g. {Crypt's Sons}, {Momentary Delay}; see [§3.5](#35-action-repetition-nra-and-canceled-actions) for the canceled-combat
case.[^3-6-9]

#### 3.6.3 Effects scoped to one block

An effect a reaction card provides on a successful block applies only in the combat that
block induced. It does not carry over to a follow-up combat, e.g. one queued by {Psyche!}.
This holds whatever the effect is — a maneuver, damage prevention, a strike or a strike
restriction, e.g. {Guard Dogs}, {Precognition}, {Night Terrors}.[^3-6-10]

If the action continues and a minion blocks again, that effect is provided afresh.[^3-6-11]

### 3.7 The action types in detail

The rulebook actions, one subsection each. Rules that are not specific to an action type live in [§3.1](#31-announcement-and-targets)-[§3.6](#36-continuing-an-action-as-if-unblocked) and [§3.8](#38-actions-provided-by-cards)-[§3.10](#310-changing-the-acting-minion).

#### 3.7.1 Bleed

**Base rules.** A bleed's default amount is 1 and its default target is your prey; if the
action succeeds with an amount of 1 or more the bleed is successful, the target burns that
much pool, and the acting minion's controller takes the Edge. [RBK bleed] The "(limited)"
rule caps increases only: one limited action modifier may increase the bleed amount per
action, while modifiers printed as not counting against the limit, and all reductions, are
unrestricted.

##### 3.7.1.1 Bleed amount

Order is free: a limited bleed modifier may be played before or after one that does not
count against the limit, e.g. {Command of the Beast}, {Power of One}.[^3-7-1-1]

The limit counts an increase only while that increase is actually applying.[^3-7-1-2] A
conditional limited modifier played when its condition is not met does not count against
the limit and lingers, applying if the condition is later met — {Foreshadowing Destruction}
at [DOM] against a target with 10 or more pool. A bonus lost during the action stops
counting and a further modifier may be played; redirection to another target is the usual
cause.

An ability granting +bleed is an action modifier and may be used at any point during the
action, e.g. {Pentex(TM) Loves You!}; see [§2.1](#21-effect-windows-and-impulse) for the windows.[^3-7-1-3]

"Only usable during a bleed action" bars the play in every other action, e.g.
{Confusion}. Where a card in play instead grants a bonus "during a bleed action", the
bonus reaches only the minion performing that bleed, e.g. {Haqim's Law: Retribution},
{Anu Diptinatpa}.[^3-7-1-4]

A vampire's "current bleed" read outside a bleed action is the amount he would bleed his
prey with, e.g. {Justicar Retribution}.[^3-7-1-5]

##### 3.7.1.2 Reduction and pool burned

A bleed reduced to zero is not successful; see [§3.4](#34-resolution-success-and-effect) for what may still be played on it. An
effect keyed to a successful bleed does not fire either, e.g. {Protected Resources} is not
burned by a bleed that resolves at 0.[^3-7-1-6]

An effect capping the pool a target burns does not change the bleed amount. Every modifier
to the amount applies first, then the cap, e.g. {Protected Resources}.[^3-7-1-7]

##### 3.7.1.3 Redirection

Redirection changes the target of the bleed, so the new target is the target for every
purpose: a reaction keyed to a bleed against you is usable by whoever the bleed ends up
against, not only by the Methuselah it was declared against, e.g.
{Elder Intervention}.[^3-7-1-8] Block attempts reopen.
[RBK summary-of-the-course-of-an-action]

The new Methuselah must be a legal target for that bleed. A restriction on whom a minion
may bleed also bars redirecting that minion's bleed to the protected Methuselah, e.g.
{Minor Boon}.[^3-7-1-9]

Redirection affects the acting vampire, so an effect stopping reaction cards from affecting
him stops {Deflection}, e.g. {Perfect Clarity}.[^3-7-1-10]

{Deflection} must be played before action resolution, ahead of the "would be successful"
window ([§3.4.3](#343-the-would-be-successful-window)).[^3-7-1-11]

Mandatory bleeds are [§3.9](#39-mandatory-actions)'s.

#### 3.7.2 Hunt

**Base rules.** The rulebook hunt action is undirected, at +1 stealth, and gains the acting
vampire blood from the blood bank equal to their hunt amount, by default 1 [RBK hunt]. Cards
also grant hunt actions of their own.

##### 3.7.2.1 A successful hunt and a successful hunt action are different conditions

A hunt action that resolves unblocked is successful even when no blood is gained. The hunt
is not: with zero blood gained the hunt is not successful, so effects keyed to a vampire
"successfully hunting" do not fire, e.g. {Hunger Moon}. A card that lets a vampire escape an
effect by hunting applies the same test and still hits him, e.g. {Thirst}.[^3-7-2-1]

Read each card for which of the two it names. {Triole's Revenge} burns a Ventrue who hunts at
full capacity: it names the hunt action, so it fires although the hunt gained nothing. It does
not fire if the action was blocked.[^3-7-2-2]

See [§3.4](#34-resolution-success-and-effect) for the general rule that an unblocked action is successful even when its effect cannot
occur.

##### 3.7.2.2 Card-provided hunt actions

A hunt action granted by a card is a hunt action for every purpose. It takes hunt bonuses and
increases to hunt value, e.g. {Kyoko Shinsegawa}. A restriction or permission worded around
hunting reaches it: {Pariah}, who cannot take undirected actions other than hunting, may take
a card-provided undirected hunt action such as {Vulture's Buffet}. Where a vampire has more
than one granted hunt action, his controller chooses among them.[^3-7-2-3]

An effect worded against the normal hunt reaches only the rulebook hunt action. A card
removing "the normal +1 stealth when hunting" does not touch the stealth printed on a
card-provided hunt action, e.g. {Igo the Hungry} against {Loki's Gift}.[^3-7-2-4]

Where the hunt action takes blood from a target, blood added by a hunt bonus comes from that
target, not from the blood bank.[^3-7-2-5] A rider that grants blood from the blood bank is
a separate gain, not hunt blood, and comes from the bank as printed, e.g.
{Festivo dello Estinto}.

##### 3.7.2.3 Hunts that steal from a vampire

A card granting a hunt that steals from a named vampire licenses that targeting for its own
hunt action only. Its bearer taking a different special hunt action cannot name a vampire,
e.g. a {Legacy of Caine} bearer taking {Abactor}.[^3-7-2-6]

The named vampire need not have blood. The action is legal and takes what is there, down to
nothing, e.g. {Week of Nightmares}.[^3-7-2-7] See [§1.7](#17-costs-and-payment) for taking less than the stated amount;
see [§1.6](#16-requirements) for the no-effect play.

Blood the hunting vampire cannot gain goes to the blood bank rather than staying with the
target.[^3-7-2-8] A rider that is not the hunt amount does not scale with hunt modifiers:
{Loki's Gift} [PRO] burns 1 blood from any vampire whatever the hunt value.[^3-7-2-9]

##### 3.7.2.4 Full capacity and mandatory hunts

A vampire at full capacity may still hunt; the excess returns to the blood bank as normal. An
effect that moves blood the hunt gained takes it before that return, e.g.
{Rabbat, The Sewer Goddess}. A card offering an alternative satisfies a mandatory hunt, e.g.
{Undying Thirst} permits diablerie instead.[^3-7-2-10] See [§3.9](#39-mandatory-actions) for mandatory actions.

#### 3.7.3 Equip actions

**Base rules.** Equipping from hand is an undirected +1 stealth action and pays the card's
cost; equipping from another minion you control is free, and the equipment taken is
announced with the action. [RBK equip]

##### 3.7.3.1 What counts as an equip action

A card that has a minion attach an equipment provides an equip action, whatever verb it
prints, e.g. {Magic of the Smith}, {Bloodstone}.[^3-7-3-1] Effects that modify equip
actions therefore reach it, e.g. {The British Museum, London}. One card may
provide an equip action or an employ action depending on what it fetches, e.g. {Jack of
Both Sides}.

Being an equip action does not settle requirements and cost. Only the wording "put … in
play" bypasses them ([§1.6](#16-requirements)): {Bloodstone} puts the equipment on the minion, {Magic of the
Smith} prints that requirements and cost apply. A requirement is checked continuously
while the action is in progress, so a trait change mid-action fizzles it — successful if
unblocked, but no effect ([§1.6.1](#161-when-a-requirement-is-checked)).

An equip granted by another card's effect is still an equip, so an ability reading "when
this minion equips" fires, e.g. {Topaz} with {Concealed Weapon} or {Pier 13, Port of
Baltimore}.[^3-7-3-2] An equipment's own on-equip clause fires the same way, e.g.
{Dagger}'s second copy. Read the trigger's wording: an ability keyed to an equip
*action* is not satisfied by an equip that is not an action, and {Pier 13, Port of
Baltimore} prints that it is not an action.

Being put into play is not equipping. A clause conditioned on the card being equipped does
not fire when an effect merely places it, e.g. {Incriminating Videotape} chooses no minion
when put on a vampire by {Alastor}, but does when equipped via {Magic of the
Smith}.[^3-7-3-3]

##### 3.7.3.2 Equipment already in play

Moving equipment between minions is neither playing nor equipping it, so a restriction
worded against playing or equipping does not reach the move, e.g. {Heidelberg Castle,
Germany}; a card may be moved onto a vampire in torpor.[^3-7-3-4] A card already played or
equipped can still enter play through an effect that is not an equip, e.g. {Kiss of
Lachesis}. Another of your minions may instead take it with an equip action from
its holder.

An equipment that is a location while in play cannot be moved, and a prohibition naming
equipment does not reach it; see [§1.3](#13-card-types-and-multi-type-cards) for the card-type rule.[^3-7-3-5]

One equip action may take several equipment from another friendly minion. It is an action
to equip with each of them, so each one's own bonus for the action to equip it applies,
e.g. {Unlicensed Taxicab}'s +1 stealth, and {Gift of Bellona} may be played.[^3-7-3-6]

Equipping from a minion targets the equipment taken. If one equipment is the same, the
action is the same and that minion cannot repeat it; see [§3.5](#35-action-repetition-nra-and-canceled-actions) for the No Repeated Action
rule.[^3-7-3-7]

##### 3.7.3.3 Minions who cannot equip

A vampire who cannot have equipment cannot attempt an equip action at all, e.g. {Enkidu,
The Noah}, {Beast, The Leatherface of Detroit}, and cannot strike to steal one
([§4.10](#410-weapons-and-equipment-in-combat)).[^3-7-3-8] If an effect places an equipment where it cannot legally sit, the
equipment is burned and its cost is not refunded; see [§1.6](#16-requirements) for it.

An effect keyed to equip actions does not reach equips performed before it entered play,
and a consequence it has already imposed survives it leaving play; see [§2.5](#25-duration-and-persistence) for
duration.[^3-7-3-9]

#### 3.7.4 Employ retainer and recruit ally

##### 3.7.4.1 The action

The cost of an employ retainer or recruit ally action is the cost printed on the retainer
or ally, and its requirements must be met to take the action.[^3-7-4-1]

Those requirements and that cost belong to the card, not to the action. An effect keyed to
the requirements or cost of the *action* does not read them — {CrimethInc.} is not usable
after recruiting an ally that requires an Anarch.

A card that brings in either an equipment or a retainer takes an equip action or an employ
action according to what it brings in, e.g. {Jack of Both Sides}.[^3-7-4-2]

A minion whose text says it cannot have equipment or retainers can neither take the action
nor steal one with a strike, e.g. {Beast, The Leatherface of Detroit} (see [§1.1](#11-card-text-and-the-rules) for the
reading of "cannot").

Employ retainer and recruit ally are ordinary actions for cancellation.

Cost reductions read the card as announced. {Ghouled} makes the ally a ghoul only on
resolution, so a reduction for recruiting a mortal still applies.

##### 3.7.4.2 Entry into play other than by the action

Two templates bring an ally or retainer in without the action: a card under which a minion
*recruits* or *employs* outside an action, e.g. {Piper}, {Pack Alpha}; and a card that
*puts* the card *in play*, e.g. {Summon History}. Requirements and cost apply as normal
under the first and are bypassed under the second ([§1.6](#16-requirements)).[^3-7-4-3]

Neither is an action, and effects worded as attaching to an action do not attach:

- Cost reductions naming an action, e.g. {Charisma}, {Erichtho}.[^3-7-4-4]
- Stealth modifiers on an action, e.g. {Blood Cult Awareness Network} does not reduce the
  stealth of a {Web of Knives Recruit} action.
- Abilities triggered by announcing the action, e.g. {Zhenga} does not work with
  {Piper}.

Effects keyed to the recruit or employ itself, or to the cost of the card, do attach
however the minion arrived, e.g. {Soul of the Earth}, {Little Tailor of
Prague}.[^3-7-4-5]

The ally or retainer is not played in the normal fashion, so nothing that cancels a card
as it is played reaches it, e.g. {Direct Intervention}, {Louhi}. It has still been played;
see [§1.8](#18-playing-and-canceling-a-card) for the distinction.[^3-7-4-6]

No action was performed, so the minion may still take the normal action to recruit or
employ the same card later that turn if it unlocks ([§3.5](#35-action-repetition-nra-and-canceled-actions)).[^3-7-4-7]

Where a minion recruits or employs, its own disciplines are read as normal to set the
card's level; where the card is merely put in play, use the basic version.

The action card of a normally recruited ally is replaced before the ally enters play. A
card brought in by an effect is not, so an ability triggering on entry has only the hand
and ash heap as they stand, e.g. {Corrupt Construction}.[^3-7-4-8]

##### 3.7.4.3 What the new minion may do

A minion recruited or employed this turn may still use its abilities, including an ability
whose cost is locking — see [§1.5](#15-abilities-and-card-plays) (and [§5.2](#52-locking-and-unlocking) for the lock).[^3-7-4-9]

Whether it may *act* that turn is [§5.5.4](#554-entering-play-and-acting)'s for allies and [§5.6.5](#565-entering-play)'s for retainers.

#### 3.7.5 Referendum procedure

##### 3.7.5.1 The referendum is part of resolution

The referendum is part of the action's resolution, not something that follows it. Cards
played "after a successful action" or "after resolution" wait until the referendum is
concluded, e.g. {Heidelberg Castle, Germany}, {Sargon}.[^3-7-5-1] Among those cards the
order is free, but none of them can forestall an oust the referendum itself
causes.[^3-7-5-2]

The referendum is conducted only if the acting minion is still ready when the action would
resolve. If combat leaves him no longer ready — in torpor or out of play — the action ends
and no referendum happens, e.g. {Yawp Court}.[^3-7-5-3]

Action modifiers and reaction cards may be played during the referendum and after it, and
vote-affecting cards before, during or after votes and ballots are cast. An effect keyed to
the tally reaches votes already cast: {Scorn of Adonis} makes every Methuselah who voted
against burn pool, whenever they voted.[^3-7-5-4]

##### 3.7.5.2 Terms

Terms are chosen once the action is successful, before polling. A card usable "during the
polling step" cannot be played before terms are set, e.g. {Business Pressure}.[^3-7-5-5]

What the terms designate is fixed then: {Revolutionary Council}'s chosen Anarchs still count
if they lock during the vote, and pool moving during the referendum does not alter {Parity
Shift}'s outcome. A quantity named in the effect clause instead of the terms is
counted when the effect applies — {Domain Challenge} counts locked minions after the
referendum completes.[^3-7-5-6] Where the terms cannot be carried out in full, the calling
Methuselah chooses within them. A cost inside the effect is paid by whoever the
terms name, e.g. {Alastor}.[^3-7-5-7] A referendum may be called with no eligible subject
in play, e.g. {Peace Treaty} with no weapons out; see [§1.6](#16-requirements) for the no-effect rule.[^3-7-5-8]

##### 3.7.5.3 Polling and the tally

Where the effect lets Methuselahs burn pool or blood for votes, each decides during that
effect's resolution and may burn one at a time, waiting on the others, e.g. {Business
Pressure}, {Mob Rule}.[^3-7-5-9] The ability does not persist for the rest of the action.
See [§2.4](#24-simultaneous-effects-and-ordering) for simultaneous choices.

An ability worded "during a referendum" is usable once per referendum; unlocking mid-vote
does not restore the use, e.g. {Michael Luther}, {Ellison Humboldt}.[^3-7-5-10] An ability
keyed to the tally fires when votes are tallied, e.g. {Astrid Thomas}.[^3-7-5-11]

Read pool-burn timing off the wording. A cost keyed to "when the votes are tallied" is paid
at the tally, before the referendum's effects; a cost keyed only to the referendum passing is
paid after all of them, including any oust and any pool gained. {Treachery} prints both
clauses.[^3-7-5-12] So an effect keyed to a passed referendum still applies when the predator
is ousted, e.g. {Donald Cargill}, but not when its own controller is ousted, e.g. {Lutz von
Hohenzollern}.[^3-7-5-13]

##### 3.7.5.4 Automatic pass, cancellation, failure

A referendum that passes automatically has no polling step. No "during a political action" or
"during a referendum" effect may be played, and no card may be burned for a vote during
it.[^3-7-5-14] Effects reading the number of votes it passed by have no effect. A card usable
*after* the referendum may still be used, with X = 0, e.g. {Voter Captivation} after a
{Cryptic Rider} referendum.[^3-7-5-15]

Canceling the referendum stops the tally, so cards keyed to the results do nothing, e.g.
{Scorn of Adonis} under {Delaying Tactics}.[^3-7-5-16] A referendum that fails produces none
of the calling card's effects, including a self-inflicted part, e.g. {Aura of
Invincibility}.[^3-7-5-17]

The political action card is set aside out of play until the action resolves, so effects
reading cards in play or in an ash heap do not see it, e.g. {Luna Giovanni}; see [§1.11](#111-the-ash-heap) for what
retrieval reaches.[^3-7-5-18] The blood hunt referendum is not a political action and is not
called by a vampire, so "during a political action" effects and effects keyed to the calling
vampire do not apply, e.g. {Power Structure}; see [§3.7.8](#378-diablerie-and-the-blood-hunt) for it.[^3-7-5-19]

#### 3.7.6 Votes and ballots

##### 3.7.6.1 Votes are not ballots

An effect worded on "votes" never reaches ballots or the prisci sub-referendum. That
holds whether the effect reduces a title's vote value, e.g. {Rastacourere}, subtracts
votes outright, e.g. {Condemnation: Mute}, or counts the votes a vampire has, e.g.
{Leadership Vacuum}, {Island of Yiaros}.[^3-7-6-1]

An effect that acts on the vampire rather than on its votes reaches both. Forcing a
vampire to abstain removes its ballot from the sub-referendum as well as its votes, and
cancels votes and ballots it has already cast, e.g. {Arishat}, {Kateline Nadasdy}.[^3-7-6-2]

Stripping a title removes the ballot the title provides but leaves a ballot granted by the
vampire's own text, and the sub-referendum still happens, e.g. {Gratiano} under
{Fall of the Sabbat}. His bonus ballot is cast on the same side as his votes.[^3-7-6-3]

##### 3.7.6.2 Which votes count

An effect counting the votes a vampire has counts its title and any unconditional bonus
votes from cards or abilities, e.g. {Eze, The Demon Prince}, {Firebrand}. It does not
count votes the vampire could obtain only by paying a cost or meeting a condition, e.g.
{Sundown}, {Aura of Invincibility}.[^3-7-6-4]

Multiple copies of a vote-granting card do not multiply votes, and an untitled vote bonus
adds to a title gained later; see [§1.15](#115-cumulative-and-stacking-effects) for both.

##### 3.7.6.3 Changing votes, canceling votes, abstaining

Where two effects alter the same vampire's votes, the last one used governs, e.g.
{Mustafa, The Heir}. An effect keyed to the act of casting fires only on the first cast
and not again when the votes are changed, e.g. {De Sade}.[^3-7-6-5]

An effect keyed to how a vampire voted reads the disposition at tally. {Madrigal} does
nothing if its player ends up abstaining, forced or not. {Scorn of Adonis} reaches
Methuselahs who voted "no" before it was played, and costs each of them 1 pool however
many "no" votes they cast. Votes granted only against the referendum are silenced, not
recast, when the bearer's votes are changed in favor, e.g. {Loyalist}. A vampire that
acquires a disqualifying trait after casting has its votes canceled and abstains, e.g.
{Khay'tall, Snake of Eden}.[^3-7-6-6]

An effect that changes votes cannot compel an abstaining vampire to vote; it only
restricts its choice if it votes, e.g. {Kindred Coercion}, {Neferu}. A force-abstain
effect may be used on a vampire that has not yet voted, keeping it abstaining. A vampire
that has not yet voted may always choose to abstain, escaping an effect worded on
non-abstaining vampires, e.g. {Astrid Thomas}; canceling that vampire's own votes does
not undo votes others already cast with it.[^3-7-6-7]

Cards usable during the polling step may be played before, during or after votes and
ballots are cast; see [§3.7.5](#375-referendum-procedure) for polling-step timing. Vote-changing effects cannot be used
in a referendum that passes automatically.[^3-7-6-8]

##### 3.7.6.4 Locked and torpid vampires

A card that locks a vampire for voting locks it as it casts, as a side effect and not as a
cost, e.g. {Disarming Presence}. A referendum ability printing no lock cost is usable
while locked, once per referendum; an unconditional one is usable in torpor as well. A
vampire in torpor casts no votes, but an effect keyed to its abstaining still applies,
e.g. {Alvaro, The Scion of Angelica}.[^3-7-6-9]

##### 3.7.6.5 The political action card's own vote

A political action card provides its inherent vote whenever it is played, including when
another card plays it from hand, e.g. {Charming Lobby}, {Echo of Harmonies}; see [§1.8](#18-playing-and-canceling-a-card) for
when it counts as played and whether it can be canceled. Burning a political action card
during a referendum for a vote is not playing it, so a once-per-game play limit is
untouched.[^3-7-6-10]

Pool paid, gained or lost as a consequence of a referendum, simultaneous ousts included,
is [§6.5](#65-pool-the-edge-and-ousting)'s; terms that cannot be carried out in full are [§3.7.5.2](#3752-terms)'s.

#### 3.7.7 Leaving torpor and rescuing from torpor

**Base rules.** Both default actions cost 2 blood, and the rescue cost may be paid by the
acting vampire, by the rescued vampire, or split between them. A blocked leave-torpor
produces no combat: a vampire blocker may diablerise the acting vampire instead, otherwise
the action simply fails and no cost is paid.[^3-7-7-1]

##### 3.7.7.1 Cards that supply their own action

A card granting a leave-torpor or rescue action supplies its own action, not the rulebook
one, so the default 2 blood is not paid — e.g. {Resume the Coil}, {Rapid Healing},
{Healing Touch}. It is still a leave-torpor (or rescue) action for anything keyed to
one.[^3-7-7-2]

##### 3.7.7.2 A blocked leave-torpor

Leaving torpor produces no combat when blocked, however the action was supplied. Cards
conditioned on entering combat therefore cannot be used, e.g. {Ghoul Escort}.[^3-7-7-3]

The blocker's diablerie opportunity arises at block resolution. An effect that ends the
action before block resolution, or unlocks the acting vampire, denies it, e.g. {Change of
Target}, {Mirror Walk} at [THA], {Blood Brother Ambush}.
See [§3.7.8](#378-diablerie-and-the-blood-hunt) for diablerie; see [§3.3](#33-blocking) for blocking.

##### 3.7.7.3 Cost and payer

The rescue cost belongs to the action, not to whoever pays it. A reduction printed on the
acting vampire applies even when the rescued vampire pays, e.g. {Frondator}.[^3-7-7-4] The
reduction is mandatory and cannot be declined to keep the higher cost ([§1.1](#11-card-text-and-the-rules)).

The same split works the other way: an effect keyed to "an action costing blood" sees the
rescue even when the acting vampire paid none of it, e.g. {Cavalier}.

##### 3.7.7.4 Torpor and the action window

A vampire in torpor is not ready, but an effect granting extra action opportunities still
reaches it. Its only available action is leave torpor, e.g. {Madness Network}.[^3-7-7-5]

A card effect that moves the vampire out of torpor after a rescue or diablerie action is
announced leaves that action successful if unblocked, but with no effect ([§3.4](#34-resolution-success-and-effect)). One that
brings back a vampire sent to torpor during the action ends that action instead, and it
cannot be continued ([§3.5](#35-action-repetition-nra-and-canceled-actions)). Both, e.g. {Warsaw Station}.[^3-7-7-6]

#### 3.7.8 Diablerie and the blood hunt

**Base rules.** The steps of diablerie resolve as one unit and cannot be interrupted; effects
are played before or after, never between them [RBK diablerie]. The blood hunt referendum is
automatic, is not an action, and cannot be blocked [RBK the-blood-hunt].

##### 3.7.8.1 The window before the blood hunt

There is a window after the diablerie resolves and before the blood hunt referendum, and
effects may be played in it.[^3-7-8-1] An action modifier keyed to the diablerie may come
before or after the discipline card, but must be played before the blood hunt, e.g.
{Draught of the Soul}, {Ritual of the Bitter Rose}.

Where the diablerie happened decides which card types fit the window. A diablerie action
takes action modifiers; an {Amaranth} diablerie happens in combat and takes combat cards.
{Slake the Thirst} covers both cases at its two levels.

The blood hunt is part of the action, though independent of it. A card that cannot be used
during an action cannot be used in that window, e.g. {Heidelberg Castle, Germany}.[^3-7-8-2]

What the action itself grants lands before the referendum: votes from {Political Struggle}
([§3.7.6](#376-votes-and-ballots)), and a {Trophy: Diablerie} retrieved for a Red List victim, which then protects the
diablerist in that same referendum.

##### 3.7.8.2 The referendum

The blood hunt referendum is not a political action and is not called by a vampire. Effects
keyed to either do not reach it, e.g. {Charming Lobby}'s follow-up referendum,
{Power Structure}.[^3-7-8-3] It is otherwise an ordinary referendum, so effects keyed to one
that passes resolve normally, e.g. {Gangrel Conspiracy} after votes and ballots are
cast.

A vampire burned by a passing blood hunt cannot answer with a "would be burned" effect, e.g.
{Reform Body}, {Abandoning the Flesh}.[^3-7-8-4] When the referendum follows an {Amaranth},
it happens during combat, so that burn is a burn in combat, e.g. {Hector
Trelane}.

##### 3.7.8.3 What counts as diablerie

{Amaranth} commits diablerie but is not a diablerie action. {Abactor} is not a diablerie at
all and only calls the referendum. A card requiring a diablerie action is unusable after
either, e.g. {Rebirth}; an effect keyed on having committed diablerie does not see
{Abactor}, e.g. {Carlton Van Wyk}.[^3-7-8-5] The referendum either one causes is a real
blood hunt, so blood-hunt effects apply, e.g. {Lay Low}, {Trophy: Diablerie}.

A diablerie the victim survives is unsuccessful: the diablerist gets nothing, blood and
equipment stay on the victim, and no blood hunt is called, e.g. {Reform Body},
{Byzar}.[^3-7-8-6] If the victim is in torpor again, another {Amaranth} may be
played. Bringing the victim out of torpor after the diablerie action is announced
does not end the action: unblocked it resolves successfully with no diablerie, e.g.
{Warsaw Station} ([§3.4](#34-resolution-success-and-effect)).

##### 3.7.8.4 Who may commit diablerie

Only a ready vampire may commit diablerie [RBK diablerie]. An ally granted the use of a card
still cannot, e.g. {Shadow Court Satyr} with {Amaranth}.[^3-7-8-7] A vampire barred from
diablerie ({Humanitas}, Blood Cursed) cannot be compelled to it, so {Undying Thirst} does
nothing to him. Cards compelling diablerie impose a mandatory action; see [§3.9](#39-mandatory-actions) for
discharge and the stuck case.

A blocker of a leave-torpor action gets the opportunity to diablerize the acting vampire
[RBK leave-torpor]; when that opportunity is lost is [§3.7.7.2](#3772-a-blocked-leave-torpor)'s.

### 3.8 Actions provided by cards

**Base rules.** A minion cannot take the action of a given action card, from hand or in
play, more than once each turn, even if it unlocks [RBK action-card-or-card-in-play].

#### 3.8.1 One source, one action

That limit attaches to the card, not to the minion. Each copy in play provides its own
action, so a minion that unlocks in between may take one action per copy, e.g. two
{Archon} on the same vampire.[^3-8-1] Actions provided by two different cards in play are
never "the same action", even at identical wording, and no card-provided action is ever
the same as a rulebook action; see [§3.5](#35-action-repetition-nra-and-canceled-actions) for the sameness test.
The same per-copy accounting governs a limited ability granted by a card in play
([§1.2](#12-wording-templates-periodicity-duration-triggers)).

One card provides its action once a turn, even where the action would fetch a different
card each time, e.g. {Bindusara, Historian of the Kindred}.[^3-8-2] Where one card
provides two different actions they are not cross-restrictive: the same minion may take
each once in the turn. The action taken to put a card into play and the action
that card provides once in play are two different actions, so a minion that unlocks may
take both, e.g. {Clandestine Contract}.

#### 3.8.2 What kind of action a provided action is

A provided action has the properties the providing text gives it, and no others.

Where the providing text limits who may take the action, that limit is the action's
requirement. {Haqim's Law: Judgment} provides an action requiring an Independent or
Anarch, so {CrimethInc.} can be used after it.[^3-8-3] This is not the fetched-card case:
the requirements of a card brought into play are not the fetching action's ([§1.6](#16-requirements)).

A provided action of a named type counts as that type for every effect keyed to the type.
A card-provided hunt is a hunt, so {Pariah}, who may take no undirected action but
hunting, can take one. A vampire who called a referendum has taken a political
action and can take no other that turn, even if the referendum is canceled.

A card-provided action is not an action card, and neither is a cardless action. Costs and
cost reductions worded against action cards reach neither, e.g. {Ravnos Carnival}'s
counters.[^3-8-4] Conversely, an [ACTION] card can provide a political action without
being a [POLITICAL ACTION] card: {Charming Lobby} calls a referendum, but effects naming
a political action card do not see it and it cannot be discarded for a vote.

A provided action that resembles a rulebook action is not that action, and only the cost
the card prints is paid: {Go Anarch} makes the vampire Anarch with no blood paid, unlike
the rulebook become-Anarch action [RBK become-anarch].

#### 3.8.3 Losing the source

If the providing card is an equipment the acting minion no longer possesses when the
action resolves, the action ends with no effect, but is still successful if it was not
blocked, e.g. {Jar of Skin Eaters}.[^3-8-5] See [§3.4](#34-resolution-success-and-effect) for successful-with-no-effect.

A card that provides its action through a contested title is face down out of play, its
action unusable ([§5.8.1](#581-printed-titles-granted-titles-contests)).

### 3.9 Mandatory actions

**Base rules.** A mandatory action is performed before any non-mandatory action, and a
minion required to take one can perform no other action. A minion with two different
mandatory actions, or with one it cannot take, is stuck and performs no action.[^3-9-1]

#### 3.9.1 When the obligation attaches

An effect makes an action mandatory only while the condition its text states holds. A
vampire whose text compels diablerie when there are torpid vampires he may diablerize is
under no obligation when there are none, and is free to take any action.[^3-9-2]

Whether another action of the same type discharges the obligation is decided by the
mandating card, not by the card used to satisfy it.

- The card **provides** the action. The obligation is to that action, and another action of
  the same type does not discharge it however it was obtained. {Elen Kamjian} must take the
  +1 bleed her ability gives her; a bleed from {Flurry of Action} does not count.[^3-9-3]
- The card **requires an action of a type**. Any action of that type discharges it,
  including one taken by playing a card. A minion compelled to bleed by {Spirit Marionette}
  [OBE] may bleed by playing {Computer Hacking}.

Where the mandate names alternatives, either branch discharges it: an empty vampire under
{Undying Thirst} satisfies his mandatory action by hunting or by diablerizing.

#### 3.9.2 Discharge and recurrence

Taking the action discharges the obligation; the action need not succeed. A minion that has
performed its mandatory action and then unlocks is free to take any action — the obligation
does not re-attach, e.g. {Cry Wolf}, {Lunatic Eruption}.[^3-9-4]

A card that requires an action of a type rather than providing one keeps demanding it while
the condition holds. {Phillipe Rigaud} must attempt diablerie again after unlocking as long
as an eligible torpid vampire remains.

#### 3.9.3 Stuck

A minion whose mandatory action cannot be taken is stuck: he takes no action at all, not
merely no mandatory one. Three cases recur.[^3-9-5]

- The action was already performed this turn, before the obligation attached. {Elen Kamjian}
  whose ability turns on after she has bled is stuck.
- An effect barred the action. {Change of Target} ends the mandatory action and forbids
  repeating it, so the acting minion is stuck.
- Two copies of the same mandatory-action card sit on one minion, e.g. {Lunatic Eruption}
  ([§1.15](#115-cumulative-and-stacking-effects) states this in one sentence).

#### 3.9.4 Masking

{Mask of a Thousand Faces} can take over an action that is mandatory for the acting minion
but not for the masking vampire. The masker must be capable of the action, not under the
same obligation, e.g. a hunt.[^3-9-6] See [§3.10](#310-changing-the-acting-minion) for masking eligibility.

### 3.10 Changing the acting minion

#### 3.10.1 Substituting the actor in an announced action

An effect that hands an announced action to a different minion leaves the action itself
unchanged; it continues from where it stood. Action modifiers already played stay in
effect and every other effect on the action carries over. The original actor's inherent
modifiers do not, e.g. an inherent +1 bleed.[^3-10-1]

The substitute must independently be capable of taking that action, and nothing may have
been played on the action that could not have been played with him as the acting minion.
{Force of Will} requires a locked acting vampire and {Mask of a Thousand Faces} requires
an unlocked one, so a {Force of Will} action cannot be taken over.[^3-10-2]

Blood already spent is disregarded in that test. It is not refunded and the substitute
does not pay it again.

A mandatory action may be taken over by a minion for whom it was not mandatory, provided
he could perform it, e.g. a hunt ([§3.9](#39-mandatory-actions)).

The substitute may play a modifier the original already played: that limit binds the
minion, not the action. He cannot use a limited effect if a limited effect has already
been used on the action ([§1.2](#12-wording-templates-periodicity-duration-triggers)).

The replaced minion unlocks, but it remains the minion that took the action; see [§3.5](#35-action-repetition-nra-and-canceled-actions) for
the No Repeat Actions consequence.

#### 3.10.2 "Is considered the acting minion"

Only text stating that a minion is considered the acting minion rewrites the designation,
e.g. {Deep Song} [ANI], {Nar-Sheptha}. Putting a different minion into the combat does
not. A slave locked to enter combat in place of a blocked clan member is not the acting
minion, and {Malleable Visage} leaves the designation with the original.[^3-10-3]

A card that reads "the acting minion" reads the current designation, for its own legality
and for its triggers alike. {Obedience} cannot be played once a slave has taken the acting
vampire's place. {FBI Special Affairs Division} does not trigger when the ally burned is
the acting minion.

Where two effects write the designation, the later governs, e.g. {Nar-Sheptha} over
{Deep Song}. When the later source leaves play its effect ends immediately and the
designation reverts for the rest of the combat, e.g. {Nar-Sheptha} burned. See [§5.9](#59-traits-and-trait-changes) for the
general trait rule.[^3-10-4]

---

## 4. Combat

### 4.1 Combat sequence and rounds

#### 4.1.1 Where cards fall in the round

An effect that sets the range for the round replaces the determine-range step, e.g.
{Omael Kuman} ([§4.2.1](#421-setting-the-range) owns range-setting).[^4-1-1]

An effect worded "after strike resolution" resolves before any further pair of strikes and
before the press step, e.g. {Shoulder Drop}. End-of-round cards are played after the presses
are handled, and remain playable when the round ends prematurely, e.g. {Infection}
[THN].[^4-1-2]

What resets at the round boundary is stated where the effect lives: range in [§4.2](#42-range), presses in
[§4.8](#48-presses), per-round abilities on cards in play in [§4.10](#410-weapons-and-equipment-in-combat).

#### 4.1.2 Combat begun outside an action

The acting minion acts first at every step of combat. A combat begun by a card or ability
rather than by a block has no acting minion of its own, so the minion the effect sends into
combat takes that role: he declares maneuvers, strikes and presses first and plays his combat
effects first, e.g. {The Guardian}, {Blissful Agony} [VAL]. Where the initiating player
controls neither combatant, the card says which side goes first — {Taunt the Caged Beast}
[ANI] gives it to the prey's vampire.[^4-1-3]

The minion using such an ability is not acting. He plays no action modifiers, and a card whose
requirement names an acting minion cannot be played against him, e.g. {Obedience} against
{Marie-Pierre}. Effects that end the combat and then do something afterwards — including
continuing the action as if unblocked — are lost, because there is no action to return to.
Unlock effects still apply.[^4-1-4]

#### 4.1.3 Combat inside an action

A combat that arises during an action is part of that action. The acting minion designation
does not change and effects applied during the action stay in force through the combat. This
holds even when the effect that caused the combat also failed the action, e.g. {Champion}: the
action continues until combat ends.[^4-1-5] See [§3.4](#34-resolution-success-and-effect) for the ordering of after-resolution effects.

A window exists between a successful block and the start of combat. A card barred "during
combat" may still be played there, e.g. {Angel of Berlin}.[^4-1-6]

#### 4.1.4 Starting a further combat

Queuing, the readiness of both combatants, and what a new combat resets are [§4.9.3](#493-queuing-a-new-combat)'s.

#### 4.1.5 Who may play cards during combat

A combat card printing permission to be played by a minion "not involved in the current
combat" may be played by a minion of any Methuselah, including one with no minion in the
combat, e.g. {Nosferatu Putrescence}, {Bliss}.[^4-1-9] Using an ability is not playing a card
and does not get this latitude; see [§1.5](#15-abilities-and-card-plays) for it.

A reaction card printing "usable even if there is no action" gains no window during combat: it
still cannot be played there.[^4-1-10]

### 4.2 Range

**Base rules.** Range is determined once per round, defaults to close, and a minion needs a
card or effect to gain a maneuver. [RBK determine-range]

#### 4.2.1 Setting the range

Many cards set the range outright instead of granting a maneuver. Once such an effect
resolves, the determine range step is skipped for that round and no other effect can reset
the range.[^4-2-1] Other before-range effects may still be played afterwards. Some
setters fix the *next* round's range instead; the same exclusivity applies to that round,
e.g. {Immortal Grapple} [POT], {Grasp of the Python} [SER].[^4-2-3]

Where two effects would set the same range, the first to resolve has priority and the later
one does nothing.[^4-2-2] Order follows when each effect actually resolves, not when its card
was played: a setter that fires on the block ({Squirrel Balance}, then the blocker's
{Asanbonsam Ghoul}) resolves before a standing "each round is at long range" effect that
applies at the determine range step ({Neutral Guard}).

A range-setting ability triggered by blocking is checked at the moment of the block. The
weapon must already be equipped then, and the ability belongs to the minion that actually
blocked, e.g. {Sniper Rifle}. A combat queued by {Psyche!} did not arise from that block, so
the ability is not available in it ([§4.9](#49-end-of-round-end-of-combat-and-new-combats)).[^4-2-6]

#### 4.2.2 The before-range window

Effects usable "before range is determined" must be played before the acting minion decides
whether to maneuver. [RBK before-range] An effect that changes the range in this window
takes effect at once, so range-dependent plays immediately follow the new range: once
{Fear of the Void Below} [dai] has made long the round's default, a close-range card such as
{Disarm} cannot be played.[^4-2-4]

Damage inflicted in this window is resolved in it. Both minions may play prevention and
non-prevention before-range effects, and simultaneous before-range damage is prevented and
mended together, e.g. {Outside the Hourglass} [TEM] (see [§4.5](#45-prevention--immunity) for prevention).[^4-2-5]

#### 4.2.3 Committing to a strike during determine range

Playing a strike card for its maneuver chooses that strike. [RBK determine-range] A cost an
opponent imposes on striking is incurred at that point, and it is a cost of the strike, not
of the card played, e.g. {Lucian, the Perfect} against a {Thrown Gate} played for its
maneuver.[^4-2-9] A restriction on playing strike cards reaches strike cards played in this
step for their maneuver, e.g. {Thoughts Betrayed} [DOM].[^4-2-8]

Committing early does not move an aim's own play window. Aims are still played in the strike
step, and cannot be played once the strike can no longer be chosen, e.g. {Target Head} after
{Immortal Grapple} (see [§4.3](#43-strikes) for aims).[^4-2-7]

#### 4.2.4 What the range gates

The range is fixed when the determine range step ends. Effects conditioned on the range
apply before strikes are chosen and cannot be dodged by the strike chosen, e.g.
{Vampiric Disease}; a card "only usable at close range" may be played before or after
strikes are chosen, e.g. {Blood to Water}.[^4-2-10]

A card triggered by an incoming effect needs that effect to reach at the current range:
{Rötschreck} cannot be played against aggravated damage that is not effective at the current
range.[^4-2-11] The trigger is unmet; futility itself is no bar ([§1.6](#16-requirements)).

Range gates strikes and strike resolution, not damage from other sources. Damage that is not
strike damage is inflicted whatever the range, e.g. {Burst of Sunlight}'s damage to the
striking vampire ([§4.4](#44-damage)). An effect riding on a strike applies at the range at which that
strike resolved, e.g. {Riposte}. Making a strike ranged does not extend its hand-strike or
melee-weapon portion beyond close range, e.g. {Blood of the Cobra} [QUI].[^4-2-12]

At long range a strike may be aimed at a retainer, and a restriction keyed to the opposing
minion's own traits does not bar it, e.g. {Earthshock} against the retainer of a minion with
[FLIGHT] ([§5.6](#56-retainers)). "Ranged weapon" means any weapon that provides a ranged strike, not only a
gun ([§4.10](#410-weapons-and-equipment-in-combat)).[^4-2-13]

### 4.3 Strikes

#### 4.3.1 Choosing a strike

Using the maneuver from a strike card or weapon chooses that minion's initial strike; a
few cards let him instead strike with the weapon he maneuvered with, e.g.
{Blessed Blade}.[^4-3-1] A strike card played in determine range for its maneuver counts
as played; a card merely granting the ability to strike does not, e.g. {.44 Magnum}.[^4-3-2]

An aim or other strike modifier is played in the strike step even when the strike was
committed during determine range, and cannot be played once the strike can no longer be
chosen, e.g. {Target Vitals} after {Immortal Grapple}. A minion committed to a strike an
effect then bars gets no strike at all.[^4-3-3]

"Strike: make a hand strike" cannot take another strike card as that hand strike; "strike:
use a weapon strike" can, and the result is still a hand strike, e.g. {Bundi}. A nested
strike inherits the base strike's properties. A card that is two strike types needs both
available, e.g. {Stutter-Step}.[^4-3-4]

A provided strike carries its card's discipline: {Heroic Might}'s are [pot] strikes.
Making a strike ranged leaves an inner hand or melee portion effective only at close
range, e.g. {Blood of the Cobra}.[^4-3-5]

Providing a strike does not compel its use: a weapon's action or its damage prevention
forces no strike with it, e.g. {Jar of Skin Eaters}, and a weapon's additional strike is
granted whether or not its strike was used, e.g. {Sword of Judgment}.[^4-3-6]

#### 4.3.2 Before strike resolution

"Before resolution" means after both strikes are declared and before they resolve. A
modifier that must affect the current strike is played in that window, ahead of damage
prevention, e.g. {Blood Agony}, {Backstab}.[^4-3-7]

A maneuver printed on a strike card or weapon is unavailable to a minion who cannot strike,
e.g. against {Hidden Lurker}; this includes optional weapon maneuvers.[^4-3-8]

Cancellation is [§1.8](#18-playing-and-canceling-a-card)'s. A minion whose strike is canceled chooses a new one and may choose
the same again, e.g. {Supernatural Resistance}; a canceled aim leaves the strike resolving
against its default target, e.g. {Target Retainer}.[^4-3-9]

#### 4.3.3 Strike resolution

Everything printed on a strike happens at strike resolution, and none of it if the strike
does not resolve: {Contagion}'s steal is dodgeable, {Escaped Mental Patient} does not burn,
and burning a committed weapon leaves that strike with no effect.[^4-3-10]

The strike's effects apply, then damage is resolved. Blood a strike moves is moved before
damage is mended, e.g. {Darkness Within}; blood from burning a minion with a strike
arrives after strike resolution and cannot mend that strike's damage.[^4-3-11]

A damage add-on may be played on any strike and does nothing on one dealing no damage,
e.g. {Target Vitals} on a dodge. Whether the strike deals damage decides, not when — a
strike inflicting damage after combat is still damage-dealing, e.g. {Catatonic Fear} [PRE].
A strike naming the object it acts on cannot be chosen when none exists ([§1.6](#16-requirements)).[^4-3-12]

#### 4.3.4 First strike

A strike done with first strike has its own earlier resolution, so an effect biting when a
strike resolves misses it: {Soul Burn} does not stop a weapon strike made with first
strike, and nullifies weapon damage only at resolution.[^4-3-13] Conversely a modifier
excluding "the current strike resolution" reaches the opponent's later normal resolution —
{Scorpion's Touch} with first strike reduces a strength-based strike, as does damage
inflicted with first strike, e.g. {Shambling Hordes}.[^4-3-14]

#### 4.3.5 Additional strikes

An additional strike is mandatory unless its card marks it optional ([§1.1](#11-card-text-and-the-rules)), e.g.
{Renegade Garou}, {Lorrie Dunsirn}.[^4-3-15] A minion barred from using additional strikes
cannot play a card providing one, even for that card's other effects, e.g. {Acrobatics}
against {Rigor Mortis}.[^4-3-16]

Additional strikes are announced after the normal pair resolves, but the card granting a
limited additional strike may be played before or after it, e.g. {Quickness}. A canceled
limited additional strike does not spend the limit ([§3.5](#35-action-repetition-nra-and-canceled-actions)). A retainer's use of a weapon is
not a strike and gives its employer no additional strike; see [§5.6](#56-retainers) for retainer strikes.[^4-3-17]

### 4.4 Damage

#### 4.4.1 How much damage

An effect granting "a strength of X" replaces the base strength; modifiers, including inherent ones, then apply to the new base. A later set overwrites the earlier one, e.g. {Erosion} then {Torn Signpost}. A "+X strength" effect adds to whichever base is current. A weapon's "current damage" is what it would inflict as a strike by its bearer against a generic opponent, so strength and other bonuses in play are not part of it. A strike's damage is fixed when strike resolution begins, e.g. {Shambling Hordes} loses no damage to life burned during that resolution.[^4-4-1]

Additional damage inherits every property of the base damage: type, preventability and source. Aggravated stays aggravated when {Target Vitals} adds to it, and a gun's added damage is still weapon damage, e.g. {Glaser Rounds}.[^4-4-2]

Adding damage to a strike that inflicts none produces no damage. {Oubliette} burns blood rather than inflicting damage, so {Target Vitals} adds nothing to it.[^4-4-3]

#### 4.4.2 Source of damage

The source is read off the card's own wording. Text naming a minion — "this vampire inflicts …" — is minion-inflicted; text naming the weapon is weapon damage; text naming no one is environmental.[RBK damage-resolution]

- A strike that lands its damage after combat is still minion-inflicted, e.g. {Catatonic Fear}, {Outside the Hourglass}.[^4-4-4]
- Equipment backfiring on its bearer ({Grenade}), a reaction damaging the striking minion ({Burst of Sunlight}) and a printed vampire ability ({Shemti}) are all environmental.[^4-4-5]
- Damage a weapon inflicts outside a strike is the weapon's, neither the bearer's nor environmental, e.g. {Talbot's Chainsaw} during the unlock phase ([§4.10](#410-weapons-and-equipment-in-combat)). Retainer damage is environmental with the retainer as its source ([§5.6](#56-retainers)).[^4-4-6]

#### 4.4.3 What sees environmental damage

Environmental damage is not inflicted by any minion, so effects that count, add to or reduce damage a minion inflicts do not see it, e.g. {Pulled Fangs} counts none of it and {Target Vitals} does not add to {Necrosis}'s press-step damage. See [§4.5](#45-prevention--immunity) for reduction and prevention.[^4-4-7]

A card worded on damage generally does reach it. {Dam the Heart's River} boosts "each strike or damaging effect", so it boosts the environmental damage as well as the strike; {Dawn Operation} turns environmental and retainer damage aggravated too. An effect limited to damage "in combat" reaches neither after-combat damage nor anything outside the combat, e.g. {Domain of Evernight}.[^4-4-8]

What environmental damage survives — dodges, combat ending early — is [§4.6.3](#463-what-survives-a-dodge)'s and [§4.7.2](#472-combat-ended-outside-strike-resolution)'s.

#### 4.4.4 Damage after combat

Damage delivered after combat ends by a strike is still strike damage. {Target Vitals} and {Dam the Heart's River} modify it and damage reduction reaches it, e.g. {Riposte}, {Catatonic Fear}.[^4-4-10] Whether such damage survives combat ending early, continuing, or a new combat beginning is [§4.9](#49-end-of-round-end-of-combat-and-new-combats)'s.

#### 4.4.5 Aggravated damage

"Treats aggravated damage as normal" changes only how the damage is applied to that minion. The damage is still aggravated at its source, so {Rötschreck} still works against it, and a card that cannot prevent aggravated damage still cannot, e.g. {Resilience} [FOR], {Flesh of Marble} [pro]. An immunity checked at application does see it as normal, e.g. {Ex Nihilo}. {Rötschreck} nonetheless requires a strike: it cannot be played against aggravated damage from a non-strike effect, even one a minion inflicts.[^4-4-11]

A minion burned by damage is burned during damage resolution; damage beyond that is lost, e.g. {Byzar}. An effect keyed on the vampire's blood reaching 0 does not fire when aggravated damage burns them instead, e.g. {Anathema}.[^4-4-12]

#### 4.4.6 Damage resolution is one block

Damage inflicted at the same moment is prevented and applied together, after all prevention. A single instantaneous prevention card covers all of it, e.g. {Tunnel Runner}'s theft damage alongside the strike damage. No ability may be used part-way through, e.g. {Vagabond Mystic}. Damage still applies if the minion inflicting it goes to torpor from the opposing strike, e.g. {Blood of Acid}.[^4-4-13]

### 4.5 Prevention & immunity

#### 4.5.1 Playing a prevention card

Damage prevention cannot be played when there is no damage to prevent, e.g. {Soak}, {Glancing
Blow} (see [§1.6](#16-requirements) for the general no-effect-play boundary).[^4-5-1]

A prevention effect that lingers past a single strike is exempt, and may be played before any
damage exists, e.g. {Apparition}, {Brother's Blood}.[^4-5-2] The restriction reaches the play
only: a standing prevention from a card already in play needs no damage pending ([§1.6](#16-requirements),
[§3.2](#32-stealth-and-intercept)).[^4-5-3]

An effect barring the opponent from playing prevention cards bars the play outright, including a
play made only to cycle, e.g. {Blood Fury}, {Dead Hand} ([§1.1](#11-card-text-and-the-rules)).[^4-5-4]

#### 4.5.2 How much is prevented

Printed "Prevent X damage" means up to X, e.g. {Soak}, {Nightstick}.[^4-5-5] Where a cost sets X,
X may be set higher than needed, but never negative, e.g. {Hidden Strength}, {Martyr's
Resilience}.[^4-5-6]

Unused prevention does not carry over.[^4-5-7] An allotment printed per round is spendable across
that round's strikes: {Armor of Caine's Fury} prevents 2 per round from any strike, or 1 from each
of two strikes.[^4-5-8]

Prevention worded against non-aggravated damage cannot prevent aggravated damage, even when the
minion treats aggravated as normal, e.g. {Flesh of Marble} against {Skin of Night}. Where both
kinds are inflicted, the preventing minion chooses which points go unprevented.[^4-5-9]

#### 4.5.3 What can be prevented

Prevention granted by blocking needs a successful block and works only in the resulting combat,
not a follow-up one, e.g. {Beast Meld}; a second block on the same action grants it
again.[^4-5-10]

A protection effect stopping the opponent's weapon strikes does not stop weapon damage the
opponent inflicts on itself, e.g. {Blood Fury}.[^4-5-11] Neither prevention nor protection applies
where the damage would not be effective at the current range, e.g. {Bollix} at long
range.[^4-5-12]

Unpreventable damage still yields to damage reduction, e.g. {Nephandus}, and to immunity.[^4-5-13]

#### 4.5.4 Sequencing

A card modifying a strike must be played before strike resolution, hence before prevention, e.g.
{Chiropteran Marauder}. Mending damage and burning blood to prevent destruction are uninterrupted:
no mending part of it, generating blood, then mending the rest, e.g. {The Coven}.[^4-5-14]

One instantaneous prevention card covers two damage events only if they are simultaneous, e.g.
{Tunnel Runner}; where the second follows strike damage it does not, e.g. {Blood of Acid} — a
lingering prevention covers both. Strike damage is prevented first, acting player first; all
damage applies at once afterwards.[^4-5-15]

Pre-range damaging effects resolve together: both minions may play prevention and further
pre-range effects before mending, and damage added then is prevented and mended with the rest,
e.g. {Outside the Hourglass}.[^4-5-16]

#### 4.5.5 Immunity

Damage from a source a minion is immune to is inflicted unsuccessfully — no mend, no wound, no
destruction ([RBK damage-resolution]). Immunity holds against unpreventable damage and outside
combat, e.g. {Bloodform}.[^4-5-17] Unlike prevention ([§4.5.2](#452-how-much-is-prevented)), immunity to non-aggravated damage
does cover aggravated damage the minion treats as normal, e.g. {Ex Nihilo} with {Skin of
Night}.[^4-5-18]

Immunity stops the damage, not the play: the source may still use an effect that would damage an
immune minion, e.g. {Charnas the Imp}. Immunity to a class of source reaches environmental damage
from that source, a retainer's damage included ([§5.6](#56-retainers)).[^4-5-19]

Prevented damage was still inflicted, so a rider keyed to inflicting damage fires anyway, e.g.
{Improvised Flamethrower}, {Weighted Walking Stick}; it does not fire where the damage was reduced
away or never inflicted. A strike rider conditioned on its damage landing survives prevention but
not a dodge, e.g. {Fleshcraft}.[^4-5-20]

A strike that sends a vampire to torpor leaves that vampire wounded; {Undying Tenacity} defers the
torpor to the end of combat but not the wound, e.g. {Coma} ([§5.3](#53-torpor)).[^4-5-21]

### 4.6 Dodge

**Base rules.** A dodge is a strike that deals no damage and protects the dodging minion
and their possessions from the effects of the opposing strike; retainers are not protected.

#### 4.6.1 A dodge negates the whole strike

A dodge stops the strike, not merely its damage. Every effect the strike would have
produced fails with it — a card placement, a lock rider, a queued new combat.[^4-6-1]
E.g. {Serpent's Numbing Kiss} places no card and locks no one; {Blissful Agony} [VAL]
starts no new combat.

A strike that would move its own card onto the opposing minion leaves that card where it
was: a weapon so worded stays equipped on the bearer, e.g. {Rowan Ring},
{Enhanced Coagulant}.

An effect worded as a step following strike resolution is still part of the strike and is
dodged with it, e.g. {Contagion} [DAI] steals the minion only if the strike
resolves.

A rider that disables the opponent's weapons fails too. Dodge the {Blood Fury} template
and the dodging minion's weapon strikes inflict damage normally that round.[^4-6-2]

#### 4.6.2 Dodge against prevention

Preventing the damage leaves the strike resolved, so the rest of the strike's effect still
applies. Dodging means the strike never resolved and none of it applies. {Fleshcraft}
prevented still places the card; {Fleshcraft} dodged does not.[^4-6-3] See [§4.5](#45-prevention--immunity) for
prevention.

#### 4.6.3 What survives a dodge

Read the source of each effect. Only what the dodged strike itself delivers is stopped.

- **Damage from anything but the dodged strike.** A card in play or a combat card
  inflicting damage on its own schedule is unaffected, e.g. {Conscripted Statue} [vis],
  {Darkling Trickery} [MYT].[^4-6-4]
- **But environmental damage printed as a rider on the strike** is dodged like any other
  rider, e.g. {Necrosis} [THN].[^4-6-5] The label does not decide it; the source does.
- **Combat ends**, which the base rules exempt from dodges. An effect ending combat after
  strike resolution still ends it, e.g. {Anesthetic Touch} [obe].[^4-6-6]
- **Effects keyed to the attempt rather than to the damage**, e.g. {Rötschreck} against an
  announced dodge or combat ends ([§4.7.2](#472-combat-ended-outside-strike-resolution)).
- **A cost or self-burn the strike card imposes.** {Flash Grenade} burns even though its
  lock rider is dodged.[^4-6-7]
- **An ability of the weapon that is not part of the strike.** {Garrote}'s
  burn-instead-of-torpor is usable when the opponent dodged but goes to torpor
  anyway.

#### 4.6.4 Dodging when it will accomplish nothing

"This strike cannot be dodged" does not stop the opponent choosing a dodge; the dodge
simply has no effect against that strike, e.g. {Scorpion Sting}, {Projectile}.[^4-6-8]
That is the permissive default ([§1.6](#16-requirements)), not an exception to it, and it does not carry over
to damage prevention, which cannot be played with no damage to prevent ([§4.5](#45-prevention--immunity)).

A card that is a dodge and another strike at once needs both to be legal choices. Its
dodge half protects, including against a strike made with first strike, while the other
half resolves normally — {Stutter-Step}.[^4-6-9]

### 4.7 Strike: combat ends

**Base rules.** A strike: combat ends always resolves first, before a strike done with
first strike, and it ends combat before any other strike or strike resolution effect
resolves [RBK strike-effects]. A dodge does not stop it.

#### 4.7.1 An unresolved strike does nothing

A strike that never resolves produces none of its effects and pays none of its costs.
A weapon or ally whose text burns it for striking is not burned, e.g. {Bomb},
{Waxen Poetica}.[^4-7-1] The same holds for every other consequence of the strike: blood
is not taken, a card the strike would place is not placed, an unlock rider does not
fire.[^4-7-2] The strike stays unresolved even if combat then continues through another
effect, e.g. {Relentless Reaper}.

A card that is itself a strike: combat ends does resolve when the opponent also plays one:
both are combat ends, so both resolve. Its burn-after-use clause therefore applies, e.g.
{Flash Grenade}, {Smoke Grenade}.[^4-7-3] Read the burn against the strike, not against the
combat: it is skipped only when the card's own strike fails to resolve.

An ability keyed to the strike resolution step is likewise unavailable, e.g.
{Gianna di Canneto}'s lock-to-damage ability. The same is true whenever combat ends during
first strike — a combatant sent to torpor by first strike aggravated damage ends combat
before the strike resolution step completes.[^4-7-4]

An effect barring strike: combat ends that arrives after the strike was announced leaves
the announced strike with no effect, e.g. {Dog Pack} put on a minion mid-combat.[^4-7-5]

#### 4.7.2 Combat ended outside strike resolution

An effect that ends combat outside the strike resolution step beats an announced strike:
combat ends. {Rötschreck} may be played after the opponent has announced a strike: dodge
or a strike: combat ends, and is effective.[^4-7-6] Combat ends immediately, no strike
resolves — including the announced strike: combat ends — and damage prevention cannot be
played. Self-burning weapons are not burned, exactly as in [§4.7.1](#471-an-unresolved-strike-does-nothing). Environmental
damage, which survives a dodge, does not survive this: a strike: combat ends ends combat
before it is applied ([§4.4](#44-damage)).

See [§4.9](#49-end-of-round-end-of-combat-and-new-combats) for what else is lost when combat ends early.

#### 4.7.3 "Combat ends after this strike resolves" is not a strike: combat ends

A card reading *combat ends immediately after this strike resolves* provides an ordinary
strike, not a combat ends. Both strikes resolve normally and simultaneously; the opposing
strike inflicts its damage, which can be prevented or mended as usual, and combat ends
afterwards, e.g. {Anesthetic Touch} [obe], {Autonomic Mastery} [DOM].[^4-7-7] A dodge
protects against the opposing strike but does not stop combat from ending, unless the card
itself says so — {Autonomic Mastery} prints "unless it is dodged", {Anesthetic Touch} does
not.

### 4.8 Presses

A press provided by a card is usable only during the round in which that card was
played.[^4-8-1] An unused press is lost at the end of the round; it cannot be saved for a
later one. This holds regardless of how long the rest of the card lasts: a press riding on
a strike, a maneuver or a range lock expires with the round even where the card's other
effect runs for the whole combat, e.g. {Immortal Grapple} [POT], {Dust to Dust} [thn]. A
card whose effect spans several rounds likewise grants one press, for the current round
only, e.g. {Undead Persistence}.[^4-8-2]

A press granted by a minion's own ability is usable only during the press step.[^4-8-3]
This applies both to an ability that gets the bearer a press, e.g. {Aeron}, and to one that
gives a press to another minion, e.g. {Don Caravelli}. Such an ability cannot be used
earlier in the round to bank a press.

A press is mandatory unless the card marks it optional.[^4-8-4] {Talbot's Chainsaw} prints
"1 press (mandatory)"; {Chameleon's Colors} [spi] prints "an optional press". A mandatory
press must be used, and where the card restricts its direction — continue only, or end only
— it is used in that direction. See [§1.1](#11-card-text-and-the-rules) for mandatory versus optional effects generally.

An existing press to continue must be handled before another press can be used to
continue.[^4-8-5] A second press to continue cannot be stacked on the first: the opposing
minion's only reply is a press to end. So {Trap}'s automatic press must be answered before
a press to continue such as {Boxed In} becomes playable.

Providing a press is not using one. A minion that cannot use presses may still play a card
that supplies them, e.g. {Mukhtar Bey} playing {Trap}: the card provides the press and the
minion is not the one pressing.[^4-8-6]

Canceling a maneuver that provides a press cancels the press; see [§1.8](#18-playing-and-canceling-a-card) for the rule.[^4-8-7]

Damage inflicted during the press step is environmental damage, e.g. {Drawing Out the
Beast} [ANI]; see [§4.4](#44-damage) for damage sources.[^4-8-8]

Effects usable at the end of a round are played after the press step is fully resolved, and
still resolve when the round ends prematurely. See [§4.9](#49-end-of-round-end-of-combat-and-new-combats) for them.

### 4.9 End of round, end of combat, and new combats

**Base rules.** The end-of-round step follows the press step and occurs even when combat ends prematurely. [RBK end-of-round]

#### 4.9.1 The end-of-round window

Effects usable at the end of a round wait for presses to be handled ([§4.8](#48-presses)), then apply even if the round ended prematurely.[^4-9-1] This governs triggered effects, not only card plays, e.g. {Ossian}'s life gain, {Masochism}'s counter.

Occupants of the window are mutually orderable: an end-of-round card may be played before or after another one and before or after a "when the combat would end" effect, e.g. {Taste of Vitae}, {Disarm}, {Telepathic Tracking}.[^4-9-2]

Ending combat does not close the window — end-of-round and end-of-combat cards can still be played, e.g. {Elysium: The Arboretum}.[^4-9-3] Conversely, a card usable at the end of combat may be played before combat ends, e.g. {Amaranth}.

A card played in this window has been played during that round, so cancels and cost modifiers keyed to the round or to combat cards reach it, e.g. {Death Seeker}, {Terror Frenzy}.[^4-9-4] A cost payable until the end of combat may still be paid after other end-of-round effects, e.g. {Loving Agony}'s unlock blood.

{Psyche!} is played after presses, when combat is about to end; end-of-round and "at the end of combat" effects may be played before or after it.[^4-9-5] A replacement effect played when a combat "would end" cannot follow {Psyche!}, e.g. {Telepathic Tracking}; played before it, combat continues and {Psyche!} becomes playable only at the end of the new round.[^4-9-6]

⚠ REVIEW — no ruling fixes the full order (presses → end of round → "would end" replacements → end of combat → after combat); only the pairwise orderings above are adjudicated.

#### 4.9.2 What survives a continued combat

An effect that ends combat and then does something else after combat loses that rider when the combat continues or a new combat begins, whether the continuation comes from a card or from a minion's ability, e.g. {Psyche!}, {Akram}.[^4-9-7]

Unlock effects are the exception. The unlock half of a "strike: combat ends" resolves when the strike resolves, before combat ends, so it survives; the rest resolves after combat ends and is lost, e.g. {Mummify}, {Meld with the Land}.[^4-9-8]

Only the after-combat half is lost; what already resolved stands. {Smoke Grenade} still burns. {Flash Grenade} burns but its lock rider is lost. {Rötschreck} is still put on the vampire, who does not go to torpor but still does not unlock as normal.[^4-9-9]

Damage, blood burn and card placement scheduled after combat do not happen, e.g. {Catatonic Fear}, {Riposte}, {Serpent's Numbing Kiss}.[^4-9-10] A modifier covering damaging effects "this combat" still reaches after-combat damage ({Dam the Heart's River}), but an effect keyed to blood reduced to 0 in combat is not triggered by it ({Anathema}).[^4-9-11]

A card whose cost is paid on resolution pays nothing when combat ends first: {Grenade} neither burns nor inflicts damage, and {Molotov Cocktail} is not placed.[^4-9-12] {Smoke Grenade} does burn against a simultaneous "strike: combat ends", because its own strike resolved ([§4.7](#47-strike-combat-ends)). An effect timed before range is determined still applies when combat ends at that point, e.g. {Weather Control}.[^4-9-13]

The "action continues as if unblocked" rider is lost like any other after-combat rider, e.g. {Form of Mist}; see [§3.6](#36-continuing-an-action-as-if-unblocked) for it.[^4-9-14]

#### 4.9.3 Queuing a new combat

At most one combat may be queued at a time. A card or ability that queues a combat cannot be used while one is queued, and no other queueing effect may be used until the queued combat begins, e.g. {Psyche!}, {Akram}, {Siren's Lure}.[^4-9-15] A queued combat does not occur if the action ends first.

A new combat cannot be started against a minion that is not ready — one going to torpor, or an ally locked by {Left for Dead}. An effect forbidding further combat likewise bars combat-starting cards, e.g. {Heaven's Gate}.[^4-9-16]

The new combat is part of the same action: the action may still be continued, and effects barred during an action stay barred between combats, e.g. {Heidelberg Castle, Germany}.[^4-9-17]

Per-combat conditions reset. A cost keyed to entering combat is paid again ({Blithe Acceptance}). Permissions tied to the blocked combat do not carry over ({Sniper Rifle}, {Scry the Hearthstone}). Cards replaced only after combat are replaced before the new combat begins.[^4-9-18] An effect triggering after combat triggers once per combat when several occur in one action, e.g. {Amelia, The Blood Red Tears}.[^4-9-19]

#### 4.9.4 After combat

Effects applied after combat ends are mutually orderable, e.g. {Provision of the Silsila}.[^4-9-20] An ability usable after combat has ended comes after cards played when combat "would end" or is "about to end", e.g. {Marie-Pierre}.

Where a new combat follows, effects sequenced between combats apply between them, and effects waiting on the action wait for the last combat, e.g. {Yawp Court}.[^4-9-21]

A "go to torpor" postponed to the end of combat is postponed again by a new combat, and the postponing card's protection does not extend into that combat, e.g. {Undead Persistence}.[^4-9-22]

### 4.10 Weapons and equipment in combat

#### 4.10.1 Using a weapon without striking with it

Most weapons print functions besides their strike: an action, a maneuver, a press, a
stealth reduction, damage prevention. Using one never commits the bearer to strike with
that weapon, e.g. {Talbot's Chainsaw}'s enter-combat action, {Starshell Grenade
Launcher}'s stealth reduction.[^4-10-1] Nor does it spend the strike: a minion who
maneuvers with a gun may still strike with that gun that round. An additional
strike the weapon grants is had even if the weapon's own strike is not used, e.g.
{Sword of Judgment}.

The dependency runs one way only. An optional maneuver printed on a strike cannot be used
when that strike cannot be used, e.g. against {Lapse} `[TEM]` or in {Hidden Lurker}'s
first round.[^4-10-2]

An ability keyed to blocking needs the weapon equipped at the time of the block; equipping
mid-combat arrives too late, e.g. {Sniper Rifle}'s range-setting after a
{Disguised Weapon}.[^4-10-3]

#### 4.10.2 Once per combat, once per round

"Only usable once each combat" and "once each round" limit the card, not the minion: a
second copy of the weapon allows a second use in the same period.[^4-10-4] The allowance
tracks the weapon, so it is not renewed when the weapon changes hands — {.44 Magnum} gives
one maneuver each combat however many bearers it passes through. A strike a card
merely grants for the round carries no such limit unless its own text prints one, e.g.
{Hunger of Marduk}.

#### 4.10.3 Weapon damage

A weapon's "current damage" is the damage it would inflict as a strike by its bearer
against a generic opponent at the appropriate range.[^4-10-5] Strength and bonuses from
the minion or from other cards in play are excluded, and the value is fixed when the
card naming it is announced, e.g. {Machine Blitz}, {Illegal Search and
Seizure}.

Reading a weapon's damage value is not using the weapon: no restriction or side effect of
the weapon applies, so a burn-after-use weapon is not burned and a once-per-combat weapon
is not spent.[^4-10-6] Such damage is not aggravated even when the weapon's own strike
is.

A weapon that provides a ranged strike is a ranged weapon whatever its printed type, e.g.
{Kerrie} under {Anachronism}.[^4-10-7] Damage from a weapon is weapon damage whatever
delivers it: the ranged option on a melee weapon still does that weapon's damage, and
{Talbot's Chainsaw}'s unlock-phase damage is weapon damage, neither inflicted by the
bearer nor environmental. See [§4.4](#44-damage) for damage classification.

#### 4.10.4 Weapons that leave or become unusable

A weapon already committed as the strike but unavailable when that strike resolves makes
the strike have no effect — burned by an opponent's effect, or contested because a
{Disguised Weapon} equipped a second copy of the same unique weapon.[^4-10-8] Up to that
point the weapon is still usable [RBK strike-effects].

A weapon that burns itself or damages its bearer on use does neither if combat ends before
the strike resolves, e.g. {Grenade}, {Dragon's Breath Rounds}.[^4-10-9] Once the strike
has resolved the burn happens as printed, even if combat continues or a new combat begins,
e.g. {Smoke Grenade}. A weapon temporarily out of play escapes a scheduled burn
([§1.14.3](#1143-cards-out-of-play)).

While an effect prevents a minion from using equipment, e.g. {Drawing Out the Beast}, the
disciplines and maneuvers his equipment provides are unavailable ([§1.5](#15-abilities-and-card-plays)). The prohibition
reaches only what the bearer uses; an equipment effect that triggers on its own still
functions, e.g. {Soul Gem of Etrius} when the bearer is burned.[^4-10-10]

Ammo and other cards improving a weapon before strike resolution can only be played on
your own minion's weapon.[^4-10-11]

---

## 5. Minions and Their States

### 5.1 Vampires: capacity, identity and merging

#### 5.1.1 Capacity

A vampire's capacity can never be reduced below one. A reduction printed as lasting until
the end of the game survives the burning of the card that imposed it, and still applies if
the vampire returns to the uncontrolled region.[^5-1-1]

Cards on an uncontrolled vampire are out of play, so a capacity modifier from one of them
does not apply there. It resumes when the vampire is controlled again, and blood held for
the raised capacity does not drain off in the meantime.[^5-1-2] With the floor of one, a
vampire whose capacity comes entirely from cards on it is a 1-capacity vampire while
uncontrolled, e.g. {The Becoming}.

Blood above capacity drains off as the vampire is moved to the ready region, before
anything else happens to them. It drains before the vampire's own entry text fires, e.g.
{Hermana Hambrienta Mayor}'s forced 2-blood burn, and before the vampire can be merged:
{Tariq, The Silent}'s printed capacity reduction applies the moment you control him, so
the blood is lost even if you merge him immediately after.[^5-1-3]

Capacity granted by a title is lost with the title; see [§5.8](#58-titles) for titles.[^5-1-4]

#### 5.1.2 Merging

Merging is not entering play, so effects keyed on a vampire who entered play or entered
the ready region in a given window do not see it, e.g. {Chameleon}, {Legendary Vampire}.
It is not moving a vampire from uncontrolled to controlled either, so a tax on that
movement does not apply, e.g. {Masquerade Enforcement}.[^5-1-5]

The advanced card's sect is written onto the vampire as it merges, including when the base
version was the one in play, e.g. {Goratrix} becomes Camarilla. Any anarch token on the
vampire is burned, unless the merged sect is itself Anarch, e.g. {Dancin' Dana}.[^5-1-6]
See [§5.9](#59-traits-and-trait-changes) for trait change and its precedence.

The advanced card need not come from your uncontrolled region. A copy you come to control
by any means may be merged, e.g. one stolen with {Graverobbing}.[^5-1-7]

#### 5.1.3 Created vampires and crypt card identity

A library card put into play as a vampire is a vampire card for every purpose while in
play: it can be moved to the uncontrolled region and influenced out again. In the ash heap
it is the library card again, so effects reaching a vampire in the ash heap cannot see
it.[^5-1-8]

Such a minion is non-unique unless its card says otherwise, e.g. {Hatchling}. Where the
card does make it unique, uniqueness runs on the card name and crosses minion types: a
mummy ally created by {Spell of Life} contests a vampire of the same name.[^5-1-9]

A card that copies a vampire copies clan, sect, capacity and disciplines only; titles and
other traits such as Infernal or Scarce are not, e.g. {Dual Form}. The copy is a snapshot
taken at resolution: disciplines held then are copied, including those granted by cards in
play, and are kept when the granting card leaves; disciplines gained later are not copied.
A capacity reduction imposed by the copying card itself applies first, so the copy has the
reduced capacity.[^5-1-10]

A vampire brought into play to replace a burned one is a new vampire for all purposes even
when it is the same vampire, e.g. through {Soul Gem of Etrius}: it may bleed although the
burned version already bled that turn.[^5-1-11] See [§3.5](#35-action-repetition-nra-and-canceled-actions) for the No Repeated Action side.

### 5.2 Locking and unlocking

**Base rules.** *Ready* means in the ready region, i.e. not in torpor; *unlocked* means not
turned sideways. A vampire in torpor is not ready but still unlocks each unlock phase — hence
"ready, unlocked" in card text.

#### 5.2.1 What a lock prevents

Locking bars acting and blocking, not ability use; see [§1.5](#15-abilities-and-card-plays) for that and the lock-as-cost half of
it.[^5-2-1] An action modifier carries no unlocked requirement of its own — even one played
by a minion other than the acting minion, e.g. {Cloak the
Gathering}, {Make an Example}.[^5-2-2] Locked vampires still vote, and lock as they cast their
votes; effects counting locked minions read the table after the referendum, e.g. {Domain
Challenge}.[^5-2-3] A locked minion remains a legal target, e.g. {Mind Rape}.[^5-2-4] A card
that must choose a ready, unlocked minion is unplayable when there is none, e.g. {Brujah
Frenzy}; see [§1.6](#16-requirements) for state requirements.[^5-2-5]

#### 5.2.2 The unlock phase and its suppression

Unlocking is the first thing in the phase; every "during your unlock phase" effect follows, in
its controller's chosen order, e.g. {Baleful Doll}.[^5-2-6] A condition on what a Methuselah
controls during that phase is checked when the phase ends: meeting it earlier does not help,
acquiring the object later does not excuse it, e.g. {Anarch Revolt}, {Arika} ([§2.5](#25-duration-and-persistence)).[^5-2-7]

"Does not unlock as normal" suppresses only that automatic unlock; wakes and unlock effects
still reach the minion, e.g. {Sensory Deprivation}, {Cry Wolf}.[^5-2-8] It is redundant on an
infernal minion, whose controller may still burn 1 pool to unlock them.[^5-2-9] A card saying
minions *cannot unlock* reaches unlock effects too, but still not wakes, e.g. {The Sleeping
Mind}.[^5-2-10]

Duration is read off the card printing it. {Rötschreck}'s is a standing effect of the card in
play and ends when it is burned or removed; {Rowan Ring}'s lasts while the vampire remains in
torpor and survives the Ring being burned or moved.[^5-2-11]

Two burn-at-unlock templates differ. "Choose not to unlock as normal and burn this card" is an
independent act, still available to a minion already prevented from unlocking, e.g.
{Putrefaction}. "Burn this card instead of unlocking as normal" is a substitution: open to an
already-unlocked minion, closed to one prevented, e.g. {Fata Amria}.[^5-2-12]

#### 5.2.3 Wakes, unlocking and blocking

A wake opens the reaction window; it does not unlock. A woken locked minion may play reactions
and attempt to block, but cannot use an effect needing an unlocked minion or costing a lock,
e.g. {Familial Bond}.[^5-2-13] Paying a lock leaves the minion unable to block without a wake
or an unlock, e.g. {Starshell Grenade Launcher}.[^5-2-14] An effect merely letting a locked
minion block is not a wake and grants no reaction cards, e.g. {No Secrets From the
Magaji}.[^5-2-15] A wake, but not an unlock-and-block effect, may be played in a card's
"as played" window ([§1.8.1](#181-the-as-played-window)).[^5-2-16]

The unlock-to-block template ({Guard Duty}, {Second Tradition: Domain}) is [§3.3.1](#331-who-may-block)'s.

A block locks the blocker only once it succeeds; an effect locking a failed blocker does so
just before action resolution, e.g. {Hard Case}, {Faceless Night}.[^5-2-19] A lock from
another card is not the block's lock, so an exemption from locking to block does not stop it,
e.g. {Mirror Walk}; locking a minion attempting to block makes the block fail, e.g.
{Alexandra}.[^5-2-20] See [§3.5](#35-action-repetition-nra-and-canceled-actions) for the canceled-combat case.

#### 5.2.4 Locking the locked, unlocking the unlocked

Both are legal, e.g. {Anarch Troublemaker}, {Under Siege}, and locking an already-locked
minion can be useful: it satisfies a lock-or-discard effect that an infernal trait then undoes,
e.g. {Nightmares upon Nightmares}.[^5-2-21] No state changes, so an effect triggered by
unlocking does not fire, e.g. {Vampiric Disease}; a mandatory unlock ability is still applied,
e.g. {Eze, The Demon Prince}. Any genuine unlock triggers, including one that already cost
blood.[^5-2-22] A minion returning to play unlocked has not unlocked, e.g. {Banishment}
([§6.4](#64-leaving-and-re-entering-play)).[^5-2-23]

#### 5.2.5 Lock as cost, lock as effect

Where a card locks a minion as part of its effect, nothing need be unlocked and no cost is
paid, e.g. {Disarming Presence}.[^5-2-24] A lock-to-use effect cannot be taken "in response"
to another effect ([§2.1](#21-effect-windows-and-impulse)), e.g. {Heidelberg Castle, Germany}.[^5-2-25]

A lock-to-reduce-cost effect may be used at any point up to payment — at announcement if it
is what makes the play affordable ([§1.7.3](#173-cost-reductions)).[^5-2-26] Equipping a
vehicle locks it however the equip came about; putting the card directly into play does not,
e.g. {Helicopter} ([§1.6](#16-requirements)).[^5-2-27]

#### 5.2.6 Unlock effects in combat

An unlock effect on a strike resolves at the strike, before combat ends, and an effect
continuing the combat or beginning a new one does not undo it, e.g. {Bond with the
Mountain}.[^5-2-28] An effect conditioned on combat ending does not apply when combat
continues, though unconditional consequences still happen — {Flash Grenade} still burns — and
a minion that unlocked during the combat is locked again once it ends.[^5-2-29] See [§4.9](#49-end-of-round-end-of-combat-and-new-combats) for
combat continuation.

### 5.3 Torpor

**Base rules.** A torpid vampire is controlled but not ready; it unlocks normally, cannot
block, play reaction cards or vote, and acts only to leave torpor [RBK torpor].

#### 5.3.1 Going to torpor

"When a vampire is going into torpor" and "when a vampire should go into torpor" are one
window. Both players may play in it, the acting minion first, and the first card played can
strip the other's requirement: once torpor is averted, no card needing the vampire to be
going to torpor may follow — including a second copy of the card that averted it.[^5-3-1]
A clause that chooses vampires and sends them to torpor opens no window in between.

A vampire on its way to torpor is still in play and still ready, and may use its abilities
and play cards until it arrives, e.g. {Watenda}, {Revelation of Wrath}.[^5-3-2] A rider
keyed to the opponent going to torpor is not part of the strike that caused it, so it
fires even when that strike was dodged, e.g. {Garrote}.

A vampire on its way to torpor is not ready for a new combat, though a combat already
queued still occurs ([§4.9.3](#493-queuing-a-new-combat)).[^5-3-3]

**Delayed torpor.** The {Undying Tenacity} / {Undead Persistence} template pushes torpor to
after combat; the vampire stays wounded and remains burnable.[^5-3-4] Everything else that
trigger produced still happens — combat ends, and an unlock or blood gain in the same clause
occurs, e.g. {Ashes to Ashes}. Where torpor is instead bundled with ending combat
and the combat does not end, the vampire unlocks but stays out of torpor, e.g.
{Mummify}.

Such a vampire may play cards a vampire going to torpor could not. The protection does not
reach a fresh combat: that ends at once with the vampire not ready unless a new copy is
played there.[^5-3-5]

#### 5.3.2 What a torpid vampire can still do

Abilities printed on cards in play remain usable in torpor; see [§1.5](#15-abilities-and-card-plays) for the rule. Printed
effects that merely apply do so too, e.g. {Nahir}'s hand size, as does a trigger keyed to
the end of combat, e.g. {Amelia, The Blood Red Tears}.[^5-3-6] Referendum abilities from
torpor are [§3.7.6.4](#3764-locked-and-torpid-vampires)'s.

Torpor bars reaction cards — absent the card's own printed permission — but not combat
cards. A combat card requiring an *unlocked* vampire
not involved in the combat may be played from torpor, since a torpid vampire unlocks as
normal — e.g. {Save Face}, {Martyr's Resilience}.[^5-3-8] A requirement naming a *ready*
vampire is not met, and a reaction stays barred even where the vampire reached torpor
during the combat that followed his block, e.g. {Cats' Guidance}.[^5-3-9]

A vampire acting from torpor — leaving torpor, or acting through an effect that does not
require readiness, e.g. {Madness Network} — plays action modifiers as normal, e.g.
{The Kiss of Ra} on the leave-torpor action itself; a torpid vampire plays no action
modifier during another minion's action, e.g. {Make an Example}.[^5-3-10] Modifiers usable
after combat may also be played from torpor, e.g. {Freak Drive}.[^5-3-11]

#### 5.3.3 Torpid vampires as objects

Torpor removes readiness, not control. A burn option opens when you control no minion
meeting the card's requirement, so torpid vampires open it where the requirement names a
ready minion, e.g. {Emergency Powers}, but not where it names only control of a vampire
with a trait, e.g. {High Orun}.[^5-3-12]

A card may be put on a torpid vampire unless the operating clause requires readiness:
{Fear of Mekhet} cannot be played on one but can be moved to one.[^5-3-13] A "burn this
card after this minion goes to torpor" clause fires on the event, not the state, so a card
entering play on a vampire already in torpor is not burned.[^5-3-14] An
ongoing effect whose subject was chosen while ready keeps applying in torpor, and stops only
if that vampire leaves your control, e.g. {The Rack}.

A change of controller does not change torpor: a stolen or defecting vampire stays in
torpor [RBK glossaries].[^5-3-15] Allies have no torpor state ([§5.5](#55-allies)): an effect that would
send an ally to torpor burns it instead, and one sending vampires to torpor leaves an
opposing ally unaffected.[^5-3-16] Incapacitation is the imbued analogue, and abilities stay
usable there too, e.g. {Abjure} ([§5.7](#57-special-minion-classes--traits)).

### 5.4 Burning minions

Only a controlled minion in play can be burned from play. Uncontrolled vampires and
contested cards are out of play and do not qualify, so effects that retrieve a minion
"burned from play" never reach them, e.g. {Blessed Resilience}.[^5-4-1] What was burned is
read off the card, not off the role it filled: a crypt card put into play as a wraith ally
by {Khazar's Diary (Endless Night)} is not an ally burned from play, and a card treated as
a vampire only while blocking is not a minion when it burns, e.g. {Unleash Hell's
Fury}. A burned minion goes to its owner's ash heap, and a pending instruction to
move it elsewhere lapses — a vampire put into play by {Chain of Command} and then burned is
not moved to the crypt.

#### 5.4.1 Who burned it

If a minion is burned in combat, its opponent is always considered to have burned it,
whatever the cause.[^5-4-2] This holds when the minion burns itself: an {Escaped Mental
Patient} burned at the end of combat is still an ally burned in combat. It also
holds when the card's controller is not the combatant — the vampire playing {Blood Brother
Ambush} has not burned a minion, but the opposing minion has.

Outside combat, the acting minion burned it only when the action's own effect did: damage
inflicted, or blood or life taken, by the action. An ally that burns as a result of a
directed action is burned by that action, so Trophy cards and {Predator's Transformation} trigger,
e.g. {Brick Laying}, {Cryptic Mission}, {Succubus}.[^5-4-3] A minion burned for any other
reason — a referendum result, a cost paid, its own ability, its last life spent — was not
burned by the acting minion, and cards keyed to "when this vampire burns a minion" do not
fire, e.g. {Taking the Skin: Minion}.[^5-4-4]

#### 5.4.2 Effects triggered by the burn

An effect keyed to a minion being burned fires however the burn came about, and an effect
keyed to blood reduced to zero fires whatever removed the blood, e.g. {Anathema},
{Political Struggle}.[^5-4-5] Blood or pool awarded for burning a minion with a strike is
awarded after strike resolution, so it is not available to heal damage from that same
strike, e.g. {Young Bloods}.

#### 5.4.3 Burns that do not happen

A replacement effect worded "if this minion would be burned, instead ..." means the minion
is not burned: effects that trigger after the burn do not fire, e.g. {Sacrificial Lamb}
gains no blood off {Byzar}.[^5-4-6] An instruction or condition to burn a minion is still
satisfied — {Byzar}'s controller may still burn him to burn a {Judgment: Camarilla
Segregation}. Such a replacement takes effect before anything triggering on the
burn, e.g. {Soul Gem of Etrius}; a competing replacement may still be played first, by
normal sequencing ([§2.3](#23-after-resolution-and-after-combat)).

An effect that saves a minion by ending combat cannot reach a burn that occurs as combat
ends, e.g. {Heaven's Gate} and {Left for Dead} cannot save an {Escaped Mental Patient}
whose strike resolved. A minion so saved was never burned, so burn triggers do not
fire.

#### 5.4.4 The "would be burned" window

A minion on its way out of play is still in play and may still play cards, e.g.
{Revelation of Wrath}.[^5-4-7] A burn from a blood hunt referendum opens no such window:
{Abandoning the Flesh} cannot be played against it (see [§3.7.8](#378-diablerie-and-the-blood-hunt) for the blood hunt).

### 5.5 Allies

#### 5.5.1 Life, not blood

An ally has life, not blood, and can never pay a blood cost. A card or ability whose cost
is in blood is unplayable by an ally, e.g. {Codex of the Edenic Groundskeepers}. An effect
that demands blood from the acting or blocking minion fails for an ally: an ally's action
is lost to {Hide the Heart} [val], and an ally cannot block through {Tenebrous Form} [OBT]
or take a directed action against {Étienne Fauberge}. A cost reduced to zero is payable —
{The Shard, London} lets an ally play a blood-cost card that does not otherwise require a
vampire, and an ally recruited for blood is kept for 0 pool under {Kindred Segregation}.[^5-5-1]

A card whose effect names the opposing vampire has no object in an ally and cannot be
played against one, e.g. {Taste of Vitae}, {Enhanced Coagulant}. Where the blood is only a
rider, the rest of the effect still applies: {Shackles of Enkidu} holds an ally but burns
nothing. An effect worded on vampires passes an ally over — {Legacy of Power} sends the
vampires to torpor and leaves the ally where it stands.[^5-5-2]

#### 5.5.2 Life totals

An ally's life is not capped by its starting life; life gained above it stays. "Starting
life" is the printed value of the card that entered play, and later change does not move
it: {Ghouled} adds a life but the ally's starting life is still the mortal's, and an animal
retainer moved to the ready region by {Demdemeh} keeps its counters and its original
starting life while losing its abilities and any continuous effect on it. A vampire treated
as an ally has no starting life at all, so {Vagabond Mystic} cannot give it life; its blood
is its life, and an "as if he had the Discipline" ability still works while it is an
ally.[^5-5-3]

#### 5.5.3 Acting "as a vampire"

An ally that can play cards as a vampire may play any card its own text admits, not only
Discipline cards, e.g. {Shadow Court Satyr} playing {Taste of Vitae}. It may call a
referendum listed on a political action card in hand, e.g. {Herald of Topheth} with
{Charming Lobby}. It cannot commit diablerie ([§3.7.8](#378-diablerie-and-the-blood-hunt)), e.g. {Amaranth}. An ally granted a
single Discipline cannot play a card requiring two or more, and the Discipline level it
came into play with fixes which version it uses for good.[^5-5-4]

The treatment covers only the effect generated by playing the card. An outside effect
keying on "a vampire" does not see the ally: {Veil of Darkness} ignores it and {The Line}
cannot reduce its cost. Neither does the played card's own in-play text, so an ally that
plays {Descent into Darkness} never returns. A card that lets a minion act or block "as an
ally" likewise changes only the check it names — {Sonja Blue} blocks as an ally and still
plays Discipline cards.[^5-5-5]

Life pays for the card, so spending the last life burns the ally mid-play. An action
modifier played with the last life fails; a strike played with the last life ends combat
before strike resolution; but a cost paid for an action still resolves the action fully,
and the oust order is [§6.5.2](#652-when-the-oust-resolves)'s.[^5-5-6]

#### 5.5.4 Entering play and acting

A recruited ally cannot act the turn it enters play; one brought into play by other means
can [RBK recruit-ally]. The keyword decides it: cards that make a minion **recruit** an
ally leave it unable to act that turn, e.g. {The Summoning}, {Piper}; cards that **put** it
in play do not, e.g. {Summon History}, {Khazar's Diary (Endless Night)} ([§1.6](#16-requirements)).[^5-5-7]

An ally whose text lets it act the turn it is recruited still acts only in your minion
phase, so recruiting it on an opponent's turn gives it no action, e.g. {Nocturn},
{Infernal Servitor}.[^5-5-8]

An effect triggered by the ally entering play applies however it entered. {War Ghoul} burns
one of your allies or retainers on entry, and burns itself if you control none, even when
put into play abnormally — it is an on-entry effect, not a recruit requirement, so [§1.6](#16-requirements)'s
bypass does not reach it. Abilities keyed on an ally being "recruited" cover non-standard
recruitment routes, e.g. {Sébastien Goulet} with {Piper}.[^5-5-9]

### 5.6 Retainers

#### 5.6.1 The retainer is not the bearer

A retainer that uses a weapon is not its bearer; the employing minion remains the
bearer.[^5-6-1] Damage or costs the weapon puts on the bearer therefore fall on the
employer, e.g. {Zip Gun}'s 1 damage during strike resolution. An option the weapon
grants the bearer is not available when the retainer used it: {Garrote} does not let the
employer burn the opposing vampire. A limit on the bearer's use does not limit the
retainer — {Ghoul Retainer} may use {Jar of Skin Eaters} with nothing on it.

A card that restricts a minion's use of equipment does not reach that minion's retainers,
e.g. {Spiritual Protector}.

#### 5.6.2 Using a weapon is not a strike

The retainer's use resolves the weapon's whole text, not only damage: {Rowan Ring} sends
to torpor, {Flash Grenade} ends combat, {Weighted Walking Stick} burns its counters.

It is not a strike. It gives the employer no maneuver, no press and no additional strike,
e.g. {Meat Hook}. A retainer that does strike gains no additional strikes from its
employer.

A retainer cannot play ammo cards, not even through a {Magazine}. It does benefit from
ammo the employer played in an earlier round, e.g. {Scattershot}.

#### 5.6.3 Damage from a retainer

Damage inflicted by a retainer is environmental damage and the retainer is its source.
Immunity to retainers, or to that type of retainer, stops it.[^5-6-2]

An effect conditioned on the retainer being ready still resolves if the opposing strike
burns the retainer that round, e.g. {Bestial Vengeance}.

#### 5.6.4 Retainers as targets, and effects outliving them

An action that targets a retainer does not target the minion carrying it, so cards keyed
to actions directed at a minion do not apply, e.g. {Detect Authority} [ani].[^5-6-3]

A rider keyed to a minion does nothing when the target is a retainer, e.g. {Shadow Twin}
at [OBT].

An effect the retainer has already produced survives the retainer being burned or stolen:
{Camarilla Vitae Slave}'s chosen Discipline lasts to the controller's next unlock
phase.

#### 5.6.5 Entering play

A retainer is usable the turn it is employed; the "cannot act this turn" restriction is on
recruited allies, [§5.5.4](#554-entering-play-and-acting)'s.[^5-6-4]

### 5.7 Special minion classes & traits

#### 5.7.1 Subtypes

A minion's subtype is what its type line prints, and nothing else. Ghouls are monsters
and are not mortal; animals are neither mortal nor monster.[^5-7-1] The card name is not
a subtype: {Camarilla Vitae Slave} is a retainer with no subtype, and {Gargoyle Slave} is
an ally, neither a slave nor a Gargoyle. An effect naming a subtype, e.g.
{Abjure} ending a combat between a monster and a mortal, reads only that line.

#### 5.7.2 Slaves

A slave locking to take a blocked clan member's place cancels the combat, unlocks the
acting vampire, and enters a new combat with the blocker ([RBK traits]); see [§3.5](#35-action-repetition-nra-and-canceled-actions) for
canceled combats. The slave becomes the combatant but never the acting minion.[^5-7-2]
It cannot play a card whose use requires it to be acting, e.g. {Shadow Boxing} at
[OBF][POT], and the blocker cannot play a card requiring the opposing minion to be the
acting vampire, e.g. {Obedience}. Effects naming the canceled combat are dead, e.g.
{Sniper Rifle} cannot set the range. The acting vampire keeps what it independently
qualifies for after resolution, e.g. {Momentary Delay}.

#### 5.7.3 Infernal

The infernal unlock — the controller burning 1 pool during their unlock phase — is not
normal unlocking, so an effect preventing normal unlocking leaves it available.[^5-7-3]
It is not tied to the unlock step: a minion locked by another effect during that phase
can still be unlocked by paying, e.g. {Nightmares upon Nightmares}. An effect
keyed to unlocking *with the infernal trait* does not fire on any other unlock effect,
e.g. {Ruins of Charizel}. A card in play requiring an infernal vampire is
satisfied by one in torpor; see [§1.6](#16-requirements) for requirements on cards already in play.

#### 5.7.4 Black Hand

Black Hand is a trait, not a title, and is unrelated to sect: a vampire printed Black
Hand keeps it through a sect change.[^5-7-4] A card that confers the trait writes it on a
*Sabbat* vampire, so the grant stops applying if he ceases to be Sabbat, e.g. {Cadet},
{Mustajib}. A vampire who gains the trait by resolving an action has it for cards
played after that resolution, e.g. {Seraph's Second} ([§5.9](#59-traits-and-trait-changes)).

#### 5.7.5 Imbued

Imbued are mortal allies with life rather than blood, and their cost is their starting
life ([RBK appendix-imbued-rules]). Effects reading a minion's cost read that starting
life, e.g. {Keystone Kine} at [obf]; effects reading a cost to *recruit* read zero, since
an Imbued is influenced, not recruited, e.g. {Kindred Segregation}.[^5-7-5]

An Imbued in the uncontrolled region takes no blood, e.g. {Dreams of the Sphinx}.[^5-7-6]
An effect moving a crypt card to the ready region *with blood* gives an Imbued nothing:
it arrives with no life and is incapacitated at once, e.g. {Soul Gem of Etrius}. Where
such an effect compares capacity blind, read the starting life as the capacity.

Incapacitation is neither burning nor torpor, so effects keyed to either do not fire,
e.g. {Tension in the Ranks} burns no pool.[^5-7-7] An incapacitated Imbued is still in
play and may be locked to play a card, e.g. {Abjure} ([§5.3](#53-torpor)). A card that rewrites
the minion's subtype ends the class outright: an Imbued returned as a zombie ally by
{Pressing Flesh} has no creed, gains no conviction and cannot use virtues.

#### 5.7.6 Other traits

Scarce counts the apparent clan while the vampire is controlled, so a clan override
changes what the influencing player pays, e.g. {Clan Impersonation}; that same override
does not remove slave status, which is a separate trait.[^5-7-8] Sterile bars any action
to put a vampire into play, including the last step of a multi-action process: the action
placing the counter that completes {Call the Great Beast} is such an action, and {Blood
Cult Awareness Network} reads it the same way. A restriction on cards *requiring*
a discipline reaches only the option actually used, so a True Brujah may play a
multi-discipline card for a non-[cel] option. A [FLIGHT] restriction reads the
object of the effect, not its controller: a ranged strike barred against a flying minion
still reaches a retainer that minion employs, e.g. {Earthshock} ([§5.6](#56-retainers)).

An effect that required a class when it applied keeps applying after the class lapses,
e.g. {Concordance} on a vampire that stops being infernal ([§2.5](#25-duration-and-persistence), [§5.9](#59-traits-and-trait-changes)).[^5-7-9]

#### 5.7.7 Blood Brother circles

A vampire with no printed circle is in his own circle of one, and vampires sharing a
name do not share a circle. Two uncontrolled copies of {Angelo} or {New Blood} are
therefore in different circles, so an effect reading "the same circle" requires choosing
one; a vampire created by {The Embrace} is likewise in a circle of his own.[^5-7-10]

### 5.8 Titles

#### 5.8.1 Printed titles, granted titles, contests

An Independent vampire's printed "N votes (titled)" is a title of its own and is tied to no sect. It and its votes survive any sect change, e.g. {Ambrogino Giovanni}, {Xaviar}.[^5-8-1]

A title granted by a library card is tied to that title's sect. While the bearer is off-sect the title is dormant: he counts as untitled and cannot use the title to make himself titled, e.g. {Fee Stake: Perth} on a vampire who is no longer Anarch.[^5-8-2]

A card-granted title and a printed title of the same name are one title and contest each other: {Imperator} grants the same unique Camarilla Imperator title that {Karsh} prints.[^5-8-3]

Contesting a title costs 1 blood, paid by the vampire. Effects that raise the pool cost of contesting a card do not reach it, e.g. {Democritus}.[^5-8-4]

A contested title-providing card is turned face down out of play, and any action it provides is unusable while the contest lasts.[^5-8-5]

Effects keyed to a title are re-evaluated continuously. Capacity granted by a title is lost with the title. A card keyed to its bearer's title stops working when the title goes and resumes if it returns, e.g. {The Treatment}. An effect conditioned on the vampire being untitled is suppressed while he holds a title, e.g. {Bloodbath}.[^5-8-6]

Votes granted by an ability are not a title. The vampire remains untitled, so an ability conditioned on his being untitled keeps working, e.g. {Gerald Windham}, {Xeper, Sultan of Lepers}.[^5-8-7] See [§1.15](#115-cumulative-and-stacking-effects) for how such votes combine with a title gained later.

A vampire who leaves play and returns remembers titles gained and lost ([§6.4.1](#641-set-aside-out-of-play--the-card-remembers-everything)).[^5-8-8]

A representation of a titled vampire uses that title's votes even while another instance of the title is in play; it does not contest ([§1.4](#14-representation-and-placeholders)).[^5-8-21]

#### 5.8.2 Off-sect and off-clan titles

A vampire whose sect becomes inappropriate for his title loses its benefit: he gets no vote, is not considered titled, and yields the title immediately if it is contested or if he receives a new one. The benefit returns when his sect becomes appropriate again.[^5-8-9] The rule is trait-general — an inappropriate clan change does the same, e.g. {Clan Impersonation}, {Derange}.[^5-8-10] [§5.9](#59-traits-and-trait-changes) governs which of two competing trait changes stands, and see [§5.9](#59-traits-and-trait-changes) for the "is considered" override that {Writ of Acceptance} applies.

Mass sect-removal events apply the same rule to every holder, e.g. {Fall of the Camarilla}.[^5-8-11] Losing the benefit strips the title's votes and ballots but not the referendum structures the title defines: under {Fall of the Sabbat} the priscus subreferendum still happens, and a printed bonus ballot not granted by the title still applies, e.g. {Gratiano}.[^5-8-12]

An ability that grants its bearer a title cannot be used once he is off-sect: {Horatio Ballard} cannot call the referendum to become Prince of Chicago while Independent.[^5-8-13]

A card that puts a title on a vampire of a named sect has no legal target when no such vampire is in play, and cannot be played ([§3.1](#31-announcement-and-targets)).[^5-8-14]

#### 5.8.3 How requirements read titles

A requirement naming a sect-restricted title is also a requirement for that sect. A card requiring a baron is a card requiring an Anarch, so {Open War} counts as Anarch-requiring for {Powerbase: Los Angeles}.[^5-8-15]

A title inside a vampire's name is not a title: {The Baron} cannot play cards requiring a baron.[^5-8-16] A permission a card extends to Anarchs does not make the action one "requiring an Anarch", e.g. {Club Illusion}.[^5-8-17]

A title is a vampire trait ([§5.7](#57-special-minion-classes--traits)), so a card that fakes vampire traits reaches title requirements, e.g. {Vidal Jarbeaux}.[^5-8-22]

A vampire who can meet title requirements ({Vlad Tepes}, {Vidal Jarbeaux}, {Kemintiri}) is also considered a member of the title's underlying sect; the controller chooses how each requirement is met — any city, even an invented one.[^5-8-18] {Vidal Jarbeaux}'s own text additionally caps each requirement at once per game: required to be "a titled vampire" he must name a title, may use each title only once, and may choose the generic "X votes" title only once. A card canceled as it is played has still spent that use.[^5-8-23]

Such a requirement can be met after the sect has ceased to exist, e.g. a Camarilla or justicar requirement under {Fall of the Camarilla}.[^5-8-19]

Meeting a title requirement to call a political action grants none of that title's votes in the referendum.[^5-8-20]

Whether the ability reaches cards the Methuselah plays is per card: {Vidal Jarbeaux} meets requirements on master cards too; merged {Kemintiri} does not enable master card plays.[^5-8-24]

See [§1.6](#16-requirements) for the limits of requirement-faking: it substitutes only for the effects of the card played, only on a normal play, and only where the card prints the requirement ({Mata Hari}).

### 5.9 Traits and trait changes

#### 5.9.1 Actual change and temporary override

A card that says a vampire *becomes* a sect changes the actual sect, e.g. {Into the Fire},
{Go Anarch}. A card that says a minion *is considered* a sect while the card stays in play
is a temporary override on an unchanged underlying sect, e.g. {Writ of Acceptance}. The
override has precedence over the actual sect. A card that made the actual change and burns
itself on a sect change burns when an override lands, e.g. {Field Training}.[^5-9-1]

The value an override writes is fixed when the card is played: the clan and sect {Derange}
assigns do not change when the card is moved. When the override leaves play, the
underlying trait resurfaces. An effect writing one trait does not write another —
{Clan Impersonation} changes clan and leaves sect alone.[^5-9-2]

#### 5.9.2 Which effect governs

Where two effects write the same trait, the most recent governs. This is not sect-specific:
{Clan Impersonation} and {Derange} yield to whichever was played later, and
{Nar-Sheptha} supersedes an earlier {Deep Song} on who is the acting minion.[^5-9-3]
(See [§2.4](#24-simultaneous-effects-and-ordering) for simultaneous effects; see [§3.10](#310-changing-the-acting-minion) for acting-minion designation.)

An override survives a later change to the *underlying* trait. A vampire with
{Writ of Acceptance} who takes the rulebook action to become anarch is still Camarilla;
so is an Assamite carrying a {Tegyrius, Vizier} allegiance counter.[^5-9-4]

{Fall of the Camarilla} overrides sect but also redirects: a later effect that would set a
vampire to Camarilla sets him Independent instead while the Fall is in play. Such cards
remain legal to play. When the Fall leaves play, underlying sects resurface.
{Fall of the Sabbat} is the mirror case.[^5-9-5]

⚠ REVIEW — no ruling covers two live overrides on one trait where the earlier one lapses
first.

#### 5.9.3 Reading a changed trait

A changed trait is the trait for all purposes, and effects keyed to it re-evaluate as it
changes. Requirements are checked continuously while an action is in progress ([§1.6.1](#161-when-a-requirement-is-checked)): if
{The Red Question} makes the acting vampire Anarch during an action that required another
sect, the action fizzles — successful but with no effect. {Ministry} grants its extra intercept
only while the acting vampire is Sabbat, gained or lost mid-action; {Teresita, The
Godmother} likewise, and she is not the minion whose sect changed. An effect applied after
resolution reads the trait at that moment — {Warsaw Station} does not unlock an acting
vampire who is no longer Nosferatu when the unlock applies.[^5-9-6]

A vampire who plays cards "as if" he had a sect or title meets those requirements even
when the sect has been abolished: {Vlad Tepes} still plays Camarilla cards under
{Fall of the Camarilla}. Conversely, writing a trait onto a vampire does not make the
action one *described* by that trait — {The Red Question} is not an action that "makes
this vampire anarch", so {CrimethInc.} cannot follow it.[^5-9-7]

Allies have no sect. An ally permitted to play cards "as an Anarch vampire" is not Anarch
and gains nothing from cards keyed to the trait, e.g. {Grey Thorne}, {Vivienne Géroux} do
not benefit from {Anarch Manifesto, An}.[^5-9-8]

A vampire whose sect or clan changes to one inappropriate for his title loses the title's
benefit until it is appropriate again, and immediately yields the title if it is contested
or if he receives a new one.[^5-9-9]

---

## 6. Methuselahs and the Game

### 6.1 Owner and controller

**Base rules.** Ownership fixes which library, hand and ash heap a card belongs to.
Control fixes who plays it, who chooses, and what an oust removes. [RBK important-terms-of-the-game]

#### 6.1.1 Zones belong to the owner

A card leaves play to its **owner's** ash heap, hand or library, whoever controlled it.[^6-1-1]

- A minion put into play from another Methuselah's ash heap returns to that ash heap when
  burned, e.g. {Khazar's Diary (Endless Night)}.
- A card held face down under a stolen card travels with the card, but still goes to its
  owner's library or ash heap if an effect moves it there, e.g. {Storage Annex}.
- A card drawn from another Methuselah's library is in your hand and is played or discarded
  from it, but returns to its owner's zone, e.g. {Agaitas, The Scholar of Antiquities}.
- A vampire burned while under another Methuselah's control goes to his owner's ash heap,
  breaking every control effect, and from there to his owner's uncontrolled region. A rider
  printed for "you" still pays the Methuselah who controlled him when he burned,
  e.g. {The Capuchin}.

#### 6.1.2 Control decides what an oust removes

An oust removes what the ousted Methuselah **controlled**. Cards he owns but does not
control stay in play. [RBK important-terms-of-the-game]

A card put on a minion by another Methuselah's effect is controlled by that minion's
controller, so it survives its player's oust, e.g. {Anathema}.[^6-1-2]

Only printed text keeps control elsewhere. {Shackles of Enkidu} goes on the opposing
minion but stays with the controller of the vampire that used it, and changes hands with
that vampire. Taking control of a card already in play is [§6.3](#63-taking-control-of-a-card-in-play)'s.

A vampire in the uncontrolled region belongs to his last permanent controller, who need
not be his owner; what an oust then removes is [§6.5.3](#653-cards-of-an-ousted-methuselah)'s.

#### 6.1.3 Control decides who plays and who chooses

A card usable by a ready vampire other than the acting minion is still played by the
controller of the acting minion, and that vampire must be one he controls,
e.g. {Hidden Lurker}, {Zapaderin}.[^6-1-3]

The acting minion's controller makes the choices the action calls for, even when another
Methuselah steals its outcome: on a blocked recruit or employ action the acting minion's
controller still decides how the ally or retainer enters play, e.g. {Set's Call}.

A minion card is played by the Methuselah, not by the minion, so an effect reducing the
cost of "a card you play" reaches it, e.g. {The Shard, London}. That Methuselah
pays; see [§1.7](#17-costs-and-payment) for cost.

#### 6.1.4 Cards no one controls

A vampire in the uncontrolled region, or yielded in a contest, is not controlled and his
abilities do not apply, e.g. {Byzar}.[^6-1-4] He is not in play either, so an effect keyed
to a vampire burned *from play* does not reach him, e.g. {Blessed Resilience}.

Card text naming cards in play is not limited to cards you control unless it says so,
e.g. {Spell of Life} burns copies controlled by anyone.

### 6.2 Taking control of minions

**Base rules.** An ousted Methuselah's cards are removed from the game; cards he owns but
does not control stay in play. [RBK 5-ending-the-game]

#### 6.2.1 When the control change happens

A card that lets you burn counters to steal a minion offers the steal only at its own
timing; placing a counter does not open the opportunity, e.g. {Velvet Tongue}.[^6-2-1]
Where the card names a phase, the taking may happen at any point in it, including after
other actions, e.g. {Mind Rape}.

A reversion timed to the unlock phase happens at the start of that phase, before unlocking.
It cannot be ordered among unlock effects, and the minion does not unlock that phase, e.g.
{Malkavian Dementia}.

A steal does not change the minion's lock state; a card that wants it unlocked prints the
unlock, e.g. {Temptation}. Cards on the minion travel with it ([§6.3](#63-taking-control-of-a-card-in-play)).

#### 6.2.2 Stealing mid-action and mid-combat

Stealing a minion that is acting does not end the action. It continues against the same
target, and Methuselahs who already declined to block get no second opportunity; the new
controller, if eligible and not yet declined, may still block with the stolen
minion.[^6-2-2][^6-2-3]

If the target no longer qualifies after the steal, the action still resolves, succeeds and
is paid for, with no effect ([§3.4](#34-resolution-success-and-effect)). The same holds when the target empties the
action in response — {War Ghoul} locking and burning itself to burn a location.

Stealing a minion that is attempting to block makes the block attempt fail.
Stealing the acting minion instead leaves the block standing and the blocker locked, e.g.
{Revelation of Despair}. Stealing a minion in combat ends the combat, but damage
still to resolve resolves before control changes, e.g. {Temptation}.

An effect that stops the control change stops only that. Counters burned to attempt the
steal are not refunded, e.g. {The Diamond Thunderbolt} (see [§1.8](#18-playing-and-canceling-a-card) for canceled costs).

#### 6.2.3 Return to the previous controller

The minion returns in the state it is in, including torpor, and stays in torpor, e.g.
{Temptation}.[^6-2-4] Canceling an action the stolen minion was forced to take does not
keep it under the new controller; it still returns, e.g. {Spirit Marionette}.
"After resolution" effects apply before the return.

"Breaking any temporary control effects" hands the minion to its last permanent controller,
who then receives the rest of the effect and any card placed on it — {Lay Low} into that
Methuselah's uncontrolled region, {Descent into Darkness} out of play.

#### 6.2.4 An ousted Methuselah

A minion held on temporary control is removed from the game if its temporary controller is
ousted, e.g. {The Ailing Spirit}.[^6-2-5] It is likewise removed at the moment it should
return to a Methuselah who has been ousted, e.g. {Temptation}.

If that return can no longer occur, control never reverts and the temporary controller keeps
the minion indefinitely: {Parmenides} returns at his owner's next unlock phase, which an
ousted owner never has.[^6-2-6] What an oust removes under permanent control is
[§6.5.3](#653-cards-of-an-ousted-methuselah)'s.

#### 6.2.5 Effects after a control change

An effect that charges or credits "the controller" follows the new one: {Betrayer}'s pool
loss is taken by whoever controls the named vampire.[^6-2-7] Who takes or declines an
optional effect follows the card's wording, not control of the card ([§1.1](#11-card-text-and-the-rules)): {The Rack}
lets the chosen vampire gain blood, so the new controller of a stolen vampire decides
whether it gains.

A duration or use limit written against "your" turn or unlock reads against the current
controller and is not refreshed by the control change: {Rutor's Hand} grants no extra
unlock until a Methuselah begins a turn controlling the bearer, and a spent per-phase use
stays spent ([§1.2.1](#121-how-often-an-effect-may-be-used)). An effect
already generated survives the change: {Imposing Phantasm} returns the blood lost to damage
even if the opposing minion has changed controller.

### 6.3 Taking control of a card in play

#### 6.3.1 Requirements are not checked

Taking control of a card already in play is not playing it, so the card's requirements do
not apply to the new controller.[^6-3-1] A vampire may steal a retainer whose discipline
requirement it does not meet, e.g. {Far Mastery}, and a Methuselah may take a location
whose requirement no minion of his satisfies, e.g. {New Management}. The card stays
in play and works normally. See [§1.6](#16-requirements) for requirements; it states this in one sentence.

#### 6.3.2 Where the card is placed

An equipment, retainer or location on a minion whose control changes is placed on a minion
the new controller controls; the new controller chooses which one.[^6-3-2] If the new
controller has no minion to take it, it is burned. This is the rule for locations
that are equipment — the {Dartmoor, England} template — as much as for ordinary equipment
and retainers.

Placement happens only on an actual change of controller. A card "taken control of" by the
Methuselah who already controls it stays where it is and cannot be moved to another of his
minions.[^6-3-3] Naming your own card is still a legal play, e.g. {New Management} on your
own location.

#### 6.3.3 Cards carried along

Control of a card on a minion follows control of the minion: take the vampire and you take
its equipment and retainers.[^6-3-4] A card hosted on another card goes with its host, e.g.
the face-down card on {Storage Annex}, and the new controller may use it. A stolen
master Discipline card is controlled by the Methuselah of the vampire that took it, e.g.
{Ethan Locke}.

Where a card goes when it later leaves play is set by ownership, not control; see [§6.1](#61-owner-and-controller) for it.

#### 6.3.4 What does not move

A minion written into the card's effect when it was played is fixed and is not
re-chosen.[^6-3-5] {Incriminating Videotape} keeps the minion chosen at play: once the
equipment is stolen, that minion cannot block the new bearer and can block the old
one. Only the minion the card sits on is re-designated (6.3.2), never a choice
already made by the effect.

#### 6.3.5 When a forced transfer happens

Some cards hand themselves to another Methuselah during the controller's discard phase.
Where the transfer rides on an optional choice being taken, the card moves as soon as that
choice is made, ahead of any mandatory effects still pending, e.g. {Scourge of the
Enochians} when the burn option is used.[^6-3-6] Otherwise the receiving Methuselah takes
the card at his first opportunity to play effects, after the acting Methuselah's other
mandatory effects have applied. A controller who declares the end of his turn
cannot then use the card, even where the transfer was overlooked and the card is still in
front of him. See [§1.1](#11-card-text-and-the-rules) for overlooked mandatory effects.

### 6.4 Leaving and re-entering play

**Base rules.** Contested cards are face down and out of play; a vampire in the uncontrolled
region is not in play and is not a legal target. `[RBK contested-cards]`

#### 6.4.1 Set aside out of play — the card remembers everything

A card moved out of play without reaching the ash heap keeps its state. The wording template
is {Lay Low} and {Banishment}: cards and counters stay with the vampire but are out of play
while it is.

On return the vampire remembers every effect that had been applied to it, exactly as a
contested vampire does, including gained or lost titles.[^6-4-1] Cards on it return unlocked,
and a contested card on it drops out of the contest until it comes back. A vampire
brought out of the uncontrolled region keeps its blood and its cards.

Leaving play breaks temporary control effects: the vampire goes face down to its permanent
controller, and so does the card that removed it.[^6-4-2] See [§6.2](#62-taking-control-of-minions) for control changes; if the
permanent controller is ousted before the return condition is met, the current controller
keeps it.

#### 6.4.2 Through the ash heap — a new card

A card that reaches the ash heap and comes back is a new card: continuous effects applied to
it before are lost, e.g. {Possession}, and a returned ally or retainer is a new ally or
retainer for all game purposes, e.g. {Compel the Spirit}.[^6-4-3] See [§3.5](#35-action-repetition-nra-and-canceled-actions) for the No Repeated
Action consequence.

#### 6.4.3 Effects aimed at a card that has left play

An ongoing effect pointed at a card is suspended, not lost, while that card is out of play,
and resumes if and when it returns. This includes effects worded "for the rest of the game".
{The Rack} tracks its chosen vampire through a contest or a {Banishment} and gives blood
again on the vampire's return.[^6-4-4]

While the card is out of play the effect does nothing, because the card is not controlled.
Torpor is not out of play: an effect naming a controlled vampire still reaches one in
torpor. A pending effect that would land after the card has left play does not
land, e.g. the {Daring the Dawn} damage on a vampire already removed by
{Descent into Darkness}.

Effects the card already produced survive it leaving play. Counters it placed keep working,
e.g. {Tegyrius, Vizier}'s allegiance counters.[^6-4-5] Conversely a card in play reaches
only events after its arrival: {NRA PAC} does not affect equip actions performed before it
entered play. An in-play effect card is removed when the Methuselah who played it is
ousted ([§6.5](#65-pool-the-edge-and-ousting)).

#### 6.4.4 Leaving the ready region as a trigger

An effect keyed to a minion leaving the ready region fires whatever the route out — burned,
or the controller ousted — and fires even if the triggering card is burned in the same
event, e.g. {The Black Throne}, {Priority Contract}.[^6-4-6]

#### 6.4.5 Entering play

Merging an advanced vampire onto its base copy is not entering play, so cards keyed to a
vampire who entered play recently do not see it, e.g. {Chameleon},
{Legendary Vampire}.[^6-4-7]

A card returns at the moment its own text names and is not in play before then. {Parmenides}
returns as the unlock phase begins and unlocks as normal; a contested unique won face down
turns face up during the next unlock phase.[^6-4-8]

A card carrying a "do not replace until" clause is still not replaced until the condition is
met, even after the card itself is burned.[^6-4-9] See [§1.9](#19-replacement) for replacement timing.

### 6.5 Pool, the Edge and ousting

#### 6.5.1 Gaining and losing pool

Any decrease in pool — burning, paying a cost, a rival taking it — is losing pool; any
increase is gaining pool.[^6-5-1] An effect measured on pool actually lost counts nothing
when none was lost, e.g. {Dirty Little Secrets}.

A gain never offsets a loss: where one effect grants then takes pool, a card keying on pool
lost sees the loss, not the net, e.g. {Poison Pill} against {Ancient Influence}.[^6-5-2]

A card's cost and its pool gain happen together, with no oust between, and the printed cost
must still be affordable, e.g. {The Eternals of Sirius} ([§1.7.1](#171-when-a-cost-is-paid), [§1.7.2](#172-cost-arithmetic)).[^6-5-3]

A Methuselah obliged to pay more pool than she holds pays all of it and is ousted; the
effect still happens, e.g. {Thanks for the Donation}. The shortfall is real: an effect
saving her must cover the whole amount, not bring her to zero, e.g. {Life Boon}. A
mandatory cost is paid even when paying ousts you ([§1.1](#11-card-text-and-the-rules)).[^6-5-4]

Withdrawal fails on any pool loss, including pool spent as a cost, and a later gain does
not repair it [RBK 5-ending-the-game].

#### 6.5.2 When the oust resolves

An oust resolves as soon as pool reaches zero, ahead of anything else the same event
triggers. A minion spending its last life to pay for an action still resolves it in full,
and the oust precedes the effects triggered by that minion burning, e.g. {Herald of
Topheth}. If a cancel's cost ousts a player, handle the oust before the canceled card.[^6-5-5]

An effect applying after a referendum applies after the referendum's own effects, including
any oust and pool gained, so it cannot pre-empt an oust ({Voter Captivation}). A vote-title
ability of this shape still applies when the predator is ousted by the referendum, and does
not when the bearer's own controller is, e.g. {Lutz von Hohenzollern}.[^6-5-6]

When a card ends the turn on an oust ({Last Stand}), the turn ends after the current action
concludes: effects usable after action resolution are still played, e.g. {Freak Drive}. The
next turn then begins immediately, with no discard phase and no replacement.[^6-5-7]

#### 6.5.3 Cards of an ousted Methuselah

Cards controlled by an ousted Methuselah are removed from the game, not burned, so burn
triggers do not fire, e.g. {Charnas the Imp}; an ongoing effect such a card imposed is
canceled with it, e.g. {The Meddling of Semsith}. A vampire in another Methuselah's
uncontrolled region is removed if that Methuselah is ousted and stays if only its owner is,
e.g. {Lay Low}; a stolen minion due to return to an ousted one is removed.[^6-5-8] See [§6.4](#64-leaving-and-re-entering-play)
for control and [§6.2](#62-taking-control-of-minions) for theft.

Counters already placed on other Methuselahs stay active, e.g. {Shatter the Gate}. Leaving
the ready region because your controller is ousted is still leaving the ready region, so
effects keyed to that fire, e.g. {Priority Contract}. The minions are gone at once, so a
later effect needing one has no object ([§1.6](#16-requirements)): {Revelation of the Serpent} cannot unlock
when the target is ousted by the bleed.[^6-5-9]

#### 6.5.4 Victory points and the Edge

A Methuselah ousted at the same moment as her prey still scores the victory point but takes
no pool, and pool comes only from your own prey, never a grand-prey. Where two effects are
available at once you choose the order: the victory point before or after the 6 pool, or
your unlock-phase Edge pool before burning the Edge, e.g. {Sabbat Threat}.[^6-5-10]

A restriction on gaining pool is tested when the pool is gained, not when the action is
announced. Pool granted as part of a successful bleed arrives before any Edge that bleed
grants; pool from a separate post-resolution effect arrives after it. That decides both
halves of {The Rising}.[^6-5-11]

An effect moving or burning the Edge on an action applies at resolution, e.g. {Sargon}
(after the referendum concludes, for a political action), {Hrothulf}. A minion stealing the
Edge gets it even if the holder burned it during the action. A card that burns your own
Edge does nothing if you no longer control it at resolution, while the rest of its text
still applies ([§3.4](#34-resolution-success-and-effect)), e.g. {Enticement}. Legality is checked on announcement: the Edge
cannot be stolen while uncontrolled. "A new Methuselah gets the Edge" means one who did not
have it, e.g. {Curse of Nitocris}.[^6-5-12]

### 6.6 Master phase

**Base rules.** You receive one master phase action per master phase, unused actions are
lost, and you choose the order in which your master phase actions and any other
master-phase effects happen [RBK master-phase]. An out-of-turn master card spends an
action from your next master phase [RBK master-cards].

#### 6.6.1 Master phase action accounting

Cancellation does not unwind the accounting. A canceled out-of-turn master still costs its
player the master phase action against their next master phase, and that player still
cannot play a second out-of-turn master before that phase.[^6-6-1] A canceled trifle
grants no additional master phase action (see [§1.8](#18-playing-and-canceling-a-card) for this).[^6-6-2]

An additional master phase action handed to a Methuselah by a card effect is not that
Methuselah's trifle bonus. A trifle they play afterwards still grants its one, e.g.
{Wash}.[^6-6-3] The one-per-phase cap counts only actions gained from trifles
[RBK trifle].

#### 6.6.2 Out-of-turn masters

One out-of-turn master card between two of your master phases, regardless of how many
master phase actions you have [RBK master-cards]. An ability that grants access to
out-of-turn masters, or that pays for an extra master phase action, does not raise the
cap, e.g. {Synesios}.[^6-6-4]

An out-of-turn master played during your own turn under a card's own permission counts
against your **next** master phase, and bars a second out-of-turn master until then, e.g.
{Proxy Kissed}.

An out-of-turn master is played from hand in the normal fashion, so it can be canceled as
it is played. That holds where the card's text sends it from hand to the ash heap rather
than into play, e.g. {Vox Senis}.[^6-6-5] See [§1.8](#18-playing-and-canceling-a-card) for cancellation.

#### 6.6.3 Master cards on minions

A master card in play is controlled by the Methuselah who played it, even when it sits on
another Methuselah's minion [RBK master-cards]. Who takes or declines a choice its effect
offers follows the card's wording, not control of the card, e.g. {Perfectionist}
([§1.1.1](#111-mandatory-and-optional-effects)).

An upkeep printed as an alternative is a real choice, even when one branch burns the
minion: {Ex Nihilo} lets the vampire's controller burn 1 blood or burn the vampire during
the master phase.[^6-6-7]

#### 6.6.4 Abilities used during the master phase

Periodicity reads off the wording: an ability that costs a master phase action is spent per
action, one framed by the phase once per phase, e.g. {Nahir}, {Nonu Dis} — [§1.2.1](#121-how-often-an-effect-may-be-used)
owns the templates.[^6-6-8]

### 6.7 Influence phase and the uncontrolled region

**Base rules.** Transfers are granted at the start of your influence phase and cannot be
saved. The uncontrolled region is not in play.

#### 6.7.1 The uncontrolled region as a zone

A vampire in the uncontrolled region is not a legal target unless the card names the
region, and it cannot play cards, e.g. {Reform Body}.[^6-7-1]

An effect that adds blood to "a vampire in your uncontrolled region" cannot be used on an
imbued there — an imbued is not a vampire, e.g. {Dreams of the Sphinx}. When the
crypt card is chosen blind, from a crypt or from another Methuselah's uncontrolled region,
the effect works with whatever is found, and an imbued's cost counts as its capacity.

A library card that becomes a vampire stays a vampire if moved to the uncontrolled region
and can be influenced normally, e.g. {Creation Rites}.[^6-7-2]

Cards and counters on a vampire moved to the uncontrolled region stay with it, out of play,
and return with it, e.g. {Banishment}, {Thicker than Blood}. Suspended capacity
modifiers are [§5.1.1](#511-capacity)'s; what else the vampire remembers is [§6.4](#64-leaving-and-re-entering-play)'s.

A vampire moved to the uncontrolled region while under a temporary control effect goes to
its **last permanent controller's** region, which need not be the owner's, e.g.
{Banishment}, {Lay Low}; ousts are [§6.5.3](#653-cards-of-an-ousted-methuselah)'s.[^6-7-3]

#### 6.7.2 Influencing out

A vampire whose blood equals or exceeds its capacity may be moved to the ready region at
any moment during its controller's influence phase, not only at the end.[^6-7-4]

Excess blood drains off as it enters play — before a contest is entered, and before any
"as he enters play" effect is played. A vampire may be influenced out into a
contest it will lose; see [§1.13](#113-contests) for contests.

#### 6.7.3 Transfers and the influence-phase window

The number of transfers is fixed when the phase begins. A vampire influenced out during the
phase adds no transfers to it, e.g. {Ingrid Rossler}.[^6-7-5] Its other abilities are usable
for the remainder of that phase, e.g. {Angela Preston}; see [§1.5](#15-abilities-and-card-plays) for the general rule.

An effect granting an extra transfer may be used at any moment during the phase, not only
before the first transfer is spent, e.g. {Ennoia's Theater}.

Read the possessive. "During **your** influence phase" restricts a card to its controller's
phase; "during **the** influence phase" makes it usable in any Methuselah's, e.g.
{Gather}.

Transfers and card effects are independent. A Methuselah who takes no transfers, or who has
lost them all, may still use effects that add blood to uncontrolled vampires, e.g.
{Powerbase: Montreal}.

#### 6.7.4 Cards that require an uncontrolled vampire

A card whose play clause names a vampire in the uncontrolled region cannot be played with
no qualifying vampire there; the vampire is chosen on announcement ([§3.1](#31-announcement-and-targets)), e.g.
{Undue Influence}, {Break the Bonds} at [pre].[^6-7-6] The same bars an ability worded that
way, e.g. {Lázár Dobrescu}.

A clause that only describes what the effect does to the region is not a play requirement.
{Social Ladder} may be played with no older vampire in the uncontrolled region; its
influence-phase clause then removes the ready vampire and the blood is lost. See [§1.6](#16-requirements)
for the no-effect boundary.

### 6.9 Hand, draw & discard

**Base rules.** Default hand size is seven. Whenever an effect changes your hand size, or
adds or removes cards from your hand, you immediately discard down or draw up to match
[RBK drawing-cards].

#### 6.9.1 Hand size

Cards you play but do not replace count against your hand size, so a "do not replace"
clause works as a hand-size reduction: any further draw forces a discard, e.g.
{Hagar Stone}.[^6-9-1] Non-replacements accumulate while the effect lasts. A
hand-size change that comes and goes repeats the adjustment each time, e.g. a fresh combat
against {Raptor} makes the opponent draw up, then discard again.

A hand-size bonus can be taken more than once in a turn if you have more than one master
phase action, e.g. {Edward Neally}.[^6-9-2] It lasts as long as its source is in play:
{The Meddling of Semsith} keeps reducing your hand size after the chosen Methuselah is
ousted, and {Nahir}'s bonus survives her going to torpor ([§5.3](#53-torpor)). A card in play
that draws or raises your hand size may be used during an action, at any point where its
controller may play a card, e.g. {The Barrens}, {Dreams of the Sphinx}.

#### 6.9.2 The discard phase

"Until end of turn" durations expire in the discard phase. The acting Methuselah orders
that expiry against other discard-phase effects under normal sequencing ([§2.4](#24-simultaneous-effects-and-ordering)), e.g.
{Dreams of the Sphinx}.[^6-9-3] Discard-phase effects apply before an ally taken until end
of turn goes back; an ally you already lost control of does not go back at all.

Each discard phase action carries its own use of an ability keyed to one, e.g.
{Josef von Bauren} (see [§1.5](#15-abilities-and-card-plays) for the once-per-window rule). A Methuselah ousted during
their turn gets no discard phase ([§6.5.2](#652-when-the-oust-resolves)). A discard imposed by an action card lands after the
action resolves and after any combat it caused ([§2.3](#23-after-resolution-and-after-combat)).

#### 6.9.3 Draw and discard mechanics

When an effect discards several cards, all discards are made at once and replaced
afterwards, e.g. {Ruxandra}.[^6-9-4] Replacement draws therefore cannot be fed back in as
further discards. An effect that redirects the discarded cards acts only once every
discard and redraw is done, e.g. {Rachel Brandywine} shuffling them back. A discard
you cannot make in full is made as far as you can ([§1.7](#17-costs-and-payment)).

"Draw, then discard" does not restrict the discard to the cards just drawn; discard any
card in hand.[^6-9-5] A trigger reading "each time you replace a card" sees every
replacement draw, whatever took the card out of hand, e.g. {Infernal Pursuit}. A
trigger keyed to replacing a card you *played* does not see extra draws granted by other
cards: {Agaitas, The Scholar of Antiquities} does not redirect a {Learjet} additional
draw. Cards returned to an empty library are drawn at once if your hand is below
hand size, e.g. {Waste Management Operation}; that refill precedes any random discard the
same card imposes.

#### 6.9.4 Visibility

Library searches and replacement draws are private. You do not show the cards you look at
while searching, e.g. {Vast Wealth}, and no one sees a card drawn as replacement, e.g.
{Vaticination}.[^6-9-6] Where the cards are already public knowledge, you show which one
goes to hand, e.g. {Ashur Tablets}. An effect that reads a hand after the
replacement draw sees it without one when the replacement is delayed, e.g. {Troglodytia}
against a master card canceled by {Wash}; an optional extra draw is decided after the
normal replacement has been seen, e.g. {Learjet} (see [§1.9](#19-replacement) for replacement timing).

---

---

## Appendix A. Glossary of wording templates

<!-- TODO Phase 8: collect the wording templates named across the document. -->

## References

[^1-1-1]: [RTR 19980707](https://groups.google.com/g/rec.games.trading-cards.jyhad/c/t3BWHkOrdyE/m/1jH5udLMdiYJ) [LSJ 19980722](https://groups.google.com/g/rec.games.trading-cards.jyhad/c/0kbbA-SNchg/m/Urog66UtAzYJ) — {Aaron's Feeding Razor}, {The Ancestor's Talisman}, {Changeling Skin Mask}, {Enchanted Marionette}, {Writ of Acceptance}.
[^1-1-2]: [PIB 20121028](https://www.vekn.net/forum/rules-questions/39816-ec-2012-can-you-answer-these?start=6#39843) [LSJ 20051016](https://groups.google.com/g/rec.games.trading-cards.jyhad/c/s_At5syL66k/m/1eGsxyhDn1YJ) [LSJ 20051017](https://groups.google.com/g/rec.games.trading-cards.jyhad/c/s_At5syL66k/m/bCvu2ks001gJ) [LSJ 20051211](https://groups.google.com/g/rec.games.trading-cards.jyhad/c/TuwXiJ8A9mo/m/Ef_5xj46lA8J) — group "Mandatory additional strike" (G00134), {Lorrie Dunsirn}, {Eze, The Demon Prince}.
[^1-1-3]: [RTR 19941109](https://groups.google.com/d/msg/rec.games.deckmaster/_6CXoKTSLnw/FdG67-3HEAQJ) [RTR 20010710](https://groups.google.com/g/rec.games.trading-cards.jyhad/c/GsI1UyH54jU/m/x9LfDZX1vR4J) [ANK 20180420-2](https://www.vekn.net/forum/rules-questions/76522-majesty-against-serpent-s-numbing-kiss#86278) [LSJ 20020304-2](https://groups.google.com/g/rec.games.trading-cards.jyhad/c/L-8OGYP5xsE/m/h5WnSofVrfUJ) [PIB 20110918](https://www.vekn.net/forum/rules-questions/10458-frondator#10459) — {Repo Man}, {Vast Wealth}, {Serpent's Numbing Kiss}, group "Discounts for rescue" (G00075).
[^1-1-4]: [LSJ 19971215](https://groups.google.com/g/rec.games.trading-cards.jyhad/c/mfBmRrUKZQ0/m/5Py-ENuzoGwJ) [TOM 19951129](https://groups.google.com/g/rec.games.trading-cards.jyhad/c/jjBzopH-yrQ/m/L51mbZ5KGLkJ) — {Bomb}, {Bundi}, group "Wake" (G00115).
[^1-1-5]: [PIB 20150418](https://www.vekn.net/forum/rules-questions/70589-bima#70591) [ANK 20210309-3](https://www.vekn.net/forum/rules-questions/79065-master-cards-attached-to-a-stolen-minion#101806) [RBK important-terms-of-the-game](https://www.vekn.net/rulebook#important-terms-of-the-game) — {Third Tradition: Progeny}; {Perfectionist}, {Corporal Reservoir} (ruling removed from the database with group "Master on vampire who can use it" (G00031); original at vekn.net forum thread 79065).
[^1-1-6]: [LSJ 20100723](https://groups.google.com/g/rec.games.trading-cards.jyhad/c/0u5KQWiutdg/m/lAZoy4vIwiIJ) [PIB 20111002](https://www.vekn.net/forum/rules-questions/8235-re-coven-timing?start=18#11317) [LSJ 20021210-1](https://groups.google.com/g/rec.games.trading-cards.jyhad/c/kOZf54CTBUU/m/rVsPlZzjfpcJ) — {The Coven}, {Owain Evans, The Wanderer}, {Leandro}.
[^1-1-7]: [LSJ 20050628](https://groups.google.com/g/rec.games.trading-cards.jyhad/c/lN3eieA3xgs/m/c4ZoOWHUsPEJ) [LSJ 20011214-5](https://groups.google.com/g/rec.games.trading-cards.jyhad/c/gI44SEC82Yk/m/Kgipu7IXwWkJ) — groups "Prevent discipline based prevention" (G00141) and "Prohibits additional strikes" (G00137).
[^1-1-8]: [RTR 19941109](https://groups.google.com/d/msg/rec.games.deckmaster/_6CXoKTSLnw/FdG67-3HEAQJ) [LSJ 20010809-1](https://groups.google.com/g/rec.games.trading-cards.jyhad/c/LB6Zg4bEggc/m/g5eYOHiKrvUJ) — {Charnas the Imp}, group "Steal blood as a Hunt action" (G00121).
[^1-1-9]: [RTR 19980928](https://groups.google.com/g/rec.games.trading-cards.jyhad/c/Xva4_IRavxM/m/F-_fjzTmo88J) [LSJ 20001114](https://groups.google.com/g/rec.games.trading-cards.jyhad/c/qXSlM7Grq1c/m/cSDoQ9mw0z4J) [RTR 20010711](https://groups.google.com/g/rec.games.trading-cards.jyhad/c/GsI1UyH54jU/m/x9LfDZX1vR4J) — {Blessing of Durga Syn}, {Fractured Armament}, {Hidden Strength}, group "Immideate damage prevention" (G00154), {Absorb the Mind}.
[^1-1-10]: [ANK 20180518](https://www.vekn.net/forum/rules-questions/76623-big-game#87131) [LSJ 19990218](https://groups.google.com/g/rec.games.trading-cards.jyhad/c/B27J0sAwUuw/m/tKumJHAkOVMJ) — {Big Game}, {Major Boon}.
[^1-2-1]: [ANK 20180719-4](https://www.vekn.net/forum/rules-questions/76833-once-each-turn#89014) [ANK 20230122](https://www.vekn.net/forum/rules-questions/79926-maila-ability-new-promo-from-ec?start=0#107235) [ANK 20190207](https://www.vekn.net/forum/rules-questions/77344-black-chantry-rulebook-feedback?start=18#93328) [ANK 20220617](https://www.vekn.net/forum/rules-questions/79835-nonu-dis-and-during-x-do-y#105494) [ANK 20200729](https://www.vekn.net/forum/rules-questions/78776-is-carver-s-meat-packing-and-storage-burn-hostage-counter-a-during-x-do-y#100448) [RBK wording-templates](https://www.vekn.net/rulebook#wording-templates) — group "Once each turn" (G00014), {Maila}, {Qawiyya el-Ghaduba}, {Nonu Dis}, {Carver's Meat Packing and Storage}.
[^1-2-2]: [LSJ 20081123](https://groups.google.com/g/rec.games.trading-cards.jyhad/c/_Pb29pBJ1kU/m/8ugWH0lVOtoJ) [LSJ 20001102-2](https://groups.google.com/g/rec.games.trading-cards.jyhad/c/LlPyLJjLdx0/m/eVTwHPkEgOMJ) [ANK 20191218](https://www.vekn.net/forum/rules-questions/62700-re-nahir-and-research-counters?start=6#98297) [ANK 20220617](https://www.vekn.net/forum/rules-questions/79835-nonu-dis-and-during-x-do-y#105494) [LSJ 20050215](https://groups.google.com/g/rec.games.trading-cards.jyhad/c/nxlYFsU10Uo/m/Teu243qv5JgJ) [ANK 20230116](https://www.vekn.net/forum/rules-questions/80266-confirmation-needed-about-phased-motion-detector#107207) [LSJ 20010111](https://groups.google.com/g/rec.games.trading-cards.jyhad/c/d3WSV1UXBV0/m/gvRQWzPxOzEJ) [RBK wording-templates](https://www.vekn.net/rulebook#wording-templates) — {Andre LeRoux}, {Courier}, {Nahir}, {Nonu Dis}, {NSA Trio}, {Phased Motion Detector}, {Angelica, The Canonicus}.
[^1-2-3]: [LSJ 20020814](https://groups.google.com/g/rec.games.trading-cards.jyhad/c/gt8wQhk76lA/m/qjDJXRLxM7cJ) [ANK 20180307-2](https://www.vekn.net/forum/rules-questions/76451-ellison-humboldt-and-matteus-flesh-sculptor?start=0#85598) [LSJ 20040617](https://groups.google.com/g/rec.games.trading-cards.jyhad/c/WxJVsEWWmbc/m/gbOBOI7T9kwJ) [LSJ 20100206-2](https://groups.google.com/g/rec.games.trading-cards.jyhad/c/reXyybyIYX8/m/jeCyjdiZ5T4J) [LSJ 20070320-2](https://groups.google.com/g/rec.games.trading-cards.jyhad/c/QPCnTltI2Rk/m/_DIkIPJSPTgJ) [ANK 20200420-2](https://www.vekn.net/forum/rules-questions/58209-santaleous-questions?start=6#99643) — {Maris Streck}, {Edith Blount}, {Slake the Thirst}, {Hukros}, {Santaleous}.
[^1-2-4]: [ANK 20230316](https://www.vekn.net/forum/rules-questions/80385-amulet-of-temporal-perception-burning-and-reuse#107638) [ANK 20221102-2](https://www.vekn.net/forum/rules-questions/80130-motf-hl-retribution#106694) [RBK wording-templates](https://www.vekn.net/rulebook#wording-templates) — {Amulet of Temporal Perception}, groups "Weapon once per combat" (G00045) and "Weapon once per round" (G00046), {Haqim's Law: Retribution}.
[^1-2-5]: [LSJ 20040127](https://groups.google.com/g/rec.games.trading-cards.jyhad/c/2b3SFZyo3ik/m/2hwET6zRCykJ) [ANK 20221102-2](https://www.vekn.net/forum/rules-questions/80130-motf-hl-retribution#106694) — {Owain Evans, The Wanderer}, {Haqim's Law: Retribution}.
[^1-2-6]: [ANK 20220204](https://www.vekn.net/forum/rules-questions/79634-multi-dust-up-question#104626) [LSJ 20100206](https://groups.google.com/g/rec.games.trading-cards.jyhad/c/cAGrXqpO-YQ/m/GJHdeYt0GdUJ) [LSJ 20030224](https://groups.google.com/g/rec.games.trading-cards.jyhad/c/67261v339Ds/m/um8V7VVp2Y4J) [ANK 20180627-1](https://www.vekn.net/forum/rules-questions/76757-inscription-and-mirror-walk#88419) — {Dust Up}, {Asguresh}, group "Cancel" (G00058), {Inscription}.
[^1-2-15]: [ANK 20190117-1](https://www.vekn.net/forum/rules-questions/77308-mask-of-a-1000-faces-and-bleed-modifiers#92987) — {Mask of a Thousand Faces}.
[^1-2-7]: [ANK 20220705](https://www.vekn.net/forum/rules-questions/79895-question-regarding-using-a-minion-card-text-ability-when-locked#105630) [LSJ 20100705](https://groups.google.com/g/rec.games.trading-cards.jyhad/c/Dm_Zqyjdx8s/m/Fw-T7QAU8mkJ) [RBK wording-templates](https://www.vekn.net/rulebook#wording-templates) — groups "Unconditional referendum ability" (G00039) and "Non-locking referendum ability" (G00040).
[^1-2-8]: [LSJ 20100909](https://groups.google.com/g/rec.games.trading-cards.jyhad/c/9Mn1QueD1I4/m/5hwidUeZH6EJ) [ANK 20220615](https://www.vekn.net/forum/rules-questions/72394-re-kaymakli-fragment?start=6#105476) [ANK 20200810](https://www.vekn.net/forum/rules-questions/78797-easy-nra-question-for-bindusara#100517) [RBK action-card-or-card-in-play](https://www.vekn.net/rulebook#action-card-or-card-in-play) — group "Provide multiple actions" (G00035), {Annazir}, {Bindusara, Historian of the Kindred}.
[^1-2-9]: [LSJ 20040518](https://groups.google.com/g/rec.games.trading-cards.jyhad/c/4emymfUPwAM/m/B2SCC7L6kuMJ) [ANK 20210309-2](https://www.vekn.net/forum/rules-questions/79005-rulebook-gaining-votes?start=6#101807) [LSJ 20020429](https://groups.google.com/g/rec.games.trading-cards.jyhad/c/7ZfedGTVt9g/m/kQnfy7J_UYkJ) — {Filchware's Pawn Shop}, group "Vote playable once per game" (G00030), group "Since your last turn" (G00010).
[^1-2-10]: [TOM 19960521](https://groups.google.com/g/rec.games.trading-cards.jyhad/c/poYD3n0TKGo/m/xvU5HW7lBxMJ) — group "Optional press" (G00096); as previously recorded for member {Dust to Dust}, the ruling covered its optional maneuver as well.
[^1-2-11]: [ANK 20191108](https://www.vekn.net/forum/rules-questions/78081-eyes-of-the-beast#97710) — {Eyes of the Beast}.
[^1-2-12]: [RTR 19980623](https://groups.google.com/g/rec.games.trading-cards.jyhad/c/tSpd9dtTElc/m/-CuHJF54_n0J) [LSJ 20021122-2](https://groups.google.com/g/rec.games.trading-cards.jyhad/c/1hL0-URtroc/m/iF5fPuJC39IJ) [ANK 20211112](https://www.vekn.net/forum/rules-questions/79475-amaranth-anathema#103872) — {Anathema}.
[^1-2-13]: [LSJ 20001127-2](https://groups.google.com/g/rec.games.trading-cards.jyhad/c/KInac4MQMuA/m/LnpxH08HVbMJ) [RTR 20020501](https://groups.google.com/g/rec.games.trading-cards.jyhad/c/M1snoR2msbQ/m/RFwCmX3anDkJ) [LSJ 20031011](https://groups.google.com/g/rec.games.trading-cards.jyhad/c/GZZJjzAeuxU/m/HtZKyNDKiOAJ) — {Escaped Mental Patient}, {Flaming Candle}, {First Tradition: The Masquerade}.
[^1-2-14]: [LSJ 20090205](https://groups.google.com/g/rec.games.trading-cards.jyhad/c/l5bUtHOejmc/m/Ksw_nyldc3QJ) [LSJ 19980105](https://groups.google.com/g/rec.games.trading-cards.jyhad/c/PzVC-AeFuUQ/m/ncbtQyYNpFQJ) [LSJ 20081123](https://groups.google.com/g/rec.games.trading-cards.jyhad/c/_Pb29pBJ1kU/m/8ugWH0lVOtoJ) — {Andre LeRoux}, {Archon Investigation}.
[^1-3-1]: [LSJ 20080114](https://groups.google.com/g/rec.games.trading-cards.jyhad/c/aMum-K7LEeo/m/94iN92zwYTcJ) [ANK 20220824](https://www.vekn.net/forum/rules-questions/79986-the-british-museum-london-and-pier-13-port-of-baltimore?start=6#106118) — group "Locquipments" (G00047), {The British Museum, London}.
[^1-3-2]: [ANK 20220824](https://www.vekn.net/forum/rules-questions/79986-the-british-museum-london-and-pier-13-port-of-baltimore?start=6#106118) [ANK 20221026](https://www.vekn.net/forum/rules-questions/80117-the-british-museum-london#106651) [LSJ 20080107](https://groups.google.com/g/rec.games.trading-cards.jyhad/c/XpZ6F53jK-c/m/wB6HHGzgFi4J) [LSJ 20080109](https://groups.google.com/g/rec.games.trading-cards.jyhad/c/XpZ6F53jK-c/m/EQWCLO72MbsJ) [LSJ 20080114](https://groups.google.com/g/rec.games.trading-cards.jyhad/c/aMum-K7LEeo/m/94iN92zwYTcJ) — {The British Museum, London}, {Therbold Realty}, {Marie Faucigny}, {Regina Blake}.
[^1-3-3]: [LSJ 19971001-2](https://groups.google.com/g/rec.games.trading-cards.jyhad/c/RY_nhdykKP0/m/9boDeD_qAXAJ) [LSJ 20080114](https://groups.google.com/g/rec.games.trading-cards.jyhad/c/aMum-K7LEeo/m/94iN92zwYTcJ) [ANK 20221210](https://www.vekn.net/forum/rules-questions/80203-danylo-special-clarification#106965) [LSJ 20020211](https://groups.google.com/g/rec.games.trading-cards.jyhad/c/ubqDaLeG3qo/m/TGKL07dP8NkJ) [LSJ 20060221](https://groups.google.com/g/rec.games.trading-cards.jyhad/c/OC41YQYfJO4/m/g_y0RPVpXNkJ) — {Magic of the Smith}, {Danylo}, {Reg Driscoll}.
[^1-3-4]: [LSJ 20050315](https://groups.google.com/g/rec.games.trading-cards.jyhad/c/COcJX2hHP-E/m/YLUW8FaGP0kJ) [LSJ 20050413-1](https://groups.google.com/g/rec.games.trading-cards.jyhad/c/1TXRhYopt70/m/OZMBb0AlfOUJ) [LSJ 20050413-2](https://groups.google.com/g/rec.games.trading-cards.jyhad/c/1TXRhYopt70/m/YnL8Fiaim0IJ) — {Beast, The Leatherface of Detroit}, {Enkidu, The Noah}, {Helen Fairchild}, {Lorrie Dunsirn}.
[^1-3-5]: [RTR 19960112](https://groups.google.com/g/rec.games.trading-cards.jyhad/c/d3n3StNS7no/m/k2NmZFUl9fAJ) [LSJ 19971002](https://groups.google.com/g/rec.games.trading-cards.jyhad/c/RY_nhdykKP0/m/fOdKJtOy4kgJ) [LSJ 20090324](https://groups.google.com/g/rec.games.trading-cards.jyhad/c/Zc_ogoVhsug/m/tJ2VBYI7resJ) — group "Locquipments" (G00047), {Disputed Territory}, {Dominate Kine}.
[^1-3-6]: [PIB 20150924-2](https://www.vekn.net/forum/rules-questions/73293-adana-de-sforza-combo-cards#73307) [LSJ 20031221](https://groups.google.com/g/rec.games.trading-cards.jyhad/c/OJW-3jpaM04/m/LLYmjhAWO7kJ) — {Adana de Sforza}, {Conrad Adoula}, {Horrock}, {Jane Sims}, {Nergal}, {Rex, The Necronomist}, {Scout Youngwood}, {Henry Taylor}.
[^1-3-7]: [ANK 20230824](https://www.vekn.net/forum/news-and-announcements/80782-the-line-pack-alpha?start=6#109157) [RTR 20070707](https://groups.google.com/g/rec.games.trading-cards.jyhad/c/vSOt2c1uRzQ/m/MsRAv47Cd4YJ) [ANK 20220704](https://www.vekn.net/forum/rules-questions/79890-charming-lobby-a-political-action-card-krc?start=0#105616) [LSJ 20070927](https://groups.google.com/g/rec.games.trading-cards.jyhad/c/VaSQ7JL2N2Y/m/BenDHsAETG4J) [LSJ 20050407](https://groups.google.com/g/rec.games.trading-cards.jyhad/c/fDl3t2lJ3Pc/m/pdmWZOwllPMJ) [LSJ 20100527](https://groups.google.com/g/rec.games.trading-cards.jyhad/c/Tr3X4DsZr-8/m/O06iXN6LtzsJ) [ANK 20220818](https://www.vekn.net/forum/rules-questions/79972-is-enhanced-coagulant-still-an-equipment-after-a-successful-strike?start=6#106039) — {Pack Alpha}, groups "Lock to reduce cost" (G00130) and "Equip/employ/recruit outside of an action" (G00131), {Charming Lobby}, {Shackles of Enkidu}, {Enhanced Coagulant}.
[^1-3-8]: [ANK 20180719-3](https://www.vekn.net/forum/rules-questions/76834-moving-equipment-with-requirements#89044) — group "Clan equipment" (G00013).
[^1-3-9]: [LSJ 20051113](https://groups.google.com/g/rec.games.trading-cards.jyhad/c/L-ctaLucuKU/m/dG0EKdSd4g0J) — group "Reflex" (G00060).
[^1-4-1]: [LSJ 20071001-1](https://groups.google.com/g/rec.games.trading-cards.jyhad/c/bb9ac-kN5WY/m/l8mfTxW6a6gJ) [LSJ 20040623](https://groups.google.com/g/rec.games.trading-cards.jyhad/c/PlPp5igHOEg/m/6IOQqMJA53gJ) — {Agent of Power}, {Absimiliard's Army}.
[^1-4-2]: [LSJ 20040623](https://groups.google.com/g/rec.games.trading-cards.jyhad/c/PlPp5igHOEg/m/6IOQqMJA53gJ) [LSJ 20071003](https://groups.google.com/g/rec.games.trading-cards.jyhad/c/duRrP46XygI/m/zAHBdn4JnNQJ) [LSJ 20040812](https://groups.google.com/g/rec.games.trading-cards.jyhad/c/n_0DGDsWG0E/m/lxG2zMPetwAJ) — {Absimiliard's Army}, {Père Lachaise, France}.
[^1-4-3]: [LSJ 20100213](https://groups.google.com/g/rec.games.trading-cards.jyhad/c/vXDkYrTmkws/m/sKy3jXz7AB4J) [LSJ 19991110](https://groups.google.com/g/rec.games.trading-cards.jyhad/c/5hDqAMewLtg/m/fib2UDF58CUJ) — {Illusions of the Kindred}.
[^1-4-4]: [LSJ 20071014](https://groups.google.com/g/rec.games.trading-cards.jyhad/c/Bom6ae7qjbI/m/OznLIo66qgsJ) [LSJ 20100325-2](https://groups.google.com/g/rec.games.trading-cards.jyhad/c/aC6OOfaulbM/m/svWv9UqH6isJ) — {Compel the Spirit}, {Spell of Life}, {Pressing Flesh}.
[^1-4-5]: [LSJ 20020426](https://groups.google.com/g/rec.games.trading-cards.jyhad/c/xFGNrTa9CPk/m/FNTh_ouCem8J) — {Reality Mirror}.
[^1-5-1]: [ANK 20180805](https://www.vekn.net/forum/rules-questions/76897-a-question-on-function-of-safe-passage#89666) [ANK 20221120](https://www.vekn.net/forum/rules-questions/80172-secure-haven-and-cards-with-targeted-effects-that-are-already-in-play#106845) — {Safe Passage}, {Secure Haven}.
[^1-5-2]: [LSJ 20070403](https://groups.google.com/g/rec.games.trading-cards.jyhad/c/TJ2ktt_1tjk/m/fdH_x9tDmN8J) [LSJ 20070413](https://groups.google.com/g/rec.games.trading-cards.jyhad/c/umdINigMKqs/m/lfUAxTnfttIJ) — {Champion}, {Discern}, {Donate}, {Hide}, {Surge}, {Vigilance}.
[^1-5-4]: [PIB 20150720](https://www.vekn.net/forum/rules-questions/72088-action-modifiers#72124) [RTR 19941109](https://groups.google.com/d/msg/rec.games.deckmaster/_6CXoKTSLnw/FdG67-3HEAQJ) [ANK 20220705](https://www.vekn.net/forum/rules-questions/79895-question-regarding-using-a-minion-card-text-ability-when-locked#105630) [LSJ 20100705](https://groups.google.com/g/rec.games.trading-cards.jyhad/c/Dm_Zqyjdx8s/m/Fw-T7QAU8mkJ) [LSJ 20001102](https://groups.google.com/g/rec.games.trading-cards.jyhad/c/LlPyLJjLdx0/m/mXimdmP14GEJ) [RBK important-terms-of-the-game](https://www.vekn.net/rulebook#important-terms-of-the-game) — {Make an Example}, {Montano}, {Toby}, {Paul Forrest, False Prophet}, {Courier}, groups "Unconditional referendum ability" (G00039) and "Non-locking referendum ability" (G00040).
[^1-5-5]: [LSJ 20011022](https://groups.google.com/g/rec.games.trading-cards.jyhad/c/KMg4MwD-Jn0/m/Vl-TD6DfyhoJ) [LSJ 20100902-2](https://groups.google.com/g/rec.games.trading-cards.jyhad/c/mFpx91METxM/m/ETLGtyQfvksJ) [LSJ 20010813-2](https://groups.google.com/g/rec.games.trading-cards.jyhad/c/zkKhvgZy9hA/m/8uH5sgbQaSoJ) [ANK 20220705](https://www.vekn.net/forum/rules-questions/79895-question-regarding-using-a-minion-card-text-ability-when-locked#105630) [LSJ 20100705](https://groups.google.com/g/rec.games.trading-cards.jyhad/c/Dm_Zqyjdx8s/m/Fw-T7QAU8mkJ) [RBK torpor](https://www.vekn.net/rulebook#torpor) — group "Ability usable in torpor" (G00027), {Marciana Giovanni, Investigator}, {Pariah}, {Tori Longwood}, {Montano}.
[^1-5-6]: [ANK 20180517](https://www.vekn.net/forum/rules-questions/76447-rules-team-rulings-rtr-03-03-2018?start=30#87041) [RTR 20180303](https://www.vekn.net/forum/rules-questions/76447-rules-team-rulings-rtr-03-03-2018#85536) [RBK recruit-ally](https://www.vekn.net/rulebook#recruit-ally) — group "Allies with 'lock this ally to' abilities" (G00119), {Abomination}, {Underbridge Stray}, {War Ghoul}, {Paul "Sixofswords29" Moreton}.
[^1-5-14]: [LSJ 20070301](https://groups.google.com/g/rec.games.trading-cards.jyhad/c/-CeFWHQ2wXE/m/TtbyH4rAcoIJ) — {The Grandest Trick}.
[^1-5-7]: [TOM 19960109](https://groups.google.com/g/rec.games.trading-cards.jyhad/c/gB3xexVAV0s/m/zGnkjIMjyJsJ) [RTR 20180511](https://www.vekn.net/forum/rules-questions/76595-rules-team-rulings-rtr-11-05-2018#86780) [LSJ 20030605](https://groups.google.com/g/rec.games.trading-cards.jyhad/c/jlVA4lGfpkA/m/XrmR0nLZ-NUJ) [LSJ 20020814](https://groups.google.com/g/rec.games.trading-cards.jyhad/c/gt8wQhk76lA/m/qjDJXRLxM7cJ) [ANK 20180307-2](https://www.vekn.net/forum/rules-questions/76451-ellison-humboldt-and-matteus-flesh-sculptor?start=0#85598) [ANK 20200420-2](https://www.vekn.net/forum/rules-questions/58209-santaleous-questions?start=6#99643) [LSJ 20040617](https://groups.google.com/g/rec.games.trading-cards.jyhad/c/WxJVsEWWmbc/m/gbOBOI7T9kwJ) — {Corpse Minion}, {Count Zaroff}, {General Perfidio Díos}, {Maris Streck}, {Matteus, Flesh Sculptor}, {Santaleous}, {Edith Blount}.
[^1-5-8]: [TOM 19960109](https://groups.google.com/g/rec.games.trading-cards.jyhad/c/gB3xexVAV0s/m/zGnkjIMjyJsJ) [LSJ 20070320-2](https://groups.google.com/g/rec.games.trading-cards.jyhad/c/QPCnTltI2Rk/m/_DIkIPJSPTgJ) [ANK 20190725](https://www.vekn.net/forum/rules-questions/77813-card-questions#95969) [ANK 20191218](https://www.vekn.net/forum/rules-questions/62700-re-nahir-and-research-counters?start=6#98297) [LSJ 20020814](https://groups.google.com/g/rec.games.trading-cards.jyhad/c/gt8wQhk76lA/m/qjDJXRLxM7cJ) [ANK 20221229](https://www.vekn.net/forum/rules-questions/80231-clarifications-on-osric-vladislav-s-wording#107109) — {Forest of Shadows}, {Hukros}, {Josef von Bauren}, {Nahir}, {Osric Vladislav}.
[^1-5-9]: [LSJ 20091021-2](https://groups.google.com/g/rec.games.trading-cards.jyhad/c/x5oG5J7Egtg/m/yafJrZAoqjgJ) — {Nergal}.
[^1-5-10]: [LSJ 19970718](https://groups.google.com/g/rec.games.trading-cards.jyhad/c/QujjxfQHYzw/m/S4tNTm4gpi8J) [SFC 19960819](https://groups.google.com/g/rec.games.trading-cards.jyhad/c/G40EE8vCBB8/m/Bj3qpDZ_VLkJ) — group "Permanents that increase bleed amount during an action" (G00117), {Spiridonas}.
[^1-5-11]: [ANK 20221021](https://www.vekn.net/forum/rules-questions/80108-patagia#106628) — {Watenda}, {White Lily}.
[^1-5-12]: [RTR 20010710](https://groups.google.com/g/rec.games.trading-cards.jyhad/c/GsI1UyH54jU/m/x9LfDZX1vR4J) — {Drum of Xipe Totec}.
[^1-6-1]: [LSJ 20030214](https://groups.google.com/g/rec.games.trading-cards.jyhad/c/A3U-Dy1yx8Y/m/2LHXvLrmybwJ) [ANK 20171212](https://www.vekn.net/forum/rules-questions/76334-slave-mental-maze-interaction?start=12#84553) [LSJ 20030202](https://groups.google.com/g/rec.games.trading-cards.jyhad/c/ox7A8EvaNJo/m/5CyLJo7pmUYJ) [ANK 20210124](https://www.vekn.net/forum/rules-questions/79001-the-question-of-the-month-action-fizzles#101492) [RBK requirements-for-playing-cards](https://www.vekn.net/rulebook#requirements-for-playing-cards) — {Undead Persistence}, {Mental Maze}, {Maxwell}, {The Red Question}.
[^1-6-2]: [PIB 20121031](https://www.vekn.net/forum/rules-questions/39816-ec-2012-can-you-answer-these?start=18#39908) — group "Require Gehenna" (G00009).
[^1-6-3]: [LSJ 20051110](https://groups.google.com/g/rec.games.trading-cards.jyhad/c/fMW3tSF5oUc/m/-Eft6gDzxmsJ) — {Orun}.
[^1-6-4]: [LSJ 20030607](https://groups.google.com/g/rec.games.trading-cards.jyhad/c/DG7s60pwv1U/m/FPqlZYJ3upcJ) [ANK 20180801](https://www.vekn.net/forum/rules-questions/76839-seal-of-veddartha#89529) [ANK 20221208](https://www.vekn.net/forum/rules-questions/80197-clarification-on-using-orun-and-changing-sect#106952) [LSJ 20100527](https://groups.google.com/g/rec.games.trading-cards.jyhad/c/Tr3X4DsZr-8/m/O06iXN6LtzsJ) — {Seal of Veddartha}, {The Crusader Sword}, {Agate Talisman}, {Blade of Enoch}, {Stolen Police Cruiser}, {Exile}, {Soul Gem of Etrius}.
[^1-6-5]: [LSJ 19980303](https://groups.google.com/g/rec.games.trading-cards.jyhad/c/Q_kKQiACZqk/m/Nu-cOlCq1cgJ) [LSJ 20050128-2](https://groups.google.com/g/rec.games.trading-cards.jyhad/c/HVy8iPUxNbI/m/jXmrJxMaJ9MJ) [ANK 20221011-4](https://www.vekn.net/forum/rules-questions/79988-keminitiri-closed-session#106540) [RTR 20070707](https://groups.google.com/g/rec.games.trading-cards.jyhad/c/vSOt2c1uRzQ/m/MsRAv47Cd4YJ) [PIB 20150304](https://www.vekn.net/forum/rules-questions/69627-vlad-tepes-regent?start=6#69653) — {Talaq, The Immortal}, {Kemintiri}, {Vlad Tepes}.
[^1-6-6]: [ANK 20190203](https://www.vekn.net/forum/rules-questions/77343-ennoia-s-theater-do-i-need-both-gangrel-and-gangrel#93265) [LSJ 20050128](https://groups.google.com/g/rec.games.trading-cards.jyhad/c/HVy8iPUxNbI/m/ZHGTnprQjGUJ) [LSJ 20080603](https://groups.google.com/g/rec.games.trading-cards.jyhad/c/9usl4idp-pY/m/LuT1iK1b4QIJ) — {Defender of the Haven}, {Derange}, {Ennoia's Theater}, group "Require a Baron" (G00037), {Powerbase: Los Angeles}, {Salvador Garcia}.
[^1-6-7]: [LSJ 20100204](https://groups.google.com/g/rec.games.trading-cards.jyhad/c/o5Xnzc8G774/m/yovVizGngKsJ) [LSJ 20051116-2](https://groups.google.com/g/rec.games.trading-cards.jyhad/c/5Bovsb8I6R0/m/_KIlJky3D5oJ) [LSJ 20071001-1](https://groups.google.com/g/rec.games.trading-cards.jyhad/c/bb9ac-kN5WY/m/l8mfTxW6a6gJ) [LSJ 20100422](https://groups.google.com/g/rec.games.trading-cards.jyhad/c/tMEimr0yxLA/m/RWgvaOj6i9UJ) [LSJ 20040531](https://groups.google.com/g/rec.games.trading-cards.jyhad/c/oTb4vsFNi1s/m/pCwoAggb97UJ) [LSJ 20040518-2](https://groups.google.com/g/rec.games.trading-cards.jyhad/c/4emymfUPwAM/m/JF_o7OOoCbkJ) [LSJ 20100303](https://groups.google.com/g/rec.games.trading-cards.jyhad/c/jmmm0WRUPvs/m/x9pv1OmWFS4J) [LSJ 20100426](https://groups.google.com/g/rec.games.trading-cards.jyhad/c/BN3xmoZ0W1A/m/ui4w2OyGLjAJ) — groups "Put card in play ignoring requirements" (G00110) and "Equip/employ/recruit outside of an action" (G00131), {Abombwe}, {Agent of Power}, {Absimiliard's Army}, {Echo of Harmonies}.
[^1-6-8]: [LSJ 20071015](https://groups.google.com/g/rec.games.trading-cards.jyhad/c/Bom6ae7qjbI/m/1ov2qqChTdMJ) [LSJ 20100302-1](https://groups.google.com/g/rec.games.trading-cards.jyhad/c/jmmm0WRUPvs/m/ny5F1OnSUsEJ) [PIB 20111101](https://www.vekn.net/forum/rules-questions/12975-summon-history-reanimated-corpse#13169) — {Compel the Spirit}, {Pressing Flesh}, {Summon History}.
[^1-6-9]: [ANK 20200810](https://www.vekn.net/forum/rules-questions/78797-easy-nra-question-for-bindusara#100517) [RTR 20010710](https://groups.google.com/g/rec.games.trading-cards.jyhad/c/GsI1UyH54jU/m/x9LfDZX1vR4J) [TOM 19950407](https://groups.google.com/g/rec.games.trading-cards.jyhad/c/FWVnIu3zLAQ/m/ODGlyMGc_hgJ) [LSJ 20080702-4](https://groups.google.com/g/rec.games.trading-cards.jyhad/c/sCHpPQkjeAE/m/9GGAf6TbiP0J) [ANK 20210714](https://www.vekn.net/forum/rules-questions/79224-can-i-do-a-3rd-villein-in-a-vampire-if-i-have-only-1-pool-remaining#102697) — {Bindusara, Historian of the Kindred}, {Horrid Reality}, {Vast Wealth}, {Topaz}, {Villein}.
[^1-6-10]: [LSJ 19980831](https://groups.google.com/g/rec.games.trading-cards.jyhad/c/Za8AS17xXPM/m/Ttki0DplaeYJ) [LSJ 19990602](https://groups.google.com/g/rec.games.trading-cards.jyhad/c/tnBL-IWbBV4/m/71ehpSwV1eoJ) [ANK 20170309-2](https://www.vekn.net/forum/rules-questions/75650-pressing-flesh#81050) [ANK 20200320](https://www.vekn.net/forum/rules-questions/78531-does-deviki-get-around-can-not-play-discipline-cards-on-vampires-with-superior#99397) [LSJ 19980206](https://groups.google.com/g/rec.games.trading-cards.jyhad/c/p_uyqQgE9Ms/m/86kfy6jI0lUJ) [LSJ 20020426](https://groups.google.com/g/rec.games.trading-cards.jyhad/c/xFGNrTa9CPk/m/FNTh_ouCem8J) — {Heidelberg Castle, Germany}, {Rowan Ring}, {Shackles of Enkidu}, {Wooden Stake}, {War Ghoul}, {Deviki Prasanta}, {Lucian}, {Reality Mirror}.
[^1-6-11]: [TOM 19960226-1](https://groups.google.com/g/rec.games.trading-cards.jyhad/c/16y-ZD7Xats/m/oMeZDnSFdYAJ) [ANK 20180719-3](https://www.vekn.net/forum/rules-questions/76834-moving-equipment-with-requirements#89044) — {The Art of Love}, {The Book of Going Forth by Night}, {Far Mastery}, {Legend of the Leopard}, {Lure of the Serpent}, {Malkavian Time Auction}, {Putrescent Servitude}, {Restructure}, {Revelation of Ecstasy}, {Set's Call}, {Spirit Marionette}, {Transfusion}, group "Clan equipment" (G00013).
[^1-6-12]: [LSJ 20090415](https://groups.google.com/g/rec.games.trading-cards.jyhad/c/oDvJWs7majs/m/fAtt19fFsTcJ) [LSJ 20100119](https://groups.google.com/g/rec.games.trading-cards.jyhad/c/1eULCGaVcO0/m/eefMWzjoK0IJ) [LSJ 20090506](https://groups.google.com/g/rec.games.trading-cards.jyhad/c/887DQTpntKI/m/L-ETC1-5nR0J) [LSJ 20060209](https://groups.google.com/g/rec.games.trading-cards.jyhad/c/ZuOfZorIhhU/m/X5G1JfqDPhcJ) [LSJ 20100421](https://groups.google.com/g/rec.games.trading-cards.jyhad/c/Vp--M79gpqk/m/mah3wmaFYREJ) [LSJ 20080702-2](https://groups.google.com/g/rec.games.trading-cards.jyhad/c/sCHpPQkjeAE/m/8N5_G2gMHAIJ) — {Helicopter}, {Incriminating Videotape}, {Shilmulo Tarot}, {Flaming Candle}, {Dagger}, {Baseball Bat}.
[^1-6-13]: [PIB 20150105-2](https://www.vekn.net/forum/rules-questions/68482-topaz-successfully-equips-baby-yaga-successfully-employs#68483) [ANK 20210913](https://www.vekn.net/forum/rules-questions/79322-piper-and-sebastien-goulet#103113) [LSJ 20090116](https://groups.google.com/g/rec.games.trading-cards.jyhad/c/RQ3ARP9Kvfk/m/e-o1t79x1gUJ) [ANK 20210928](https://www.vekn.net/forum/rules-questions/79364-combo-piper-x-soul-of-earth#103363) [LSJ 20090115-1](https://groups.google.com/g/rec.games.trading-cards.jyhad/c/RQ3ARP9Kvfk/m/dBN_M7SnIHAJ) [ANK 20170309](https://www.vekn.net/forum/rules-questions/75649-reduce-ally-cost-and-piper-combo#81049) — {Synner-G}, {Topaz}, {Little Tailor of Prague}, {Sébastien Goulet}, {Kuyén}, {Soul of the Earth}, {Zhenga}.
[^1-6-14]: [LSJ 20100725](https://groups.google.com/g/rec.games.trading-cards.jyhad/c/9d1zMZfsfNo/m/l3fbDtbr9xwJ) [LSJ 20100303](https://groups.google.com/g/rec.games.trading-cards.jyhad/c/jmmm0WRUPvs/m/x9pv1OmWFS4J) [ANK 20180817](https://www.vekn.net/forum/rules-questions/76933-cock-robin-jack-of-both-sides#90064) [ANK 20220704](https://www.vekn.net/forum/rules-questions/79890-charming-lobby-a-political-action-card-krc?start=0#105616) [LSJ 20100819](https://groups.google.com/g/rec.games.trading-cards.jyhad/c/x_u1Qtiguzg/m/FZjjjIQu-FoJ) — {Jack of Both Sides}, {Muricia's Call}, {The Summoning}, {Charming Lobby}.
[^1-6-15]: [ANK 20190228](https://www.vekn.net/forum/rules-questions/77427-mata-hari-and-hakim-s-law-leadership?start=42#93785) [RTR 20070707](https://groups.google.com/g/rec.games.trading-cards.jyhad/c/vSOt2c1uRzQ/m/MsRAv47Cd4YJ) [LSJ 20070708](https://groups.google.com/g/rec.games.trading-cards.jyhad/c/vSOt2c1uRzQ/m/F4ZIvIyp7lcJ) [LSJ 20101013](https://groups.google.com/g/rec.games.trading-cards.jyhad/c/hpFRDAmtSbA/m/httYmI5wpB8J) [ANK 20201028](https://www.vekn.net/forum/rules-questions/78885-vlad-tepes-and-archon#100998) [LSJ 20091015](https://groups.google.com/g/rec.games.trading-cards.jyhad/c/pqa7mYZ6NEM/m/HhxAS7Rh3JwJ) [PIB 20130128](https://www.vekn.net/forum/rules-questions/43572-can-i-put-infernal-pact-on-vidal-jarbeaux?start=36#44503) — {Mata Hari}, {Vidal Jarbeaux}, {Gem Ghastly}, {Kemintiri}, {Lisandro Giovanni}, {Petaniqua}, {Philip van Vermeer IV}, {Tatiana Stepanova, Alastor}, {Victor Gerard}, {Vlad Tepes}, {Winterlich}.
[^1-6-16]: [LSJ 20050119](https://groups.google.com/g/rec.games.trading-cards.jyhad/c/NKWhBnp7uP4/m/6_56LlSV658J) — {Mata Hari}, {Vidal Jarbeaux}, {Gem Ghastly}, {Lisandro Giovanni}, {Petaniqua}, {Philip van Vermeer IV}, {Tatiana Stepanova, Alastor}, {Vlad Tepes}, {Winterlich}, {Abraham Mellon}, {Lady Scarlett Churchill}.
[^1-6-17]: [LSJ 20100526](https://groups.google.com/g/rec.games.trading-cards.jyhad/c/ch0oKrlxX30/m/MiuMxqszAUgJ) [ANK 20220718](https://www.vekn.net/forum/rules-questions/79913-mata-hari-and-infamous-insurgent#105762) [LSJ 20050721](https://groups.google.com/g/rec.games.trading-cards.jyhad/c/g39H3dwXqvc/m/R0kKrr7JDasJ) [PIB 20150306](https://www.vekn.net/forum/rules-questions/69627-vlad-tepes-regent?start=12#69696) — {Sacrifice}, {Infamous Insurgent}, {Kemintiri}, {Vlad Tepes}.
[^1-6-18]: [PIB 20150530](https://www.vekn.net/forum/rules-questions/66061-houngan-on-lisandro?start=6#71415) [LSJ 20070708](https://groups.google.com/g/rec.games.trading-cards.jyhad/c/vSOt2c1uRzQ/m/F4ZIvIyp7lcJ) [LSJ 20071109](https://groups.google.com/g/rec.games.trading-cards.jyhad/c/mXspOwNnPDc/m/UJAVuSqFBNoJ) — {Lisandro Giovanni}, {Vidal Jarbeaux}, {Mata Hari}.
[^1-6-25]: [LSJ 20050225](https://groups.google.com/g/rec.games.trading-cards.jyhad/c/OjszbddbvxM/m/eKkxVIJPoG4J) — {Mata Hari}, {Lisandro Giovanni}, {Petaniqua}, {Vidal Jarbeaux}, {Winterlich}.
[^1-6-20]: [LSJ 20090508](https://groups.google.com/g/rec.games.trading-cards.jyhad/c/B7dz3qoIITQ/m/0YV5PNQvijsJ) [LSJ 20011217](https://groups.google.com/g/rec.games.trading-cards.jyhad/c/vZ13bh7FEvQ/m/KaZlbqc4LO0J) [ANK 20180731-1](https://www.vekn.net/forum/rules-questions/76877-vivienne-geroux-and-anarh-cards#89482) [LSJ 20031116](https://groups.google.com/g/rec.games.trading-cards.jyhad/c/RQBw8EnnD5s/m/NpdTwIuChy8J) [ANK 20230816-2](https://www.vekn.net/forum/rules-questions/80683-inscription-and-hunger-of-marduk?start=12#109056) — {Inceptor}, {Infernal Familiar}, {Ian Forestal}, {Grey Thorne}, {Inscription}.
[^1-6-21]: [RTR 20010711](https://groups.google.com/g/rec.games.trading-cards.jyhad/c/GsI1UyH54jU/m/x9LfDZX1vR4J) [LSJ 20021211](https://groups.google.com/g/rec.games.trading-cards.jyhad/c/-J07wvmidOA/m/gPQ5ngEZ6HcJ) [PIB 20110725](https://www.vekn.net/forum/rules-questions/6728-announcing-siphon#6740) [RTR 20010710](https://groups.google.com/g/rec.games.trading-cards.jyhad/c/GsI1UyH54jU/m/x9LfDZX1vR4J) — {Absorb the Mind}, {Call the Lamprey}, {Draba}, {Night Terrors}, {Siphon}, {Kindred Segregation}, {Peace Treaty}.
[^1-6-22]: [RTR 19980928](https://groups.google.com/g/rec.games.trading-cards.jyhad/c/Xva4_IRavxM/m/F-_fjzTmo88J) [RTR 19951110](https://groups.google.com/g/rec.games.trading-cards.jyhad/c/TXfganI5B2o/m/QYh3AdPNbUwJ) [ANK 20200420-3](https://www.vekn.net/forum/rules-questions/78574-vulture-s-buffet#99642) [LSJ 20100527](https://groups.google.com/g/rec.games.trading-cards.jyhad/c/Tr3X4DsZr-8/m/O06iXN6LtzsJ) [LSJ 20070901](https://groups.google.com/g/rec.games.trading-cards.jyhad/c/EouVnC0MuH4/m/_b3gw2Hqxb8J) [LSJ 20060623](https://groups.google.com/g/rec.games.trading-cards.jyhad/c/mfgW0TeoLNM/m/e_QgbzZCqa8J) [LSJ 20010810](https://groups.google.com/g/rec.games.trading-cards.jyhad/c/FUXkrq3B_O8/m/pimj1Vvw7WIJ) [PIB 20121028](https://www.vekn.net/forum/rules-questions/39816-ec-2012-can-you-answer-these?start=6#39843) — {Shattering Blow}, {Fractured Armament}, {Canine Horde}, {Blessing of Durga Syn}, {Brujah Frenzy}, {Vulture's Buffet}, {Storage Annex}, {Liquidation}, {Undue Influence}, {Free States Rant}, {Taste of Vitae}.
[^1-6-23]: [LSJ 20001114](https://groups.google.com/g/rec.games.trading-cards.jyhad/c/qXSlM7Grq1c/m/cSDoQ9mw0z4J) [LSJ 20030121](https://groups.google.com/g/rec.games.trading-cards.jyhad/c/lED3kZ2UUUo/m/8TgrW3RxQ9QJ) [TOM 19951109](https://groups.google.com/g/rec.games.trading-cards.jyhad/c/WhJj5K1Fa-0/m/m673ruvTozEJ) [LSJ 20010315](https://groups.google.com/g/rec.games.trading-cards.jyhad/c/m9CrEOn1veo/m/gmx_Nou4BTQJ) [LSJ 20100527](https://groups.google.com/g/rec.games.trading-cards.jyhad/c/Tr3X4DsZr-8/m/O06iXN6LtzsJ) — group "Immideate damage prevention" (G00154), {Hidden Strength}, {Apparition}, {Brother's Blood}, {Bonding}.
[^1-6-24]: [LSJ 20011214-2](https://groups.google.com/g/rec.games.trading-cards.jyhad/c/TinQ8ywzIHU/m/-zW_hcYbiD4J) — {Repulsion}.
[^1-7-1]: [LSJ 20091021-2](https://groups.google.com/g/rec.games.trading-cards.jyhad/c/x5oG5J7Egtg/m/yafJrZAoqjgJ) [LSJ 20080201](https://groups.google.com/g/rec.games.trading-cards.jyhad/c/y5Uoc7nEulU/m/Nbp6ZMfhj1wJ) [ANK 20200703-2](https://www.vekn.net/forum/rules-questions/78713-blood-of-water-timing-before-strike-resolution#100242) — {Nergal}, {Yawp Court}, {Preternatural Evasion}.
[^1-7-2]: [ANK 20210124](https://www.vekn.net/forum/rules-questions/79001-the-question-of-the-month-action-fizzles#101492) [LSJ 20070411](https://groups.google.com/g/rec.games.trading-cards.jyhad/c/umdINigMKqs/m/l6GFRVKdkMsJ) [LSJ 20090514](https://groups.google.com/g/rec.games.trading-cards.jyhad/c/PKQ6lQUBUOI/m/Zra43F1WXGcJ) — groups "Action targeting locked minion" (G00078), "Action targeting vampire in torpor" (G00080) and "Action targeting unlocked minion" (G00081).
[^1-7-3]: [ANK 20190625](https://www.vekn.net/forum/rules-questions/77741-slow-witheringand-paying-superior-action-card#95611) [PIB 20121031](https://www.vekn.net/forum/rules-questions/39816-ec-2012-can-you-answer-these?start=18#39908) [LSJ 20090208](https://groups.google.com/g/rec.games.trading-cards.jyhad/c/07gUFmSeIxU/m/yIrwcMsATB4J) [LSJ 20040730](https://groups.google.com/g/rec.games.trading-cards.jyhad/c/vCZw1_QnhfE/m/6dxskyrN040J) [ANK 20230527](https://www.vekn.net/forum/rules-questions/80553-blithe-acceptance-and-multiple-combat#108178) — {The Slow Withering}, {Tryphosa}, {Enrage}, {Aura of Invincibility}, {Blithe Acceptance}.
[^1-7-4]: [LSJ 19990421](https://groups.google.com/g/rec.games.trading-cards.jyhad/c/bYwaXWdJX84/m/qajsOL_I_LoJ) [LSJ 20070417](https://groups.google.com/g/rec.games.trading-cards.jyhad/c/ecDUqbSUsNg/m/3W9aOm0MfYEJ) [LSJ 20031121-2](https://groups.google.com/g/rec.games.trading-cards.jyhad/c/1khXmKPU0ws/m/Je_X4gvv72kJ) — {Forced Awakening}, group "Burn blood to attempt to block" (G00088).
[^1-7-5]: [LSJ 20020620](https://groups.google.com/g/rec.games.trading-cards.jyhad/c/WoXWzLYaFSY/m/ug3CHnpMCUQJ) [LSJ 20080512](https://groups.google.com/g/rec.games.trading-cards.jyhad/c/z2DGSFph6sM/m/IjJB89nbtlsJ) [LSJ 20050607](https://groups.google.com/g/rec.games.trading-cards.jyhad/c/WLv9R8wA0Ow/m/gQyOMb3fEKQJ) [LSJ 20050608](https://groups.google.com/g/rec.games.trading-cards.jyhad/c/WLv9R8wA0Ow/m/dyAPpxSMoSYJ) [RTR 20010710](https://groups.google.com/g/rec.games.trading-cards.jyhad/c/GsI1UyH54jU/m/x9LfDZX1vR4J) [RTR 19941109](https://groups.google.com/d/msg/rec.games.deckmaster/_6CXoKTSLnw/FdG67-3HEAQJ) — {Minion Tap}, {Villein}, group "Allies who can play as a vampire" (G00011), {Spying Mission}, {Thanks for the Donation}, {Repo Man}.
[^1-7-6]: [RTR 20070707](https://groups.google.com/g/rec.games.trading-cards.jyhad/c/vSOt2c1uRzQ/m/MsRAv47Cd4YJ) [PIB 20150917](https://www.vekn.net/forum/rules-questions/73156-corner-case-thin-blooded-seer-question#73166) — {The Ankara Citadel, Turkey}, {Thin-Blooded Seer}.
[^1-7-7]: [RTR 19941109](https://groups.google.com/d/msg/rec.games.deckmaster/_6CXoKTSLnw/FdG67-3HEAQJ) [PIB 20150725](https://www.vekn.net/forum/rules-questions/72184-cavalier#72185) [LSJ 20100429](https://groups.google.com/g/rec.games.trading-cards.jyhad/c/OUcf-1EMXXA/m/DOGZdKnJ1zgJ) [ANK 20170716](https://www.vekn.net/forum/rules-questions/75987-question-about-khobar-towers-al-khubar#82606) [RTR 20020501](https://groups.google.com/g/rec.games.trading-cards.jyhad/c/M1snoR2msbQ/m/RFwCmX3anDkJ) — {Black Cat}, {Ivan Krenyenko}, {Cavalier}, {Khobar Towers, Al-Khubar}.
[^1-7-8]: [LSJ 20040701](https://groups.google.com/g/rec.games.trading-cards.jyhad/c/O7cT51Yl2Uk/m/RvMWaiqAFS8J) [LSJ 20080125](https://groups.google.com/g/rec.games.trading-cards.jyhad/c/HcCobkGPcFI/m/GlBdNwMvAjwJ) [ANK 20181216](https://www.vekn.net/forum/rules-questions/77213-discussion-card-costs-and-presentation?start=36#92386) [RTR 19960112](https://groups.google.com/g/rec.games.trading-cards.jyhad/c/d3n3StNS7no/m/k2NmZFUl9fAJ) [LSJ 20050408](https://groups.google.com/g/rec.games.trading-cards.jyhad/c/idZy8QCxBT0/m/ymQE3s1kEkoJ) [RTR 20111202](https://www.vekn.net/forum/rules-questions/16769-rules-team-rulings-02-dec-11#16769) [ANK 20180109](https://www.vekn.net/forum/rules-questions/76360-ravnos-carnival#84826) — {Concealed Weapon}, {Ravnos Cache}, {Ravnos Carnival}.
[^1-7-9]: [ANK 20200709](https://www.vekn.net/forum/rules-questions/74710-jenna-cross-salvador-garcia-specials-question#100325) — {Jenna Cross}.
[^1-7-10]: [ANK 20210714-2](https://www.vekn.net/forum/rules-questions/79217-clarification-needed-on-eternals-of-sirius-rulings?start=6#102696) [ANK 20210714](https://www.vekn.net/forum/rules-questions/79224-can-i-do-a-3rd-villein-in-a-vampire-if-i-have-only-1-pool-remaining#102697) [ANK 20230621](https://www.vekn.net/forum/rules-questions/80691-procurer-recruiting-another-with-the-shard?start=12#108765) — {The Eternals of Sirius}, {Villein}, {Powerbase: Tshwane}, {The Shard, London}.
[^1-7-11]: [LSJ 20030502](https://groups.google.com/g/rec.games.trading-cards.jyhad/c/qBa9CvBwqNA/m/ZuBgMjNgb6EJ) [LSJ 19970224](https://groups.google.com/g/rec.games.trading-cards.jyhad/c/80KRDjVFkyg/m/TBJso9Ra_9QJ) [LSJ 20071015](https://groups.google.com/g/rec.games.trading-cards.jyhad/c/Bom6ae7qjbI/m/1ov2qqChTdMJ) [LSJ 20100302-1](https://groups.google.com/g/rec.games.trading-cards.jyhad/c/jmmm0WRUPvs/m/ny5F1OnSUsEJ) [PIB 20111101](https://www.vekn.net/forum/rules-questions/12975-summon-history-reanimated-corpse#13169) [ANK 20220704](https://www.vekn.net/forum/rules-questions/79890-charming-lobby-a-political-action-card-krc?start=0#105616) — group "Cost X" (G00032), {Hidden Strength}, {Compel the Spirit}, {Pressing Flesh}, {Summon History}, {Charming Lobby}.
[^1-7-12]: [ANK 20230620](https://www.vekn.net/forum/rules-questions/80612-when-to-use-shard-the-line-when-action-becoems-to-expensive-after-announcement#108409) [ANK 20170605](https://www.vekn.net/forum/rules-questions/75862-timing-of-the-line#82113) [LSJ 20090705](https://groups.google.com/g/rec.games.trading-cards.jyhad/c/3Ekxk6uQ_wo/m/Y25g9tS6qSoJ) [LSJ 20030917](https://groups.google.com/g/rec.games.trading-cards.jyhad/c/i3Ugq5AQWFI/m/TxPoXM78hFAJ) — group "Lock to reduce cost" (G00130), {Powerbase: Tshwane}, {The Line}, {The Shard, London}, {Eccentric Billionaire}, {Sunset Strip, Hollywood}.
[^1-7-13]: [RTR 20070707](https://groups.google.com/g/rec.games.trading-cards.jyhad/c/vSOt2c1uRzQ/m/MsRAv47Cd4YJ) [ANK 20230824](https://www.vekn.net/forum/news-and-announcements/80782-the-line-pack-alpha?start=6#109157) [ANK 20210928](https://www.vekn.net/forum/rules-questions/79364-combo-piper-x-soul-of-earth#103363) [LSJ 20090115-1](https://groups.google.com/g/rec.games.trading-cards.jyhad/c/RQ3ARP9Kvfk/m/dBN_M7SnIHAJ) [ANK 20170309](https://www.vekn.net/forum/rules-questions/75649-reduce-ally-cost-and-piper-combo#81049) [LSJ 20090920-2](https://groups.google.com/g/rec.games.trading-cards.jyhad/c/nbgHtblc8jc/m/vdxPu5hPxGIJ) — {Powerbase: Tshwane}, {Pack Alpha}, {Soul of the Earth}, {Piper}, {Antonio d'Erlette}.
[^1-7-14]: [ANK 20221102](https://www.vekn.net/forum/rules-questions/80129-fall-of-london-card-rules-questions#106688) [LSJ 20081124-1](https://groups.google.com/g/rec.games.trading-cards.jyhad/c/Fp4wSGFJ7N4/m/GQlX8JKdT04J) [TOM 19951208-1](https://groups.google.com/g/rec.games.trading-cards.jyhad/c/tEHebi9BYfc/m/Q2zsWUbTURUJ) [ANK 20181007](https://www.vekn.net/forum/rules-questions/77057-quick-question-on-the-line#91020) [RTR 19950509](https://groups.google.com/g/rec.games.trading-cards.jyhad/c/_LKyR7pdMig/m/ZvwdGmIwUnsJ) [ANK 20230621](https://www.vekn.net/forum/rules-questions/80691-procurer-recruiting-another-with-the-shard?start=12#108765) — {Powerbase: Tshwane}, {The Shard, London}, {Walks-With-Might}, {Secure Haven}, {The Line}, {Democritus}.
[^1-7-15]: [LSJ 20080114](https://groups.google.com/g/rec.games.trading-cards.jyhad/c/aMum-K7LEeo/m/94iN92zwYTcJ) [LSJ 20080107](https://groups.google.com/g/rec.games.trading-cards.jyhad/c/XpZ6F53jK-c/m/wB6HHGzgFi4J) [LSJ 20080109](https://groups.google.com/g/rec.games.trading-cards.jyhad/c/XpZ6F53jK-c/m/EQWCLO72MbsJ) [ANK 20221026](https://www.vekn.net/forum/rules-questions/80117-the-british-museum-london#106651) — group "Locquipments" (G00047), {Therbold Realty}, {Marie Faucigny}, {Regina Blake}, {The British Museum, London}.
[^1-7-16]: [ANK 20210226](https://www.vekn.net/forum/rules-questions/79045-paths-and-burn-blood-requrement?start=18#101726) [ANK 20180327](https://www.vekn.net/forum/rules-questions/76480-enrage-and-burning-blood#86056) — groups "Burn blood for effect" (G00065) and "Burn blood for effect (mandatory)" (G00097), {Preternatural Evasion}, {Shadow Boxing}, {Aura Absorption}, {Enrage}.
[^1-7-17]: [LSJ 20090107](https://groups.google.com/g/rec.games.trading-cards.jyhad/c/qPDLvbgqfCg/m/DlRVFoE_C64J) [LSJ 20070829-3](https://groups.google.com/g/rec.games.trading-cards.jyhad/c/sVXZw1J43ik/m/J018OOhbEoQJ) [ANK 20220809](https://www.vekn.net/forum/rules-questions/79949-loki-s-gift-hunt-bonus#105914) — {Dragos}, {Loki's Gift}.
[^1-7-18]: [LSJ 20070829-1](https://groups.google.com/g/rec.games.trading-cards.jyhad/c/sVXZw1J43ik/m/OByFPgQsynwJ) [ANK 20191221](https://www.vekn.net/forum/rules-questions/76990-correct-order-impulse-for-combat-cards-after-combat#90516) — {Terror Frenzy}.
[^1-7-19]: [LSJ 20100216](https://groups.google.com/g/rec.games.trading-cards.jyhad/c/nrXTh1XKJJ8/m/KF7iiXQk3jsJ) [ANK 20180512-2](https://www.vekn.net/forum/rules-questions/76595-rules-team-rulings-rtr-11-05-2018?start=24#86823) [RTR 20010711](https://groups.google.com/g/rec.games.trading-cards.jyhad/c/GsI1UyH54jU/m/x9LfDZX1vR4J) — {Villein}, {Minion Tap}, {Theft of Vitae}, {Tongue of the Serpent}, {Succubus}.
[^1-7-20]: [LSJ 20090901](https://groups.google.com/g/rec.games.trading-cards.jyhad/c/9BZPgQH9PFk/m/ulMGheX3NTIJ) [LSJ 20030522-2](https://groups.google.com/g/rec.games.trading-cards.jyhad/c/iBfBo7CQn4Q/m/-0EK5GbgRZUJ) [LSJ 20031219](https://groups.google.com/g/rec.games.trading-cards.jyhad/c/leLLrcPsiBY/m/cnSR-CQGqdMJ) [LSJ 20100527](https://groups.google.com/g/rec.games.trading-cards.jyhad/c/Tr3X4DsZr-8/m/O06iXN6LtzsJ) — {Sword of Nuln}.
[^1-7-21]: [LSJ 19970707](https://groups.google.com/g/rec.games.trading-cards.jyhad/c/KWekwiRSa2I/m/9pS17rzBBDYJ) [ANK 20230226](https://www.vekn.net/forum/rules-questions/31040-unleash-hells-fury-vs-burn-x-blood-to-attempt-to-block?start=6#107484) [LSJ 20031121-2](https://groups.google.com/g/rec.games.trading-cards.jyhad/c/1khXmKPU0ws/m/Je_X4gvv72kJ) — {Camarilla Exemplary}, {Unleash Hell's Fury}, group "Burn blood to attempt to block" (G00088).
[^1-7-22]: [LSJ 19971212](https://groups.google.com/g/rec.games.trading-cards.jyhad/c/jQUqciN0Z9E/m/KkmcboJgjl8J) [ANK 20181006](https://www.vekn.net/forum/rules-questions/77053-smiling-jack#91000) — {Smiling Jack, The Anarch}.
[^1-7-23]: [LSJ 20100725](https://groups.google.com/g/rec.games.trading-cards.jyhad/c/9d1zMZfsfNo/m/l3fbDtbr9xwJ) [LSJ 20091021](https://groups.google.com/g/rec.games.trading-cards.jyhad/c/B_MVmqTcUXE/m/0-IIMaTSfq0J) [TOM 19951212-1](https://groups.google.com/g/rec.games.trading-cards.jyhad/c/NJa6LfMSPks/m/0CQKgKoeWgUJ) [LSJ 20080702-4](https://groups.google.com/g/rec.games.trading-cards.jyhad/c/sCHpPQkjeAE/m/9GGAf6TbiP0J) [ANK 20180509](https://www.vekn.net/forum/rules-questions/76585-emerald-legionnaire-and-hos-requirement?start=0#86672) — {Muricia's Call}, {Charming Lobby}, {Horrid Reality}, {Topaz}, {Emerald Legionnaire}.
[^1-7-24]: [LSJ 20040518](https://groups.google.com/g/rec.games.trading-cards.jyhad/c/4emymfUPwAM/m/B2SCC7L6kuMJ) [LSJ 20100315](https://groups.google.com/g/rec.games.trading-cards.jyhad/c/06C5ufFEaJs/m/LClmjWq7DRYJ) — {Alastor}, {Cavalier}.
[^1-7-25]: [LSJ 20060831](https://groups.google.com/g/rec.games.trading-cards.jyhad/c/wdVbwFZo8Jg/m/U8P1de7moZ0J) [LSJ 20071015-2](https://groups.google.com/g/rec.games.trading-cards.jyhad/c/Ei307R78l4A/m/sZzwphkIbH4J) [ANK 20220503](https://www.vekn.net/forum/rules-questions/39040-re-ex-nihilo-can-i-choose-to-burn-my-minion#105161) — {Lord Aaron Wesley Wilkshire}, {Watenda}, {Ex Nihilo}.
[^1-7-26]: [ANK 20181017](https://www.vekn.net/forum/rules-questions/77086-question-recure-of-the-homeland-cost#91228) — {Go Anarch}, {Healing Touch}.
[^1-7-27]: [ANK 20180805](https://www.vekn.net/forum/rules-questions/76897-a-question-on-function-of-safe-passage#89666) [ANK 20221120](https://www.vekn.net/forum/rules-questions/80172-secure-haven-and-cards-with-targeted-effects-that-are-already-in-play#106845) — {Safe Passage}, {Secure Haven}.
[^1-7-28]: [PIB 20121031](https://www.vekn.net/forum/rules-questions/39816-ec-2012-can-you-answer-these?start=18#39908) [LSJ 20090601-2](https://groups.google.com/g/rec.games.trading-cards.jyhad/c/RkEUabeJNdM/m/JEGebBucNfEJ) [LSJ 20040518](https://groups.google.com/g/rec.games.trading-cards.jyhad/c/4emymfUPwAM/m/B2SCC7L6kuMJ) [LSJ 20040518-2](https://groups.google.com/g/rec.games.trading-cards.jyhad/c/4emymfUPwAM/m/JF_o7OOoCbkJ) [LSJ 20081213-1](https://groups.google.com/g/rec.games.trading-cards.jyhad/c/MNmJu12AU8I/m/Pol1P9fWMmoJ) [ANK 20210124](https://www.vekn.net/forum/rules-questions/79001-the-question-of-the-month-action-fizzles#101492) — {Target Head}, {Santaleous}, {The Diamond Thunderbolt}, {Enkil Cog}.
[^1-7-29]: [RTR 20010710](https://groups.google.com/g/rec.games.trading-cards.jyhad/c/GsI1UyH54jU/m/x9LfDZX1vR4J) [ANK 20190724](https://www.vekn.net/forum/rules-questions/77810-a-monthly-doubts-for-rookie#95945) [LSJ 20060409](https://groups.google.com/g/rec.games.trading-cards.jyhad/c/gsFQXsCGTG4/m/q5H8FvuKksIJ) [ANK 20220528](https://www.vekn.net/forum/rules-questions/76455-keystone-kine-and-imbued?start=18#105328) — {Kindred Segregation}, {Peace Treaty}, {Keystone Kine}.
[^1-8-1]: [LSJ 20061207](https://groups.google.com/g/rec.games.trading-cards.jyhad/c/nqcrJlhg4Ng/m/qQu7p-LLhfAJ) [LSJ 20061013](https://groups.google.com/g/rec.games.trading-cards.jyhad/c/6w8K3yDtBH0/m/M_SZH9Id8n8J) [RTR 20040501](https://groups.google.com/g/rec.games.trading-cards.jyhad/c/7-mp3Ada86I/m/yenQ7FZ-VMIJ) [RBK playing-a-card](https://www.vekn.net/rulebook#playing-a-card) — group "Cancel" (G00058), {The Admonitions}, {The Barrens}, {Dreams of the Sphinx}, {The Erciyes Fragments}, {Fragment of the Book of Nod}. 
[^1-8-2]: [LSJ 20021011](https://groups.google.com/g/rec.games.trading-cards.jyhad/c/9WWIzxek9Nc/m/PlIwI11sNpkJ) [ANK 20231028](https://www.vekn.net/forum/rules-questions/80925-wake-timing-effects#109683) — group "Cancel as a reaction" (G00062), {Deed the Heart's Desire}, {Psalm of the Damned}. 
[^1-8-3]: [LSJ 20100728](https://groups.google.com/g/rec.games.trading-cards.jyhad/c/mzzPS-cOprI/m/BRBR4OBUOaQJ) [LSJ 20090213](https://groups.google.com/g/rec.games.trading-cards.jyhad/c/hkTPcLPgZk4/m/WPZLiL2A91sJ) — {Andrew Stuart}. 
[^1-8-4]: [LSJ 20031201](https://groups.google.com/g/rec.games.trading-cards.jyhad/c/Mi_j7sUsZZw/m/ScJPKbfiCAgJ) [LSJ 20070214](https://groups.google.com/g/rec.games.trading-cards.jyhad/c/o_BltcAJ_So/m/r_uEap9msOYJ) [ANK 20180910-2](https://www.vekn.net/forum/rules-questions/76990-correct-order-impulse-for-combat-cards-after-combat?start=6#90521) [ANK 20191221](https://www.vekn.net/forum/rules-questions/76990-correct-order-impulse-for-combat-cards-after-combat#90516) [ANK 20180909](https://www.vekn.net/forum/rules-questions/76987-ophidian-gaze-and-post-referendum-action-modifiers#90501) [PIB 20120808](https://www.vekn.net/forum/rules-questions/34265-rules-tweak-suggestion-rewind-time-et-al?start=12#34448) [LSJ 20080618](https://groups.google.com/g/rec.games.trading-cards.jyhad/c/9FAkwIsuYZc/m/gCoYa59TEGIJ) — {Vox Senis}, {Botched Move}, {Death Seeker}, {Ophidian Gaze}, group "Cancel with no action" (G00063). 
[^1-8-5]: [PIB 20130704](https://www.vekn.net/forum/rules-questions/50982-iron-heart-vs-virtuosa#50984) — {Hide the Mind}, {Iron Heart}. 
[^1-8-6]: [RTR 20001020](https://groups.google.com/g/rec.games.trading-cards.jyhad/c/GvxNYsYsWJ4/m/EY7NOjdsGCsJ) [ANK 20201229](https://www.vekn.net/forum/rules-questions/78959-louhi-and-piper#101325) [LSJ 20060530-2](https://groups.google.com/g/rec.games.trading-cards.jyhad/c/7ezcZoziFWw/m/G07cu5_UZnQJ) [RTR 20040501](https://groups.google.com/g/rec.games.trading-cards.jyhad/c/7-mp3Ada86I/m/yenQ7FZ-VMIJ) — group "Cancel an action" (G00061), {Sudden Reversal}, {Asguresh}, {Piper}, {The Summoning}, {Zhenga}, {The Erciyes Fragments}. 
[^1-8-7]: [ANK 20180627-1](https://www.vekn.net/forum/rules-questions/76757-inscription-and-mirror-walk#88419) [LSJ 20010716](https://groups.google.com/g/rec.games.trading-cards.jyhad/c/x2EdFtlPs8Q/m/IPCbfV2Qct0J) [ANK 20221011](https://www.vekn.net/forum/rules-questions/80070-thoughts-betrayed-vs-shadow-court-satyr?start=6#106537) — {Inscription}, {Shadow Court Satyr}. 
[^1-8-8]: [ANK 20220704](https://www.vekn.net/forum/rules-questions/79890-charming-lobby-a-political-action-card-krc?start=0#105616) [LSJ 20090113-3](https://groups.google.com/g/rec.games.trading-cards.jyhad/c/8FHCL4AQblI/m/DejFKS9wmXUJ) [LSJ 20100426](https://groups.google.com/g/rec.games.trading-cards.jyhad/c/BN3xmoZ0W1A/m/ui4w2OyGLjAJ) [LSJ 20091128](https://groups.google.com/g/rec.games.trading-cards.jyhad/c/-IxzB0bvhKU/m/ogGuu7J80R4J) [LSJ 20011205](https://groups.google.com/g/rec.games.trading-cards.jyhad/c/dkK2L81_cYk/m/mj0NOMJAGucJ) — {Charming Lobby}, {Echo of Harmonies}. 
[^1-8-9]: [ANK 20190104](https://www.vekn.net/forum/rules-questions/77254-canceling-cards-and-bold-text?start=6#92640) [LSJ 19980212](https://groups.google.com/g/rec.games.trading-cards.jyhad/c/fLFLlXZXHqA/m/ggjw8aGjdRoJ) [ANK 20200525-2](https://www.vekn.net/forum/rules-questions/78653-charismatic-aura#99943) [RBK cancel-a-card](https://www.vekn.net/rulebook#cancel-a-card) — group "Cancel" (G00058), {Immortal Grapple}. 
[^1-8-10]: [ANK 20220411](https://www.vekn.net/forum/rules-questions/79730-dabbler-and-direct-intervention#104995) [LSJ 20000424](https://groups.google.com/g/rec.games.trading-cards.jyhad/c/6pK4rFvqmmg/m/LGEB9PuA4TUJ) [LSJ 20070330](https://groups.google.com/g/rec.games.trading-cards.jyhad/c/gsI3SYz2g3o/m/Fj3x7Kn32HEJ) [ANK 20190701](https://www.vekn.net/forum/rules-questions/77763-multiple-questions#95690) — {Dabbler}, {Infernal Familiar}, {Perfectionist}, {Marthe Dizier}. 
[^1-8-11]: [LSJ 20090601-2](https://groups.google.com/g/rec.games.trading-cards.jyhad/c/RkEUabeJNdM/m/JEGebBucNfEJ) [PIB 20121031](https://www.vekn.net/forum/rules-questions/39816-ec-2012-can-you-answer-these?start=18#39908) [LSJ 20071015-2](https://groups.google.com/g/rec.games.trading-cards.jyhad/c/Ei307R78l4A/m/sZzwphkIbH4J) — {Santaleous}, {Watenda}, the {Target} aim cycle ({Target Hand}, {Target Head}, {Target Leg}, {Target Retainer}, {Target Vitals}). 
[^1-8-12]: [LSJ 20040518](https://groups.google.com/g/rec.games.trading-cards.jyhad/c/4emymfUPwAM/m/B2SCC7L6kuMJ) [LSJ 20040518-2](https://groups.google.com/g/rec.games.trading-cards.jyhad/c/4emymfUPwAM/m/JF_o7OOoCbkJ) [LSJ 20070222-2](https://groups.google.com/g/rec.games.trading-cards.jyhad/c/jBrfK77gayo/m/X4wqXnwhzDoJ) — {The Diamond Thunderbolt}. 
[^1-8-13]: [LSJ 20080630](https://groups.google.com/g/rec.games.trading-cards.jyhad/c/nvuXBpEaKAA/m/ymiC3yAQVOwJ) [LSJ 20011023](https://groups.google.com/g/rec.games.trading-cards.jyhad/c/2GOLIrXAF8M/m/P4T3Dj6UNL0J) [LSJ 20021022](https://groups.google.com/g/rec.games.trading-cards.jyhad/c/WIXqYpkKuj8/m/lDWFfFjwn8YJ) — group "Cancel" (G00058), {The Diamond Thunderbolt}, {React with Conviction}, {Asguresh}, {Infernal Pursuit}. 
[^1-8-14]: [LSJ 20030224](https://groups.google.com/g/rec.games.trading-cards.jyhad/c/67261v339Ds/m/um8V7VVp2Y4J) [LSJ 20100206](https://groups.google.com/g/rec.games.trading-cards.jyhad/c/cAGrXqpO-YQ/m/GJHdeYt0GdUJ) [LSJ 20090126](https://groups.google.com/g/rec.games.trading-cards.jyhad/c/3Cd-DNfT7yQ/m/-BfYOkP1OUUJ) [ANK 20170124](https://www.vekn.net/forum/rules-questions/75556-vessel-wash-and-mpa#80362) [RBK trifle](https://www.vekn.net/rulebook#trifle) — group "Cancel" (G00058), {Asguresh}, {Sudden Reversal}, {Wash}. 
[^1-8-15]: [RTR 20040501](https://groups.google.com/g/rec.games.trading-cards.jyhad/c/7-mp3Ada86I/m/yenQ7FZ-VMIJ) [LSJ 20100206](https://groups.google.com/g/rec.games.trading-cards.jyhad/c/cAGrXqpO-YQ/m/GJHdeYt0GdUJ) [RBK cancel-a-card](https://www.vekn.net/rulebook#cancel-a-card) — {Primal Instincts}, {Death Seeker}, {Asguresh}. 
[^1-8-16]: [LSJ 20050228-3](https://groups.google.com/g/rec.games.trading-cards.jyhad/c/UHEZEmX22jA/m/u0IldHuItjgJ) [ANK 20230111](https://www.vekn.net/forum/rules-questions/80258-rigor-mortis-and-aid-from-bats-and-other-manuver-strike-cards#107179) [ANK 20230114](https://www.vekn.net/forum/rules-questions/80258-rigor-mortis-and-aid-from-bats-and-other-manuver-strike-cards?start=6#107195) — {Rigor Mortis}. 
[^1-8-17]: [ANK 20200311](https://www.vekn.net/forum/rules-questions/78506-target-retainer-cancelled#99256) — {Target Retainer}. 
[^1-8-18]: [LSJ 20060425](https://groups.google.com/g/rec.games.trading-cards.jyhad/c/U34QDob4Vco/m/hcaMIn9W88kJ) [ANK 20200813-2](https://www.vekn.net/forum/rules-questions/78799-rewind-time-inf-and-action-cards#100526) [LSJ 20090323](https://groups.google.com/g/rec.games.trading-cards.jyhad/c/bG4PSmditm4/m/wR15DaRI8KUJ) [ANK 20210124](https://www.vekn.net/forum/rules-questions/79001-the-question-of-the-month-action-fizzles#101492) — {React with Conviction}, {Veil of Darkness}, {Veil the Legions}. 
[^1-8-19]: [RTR 20010711](https://groups.google.com/g/rec.games.trading-cards.jyhad/c/GsI1UyH54jU/m/x9LfDZX1vR4J) [LSJ 20021211](https://groups.google.com/g/rec.games.trading-cards.jyhad/c/-J07wvmidOA/m/gPQ5ngEZ6HcJ) [PIB 20110725](https://www.vekn.net/forum/rules-questions/6728-announcing-siphon#6740) [LSJ 20070411](https://groups.google.com/g/rec.games.trading-cards.jyhad/c/umdINigMKqs/m/l6GFRVKdkMsJ) — {Absorb the Mind}, {Call the Lamprey}, {Draba}, {Night Terrors}, {Siphon}. 
[^1-8-20]: [LSJ 20091021-2](https://groups.google.com/g/rec.games.trading-cards.jyhad/c/x5oG5J7Egtg/m/yafJrZAoqjgJ) [ANK 20200710](https://www.vekn.net/forum/rules-questions/77985-vidal-jarbeaux-ability#100333) — {Nergal}, {Vidal Jarbeaux}.
[^1-9-1]: [ANK 20181208](https://www.vekn.net/forum/rules-questions/77210-touch-of-clarity-and-fast-reaction-is-posible-to-play-with-locked-minion?start=6#92308) — group "Modifier as announced" (G00052), {Approximation of Loyalty}, {Predator's Transformation}, {Force of Personality}.
[^1-9-2]: [RTR 19991001](https://groups.google.com/g/rec.games.trading-cards.jyhad/c/RAvWWmYoX3U/m/lb2bLOvJDhoJ) [LSJ 20101210](https://groups.google.com/g/rec.games.trading-cards.jyhad/c/QTAA0y6cANI/m/gU0hztzp8mUJ) [PIB 20150428](https://www.vekn.net/forum/rules-questions/70714-card-replacement?start=6#70747) [LSJ 20100206-2](https://groups.google.com/g/rec.games.trading-cards.jyhad/c/reXyybyIYX8/m/jeCyjdiZ5T4J) — {Charming Lobby}, {Jack of Both Sides}, {Blessing of the Beast}, {Gift of Proteus}.
[^1-9-3]: [LSJ 19981005](https://groups.google.com/g/rec.games.trading-cards.jyhad/c/9vOWIR4P_4o/m/UkztBlUMR_QJ) [ANK 20230404](https://www.vekn.net/forum/rules-questions/80431-ruxandra-and-discarding#107788) [LSJ 20090618](https://groups.google.com/g/rec.games.trading-cards.jyhad/c/jxTaf6lnYb0/m/KoQF6jLw5zAJ) [LSJ 20060215](https://groups.google.com/g/rec.games.trading-cards.jyhad/c/BhecJx5BqtQ/m/nqEdwFmnQnwJ) [ANK 20180925-1](https://www.vekn.net/forum/rules-questions/77029-order-of-draw-and-replace-for-concealed-weapon-under-infernal-pursuit?start=6#90750) [LSJ 20100506](https://groups.google.com/g/rec.games.trading-cards.jyhad/c/H6Jm74N0v7k/m/zPi11g24bBUJ) — {Angelica, The Canonicus}, {Ruxandra}, {Constant Revolution}, {Call the Wild Hunt}, {Infernal Pursuit}.
[^1-9-4]: [LSJ 20001120](https://groups.google.com/g/rec.games.trading-cards.jyhad/c/Br8FPS5mRn4/m/2tbPhQquS7gJ) — group "Action not replaced" (G00020), {Steely Tenacity}.
[^1-9-5]: [ANK 20200129](https://www.vekn.net/forum/rules-questions/78701-replace-during-unlock-and-other-unlock-effects#100210) [LSJ 20091208](https://groups.google.com/g/rec.games.trading-cards.jyhad/c/ptHbJM9MlVI/m/O61W2JkI_rIJ) [RTR 19951017](https://groups.google.com/g/rec.games.trading-cards.jyhad/c/ouhNUbHYg50/m/rco157ZHyqEJ) [LSJ 20100527](https://groups.google.com/g/rec.games.trading-cards.jyhad/c/Tr3X4DsZr-8/m/O06iXN6LtzsJ) [LSJ 20001122](https://groups.google.com/g/rec.games.trading-cards.jyhad/c/Br8FPS5mRn4/m/EUCAQhATZC8J) [LSJ 20080805](https://groups.google.com/g/rec.games.trading-cards.jyhad/c/SIbzFAwWDKs/m/BDkEg19txtoJ) — group "Replace next turn" (G00025), group "Permanent not replaced" (G00008), {Port Authority}, {The New Inquisition}, {Psyche!}.
[^1-9-6]: [LSJ 20070320-1](https://groups.google.com/g/rec.games.trading-cards.jyhad/c/goUs4JXcqMw/m/-o_yFpUV-TIJ) [ANK 20200905](https://www.vekn.net/forum/rules-questions/78836-visit-from-the-capuchin-vs-steelytenacity#100698) — {The Meddling of Semsith}, {Hagar Stone}, {Visit from the Capuchin}.
[^1-9-7]: [PIB 20110718](https://www.vekn.net/forum/rules-questions/6435-learjet-question#6436) [LSJ 20020718](https://groups.google.com/g/rec.games.trading-cards.jyhad/c/H0ZTfiyxrbg/m/9zltOm8A5ogJ) [ANK 20180512](https://www.vekn.net/forum/rules-questions/76599-troglodytia-special-vs-wash#86842) — {Learjet}, {Agaitas, The Scholar of Antiquities}, {Troglodytia}.
[^1-9-8]: [LSJ 20080702-2](https://groups.google.com/g/rec.games.trading-cards.jyhad/c/sCHpPQkjeAE/m/8N5_G2gMHAIJ) [ANK 20200517-3](https://www.vekn.net/forum/rules-questions/78606-disguised-baseball-bat#99854) [LSJ 20070707](https://groups.google.com/g/rec.games.trading-cards.jyhad/c/ZtRk5z2TcoI/m/gJWD0dT3kUwJ) — {Baseball Bat}, {Corrupt Construction}.
[^1-9-9]: [LSJ 20011023](https://groups.google.com/g/rec.games.trading-cards.jyhad/c/2GOLIrXAF8M/m/P4T3Dj6UNL0J) [LSJ 20080630](https://groups.google.com/g/rec.games.trading-cards.jyhad/c/nvuXBpEaKAA/m/ymiC3yAQVOwJ) [LSJ 20021022](https://groups.google.com/g/rec.games.trading-cards.jyhad/c/WIXqYpkKuj8/m/lDWFfFjwn8YJ) — group "Cancel" (G00058), {Asguresh}, {Infernal Pursuit}.
[^1-9-10]: [RTR 20000501](https://groups.google.com/g/rec.games.trading-cards.jyhad/c/MKrA0hBXuaU/m/1M5LOLftKWAJ) [LSJ 20070411-2](https://groups.google.com/g/rec.games.trading-cards.jyhad/c/-B6BlRIT0Rg/m/VOYol5mcbO8J) — group "Move or reveal card from crypt" (G00126).
[^1-9-11]: [ANK 20180318](https://www.vekn.net/forum/rules-questions/76464-dnr-counts-against-hand-size-meddling-of-semsith-and-raptor#85841) [ANK 20231229](https://www.vekn.net/forum/rules-questions/81077-do-not-replace-rule-question#110227) [LSJ 20100119](https://groups.google.com/g/rec.games.trading-cards.jyhad/c/1eULCGaVcO0/m/eefMWzjoK0IJ) [PIB 20121031](https://www.vekn.net/forum/rules-questions/39816-ec-2012-can-you-answer-these?start=18#39908) [ANK 20211020](https://www.vekn.net/forum/rules-questions/79416-sergei-voshkov-the-eye#103610) — {Dreams of the Sphinx}, {The Meddling of Semsith}, {Hagar Stone}, {Revelations}, {Sergei Voshkov, The Eye}.
[^1-10-1]: [LSJ 20000113](https://groups.google.com/g/rec.games.trading-cards.jyhad/c/-qvB4bbD-rE/m/0EUdps3thQQJ) [LSJ 20021010](https://groups.google.com/g/rec.games.trading-cards.jyhad/c/IAamJNEJAug/m/iztHSQVIUcYJ) — {Soul Gem of Etrius}, {Abandoning the Flesh}; [LSJ 20090920](https://groups.google.com/g/rec.games.trading-cards.jyhad/c/mCPE3I6343Y/m/KqkCJgjur5IJ) — {Absimiliard's Army}; [ANK 20180408](https://www.vekn.net/forum/rules-questions/76500-charnas-the-imp#86191) — {Charnas the Imp}.
[^1-10-2]: [PIB 20110810](https://www.vekn.net/forum/rules-questions/6809-illusions-of-the-kindred--amaranth?limit=10&start=10#7737) — {Illusions of the Kindred}; [LSJ 20060209](https://groups.google.com/g/rec.games.trading-cards.jyhad/c/ZuOfZorIhhU/m/X5G1JfqDPhcJ) — {Grasp the Ghostly}; [ANK 20170331](https://www.vekn.net/forum/rules-questions/75683-shroudsight-and-summon-soul#81245) — {Summon Soul}; [LSJ 20080314](https://groups.google.com/g/rec.games.trading-cards.jyhad/c/GqHN0I3c8Sc/m/PsOWtyMWjXsJ) — {Wider View}.
[^1-10-3]: [LSJ 20011216-1](https://groups.google.com/g/rec.games.trading-cards.jyhad/c/xwirj771uGM/m/0w1qJBEabFEJ) — {Resurrection}; [LSJ 20010710](https://groups.google.com/g/rec.games.trading-cards.jyhad/c/GsI1UyH54jU/m/x9LfDZX1vR4J) [ANK 20200813](https://www.vekn.net/forum/rules-questions/78798-mummies-and-burning-effects#100529) — group "Shuffle when burned" (G00056); [ANK 20200813](https://www.vekn.net/forum/rules-questions/78798-mummies-and-burning-effects#100529) — {Set's Curse}.
[^1-10-4]: [ANK 20190422](https://www.vekn.net/forum/rules-questions/77571-ilomba-and-set-s-curse#94614) — {Set's Curse}; [LSJ 20100423](https://groups.google.com/g/rec.games.trading-cards.jyhad/c/YnQCu0GeMhc/m/ET__SGvjD7QJ) — {Sacrificial Lamb}; [LSJ 19981006](https://groups.google.com/g/rec.games.trading-cards.jyhad/c/RU5yM2Ov5Mg/m/n8Phcid1tCQJ) [LSJ 20001127-2](https://groups.google.com/g/rec.games.trading-cards.jyhad/c/KInac4MQMuA/m/LnpxH08HVbMJ) [LSJ 20010806-1](https://groups.google.com/g/rec.games.trading-cards.jyhad/c/PuawBcgSIKI/m/D7zOKJXQDbMJ) — {Bomb}.
[^1-10-5]: [LSJ 20070307](https://groups.google.com/g/rec.games.trading-cards.jyhad/c/QlMNPzNtXh8/m/8Fn_o90mcoMJ) [LSJ 20070308](https://groups.google.com/g/rec.games.trading-cards.jyhad/c/QlMNPzNtXh8/m/D-1FzDFnhhUJ) — {Riddle Phantastique}, {Secret Horde}; [LSJ 20001118](https://groups.google.com/g/rec.games.trading-cards.jyhad/c/r59jQZbWMi0/m/kesQz7kYbD0J) — {Dominique}.
[^1-10-6]: [LSJ 20041201](https://groups.google.com/g/rec.games.trading-cards.jyhad/c/DY1OggZnMvs/m/_ksMXm3AZd0J) — group "From ash heap to deck" (G00002); [LSJ 20071014](https://groups.google.com/g/rec.games.trading-cards.jyhad/c/Bom6ae7qjbI/m/OznLIo66qgsJ) — {Kaymakli Fragment}; [RTR 20030519](https://groups.google.com/g/rec.games.trading-cards.jyhad/c/NOBWXWrd-vA/m/iEOpQp1uhvAJ) — {Rachel Brandywine}.
[^1-10-7]: [PIB 20150512](https://www.vekn.net/forum/rules-questions/71020-priority-contract-and-provision-of-the-silsila#71053) — {The Black Throne}, {Provision of the Silsila}; [LSJ 20031201-2](https://groups.google.com/g/rec.games.trading-cards.jyhad/c/6lN9MbBeL1E/m/C5qoUyYbEhkJ) — {Taste of Vitae}; [LSJ 20040726](https://groups.google.com/g/rec.games.trading-cards.jyhad/c/LlqCB6LN64g/m/k98Xj1pwjPcJ) [ANK 20191031](https://www.vekn.net/forum/rules-questions/11417-eternal-mask-khobar-towers?start=6#97642) — {The Eternal Mask}.
[^1-11-7]: [LSJ 20090710](https://groups.google.com/g/rec.games.trading-cards.jyhad/c/PBi3na64nkw/m/KOY1R8yWBsIJ) [ANK 20200523](https://www.vekn.net/forum/rules-questions/78648-maabara-and-the-erciyes-fragments-show-or-hidden-card#99928) — {Trochomancy}, {Maabara}.
[^1-11-1]: [LSJ 20090430](https://groups.google.com/g/rec.games.trading-cards.jyhad/c/2STzSnaSgxU/m/CVRMrvVPQmMJ) [ANK 20180628](https://www.vekn.net/forum/rules-questions/76758-toreador-questions?start=6#88446) [LSJ 20041119](https://groups.google.com/g/rec.games.trading-cards.jyhad/c/HMV_pN5mJhQ/m/tzkinpwUq-MJ) [LSJ 19980212](https://groups.google.com/g/rec.games.trading-cards.jyhad/c/fLFLlXZXHqA/m/ggjw8aGjdRoJ) [ANK 20190701](https://www.vekn.net/forum/rules-questions/77763-multiple-questions#95690) [LSJ 20041115](https://groups.google.com/g/rec.games.trading-cards.jyhad/c/ZCmZl5xUhis/m/YoKKqsiFLFgJ) — {Epikasta Rigatos}, {Marthe Dizier}, {The Art of Memory}.
[^1-11-2]: [ANK 20210309-2](https://www.vekn.net/forum/rules-questions/79005-rulebook-gaining-votes?start=6#101807) [LSJ 20020911](https://groups.google.com/g/rec.games.trading-cards.jyhad/c/_lLSO5aevoM/m/7BXDmpWjdLIJ) — group "Vote playable once per game" (G00030), {Echo of Harmonies}.
[^1-11-3]: [ANK 20220805](https://www.vekn.net/forum/rules-questions/79939-attachable-modifiers-reactions-being-removed-prior-to-attachment#105881) [LSJ 20050804](https://groups.google.com/g/rec.games.trading-cards.jyhad/c/Xqa8boGP7C8/m/fpfYjwbay0QJ) — {Melange}, {Darksight}, {Ghouled}, {Echo of Harmonies}.
[^1-11-4]: [LSJ 20050324](https://groups.google.com/g/rec.games.trading-cards.jyhad/c/vhSqnoAt_Bs/m/4yurSS3iyqAJ) [LSJ 20050322](https://groups.google.com/g/rec.games.trading-cards.jyhad/c/vhSqnoAt_Bs/m/ARfTKxaZII0J) [RTR 19980928](https://groups.google.com/g/rec.games.trading-cards.jyhad/c/Xva4_IRavxM/m/F-_fjzTmo88J) [LSJ 19980929](https://groups.google.com/g/rec.games.trading-cards.jyhad/c/Xva4_IRavxM/m/EXmGKbctBzwJ) — {Delaying Tactics}, {The Erciyes Fragments}, {Compel the Spirit}.
[^1-11-5]: [LSJ 20020115](https://groups.google.com/g/rec.games.trading-cards.jyhad/c/wG_tDLgfZso/m/6mKkp7Rw3OcJ) [LSJ 20071014](https://groups.google.com/g/rec.games.trading-cards.jyhad/c/Bom6ae7qjbI/m/OznLIo66qgsJ) [LSJ 20030128](https://groups.google.com/g/rec.games.trading-cards.jyhad/c/d25nONe01WY/m/xqfEs_qwc7gJ) [LSJ 20011216-1](https://groups.google.com/g/rec.games.trading-cards.jyhad/c/xwirj771uGM/m/0w1qJBEabFEJ) — group "Action creating vampire" (G00054), {Jake Washington}, {Spell of Life}, {Compel the Spirit}, {Resurrection}.
[^1-11-6]: [ANK 20200417](https://www.vekn.net/forum/rules-questions/78568-the-capuchin-burns-temporary-control?start=12#99616) [LSJ 20060209](https://groups.google.com/g/rec.games.trading-cards.jyhad/c/ZuOfZorIhhU/m/X5G1JfqDPhcJ) [LSJ 20040812](https://groups.google.com/g/rec.games.trading-cards.jyhad/c/n_0DGDsWG0E/m/lxG2zMPetwAJ) [LSJ 20010627](https://groups.google.com/g/rec.games.trading-cards.jyhad/c/NhNCVCCDyU0/m/I5Yph3-UUPsJ) — {The Capuchin}, {Grasp the Ghostly}, {Père Lachaise, France}, {Khazar's Diary (Endless Night)}.
[^1-11-8]: [LSJ 20070808-1](https://groups.google.com/g/rec.games.trading-cards.jyhad/c/jzMOxZ9oxOs/m/o0X7GUFmii0J) — {Ambulance}, {Foresee}, {Torrent}.
[^1-12-1]: [LSJ 20021128](https://groups.google.com/g/rec.games.trading-cards.jyhad/c/6rqhybcysh8/m/hU-qIp2on-YJ) [SFC 19960919](https://groups.google.com/g/rec.games.trading-cards.jyhad/c/_UxVq0Lrg2U/m/xlsK8NogrW4J) [LSJ 20100302-2](https://groups.google.com/g/rec.games.trading-cards.jyhad/c/b2cW6X-RQMs/m/RY2Zrzk6Ga0J) [RTR 19941109](https://groups.google.com/d/msg/rec.games.deckmaster/_6CXoKTSLnw/FdG67-3HEAQJ) [ANK 20200417](https://www.vekn.net/forum/rules-questions/78568-the-capuchin-burns-temporary-control?start=12#99616) [RBK important-terms-of-the-game](https://www.vekn.net/rulebook#important-terms-of-the-game) — group "Cards holding cards" (G00028), {Memory's Fading Glimpse}, {Raw Recruit}, {Betrayer}, {The Capuchin}.
[^1-12-8]: [LSJ 20080816](https://groups.google.com/g/rec.games.trading-cards.jyhad/c/FKBTEzLf0_A/m/eK1AuUnPolMJ) [RBK contested-cards](https://www.vekn.net/rulebook#contested-cards) — {Descent into Darkness}.
[^1-12-2]: [ANK 20180511-1](https://www.vekn.net/forum/rules-questions/76594-lost-kindred-faq#86769) — {Righteous Aura}.
[^1-12-3]: [LSJ 20071206](https://groups.google.com/g/rec.games.trading-cards.jyhad/c/B-5oDAJrwiI/m/ui9coMgXYUMJ) [LSJ 20090725](https://groups.google.com/g/rec.games.trading-cards.jyhad/c/isG743Sws-8/m/cjTJkGtfl_gJ) [LSJ 20010616](https://groups.google.com/g/rec.games.trading-cards.jyhad/c/h7gnHNBFliE/m/MsfJ0qqv_jsJ) [LSJ 20030522-1](https://groups.google.com/g/rec.games.trading-cards.jyhad/c/_krZG-uPtzc/m/94US5l81edwJ) — {The Eternal Mask}, {Tegyrius, Vizier}.
[^1-12-4]: [ANK 20190629](https://www.vekn.net/forum/rules-questions/77740-mummify-and-shadow-court-satyr?start=6#95656) — {Shadow Court Satyr}.
[^1-12-5]: [PIB 20121028](https://www.vekn.net/forum/rules-questions/39816-ec-2012-can-you-answer-these?start=6#39843) [LSJ 20001031](https://groups.google.com/g/rec.games.trading-cards.jyhad/c/y8LNZhRyXO0/m/EJzinwvnFoYJ) [PIB 20121220](https://www.vekn.net/forum/rules-questions/43188-storage-annex-changes-control?start=6#43199) — {Anathema}, {Storage Annex}.
[^1-12-6]: [ANK 20221028](https://www.vekn.net/forum/rules-questions/80119-contesting-mokole-blood#106671) [LSJ 20090428-1](https://groups.google.com/g/rec.games.trading-cards.jyhad/c/887DQTpntKI/m/hYSLzUDm5iUJ) — {Mokolé Blood}, {Shilmulo Tarot}, {Elder Library}.
[^1-12-7]: [LSJ 20070307](https://groups.google.com/g/rec.games.trading-cards.jyhad/c/QlMNPzNtXh8/m/8Fn_o90mcoMJ) [LSJ 20070308](https://groups.google.com/g/rec.games.trading-cards.jyhad/c/QlMNPzNtXh8/m/D-1FzDFnhhUJ) [RTR 19970306](https://groups.google.com/g/rec.games.trading-cards.jyhad/c/1dlmpgX6t14/m/hNDHCjT8Ew8J) [LSJ 20001118](https://groups.google.com/g/rec.games.trading-cards.jyhad/c/r59jQZbWMi0/m/kesQz7kYbD0J) — {Riddle Phantastique}, {Secret Horde}, {Goth Band}, {Dominique}.
[^1-13-1]: [LSJ 20070928-2](https://groups.google.com/g/rec.games.trading-cards.jyhad/c/duRrP46XygI/m/FrFYvbUYFf0J) [LSJ 20071001-2](https://groups.google.com/g/rec.games.trading-cards.jyhad/c/XoMeEYJw1ZA/m/zVM8X9aZlgQJ) [RBK contested-cards](https://www.vekn.net/rulebook#contested-cards) — {Spell of Life}.
[^1-13-2]: [LSJ 20100213](https://groups.google.com/g/rec.games.trading-cards.jyhad/c/vXDkYrTmkws/m/sKy3jXz7AB4J) [LSJ 19991110](https://groups.google.com/g/rec.games.trading-cards.jyhad/c/5hDqAMewLtg/m/fib2UDF58CUJ) [LSJ 20030419](https://groups.google.com/g/rec.games.trading-cards.jyhad/c/A0mvllC-tgs/m/GqjZTFN9SvMJ) [RTR 20180303](https://www.vekn.net/forum/rules-questions/76447-rules-team-rulings-rtr-03-03-2018#85536) — {Illusions of the Kindred}, {Jimmy Dunn}.
[^1-13-3]: [PIB 20121031](https://www.vekn.net/forum/rules-questions/39816-ec-2012-can-you-answer-these?start=18#39908) [LSJ 20040722](https://groups.google.com/g/rec.games.trading-cards.jyhad/c/z3Tfg9PZVNo/m/TAasVyubnpsJ) [LSJ 20010623-2](https://groups.google.com/g/rec.games.trading-cards.jyhad/c/65IHHAii7ms/m/uoIs8B1vdToJ) [RTR 20010710](https://groups.google.com/g/rec.games.trading-cards.jyhad/c/GsI1UyH54jU/m/x9LfDZX1vR4J) [LSJ 20030918](https://groups.google.com/g/rec.games.trading-cards.jyhad/c/Lae6k2AG-1c/m/GOqdTox6CRsJ) [RBK contested-cards](https://www.vekn.net/rulebook#contested-cards) — {Visit from the Capuchin}, {Chain of Command}, {Parmenides}, {Soul Gem of Etrius}.
[^1-13-4]: [LSJ 20080526](https://groups.google.com/g/rec.games.trading-cards.jyhad/c/zO3l3b76rjQ/m/da5R20AzyO4J) [LSJ 20100902](https://groups.google.com/g/rec.games.trading-cards.jyhad/c/SM2_578Th0U/m/-GX0pSP_rCcJ) [ANK 20180626-1](https://www.vekn.net/forum/rules-questions/76751-two-questions-that-recently-came-up#88393) [ANK 20211214](https://www.vekn.net/forum/rules-questions/79542-anarch-convert?start=6#104185) [ANK 20221028](https://www.vekn.net/forum/rules-questions/80119-contesting-mokole-blood#106671) [LSJ 20090428-1](https://groups.google.com/g/rec.games.trading-cards.jyhad/c/887DQTpntKI/m/hYSLzUDm5iUJ) — {Wormwood}, {Anarch Convert}, {Dr. Solomon Grey}, {Erlik}, {Mokolé Blood}, {Shilmulo Tarot}.
[^1-13-5]: [LSJ 20070829-2](https://groups.google.com/g/rec.games.trading-cards.jyhad/c/drn7wHaGugQ/m/QqaYmjAf2UYJ) — {Sonja Blue}.
[^1-13-6]: [ANK 20221028](https://www.vekn.net/forum/rules-questions/80119-contesting-mokole-blood#106671) [LSJ 20080107](https://groups.google.com/g/rec.games.trading-cards.jyhad/c/XpZ6F53jK-c/m/wB6HHGzgFi4J) [RTR 19960124](https://groups.google.com/g/rec.games.trading-cards.jyhad/c/wF82VdVPlm0/m/cSshmBFQs-EJ) [LSJ 20100423](https://groups.google.com/g/rec.games.trading-cards.jyhad/c/YnQCu0GeMhc/m/ET__SGvjD7QJ) [LSJ 20100127](https://groups.google.com/g/rec.games.trading-cards.jyhad/c/YnQCu0GeMhc/m/ET__SGvjD7QJ) [LSJ 19980319](https://groups.google.com/g/rec.games.trading-cards.jyhad/c/i1Eqqm5Ctv0/m/TQIvuprMrjsJ) — {Elder Library}, {Guillaume Giovanni}, {Secure Haven}, {Byzar}, {Disguised Weapon}.
[^1-13-7]: [RTR 19941109](https://groups.google.com/d/msg/rec.games.deckmaster/_6CXoKTSLnw/FdG67-3HEAQJ) [LSJ 20080816](https://groups.google.com/g/rec.games.trading-cards.jyhad/c/FKBTEzLf0_A/m/eK1AuUnPolMJ) — {Betrayer}, {Descent into Darkness}.
[^1-13-8]: [LSJ 20070808-2](https://groups.google.com/g/rec.games.trading-cards.jyhad/c/gaFBeSrs7fU/m/v0VVEOJd2HYJ) [RBK contested-titles](https://www.vekn.net/rulebook#contested-titles) — group "Title providing action" (G00042).
[^1-13-9]: [RTR 20000501](https://groups.google.com/g/rec.games.trading-cards.jyhad/c/MKrA0hBXuaU/m/1M5LOLftKWAJ) [LSJ 20060908](https://groups.google.com/g/rec.games.trading-cards.jyhad/c/CTy2GjM6-Dc/m/9OPulYVGaFcJ) [ANK 20210630](https://www.vekn.net/forum/rules-questions/79205-lay-low-vs-banishment#102601) [LSJ 20010809-2](https://groups.google.com/g/rec.games.trading-cards.jyhad/c/9ggmJcK2De0/m/2xW0xE2SzisJ) [LSJ 20010809-3](https://groups.google.com/g/rec.games.trading-cards.jyhad/c/gLl8F0zcCF0/m/cR8nsUweLQIJ) — {Descent into Darkness}, {Lay Low}, {The Rack}.
[^1-13-10]: [RTR 19960112](https://groups.google.com/g/rec.games.trading-cards.jyhad/c/d3n3StNS7no/m/k2NmZFUl9fAJ) [TOM 19960122](https://groups.google.com/g/rec.games.trading-cards.jyhad/c/d3n3StNS7no/m/Wwj5SYMQPskJ) — {The Rack}.
[^1-13-11]: [LSJ 19990719](https://groups.google.com/g/rec.games.trading-cards.jyhad/c/kKtW2qo6ACE/m/4hs5tbGDC1cJ) [RTR 19991001](https://groups.google.com/g/rec.games.trading-cards.jyhad/c/RAvWWmYoX3U/m/lb2bLOvJDhoJ) — {Jimmy Dunn}.
[^1-14-1]: [LSJ 20010627](https://groups.google.com/g/rec.games.trading-cards.jyhad/c/NhNCVCCDyU0/m/I5Yph3-UUPsJ) [LSJ 20050422](https://groups.google.com/g/rec.games.trading-cards.jyhad/c/nJPfMOuTBtw/m/COytKb_oEM4J) — {The Sargon Fragment}, {Pochtli}, {Sudario Refraction}; same wording on {Clio's Kiss}, {Gear Up}, {Pandora's Whisper}, {Scarlet Lore}, {Whispers from the Dead}, {Drozodny}, {Patrizia Giovanni, Collector of Secrets}.
[^1-14-2]: [LSJ 20091030](https://groups.google.com/g/rec.games.trading-cards.jyhad/c/ZKuCyTayYbc/m/5nMjLpX4DuMJ) — {Magic of the Smith}, {Ashur Tablets}.
[^1-14-3]: [PIB 20110725](https://www.vekn.net/forum/rules-questions/6728-announcing-siphon#6740) [LSJ 20090722](https://groups.google.com/g/rec.games.trading-cards.jyhad/c/r-N65rA52uo/m/OXW8xk1r1iMJ) — {Siphon}, {Sudario Refraction}.
[^1-14-4]: [LSJ 19991207](https://groups.google.com/g/rec.games.trading-cards.jyhad/c/aQaOTYwC-fg/m/vdyo09QZoicJ) [ANK 20180925-2](https://www.vekn.net/forum/rules-questions/77029-order-of-draw-and-replace-for-concealed-weapon-under-infernal-pursuit?start=6#90757) [LSJ 20100130](https://groups.google.com/g/rec.games.trading-cards.jyhad/c/X8Uu7Sk56P4/m/twUvR4ZnBBkJ) [RTR 19991001](https://groups.google.com/g/rec.games.trading-cards.jyhad/c/RAvWWmYoX3U/m/lb2bLOvJDhoJ) [LSJ 20101210](https://groups.google.com/g/rec.games.trading-cards.jyhad/c/QTAA0y6cANI/m/gU0hztzp8mUJ) [ANK 20220704](https://www.vekn.net/forum/rules-questions/79890-charming-lobby-a-political-action-card-krc?start=0#105616) [PIB 20150428](https://www.vekn.net/forum/rules-questions/70714-card-replacement?start=6#70747) — {Disguised Weapon}, {Concealed Weapon}, {Charming Lobby}, {Jack of Both Sides}, {Gift of Proteus}.
[^1-14-5]: [ANK 20201029](https://www.vekn.net/forum/rules-questions/78889-charming-lobby-and-echo-of-harmonies#101020) [LSJ 20041130](https://groups.google.com/g/rec.games.trading-cards.jyhad/c/6uTPqRg387A/m/fa9DW8-Hu38J) [LSJ 20100527](https://groups.google.com/g/rec.games.trading-cards.jyhad/c/Tr3X4DsZr-8/m/O06iXN6LtzsJ) — {Charming Lobby}, {Delaying Tactics}.
[^1-14-6]: [LSJ 20050118](https://groups.google.com/g/rec.games.trading-cards.jyhad/c/W784_3oyz7I/m/Cgek1j9Hv-8J) — {The Erciyes Fragments}.
[^1-14-7]: [LSJ 20100211-2](https://groups.google.com/g/rec.games.trading-cards.jyhad/c/pL63VXEPGME/m/n2dEkxwYyjcJ) — {Baal's Bloody Talons}, {Cleave}.
[^1-15-1]: [LSJ 19980225](https://groups.google.com/g/rec.games.trading-cards.jyhad/c/62y-5miA8MQ/m/EhtcS-ia9b8J) [RTR 19941222](https://groups.google.com/g/rec.games.trading-cards.jyhad/c/19Ys4rdQPQw/m/bijoNa8Z8FsJ) [LSJ 20061018](https://groups.google.com/g/rec.games.trading-cards.jyhad/c/Prc45fTQd9Y/m/uvFhSQKCBakJ) [ANK 20200703-4](https://www.vekn.net/forum/rules-questions/78709-judgement#100235) [RTR 19941109](https://groups.google.com/d/msg/rec.games.deckmaster/_6CXoKTSLnw/FdG67-3HEAQJ) — {Aching Beauty}, {Anarch Revolt}, {Archon}, {Camarilla Exemplary}, {Sabbat Priest}, {First Tradition: The Masquerade}, {Frontal Assault}, {Judgment: Camarilla Segregation}, {Betrayer}.
[^1-15-2]: [LSJ 20020904](https://groups.google.com/g/rec.games.trading-cards.jyhad/c/Qmi4hFk6QqE/m/VmoU2tfLMgEJ) [LSJ 20010819](https://groups.google.com/g/rec.games.trading-cards.jyhad/c/2dXfHhG98Rs/m/RMqiA8RXDncJ) [PIB 20130722](https://www.vekn.net/forum/rules-questions/52017-legacy-of-pander#52019) [PIB 20130303](https://www.vekn.net/forum/rules-questions/45620-rock-cat-vs-torn-signpost#45626) [LSJ 20100813](https://groups.google.com/g/rec.games.trading-cards.jyhad/c/nOb3cmvA_3U/m/0UJqPZGujHsJ) [LSJ 20051204](https://groups.google.com/g/rec.games.trading-cards.jyhad/c/K-RE-nTJ_Cg/m/pw5WbBaM1WEJ) [LSJ 20060407](https://groups.google.com/g/rec.games.trading-cards.jyhad/c/YY2aBVshruI/m/2EBdovv4CeEJ) [LSJ 20090625-2](https://groups.google.com/g/rec.games.trading-cards.jyhad/c/WqwoI03BW1U/m/C5t35BEoTroJ) [LSJ 20100601](https://groups.google.com/g/rec.games.trading-cards.jyhad/c/R7YgwD0VlUQ/m/lhGLnME9m2IJ) — {Mass Reality}, {Legacy of Pander}, {Torn Signpost}, {Orun}, {Xeper, Sultan of Lepers}.
[^1-15-3]: [LSJ 19970707](https://groups.google.com/g/rec.games.trading-cards.jyhad/c/KWekwiRSa2I/m/9pS17rzBBDYJ) [LSJ 20001102](https://groups.google.com/g/rec.games.trading-cards.jyhad/c/LlPyLJjLdx0/m/mXimdmP14GEJ) [RTR 19951017](https://groups.google.com/g/rec.games.trading-cards.jyhad/c/ouhNUbHYg50/m/rco157ZHyqEJ) [LSJ 20010227](https://groups.google.com/g/rec.games.trading-cards.jyhad/c/rdkVAtZFC2I/m/rW1nXhSsyVcJ) — {Camarilla Exemplary}, {Courier}, {Kindred Society Games}, {Temptation}.
[^1-15-4]: [LSJ 20070306](https://groups.google.com/g/rec.games.trading-cards.jyhad/c/QiFXAaAeJds/m/M5TWYR2cZLMJ) [LSJ 20030820](https://groups.google.com/g/rec.games.trading-cards.jyhad/c/Zjmffk-EbJw/m/ExNZqDUNQt8J) [LSJ 20090603](https://groups.google.com/g/rec.games.trading-cards.jyhad/c/LpFSLRuWONA/m/Ma_3LtLeyCAJ) [RTR 19951110](https://groups.google.com/g/rec.games.trading-cards.jyhad/c/TXfganI5B2o/m/QYh3AdPNbUwJ) — {Dr. Morrow, The Skindoctor}, {Kahina the Sorceress}, {Orun}, {Scorn of Adonis}.
[^1-15-5]: [ANK 20180111](https://www.vekn.net/forum/rules-questions/76364-leech-putrescent-servitude#84864) — {Leech}, {Putrescent Servitude}.
[^1-15-6]: [ANK 20200515](https://www.vekn.net/forum/rules-questions/78634-blanket-of-night#99838) — {Blanket of Night}, {Cloak the Gathering}, {Inspire Greatness}, {Mask of a Thousand Faces}, {Suppressing Fire}.
[^1-15-7]: [LSJ 20041103](https://groups.google.com/g/rec.games.trading-cards.jyhad/c/MiPHVp-NmCA/m/P323pUaD4DwJ) — {Lunatic Eruption}.
[^2-1-1]: [LSJ 20100723](https://groups.google.com/g/rec.games.trading-cards.jyhad/c/0u5KQWiutdg/m/lAZoy4vIwiIJ) [ANK 20200616](https://www.vekn.net/forum/rules-questions/78687-the-erciyes-fragments-fragment-of-the-book-of-nod-barrens-impulse#100110) [PIB 20120808](https://www.vekn.net/forum/rules-questions/34265-rules-tweak-suggestion-rewind-time-et-al?start=12#34448) [RBK targeting-of-cards](https://www.vekn.net/rulebook#targeting-of-cards) — {Owain Evans, The Wanderer}; group "Can draw during action" (G00023); group "Cancel with no action" (G00063).
[^2-1-2]: [LSJ 19990425](https://groups.google.com/g/rec.games.trading-cards.jyhad/c/Mmfn07ib6Yw/m/YfwpUlqEdrEJ) [SFC 19960819](https://groups.google.com/g/rec.games.trading-cards.jyhad/c/G40EE8vCBB8/m/Bj3qpDZ_VLkJ) [RBK summary-of-the-course-of-an-action](https://www.vekn.net/rulebook#summary-of-the-course-of-an-action) — {Blanket of Night}, {Siren's Lure}, {Veil the Legions}, {Empowering the Puppet King}, {Inspire Greatness}, {Spiridonas}.
[^2-1-3]: [ANK 20181101](https://www.vekn.net/forum/rules-questions/77132-save-face#91633) [LSJ 20070403](https://groups.google.com/g/rec.games.trading-cards.jyhad/c/TJ2ktt_1tjk/m/fdH_x9tDmN8J) [LSJ 20070413](https://groups.google.com/g/rec.games.trading-cards.jyhad/c/umdINigMKqs/m/lfUAxTnfttIJ) — {Bliss}, {Hide}, {Surge}, {Vigilance}.
[^2-1-4]: [LSJ 20010110](https://groups.google.com/g/rec.games.trading-cards.jyhad/c/Vtm465mblX4/m/B6pCvotsfFsJ) [LSJ 20050111](https://groups.google.com/g/rec.games.trading-cards.jyhad/c/lnW6nMIX-Vw/m/iVd07z5jvu8J) [LSJ 19980825](https://groups.google.com/g/rec.games.trading-cards.jyhad/c/g7N36pL8Gsk/m/YurxIfPsy7kJ) [PIB 20121028](https://www.vekn.net/forum/rules-questions/39816-ec-2012-can-you-answer-these?start=6#39843) [LSJ 20001111](https://groups.google.com/g/rec.games.trading-cards.jyhad/c/m23Hj3OW2A4/m/n23vvkXo6AkJ) — {Heidelberg Castle, Germany}, {Mask of a Thousand Faces}, {Baltimore Purge}, {Temptation}, {Vagabond Mystic}.
[^2-1-5]: [ANK 20210608](https://www.vekn.net/forum/rules-questions/79166-correct-time-to-use-heidelberg-castle-germany-for-non-acting-player?start=12#102425) [ANK 20170918-2](https://www.vekn.net/forum/rules-questions/76178-siren-s-lure-and-heidelberg-castle-timing-question#83580) — {Heidelberg Castle, Germany}, {Louvre, Paris, The}, {Siren's Lure}.
[^2-1-6]: [RTR 19960112](https://groups.google.com/g/rec.games.trading-cards.jyhad/c/d3n3StNS7no/m/k2NmZFUl9fAJ) [LSJ 19990217](https://groups.google.com/g/rec.games.trading-cards.jyhad/c/9Bsf2LC1274/m/pHWAxcO_7pgJ) [RTR 20041202](https://groups.google.com/g/rec.games.trading-cards.jyhad/c/WUWh7AdooDU/m/vojisZMCSnsJ) [LSJ 20100119](https://groups.google.com/g/rec.games.trading-cards.jyhad/c/1eULCGaVcO0/m/eefMWzjoK0IJ) [ANK 20201228](https://www.vekn.net/forum/rules-questions/78956-timing-of-blood-hunt-following-amaranth#101316) [RTR 19991206](https://groups.google.com/g/rec.games.trading-cards.jyhad/c/N7iEmqgP9WU/m/gX80TroOBsUJ) [ANK 20230620](https://www.vekn.net/forum/rules-questions/80612-when-to-use-shard-the-line-when-action-becoems-to-expensive-after-announcement#108409) [ANK 20180531](https://www.vekn.net/forum/rules-questions/76673-melange-vs-archon#87771) — {Spirit Claws}, {Rötschreck}, {Slake the Thirst}, {Soul Stealing}, {Powerbase: Tshwane}, {Melange}.
[^2-1-7]: [LSJ 19980105](https://groups.google.com/g/rec.games.trading-cards.jyhad/c/PzVC-AeFuUQ/m/ncbtQyYNpFQJ) [LSJ 20090205](https://groups.google.com/g/rec.games.trading-cards.jyhad/c/l5bUtHOejmc/m/Ksw_nyldc3QJ) — {Deflection}, {Redirection}, {Lost in Translation}, {My Enemy's Enemy}, {Major Boon}.
[^2-2-1]: [ANK 20190425](https://www.vekn.net/forum/rules-questions/77581-action-modifiers-played-at-beginning-and-end-of-an-action#94652) [RBK summary-of-the-course-of-an-action](https://www.vekn.net/rulebook#summary-of-the-course-of-an-action) — group "Modifier as announced" (G00052); {Force of Personality}, {Shroud Mastery}, {Hide}.
[^2-2-2]: [LSJ 20081105](https://groups.google.com/g/rec.games.trading-cards.jyhad/c/CYjOJtTBMGU/m/H8kQXN1w2ycJ) [PIB 20150820](https://www.vekn.net/forum/rules-questions/72462-hide-the-heart-timing-questions#72626) — {Yoruba Shrine}, {Car Bomb}.
[^2-2-3]: [ANK 20181208](https://www.vekn.net/forum/rules-questions/77210-touch-of-clarity-and-fast-reaction-is-posible-to-play-with-locked-minion?start=6#92308) — group "Modifier as announced" (G00052); {Approximation of Loyalty}, {Force of Personality}.
[^2-2-4]: [LSJ 20100402](https://groups.google.com/g/rec.games.trading-cards.jyhad/c/BNPERBLJwRc/m/ynUIJFJ0EZcJ) — {Concoction of Vitality}.
[^2-2-5]: [LSJ 19980105](https://groups.google.com/g/rec.games.trading-cards.jyhad/c/PzVC-AeFuUQ/m/ncbtQyYNpFQJ) — {Telepathic Misdirection}, {Archon Investigation}.
[^2-3-1]: [LSJ 19981028](https://groups.google.com/g/rec.games.trading-cards.jyhad/c/JZHY1bTCAa0/m/XqDVERty0roJ) [ANK 20190425](https://www.vekn.net/forum/rules-questions/77581-action-modifiers-played-at-beginning-and-end-of-an-action#94652) — group "Modifier after resolution" (G00006); {Domain of Evernight}, {Forced March}, {Fata Amria}. [LSJ 20030219](https://groups.google.com/g/rec.games.trading-cards.jyhad/c/ugfckv9DAbo/m/w5UP-Ch-u5MJ) — {Spirit Marionette}. [LSJ 20090731](https://groups.google.com/g/rec.games.trading-cards.jyhad/c/y6f0s6tUtqs/m/H3dk4qr4nfkJ) — {Last Stand}. [ANK 20180909](https://www.vekn.net/forum/rules-questions/76987-ophidian-gaze-and-post-referendum-action-modifiers#90501) — {Ophidian Gaze}.
[^2-3-2]: [LSJ 20050422](https://groups.google.com/g/rec.games.trading-cards.jyhad/c/nJPfMOuTBtw/m/COytKb_oEM4J) — {Dis Pater}. [ANK 20190113](https://www.vekn.net/forum/rules-questions/77290-freak-drive-capitalist?start=12#92827) [ANK 20190425](https://www.vekn.net/forum/rules-questions/77581-action-modifiers-played-at-beginning-and-end-of-an-action#94652) — {Capitalist}, {Cavalier}, {Perfectionist}, {Scrying of Secrets}, {Truth of a Thousand Lies}, {Vigilance}.
[^2-3-3]: [LSJ 20110502](https://boardgamegeek.com/thread/648695/article/6701545) [LSJ 19980105](https://groups.google.com/g/rec.games.trading-cards.jyhad/c/PzVC-AeFuUQ/m/ncbtQyYNpFQJ) — {Spying Mission}.
[^2-3-4]: [LSJ 20041022](https://groups.google.com/g/rec.games.trading-cards.jyhad/c/gqhND6kd2wE/m/LDmEotxa_4kJ) [RTR 20180719](https://www.blackchantry.com/2018/07/18/rules-team-rulings-rtr-19-07-2018/) [ANK 20220118](https://www.vekn.net/forum/rules-questions/79389-when-does-nra-apply-not-apply?start=6#104506) [ANK 20221205](https://www.vekn.net/forum/rules-questions/80196-clarification-regarding-detect-authority#106923) — {Champion}, {Car Bomb}, {Ensconced}, {Detect Authority}, {Faerie Wards}, {Final Loosening}, {Hide}, {Hide the Heart}, {Malkavian Derangement: Alternate Personality}, {Purification}, {Scobax}. [LSJ 20010803-1](https://groups.google.com/g/rec.games.trading-cards.jyhad/c/5QuGIF5ERUI/m/nGJoAyeiOJQJ) [ANK 20200207](https://www.vekn.net/forum/rules-questions/78423-mental-maze-and-obedience#98906) — {Change of Target}, {Claiming the Body}, {The Kiss of Ra}.
[^2-3-5]: [LSJ 19981028](https://groups.google.com/g/rec.games.trading-cards.jyhad/c/JZHY1bTCAa0/m/XqDVERty0roJ) [LSJ 20100206-2](https://groups.google.com/g/rec.games.trading-cards.jyhad/c/reXyybyIYX8/m/jeCyjdiZ5T4J) — {Follow the Blood}, {Momentary Delay}.
[^2-3-6]: [ANK 20180206](https://www.vekn.net/forum/rules-questions/76404-timing-of-shemti-s-special-and-ecstasy#85223) — {The Damned}, {Ecstasy}, {Travelers Obey the Tenets}, {Shemti}. [LSJ 20100324](https://groups.google.com/g/rec.games.trading-cards.jyhad/c/PWhoejXDuuA/m/4E1wohx0oHwJ) [LSJ 20071116](https://groups.google.com/g/rec.games.trading-cards.jyhad/c/ZPsShBUBWZI/m/MJ9zobOVjHkJ) — {Games of Instinct}, {Save Face}.
[^2-3-7]: [ANK 20230314](https://www.vekn.net/forum/rules-questions/80378-monster-vs-provision-of-silsila#107622) — {Provision of the Silsila}, {Monster}, {Shadow Boxing}.
[^2-3-8]: [LSJ 20010715](https://groups.google.com/g/rec.games.trading-cards.jyhad/c/u91PfJOfOjE/m/BS264hmTIEgJ) — {Force of Will}. [ANK 20171124](https://www.vekn.net/forum/rules-questions/76304-question-about-timing-of-force-of-will-damage-and-heidelberg?start=0#84354) — {Heidelberg Castle, Germany}. [LSJ 20100325](https://groups.google.com/g/rec.games.trading-cards.jyhad/c/PWhoejXDuuA/m/5565uQm2dpEJ) — {Slake the Thirst}. [PIB 20150915](https://www.vekn.net/forum/rules-questions/73134-learjet#73139) — {Freak Drive}.
[^2-3-9]: [LSJ 20091123](https://groups.google.com/g/rec.games.trading-cards.jyhad/c/Yt7LsvWFwiM/m/op6oRS8SLiYJ) — {Wake with Evening's Freshness}, {Eyes of Argus}, {Forced Awakening}, {On the Qui Vive}.
[^2-3-10]: [LSJ 20030103](https://groups.google.com/g/rec.games.trading-cards.jyhad/c/TUDO_4FwdyY/m/DWOwgQL850gJ) [ANK 20181219](https://www.vekn.net/forum/rules-questions/77232-zephyr-timing#92505) [ANK 20180906](https://www.vekn.net/forum/rules-questions/76981-freak-drive-while-going-to-torpor#90451) — group "Modifier after combat" (G00007); [RTR 19980623](https://groups.google.com/g/rec.games.trading-cards.jyhad/c/tSpd9dtTElc/m/-CuHJF54_n0J) — {Freak Drive}, {Hay Ride}; [LSJ 20040219](https://groups.google.com/g/rec.games.trading-cards.jyhad/c/zFmoLa6tzWA/m/eJnERTCB-NEJ) [ANK 20221130](https://www.vekn.net/forum/rules-questions/80176-cats-guidance-before-psyche-combat?start=0#106906) — {Cats' Guidance}.
[^2-3-11]: [ANK 20200221](https://www.vekn.net/forum/rules-questions/78458-strix-daring-the-dawn-and-much-more#99036) — {Strix}. [LSJ 20060426](https://groups.google.com/g/rec.games.trading-cards.jyhad/c/4e6z1_JWIzA/m/oMQz7oVR1O8J) — {High Aye}. [LSJ 20031112](https://groups.google.com/g/rec.games.trading-cards.jyhad/c/NW4HWUWlzDI/m/qDPeTd5ZuugJ) — {The Art of Memory}.
[^2-3-12]: [LSJ 20100112](https://groups.google.com/g/rec.games.trading-cards.jyhad/c/SJu0kgw_2tE/m/p5cshF90vkEJ) [PIB 20121028](https://www.vekn.net/forum/rules-questions/39816-ec-2012-can-you-answer-these?start=6#39843) — {Abactor}. [LSJ 20090722-2](https://groups.google.com/g/rec.games.trading-cards.jyhad/c/Ry0xU4IuJmQ/m/6WqoTXkzrVUJ) [LSJ 20030618](https://groups.google.com/g/rec.games.trading-cards.jyhad/c/AdfUNNicx-Y/m/SDYFb37pS-wJ) — {Heidelberg Castle, Germany}. [ANK 20201228](https://www.vekn.net/forum/rules-questions/78956-timing-of-blood-hunt-following-amaranth#101316) — {Ritual of the Bitter Rose}. [LSJ 20090115-2](https://groups.google.com/g/rec.games.trading-cards.jyhad/c/rSaiVPMbpvY/m/ZYG3cYIdQZkJ) — {Guru}.
[^2-4-1]: [ANK 20180206](https://www.vekn.net/forum/rules-questions/76404-timing-of-shemti-s-special-and-ecstasy#85223) [LSJ 20020904-2](https://groups.google.com/g/rec.games.trading-cards.jyhad/c/ObuKimgcCpI/m/PVsmKoSZueoJ) [LSJ 20100211-2](https://groups.google.com/g/rec.games.trading-cards.jyhad/c/pL63VXEPGME/m/n2dEkxwYyjcJ) [LSJ 20020301](https://groups.google.com/g/rec.games.trading-cards.jyhad/c/HgmPj9MEdiQ/m/P_y2T-_6MH4J) [RBK sequencing](https://www.vekn.net/rulebook#sequencing) — {The Damned}, {Ecstasy}, {Travelers Obey the Tenets}, {Shemti}, {Dreams of the Sphinx}, {Cleave}, {Darkness Within}.
[^2-4-2]: [LSJ 20021113](https://groups.google.com/g/rec.games.trading-cards.jyhad/c/df2P8YHZex8/m/mGCmsxDjI_YJ) [ANK 20191219](https://www.vekn.net/forum/rules-questions/78241-relentless-reaper-vs-blissful-agony-and-scheduled-combat-rulings-ambiguity#98308) [ANK 20180910-1](https://www.vekn.net/forum/rules-questions/76990-correct-order-impulse-for-combat-cards-after-combat#90517) [RTR 20030519](https://groups.google.com/g/rec.games.trading-cards.jyhad/c/NOBWXWrd-vA/m/iEOpQp1uhvAJ) — {Disarm}, {Pulled Fangs}, {Street Cred}, {Taste of Vitae}, {Relentless Reaper}, {Psyche!}, {Telepathic Tracking}.
[^2-4-3]: [LSJ 20100218](https://groups.google.com/g/rec.games.trading-cards.jyhad/c/x-uJChHi76Y/m/F92fWI7WwaEJ) [RTR 20180511-2](https://www.vekn.net/forum/rules-questions/76595-rules-team-rulings-rtr-11-05-2018?start=30#86840) [LSJ 20001206](https://groups.google.com/g/rec.games.trading-cards.jyhad/c/kFIO74LxqFQ/m/U1Dtf3f4CPgJ) [ANK 20211124](https://www.vekn.net/forum/rules-questions/79501-addition-strikes#103982) — {Power of One}, {Quicksilver Contemplation}, {Quickness}.
[^2-4-4]: [ANK 20191219](https://www.vekn.net/forum/rules-questions/78241-relentless-reaper-vs-blissful-agony-and-scheduled-combat-rulings-ambiguity#98308) — {Telepathic Tracking}.
[^2-4-5]: [TOM 19960413](https://groups.google.com/g/rec.games.trading-cards.jyhad/c/Gm-NLCP6bF0/m/sVxss5F1bBYJ) [LSJ 20030213](https://groups.google.com/g/rec.games.trading-cards.jyhad/c/j6cuQ6pFJSA/m/F-A_hlBMpd0J) — {Protected Resources}, {Merrill Molitor}.
[^2-4-9]: [RTR 20010710](https://groups.google.com/g/rec.games.trading-cards.jyhad/c/GsI1UyH54jU/m/x9LfDZX1vR4J) [LSJ 20090304-2](https://groups.google.com/g/rec.games.trading-cards.jyhad/c/PcbRGxbYQUY/m/eOqxJaT85dwJ) [PIB 20120214](https://www.vekn.net/forum/rules-questions/22906-re-set-the-range?start=12#22999) — {Amaranth}, {Decapitate}, {Mustafa, The Heir}, {Squirrel Balance}, {Storm Sewers}.
[^2-4-10]: [LSJ 20021117](https://groups.google.com/g/rec.games.trading-cards.jyhad/c/4TgUatcTtdk/m/HfuRL6wM8IcJ) [PIB 20120225](https://www.vekn.net/forum/rules-questions/24105-blissful-agony-vs-blissful-agony#24106) [LSJ 20011215](https://groups.google.com/g/rec.games.trading-cards.jyhad/c/9WJX_WF656A/m/LpUwuigFmJkJ) [LSJ 20050805](https://groups.google.com/g/rec.games.trading-cards.jyhad/c/mJzy9HKytEc/m/gt6s2WzEqUMJ) — {Anathema}, {Blissful Agony}, {Dual Form}.
[^2-4-11]: [ANK 20200709](https://www.vekn.net/forum/rules-questions/74710-jenna-cross-salvador-garcia-specials-question#100325) [ANK 20181016](https://www.vekn.net/forum/rules-questions/77075-sequencing-and-checking-for-triggers?start=6#91215) [ANK 20170625](https://www.vekn.net/forum/rules-questions/75929-khobar-towers-and-nocturns#82336) [ANK 20210110](https://www.vekn.net/forum/rules-questions/78984-first-tradition-the-masquerade-goes-first?start=6#101413) — {Jenna Cross}, {Judgment: Camarilla Segregation}, {Khobar Towers, Al-Khubar}, {First Tradition: The Masquerade}.
[^2-4-12]: [LSJ 20100203](https://groups.google.com/g/rec.games.trading-cards.jyhad/c/HQD-UNP7Y0s/m/cHxAnD8Z9dwJ) [ANK 20200905](https://www.vekn.net/forum/rules-questions/78836-visit-from-the-capuchin-vs-steelytenacity#100698) [ANK 20220503](https://www.vekn.net/forum/rules-questions/39040-re-ex-nihilo-can-i-choose-to-burn-my-minion#105161) [LSJ 20060530-1](https://groups.google.com/g/rec.games.trading-cards.jyhad/c/7ezcZoziFWw/m/bkivGTQIO3wJ) [LSJ 20090617-2](https://groups.google.com/g/rec.games.trading-cards.jyhad/c/ClO_zsSSgVU/m/TBaLfhQUN_8J) — {Slake the Thirst}, {Visit from the Capuchin}, {Drink the Blood of Ahriman}, {Zhenga}, {Ilomba}.
[^2-4-13]: [ANK 20180725](https://www.vekn.net/forum/rules-questions/76858-feline-saboteur-timing#89295) [LSJ 20050116](https://groups.google.com/g/rec.games.trading-cards.jyhad/c/yX5rqVaarvs/m/w6JXnFytdq4J) [ANK 20240724](https://www.vekn.net/forum/rules-questions/81635-erlik-and-illusions-of-the-kindred?start=6#112151) — {Feline Saboteur}, {Dual Form}, {Illusions of the Kindred}.
[^2-4-14]: [LSJ 20071003-2](https://groups.google.com/g/rec.games.trading-cards.jyhad/c/Tr9VQRVDbg0/m/EKNVTdvidvIJ) [ANK 20230816](https://www.vekn.net/forum/rules-questions/80772-heaven-s-gate-vs-charigger-the-axe#109057) — {Charigger, The Axe}, {Heaven's Gate}.
[^2-4-16]: [TOM 19951214-1](https://groups.google.com/g/rec.games.trading-cards.jyhad/c/8Fr6gioYZDI/m/p1eW5eaUMO0J) — {Sabbat Threat}.
[^2-4-17]: [LSJ 20080512](https://groups.google.com/g/rec.games.trading-cards.jyhad/c/z2DGSFph6sM/m/IjJB89nbtlsJ) — {Herald of Topheth}.
[^2-4-18]: [ANK 20210627](https://www.vekn.net/forum/rules-questions/79192-mirror-walk-and-slave?start=12#102578) [ANK 20211207](https://www.vekn.net/forum/rules-questions/79528-crypt-s-sons-versus-unleash-hell-s-fury?start=6#104139) [ANK 20220116](https://www.vekn.net/forum/rules-questions/79600-unleash-hell-s-fury-and-other-delayed-triggered-effects#104488) — {Unleash Hell's Fury}, {Millicent Smith, Puritan Vampire Hunter}, {Mirror Walk}, {Banshee Ironwail}.
[^2-4-19]: [PIB 20151009](https://www.vekn.net/forum/rules-questions/73577-baleful-doll#73580) [ANK 20180702](https://www.vekn.net/forum/rules-questions/76770-triggered-effects#88491) [RBK unlock-phase](https://www.vekn.net/rulebook#unlock-phase) — {Baleful Doll}, {Vampiric Disease}.
[^2-4-20]: [ANK 20200129](https://www.vekn.net/forum/rules-questions/78701-replace-during-unlock-and-other-unlock-effects#100210) [LSJ 20091208](https://groups.google.com/g/rec.games.trading-cards.jyhad/c/ptHbJM9MlVI/m/O61W2JkI_rIJ) [RTR 19951017](https://groups.google.com/g/rec.games.trading-cards.jyhad/c/ouhNUbHYg50/m/rco157ZHyqEJ) — group "Replace next turn" (G00025); {Port Authority}, {Malkavian Dementia}.
[^2-4-21]: [LSJ 20010121](https://boardgamegeek.com/thread/609699/article/6142361#6142361) [ANK 20200508-1](https://www.vekn.net/forum/rules-questions/78622-scourge-of-the-enochians-timing?start=12#99786) — {Fame}, {Scourge of the Enochians}.
[^2-4-22]: [ANK 20200123](https://www.vekn.net/forum/rules-questions/78373-theft-of-vitae-vs-theft-of-vitae#98717) [LSJ 20041027](https://groups.google.com/g/rec.games.trading-cards.jyhad/c/BHeGvhd4yEA/m/SdKih5fV34wJ) — {Theft of Vitae}.
[^2-4-23]: [ANK 20200702](https://www.vekn.net/forum/rules-questions/78711-deep-song-vs-obedience#100233) [ANK 20180627-2](https://www.vekn.net/forum/rules-questions/76756-flames-of-insurrection#88416) — {Deep Song}, {Flames of Insurrection}.
[^2-4-24]: [ANK 20170427](https://www.vekn.net/forum/rules-questions/75755-resolution-card-blood-of-acid?start=6#81627) [LSJ 20040805](https://groups.google.com/g/rec.games.trading-cards.jyhad/c/WuER8RUMzTE/m/OmQhmQFkFLkJ) [LSJ 20090528-1](https://groups.google.com/g/rec.games.trading-cards.jyhad/c/63JZWOiuAIQ/m/qx6_7pyDQEsJ) — {Blood of Acid}, {Blood Shield}.
[^2-5-1]: [LSJ 20060412](https://groups.google.com/g/rec.games.trading-cards.jyhad/c/DuZXjDEQ9cE/m/Q4MdfMG2eFUJ) [LSJ 20070217](https://groups.google.com/g/rec.games.trading-cards.jyhad/c/HkKuwBe9LRk/m/3GccpU4eaK8J) [LSJ 20010814-2](https://groups.google.com/g/rec.games.trading-cards.jyhad/c/8MR4bq0Cxj4/m/SH4dKuz8qO0J) [ANK 20181127](https://www.vekn.net/forum/rules-questions/77176-eagle-s-sight-and-guardian-vigil?start=6#92037) — {Cleave}, {Ensconced}, {Champion}, {Guardian Vigil}.
[^2-5-2]: [ANK 20191108](https://www.vekn.net/forum/rules-questions/78081-eyes-of-the-beast#97710) [LSJ 20100604-2](https://groups.google.com/g/rec.games.trading-cards.jyhad/c/Tr3X4DsZr-8/m/fF0rs8s_YYEJ) [LSJ 20100611](https://groups.google.com/g/rec.games.trading-cards.jyhad/c/Tr3X4DsZr-8/m/6XTlnrJSM8EJ) [LSJ 20050607-1](https://groups.google.com/g/rec.games.trading-cards.jyhad/c/vet0HGRxtXQ/m/gRJalPv4lLoJ) [LSJ 20080818](https://groups.google.com/g/rec.games.trading-cards.jyhad/c/O5HUPRkKY-k/m/IVBZIwrEtboJ) — {Eyes of the Beast}, {Marciana Giovanni, Investigator}, {Valerius Maior, Hell's Fool}, {Blessing of Chaos}.
[^2-5-3]: [LSJ 20070707](https://groups.google.com/g/rec.games.trading-cards.jyhad/c/ZtRk5z2TcoI/m/gJWD0dT3kUwJ) [RTR 20201130](https://www.blackchantry.com/2020/12/25/rtr-30-11-2020/) [ANK 20200415](https://www.vekn.net/forum/rules-questions/7516-re-derange-titles-and-bloodbrothers?start=6#99609) [ANK 20221208-2](https://www.vekn.net/forum/rules-questions/80200-malkavian-dementia?start=6#106953) [ANK 20221024](https://www.vekn.net/forum/rules-questions/80110-goth-band-and-leadership-vacuum#106640) — {Derange}, {Malkavian Dementia}, {Leadership Vacuum}.
[^2-5-4]: [ANK 20190416](https://www.vekn.net/forum/rules-questions/77560-conditional-intercepts#94528) [ANK 20180626-2](https://www.vekn.net/forum/rules-questions/76752-tygerius-allegiance-counters-and-going-anarch#88401) [ANK 20230103](https://www.vekn.net/forum/rules-questions/80237-victim-of-habit-subsequent-prey#107123) — {Teresita, The Godmother}, {Tegyrius, Vizier}, {Victim of Habit}.
[^2-5-5]: [LSJ 20090207](https://groups.google.com/g/rec.games.trading-cards.jyhad/c/0UGI9W2sSpk/m/An-ZYLIxAiwJ) [LSJ 20100212](https://groups.google.com/g/rec.games.trading-cards.jyhad/c/NIIFHQg_x1c/m/e5cReQuEqxYJ) [ANK 20171212](https://www.vekn.net/forum/rules-questions/76334-slave-mental-maze-interaction?start=12#84553) — {Concordance}, {Cry Wolf}, {Mental Maze}.
[^2-5-6]: [RTR 20070707](https://groups.google.com/g/rec.games.trading-cards.jyhad/c/vSOt2c1uRzQ/m/MsRAv47Cd4YJ) [LSJ 20070708](https://groups.google.com/g/rec.games.trading-cards.jyhad/c/vSOt2c1uRzQ/m/F4ZIvIyp7lcJ) [ANK 20190228](https://www.vekn.net/forum/rules-questions/77427-mata-hari-and-hakim-s-law-leadership?start=42#93785) [LSJ 20071109](https://groups.google.com/g/rec.games.trading-cards.jyhad/c/mXspOwNnPDc/m/UJAVuSqFBNoJ) — {Mata Hari}, {Philip van Vermeer IV}, {Tatiana Stepanova, Alastor}, {Petaniqua}.
[^2-5-7]: [LSJ 20030811](https://groups.google.com/g/rec.games.trading-cards.jyhad/c/Ivy3fm45bb4/m/7AYdBH7VI9QJ) [LSJ 19970814](https://groups.google.com/g/rec.games.trading-cards.jyhad/c/Xd6HOjnqBpw/m/_wNl-bMoKiAJ) — {Annabelle Triabell}, {Toreador Grand Ball}.
[^2-5-8]: [LSJ 20010616](https://groups.google.com/g/rec.games.trading-cards.jyhad/c/h7gnHNBFliE/m/MsfJ0qqv_jsJ) [LSJ 20030522-1](https://groups.google.com/g/rec.games.trading-cards.jyhad/c/_krZG-uPtzc/m/94US5l81edwJ) [LSJ 19970224](https://groups.google.com/g/rec.games.trading-cards.jyhad/c/80KRDjVFkyg/m/TBJso9Ra_9QJ) [LSJ 20071005-1](https://groups.google.com/g/rec.games.trading-cards.jyhad/c/Ugcdb0ljZrU/m/J3Gqxj_615gJ) [LSJ 20071206](https://groups.google.com/g/rec.games.trading-cards.jyhad/c/B-5oDAJrwiI/m/ui9coMgXYUMJ) [LSJ 20090725](https://groups.google.com/g/rec.games.trading-cards.jyhad/c/isG743Sws-8/m/cjTJkGtfl_gJ) — {Tegyrius, Vizier}, {Camarilla Vitae Slave}, {Agent of Power}, {The Eternal Mask}.
[^2-5-9]: [LSJ 20100206-2](https://groups.google.com/g/rec.games.trading-cards.jyhad/c/reXyybyIYX8/m/jeCyjdiZ5T4J) [LSJ 20080619](https://groups.google.com/g/rec.games.trading-cards.jyhad/c/-JNytF94ST8/m/jOxRkvh8RGwJ) [LSJ 20021008](https://groups.google.com/g/rec.games.trading-cards.jyhad/c/Mc3xfym_uw8/m/zY9ipcHSXF8J) [ANK 20180104](https://www.vekn.net/forum/rules-questions/76356-illusions-of-the-kindred-vs-outside-the-hourglass#84724) [ANK 20191218](https://www.vekn.net/forum/rules-questions/62700-re-nahir-and-research-counters?start=6#98297) — {Shatter the Gate}, {NRA PAC}, {The Meddling of Semsith}, {Illusions of the Kindred}, {Nahir}.
[^2-5-10]: [TOM 19960326](https://groups.google.com/g/rec.games.trading-cards.jyhad/c/8DA9p_p5v8s/m/lJlHFYXPTBYJ) [LSJ 20010610](https://groups.google.com/g/rec.games.trading-cards.jyhad/c/KVyVn-Y_UIY/m/FmhagXANIzcJ) [LSJ 20040210](https://groups.google.com/g/rec.games.trading-cards.jyhad/c/FWzKVXDEJ5k/m/ITxevWshkYIJ) — {Frenzy}, {Kraken's Kiss}, {Sire's Index Finger}.
[^2-5-11]: [LSJ 19980831](https://groups.google.com/g/rec.games.trading-cards.jyhad/c/Za8AS17xXPM/m/Ttki0DplaeYJ) [ANK 20191025](https://www.vekn.net/forum/rules-questions/78050-roetschreck-controler-is-ousted#97560) — {Rowan Ring}, {Wooden Stake}, {Rötschreck}.
[^2-5-12]: [LSJ 20001019](https://groups.google.com/g/rec.games.trading-cards.jyhad/c/bSH8Q_kDhNQ/m/eHEX6PmfaB0J) [ANK 20220525](https://www.vekn.net/forum/rules-questions/79777-lorenzo-detuono-and-imposing-phantasm#105316) [LSJ 20031106](https://groups.google.com/g/rec.games.trading-cards.jyhad/c/bFZCLXzzOeM/m/n1C6p6xw1O0J) — {Horrid Reality}, {Imposing Phantasm}, {Rutor's Hand}.
[^2-5-13]: [LSJ 20040726](https://groups.google.com/g/rec.games.trading-cards.jyhad/c/LlqCB6LN64g/m/k98Xj1pwjPcJ) [ANK 20200417](https://www.vekn.net/forum/rules-questions/78568-the-capuchin-burns-temporary-control?start=12#99616) [LSJ 20071014](https://groups.google.com/g/rec.games.trading-cards.jyhad/c/Bom6ae7qjbI/m/OznLIo66qgsJ) [LSJ 20051116-1](https://groups.google.com/g/rec.games.trading-cards.jyhad/c/MfGC7sJ8vh8/m/9ylhc34zFesJ) [LSJ 20081213-3](https://groups.google.com/g/rec.games.trading-cards.jyhad/c/cbZ2jl8-yGQ/m/OJljr9wcC4sJ) — {Possession}, {The Capuchin}, {Kaymakli Fragment}, {Demdemeh}.
[^2-5-14]: [PIB 20140122](https://www.vekn.net/forum/rules-questions/58586-banishment-and-master-discipline#58772) [TOM 19951209](https://groups.google.com/g/rec.games.trading-cards.jyhad/c/qP2j6CpBUDI/m/2qsG4E23bl4J) [LSJ 20010809-3](https://groups.google.com/g/rec.games.trading-cards.jyhad/c/gLl8F0zcCF0/m/cR8nsUweLQIJ) [LSJ 20010809-2](https://groups.google.com/g/rec.games.trading-cards.jyhad/c/9ggmJcK2De0/m/2xW0xE2SzisJ) [TOM 19960210](https://groups.google.com/g/rec.games.trading-cards.jyhad/c/PiOmH08RyVw/m/CqzTRcOLDNIJ) [RTR 20000501](https://groups.google.com/g/rec.games.trading-cards.jyhad/c/MKrA0hBXuaU/m/1M5LOLftKWAJ) [ANK 20210630](https://www.vekn.net/forum/rules-questions/79205-lay-low-vs-banishment#102601) [LSJ 20010211](https://groups.google.com/g/rec.games.trading-cards.jyhad/c/Fd9tcsKTzjE/m/dtIxb5Mof50J) [LSJ 20051103](https://groups.google.com/g/rec.games.trading-cards.jyhad/c/BD7KIWBI0Cs/m/g8vJICHAu7oJ) — {Banishment}, {Lay Low}, {Brainwash}, {Dual Form}.
[^3-1-1]: [RTR 20111202](https://www.vekn.net/forum/rules-questions/16769-rules-team-rulings-02-dec-11#16769) [RTR 19980928](https://groups.google.com/g/rec.games.trading-cards.jyhad/c/Xva4_IRavxM/m/F-_fjzTmo88J) — {Ravnos Carnival}, {Travis "Traveler72" Miller}, {Betrayer}.
[^3-1-5]: [LSJ 20081203](https://groups.google.com/g/rec.games.trading-cards.jyhad/c/gaskAJqA-mE/m/GpuegB2W0IgJ) [TOM 19960114](https://groups.google.com/g/rec.games.trading-cards.jyhad/c/cOqrGO0UrSw/m/5pDhn3YVyG4J) [LSJ 20020514](https://groups.google.com/g/rec.games.trading-cards.jyhad/c/xBDPee5wq40/m/WWX0GrKppzsJ) — {Revolutionary Council}, {Incriminating Videotape}.
[^3-1-6]: [ANK 20240706](https://www.vekn.net/forum/rules-questions/81563-break-the-bonds-presence-target?start=18#111945) [RTR 19970425](https://groups.google.com/g/rec.games.trading-cards.jyhad/c/DhP_l2cX3mQ/m/9ZZZqL8NFSAJ) — {Break the Bonds}, {Public Trust}, {Fire Dance}.
[^3-1-7]: [ANK 20240706](https://www.vekn.net/forum/rules-questions/81563-break-the-bonds-presence-target?start=18#111945) [LSJ 20080608](https://groups.google.com/g/rec.games.trading-cards.jyhad/c/j5ShUmUt-vM/m/E0CqmXp_R0IJ) [PIB 20110725](https://www.vekn.net/forum/rules-questions/6728-announcing-siphon#6740) — {Keystone Kine}, {The Platinum Protocol}, {Magic of the Smith}, {Siphon}.
[^3-1-8]: [LSJ 20041026](https://groups.google.com/g/rec.games.trading-cards.jyhad/c/54Zr4RUuVx8/m/fJCT8qW_90EJ) [ANK 20240706](https://www.vekn.net/forum/rules-questions/81563-break-the-bonds-presence-target?start=18#111945) — group "Justicar title vote without Camarilla" (G00034), {Break the Bonds}.
[^3-1-9]: [RTR 20010711](https://groups.google.com/g/rec.games.trading-cards.jyhad/c/GsI1UyH54jU/m/x9LfDZX1vR4J) [PIB 20110725](https://www.vekn.net/forum/rules-questions/6728-announcing-siphon#6740) [LSJ 20100216](https://groups.google.com/g/rec.games.trading-cards.jyhad/c/nrXTh1XKJJ8/m/KF7iiXQk3jsJ) [ANK 20180512-2](https://www.vekn.net/forum/rules-questions/76595-rules-team-rulings-rtr-11-05-2018?start=24#86823) — {Siphon}, {Villein}, {Diversion}, {Donnybrook}, {Drain Essence}.
[^3-1-10]: [RTR 20080808](https://groups.google.com/g/rec.games.trading-cards.jyhad/c/1jW6GXrIRSU/m/8QTYL98kB0gJ) — {Edged Illusion}, {Jaroslav Pascek}.
[^3-1-11]: [ANK 20180623](https://www.vekn.net/forum/rules-questions/76748-black-sunrise#88361) — {Second Tradition: Domain}, {Black Sunrise}, {Sense the Savage Way}.
[^3-1-12]: [LSJ 20031010](https://groups.google.com/g/rec.games.trading-cards.jyhad/c/clifT98_Zrk/m/aQ4cGuJnT9wJ) [LSJ 20090319](https://groups.google.com/g/rec.games.trading-cards.jyhad/c/G1w6TeymEnQ/m/QS78VbaUmgIJ) [ANK 20180907](https://www.vekn.net/forum/rules-questions/76983-secure-haven-target?start=6#90481) [LSJ 20051113](https://groups.google.com/g/rec.games.trading-cards.jyhad/c/L-ctaLucuKU/m/dG0EKdSd4g0J) [TOM 19951208-1](https://groups.google.com/g/rec.games.trading-cards.jyhad/c/tEHebi9BYfc/m/Q2zsWUbTURUJ) [LSJ 19980302-1](https://groups.google.com/g/rec.games.trading-cards.jyhad/c/kijV8VfB56s/m/_iWuwvavBGgJ) — {Secure Haven}, {Aye}.
[^3-1-13]: [PIB 20121028](https://www.vekn.net/forum/rules-questions/39816-ec-2012-can-you-answer-these?start=6#39843) — {Baltimore Purge}.
[^3-1-14]: [RBK who-may-attempt-to-block](https://www.vekn.net/rulebook#who-may-attempt-to-block) [LSJ 20090324](https://groups.google.com/g/rec.games.trading-cards.jyhad/c/Zc_ogoVhsug/m/tJ2VBYI7resJ) [ANK 20190606](https://www.vekn.net/forum/rules-questions/77692-of-noble-blood#95258) [PIB 20121210](https://www.vekn.net/forum/rules-questions/42498-does-eurayle-s-special-cost-her-blood-while-targeting-hazimel?start=18#42659) [PIB 20121028](https://www.vekn.net/forum/rules-questions/39816-ec-2012-can-you-answer-these?start=6#39843) [LSJ 20010328](https://groups.google.com/g/rec.games.trading-cards.jyhad/c/VMAMljUO4NE/m/BHgmaN_3HRkJ) [LSJ 20010828](https://groups.google.com/g/rec.games.trading-cards.jyhad/c/KoP_nqv-feM/m/faZPeRBTL_QJ) [ANK 20180917](https://www.vekn.net/forum/rules-questions/77011-condemn-the-sins-of-the-father#90639) — group "Directed at a card" (G00036), {Of Noble Blood}, {Renewed Vigor}, {Eurayle Gelasia Mylonas}, {Mylan Horseed}, {Lunatic Eruption}, {Temptation}, {Impundulu}.
[^3-1-15]: [LSJ 20090324](https://groups.google.com/g/rec.games.trading-cards.jyhad/c/Zc_ogoVhsug/m/tJ2VBYI7resJ) [RBK who-may-attempt-to-block](https://www.vekn.net/rulebook#who-may-attempt-to-block) [LSJ 19970224](https://groups.google.com/g/rec.games.trading-cards.jyhad/c/80KRDjVFkyg/m/TBJso9Ra_9QJ) — {Conceal}, {Haunt}, {Goblinism}, group "Locquipments" (G00047), {Annazir}, {Arcanum Investigator}, {Gremlins}, {Loss}, {Principia Discordia}, {Ethan Locke}.
[^3-1-16]: [LSJ 20061222](https://groups.google.com/g/rec.games.trading-cards.jyhad/c/WUKedBpp_h0/m/LpJkrGZWvg0J) [LSJ 20090324](https://groups.google.com/g/rec.games.trading-cards.jyhad/c/Zc_ogoVhsug/m/tJ2VBYI7resJ) [LSJ 20030214-2](https://groups.google.com/g/rec.games.trading-cards.jyhad/c/nU7PaMBymtY/m/ELcjZX2caJUJ) — {Abbot}, {Detect Authority}, {Ambrosio Luis Monçada, Plenipotentiary}, {Evan Klein}.
[^3-1-17]: [LSJ 20010627](https://groups.google.com/g/rec.games.trading-cards.jyhad/c/NhNCVCCDyU0/m/I5Yph3-UUPsJ) [ANK 20221019-3](https://www.vekn.net/forum/rules-questions/21158-re-secure-haven-banishment?start=6#106615) — {Daemonic Possession}, {The Eternal Mask}, {Ghost-Eater}, {Khazar's Diary (Endless Night)}, {Pressing Flesh}, {Banishment}.
[^3-1-18]: [PIB 20150821](https://www.vekn.net/forum/rules-questions/72609-sowing-dissension?start=6#72632) [RTR 20080808](https://groups.google.com/g/rec.games.trading-cards.jyhad/c/1jW6GXrIRSU/m/8QTYL98kB0gJ) [RTR 20081119](https://www.vekn.net/card-lists/140-keepers-of-tradition) [ANK 20180917](https://www.vekn.net/forum/rules-questions/77011-condemn-the-sins-of-the-father#90639) [LSJ 20080809-1](https://groups.google.com/g/rec.games.trading-cards.jyhad/c/1jW6GXrIRSU/m/7ywPFR39rb4J) — {Sowing Dissension}, {Condemn the Sins of the Father}, {Shepherd's Innocence}, {Wave of Insanity}.
[^3-1-19]: [LSJ 20080809-2](https://groups.google.com/g/rec.games.trading-cards.jyhad/c/1jW6GXrIRSU/m/6SpheeDqQeUJ) [RTR 20081119](https://www.vekn.net/card-lists/140-keepers-of-tradition) [RTR 20080808](https://groups.google.com/g/rec.games.trading-cards.jyhad/c/1jW6GXrIRSU/m/8QTYL98kB0gJ) [ANK 20180515](https://www.vekn.net/forum/rules-questions/76612-weigh-the-heart-and-mulible-targets#86920) — {Chanjelin Ward}, {Talley, The Hound}, {Weigh the Heart}.
[^3-2-1]: [TOM 19951109](https://groups.google.com/g/rec.games.trading-cards.jyhad/c/WhJj5K1Fa-0/m/m673ruvTozEJ) [LSJ 20060409](https://groups.google.com/g/rec.games.trading-cards.jyhad/c/gsFQXsCGTG4/m/q5H8FvuKksIJ) [ANK 20200329](https://www.vekn.net/forum/rules-questions/78546-familial-bond#99451) [LSJ 20020814](https://groups.google.com/g/rec.games.trading-cards.jyhad/c/gt8wQhk76lA/m/qjDJXRLxM7cJ) [ANK 20221229](https://www.vekn.net/forum/rules-questions/80231-clarifications-on-osric-vladislav-s-wording#107109) — {Bonding}, {Mask of a Thousand Faces}, {Familial Bond}, {Osric Vladislav}.
[^3-2-2]: [RBK wording-templates](https://www.vekn.net/rulebook#wording-templates) [RBK who-may-attempt-to-block](https://www.vekn.net/rulebook#who-may-attempt-to-block) [LSJ 20010111](https://groups.google.com/g/rec.games.trading-cards.jyhad/c/d3WSV1UXBV0/m/gvRQWzPxOzEJ) [LSJ 20100329](https://groups.google.com/g/rec.games.trading-cards.jyhad/c/1SAloV6P7Xk/m/p96tZsTI9SsJ) [PIB 20150216](https://www.vekn.net/forum/rules-questions/57153-can-you-untap-an-untapped-vampire-minion?start=6#69272) — {Angelica, The Canonicus}, {Phased Motion Detector}, {Under Siege}.
[^3-2-3]: [RTR 20030519](https://groups.google.com/g/rec.games.trading-cards.jyhad/c/NOBWXWrd-vA/m/iEOpQp1uhvAJ) [LSJ 20021211](https://groups.google.com/g/rec.games.trading-cards.jyhad/c/-J07wvmidOA/m/gPQ5ngEZ6HcJ) — {Draba}, {Night Terrors}.
[^3-2-4]: [LSJ 20011214-2](https://groups.google.com/g/rec.games.trading-cards.jyhad/c/TinQ8ywzIHU/m/-zW_hcYbiD4J) — {Repulsion}.
[^3-2-5]: [RBK stealth-and-intercept](https://www.vekn.net/rulebook#stealth-and-intercept) [LSJ 20100604-2](https://groups.google.com/g/rec.games.trading-cards.jyhad/c/Tr3X4DsZr-8/m/fF0rs8s_YYEJ) [LSJ 20100611](https://groups.google.com/g/rec.games.trading-cards.jyhad/c/Tr3X4DsZr-8/m/6XTlnrJSM8EJ) — {Marciana Giovanni, Investigator}.
[^3-2-6]: [LSJ 20100527](https://groups.google.com/g/rec.games.trading-cards.jyhad/c/Tr3X4DsZr-8/m/O06iXN6LtzsJ) [LSJ 20010813-2](https://groups.google.com/g/rec.games.trading-cards.jyhad/c/zkKhvgZy9hA/m/8uH5sgbQaSoJ) [ANK 20211112-2](https://www.vekn.net/forum/rules-questions/79478-unleash-hell-s-fury-and-extra-intercept#103870) — {Marciana Giovanni, Investigator}, {Unleash Hell's Fury}.
[^3-2-7]: [RTR 20080808](https://groups.google.com/g/rec.games.trading-cards.jyhad/c/1jW6GXrIRSU/m/8QTYL98kB0gJ) [RTR 20081119](https://www.vekn.net/card-lists/140-keepers-of-tradition) [LSJ 20061222](https://groups.google.com/g/rec.games.trading-cards.jyhad/c/WUKedBpp_h0/m/LpJkrGZWvg0J) [ANK 20190416](https://www.vekn.net/forum/rules-questions/77560-conditional-intercepts#94528) — {Talley, The Hound}, {Abbot}, {Ministry}, {Protection Racket}, {Teresita, The Godmother}.
[^3-2-8]: [LSJ 19990425](https://groups.google.com/g/rec.games.trading-cards.jyhad/c/Mmfn07ib6Yw/m/YfwpUlqEdrEJ) [ANK 20200515](https://www.vekn.net/forum/rules-questions/78634-blanket-of-night#99838) — {Cloak the Gathering}.
[^3-2-9]: [ANK 20180926](https://www.vekn.net/forum/rules-questions/77030-is-guardian-vigil-playable-after-the-block-succeeds#90768) [ANK 20210926](https://www.vekn.net/forum/rules-questions/79337-eluding-the-arms-of-morpheus-after-block-declare?start=18#103333) [ANK 20211003](https://www.vekn.net/forum/rules-questions/79372-fail-to-block-and-telepathic-misdirection#103416) — {Guardian Vigil}, {Inspire Greatness}, {Deflection}, {My Enemy's Enemy}, {Redirection}.
[^3-2-10]: [RBK wording-templates](https://www.vekn.net/rulebook#wording-templates) [ANK 20230116](https://www.vekn.net/forum/rules-questions/80266-confirmation-needed-about-phased-motion-detector#107207) [ANK 20180307-2](https://www.vekn.net/forum/rules-questions/76451-ellison-humboldt-and-matteus-flesh-sculptor?start=0#85598) [LSJ 20011023-2](https://groups.google.com/g/rec.games.trading-cards.jyhad/c/47-PhTMiAOU/m/g4sVfXt9TmsJ) — {Phased Motion Detector}, {Matteus, Flesh Sculptor}, {Starshell Grenade Launcher}.
[^3-3-1]: [RTR 19950413](https://groups.google.com/g/rec.games.trading-cards.jyhad/c/zB2vyPBnO6g/m/i1myM9tD54AJ) [RTR 20020501](https://groups.google.com/g/rec.games.trading-cards.jyhad/c/M1snoR2msbQ/m/RFwCmX3anDkJ) [LSJ 20020112](https://groups.google.com/g/rec.games.trading-cards.jyhad/c/9yhb-ToEzL8/m/Eq59W8cS65YJ) [LSJ 20041203](https://groups.google.com/g/rec.games.trading-cards.jyhad/c/_iogrCkrCmc/m/hTkREMXGFR0J) [LSJ 20050224-1](https://groups.google.com/g/rec.games.trading-cards.jyhad/c/enxwleC-ZKw/m/zDDSPMF8FOYJ) — {Eagle's Sight}, {Falcon's Eye}, {Anneke}, {Sonja Blue}.
[^3-3-2]: [LSJ 20030227](https://groups.google.com/g/rec.games.trading-cards.jyhad/c/c9KLhUd-Isg/m/Zz0zAzvZ8TYJ) — {Eagle's Sight}.
[^3-3-3]: [LSJ 20010714-2](https://groups.google.com/g/rec.games.trading-cards.jyhad/c/9U-jt3p3R_Q/m/WxDJwkgc25kJ) — {Guard Duty}, {Second Tradition: Domain}, {Black Sunrise}, and the same wording on eight further cards.
[^3-3-4]: [ANK 20180623](https://www.vekn.net/forum/rules-questions/76748-black-sunrise#88361) — {Guard Duty}, {Trophy: Domain}, {Under Siege}.
[^3-3-5]: [ANK 20181122-2](https://www.vekn.net/forum/rules-questions/77176-eagle-s-sight-and-guardian-vigil#91965) — {Second Tradition: Domain}, {Guardian Vigil}, {The Mole}.
[^3-3-6]: [LSJ 20090514](https://groups.google.com/g/rec.games.trading-cards.jyhad/c/PKQ6lQUBUOI/m/Zra43F1WXGcJ) — {Guard Duty}, {Coterie Tactics}, {Eternal Vigilance}.
[^3-3-7]: [ANK 20200607](https://www.vekn.net/forum/rules-questions/78676-draba-timing#100043) [LSJ 20100507](https://groups.google.com/g/rec.games.trading-cards.jyhad/c/vJQTPYtp-Eg/m/6_nkxd28-v8J) [PIB 20150820](https://www.vekn.net/forum/rules-questions/72462-hide-the-heart-timing-questions#72626) [ANK 20210131-1](https://www.vekn.net/forum/rules-questions/79007-netwar-timing#101527) [RBK sequencing](https://www.vekn.net/rulebook#sequencing) — {Hide the Heart}, {Draba}, {Netwar}, {Folderol}.
[^3-3-8]: [LSJ 20000507](https://groups.google.com/g/rec.games.trading-cards.jyhad/c/6-sMg4Wo7KE/m/s0fQkYbR5_QJ) [ANK 20211003](https://www.vekn.net/forum/rules-questions/79372-fail-to-block-and-telepathic-misdirection#103416) — {Archon Investigation}, {Deflection}, {Telepathic Misdirection}.
[^3-3-9]: [TOM 19951129](https://groups.google.com/g/rec.games.trading-cards.jyhad/c/jjBzopH-yrQ/m/L51mbZ5KGLkJ) — {Wake with Evening's Freshness}, {Eyes of Argus}, {Forced Awakening}.
[^3-3-10]: [LSJ 20081202](https://groups.google.com/g/rec.games.trading-cards.jyhad/c/GMxeDWiDXP8/m/twr__FgYvmMJ) [LSJ 19990106](https://groups.google.com/g/rec.games.trading-cards.jyhad/c/tJR6Hw6CmBQ/m/1Jgm5AT7rNMJ) — {Faceless Night}, {Mask of a Thousand Faces}.
[^3-3-11]: [LSJ 20031121-2](https://groups.google.com/g/rec.games.trading-cards.jyhad/c/1khXmKPU0ws/m/Je_X4gvv72kJ) — {Tenebrous Form}.
[^3-3-12]: [TOM 19951007](https://groups.google.com/g/rec.games.trading-cards.jyhad/c/HUipqz0LFSw/m/pY6uEa3f8-gJ) [LSJ 19991025](https://groups.google.com/g/rec.games.trading-cards.jyhad/c/R94tyTGJ6VQ/m/KxvkGm1aon8J) [LSJ 20080326](https://groups.google.com/g/rec.games.trading-cards.jyhad/c/KUQEznVQlOU/m/e_6GMg__zdMJ) — {Alexandra}, {Temptation}.
[^3-3-13]: [PIB 20150501](https://www.vekn.net/forum/rules-questions/70780-change-of-control-during-the-action?start=6#70800) [LSJ 20020725](https://groups.google.com/g/rec.games.trading-cards.jyhad/c/wCPFIH_g5ZE/m/inchZQXKRrsJ) [ANK 20220127](https://www.vekn.net/forum/rules-questions/79615-burn-counter-to-gain-control-of-steal-a-minion#104588) — {Temptation}, {Revelation of Despair}.
[^3-3-14]: [RTR 19950906](https://groups.google.com/g/rec.games.trading-cards.jyhad/c/P4uSsWk4jj8/m/ZepBwGus2VcJ) [ANK 20200714](https://www.vekn.net/forum/rules-questions/78742-ohoyo-hopoksia#100352) — {Brujah Frenzy}, {Ohoyo Hopoksia (Bastet)}.
[^3-3-15]: [ANK 20230226](https://www.vekn.net/forum/rules-questions/31040-unleash-hells-fury-vs-burn-x-blood-to-attempt-to-block?start=6#107484) — {Unleash Hell's Fury}.
[^3-3-16]: [LSJ 19970707](https://groups.google.com/g/rec.games.trading-cards.jyhad/c/KWekwiRSa2I/m/9pS17rzBBDYJ) [TOM 19951215-1](https://groups.google.com/g/rec.games.trading-cards.jyhad/c/mLnhwWDRglQ/m/0Ghd3eyRaFQJ) [RTR 19960530](https://groups.google.com/g/rec.games.trading-cards.jyhad/c/DpvF2Peet9o/m/dJwiudauzEwJ) — {Sabbat Priest}, {Camarilla Exemplary}, {Archon}, {Dónal O'Connor}.
[^3-3-17]: [LSJ 20050607-1](https://groups.google.com/g/rec.games.trading-cards.jyhad/c/vet0HGRxtXQ/m/gRJalPv4lLoJ) [LSJ 20080818](https://groups.google.com/g/rec.games.trading-cards.jyhad/c/O5HUPRkKY-k/m/IVBZIwrEtboJ) [LSJ 20090810](https://groups.google.com/g/rec.games.trading-cards.jyhad/c/g3ukXdsh8xo/m/0qTp2vtFVz8J) [LSJ 20100305](https://groups.google.com/g/rec.games.trading-cards.jyhad/c/gyDkgm2qXMs/m/j_7nZNsJTrgJ) — {Blessing of Chaos}, {Valerius Maior, Hell's Fool}, {No Secrets From the Magaji}, {Libertas}.
[^3-3-18]: [LSJ 19980224](https://groups.google.com/g/rec.games.trading-cards.jyhad/c/xV22ImgKblY/m/FECdNXgf5s4J) [RTR 19991206](https://groups.google.com/g/rec.games.trading-cards.jyhad/c/N7iEmqgP9WU/m/gX80TroOBsUJ) [ANK 20180321](https://www.vekn.net/forum/rules-questions/76378-clan-loyalty?start=12#85923) [LSJ 20060410](https://groups.google.com/g/rec.games.trading-cards.jyhad/c/jr8wSeSchsc/m/xIIeqsJxHrIJ) [ANK 20171017](https://www.vekn.net/forum/rules-questions/76233-question-about-failing-to-block-faceless-night-and-playing-guard-dogs#83900) [ANK 20230305](https://www.vekn.net/forum/rules-questions/63821-re-faceless-night-x-deflection?start=36#107536) [RBK resolve-the-action](https://www.vekn.net/rulebook#resolve-the-action) — {Change of Target}, {Clan Loyalty}, {Angel of Berlin}, {Faceless Night}.
[^3-3-19]: [RTR 19991206](https://groups.google.com/g/rec.games.trading-cards.jyhad/c/N7iEmqgP9WU/m/gX80TroOBsUJ) [LSJ 20091125](https://groups.google.com/g/rec.games.trading-cards.jyhad/c/1dYtrdRjRI8/m/Iz5qzFYoboQJ) [RTR 20080808](https://groups.google.com/g/rec.games.trading-cards.jyhad/c/1jW6GXrIRSU/m/8QTYL98kB0gJ) — {Aching Beauty}, {Change of Target}, {Lesser Boon}.
[^3-3-20]: [TOM 19951208-2](https://groups.google.com/g/rec.games.trading-cards.jyhad/c/UqLxnP1C_Wg/m/yZRM6DLarm4J) [RTR 20080808](https://groups.google.com/g/rec.games.trading-cards.jyhad/c/1jW6GXrIRSU/m/8QTYL98kB0gJ) — {Spiritual Protector}, {Lesser Boon}.
[^3-3-21]: [ANK 20210627](https://www.vekn.net/forum/rules-questions/79192-mirror-walk-and-slave?start=12#102578) [ANK 20211207](https://www.vekn.net/forum/rules-questions/79528-crypt-s-sons-versus-unleash-hell-s-fury?start=6#104139) [ANK 20220116](https://www.vekn.net/forum/rules-questions/79600-unleash-hell-s-fury-and-other-delayed-triggered-effects#104488) [ANK 20190524](https://www.vekn.net/forum/rules-questions/77659-venenation-change-of-target-and-psychomachia#95070) [LSJ 20020126](https://groups.google.com/g/rec.games.trading-cards.jyhad/c/Fhm2Zi2RZRU/m/K4FiHLWuSbMJ) — {Banshee Ironwail}, {Unleash Hell's Fury}, {Millicent Smith, Puritan Vampire Hunter}, {Venenation}.
[^3-3-22]: [LSJ 20010813](https://groups.google.com/g/rec.games.trading-cards.jyhad/c/8MR4bq0Cxj4/m/f_rAOuj3CboJ) [LSJ 20010819-2](https://groups.google.com/g/rec.games.trading-cards.jyhad/c/8MR4bq0Cxj4/m/YgNsk8nGcREJ) — {Guard Dogs}, {Guardian Vigil}, {Precognition}.
[^3-3-23]: [ANK 20190116](https://www.vekn.net/forum/rules-questions/77302-strike-combat-ends-continue-with-the-action#92916) [RTR 19941109](https://groups.google.com/d/msg/rec.games.deckmaster/_6CXoKTSLnw/FdG67-3HEAQJ) — {Those Who Endure Judge}.
[^3-4-1]: [LSJ 20070411](https://groups.google.com/g/rec.games.trading-cards.jyhad/c/umdINigMKqs/m/l6GFRVKdkMsJ) [LSJ 20090514](https://groups.google.com/g/rec.games.trading-cards.jyhad/c/PKQ6lQUBUOI/m/Zra43F1WXGcJ) [PIB 20121031](https://www.vekn.net/forum/rules-questions/39816-ec-2012-can-you-answer-these?start=18#39908) [ANK 20220218](https://www.vekn.net/forum/rules-questions/79001-the-question-of-the-month-action-fizzles?start=12#104697) [ANK 20181107](https://www.vekn.net/forum/rules-questions/77152-warsaw-station-vs-diablerie#91708) [LSJ 20020725](https://groups.google.com/g/rec.games.trading-cards.jyhad/c/wCPFIH_g5ZE/m/inchZQXKRrsJ) — {Ambush}, {Harass}, {Spirit Marionette}, {Warsaw Station}, {Temptation}, and the further cards carrying the same three templates.
[^3-4-3]: [LSJ 20090514](https://groups.google.com/g/rec.games.trading-cards.jyhad/c/PKQ6lQUBUOI/m/Zra43F1WXGcJ) — {Coterie Tactics}, {Eternal Vigilance}.
[^3-4-4]: [LSJ 20070411](https://groups.google.com/g/rec.games.trading-cards.jyhad/c/umdINigMKqs/m/l6GFRVKdkMsJ) [LSJ 20030519](https://groups.google.com/g/rec.games.trading-cards.jyhad/c/E6Jz8m3iKrA/m/BoCMzQoGzyQJ) [RTR 19980623](https://groups.google.com/g/rec.games.trading-cards.jyhad/c/tSpd9dtTElc/m/-CuHJF54_n0J) [LSJ 20011222](https://groups.google.com/g/rec.games.trading-cards.jyhad/c/DlCBJmB2fzY/m/HVLdn4Hr9uIJ) [ANK 20221028-2](https://www.vekn.net/forum/rules-questions/80122-the-shard-london-and-sargon#106673) — {Forced March}, {Freak Drive}, {Instantaneous Transformation}, {CrimethInc.}, {Perfectionist}, {Hrothulf}, {Tereza Rostas}, {Sargon}.
[^3-4-5]: [LSJ 20090411](https://groups.google.com/g/rec.games.trading-cards.jyhad/c/2aJf9bN7ZGc/m/YRt70QmwFLkJ) — {Abactor}.
[^3-4-6]: [LSJ 20050720-2](https://groups.google.com/g/rec.games.trading-cards.jyhad/c/1vbIkgvKDJ0/m/3ErIIMXFgPIJ) [LSJ 20050727](https://groups.google.com/g/rec.games.trading-cards.jyhad/c/QfVIg4fJP38/m/wMJU5oik9G8J) — {Hospital Food}, {The Anarch Free Press}, {Hunger Moon}, {Thirst}, and the ten further cards carrying the same hunt ruling.
[^3-4-7]: [RTR 20080808](https://groups.google.com/g/rec.games.trading-cards.jyhad/c/1jW6GXrIRSU/m/8QTYL98kB0gJ) [LSJ 20100527](https://groups.google.com/g/rec.games.trading-cards.jyhad/c/Tr3X4DsZr-8/m/O06iXN6LtzsJ) — {Edged Illusion}, {Jaroslav Pascek}, {Enticement}.
[^3-4-8]: [LSJ 20090323](https://groups.google.com/g/rec.games.trading-cards.jyhad/c/bG4PSmditm4/m/wR15DaRI8KUJ) [RBK wording-templates](https://www.vekn.net/rulebook#wording-templates) — {Veil of Darkness}.
[^3-4-9]: [ANK 20240706](https://www.vekn.net/forum/rules-questions/81563-break-the-bonds-presence-target?start=18#111945) [LSJ 20080608](https://groups.google.com/g/rec.games.trading-cards.jyhad/c/j5ShUmUt-vM/m/E0CqmXp_R0IJ) [PIB 20150418](https://www.vekn.net/forum/rules-questions/70589-bima#70591) [ANK 20170226](https://www.vekn.net/forum/rules-questions/75625-dual-form-extra-disciplines#80868) — {The Platinum Protocol}, {Third Tradition: Progeny}, {Dual Form}.
[^3-4-10]: [TOM 19951107](https://groups.google.com/g/rec.games.trading-cards.jyhad/c/lb3GhBTmgpM/m/x6qb8MwfFnAJ) [PIB 20121031](https://www.vekn.net/forum/rules-questions/39816-ec-2012-can-you-answer-these?start=18#39908) — {Magic of the Smith}, {Vast Wealth}, {Tryphosa}.
[^3-4-11]: [ANK 20220331](https://www.vekn.net/forum/rules-questions/79720-daring-the-dawn-and-mirror-walk#104919) [ANK 20210124](https://www.vekn.net/forum/rules-questions/79001-the-question-of-the-month-action-fizzles#101492) [LSJ 20020927](https://groups.google.com/g/rec.games.trading-cards.jyhad/c/wg3PH7vOs1s/m/gYFNbAwk84gJ) [LSJ 20021115](https://groups.google.com/g/rec.games.trading-cards.jyhad/c/35vszszGZOA/m/GXrurZ9Rw-oJ) [ANK 20221011-2](https://www.vekn.net/forum/rules-questions/79984-force-of-wil-and-daring-the-dawn-vs-red-herring#106538) [LSJ 20100301](https://groups.google.com/g/rec.games.trading-cards.jyhad/c/TcUDpHnvW8M/m/YznjkbV3JLoJ) [ANK 20220116](https://www.vekn.net/forum/rules-questions/79600-unleash-hell-s-fury-and-other-delayed-triggered-effects#104488) — {Daring the Dawn}, {Force of Will}, {Unleash Hell's Fury}.
[^3-4-12]: [ANK 20200221](https://www.vekn.net/forum/rules-questions/78458-strix-daring-the-dawn-and-much-more#99036) — {Strix}.
[^3-4-13]: [LSJ 20110502](https://boardgamegeek.com/thread/648695/article/6701545) [LSJ 20081123](https://groups.google.com/g/rec.games.trading-cards.jyhad/c/_Pb29pBJ1kU/m/8ugWH0lVOtoJ) [LSJ 20050422](https://groups.google.com/g/rec.games.trading-cards.jyhad/c/nJPfMOuTBtw/m/COytKb_oEM4J) [LSJ 20090205](https://groups.google.com/g/rec.games.trading-cards.jyhad/c/l5bUtHOejmc/m/Ksw_nyldc3QJ) — {Spying Mission}, {Andre LeRoux}, {Dis Pater}, {Major Boon}.
[^3-4-14]: [LSJ 19980105](https://groups.google.com/g/rec.games.trading-cards.jyhad/c/PzVC-AeFuUQ/m/ncbtQyYNpFQJ) [TOM 19960303](https://groups.google.com/g/rec.games.trading-cards.jyhad/c/SEU6ztVpR94/m/F8NmjGw8ml8J) [LSJ 20061212](https://groups.google.com/g/rec.games.trading-cards.jyhad/c/h3onVZ1NqpQ/m/JYIxdaT9wMEJ) — {My Enemy's Enemy}, {Redirection}, {Telepathic Misdirection}, {Telepathic Counter}, {Spying Mission}.
[^3-4-15]: [PIB 20150612](https://www.vekn.net/forum/rules-questions/71660-andre-leroux-spying-mission#71685) — {Andre LeRoux}, {Spying Mission}.
[^3-5-1]: [RTR 20180719](https://www.blackchantry.com/2018/07/18/rules-team-rulings-rtr-19-07-2018/) [ANK 20211015](https://www.vekn.net/forum/rules-questions/79389-when-does-nra-apply-not-apply?start=6#103563) [LSJ 20070709](https://groups.google.com/g/rec.games.trading-cards.jyhad/c/qKrJPLXBFFw/m/hE5z511E_PgJ) [RTR 20020501](https://groups.google.com/g/rec.games.trading-cards.jyhad/c/M1snoR2msbQ/m/RFwCmX3anDkJ) [ANK 20221011-2](https://www.vekn.net/forum/rules-questions/79984-force-of-wil-and-daring-the-dawn-vs-red-herring#106538) [LSJ 20011202-2](https://groups.google.com/g/rec.games.trading-cards.jyhad/c/qnVBhys6loo/m/5IuE9b3iTyoJ) [LSJ 20091224](https://groups.google.com/g/rec.games.trading-cards.jyhad/c/AV34Lb49JlE/m/WoKnfq6qCuwJ) [LSJ 20070214-2](https://groups.google.com/g/rec.games.trading-cards.jyhad/c/C_QjWH6VIh4/m/LGMpWNyO_e4J) — {Change of Target}, {Champion}, {Krassimir}, {Obedience}, {Red Herring}, {Secret Passage}, {Black Forest Base}, and sixteen further cards carrying the identical "has reached resolution" template.
[^3-5-2]: [LSJ 19980212](https://groups.google.com/g/rec.games.trading-cards.jyhad/c/fLFLlXZXHqA/m/ggjw8aGjdRoJ) [RBK cancel-a-card](https://www.vekn.net/rulebook#cancel-a-card) [LSJ 20060425](https://groups.google.com/g/rec.games.trading-cards.jyhad/c/U34QDob4Vco/m/hcaMIn9W88kJ) [ANK 20220411](https://www.vekn.net/forum/rules-questions/79730-dabbler-and-direct-intervention#104995) [LSJ 20050607](https://groups.google.com/g/rec.games.trading-cards.jyhad/c/WLv9R8wA0Ow/m/gQyOMb3fEKQJ) [LSJ 20050608](https://groups.google.com/g/rec.games.trading-cards.jyhad/c/WLv9R8wA0Ow/m/dyAPpxSMoSYJ) — group "Cancel an action" (G00061), {React with Conviction}, {Dabbler}, {Spying Mission}.
[^3-5-3]: [ANK 20211015](https://www.vekn.net/forum/rules-questions/79389-when-does-nra-apply-not-apply?start=6#103563) [ANK 20210124](https://www.vekn.net/forum/rules-questions/79001-the-question-of-the-month-action-fizzles#101492) [LSJ 20090220](https://groups.google.com/g/rec.games.trading-cards.jyhad/c/JMgZa9jdrc4/m/kdM4QIf5LE0J) [LSJ 20070709](https://groups.google.com/g/rec.games.trading-cards.jyhad/c/qKrJPLXBFFw/m/hE5z511E_PgJ) — {The Kiss of Ra}, {Tangle Atropos' Hand}.
[^3-5-4]: [ANK 20210124](https://www.vekn.net/forum/rules-questions/79001-the-question-of-the-month-action-fizzles#101492) — {The Kiss of Ra}, {Tangle Atropos' Hand}, {Veil the Legions}.
[^3-5-5]: [LSJ 20090208](https://groups.google.com/g/rec.games.trading-cards.jyhad/c/07gUFmSeIxU/m/yIrwcMsATB4J) [LSJ 20070222-1](https://groups.google.com/g/rec.games.trading-cards.jyhad/c/jBrfK77gayo/m/fnk0EgSpN8AJ) [ANK 20221102](https://www.vekn.net/forum/rules-questions/80129-fall-of-london-card-rules-questions#106688) — {Enrage}, {React with Conviction}, {Mobile HQ, Operation Antigen}.
[^3-5-6]: [LSJ 20081213-1](https://groups.google.com/g/rec.games.trading-cards.jyhad/c/MNmJu12AU8I/m/Pol1P9fWMmoJ) [ANK 20210124](https://www.vekn.net/forum/rules-questions/79001-the-question-of-the-month-action-fizzles#101492) — {Enkil Cog}.
[^3-5-7]: [LSJ 20060522](https://groups.google.com/g/rec.games.trading-cards.jyhad/c/2f0wF9CECu8/m/SZn9iGo-LOQJ) [LSJ 20060824](https://groups.google.com/g/rec.games.trading-cards.jyhad/c/zsZTYTbRVRI/m/VmMfnKWuMlMJ) [LSJ 20080725](https://groups.google.com/g/rec.games.trading-cards.jyhad/c/jWWCwKnran0/m/6JxzHnKdJkkJ) [LSJ 20090617](https://groups.google.com/g/rec.games.trading-cards.jyhad/c/OMTF0_ZqUL0/m/ijdnbYacuNkJ) — {Change of Target}, {Obedience}, {Red Herring}.
[^3-5-8]: [RTR 19950509](https://groups.google.com/g/rec.games.trading-cards.jyhad/c/_LKyR7pdMig/m/ZvwdGmIwUnsJ) [LSJ 20080710](https://groups.google.com/g/rec.games.trading-cards.jyhad/c/f1NpGhdtk-E/m/MEbLGzSGessJ) [ANK 20200502](https://www.vekn.net/forum/rules-questions/78616-change-of-target-equip-from-a-minion#99734) — {Change of Target}, {Obedience}, {Red Herring}.
[^3-5-9]: [LSJ 20080725](https://groups.google.com/g/rec.games.trading-cards.jyhad/c/jWWCwKnran0/m/6JxzHnKdJkkJ) — {Change of Target}, {Obedience}, {Red Herring}.
[^3-5-10]: [LSJ 20011023](https://groups.google.com/g/rec.games.trading-cards.jyhad/c/2GOLIrXAF8M/m/P4T3Dj6UNL0J) [RTR 20020501](https://groups.google.com/g/rec.games.trading-cards.jyhad/c/M1snoR2msbQ/m/RFwCmX3anDkJ) — {Malleable Visage}.
[^3-5-11]: [LSJ 20010627](https://groups.google.com/g/rec.games.trading-cards.jyhad/c/NhNCVCCDyU0/m/I5Yph3-UUPsJ) [LSJ 20100213](https://groups.google.com/g/rec.games.trading-cards.jyhad/c/vXDkYrTmkws/m/sKy3jXz7AB4J) — {Compel the Spirit}, {Soul Gem of Etrius}.
[^3-5-12]: [LSJ 20080815](https://groups.google.com/g/rec.games.trading-cards.jyhad/c/0_1JBbdwi74/m/c1GepnS4ylEJ) [ANK 20180817](https://www.vekn.net/forum/rules-questions/76933-cock-robin-jack-of-both-sides#90064) [ANK 20220910](https://www.vekn.net/forum/rules-questions/80021-clandestine-contrac-x-forced-march-freak#106314) — {Piper}, {Muricia's Call}, {Clandestine Contract}.
[^3-5-13]: [RTR 20180719](https://www.blackchantry.com/2018/07/18/rules-team-rulings-rtr-19-07-2018/) [ANK 20200207](https://www.vekn.net/forum/rules-questions/78423-mental-maze-and-obedience#98906) [LSJ 20010803-1](https://groups.google.com/g/rec.games.trading-cards.jyhad/c/5QuGIF5ERUI/m/nGJoAyeiOJQJ) [ANK 20170105](https://www.vekn.net/forum/rules-questions/75512-raptor-obedience#80020) [ANK 20210627](https://www.vekn.net/forum/rules-questions/79192-mirror-walk-and-slave?start=12#102578) [ANK 20211207](https://www.vekn.net/forum/rules-questions/79528-crypt-s-sons-versus-unleash-hell-s-fury?start=6#104139) [ANK 20220116](https://www.vekn.net/forum/rules-questions/79600-unleash-hell-s-fury-and-other-delayed-triggered-effects#104488) [TOM 19960303](https://groups.google.com/g/rec.games.trading-cards.jyhad/c/SEU6ztVpR94/m/F8NmjGw8ml8J) — {Mirror Walk}, {Tangle Atropos' Hand}, {Change of Target}, {Obedience}, {The Kiss of Ra}, {Spying Mission}, and eleven further cards carrying the identical "ends unsuccessfully immediately" template.
[^3-5-14]: [LSJ 20010806-2](https://groups.google.com/g/rec.games.trading-cards.jyhad/c/5QuGIF5ERUI/m/3iHzZVBOjG4J) [TOM 19950829](https://groups.google.com/g/rec.games.trading-cards.jyhad/c/iVm2VboVp6Q/m/fbsieL8XHQwJ) — {Blood Brother Ambush}, {Brujah Frenzy}.
[^3-5-15]: [LSJ 20041022](https://groups.google.com/g/rec.games.trading-cards.jyhad/c/gqhND6kd2wE/m/LDmEotxa_4kJ) [RTR 20180719](https://www.blackchantry.com/2018/07/18/rules-team-rulings-rtr-19-07-2018/) [ANK 20220118](https://www.vekn.net/forum/rules-questions/79389-when-does-nra-apply-not-apply?start=6#104506) [ANK 20221205](https://www.vekn.net/forum/rules-questions/80196-clarification-regarding-detect-authority#106923) — {Detect Authority}, {Mistaken Identity}, {Scobax}, {Unseen Hibernation}, {Car Bomb}, {Champion}, {Hide the Heart}, {Malkavian Derangement: Alternate Personality}.
[^3-5-16]: [LSJ 20070219](https://groups.google.com/g/rec.games.trading-cards.jyhad/c/HkKuwBe9LRk/m/RGUse0Ow8L4J) — {Champion}.
[^3-5-17]: [ANK 20200702](https://www.vekn.net/forum/rules-questions/78711-deep-song-vs-obedience#100233) [LSJ 20090826](https://groups.google.com/g/rec.games.trading-cards.jyhad/c/KTwa1Hf_gHI/m/IlgyfFaqqeEJ) [LSJ 20060902](https://groups.google.com/g/rec.games.trading-cards.jyhad/c/QAKz6Qtr7Ts/m/JpnA6qgxS2oJ) [LSJ 20090325-1](https://groups.google.com/g/rec.games.trading-cards.jyhad/c/5CW9tD5OfGk/m/nydaMm7gqNsJ) [ANK 20220218](https://www.vekn.net/forum/rules-questions/79001-the-question-of-the-month-action-fizzles?start=12#104697) [LSJ 20090325-2](https://groups.google.com/g/rec.games.trading-cards.jyhad/c/5CW9tD5OfGk/m/wzlh-bhnTQcJ) — {Deep Song}, {Siren's Lure}, {Yawp Court}, {Warsaw Station}.
[^3-5-18]: [ANK 20220331](https://www.vekn.net/forum/rules-questions/79720-daring-the-dawn-and-mirror-walk#104919) [ANK 20210124](https://www.vekn.net/forum/rules-questions/79001-the-question-of-the-month-action-fizzles#101492) [LSJ 20020927](https://groups.google.com/g/rec.games.trading-cards.jyhad/c/wg3PH7vOs1s/m/gYFNbAwk84gJ) [LSJ 20021115](https://groups.google.com/g/rec.games.trading-cards.jyhad/c/35vszszGZOA/m/GXrurZ9Rw-oJ) [ANK 20221011-2](https://www.vekn.net/forum/rules-questions/79984-force-of-wil-and-daring-the-dawn-vs-red-herring#106538) [ANK 20220401](https://www.vekn.net/forum/rules-questions/79720-daring-the-dawn-and-mirror-walk?start=6#104927) [ANK 20211015](https://www.vekn.net/forum/rules-questions/79389-when-does-nra-apply-not-apply?start=6#103563) [RTR 19980623](https://groups.google.com/g/rec.games.trading-cards.jyhad/c/tSpd9dtTElc/m/-CuHJF54_n0J) — {Daring the Dawn}, {Force of Will}.
[^3-5-19]: [RTR 19991206](https://groups.google.com/g/rec.games.trading-cards.jyhad/c/N7iEmqgP9WU/m/gX80TroOBsUJ) [LSJ 20091125](https://groups.google.com/g/rec.games.trading-cards.jyhad/c/1dYtrdRjRI8/m/Iz5qzFYoboQJ) [LSJ 20100301](https://groups.google.com/g/rec.games.trading-cards.jyhad/c/TcUDpHnvW8M/m/YznjkbV3JLoJ) [ANK 20220116](https://www.vekn.net/forum/rules-questions/79600-unleash-hell-s-fury-and-other-delayed-triggered-effects#104488) — {Aching Beauty}, {Unleash Hell's Fury}.
[^3-5-20]: [LSJ 20110419](https://boardgamegeek.com/thread/643948) — {Crocodile's Tongue} (ruling removed from the database in 2024; original at boardgamegeek.com thread 643948, database wording relied on).
[^3-5-21]: [LSJ 20090322](https://groups.google.com/g/rec.games.trading-cards.jyhad/c/tROpvfFdgBI/m/qDwA9JTPMxgJ) [ANK 20181003](https://www.vekn.net/forum/rules-questions/77036-continuing-an-action-after-stealing-with-venenation#90942) [LSJ 20010803-2](https://groups.google.com/g/rec.games.trading-cards.jyhad/c/s1lJEsLMf-8/m/3CwIMglRboIJ) [ANK 20220127](https://www.vekn.net/forum/rules-questions/79615-burn-counter-to-gain-control-of-steal-a-minion#104588) [LSJ 20080611](https://groups.google.com/g/rec.games.trading-cards.jyhad/c/gvb3uijtpZw/m/ZRX2hunjsRYJ) [ANK 20210131](https://www.vekn.net/forum/rules-questions/79008-crypt-s-sons-lock-and-obedience#101525) — {Bear-Baiting}, {Venenation}, {Crypt's Sons}.
[^3-5-22]: [LSJ 20070309-2](https://groups.google.com/g/rec.games.trading-cards.jyhad/c/c3Kx0-C_5JU/m/CRscFEQfeC0J) [RBK cancel-a-card](https://www.vekn.net/rulebook#cancel-a-card) — {Wash}.
[^3-5-23]: [LSJ 20030224](https://groups.google.com/g/rec.games.trading-cards.jyhad/c/67261v339Ds/m/um8V7VVp2Y4J) — group "Cancel" (G00058).
[^3-5-24]: [RBK cancel-a-card](https://www.vekn.net/rulebook#cancel-a-card) [LSJ 20090818](https://groups.google.com/g/rec.games.trading-cards.jyhad/c/jkKBGVLmFHc/m/YXwYthjI7isJ) — {Supernatural Resistance}.
[^3-5-25]: [ANK 20200813-2](https://www.vekn.net/forum/rules-questions/78799-rewind-time-inf-and-action-cards#100526) — group "Cancel an action" (G00061), {React with Conviction}.
[^3-5-26]: [RTR 20001020](https://groups.google.com/g/rec.games.trading-cards.jyhad/c/GvxNYsYsWJ4/m/EY7NOjdsGCsJ) [ANK 20201229](https://www.vekn.net/forum/rules-questions/78959-louhi-and-piper#101325) — group "Cancel an action" (G00061), {Sudden Reversal}, {Asguresh}, {The Summoning}.
[^3-6-1]: [LSJ 20070808-1](https://groups.google.com/g/rec.games.trading-cards.jyhad/c/jzMOxZ9oxOs/m/o0X7GUFmii0J) — {Form of Mist}, {Mirror Image}, {Shadow Body}, and twelve further cards carrying the same wording.
[^3-6-2]: [RTR 19941109](https://groups.google.com/d/msg/rec.games.deckmaster/_6CXoKTSLnw/FdG67-3HEAQJ) [LSJ 20080611](https://groups.google.com/g/rec.games.trading-cards.jyhad/c/gvb3uijtpZw/m/ZRX2hunjsRYJ) [ANK 20190116](https://www.vekn.net/forum/rules-questions/77302-strike-combat-ends-continue-with-the-action#92916) — {Form of Mist}, {Crypt's Sons}, {Momentary Delay}, and thirteen further cards carrying the same wording.
[^3-6-3]: [ANK 20190116](https://www.vekn.net/forum/rules-questions/77302-strike-combat-ends-continue-with-the-action#92916) [ANK 20191108](https://www.vekn.net/forum/rules-questions/78081-eyes-of-the-beast#97710) [RBK summary-of-the-course-of-an-action](https://www.vekn.net/rulebook#summary-of-the-course-of-an-action) — {Form of Mist}, {Mirror Image}, {Wamukota} (and thirteen further cards); {Eyes of the Beast}.
[^3-6-4]: [ANK 20230319](https://www.vekn.net/forum/rules-questions/80393-forced-awakening-and-wmrh-talk-radio-vs-form-of-mist#107674) [LSJ 20070417](https://groups.google.com/g/rec.games.trading-cards.jyhad/c/ecDUqbSUsNg/m/3W9aOm0MfYEJ) — {Forced Awakening}, {WMRH Talk Radio}.
[^3-6-5]: [LSJ 20030227](https://groups.google.com/g/rec.games.trading-cards.jyhad/c/c9KLhUd-Isg/m/Zz0zAzvZ8TYJ) [LSJ 20010814-2](https://groups.google.com/g/rec.games.trading-cards.jyhad/c/8MR4bq0Cxj4/m/SH4dKuz8qO0J) [ANK 20181127](https://www.vekn.net/forum/rules-questions/77176-eagle-s-sight-and-guardian-vigil?start=6#92037) — {Eagle's Sight}, {Falcon's Eye}, {Guardian Vigil}.
[^3-6-6]: [RTR 19970630](https://groups.google.com/g/rec.games.trading-cards.jyhad/c/KireUeOYY3c/m/t6ifm9lur1kJ) — {Form of Mist}, {Chameleon's Colors}, {Torrent}, and nine further cards carrying the same wording.
[^3-6-7]: [LSJ 19980109](https://groups.google.com/g/rec.games.trading-cards.jyhad/c/d2U51Uw0Hfg/m/uIPoVvPFePgJ) [RTR 20020501](https://groups.google.com/g/rec.games.trading-cards.jyhad/c/M1snoR2msbQ/m/RFwCmX3anDkJ) [LSJ 20031123](https://groups.google.com/g/rec.games.trading-cards.jyhad/c/HvM2cHJ6yIo/m/jsb4iRoNdWkJ) — {Form of Mist}, {Fast Reaction}, {Akram}, and seven further cards carrying the same wording.
[^3-6-8]: [LSJ 20021213](https://groups.google.com/g/rec.games.trading-cards.jyhad/c/Puk_eXStfE8/m/jBRJ7bleXP4J) — {Psyche!}.
[^3-6-9]: [LSJ 20090322](https://groups.google.com/g/rec.games.trading-cards.jyhad/c/tROpvfFdgBI/m/qDwA9JTPMxgJ) [LSJ 20010803-2](https://groups.google.com/g/rec.games.trading-cards.jyhad/c/s1lJEsLMf-8/m/3CwIMglRboIJ) [ANK 20181003](https://www.vekn.net/forum/rules-questions/77036-continuing-an-action-after-stealing-with-venenation#90942) [ANK 20220127](https://www.vekn.net/forum/rules-questions/79615-burn-counter-to-gain-control-of-steal-a-minion#104588) — {Bear-Baiting}, {Venenation}.
[^3-6-10]: [LSJ 20010813](https://groups.google.com/g/rec.games.trading-cards.jyhad/c/8MR4bq0Cxj4/m/f_rAOuj3CboJ) [LSJ 20010819-2](https://groups.google.com/g/rec.games.trading-cards.jyhad/c/8MR4bq0Cxj4/m/YgNsk8nGcREJ) — {Guard Dogs}, {Night Terrors}, {One With the Land}, and seven further cards carrying the same wording.
[^3-6-11]: [LSJ 20010814-2](https://groups.google.com/g/rec.games.trading-cards.jyhad/c/8MR4bq0Cxj4/m/SH4dKuz8qO0J) — {Precognition}, {Instinctive Reaction}, {Form of the Bat}, and seven further cards carrying the same wording.
[^3-7-1-1]: [LSJ 20100218](https://groups.google.com/g/rec.games.trading-cards.jyhad/c/x-uJChHi76Y/m/F92fWI7WwaEJ) [RTR 20180511-2](https://www.vekn.net/forum/rules-questions/76595-rules-team-rulings-rtr-11-05-2018?start=30#86840) — {Command of the Beast}, {Power of One}, {Divine Image}, {Leverage}, {Quicksilver Contemplation}.
[^3-7-1-2]: [PIB 20110817](https://www.vekn.net/forum/rules-questions/8405-foreshadowing-destruction-is-usable-at-dom-vs-10-pool#8414) [RTR 20191031](https://www.vekn.net/2-uncategorised/465-vampire-elder-kindred-network-newsletter-october-2019) [ANK 20211019-2](https://www.vekn.net/forum/rules-questions/79390-sup-foreshadoing-destruction-when-the-target-has-10-or-more-pool?start=6#103593) — {Foreshadowing Destruction}.
[^3-7-1-3]: [LSJ 19970718](https://groups.google.com/g/rec.games.trading-cards.jyhad/c/QujjxfQHYzw/m/S4tNTm4gpi8J) — {Pentex(TM) Loves You!}.
[^3-7-1-4]: [ANK 20171023](https://www.vekn.net/forum/rules-questions/76252-power-of-one#83985) [RTR 19941109](https://groups.google.com/d/msg/rec.games.deckmaster/_6CXoKTSLnw/FdG67-3HEAQJ) [ANK 20220502](https://www.vekn.net/forum/rules-questions/79757-haqim-s-law-retribution-and-anu-diptinatpa#105140) — {Confusion}, {Power of One}, {Haqim's Law: Retribution}, {Anu Diptinatpa}.
[^3-7-1-5]: [RTR 19980623](https://groups.google.com/g/rec.games.trading-cards.jyhad/c/tSpd9dtTElc/m/-CuHJF54_n0J) — {Justicar Retribution}.
[^3-7-1-6]: [PIB 20150612](https://www.vekn.net/forum/rules-questions/71660-andre-leroux-spying-mission#71685) [LSJ 20030701-1](https://groups.google.com/g/rec.games.trading-cards.jyhad/c/8pVaGxWYeyA/m/hDIxE9ipPCgJ) — {Andre LeRoux}, {Protected Resources}.
[^3-7-1-7]: [TOM 19960413](https://groups.google.com/g/rec.games.trading-cards.jyhad/c/Gm-NLCP6bF0/m/sVxss5F1bBYJ) [LSJ 20030211](https://groups.google.com/g/rec.games.trading-cards.jyhad/c/xhpVMShX6qc/m/6KDcgiFIxhMJ) — {Protected Resources}.
[^3-7-1-8]: [RTR 19960530](https://groups.google.com/g/rec.games.trading-cards.jyhad/c/DpvF2Peet9o/m/dJwiudauzEwJ) — {Elder Intervention}.
[^3-7-1-9]: [RTR 19950622](https://groups.google.com/g/rec.games.trading-cards.jyhad/c/86Y38Vps-7E/m/BPIFvB_eLzQJ) [PIB 20130711](https://www.vekn.net/forum/rules-questions/51279-big-boon-bounce?fbclid=IwAR3-kLQKFt415mAPpGL0sYpi4yx6ZzJbiyP57z3R6nkIW7V-g0F93z_ob-s#51307) — {Deflection}, {Minor Boon}.
[^3-7-1-10]: [LSJ 20010621](https://groups.google.com/g/rec.games.trading-cards.jyhad/c/VTHXJOrxlP4/m/be0uDkX78NwJ) [LSJ 20010830](https://groups.google.com/g/rec.games.trading-cards.jyhad/c/pWNZjWmtCk0/m/yV-5T_pUB3oJ) — {Perfect Clarity}.
[^3-7-1-11]: [LSJ 19980105](https://groups.google.com/g/rec.games.trading-cards.jyhad/c/PzVC-AeFuUQ/m/ncbtQyYNpFQJ) — {Deflection}.
[^3-7-2-1]: [LSJ 20050720-2](https://groups.google.com/g/rec.games.trading-cards.jyhad/c/1vbIkgvKDJ0/m/3ErIIMXFgPIJ) [LSJ 20050727](https://groups.google.com/g/rec.games.trading-cards.jyhad/c/QfVIg4fJP38/m/wMJU5oik9G8J) — {Hunger Moon}, {Thirst}, {Tainted Vitae}, and eleven further cards carrying the same ruling.
[^3-7-2-2]: [TOM 19951212-3](https://groups.google.com/g/rec.games.trading-cards.jyhad/c/cYwUsviEhr4/m/J_ijOFuOK1IJ) — {Triole's Revenge}.
[^3-7-2-3]: [LSJ 20060306](https://groups.google.com/g/rec.games.trading-cards.jyhad/c/H-W0Wqx3t9w/m/jgTHm_Ac8dwJ) [ANK 20180202](https://www.vekn.net/forum/rules-questions/76402-pariah-vulture-s-buffet#85206) [RTR 20030519](https://groups.google.com/g/rec.games.trading-cards.jyhad/c/NOBWXWrd-vA/m/iEOpQp1uhvAJ) [RTR 20180511](https://www.vekn.net/forum/rules-questions/76595-rules-team-rulings-rtr-11-05-2018#86780) — group "Hunt bonus" (G00004), {Pariah}, group "Special Hunt action" (G00064).
[^3-7-2-4]: [PIB 20150820-2](https://www.vekn.net/forum/rules-questions/72575-hunt-actions#72623) [PIB 20120204](https://www.vekn.net/forum/rules-questions/22233-strained-vitae-supply-vs-lokis-gift#22343) — {Igo the Hungry}, {Strained Vitae Supply}.
[^3-7-2-5]: [RTR 20030519](https://groups.google.com/g/rec.games.trading-cards.jyhad/c/NOBWXWrd-vA/m/iEOpQp1uhvAJ) [RTR 20180511](https://www.vekn.net/forum/rules-questions/76595-rules-team-rulings-rtr-11-05-2018#86780) — groups "Hunt bonus" (G00004) and "Steal blood as a Hunt action" (G00121); {Festivo dello Estinto}, {Inbase Discotek, Frankfurt} (bank-blood riders printed on the cards).
[^3-7-2-6]: [LSJ 20090606](https://groups.google.com/g/rec.games.trading-cards.jyhad/c/-hy9E1u2t_o/m/CPU8rltzhesJ) [ANK 20190707](https://www.vekn.net/forum/rules-questions/77694-ok-a-new-round-of-doubts-for-a-noobie#95274) — {Legacy of Caine}, {Week of Nightmares}, {Kyoko Shinsegawa}.
[^3-7-2-7]: [RTR 20010711](https://groups.google.com/g/rec.games.trading-cards.jyhad/c/GsI1UyH54jU/m/x9LfDZX1vR4J) [LSJ 19970224](https://groups.google.com/g/rec.games.trading-cards.jyhad/c/80KRDjVFkyg/m/TBJso9Ra_9QJ) [LSJ 20100915](https://groups.google.com/g/rec.games.trading-cards.jyhad/c/lFLocuKV8NI/m/TcAPvYUfrWcJ) — {Week of Nightmares}, {Legacy of Caine}, {Kyoko Shinsegawa}.
[^3-7-2-8]: [LSJ 20010809-1](https://groups.google.com/g/rec.games.trading-cards.jyhad/c/LB6Zg4bEggc/m/g5eYOHiKrvUJ) — {Legacy of Caine}.
[^3-7-2-9]: [ANK 20220809](https://www.vekn.net/forum/rules-questions/79949-loki-s-gift-hunt-bonus#105914) — {Loki's Gift}.
[^3-7-2-10]: [LSJ 20050331](https://groups.google.com/g/rec.games.trading-cards.jyhad/c/J0CgOqvbfEk/m/P1VelhBkcr8J) [LSJ 20081213-2](https://groups.google.com/g/rec.games.trading-cards.jyhad/c/0Yf2s-qrWpM/m/0u8svYOAZ3cJ) [RBK hunt](https://www.vekn.net/rulebook#hunt) — {Rabbat, The Sewer Goddess}, {Undying Thirst}.
[^3-7-3-1]: [TOM 19960130](https://groups.google.com/g/rec.games.trading-cards.jyhad/c/wF82VdVPlm0/m/MmFo2E7lrY8J) [LSJ 20050313](https://groups.google.com/g/rec.games.trading-cards.jyhad/c/eSShNquHnXI/m/4H7zIau2DjoJ) [ANK 20230408](https://www.vekn.net/forum/rules-questions/80438-the-british-museum-london-bloodstone#107810) — {Magic of the Smith}, {Bloodstone}, {Jack of Both Sides}, {Children of Stone}, {Sleight of Hand}, {Lambach}.
[^3-7-3-2]: [PIB 20150105-2](https://www.vekn.net/forum/rules-questions/68482-topaz-successfully-equips-baby-yaga-successfully-employs#68483) [LSJ 20100421](https://groups.google.com/g/rec.games.trading-cards.jyhad/c/Vp--M79gpqk/m/mah3wmaFYREJ) — {Topaz}, {Synner-G}, {Vulture}, {Dagger}.
[^3-7-3-3]: [LSJ 20090506](https://groups.google.com/g/rec.games.trading-cards.jyhad/c/887DQTpntKI/m/L-ETC1-5nR0J) — {Incriminating Videotape}, {Mokolé Blood}, {Shilmulo Tarot}.
[^3-7-3-4]: [LSJ 20060209](https://groups.google.com/g/rec.games.trading-cards.jyhad/c/ZuOfZorIhhU/m/X5G1JfqDPhcJ) [ANK 20221103](https://www.vekn.net/forum/rules-questions/80131-can-a-flaming-candle-be-moved-by-a-heidelberg-castle-germany#106697) [ANK 20210109](https://www.vekn.net/forum/rules-questions/78983-fear-of-mekhet-and-torpor#101392) — {Flaming Candle}, {Fear of Mekhet}.
[^3-7-3-5]: [LSJ 20050315](https://groups.google.com/g/rec.games.trading-cards.jyhad/c/COcJX2hHP-E/m/YLUW8FaGP0kJ) [LSJ 20050413-1](https://groups.google.com/g/rec.games.trading-cards.jyhad/c/1TXRhYopt70/m/OZMBb0AlfOUJ) [LSJ 20050413-2](https://groups.google.com/g/rec.games.trading-cards.jyhad/c/1TXRhYopt70/m/YnL8Fiaim0IJ) [LSJ 20020211](https://groups.google.com/g/rec.games.trading-cards.jyhad/c/ubqDaLeG3qo/m/TGKL07dP8NkJ) [LSJ 20060221](https://groups.google.com/g/rec.games.trading-cards.jyhad/c/OC41YQYfJO4/m/g_y0RPVpXNkJ) — {Enkidu, The Noah}, {Beast, The Leatherface of Detroit}, {Helen Fairchild}, {Lorrie Dunsirn}, {Reg Driscoll}.
[^3-7-3-6]: [LSJ 20060222](https://groups.google.com/g/rec.games.trading-cards.jyhad/c/Gv-gf5sAJxM/m/4scio5aXDCkJ) [ANK 20170326](https://www.vekn.net/forum/rules-questions/75635-transferring-weapons-and-gift-of-bellona#81215) — {Unlicensed Taxicab}, {Gift of Bellona}.
[^3-7-3-7]: [RTR 19950509](https://groups.google.com/g/rec.games.trading-cards.jyhad/c/_LKyR7pdMig/m/ZvwdGmIwUnsJ) [LSJ 20080710](https://groups.google.com/g/rec.games.trading-cards.jyhad/c/f1NpGhdtk-E/m/MEbLGzSGessJ) [ANK 20200502](https://www.vekn.net/forum/rules-questions/78616-change-of-target-equip-from-a-minion#99734) — {Change of Target}, {Obedience}, {Red Herring}.
[^3-7-3-8]: [LSJ 20050315](https://groups.google.com/g/rec.games.trading-cards.jyhad/c/COcJX2hHP-E/m/YLUW8FaGP0kJ) [LSJ 20010210](https://groups.google.com/g/rec.games.trading-cards.jyhad/c/NtMa5w_NVOE/m/jtpqcS6CwpIJ) [LSJ 19980206](https://groups.google.com/g/rec.games.trading-cards.jyhad/c/p_uyqQgE9Ms/m/86kfy6jI0lUJ) [TOM 19950407](https://groups.google.com/g/rec.games.trading-cards.jyhad/c/FWVnIu3zLAQ/m/ODGlyMGc_hgJ) — {Beast, The Leatherface of Detroit}, {Enkidu, The Noah}, {Howler}, {Lucian}, {Vast Wealth}.
[^3-7-3-9]: [LSJ 20061218](https://groups.google.com/g/rec.games.trading-cards.jyhad/c/DTBI6LkPdZ4/m/Qtu3QUPERdIJ) [LSJ 20080619](https://groups.google.com/g/rec.games.trading-cards.jyhad/c/-JNytF94ST8/m/jOxRkvh8RGwJ) — {NRA PAC}.
[^3-7-4-1]: [LSJ 20100303](https://groups.google.com/g/rec.games.trading-cards.jyhad/c/jmmm0WRUPvs/m/x9pv1OmWFS4J) [ANK 20180817](https://www.vekn.net/forum/rules-questions/76933-cock-robin-jack-of-both-sides#90064) [LSJ 20100725](https://groups.google.com/g/rec.games.trading-cards.jyhad/c/9d1zMZfsfNo/m/l3fbDtbr9xwJ) [LSJ 20030520-2](https://groups.google.com/g/rec.games.trading-cards.jyhad/c/GcymCHOJDVY/m/bM6Z5o-beQgJ) [RBK employ-retainer](https://www.vekn.net/rulebook#employ-retainer) [RBK recruit-ally](https://www.vekn.net/rulebook#recruit-ally) — {Muricia's Call}, {The Summoning}, {Ghouled}.
[^3-7-4-2]: [TOM 19960130](https://groups.google.com/g/rec.games.trading-cards.jyhad/c/wF82VdVPlm0/m/MmFo2E7lrY8J) [LSJ 20050315](https://groups.google.com/g/rec.games.trading-cards.jyhad/c/COcJX2hHP-E/m/YLUW8FaGP0kJ) [LSJ 20010210](https://groups.google.com/g/rec.games.trading-cards.jyhad/c/NtMa5w_NVOE/m/jtpqcS6CwpIJ) [ANK 20200813-2](https://www.vekn.net/forum/rules-questions/78799-rewind-time-inf-and-action-cards#100526) — {Jack of Both Sides}, {Beast, The Leatherface of Detroit}, {Angelo}, {Lorrie Dunsirn}, group "Cancel an action" (G00061).
[^3-7-4-3]: [LSJ 20100204](https://groups.google.com/g/rec.games.trading-cards.jyhad/c/o5Xnzc8G774/m/yovVizGngKsJ) [LSJ 20080803](https://groups.google.com/g/rec.games.trading-cards.jyhad/c/VgARso4nY7w/m/cAl0o7WpblAJ) [RBK employ-retainer](https://www.vekn.net/rulebook#employ-retainer) [RBK recruit-ally](https://www.vekn.net/rulebook#recruit-ally) — {Summon History}, {Piper}.
[^3-7-4-4]: [LSJ 20090115-1](https://groups.google.com/g/rec.games.trading-cards.jyhad/c/RQ3ARP9Kvfk/m/dBN_M7SnIHAJ) [ANK 20170309](https://www.vekn.net/forum/rules-questions/75649-reduce-ally-cost-and-piper-combo#81049) [LSJ 20060616-2](https://groups.google.com/g/rec.games.trading-cards.jyhad/c/YGA7bnOj04Y/m/wOVi6CvB8Z0J) — {Piper}, {Zhenga}, {Web of Knives Recruit}.
[^3-7-4-5]: [ANK 20210928](https://www.vekn.net/forum/rules-questions/79364-combo-piper-x-soul-of-earth#103363) [ANK 20210913](https://www.vekn.net/forum/rules-questions/79322-piper-and-sebastien-goulet#103113) [LSJ 20090116](https://groups.google.com/g/rec.games.trading-cards.jyhad/c/RQ3ARP9Kvfk/m/e-o1t79x1gUJ) [PIB 20150105-2](https://www.vekn.net/forum/rules-questions/68482-topaz-successfully-equips-baby-yaga-successfully-employs#68483) — {Soul of the Earth}, {Little Tailor of Prague}, {Kuyén}, {Baba Yaga, the Iron Hag}.
[^3-7-4-6]: [ANK 20201229](https://www.vekn.net/forum/rules-questions/78959-louhi-and-piper#101325) [LSJ 20060530-2](https://groups.google.com/g/rec.games.trading-cards.jyhad/c/7ezcZoziFWw/m/G07cu5_UZnQJ) — {Piper}, {Zhenga}.
[^3-7-4-7]: [LSJ 20080815](https://groups.google.com/g/rec.games.trading-cards.jyhad/c/0_1JBbdwi74/m/c1GepnS4ylEJ) [ANK 20180817](https://www.vekn.net/forum/rules-questions/76933-cock-robin-jack-of-both-sides#90064) — {Piper}, {Muricia's Call}, {The Summoning}.
[^3-7-4-8]: [LSJ 20070707](https://groups.google.com/g/rec.games.trading-cards.jyhad/c/ZtRk5z2TcoI/m/gJWD0dT3kUwJ) — {Corrupt Construction}.
[^3-7-4-9]: [ANK 20180517](https://www.vekn.net/forum/rules-questions/76447-rules-team-rulings-rtr-03-03-2018?start=30#87041) — {Rom Gypsy}, {Underbridge Stray}, {War Ghoul} (and nine further cards on the same ruling).
[^3-7-5-1]: [LSJ 20100112](https://groups.google.com/g/rec.games.trading-cards.jyhad/c/SJu0kgw_2tE/m/p5cshF90vkEJ) [PIB 20121028](https://www.vekn.net/forum/rules-questions/39816-ec-2012-can-you-answer-these?start=6#39843) [LSJ 20011222](https://groups.google.com/g/rec.games.trading-cards.jyhad/c/DlCBJmB2fzY/m/HVLdn4Hr9uIJ) [ANK 20221028-2](https://www.vekn.net/forum/rules-questions/80122-the-shard-london-and-sargon#106673) [RBK politics](https://www.vekn.net/rulebook#politics) — {Abactor}, {Sargon}.
[^3-7-5-2]: [RTR 19951110](https://groups.google.com/g/rec.games.trading-cards.jyhad/c/TXfganI5B2o/m/QYh3AdPNbUwJ) — {Voter Captivation}.
[^3-7-5-3]: [LSJ 20060902](https://groups.google.com/g/rec.games.trading-cards.jyhad/c/QAKz6Qtr7Ts/m/JpnA6qgxS2oJ) [LSJ 20090325-1](https://groups.google.com/g/rec.games.trading-cards.jyhad/c/5CW9tD5OfGk/m/nydaMm7gqNsJ) [ANK 20180910-1](https://www.vekn.net/forum/rules-questions/76990-correct-order-impulse-for-combat-cards-after-combat#90517) [LSJ 20060903](https://groups.google.com/g/rec.games.trading-cards.jyhad/c/QAKz6Qtr7Ts/m/kyhzKIdtR54J) — {Yawp Court}.
[^3-7-5-4]: [LSJ 20081202-2](https://groups.google.com/g/rec.games.trading-cards.jyhad/c/hlK89M1M9rk/m/k2mbokPTCccJ) [LSJ 19980130](https://groups.google.com/g/rec.games.trading-cards.jyhad/c/mtjOAd7aaYI/m/XZq9o1cUd-8J) [RTR 19951110](https://groups.google.com/g/rec.games.trading-cards.jyhad/c/TXfganI5B2o/m/QYh3AdPNbUwJ) — {Veles' Hunt}, {Bernard, the Scourge}, {Delaying Tactics}, {Telepathic Vote Counting}, {Scorn of Adonis}.
[^3-7-5-5]: [RTR 20040501](https://groups.google.com/g/rec.games.trading-cards.jyhad/c/7-mp3Ada86I/m/yenQ7FZ-VMIJ) [RBK politics](https://www.vekn.net/rulebook#politics) — {Business Pressure}.
[^3-7-5-6]: [LSJ 20081203](https://groups.google.com/g/rec.games.trading-cards.jyhad/c/gaskAJqA-mE/m/GpuegB2W0IgJ) [LSJ 20041004](https://groups.google.com/g/rec.games.trading-cards.jyhad/c/UZbyxuVsTJE/m/47dqvgl6t2QJ) [RTR 19941109](https://groups.google.com/d/msg/rec.games.deckmaster/_6CXoKTSLnw/FdG67-3HEAQJ) — {Revolutionary Council}, {Parity Shift}, {Domain Challenge}.
[^3-7-5-7]: [LSJ 20010606](https://groups.google.com/g/rec.games.trading-cards.jyhad/c/2Dj_N6wtifI/m/j_bddYqDbOYJ) [LSJ 20040518](https://groups.google.com/g/rec.games.trading-cards.jyhad/c/4emymfUPwAM/m/B2SCC7L6kuMJ) — {Parity Shift}, {Alastor}.
[^3-7-5-8]: [RTR 20010710](https://groups.google.com/g/rec.games.trading-cards.jyhad/c/GsI1UyH54jU/m/x9LfDZX1vR4J) — {Peace Treaty}.
[^3-7-5-9]: [RTR 19960530](https://groups.google.com/g/rec.games.trading-cards.jyhad/c/DpvF2Peet9o/m/dJwiudauzEwJ) [LSJ 20030602](https://groups.google.com/g/rec.games.trading-cards.jyhad/c/dy31XE695_M/m/4UCERLZkIDgJ) — {Business Pressure}, {Mob Rule}.
[^3-7-5-10]: [LSJ 20041207](https://groups.google.com/g/rec.games.trading-cards.jyhad/c/6oC7FtG2Ac4/m/lI5hqeuSioIJ) [ANK 20180307-2](https://www.vekn.net/forum/rules-questions/76451-ellison-humboldt-and-matteus-flesh-sculptor?start=0#85598) [RBK wording-templates](https://www.vekn.net/rulebook#wording-templates) — {Michael Luther}, {Ellison Humboldt}.
[^3-7-5-11]: [RTR 20001020](https://groups.google.com/g/rec.games.trading-cards.jyhad/c/GvxNYsYsWJ4/m/EY7NOjdsGCsJ) — {Astrid Thomas}.
[^3-7-5-12]: [RTR 20010710](https://groups.google.com/g/rec.games.trading-cards.jyhad/c/GsI1UyH54jU/m/x9LfDZX1vR4J) [LSJ 20090115-2](https://groups.google.com/g/rec.games.trading-cards.jyhad/c/rSaiVPMbpvY/m/ZYG3cYIdQZkJ) — {Treachery}, {Guru}.
[^3-7-5-13]: [LSJ 20090115-2](https://groups.google.com/g/rec.games.trading-cards.jyhad/c/rSaiVPMbpvY/m/ZYG3cYIdQZkJ) [ANK 20220808](https://www.vekn.net/forum/rules-questions/79952-when-does-lutz-ability-trigger#105913) — {Donald Cargill}, {Lutz von Hohenzollern}, {Armin Brenner}.
[^3-7-5-14]: [LSJ 19980107](https://groups.google.com/g/rec.games.trading-cards.jyhad/c/aUUs4VCR_Ec/m/PLecvfrEqbgJ) [PIB 20150105](https://www.vekn.net/forum/rules-questions/68465-voting-is-complicated#68493) — group "Vote change" (G00022), {Charming Lobby}, {Cryptic Rider}, {Distant Friend}, {Quicksilver Contemplation}.
[^3-7-5-15]: [PIB 20150105](https://www.vekn.net/forum/rules-questions/68465-voting-is-complicated#68493) [LSJ 19980107](https://groups.google.com/g/rec.games.trading-cards.jyhad/c/aUUs4VCR_Ec/m/PLecvfrEqbgJ) — {Voter Captivation}, {Cryptic Rider}.
[^3-7-5-16]: [LSJ 20010209](https://groups.google.com/g/rec.games.trading-cards.jyhad/c/wYp61ffInqs/m/fG4QzQs9p9IJ) [ANK 20201029-2](https://www.vekn.net/forum/rules-questions/78890-charming-lobby-and-delaying-tactics#101026) [LSJ 20030426](https://groups.google.com/g/rec.games.trading-cards.jyhad/c/JmGLxQmAF6s/m/LrO51CS3CgoJ) — {Delaying Tactics}, {Telepathic Vote Counting}.
[^3-7-5-17]: [LSJ 20040730](https://groups.google.com/g/rec.games.trading-cards.jyhad/c/vCZw1_QnhfE/m/6dxskyrN040J) [ANK 20220805](https://www.vekn.net/forum/rules-questions/79939-attachable-modifiers-reactions-being-removed-prior-to-attachment#105881) — {Aura of Invincibility}.
[^3-7-5-18]: [LSJ 20070927](https://groups.google.com/g/rec.games.trading-cards.jyhad/c/VaSQ7JL2N2Y/m/BenDHsAETG4J) [LSJ 20041130](https://groups.google.com/g/rec.games.trading-cards.jyhad/c/6uTPqRg387A/m/fa9DW8-Hu38J) [LSJ 20100527](https://groups.google.com/g/rec.games.trading-cards.jyhad/c/Tr3X4DsZr-8/m/O06iXN6LtzsJ) [LSJ 20020911](https://groups.google.com/g/rec.games.trading-cards.jyhad/c/_lLSO5aevoM/m/7BXDmpWjdLIJ) — {Luna Giovanni}, {Delaying Tactics}, {Echo of Harmonies}.
[^3-7-5-19]: [ANK 20190707](https://www.vekn.net/forum/rules-questions/77694-ok-a-new-round-of-doubts-for-a-noobie#95274) [TOM 19950921](https://groups.google.com/g/rec.games.trading-cards.jyhad/c/--zrAV3UcGI/m/Ywq8gud9r6cJ) [LSJ 20081203-2](https://groups.google.com/g/rec.games.trading-cards.jyhad/c/hlK89M1M9rk/m/qNtOFQfDK-oJ) — {Power Structure}, {Charming Lobby}, {Gangrel Conspiracy}.
[^3-7-6-1]: [PIB 20110802](https://www.vekn.net/forum/rules-questions/7238-couple-questions-about-prisci#7249) [LSJ 20041202](https://groups.google.com/g/rec.games.trading-cards.jyhad/c/8MwcrUpCdBc/m/E5hnEF8WU8UJ) [ANK 20180307-1](https://www.vekn.net/forum/rules-questions/76452-ballot-vs-fee-stake#85610) [RTR 19970630](https://groups.google.com/g/rec.games.trading-cards.jyhad/c/KireUeOYY3c/m/t6ifm9lur1kJ) [ANK 20211009](https://www.vekn.net/forum/rules-questions/79388-political-struggle-and-victim-priscus#103481) [LSJ 20041025](https://groups.google.com/g/rec.games.trading-cards.jyhad/c/sbfkGmojYao/m/obMvk67O5PYJ) — {Condemnation: Mute}, {Rastacourere}, {Island of Yiaros}, {Leadership Vacuum}, {Political Struggle}, group "Reduce votes" (G00021).
[^3-7-6-2]: [LSJ 19971001](https://groups.google.com/g/rec.games.trading-cards.jyhad/c/_Yu65rf2qE4/m/TqY70rjSogYJ) [LSJ 20100311](https://groups.google.com/g/rec.games.trading-cards.jyhad/c/Ogc7-acbMFs/m/cJsbFPUiReIJ) — {Arishat}, {Kateline Nadasdy}, {Sundown}.
[^3-7-6-3]: [LSJ 20040519](https://groups.google.com/g/rec.games.trading-cards.jyhad/c/fz-EAPmmqZY/m/bj4sR5CxnmQJ) [RBK gaining-votes](https://www.vekn.net/rulebook#gaining-votes) [LSJ 20051113-2](https://groups.google.com/g/rec.games.trading-cards.jyhad/c/O2cgcyCHBSI/m/7vfAvsEbiU8J) — {Gratiano}, {Genevieve}.
[^3-7-6-4]: [ANK 20211009](https://www.vekn.net/forum/rules-questions/79388-political-struggle-and-victim-priscus#103481) [LSJ 20040518-2](https://groups.google.com/g/rec.games.trading-cards.jyhad/c/4emymfUPwAM/m/JF_o7OOoCbkJ) — {Leadership Vacuum}, {Political Struggle}.
[^3-7-6-5]: [LSJ 20090304-2](https://groups.google.com/g/rec.games.trading-cards.jyhad/c/PcbRGxbYQUY/m/eOqxJaT85dwJ) [ANK 20221019](https://www.vekn.net/forum/rules-questions/80100-de-sades-special-and-kindred-manipulation#106609) — {Mustafa, The Heir}, {De Sade}.
[^3-7-6-6]: [LSJ 20020123](https://groups.google.com/g/rec.games.trading-cards.jyhad/c/F2PELnDgM_g/m/t6YG7lvcmyoJ) [RTR 19951110](https://groups.google.com/g/rec.games.trading-cards.jyhad/c/TXfganI5B2o/m/QYh3AdPNbUwJ) [LSJ 20031115](https://groups.google.com/g/rec.games.trading-cards.jyhad/c/quF7butlINo/m/XVswJuKMke4J) [PIB 20141226](https://www.vekn.net/forum/6-rules-questions/66453-double-velvet-tongue-qcannot-cast-votes-or-ballotsq?limit=10&start=20#66964) — {Madrigal}, {Scorn of Adonis}, {Loyalist}, {Khay'tall, Snake of Eden}.
[^3-7-6-7]: [RTR 19991001](https://groups.google.com/g/rec.games.trading-cards.jyhad/c/RAvWWmYoX3U/m/lb2bLOvJDhoJ) [LSJ 20030828](https://groups.google.com/g/rec.games.trading-cards.jyhad/c/enVCjRhydLo/m/tj5HN0_n98gJ) [ANK 20190731](https://www.vekn.net/forum/rules-questions/77812-abstain-from-voting?start=6#96048) [RTR 19941006](https://groups.google.com/g/rec.games.trading-cards.jyhad/c/HUipqz0LFSw/m/pY6uEa3f8-gJ) [RTR 19960530](https://groups.google.com/g/rec.games.trading-cards.jyhad/c/DpvF2Peet9o/m/dJwiudauzEwJ) — {Kindred Coercion}, {Kindred Manipulation}, {Neferu}, {Astrid Thomas}.
[^3-7-6-8]: [LSJ 19980130](https://groups.google.com/g/rec.games.trading-cards.jyhad/c/mtjOAd7aaYI/m/XZq9o1cUd-8J) [PIB 20150105](https://www.vekn.net/forum/rules-questions/68465-voting-is-complicated#68493) [LSJ 19980107](https://groups.google.com/g/rec.games.trading-cards.jyhad/c/aUUs4VCR_Ec/m/PLecvfrEqbgJ) — {Delaying Tactics}, {Telepathic Vote Counting}, group "Vote change" (G00022).
[^3-7-6-9]: [RTR 19941109](https://groups.google.com/d/msg/rec.games.deckmaster/_6CXoKTSLnw/FdG67-3HEAQJ) [RTR 19970425](https://groups.google.com/g/rec.games.trading-cards.jyhad/c/DhP_l2cX3mQ/m/9ZZZqL8NFSAJ) [ANK 20220705](https://www.vekn.net/forum/rules-questions/79895-question-regarding-using-a-minion-card-text-ability-when-locked#105630) [LSJ 20100705](https://groups.google.com/g/rec.games.trading-cards.jyhad/c/Dm_Zqyjdx8s/m/Fw-T7QAU8mkJ) [ANK 20180307-2](https://www.vekn.net/forum/rules-questions/76451-ellison-humboldt-and-matteus-flesh-sculptor?start=0#85598) [LSJ 20010526](https://groups.google.com/g/rec.games.trading-cards.jyhad/c/0Sy3xNbjYeU/m/VAbmQA5axSQJ) [RBK wording-templates](https://www.vekn.net/rulebook#wording-templates) — {Disarming Presence}, {Alvaro, The Scion of Angelica}, group "Unconditional referendum ability" (G00039), group "Non-locking referendum ability" (G00040).
[^3-7-6-10]: [ANK 20220704](https://www.vekn.net/forum/rules-questions/79890-charming-lobby-a-political-action-card-krc?start=0#105616) [LSJ 20100426](https://groups.google.com/g/rec.games.trading-cards.jyhad/c/BN3xmoZ0W1A/m/ui4w2OyGLjAJ) [LSJ 20091128](https://groups.google.com/g/rec.games.trading-cards.jyhad/c/-IxzB0bvhKU/m/ogGuu7J80R4J) [ANK 20210309-2](https://www.vekn.net/forum/rules-questions/79005-rulebook-gaining-votes?start=6#101807) — {Charming Lobby}, {Echo of Harmonies}, group "Vote playable once per game" (G00030).
[^3-7-7-1]: [RBK leave-torpor](https://www.vekn.net/rulebook#leave-torpor) [RBK rescue-a-vampire-from-torpor](https://www.vekn.net/rulebook#rescue-a-vampire-from-torpor) — rulebook action templates.
[^3-7-7-2]: [ANK 20181017](https://www.vekn.net/forum/rules-questions/77086-question-recure-of-the-homeland-cost#91228) [LSJ 19980126](https://groups.google.com/g/rec.games.trading-cards.jyhad/c/C96l_KOk174/m/V-MZhuAuZY4J) — {Resume the Coil}, {Rapid Healing}, {Healing Touch}, {Recure of the Homeland}, {Root of Vitality}, {Sense Vitality}, {Warding the Beast}, {Lord of Serenity}.
[^3-7-7-3]: [ANK 20181122-1](https://www.vekn.net/forum/rules-questions/77171-acting-in-torpor-with-ghoul-escort?start=12#91966) [LSJ 20050105-2](https://groups.google.com/g/rec.games.trading-cards.jyhad/c/sAErRDiSXfU/m/GMQXJ7TvOrsJ) [PIB 20121216](https://www.vekn.net/forum/rules-questions/42974-leave-from-torpor-question#43002) [RTR 20010710](https://groups.google.com/g/rec.games.trading-cards.jyhad/c/GsI1UyH54jU/m/x9LfDZX1vR4J) — {Ghoul Escort}, {Change of Target}, {Mirror Walk}, {Blood Brother Ambush}.
[^3-7-7-4]: [LSJ 20020304-2](https://groups.google.com/g/rec.games.trading-cards.jyhad/c/L-8OGYP5xsE/m/h5WnSofVrfUJ) [PIB 20110918](https://www.vekn.net/forum/rules-questions/10458-frondator#10459) [LSJ 20100315](https://groups.google.com/g/rec.games.trading-cards.jyhad/c/06C5ufFEaJs/m/LClmjWq7DRYJ) — {Frondator}, {Miriam Benyona}, {Cavalier}.
[^3-7-7-5]: [RTR 19950509](https://groups.google.com/g/rec.games.trading-cards.jyhad/c/_LKyR7pdMig/m/ZvwdGmIwUnsJ) — {Madness Network}.
[^3-7-7-6]: [ANK 20220218](https://www.vekn.net/forum/rules-questions/79001-the-question-of-the-month-action-fizzles?start=12#104697) [ANK 20181107](https://www.vekn.net/forum/rules-questions/77152-warsaw-station-vs-diablerie#91708) [LSJ 20090325-2](https://groups.google.com/g/rec.games.trading-cards.jyhad/c/5CW9tD5OfGk/m/wzlh-bhnTQcJ) — {Warsaw Station}.
[^3-7-8-1]: [RTR 19991206](https://groups.google.com/g/rec.games.trading-cards.jyhad/c/N7iEmqgP9WU/m/gX80TroOBsUJ) [ANK 20201228](https://www.vekn.net/forum/rules-questions/78956-timing-of-blood-hunt-following-amaranth#101316) — {Draught of the Soul}, {Soul Stealing}, {Taking the Skin: Minion}, {Ritual of the Bitter Rose}, {Slake the Thirst}.
[^3-7-8-2]: [LSJ 20090722-2](https://groups.google.com/g/rec.games.trading-cards.jyhad/c/Ry0xU4IuJmQ/m/6WqoTXkzrVUJ) [LSJ 20030618](https://groups.google.com/g/rec.games.trading-cards.jyhad/c/AdfUNNicx-Y/m/SDYFb37pS-wJ) [LSJ 20050707](https://groups.google.com/g/rec.games.trading-cards.jyhad/c/S5UbigI9faM/m/7RcuPKon0R0J) [LSJ 20050222](https://groups.google.com/g/rec.games.trading-cards.jyhad/c/pwPVmNg8hDY/m/DB4eM98iptkJ) — {Heidelberg Castle, Germany}, {Political Struggle}, {Trophy: Diablerie}.
[^3-7-8-3]: [TOM 19950921](https://groups.google.com/g/rec.games.trading-cards.jyhad/c/--zrAV3UcGI/m/Ywq8gud9r6cJ) [ANK 20190707](https://www.vekn.net/forum/rules-questions/77694-ok-a-new-round-of-doubts-for-a-noobie#95274) [LSJ 20081203-2](https://groups.google.com/g/rec.games.trading-cards.jyhad/c/hlK89M1M9rk/m/qNtOFQfDK-oJ) — {Charming Lobby}, {Power Structure}, {Gangrel Conspiracy}.
[^3-7-8-4]: [LSJ 20070417](https://groups.google.com/g/rec.games.trading-cards.jyhad/c/ecDUqbSUsNg/m/3W9aOm0MfYEJ) [LSJ 20010814-4](https://groups.google.com/g/rec.games.trading-cards.jyhad/c/8C05aiy4bdg/m/2F-8DWmrgEcJ) [LSJ 20091210](https://groups.google.com/g/rec.games.trading-cards.jyhad/c/6gInH1jtvkc/m/T_LRjaQw7kQJ) — {Abandoning the Flesh}, {Ashes to Ashes}, {Reform Body}, {Hector Trelane}.
[^3-7-8-5]: [LSJ 20090724](https://groups.google.com/g/rec.games.trading-cards.jyhad/c/1vJy-UKWR7Y/m/EOp-bsntrngJ) [ANK 20180129-1](https://www.vekn.net/forum/rules-questions/76390-abactor-carlton-van-wyk-interaction#85159) [ANK 20190701](https://www.vekn.net/forum/rules-questions/77763-multiple-questions#95690) [LSJ 20091026](https://groups.google.com/g/rec.games.trading-cards.jyhad/c/rPfGPwFH0_E/m/A8kRzU_POnoJ) [LSJ 20100112](https://groups.google.com/g/rec.games.trading-cards.jyhad/c/SJu0kgw_2tE/m/p5cshF90vkEJ) — {Abactor}, {Rebirth}.
[^3-7-8-6]: [LSJ 19970224](https://groups.google.com/g/rec.games.trading-cards.jyhad/c/80KRDjVFkyg/m/TBJso9Ra_9QJ) [LSJ 20011214-4](https://groups.google.com/g/rec.games.trading-cards.jyhad/c/RSCjaaZXY28/m/IQxqjgU_oUsJ) [LSJ 20100228](https://groups.google.com/g/rec.games.trading-cards.jyhad/c/yDeGOj1RBuU/m/k2CfIfBk770J) [ANK 20210424](https://www.vekn.net/forum/rules-questions/79121-burning-byzar-during-combat#102140) [ANK 20220218](https://www.vekn.net/forum/rules-questions/79001-the-question-of-the-month-action-fizzles?start=12#104697) [ANK 20181107](https://www.vekn.net/forum/rules-questions/77152-warsaw-station-vs-diablerie#91708) — {Reform Body}, {Ashes to Ashes}, {Byzar}, {Warsaw Station}.
[^3-7-8-7]: [LSJ 20080717](https://groups.google.com/g/rec.games.trading-cards.jyhad/c/DMsE6V84GWI/m/af5Oggz9XlQJ) [RTR 19970630](https://groups.google.com/g/rec.games.trading-cards.jyhad/c/KireUeOYY3c/m/t6ifm9lur1kJ) [LSJ 20050324-2](https://groups.google.com/g/rec.games.trading-cards.jyhad/c/aIzKlsTs51k/m/D07dQjMzaj4J) [LSJ 20050514](https://groups.google.com/g/rec.games.trading-cards.jyhad/c/9803Eu3PvDs/m/4xj8UAK_LZAJ) [ANK 20211010](https://www.vekn.net/forum/rules-questions/79335-elen-camjian-second-action?start=6#103500) [LSJ 20081213-2](https://groups.google.com/g/rec.games.trading-cards.jyhad/c/0Yf2s-qrWpM/m/0u8svYOAZ3cJ) — {Shadow Court Satyr}, {Undying Thirst}, {Phillipe Rigaud}.
[^3-8-1]: [RTR 20030519](https://groups.google.com/g/rec.games.trading-cards.jyhad/c/NOBWXWrd-vA/m/iEOpQp1uhvAJ) [LSJ 20020201](https://groups.google.com/g/rec.games.trading-cards.jyhad/c/FZ_S1BukETE/m/O_7aq0Y0Dg0J) [LSJ 20060522](https://groups.google.com/g/rec.games.trading-cards.jyhad/c/2f0wF9CECu8/m/SZn9iGo-LOQJ) [LSJ 20090617](https://groups.google.com/g/rec.games.trading-cards.jyhad/c/OMTF0_ZqUL0/m/ijdnbYacuNkJ) [ANK 20221102-2](https://www.vekn.net/forum/rules-questions/80130-motf-hl-retribution#106694) — {Archon}, {Templar}, {Delaying Tactics}, {Red Herring}, {Haqim's Law: Retribution}.
[^3-8-2]: [LSJ 20100909](https://groups.google.com/g/rec.games.trading-cards.jyhad/c/9Mn1QueD1I4/m/5hwidUeZH6EJ) [ANK 20220615](https://www.vekn.net/forum/rules-questions/72394-re-kaymakli-fragment?start=6#105476) [ANK 20200810](https://www.vekn.net/forum/rules-questions/78797-easy-nra-question-for-bindusara#100517) [ANK 20220910](https://www.vekn.net/forum/rules-questions/80021-clandestine-contrac-x-forced-march-freak#106314) — group "Provide multiple actions" (G00035), {Annazir}, {Bindusara, Historian of the Kindred}, {Clandestine Contract}.
[^3-8-3]: [ANK 20180202](https://www.vekn.net/forum/rules-questions/76402-pariah-vulture-s-buffet#85206) [RTR 19970630](https://groups.google.com/g/rec.games.trading-cards.jyhad/c/KireUeOYY3c/m/t6ifm9lur1kJ) — {Haqim's Law: Judgment}, {Pariah}, {Delaying Tactics}.
[^3-8-4]: [ANK 20180109](https://www.vekn.net/forum/rules-questions/76360-ravnos-carnival#84826) [LSJ 20070224](https://groups.google.com/g/rec.games.trading-cards.jyhad/c/lJBIPgsqNDg/m/Xoa0o6DDlWMJ) [ANK 20220704](https://www.vekn.net/forum/rules-questions/79890-charming-lobby-a-political-action-card-krc?start=0#105616) [LSJ 20070927](https://groups.google.com/g/rec.games.trading-cards.jyhad/c/VaSQ7JL2N2Y/m/BenDHsAETG4J) [LSJ 20050407](https://groups.google.com/g/rec.games.trading-cards.jyhad/c/fDl3t2lJ3Pc/m/pdmWZOwllPMJ) [ANK 20181017](https://www.vekn.net/forum/rules-questions/77086-question-recure-of-the-homeland-cost#91228) — {Ravnos Carnival}, {Charming Lobby}, {Go Anarch}.
[^3-8-5]: [RTR 19960221](https://groups.google.com/g/rec.games.trading-cards.jyhad/c/UdU535eVm0Y/m/AQGxbaznHL0J) [LSJ 20020926](https://groups.google.com/g/rec.games.trading-cards.jyhad/c/C7vgb-0Mcbo/m/6UHJsQjBs9wJ) — {Bomb}, {Camera Phone}, {Chalice of Kinship}, {Guarded Rubrics}, {Jar of Skin Eaters}, {Karavalanisha Vrana}.
[^3-9-1]: [LSJ 20001127](https://groups.google.com/g/rec.games.trading-cards.jyhad/c/XgeLMemLbj0/m/pLPfOn3ijkkJ) [LSJ 20011216-2](https://groups.google.com/g/rec.games.trading-cards.jyhad/c/eYJFjfISdPY/m/LplHHT2EZ68J) [RBK minion-phase](https://www.vekn.net/rulebook#minion-phase) — {Lunatic Eruption}, {Spirit Marionette}.
[^3-9-2]: [LSJ 20050514](https://groups.google.com/g/rec.games.trading-cards.jyhad/c/9803Eu3PvDs/m/4xj8UAK_LZAJ) [ANK 20211010](https://www.vekn.net/forum/rules-questions/79335-elen-camjian-second-action?start=6#103500) — {Phillipe Rigaud}.
[^3-9-3]: [ANK 20211009-2](https://www.vekn.net/forum/rules-questions/79335-elen-camjian-second-action?start=6#103483) [LSJ 20021121-2](https://groups.google.com/g/rec.games.trading-cards.jyhad/c/Nc72KRVbd-g/m/22PbqShf7AMJ) [LSJ 20081213-2](https://groups.google.com/g/rec.games.trading-cards.jyhad/c/0Yf2s-qrWpM/m/0u8svYOAZ3cJ) — {Elen Kamjian}, {Spirit Marionette}, {Undying Thirst}.
[^3-9-4]: [LSJ 20090226](https://groups.google.com/g/rec.games.trading-cards.jyhad/c/f7pLAO9n--U/m/u6Q1HaHK2rUJ) [ANK 20211009-2](https://www.vekn.net/forum/rules-questions/79335-elen-camjian-second-action?start=6#103483) [ANK 20200227](https://www.vekn.net/forum/rules-questions/78474-lunatic-eruption-rule#99083) — {Cry Wolf}, {Elen Kamjian}, {Lunatic Eruption}.
[^3-9-5]: [ANK 20211009-2](https://www.vekn.net/forum/rules-questions/79335-elen-camjian-second-action?start=6#103483) [LSJ 19980112](https://groups.google.com/g/rec.games.trading-cards.jyhad/c/C7WoO_yDhN0/m/FITemQKvw_AJ) [LSJ 20041103](https://groups.google.com/g/rec.games.trading-cards.jyhad/c/MiPHVp-NmCA/m/P323pUaD4DwJ) — {Elen Kamjian}, {Change of Target}, {Lunatic Eruption}.
[^3-9-6]: [LSJ 20001113](https://groups.google.com/g/rec.games.trading-cards.jyhad/c/m2grSgEaYMw/m/UYODWWyf_BEJ) — {Mask of a Thousand Faces}.
[^3-10-1]: [RTR 19951110](https://groups.google.com/g/rec.games.trading-cards.jyhad/c/TXfganI5B2o/m/QYh3AdPNbUwJ) [LSJ 19971201](https://groups.google.com/g/rec.games.trading-cards.jyhad/c/0I7KUhvhAig/m/kLiqzfugXTwJ) [RTR 20030519](https://groups.google.com/g/rec.games.trading-cards.jyhad/c/NOBWXWrd-vA/m/iEOpQp1uhvAJ) [LSJ 20030521](https://groups.google.com/g/rec.games.trading-cards.jyhad/c/Ude2or4n9nI/m/6u41LfeOpQQJ) [ANK 20210309](https://www.vekn.net/forum/rules-questions/79063-daring-the-dawn-and-then-mask-of-a-thousand-faces#101805) — {Mask of a Thousand Faces}.
[^3-10-2]: [RTR 19980623](https://groups.google.com/g/rec.games.trading-cards.jyhad/c/tSpd9dtTElc/m/-CuHJF54_n0J) [RTR 20030519](https://groups.google.com/g/rec.games.trading-cards.jyhad/c/NOBWXWrd-vA/m/iEOpQp1uhvAJ) [LSJ 20030520](https://groups.google.com/g/rec.games.trading-cards.jyhad/c/wltIoG3qv_I/m/8-SFgJp_hmUJ) [RTR 20041202](https://groups.google.com/g/rec.games.trading-cards.jyhad/c/WUWh7AdooDU/m/vojisZMCSnsJ) [LSJ 20001113](https://groups.google.com/g/rec.games.trading-cards.jyhad/c/m2grSgEaYMw/m/UYODWWyf_BEJ) [ANK 20190117-1](https://www.vekn.net/forum/rules-questions/77308-mask-of-a-1000-faces-and-bleed-modifiers#92987) — {Mask of a Thousand Faces}; [LSJ 20020927](https://groups.google.com/g/rec.games.trading-cards.jyhad/c/wg3PH7vOs1s/m/gYFNbAwk84gJ) — {Force of Will}; [ANK 20221102-2](https://www.vekn.net/forum/rules-questions/80130-motf-hl-retribution#106694) — {Haqim's Law: Retribution}.
[^3-10-3]: [RBK traits](https://www.vekn.net/rulebook#traits) [LSJ 20011023](https://groups.google.com/g/rec.games.trading-cards.jyhad/c/2GOLIrXAF8M/m/P4T3Dj6UNL0J) [RTR 20020501](https://groups.google.com/g/rec.games.trading-cards.jyhad/c/M1snoR2msbQ/m/RFwCmX3anDkJ) — {Malleable Visage}; [ANK 20171212](https://www.vekn.net/forum/rules-questions/76334-slave-mental-maze-interaction?start=12#84553) — {Obedience}; [ANK 20200114](https://www.vekn.net/forum/rules-questions/78321-slave-rule-and-acting-minion#98584) — {Shadow Boxing}; [ANK 20180913-2](https://www.vekn.net/forum/rules-questions/76998-narsheptha-fbi?start=6#90588) — {FBI Special Affairs Division}; [ANK 20230814](https://www.vekn.net/forum/rules-questions/80752-deep-song-and-powerbase-savannah?start=12#109035) — {Powerbase: Savannah}.
[^3-10-4]: [ANK 20211022](https://www.vekn.net/forum/rules-questions/79422-nar-sheptha#103636) — {Deep Song}, {Nar-Sheptha}.
[^4-1-1]: [RTR 19970630](https://groups.google.com/g/rec.games.trading-cards.jyhad/c/KireUeOYY3c/m/t6ifm9lur1kJ) [ANK 20180720](https://www.vekn.net/forum/rules-questions/76840-setting-range-and-pre-range#89125) — {Omael Kuman}.
[^4-1-2]: [ANK 20171226](https://www.vekn.net/forum/rules-questions/76349-shoulder-drop?start=0#84655) [RTR 20030519](https://groups.google.com/g/rec.games.trading-cards.jyhad/c/NOBWXWrd-vA/m/iEOpQp1uhvAJ) [RBK combat](https://www.vekn.net/rulebook#combat) — {Shoulder Drop}, {Infection}, {Coordinate Attacks}.
[^4-1-3]: [ANK 20221102](https://www.vekn.net/forum/rules-questions/80129-fall-of-london-card-rules-questions#106688) [LSJ 20011214-3](https://groups.google.com/g/rec.games.trading-cards.jyhad/c/9WJX_WF656A/m/2V1mYoHPB6IJ) [LSJ 20031212](https://groups.google.com/g/rec.games.trading-cards.jyhad/c/dOATNbVuaqs/m/g8FtHUHX1kUJ) [LSJ 20070319](https://groups.google.com/g/rec.games.trading-cards.jyhad/c/9ArBwoYDquw/m/y-nmJqY3em0J) [RBK combat](https://www.vekn.net/rulebook#combat) — {Guardian, The}, {Blissful Agony}, {Taunt the Caged Beast}.
[^4-1-4]: [ANK 20180929](https://www.vekn.net/forum/rules-questions/77035-questions-about-marie-pierre?start=6#90835) [LSJ 19980109](https://groups.google.com/g/rec.games.trading-cards.jyhad/c/d2U51Uw0Hfg/m/uIPoVvPFePgJ) [RTR 20020501](https://groups.google.com/g/rec.games.trading-cards.jyhad/c/M1snoR2msbQ/m/RFwCmX3anDkJ) [ANK 20180928-2](https://www.vekn.net/forum/rules-questions/77035-questions-about-marie-pierre#90826) — {Marie-Pierre}.
[^4-1-5]: [LSJ 20070217](https://groups.google.com/g/rec.games.trading-cards.jyhad/c/HkKuwBe9LRk/m/3GccpU4eaK8J) — {Champion}.
[^4-1-6]: [LSJ 20060410](https://groups.google.com/g/rec.games.trading-cards.jyhad/c/jr8wSeSchsc/m/xIIeqsJxHrIJ) [LSJ 20020204](https://groups.google.com/g/rec.games.trading-cards.jyhad/c/DDjGFeolsxg/m/bM64eWo1jCEJ) — {Angel of Berlin}, {Internal Recursion}.
[^4-1-9]: [ANK 20181101](https://www.vekn.net/forum/rules-questions/77132-save-face#91633) [RBK combat](https://www.vekn.net/rulebook#combat) — {Nosferatu Putrescence}, {Bliss}, {Martyr's Resilience}.
[^4-1-10]: [LSJ 20080618](https://groups.google.com/g/rec.games.trading-cards.jyhad/c/9FAkwIsuYZc/m/gCoYa59TEGIJ) — group "Cancel with no action" (G00063).
[^4-2-1]: [RTR 19970630](https://groups.google.com/g/rec.games.trading-cards.jyhad/c/KireUeOYY3c/m/t6ifm9lur1kJ) [ANK 20180720](https://www.vekn.net/forum/rules-questions/76840-setting-range-and-pre-range#89125) — {Neutral Guard}, {Squirrel Balance}, {Charge of the Buffalo}, and sixteen further cards carrying the identical wording.
[^4-2-3]: [RTR 19970630](https://groups.google.com/g/rec.games.trading-cards.jyhad/c/KireUeOYY3c/m/t6ifm9lur1kJ) [ANK 20180720](https://www.vekn.net/forum/rules-questions/76840-setting-range-and-pre-range#89125) [PIB 20120214](https://www.vekn.net/forum/rules-questions/22906-re-set-the-range?start=12#22999) — {Immortal Grapple}, {Grasp of the Python}, {Lam Into}.
[^4-2-2]: [PIB 20120214](https://www.vekn.net/forum/rules-questions/22906-re-set-the-range?start=12#22999) — {Asanbonsam Ghoul}, {Neutral Guard}, {Squirrel Balance}, {Gang Tactics}, {Storm Sewers}.
[^4-2-6]: [LSJ 20021028](https://groups.google.com/g/rec.games.trading-cards.jyhad/c/g0GGiVIxyis/m/35WA-O9XrroJ) [ANK 20200115](https://www.vekn.net/forum/rules-questions/78321-slave-rule-and-acting-minion?start=6#98594) [LSJ 20010814](https://groups.google.com/g/rec.games.trading-cards.jyhad/c/z7uYIO39YCo/m/aufoimHncvQJ) [RTR 20020501](https://groups.google.com/g/rec.games.trading-cards.jyhad/c/M1snoR2msbQ/m/RFwCmX3anDkJ) — {Sniper Rifle}.
[^4-2-4]: [LSJ 20100709](https://groups.google.com/g/rec.games.trading-cards.jyhad/c/j98aqFIFjnE/m/h_FjFos8S2UJ) [RBK before-range](https://www.vekn.net/rulebook#before-range) — {Fear of the Void Below}.
[^4-2-5]: [ANK 20170930](https://www.vekn.net/forum/rules-questions/76197-still-confused-about-multiple-outside-the-hourglasses#83682) — {Outside the Hourglass}, {Weather Control}.
[^4-2-9]: [LSJ 20090529](https://groups.google.com/g/rec.games.trading-cards.jyhad/c/LpFSLRuWONA/m/daxDmJiGX0AJ) — {Lucian, the Perfect}.
[^4-2-8]: [ANK 20210928-2](https://www.vekn.net/forum/rules-questions/79330-thoughts-betrayed-and-hunger-of-marduk?start=12#103364) — {Thoughts Betrayed}.
[^4-2-7]: [LSJ 20080409](https://groups.google.com/g/rec.games.trading-cards.jyhad/c/jrN1Pc_Quk0/m/XwWAWfq_KRIJ) — {Target Head}, {Target Hand}, {Target Leg}, {Target Retainer}, {Target Vitals}.
[^4-2-10]: [ANK 20210422](https://www.vekn.net/forum/rules-questions/79111-vampiric-disease-and-dodge#102098) [LSJ 20040830](https://groups.google.com/g/rec.games.trading-cards.jyhad/c/KHMhiNiSKo4/m/MCfo9aA-EjcJ) [ANK 20200703](https://www.vekn.net/forum/rules-questions/78713-blood-of-water-timing-before-strike-resolution#100237) [LSJ 20031008](https://groups.google.com/g/rec.games.trading-cards.jyhad/c/JUnIGIrb3pw/m/EOo-cGykdmYJ) — {Vampiric Disease}, {Blood to Water}.
[^4-2-11]: [RTR 19980928](https://groups.google.com/g/rec.games.trading-cards.jyhad/c/Xva4_IRavxM/m/F-_fjzTmo88J) [ANK 20211102](https://www.vekn.net/forum/rules-questions/79447-rotschreck-and-dodge#103743) — {Rötschreck}.
[^4-2-12]: [LSJ 19970801](https://groups.google.com/g/rec.games.trading-cards.jyhad/c/7ZnLKTdPEn4/m/6L-nVarAJwMJ) [ANK 20221212](https://www.vekn.net/forum/rules-questions/80208-burst-of-sunlight?start=6#107000) [ANK 20181024](https://www.vekn.net/forum/rules-questions/77108-potio-martyrium-questions#91462) [LSJ 19970915](https://groups.google.com/g/rec.games.trading-cards.jyhad/c/in3R3mQs5Do/m/41KNa8aVpV0J) [RTR 20010710](https://groups.google.com/g/rec.games.trading-cards.jyhad/c/GsI1UyH54jU/m/x9LfDZX1vR4J) — {Burst of Sunlight}, {Potio Martyrium}, {Riposte}, {Blood of the Cobra}.
[^4-2-13]: [LSJ 20060509](https://groups.google.com/g/rec.games.trading-cards.jyhad/c/KBFnBRrOGB4/m/7ZYNQnvZ5tEJ) [LSJ 20060825](https://groups.google.com/g/rec.games.trading-cards.jyhad/c/2usG7ml8BAw/m/Xa1o5-C1dSAJ) — {Earthshock}, {Anachronism}.
[^4-3-1]: [ANK 20180704](https://www.vekn.net/forum/rules-questions/76784-blessed-blade-blade-of-bellona#88556) [LSJ 20050304](https://groups.google.com/g/rec.games.trading-cards.jyhad/c/X5JZBbSIj3U/m/CBdkcQ-rAesJ) [RBK combat](https://www.vekn.net/rulebook#combat) — {Blessed Blade}, {Projectile}.
[^4-3-2]: [ANK 20210928-2](https://www.vekn.net/forum/rules-questions/79330-thoughts-betrayed-and-hunger-of-marduk?start=12#103364) — {Thoughts Betrayed}.
[^4-3-3]: [LSJ 20080409](https://groups.google.com/g/rec.games.trading-cards.jyhad/c/jrN1Pc_Quk0/m/XwWAWfq_KRIJ) [TOM 19951217](https://groups.google.com/g/rec.games.trading-cards.jyhad/c/Y2_A66iRqMc/m/LkT-8j5cz2cJ) [LSJ 20100308](https://groups.google.com/g/rec.games.trading-cards.jyhad/c/-euEN_y8ius/m/yrDIv--PZfsJ) — {Target Vitals}, {Target Head}, {Target Leg}, {Target Hand}, {Target Retainer}, {Immortal Grapple}, {Mind of the Wilds}.
[^4-3-4]: [LSJ 20080702-1](https://groups.google.com/g/rec.games.trading-cards.jyhad/c/JtLgB7Apqq0/m/lWdtq38KJ-wJ) [LSJ 20090114](https://groups.google.com/g/rec.games.trading-cards.jyhad/c/fZIdIRDDxdo/m/dtdSNVk_IIkJ) [TOM 19960225](https://groups.google.com/g/rec.games.trading-cards.jyhad/c/0LLTOfvyVbM/m/ih72_C-LriwJ) [LSJ 20071020](https://groups.google.com/g/rec.games.trading-cards.jyhad/c/ap2IBEgm0gI/m/sL_XyMwDK4cJ) [LSJ 20010627](https://groups.google.com/g/rec.games.trading-cards.jyhad/c/NhNCVCCDyU0/m/I5Yph3-UUPsJ) [LSJ 20010919](https://groups.google.com/g/rec.games.trading-cards.jyhad/c/08AhThj0IxI/m/ZmMxUKqbymIJ) — {Bundi}, {Lucky Blow}, {Scorpion's Touch}, {Stutter-Step}.
[^4-3-5]: [LSJ 20081120-2](https://groups.google.com/g/rec.games.trading-cards.jyhad/c/e2PNDpg-l_c/m/wqEDxGHKJQgJ) [RTR 20010710](https://groups.google.com/g/rec.games.trading-cards.jyhad/c/GsI1UyH54jU/m/x9LfDZX1vR4J) [LSJ 20050224-3](https://groups.google.com/g/rec.games.trading-cards.jyhad/c/tzl6213crbI/m/HlnYVX9L3fAJ) — {Heroic Might}, {Blood of the Cobra}, {Projectile}.
[^4-3-6]: [LSJ 19971215](https://groups.google.com/g/rec.games.trading-cards.jyhad/c/mfBmRrUKZQ0/m/5Py-ENuzoGwJ) [LSJ 20030213-2](https://groups.google.com/g/rec.games.trading-cards.jyhad/c/Jwj7VjhFU5o/m/VbR1wZ23gvIJ) — {Jar of Skin Eaters}, {Talbot's Chainsaw}, {Sword of Judgment}.
[^4-3-7]: [RTR 19990105](https://groups.google.com/g/rec.games.trading-cards.jyhad/c/2LT2jSX4Nlk/m/vNjIMCxSYTIJ) [RTR 19960112](https://groups.google.com/g/rec.games.trading-cards.jyhad/c/d3n3StNS7no/m/k2NmZFUl9fAJ) [LSJ 20000215](https://groups.google.com/g/rec.games.trading-cards.jyhad/c/8to3EBsk-iY/m/jFT-RgP3WjEJ) [ANK 20200703](https://www.vekn.net/forum/rules-questions/78713-blood-of-water-timing-before-strike-resolution#100237) [LSJ 20031008](https://groups.google.com/g/rec.games.trading-cards.jyhad/c/JUnIGIrb3pw/m/EOo-cGykdmYJ) — group "Improve weapon before resolution" (G00050), {Blood Agony}, {Wolf Claws}, {Backstab}, {Blood to Water}.
[^4-3-8]: [LSJ 20021028](https://groups.google.com/g/rec.games.trading-cards.jyhad/c/g0GGiVIxyis/m/35WA-O9XrroJ) [LSJ 20001126](https://groups.google.com/g/rec.games.trading-cards.jyhad/c/ZK97Kk4WQ00/m/SJPz6uc5Xw8J) — group "Weapon with optional maneuver" (G00024), {Hidden Lurker}, {Deer Rifle}.
[^4-3-9]: [RBK cancel-a-card](https://www.vekn.net/rulebook#cancel-a-card) [LSJ 20090818](https://groups.google.com/g/rec.games.trading-cards.jyhad/c/jkKBGVLmFHc/m/YXwYthjI7isJ) [LSJ 20100206](https://groups.google.com/g/rec.games.trading-cards.jyhad/c/cAGrXqpO-YQ/m/GJHdeYt0GdUJ) [RTR 20040501](https://groups.google.com/g/rec.games.trading-cards.jyhad/c/7-mp3Ada86I/m/yenQ7FZ-VMIJ) [LSJ 20050228-3](https://groups.google.com/g/rec.games.trading-cards.jyhad/c/UHEZEmX22jA/m/u0IldHuItjgJ) [ANK 20230111](https://www.vekn.net/forum/rules-questions/80258-rigor-mortis-and-aid-from-bats-and-other-manuver-strike-cards#107179) [ANK 20200311](https://www.vekn.net/forum/rules-questions/78506-target-retainer-cancelled#99256) — {Supernatural Resistance}, {Death Seeker}, {Primal Instincts}, {Rigor Mortis}, {Target Retainer}.
[^4-3-10]: [ANK 20200909](https://www.vekn.net/forum/rules-questions/78845-contagion-corruption-counters-vs-strike-dodge#100726) [LSJ 20040130](https://groups.google.com/g/rec.games.trading-cards.jyhad/c/wvuR79dNCDU/m/z4C2L5NCgg8J) [LSJ 20001127-2](https://groups.google.com/g/rec.games.trading-cards.jyhad/c/KInac4MQMuA/m/LnpxH08HVbMJ) [LSJ 20070508](https://groups.google.com/g/rec.games.trading-cards.jyhad/c/FOLkbrSh0Ns/m/Kbt2Ox1GBI8J) [LSJ 20010806-1](https://groups.google.com/g/rec.games.trading-cards.jyhad/c/PuawBcgSIKI/m/D7zOKJXQDbMJ) [PIB 20141026](https://www.vekn.net/forum/rules-questions/66960-gianna-di-canneto#66971) [LSJ 20100310](https://groups.google.com/g/rec.games.trading-cards.jyhad/c/hYN6L3COpqw/m/RPdTARngQLgJ) — {Contagion}, {Escaped Mental Patient}, {Flash Grenade}, {Gianna di Canneto}, {Zip Gun}.
[^4-3-11]: [LSJ 20051123](https://groups.google.com/g/rec.games.trading-cards.jyhad/c/Ww3zSY8cVNs/m/QVDV21-IjysJ) [LSJ 20080212](https://groups.google.com/g/rec.games.trading-cards.jyhad/c/Yg1nZfgkpGM/m/OxDoRLREnewJ) [RBK strike-effects](https://www.vekn.net/rulebook#strike-effects) — {Darkness Within}, {Young Bloods}.
[^4-3-12]: [RTR 19960221](https://groups.google.com/g/rec.games.trading-cards.jyhad/c/UdU535eVm0Y/m/AQGxbaznHL0J) [PIB 20130319](https://www.vekn.net/forum/rules-questions/46164-catatonic-fear-and-loving-agony#46168) [ANK 20170111](https://www.vekn.net/forum/rules-questions/72635-dam-the-heart-s-river-and-catatonic-fear?start=6#80117) [LSJ 20071011](https://groups.google.com/g/rec.games.trading-cards.jyhad/c/GSQqnAEBkgU/m/gFKF1ltY4JEJ) [RTR 19980928](https://groups.google.com/g/rec.games.trading-cards.jyhad/c/Xva4_IRavxM/m/F-_fjzTmo88J) — {Target Vitals}, {Target Head}, {Lucky Blow}, {Catatonic Fear}, {Loving Agony}, {Talith}.
[^4-3-13]: [LSJ 20040928](https://groups.google.com/g/rec.games.trading-cards.jyhad/c/GBcR6aNjIk4/m/DXPyqBM1R8kJ) [ANK 20170519](https://www.vekn.net/forum/rules-questions/75805-blood-fury-vs-ivory-bow-roetschreck#81933) — {Soul Burn}, {Blood Fury}.
[^4-3-14]: [PIB 20110830](https://www.vekn.net/forum/rules-questions/9340-first-strike--strength-reduction#9345) [LSJ 20030307](https://groups.google.com/g/rec.games.trading-cards.jyhad/c/zhdj4jnSdrM/m/tAU_FosRtbwJ) [LSJ 20100119](https://groups.google.com/g/rec.games.trading-cards.jyhad/c/1eULCGaVcO0/m/eefMWzjoK0IJ) [ANK 20180913-1](https://www.vekn.net/forum/rules-questions/77003-stutter-step-question#90610) [RBK first-strike](https://www.vekn.net/rulebook#first-strike) — {Scorpion's Touch}, {Shambling Hordes}, {Stutter-Step}.
[^4-3-15]: [PIB 20121028](https://www.vekn.net/forum/rules-questions/39816-ec-2012-can-you-answer-these?start=6#39843) [LSJ 20051016](https://groups.google.com/g/rec.games.trading-cards.jyhad/c/s_At5syL66k/m/1eGsxyhDn1YJ) [LSJ 20051017](https://groups.google.com/g/rec.games.trading-cards.jyhad/c/s_At5syL66k/m/bCvu2ks001gJ) [ANK 20220204](https://www.vekn.net/forum/rules-questions/79634-multi-dust-up-question#104626) — {Renegade Garou}, {Lorrie Dunsirn}, {Dust Up}.
[^4-3-16]: [LSJ 20011214-5](https://groups.google.com/g/rec.games.trading-cards.jyhad/c/gI44SEC82Yk/m/Kgipu7IXwWkJ) — {Rigor Mortis}.
[^4-3-17]: [LSJ 20001206](https://groups.google.com/g/rec.games.trading-cards.jyhad/c/kFIO74LxqFQ/m/U1Dtf3f4CPgJ) [ANK 20211124](https://www.vekn.net/forum/rules-questions/79501-addition-strikes#103982) [LSJ 20030224](https://groups.google.com/g/rec.games.trading-cards.jyhad/c/67261v339Ds/m/um8V7VVp2Y4J) [LSJ 20080210](https://groups.google.com/g/rec.games.trading-cards.jyhad/c/nL-xqiydvYg/m/hWQZF3aBdwsJ) [RTR 19941109](https://groups.google.com/d/msg/rec.games.deckmaster/_6CXoKTSLnw/FdG67-3HEAQJ) [RBK additional-strikes](https://www.vekn.net/rulebook#additional-strikes) — {Hell-for-Leather}, {Quickness}, {Ghoul Retainer}, group "Cancel" (G00058), group "Retainer that strike" (G00029).
[^4-4-1]: [LSJ 19971211-2](https://groups.google.com/g/rec.games.trading-cards.jyhad/c/2s5V_AIczYw/m/uucMcHxSQawJ) [PIB 20130303](https://www.vekn.net/forum/rules-questions/45620-rock-cat-vs-torn-signpost#45626) [LSJ 20100813](https://groups.google.com/g/rec.games.trading-cards.jyhad/c/nOb3cmvA_3U/m/0UJqPZGujHsJ) [RTR 19980623](https://groups.google.com/g/rec.games.trading-cards.jyhad/c/tSpd9dtTElc/m/-CuHJF54_n0J) [LSJ 20020821](https://groups.google.com/g/rec.games.trading-cards.jyhad/c/o_nBNZraMvE/m/g0xPNLGquKIJ) [LSJ 20020904](https://groups.google.com/g/rec.games.trading-cards.jyhad/c/Qmi4hFk6QqE/m/VmoU2tfLMgEJ) [LSJ 20030307](https://groups.google.com/g/rec.games.trading-cards.jyhad/c/zhdj4jnSdrM/m/tAU_FosRtbwJ) [LSJ 20100119](https://groups.google.com/g/rec.games.trading-cards.jyhad/c/1eULCGaVcO0/m/eefMWzjoK0IJ) — {Erosion}, {Torn Signpost}, {Illegal Search and Seizure}, {Concealed Weapon}, {Shambling Hordes}.
[^4-4-2]: [TOM 19960225](https://groups.google.com/g/rec.games.trading-cards.jyhad/c/0LLTOfvyVbM/m/ih72_C-LriwJ) [RTR 19970630](https://groups.google.com/g/rec.games.trading-cards.jyhad/c/KireUeOYY3c/m/t6ifm9lur1kJ) [LSJ 20100527](https://groups.google.com/g/rec.games.trading-cards.jyhad/c/Tr3X4DsZr-8/m/O06iXN6LtzsJ) [ANK 20210620](https://www.vekn.net/forum/rules-questions/79186-alejandro-aguirre-true-faith#102522) — {Target Vitals}, {Increased Strength}, {Glaser Rounds}, {Merrill Molitor}, {Alejandro Aguirre}, and ~45 further cards carrying the same sentence.
[^4-4-3]: [RTR 19960221](https://groups.google.com/g/rec.games.trading-cards.jyhad/c/UdU535eVm0Y/m/AQGxbaznHL0J) [LSJ 20080226](https://groups.google.com/g/rec.games.trading-cards.jyhad/c/NAfcSQEiLXY/m/GyMO2byB0AkJ) — {Dam the Heart's River}, {Lucky Blow}, {Rowan Ring}, {Oubliette}.
[^4-4-4]: [RTR 19970630](https://groups.google.com/g/rec.games.trading-cards.jyhad/c/KireUeOYY3c/m/t6ifm9lur1kJ) [LSJ 19990723](https://groups.google.com/g/rec.games.trading-cards.jyhad/c/6Lx2jnw7hMA/m/tMpV0CndVxwJ) [PIB 20120426](https://www.vekn.net/forum/rules-questions/27863-disarm-vs-combat-ends?start=6#28739) — {Catatonic Fear}, {Loving Agony}, {Outside the Hourglass}.
[^4-4-5]: [RTR 19970630](https://groups.google.com/g/rec.games.trading-cards.jyhad/c/KireUeOYY3c/m/t6ifm9lur1kJ) [LSJ 19970801](https://groups.google.com/g/rec.games.trading-cards.jyhad/c/7ZnLKTdPEn4/m/6L-nVarAJwMJ) [LSJ 20060217](https://groups.google.com/g/rec.games.trading-cards.jyhad/c/BhecJx5BqtQ/m/MjBL57IRDjQJ) [RBK damage-resolution](https://www.vekn.net/rulebook#damage-resolution) — {Grenade}, {Burst of Sunlight}, {Shemti}, and ~24 further cards carrying the same sentence.
[^4-4-6]: [LSJ 20090304-1](https://groups.google.com/g/rec.games.trading-cards.jyhad/c/B7EQiAVOr1Q/m/gg-GkqQBRp8J) [LSJ 20100514](https://groups.google.com/g/rec.games.trading-cards.jyhad/c/Mz_fcIldfAY/m/Ys_W0MtwqLgJ) [LSJ 20051220](https://groups.google.com/g/rec.games.trading-cards.jyhad/c/bIcX7F3wzf0/m/Oi91XAFSwKUJ) [ANK 20180612](https://www.vekn.net/forum/rules-questions/76717-retainers-damage-and-disciplines#88129) [ANK 20211127](https://www.vekn.net/forum/rules-questions/76687-retainers-inflicting-damage-environmental?start=6#104017) — {Talbot's Chainsaw}, {Kerrie}, group "Retainer doing damage" (G00016).
[^4-4-7]: [TOM 19950304](https://groups.google.com/g/rec.games.trading-cards.jyhad/c/DYxpGPWoSaE/m/05x_CdfRdLgJ) [LSJ 20010812](https://groups.google.com/g/rec.games.trading-cards.jyhad/c/uXGLWUAuByc/m/omHFVEtV-A0J) [ANK 20201228-2](https://www.vekn.net/forum/rules-questions/78954-necrosis-and-target-vitals?start=0#101314) [ANK 20200925](https://www.vekn.net/forum/rules-questions/78861-revelation-of-wrath#100820) [ANK 20200517](https://www.vekn.net/forum/rules-questions/78638-transfusion-and-elemental-damage#99853) [PIB 20111017](https://www.vekn.net/forum/rules-questions/12104-archon-in-3-pool-and-carrion-crows-vs-nephandus#12110) [LSJ 20010626](https://groups.google.com/g/rec.games.trading-cards.jyhad/c/tkCRUBRp82E/m/Xz54yldDdycJ) — {Pulled Fangs}, {Necrosis}, {Nephandus}, {Blood of Acid}, {Disarm}.
[^4-4-8]: [ANK 20181128](https://www.vekn.net/forum/rules-questions/77187-dam-the-heart-s-river-and-weather-control#92076) [PIB 20150520](https://www.vekn.net/forum/rules-questions/68512-re-dam-the-heart-s-river-and-dagon-s-call?start=0#71259) [PIB 20150603-1](https://www.vekn.net/forum/rules-questions/71468-dawn-operation-and-environmental-damage#71470) [LSJ 20020314](https://groups.google.com/g/rec.games.trading-cards.jyhad/c/1uKDkopJTRo/m/w7d5OktOJhYJ) [PIB 20130319](https://www.vekn.net/forum/rules-questions/46164-catatonic-fear-and-loving-agony#46168) — {Dam the Heart's River}, {Dagon's Call}, {Dawn Operation}, {Domain of Evernight}.
[^4-4-10]: [ANK 20170111](https://www.vekn.net/forum/rules-questions/72635-dam-the-heart-s-river-and-catatonic-fear?start=6#80117) [LSJ 20071011](https://groups.google.com/g/rec.games.trading-cards.jyhad/c/GSQqnAEBkgU/m/gFKF1ltY4JEJ) [PIB 20130319](https://www.vekn.net/forum/rules-questions/46164-catatonic-fear-and-loving-agony#46168) [LSJ 20080630](https://groups.google.com/g/rec.games.trading-cards.jyhad/c/nvuXBpEaKAA/m/ymiC3yAQVOwJ) [RTR 19970630](https://groups.google.com/g/rec.games.trading-cards.jyhad/c/KireUeOYY3c/m/t6ifm9lur1kJ) — {Catatonic Fear}, {Loving Agony}, {Riposte}, {Nephandus}.
[^4-4-11]: [LSJ 20040812-2](https://groups.google.com/g/rec.games.trading-cards.jyhad/c/E7D1cVmAdqQ/m/MvPApbrT14gJ) [PIB 20130327](https://www.vekn.net/forum/rules-questions/46279-soak-vs-treat-agg-damage-as-normal-damage#46285) [ANK 20200130-1](https://www.vekn.net/forum/rules-questions/78400-rotshreck#98821) [ANK 20220114](https://www.vekn.net/forum/rules-questions/79432-rotschreck-and-non-strike-agravated-damage?start=12#104475) [LSJ 20040120](https://groups.google.com/g/rec.games.trading-cards.jyhad/c/5zBRtwg6lpU/m/MMisbKi7_Z0J) [LSJ 20060409](https://groups.google.com/g/rec.games.trading-cards.jyhad/c/gsFQXsCGTG4/m/q5H8FvuKksIJ) [LSJ 20030213](https://groups.google.com/g/rec.games.trading-cards.jyhad/c/j6cuQ6pFJSA/m/F-A_hlBMpd0J) — group "Prevent non-aggravated" (G00033), {Resilience}, {Flesh of Marble}, {Rötschreck}, {Ex Nihilo}, {Shadow Court Satyr}, {Merrill Molitor}.
[^4-4-12]: [ANK 20210424](https://www.vekn.net/forum/rules-questions/79121-burning-byzar-during-combat#102140) [LSJ 20021120](https://groups.google.com/g/rec.games.trading-cards.jyhad/c/4TgUatcTtdk/m/OUN021UtXV8J) [RBK damage-resolution](https://www.vekn.net/rulebook#damage-resolution) — {Byzar}, {Anathema}.
[^4-4-13]: [ANK 20170427](https://www.vekn.net/forum/rules-questions/75755-resolution-card-blood-of-acid?start=6#81627) [LSJ 20040805](https://groups.google.com/g/rec.games.trading-cards.jyhad/c/WuER8RUMzTE/m/OmQhmQFkFLkJ) [ANK 20200517-2](https://www.vekn.net/forum/rules-questions/78629-damage-prevention-windows-what-can-you-soak?start=6#99855) [LSJ 20001111](https://groups.google.com/g/rec.games.trading-cards.jyhad/c/m23Hj3OW2A4/m/n23vvkXo6AkJ) [PIB 20150426](https://www.vekn.net/forum/rules-questions/70713-blood-of-acid-and-successfully-inflicted-also-krakens-kiss#70715) — {Blood of Acid}, {Tunnel Runner}, {Vagabond Mystic}.
[^4-5-1]: [LSJ 20001114](https://groups.google.com/g/rec.games.trading-cards.jyhad/c/qXSlM7Grq1c/m/cSDoQ9mw0z4J) — {Soak}, {Skin of Night}, {Glancing Blow}, {Armor of Vitality}, {Indomitability}.
[^4-5-2]: [LSJ 20010315](https://groups.google.com/g/rec.games.trading-cards.jyhad/c/m9CrEOn1veo/m/gmx_Nou4BTQJ) [LSJ 20100527](https://groups.google.com/g/rec.games.trading-cards.jyhad/c/Tr3X4DsZr-8/m/O06iXN6LtzsJ) — {Apparition}, {Brother's Blood}.
[^4-5-3]: [LSJ 20011214-2](https://groups.google.com/g/rec.games.trading-cards.jyhad/c/TinQ8ywzIHU/m/-zW_hcYbiD4J) — {Repulsion}.
[^4-5-4]: [LSJ 20050628](https://groups.google.com/g/rec.games.trading-cards.jyhad/c/lN3eieA3xgs/m/c4ZoOWHUsPEJ) — {Blood Fury}, {Blood Rage}, {Dead Hand}, {Soul Burn}.
[^4-5-5]: [RTR 20041202](https://groups.google.com/g/rec.games.trading-cards.jyhad/c/WUWh7AdooDU/m/vojisZMCSnsJ) — {Soak}, {Nightstick}, {Forearm Block}, {Rego Motum}.
[^4-5-6]: [RTR 20041202](https://groups.google.com/g/rec.games.trading-cards.jyhad/c/WUWh7AdooDU/m/vojisZMCSnsJ) [PIB 20121202](https://www.vekn.net/forum/rules-questions/42195-hidden-strength-can-you-prevent-damage-that-wasn-t-dealt#42225) [LSJ 20030121](https://groups.google.com/g/rec.games.trading-cards.jyhad/c/lED3kZ2UUUo/m/8TgrW3RxQ9QJ) [LSJ 20001114](https://groups.google.com/g/rec.games.trading-cards.jyhad/c/qXSlM7Grq1c/m/cSDoQ9mw0z4J) — {Hidden Strength}, {Martyr's Resilience}.
[^4-5-7]: [LSJ 20001114](https://groups.google.com/g/rec.games.trading-cards.jyhad/c/qXSlM7Grq1c/m/cSDoQ9mw0z4J) — {Armor of Vitality}, {Rego Motum}, {Undead Persistence}, {Skin of Rock}.
[^4-5-8]: [ANK 20200318](https://www.vekn.net/forum/rules-questions/78525-apparition#99356) [LSJ 20081210](https://groups.google.com/g/rec.games.trading-cards.jyhad/c/pUUGH1nSKpc/m/aRxHUjHMxZsJ) — {Armor of Caine's Fury}, {Apparition}, {Kevlar Vest}.
[^4-5-9]: [LSJ 20040812-2](https://groups.google.com/g/rec.games.trading-cards.jyhad/c/E7D1cVmAdqQ/m/MvPApbrT14gJ) [PIB 20130327](https://www.vekn.net/forum/rules-questions/46279-soak-vs-treat-agg-damage-as-normal-damage#46285) [LSJ 20021001](https://groups.google.com/g/rec.games.trading-cards.jyhad/c/FW-bmZpIM68/m/gLoYcvpUB7UJ) — group "Prevent non-aggravated" (G00033), {Flesh of Marble}, {Resilience}.
[^4-5-10]: [LSJ 20010813](https://groups.google.com/g/rec.games.trading-cards.jyhad/c/8MR4bq0Cxj4/m/f_rAOuj3CboJ) [LSJ 20010819-2](https://groups.google.com/g/rec.games.trading-cards.jyhad/c/8MR4bq0Cxj4/m/YgNsk8nGcREJ) [LSJ 20010814-2](https://groups.google.com/g/rec.games.trading-cards.jyhad/c/8MR4bq0Cxj4/m/SH4dKuz8qO0J) — {Beast Meld}, {Precognition}.
[^4-5-11]: [LSJ 19980216](https://groups.google.com/g/rec.games.trading-cards.jyhad/c/kyuR_x6pRmo/m/dXNCT3ORc7QJ) — {Blood Fury}, {Blood Rage}, {Soul Burn}.
[^4-5-12]: [RTR 19980928](https://groups.google.com/g/rec.games.trading-cards.jyhad/c/Xva4_IRavxM/m/F-_fjzTmo88J) [ANK 20211102](https://www.vekn.net/forum/rules-questions/79447-rotschreck-and-dodge#103743) [ANK 20230823](https://www.vekn.net/forum/rules-questions/75182-can-you-use-bollix-tha-as-defense-against-long-range-strike?start=6#109132) [LSJ 19980219](https://groups.google.com/g/rec.games.trading-cards.jyhad/c/FoVObdCLJPM/m/Wb6cYwW6-jMJ) — {Rötschreck}, {Bollix}, {Rowan Ring}.
[^4-5-13]: [LSJ 20100519](https://groups.google.com/g/rec.games.trading-cards.jyhad/c/criytfhw97o/m/sj9_vGAi-xQJ) [LSJ 20090304-1](https://groups.google.com/g/rec.games.trading-cards.jyhad/c/B7EQiAVOr1Q/m/gg-GkqQBRp8J) — {Nephandus}, group "Immune to damage" (G00026).
[^4-5-14]: [RTR 19960112](https://groups.google.com/g/rec.games.trading-cards.jyhad/c/d3n3StNS7no/m/k2NmZFUl9fAJ) [PIB 20121031](https://www.vekn.net/forum/rules-questions/39816-ec-2012-can-you-answer-these?start=18#39908) — {Chiropteran Marauder}, {Claws of the Dead}, {The Coven}.
[^4-5-15]: [ANK 20200517-2](https://www.vekn.net/forum/rules-questions/78629-damage-prevention-windows-what-can-you-soak?start=6#99855) [ANK 20170427](https://www.vekn.net/forum/rules-questions/75755-resolution-card-blood-of-acid?start=6#81627) [LSJ 20040805](https://groups.google.com/g/rec.games.trading-cards.jyhad/c/WuER8RUMzTE/m/OmQhmQFkFLkJ) [LSJ 20100205](https://groups.google.com/g/rec.games.trading-cards.jyhad/c/owQe9egif0U/m/84l6snr9RWIJ) — {Blood of Acid}, {Tunnel Runner}, {Potio Martyrium}.
[^4-5-16]: [ANK 20170930](https://www.vekn.net/forum/rules-questions/76197-still-confused-about-multiple-outside-the-hourglasses#83682) — {Outside the Hourglass}, {Weather Control}.
[^4-5-17]: [LSJ 20010627](https://groups.google.com/g/rec.games.trading-cards.jyhad/c/NhNCVCCDyU0/m/I5Yph3-UUPsJ) [LSJ 20010629](https://groups.google.com/g/rec.games.trading-cards.jyhad/c/MhHKBY7II78/m/EyI_ise9M-kJ) [LSJ 20090304-1](https://groups.google.com/g/rec.games.trading-cards.jyhad/c/B7EQiAVOr1Q/m/gg-GkqQBRp8J) [RBK damage-resolution](https://www.vekn.net/rulebook#damage-resolution) — group "Immune to damage" (G00026), {Bloodform}, {Ignore the Searing Flames}.
[^4-5-18]: [LSJ 20040120](https://groups.google.com/g/rec.games.trading-cards.jyhad/c/5zBRtwg6lpU/m/MMisbKi7_Z0J) — {Ex Nihilo}.
[^4-5-19]: [RTR 19941109](https://groups.google.com/d/msg/rec.games.deckmaster/_6CXoKTSLnw/FdG67-3HEAQJ) [ANK 20180612](https://www.vekn.net/forum/rules-questions/76717-retainers-damage-and-disciplines#88129) [ANK 20211127](https://www.vekn.net/forum/rules-questions/76687-retainers-inflicting-damage-environmental?start=6#104017) — {Charnas the Imp}, group "Retainer doing damage" (G00016).
[^4-5-20]: [LSJ 20040802](https://groups.google.com/g/rec.games.trading-cards.jyhad/c/b6V_OGl-TgE/m/bi8evHga9X8J) [LSJ 20100519](https://groups.google.com/g/rec.games.trading-cards.jyhad/c/criytfhw97o/m/sj9_vGAi-xQJ) [LSJ 19990106-2](https://groups.google.com/g/rec.games.trading-cards.jyhad/c/6dDhJmBlpXY/m/4b0RVRiwmXAJ) — {Improvised Flamethrower}, {Weighted Walking Stick}, {Fleshcraft}, {Bonecraft}.
[^4-5-21]: [LSJ 20090622-2](https://groups.google.com/g/rec.games.trading-cards.jyhad/c/1zt1SZb2TIk/m/CYNhVovmlk8J) — {Coma}, {Rowan Ring}, {Rabbat, The Sewer Goddess}, {Seren Sukardi}.
[^4-6-1]: [RTR 20041202](https://groups.google.com/g/rec.games.trading-cards.jyhad/c/WUWh7AdooDU/m/vojisZMCSnsJ) [LSJ 19980526](https://groups.google.com/g/rec.games.trading-cards.jyhad/c/tRTwM9wYaVI/m/jdC09vmHk3kJ) [LSJ 19980219](https://groups.google.com/g/rec.games.trading-cards.jyhad/c/FoVObdCLJPM/m/Wb6cYwW6-jMJ) [ANK 20220923](https://www.vekn.net/forum/rules-questions/80044-enhanced-coagulant-vs-dodge#106405) [ANK 20200909](https://www.vekn.net/forum/rules-questions/78845-contagion-corruption-counters-vs-strike-dodge#100726) [LSJ 20040130](https://groups.google.com/g/rec.games.trading-cards.jyhad/c/wvuR79dNCDU/m/z4C2L5NCgg8J) [LSJ 20051020](https://groups.google.com/g/rec.games.trading-cards.jyhad/c/jqPoW66sEkY/m/RH3yS-8MQCoJ) — {Serpent's Numbing Kiss}, {Morphean Blow}, {Oubliette}, {Rowan Ring}, {Enhanced Coagulant}, {Contagion}, {Blissful Agony}.
[^4-6-2]: [LSJ 20040928](https://groups.google.com/g/rec.games.trading-cards.jyhad/c/GBcR6aNjIk4/m/DXPyqBM1R8kJ) — {Blood Fury}, {Blood Rage}, {Personal Scourge}, {Soul Burn}.
[^4-6-3]: [LSJ 19990106-2](https://groups.google.com/g/rec.games.trading-cards.jyhad/c/6dDhJmBlpXY/m/4b0RVRiwmXAJ) — {Fleshcraft}, {Bonecraft}.
[^4-6-4]: [RTR 19941109](https://groups.google.com/d/msg/rec.games.deckmaster/_6CXoKTSLnw/FdG67-3HEAQJ) [TOM 19951216](https://groups.google.com/g/rec.games.trading-cards.jyhad/c/0G-jqB_fcyE/m/8jUhfCXRtPUJ) [PIB 20140324](https://www.vekn.net/forum/rules-questions/60259-carrion-crows-first-strike-strikes-not-anaesthetic-touch?start=0#60260) [ANK 20200422](https://www.vekn.net/forum/rules-questions/78582-thoughts-betrayed-interaction-with-different-striking-situation#99680) [RBK strike-effects](https://www.vekn.net/rulebook#strike-effects) — group "Environmental damage" (G00017), {Conscripted Statue}, {Darkling Trickery}, {Thoughts Betrayed}.
[^4-6-5]: [ANK 20200517](https://www.vekn.net/forum/rules-questions/78638-transfusion-and-elemental-damage#99853) — {Necrosis}.
[^4-6-6]: [LSJ 20011210-2](https://groups.google.com/g/rec.games.trading-cards.jyhad/c/mUwzyHLcAx8/m/GghxO9mnnTIJ) [LSJ 20011005](https://groups.google.com/g/rec.games.trading-cards.jyhad/c/9fyH2X1YGAQ/m/r8ZViiGnRzoJ) [ANK 20211102](https://www.vekn.net/forum/rules-questions/79447-rotschreck-and-dodge#103743) [RBK strike-effects](https://www.vekn.net/rulebook#strike-effects) — {Anesthetic Touch}, {Rötschreck}.
[^4-6-7]: [RTR 20041202](https://groups.google.com/g/rec.games.trading-cards.jyhad/c/WUWh7AdooDU/m/vojisZMCSnsJ) [LSJ 20060808](https://groups.google.com/g/rec.games.trading-cards.jyhad/c/ncZn3knH-Uo/m/sBjnMxAk1msJ) [ANK 20210612](https://www.vekn.net/forum/rules-questions/79173-confirmation-needed-about-garrote?start=6#102470) [LSJ 20020416-2](https://groups.google.com/g/rec.games.trading-cards.jyhad/c/tEC5uN8yqUE/m/czJYA-Pt00sJ) — {Flash Grenade}, {Garrote}.
[^4-6-8]: [LSJ 20030902-2](https://groups.google.com/g/rec.games.trading-cards.jyhad/c/mgZt4f2LyOg/m/FCeKmePPkxwJ) [LSJ 20060808-1](https://groups.google.com/g/rec.games.trading-cards.jyhad/c/7oK-hKbOs9g/m/EGeyVt3vfl4J) — {Collapse the Arches}, {Scorpion Sting}, {Projectile}, {Shadow Feint}.
[^4-6-9]: [LSJ 20010919](https://groups.google.com/g/rec.games.trading-cards.jyhad/c/08AhThj0IxI/m/ZmMxUKqbymIJ) [ANK 20180913-1](https://www.vekn.net/forum/rules-questions/77003-stutter-step-question#90610) — {Stutter-Step}.
[^4-7-1]: [LSJ 19981006](https://groups.google.com/g/rec.games.trading-cards.jyhad/c/RU5yM2Ov5Mg/m/n8Phcid1tCQJ) [LSJ 20001127-2](https://groups.google.com/g/rec.games.trading-cards.jyhad/c/KInac4MQMuA/m/LnpxH08HVbMJ) [LSJ 20010806-1](https://groups.google.com/g/rec.games.trading-cards.jyhad/c/PuawBcgSIKI/m/D7zOKJXQDbMJ) [LSJ 20010627](https://groups.google.com/g/rec.games.trading-cards.jyhad/c/NhNCVCCDyU0/m/I5Yph3-UUPsJ) [LSJ 20070508](https://groups.google.com/g/rec.games.trading-cards.jyhad/c/FOLkbrSh0Ns/m/Kbt2Ox1GBI8J) — {Bomb}, {Jar of Skin Eaters}, {Waxen Poetica}, {White Phosphorus Grenade}, {Dragon's Breath Rounds}, {Elixir of Distillation}, {Escaped Mental Patient}.
[^4-7-2]: [LSJ 20051123](https://groups.google.com/g/rec.games.trading-cards.jyhad/c/Ww3zSY8cVNs/m/QVDV21-IjysJ) [ANK 20200203-1](https://www.vekn.net/forum/rules-questions/78416-molotov-vs-combat-ends#98878) [LSJ 19980219](https://groups.google.com/g/rec.games.trading-cards.jyhad/c/FoVObdCLJPM/m/Wb6cYwW6-jMJ) [ANK 20220923](https://www.vekn.net/forum/rules-questions/80044-enhanced-coagulant-vs-dodge#106405) [RTR 20020501](https://groups.google.com/g/rec.games.trading-cards.jyhad/c/M1snoR2msbQ/m/RFwCmX3anDkJ) — {Darkness Within}, {Molotov Cocktail}, {Rowan Ring}, {Internal Recursion}.
[^4-7-3]: [LSJ 20001127-2](https://groups.google.com/g/rec.games.trading-cards.jyhad/c/KInac4MQMuA/m/LnpxH08HVbMJ) [LSJ 20010806-1](https://groups.google.com/g/rec.games.trading-cards.jyhad/c/PuawBcgSIKI/m/D7zOKJXQDbMJ) — {Flash Grenade}, {Smoke Grenade}.
[^4-7-4]: [ANK 20211130](https://www.vekn.net/forum/rules-questions/66960-re-gianna-di-canneto?start=6#104061) [RTR 19941109](https://groups.google.com/d/msg/rec.games.deckmaster/_6CXoKTSLnw/FdG67-3HEAQJ) [TOM 19951216](https://groups.google.com/g/rec.games.trading-cards.jyhad/c/0G-jqB_fcyE/m/8jUhfCXRtPUJ) [PIB 20140324](https://www.vekn.net/forum/rules-questions/60259-carrion-crows-first-strike-strikes-not-anaesthetic-touch?start=0#60260) [ANK 20200422](https://www.vekn.net/forum/rules-questions/78582-thoughts-betrayed-interaction-with-different-striking-situation#99680) [RBK first-strike](https://www.vekn.net/rulebook#first-strike) — {Gianna di Canneto}, group "Environmental damage" (G00017).
[^4-7-5]: [ANK 20190412](https://www.vekn.net/forum/rules-questions/77543-strike-restriction-and-dog-pack?start=6#94497) — {Dog Pack}.
[^4-7-6]: [LSJ 20011005](https://groups.google.com/g/rec.games.trading-cards.jyhad/c/9fyH2X1YGAQ/m/r8ZViiGnRzoJ) [ANK 20211102](https://www.vekn.net/forum/rules-questions/79447-rotschreck-and-dodge#103743) [LSJ 19990217](https://groups.google.com/g/rec.games.trading-cards.jyhad/c/9Bsf2LC1274/m/pHWAxcO_7pgJ) [LSJ 20020715](https://groups.google.com/g/rec.games.trading-cards.jyhad/c/-FBxPz-oms0/m/OV6b9Cc6nl4J) [LSJ 20060803](https://groups.google.com/g/rec.games.trading-cards.jyhad/c/z8Nd8EFQsKc/m/sP8_LxnEpEIJ) — {Rötschreck}.
[^4-7-7]: [LSJ 20011210-1](https://groups.google.com/g/rec.games.trading-cards.jyhad/c/mUwzyHLcAx8/m/BFFVIH0Ha2kJ) [LSJ 20011210-2](https://groups.google.com/g/rec.games.trading-cards.jyhad/c/mUwzyHLcAx8/m/GghxO9mnnTIJ) [LSJ 20011210-3](https://groups.google.com/g/rec.games.trading-cards.jyhad/c/mUwzyHLcAx8/m/u4tViuMvZDUJ) [LSJ 20071112](https://groups.google.com/g/rec.games.trading-cards.jyhad/c/2fFyhL6YqI0/m/-zsMEGtt4qEJ) — {Anesthetic Touch}, {Autonomic Mastery}.
[^4-8-1]: [TOM 19960521](https://groups.google.com/g/rec.games.trading-cards.jyhad/c/poYD3n0TKGo/m/xvU5HW7lBxMJ) — {Immortal Grapple}, {Dust to Dust}, {Chameleon's Colors}, and 33 further cards carrying the same wording.
[^4-8-2]: [ANK 20180110](https://www.vekn.net/forum/rules-questions/76362) — {Undead Persistence} (ruling removed from the database when group "Optional press" (G00096) was created; original verified at vekn.net forum thread 76362).
[^4-8-3]: [PIB 20150121](https://www.vekn.net/forum/rules-questions/68745-presses-outside-of-the-press-step?start=0#68757) — {Aeron}, {Don Caravelli}, and six further crypt cards carrying the same wording.
[^4-8-4]: [LSJ 20051016](https://groups.google.com/g/rec.games.trading-cards.jyhad/c/s_At5syL66k/m/1eGsxyhDn1YJ) [LSJ 20051017](https://groups.google.com/g/rec.games.trading-cards.jyhad/c/s_At5syL66k/m/bCvu2ks001gJ) [TOM 19960521](https://groups.google.com/g/rec.games.trading-cards.jyhad/c/poYD3n0TKGo/m/xvU5HW7lBxMJ) — {Talbot's Chainsaw}, {Lorrie Dunsirn}, {Chameleon's Colors}, {Mighty Grapple}.
[^4-8-5]: [ANK 20200525-1](https://www.vekn.net/forum/rules-questions/78650-trap-and-boxed-in#99933) — {Trap}.
[^4-8-6]: [LSJ 20040521](https://groups.google.com/g/rec.games.trading-cards.jyhad/c/Giv8nDnYVGo/m/RODFe7KlT1UJ) — {Trap}.
[^4-8-7]: [ANK 20230114](https://www.vekn.net/forum/rules-questions/80258-rigor-mortis-and-aid-from-bats-and-other-manuver-strike-cards?start=6#107195) — {Rigor Mortis}.
[^4-8-8]: [RTR 19970630](https://groups.google.com/g/rec.games.trading-cards.jyhad/c/KireUeOYY3c/m/t6ifm9lur1kJ) — {Drawing Out the Beast}.
[^4-9-1]: [RTR 20030519](https://groups.google.com/g/rec.games.trading-cards.jyhad/c/NOBWXWrd-vA/m/iEOpQp1uhvAJ) — {Disarm}, {Pulled Fangs}, {Revelation of Wrath}, {Street Cred}, {Taste of Vitae}, {Ossian}, {Masochism}.
[^4-9-2]: [LSJ 20021113](https://groups.google.com/g/rec.games.trading-cards.jyhad/c/df2P8YHZex8/m/mGCmsxDjI_YJ) [ANK 20191219](https://www.vekn.net/forum/rules-questions/78241-relentless-reaper-vs-blissful-agony-and-scheduled-combat-rulings-ambiguity#98308) [ANK 20180910-1](https://www.vekn.net/forum/rules-questions/76990-correct-order-impulse-for-combat-cards-after-combat#90517) — {Disarm}, {Pulled Fangs}, {Street Cred}, {Taste of Vitae}, {Telepathic Tracking}, {Relentless Reaper}.
[^4-9-3]: [RTR 20001020](https://groups.google.com/g/rec.games.trading-cards.jyhad/c/GvxNYsYsWJ4/m/EY7NOjdsGCsJ) [LSJ 20001024](https://groups.google.com/g/rec.games.trading-cards.jyhad/c/GvxNYsYsWJ4/m/8PDeV_mQ8XEJ) [LSJ 20011214-4](https://groups.google.com/g/rec.games.trading-cards.jyhad/c/RSCjaaZXY28/m/IQxqjgU_oUsJ) — {Elysium: The Arboretum}, {Alpha Glint}, {Garibaldi-Meucci Museum}, {Ashes to Ashes}.
[^4-9-4]: [ANK 20180910-2](https://www.vekn.net/forum/rules-questions/76990-correct-order-impulse-for-combat-cards-after-combat?start=6#90521) [ANK 20191221](https://www.vekn.net/forum/rules-questions/76990-correct-order-impulse-for-combat-cards-after-combat#90516) [ANK 20180618](https://www.vekn.net/forum/rules-questions/76735-loving-agony-timing#88268) — {Death Seeker}, {Terror Frenzy}, {Loving Agony}.
[^4-9-5]: [RTR 20030519](https://groups.google.com/g/rec.games.trading-cards.jyhad/c/NOBWXWrd-vA/m/iEOpQp1uhvAJ) [LSJ 20021113](https://groups.google.com/g/rec.games.trading-cards.jyhad/c/df2P8YHZex8/m/mGCmsxDjI_YJ) [ANK 20191219](https://www.vekn.net/forum/rules-questions/78241-relentless-reaper-vs-blissful-agony-and-scheduled-combat-rulings-ambiguity#98308) [ANK 20180910-1](https://www.vekn.net/forum/rules-questions/76990-correct-order-impulse-for-combat-cards-after-combat#90517) — {Psyche!}.
[^4-9-6]: [ANK 20191219](https://www.vekn.net/forum/rules-questions/78241-relentless-reaper-vs-blissful-agony-and-scheduled-combat-rulings-ambiguity#98308) — {Psyche!}, {Telepathic Tracking}.
[^4-9-7]: [LSJ 19980109](https://groups.google.com/g/rec.games.trading-cards.jyhad/c/d2U51Uw0Hfg/m/uIPoVvPFePgJ) [RTR 20020501](https://groups.google.com/g/rec.games.trading-cards.jyhad/c/M1snoR2msbQ/m/RFwCmX3anDkJ) [ANK 20180928-2](https://www.vekn.net/forum/rules-questions/77035-questions-about-marie-pierre#90826) — {Psyche!}, {Fast Reaction}, {Haven Hunting}, {Akram}, {Jalal Sayad}, {Marie-Pierre}.
[^4-9-8]: [RTR 19970630](https://groups.google.com/g/rec.games.trading-cards.jyhad/c/KireUeOYY3c/m/t6ifm9lur1kJ) [RTR 20020501](https://groups.google.com/g/rec.games.trading-cards.jyhad/c/M1snoR2msbQ/m/RFwCmX3anDkJ) [LSJ 20030717](https://groups.google.com/g/rec.games.trading-cards.jyhad/c/IkMD8wfAcqw/m/2OdnRU3Q1AQJ) — {Mummify}, {Meld with the Land}, {Bond with the Mountain}, {Earth Meld}, {Majesty}, {Loving Agony}.
[^4-9-9]: [RTR 20020501](https://groups.google.com/g/rec.games.trading-cards.jyhad/c/M1snoR2msbQ/m/RFwCmX3anDkJ) [LSJ 20040602](https://groups.google.com/g/rec.games.trading-cards.jyhad/c/bEvYg3Za-fc/m/eK2rBRFelmoJ) [LSJ 20071009](https://groups.google.com/g/rec.games.trading-cards.jyhad/c/vSI2MhyB710/m/QweM8isk3f0J) [LSJ 20021126](https://groups.google.com/g/rec.games.trading-cards.jyhad/c/9Ui7pesvu5g/m/P4p-nKZa6lQJ) — {Smoke Grenade}, {Flash Grenade}, {Rötschreck}, {Morphean Blow}, {Legacy of Power}, {Illusions of the Kindred}.
[^4-9-10]: [RTR 19970630](https://groups.google.com/g/rec.games.trading-cards.jyhad/c/KireUeOYY3c/m/t6ifm9lur1kJ) [RTR 20020501](https://groups.google.com/g/rec.games.trading-cards.jyhad/c/M1snoR2msbQ/m/RFwCmX3anDkJ) [ANK 20180420-1](https://www.vekn.net/forum/rules-questions/76522-majesty-against-serpent-s-numbing-kiss#86272) [ANK 20200705](https://www.vekn.net/forum/rules-questions/66086-serpent-s-numbing-kiss?start=6#100266) — {Catatonic Fear}, {Riposte}, {Serpent's Numbing Kiss}, {Mercy for the Weak}, {Unholy Penance}, {Mariel, Lady Thunder}, {Oubliette}.
[^4-9-11]: [ANK 20170111](https://www.vekn.net/forum/rules-questions/72635-dam-the-heart-s-river-and-catatonic-fear?start=6#80117) [LSJ 20071011](https://groups.google.com/g/rec.games.trading-cards.jyhad/c/GSQqnAEBkgU/m/gFKF1ltY4JEJ) [LSJ 19980225](https://groups.google.com/g/rec.games.trading-cards.jyhad/c/62y-5miA8MQ/m/EhtcS-ia9b8J) — {Dam the Heart's River}, {Anathema}.
[^4-9-12]: [LSJ 20001127-2](https://groups.google.com/g/rec.games.trading-cards.jyhad/c/KInac4MQMuA/m/LnpxH08HVbMJ) [LSJ 20010806-1](https://groups.google.com/g/rec.games.trading-cards.jyhad/c/PuawBcgSIKI/m/D7zOKJXQDbMJ) [LSJ 19981006](https://groups.google.com/g/rec.games.trading-cards.jyhad/c/RU5yM2Ov5Mg/m/n8Phcid1tCQJ) [ANK 20200203-1](https://www.vekn.net/forum/rules-questions/78416-molotov-vs-combat-ends#98878) — {Grenade}, {Smoke Grenade}, {Molotov Cocktail}, {Elixir of Distillation}, {Waxen Poetica}, {White Phosphorus Grenade}.
[^4-9-13]: [ANK 20180104](https://www.vekn.net/forum/rules-questions/76356-illusions-of-the-kindred-vs-outside-the-hourglass#84724) [LSJ 19971110](https://groups.google.com/g/rec.games.trading-cards.jyhad/c/IlQdghRurtM/m/STZjah9cGbAJ) [ANK 20190725](https://www.vekn.net/forum/rules-questions/77813-card-questions#95969) — {Outside the Hourglass}, {Weather Control}.
[^4-9-14]: [LSJ 19980109](https://groups.google.com/g/rec.games.trading-cards.jyhad/c/d2U51Uw0Hfg/m/uIPoVvPFePgJ) [RTR 20020501](https://groups.google.com/g/rec.games.trading-cards.jyhad/c/M1snoR2msbQ/m/RFwCmX3anDkJ) [LSJ 20031123](https://groups.google.com/g/rec.games.trading-cards.jyhad/c/HvM2cHJ6yIo/m/jsb4iRoNdWkJ) — {Form of Mist}, {Chameleon's Colors}, {Mirror Image}.
[^4-9-15]: [RTR 20020501](https://groups.google.com/g/rec.games.trading-cards.jyhad/c/M1snoR2msbQ/m/RFwCmX3anDkJ) [LSJ 19971003](https://groups.google.com/g/rec.games.trading-cards.jyhad/c/mUZ2704tVsk/m/K4b9NjIeDhwJ) [LSJ 20021121](https://groups.google.com/g/rec.games.trading-cards.jyhad/c/UddkVI7G8iA/m/qqR2EMYZKIYJ) [LSJ 20090826](https://groups.google.com/g/rec.games.trading-cards.jyhad/c/KTwa1Hf_gHI/m/IlgyfFaqqeEJ) — {Psyche!}, {Akram}, {Jalal Sayad}, {Siren's Lure}, {Illusions of the Kindred}, {Pocket Out of Time}.
[^4-9-16]: [ANK 20220429](https://www.vekn.net/forum/rules-questions/79754-heavens-gate-new-wording#105112) [LSJ 20100604-1](https://groups.google.com/g/rec.games.trading-cards.jyhad/c/Tr3X4DsZr-8/m/DMXtyDoNqLIJ) [LSJ 20020509](https://groups.google.com/g/rec.games.trading-cards.jyhad/c/-dqteu2lStc/m/0b9C4HuqvUgJ) — {Hidden Lurker}, {Psyche!}, {Blissful Agony}, {Pocket Out of Time}, {Left for Dead}, {Heaven's Gate}.
[^4-9-17]: [LSJ 20021213](https://groups.google.com/g/rec.games.trading-cards.jyhad/c/Puk_eXStfE8/m/jBRJ7bleXP4J) [ANK 20170918-2](https://www.vekn.net/forum/rules-questions/76178-siren-s-lure-and-heidelberg-castle-timing-question#83580) [LSJ 19991025](https://groups.google.com/g/rec.games.trading-cards.jyhad/c/R94tyTGJ6VQ/m/KxvkGm1aon8J) — {Psyche!}, {Siren's Lure}, {Obedience}.
[^4-9-18]: [ANK 20230527](https://www.vekn.net/forum/rules-questions/80553-blithe-acceptance-and-multiple-combat#108178) [LSJ 20010814](https://groups.google.com/g/rec.games.trading-cards.jyhad/c/z7uYIO39YCo/m/aufoimHncvQJ) [LSJ 20010813](https://groups.google.com/g/rec.games.trading-cards.jyhad/c/8MR4bq0Cxj4/m/f_rAOuj3CboJ) [LSJ 20010819-2](https://groups.google.com/g/rec.games.trading-cards.jyhad/c/8MR4bq0Cxj4/m/YgNsk8nGcREJ) [LSJ 20030530](https://groups.google.com/g/rec.games.trading-cards.jyhad/c/SZehI8SwAc4/m/shpyPIdsHxUJ) [LSJ 20001122](https://groups.google.com/g/rec.games.trading-cards.jyhad/c/Br8FPS5mRn4/m/EUCAQhATZC8J) — {Blithe Acceptance}, {Sniper Rifle}, {Scry the Hearthstone}, {Raptor}, {Psyche!}.
[^4-9-19]: [ANK 20200420-1](https://www.vekn.net/forum/rules-questions/78576-amelia-the-blood-red-tears#99641) — {Amelia, The Blood Red Tears}.
[^4-9-20]: [ANK 20230314](https://www.vekn.net/forum/rules-questions/80378-monster-vs-provision-of-silsila#107622) [ANK 20180928-2](https://www.vekn.net/forum/rules-questions/77035-questions-about-marie-pierre#90826) [RTR 19980623](https://groups.google.com/g/rec.games.trading-cards.jyhad/c/tSpd9dtTElc/m/-CuHJF54_n0J) [LSJ 20040219](https://groups.google.com/g/rec.games.trading-cards.jyhad/c/zFmoLa6tzWA/m/eJnERTCB-NEJ) [ANK 20221130](https://www.vekn.net/forum/rules-questions/80176-cats-guidance-before-psyche-combat?start=0#106906) — {Provision of the Silsila}, {Marie-Pierre}, {Cats' Guidance}.
[^4-9-21]: [ANK 20180910-1](https://www.vekn.net/forum/rules-questions/76990-correct-order-impulse-for-combat-cards-after-combat#90517) [LSJ 20060903](https://groups.google.com/g/rec.games.trading-cards.jyhad/c/QAKz6Qtr7Ts/m/kyhzKIdtR54J) [LSJ 20080821](https://groups.google.com/g/rec.games.trading-cards.jyhad/c/hZF1Joxwc2s/m/o1FSURsGv0wJ) — {Yawp Court}.
[^4-9-22]: [LSJ 20030214](https://groups.google.com/g/rec.games.trading-cards.jyhad/c/A3U-Dy1yx8Y/m/2LHXvLrmybwJ) [ANK 20190624](https://www.vekn.net/forum/rules-questions/77737-undead-persistence-and-psyche#95596) [LSJ 20020211](https://groups.google.com/g/rec.games.trading-cards.jyhad/c/ubqDaLeG3qo/m/TGKL07dP8NkJ) [LSJ 20021122](https://groups.google.com/g/rec.games.trading-cards.jyhad/c/LieFYA_gyFo/m/Ma_4_gNijmoJ) — {Undead Persistence}, {Ashes to Ashes}.
[^4-10-1]: [LSJ 19971215](https://groups.google.com/g/rec.games.trading-cards.jyhad/c/mfBmRrUKZQ0/m/5Py-ENuzoGwJ) [LSJ 20030213-2](https://groups.google.com/g/rec.games.trading-cards.jyhad/c/Jwj7VjhFU5o/m/VbR1wZ23gvIJ) [LSJ 20050304](https://groups.google.com/g/rec.games.trading-cards.jyhad/c/X5JZBbSIj3U/m/CBdkcQ-rAesJ) — {Talbot's Chainsaw}, {Starshell Grenade Launcher}, {Banshee Ironwail}, {Sword of Judgment}, {Projectile}.
[^4-10-2]: [LSJ 20021028](https://groups.google.com/g/rec.games.trading-cards.jyhad/c/g0GGiVIxyis/m/35WA-O9XrroJ) [LSJ 20001126](https://groups.google.com/g/rec.games.trading-cards.jyhad/c/ZK97Kk4WQ00/m/SJPz6uc5Xw8J) [LSJ 20050224-3](https://groups.google.com/g/rec.games.trading-cards.jyhad/c/tzl6213crbI/m/HlnYVX9L3fAJ) — groups "Strikes with optional maneuver" (G00024) and "Cannot strike" (G00093), {Deer Rifle}, {Lapse}, {Projectile}.
[^4-10-3]: [LSJ 20021028](https://groups.google.com/g/rec.games.trading-cards.jyhad/c/g0GGiVIxyis/m/35WA-O9XrroJ) — {Sniper Rifle}.
[^4-10-4]: [ANK 20230316](https://www.vekn.net/forum/rules-questions/80385-amulet-of-temporal-perception-burning-and-reuse#107638) [LSJ 19980302-2](https://groups.google.com/g/rec.games.trading-cards.jyhad/c/9YVFkeiL3Js/m/4UZXMyicluwJ) [ANK 20220207](https://www.vekn.net/forum/rules-questions/79639-hunger-of-marduk-and-additional-strike#104645) — groups "Weapon once per combat" (G00045) and "Weapon once per round" (G00046), {.44 Magnum}, {Hunger of Marduk}.
[^4-10-5]: [RTR 19980623](https://groups.google.com/g/rec.games.trading-cards.jyhad/c/tSpd9dtTElc/m/-CuHJF54_n0J) [LSJ 20020821](https://groups.google.com/g/rec.games.trading-cards.jyhad/c/o_nBNZraMvE/m/g0xPNLGquKIJ) [LSJ 20020904](https://groups.google.com/g/rec.games.trading-cards.jyhad/c/Qmi4hFk6QqE/m/VmoU2tfLMgEJ) [LSJ 19970224](https://groups.google.com/g/rec.games.trading-cards.jyhad/c/80KRDjVFkyg/m/TBJso9Ra_9QJ) — {Machine Blitz}, {Concealed Weapon}, {Illegal Search and Seizure}.
[^4-10-6]: [LSJ 20010806-1](https://groups.google.com/g/rec.games.trading-cards.jyhad/c/PuawBcgSIKI/m/D7zOKJXQDbMJ) — {Machine Blitz}.
[^4-10-7]: [LSJ 20060825](https://groups.google.com/g/rec.games.trading-cards.jyhad/c/2usG7ml8BAw/m/Xa1o5-C1dSAJ) [LSJ 20051220](https://groups.google.com/g/rec.games.trading-cards.jyhad/c/bIcX7F3wzf0/m/Oi91XAFSwKUJ) [LSJ 20090304-1](https://groups.google.com/g/rec.games.trading-cards.jyhad/c/B7EQiAVOr1Q/m/gg-GkqQBRp8J) [LSJ 20100514](https://groups.google.com/g/rec.games.trading-cards.jyhad/c/Mz_fcIldfAY/m/Ys_W0MtwqLgJ) [LSJ 20091123-2](https://groups.google.com/g/rec.games.trading-cards.jyhad/c/_IwgQEvViWQ/m/1g36C5Y2BSoJ) — {Anachronism}, {Kerrie}, {Talbot's Chainsaw}, {Nephandus}.
[^4-10-8]: [PIB 20141026](https://www.vekn.net/forum/rules-questions/66960-gianna-di-canneto#66971) [LSJ 19980319](https://groups.google.com/g/rec.games.trading-cards.jyhad/c/i1Eqqm5Ctv0/m/TQIvuprMrjsJ) [RBK strike-effects](https://www.vekn.net/rulebook#strike-effects) — {Gianna di Canneto}, {Disguised Weapon}.
[^4-10-9]: [LSJ 19981006](https://groups.google.com/g/rec.games.trading-cards.jyhad/c/RU5yM2Ov5Mg/m/n8Phcid1tCQJ) [LSJ 20001127-2](https://groups.google.com/g/rec.games.trading-cards.jyhad/c/KInac4MQMuA/m/LnpxH08HVbMJ) [LSJ 20010806-1](https://groups.google.com/g/rec.games.trading-cards.jyhad/c/PuawBcgSIKI/m/D7zOKJXQDbMJ) [RTR 20020501](https://groups.google.com/g/rec.games.trading-cards.jyhad/c/M1snoR2msbQ/m/RFwCmX3anDkJ) [LSJ 20040602](https://groups.google.com/g/rec.games.trading-cards.jyhad/c/bEvYg3Za-fc/m/eK2rBRFelmoJ) — {Grenade}, {Dragon's Breath Rounds}, {Jar of Skin Eaters}, {Smoke Grenade}.
[^4-10-10]: [RTR 20010710](https://groups.google.com/g/rec.games.trading-cards.jyhad/c/GsI1UyH54jU/m/x9LfDZX1vR4J) [LSJ 20010729](https://groups.google.com/g/rec.games.trading-cards.jyhad/c/RkvrP5tplXA/m/Wr-EQ_G0g_IJ) — {Hand of Conrad}, {Drum of Xipe Totec}, {Soul Gem of Etrius}.
[^4-10-11]: [LSJ 20020425](https://groups.google.com/g/rec.games.trading-cards.jyhad/c/_Rh8P34zTZo/m/u-WavRjp5uYJ) — group "Improve weapon before resolution" (G00050).
[^5-1-1]: [RTR 19990712](https://groups.google.com/g/rec.games.trading-cards.jyhad/c/x5k5Vw_hkI0/m/lCqkvlUz5yIJ) [LSJ 20051103](https://groups.google.com/g/rec.games.trading-cards.jyhad/c/BD7KIWBI0Cs/m/g8vJICHAu7oJ) — {Dual Form}.
[^5-1-2]: [PIB 20140122](https://www.vekn.net/forum/rules-questions/58586-banishment-and-master-discipline#58772) [TOM 19951209](https://groups.google.com/g/rec.games.trading-cards.jyhad/c/qP2j6CpBUDI/m/2qsG4E23bl4J) [LSJ 20090625](https://groups.google.com/g/rec.games.trading-cards.jyhad/c/C3daj-vYqu4/m/2V2yTyLebHEJ) — {Banishment}, {The Becoming}.
[^5-1-3]: [LSJ 20051126](https://groups.google.com/g/rec.games.trading-cards.jyhad/c/dDgHGEG18D0/m/OMk_F9bKqW4J) [ANK 20190522](https://www.vekn.net/forum/rules-questions/77648-tariq-merge-during-influence-phase?start=12#95023) — {Hermana Hambrienta Mayor}, {Hermana Hambrienta Menor}, {Tariq, The Silent}.
[^5-1-4]: [TOM 19960210](https://groups.google.com/g/rec.games.trading-cards.jyhad/c/PiOmH08RyVw/m/CqzTRcOLDNIJ) — group "Title providing capacity" (G00038).
[^5-1-5]: [PIB 20150728](https://www.vekn.net/forum/rules-questions/72285-chameleon-v-merged-vampire#72285) [LSJ 20030519-2](https://groups.google.com/g/rec.games.trading-cards.jyhad/c/mi8M1lSCLqo/m/Rdg9SU5nA6QJ) [LSJ 20030527](https://groups.google.com/g/rec.games.trading-cards.jyhad/c/1hViTSXv544/m/nOXqGMitwP0J) — {Chameleon}, {Legendary Vampire}, {Masquerade Enforcement}.
[^5-1-6]: [ANK 20180524](https://www.vekn.net/forum/rules-questions/76595-rules-team-rulings-rtr-11-05-2018?start=60#87433) [ANK 20180523](https://www.vekn.net/forum/rules-questions/76595-rules-team-rulings-rtr-11-05-2018?start=54#87370) [LSJ 20031121-3](https://groups.google.com/g/rec.games.trading-cards.jyhad/c/JQO1RBmvV_o/m/-U5iv7M12vAJ) [RBK influence-phase](https://www.vekn.net/rulebook#influence-phase) — the [MERGED] crypt-card clause, e.g. {Goratrix}, {Dancin' Dana}, {Tariq, The Silent}.
[^5-1-7]: [ANK 20220805-2](https://www.vekn.net/forum/rules-questions/79934-merging-group-2-theo-bell-and-group-6-theo-bell-and-similar-cases#105886) [RBK influence-phase](https://www.vekn.net/rulebook#influence-phase) — {Theo Bell}.
[^5-1-8]: [RTR 19990712](https://groups.google.com/g/rec.games.trading-cards.jyhad/c/x5k5Vw_hkI0/m/lCqkvlUz5yIJ) [LSJ 20020115](https://groups.google.com/g/rec.games.trading-cards.jyhad/c/wG_tDLgfZso/m/6mKkp7Rw3OcJ) — group "Action creating vampire" (G00054).
[^5-1-9]: [LSJ 20100221](https://groups.google.com/g/rec.games.trading-cards.jyhad/c/TojSBPeGCFw/m/0FaCEfqRs3QJ) [LSJ 20070928-2](https://groups.google.com/g/rec.games.trading-cards.jyhad/c/duRrP46XygI/m/FrFYvbUYFf0J) [LSJ 20071001-2](https://groups.google.com/g/rec.games.trading-cards.jyhad/c/XoMeEYJw1ZA/m/zVM8X9aZlgQJ) — {Hatchling}, {Raw Recruit}, {Spell of Life}.
[^5-1-10]: [LSJ 20050116](https://groups.google.com/g/rec.games.trading-cards.jyhad/c/yX5rqVaarvs/m/w6JXnFytdq4J) [ANK 20170226](https://www.vekn.net/forum/rules-questions/75625-dual-form-extra-disciplines#80868) [LSJ 20071005-1](https://groups.google.com/g/rec.games.trading-cards.jyhad/c/Ugcdb0ljZrU/m/J3Gqxj_615gJ) — {Dual Form}, {Agent of Power}.
[^5-1-11]: [LSJ 20100213](https://groups.google.com/g/rec.games.trading-cards.jyhad/c/vXDkYrTmkws/m/sKy3jXz7AB4J) — {Soul Gem of Etrius}.
[^5-2-1]: [ANK 20220705](https://www.vekn.net/forum/rules-questions/79895-question-regarding-using-a-minion-card-text-ability-when-locked#105630) [LSJ 20100705](https://groups.google.com/g/rec.games.trading-cards.jyhad/c/Dm_Zqyjdx8s/m/Fw-T7QAU8mkJ) [LSJ 20001102](https://groups.google.com/g/rec.games.trading-cards.jyhad/c/LlPyLJjLdx0/m/mXimdmP14GEJ) [TOM 19960214](https://groups.google.com/g/rec.games.trading-cards.jyhad/c/AP9ub18aVjg/m/5zCfEMIz3ZEJ) — {Montano}, {Maris Streck}, {Paul Forrest, False Prophet}, {Sundown}, {Toby}, {Courier}, {Alexandra}.
[^5-2-2]: [RTR 19941109](https://groups.google.com/d/msg/rec.games.deckmaster/_6CXoKTSLnw/FdG67-3HEAQJ) [LSJ 19980210](https://groups.google.com/g/rec.games.trading-cards.jyhad/c/v7PxbzgVG0c/m/Fr0CsYqf9QMJ) [PIB 20150720](https://www.vekn.net/forum/rules-questions/72088-action-modifiers#72124) — {Cloak the Gathering}, {Echo of Harmonies}, {Mouthpiece}, {Make an Example}.
[^5-2-3]: [RTR 19941109](https://groups.google.com/d/msg/rec.games.deckmaster/_6CXoKTSLnw/FdG67-3HEAQJ) [RTR 19970425](https://groups.google.com/g/rec.games.trading-cards.jyhad/c/DhP_l2cX3mQ/m/9ZZZqL8NFSAJ) — {Disarming Presence}, {Domain Challenge}.
[^5-2-4]: [PIB 20150412](https://www.vekn.net/forum/rules-questions/70519-can-you-play-mind-rape-on-a-tapped-vampire#70528) — {Mind Rape}.
[^5-2-5]: [RTR 19951110](https://groups.google.com/g/rec.games.trading-cards.jyhad/c/TXfganI5B2o/m/QYh3AdPNbUwJ) [RTR 20010710](https://groups.google.com/g/rec.games.trading-cards.jyhad/c/GsI1UyH54jU/m/x9LfDZX1vR4J) [ANK 20200508-2](https://www.vekn.net/forum/rules-questions/78623-locked-t-j-and-referendum#99791) [ANK 20230817](https://www.vekn.net/forum/rules-questions/80780-hide-the-heart#109068) [LSJ 20020927](https://groups.google.com/g/rec.games.trading-cards.jyhad/c/wg3PH7vOs1s/m/gYFNbAwk84gJ) [RBK wording-templates](https://www.vekn.net/rulebook#wording-templates) — {Brujah Frenzy}, {Malleable Visage}, {T.J.}, {Hide the Heart}, {Force of Will}.
[^5-2-6]: [LSJ 20060911](https://groups.google.com/g/rec.games.trading-cards.jyhad/c/oznDQgIFZ-I/m/dU2xMMkxPwsJ) [PIB 20151009](https://www.vekn.net/forum/rules-questions/73577-baleful-doll#73580) [ANK 20180702](https://www.vekn.net/forum/rules-questions/76770-triggered-effects#88491) [LSJ 20010622](https://groups.google.com/g/rec.games.trading-cards.jyhad/c/65IHHAii7ms/m/kyS0uVtsbNMJ) [RBK unlock-phase](https://www.vekn.net/rulebook#unlock-phase) — {Raphael Catarari}, {Baleful Doll}, {Vampiric Disease}, {Parmenides}.
[^5-2-7]: [LSJ 20080106](https://groups.google.com/g/rec.games.trading-cards.jyhad/c/q4s1P6ozsW8/m/N9wEQl5sgTgJ) [ANK 20200629](https://www.vekn.net/forum/rules-questions/78700-arika-special-order?start=6#100211) [ANK 20220503](https://www.vekn.net/forum/rules-questions/39040-re-ex-nihilo-can-i-choose-to-burn-my-minion#105161) — {Anarch Revolt}, {Arika}, {Drink the Blood of Ahriman}.
[^5-2-8]: [PIB 20150111](https://www.vekn.net/forum/rules-questions/68580-sensory-deprivation-ruling#68584) [LSJ 20031014](https://groups.google.com/g/rec.games.trading-cards.jyhad/c/J8eZuZCZJUY/m/RsZFBMqFHKkJ) [ANK 20180917](https://www.vekn.net/forum/rules-questions/77011-condemn-the-sins-of-the-father#90639) [LSJ 20010828](https://groups.google.com/g/rec.games.trading-cards.jyhad/c/KoP_nqv-feM/m/faZPeRBTL_QJ) — {Sensory Deprivation}, {Cry Wolf}, {Temptation}.
[^5-2-9]: [LSJ 20050114](https://groups.google.com/g/rec.games.trading-cards.jyhad/c/JWiZmyC2Y6s/m/q6JHYrE1zKYJ) [ANK 20210322-2](https://www.vekn.net/forum/rules-questions/79080-nightmares-upon-nightmares?start=6#101910) — group "Prevent normal unlock" (G00005), {Nightmares upon Nightmares}.
[^5-2-10]: [PIB 20150703](https://www.vekn.net/forum/rules-questions/71918-sleeping-mind-vs-wakes#71932) — {The Sleeping Mind}.
[^5-2-11]: [ANK 20191025](https://www.vekn.net/forum/rules-questions/78050-roetschreck-controler-is-ousted#97560) [LSJ 19980831](https://groups.google.com/g/rec.games.trading-cards.jyhad/c/Za8AS17xXPM/m/Ttki0DplaeYJ) [PIB 20110915-1](https://www.vekn.net/forum/rules-questions/10264-lubomira-hradok-clarification#10266) — {Rötschreck}, {Rowan Ring}, {Lubomira Hradok}.
[^5-2-12]: [LSJ 20010814-3](https://groups.google.com/g/rec.games.trading-cards.jyhad/c/4U6VYR9kBTA/m/1OjgFwTysAYJ) [LSJ 20020109](https://groups.google.com/g/rec.games.trading-cards.jyhad/c/3aWGnESUYi0/m/8CQ3HDk-SrMJ) [RTR 20070707](https://groups.google.com/g/rec.games.trading-cards.jyhad/c/vSOt2c1uRzQ/m/MsRAv47Cd4YJ) — {Fata Amria}, {Putrefaction}.
[^5-2-13]: [PIB 20121107](https://www.vekn.net/forum/rules-questions/40504-familial-bond#40540) [LSJ 20070403](https://groups.google.com/g/rec.games.trading-cards.jyhad/c/TJ2ktt_1tjk/m/fdH_x9tDmN8J) [LSJ 20070413](https://groups.google.com/g/rec.games.trading-cards.jyhad/c/umdINigMKqs/m/lfUAxTnfttIJ) — {Familial Bond}, {Champion}, {Discern}, {Donate}.
[^5-2-14]: [LSJ 20010702](https://groups.google.com/g/rec.games.trading-cards.jyhad/c/jvIS3SDulqU/m/V8wtgvqoFOAJ) [LSJ 20011023-2](https://groups.google.com/g/rec.games.trading-cards.jyhad/c/47-PhTMiAOU/m/g4sVfXt9TmsJ) [LSJ 20100527](https://groups.google.com/g/rec.games.trading-cards.jyhad/c/Tr3X4DsZr-8/m/O06iXN6LtzsJ) — {Starshell Grenade Launcher}, {Marciana Giovanni, Investigator}.
[^5-2-15]: [LSJ 20070208](https://groups.google.com/g/rec.games.trading-cards.jyhad/c/ssk96EKyqjQ/m/VfgesEwO2FwJ) [LSJ 20041022-2](https://groups.google.com/g/rec.games.trading-cards.jyhad/c/UAhJ3vWLyMM/m/gp04WTgORSQJ) [LSJ 20100210](https://groups.google.com/g/rec.games.trading-cards.jyhad/c/HHJfsSbIEf0/m/6UxQ3UJT9aEJ) — {No Secrets From the Magaji}, {Madness Network}, {Unleash Hell's Fury}.
[^5-2-16]: [LSJ 20021011](https://groups.google.com/g/rec.games.trading-cards.jyhad/c/9WWIzxek9Nc/m/PlIwI11sNpkJ) [ANK 20231028](https://www.vekn.net/forum/rules-questions/80925-wake-timing-effects#109683) — group "Cancel as a reaction" (G00062), {Unleashing the Bestial Soul}, {Deed the Heart's Desire}, {Psalm of the Damned}.
[^5-2-19]: [ANK 20190708](https://www.vekn.net/forum/rules-questions/77776-when-can-i-play-hard-case#95800) [ANK 20171017](https://www.vekn.net/forum/rules-questions/76233-question-about-failing-to-block-faceless-night-and-playing-guard-dogs#83900) [ANK 20230305](https://www.vekn.net/forum/rules-questions/63821-re-faceless-night-x-deflection?start=36#107536) [LSJ 20080611](https://groups.google.com/g/rec.games.trading-cards.jyhad/c/gvb3uijtpZw/m/ZRX2hunjsRYJ) [ANK 20210131](https://www.vekn.net/forum/rules-questions/79008-crypt-s-sons-lock-and-obedience#101525) — {Hard Case}, {Faceless Night}, {Crypt's Sons}.
[^5-2-20]: [ANK 20191204](https://www.vekn.net/forum/rules-questions/78164-mirror-walk-change-and-guardian-vigil?start=6#98139) [ANK 20200714](https://www.vekn.net/forum/rules-questions/78742-ohoyo-hopoksia#100352) [TOM 19951007](https://groups.google.com/g/rec.games.trading-cards.jyhad/c/HUipqz0LFSw/m/pY6uEa3f8-gJ) [LSJ 19991025](https://groups.google.com/g/rec.games.trading-cards.jyhad/c/R94tyTGJ6VQ/m/KxvkGm1aon8J) — {Mirror Walk}, {Ohoyo Hopoksia (Bastet)}, {Alexandra}.
[^5-2-21]: [PIB 20121031](https://www.vekn.net/forum/rules-questions/39816-ec-2012-can-you-answer-these?start=18#39908) [LSJ 20010508](https://groups.google.com/g/rec.games.trading-cards.jyhad/c/mvfdiWb-edk/m/P_8P7VblmR0J) [ANK 20210322-2](https://www.vekn.net/forum/rules-questions/79080-nightmares-upon-nightmares?start=6#101910) [LSJ 19970707](https://groups.google.com/g/rec.games.trading-cards.jyhad/c/KWekwiRSa2I/m/9pS17rzBBDYJ) — {Anarch Troublemaker}, {Brujah Debate}, {Nightmares upon Nightmares}, {Glutton}.
[^5-2-22]: [ANK 20170227](https://www.vekn.net/forum/rules-questions/75632-untapping-an-untapped-minion-triggers#80891) [LSJ 20020408](https://groups.google.com/g/rec.games.trading-cards.jyhad/c/4LXlqwmGQGc/m/S8aQ4et5KMIJ) [ANK 20221210-2](https://www.vekn.net/forum/rules-questions/80206-derange-disease-counter-from-vampiric-disease#106970) [LSJ 20051211](https://groups.google.com/g/rec.games.trading-cards.jyhad/c/TuwXiJ8A9mo/m/Ef_5xj46lA8J) — {Vampiric Disease}, {Eze, The Demon Prince}.
[^5-2-23]: [LSJ 20060213](https://groups.google.com/g/rec.games.trading-cards.jyhad/c/ZZkDUiO9qOw/m/2j1gRMDx0BgJ) [LSJ 20060908](https://groups.google.com/g/rec.games.trading-cards.jyhad/c/CTy2GjM6-Dc/m/9OPulYVGaFcJ) — {Banishment}, {Descent into Darkness}.
[^5-2-24]: [RTR 19941109](https://groups.google.com/d/msg/rec.games.deckmaster/_6CXoKTSLnw/FdG67-3HEAQJ) [ANK 20221102](https://www.vekn.net/forum/rules-questions/80129-fall-of-london-card-rules-questions#106688) [ANK 20180517](https://www.vekn.net/forum/rules-questions/76447-rules-team-rulings-rtr-03-03-2018?start=30#87041) — {Disarming Presence}, {Mobile HQ, Operation Antigen}, {Gianna di Canneto}.
[^5-2-25]: [LSJ 20010110](https://groups.google.com/g/rec.games.trading-cards.jyhad/c/Vtm465mblX4/m/B6pCvotsfFsJ) [LSJ 20050111](https://groups.google.com/g/rec.games.trading-cards.jyhad/c/lnW6nMIX-Vw/m/iVd07z5jvu8J) [PIB 20121031](https://www.vekn.net/forum/rules-questions/39816-ec-2012-can-you-answer-these?start=18#39908) — {Heidelberg Castle, Germany}, {The Coven}.
[^5-2-26]: [ANK 20170605](https://www.vekn.net/forum/rules-questions/75862-timing-of-the-line#82113) [ANK 20230620](https://www.vekn.net/forum/rules-questions/80612-when-to-use-shard-the-line-when-action-becoems-to-expensive-after-announcement#108409) [LSJ 20090705](https://groups.google.com/g/rec.games.trading-cards.jyhad/c/3Ekxk6uQ_wo/m/Y25g9tS6qSoJ) [LSJ 20030917](https://groups.google.com/g/rec.games.trading-cards.jyhad/c/i3Ugq5AQWFI/m/TxPoXM78hFAJ) [LSJ 20080201](https://groups.google.com/g/rec.games.trading-cards.jyhad/c/y5Uoc7nEulU/m/Nbp6ZMfhj1wJ) — {The Line}, {The Shard, London}, {Eccentric Billionaire}, {Sunset Strip, Hollywood}, {Yawp Court}.
[^5-2-27]: [LSJ 20090415](https://groups.google.com/g/rec.games.trading-cards.jyhad/c/oDvJWs7majs/m/fAtt19fFsTcJ) [LSJ 20100119](https://groups.google.com/g/rec.games.trading-cards.jyhad/c/1eULCGaVcO0/m/eefMWzjoK0IJ) — {Helicopter}.
[^5-2-28]: [RTR 19970630](https://groups.google.com/g/rec.games.trading-cards.jyhad/c/KireUeOYY3c/m/t6ifm9lur1kJ) [RTR 20020501](https://groups.google.com/g/rec.games.trading-cards.jyhad/c/M1snoR2msbQ/m/RFwCmX3anDkJ) [LSJ 20030717](https://groups.google.com/g/rec.games.trading-cards.jyhad/c/IkMD8wfAcqw/m/2OdnRU3Q1AQJ) — {Bond with the Mountain}, {Meld with the Land}, {Earth Meld}, {Majesty}.
[^5-2-29]: [RTR 20041202](https://groups.google.com/g/rec.games.trading-cards.jyhad/c/WUWh7AdooDU/m/vojisZMCSnsJ) [LSJ 20060808](https://groups.google.com/g/rec.games.trading-cards.jyhad/c/ncZn3knH-Uo/m/sBjnMxAk1msJ) [LSJ 20040602](https://groups.google.com/g/rec.games.trading-cards.jyhad/c/bEvYg3Za-fc/m/eK2rBRFelmoJ) [LSJ 20040601](https://groups.google.com/g/rec.games.trading-cards.jyhad/c/bEvYg3Za-fc/m/p0CSDyi5MWkJ) [LSJ 20071009](https://groups.google.com/g/rec.games.trading-cards.jyhad/c/vSI2MhyB710/m/QweM8isk3f0J) — {Flash Grenade}, {Rötschreck}, {Loving Agony}.
[^5-3-1]: [RTR 20010710](https://groups.google.com/g/rec.games.trading-cards.jyhad/c/GsI1UyH54jU/m/x9LfDZX1vR4J) [LSJ 20040608](https://groups.google.com/g/rec.games.trading-cards.jyhad/c/p1uCHeAO7ak/m/n7qfDGYXuu4J) [LSJ 20030214](https://groups.google.com/g/rec.games.trading-cards.jyhad/c/A3U-Dy1yx8Y/m/2LHXvLrmybwJ) [LSJ 20020402](https://groups.google.com/g/rec.games.trading-cards.jyhad/c/eQCXHND3j5o/m/LMv8SYYE3OoJ) [LSJ 20050111](https://groups.google.com/g/rec.games.trading-cards.jyhad/c/lnW6nMIX-Vw/m/iVd07z5jvu8J) — {Decapitate}, {Ahriman's Demesne}, {Undead Persistence}, {Rötschreck}, {Baltimore Purge}.
[^5-3-2]: [LSJ 20021007](https://groups.google.com/g/rec.games.trading-cards.jyhad/c/wkyqKMka_F0/m/PY1IegrQszUJ) [ANK 20201122](https://www.vekn.net/forum/rules-questions/78861-revelation-of-wrath?start=6#101144) [ANK 20200926](https://www.vekn.net/forum/rules-questions/78861-revelation-of-wrath#100824) [LSJ 20100721](https://groups.google.com/g/rec.games.trading-cards.jyhad/c/Z9QNJ6SPIJM/m/g0uHQFp6G_QJ) [ANK 20210612](https://www.vekn.net/forum/rules-questions/79173-confirmation-needed-about-garrote?start=6#102470) [LSJ 20020416-2](https://groups.google.com/g/rec.games.trading-cards.jyhad/c/tEC5uN8yqUE/m/czJYA-Pt00sJ) — {Watenda}, {Revelation of Wrath}, {Orgy of Blood}, {Garrote}.
[^5-3-3]: [LSJ 20100604-1](https://groups.google.com/g/rec.games.trading-cards.jyhad/c/Tr3X4DsZr-8/m/DMXtyDoNqLIJ) [ANK 20220429](https://www.vekn.net/forum/rules-questions/79754-heavens-gate-new-wording#105112) [ANK 20180104](https://www.vekn.net/forum/rules-questions/76356-illusions-of-the-kindred-vs-outside-the-hourglass#84724) — {Hidden Lurker}, {Blissful Agony}, {Psyche!}, {Illusions of the Kindred}.
[^5-3-4]: [LSJ 20020211](https://groups.google.com/g/rec.games.trading-cards.jyhad/c/ubqDaLeG3qo/m/TGKL07dP8NkJ) [LSJ 20021122](https://groups.google.com/g/rec.games.trading-cards.jyhad/c/LieFYA_gyFo/m/Ma_4_gNijmoJ) [LSJ 20090622-2](https://groups.google.com/g/rec.games.trading-cards.jyhad/c/1zt1SZb2TIk/m/CYNhVovmlk8J) [RTR 20020501](https://groups.google.com/g/rec.games.trading-cards.jyhad/c/M1snoR2msbQ/m/RFwCmX3anDkJ) [LSJ 20020505](https://groups.google.com/g/rec.games.trading-cards.jyhad/c/ka9MajuWTAo/m/M4oCzY97K_kJ) — {Ashes to Ashes}, {Coma}, {Entombment}, {Rowan Ring}, {Rabbat, The Sewer Goddess}, {Seren Sukardi}, {Mummify}.
[^5-3-5]: [LSJ 20030214](https://groups.google.com/g/rec.games.trading-cards.jyhad/c/A3U-Dy1yx8Y/m/2LHXvLrmybwJ) [ANK 20190624](https://www.vekn.net/forum/rules-questions/77737-undead-persistence-and-psyche#95596) — {Undead Persistence}, {Undying Tenacity}.
[^5-3-6]: [LSJ 20011022](https://groups.google.com/g/rec.games.trading-cards.jyhad/c/KMg4MwD-Jn0/m/Vl-TD6DfyhoJ) [LSJ 20100902-2](https://groups.google.com/g/rec.games.trading-cards.jyhad/c/mFpx91METxM/m/ETLGtyQfvksJ) [ANK 20191218](https://www.vekn.net/forum/rules-questions/62700-re-nahir-and-research-counters?start=6#98297) [ANK 20200420-1](https://www.vekn.net/forum/rules-questions/78576-amelia-the-blood-red-tears#99641) [LSJ 20010526](https://groups.google.com/g/rec.games.trading-cards.jyhad/c/0Sy3xNbjYeU/m/VAbmQA5axSQJ) [LSJ 20010813-2](https://groups.google.com/g/rec.games.trading-cards.jyhad/c/zkKhvgZy9hA/m/8uH5sgbQaSoJ) — group "Ability usable in torpor" (G00027), {Nahir}, {Amelia, The Blood Red Tears}, {Alvaro, The Scion of Angelica}, {Lord Tremere}, {Wamukota}, {Marciana Giovanni, Investigator}.
[^5-3-8]: [LSJ 20020416](https://groups.google.com/g/rec.games.trading-cards.jyhad/c/XS0Z0P5qaew/m/5hv141ZGzTIJ) [RBK torpor](https://www.vekn.net/rulebook#torpor) — {Save Face}, {Martyr's Resilience}, {Bliss}, {Nosferatu Putrescence}.
[^5-3-9]: [PIB 20150720](https://www.vekn.net/forum/rules-questions/72088-action-modifiers#72124) [RTR 19970306](https://groups.google.com/g/rec.games.trading-cards.jyhad/c/1dlmpgX6t14/m/hNDHCjT8Ew8J) — {Cats' Guidance}, {Make an Example}.
[^5-3-10]: [LSJ 19970325](https://groups.google.com/g/rec.games.trading-cards.jyhad/c/R-t138q8688/m/Zj1Y_jlq29AJ) [RTR 19950509](https://groups.google.com/g/rec.games.trading-cards.jyhad/c/_LKyR7pdMig/m/ZvwdGmIwUnsJ) [RTR 20010710](https://groups.google.com/g/rec.games.trading-cards.jyhad/c/GsI1UyH54jU/m/x9LfDZX1vR4J) [RTR 19970306](https://groups.google.com/g/rec.games.trading-cards.jyhad/c/1dlmpgX6t14/m/hNDHCjT8Ew8J) [RBK torpor](https://www.vekn.net/rulebook#torpor) — {The Kiss of Ra}, {Madness Network}, {Blood Brother Ambush}, {Make an Example}.
[^5-3-11]: [RTR 19980623](https://groups.google.com/g/rec.games.trading-cards.jyhad/c/tSpd9dtTElc/m/-CuHJF54_n0J) [LSJ 20030103](https://groups.google.com/g/rec.games.trading-cards.jyhad/c/TUDO_4FwdyY/m/DWOwgQL850gJ) [ANK 20180906](https://www.vekn.net/forum/rules-questions/76981-freak-drive-while-going-to-torpor#90451) [ANK 20181219](https://www.vekn.net/forum/rules-questions/77232-zephyr-timing#92505) — group "Modifier after combat" (G00007), {Freak Drive}.
[^5-3-12]: [LSJ 20091203](https://groups.google.com/g/rec.games.trading-cards.jyhad/c/JBdmMh1udN8/m/5f5UX4qfOMMJ) [ANK 20240610](https://www.vekn.net/forum/rules-questions/81521-burn-option-wording-in-rulebook-v1-1?start=12#111649) [RBK unlock-phase](https://www.vekn.net/rulebook#unlock-phase) — {Emergency Powers}, {Barrenness}, {Evil Eye}, {High Orun}.
[^5-3-13]: [PIB 20150522](https://www.vekn.net/forum/rules-questions/71291-blood-doll-and-the-rack-clarity#71293) [LSJ 20010610](https://groups.google.com/g/rec.games.trading-cards.jyhad/c/KVyVn-Y_UIY/m/FmhagXANIzcJ) [ANK 20210109](https://www.vekn.net/forum/rules-questions/78983-fear-of-mekhet-and-torpor#101392) — {Blood Doll}, {Vessel}, {Secure Haven}, {Fear of Mekhet}.
[^5-3-14]: [RTR 19960124](https://groups.google.com/g/rec.games.trading-cards.jyhad/c/wF82VdVPlm0/m/cSshmBFQs-EJ) [PIB 20150522](https://www.vekn.net/forum/rules-questions/71291-blood-doll-and-the-rack-clarity#71293) [LSJ 20010623](https://groups.google.com/g/rec.games.trading-cards.jyhad/c/GN5MqcCTOo8/m/7ll40gxjFWYJ) — {Secure Haven}, {The Rack}.
[^5-3-15]: [LSJ 20010119](https://groups.google.com/g/rec.games.trading-cards.jyhad/c/XB0IvK7I6PQ/m/foA7igsB8EEJ) [RTR 19941109](https://groups.google.com/d/msg/rec.games.deckmaster/_6CXoKTSLnw/FdG67-3HEAQJ) — {Mind Rape}, {Temptation}, {Uriah Winter}.
[^5-3-16]: [LSJ 20060409](https://groups.google.com/g/rec.games.trading-cards.jyhad/c/gsFQXsCGTG4/m/q5H8FvuKksIJ) [RTR 19960112](https://groups.google.com/g/rec.games.trading-cards.jyhad/c/d3n3StNS7no/m/k2NmZFUl9fAJ) [LSJ 20081016](https://groups.google.com/g/rec.games.trading-cards.jyhad/c/GizIs4K_HiY/m/sCutpP29EgIJ) — {Shadow Court Satyr}, {Legacy of Power}, {Abjure}.
[^5-4-1]: [ANK 20210813](https://www.vekn.net/forum/rules-questions/79279-might-of-the-camarilla-burned-from-play#102903) [PIB 20130128-2](https://www.vekn.net/forum/rules-questions/44232-khazar-s-diary-question#44504) [LSJ 20100325-2](https://groups.google.com/g/rec.games.trading-cards.jyhad/c/aC6OOfaulbM/m/svWv9UqH6isJ) [LSJ 20040616](https://groups.google.com/g/rec.games.trading-cards.jyhad/c/jQkkiC3I8P8/m/uDZ--HnPtf0J) [ANK 20230317](https://www.vekn.net/forum/rules-questions/76656-unleash-hell-s-fury-tension-in-the-ranks#107653) [RBK important-terms-of-the-game](https://www.vekn.net/rulebook#important-terms-of-the-game) [RBK contested-cards](https://www.vekn.net/rulebook#contested-cards) — {Blessed Resilience}, {Khazar's Diary (Endless Night)}, {Chain of Command}, {Unleash Hell's Fury}.
[^5-4-2]: [LSJ 20090922](https://groups.google.com/g/rec.games.trading-cards.jyhad/c/UdvGbJqOeo4/m/qFeNdWilXzUJ) [ANK 20220916](https://www.vekn.net/forum/rules-questions/80030-blood-brother-ambush-taking-the-skin-minion#106354) [LSJ 20100527](https://groups.google.com/g/rec.games.trading-cards.jyhad/c/Tr3X4DsZr-8/m/O06iXN6LtzsJ) — {Draught of the Soul}, {Soul Stealing}, {Taking the Skin: Minion}, {Blood Brother Ambush}, {Conscripted Statue}, {FBI Special Affairs Division}.
[^5-4-3]: [ANK 20220507](https://www.vekn.net/forum/rules-questions/79763-damage-lifeloss-d-actions-and-trophies-predators-tranformation#105200) [LSJ 20080608](https://groups.google.com/g/rec.games.trading-cards.jyhad/c/j5ShUmUt-vM/m/E0CqmXp_R0IJ) — {Brick Laying}, {Cryptic Mission}, {Succubus}, {Consignment to Duat}, {Horseshoes}, {Jar the Soul}, {Keystone Kine}, {Smash and Grab}, {Abyssal Hunter}.
[^5-4-4]: [RTR 19960124](https://groups.google.com/g/rec.games.trading-cards.jyhad/c/wF82VdVPlm0/m/cSshmBFQs-EJ) [LSJ 20090922](https://groups.google.com/g/rec.games.trading-cards.jyhad/c/UdvGbJqOeo4/m/qFeNdWilXzUJ) [ANK 20181022](https://www.vekn.net/forum/rules-questions/77103-kamiri-wa-itherero-blocked-by-a-minion-use-of-taking-the-skin-minion?start=6#91389) [ANK 20220916](https://www.vekn.net/forum/rules-questions/80030-blood-brother-ambush-taking-the-skin-minion#106354) — {Taking the Skin: Minion}, {Soul Stealing}, {Draught of the Soul}.
[^5-4-5]: [RTR 19980623](https://groups.google.com/g/rec.games.trading-cards.jyhad/c/tSpd9dtTElc/m/-CuHJF54_n0J) [LSJ 19990119](https://groups.google.com/g/rec.games.trading-cards.jyhad/c/Iez0G178MRM/m/LywKDWeV3qAJ) [LSJ 20080212](https://groups.google.com/g/rec.games.trading-cards.jyhad/c/Yg1nZfgkpGM/m/OxDoRLREnewJ) — {Anathema}, {Political Struggle}, {Young Bloods}.
[^5-4-6]: [LSJ 20091217](https://groups.google.com/g/rec.games.trading-cards.jyhad/c/Xa8dbfnAbv0/m/xNtPZla9Py4J) [LSJ 20091217-2](http://groups.google.com/group/rec.games.trading-cards.jyhad/msg/fc284dfba7dfa9c5) [LSJ 20071003-2](https://groups.google.com/g/rec.games.trading-cards.jyhad/c/Tr9VQRVDbg0/m/EKNVTdvidvIJ) [ANK 20230816](https://www.vekn.net/forum/rules-questions/80772-heaven-s-gate-vs-charigger-the-axe#109057) [LSJ 20070507](https://groups.google.com/g/rec.games.trading-cards.jyhad/c/FOLkbrSh0Ns/m/wdtfyqkD26MJ) [LSJ 20021205](https://groups.google.com/g/rec.games.trading-cards.jyhad/c/0MhU0auTJO4/m/39sI3Lpp-6MJ) [PIB 20121028](https://www.vekn.net/forum/rules-questions/39816-ec-2012-can-you-answer-these?start=6#39843) — {Byzar}, {Charigger, The Axe}, {Escaped Mental Patient}, {FBI Special Affairs Division}.
[^5-4-7]: [ANK 20201122](https://www.vekn.net/forum/rules-questions/78861-revelation-of-wrath?start=6#101144) [ANK 20200926](https://www.vekn.net/forum/rules-questions/78861-revelation-of-wrath#100824) [LSJ 20100721](https://groups.google.com/g/rec.games.trading-cards.jyhad/c/Z9QNJ6SPIJM/m/g0uHQFp6G_QJ) [LSJ 20070417](https://groups.google.com/g/rec.games.trading-cards.jyhad/c/ecDUqbSUsNg/m/3W9aOm0MfYEJ) — {Revelation of Wrath}, {Orgy of Blood}, {Abandoning the Flesh}, {Ashes to Ashes}.
[^5-5-1]: [LSJ 20050216](https://groups.google.com/g/rec.games.trading-cards.jyhad/c/5_rUFgufFc4/m/7OVVD0KpnS4J) [ANK 20190701](https://www.vekn.net/forum/rules-questions/77763-multiple-questions#95690) [LSJ 20030815](https://groups.google.com/g/rec.games.trading-cards.jyhad/c/sf1U7vnVE-o/m/VjhroQN1NP4J) [ANK 20230621](https://www.vekn.net/forum/rules-questions/80691-procurer-recruiting-another-with-the-shard?start=12#108765) [RTR 20010710](https://groups.google.com/g/rec.games.trading-cards.jyhad/c/GsI1UyH54jU/m/x9LfDZX1vR4J) — {Codex of the Edenic Groundskeepers}, {Hide the Heart}, {Tenebrous Form}, {Étienne Fauberge}, {The Shard, London}, {Kindred Segregation}.
[^5-5-2]: [PIB 20121028](https://www.vekn.net/forum/rules-questions/39816-ec-2012-can-you-answer-these?start=6#39843) [ANK 20220818](https://www.vekn.net/forum/rules-questions/79972-is-enhanced-coagulant-still-an-equipment-after-a-successful-strike?start=6#106039) [ANK 20221102](https://www.vekn.net/forum/rules-questions/80129-fall-of-london-card-rules-questions#106688) [RTR 19971201](https://groups.google.com/g/rec.games.trading-cards.jyhad/c/zpIp5xOzQT0/m/IkqqeD6dinYJ) [RTR 19960112](https://groups.google.com/g/rec.games.trading-cards.jyhad/c/d3n3StNS7no/m/k2NmZFUl9fAJ) — {Taste of Vitae}, {Enhanced Coagulant}, {Shackles of Enkidu}, {Legacy of Power}.
[^5-5-3]: [ANK 20171109](https://www.vekn.net/forum/rules-questions/76282-ossian-and-nephandus#84174) [LSJ 20030520-2](https://groups.google.com/g/rec.games.trading-cards.jyhad/c/GcymCHOJDVY/m/bM6Z5o-beQgJ) [LSJ 20051116-1](https://groups.google.com/g/rec.games.trading-cards.jyhad/c/MfGC7sJ8vh8/m/9ylhc34zFesJ) [LSJ 20081213-3](https://groups.google.com/g/rec.games.trading-cards.jyhad/c/cbZ2jl8-yGQ/m/OJljr9wcC4sJ) [LSJ 20011214-1](https://groups.google.com/g/rec.games.trading-cards.jyhad/c/m2zsNI0McoE/m/-izuxRCo9VQJ) [LSJ 20070301](https://groups.google.com/g/rec.games.trading-cards.jyhad/c/-CeFWHQ2wXE/m/TtbyH4rAcoIJ) — {Nephandus}, {Ossian}, {Ghouled}, {Demdemeh}, {The Grandest Trick}.
[^5-5-4]: [LSJ 20080717](https://groups.google.com/g/rec.games.trading-cards.jyhad/c/DMsE6V84GWI/m/af5Oggz9XlQJ) [RTR 19970630](https://groups.google.com/g/rec.games.trading-cards.jyhad/c/KireUeOYY3c/m/t6ifm9lur1kJ) [RTR 20020501](https://groups.google.com/g/rec.games.trading-cards.jyhad/c/M1snoR2msbQ/m/RFwCmX3anDkJ) [RTR 19941109](https://groups.google.com/d/msg/rec.games.deckmaster/_6CXoKTSLnw/FdG67-3HEAQJ) [ANK 20180612](https://www.vekn.net/forum/rules-questions/76717-retainers-damage-and-disciplines#88129) — {Shadow Court Satyr}, {Charming Lobby}, {Herald of Topheth}, group "Retainer with discipline level" (G00018).
[^5-5-5]: [LSJ 20050606](https://groups.google.com/g/rec.games.trading-cards.jyhad/c/IkZS3ikg7y8/m/TrHmf3-jPvEJ) [ANK 20200605](https://www.vekn.net/forum/rules-questions/78671-can-an-ally-with-play-as-a-vampire-use-the-line-to-reduce-action-costs#100015) [LSJ 20060124](https://groups.google.com/g/rec.games.trading-cards.jyhad/c/PBEBNFH61ik/m/Fp2dosujs5YJ) [LSJ 20050224-1](https://groups.google.com/g/rec.games.trading-cards.jyhad/c/enxwleC-ZKw/m/zDDSPMF8FOYJ) [RBK allies](https://www.vekn.net/rulebook#allies) — {Veil of Darkness}, {The Line}, {Descent into Darkness}, {Sonja Blue}.
[^5-5-6]: [ANK 20180928-1](https://www.vekn.net/forum/rules-questions/77034-allies-and-vampire-disciplines-specifically-the-nocturn#90809) [LSJ 20080512](https://groups.google.com/g/rec.games.trading-cards.jyhad/c/z2DGSFph6sM/m/IjJB89nbtlsJ) — group "Allies who can play as a vampire" (G00011).
[^5-5-7]: [LSJ 20080630](https://groups.google.com/g/rec.games.trading-cards.jyhad/c/nvuXBpEaKAA/m/ymiC3yAQVOwJ) [RTR 20180303](https://www.vekn.net/forum/rules-questions/76447-rules-team-rulings-rtr-03-03-2018#85536) [LSJ 20100204](https://groups.google.com/g/rec.games.trading-cards.jyhad/c/o5Xnzc8G774/m/yovVizGngKsJ) [LSJ 20080426](https://groups.google.com/g/rec.games.trading-cards.jyhad/c/VIV521VtVfk/m/qQRxntT52F4J) — {The Summoning}, {Piper}, {Summon History}, {Khazar's Diary (Endless Night)}.
[^5-5-8]: [ANK 20200813-3](https://www.vekn.net/forum/rules-questions/78800-off-turn-nocturn#100536) [ANK 20200930](https://www.vekn.net/forum/rules-questions/78800-off-turn-nocturn?start=6#100838) — {Nocturn}, {Infernal Servitor}.
[^5-5-9]: [RTR 19961113](https://groups.google.com/g/rec.games.trading-cards.jyhad/c/VbMEQmJjI_w/m/hkDh73Y1IukJ) [ANK 20170309-2](https://www.vekn.net/forum/rules-questions/75650-pressing-flesh#81050) [ANK 20210913](https://www.vekn.net/forum/rules-questions/79322-piper-and-sebastien-goulet#103113) [LSJ 20090116](https://groups.google.com/g/rec.games.trading-cards.jyhad/c/RQ3ARP9Kvfk/m/e-o1t79x1gUJ) — {War Ghoul}, {Sébastien Goulet}.
[^5-6-1]: [TOM 19951114](https://groups.google.com/g/rec.games.trading-cards.jyhad/c/LOEFFpprXKs/m/3iG4c1loOqgJ) [LSJ 20080210](https://groups.google.com/g/rec.games.trading-cards.jyhad/c/nL-xqiydvYg/m/hWQZF3aBdwsJ) [ANK 20171003](https://www.vekn.net/forum/rules-questions/76205-ghoul-retainer-and-jar-of-skin-eaters#83712) [RTR 19941109](https://groups.google.com/d/msg/rec.games.deckmaster/_6CXoKTSLnw/FdG67-3HEAQJ) [RTR 19960112](https://groups.google.com/g/rec.games.trading-cards.jyhad/c/d3n3StNS7no/m/k2NmZFUl9fAJ) — {Ghoul Retainer}, {Jar of Skin Eaters}, {Spiritual Protector}, group "Retainer that strike" (G00029).
[^5-6-2]: [ANK 20180612](https://www.vekn.net/forum/rules-questions/76717-retainers-damage-and-disciplines#88129) [ANK 20211127](https://www.vekn.net/forum/rules-questions/76687-retainers-inflicting-damage-environmental?start=6#104017) [LSJ 20090616](https://groups.google.com/g/rec.games.trading-cards.jyhad/c/6DEbXHjKGhE/m/1T4TclVRikoJ) — group "Retainer doing damage" (G00016), {Bestial Vengeance}.
[^5-6-3]: [LSJ 20090324](https://groups.google.com/g/rec.games.trading-cards.jyhad/c/Zc_ogoVhsug/m/tJ2VBYI7resJ) [LSJ 20010303](https://groups.google.com/g/rec.games.trading-cards.jyhad/c/OjxDSCbB6i4/m/xmsYv7Y27w4J) [LSJ 19970224](https://groups.google.com/g/rec.games.trading-cards.jyhad/c/80KRDjVFkyg/m/TBJso9Ra_9QJ) — {Detect Authority}, {Shadow Twin}, {Camarilla Vitae Slave}.
[^5-6-4]: [RBK recruit-ally](https://www.vekn.net/rulebook#recruit-ally) — rulebook template.
[^5-7-1]: [ANK 20200203-2](https://www.vekn.net/forum/rules-questions/78415-is-ghoul-mortal#98872) [LSJ 20060515](https://groups.google.com/g/rec.games.trading-cards.jyhad/c/bzusnKlnYr8/m/OSMvzE7YjokJ) [ANK 20230308](https://www.vekn.net/forum/rules-questions/80369-camarilla-vitae-slave-creature-type-putrescent-servitude#107576) [LSJ 20011210-4](https://groups.google.com/g/rec.games.trading-cards.jyhad/c/WT1LwCFnU9A/m/T4bZS_BQXGUJ) — group "Animal" (G00019), group "Ghoul" (G00044), {Murder of Crows}, {Camarilla Vitae Slave}, {Gargoyle Slave}.
[^5-7-2]: [ANK 20200114](https://www.vekn.net/forum/rules-questions/78321-slave-rule-and-acting-minion#98584) [ANK 20200115](https://www.vekn.net/forum/rules-questions/78321-slave-rule-and-acting-minion?start=6#98594) [ANK 20171212](https://www.vekn.net/forum/rules-questions/76334-slave-mental-maze-interaction?start=12#84553) — {Momentary Delay}, {Shadow Boxing}, {Sniper Rifle}, {Obedience}.
[^5-7-3]: [LSJ 20050114](https://groups.google.com/g/rec.games.trading-cards.jyhad/c/JWiZmyC2Y6s/m/q6JHYrE1zKYJ) [LSJ 20050228-2](https://groups.google.com/g/rec.games.trading-cards.jyhad/c/xBb9HQz2KPo/m/sKirLvafQqUJ) [ANK 20210322-2](https://www.vekn.net/forum/rules-questions/79080-nightmares-upon-nightmares?start=6#101910) [RBK traits](https://www.vekn.net/rulebook#traits) — group "Prevent normal unlock" (G00005), {Ruins of Charizel}, {Nightmares upon Nightmares}.
[^5-7-4]: [LSJ 20070322](https://groups.google.com/g/rec.games.trading-cards.jyhad/c/Ww-4rYJxi4w/m/P3QchWVq2o4J) [ANK 20180807](https://www.vekn.net/forum/rules-questions/76905-going-anarch-as-black-hand#89735) [LSJ 20070702](https://groups.google.com/g/rec.games.trading-cards.jyhad/c/Y8fFI0VCwfw/m/e1xrXrq8T5gJ) — group "Black Hand" (G00012), {Cadet}, {Mustajib}, {Seraph's Second}.
[^5-7-5]: [ANK 20220528](https://www.vekn.net/forum/rules-questions/76455-keystone-kine-and-imbued?start=18#105328) [LSJ 20060409](https://groups.google.com/g/rec.games.trading-cards.jyhad/c/gsFQXsCGTG4/m/q5H8FvuKksIJ) [RBK appendix-imbued-rules](https://www.vekn.net/rulebook#appendix-imbued-rules) — {Keystone Kine}, {Kindred Segregation}.
[^5-7-6]: [LSJ 20070516](https://groups.google.com/g/rec.games.trading-cards.jyhad/c/zalQ_AHTpAY/m/vODJ6Q6CluUJ) [LSJ 20060323](https://groups.google.com/g/rec.games.trading-cards.jyhad/c/taLKfNyQ3Kc/m/Av7TF4lHvpUJ) [RBK appendix-imbued-rules](https://www.vekn.net/rulebook#appendix-imbued-rules) — {Dreams of the Sphinx}, {Soul Gem of Etrius}, {Illusions of the Kindred}.
[^5-7-7]: [LSJ 20060409-2](https://groups.google.com/g/rec.games.trading-cards.jyhad/c/lWdr_Ym-UIg/m/t_xVzJIXW18J) [LSJ 20081016](https://groups.google.com/g/rec.games.trading-cards.jyhad/c/GizIs4K_HiY/m/sCutpP29EgIJ) [LSJ 20100211](https://groups.google.com/g/rec.games.trading-cards.jyhad/c/pL63VXEPGME/m/gBjYSBLMwlYJ) [RBK appendix-imbued-rules](https://www.vekn.net/rulebook#appendix-imbued-rules) — {Tension in the Ranks}, {Abjure}, {Pressing Flesh}.
[^5-7-8]: [LSJ 20011015](https://groups.google.com/g/rec.games.trading-cards.jyhad/c/ZXW0ScxTsBA/m/OvbMemV2oXUJ) [LSJ 20030511](https://groups.google.com/g/rec.games.trading-cards.jyhad/c/qSKbZFF7F2A/m/0_Wt6FIxdqsJ) [LSJ 20060815](https://groups.google.com/g/rec.games.trading-cards.jyhad/c/nxExSHh-QjA/m/QFBqiTmg3scJ) [LSJ 20011212](https://groups.google.com/g/rec.games.trading-cards.jyhad/c/3jinbBVvqIE/m/9QaMi2N1VeoJ) [LSJ 20060509](https://groups.google.com/g/rec.games.trading-cards.jyhad/c/KBFnBRrOGB4/m/7ZYNQnvZ5tEJ) [LSJ 20050322-2](https://groups.google.com/g/rec.games.trading-cards.jyhad/c/jiavUD9IgIA/m/SuMUFkb5uLMJ) — group "Scarce" (G00043), group "True Brujah" (G00041), {Clan Impersonation}, {Call the Great Beast}, {Earthshock}.
[^5-7-9]: [LSJ 20090207](https://groups.google.com/g/rec.games.trading-cards.jyhad/c/0UGI9W2sSpk/m/An-ZYLIxAiwJ) [LSJ 20100212](https://groups.google.com/g/rec.games.trading-cards.jyhad/c/NIIFHQg_x1c/m/e5cReQuEqxYJ) [LSJ 20081120-1](https://groups.google.com/g/rec.games.trading-cards.jyhad/c/e2PNDpg-l_c/m/zsGPhfQgLL8J) [LSJ 20091016](https://groups.google.com/g/rec.games.trading-cards.jyhad/c/pqa7mYZ6NEM/m/yvS8jE0ncrQJ) [LSJ 20100226](https://groups.google.com/g/rec.games.trading-cards.jyhad/c/JnycCGrNQmY/m/CCqxwTVXpbEJ) — {Concordance}, {Cry Wolf}, {Vidal Jarbeaux}.
[^5-7-10]: [LSJ 20020609](https://groups.google.com/g/rec.games.trading-cards.jyhad/c/Q_Lk0DPHqC8/m/nAfGfCvsISgJ) [ANK 20211113](https://www.vekn.net/forum/rules-questions/79465-unwholesome-bond-angelo-circle-of-one-new-blood-and-circle#103879) [LSJ 20050927](https://groups.google.com/g/rec.games.trading-cards.jyhad/c/oLMw6SSSgmA/m/-iwdHzdBMF8J) [LSJ 20091012](https://groups.google.com/g/rec.games.trading-cards.jyhad/c/UWmuZnBo6FM/m/DrX_I39ZObcJ) — group "Circle" (G00003), {Angelo}, {New Blood}, {Hermana Hambrienta Mayor}.
[^5-8-1]: [LSJ 20010714](https://groups.google.com/g/rec.games.trading-cards.jyhad/c/-xrhpMEiMrw/m/Vnr8QIyt41cJ) [RBK 6-vampire-sects](https://www.vekn.net/rulebook#6-vampire-sects) — {Ambrogino Giovanni}, {The Baron}, {Kemintiri}, {Xaviar}, {Zayyat, The Sandstorm}, and the other crypt cards printing "N votes (titled)".
[^5-8-2]: [ANK 20190211](https://www.vekn.net/forum/rules-questions/76865-vlad-tepes-anarch-secession?start=12#93409) [RBK 8-glossaries](https://www.vekn.net/rulebook#8-glossaries) — {Vlad Tepes}.
[^5-8-3]: [ANK 20190407](https://www.vekn.net/forum/rules-questions/77533-title-imperator#94416) — {Karsh}.
[^5-8-4]: [RTR 19950509](https://groups.google.com/g/rec.games.trading-cards.jyhad/c/_LKyR7pdMig/m/ZvwdGmIwUnsJ) [RBK contested-titles](https://www.vekn.net/rulebook#contested-titles) — {Democritus}.
[^5-8-5]: [LSJ 20070808-2](https://groups.google.com/g/rec.games.trading-cards.jyhad/c/gaFBeSrs7fU/m/v0VVEOJd2HYJ) — group "Title providing action" (G00042).
[^5-8-6]: [TOM 19960210](https://groups.google.com/g/rec.games.trading-cards.jyhad/c/PiOmH08RyVw/m/CqzTRcOLDNIJ) [LSJ 19980209](https://groups.google.com/g/rec.games.trading-cards.jyhad/c/8boERT-e5e4/m/Gft5ZJszVRAJ) [LSJ 19970224](https://groups.google.com/g/rec.games.trading-cards.jyhad/c/80KRDjVFkyg/m/TBJso9Ra_9QJ) — group "Title providing capacity" (G00038); {The Treatment}, {Bloodbath}.
[^5-8-7]: [LSJ 20100601](https://groups.google.com/g/rec.games.trading-cards.jyhad/c/R7YgwD0VlUQ/m/lhGLnME9m2IJ) [ANK 20190725](https://www.vekn.net/forum/rules-questions/77813-card-questions#95969) — {Xeper, Sultan of Lepers}, {Gerald Windham}.
[^5-8-8]: [LSJ 20010809-3](https://groups.google.com/g/rec.games.trading-cards.jyhad/c/gLl8F0zcCF0/m/cR8nsUweLQIJ) [LSJ 20010809-2](https://groups.google.com/g/rec.games.trading-cards.jyhad/c/9ggmJcK2De0/m/2xW0xE2SzisJ) [TOM 19960210](https://groups.google.com/g/rec.games.trading-cards.jyhad/c/PiOmH08RyVw/m/CqzTRcOLDNIJ) [RTR 20000501](https://groups.google.com/g/rec.games.trading-cards.jyhad/c/MKrA0hBXuaU/m/1M5LOLftKWAJ) [LSJ 20060908](https://groups.google.com/g/rec.games.trading-cards.jyhad/c/CTy2GjM6-Dc/m/9OPulYVGaFcJ) — {Banishment}, {Descent into Darkness}.
[^5-8-21]: [LSJ 20030419](https://groups.google.com/g/rec.games.trading-cards.jyhad/c/A0mvllC-tgs/m/GqjZTFN9SvMJ) — {Illusions of the Kindred}.
[^5-8-9]: [LSJ 20080602](https://groups.google.com/g/rec.games.trading-cards.jyhad/c/Y7CLzywq1Lk/m/LXmN17pA7_UJ) [LSJ 20060904](https://groups.google.com/g/rec.games.trading-cards.jyhad/c/L9D4GK0yNv8/m/H9vnUciv2psJ) [RBK 6-vampire-sects](https://www.vekn.net/rulebook#6-vampire-sects) — {No Confidence}, {Field Training}, {Go Anarch}, and the other sect-change cards carrying this ruling.
[^5-8-10]: [RTR 20201130](https://www.blackchantry.com/2020/12/25/rtr-30-11-2020/) [LSJ 20060904](https://groups.google.com/g/rec.games.trading-cards.jyhad/c/L9D4GK0yNv8/m/H9vnUciv2psJ) — {Clan Impersonation}, {Derange}.
[^5-8-11]: [LSJ 20060904](https://groups.google.com/g/rec.games.trading-cards.jyhad/c/L9D4GK0yNv8/m/H9vnUciv2psJ) — {Fall of the Camarilla}, {Fall of the Sabbat}.
[^5-8-12]: [LSJ 20040519](https://groups.google.com/g/rec.games.trading-cards.jyhad/c/fz-EAPmmqZY/m/bj4sR5CxnmQJ) — {Gratiano}.
[^5-8-13]: [LSJ 20030202](https://groups.google.com/g/rec.games.trading-cards.jyhad/c/ox7A8EvaNJo/m/5CyLJo7pmUYJ) — {Horatio Ballard}, {Maxwell}.
[^5-8-14]: [LSJ 20041026](https://groups.google.com/g/rec.games.trading-cards.jyhad/c/54Zr4RUuVx8/m/fJCT8qW_90EJ) — group "Justicar title vote without Camarilla" (G00034).
[^5-8-15]: [LSJ 20050128](https://groups.google.com/g/rec.games.trading-cards.jyhad/c/HVy8iPUxNbI/m/ZHGTnprQjGUJ) [LSJ 20080603](https://groups.google.com/g/rec.games.trading-cards.jyhad/c/9usl4idp-pY/m/LuT1iK1b4QIJ) — group "Require a Baron" (G00037); {CrimethInc.}, {Powerbase: Los Angeles}.
[^5-8-16]: [PIB 20151116](https://www.vekn.net/forum/rules-questions/74317-the-not-anarch-barons#74327) — {The Baron}, {Baron Dieudonne}.
[^5-8-17]: [ANK 20220317](https://www.vekn.net/forum/rules-questions/79706-crimetheinc-anarch-free-press-club-illusion#104811) — {Club Illusion}.
[^5-8-22]: [LSJ 20081120-1](https://groups.google.com/g/rec.games.trading-cards.jyhad/c/e2PNDpg-l_c/m/zsGPhfQgLL8J) [LSJ 20091016](https://groups.google.com/g/rec.games.trading-cards.jyhad/c/pqa7mYZ6NEM/m/yvS8jE0ncrQJ) [LSJ 20100226](https://groups.google.com/g/rec.games.trading-cards.jyhad/c/JnycCGrNQmY/m/CCqxwTVXpbEJ) — {Vidal Jarbeaux}.
[^5-8-18]: [LSJ 20050128](https://groups.google.com/g/rec.games.trading-cards.jyhad/c/HVy8iPUxNbI/m/ZHGTnprQjGUJ) [PIB 20150306](https://www.vekn.net/forum/rules-questions/69627-vlad-tepes-regent?start=12#69696) [PIB 20150307](https://www.vekn.net/forum/rules-questions/69627-vlad-tepes-regent?start=18#69732) [LSJ 20050526](https://groups.google.com/g/rec.games.trading-cards.jyhad/c/x98guZkL_CQ/m/5JmxFmAbm2IJ) — {Vidal Jarbeaux}, {Vlad Tepes}, {Kemintiri}, {Mata Hari}.
[^5-8-23]: [ANK 20211019](https://www.vekn.net/forum/rules-questions/79278-vidal-jarbeaux-cards-requiring-prince#103598) [ANK 20200710](https://www.vekn.net/forum/rules-questions/77985-vidal-jarbeaux-ability#100333) — {Vidal Jarbeaux}.
[^5-8-19]: [LSJ 20050124](https://groups.google.com/g/rec.games.trading-cards.jyhad/c/HVy8iPUxNbI/m/ZjCzAzmQFMwJ) [ANK 20230503](https://www.vekn.net/forum/rules-questions/80486-vlad-tepes-special-text-under-fall-of-the-sabbat?start=6#107971) — group "Impersonating title for non-existent sect" (G00070).
[^5-8-20]: [ANK 20231221](https://www.vekn.net/forum/rules-questions/81065-faking-title-and-votes#110148) — group "Impersonating a title for political action" (G00069).
[^5-8-24]: [LSJ 20091015](https://groups.google.com/g/rec.games.trading-cards.jyhad/c/pqa7mYZ6NEM/m/HhxAS7Rh3JwJ) [PIB 20130128](https://www.vekn.net/forum/rules-questions/43572-can-i-put-infernal-pact-on-vidal-jarbeaux?start=36#44503) [LSJ 20050721](https://groups.google.com/g/rec.games.trading-cards.jyhad/c/g39H3dwXqvc/m/R0kKrr7JDasJ) — {Vidal Jarbeaux}, {Kemintiri}.
[^5-9-1]: [LSJ 20100811](https://groups.google.com/g/rec.games.trading-cards.jyhad/c/kGKWcs3k6vI/m/Uwx7TGC8lgYJ) — {Field Training}, {Go Anarch}, {Galaric's Legacy}, {The Red Question}, {Into the Fire}, {Out of the Frying Pan} (one ruling recorded on each).
[^5-9-2]: [LSJ 20070707](https://groups.google.com/g/rec.games.trading-cards.jyhad/c/ZtRk5z2TcoI/m/gJWD0dT3kUwJ) [RTR 20201130](https://www.blackchantry.com/2020/12/25/rtr-30-11-2020/) [ANK 20200415](https://www.vekn.net/forum/rules-questions/7516-re-derange-titles-and-bloodbrothers?start=6#99609) — {Derange}, {Clan Impersonation}.
[^5-9-3]: [LSJ 20021209](https://groups.google.com/g/rec.games.trading-cards.jyhad/c/kQpR-Cn9nW0/m/0cNMARSt9PIJ) — {Clan Impersonation}, {Derange}. [ANK 20211022](https://www.vekn.net/forum/rules-questions/79422-nar-sheptha#103636) — {Deep Song}, {Nar-Sheptha}. [ANK 20230814](https://www.vekn.net/forum/rules-questions/80752-deep-song-and-powerbase-savannah?start=12#109035) — {Powerbase: Savannah}.
[^5-9-4]: [LSJ 20100811](https://groups.google.com/g/rec.games.trading-cards.jyhad/c/kGKWcs3k6vI/m/Uwx7TGC8lgYJ) [ANK 20190619](https://www.vekn.net/forum/rules-questions/77723-writ-of-acceptance-and-anarch-and-hackerspace#95462) — {Writ of Acceptance}. [ANK 20180626-2](https://www.vekn.net/forum/rules-questions/76752-tygerius-allegiance-counters-and-going-anarch#88401) — {Tegyrius, Vizier}.
[^5-9-5]: [LSJ 20040519](https://groups.google.com/g/rec.games.trading-cards.jyhad/c/fz-EAPmmqZY/m/bj4sR5CxnmQJ) [LSJ 20080510](https://groups.google.com/g/rec.games.trading-cards.jyhad/c/67g8kq3F_uw/m/MAAoEV0Jf_kJ) [LSJ 20100811](https://groups.google.com/g/rec.games.trading-cards.jyhad/c/kGKWcs3k6vI/m/Uwx7TGC8lgYJ) [ANK 20190619](https://www.vekn.net/forum/rules-questions/77723-writ-of-acceptance-and-anarch-and-hackerspace#95462) — {Fall of the Camarilla}, {Fall of the Sabbat}.
[^5-9-6]: [ANK 20210124](https://www.vekn.net/forum/rules-questions/79001-the-question-of-the-month-action-fizzles#101492) — {The Red Question}. [ANK 20190416](https://www.vekn.net/forum/rules-questions/77560-conditional-intercepts#94528) — {Ministry}, {Protection Racket}, {Teresita, The Godmother}. [LSJ 20090216](https://groups.google.com/g/rec.games.trading-cards.jyhad/c/wU4YAwE6wlI/m/k24LcDxJEecJ) [ANK 20180922](https://www.vekn.net/forum/rules-questions/77023-warsaw-station-clan-impersonation#90717) — {Warsaw Station}.
[^5-9-7]: [LSJ 20050124](https://groups.google.com/g/rec.games.trading-cards.jyhad/c/HVy8iPUxNbI/m/ZjCzAzmQFMwJ) [ANK 20230503](https://www.vekn.net/forum/rules-questions/80486-vlad-tepes-special-text-under-fall-of-the-sabbat?start=6#107971) — {Fall of the Camarilla}, {Fall of the Sabbat}. [ANK 20180125](https://www.vekn.net/forum/rules-questions/76385-red-question-and-crimethinc#85095) — {The Red Question}.
[^5-9-8]: [RBK allies](https://www.vekn.net/rulebook#allies) [ANK 20230417](https://www.vekn.net/forum/rules-questions/80399-an-anarch-manifesto-grey-thorne-vivienne-geroux#107686) — {Grey Thorne}, {Vivienne Géroux}.
[^5-9-9]: [RBK 6-vampire-sects](https://www.vekn.net/rulebook/6-vampire-sects) [LSJ 20060904](https://groups.google.com/g/rec.games.trading-cards.jyhad/c/L9D4GK0yNv8/m/H9vnUciv2psJ) [RTR 20201130](https://www.blackchantry.com/2020/12/25/rtr-30-11-2020/) — {Writ of Acceptance}, {Derange}, {Clan Impersonation}, {Fall of the Camarilla}.
[^6-1-1]: [RTR 19970425](https://groups.google.com/g/rec.games.trading-cards.jyhad/c/DhP_l2cX3mQ/m/9ZZZqL8NFSAJ) [LSJ 20060921](https://groups.google.com/g/rec.games.trading-cards.jyhad/c/Lj1GDLBmOWQ/m/-ZbHv_NcqW4J) [PIB 20130128-2](https://www.vekn.net/forum/rules-questions/44232-khazar-s-diary-question#44504) [LSJ 20100325-2](https://groups.google.com/g/rec.games.trading-cards.jyhad/c/aC6OOfaulbM/m/svWv9UqH6isJ) [LSJ 20001031](https://groups.google.com/g/rec.games.trading-cards.jyhad/c/y8LNZhRyXO0/m/EJzinwvnFoYJ) [PIB 20121220](https://www.vekn.net/forum/rules-questions/43188-storage-annex-changes-control?start=6#43199) [ANK 20200417](https://www.vekn.net/forum/rules-questions/78568-the-capuchin-burns-temporary-control?start=12#99616) — {Agaitas, The Scholar of Antiquities}, {Khazar's Diary (Endless Night)}, {Storage Annex}, {The Capuchin}.
[^6-1-2]: [PIB 20121028](https://www.vekn.net/forum/rules-questions/39816-ec-2012-can-you-answer-these?start=6#39843) [RTR 19960708](https://groups.google.com/g/rec.games.trading-cards.jyhad/c/Rd3Zb61ELuw/m/ii2OfLXTC6gJ) [ANK 20200408-2](https://www.vekn.net/forum/rules-questions/78562-banishment?start=6#99533) [ANK 20210630](https://www.vekn.net/forum/rules-questions/79205-lay-low-vs-banishment#102601) [RTR 20000501](https://groups.google.com/g/rec.games.trading-cards.jyhad/c/MKrA0hBXuaU/m/1M5LOLftKWAJ) — {Anathema}, {Shackles of Enkidu}, {Lay Low}, {Banishment}.
[^6-1-3]: [LSJ 19990425](https://groups.google.com/g/rec.games.trading-cards.jyhad/c/Mmfn07ib6Yw/m/YfwpUlqEdrEJ) [LSJ 20030701-2](https://groups.google.com/g/rec.games.trading-cards.jyhad/c/EFBCP5QI3D4/m/oU1yyA3yV04J) [ANK 20221102](https://www.vekn.net/forum/rules-questions/80129-fall-of-london-card-rules-questions#106688) — {Hidden Lurker}, {Zapaderin}, {Echo of Harmonies}, {Empowering the Puppet King}, {Set's Call}, {The Shard, London}.
[^6-1-4]: [LSJ 20100423](https://groups.google.com/g/rec.games.trading-cards.jyhad/c/YnQCu0GeMhc/m/ET__SGvjD7QJ) [LSJ 20100127](https://groups.google.com/g/rec.games.trading-cards.jyhad/c/YnQCu0GeMhc/m/ET__SGvjD7QJ) [ANK 20210813](https://www.vekn.net/forum/rules-questions/79279-might-of-the-camarilla-burned-from-play#102903) [LSJ 20090428](https://groups.google.com/g/rec.games.trading-cards.jyhad/c/BmA4xsXoEXc/m/rAIXsI8ycG4J) — {Byzar}, {Blessed Resilience}, {Spell of Life}.
[^6-2-1]: [LSJ 20001201](https://groups.google.com/g/rec.games.trading-cards.jyhad/c/BPHZsY3p20E/m/S6HiRebyeX0J) [ANK 20200129](https://www.vekn.net/forum/rules-questions/78701-replace-during-unlock-and-other-unlock-effects#100210) [LSJ 20091208](https://groups.google.com/g/rec.games.trading-cards.jyhad/c/ptHbJM9MlVI/m/O61W2JkI_rIJ) [RTR 19951017](https://groups.google.com/g/rec.games.trading-cards.jyhad/c/ouhNUbHYg50/m/rco157ZHyqEJ) [ANK 20200925](https://www.vekn.net/forum/rules-questions/78861-revelation-of-wrath#100820) [ANK 20211105](https://www.vekn.net/forum/rules-questions/79460-sarrasin-corruption-and-effect-triggers#103791) — {Mind Rape}, {Malkavian Dementia}, {Velvet Tongue}, {Sarrasine}.
[^6-2-2]: [LSJ 20020618](https://groups.google.com/g/rec.games.trading-cards.jyhad/c/DVGe6EsiMZ4/m/2-t1mFMkAX0J) [LSJ 20080326](https://groups.google.com/g/rec.games.trading-cards.jyhad/c/KUQEznVQlOU/m/e_6GMg__zdMJ) [PIB 20150501](https://www.vekn.net/forum/rules-questions/70780-change-of-control-during-the-action?start=6#70800) [ANK 20220127](https://www.vekn.net/forum/rules-questions/79615-burn-counter-to-gain-control-of-steal-a-minion#104588) — {Temptation}, {Revelation of Despair}.
[^6-2-3]: [LSJ 20020725](https://groups.google.com/g/rec.games.trading-cards.jyhad/c/wCPFIH_g5ZE/m/inchZQXKRrsJ) [PIB 20121031](https://www.vekn.net/forum/rules-questions/39816-ec-2012-can-you-answer-these?start=18#39908) [LSJ 20070222-2](https://groups.google.com/g/rec.games.trading-cards.jyhad/c/jBrfK77gayo/m/X4wqXnwhzDoJ) — {Temptation}, {War Ghoul}, {The Diamond Thunderbolt}.
[^6-2-4]: [LSJ 20010119](https://groups.google.com/g/rec.games.trading-cards.jyhad/c/XB0IvK7I6PQ/m/foA7igsB8EEJ) [RTR 20020501](https://groups.google.com/g/rec.games.trading-cards.jyhad/c/M1snoR2msbQ/m/RFwCmX3anDkJ) [LSJ 20030219](https://groups.google.com/g/rec.games.trading-cards.jyhad/c/ugfckv9DAbo/m/w5UP-Ch-u5MJ) [LSJ 20040526](https://groups.google.com/g/rec.games.trading-cards.jyhad/c/M3hDKK2JSWw/m/Z-W3F1vO8fYJ) [RTR 20000501](https://groups.google.com/g/rec.games.trading-cards.jyhad/c/MKrA0hBXuaU/m/1M5LOLftKWAJ) [ANK 20210630](https://www.vekn.net/forum/rules-questions/79205-lay-low-vs-banishment#102601) — {Temptation}, {Mind Rape}, {Spirit Marionette}, {Descent into Darkness}, {Lay Low}.
[^6-2-5]: [LSJ 20081105](https://groups.google.com/g/rec.games.trading-cards.jyhad/c/CYjOJtTBMGU/m/H8kQXN1w2ycJ) [ANK 20181110](https://www.vekn.net/forum/rules-questions/76844-some-questions?start=6#91778) — group "Temporary control" (G00001), {The Ailing Spirit}, {Temptation}, {Mind Rape}, {Spirit Marionette}.
[^6-2-6]: [LSJ 20021111](https://groups.google.com/g/rec.games.trading-cards.jyhad/c/Y6_dPn4ONCA/m/xkVBf0DCQM0J) [RBK 5-ending-the-game](https://www.vekn.net/rulebook/5-ending-the-game) — {Parmenides}.
[^6-2-7]: [RTR 19941109](https://groups.google.com/d/msg/rec.games.deckmaster/_6CXoKTSLnw/FdG67-3HEAQJ) [ANK 20200130-2](https://www.vekn.net/forum/rules-questions/78398-the-rack-vs-changing-control#98819) [LSJ 20031106](https://groups.google.com/g/rec.games.trading-cards.jyhad/c/bFZCLXzzOeM/m/n1C6p6xw1O0J) [ANK 20220525](https://www.vekn.net/forum/rules-questions/79777-lorenzo-detuono-and-imposing-phantasm#105316) — {Betrayer}, {The Rack}, {Rutor's Hand}, {Imposing Phantasm}.
[^6-3-1]: [TOM 19960226-1](https://groups.google.com/g/rec.games.trading-cards.jyhad/c/16y-ZD7Xats/m/oMeZDnSFdYAJ) — recorded identically on twelve cards; {Far Mastery}, {New Management}, {Spirit Marionette}.
[^6-3-2]: [RTR 19960112](https://groups.google.com/g/rec.games.trading-cards.jyhad/c/d3n3StNS7no/m/k2NmZFUl9fAJ) [LSJ 20030606](https://groups.google.com/g/rec.games.trading-cards.jyhad/c/qzKS4OGBgbo/m/ST8O8A0s-JMJ) — group "Locquipments" (G00047), {Disputed Territory}, {Dominate Kine}, {Malkavian Time Auction}.
[^6-3-3]: [LSJ 19971002](https://groups.google.com/g/rec.games.trading-cards.jyhad/c/RY_nhdykKP0/m/fOdKJtOy4kgJ) [LSJ 20080803-2](https://groups.google.com/g/rec.games.trading-cards.jyhad/c/OknxGrvlaNk/m/khteZ5WaNE4J) — {Disputed Territory}, {New Management}.
[^6-3-4]: [RTR 19960708](https://groups.google.com/g/rec.games.trading-cards.jyhad/c/Rd3Zb61ELuw/m/ii2OfLXTC6gJ) [LSJ 20001031](https://groups.google.com/g/rec.games.trading-cards.jyhad/c/y8LNZhRyXO0/m/EJzinwvnFoYJ) [PIB 20121220](https://www.vekn.net/forum/rules-questions/43188-storage-annex-changes-control?start=6#43199) [LSJ 19990709](https://groups.google.com/g/rec.games.trading-cards.jyhad/c/F131j-4dabU/m/gS8SFKNu02oJ) — {Shackles of Enkidu}, {Storage Annex}, {Ethan Locke}.
[^6-3-5]: [TOM 19960114](https://groups.google.com/g/rec.games.trading-cards.jyhad/c/cOqrGO0UrSw/m/5pDhn3YVyG4J) [LSJ 20020514](https://groups.google.com/g/rec.games.trading-cards.jyhad/c/xBDPee5wq40/m/WWX0GrKppzsJ) — {Incriminating Videotape}.
[^6-3-6]: [LSJ 20100723](https://groups.google.com/g/rec.games.trading-cards.jyhad/c/0u5KQWiutdg/m/lAZoy4vIwiIJ) [PIB 20111002](https://www.vekn.net/forum/rules-questions/8235-re-coven-timing?start=18#11317) [ANK 20200508-1](https://www.vekn.net/forum/rules-questions/78622-scourge-of-the-enochians-timing?start=12#99786) — {The Coven}, {Scourge of the Enochians}.
[^6-4-1]: [RTR 20000501](https://groups.google.com/g/rec.games.trading-cards.jyhad/c/MKrA0hBXuaU/m/1M5LOLftKWAJ) [LSJ 20060908](https://groups.google.com/g/rec.games.trading-cards.jyhad/c/CTy2GjM6-Dc/m/9OPulYVGaFcJ) [ANK 20210630](https://www.vekn.net/forum/rules-questions/79205-lay-low-vs-banishment#102601) [LSJ 20080816](https://groups.google.com/g/rec.games.trading-cards.jyhad/c/FKBTEzLf0_A/m/eK1AuUnPolMJ) [LSJ 20100206-2](https://groups.google.com/g/rec.games.trading-cards.jyhad/c/reXyybyIYX8/m/jeCyjdiZ5T4J) [TOM 19951209](https://groups.google.com/g/rec.games.trading-cards.jyhad/c/qP2j6CpBUDI/m/2qsG4E23bl4J) — {Descent into Darkness}, {Lay Low}, {Thicker than Blood}.
[^6-4-2]: [LSJ 20040526](https://groups.google.com/g/rec.games.trading-cards.jyhad/c/M3hDKK2JSWw/m/Z-W3F1vO8fYJ) [LSJ 20021111](https://groups.google.com/g/rec.games.trading-cards.jyhad/c/Y6_dPn4ONCA/m/xkVBf0DCQM0J) — {Descent into Darkness}, {Parmenides}.
[^6-4-3]: [LSJ 20040726](https://groups.google.com/g/rec.games.trading-cards.jyhad/c/LlqCB6LN64g/m/k98Xj1pwjPcJ) [LSJ 20010627](https://groups.google.com/g/rec.games.trading-cards.jyhad/c/NhNCVCCDyU0/m/I5Yph3-UUPsJ) — {Possession}, {Compel the Spirit}.
[^6-4-4]: [TOM 19960210](https://groups.google.com/g/rec.games.trading-cards.jyhad/c/PiOmH08RyVw/m/CqzTRcOLDNIJ) [TOM 19960211](https://groups.google.com/g/rec.games.trading-cards.jyhad/c/PiOmH08RyVw/m/9jI1_ASoupIJ) [LSJ 20010809-2](https://groups.google.com/g/rec.games.trading-cards.jyhad/c/9ggmJcK2De0/m/2xW0xE2SzisJ) [LSJ 20010809-3](https://groups.google.com/g/rec.games.trading-cards.jyhad/c/gLl8F0zcCF0/m/cR8nsUweLQIJ) [PIB 20150522](https://www.vekn.net/forum/rules-questions/71291-blood-doll-and-the-rack-clarity#71293) [LSJ 20010623](https://groups.google.com/g/rec.games.trading-cards.jyhad/c/GN5MqcCTOo8/m/7ll40gxjFWYJ) [LSJ 20040616](https://groups.google.com/g/rec.games.trading-cards.jyhad/c/jQkkiC3I8P8/m/uDZ--HnPtf0J) — {The Rack}, {Descent into Darkness}, {Lay Low}.
[^6-4-5]: [LSJ 20010616](https://groups.google.com/g/rec.games.trading-cards.jyhad/c/h7gnHNBFliE/m/MsfJ0qqv_jsJ) [LSJ 20030522-1](https://groups.google.com/g/rec.games.trading-cards.jyhad/c/_krZG-uPtzc/m/94US5l81edwJ) [LSJ 20061218](https://groups.google.com/g/rec.games.trading-cards.jyhad/c/DTBI6LkPdZ4/m/Qtu3QUPERdIJ) — {Tegyrius, Vizier}, {NRA PAC}.
[^6-4-6]: [PIB 20150512](https://www.vekn.net/forum/rules-questions/71020-priority-contract-and-provision-of-the-silsila#71053) [ANK 20180129-2](https://www.vekn.net/forum/rules-questions/76363-remove-from-play-remove-from-the-game-and-contracts#85155) — {The Black Throne}, {Priority Contract}, {Provision of the Silsila}.
[^6-4-7]: [PIB 20150728](https://www.vekn.net/forum/rules-questions/72285-chameleon-v-merged-vampire#72285) [LSJ 20030519-2](https://groups.google.com/g/rec.games.trading-cards.jyhad/c/mi8M1lSCLqo/m/Rdg9SU5nA6QJ) [LSJ 20030527](https://groups.google.com/g/rec.games.trading-cards.jyhad/c/1hViTSXv544/m/nOXqGMitwP0J) — {Chameleon}, {Legendary Vampire}, {Masquerade Enforcement}.
[^6-4-8]: [LSJ 20010622](https://groups.google.com/g/rec.games.trading-cards.jyhad/c/65IHHAii7ms/m/kyS0uVtsbNMJ) [LSJ 20070829-2](https://groups.google.com/g/rec.games.trading-cards.jyhad/c/drn7wHaGugQ/m/QqaYmjAf2UYJ) — {Parmenides}, {Sonja Blue}.
[^6-4-9]: [LSJ 20080805](https://groups.google.com/g/rec.games.trading-cards.jyhad/c/SIbzFAwWDKs/m/BDkEg19txtoJ) — group "Permanent not replaced" (G00008).
[^6-5-1]: [ANK 20180719-2](https://www.vekn.net/forum/rules-questions/76835-burn-lose-pay-pool-and-poison-pill-kindred-segregation#89046) [ANK 20181105](https://www.vekn.net/forum/rules-questions/77140-the-rising-and-gain-pool#91674) [LSJ 19970224](https://groups.google.com/g/rec.games.trading-cards.jyhad/c/80KRDjVFkyg/m/TBJso9Ra_9QJ) [RBK 5-ending-the-game](https://www.vekn.net/rulebook/5-ending-the-game) — {Poison Pill}, {The Rising}, {Dirty Little Secrets}.
[^6-5-2]: [ANK 20180813](https://www.vekn.net/forum/rules-questions/76917-poison-pill-ancient-influence#89940) [LSJ 20041025](https://groups.google.com/g/rec.games.trading-cards.jyhad/c/sbfkGmojYao/m/obMvk67O5PYJ) — {Poison Pill}, {Ancient Influence}, {Reins of Power}.
[^6-5-3]: [LSJ 20020620](https://groups.google.com/g/rec.games.trading-cards.jyhad/c/WoXWzLYaFSY/m/ug3CHnpMCUQJ) [LSJ 20080612](https://groups.google.com/g/rec.games.trading-cards.jyhad/c/THFR8YTXxGI/m/ocQc4IRWP1AJ) [ANK 20210714-2](https://www.vekn.net/forum/rules-questions/79217-clarification-needed-on-eternals-of-sirius-rulings?start=6#102696) — {Villein}, {The Eternals of Sirius}.
[^6-5-4]: [RTR 20010710](https://groups.google.com/g/rec.games.trading-cards.jyhad/c/GsI1UyH54jU/m/x9LfDZX1vR4J) [RTR 19970630](https://groups.google.com/g/rec.games.trading-cards.jyhad/c/KireUeOYY3c/m/t6ifm9lur1kJ) [ANK 20230817-2](https://www.vekn.net/forum/rules-questions/80779-play-to-win-first-tradition-life-boom#109075) [LSJ 20100527](https://groups.google.com/g/rec.games.trading-cards.jyhad/c/Tr3X4DsZr-8/m/O06iXN6LtzsJ) [RTR 19941109](https://groups.google.com/d/msg/rec.games.deckmaster/_6CXoKTSLnw/FdG67-3HEAQJ) — {Thanks for the Donation}, {Life Boon}, {Parity Shift}, {Repo Man}, {Vast Wealth}.
[^6-5-5]: [LSJ 20080512](https://groups.google.com/g/rec.games.trading-cards.jyhad/c/z2DGSFph6sM/m/IjJB89nbtlsJ) [LSJ 20050607](https://groups.google.com/g/rec.games.trading-cards.jyhad/c/WLv9R8wA0Ow/m/gQyOMb3fEKQJ) [LSJ 20050608](https://groups.google.com/g/rec.games.trading-cards.jyhad/c/WLv9R8wA0Ow/m/dyAPpxSMoSYJ) — {Herald of Topheth}, {Bima}, {Spying Mission}.
[^6-5-6]: [LSJ 20090115-2](https://groups.google.com/g/rec.games.trading-cards.jyhad/c/rSaiVPMbpvY/m/ZYG3cYIdQZkJ) [ANK 20220808](https://www.vekn.net/forum/rules-questions/79952-when-does-lutz-ability-trigger#105913) [RTR 19951110](https://groups.google.com/g/rec.games.trading-cards.jyhad/c/TXfganI5B2o/m/QYh3AdPNbUwJ) — {Lutz von Hohenzollern}, {Armin Brenner}, {Donald Cargill}, {Voter Captivation}.
[^6-5-7]: [LSJ 20090731](https://groups.google.com/g/rec.games.trading-cards.jyhad/c/y6f0s6tUtqs/m/H3dk4qr4nfkJ) — {Last Stand}.
[^6-5-8]: [ANK 20180408](https://www.vekn.net/forum/rules-questions/76500-charnas-the-imp#86191) [LSJ 20021008](https://groups.google.com/g/rec.games.trading-cards.jyhad/c/Mc3xfym_uw8/m/zY9ipcHSXF8J) [ANK 20181110](https://www.vekn.net/forum/rules-questions/76844-some-questions?start=6#91778) [ANK 20200408-2](https://www.vekn.net/forum/rules-questions/78562-banishment?start=6#99533) [ANK 20210630](https://www.vekn.net/forum/rules-questions/79205-lay-low-vs-banishment#102601) — {Charnas the Imp}, {The Meddling of Semsith}, {Mind Rape}, {Temptation}, {Lay Low}.
[^6-5-9]: [LSJ 20100206-2](https://groups.google.com/g/rec.games.trading-cards.jyhad/c/reXyybyIYX8/m/jeCyjdiZ5T4J) [ANK 20180129-2](https://www.vekn.net/forum/rules-questions/76363-remove-from-play-remove-from-the-game-and-contracts#85155) [ANK 20220210](https://www.vekn.net/forum/rules-questions/79644-timing-of-the-oust-pool-gain-vp-gain-and-life-boon#104665) — {Shatter the Gate}, {Priority Contract}, {The Black Throne}, {Revelation of the Serpent}.
[^6-5-10]: [LSJ 20000309](https://groups.google.com/g/rec.games.trading-cards.jyhad/c/ykAzsCzPkvg/m/bVefVZeCoQwJ) [LSJ 20100208](https://groups.google.com/g/rec.games.trading-cards.jyhad/c/wt2kuUJXoRI/m/CyHXMb-Cn_0J) [TOM 19951214-1](https://groups.google.com/g/rec.games.trading-cards.jyhad/c/8Fr6gioYZDI/m/p1eW5eaUMO0J) [RBK 5-ending-the-game](https://www.vekn.net/rulebook/5-ending-the-game) — group "Vote damaging multiple players" (G00015), {The Rising}, {Sabbat Threat}.
[^6-5-11]: [LSJ 20100206-2](https://groups.google.com/g/rec.games.trading-cards.jyhad/c/reXyybyIYX8/m/jeCyjdiZ5T4J) [LSJ 20100210-2](https://groups.google.com/g/rec.games.trading-cards.jyhad/c/wt2kuUJXoRI/m/XbHSJHMfk08J) [LSJ 20100207](https://groups.google.com/g/rec.games.trading-cards.jyhad/c/wt2kuUJXoRI/m/LVO2J4dRxoIJ) — {The Rising}.
[^6-5-12]: [LSJ 20011222](https://groups.google.com/g/rec.games.trading-cards.jyhad/c/DlCBJmB2fzY/m/HVLdn4Hr9uIJ) [ANK 20221028-2](https://www.vekn.net/forum/rules-questions/80122-the-shard-london-and-sargon#106673) [RTR 19980623](https://groups.google.com/g/rec.games.trading-cards.jyhad/c/tSpd9dtTElc/m/-CuHJF54_n0J) [LSJ 20030519](https://groups.google.com/g/rec.games.trading-cards.jyhad/c/E6Jz8m3iKrA/m/BoCMzQoGzyQJ) [LSJ 20100527](https://groups.google.com/g/rec.games.trading-cards.jyhad/c/Tr3X4DsZr-8/m/O06iXN6LtzsJ) [TOM 19951214-2](https://groups.google.com/g/rec.games.trading-cards.jyhad/c/lVTQ1rstpLY/m/Dz0yYCdMHg8J) [LSJ 19971006](https://groups.google.com/g/rec.games.trading-cards.jyhad/c/2to9jkow98Q/m/loNTF9VNuc8J) — {Sargon}, {Tereza Rostas}, {Hrothulf}, {Enticement}, {Curse of Nitocris}.
[^6-6-1]: [LSJ 20070309-2](https://groups.google.com/g/rec.games.trading-cards.jyhad/c/c3Kx0-C_5JU/m/CRscFEQfeC0J) [RBK master-cards](https://www.vekn.net/rulebook#master-cards) [RBK master-phase](https://www.vekn.net/rulebook#master-phase) — {Wash}. The rulebook is
    explicit that a canceled out-of-turn master still counts against the next master
    phase; the older ruling's parenthetical to the contrary is superseded.
[^6-6-2]: [LSJ 20090126](https://groups.google.com/g/rec.games.trading-cards.jyhad/c/3Cd-DNfT7yQ/m/-BfYOkP1OUUJ) [ANK 20170124](https://www.vekn.net/forum/rules-questions/75556-vessel-wash-and-mpa#80362) [RBK trifle](https://www.vekn.net/rulebook#trifle) — {Wash}, {Sudden Reversal}.
[^6-6-3]: [ANK 20170124](https://www.vekn.net/forum/rules-questions/75556-vessel-wash-and-mpa#80362) [LSJ 20090126](https://groups.google.com/g/rec.games.trading-cards.jyhad/c/3Cd-DNfT7yQ/m/-BfYOkP1OUUJ) — {Wash}.
[^6-6-4]: [PIB 20150524](https://www.vekn.net/forum/rules-questions/71300-proxy-kissed-question#71304) [ANK 20191004](https://www.vekn.net/forum/rules-questions/77994-synesios#97241) [RBK master-cards](https://www.vekn.net/rulebook#master-cards) — {Proxy Kissed}, {Synesios}.
[^6-6-5]: [LSJ 20031201](https://groups.google.com/g/rec.games.trading-cards.jyhad/c/Mi_j7sUsZZw/m/ScJPKbfiCAgJ) — {Vox Senis}.
[^6-6-7]: [ANK 20220503](https://www.vekn.net/forum/rules-questions/39040-re-ex-nihilo-can-i-choose-to-burn-my-minion#105161) — {Ex Nihilo}.
[^6-6-8]: [ANK 20191218](https://www.vekn.net/forum/rules-questions/62700-re-nahir-and-research-counters?start=6#98297) [ANK 20220617](https://www.vekn.net/forum/rules-questions/79835-nonu-dis-and-during-x-do-y#105494) — {Nahir}, {Nonu Dis}.
[^6-7-1]: [LSJ 19970224](https://groups.google.com/g/rec.games.trading-cards.jyhad/c/80KRDjVFkyg/m/TBJso9Ra_9QJ) [LSJ 20070516](https://groups.google.com/g/rec.games.trading-cards.jyhad/c/zalQ_AHTpAY/m/vODJ6Q6CluUJ) [RBK targeting-of-cards](https://www.vekn.net/rulebook#targeting-of-cards) [RBK card-rulings](https://www.vekn.net/rulebook#card-rulings) — {Reform Body}, {Dreams of the Sphinx}.
[^6-7-2]: [RTR 19990712](https://groups.google.com/g/rec.games.trading-cards.jyhad/c/x5k5Vw_hkI0/m/lCqkvlUz5yIJ) [LSJ 20090625](https://groups.google.com/g/rec.games.trading-cards.jyhad/c/C3daj-vYqu4/m/2V2yTyLebHEJ) [PIB 20140122](https://www.vekn.net/forum/rules-questions/58586-banishment-and-master-discipline#58772) [TOM 19951209](https://groups.google.com/g/rec.games.trading-cards.jyhad/c/qP2j6CpBUDI/m/2qsG4E23bl4J) [LSJ 20100206-2](https://groups.google.com/g/rec.games.trading-cards.jyhad/c/reXyybyIYX8/m/jeCyjdiZ5T4J) — {Creation Rites}, {The Becoming}, {Banishment}, {Thicker than Blood}, group "Action creating vampire" (G00054).
[^6-7-3]: [ANK 20200408-2](https://www.vekn.net/forum/rules-questions/78562-banishment?start=6#99533) [RTR 20000501](https://groups.google.com/g/rec.games.trading-cards.jyhad/c/MKrA0hBXuaU/m/1M5LOLftKWAJ) [ANK 20210630](https://www.vekn.net/forum/rules-questions/79205-lay-low-vs-banishment#102601) — {Banishment}, {Lay Low}.
[^6-7-4]: [TOM 19951209](https://groups.google.com/g/rec.games.trading-cards.jyhad/c/qP2j6CpBUDI/m/2qsG4E23bl4J) [ANK 20210630](https://www.vekn.net/forum/rules-questions/79205-lay-low-vs-banishment#102601) [LSJ 20100902](https://groups.google.com/g/rec.games.trading-cards.jyhad/c/SM2_578Th0U/m/-GX0pSP_rCcJ) [RTR 20180303](https://www.vekn.net/forum/rules-questions/76447-rules-team-rulings-rtr-03-03-2018#85536) [RBK influence-phase](https://www.vekn.net/rulebook#influence-phase) — {Lay Low}, {Wormwood}, {Jimmy Dunn}.
[^6-7-5]: [RTR 20180303](https://www.vekn.net/forum/rules-questions/76447-rules-team-rulings-rtr-03-03-2018#85536) [ANK 20240118](https://www.vekn.net/forum/rules-questions/81155-gather#110398) [LSJ 20100527](https://groups.google.com/g/rec.games.trading-cards.jyhad/c/Tr3X4DsZr-8/m/O06iXN6LtzsJ) [RBK influence-phase](https://www.vekn.net/rulebook#influence-phase) — {Ingrid Rossler}, {Angela Preston}, {Paul "Sixofswords29" Moreton}, {Ennoia's Theater}, {Gather}, {Leandro}.
[^6-7-6]: [LSJ 20060623](https://groups.google.com/g/rec.games.trading-cards.jyhad/c/mfgW0TeoLNM/m/e_QgbzZCqa8J) [LSJ 19990215](https://groups.google.com/g/rec.games.trading-cards.jyhad/c/_izcAo43T4Q/m/wSarBMJeRx8J) [ANK 20240706](https://www.vekn.net/forum/rules-questions/81563-break-the-bonds-presence-target?start=18#111945) [LSJ 20041015](https://groups.google.com/g/rec.games.trading-cards.jyhad/c/jonKzp3f8wA/m/Dgropqbf_WwJ) — {Undue Influence}, {Break the Bonds}, {Lázár Dobrescu}, {Social Ladder}.
[^6-9-1]: [ANK 20180318](https://www.vekn.net/forum/rules-questions/76464-dnr-counts-against-hand-size-meddling-of-semsith-and-raptor#85841) [ANK 20231229](https://www.vekn.net/forum/rules-questions/81077-do-not-replace-rule-question#110227) [ANK 20190707](https://www.vekn.net/forum/rules-questions/77694-ok-a-new-round-of-doubts-for-a-noobie#95274) [LSJ 20030530](https://groups.google.com/g/rec.games.trading-cards.jyhad/c/SZehI8SwAc4/m/shpyPIdsHxUJ) — {Dreams of the Sphinx}, {The Meddling of Semsith}, {Hagar Stone}, {Sascha Vykos, The Angel of Caine}, {Raptor}.
[^6-9-2]: [LSJ 20020814](https://groups.google.com/g/rec.games.trading-cards.jyhad/c/gt8wQhk76lA/m/qjDJXRLxM7cJ) [LSJ 20021008](https://groups.google.com/g/rec.games.trading-cards.jyhad/c/Mc3xfym_uw8/m/zY9ipcHSXF8J) [ANK 20191218](https://www.vekn.net/forum/rules-questions/62700-re-nahir-and-research-counters?start=6#98297) [ANK 20200616](https://www.vekn.net/forum/rules-questions/78687-the-erciyes-fragments-fragment-of-the-book-of-nod-barrens-impulse#100110) — {Edward Neally}, {The Meddling of Semsith}, {Nahir}; group "Can draw during action" (G00023).
[^6-9-3]: [LSJ 20020904-2](https://groups.google.com/g/rec.games.trading-cards.jyhad/c/ObuKimgcCpI/m/PVsmKoSZueoJ) [ANK 20210313](https://www.vekn.net/forum/rules-questions/79072-until-the-end-vs-during-art-of-love-steals-informant#101841) [ANK 20190725](https://www.vekn.net/forum/rules-questions/77813-card-questions#95969) [LSJ 20090731](https://groups.google.com/g/rec.games.trading-cards.jyhad/c/y6f0s6tUtqs/m/H3dk4qr4nfkJ) [LSJ 20060426](https://groups.google.com/g/rec.games.trading-cards.jyhad/c/4e6z1_JWIzA/m/oMQz7oVR1O8J) — {Dreams of the Sphinx}, {The Art of Love}, {Josef von Bauren}, {Last Stand}, {High Aye}.
[^6-9-4]: [LSJ 19981005](https://groups.google.com/g/rec.games.trading-cards.jyhad/c/9vOWIR4P_4o/m/UkztBlUMR_QJ) [ANK 20230404](https://www.vekn.net/forum/rules-questions/80431-ruxandra-and-discarding#107788) [LSJ 20090618](https://groups.google.com/g/rec.games.trading-cards.jyhad/c/jxTaf6lnYb0/m/KoQF6jLw5zAJ) [LSJ 20060215](https://groups.google.com/g/rec.games.trading-cards.jyhad/c/BhecJx5BqtQ/m/nqEdwFmnQnwJ) [ANK 20180725](https://www.vekn.net/forum/rules-questions/76858-feline-saboteur-timing#89295) [RTR 20030519](https://groups.google.com/g/rec.games.trading-cards.jyhad/c/NOBWXWrd-vA/m/iEOpQp1uhvAJ) [ANK 20211010](https://www.vekn.net/forum/rules-questions/79335-elen-camjian-second-action?start=6#103500) — {Ruxandra}, {Constant Revolution}, {Call the Wild Hunt}, {Feline Saboteur}, {Rachel Brandywine}, {Jaggedy Andy}.
[^6-9-5]: [TOM 19950924](https://groups.google.com/g/rec.games.trading-cards.jyhad/c/yejj-744_zc/m/g3t6CooUzVIJ) [ANK 20180925-1](https://www.vekn.net/forum/rules-questions/77029-order-of-draw-and-replace-for-concealed-weapon-under-infernal-pursuit?start=6#90750) [LSJ 20011202](https://groups.google.com/g/rec.games.trading-cards.jyhad/c/gyzUP4TCq6M/m/D-u3Uzdy6SMJ) [LSJ 20080612-2](https://groups.google.com/g/rec.games.trading-cards.jyhad/c/dVIBPf6EX_8/m/km-qYBcG_qYJ) [ANK 20211201](https://www.vekn.net/forum/rules-questions/79519-waste-management-operations-no-cards-in-the-library-and-in-the-hand#104074) — {Infernal Pursuit}, {Agaitas, The Scholar of Antiquities}, {Sudario Refraction}, {Waste Management Operation}.
[^6-9-6]: [PIB 20121028](https://www.vekn.net/forum/rules-questions/39816-ec-2012-can-you-answer-these?start=6#39843) [PIB 20121031](https://www.vekn.net/forum/rules-questions/39816-ec-2012-can-you-answer-these?start=18#39908) [ANK 20211020](https://www.vekn.net/forum/rules-questions/79416-sergei-voshkov-the-eye#103610) [LSJ 20081129](https://groups.google.com/g/rec.games.trading-cards.jyhad/c/7fMPCYIPrag/m/_gGD-1da2N8J) [ANK 20180512](https://www.vekn.net/forum/rules-questions/76599-troglodytia-special-vs-wash#86842) [LSJ 20050224-4](https://groups.google.com/g/rec.games.trading-cards.jyhad/c/LATlh09TuhA/m/oAcvZ7MfWCIJ) — {Vast Wealth}, {Vaticination}, {Sergei Voshkov, The Eye}, {Ashur Tablets}, {Troglodytia}, {Learjet}.
