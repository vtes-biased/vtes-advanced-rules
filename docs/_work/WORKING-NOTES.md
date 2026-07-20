# Extended Rules — working notes (compaction insurance)

## Mandate (from Lionel, 2026-06-12)
1. Build coverage map: classify all ~2,605 rulings against the outline sections.
2. Assess coverage (% of rulings absorbed as Principle or Example). If < 75%,
   expand sections/topics until ≥ 75%.
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
- Base rulebook: /Users/lpanhaleux/Developer/rulebook2024/content.md
- Use .venv/bin/python for yaml scripts.

## Pipeline state (update as phases complete)
- [x] Phase 0: infra (venv+pyyaml, docs/_work/)
- [ ] Phase 1: flatten rulings → docs/_work/rulings-flat.tsv (id, card, refs, text)
- [ ] Phase 2: taxonomy file → docs/_work/taxonomy.md (61 section codes)
- [ ] Phase 3: classification workflow (18 chunks → docs/_work/class/chunk-NN.tsv)
      Format per line: id<TAB>section|-<TAB>P|E|C<TAB>optional-topic-hint
- [ ] Phase 4: aggregate → docs/_work/coverage.tsv + stats; expand topics if <75%
- [ ] Phase 5: per-section extracts → docs/_work/extracts/<sec>.md
- [ ] Phase 6: drafting workflow (one agent per section → docs/_work/sections/<sec>.md)
- [ ] Phase 7: assemble into docs/extended-rules.md
- [ ] Phase 8: consistency/organization review pass (+ fixes)
- [ ] Phase 9: reference verification pass (script: all IDs exist in references.yaml;
      agents: spot-check footnotes vs rulings.yaml, flag suspicious claims)

## Section codes (taxonomy v1)
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
