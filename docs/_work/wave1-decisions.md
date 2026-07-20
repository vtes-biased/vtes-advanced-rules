# Wave 1 boundary decisions — what the other 53 sections must not contradict

Produced by the eleven wave-1 drafters after writing their sections. These are the rules
they actually stated. If your section touches one, **defer to it and cross-reference**;
do not restate it and do not contradict it. If you believe one is wrong, say so in your
report rather than silently writing the opposite.

Binding rules calls by the owner live in `owner-rulings.md` and outrank anything here.

## §1.1

- A card's printed statement of fact applies automatically; only a clause worded "may" or "can" is optional. An ability is mandatory unless the card marks it optional.
  *(binds: §4.3, §4.8, §5.2, §6.6)*
- A cost or cost reduction printed inside an effect is mandatory, and is paid even if paying ousts the controller.
  *(binds: §1.7, §6.5, §3.7.7)*
- A mandatory effect is applied at its timing point, before its controller passes the opportunity to play effects; a player who has already passed does not regain the window because the effect was overlooked, and a missed mandatory choice with no printed default is not remedied by imposing one after the fact.
  *(binds: §2.1, §6.3)*
- A "cannot" that names the cards it forbids bars playing them at all, including plays made only to cycle or for a side benefit. A "cannot" that names an outcome leaves the play legal and only nullifies the outcome.
  *(binds: §4.5, §3.7.2, §4.3)*
- 1.1 owns mandatory vs optional EFFECTS and the reading of card-text referents. It does not own mandatory ACTIONS (3.9) nor the no-target/futility boundary (1.6); 1.1 states the no-target rule in one sentence and points to 1.6.
  *(binds: §1.6, §3.9, §3.4, §3.2, §4.5, §4.6)*
- Choices inside an effect are made at resolution, not at play; an optional effect on a card in play is taken or declined by the controller of the minion it is on.
  *(binds: §3.4, §6.6)*

## §1.15

- A once-per-action limit on PLAYING a card binds the minion: different minions may each play their own copy on the same action ({Cloak the Gathering}, {Suppressing Fire}, [ANK 20200515]). A limited effect, by contrast, binds the action itself. 1.15 states the first in one sentence and cross-references §1.2 for the second; §1.2 owns the limited-effect rule and must not contradict the minion-binding half.
  *(binds: §1.2, §3.2, §3.5, §3.8)*
- Multiple copies of the same card in play each exert their own effect and impose their own cost; burn-pool/burn-blood requirements from any number of sources are cumulative. Numeric bonuses add. Votes are the exception and do not add per copy ({Legacy of Pander} 1 vote total; {Orun} 1 vote per 3).
  *(binds: §3.7.6, §5.8)*
- An effect conditioned on having 'any' counters is flat and does not scale with counter count ({Dr. Morrow} -1 stealth not -X; {Kahina} 1 damage).
  *(binds: §4.2, §5.7)*
- Discipline grants from two DIFFERENT cards do not combine into the superior level ({Leech} + {Putrescent Servitude} yields [pot], never [POT]). Stated narrowly for discipline grants only; not generalised to all cross-card effects.
  *(binds: §5.4, §1.9)*
- Two copies of a card imposing a mandatory directed action deadlock the bearer: stuck and cannot act ({Lunatic Eruption}). 1.15 states it in one sentence and defers the stuck-and-cannot-act machinery to §3.9.
  *(binds: §3.9)*
- An untitled vote bonus adds to the votes of a title gained later rather than being replaced by it ({Xeper, Sultan of Lepers}).
  *(binds: §5.8, §3.7.6)*

## §1.5

- Using an ability printed on a card in play is neither playing a card nor taking an action; costs and restrictions worded against card plays do not reach it.
  *(binds: §1.6, §1.7, §1.8, §3.7.4)*
- A [REACTION] ability does not count as playing a reaction card, but still requires a reaction window (unlocked or a wake); a conviction reaction power needs only the window, no wake.
  *(binds: §2.1, §5.2)*
- An effect letting a locked minion block is not a wake and grants no reaction-card plays.
  *(binds: §5.2, §2.1)*
- Locking bars acting and blocking, not ability use; an ability is usable while its bearer is locked unless its own text requires unlocked/acting/blocking. Where a lock is the cost, only that part requires being unlocked.
  *(binds: §5.2)*
