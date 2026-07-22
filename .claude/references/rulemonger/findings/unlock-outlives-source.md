# Findings — cross-section sweep: unlock-effect-outlives-source (2026-07-22)

Discriminator swept (adjudicated): the printed duration clause decides whether a
"does not unlock as normal" effect survives its source's removal. State-tied
({Rowan Ring}, {Wooden Stake}: "as long as he or she remains in torpor") → outlives the
card; flat in-play text ({Rötschreck}) → ends when the card leaves play.

Sources verified this sweep:
- `101655|Rowan Ring` rulings .5/.6 — "If placed on a minion that cannot have equipment,
  the Ring is burned. The 'does not unlock as normal' effect still applies." / "The
  'does not unlock as normal' effect continues to apply if the Ring is burned or moved."
  [LSJ 19980831]
- `102192|Wooden Stake` — same two sentences, same ID [LSJ 19980831].
- `101654|Rötschreck` ruling .10 — "The 'does not unlock as normal' effect stops if
  Rötschreck is burned or removed." [ANK 20191025]; original fetched (VEKN forum #97560),
  Ankha verbatim: "A unlocks as normal since Rötschreck is not in play."
- Card texts (KRCG): {Rowan Ring} / {Wooden Stake} print "doesn't unlock as normal during
  the unlock phase **as long as he or she remains in torpor**"; {Rötschreck} prints
  "This vampire does not unlock as normal." flat.

## F-unlock-1 — §1.6.3 states placement-effect persistence as general, omitting the duration-clause discriminator  [over-broad] [minor]
**Where:** §1.6.3 Cards entering play abnormally, lines 340–342:
> A card placed where it cannot legally sit is burned without cost refund, though an effect it imposed on
> placement persists, e.g. {Wooden Stake}'s "does not unlock as normal".

**Evidence:** Both rulings behind [^1-6-10]'s persistence half concern state-tied clauses
only ({Rowan Ring}/{Wooden Stake}, [LSJ 19980831], quoted above; both cards print "as
long as he or she remains in torpor"). The document's own canonical section says survival
past the source is *decided by the duration clause* (§2.5.3, [^2-5-11]), and the
Rötschreck side ([ANK 20191025]: "A unlocks as normal since Rötschreck is not in play")
shows persistence is not a general property of imposed effects. §1.6.3 attributes the
Ring/Stake outcome to a general "placement effects persist" rule; §2.5.3 attributes it to
the state-tied clause. Same outcome, divergent rationale — and the §1.6.3 rationale
misrules the next card if its imposed effect is worded flatly.

**Proposed fix** (exact against current wrapped text; footnote [^1-6-10] unchanged —
[LSJ 19980831] is already cited with {Rowan Ring}/{Wooden Stake} record keys):

Current (lines 339–342):
```
Bypassing requirements does not bypass prohibitions: {Heidelberg Castle, Germany} cannot move equipment onto {Enkidu,
The Noah}. A card placed where it cannot legally sit is burned without cost refund, though an effect it imposed on
placement persists, e.g. {Wooden Stake}'s "does not unlock as normal". An ally's on-entry clause fires however it
entered, e.g. {War Ghoul}.[^1-6-10]
```

Replacement (120-col rewrap):
```
Bypassing requirements does not bypass prohibitions: {Heidelberg Castle, Germany} cannot move equipment onto {Enkidu,
The Noah}. A card placed where it cannot legally sit is burned without cost refund, though an effect it imposed on
placement survives if its duration clause so provides, e.g. {Wooden Stake}'s "does not unlock as normal", tied to the
victim remaining in torpor ([§2.5.3](#253-effects-outliving-their-source)). An ally's on-entry clause fires however it
entered, e.g. {War Ghoul}.[^1-6-10]
```

If the owner declines the added link (R-022 cross-reference ceiling), the no-link
variant: "… though an effect it imposed on placement survives per its printed duration
clause — {Wooden Stake}'s "does not unlock as normal" is tied to the victim remaining in
torpor."

## Clean verdicts (no edit)

| Site | Verdict |
|---|---|
| §2.5.3 ¶4 + [^2-5-11] (canonical) | Clean. Both sides stated per the discriminator; [LSJ 19980831] filed under {Rowan Ring} AND {Wooden Stake}, [ANK 20191025] under {Rötschreck}; ANK original confirms the DB paraphrase. |
| §5.2.2 / §5.2.3 | Clean. Suppression-scope only (wakes/unlock effects, burn-at-unlock templates); no persistence claim, so nothing to point at §2.5.3. |
| §1.6 (Wooden Stake example) | = §1.6.3, F-unlock-1 above. |
| §4.4.1 ([^4-4-3] {Rowan Ring}) | Clean. No-damage-strike rule ([RTR 19960221]); not this tension. |
| §4.6.1 (Ring stays on bearer after dodge) | Clean. Matches Ring ruling .3 [LSJ 19980219] [ANK 20220923]; not a persistence claim. |
| §4.9.2 ({Rötschreck} in continued combat, [^4-9-9]) | Clean. Matches ruling .9 [RTR 20020501] [LSJ 20071009] — card is still in play there, so "still does not unlock as normal" is on the correct side. |
| §4.10 | No {Rowan Ring}/{Wooden Stake} content; nothing to sweep. |
| §5.3 (torpor) | Clean. "A torpid vampire unlocks as normal" is the base rule; {Rowan Ring} appears only via [^5-3-4] (Undying Tenacity delayed torpor). |
| §5.6.2 / §5.6.4 | Clean. Whole-text resolution; "already produced" survival exemplified by a stated-duration grant ({Camarilla Vitae Slave}) — consistent. |
| §6.4.3 | Clean. Restates the already-produced half with counter examples ({Tegyrius}); not divergent from the discriminator. |
| Appendix A "{Rowan Ring} / {Wooden Stake} duration clause" (lines 3997–3999) | Clean. States the discriminator exactly, points at §2.5.3. |
| Appendix A "does not unlock as normal" / "cannot unlock" / "choose not to unlock…" | Clean. Suppression-scope entries pointing at §5.2.2; the duration question correctly lives in the separate duration-clause entry. |

Status: ADJUDICATED 2026-07-22 (owner: apply) — F-unlock-1 applied to §1.6.3 (duration-clause
rationale + §2.5.3 pointer). See R-030.
