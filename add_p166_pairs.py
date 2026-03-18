#!/usr/bin/env python3
"""
Add pairs (SA, SB) where P166 holds for SA but not SB to pairs_output.txt and pairs_reduced.txt.
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


def load_existing_pairs(filepath):
    """Load existing pairs from a file."""
    pairs = set()
    import re
    with open(filepath) as f:
        for line in f:
            m = re.match(r'\((S\d+), (S\d+)\)', line.strip())
            if m:
                pairs.add((m.group(1), m.group(2)))
    return pairs


def main():
    spaces, traits = load_and_deduce()

    # Find spaces where P166 is true and where P166 is false
    p166_true = set()
    p166_false = set()
    for s in spaces:
        if traits[s].get("P000166") is True:
            p166_true.add(s)
        elif traits[s].get("P000166") is False:
            p166_false.add(s)

    print(f"P166 true: {len(p166_true)} spaces")
    print(f"P166 false: {len(p166_false)} spaces")

    new_pairs = set()
    for sa in p166_true:
        for sb in p166_false:
            new_pairs.add((sa, sb))

    print(f"New P166 pairs: {len(new_pairs)}")

    # Update pairs_output.txt
    existing_full = load_existing_pairs(BASE / "pairs_output.txt")
    added_full = new_pairs - existing_full
    print(f"New pairs to add to pairs_output.txt: {len(added_full)}")

    with open(BASE / "pairs_output.txt", "a") as f:
        for sa, sb in sorted(added_full):
            f.write(f"({sa}, {sb})  witnesses: P000166\n")

    # Update pairs_reduced.txt
    existing_reduced = load_existing_pairs(BASE / "pairs_reduced.txt")
    added_reduced = new_pairs - existing_reduced
    print(f"New pairs to add to pairs_reduced.txt: {len(added_reduced)}")

    with open(BASE / "pairs_reduced.txt", "a") as f:
        for sa, sb in sorted(added_reduced):
            f.write(f"({sa}, {sb})\n")


if __name__ == '__main__':
    main()
