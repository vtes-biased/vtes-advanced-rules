#!/usr/bin/env python3
"""Phase 5 — build the 64 per-section drafting briefs in docs/_work/extracts/.

Mechanical. Reads classification.tsv, rulings-flat.tsv, taxonomy.md,
review-findings.json, tensions.md. Writes only extracts/*.md.
"""
import json
import os
import re
from collections import defaultdict

W = "/Users/lpanhaleux/Developer/vtes-advanced-rules/docs/_work"
OUT = os.path.join(W, "extracts")

# ---------------------------------------------------------------- taxonomy
# scope lines look like "- 1.1 — text ...", continuations are indented 2 spaces.
scopes = {}
order = []
cur = None
with open(os.path.join(W, "taxonomy.md")) as fh:
    for line in fh:
        m = re.match(r"^- (\d+(?:\.\d+)+) — (.*)$", line.rstrip("\n"))
        if m:
            cur = m.group(1)
            scopes[cur] = m.group(2).strip()
            order.append(cur)
        elif cur and line.startswith("  ") and line.strip():
            scopes[cur] += " " + line.strip()
        elif not line.strip():
            cur = None

# 6.8 is retired (Phase 4.6). 6.9 deliberately not renumbered.
DELETED = {"6.8"}
codes = [c for c in order if c not in DELETED]
assert len(codes) == 64, f"expected 64 live codes, parsed {len(codes)}: {codes}"

# ------------------------------------------------------------- rulings text
rulings = {}
with open(os.path.join(W, "rulings-flat.tsv")) as fh:
    for line in fh:
        rid, card, text = line.rstrip("\n").split("\t")
        cid, _, cname = card.partition("|")
        rulings[rid] = (cid, cname, text)

# ------------------------------------------------------------ classification
cls = {}
members = defaultdict(list)  # code -> [rid] in P then E order, id-sorted
with open(os.path.join(W, "classification.tsv")) as fh:
    for line in fh:
        rid, codestr, role, note = line.rstrip("\n").split("\t")
        clist = [c.strip() for c in codestr.split(",") if c.strip() and c.strip() != "-"]
        cls[rid] = (clist, role, note)
        if role in ("P", "E"):
            for c in clist:
                members[c].append(rid)

# ------------------------------------------------------------------ findings
findings = defaultdict(list)
for f in json.load(open(os.path.join(W, "review-findings.json"))):
    findings[f["unit"]].append(f)

# ------------------------------------------------------------------ tensions
# parse "## <slug> — N rulings" blocks; capture ids and the per-ruling note.
tensions = {}  # slug -> [(rid, note)]
slug = None
with open(os.path.join(W, "tensions.md")) as fh:
    for line in fh:
        m = re.match(r"^## ([a-z-]+) — (\d+) rulings", line)
        if m:
            slug = m.group(1)
            tensions[slug] = []
            continue
        if line.startswith("## "):
            slug = None
            continue
        if slug:
            mid = re.match(r"^- `(R\d{4})`", line)
            if mid:
                tensions[slug].append([mid.group(1), ""])
            elif tensions[slug] and line.strip().startswith("- !TENSION:"):
                tensions[slug][-1][1] = re.sub(
                    r"^(?:- !TENSION:[a-z-]+|—)\s*", "",
                    re.sub(r"^- !TENSION:[a-z-]+\s*", "", line.strip()),
                )

# notes are looked up across all slugs: the Q5 split pulls the two
# prevention-without-damage rulings into no-effect-plays bucket (b).
tnote = {rid: note for entries in tensions.values() for rid, note in entries}


def tline(rid, memset, note=None):
    star = "★ " if rid in memset else ""
    note = tnote.get(rid, "") if note is None else note
    tail = f" — {note}" if note else ""
    return f"- {star}`{rid}` **{rulings[rid][1]}**{tail}"

