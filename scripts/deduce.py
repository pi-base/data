#!/usr/bin/env python3
"""
Pi-base local deduction engine + unknown-trait statistics.

Usage:
  python3 deduce.py                          # run on repo root
  python3 deduce.py --root /path/to/data    # run on a specific snapshot
  python3 deduce.py --compare /path/to/old  # compare old snapshot unknowns against current
"""

import argparse
import yaml
from collections import defaultdict
from dataclasses import dataclass
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent  # default; overridden by --root


# ---------------------------------------------------------------------------
# Data structures
# ---------------------------------------------------------------------------
@dataclass
class Theorem:
    uid: str
    conditions: list   # [(prop_uid: str, value: bool)]
    consequence: tuple  # (prop_uid: str, value: bool)


# ---------------------------------------------------------------------------
# Parsing helpers
# ---------------------------------------------------------------------------
def _parse_frontmatter(path: Path) -> dict:
    text = path.read_text(encoding="utf-8")
    parts = text.split("---")
    if len(parts) < 3:
        return {}
    return yaml.safe_load(parts[1]) or {}


def _parse_if(if_clause) -> list:
    if if_clause is None:
        return []
    if "and" in if_clause:
        result = []
        for item in if_clause["and"]:
            for pid, val in item.items():
                result.append((pid, bool(val)))
        return result
    for pid, val in if_clause.items():
        return [(pid, bool(val))]
    return []


def parse_spaces(root: Path) -> dict:
    spaces = {}
    for space_dir in sorted((root / "spaces").iterdir()):
        readme = space_dir / "README.md"
        if not readme.exists():
            continue
        fm = _parse_frontmatter(readme)
        spaces[fm["uid"]] = fm.get("name", fm["uid"])
    return spaces


def parse_properties(root: Path) -> dict:
    props = {}
    for prop_file in sorted((root / "properties").glob("*.md")):
        fm = _parse_frontmatter(prop_file)
        props[fm["uid"]] = fm.get("name", fm["uid"])
    return props


def parse_theorems(root: Path) -> list:
    theorems = []
    for th_file in sorted((root / "theorems").glob("*.md")):
        fm = _parse_frontmatter(th_file)
        uid = fm.get("uid", th_file.stem)
        conditions = _parse_if(fm.get("if"))
        then = fm.get("then")
        if not conditions or then is None:
            continue
        for pid, val in then.items():
            consequence = (pid, bool(val))
            break
        theorems.append(Theorem(uid=uid, conditions=conditions, consequence=consequence))
    return theorems


def parse_traits(root: Path) -> dict:
    traits = {}
    for space_dir in sorted((root / "spaces").iterdir()):
        prop_dir = space_dir / "properties"
        if not prop_dir.exists():
            continue
        sid = space_dir.name
        for trait_file in prop_dir.glob("*.md"):
            fm = _parse_frontmatter(trait_file)
            sid2 = fm.get("space", sid)
            pid = fm.get("property", trait_file.stem)
            val = fm.get("value")
            if val is not None:
                traits[(sid2, pid)] = bool(val)
    return traits


# ---------------------------------------------------------------------------
# Deduction engine
# ---------------------------------------------------------------------------
def expand_contrapositives(theorems: list) -> list:
    """
    For each theorem (C1 ∧ … ∧ Cn) → Q add all n contrapositives:
      for each i: (C1 ∧ … ∧ C_{i-1} ∧ C_{i+1} ∧ … ∧ Cn ∧ ¬Q) → ¬Ci
    """
    extra = []
    for th in theorems:
        conds = th.conditions
        cpid, cval = th.consequence
        neg_cons = (cpid, not cval)
        for i, (pid, val) in enumerate(conds):
            new_conds = [c for j, c in enumerate(conds) if j != i] + [neg_cons]
            extra.append(Theorem(uid=th.uid + "_cp", conditions=new_conds,
                                 consequence=(pid, not val)))
    return theorems + extra


def build_index(theorems: list) -> dict:
    """prop_uid → [theorem_index] for theorems that mention that prop in `if`."""
    index = defaultdict(list)
    for i, th in enumerate(theorems):
        for pid, _val in th.conditions:
            index[pid].append(i)
    return index


def deduce_space(known: dict, theorems: list, index: dict) -> dict:
    """
    Forward-chain from `known` traits ({pid: bool}) using theorems.
    Returns extended dict including all derivable traits.
    """
    traits = dict(known)
    queue = list(traits.keys())
    while queue:
        pid = queue.pop()
        for t_idx in index.get(pid, []):
            th = theorems[t_idx]
            if all(traits.get(p) == v for p, v in th.conditions):
                cpid, cval = th.consequence
                if cpid not in traits:
                    traits[cpid] = cval
                    queue.append(cpid)
    return traits


def compute_known(root: Path) -> tuple:
    """Return (spaces, properties, asserted, all_known_pairs) for a given root."""
    spaces     = parse_spaces(root)
    properties = parse_properties(root)
    theorems   = parse_theorems(root)
    asserted   = parse_traits(root)

    theorems = expand_contrapositives(theorems)
    index    = build_index(theorems)

    asserted_by_space = defaultdict(dict)
    for (sid, pid), val in asserted.items():
        asserted_by_space[sid][pid] = val

    all_known = set(asserted.keys())
    for sid in spaces:
        result = deduce_space(asserted_by_space.get(sid, {}), theorems, index)
        for pid in result:
            all_known.add((sid, pid))

    return spaces, properties, asserted, all_known


# ---------------------------------------------------------------------------
# Formatting helpers
# ---------------------------------------------------------------------------
def fmt_name(name: str, width: int = 40) -> str:
    if len(name) > width:
        return name[:width - 1] + "…"
    return name.ljust(width)


