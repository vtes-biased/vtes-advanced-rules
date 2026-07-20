#!/usr/bin/env python3
"""Compare two independent classification runs over the same rulings.

Agreement between two agents given identical inputs and instructions is a direct
estimate of the drift to expect across the 18-way Phase 3 fan-out. Disagreement is
the signal: a contested code is an ambiguous section boundary, and every ambiguous
boundary is a calibration lesson worth writing.

  usage: python3 compare-runs.py run-A.tsv run-B.tsv [sample.tsv]
"""
import sys
from collections import Counter, defaultdict


def load(path):
    rows = {}
    for n, line in enumerate(open(path), 1):
        line = line.rstrip("\n")
        if not line.strip():
            continue
        parts = line.split("\t")
        if len(parts) < 3:
            print(f"  !! {path}:{n} malformed ({len(parts)} fields): {line[:70]}")
            continue
        rid, codes, role = parts[0].strip(), parts[1].strip(), parts[2].strip()
        note = parts[3].strip() if len(parts) > 3 else ""
        rows[rid] = {
            "codes": [] if codes == "-" else [c.strip() for c in codes.split(",") if c.strip()],
            "role": role,
            "note": note,
        }
    return rows


def main():
    a_path, b_path = sys.argv[1], sys.argv[2]
    texts = {}
    if len(sys.argv) > 3:
        for line in open(sys.argv[3]):
            p = line.rstrip("\n").split("\t")
            if len(p) >= 3:
                texts[p[0]] = (p[1], p[2])

    A, B = load(a_path), load(b_path)
    ids = sorted(set(A) & set(B))
    print(f"run A: {len(A)} rows | run B: {len(B)} rows | comparable: {len(ids)}")
    for label, missing in (("A", set(B) - set(A)), ("B", set(A) - set(B))):
        if missing:
            print(f"  !! missing from {label}: {sorted(missing)}")

    exact = primary = overlap = role_same = 0
    absorbed_same = 0          # P/E vs C/G — the decision that drives coverage
    contested = Counter()
    cg_conflicts, primary_conflicts, absorbed_conflicts = [], [], []

    for rid in ids:
        a, b = A[rid], B[rid]
        sa, sb = set(a["codes"]), set(b["codes"])
        if sa == sb:
            exact += 1
        if a["codes"][:1] == b["codes"][:1]:
            primary += 1
        else:
            primary_conflicts.append(rid)
            for c in sa ^ sb:
                contested[c] += 1
        if sa & sb:
            overlap += 1
        if a["role"] == b["role"]:
            role_same += 1
        # coverage-critical: does this ruling enter the document at all?
        abs_a, abs_b = a["role"] in "PE", b["role"] in "PE"
        if abs_a == abs_b:
            absorbed_same += 1
        else:
            absorbed_conflicts.append(rid)
        if {a["role"], b["role"]} == {"C", "G"}:
            cg_conflicts.append(rid)

    n = len(ids) or 1
    pct = lambda x: f"{x:3d}/{n}  {100*x/n:5.1f}%"
    print("\n=== AGREEMENT ===")
    print(f"  identical code set    {pct(exact)}")
    print(f"  same primary code     {pct(primary)}")
    print(f"  any code in common    {pct(overlap)}   <- extract-membership floor")
    print(f"  same role             {pct(role_same)}")
    print(f"  same absorbed/not     {pct(absorbed_same)}   <- drives the coverage number")

    print("\n=== ROLE MIX ===")
    for label, R in (("A", A), ("B", B)):
        c = Counter(r["role"] for r in R.values())
        tot = sum(c.values()) or 1
        cov = 100 * (c["P"] + c["E"]) / tot
        multi = sum(1 for r in R.values() if len(r["codes"]) > 1)
        print(f"  {label}: P={c['P']:3d} E={c['E']:3d} C={c['C']:3d} G={c['G']:3d}"
              f" | coverage {cov:.1f}% | multi-labelled {multi} ({100*multi/tot:.0f}%)")

    if contested:
        print("\n=== MOST CONTESTED CODES (appear in one run's primary, not the other) ===")
        for code, k in contested.most_common(12):
            print(f"  {code:<8} {k}")

    print(f"\n=== C vs G CONFLICTS ({len(cg_conflicts)}) — one says 'nothing general', "
          "the other says 'missing section' ===")
    for rid in cg_conflicts:
        print(f"  {rid} {texts.get(rid, ('', ''))[0]}")
        print(f"     A: {A[rid]['role']}  {A[rid]['note'][:100]}")
        print(f"     B: {B[rid]['role']}  {B[rid]['note'][:100]}")

    print(f"\n=== ABSORBED/EXCLUDED CONFLICTS ({len(absorbed_conflicts)}) — "
          "in the document per one run, absent per the other ===")
    for rid in absorbed_conflicts:
        a, b = A[rid], B[rid]
        print(f"  {rid} {texts.get(rid, ('', ''))[0]}")
        print(f"     A: {','.join(a['codes']) or '-':<12} {a['role']}   "
              f"B: {','.join(b['codes']) or '-':<12} {b['role']}")

    print(f"\n=== PRIMARY-CODE CONFLICTS ({len(primary_conflicts)}) ===")
    for rid in primary_conflicts:
        a, b = A[rid], B[rid]
        card = texts.get(rid, ("", ""))[0]
        print(f"  {rid} {card:<34} A: {','.join(a['codes']) or '-':<12} "
              f"B: {','.join(b['codes']) or '-'}")

    # G pile: the only evidence that justifies expanding the taxonomy
    print("\n=== G PILE (both runs) ===")
    gs = defaultdict(list)
    for label, R in (("A", A), ("B", B)):
        for rid, r in R.items():
            if r["role"] == "G":
                gs[rid].append((label, r["note"]))
    for rid in sorted(gs):
        print(f"  {rid} {texts.get(rid, ('', ''))[0]}")
        for label, note in gs[rid]:
            print(f"     {label}: {note[:130]}")


if __name__ == "__main__":
    main()
