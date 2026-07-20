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
- [x] Phase 5: per-section extracts — DONE 2026-07-20. 64 files in docs/_work/extracts/.
      **RUNBOOK: docs/_work/phase5-runbook.md. GENERATOR: docs/_work/gen-extracts.py**
      (idempotent — `rm extracts/*.md && python3 gen-extracts.py` rebuilds from
      classification.tsv + taxonomy.md + review-findings.json + tensions.md + rulings-flat.tsv;
      it writes nothing else). Ran as a script, zero agent tokens.
      Validation clean: 64 files, all 2,373 P/E rulings routed and nothing extra, 0 malformed
      table rows, 64/64 carry reviewer notes, per-section P/E counts reconcile to coverage.tsv
      (which is also the check that the 3.10-vs-3.1 strnum trap did not bite — Python dict
      keys are strings, so it could not).
      ALL FOUR RIDE-ALONGS LANDED: 3.7.4 seam (clusters A/B/C/D with ids, from the structural
      Q1 finding); no-effect-plays rendered as the Q5 three-way split (a)/(b)/(c) in all 12
      sections it touches, with prevention-without-damage folded into (b); the RESOLVED
      mandatory-action principle at the TOP of 3.9, above the reviewer note that guessed it
      backwards; DO-NOT-DRAFT banners on 1.8 and 3.5.
      TWO FORMAT CHOICES beyond the runbook, both to give the drafter routing info it would
      otherwise have to go find: ruling tables are
      `| id | card id | card | codes | ruling text | classifier note |` — the `codes` column
      is how a drafter sees a ruling is filed here as a SECONDARY, and the classifier note
      carries the !TENSION/duplicate flags. Tension blocks show the whole slug with `★` on
      the rulings in this section, so a drafter always sees both poles.
      ONE RULING NOT PLACED: R1680 {Soul Burn}.5 is in the no-effect-plays slug but the Q5
      finding named only 45 of its 46. Left explicitly unplaced rather than re-decided at
      Phase 5; its own note says it matches {Blood Fury}.6, which is in bucket (b).
- [~] Phase 6: drafting. **CONTRACT: docs/_work/drafter-contract.md** (self-contained;
      compression mandate + style rules + output format + footnote scheme).
      DECIDED 2026-07-20 (Lionel): opus on all 64; TWO WAVES, deciders first; the 1.8/3.5
      pilots are REOPENED and drafted FRESH from their extracts (not revised in place) —
      the old prose stays in docs/extended-rules.md for Lionel to diff at Phase 7.
      - [x] Wave 1 DONE 2026-07-20 — 11 boundary-owning sections, 11/11, 0 failures,
        621k subagent tokens, ~13 min, 1,364 lines of prose in docs/_work/sections/.
        Sections: 1.1 1.5 1.6 1.8 1.15 3.4 3.5 3.7.4 5.5 5.6 5.9.
        Compression HELD: 2.0–5.6 rulings per footnote against a 4–6 target; **zero
        card-list violations in prose** across all 11; footnote labels uniformly
        section-prefixed; § cross-refs (no anchors); only 4 ⚠ REVIEW in 11 sections.
        The low ratios (5.5 at 2.0, 5.6 at 2.2) are legitimate — those sections are
        genuinely many independent rules, not one template stamped on N cards. Do not
        "fix" them.
        CONVERGENCE WORKED: 1.1, 1.6, 1.8, 3.4 and 5.5 independently landed on the same
        requirement-vs-futility seam because the ⚑ ride-along was in all their extracts.
        That is the evidence the wave design is sound.
      - [x] PHASE 5 DEFECT FOUND BY WAVE 1 AND FIXED: extracts carried cross-section
        material (tension-block rulings outside the membership; the 3.7.4 seam clusters
        routed to 1.5/5.5/5.6 by NAME while their codes deliberately stayed on 3.7.4)
        WITHOUT the ruling text, so the receiving drafter had no `[REF ID]` to footnote.
        gen-extracts.py now emits a **"Borrowed rulings — cited here, coded elsewhere"**
        table; 14 sections carry one. NO REDRAFT NEEDED: 1.5 self-repaired by going to
        rulings.yaml and citing group G00119 `Allies with "lock this ally to" abilities`
        [ANK 20180517], verified correct.
      - [x] Wave 1 REDRAFT DONE 2026-07-20 — the first wave-1 batch was REJECTED by Lionel
        on style (4x too long, abstract register) and 1.6 additionally on CONTENT. Archived
        at `sections-wave1-rejected/`, not deleted. Contract gained BREVITY AND PLAIN
        LANGUAGE, VERIFY CARD TEXT (mandatory krcg fetch per cited card) and the game-term
        warnings. Redraft: 11/11, 741k tokens. Prose 1150 -> 658 lines.
      - [x] Wave 2 DONE 2026-07-20 — 53/53, 0 failures, 4.0M subagent tokens, ~72 min.
        **ALL 64 SECTIONS NOW DRAFTED** in docs/_work/sections/. 3,817 prose lines +
        820 reference lines = 4,637 total. 1,345 card texts verified against krcg.
        Only 5 ⚠ REVIEW flags in 64 sections. Footnote markers/definitions balance in all 64.
      - **`owner-rulings.md` IS THE HIGHEST AUTHORITY IN THIS PROJECT.** Lionel's rules calls
        made while reading drafts, each verified against printed card text. It outranks
        `wave1-decisions.md`, the extracts, and the rulings' own paraphrases. Blocks A, A2,
        B, C. Read it before touching any section.
      - **`phase8-inbox.md`** — 9 objections + 34 card-text-vs-ruling conflicts the drafters
        RAISED instead of silently resolving. This is Phase 8's work queue, not noise.
      - LESSON, cost two rounds: mid-flight corrections to `owner-rulings.md` race the
        running agents. The "Only usable by ..." rule changed THREE times (gates use ->
        gates play -> type-dependent) and six wave-2 sections flagged the stale file rather
        than guessing — that behaviour is why nothing was corrupted. **Settle a rules call
        BEFORE launching a wave.**
      - KNOWN GAP vs Lionel's ask: he wanted ~4x shorter; wave 1 achieved 1.75x and wave 2
        averages 59 prose lines/section against a 25-50 budget. He accepted 1.6 (48 lines)
        as the density benchmark. Twelve sections exceed 70 lines and are the compression
        candidates: 1.13, 1.8, 2.4, 2.5, 3.3, 3.7.6, 4.3, 4.5, 5.2, 5.7, 6.2, 6.5.
      - DANGLING TERM for Phase 8: four sections (1.1, 1.8, 1.9, 4.2) cross-reference
        "futility" as though §1.6 defines it. §1.6 never uses the word.
      UPSTREAM DATA GAP (not ours, matters at Phase 9): **48 of the 1,369 distinct ruling
      refs cited in rulings.yaml have no entry in references.yaml** (3.5%, 57 citations;
      LSJ 23, ANK 15, PIB 6, TOM 2, KOT 1, RTR 1). Wave 1 legitimately cited 17 of them.
      Phase 9's "every ID resolves" check WILL flag these — they are an upstream hole in
      vtes-biased/vtes-rulings, not drafting errors. Do not let Phase 9 "fix" them by
      deleting the citations.