def print_table(rows, headers, col_widths):
    fmt = "  ".join(f"{{:<{w}}}" for w in col_widths)
    sep = "  ".join("-" * w for w in col_widths)
    print(fmt.format(*headers))
    print(sep)
    for row in rows:
        print(fmt.format(*row))


# ---------------------------------------------------------------------------
# Main report
# ---------------------------------------------------------------------------
def report(root: Path):
    print(f"Loading data from {root} …", flush=True)
    spaces, properties, asserted, all_known = compute_known(root)

    total_pairs = len(spaces) * len(properties)
    n_asserted  = len(asserted)
    n_derived   = len(all_known) - n_asserted
    n_unknown   = total_pairs - len(all_known)

    print()
    print("=" * 60)
    print("GLOBAL SUMMARY")
    print("=" * 60)
    print(f"  Spaces / Properties / Theorems : "
          f"{len(spaces)} / {len(properties)} / {len(parse_theorems(root))}")
    print(f"  Total (space, property) pairs  : {total_pairs:>7,}")
    print(f"  Manually asserted              : {n_asserted:>7,}  ({100*n_asserted/total_pairs:.1f}%)")
    print(f"  Deduced by engine              : {n_derived:>7,}  ({100*n_derived/total_pairs:.1f}%)")
    print(f"  Unknown (neither)              : {n_unknown:>7,}  ({100*n_unknown/total_pairs:.1f}%)")

    prop_unknown  = {pid: sum(1 for sid in spaces if (sid, pid) not in all_known)
                     for pid in properties}
    space_unknown = {sid: sum(1 for pid in properties if (sid, pid) not in all_known)
                     for sid in spaces}

    top_props = sorted(prop_unknown.items(), key=lambda x: -x[1])[:50]
    print()
    print("=" * 60)
    print("TOP 50 PROPERTIES BY UNKNOWN-SPACE COUNT")
    print("=" * 60)
    rows = [(fmt_name(properties[pid]), pid, str(cnt), f"{100*cnt/len(spaces):.0f}%")
            for pid, cnt in top_props]
    print_table(rows, ["Property name", "UID", "Unknown spaces", "Pct"], [42, 10, 14, 5])

    top_spaces = sorted(space_unknown.items(), key=lambda x: -x[1])[:50]
    print()
    print("=" * 60)
    print("TOP 50 SPACES BY UNKNOWN-PROPERTY COUNT")
    print("=" * 60)
    rows = [(fmt_name(spaces[sid]), sid, str(cnt), f"{100*cnt/len(properties):.0f}%")
            for sid, cnt in top_spaces]
    print_table(rows, ["Space name", "UID", "Unknown props", "Pct"], [42, 10, 13, 5])


# ---------------------------------------------------------------------------
# Comparison: old snapshot unknowns resolved by current data
# ---------------------------------------------------------------------------
def compare(old_root: Path, new_root: Path):
    print(f"Loading OLD snapshot from {old_root} …", flush=True)
    old_spaces, old_props, _, old_known = compute_known(old_root)

    print(f"Loading CURRENT snapshot from {new_root} …", flush=True)
    _, _, _, new_known = compute_known(new_root)

    old_universe  = {(sid, pid) for sid in old_spaces for pid in old_props}
    old_unknown   = old_universe - old_known
    now_resolved  = old_unknown & new_known
    still_unknown = old_unknown - new_known

    print()
    print("=" * 60)
    print("COMPARISON: Nov 1 2025 unknowns → today")
    print("=" * 60)
    print(f"  Unknown pairs on Nov 1 (old universe) : {len(old_unknown):>5,}")
    print(f"  Now resolved                          : {len(now_resolved):>5,}  "
          f"({100*len(now_resolved)/len(old_unknown):.1f}%)")
    print(f"  Still unknown today                   : {len(still_unknown):>5,}  "
          f"({100*len(still_unknown)/len(old_unknown):.1f}%)")

    by_prop = defaultdict(int)
    for sid, pid in now_resolved:
        by_prop[pid] += 1

    top = sorted(by_prop.items(), key=lambda x: -x[1])[:20]
    print()
    print("TOP 20 PROPERTIES WITH MOST RESOLUTIONS SINCE NOV 1")
    print("-" * 60)
    rows = [(fmt_name(old_props[pid]), pid, str(cnt)) for pid, cnt in top]
    print_table(rows, ["Property name", "UID", "Resolved"], [42, 10, 8])

    by_space = defaultdict(int)
    for sid, pid in now_resolved:
        by_space[sid] += 1

    top_s = sorted(by_space.items(), key=lambda x: -x[1])[:20]
    print()
    print("TOP 20 SPACES WITH MOST RESOLUTIONS SINCE NOV 1")
    print("-" * 60)
    rows = [(fmt_name(old_spaces[sid]), sid, str(cnt)) for sid, cnt in top_s]
    print_table(rows, ["Space name", "UID", "Resolved"], [42, 10, 8])


# ---------------------------------------------------------------------------
# Entry point
# ---------------------------------------------------------------------------
def main():
    global ROOT
    parser = argparse.ArgumentParser()
    parser.add_argument("--root", type=Path,
                        default=Path(__file__).resolve().parent.parent)
    parser.add_argument("--compare", type=Path, metavar="OLD_ROOT",
                        help="compare OLD_ROOT unknowns against --root (current)")
    args = parser.parse_args()
    ROOT = args.root

    if args.compare:
        compare(old_root=args.compare, new_root=ROOT)
    else:
        report(ROOT)


if __name__ == "__main__":
    main()
