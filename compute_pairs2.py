#!/usr/bin/env python3
"""
Compute pairs (SA, SB) from pairs_reduced.txt that satisfy at least one of:
- SA = SB (identity, won't appear in pairs_reduced since those require a distinguishing property)
- SB = S000163
- SB = S000164 and SA != S000163
- SB = S000001 and P000125 and P000002 hold for SA
- SB = S000189 and P000175 and P000002 hold for SA
"""

import re
from collections import defaultdict
from pathlib import Path
import yaml
import os

BASE = Path("/home/batixx/Documents/GitHub/data")

# Reuse the deduction engine from compute_pairs.py
IY_PROPERTIES = {
    "P000001", "P000002", "P000003", "P000004", "P000005", "P000006",
    "P000008", "P000009", "P000011", "P000012", "P000014", "P000015",
    "P000027", "P000028", "P000046", "P000047", "P000048", "P000050",
    "P000051", "P000053", "P000080", "P000081", "P000084", "P000090",
    "P000093", "P000099", "P000102", "P000103", "P000106", "P000109",
    "P000110", "P000121", "P000126", "P000134", "P000135", "P000136",
    "P000154", "P000167", "P000168", "P000170", "P000172", "P000174",
    "P000182", "P000186", "P000187", "P000191", "P000196", "P000197",
    "P000208", "P000210", "P000211", "P000212", "P000213", "P000214",
    "P000215", "P000216", "P000226",
    "P000052", "P000054", "P000057", "P000058", "P000059", "P000067",
    "P000074", "P000078", "P000082", "P000094", "P000097", "P000100",
    "P000108", "P000112", "P000113", "P000117", "P000118", "P000129",
    "P000131", "P000132", "P000137", "P000143", "P000144", "P000147",
    "P000163", "P000164", "P000171", "P000177", "P000178", "P000179",
    "P000180", "P000183", "P000184", "P000185", "P000220", "P000222",
}


def parse_frontmatter(filepath):
    with open(filepath, 'r') as f:
        content = f.read()
    if not content.startswith('---'):
        return None
    parts = content.split('---', 2)
    if len(parts) < 3:
        return None
    try:
        return yaml.safe_load(parts[1])
    except yaml.YAMLError:
        return None


def extract_conditions(cond):
    if isinstance(cond, dict):
        if 'and' in cond:
            result = {}
            for item in cond['and']:
                result.update(extract_conditions(item))
            return result
        else:
            return {k: v for k, v in cond.items()}
    return {}


def load_and_deduce():
    traits = defaultdict(dict)
    spaces_dir = BASE / "spaces"
    spaces = []
    for d in sorted(os.listdir(spaces_dir)):
        if d.startswith('S') and os.path.isdir(spaces_dir / d):
            spaces.append(d)
            props_dir = spaces_dir / d / "properties"
            if not props_dir.exists():
                continue
            for pf in os.listdir(props_dir):
                if not pf.endswith('.md'):
                    continue
                prop_id = pf[:-3]
                fm = parse_frontmatter(props_dir / pf)
                if fm and 'value' in fm:
                    traits[d][prop_id] = fm['value']

    theorems = []
    theorems_dir = BASE / "theorems"
    for tf in sorted(os.listdir(theorems_dir)):
        if not tf.endswith('.md'):
            continue
        fm = parse_frontmatter(theorems_dir / tf)
        if fm and 'if' in fm and 'then' in fm:
            theorems.append(fm)

    # Deduce
    changed = True
    iteration = 0
    while changed and iteration < 100:
        changed = False
        iteration += 1
        for thm in theorems:
            if_conds = extract_conditions(thm['if'])
            then_conds = extract_conditions(thm['then'])
            for space in spaces:
                # Forward
                all_if_met = all(
                    traits[space].get(p) == v for p, v in if_conds.items()
                )
                if all_if_met:
                    for p, v in then_conds.items():
                        if p not in traits[space]:
                            traits[space][p] = v
                            changed = True
                # Contrapositive
                for tp, tv in then_conds.items():
                    if traits[space].get(tp) == (not tv):
                        unknown = [(p, v) for p, v in if_conds.items() if p not in traits[space]]
                        known_met = all(
                            traits[space].get(p) == v
                            for p, v in if_conds.items() if p in traits[space]
                        )
                        if known_met and len(unknown) == 1:
                            p, v = unknown[0]
                            traits[space][p] = not v
                            changed = True

    return spaces, traits


def main():
    # Load pairs from pairs_reduced.txt
    pairs_from_file = set()
    with open(BASE / "pairs_reduced.txt") as f:
        for line in f:
            m = re.match(r'\((S\d+), (S\d+)\)', line.strip())
            if m:
                pairs_from_file.add((m.group(1), m.group(2)))

    print(f"Loaded {len(pairs_from_file)} pairs from pairs_reduced.txt")

    # Load traits for conditions involving P125, P2, P175
    spaces, traits = load_and_deduce()

    result_pairs = set()

    for sa, sb in pairs_from_file:
        keep = False

        # A = B (sa == sb won't happen in the file, but check anyway)
        if sa == sb:
            keep = True

        # SB = S163
        if sb == "S000163":
            keep = True

        # SB = S162, SA != S163
        if sb == "S000162" and sa != "S000163":
            keep = True

        # SB = S1, P125 and P2 hold for SA
        if sb == "S000001" and traits[sa].get("P000125") == True and traits[sa].get("P000002") == True:
            keep = True

        # SB = S189, P175 and P2 hold for SA
        if sb == "S000189" and traits[sa].get("P000175") == True and traits[sa].get("P000002") == True:
            keep = True

        if keep:
            result_pairs.add((sa, sb))

    result_pairs = sorted(result_pairs)
    print(f"Filtered pairs: {len(result_pairs)}")
    print("=" * 60)
    for sa, sb in result_pairs:
        print(f"({sa}, {sb})")


if __name__ == '__main__':
    main()
