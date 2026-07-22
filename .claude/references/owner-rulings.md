# Owner adjudications — binding

Rules calls made by Lionel (the owner) on 2026-07-20 after reading the wave-1 drafts.
**These are authoritative and settle the point.** Do not re-derive them, do not soften
them, do not mark them `⚠ REVIEW`. Where a ruling in your extract appears to contradict
one of these, the adjudication wins and the ruling is the thing needing explanation.

Each was verified against actual card text via `https://api.krcg.org/card/<name>` before
being recorded here. The card text is quoted because it is the evidence.

---

## A. Requirements are checked CONTINUOUSLY during an action

Wave 1's 1.6 stated "requirements are checked when the card is played, and only then."
**That is wrong** and it inverts the real rule.

- **While an action is in progress, its requirement is checked continuously.** If the
  acting minion stops satisfying it part-way through, the action fizzles. Equip with a
  Sabbat-only equipment and change sect during the action, and the equip fails.
- **Once a card is in play with its requirements met, it stays in play** even if the
  requirement later lapses. A retainer stays when its bearer loses the discipline that
  allowed employing it; an equipment stays when the vampire's clan changes.

So the play-vs-keep distinction is about **permanents already in play**, not about actions
in progress. An action in progress is the continuously-checked case, not the frozen one.

**A trait gained later reaches a card already in play only if that card checks the trait on
an ongoing basis.** If the trait was checked only at the moment of play, acquiring it
afterwards changes nothing. `{Orun}`'s capacity bonus is checked continuously, so it
applies; the discipline level required to employ a retainer such as `{Raven Spy}` was
checked once at play, so gaining the discipline later does not retroactively validate it.
(Owner correction to the wave-1 draft, 2026-07-20.)

The owner's word for an action that fails part-way because its requirement lapsed is
**"fizzles"**. Use it.

---

## A2. "Only usable by ..." — what it restricts depends on the card type

**Owner correction, then owner re-correction, 2026-07-20. This is the settled form; earlier
drafts of this file overstated it.** The rule turns on whether using the card and playing it
are the same act.

