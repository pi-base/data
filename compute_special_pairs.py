#!/usr/bin/env python3
"""
Generate all pairs (SA, SB) of spaces where at least one of:
- SA = SB
- SB = S000163
- SB = S000162 and SA != S000163
- SB = S000001 and P000125 and P000002 hold for SA
- SB = S000189 and P000175 and P000002 hold for SA
"""

import os
import yaml
from collections import defaultdict
from pathlib import Path

BASE = Path("/home/batixx/Documents/GitHub/data")


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
                if all(traits[space].get(p) == v for p, v in if_conds.items()):
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


def load_existing_pairs(filepath):
    """Load existing pairs so manually-added ones are preserved."""
    import re
    pairs = set()
    try:
        with open(filepath) as f:
            for line in f:
                m = re.match(r'\((S\d+), (S\d+)\)', line.strip())
                if m:
                    pairs.add((m.group(1), m.group(2)))
    except FileNotFoundError:
        pass
    return pairs


def main():
    spaces, traits = load_and_deduce()

    # Load manually-added pairs from the durable file (survives regeneration)
    result_pairs = load_existing_pairs(BASE / "special_pairs_manual.txt")

    # Explicit containment pairs (manually verified)
    result_pairs.add(("S000089", "S000079"))  # Deleted Tychonoff corkscrew ⊃ Deleted Tychonoff plank
    result_pairs.add(("S000089", "S000035"))  # Deleted Tychonoff corkscrew ⊃ ω₁
    result_pairs.add(("S000078", "S000036"))  # Tychonoff plank ⊃ ω₁+1
    result_pairs.add(("S000218", "S000036"))  # ω₁×(ω₁+1) ⊃ ω₁+1

    for sa in spaces:
        # SA = SB
        result_pairs.add((sa, sa))

        # SB = S163
        result_pairs.add((sa, "S000163"))

        # SB = S162, SA != S163
        if sa != "S000163":
            result_pairs.add((sa, "S000162"))

        # SB = S1, P125 and P2 hold for SA
        if traits[sa].get("P000125") is True and traits[sa].get("P000002") is True:
            result_pairs.add((sa, "S000001"))

        # SB = S189, P175 and P2 hold for SA
        if traits[sa].get("P000175") is True and traits[sa].get("P000002") is True:
            result_pairs.add((sa, "S000189"))

        # (S25, SA) where P97 holds for SA
        if traits[sa].get("P000097") is True:
            result_pairs.add(("S000025", sa))

        # (SA, S4) where P1 does NOT hold for SA and P125 holds for SA
        if traits[sa].get("P000001") is False and traits[sa].get("P000125") is True:
            result_pairs.add((sa, "S000004"))

        # (SA, S10) where P135 does NOT hold for SA
        if traits[sa].get("P000135") is False:
            result_pairs.add((sa, "S000010"))

        # (SA, S25) where NOT P139, P122, NOT P137 hold for SA
        if traits[sa].get("P000139") is False and traits[sa].get("P000122") is True and traits[sa].get("P000137") is False:
            result_pairs.add((sa, "S000025"))

        # (SA, S3) where P227 holds for SA
        if traits[sa].get("P000227") is True:
            result_pairs.add((sa, "S000003"))

        # (SA, S2) where P203 and NOT P78 hold for SA
        if traits[sa].get("P000203") is True and traits[sa].get("P000078") is False:
            result_pairs.add((sa, "S000002"))

        # (SA, S3) where P203 and NOT P58 hold for SA
        if traits[sa].get("P000203") is True and traits[sa].get("P000058") is False:
            result_pairs.add((sa, "S000003"))

        # (SA, S2) where P168 and NOT P78 hold for SA
        if traits[sa].get("P000168") is True and traits[sa].get("P000078") is False:
            result_pairs.add((sa, "S000002"))

        # (SA, S2) where NOT P198 holds for SA
        if traits[sa].get("P000198") is False:
            result_pairs.add((sa, "S000002"))

        # (SA, S1) where P135 and NOT P129 hold for SA
        if traits[sa].get("P000135") is True and traits[sa].get("P000129") is False:
            result_pairs.add((sa, "S000001"))

        # (SA, S1) where NOT P196 holds for SA
        if traits[sa].get("P000196") is False:
            result_pairs.add((sa, "S000001"))

    result_pairs = sorted(result_pairs)
    for sa, sb in result_pairs:
        print(f"({sa}, {sb})")


if __name__ == '__main__':
    main()
