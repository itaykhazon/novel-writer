#!/usr/bin/env python3
"""Scaffold a new reviewer skill under reviewers/, in both .agents/skills/ and
.claude/skills/, conformant to reviewers/TEMPLATE.md's frontmatter contract.

Self-locating: assumes skills-root/add-reviewer/scripts/<this file>, with
reviewers/ and chapter-cycle/ as siblings under the same skills root. Run it
once, from either tree (it doesn't matter which) -- it writes byte-identical
skeleton SKILL.md files to both .agents/skills/reviewers/<name>/ and
.claude/skills/reviewers/<name>/.

Usage:
    python3 scripts/scaffold_reviewer.py --name my-reviewer \
        --description "Full SKILL.md frontmatter description line -- what it \
checks, when to use it." \
        --reviewer-kind line --reviewer-scope chapter \
        --thinking-level medium --complexity 5 \
        --default-in-cycle true --cycle-order 3

--cycle-order is required when --default-in-cycle is true, and rejected
otherwise. When given, every existing default-in-cycle reviewer at or after
that slot (in either tree) is shifted down by one to make room -- nothing is
overwritten, and nothing needs hand-renumbering afterward.

This only writes the frontmatter and a stubbed section skeleton (each
required section from reviewers/TEMPLATE.md, marked with an HTML comment
saying what belongs there). Writing the actual reviewing logic -- what this
reviewer checks, its scope-and-boundaries language, its severity scale, its
workflow and output format -- is a judgment call for whoever runs this skill,
not something this script can generate.
"""

import argparse
import json
import os
import re
import subprocess
import sys

SKELETON = """---
name: {name}
description: |
  {description}
reviewer-kind: {reviewer_kind}
reviewer-scope: {reviewer_scope}
thinking-level: {thinking_level}
complexity: {complexity}
default-in-cycle: {default_in_cycle}{cycle_order_line}
---

# {title}

<!-- Opening paragraph(s), no heading -- see reviewers/TEMPLATE.md item 1.
     One or two sentences: what does this reviewer look for, and what does
     it hand back? -->

## Required reading

<!-- What to read before reviewing: reference files bundled with this skill,
     codex/ files, a POV voice guide, a bundled analysis script to run
     first. Say explicitly what NOT to do here too, if this reviewer is
     meant to work from a prebuilt bundle rather than exploring the vault.
     See reviewers/TEMPLATE.md item 2. -->

## Scope and boundaries

<!-- What this reviewer owns, and an explicit list of sibling reviewers it
     defers to for anything adjacent, by name. This is the mechanism that
     keeps reviewers from duplicating each other's findings on the same
     passage -- skipping it is how that drifts. See reviewers/TEMPLATE.md
     item 3, and read a couple of existing reviewers' own "Scope and
     boundaries" sections before writing this one. -->

## Severity

<!-- The scale this reviewer's findings are labeled with. This vault has
     both a HIGH/MEDIUM/LOW and a CRITICAL/WARNING/NOTE convention in use --
     pick whichever fits this reviewer's own judgment calls better, say
     which, and define each tier. See reviewers/TEMPLATE.md item 4. -->

## Workflow

<!-- The numbered steps from "read the input" to "return/save the report."
     See reviewers/TEMPLATE.md item 5. -->

## Output format

<!-- The exact report template, including where (and under what filename)
     it gets saved, and what happens for input that isn't a saved chapter
     (an unnamed pasted passage). See reviewers/TEMPLATE.md item 6. -->

## Hard safeguards

<!-- The explicit do-not-do list: never edit manuscript prose, never
     overreach into a sibling reviewer's territory, whatever failure modes
     are specific to this reviewer's judgment call. See reviewers/TEMPLATE.md
     item 7. -->
"""


def title_case(name):
    return " ".join(w.capitalize() for w in name.split("-"))


def load_cycle_json(list_reviewers_py):
    out = subprocess.run(
        [sys.executable, list_reviewers_py, "--all", "--json"],
        capture_output=True, text=True, check=True,
    )
    return json.loads(out.stdout)


