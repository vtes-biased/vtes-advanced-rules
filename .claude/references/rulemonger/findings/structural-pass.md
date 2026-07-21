# Structural pass — whole-document survey (2026-07-21)

Scope: `docs/extended-rules.md` at 4,858 lines, 64 sections, all four lenses
(duplications / placements / tensions / open questions). REPORT-ONLY; no document
edits. Citation-level verification was NOT redone except where needed to adjudicate a
specific tension (each such lookup is quoted below). Internal anchors were validated:
all `(#…)` links resolve (three apparent misses — `45-prevention--immunity` etc. — are
correct GitHub double-hyphen slugs for `&` headings; checker artifact, not defects).

Ranking note: findings are numbered by lens; the report's top-10 ranking is in the
session summary.

**PASS COMPLETE 2026-07-21.** All findings dispositioned: applied (E1–E118), closed by
owner adjudication, or recorded as deliberate no-change. This file stands as the record.

---

## Lens 3 — TENSIONS (reported first: these change rulings)

## F-struct-21 — §5.8.3 applies {Vidal Jarbeaux}'s once-per-game cap to {Vlad Tepes} and {Kemintiri}  [over-broad] [blocking] — APPLIED 2026-07-21 (E4/E6)
**Where:** §5.8.3: "A vampire who can meet title requirements ({Vlad Tepes}, {Vidal
Jarbeaux}, {Kemintiri}) is also considered a member of the title's underlying sect. The
controller chooses how each requirement is met — any city, even an invented one — and
each title may be used only once per game. Required to be 'a titled vampire', he must
name a title, and may choose the generic 'X votes' title only once."[^5-8-18]
Contradicts §1.6.4: "{Vidal Jarbeaux}'s own text caps each requirement at once per
game" (correctly Vidal-specific; cf. resolution R-014 item U6).
**Evidence:** {Vidal Jarbeaux} card text (KRCG): "He can meet a given requirement only
once each game." {Vlad Tepes} card text: "Vlad uses and can play cards requiring a
title or a sect as if he had that required title or were of that required sect. +1
bleed." — no cap; his rulings block (rulings.yaml 4143–4157) has none. {Kemintiri}
records (3767–3773) have none. The once-caps and the X-votes-once rule are recorded
only under Vidal: "He can meet a given generic title (eg. Prince) only once … He must
choose a title when playing a card required a 'titled' vampire … but can only choose
each title once. He can choose the non-descript 'X votes' title, but only once.
[LSJ 20050128] [PIB 20150306] [PIB 20150307] [ANK 20211019]" (rulings.yaml 4125–4128).
**Proposed fix:** In §5.8.3, keep sect-membership and made-up-city as class-general;
scope the caps: "…any city, even an invented one. {Vidal Jarbeaux}'s own text
additionally caps each requirement at once per game: required to be 'a titled vampire'
he must name a title, may use each title only once, and may choose the generic 'X
votes' title only once." A judge relying on the current text would cap {Vlad Tepes}.