- [x] Phase 7: ASSEMBLED 2026-07-20. **SCRIPT: docs/_work/assemble.py** — idempotent,
      rebuilds the whole document from sections/*.md every run (`python3 docs/_work/assemble.py`).
      Reads only sections/; writes only docs/extended-rules.md. Re-run it after ANY edit to a
      section draft; do not hand-edit the assembled file and expect it to survive.
      **docs/extended-rules.md: 4,831 lines, 64 sections, 754 footnotes, 59 cross-references.**
      Validation built into the script and CLEAN: no duplicate footnote labels document-wide,
      no marker without a definition, no definition without a marker, every `§x.y`
      cross-reference resolves to a real heading, no duplicate section headings.
      STRUCTURE: 6 chapters. 3.7.1-3.7.8 are nested one level under a `### 3.7 The action
      types in detail` parent (their internal headings were demoted to match). Chapter 6
      skips 6.8 deliberately. New codes 1.15 / 3.9 / 3.10 / 5.9 / 6.9 now have real headings;
      the old 6.8 stub is gone.
      NOTE: the front matter was rewritten (status line, plus a `§` cross-reference
      convention added). The old hand-written stubs and their HTML comments are all gone.
- [ ] Phase 8: consistency/organization review pass (+ fixes). **NEXT — Lionel is running
      this from a FRESH HARNESS, so everything it needs is written down below.**
      READ FIRST, IN THIS ORDER:
      1. `docs/_work/owner-rulings.md` — **the highest authority in this project.** Lionel's
         rules calls, each verified against printed card text. Outranks the drafts, the
         extracts, `wave1-decisions.md`, and the rulings' own paraphrases.
      2. `docs/_work/phase8-inbox.md` — the work queue. 9 objections + 34 card-text-vs-ruling
         conflicts that drafters RAISED rather than silently resolving. 6 of the 9 objections
         are the already-resolved stale "Only usable by" entry, kept only as the record.
         The 3 live ones: 1.2 vs 1.15 on whether "(limited)" binds the action or the
         minion-per-round; 4.3 arguing {Rigor Mortis} is a counterexample to 1.1's
         cannot-names-cards vs cannot-names-outcome test; 1.11 wanting 1.8's "retrieve cards
         played" clause scoped to canceled cards only.
      3. `docs/_work/drafter-contract.md` — the style contract the document was written to.
         Judge consistency against THIS, not against taste.
      KNOWN DEFECTS ALREADY IDENTIFIED, do not re-discover them:
      * **Length.** Lionel asked for ~4x shorter than the first attempt; the finished draft
        averages 59 prose lines/section against a 25-50 budget. He accepted §1.6 (48 lines)
        as the density benchmark. The 12 sections over 70 lines are the compression
        candidates: 1.13, 1.8, 2.4, 2.5, 3.3, 3.7.6, 4.3, 4.5, 5.2, 5.7, 6.2, 6.5.
      * **Dangling term.** 1.1, 1.8, 1.9 and 4.2 cross-reference "futility" as though §1.6
        defines it. §1.6 never uses the word. Either define it or rewrite the four refs.
      * **Title style drift.** Some headings use "&", others "and" (4.5 "Prevention &
        immunity", 5.7 "...classes & traits", 6.9 "Hand, draw & discard" vs 6.1 "Owner and
        controller"). Also 4.7 "Strike: combat ends" should probably match the game term's
        capitalisation, "Strike: Combat Ends".
      * **Cross-references are plain `§x.y` markers by design** — Phase 8 converts them to
        markdown anchor links. 59 of them, all validated as resolving.
      WORKFLOW NOTE: assemble.py is the source of truth for the document. Fix section drafts
      in `sections/`, then re-run it. Editing `docs/extended-rules.md` directly loses the fix.
      LESSON FROM PHASE 6, worth honouring: a rules call changed three times mid-run and six
      agents flagged the stale file instead of guessing — that is why nothing was corrupted.
      Settle rules calls BEFORE launching a wave, and keep telling agents to raise conflicts
      rather than resolve them silently.
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
