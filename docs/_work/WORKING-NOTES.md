# Extended Rules — working notes (compaction insurance)

## Mandate (from Lionel, 2026-06-12)
1. Build coverage map: classify all ~2,605 rulings against the outline sections.
2. Assess coverage (% of rulings absorbed as Principle or Example). If < 75%,
   expand sections/topics until ≥ 75%.
   AMENDED 2026-07-20 (Lionel): **75% is a placeholder, not a calibrated target.**
   It exists to push the pipeline toward covering as much as possible; the true
   achievable level is unknown, and we don't want to overdo it either. Treat the
   number as DIAGNOSTIC. A healthy C fraction is correct by design — pure one-card
   interpretations stay in the rulings database (style rules). Chasing 75% by
   absorbing card trivia would violate the style constraints to satisfy the coverage
   constraint. If coverage lands low, investigate WHY before expanding: over-C'ing
   by tired classifiers looks identical to missing sections, and the prescribed fix
   (add sections) makes the document worse if the cause was classifier laziness.
   Expand only on evidence — a cluster of related C notes naming the same absent
   topic. Hence the C-note requirement in classifier-contract.md.
3. Write the whole document (all stub sections) without further help.
4. Then: consistency & organization review pass on the full document.
5. Then: check references for oddities/suspicious parts.

## Key constraints & style (validated by Lionel)
- Mechanics-first structure, 6 chapters; judge-level terse prose.
- NO exhaustive card lists — tie rules to wording templates, "e.g." + 1-3 cards.
- Be synthetic; cross-reference instead of repeating; merge redundant subsections.
- Footnotes per section: ruling IDs + card/group where recorded in rulings.yaml.
  Footnote labels unique doc-wide (pilot used ^c1..c19, ^n1..n21; new sections use
  section-prefixed labels like [^4-4-1]).
- Rulebook actions are NOT subject to NRA (only card name/copy rules). Sameness
  matters only for card effects ({Obedience}, {Red Herring}, {Change of Target}).