def shift_cycle_order(skill_md_path, at_or_after):
    """Bump this file's cycle-order by one if it's >= at_or_after. Returns
    True if the file was changed."""
    with open(skill_md_path, encoding="utf-8") as f:
        content = f.read()

    def bump(m):
        val = int(m.group(1))
        if val >= at_or_after:
            val += 1
        return "cycle-order: %d" % val

    new_content, n = re.subn(r"cycle-order:\s*(\d+)", bump, content, count=1)
    if n and new_content != content:
        with open(skill_md_path, "w", encoding="utf-8") as f:
            f.write(new_content)
        return True
    return False


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--name", required=True, help="kebab-case skill name, e.g. dialogue-tag-review")
    ap.add_argument("--description", required=True, help="the frontmatter description line (what it checks, when to use it)")
    ap.add_argument("--reviewer-kind", required=True, choices=["line", "structural", "reader-simulation"])
    ap.add_argument("--reviewer-scope", required=True, choices=["chapter", "arc", "book"])
    ap.add_argument("--thinking-level", required=True, choices=["very-low", "low", "medium", "high"])
    ap.add_argument("--complexity", required=True, type=int, choices=range(1, 11))
    ap.add_argument("--default-in-cycle", required=True, choices=["true", "false"])
    ap.add_argument("--cycle-order", type=int, help="required iff --default-in-cycle true; the position (1-based) this reviewer should run at")
    args = ap.parse_args()

    if args.default_in_cycle == "true" and args.cycle_order is None:
        ap.error("--cycle-order is required when --default-in-cycle true")
    if args.default_in_cycle == "false" and args.cycle_order is not None:
        ap.error("--cycle-order only applies when --default-in-cycle true")

    script_dir = os.path.dirname(os.path.abspath(__file__))
    this_tree_skills = os.path.dirname(os.path.dirname(script_dir))  # add-reviewer/scripts -> add-reviewer -> skills root
    tool_dir = os.path.dirname(this_tree_skills)                     # .agents or .claude
    vault_root = os.path.dirname(tool_dir)
    tree_a = os.path.join(vault_root, ".agents", "skills")
    tree_b = os.path.join(vault_root, ".claude", "skills")

    for tree in (tree_a, tree_b):
        dest = os.path.join(tree, "reviewers", args.name)
        if os.path.exists(dest):
            print("error: %s already exists" % dest, file=sys.stderr)
            return 1

    cycle_order_line = ""
    if args.default_in_cycle == "true":
        cycle_order_line = "\ncycle-order: %d" % args.cycle_order

    content = SKELETON.format(
        name=args.name,
        description=args.description.strip(),
        reviewer_kind=args.reviewer_kind,
        reviewer_scope=args.reviewer_scope,
        thinking_level=args.thinking_level,
        complexity=args.complexity,
        default_in_cycle=args.default_in_cycle,
        cycle_order_line=cycle_order_line,
        title=title_case(args.name),
    )

    for tree in (tree_a, tree_b):
        dest_dir = os.path.join(tree, "reviewers", args.name)
        os.makedirs(dest_dir)
        dest_file = os.path.join(dest_dir, "SKILL.md")
        with open(dest_file, "w", encoding="utf-8") as f:
            f.write(content)
        print("wrote", dest_file)

    if args.default_in_cycle == "true":
        shifted = []
        for tree in (tree_a, tree_b):
            list_reviewers_py = os.path.join(tree, "chapter-cycle", "scripts", "list_reviewers.py")
            for r in load_cycle_json(list_reviewers_py):
                if r.get("name") == args.name:
                    continue
                if r.get("default-in-cycle") and r.get("cycle-order") is not None and r["cycle-order"] >= args.cycle_order:
                    path = os.path.join(tree, "reviewers", r["name"], "SKILL.md")
                    if shift_cycle_order(path, args.cycle_order):
                        shifted.append(path)
        if shifted:
            print("shifted cycle-order +1 for:")
            for p in shifted:
                print(" ", p)

    diff_script = os.path.join(tree_a, "sync-skills", "scripts", "diff_skill_dirs.py")
    print()
    print("Next: fill in the body sections in both new SKILL.md files (they're")
    print("identical right now -- write the content once, then copy it over the")
    print("other rather than retyping it) per reviewers/TEMPLATE.md, then verify:")
    print("  python3 %s \\" % diff_script)
    print("      --a %s --b %s --single" % (
        os.path.join(tree_a, "reviewers", args.name), os.path.join(tree_b, "reviewers", args.name)))
    return 0


if __name__ == "__main__":
    sys.exit(main())
