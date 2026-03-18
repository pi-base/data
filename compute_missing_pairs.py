#!/usr/bin/env python3
"""Find all ordered pairs (SA, SB) of spaces that appear in neither pairs_reduced.txt nor special_pairs.txt."""

import re
import os
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

spaces = sorted(d for d in os.listdir(BASE / "spaces") if d.startswith('S') and os.path.isdir(BASE / "spaces" / d))

covered = load_pairs(BASE / "pairs_reduced.txt") | load_pairs(BASE / "special_pairs.txt")

all_pairs = {(sa, sb) for sa in spaces for sb in spaces}

missing = sorted(all_pairs - covered)

print(f"Total possible pairs: {len(all_pairs)}")
print(f"Covered pairs: {len(covered)}")
print(f"Missing pairs: {len(missing)}")
print("=" * 40)
for sa, sb in missing:
    print(f"({sa}, {sb})")
