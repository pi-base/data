#!/usr/bin/env python3
"""Test if transitive closure rules would produce conflicts between reduced and special."""

import re
from pathlib import Path

BASE = Path("/home/batixx/Documents/GitHub/data")

def load_pairs(filepath):
    pairs = set()
    with open(filepath) as f:
        for line in f:
            m = re.match(r'\((S\d+), (S\d+)\)', line.strip())
            if m:
                pairs.add((m.group(1), m.group(2)))
    return pairs

reduced = load_pairs(BASE / "pairs_reduced.txt")
special = load_pairs(BASE / "special_pairs.txt")
missing = load_pairs(BASE / "missing_pairs.txt")

# Rule 1: (A,B) ∈ special, (B,C) ∈ special → (A,C) should go to special
# Check if any such (A,C) is already in reduced
special_by_first = {}
special_by_second = {}
for a, b in special:
    special_by_first.setdefault(a, set()).add(b)
    special_by_second.setdefault(b, set()).add(a)

rule1_new = set()
rule1_conflicts = set()
for a, b in special:
    if b in special_by_first:
        for c in special_by_first[b]:
            pair = (a, c)
            if pair not in special:
                if pair in reduced:
                    rule1_conflicts.add(pair)
                else:
                    rule1_new.add(pair)

print(f"Rule 1 (special transitivity):")
print(f"  New pairs to add to special: {len(rule1_new)}")
print(f"  Conflicts (already in reduced): {len(rule1_conflicts)}")
if rule1_conflicts:
    for p in sorted(rule1_conflicts):
        print(f"    CONFLICT: {p}")

# Rule 2: (A,B) ∈ reduced, (A,C) ∈ special → (C,B) should go to reduced
# Check if any such (C,B) is already in special
reduced_by_first = {}
for a, b in reduced:
    reduced_by_first.setdefault(a, set()).add(b)

rule2_new = set()
rule2_conflicts = set()
for a, c in special:
    if a in reduced_by_first:
        for b in reduced_by_first[a]:
            pair = (c, b)
            if pair not in reduced:
                if pair in special:
                    rule2_conflicts.add(pair)
                else:
                    rule2_new.add(pair)

print(f"\nRule 2 (reduced + special → reduced):")
print(f"  New pairs to add to reduced: {len(rule2_new)}")
print(f"  Conflicts (already in special): {len(rule2_conflicts)}")
if rule2_conflicts:
    for p in sorted(rule2_conflicts):
        print(f"    CONFLICT: {p}")

# How many of the new pairs come from missing?
rule1_from_missing = rule1_new & missing
rule2_from_missing = rule2_new & missing
print(f"\nRule 1 new pairs in missing: {len(rule1_from_missing)}")
print(f"Rule 2 new pairs in missing: {len(rule2_from_missing)}")
print(f"Rule 1 new pairs NOT in any list: {len(rule1_new - missing - reduced - special)}")
print(f"Rule 2 new pairs NOT in any list: {len(rule2_new - missing - reduced - special)}")
