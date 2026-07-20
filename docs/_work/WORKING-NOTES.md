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
- [ ] Phase 3: PRODUCTION CLASSIFICATION — 18 chunks → docs/_work/class/chunk-NN.tsv
      **RUNBOOK: docs/_work/phase3-runbook.md — read it, it is self-sufficient.**
      Sonnet ×18, self-contained. class/ exists and is empty.
- [ ] Phase 4: aggregate → docs/_work/coverage.tsv + stats. Coverage is DIAGNOSTIC,
      not a target (see gate note below). Report P+E / C / G separately: the G pile
      is the ONLY evidence that justifies adding sections. Low coverage with near-zero
      G = the corpus's true ceiling, do nothing. Low coverage with a clustered G pile
      = real missing sections, expand there and reclassify only the affected rulings.
- [ ] Phase 4.5: SECTION REVIEW (opus), per section, not per chunk. Reviews each
      section's membership + the C pile for recoverable rulings. Cross-chunk drift
      and per-section completeness are only visible on this axis: one boilerplate
      wording recurs on 10 cards across 7 chunks, so no chunk reviewer can see it.
      Typed findings, ranked, no padding — no finding is a valid result.
- [ ] Phase 5: per-section extracts → docs/_work/extracts/<sec>.md
- [ ] Phase 6: drafting workflow (one agent per section → docs/_work/sections/<sec>.md)
- [ ] Phase 7: assemble into docs/extended-rules.md
- [ ] Phase 8: consistency/organization review pass (+ fixes)
- [ ] Phase 9: reference verification pass (script: all IDs exist in references.yaml;
      agents: spot-check footnotes vs rulings.yaml, flag suspicious claims)
- [ ] Phase 10: cleanup — delete docs/_work/ (tsv, chunks, flattening script, extracts,
      sections, this file). All of it is in-flight tooling; tracked in git only so
      mid-pipeline state survives iterations. Only docs/extended-rules.md ships.

## Section codes (taxonomy v1) — 61 codes
(6.9 hand-draw-discard added 2026-07-20 on calibration evidence; list below is v1 and
does not include it — taxonomy.md is authoritative.)
1.1 card-text-vs-rules; 1.2 wording-templates; 1.3 card-types-multitype;
1.4 placeholders; 1.5 abilities-vs-cards; 1.6 requirements; 1.7 costs-payment;
1.8 playing-canceling (DONE); 1.9 replacement; 1.10 burn-rfg-shuffle; 1.11 ash-heap;
1.12 cards-on-cards; 1.13 contests; 1.14 set-aside
2.1 windows-overview; 2.2 as-announced; 2.3 after-resolution;
2.4 simultaneous-ordering; 2.5 duration-persistence
3.1 announcement-targets; 3.2 stealth-intercept; 3.3 blocking;
3.4 resolution-success; 3.5 nra-cancel (DONE); 3.6 continue-unblocked;
3.7.1 bleed; 3.7.2 hunt; 3.7.3 equip-actions; 3.7.4 employ-recruit;
3.7.5 referendum-procedure; 3.7.6 votes-ballots; 3.7.7 torpor-actions;
3.7.8 diablerie-bloodhunt; 3.8 card-title-actions
4.1 combat-sequence; 4.2 range; 4.3 strikes; 4.4 damage; 4.5 prevention-immunity;
4.6 dodge; 4.7 sce; 4.8 presses; 4.9 combat-end; 4.10 weapons-combat
5.1 vampires; 5.2 lock-unlock; 5.3 torpor-state; 5.4 burning-minions; 5.5 allies;
5.6 retainers; 5.7 special-classes; 5.8 titles
6.1 owner-controller; 6.2 control-minions; 6.3 control-cards; 6.4 leave-reenter;
6.5 pool-edge-oust; 6.6 master-phase; 6.7 influence-crypt; 6.8 events-gehenna
