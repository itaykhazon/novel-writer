#!/usr/bin/env python3
"""Compare two skill-root directories (e.g. .agents/skills vs .claude/skills,
or either of those against an unzipped Cowork .skill export) and report drift.

Each skill root is a directory of <skill-name>/ folders, each containing at
least a SKILL.md plus optional scripts/, references/, assets/. This does a
plain recursive file-content comparison — it doesn't understand SKILL.md
semantics, it just tells you what's different so a human (or an agent) can
decide which side is right.

Usage:
    python3 diff_skill_dirs.py --a .agents/skills --b .claude/skills
    python3 diff_skill_dirs.py --a .agents/skills --b /tmp/cowork-export/draft-chapter --single
"""

import argparse
import hashlib
import os
import sys


def walk_files(root):
    """Return {relative_path: sha256} for every file under root."""
    out = {}
    if not os.path.isdir(root):
        return out
    for dirpath, _dirs, files in os.walk(root):
        for f in files:
            full = os.path.join(dirpath, f)
            rel = os.path.relpath(full, root).replace(os.sep, "/")
            with open(full, "rb") as fh:
                out[rel] = hashlib.sha256(fh.read()).hexdigest()
    return out


def skill_names(root):
    if not os.path.isdir(root):
        return set()
    return {d for d in os.listdir(root) if os.path.isdir(os.path.join(root, d))}


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--a", required=True, help="first skill root (e.g. .agents/skills)")
    ap.add_argument("--b", required=True, help="second skill root (e.g. .claude/skills)")
    ap.add_argument("--single", action="store_true",
                     help="treat --a and --b as a single skill's own folder, not a root of many skills")
    args = ap.parse_args()

    a, b = os.path.abspath(args.a), os.path.abspath(args.b)

    any_drift = False

    if args.single:
        pairs = [(os.path.basename(a.rstrip("/")), a, b)]
    else:
        names_a, names_b = skill_names(a), skill_names(b)
        only_a = sorted(names_a - names_b)
        only_b = sorted(names_b - names_a)
        both = sorted(names_a & names_b)

        if only_a:
            print("Only in %s:" % a)
            for n in only_a:
                print("  - %s" % n)
        if only_b:
            print("Only in %s:" % b)
            for n in only_b:
                print("  - %s" % n)
        if only_a or only_b:
            any_drift = True
            print()

        pairs = [(n, os.path.join(a, n), os.path.join(b, n)) for n in both]

    for name, pa, pb in pairs:
        fa, fb = walk_files(pa), walk_files(pb)
        files_only_a = sorted(set(fa) - set(fb))
        files_only_b = sorted(set(fb) - set(fa))
        changed = sorted(f for f in (set(fa) & set(fb)) if fa[f] != fb[f])

        if not (files_only_a or files_only_b or changed):
            continue

        any_drift = True
        print("=== %s : DRIFT ===" % name)
        for f in files_only_a:
            print("  only in A: %s" % f)
        for f in files_only_b:
            print("  only in B: %s" % f)
        for f in changed:
            print("  content differs: %s" % f)
        print()

    if not any_drift:
        print("No drift detected in %d shared skill folder(s)." % len(pairs))
        return 0

    print("Reconcile by copying the correct side over the other, file by file")
    print("or whole-folder. See this skill's SKILL.md for the recommended")
    print("direction of truth.")
    return 1


if __name__ == "__main__":
    sys.exit(main())