# --------------------------------------------------------- ride-along blocks
# (1) The 3.7.4 seam. Cluster membership from the structural Q1 finding.
SEAM_374 = """
## ⚑ RIDE-ALONG — the 3.7.4 seam (Phase 4.6, Q1). READ THIS FIRST.

Phase 4.6 split this section's **scope line** into three topics but **deliberately did NOT
reclassify its 45 rulings** — the reviewer's own instruction was "tell the drafter the seam,
do not migrate". So the membership table below is still one undifferentiated pile while the
taxonomy says three topics. Sort it yourself, using these clusters:

- **Cluster A — "may still USE abilities the turn recruited" → this is 1.5's principle,
  not 3.7.4's.** One `[ANK 20180517]` wording template; nine verbatim identical.
  R0247, R0535, R0566, R0766, R0773, R1501, R1521, R1777, R1944 (verbatim), plus variants
  R1922, R2001, R0285, R0014. Ability use is not an action; locking as an ability cost is
  not acting. Cross-ref 5.2 for the lock. **Do not write this pile as thirteen entries** —
  one principle, at most three "e.g." cards (a plain lock-to-use case, R1922 burn-life,
  R2001 lock-and-burn). R0014 and R0285 are not duplicates (werewolf burn, diablerie
  trigger) and are judged on their own.
- **Cluster B — "may a minion entering play ACT that turn" → 5.5 (allies) / 5.6 (retainers).**
  R0928, R1243, R1313, R1767, R1761, R0978.
- **Cluster C — 3.7.4's LARGEST and most general topic, and the one its scope line never
  used to name.** A card effect putting an ally or retainer into play is **not** an
  employ/recruit action, so action-keyed effects do not attach: cost reductions naming an
  action (R1314, R2521), stealth modifiers (R2017), cancel-a-played-card (R1317, R2520),
  the NRA (R1315, R1207, R1765), the action's own requirements/costs (R1766, R1761).
  Effects keyed to the recruiting minion **do** attach (R1688, R2151, R2300, R2522, R1044).
  That two-sided statement is this section's best material. Cross-ref 1.6 (requirements
  under abnormal entry) and 3.5 (already drafted — cross-reference the NRA, do not restate).
- **Cluster D — the employ/recruit action itself.** R0948, R1206, R1779, R1998, R2127,
  R2155, R2305, R2600, R0762.

**3.7.4 keeps C + D.** A and B are written elsewhere; carry a cross-reference, not the prose.
"""

# (2) no-effect-plays is three questions (Phase 4.5 Q5), with the
#     prevention-without-damage slug merged into (b).
NEP_SPLIT = {
    "a": (
        "PERMISSIVE DEFAULT — a card may be played, or an action taken, knowing it will "
        "accomplish nothing.",
        ["R0533", "R2087", "R1459", "R0269", "R0018", "R0936", "R0986", "R1637", "R1296",
         "R1368", "R1545", "R1612", "R1971", "R1805", "R1814", "R0465", "R0714"],
    ),
    "b": (
        "NAMED-OBJECT PROHIBITION — a card whose text names an object it acts on cannot be "
        "played when no such object exists. Includes the eight-copy prevention template, "
        "into which the standalone `prevention-without-damage` slug (R0065, R0082) merges: "
        "ten rulings, one template, ONE answer.",
        ["R0170", "R0195", "R0205", "R0224", "R0280", "R0730", "R1623", "R0458", "R1487",
         "R0737", "R1815", "R0251", "R0254", "R0233", "R0774", "R0833", "R0856", "R1634",
         "R1646", "R1647", "R1671", "R1736", "R0065", "R0082"],
    ),
    "c": (
        "SUCCESS WITHOUT EFFECT — whether a no-effect action still resolves successfully "
        "and still locks the actor. A different question entirely; it is 3.4's own scope "
        "line, not a tension.",
        ["R0228", "R0278", "R0735", "R1715", "R1023", "R1958"],
    ),
}
NEP_HEAD = """**⚑ RIDE-ALONG — this slug is THREE questions, not one (Phase 4.5 Q5).** Its size
is an artifact of merging them. Do not meet one polarity and state an over-broad rule.
(a) and (b) do not contradict: they are two sides of one rule whose deciding distinction is
**a requirement to play** versus **mere futility** — that boundary is **1.6's** to own, even
though 20 of the 46 were filed 1.1 first. Sections that must agree before any of this is
drafted: 1.6 (the deciding section), 3.4 (owns (c)), 1.1 (currently over-claiming this pile),
4.5, 4.6, 4.3, 3.2, 1.8. **1.8 is already drafted** and says nothing about no-effect plays;
it is the natural owner of the permissive default, so adopting (a) there is a light edit to
reviewed text — **the owner's call, not the drafter's.**
"""

