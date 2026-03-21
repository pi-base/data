#!/usr/bin/env python3
"""
Check which newly added trait files are redundant (can be deduced from existing traits + theorems).

Usage:
  python3 check_redundancy.py S000076 P000093 P000102 P000110 P000113 P000117 P000177

This checks if any of the listed properties for the given space are redundant.
A trait is redundant if it can be deduced from all other traits (existing + remaining new ones).
Traits are removed one at a time to handle mutual dependencies correctly.
"""

import sys
import os
import yaml
from pathlib import Path
from collections import defaultdict

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


def load_theorems():
    theorems = []
    theorems_dir = BASE / "theorems"
    for tf in sorted(os.listdir(theorems_dir)):
        if not tf.endswith('.md'):
            continue
        fm = parse_frontmatter(theorems_dir / tf)
        if fm and 'if' in fm and 'then' in fm:
            theorems.append(fm)
    return theorems


def load_space_traits(space_id):
    """Load traits from files for a single space."""
    traits = {}
    props_dir = BASE / "spaces" / space_id / "properties"
    if not props_dir.exists():
        return traits
    for pf in os.listdir(props_dir):
        if not pf.endswith('.md'):
            continue
        prop_id = pf[:-3]
        fm = parse_frontmatter(props_dir / pf)
        if fm and 'value' in fm:
            traits[prop_id] = fm['value']
    return traits


def deduce(traits, theorems):
    """Run deduction engine on a single space's traits. Returns new traits dict."""
    result = dict(traits)
    changed = True
    while changed:
        changed = False
        for thm in theorems:
            if_conds = extract_conditions(thm['if'])
            then_conds = extract_conditions(thm['then'])
            # Forward
            if all(result.get(p) == v for p, v in if_conds.items()):
                for p, v in then_conds.items():
                    if p not in result:
                        result[p] = v
                        changed = True
            # Contrapositive (single unknown)
            for tp, tv in then_conds.items():
                if result.get(tp) == (not tv):
                    unknown = [(p, v) for p, v in if_conds.items() if p not in result]
                    known_met = all(
                        result.get(p) == v
                        for p, v in if_conds.items() if p in result
                    )
                    if known_met and len(unknown) == 1:
                        p, v = unknown[0]
                        result[p] = not v
                        changed = True
    return result


def check_redundancy(space_id, new_props):
    """Check which new properties are redundant for a space.

    Returns list of redundant property IDs.
    """
    theorems = load_theorems()
    base_traits = load_space_traits(space_id)

    print(f"Space {space_id}: {len(base_traits)} traits from files")
    print(f"New traits to check: {new_props}")

    # Separate existing from new
    existing = {p: v for p, v in base_traits.items() if p not in new_props}
    new = {p: v for p, v in base_traits.items() if p in new_props}

    # Also check if any new props aren't in the files (not yet added)
    missing = [p for p in new_props if p not in base_traits]
    if missing:
        print(f"WARNING: {missing} not found in trait files for {space_id}")

    print(f"Existing traits: {len(existing)}, New traits under test: {len(new)}")

    # Iteratively check each new trait
    remaining_new = dict(new)
    redundant = []

    for prop in sorted(new_props):
        if prop not in remaining_new:
            continue

        expected_value = remaining_new[prop]

        # Build trait set WITHOUT this property
        test_traits = dict(existing)
        for p, v in remaining_new.items():
            if p != prop:
                test_traits[p] = v

        # Run deduction
        deduced = deduce(test_traits, theorems)

        if deduced.get(prop) == expected_value:
            print(f"  {prop}={expected_value} is REDUNDANT (deduced from others)")
            redundant.append(prop)
            del remaining_new[prop]
        else:
            print(f"  {prop}={expected_value} is NEEDED (not deducible)")

    return redundant


if __name__ == '__main__':
    if len(sys.argv) < 3:
        print("Usage: python3 check_redundancy.py SPACE_ID PROP1 PROP2 ...")
        sys.exit(1)

    space_id = sys.argv[1]
    new_props = [f"P{int(p.lstrip('P')):06d}" if not p.startswith('P000') else p for p in sys.argv[2:]]

    redundant = check_redundancy(space_id, new_props)

    if redundant:
        print(f"\nRedundant traits to delete: {redundant}")
    else:
        print("\nNo redundant traits found.")