- rulings.yaml wording may paraphrase the original ruling — verify against card text
  (https://api.krcg.org/card/<id-or-name>, key card_text) and original rulings
  (VEKN forum fetchable; LSJ Google Groups not practical).
- History of rules changes gist (when rules changed/reverted):
  https://gist.githubusercontent.com/lionel-panhaleux/a4a9cad2e492af7c45c50a1cea7e6cf6/raw/92a6f169931c08ea3a4ae62ccbf2d6da17bc8970/VTES%2520History%2520of%2520changes.md
- Pilot sections 1.8 and 3.5 in docs/extended-rules.md are DRAFTED AND REVIEWED —
  use as style exemplars, do not rewrite (light edits only if review pass demands).
- Base rulebook: rulebook2024/content.md (now a git submodule, was a sibling checkout).
  Rulings DB likewise: vtes-rulings/rulings/*.yaml.
- Use .venv/bin/python for yaml scripts.

## Model split (agreed 2026-07-20)
- Opus on judgment: calibration (2.5), section review (4.5), the Phase 4 expand-or-not call.
- Sonnet on volume: the 18-way classification pass.
- Rationale: anchoring consistency up front beats detecting drift afterward, and
  calibration also de-risks the taxonomy before ~500k tokens are spent against it.

## Agent design principles (from the codex strategist, adapted)
- Agents are SELF-CONTAINED: contract + taxonomy + calibration + own chunk. No agent
  goes reading the vtes skill or the rulebook on its own — N agents choosing what to
  read is N chances to drift.
- Calibration corpus is MAINTAINED, not appended: promote generalizable corrections
  into "General lessons", keep case verdicts thin. The file must not grow unbounded.
- Reviews emit typed, ranked findings with evidence; "no finding" is a valid result.
  A reviewer obliged to produce findings will manufacture them.
- Worth stealing later: codex-of-the-damned/.claude/references/strategist/
  card-changes-history.md — a maintained local copy of the History of changes gist
  (424 dated entries, through 2026-05). Useful at Phase 9: a principle resting on a
  ruling that errata later reversed is invisible at the footnote level.

## Pipeline state (update as phases complete)
- [x] Phase 0: infra (venv+pyyaml, docs/_work/)
- [x] Phase 1: flatten rulings → docs/_work/rulings-flat.tsv (2,605 rulings)
- [x] Phase 2: taxonomy file → docs/_work/taxonomy.md (61 codes; 6.9 added at 2.5)
- [x] Phase 2.5: CALIBRATION — DONE 2026-07-20, two rounds, four opus passes.
      Method: TWO independent passes per round over the same 111-ruling sample
      (calib-sample.tsv), graded against each other (compare-runs.py). Agreement
      between two agents given identical instructions estimates the drift expected
      across the 18-way fan-out, and needs no owner grading of 111 items.
      Artifacts: calib-run-{A,B}.tsv (r1), calib-run-{A2,B2}.tsv (r2).
      Outcome: contract restructured twice, 6.9 added, tension mechanism added,
      two instruction defects caught that would have split the production run.
      Round 2 agreement: 93.7% extract-membership floor, 94.6% absorbed/not,
      84.7% identical code set. Full verdicts: calibration.md → Grading history.
      KNOWN OPEN: the corpus's true C rate is still unmeasured — both rounds ran
      against instruments that leaned against C. The round-3 fix (two independent
      judgments, absorption decided first) is IN PLACE BUT UNTESTED. Decision taken:
      proceed to production rather than spend a third round on a diagnostic-only
      number whose error runs in the cheap direction; Phase 4.5 section review sees
      over-absorption directly. If Phase 4 coverage again reads ~90% with a ~5% C
      rate, that is the untested fix having failed — treat it as a finding, not a
      surprise, and do NOT expand the taxonomy in response (see gate note above).
- [x] Phase 3: PRODUCTION CLASSIFICATION — DONE 2026-07-20. 18 chunks → class/chunk-NN.tsv
      **RUNBOOK: docs/_work/phase3-runbook.md — read it, it is self-sufficient.**
      Sonnet ×18, self-contained, one workflow, 0 failures, ~1.95M subagent tokens.
      Result: P 1020 / E 1272 / C 222 / G 91 over 2,605. Coverage (P+E) 88.0%, C 8.5%.
      Validation clean: line counts, id set, roles, codes, C/G notes all pass.
      TWO ARTIFACTS FOR PHASE 4/4.5 TO KNOW ABOUT:
      1. Trailing-tab variance — 1,938 P/E rows have an empty note written as 3 fields
         instead of 4 (only chunk-10 and chunk-17 emitted the trailing tab). Every C and
         G row has 4 fields. Harmless for field-indexed parsing; do not hand-patch.
      2. C-row nearest-code inconsistency — 119 of 222 C rows (54%) carry a bare `-` in
         the codes column even when their note names a nearest section; 8 chunks did it
         to 100% of their C rows, 6 chunks to none. Contract says carry the nearest code.
         Do NOT recover these from the codes column — recover from the C notes instead.
      C rate 8.5% with 88.0% coverage: NOT the ~5%/~90% failure signature the watch list
      named, so the round-3 two-judgments fix reads as partially effective. Still not a
      licence to expand the taxonomy on coverage grounds — G is the only such evidence.
- [x] Phase 4: aggregate + expand-or-not. DECIDED 2026-07-20 (Lionel).
      DONE: coverage.tsv (per-section P/E/G membership), tensions.md (4 slugs, 53 rows).
      DECISION: expand by FOUR codes — 1.15 cumulative/stacking (28 G), 5.9 traits &
      trait-change precedence (25 sect G + 3 generic precedence), 3.9 mandatory actions
      (7, absorbs the failed minion-phase-ordering watch item), 3.10 changing the acting
      minion (4). Plus FIVE scope-line widenings (1.5, 1.7, 1.9, 1.12, 6.9) for real
      principles too thin to be sections. Rationale + rejected candidates recorded in
      taxonomy.md — read that, not this summary.
      KEY RESHAPE: the agents converged on "sect as a trait", but sect is the most-ruled
      INSTANCE of a general trait-precedence rule ({Derange}.7 clan, {Deep Song}.2 acting
      minion). 5.9 is scoped to traits generally so a drafter does not state a sect-only
      rule that is actually general.
      REJECTED: question-cards (all 5 = {Monocle of Clarity}) and auctions (both =
      {Extremis Boon}) — single-card topics mislabelled G. 9 of 91 G rows are single-card:
      agents used G to mean "homeless" when it means "general AND homeless".
      REMAINING: reclassify the ~275 affected rulings against the expanded taxonomy.
- [x] Phase 4b: RECLASSIFICATION — DONE 2026-07-20. Sonnet ×2 over 275 affected rulings
      (confirm-or-change). 101 changed, 174 kept. Change concentrated exactly where it
      should be: 90% of orig-G rows moved, only 2% of orig-P. No over-migration (3.1 lost
      2 members to 3.10, not dozens). Transitions: G→P 53, G→E 21, G→C 7 (the rejected
      single-card topics), C→E 2, E→P 1.
      **OUTPUT: docs/_work/classification.tsv — 2,605 rows, THE canonical labels.**
      Phases 5+ read this file, NOT class/chunk-*.tsv. The chunk files are the immutable
      per-agent record and are now superseded for the 275 rechecked rows. classification.tsv
      is normalized to 4 fields throughout (fixes the Phase 3 trailing-tab variance).
      FINAL: P 1074 / E 1294 / C 227 / G 10. Coverage 90.9%, C 8.7%, G down from 91 to 10.
      New-code membership: 1.15=32, 5.9=28, 3.10=14, 3.9=11.
      AWK GOTCHA that cost a false reading: `-v C="3.10"` makes a strnum, so `a[i]==C`
      matches "3.1" numerically. Use array subscripts (always string keys) or force string
      context when counting codes. Bit me once; will bite again at Phase 5.
- [x] Phase 4.5: SECTION REVIEW — RUN 2026-07-20. 68 opus units (64 sections, 3 C-pile
      shards, 1 structural), 0 failures, ~2.58M tokens. 525 findings.
      **OUTPUT: review-findings.md (readable) + review-findings.json (machine).**
      *** CALIBRATION CAVEAT — READ BEFORE USING THESE FINDINGS ***
      68/68 units returned the middle verdict `coherent-with-issues`. ZERO returned
      `coherent`, zero returned `incoherent`, and ZERO returned an empty finding list
      despite the prompt saying in capitals that no finding is a valid result. Minimum
      findings per unit = 3, mean 7.7. That is a floor effect: reviewers produced to a
      quota. CONSEQUENCE: **do not triage by severity** — supported and unsupported
      findings have near-identical severity mixes (high: 45 vs 46 on the checkable type),
      so the labels carry no signal. Volume is inflated; content is mostly sound.
      VERIFICATION ACTUALLY DONE (not assumed): the 238 duplicate-template findings are
      lexically checkable. Pairwise, 135 clusters have >=50% of pairs either near-identical
      or sharing a ruling reference; 56 partial; 47 with no lexical evidence — but spot
      reading shows those 47 are semantically valid (same principle, different words), so
      they are unrefuted, not refuted. The findings are real; the quota is the problem.
      HEADLINE: **1,553 of 2,605 rulings (60%) are named as template duplicates.** This is
      the corpus's true shape and the single most important input to drafting. Also
      proposed: 176 demotions to C, 46 recoveries from C, 153 section moves.
      NOT YET DECIDED: whether to apply the 176/46/153. See Phase 4.6.
      Q3 was skipped by the structural unit (6 findings covering Q1, Q2, Q4, Q5 — two of
      them duplicates — and nothing on 3.9/3.10). ANSWERED SEPARATELY 2026-07-20 by reading
      both memberships directly:
      * **3.10 KEEPS its code, comfortably.** 14 rulings across TEN distinct cards, five
        sub-topics: what carries over (R1116), eligibility (R0706/R1257/R1599), precedence
        between two actor-changing effects (R0467/R1215/R1214), the NRA interaction
        (R1102/R2063), and a clean negative contrast in {Malleable Visage}, which does NOT
        change the acting minion. Judged by content, not count.
      * **3.9 KEEPS its code, but is genuinely marginal and its survival is CONDITIONAL on
        the 1.1 misfiling being applied.** As filed: 11 rulings, 7 cards, but R0424/R2524
        literally share [LSJ 20090226] and R1065/R1703 are the same sentence — ~7 distinct
        rulings after dedup. The 1.1 reviewer found R1066, R2393, R2394 are mandatory-ACTION
        discharge rulings sitting in 1.1, which owns mandatory EFFECTS. Move them and 3.9 is
        ~10 distinct rulings over four sub-topics. **Treat that move as part of the Q3
        decision, not as a separate finding to triage later.**
      RULES QUESTION INSIDE 3.9 — ADJUDICATED by Lionel, recorded in tensions.md under
      "RESOLVED — mandatory-action-satisfaction". R1704 vs R2525 look contradictory; they
      are not. The discriminator is whether the MANDATING effect provides the action
      ({Elen Kamjian} — only that action discharges it) or merely requires one of that type
      ({Spirit Marionette} — any such action discharges it, including one made by playing a
      card). The satisfying card is irrelevant. Predicts R1926 {Undying Thirst}. Not marked
      ⚠ REVIEW — this is settled.
- [x] Phase 4.6: ADJUDICATED & APPLIED 2026-07-20 (Lionel approved after reading
      review-findings.md). NINE rows changed in classification.tsv; backup at
      classification.tsv.bak. Live codes now 64 (6.8 retired).
      * **Q1 3.7.4 — scope-line split, NO reclassification.** Phase 4.5 found three topics,
        not two, and the unnamed third was the largest: a card effect putting an ally or
        retainer into play is NOT an employ/recruit action, so action-keyed effects
        (cost reductions, stealth modifiers, cancel-a-played-card, the NRA) do not attach.
        3.7.4's scope line never named it — that is why 44 rulings piled in. It says so now.
        "Acting the turn recruited" moved OUT to 1.5 (ability use is not an action) and
        5.5/5.6 (whether an entering minion may act). **The 44 keep their codes on purpose**
        — the reviewer's own instruction was "tell the drafter the seam, do not migrate".
        Phase 5 MUST pass the seam into the 3.7.4 extract or this is lost.
      * **Q2 6.8 — DELETED.** Its one ruling R2544 carried it only as a secondary code;
        now 1.6 alone. Not folded into 6.6 (nothing about the master phase).
        **6.9 deliberately NOT renumbered** — would invalidate every 6.9 reference in
        classification.tsv, coverage.tsv and review-findings.* for no gain. Chapter 6 skips 8.
      * **Q3 — both new codes keep their place.** 3.10 comfortable (14 rulings, 10 cards,
        5 sub-topics). 3.9 was marginal at 11 and its survival was CONDITIONAL on the 1.1
        misfiling; that move is applied (R1066, R2393, R2394), so 3.9 is now 14. 1.1 owns
        mandatory EFFECTS, 3.9 owns mandatory ACTIONS.
      * **Q4 — five stale pre-expansion G labels re-coded.** R1733/R1734/R1985 -> 5.9/E
        (which was starved of examples at 24 P to 4 E), R2017 -> 3.7.4/E, R2483 -> 1.6/E.
        R2483 struck from the watch list so it is not proposed a third time.
      * **Q5 — not applied, it is a drafting instruction:** split the no-effect-plays slug
        into three before drafting. Recorded in tensions.md.
      FINAL: P 1074 / E 1299 / C 227 / G 5. Coverage 91.1%.
      NOT APPLIED, BY DECISION: the 525 per-section findings (176 C-demotions, 153 section
      moves, 46 C-recoveries). They carry into Phase 5 as drafter instructions. Re-read the
      Phase 4.5 calibration caveat before anyone decides to bulk-apply them later.
      WHY 4.5 EXISTED, kept because it is the standing rationale for any future review:
      cross-chunk drift and per-section completeness are visible ONLY on the section axis
      (one boilerplate wording recurs on 10 cards across 7 chunks, so no chunk reviewer can
      see it), and it is the only safety net for over-absorption, which no classifier can
      see from inside its own 145 lines. The design was right; the calibration was not.
      If this pass is ever re-run, force the reviewer to earn its findings — the "no finding
      is a valid result" instruction was present, in capitals, and was ignored by 68 of 68.
- [ ] Phase 5: per-section extracts → docs/_work/extracts/<sec>.md
      **RUNBOOK: docs/_work/phase5-runbook.md — read it, it is self-sufficient.**
      MECHANICAL (a script, not a fan-out) — every input already exists, the judgment was
      spent at 4.5/4.6. 64 extracts. Four things must ride along or they are lost: the
      3.7.4 seam (its 45 rulings were deliberately NOT reclassified), the three-way split
      of no-effect-plays, the resolved mandatory-action principle, and DO-NOT-DRAFT marks
      on the 1.8/3.5 pilots.
- [ ] Phase 6: drafting workflow (one agent per section → docs/_work/sections/<sec>.md)
- [ ] Phase 7: assemble into docs/extended-rules.md
- [ ] Phase 8: consistency/organization review pass (+ fixes)
- [ ] Phase 9: reference verification pass (script: all IDs exist in references.yaml;
      agents: spot-check footnotes vs rulings.yaml, flag suspicious claims)
- [ ] Phase 10: cleanup — delete docs/_work/ (tsv, chunks, flattening script, extracts,
      sections, this file). All of it is in-flight tooling; tracked in git only so
      mid-pipeline state survives iterations. Only docs/extended-rules.md ships.

## Section codes — 65 codes (taxonomy.md is AUTHORITATIVE, this is a convenience index)
v1 had 61. 6.9 added 2026-07-20 on calibration evidence; 1.15 / 3.9 / 3.10 / 5.9 added
2026-07-20 on Phase 3 G-pile evidence (rationale in taxonomy.md, do not re-litigate here).
1.1 card-text-vs-rules; 1.2 wording-templates; 1.3 card-types-multitype;
1.4 placeholders; 1.5 abilities-vs-cards; 1.6 requirements; 1.7 costs-payment;
1.8 playing-canceling (DONE); 1.9 replacement; 1.10 burn-rfg-shuffle; 1.11 ash-heap;
1.12 cards-on-cards; 1.13 contests; 1.14 set-aside; **1.15 cumulative-stacking (NEW)**
2.1 windows-overview; 2.2 as-announced; 2.3 after-resolution;
2.4 simultaneous-ordering; 2.5 duration-persistence
3.1 announcement-targets; 3.2 stealth-intercept; 3.3 blocking;
3.4 resolution-success; 3.5 nra-cancel (DONE); 3.6 continue-unblocked;
3.7.1 bleed; 3.7.2 hunt; 3.7.3 equip-actions; 3.7.4 employ-recruit (OVERLOADED, 44);
3.7.5 referendum-procedure; 3.7.6 votes-ballots; 3.7.7 torpor-actions;
3.7.8 diablerie-bloodhunt; 3.8 card-title-actions;
**3.9 mandatory-actions (NEW)**; **3.10 changing-acting-minion (NEW)**
4.1 combat-sequence; 4.2 range; 4.3 strikes; 4.4 damage; 4.5 prevention-immunity;
4.6 dodge; 4.7 sce; 4.8 presses; 4.9 combat-end; 4.10 weapons-combat
5.1 vampires; 5.2 lock-unlock; 5.3 torpor-state; 5.4 burning-minions; 5.5 allies;
5.6 retainers; 5.7 special-classes; 5.8 titles;
**5.9 traits-and-trait-change-precedence (NEW)**
6.1 owner-controller; 6.2 control-minions; 6.3 control-cards; 6.4 leave-reenter;
6.5 pool-edge-oust; 6.6 master-phase; 6.7 influence-crypt;
6.8 events-gehenna (1 RULING IN THE WHOLE CORPUS — may not survive as a heading);
6.9 hand-draw-discard

NOTE on 3.10: `awk -v C="3.10"` makes a strnum that compares equal to "3.1". Match codes
via array subscripts (always string keys) or force string context. This produced a false
count once already.