# (3) The resolved mandatory-action principle (tensions.md, RESOLVED).
RESOLVED_39 = """
## ⚑ RIDE-ALONG — RESOLVED: mandatory-action satisfaction (tensions.md)

`R1704` {Spirit Marionette}.3 and `R2525` {Elen Kamjian}.2 look like a flat contradiction.
They are not. **Adjudicated 2026-07-20 by the owner** — this is settled, do **NOT** mark it
`⚠ REVIEW`:

> When an effect makes an action mandatory, whether another action of that type discharges
> the obligation depends on whether the mandating effect **provides** the action or merely
> **requires that one of that type be taken**.
> - PROVIDES ({Elen Kamjian}) — the obligation is to that specific provided action. Another
>   action of the same type, however obtained, does not discharge it.
> - REQUIRES A TYPE ({Spirit Marionette}) — any action of that type discharges it, including
>   one made by playing a card.

{Computer Hacking} vs {Flurry of Action} is **not** the variable — the first analysis to
reach this got it backwards. The satisfying card is irrelevant; the mandating card decides.
Predicts `R1926` {Undying Thirst}.1 (requires a type, provides nothing → any hunt discharges
it). State the principle; cite {Elen Kamjian} and {Spirit Marionette} as the contrasting pair.
"""

# The 3.7.4 seam routes two clusters to sections that hold none of their rulings.
# Phase 4.6 moved the TOPIC and deliberately left the CODES on 3.7.4, so membership
# cannot carry them. Ids from the structural Q1 finding.
CLUSTER_A = ["R0247", "R0535", "R0566", "R0766", "R0773", "R1501", "R1521", "R1777",
             "R1944", "R1922", "R2001", "R0285", "R0014"]
CLUSTER_B = ["R0928", "R1243", "R1313", "R1767", "R1761", "R0978"]
SEAM_ROUTE = {"1.5": CLUSTER_A, "5.5": CLUSTER_B, "5.6": CLUSTER_B}
SEAM_WHY = {
    "1.5": "3.7.4 seam cluster A — the ability-use principle is YOURS; "
           "the canonical record is group G00119 in rulings.yaml",
    "5.5": "3.7.4 seam cluster B — whether a minion entering play may ACT that turn",
    "5.6": "3.7.4 seam cluster B — whether a minion entering play may ACT that turn",
}

PILOTS = {
    "1.8": "1.8 Playing and canceling a card",
    "3.5": "3.5 Action repetition (NRA) and canceled actions",
}

CONSTRAINTS = """## Drafting constraints

- Judge-level terse prose, mechanics-first. Full fluency with the base rules is assumed;
  precision over accessibility.
- **NO exhaustive card lists.** Tie the rule to its wording template, then "e.g." + 1-3 cards.
- Be synthetic: cross-reference other sections rather than repeating; merge redundant points.
- Card names in braces `{Abbot}`; disciplines and card types in brackets `[pot]`, `[POT]`,
  `[ACTION]`.
- Every derived statement carries a footnote in a `#### References` block at the section end,
  listing the ruling reference IDs plus the card or group the ruling is recorded under, e.g.
  `[^x]: [LSJ 20061207] [RBK playing-a-card] — group "Cancel" (G00058).`
- Pure one-card text interpretations do **not** enter the document; they stay in the
  rulings database.
- `⚠ REVIEW` marks a point that still needs judge confirmation.
"""

CAVEAT = """> **CALIBRATION CAVEAT.** The Phase 4.5 pass produced to a quota: all 68 units returned the
> same middle verdict and none returned zero findings, despite the prompt saying in capitals
> that no finding is a valid result. Volume is inflated and **severity labels carry no signal
> — do not triage by them.** Content was spot-verified as largely sound. Treat these as leads
> to check, not instructions to obey. The `duplicate-template` findings are the most valuable
> thing here: they are the one defect class no classifier could see (one boilerplate wording
> recurs on ten cards across seven chunks), and they are what keeps this section from
> becoming a card list. **60% of the whole corpus is named as template duplication.**
"""


