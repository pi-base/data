#!/usr/bin/env python3
"""
Compute all pairs (SA, SB) where there exists a property P (marked I or Y in the PDF)
such that P is true for SA and false for SB, using the pi-base deduction engine.
"""

import os
import yaml
import re
from collections import defaultdict
from pathlib import Path

BASE = Path("/home/batixx/Documents/GitHub/data")

# Properties marked I or Y in the PDF
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
    """Parse YAML frontmatter from a markdown file."""
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


def load_spaces():
    """Load all space IDs."""
    spaces_dir = BASE / "spaces"
    spaces = []
    for d in sorted(os.listdir(spaces_dir)):
        if d.startswith('S') and os.path.isdir(spaces_dir / d):
            spaces.append(d)
    return spaces


def load_manual_traits():
    """Load manually entered traits for all spaces."""
    # traits[space_id][prop_id] = True/False
    traits = defaultdict(dict)
    spaces_dir = BASE / "spaces"
    for space in sorted(os.listdir(spaces_dir)):
        if not space.startswith('S'):
            continue
        props_dir = spaces_dir / space / "properties"
        if not props_dir.exists():
            continue
        for pf in os.listdir(props_dir):
            if not pf.endswith('.md'):
                continue
            prop_id = pf[:-3]  # Remove .md
            fm = parse_frontmatter(props_dir / pf)
            if fm and 'value' in fm:
                traits[space][prop_id] = fm['value']
    return traits


def load_theorems():
    """Load all theorems (implications)."""
    theorems = []
    theorems_dir = BASE / "theorems"
    for tf in sorted(os.listdir(theorems_dir)):
        if not tf.endswith('.md'):
            continue
        fm = parse_frontmatter(theorems_dir / tf)
        if fm and 'if' in fm and 'then' in fm:
            theorems.append(fm)
    return theorems


def extract_conditions(cond):
    """
    Extract conditions as a dict of {prop_id: bool_value}.
    Handles both simple {P: true/false} and {and: [{P1: true}, {P2: false}]} forms.
    """
    if isinstance(cond, dict):
        if 'and' in cond:
            result = {}
            for item in cond['and']:
                result.update(extract_conditions(item))
            return result
        else:
            return {k: v for k, v in cond.items()}
    return {}


def deduce(traits, theorems, max_iterations=100):
    """
    Run forward-chaining deduction engine.
    Also handles contrapositives.
    """
    changed = True
    iteration = 0
    while changed and iteration < max_iterations:
        changed = False
        iteration += 1
        for thm in theorems:
            if_conds = extract_conditions(thm['if'])
            then_conds = extract_conditions(thm['then'])

            for space in list(traits.keys()):
                # Forward: if all 'if' conditions are met, deduce 'then'
                all_if_met = True
                for prop, val in if_conds.items():
                    if prop not in traits[space] or traits[space][prop] != val:
                        all_if_met = False
                        break
                if all_if_met:
                    for prop, val in then_conds.items():
                        if prop not in traits[space]:
                            traits[space][prop] = val
                            changed = True

                # Contrapositive: if some 'then' condition is known to be opposite,
                # and all but one 'if' condition is met, deduce the remaining is opposite.
                # For single-antecedent theorems with single consequent:
                # if A -> B, and ~B, then ~A
                # More generally: if (A1 & A2 & ... & An) -> B, and ~B,
                # and A1...A(n-1) are all true, then ~An

                # Check contrapositive for each 'then' condition
                for then_prop, then_val in then_conds.items():
                    if then_prop in traits[space] and traits[space][then_prop] == (not then_val):
                        # A consequent is violated
                        # Check if all but one antecedent is satisfied
                        unknown_ifs = []
                        all_known_met = True
                        for if_prop, if_val in if_conds.items():
                            if if_prop not in traits[space]:
                                unknown_ifs.append((if_prop, if_val))
                            elif traits[space][if_prop] != if_val:
                                all_known_met = False
                                break
                        if all_known_met and len(unknown_ifs) == 1:
                            prop, val = unknown_ifs[0]
                            neg_val = not val
                            if prop not in traits[space]:
                                traits[space][prop] = neg_val
                                changed = True

    print(f"Deduction completed in {iteration} iterations")
    return traits


def main():
    print("Loading spaces...")
    spaces = load_spaces()
    print(f"Found {len(spaces)} spaces")

    print("Loading manual traits...")
    traits = load_manual_traits()
    total_manual = sum(len(v) for v in traits.values())
    print(f"Found {total_manual} manual traits")

    print("Loading theorems...")
    theorems = load_theorems()
    print(f"Found {len(theorems)} theorems")

    print("Running deduction engine...")
    traits = deduce(traits, theorems)
    total_deduced = sum(len(v) for v in traits.values())
    print(f"Total traits after deduction: {total_deduced} (added {total_deduced - total_manual})")

    # For each I/Y property, find spaces where it's true and where it's false
    prop_true = defaultdict(set)   # prop -> set of spaces where true
    prop_false = defaultdict(set)  # prop -> set of spaces where false

    for space in spaces:
        for prop in IY_PROPERTIES:
            if prop in traits[space]:
                if traits[space][prop] == True:
                    prop_true[prop].add(space)
                elif traits[space][prop] == False:
                    prop_false[prop].add(space)

    # Find all pairs (SA, SB) where exists P in IY s.t. P true for SA, P false for SB
    # Collect pairs as a set
    pairs = set()
    for prop in IY_PROPERTIES:
        for sa in prop_true[prop]:
            for sb in prop_false[prop]:
                pairs.add((sa, sb))

    # Sort and print
    pairs = sorted(pairs)
    print(f"\nTotal pairs: {len(pairs)}")
    print("=" * 60)
    for sa, sb in pairs:
        # Find witnessing properties
        witnesses = []
        for prop in sorted(IY_PROPERTIES):
            if sa in prop_true[prop] and sb in prop_false[prop]:
                witnesses.append(prop)
        print(f"({sa}, {sb})  witnesses: {', '.join(witnesses)}")


if __name__ == '__main__':
    main()
