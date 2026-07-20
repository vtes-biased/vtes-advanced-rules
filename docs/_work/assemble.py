#!/usr/bin/env python3
"""Phase 7 — assemble docs/_work/sections/*.md into docs/extended-rules.md.

Idempotent: rebuilds the whole document from the section drafts every run.
Reads only sections/*.md; writes only docs/extended-rules.md.
"""
import glob
import os
import re
import sys
from collections import Counter

REPO = "/Users/lpanhaleux/Developer/vtes-advanced-rules"
SEC = os.path.join(REPO, "docs/_work/sections")
OUT = os.path.join(REPO, "docs/extended-rules.md")

CHAPTERS = [
    ("1", "Cards"),
    ("2", "Timing and Sequencing"),
    ("3", "Actions and Politics"),
    ("4", "Combat"),
    ("5", "Minions and Their States"),
    ("6", "Methuselahs and the Game"),
]

# 3.7.x are nested under a parent heading, per the agreed skeleton.
PARENT_37 = ("3.7", "The action types in detail",
             "The rulebook actions, one subsection each. Rules that are not specific to an "
             "action type live in §3.1-§3.6 and §3.8-§3.10.")

FRONT = """# VTES Extended Rules

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
- Statements derived from rulings carry footnote markers. Footnotes list the ruling
  reference IDs (e.g. `[LSJ 20090411]`), which resolve to URLs via
  [references.yaml](../rulings/references.yaml), and name the card or group under which
  the ruling is recorded in [rulings.yaml](../rulings/rulings.yaml).
- Card-specific rulings are quoted as examples where they illustrate a general
  principle. Pure one-card text interpretations remain in the rulings database.

---
"""

APPENDICES = """
---

## Appendix A. Glossary of wording templates

<!-- TODO Phase 8: collect the wording templates named across the document. -->

## Appendix B. Index of cited cards

<!-- TODO Phase 8: generate from the {Card} references in the assembled text. -->
"""


def key(code):
    return tuple(int(x) for x in code.split("."))


def demote(body, levels=1):
    """Push every ATX heading down N levels (### -> ####)."""
    return re.sub(r"^(#{3,6}) ", lambda m: "#" * (len(m.group(1)) + levels) + " ",
                  body, flags=re.M)


codes = sorted((os.path.basename(p)[:-3] for p in glob.glob(f"{SEC}/*.md")), key=key)
if len(codes) != 64:
    sys.exit(f"expected 64 sections, found {len(codes)}")

bodies = {c: open(f"{SEC}/{c}.md").read().strip() for c in codes}

parts = [FRONT]
for ch, title in CHAPTERS:
    parts.append(f"\n## {ch}. {title}\n")
    mine = [c for c in codes if c.split(".")[0] == ch]
    emitted_37 = False
    for c in mine:
        if c.startswith("3.7."):
            if not emitted_37:
                parts.append(f"\n### {PARENT_37[0]} {PARENT_37[1]}\n\n{PARENT_37[2]}\n")
                emitted_37 = True
            parts.append("\n" + demote(bodies[c]) + "\n")
        else:
            parts.append("\n" + bodies[c] + "\n")
    parts.append("\n---\n")

doc = "".join(parts).rstrip() + "\n" + APPENDICES
doc = re.sub(r"\n{4,}", "\n\n\n", doc)
open(OUT, "w").write(doc)

# ----------------------------------------------------------------- validation
text = open(OUT).read()
errs = []

labels = re.findall(r"^\[\^([^\]]+)\]:", text, re.M)
dupes = [l for l, n in Counter(labels).items() if n > 1]
if dupes:
    errs.append(f"duplicate footnote labels: {dupes[:10]}")

markers = set(re.findall(r"\[\^([^\]]+)\](?!:)", text))
undef = sorted(markers - set(labels))
unused = sorted(set(labels) - markers)
if undef:
    errs.append(f"footnote markers with no definition: {undef[:10]}")
if unused:
    errs.append(f"footnote definitions never referenced: {unused[:10]}")

# A cross-reference may point at a section OR at any subsection heading the drafts
# created (e.g. §4.5.2), so validate against every numbered heading in the document.
targets = set(codes) | set(re.findall(r"^#{2,6} (\d+(?:\.\d+)*)", text, re.M))
xrefs = set(re.findall(r"§(\d+(?:\.\d+)*)", text))
bad = sorted((x for x in xrefs if x not in targets), key=key)
if bad:
    errs.append(f"cross-references with no matching heading: {bad}")

heads = re.findall(r"^#{2,5} (\S+)", text, re.M)
hd = [h for h, n in Counter(heads).items() if n > 1 and re.match(r"^\d", h)]
if hd:
    errs.append(f"duplicate section headings: {hd}")

print(f"assembled {len(codes)} sections -> {OUT}")
print(f"  lines: {len(text.splitlines())}   footnotes: {len(labels)}"
      f"   cross-refs: {len(xrefs)}")
print(f"  chapter 6 skips 6.8 (deliberate): {'6.8' not in codes}")
if errs:
    print("\nVALIDATION ERRORS:")
    for e in errs:
        print("  -", e)
    sys.exit(1)
print("\nvalidation clean.")
