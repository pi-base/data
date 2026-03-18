#!/usr/bin/env python3
"""
Use special_pairs (SA contains SB) + hereditary properties to deduce new trait values.

If P is hereditary (I or Y) and (SA,SB) in special_pairs:
  - P holds for SA, P unknown for SB → P holds for SB
  - P does NOT hold for SB, P unknown for SA → P does NOT hold for SA
"""

import os
import re
import yaml
from collections import defaultdict
from pathlib import Path

BASE = Path("/home/batixx/Documents/GitHub/data")

# Hereditary properties from the PDF (I or Y)
IY_PROPERTIES = {
    # I properties
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
    # Y properties
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

    changed = True
    iteration = 0
    while changed and iteration < 100:
        changed = False
        iteration += 1
        for thm in theorems:
            if_conds = extract_conditions(thm['if'])
            then_conds = extract_conditions(thm['then'])
            for space in spaces:
                if all(traits[space].get(p) == v for p, v in if_conds.items()):
                    for p, v in then_conds.items():
                        if p not in traits[space]:
                            traits[space][p] = v
                            changed = True
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


def load_pairs(filepath):
    pairs = set()
    with open(filepath) as f:
        for line in f:
            m = re.match(r'\((S\d+), (S\d+)\)', line.strip())
            if m:
                pairs.add((m.group(1), m.group(2)))
    return pairs


def load_space_names():
    names = {}
    spaces_dir = BASE / "spaces"
    for d in sorted(os.listdir(spaces_dir)):
        if not d.startswith('S'):
            continue
        readme = spaces_dir / d / "README.md"
        if not readme.exists():
            continue
        with open(readme) as f:
            content = f.read()
        parts = content.split('---', 2)
        if len(parts) >= 3:
            try:
                fm = yaml.safe_load(parts[1])
                if fm and 'name' in fm:
                    names[d] = fm['name']
            except Exception:
                pass
    return names


def main():
    print("Running deduction engine...")
    spaces, traits = load_and_deduce()
    special = load_pairs(BASE / "special_pairs.txt")
    space_names = load_space_names()

    # Also include closure pairs
    changed = True
    while changed:
        changed = False
        sb = {}
        for a, b in special:
            sb.setdefault(a, set()).add(b)
        ns = set()
        for a, b in list(special):
            if b in sb:
                for c in sb[b]:
                    if (a, c) not in special:
                        ns.add((a, c))
        if ns:
            special.update(ns)
            changed = True

    print(f"Special pairs (with closure): {len(special)}")

    # Forward: P holds for SA, unknown for SB → P holds for SB
    forward = []
    # Contrapositive: P false for SB, unknown for SA → P false for SA
    contra = []

    for sa, sb in sorted(special):
        if sa == sb:
            continue
        for p in sorted(IY_PROPERTIES):
            # Forward
            if traits[sa].get(p) is True and p not in traits[sb]:
                forward.append((sa, sb, p))
            # Contrapositive
            if traits[sb].get(p) is False and p not in traits[sa]:
                contra.append((sa, sb, p))

    print(f"\n=== Forward: P holds for SA, unknown for SB → P holds for SB ===")
    print(f"Count: {len(forward)}")
    # Group by (SB, P) since that's the new deduction
    from collections import Counter
    fwd_deductions = {}
    for sa, sb, p in forward:
        key = (sb, p)
        if key not in fwd_deductions:
            fwd_deductions[key] = []
        fwd_deductions[key].append(sa)

    for (sb, p), sources in sorted(fwd_deductions.items()):
        nb = space_names.get(sb, sb)
        print(f"  {p} holds for {nb} ({sb})  [via {sources[0]}]")

    print(f"\n=== Contrapositive: P false for SB, unknown for SA → P false for SA ===")
    print(f"Count: {len(contra)}")
    contra_deductions = {}
    for sa, sb, p in contra:
        key = (sa, p)
        if key not in contra_deductions:
            contra_deductions[key] = []
        contra_deductions[key].append(sb)

    for (sa, p), sources in sorted(contra_deductions.items()):
        na = space_names.get(sa, sa)
        print(f"  {p} does NOT hold for {na} ({sa})  [via {sources[0]}]")


if __name__ == '__main__':
    main()