## F-struct-22 — §3.7.5.1 says a *locked* acting minion kills the referendum; the ruling says *not ready*  [contradiction] [blocking] — APPLIED 2026-07-21 (E7)
**Where:** §3.7.5.1: "The referendum is conducted only if the acting minion is still
ready when the action would resolve. If combat leaves him locked, in torpor or out of
play, the action ends and no referendum happens, e.g. {Yawp Court}."[^3-7-5-3]
**Evidence:** {Yawp Court} (rulings.yaml 3310–3320): "If the acting minion is not
ready after the combat, then the action ends and no referendum is conducted.
[LSJ 20060902]" and "…the referendum is conducted after all the combats if the acting
vampire is still ready. [ANK 20180910-1] [LSJ 20060903]". "Locked" appears nowhere.
An acting minion is normally locked throughout its own action; as written, the
sentence tells a judge that *any* combat (e.g. blocked, then continued as if
unblocked) cancels the referendum — flatly wrong. §3.5.3 states the same rule
correctly ("an action whose acting minion is not ready when it would resolve simply
ends").
**Proposed fix:** "…If combat leaves him in torpor or out of play — no longer ready —
the action ends and no referendum happens." Delete "locked".

## F-struct-23 — "fizzles" is undefined and §3.4.1 frames it as the opposite of what the ruling says  [contradiction] [blocking] — APPLIED 2026-07-21 (E9–E13)
**Where:** §1.6.1: "During an action it is checked continuously; a minion who stops
meeting it fizzles the action." §3.4.1: "The target ceasing to qualify does not end
the action… An acting minion that stops meeting the action's own requirement is **the
other case** — the action fizzles ([§1.6])." §3.7.3.1: "a trait change mid-action
fizzles it." vs §5.9.3: "if {The Red Question} makes the acting vampire Anarch during
an action that required another sect, the action is **successful but has no effect**."
**Evidence:** {The Red Question} (rulings.yaml 2409–2415): "If the action required
another (non-Anarch) sect and is not blocked, the action fizzles (**is successful but
has no effect**). [ANK 20210124]". So "fizzle" = successful-with-no-effect — the SAME
outcome as the target-lapse case, not "the other case". A judge reading §1.6.1/§3.4.1
would treat the action as ended/failed (cost not paid, no riders, different NRA
posture); the source says it succeeds and pays. Note also [^1-6-1] (LSJ 20030214 /
ANK 20171212 / LSJ 20030202 — {Undead Persistence}, {Mental Maze}, {Maxwell}) does not
itself establish the continuous-check/fizzle sentence; the supporting ruling is
[ANK 20210124], cited only in §5.9's [^5-9-6].
**Proposed fix:** Define once (in §1.6.1): "…a minion who stops meeting it fizzles the
action: the action still resolves and, if unblocked, is successful and paid for, but
has no effect [ANK 20210124]." Rewrite §3.4.1's contrast — both lapse cases resolve
successful-with-no-effect; the genuine contrast is target-lapse vs *play-time*
requirement failure. Add [ANK 20210124] to [^1-6-1] or cross-cite §5.9.3.

## F-struct-24 — §3.1.1 states the superseded two-point cost-reduction timing  [stale] [minor] — APPLIED 2026-07-21 (E14–E16)
**Where:** §3.1.1: "A cost reduction offered by a card in play may be applied **either
at announcement or when the cost is paid**, e.g. {Eccentric Billionaire}."[^3-1-1]
vs §1.7.3/§2.1.4/§5.2.5: "at any point from announcement until just before the cost is
paid."
**Evidence:** G00130 "Lock to reduce cost" (rulings.yaml 4624–4627): "Can be locked to
reduce the cost **at any point before resolution, from when the action is announced to
just before the cost is paid**. [ANK 20230620] [ANK 20170605] [LSJ 20090705]". The
{Eccentric Billionaire} per-card record retains the older two-point phrasing
[LSJ 20090705] [ANK 20170605]; the group record consolidating the same IDs states the
continuous window. A judge reading only §3.1.1 disallows a mid-window lock.
**Proposed fix:** Trim §3.1.1's sentence to a cross-reference ("a lock-to-reduce
reduction may be applied at any point up to payment — [§1.7.3]"), which also resolves
duplication F-struct-8. Cite G00130.

## F-struct-25 — §1.12.1 "burned when the host leaves play, whatever sends it away" is over-broad against §6.4.1  [over-broad] [minor] — APPLIED 2026-07-21 (E17–E18, owner's region model + printed-text override)
**Where:** §1.12.1: "A card on a host is burned when the host leaves play, whatever
sends it away. **This covers a minion moved out of play by a card effect**: cards on
the initial target burn, e.g. {Memory's Fading Glimpse}, {Raw Recruit}." vs §6.4.1:
"The wording template is {Lay Low} and {Banishment}: cards and counters stay with the
vampire but are out of play while it is." A {Banishment}ed vampire *is* "moved out of
play by a card effect", yet its cards are not burned. The reconciling discriminator is
in neither subsection (the §1.12 preamble has only half of it).
**Evidence:** {Memory's Fading Glimpse} text: host goes "to the bottom of his or her
crypt" — "Any cards on the target minion are burned. [SFC 19960919]" (rulings.yaml
1949). {Raw Recruit}: torpid vampire moved onto the card, "face up and out of play" —
"Blood, equipments and other cards on the initial target are burned. [LSJ 20100302-2]"
(2373). {Lay Low} card text *prints* the exception: "Any cards and counters on this
vampire remain with him or her (but are out of play…)". {Banishment} moves to the
uncontrolled region, where the rulebook keeps cards. So: cards burn on any departure
from play **except** a move to torpor/the uncontrolled region or an effect that prints
that they stay — {Raw Recruit} shows that a mere set-aside out of play does NOT keep
them.
**Proposed fix:** §1.12.1 first paragraph: "…whatever sends it away, unless the minion
moves to torpor or the uncontrolled region, or the effect prints that the cards stay
({Lay Low}). A set-aside without such text still burns them, e.g. {Raw Recruit}."

## F-struct-26 — §6.2.5 restates the optional-effect decider in the flat form R-003 rejected  [contradiction] [note] — APPLIED 2026-07-21 (E19; R-003 settled wording-decides)
**Where:** §6.2.5: "An optional effect on a minion is taken or declined by that
minion's controller ([§1.1])…" vs §1.1.1: "Who takes or declines an optional effect on
a card in play **follows the card's wording**, not control of the card."
**Evidence:** R-003 (open): the recovered [ANK 20210309-3] grounds the decider in the
card's wording ("this vampire can…" → vampire's controller; "you may" → card's
controller). §6.2.5's flat form would misrule a "you"-worded master on a stolen
minion. {The Rack}'s gain is vampire-directed, so the example survives either way.
**Proposed fix:** "…is taken or declined per the card's wording ([§1.1]): the new
controller of a stolen vampire decides whether it gains blood from {The Rack}." Hold
until R-003 is settled; whatever wording the owner picks must land in both places.

## F-struct-27 — §3.4.1 lists {Triole's Revenge} on the wrong side of the hunt/hunt-action split  [style] [note] — APPLIED 2026-07-21 (E20–E21, with bleed parallel)
**Where:** §3.4.1: "A hunt is unsuccessful if no blood is gained, though the hunt
action itself succeeded, e.g. {Hospital Food}, {Triole's Revenge} (see [§3.7.2])."
**Evidence:** §3.7.2.2 (correct, [TOM 19951212-3]): "{Triole's Revenge} … names the
hunt **action**, so it fires although the hunt gained nothing." Attaching it to the
"hunt unsuccessful" sentence invites the opposite reading.
**Proposed fix:** Drop {Triole's Revenge} from §3.4.1's example list (keep {Hospital
Food}); §3.7.2.2 already owns the contrast.

---

## Lens 1 — DUPLICATIONS

The style mandate is synthetic: full statement once, cross-reference elsewhere. Class
for all: [style]; severity [minor] unless noted — the aggregate is the single biggest
tightening opportunity. "Owner" = section that should keep the full statement.

## F-struct-1 — §1.14.1–.2 vs §3.1.1: named/announced cards, near-verbatim twice — APPLIED 2026-07-21 (E34–E36)
**Where:** §1.14.2: "A card named from hand must be in hand when the naming card is
played, before the replacement for that card is drawn. It need not be shown: you may
set it apart face down, e.g. {Disguised Weapon}, {Charming Lobby}… If the action is
canceled or fails, the named card stays in hand…" ≈ §3.1.1: "A card named as part of
the announcement must be in hand at that moment, before the announcing card is
replaced. It need not be shown and may be set apart face down, e.g. {Concealed
Weapon}, {Charming Lobby}… If the action is canceled or fails, that card stays in
hand." Footnotes [^1-14-4] and [^3-1-2] cite the same six IDs. Same pattern for
ash-heap naming: §1.14.1 vs §3.1's "A card to be retrieved from the ash heap is named
at declaration" ([^1-14-1] = [^3-1-4]: LSJ 20010627, LSJ 20050422).
**Proposed fix:** §1.14 owns (the section exists for set-aside/announced cards).
§3.1.1 keeps one sentence per rule + link; §1.9.1 keeps only its replacement-ordering
angle. Saves ~a paragraph and removes a drift risk between two full statements.

## F-struct-2 — Chapter 6 states the ousted-controller removal rule four times — APPLIED 2026-07-21 (E37–E40)
**Where:** §6.1.2 ("A vampire in the uncontrolled region belongs to his last permanent
controller… removed from the game if that Methuselah is ousted… {Lay Low},
{Banishment}"), §6.2.4 ("A vampire permanently controlled by a Methuselah other than
his owner is removed when that controller is ousted, and stays in play when only his
owner is ousted, e.g. {Lay Low}"), §6.5.3 ("A vampire in another Methuselah's
uncontrolled region is removed if that Methuselah is ousted and stays if only its
owner is… a stolen minion due to return to an ousted one is removed"), §6.7.1 ("…goes
to its last permanent controller's region… removed from the game if that Methuselah is
ousted, e.g. {Banishment}, {Lay Low}"). All four cite ANK 20200408-2 / ANK 20210630 /
RTR 20000501.
**Proposed fix:** §6.5.3 ("Cards of an ousted Methuselah") owns the full doctrine.
§6.2.4 keeps only the reversion mechanics unique to it ({Parmenides} indefinite keep);
§6.1.2 and §6.7.1 keep one line + link each.

## F-struct-3 — The "would be successful" sequencing rule is stated six times — APPLIED 2026-07-21 (E41–E46)
**Where:** §1.2.3 ("once a card with that timing has been played, only cards with the
same timing may follow"), §2.1.4 ("The 'as the action/bleed would be successful'
window is the last one…"), §2.2 ("A card printed 'before action resolution' is barred
once any card usable 'as the action would be successful' has been played"), §2.3.1
("…a card usable when a bleed would be successful is earlier still and cannot follow
one"), §3.4.3 ("After one is played the action is about to resolve: only other cards
with that same timing may follow"), §3.7.1.3 ("{Deflection} must be played before
action resolution, ahead of any card usable as the bleed would be successful"). The
cross-refs even point at each other ("[§3.4] states the same sequencing").
**Proposed fix:** §3.4.3 owns (the window is its subject). §2.3.1 keeps the
window-ordering frame; the other four reduce to one clause + link. Delete the
"states the same sequencing" admissions.

## F-struct-4 — Block-burn cost/effect discriminator: §1.7 and §3.3.3 each state it in full — APPLIED 2026-07-21 (E47–E50)
**Where:** §1.7.5: "A burn triggered by blocking does not gate the block: an empty
vampire blocks and burns what it has, e.g. {Camarilla Exemplary}, {Dónal O'Connor}. A
cost 'to attempt to block' does gate it… e.g. {Tenebrous Form}."[^1-7-21] ≈ §3.3.3:
"'Must burn 1 blood to attempt to block' is a cost, so a minion who cannot pay cannot
attempt, e.g. {Dominion}, {Tenebrous Form}… 'Vampires blocking this vampire burn 1
blood' is an automatic effect: an empty vampire still blocks and burns what it
can…"[^3-3-15][^3-3-16]. Plus the per-attempt/resign rule twice: §1.7.1 and §3.3.2.
Shared refs: LSJ 19970707, TOM 19951215-1, ANK 20230226, LSJ 20031121-2.
**Proposed fix:** §3.3.3 ("The cost of blocking") owns both halves and the resign
rule. §1.7.1/§1.7.5 keep the generic cost-vs-triggered-burn discriminator (their
topic) with {Tenebrous Form} as a pointer example + link.

## F-struct-5 — Queued-combat rules stated in §4.1.4, §4.9.3 and §5.3.1 — APPLIED 2026-07-21 (E51–E54)
**Where:** §4.1.4: "Only one combat is pending at a time… Both intended combatants
must be ready when the effect resolves, and a vampire on his way to torpor is not
ready, e.g. {Hidden Lurker}, {Pocket Out of Time}." ≈ §4.9.3: "At most one combat may
be queued at a time… A new combat cannot be started against a minion that is not ready
— one going to torpor…" ≈ §5.3.1: "No effect may bring a vampire on its way to torpor
into a new combat, e.g. {Hidden Lurker}, {Psyche!}." All cite RTR 20020501 /
ANK 20220429 / LSJ 20100604-1.
**Proposed fix:** §4.9.3 ("Queuing a new combat") owns. §4.1.4 collapses to a link (it
adds nothing); §5.3.1 keeps one line + link.

## F-struct-6 — §4.1.1 vs §4.2.1: range-setting replaces determine-range, near-verbatim — APPLIED 2026-07-21 (E55)
**Where:** §4.1.1: "An effect that sets the range for the round replaces the
determine-range step: that step is skipped and no maneuver or other effect can reset
the range that round, e.g. {Omael Kuman}. Cards playable before range is determined
may still be played after it."[^4-1-1] ≈ §4.2.1: "Once such an effect resolves, the
determine range step is skipped for that round and no other effect can reset the
range. Other before-range effects may still be played afterwards."[^4-2-1] Both cite
RTR 19970630 + ANK 20180720.
**Proposed fix:** §4.2.1 owns (Range). §4.1.1 keeps its where-cards-fall framing with
a link; delete the restatement.

## F-struct-7 — Title-requirement-faking: §1.6.4 vs §5.8.3 full duplication — APPLIED 2026-07-21 (E1–E6, consolidated into §5.8.3)
**Where:** §1.6.4: "Meeting a title requirement makes the vampire a member of the
underlying sect; the controller chooses how it is met, including a made-up city…
The title grants no votes in the resulting referendum, and remains available after the
sect ceases to exist."[^1-6-19] ≈ §5.8.3 (same content, [^5-8-18]–[^5-8-20]; identical
IDs LSJ 20050128, PIB 20150306/307, ANK 20211019, ANK 20231221, LSJ 20050124,
ANK 20230503).
**Proposed fix:** §5.8.3 ("How requirements read titles") owns everything
title-specific. §1.6.4 keeps the general Mata-Hari template and one line + link for
titles. Fixing F-struct-21 at the same time leaves only one place to get right.

## F-struct-8 — Lock-to-reduce-cost timing stated four times — APPLIED 2026-07-21 (E14 + E56–E57)
**Where:** §1.7.3 ("may be locked at any point from announcement until just before the
cost is paid… must be locked at announcement [when it enables affordability], e.g.
{Sunset Strip, Hollywood}"), §2.1.4, §3.1.1 (stale variant, F-struct-24), §5.2.5
(full restatement with both halves).
**Proposed fix:** §1.7.3 owns (costs). §2.1.4, §3.1.1, §5.2.5 keep one clause + link.
Cite G00130 in the owner's footnote.

## F-struct-9 — Cost/gain simultaneity (3×) and oust-before-triggers (4×) — APPLIED 2026-07-21 (E58–E61)
**Where:** simultaneity: §1.7.1 ("The cost of playing a card and the gain that card
yields happen in one step, so no oust intervenes — even where another card imposed the
cost"), §2.4.3 ("A cost paid and a benefit gained by the same effect happen at the
same time… {Minion Tap} is playable at 4 pool with {Villein}"), §6.5.1 ("A card's cost
and its pool gain happen together, with no oust between: {The Eternals of Sirius}…").
Oust-first: §1.7.1, §2.4.3 ([^2-4-17]), §5.5.3 ("an oust resolves before the effects
triggered by the burn"), §6.5.2 ("the oust precedes the effects triggered by that
minion burning, e.g. {Herald of Topheth}"). Shared IDs LSJ 20020620, LSJ 20080512.
**Proposed fix:** §1.7.1 owns simultaneity; §6.5.2 owns oust-ordering. The other
occurrences keep one clause + link.

## F-struct-10 — Recruit-vs-put acting rules: §3.7.4.3, §5.5.4, §5.6.5 — APPLIED 2026-07-21 (E62–E65)
**Where:** §5.6.5 restates §5.5.4's ally content nearly verbatim ("An ally recruited
by a card effect still cannot act that turn, e.g. {Piper}, {The Summoning}… An ally
put into play rather than recruited can act that turn, e.g. {Summon History}. Text
letting a minion act the turn it is recruited does not let it act on an opponent's
turn… {Nocturn}, {Infernal Servitor}") with the same six IDs; §3.7.4.3 both defers to
§5.5/§5.6 AND restates the opponent's-turn rule.
**Proposed fix:** §5.5.4 owns the ally rules. §5.6.5 keeps only the retainer side
("usable the turn it is employed") + link; §3.7.4.3 keeps the pure cross-reference.

## F-struct-11 — Unlock-to-block template: §3.3.1 vs §5.2.3 — APPLIED 2026-07-21 (E66–E67)
**Where:** §3.3.1's four-bullet template ({Guard Duty}, {Second Tradition: Domain})
vs §5.2.3: "An unlock-to-block effect may be used by a minion already attempting to
block, e.g. {Second Tradition: Domain}. The block and any resulting combat still
happen when the unlock leaves the action without a suitable target, e.g. {Guard Duty}
against an {Ambush}." Both cite ANK 20181122-2 and LSJ 20090514.
**Proposed fix:** §3.3.1 owns the template. §5.2.3 keeps one line + link.

## F-struct-12 — Torpor card-play doctrine in §1.5.2 duplicates §5.3 (also a placement defect, F-struct-17)
**Where:** §1.5.2: "A vampire in torpor can take no action but leave torpor, and
cannot block, play reaction cards or vote… Action modifiers are not barred either…
{Cloak the Gathering}, {Make an Example} — and a vampire in torpor plays them during
his own actions, e.g. {The Kiss of Ra}… but not during another minion's action." ≈
§5.3 base rules + §5.3.2 ("A vampire acting from torpor… plays action modifiers as
normal, e.g. {The Kiss of Ra}") with overlapping refs (PIB 20150720, RTR 19970306,
LSJ 19970325).
**Proposed fix:** §5.3 owns torpor card-play rules. §1.5.2 keeps its actual subject —
lock/torpor do not bar *ability* use, lock-as-cost needs unlocked — plus a link.

## F-struct-13 — Blocked leave-torpor diablerie window: §3.7.7.2 vs §3.7.8.4 — APPLIED 2026-07-21 (E68–E71)
**Where:** §3.7.7.2: "The blocker's diablerie opportunity arises at block resolution.
A card that ends the action before block resolution denies it, e.g. {Change of
Target}, {Mirror Walk} at [THA]." ≈ §3.7.8.4: "An effect that unlocks the acting
minion or ends the action before block resolution removes that opportunity, e.g.
{Change of Target}." [^3-7-7-3] and [^3-7-8-8] share LSJ 20050105-2 / PIB 20121216.
**Proposed fix:** §3.7.7.2 owns; §3.7.8.4 keeps one line + link.

## F-struct-14 — Leave/re-enter memory and uncontrolled-region suspension: five statements — APPLIED 2026-07-21 (E72–E75)
**Where:** "same card remembers everything / effects resume": §1.13.4 ({The Rack}
resumes), §2.5.4 ("The uncontrolled region suspends rather than erases… titles and
continuous effects resume"), §5.8.1 ("A vampire who leaves play and returns remembers
titles gained and lost"), §6.4.1 (owns: "the card remembers everything"), §6.4.3
({The Rack} tracks). Capacity-modifier suspension specifically: §2.5.4, §5.1.2,
§6.7.1 — three full statements with identical refs (PIB 20140122, TOM 19951209).
**Proposed fix:** §6.4.1/§6.4.3 own the general suspension/memory doctrine; §5.1.2
owns the capacity instance. §1.13.4 keeps contest-specifics (fresh copy ≠ same card),
§2.5.4 and §6.7.1 and §5.8.1 reduce to one line + link each.

## F-struct-15 — Long tail of two-place restatements — APPLIED 2026-07-21 (E76–E114). Skipped as already resolved: Yawp (E7/E8), ousted-no-discard (E33), hunt-vs-hunt-action (E20). Owner-recorded NO CHANGE: immediate-vs-duration prevention dual statement (§1.6.5/§4.5.1); {Repulsion} triple statement kept (only [^4-5-3]'s parenthetical trimmed, E114).
Each item: statement locations → proposed owner. Shared reference IDs verified via
footnote grep; quotes on request.
- Referendum-ability once-per-referendum / locked / torpor (G00039/G00040): §1.2.1,
  §3.7.6.4, §5.3.2 (+ cited again in §1.5's [^1-5-4]) → **§3.7.6.4**.
- Two actions from one source not cross-restrictive: §1.2.1 vs §3.8.1–.2 (same IDs
  LSJ 20100909, ANK 20220615, ANK 20200810) → **§3.8**.
- Equipment-provided action with equipment lost at resolution: §3.4.1 vs §3.8.3 (both
  RTR 19960221) → **§3.8.3**.
- {Perfectionist}/{Corporal Reservoir} decider: §1.1.1 vs §6.6.3 (both
  ANK 20210309-3) → **§1.1.1**; §6.6.3 line + link (pending R-003).
- Wake playable in the "as played" window: §1.8.1 vs §5.2.3 (both LSJ 20021011,
  ANK 20231028) → **§1.8.1**.
- {Michael Luther} unlock-mid-referendum: §1.2.1 vs §3.7.5.3 (LSJ 20041207) →
  **§3.7.5.3**.
- {.44 Magnum} limit travels with the card: §1.2.1 vs §4.10.2 (LSJ 19980302-2) →
  **§4.10.2** for weapons; §1.2 keeps the abstract template.
- {Owain Evans} per-phase across control change: §1.2.1 vs §6.2.5 (LSJ 20040127) →
  **§1.2.1** (or §6.2.5); one of the two trims.
- {Kerrie}/{Baal's Bloody Talons} out-of-play weapon: §1.10.3, §1.14.3, §4.10.4 (all
  LSJ 20100211-2) → **§1.14.3**. (Also: the three state the burn moment as "end of
  the round" / "end of the round or of the action" / "end-of-action" — harmonize to
  the card wordings when trimming.)
- Cancel kills do-not-replace clause: §1.8.3 vs §1.9.3 (identical ID sets) →
  **§1.8.3**; §1.9.3 line + link.
- {Malkavian Dementia} / {Port Authority} unlock-phase ordering: §1.9.2, §2.4.5,
  §6.2.1 (ANK 20200129, LSJ 20091208, RTR 19951017) → replacement half **§1.9.2**,
  control-reversion half **§6.2.1**; §2.4.5 trims.
- Post-resolution/after-combat mutual orderability: §2.3.2, §2.4.1, §4.9.4 (shared
  ANK 20230314, LSJ 20100324, LSJ 20071116) → **§2.3.2** (action) and **§4.9.4**
  (combat); §2.4.1 keeps the abstract principle only.
- {Momentary Delay}/{Follow the Blood} take others only before: §2.3.1 vs §2.4.1
  (LSJ 20100206-2) → **§2.3.1**.
- Environmental damage vs dodge (standing lands, strike-rider dodged): §4.4.3 vs
  §4.6.3 (identical ID sets) → **§4.6.3**; §4.4.3 keeps classification + link.
- {Rötschreck} beats announced dodge/combat-ends: §4.6.3 bullet vs §4.7.2
  (LSJ 20011005, ANK 20211102) → **§4.7.2**.
- {No Secrets From the Magaji} not a wake: §1.5.1 vs §5.2.3 (LSJ 20070208) →
  **§5.2.3**; §1.5.1 line + link.
- Non-target Methuselah waits before reducing stealth: §3.2.5 vs §3.3.2
  (ANK 20200607) → **§3.3.2**.
- Block triggers survive the action ending: §3.3.4 vs §3.5.3 (RTR 19991206,
  LSJ 20091125) → **§3.3.4**.
- Delayed block-triggered effect pre-empts: §2.4.4 vs §3.3.4 (ANK 20210627/20211207/
  20220116) → **§2.4.4**; §3.3.4 line + link.
- Contested title-providing card face down, action unusable: §1.13.3, §3.8.3, §5.8.1
  (all LSJ 20070808-2) → **§5.8.1**; other two line + link.
- {Yawp Court} no-referendum-if-not-ready: §3.5.3 vs §3.7.5.1 → **§3.7.5.1** (after
  F-struct-22's fix); §3.5.3 keeps the generic ends-if-not-ready sentence. — APPLIED
  2026-07-21 (E8).
- Locquipment control-change and directed-at rules: §1.3.1 restates §6.3.2/§6.3.3 and
  §3.1.5 (RTR 19960112, LSJ 19971002, LSJ 20090324) → **§6.3** / **§3.1.5**; §1.3.1
  lines + links (links already present).
- Hunt vs hunt-action success: §3.4.1 vs §3.7.2.1 (same IDs) → **§3.7.2.1**; §3.4.1
  one clause + link (near-compliant already; see F-struct-27).
- {Nahir}/{Nonu Dis}: §1.2.1 vs §6.6.4 (same IDs) — R-001 kept both consistent;
  optional trim of §6.6.4 to a link. Flag only.
- Immediate-vs-duration prevention: §1.6.5 vs §4.5.1 (same IDs) → **§4.5.1**; §1.6.5
  keeps the family taxonomy (by design) — no change, recorded for completeness.
- {Repulsion} play-vs-standing: §1.6.5, §3.2.3, §4.5.1 — deliberate post-R-012
  emphasis; §3.2.3 owns; consider trimming §4.5.1's [^4-5-3] parenthetical.
- Ousted mid-turn → no discard phase/no replacement: §6.5.2 vs §6.9.2 (LSJ 20090731)
  → **§6.5.2**; §6.9.2 line + link.

---

## Lens 2 — WRONG PLACEMENTS

## F-struct-16 — {Deer Rifle}/cannot-strike maneuver rule sits in a duration section  [style] [minor] — APPLIED 2026-07-21 (E22–E24)
**Where:** §1.2.2 ("Duration of maneuvers and presses"): "An optional maneuver printed
on a weapon cannot be used when the strike itself cannot be used, e.g. {Deer Rifle}
against {Hidden Lurker}; a minion who cannot strike at all can neither play nor use
one."[^1-2-11] Not a duration/periodicity rule.
**Proposed fix:** Move (clean) to §4.10.1, which already states it ("The dependency
runs one way only…"); delete here, keep §1.2.2 for the genuinely durational {Eyes of
the Beast} sentence.

## F-struct-17 — §1.5.2's torpor card-play sentences belong to §5.3  [style] [minor] — APPLIED 2026-07-21 (E25–E30)
**Where/fix:** see F-struct-12. Move is clean: §5.3.2 already carries the content.

## F-struct-18 — §1.6.4's title-requirement paragraph belongs to §5.8.3  [style] [minor] — APPLIED 2026-07-21 (with E1–E6, first batch)
**Where/fix:** see F-struct-7. Clean move; §1.6.4 keeps one pointer line.

## F-struct-19 — §4.7.4 "Environmental damage" is a two-line stub of other sections  [style] [note] — APPLIED 2026-07-21 (E31–E32, subsection deleted)
**Where:** §4.7.4: "Environmental damage is inflicted even against a dodge, but a
strike: combat ends ends combat before it is applied. See [§4.4]." The dodge half is
§4.6.3's bullet; the combat-ends half belongs in §4.7.1/§4.7.2 as one sentence.
**Proposed fix:** Fold the sentence into §4.7.2 and delete the subsection (renumber or
leave a tombstone per the chapter-6.8 precedent — owner's call).

## F-struct-20 — §6.9.2's ousted-no-discard-phase sentence duplicates §6.5.2  [style] [note] — APPLIED 2026-07-21 (E33)
**Where:** §6.9.2: "A Methuselah ousted during their turn gets no discard phase — the
next turn begins at once and cards left unreplaced are never replaced ([§6.5])."
**Proposed fix:** Already carries the link; trim to "An ousted Methuselah gets no
discard phase ([§6.5.2])" or delete.

---

## Lens 4 — OPEN QUESTIONS

## F-struct-28 — ⚠ REVIEW inventory (5 markers; 2 closable on present evidence)
1. **§1.8.5 (line 609)** — CLOSED, APPLIED 2026-07-21 (owner adjudication; proposed
   text applied) — "whether a canceled play consumes the resource that enabled
   it is unsettled: {Nergal}… {Vidal Jarbeaux}…" — **closable**. Evidence: {Nergal}
   [LSJ 20091021-2]: "If a card he plays is cancelled as it played **and no cost is
   paid**, his ability is not considered used for the turn" — his ability is a cost
   reduction, and the thing it applies to (the cost) never happened; cf. §1.5.4's own
   rule "a once-each-turn ability is spent only if it actually applies". {Vidal}
   [ANK 20200710]: "If a card he plays is canceled as it is played, he is still
   considered having used the requirement" — requirement-meeting applies to the
   *play*, and a canceled card has still been played (§1.8.3). Proposed replacement
   text: "A canceled play spends a use if the use attached to the play itself
   ({Vidal Jarbeaux} [ANK 20200710]: the canceled card was still played), and does not
   if it attached to an element the cancellation removed ({Nergal} [LSJ 20091021-2]:
   no cost paid, so the cost reduction never applied — §1.5.4)." Owner adjudicates.
2. **§2.2 (line 1221)** — as-announced stealth vs the not-needed bar — **stays open**;
   no adjudicated source found this pass.
3. **§3.7.2.2 (line 2095)** — CLOSED, APPLIED 2026-07-21 (owner adjudication; proposed
   text applied) — hunt-bonus blood source — **closable: the contradiction
   the footnote asserts does not exist.** G00121 (rulings.yaml 4595): "Is affected by
   Hunt value. All blood that is gained from the Hunt is taken from the target minion.
   (**{Festivo dello Estinto} is not blood gained from the hunt**) [RTR 20180511]
   [RTR 20030519]". The "blood bank" per-card copies live under {Festivo dello
   Estinto} and {Inbase Discotek, Frankfurt} — neither is a G00004 member, and both
   cards *print* "from the blood bank" ("gain enough blood **from the blood bank** to
   reach full capacity" / "an additional blood **from the blood bank**"). Proposed
   fix: drop the ⚠ and the "contradicted by" clause in [^3-7-2-5]; add: "A rider that
   grants blood from the blood bank is a separate gain, not hunt blood, and comes from
   the bank as printed, e.g. {Festivo dello Estinto} [RTR 20180511]." Cite G00121
   alongside G00004.
4. **§4.9.1 (line 3379)** — full end-of-round order unadjudicated — **stays open**;
   correctly scoped (the Yawp Court G-record confirms only pairwise orderings).
5. **§5.9.2 (line 4215)** — two live overrides, earlier lapses first — **stays open**.

## F-struct-29 — Half-empty promise: §3.7.6.5 sends "allocation limits" to §6.5, which doesn't cover them  [style] [note] — APPLIED 2026-07-21 (E115)
**Where:** §3.7.6.5: "Pool paid, gained or lost as a consequence of a referendum,
including allocation limits and simultaneous ousts, is [§6.5]'s." §6.5.4 delivers
simultaneous ousts; nothing in §6.5 addresses allocation limits. The nearest content
is §3.7.5.2 ("Where the terms cannot be carried out in full, the calling Methuselah
chooses within them", {Parity Shift} [LSJ 20010606]).
**Proposed fix:** Either point the allocation clause at §3.7.5.2, or add the
allocation rule to §6.5 (owner's call on which section owns {Parity Shift}
allocation).

## F-struct-30 — Promised but unstated: "a limited effect binds the action" is attributed to §1.2, which only implies it  [gap] [note] — APPLIED 2026-07-21 (E116–E117; supporting ID verified as [ANK 20190117-1] under {Mask of a Thousand Faces})
**Where:** §1.15: "A limited effect binds the action itself; see [§1.2]." §3.10.1:
"He cannot use a limited effect if a limited effect has already been used on the
action ([§1.2])." §1.2.6 states only that "(limited)" is a rulebook cap and gives the
once-per-round additional-strike example; it never states the binds-the-action(-not-
the-minion) rule the two callers promise.
**Proposed fix:** Add one sentence to §1.2.6: "The limit binds the action (or round),
not the minion: a substitute acting minion cannot use a limited effect if one has
already been used on the action" with the §3.10.1 citation ([RTR 20041202] or the ID
verified by the per-section cycle), or repoint both cross-references at §3.7.1's base
rules.

## F-struct-31 — Ⓓ symbol used once, undefined by the conventions  [style] [note] — APPLIED 2026-07-21 (E118)
**Where:** §5.4.1: "An ally that burns as a result of a Ⓓ action…" The conventions
block defines braces and brackets only. Ⓓ is standard card-text notation but appears
exactly once in the document.
**Proposed fix:** Either replace with "directed" or add Ⓓ to the conventions list.

## Checked clean
- All internal `(#…)` anchors resolve (GitHub double-hyphen slugs for `&` headings are
  correct as written).
- Spot-checked ~25 cross-reference promises (targets deliver the promised content):
  §1.2.6→§1.8, §1.6.5→§1.9.4/§4.5, §3.2.1→§1.6, §4.2.4→§4.10, §5.3.3→§5.7,
  §2.4.6→§5.9, §3.3.1→§5.5, §1.7.3→§1.3, §6.9.1→§5.3, §3.6.2→§4.9, §5.2.5→§1.6,
  §4.3.5→§5.6, §1.13.1→§5.7.7 (the R-016 fix holds), and others — no further broken
  promises found beyond F-struct-29/-30.
- The two §1.8/§3.5 pilot sections were treated as exemplars; no findings against
  their register.
