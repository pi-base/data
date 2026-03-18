#!/usr/bin/env python3
"""
Interactive tool to assign missing pairs to either pairs_reduced or special_pairs.

Usage:
  python3 assign_pairs.py

Commands:
  r SA SB        — add (SA, SB) to pairs_reduced
  s SA SB        — add (SA, SB) to special_pairs
  r SA SB1 SB2 SB3  — add (SA, SB1), (SA, SB2), (SA, SB3) to pairs_reduced
  s SA SB1 SB2 SB3  — same but to special_pairs
  r SA *         — add all missing pairs (SA, *) to pairs_reduced
  s * SB         — add all missing pairs (*, SB) to special_pairs
  status         — show counts
  check          — verify all three lists are pairwise disjoint
  see SA SB      — show which list (SA, SB) is in
  show SA        — show all missing pairs involving SA (as first or second)
  q              — quit and save

Transitive closure runs after every command:
  Rule 1: (A,B) ∈ special, (B,C) ∈ special → (A,C) added to special
  Rule 2: (A,B) ∈ reduced, (A,C) ∈ special → (C,B) added to reduced
  Rule 3: (A,B) ∈ reduced, (C,B) ∈ special → (A,C) added to reduced

Space IDs can be shortened: 1 -> S000001, 25 -> S000025, etc.
"""

import re
import os
import yaml
import datetime
from collections import defaultdict
from pathlib import Path

BASE = Path("/home/batixx/Documents/GitHub/data")

# Hereditary properties (I or Y in the PDF)
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


def load_traits_and_deduce():
    """Run the deduction engine: load manual traits + theorems, deduce until fixpoint."""
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

    return spaces, traits, theorems


def propagate_hereditary(traits, special, theorems, spaces, space_names):
    """Use special_pairs + hereditary properties to deduce new traits.
    Then re-run deduction. Returns list of new deductions."""
    new_deductions = []
    changed = True
    while changed:
        changed = False
        for sa, sb in special:
            if sa == sb:
                continue
            for p in IY_PROPERTIES:
                # Forward: P holds for SA, unknown for SB → P holds for SB
                if traits[sa].get(p) is True and p not in traits[sb]:
                    traits[sb][p] = True
                    na = space_names.get(sb, sb)
                    new_deductions.append((sb, p, True, sa))
                    changed = True
                # Contrapositive: P false for SB, unknown for SA → P false for SA
                if traits[sb].get(p) is False and p not in traits[sa]:
                    traits[sa][p] = False
                    na = space_names.get(sa, sa)
                    new_deductions.append((sa, p, False, sb))
                    changed = True

        # Re-run theorem deduction with new traits
        thm_changed = True
        while thm_changed:
            thm_changed = False
            for thm in theorems:
                if_conds = extract_conditions(thm['if'])
                then_conds = extract_conditions(thm['then'])
                for space in spaces:
                    if all(traits[space].get(p) == v for p, v in if_conds.items()):
                        for p, v in then_conds.items():
                            if p not in traits[space]:
                                traits[space][p] = v
                                thm_changed = True
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
                                thm_changed = True
                                changed = True

    return new_deductions

def pad(s):
    """Convert shorthand like '1' or '25' to 'S000001' or 'S000025'."""
    s = s.strip()
    if s == '*':
        return '*'
    if s.startswith('S'):
        return f"S{int(s[1:]):06d}"
    return f"S{int(s):06d}"

def load_pairs(filepath):
    pairs = set()
    with open(filepath) as f:
        for line in f:
            m = re.match(r'\((S\d+), (S\d+)\)', line.strip())
            if m:
                pairs.add((m.group(1), m.group(2)))
    return pairs

def load_space_names():
    """Load space names from README.md files."""
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
                import yaml
                fm = yaml.safe_load(parts[1])
                if fm and 'name' in fm:
                    names[d] = fm['name']
            except Exception:
                pass
    return names

def save_append(filepath, new_pairs):
    with open(filepath, 'a') as f:
        for sa, sb in sorted(new_pairs):
            f.write(f"({sa}, {sb})\n")

