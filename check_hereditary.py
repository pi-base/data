#!/usr/bin/env python3
"""Check whether certain properties are hereditary using deduced traits and special_pairs."""

import re
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


def load_traits_and_deduce():
    """Load manual traits + theorems, deduce until fixpoint."""
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

    # Deduce until fixpoint
    changed = True
    iteration = 0
    while changed and iteration < 100:
        changed = False
        iteration += 1
        for thm in theorems:
            if_conds = extract_conditions(thm['if'])
            then_conds = extract_conditions(thm['then'])
            for space in spaces:
                # Forward: all if-conditions met => conclude then-conditions
                if all(traits[space].get(p) == v for p, v in if_conds.items()):
                    for p, v in then_conds.items():
                        if p not in traits[space]:
                            traits[space][p] = v
                            changed = True
                # Contrapositive: then-condition violated + all but one if-condition met => negate unknown
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

    return spaces, traits, theorems


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


def load_property_names():
    names = {}
    props_dir = BASE / "properties"
    for pf in sorted(os.listdir(props_dir)):
        if not pf.startswith('P'):
            continue
        readme = props_dir / pf / "README.md"
        if not readme.exists():
            continue
        fm = parse_frontmatter(readme)
        if fm and 'name' in fm:
            names[pf] = fm['name']
    return names


def main():
    print("Loading traits and running deduction engine...")
    spaces, traits, theorems = load_traits_and_deduce()
    total_traits = sum(len(v) for v in traits.values())
    print(f"  {len(spaces)} spaces, {len(theorems)} theorems, {total_traits} deduced trait values.")

    print("Loading special_pairs.txt...")
    special = load_pairs(BASE / "special_pairs.txt")
    print(f"  {len(special)} special pairs loaded.")

    print("Loading space and property names...")
    space_names = load_space_names()
    prop_names = load_property_names()

    # Properties to check
    props_to_check = [
        "P000076", "P000101", "P000120", "P000138", "P000166", "P000169",
        "P000173", "P000228", "P000221", "P000223", "P000224", "P000225",
    ]

    print()
    print("=" * 80)
    print("Checking hereditary status for each property")
    print("A property is hereditary if: SA contains SB and P(SA)=True => P(SB)=True")
    print("Counterexample: SA contains SB, P(SA)=True, P(SB)=False")
    print("=" * 80)

    for prop in props_to_check:
        pname = prop_names.get(prop, "???")
        counterexamples = []
        for sa, sb in special:
            if sa == sb:
                continue
            val_a = traits[sa].get(prop)
            val_b = traits[sb].get(prop)
            if val_a is True and val_b is False:
                counterexamples.append((sa, sb))

        print()
        print(f"--- {prop}: {pname} ---")
        if counterexamples:
            print(f"  NOT HEREDITARY  ({len(counterexamples)} counterexample(s))")
            for sa, sb in sorted(counterexamples)[:10]:
                na = space_names.get(sa, sa)
                nb = space_names.get(sb, sb)
                print(f"    ({sa}, {sb})  {na} contains {nb}")
                print(f"      {prop}({sa}) = True,  {prop}({sb}) = False")
        else:
            # Check how many pairs have data
            pairs_with_data = 0
            pairs_true_true = 0
            pairs_true_unknown = 0
            for sa, sb in special:
                if sa == sb:
                    continue
                val_a = traits[sa].get(prop)
                val_b = traits[sb].get(prop)
                if val_a is True:
                    pairs_with_data += 1
                    if val_b is True:
                        pairs_true_true += 1
                    elif val_b is None:
                        pairs_true_unknown += 1
            print(f"  No counterexample found (possibly hereditary)")
            print(f"    Pairs where P(SA)=True: {pairs_with_data}")
            print(f"      of which P(SB)=True: {pairs_true_true}, P(SB)=unknown: {pairs_true_unknown}")


if __name__ == '__main__':
    main()