def row(rid):
    cid, cname, text = rulings[rid]
    clist, role, note = cls[rid]
    codestr = ",".join(clist)
    note = "" if note.strip() == "-" else note.strip()
    return f"| {rid} | {cid} | {cname} | {codestr} | {text} | {note} |"


os.makedirs(OUT, exist_ok=True)
stats = []

for code in codes:
    mem = sorted(set(members.get(code, [])))
    ps = [r for r in mem if cls[r][1] == "P"]
    es = [r for r in mem if cls[r][1] == "E"]
    L = []
    A = L.append

    A(f"# {code} — {scopes[code]}")
    A("")
    A(f"Membership: **{len(mem)} rulings** (P {len(ps)}, E {len(es)}). "
      f"Generated from `classification.tsv` (Phase 5, mechanical).")
    A(f"Footnote label prefix for this section: `[^{code.replace('.', '-')}-N]` "
      f"— labels must be unique document-wide.")
    A("")

    if code in PILOTS:
        A("> # ⟳ DRAFT FRESH — this supersedes the earlier DO-NOT-DRAFT mark")
        A(">")
        A(f"> Section **{PILOTS[code]}** already exists, drafted and reviewed, in")
        A("> `docs/extended-rules.md`. **The owner reopened it on 2026-07-20: draft it fresh")
        A("> from this extract, exactly like every other section.** Do not read the existing")
        A("> prose and do not try to preserve its wording — the point of drafting fresh is an")
        A("> independent pass over the full membership, which the original did not have.")
        A("> The old text is kept for the owner to diff against at Phase 7; that comparison")
        A("> is theirs to make, not yours.")
        A(">")
        A("> Two things the original is known to be missing, both from Phase 4.5:")
        if code == "1.8":
            A("> it says nothing about **no-effect plays**, and the Q5 finding names 1.8 as the")
            A("> natural owner of the PERMISSIVE DEFAULT — a card may be played knowing it will")
            A("> accomplish nothing. Draft that in, coordinating with 1.6 (which owns the")
            A("> requirement-to-play counterpole) and 3.4 (success without effect).")
        else:
            A("> check its coverage against this extract's full membership, and against the")
            A("> `no-effect-plays` split if a tension block appears below.")
        A(">")
        A("> Footnote labels: the original used `[^c1..c19]` (1.8) and `[^n1..n21]` (3.5).")
        A(f"> **Use the section-prefixed scheme instead** — `[^{code.replace('.', '-')}-N]` —")
        A("> so the document is uniform once every section is drafted.")
        A("")

    A(CONSTRAINTS)

    if code == "3.7.4":
        A(SEAM_374)
    if code == "3.9":
        A(RESOLVED_39)

    fs = findings.get(code, [])
    if fs:
        A("## Reviewer notes (Phase 4.5) — READ BEFORE DRAFTING")
        A("")
        A(CAVEAT)
        A("")
        for f in fs:
            A(f"### [{f['severity']}] {f['type']}")
            A("")
            A(f["summary"])
            A("")
            A(f"**Recommendation:** {f['recommendation']}")
            A("")
            A(f"*Rulings:* {', '.join(f['ruling_ids'])}")
            A("")
    else:
        A("## Reviewer notes (Phase 4.5)")
        A("")
        A("_No Phase 4.5 finding was filed against this section._")
        A("")

    memset = set(mem)
    blocks = []
    for slug, entries in tensions.items():
        hit = [e for e in entries if e[0] in memset]
        if hit:
            blocks.append((slug, entries, hit))
    ntens = len(blocks)
    if blocks:
        A("## Tensions touching this section")
        A("")
        A("Contradictory-polarity rulings. **A drafter who meets only one side states an")
        A("over-broad rule** — resolve each slug as a unit before drafting. `★` marks the")
        A("rulings that are in THIS section's membership; the others are shown so you see")
        A("both poles.")
        A("")
        for slug, entries, hit in blocks:
            A(f"### `{slug}` — {len(entries)} rulings, {len(hit)} in this section")
            A("")
            if slug == "no-effect-plays":
                A(NEP_HEAD)
                seen = set()
                for key in ("a", "b", "c"):
                    label, ids = NEP_SPLIT[key]
                    A(f"**({key}) {label}**")
                    A("")
                    for rid in ids:
                        seen.add(rid)
                        A(tline(rid, memset))
                    A("")
                left = [e for e in entries if e[0] not in seen]
                if left:
                    A(f"**Not placed by the Q5 split** — it named {len(entries) - len(left)}"
                      f" of the slug's {len(entries)}. Judge these on their own:")
                    A("")
                    for rid, note in left:
                        A(tline(rid, memset, note))
                    A("")
            else:
                if slug == "prevention-without-damage":
                    A("**⚑ This slug is the SAME adjudication as the named-object "
                      "prohibition (b) in `no-effect-plays`** — the eight-copy prevention "
                      "template (R0774, R0833, R0856, R1634, R1646, R1647, R1671, R1736). "
                      "Ten rulings, one template, one answer. Do not resolve it in isolation.")
                    A("")
                for rid, note in entries:
                    A(tline(rid, memset, note))
                A("")
    ntens_flag = ntens > 0

    # ---- BORROWED RULINGS -------------------------------------------------
    # A section can be told to own material whose rulings are coded elsewhere:
    # tension-block rulings outside its membership, and the 3.7.4 seam clusters
    # that Phase 4.6 routed by NAME while deliberately leaving their codes put.
    # Without the citable text those drafters cannot build a footnote. Wave 1
    # hit this on 1.5, 1.6, 5.5 and 5.6.
    borrow = {}
    for rid in SEAM_ROUTE.get(code, []):
        borrow[rid] = SEAM_WHY[code]
    for slug, entries, hit in blocks:
        for rid, _ in entries:
            if rid not in memset and rid not in borrow:
                borrow[rid] = f"shown in the `{slug}` tension block above but coded elsewhere"

    hdr = ("| id | card id | card | codes | ruling text | classifier note |\n"
           "|---|---|---|---|---|---|")

    if borrow:
        A("## Borrowed rulings — cited here, coded elsewhere")
        A("")
        A("These are **not** in this section's membership. They appear because a ride-along or")
        A("a tension block above makes them yours to state, while their codes stay where they")
        A("are. They are reproduced in full so you can **cite them** — you cannot build a")
        A("footnote from an id and a card name alone. Their owning section will also see them;")
        A("that is intended, and the ride-along tells you which of you writes the prose.")
        A("")
        A(hdr)
        for rid in sorted(borrow):
            A(row(rid) + f" _{borrow[rid]}_")
        A("")
    A("## Rulings — PRINCIPLE candidates (P)")
    A("")
    A("The section's PROSE comes from these. `codes` shows the ruling's full code list — a")
    A("ruling whose first code is not this section is filed here as a secondary. Reconstruct")
    A("the `rulings.yaml` key for footnotes as `<card id>|<card>` with the trailing `.n`")
    A("index dropped. `[REF ID]` tags in the text are what the footnotes cite.")
    A("")
    if ps:
        A(hdr)
        for rid in ps:
            A(row(rid))
    else:
        A("_None._")
    A("")
    A("## Rulings — EXAMPLE candidates (E)")
    A("")
    A('These are the "e.g." cards the prose cites — 1-3 per principle, never a list.')
    A("")
    if es:
        A(hdr)
        for rid in es:
            A(row(rid))
    else:
        A("_None._")
    A("")

    with open(os.path.join(OUT, f"{code}.md"), "w") as fh:
        fh.write("\n".join(L).rstrip() + "\n")

    stats.append((code, len(mem), len(ps), len(es), len(fs), ntens_flag))

# ------------------------------------------------------------------- report
print(f"wrote {len(stats)} extracts to {OUT}")
print(f"with reviewer notes: {sum(1 for s in stats if s[4])}")
print(f"with a tension block: {sum(1 for s in stats if s[5])}")
print("\nlargest:")
for s in sorted(stats, key=lambda x: -x[1])[:8]:
    print(f"  {s[0]:6} {s[1]:4} rulings (P {s[2]}, E {s[3]})  findings {s[4]}")
print("\nsmallest:")
for s in sorted(stats, key=lambda x: x[1])[:10]:
    print(f"  {s[0]:6} {s[1]:4} rulings (P {s[2]}, E {s[3]})  findings {s[4]}")
