#!/usr/bin/env python3
"""List reviewer skills from the sibling reviewers/ directory, parsed from
each SKILL.md's frontmatter, filtered and ordered for chapter-cycle's Phase 2.

Self-locating: assumes the layout skills-root/chapter-cycle/scripts/<this file>
and skills-root/reviewers/<name>/SKILL.md, since chapter-cycle and reviewers/
are always siblings under the same .agents/skills or .claude/skills tree.

Usage:
    python3 scripts/list_reviewers.py                # default-in-cycle only, in cycle-order
    python3 scripts/list_reviewers.py --all           # every reviewer, alphabetical
    python3 scripts/list_reviewers.py --json          # machine-readable
"""

import argparse
import json
import os
import re
import sys

FRONTMATTER_FIELDS = (
    "name", "reviewer-kind", "reviewer-scope", "thinking-level",
    "complexity", "default-in-cycle", "cycle-order",
)


def parse_frontmatter(path):
    with open(path, encoding="utf-8") as f:
        lines = f.readlines()
    if not lines or lines[0].strip() != "---":
        return None
    end = None
    for i in range(1, len(lines)):
        if lines[i].strip() == "---":
            end = i
            break
    if end is None:
        return None
    data = {}
    for line in lines[1:end]:
        m = re.match(r"^([A-Za-z0-9_-]+):\s*(.*)$", line)
        if not m:
            continue
        key, val = m.group(1), m.group(2).strip()
        if key in FRONTMATTER_FIELDS:
            data[key] = val
    return data


def load_reviewers(reviewers_root):
    out = []
    if not os.path.isdir(reviewers_root):
        return out
    for name in sorted(os.listdir(reviewers_root)):
        skill_path = os.path.join(reviewers_root, name, "SKILL.md")
        if not os.path.isfile(skill_path):
            continue  # e.g. TEMPLATE.md, which has no SKILL.md of its own
        fm = parse_frontmatter(skill_path)
        if not fm or "reviewer-kind" not in fm:
            continue  # not a reviewer-template-conformant skill; skip rather than guess
        fm.setdefault("name", name)
        fm["default-in-cycle"] = fm.get("default-in-cycle", "false").lower() == "true"
        try:
            fm["cycle-order"] = int(fm["cycle-order"]) if "cycle-order" in fm else None
        except ValueError:
            fm["cycle-order"] = None
        try:
            fm["complexity"] = int(fm["complexity"]) if "complexity" in fm else None
        except ValueError:
            fm["complexity"] = None
        out.append(fm)
    return out


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--all", action="store_true", help="list every reviewer, not just default-in-cycle ones")
    ap.add_argument("--json", action="store_true", help="machine-readable output")
    args = ap.parse_args()

    script_dir = os.path.dirname(os.path.abspath(__file__))
    skills_root = os.path.dirname(os.path.dirname(script_dir))  # .../chapter-cycle/scripts -> .../chapter-cycle -> skills root
    reviewers_root = os.path.join(skills_root, "reviewers")

    reviewers = load_reviewers(reviewers_root)
    if not args.all:
        reviewers = [r for r in reviewers if r["default-in-cycle"]]
        reviewers.sort(key=lambda r: (r["cycle-order"] is None, r["cycle-order"]))
    else:
        reviewers.sort(key=lambda r: r["name"])

    if args.json:
        print(json.dumps(reviewers, indent=2))
        return 0

    if not reviewers:
        print("No reviewers found under %s" % reviewers_root, file=sys.stderr)
        return 1

    width = max(len(r["name"]) for r in reviewers)
    for r in reviewers:
        order = r.get("cycle-order")
        order_s = str(order) if order is not None else "-"
        print("%-3s %-*s  thinking=%-9s complexity=%-2s scope=%-8s kind=%s" % (
            order_s, width, r["name"], r.get("thinking-level", "?"),
            r.get("complexity", "?"), r.get("reviewer-scope", "?"), r.get("reviewer-kind", "?"),
        ))
    return 0


if __name__ == "__main__":
    sys.exit(main())