def run_closure(reduced, special, missing, added_reduced, added_special, log_fn=None, origin=None):
    """Run transitive closure until fixpoint. Returns count of pairs added."""
    total_added = 0
    changed = True
    while changed:
        changed = False

        # Rule 1: (A,B) ∈ special, (B,C) ∈ special → (A,C) to special
        special_by_first = {}
        for a, b in special:
            special_by_first.setdefault(a, set()).add(b)

        new_special = set()
        for a, b in list(special):
            if b in special_by_first:
                for c in special_by_first[b]:
                    pair = (a, c)
                    if pair not in special and pair not in reduced:
                        new_special.add(pair)

        if new_special:
            special.update(new_special)
            missing -= new_special
            added_special.update(new_special)
            total_added += len(new_special)
            changed = True
            print(f"  Closure rule 1: added {len(new_special)} to special")
            if log_fn and origin:
                for sa, sb in sorted(new_special):
                    log_fn(f"  +special ({sa}, {sb}) [closure rule 1, origin: {origin}]")

        # Rule 2: (A,B) ∈ reduced, (A,C) ∈ special → (C,B) to reduced
        reduced_by_first = {}
        for a, b in reduced:
            reduced_by_first.setdefault(a, set()).add(b)

        new_reduced = set()
        for a, c in list(special):
            if a in reduced_by_first:
                for b in reduced_by_first[a]:
                    pair = (c, b)
                    if pair not in reduced and pair not in special:
                        new_reduced.add(pair)

        if new_reduced:
            reduced.update(new_reduced)
            missing -= new_reduced
            added_reduced.update(new_reduced)
            total_added += len(new_reduced)
            changed = True
            print(f"  Closure rule 2: added {len(new_reduced)} to reduced")
            if log_fn and origin:
                for sa, sb in sorted(new_reduced):
                    log_fn(f"  +reduced ({sa}, {sb}) [closure rule 2, origin: {origin}]")

        # Rule 3: (A,B) ∈ reduced, (C,B) ∈ special → (A,C) to reduced
        # Because: if A⊃C and C⊃B then A⊃B, but A doesn't contain B, so A can't contain C
        reduced_by_second = {}
        for a, b in reduced:
            reduced_by_second.setdefault(b, set()).add(a)

        new_reduced3 = set()
        for c, b in list(special):
            if b in reduced_by_second:
                for a in reduced_by_second[b]:
                    pair = (a, c)
                    if pair not in reduced and pair not in special:
                        new_reduced3.add(pair)

        if new_reduced3:
            reduced.update(new_reduced3)
            missing -= new_reduced3
            added_reduced.update(new_reduced3)
            total_added += len(new_reduced3)
            changed = True
            print(f"  Closure rule 3: added {len(new_reduced3)} to reduced")
            if log_fn and origin:
                for sa, sb in sorted(new_reduced3):
                    log_fn(f"  +reduced ({sa}, {sb}) [closure rule 3, origin: {origin}]")

    return total_added

def save_all(reduced, special, missing, added_reduced, added_special):
    """Save full state to disk immediately."""
    # Rewrite all three files completely (no append, no duplicates)
    with open(BASE / "pairs_reduced.txt", 'w') as f:
        for sa, sb in sorted(reduced):
            f.write(f"({sa}, {sb})\n")
    with open(BASE / "special_pairs.txt", 'w') as f:
        for sa, sb in sorted(special):
            f.write(f"({sa}, {sb})\n")
    # Append new manual special pairs to the durable file
    if added_special:
        save_append(BASE / "special_pairs_manual.txt", added_special)
    with open(BASE / "missing_pairs.txt", 'w') as f:
        f.write(f"Missing pairs: {len(missing)}\n")
        f.write("=" * 40 + "\n")
        for sa, sb in sorted(missing):
            f.write(f"({sa}, {sb})\n")
    n_r, n_s = len(added_reduced), len(added_special)
    added_reduced.clear()
    added_special.clear()
    return n_r, n_s