- **Cards that are played and resolve — actions, action modifiers, reactions, combat cards
  — "only usable by/when" restricts the PLAY.** Using such a card *is* playing it, so a
  minion that does not qualify simply cannot play it. `{Regeneration}` ("Only usable by a
  vampire in torpor") cannot be played by an untorpid vampire; `{Freak Drive}` ("Only usable
  after action resolution"); `{Second Tradition: Domain}` `[REACTION]` ("Only usable by a
  locked prince or justicar").
- **Cards that go into play — equipment and other permanents — it restricts the USE of the
  ability the card confers, not putting the card into play.** `{Seal of Veddartha}` prints
  "Only usable by a vampire with capacity above 5", and a capacity-5 vampire **can still
  equip it**: the counters accrue and the granted [dom] and [for] levels still apply. What
  that vampire cannot do is use the +1 bleed Ⓓ action the clause governs.
  A ruling states this outright for the second case: `{Agate Talisman}` ("Only usable by a
  vampire with capacity 4 or more") — *"Can be equipped by a vampire with capacity less than
  4, although they cannot lock it to get a vote."* `[LSJ 20030607]`, `R0025`. Two independent
  equipment cases, both permitting the equip. Keep `R0025` in §1.6; the wave-2 3.7.6 drafter
  dropped it only because the guidance was in flux.

So: for a played-and-resolved card the clause is a play restriction; for a permanent it
gates the conferred ability while the rest of the card works normally.

*Owns it:* §1.6. *Must not contradict:* §1.3 (card types), §1.5 (ability use is not a card
play — the same seam), §1.8, §3.7.3, §4.3, §6.3.

*Owns it:* §1.6. *Must not contradict:* §3.4 (resolution), §3.7.3, §3.7.4, §5.9 (a trait
change mid-action is exactly how this comes up), §6.3.

---

## B. "Put into play" bypasses requirements — equip / recruit / employ do NOT

Wave 1's 1.6 cited `{Concealed Weapon}`, `{Piper}` and `{The Summoning}` as cards that
bypass requirements. **They are the exact opposite**, and their own text says so:

| card | text | verdict |
|---|---|---|
| `{Concealed Weapon}` | "This minion **equips** with a non-unique weapon card from your hand **(requirements and cost apply as normal)**" | requirements APPLY |
| `{Piper}` | "That Anarch **recruits or employs** an ally or retainer from your hand **(requirements and cost apply as normal)**" | requirements APPLY |
| `{The Summoning}` | "This vampire **recruits** that ally **(requirements and cost apply as normal)**" | requirements APPLY |
| `{Disguised Weapon}` | "**Equip** this vampire with that weapon **(and pay cost to equip as normal)**" | cost APPLIES |
| `{Summon History}` | "...and **put that card in play**, on this vampire" | requirements BYPASSED |

**The rule.** The keywords **equip**, **recruit** and **employ** invoke the normal
machinery, so requirements and costs apply. Only **"put ... in play"** bypasses them.

**Corollary, and it is the part that gets missed.** A card played "not in the normal
fashion" **has still been played**. What it loses is only the normal-play window: it
cannot be canceled "as it is played" and it does not open an "as played" window.
Wave 1's 1.8 is imprecise on exactly this and must be fixed.

*Owns it:* §1.6 (requirements), §1.8 (the played-but-not-normally corollary).
*Must not contradict:* §3.7.3, §3.7.4, §6.3, §1.9.

---

## C. Futility is NOT a universal permission

Wave 1's 1.6 stated "futility is never a bar." **That is too broad.** Two mechanics bar
the play outright when it would do nothing:

- **Damage prevention cannot be played when there is no damage to prevent.**
  `{Soak}`.1 and `{Glancing Blow}`.1, both `[LSJ 20001114]`: "Cannot be used if there is
  no damage to prevent."
- **You cannot GAIN stealth or intercept you do not need.**
  `{Bonding}`.1 `[TOM 19951109]`: "Cannot be used if you do not need the stealth at the
  time you play it."
  Independently confirmed by printed card text: `{Second Tradition: Domain}` `[REACTION]`
  reads "...attempt to block with +2 intercept, **even if intercept is not yet needed**."
  A card has to *override* the restriction explicitly, which is only necessary because the
  restriction is the default. Good example for §3.2.

But **reducing** the opposing value is always allowed, even to no effect:

- `{Draba}`.3 and `{Night Terrors}`.3, both `[LSJ 20021211]`: "Can be played on a minion
  with no or negative stealth, in which case it has no effect." Reducing stealth to 0 when
  it is already 0 is a legal play.

So the shape is: **playing a card to gain what you do not need is barred; reducing what is
already at the floor is not.** The permissive default still holds everywhere else — stealing
or burning blood from a vampire that has none, an action that cannot succeed — it is simply
not universal. And the bar reaches only the play itself; see the next block.

### The restriction is on PLAYING, not on effects already in play

**ADJUDICATED by the owner 2026-07-20. Settled — do NOT mark this `⚠ REVIEW`.**

`{Repulsion}`.1 `[LSJ 20011214-2]` ("`[OBE]` can be used even if the stealth is not
currently needed") looks like it contradicts `{Bonding}`. It does not, and the reason
generalises well beyond stealth.

- **Playing `{Repulsion}` is still restricted.** It is an action modifier providing +1
  stealth, so it cannot be played when the stealth is not needed, exactly like `{Bonding}`.
- **Once played at `[OBE]` it is put on the vampire** and gives a continuous +1 stealth on
  every action. That standing bonus is not a card play, so nothing restricts it. It applies
  whether or not stealth is needed on any given action.

**The general rule: a "cannot use it if you do not need it" restriction attaches to the ACT
OF PLAYING A CARD. It does not reach a continuous effect from a card already in play.**
Do not write this as a `{Repulsion}` exception — write the general rule and use
`{Repulsion}` as the example that separates the play from the standing effect.

*Owns it:* §1.6 (the restriction), §3.2 (stealth & intercept), §4.5 (prevention).
*Must not contradict:* §1.5 (ability use is not a card play — same shape), §1.8,
§2.5 (persistence of in-play effects), §3.4, §4.6.