- Abilities remain usable in torpor (including lock-to-use ones) because torpor bars only acting, blocking, reaction cards and voting; card plays from torpor require the card's own permission.
  *(binds: §5.3)*
- A minion that cannot act may still use its abilities: a recruited ally can use its abilities, including lock-to-use ones, the turn it is recruited (group G00119); likewise a minion influenced out during that influence phase.
  *(binds: §3.7.4, §5.2, §6.7)*
- An ability may be used any number of times in one action unless its own text limits it. Limits read off the wording: locking the bearer/source = once per unlock; keyed to a phase action = once per available window; other conditions rechecked at each use.
  *(binds: §1.2, §3.2, §6.6, §6.9)*
- A once-each-turn ability is spent only if it actually applies (no cost paid / action unpayable = not used).
  *(binds: §1.7, §1.8, §3.5)*
- An ability whose text is framed by combat requires its bearer to be a combatant, not merely that a combat is occurring.
  *(binds: §4.1)*
- An ability granted by a card in play is unavailable while an effect prevents the bearer from using that card.
  *(binds: §4.10, §4.1)*

## §1.6

- A requirement is checked when the card is played and on every later play; while an action is in progress it is checked continuously, so a minion who stops meeting it fails the action. A card ALREADY IN PLAY keeps its place when the requirement later lapses, and its burn options stay usable. The frozen case is permanents in play, never actions in progress.
  *(binds: §3.4, §3.7.3, §3.7.4, §5.9, §6.3, §5.1)*
- Only the keyword "put ... in play" bypasses requirements. "Equip", "recruit" and "employ" invoke the normal machinery, so requirements and cost apply as printed — {Concealed Weapon}, {Piper}, {The Summoning}, {Magic of the Smith}, {Vast Wealth}, {Pack Alpha}, {Zhenga} all print "requirements and cost apply as normal". No section may cite these as bypassing requirements.
  *(binds: §1.8, §1.9, §3.7.3, §3.7.4, §6.3, §5.5)*
- A card played "not in the normal fashion" HAS been played; it only loses the normal-play window (cannot be canceled as it is played, opens no "as played" window). 1.6 states the requirement side and cross-refs 1.8 for the played-but-not-normally corollary.
  *(binds: §1.8, §1.9, §3.4)*
- Bypassing requirements does not bypass prohibitions. A "cannot have" prohibition still blocks placement; a card placed where it cannot legally sit is burned with no cost refund, and an effect it imposed at the moment of placement persists ({Wooden Stake}). An ally's own on-entry clause fires however it entered ({War Ghoul}). This resolves the `abnormal-entry-requirements` tension.
  *(binds: §2.5, §5.2, §5.5, §3.7.3, §6.3)*
- Taking control of a card already in play is not playing it, so requirements do not apply. 1.6 carries one cross-reference sentence only; §6.3 owns the rule and the twelve [TOM 19960226-1] copies.
  *(binds: §6.3)*
- No-effect plays: the permissive default holds (a card may be played, an action taken, knowing it will accomplish nothing). Two families bar it — (i) a card whose text names the object it acts on, when no such object exists; (ii) damage prevention with no damage to prevent, and GAINING stealth or intercept not needed. REDUCING an opposing value already at its floor stays legal ({Draba}, {Night Terrors}). No section may state "futility is never a bar" or its converse.
  *(binds: §1.1, §1.8, §3.2, §3.4, §4.3, §4.5, §4.6)*
- **[SUPERSEDED 2026-07-20 — see `owner-rulings.md` A2, which is the settled form.]** What a
  printed "Only usable by ..." line restricts depends on whether using the card is the same
  act as playing it. On a card that is played and resolves (action, action modifier,
  reaction, combat card) it bars the play — `{Regeneration}` cannot be played by an untorpid
  vampire. On a card that goes into play (equipment, permanents) it gates only the conferred
  ability, and the card can still be equipped: `{Seal of Veddartha}` and `{Agate Talisman}`
  both permit the equip by a vampire under the stated capacity, and the rest of the card
  works.
  *(binds: §1.3, §1.5, §1.6, §1.8, §3.7.3, §3.7.6, §4.3, §6.3)*
  *(binds: §3.7.3, §5.1, §5.9)*