def main():
    reduced = load_pairs(BASE / "pairs_reduced.txt")
    special = load_pairs(BASE / "special_pairs.txt")
    space_names = load_space_names()

    # Compute missing pairs dynamically: all pairs minus reduced minus special
    spaces_dir = BASE / "spaces"
    all_space_ids = sorted(d for d in os.listdir(spaces_dir) if d.startswith('S') and os.path.isdir(spaces_dir / d))
    all_pairs = {(sa, sb) for sa in all_space_ids for sb in all_space_ids}
    missing = all_pairs - reduced - special

    # Deduction engine state (loaded lazily on first 'propagate')
    traits = None
    theorems = None
    all_spaces = None

    # Track what we add (pending save)
    added_reduced = set()
    added_special = set()

    # Cumulative session counters (not cleared on save)
    session_reduced = 0
    session_special = 0

    # Undo stack: stores snapshots before each r/s command
    undo_stack = []

    # History of manually added pairs (not closure)
    history = []  # list of (label, pairs) tuples

    # Open log file (append mode)
    log_path = BASE / "assign_pairs.log"
    logfile = open(log_path, 'a')
    def log(cmd_line):
        ts = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        logfile.write(f"[{ts}] {cmd_line}\n")
        logfile.flush()

    log(f"--- session start --- Reduced={len(reduced)} Special={len(special)}")

    print(f"Reduced: {len(reduced)}  Special: {len(special)}  Missing: {len(missing)}")

    # Run closure on startup
    n = run_closure(reduced, special, missing, added_reduced, added_special)
    if n:
        print(f"Startup closure added {n} pairs. Missing: {len(missing)}")

    print("Commands: r/s SA SB [SB2 ...], r/s SA *, r/s * SB, status, check, show SA, help, q")

    while True:
        try:
            line = input("> ").strip()
        except (EOFError, KeyboardInterrupt):
            break
        if not line:
            continue
        log(line)

        parts = line.split()
        cmd = parts[0].lower()

        if cmd == 'q':
            break
        elif cmd in ('help', 'h', '?'):
            print("Commands:")
            print("  r SA SB [SB2 ...]  — add pair(s) (SA, SBx) to pairs_reduced")
            print("  s SA SB [SB2 ...]  — add pair(s) (SA, SBx) to special_pairs")
            print("  r SA *             — add all missing (SA, ?) to pairs_reduced")
            print("  r * SB             — add all missing (?, SB) to pairs_reduced")
            print("  s SA *             — add all missing (SA, ?) to special_pairs")
            print("  s * SB             — add all missing (?, SB) to special_pairs")
            print("  info SA            — show pair counts per list for SA")
            print("  see SA SB          — show which list (SA, SB) is in")
            print("  show SA            — show all missing pairs involving SA")
            print("  show1 SA           — show missing pairs (SA, ?)")
            print("  show2 SA           — show missing pairs (?, SA)")
            print("  propagate          — use hereditary properties + special_pairs to deduce new traits & pairs")
            print("  status             — show current counts")
            print("  top                — top 20 spaces by missing pairs (either position)")
            print("  top1               — top 20 spaces by missing pairs (SA, ?)")
            print("  top2               — top 20 spaces by missing pairs (?, SA)")
            print("  bottom/bottom1/2   — bottom 20 spaces by missing pairs")
            print("  completed/1/2      — spaces with no missing pairs")
            print("  history [N]        — show last N manual additions (default 10)")
            print("  undo               — undo the last r/s command")
            print("  check              — verify all three lists are pairwise disjoint")
            print("  help               — show this message")
            print("  q                  — save and quit")
            print()
            print("Space IDs: 1 = S000001, 25 = S000025, etc.")
            print("Closure runs automatically after every r/s command.")
            continue
        elif cmd == 'status':
            print(f"Reduced: {len(reduced)}  Special: {len(special)}  Missing: {len(missing)}")
            print(f"Added this session — reduced: {session_reduced}, special: {session_special}")
            continue
        elif cmd == 'check':
            rs = reduced & special
            rm = reduced & missing
            sm = special & missing
            if rs or rm or sm:
                if rs:
                    print(f"  OVERLAP reduced & special: {len(rs)}")
                    for p in sorted(rs)[:10]:
                        print(f"    {p}")
                if rm:
                    print(f"  OVERLAP reduced & missing: {len(rm)}")
                    for p in sorted(rm)[:10]:
                        print(f"    {p}")
                if sm:
                    print(f"  OVERLAP special & missing: {len(sm)}")
                    for p in sorted(sm)[:10]:
                        print(f"    {p}")
            else:
                print("All three lists are pairwise disjoint. OK.")
            continue
        elif cmd == 'info':
            if len(parts) < 2:
                print("Usage: info SA")
                continue
            sid = pad(parts[1])
            sname = space_names.get(sid, sid)
            r1 = sum(1 for a, b in reduced if a == sid)
            r2 = sum(1 for a, b in reduced if b == sid)
            s1 = sum(1 for a, b in special if a == sid)
            s2 = sum(1 for a, b in special if b == sid)
            m1 = sum(1 for a, b in missing if a == sid)
            m2 = sum(1 for a, b in missing if b == sid)
            short = parts[1].strip()
            print(f"{sname} ({sid}):")
            h1 = f"({short},?)"
            h2 = f"(?,{short})"
            print(f"               {h1:>7s}  {h2:>7s}  total")
            print(f"  reduced:     {r1:5d}    {r2:5d}  {r1+r2:5d}")
            print(f"  special:     {s1:5d}    {s2:5d}  {s1+s2:5d}")
            print(f"  missing:     {m1:5d}    {m2:5d}  {m1+m2:5d}")
            continue
        elif cmd == 'show':
            if len(parts) < 2:
                print("Usage: show SA")
                continue
            sid = pad(parts[1])
            matches = sorted(p for p in missing if p[0] == sid or p[1] == sid)
            sname = space_names.get(sid, sid)
            print(f"{len(matches)} missing pairs involving {sname} ({sid}):")
            for sa, sb in matches:
                na = space_names.get(sa, sa)
                nb = space_names.get(sb, sb)
                print(f"  ({sa}, {sb})  {na} / {nb}")
            continue
        elif cmd in ('show1', 'show2'):
            if len(parts) < 2:
                print(f"Usage: {cmd} SA")
                continue
            sid = pad(parts[1])
            sname = space_names.get(sid, sid)
            if cmd == 'show1':
                matches = sorted(p for p in missing if p[0] == sid)
                print(f"{len(matches)} missing pairs ({sid}, ?) for {sname}:")
            else:
                matches = sorted(p for p in missing if p[1] == sid)
                print(f"{len(matches)} missing pairs (?, {sid}) for {sname}:")
            for sa, sb in matches:
                na = space_names.get(sa, sa)
                nb = space_names.get(sb, sb)
                print(f"  ({sa}, {sb})  {na} / {nb}")
            continue
        elif cmd in ('top', 'top1', 'top2'):
            from collections import Counter
            n = 20
            if len(parts) >= 2:
                try:
                    n = int(parts[1])
                except ValueError:
                    pass
            if cmd == 'top':
                cnt = Counter()
                for sa, sb in missing:
                    cnt[sa] += 1
                    cnt[sb] += 1
                label = "missing pairs (as first or second)"
            elif cmd == 'top1':
                cnt = Counter(sa for sa, sb in missing)
                label = "missing pairs (SA, ?)"
            else:
                cnt = Counter(sb for sa, sb in missing)
                label = "missing pairs (?, SA)"
            print(f"Top {n} spaces by {label}:")
            for sid, count in cnt.most_common(n):
                sname = space_names.get(sid, sid)
                print(f"  {sid}  {sname:40s}  {count}")
            continue
        elif cmd in ('bottom', 'bottom1', 'bottom2'):
            from collections import Counter
            n = 20
            if len(parts) >= 2:
                try:
                    n = int(parts[1])
                except ValueError:
                    pass
            if cmd == 'bottom':
                cnt = Counter()
                for sa, sb in missing:
                    cnt[sa] += 1
                    cnt[sb] += 1
                label = "missing pairs (as first or second)"
            elif cmd == 'bottom1':
                cnt = Counter(sa for sa, sb in missing)
                label = "missing pairs (SA, ?)"
            else:
                cnt = Counter(sb for sa, sb in missing)
                label = "missing pairs (?, SA)"
            ranked = cnt.most_common()
            ranked.reverse()
            print(f"Bottom {n} spaces by {label}:")
            for sid, count in ranked[:n]:
                sname = space_names.get(sid, sid)
                print(f"  {sid}  {sname:40s}  {count}")
            continue
        elif cmd in ('completed', 'completed1', 'completed2'):
            from collections import Counter
            spaces_dir = BASE / "spaces"
            all_sids = sorted(d for d in os.listdir(spaces_dir) if d.startswith('S') and os.path.isdir(spaces_dir / d))
            if cmd == 'completed':
                cnt = Counter()
                for sa, sb in missing:
                    cnt[sa] += 1
                    cnt[sb] += 1
                done = sorted(s for s in all_sids if cnt[s] == 0)
                label = "either position"
            elif cmd == 'completed1':
                cnt = Counter(sa for sa, sb in missing)
                done = sorted(s for s in all_sids if cnt[s] == 0)
                label = "first position (SA, ?)"
            else:
                cnt = Counter(sb for sa, sb in missing)
                done = sorted(s for s in all_sids if cnt[s] == 0)
                label = "second position (?, SA)"
            print(f"{len(done)} spaces fully resolved in {label}:")
            for sid in done:
                sname = space_names.get(sid, sid)
                print(f"  {sid}  {sname}")
            continue
        elif cmd == 'propagate':
            # Always reload fresh traits so we can see what hereditary adds
            print("Loading deduction engine...")
            all_spaces, traits, theorems = load_traits_and_deduce()
            baseline = sum(len(v) for v in traits.values())
            print(f"  Deduction engine: {len(all_spaces)} spaces, {baseline} trait values.")

            # Build closure-expanded special set for propagation
            special_expanded = set(special)
            changed = True
            while changed:
                changed = False
                sb = {}
                for a, b in special_expanded:
                    sb.setdefault(a, set()).add(b)
                ns = set()
                for a, b in list(special_expanded):
                    if b in sb:
                        for c in sb[b]:
                            if (a, c) not in special_expanded:
                                ns.add((a, c))
                if ns:
                    special_expanded.update(ns)
                    changed = True
            if len(special_expanded) > len(special):
                print(f"  Special pairs expanded by closure: {len(special)} → {len(special_expanded)}")

            # Run hereditary propagation on fresh traits with closure-expanded special
            new_deductions = propagate_hereditary(traits, special_expanded, theorems, all_spaces, space_names)
            after = sum(len(v) for v in traits.values())
            if new_deductions:
                print(f"  Hereditary propagation found {len(new_deductions)} new trait values ({after - baseline} total with theorem re-deduction):")
                for space, prop, val, via in new_deductions:
                    ns = space_names.get(space, space)
                    nv = space_names.get(via, via)
                    vstr = "holds" if val else "does NOT hold"
                    print(f"    {prop} {vstr} for {ns} ({space})  [via {nv} ({via})]")
            else:
                print("  No new trait values from hereditary propagation.")

            # Now check if any missing pairs can be resolved
            new_reduced = set()
            for sa, sb in list(missing):
                for p in IY_PROPERTIES:
                    if traits[sa].get(p) is True and traits[sb].get(p) is False:
                        new_reduced.add((sa, sb))
                        break

            if new_reduced:
                print(f"  {len(new_reduced)} missing pairs now distinguishable → pairs_reduced")
                reduced.update(new_reduced)
                missing -= new_reduced
                added_reduced.update(new_reduced)
                for sa, sb in sorted(new_reduced):
                    log(f"  +pairs_reduced ({sa}, {sb}) [propagate, hereditary]")
                # Run closure after
                run_closure(reduced, special, missing, added_reduced, added_special, log_fn=log, origin="propagate")
                print(f"  After closure — Missing: {len(missing)}")
                # Save immediately
                n_r, n_s = save_all(reduced, special, missing, added_reduced, added_special)
                session_reduced += n_r
                session_special += n_s
                if n_r or n_s:
                    print(f"  Saved {n_r} reduced + {n_s} special pairs to disk.")
            else:
                print("  No new pairs resolved.")
            continue
        elif cmd == 'undo':
            if not undo_stack:
                print("Nothing to undo.")
                continue
            snapshot = undo_stack.pop()
            reduced.clear()
            reduced.update(snapshot['reduced'])
            special.clear()
            special.update(snapshot['special'])
            missing.clear()
            missing.update(snapshot['missing'])
            added_reduced.clear()
            added_special.clear()
            # Rewrite files to match the restored state
            with open(BASE / "pairs_reduced.txt", 'w') as f:
                for sa, sb in sorted(reduced):
                    f.write(f"({sa}, {sb})\n")
            with open(BASE / "special_pairs.txt", 'w') as f:
                for sa, sb in sorted(special):
                    f.write(f"({sa}, {sb})\n")
            with open(BASE / "missing_pairs.txt", 'w') as f:
                f.write(f"Missing pairs: {len(missing)}\n")
                f.write("=" * 40 + "\n")
                for sa, sb in sorted(missing):
                    f.write(f"({sa}, {sb})\n")
            print(f"Undone and saved. Reduced: {len(reduced)}  Special: {len(special)}  Missing: {len(missing)}")
            continue
        elif cmd == 'random':
            import random
            missing_list = sorted(missing)
            while True:
                if not missing_list:
                    print("No missing pairs left!")
                    break
                sa, sb = random.choice(missing_list)
                na = space_names.get(sa, sa)
                nb = space_names.get(sb, sb)
                print(f"\n({sa}, {sb})  {na} / {nb}")
                ans = input(f"Is {na} ({sa}) a superspace of {nb} ({sb})? [s/r/skip/end] ").strip().lower()
                if ans == 'end':
                    break
                elif ans in ('s', 'r'):
                    target = special if ans == 's' else reduced
                    target_added = added_special if ans == 's' else added_reduced
                    label = "special_pairs" if ans == 's' else "pairs_reduced"
                    undo_stack.append({
                        'reduced': set(reduced),
                        'special': set(special),
                        'missing': set(missing),
                        'added_reduced': set(added_reduced),
                        'added_special': set(added_special),
                    })
                    target.add((sa, sb))
                    missing.discard((sa, sb))
                    target_added.add((sa, sb))
                    history.append((label, [(sa, sb)]))
                    log(f"  +{label} ({sa}, {sb}) [direct, random]")
                    print(f"Added ({sa}, {sb}) to {label}.")
                    run_closure(reduced, special, missing, added_reduced, added_special, log_fn=log, origin=f"random {ans} {sa} {sb}")
                    n_r, n_s = save_all(reduced, special, missing, added_reduced, added_special)
                    session_reduced += n_r
                    session_special += n_s
                    print(f"  Missing: {len(missing)}")
                    missing_list = sorted(missing)
                else:
                    print("Skipped.")
            continue
        elif cmd in ('r', 's'):
            if len(parts) < 3:
                print("Usage: r/s SA SB [SB2 ...] or r/s SA * or r/s * SB")
                continue

            target = reduced if cmd == 'r' else special
            other = special if cmd == 'r' else reduced
            target_added = added_reduced if cmd == 'r' else added_special
            label = "pairs_reduced" if cmd == 'r' else "special_pairs"

            a = pad(parts[1])
            bs = [pad(x) for x in parts[2:]]

            to_add = set()

            if a == '*' and len(bs) == 1:
                sb = bs[0]
                to_add = {p for p in missing if p[1] == sb}
            elif len(bs) == 1 and bs[0] == '*':
                to_add = {p for p in missing if p[0] == a}
            else:
                for b in bs:
                    pair = (a, b)
                    to_add.add(pair)

            # Validate
            problems = []
            for p in to_add:
                if p not in missing:
                    problems.append(f"  {p} not in missing")
                if p in other:
                    problems.append(f"  {p} already in {'special' if cmd == 'r' else 'reduced'}!")

            if problems:
                print("Issues:")
                for prob in problems:
                    print(prob)
                if any("already in" in p for p in problems):
                    print("Aborted (would break disjointness).")
                    continue
                # Filter to only those actually in missing
                to_add = {p for p in to_add if p in missing}
                if not to_add:
                    print("Nothing to add.")
                    continue

            # Confirmation prompt for each pair
            confirmed = set()
            for sa, sb in sorted(to_add):
                na = space_names.get(sa, sa)
                nb = space_names.get(sb, sb)
                if cmd == 's':
                    prompt = f"Are you sure {na} ({sa}) contains {nb} ({sb})? [y/n] "
                else:
                    prompt = f"Are you sure {na} ({sa}) does NOT contain {nb} ({sb})? [y/n] "
                ans = input(prompt).strip().lower()
                if ans in ('y', 'yes'):
                    confirmed.add((sa, sb))
                else:
                    print(f"  Skipped ({sa}, {sb})")

            if not confirmed:
                print("Nothing added.")
                continue

            # Save snapshot for undo (before mutation)
            undo_stack.append({
                'reduced': set(reduced),
                'special': set(special),
                'missing': set(missing),
                'added_reduced': set(added_reduced),
                'added_special': set(added_special),
            })

            target.update(confirmed)
            missing -= confirmed
            target_added.update(confirmed)
            history.append((label, sorted(confirmed)))
            for sa, sb in sorted(confirmed):
                log(f"  +{label} ({sa}, {sb}) [direct]")
            print(f"Added {len(confirmed)} pairs to {label}. Missing: {len(missing)}")

            # Run closure
            run_closure(reduced, special, missing, added_reduced, added_special, log_fn=log, origin=line)
            print(f"  After closure — Missing: {len(missing)}")

            # Save immediately so no data is lost
            n_r, n_s = save_all(reduced, special, missing, added_reduced, added_special)
            session_reduced += n_r
            session_special += n_s
            if n_r or n_s:
                print(f"  Saved {n_r} reduced + {n_s} special pairs to disk.")
        elif cmd == 'see':
            if len(parts) < 3:
                print("Usage: see SA SB")
                continue
            sa = pad(parts[1])
            sb = pad(parts[2])
            pair = (sa, sb)
            na = space_names.get(sa, sa)
            nb = space_names.get(sb, sb)
            if pair in special:
                print(f"({sa}, {sb})  {na} / {nb}  →  special_pairs  // known to be subspace")
            elif pair in reduced:
                print(f"({sa}, {sb})  {na} / {nb}  →  pairs_reduced  // known NOT to be subspace")
            elif pair in missing:
                print(f"({sa}, {sb})  {na} / {nb}  →  missing_pairs  // unknown if subspace")
            else:
                print(f"({sa}, {sb})  {na} / {nb}  →  NOT FOUND (invalid pair?)")
        elif cmd == 'history':
            n = 10
            if len(parts) >= 2:
                try:
                    n = int(parts[1])
                except ValueError:
                    pass
            recent = history[-n:]
            if not recent:
                print("No manual additions yet this session.")
            else:
                for i, (label, pairs) in enumerate(recent, 1):
                    print(f"  {i}. {label}: {len(pairs)} pair(s)")
                    for sa, sb in pairs:
                        na = space_names.get(sa, sa)
                        nb = space_names.get(sb, sb)
                        print(f"       ({sa}, {sb})  {na} / {nb}")
        else:
            print("Unknown command. Use r, s, see, history, undo, status, show, propagate, or q.")

    log("--- session end ---")
    logfile.close()

    # Final save (in case propagate added pairs)
    n_r, n_s = save_all(reduced, special, missing, added_reduced, added_special)
    if n_r or n_s:
        print(f"Saved {n_r} reduced + {n_s} special pairs to disk.")

    # Final disjointness check
    overlap = reduced & special
    if overlap:
        print(f"WARNING: {len(overlap)} pairs in BOTH lists!")
    else:
        print("Disjointness OK.")

if __name__ == '__main__':
    main()
