#!/usr/bin/env python3
"""Apply exact-match diffs to a chapter file. Refuses to guess.

Rewriting a whole chapter to land a handful of review fixes is both wasteful and
a reliable source of regressions — in the run this was built for, three
already-fixed problems came back inside rewritten material. This applies edits as anchored
replacements, and fails loudly rather than silently doing the wrong one.

Patch format (repeat the block as many times as needed):

    --- PATCH: short label ---
    <<<<<<< OLD
    exact text currently in the file
    =======
    replacement text
    >>>>>>> NEW

Rules enforced:
  * every OLD must appear EXACTLY ONCE in the file (zero or many => abort)
  * nothing is written unless every patch validates
  * --check validates without writing
  * a .bak copy is kept next to the file

Usage:
    python3 apply_patches.py --file chapter.md --patch round1.patch
    python3 apply_patches.py --file chapter.md --patch round1.patch --check
"""

import argparse
import os
import re
import shutil
import sys

HEADER = re.compile(r"^---\s*PATCH:?\s*(.*?)\s*---\s*$")
OLD_OPEN = "<<<<<<< OLD"
SEP = "======="
NEW_CLOSE = ">>>>>>> NEW"


def parse(text):
    """Return [(label, old, new)] in file order."""
    patches = []
    label = None
    lines = text.splitlines()
    i, n = 0, len(lines)

    while i < n:
        line = lines[i]
        m = HEADER.match(line)
        if m:
            label = m.group(1) or "unlabelled"
            i += 1
            continue

        if line.rstrip() == OLD_OPEN:
            i += 1
            old = []
            while i < n and lines[i].rstrip() != SEP:
                old.append(lines[i])
                i += 1
            if i >= n:
                raise ValueError("patch %r: missing '%s' separator" % (label, SEP))
            i += 1
            new = []
            while i < n and lines[i].rstrip() != NEW_CLOSE:
                new.append(lines[i])
                i += 1
            if i >= n:
                raise ValueError("patch %r: missing '%s' terminator" % (label, NEW_CLOSE))
            i += 1
            patches.append((label or "unlabelled", "\n".join(old), "\n".join(new)))
            label = None
            continue

        i += 1

    if not patches:
        raise ValueError("no patch blocks found — check the delimiters")
    return patches


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--file", required=True, help="chapter file to edit in place")
    ap.add_argument("--patch", required=True, help="patch file")
    ap.add_argument("--check", action="store_true", help="validate only, write nothing")
    args = ap.parse_args()

    if not os.path.isfile(args.file):
        sys.exit("ERROR: no such file: %s" % args.file)

    with open(args.file, encoding="utf-8") as fh:
        text = fh.read()
    with open(args.patch, encoding="utf-8") as fh:
        patch_text = fh.read()

    try:
        patches = parse(patch_text)
    except ValueError as exc:
        sys.exit("ERROR: %s" % exc)

    # Validate everything before touching anything.
    problems = []
    working = text
    for idx, (label, old, new) in enumerate(patches, 1):
        if not old.strip():
            problems.append("%d. %s: OLD block is empty" % (idx, label))
            continue
        count = working.count(old)
        if count == 0:
            problems.append(
                "%d. %s: OLD not found.\n     first line: %r" % (idx, label, old.splitlines()[0][:100]))
        elif count > 1:
            problems.append(
                "%d. %s: OLD appears %d times — add surrounding context to make it unique.\n"
                "     first line: %r" % (idx, label, count, old.splitlines()[0][:100]))
        else:
            working = working.replace(old, new, 1)

    if problems:
        sys.stderr.write("Refusing to write. %d of %d patches failed:\n\n"
                         % (len(problems), len(patches)))
        sys.stderr.write("\n".join(problems) + "\n\n")
        sys.stderr.write("Fix the patch file. Do NOT rewrite the chapter to work around this.\n")
        sys.exit(1)

    words_before = len(text.split())
    words_after = len(working.split())

    if args.check:
        print("OK (check only): %d/%d patches would apply cleanly." % (len(patches), len(patches)))
        print("   words %d -> %d (%+d)" % (words_before, words_after, words_after - words_before))
        return

    shutil.copyfile(args.file, args.file + ".bak")
    with open(args.file, "w", encoding="utf-8") as fh:
        fh.write(working)

    print("Applied %d/%d patches to %s" % (len(patches), len(patches), args.file))
    print("   backup: %s.bak" % args.file)
    print("   words %d -> %d (%+d)" % (words_before, words_after, words_after - words_before))
    for idx, (label, _o, _n) in enumerate(patches, 1):
        print("   %2d. %s" % (idx, label))


if __name__ == "__main__":
    main()