- The requirements and cost of a card fetched into play are not requirements or cost of the fetching action ({CrimethInc.} cannot key off an ally's Anarch requirement).
  *(binds: §1.7, §3.7.4, §5.8)*
- A requirement-faking ability ({Mata Hari} class) substitutes only for the effects of the card played, including its duration effects, and never for what the card does from being in play; only on a card played normally; only where the card PRINTS the requirement.
  *(binds: §2.5, §5.8, §3.7.5, §1.8)*

## §1.8

- A card brought into play by another card's effect HAS been played; it loses only the normal-play window, so it opens no "as played" window and cannot be canceled as it is played. Requirements and cost are a separate question and still apply (owner-rulings B).
  *(binds: §1.6, §1.9, §3.5, §3.7.3, §3.7.4, §6.3)*
- A canceled card's cost is paid UNLESS the canceling card's own text says otherwise. Most cancel cards print "and its cost is not paid" ({Direct Intervention}, {Sudden Reversal}, {Death Seeker}, {Asguresh}, {Hide the Mind}, {Iron Heart}, {Ophidian Gaze}, {React with Conviction}); those that do not ({Santaleous}, the {Target} aims' own discard clause) leave the cost payable, and {Botched Move} says so explicitly. The blanket phrasing "a canceled card's cost is still paid" is wrong.
  *(binds: §1.7, §3.5, §4.3)*
- An effect that lets a minion USE THE ABILITY of a card plays no card at all (e.g. {Inscription}, {Shadow Court Satyr}); it therefore does not consume that minion's own once-per-action limit on the same modifier. This is distinct from an effect that tells him to PLAY the card (e.g. {Echo of Harmonies}), which is a normal play and is cancelable as it is played.
  *(binds: §1.2, §3.7.6, §5.5)*
- When a card counts as played fixes when the window is: a political action card played from hand via {Charming Lobby} counts as played only at successful resolution and so is never open to cancellation as it is played.
  *(binds: §3.4, §3.7.6)*
- A canceled card has still been played: it consumes same-card / once-per-round limits, counts for effects that count or retrieve cards played, and its replacement happens normally with any "do not replace until" clause canceled along with it. But a canceled LIMITED effect does not trigger its limit, and a canceled Trifle grants no extra master phase action.
  *(binds: §1.2, §1.9, §1.11, §3.5, §4.3, §6.6)*
- A canceled action is not performed and the acting minion stays unlocked and may attempt it again; the same holds for an action card nullified as it is played ({Veil of Darkness}). An action canceled AFTER it has been played still counts against a "next X actions" allowance.
  *(binds: §3.4, §3.5, §5.2)*
- Canceling a strike cancels the rest of that card's effect and a new strike is chosen; canceling a maneuver provided by a strike card does NOT cancel the strike (which cannot be changed), but canceling a maneuver that provides a press does cancel the press.
  *(binds: §4.3, §4.8)*
- Permissive default stated here: a card may be played, and an action taken, knowing it will accomplish nothing. Bars on such plays are requirement-based, not futility-based, and are §1.6's to state; whether a no-effect action still succeeds and locks is §3.4's.
  *(binds: §1.1, §1.6, §3.2, §3.4, §4.5, §4.6)*

## §3.4

- An unblocked action is SUCCESSFUL and its cost is paid even when the effect cannot occur; failure of the effect never retroactively makes the action unsuccessful.
  *(binds: §3.3, §3.5, §3.7.2, §1.7, §6.5)*
- The target ceasing to qualify does not end the action — blocks and any resulting combat still happen. Only the ACTING minion ceasing to meet the action's requirement fizzles the action (owner ruling A, §1.6 owns it).
  *(binds: §1.6, §3.3, §3.7.3, §3.7.4, §5.9)*
- Riders worded 'if the action is successful' fire on a no-effect successful action; riders naming the effect itself (hunt gained blood, 'successful resolution') require the effect to have happened.
  *(binds: §3.7.2, §6.5, §3.7.1)*
- An action card nullified before the action begins produces NO action: the minion does not lock and may act again ({Veil of Darkness}, per [RBK wording-templates] cancel rule). This is distinct from a resolved action with no effect, which does lock.
  *(binds: §1.8, §1.1)*
- After a card usable 'when the action/bleed would be successful' is played, only cards with that same timing may follow; {Deflection}, {Archon Investigation}, {Telepathic Counter} must precede it. §2.3 owns the general sequencing rule.
  *(binds: §2.1, §2.3, §3.3, §1.2)*
- A bleed reduced to zero is not successful, so 'would be successful' cards cannot be used on it.
  *(binds: §3.7.1, §1.2)*
- An action that sends its acting minion into combat resolves first; 'after action resolution' effects wait until that combat ends.
  *(binds: §2.3, §4.1)*

## §3.5

- NRA bites on REACHED RESOLUTION. An action that fails or is ended has reached resolution and cannot be re-attempted by that minion; an action that is CANCELED has not reached resolution and may be re-attempted, unless it was blocked and then continued before the cancellation.
  *(binds: §1.8, §3.4, §3.6, §3.7.3, §3.7.4, §3.7.5)*
- ENDED vs FAILED: an action that ends closes the window immediately (no further modifier or reaction); an action that fails still permits modifiers and reactions usable at the end of / after an action. A failed action was NOT blocked, so block-dependent cards cannot be played.
  *(binds: §2.3, §2.4, §3.4, §3.6)*
- A canceled action is not performed and its cost is not paid, but it was still TAKEN — it counts against effects that count actions ({Enkil Cog}, {Veil the Legions}). Failure, by contrast, does not refund cost.
  *(binds: §1.7, §1.8, §6.6)*
- Sameness test for 'the same action': rulebook actions are never the same as card-provided actions; rulebook actions differ by target (equip-from-minion targets the equipment); actions from two different cards in play are not the same even at equal name. Sameness is a card-effect test ({Change of Target}, {Obedience}, {Red Herring}), not the base NRA rule.
  *(binds: §3.7.3, §3.8, §3.10)*
- Putting a card into play, or being made to recruit/employ out of turn, is not performing that card's action; the normal action remains available that turn. Consistent with owner ruling B (put-into-play bypasses requirements; the card is still played).
  *(binds: §1.6, §1.8, §3.7.4)*
- Canceling a combat leaves the action BLOCKED: blocker stays locked, {Mask of a Thousand Faces} cannot take over, combat-pertaining reactions are dead, but continue-as-if-unblocked effects still work.
  *(binds: §3.6, §5.2)*
- A canceled card is still played and still consumes its play slot (out-of-turn master), but a canceled LIMITED effect does not trigger the limit.
  *(binds: §1.8, §4.3, §6.6)*
- Cancel effects reach all action cards (employ retainer, recruit ally, political) but only cards played from hand in the normal fashion.
  *(binds: §1.8, §3.7.4, §3.7.5)*
- A minion that leaves play and returns is a new minion for NRA; substituting the acting minion mid-action does not change who took the action.
  *(binds: §5.1, §5.5, §6.4, §3.10)*

## §3.7.4

- The keywords 'recruits' / 'employs' invoke the normal machinery, so requirements and cost apply even when no action is taken ({Piper}, {Pack Alpha}, {Zhenga}); only 'put ... in play' bypasses requirements ({Summon History}). Per owner-rulings.md section B.
  *(binds: §1.6, §3.7.3, §6.3, §5.5, §5.6)*
- An ally's or retainer's own requirements and cost are NOT requirements or cost of the employ/recruit action. Effects reading the action's requirements do not see them ({CrimethInc.} not usable after recruiting an Anarch-requiring ally).
  *(binds: §1.6, §1.7, §3.4)*
- Entry by a card effect is not an action, so action-keyed effects do not attach (cost reductions naming an action, action stealth modifiers, abilities triggered by announcing an action). Effects keyed to the recruit/employ event or to the card's cost DO attach however the minion arrived.
  *(binds: §1.7, §3.2, §5.5, §5.6)*
- Such an ally/retainer is not played in the normal fashion, so nothing that cancels a card as it is played reaches it — but it HAS been played. Stated per owner-rulings.md section B corollary; §1.8 owns the distinction.
  *(binds: §1.8, §1.9)*
- Non-action entry does not count as performing the employ/recruit action, so the same minion may take the normal action for the same card later that turn if it unlocks. §3.5 owns the NRA.
  *(binds: §3.5)*
- Where a minion recruits/employs, that minion's own disciplines set the card's level; where the card is merely put in play, use the basic version ([RBK employ-retainer] / [RBK recruit-ally] advanced-rules boxes).
  *(binds: §5.5, §5.6, §6.3)*
- 3.7.4 carries only a one-sentence cross-reference for 'may use abilities the turn recruited' (§1.5, §5.2) and for 'may act that turn' (§5.5/§5.6). It does not state those principles.
  *(binds: §1.5, §5.2, §5.5, §5.6)*

## §5.5

- {Taste of Vitae} and {Enhanced Coagulant} cannot be played against an ally because their effect names the opposing vampire - there is no object. This is a missing-object case, not futility, consistent with owner ruling C.
  *(binds: §1.6, §1.1, §3.2, §4.5)*
- Cards that make a minion RECRUIT an ally ({The Summoning}, {Piper}) leave the ally unable to act that turn; cards that PUT it in play ({Summon History}, {Khazar's Diary}) do not. Same keyword split as owner ruling B.
  *(binds: §1.6, §3.7.4)*
- {War Ghoul}'s entry burn is an on-entry effect, not a recruit requirement, so 1.6's requirement bypass through abnormal entry does not reach it. Resolves the abnormal-entry-requirements tension without weakening 1.6.
  *(binds: §1.6, §3.7.4)*
- An ally acting 'as a vampire' is a vampire only for the effect generated by playing that card. Outside effects keying on 'a vampire' ({Veil of Darkness}, {The Line}) and the played card's own in-play clauses ({Descent into Darkness}) do not see it.
  *(binds: §1.5, §1.7, §6.4)*
- An added blood cost on an action or block bars an ally (e.g. {Hide the Heart} [val], {Tenebrous Form} [OBT], {Etienne Fauberge}), but a cost reduced to zero is payable ({The Shard, London}, {Kindred Segregation}).
  *(binds: §1.7, §3.3)*
- 'Starting life' is the printed value of the card that entered play and does not move with later effects; current life may exceed it.
  *(binds: §2.5, §5.7)*
- A card that lets a minion act or block 'as an ally' changes only the check it names ({Sonja Blue} blocks as an ally, still plays Discipline cards).
  *(binds: §3.3, §1.2)*

## §5.6

- A retainer using a weapon is not the weapon's bearer; the employing minion remains the bearer. Effects and costs phrased on 'the bearer' resolve against the employer; restrictions phrased on 'the bearer' do not restrict the retainer.
  *(binds: §4.3, §5.5, §1.12)*
- A retainer's use of a weapon is not a strike. It resolves the weapon's full text (torpor, combat-ending, counter burn), but yields the employer no maneuver, press or additional strike, and a striking retainer gains no additional strikes from its employer.
  *(binds: §4.3, §4.2)*
- Damage inflicted by a retainer is environmental damage with the retainer as its source; immunity to retainers or to a retainer type stops it.
  *(binds: §4.4, §4.5)*
- An action targeting a retainer does not target the minion carrying it.
  *(binds: §3.1, §3.7.4)*
- Effects already produced by a retainer survive the retainer being burned or stolen.
  *(binds: §2.5, §5.4)*
- A retainer is usable the turn it is employed. The 'cannot act this turn' restriction applies to recruited allies only: recruited by a card effect still cannot act; put into play can act. Card text granting 'can act the turn it is recruited' does not extend to an opponent's turn.
  *(binds: §3.7.4, §5.5, §1.6)*

## §5.9

- A card whose text says a vampire 'becomes' a sect changes the actual sect; a card saying a minion 'is considered' a sect while it remains in play is a temporary override on an unchanged underlying sect. The override has precedence.
  *(binds: §5.8, §2.5, §1.6)*
- Where two effects write the same trait, the most recent governs. This holds for sect, clan and acting-minion designation alike — it is not sect-specific.
  *(binds: §2.4, §3.10, §5.1)*
- An override survives a later change to the underlying trait; when the override leaves play the underlying trait resurfaces. The value an override writes is fixed at the time the card is played and is not re-read afterwards.
  *(binds: §2.5, §5.8)*
- A changed trait is the trait for all purposes and trait-keyed effects re-evaluate continuously, including mid-action (consistent with owner block A: an action whose requirement lapses mid-action fizzles) and at the moment a post-resolution effect applies.
  *(binds: §1.6, §3.2, §3.4, §3.7.7, §5.2)*
- Writing a trait onto a vampire does not make the action one 'described by' that trait: {The Red Question} is not an action that 'makes this vampire anarch'.
  *(binds: §3.7.3, §1.6)*
- Allies have no sect; permission to play cards 'as an Anarch vampire' does not confer the Anarch trait.
  *(binds: §5.5)*
