#!/usr/bin/env python3
"""Find wikilinks in the vault that don't resolve to anything, and (with
--orphans) notes that nothing links to at all.

A dangling link is invisible in Obsidian but silently degrades the review
bundle: build_bundle.py can't include a note that doesn't exist, so the reviewer
is missing context nobody realises is missing. Run this after any session that
adds codex entries.

Resolution order, matching build_bundle.py:
  1. a note filename anywhere in the vault
  2. a frontmatter `aliases:` entry on some note
  3. a chapter folder under novel/arc <N>/ (including Chapter 0 - Prologue)

`templates/` is skipped — its [[Character]] / [[Chapter X]] placeholders are
meant to be unresolved.

An orphan is a different problem: the note resolves fine, but no other note
links to it, so it's invisible in Obsidian's backlink graph even though it's
discoverable by folder. The 2026-08-15 "Story So Far" audit found three
drafted chapters' Outline.md files in exactly this state — harmless if that's
an intentional convention (drafted outlines are archival), but worth seeing
explicitly rather than only via a manual whole-vault read. --orphans never
exits non-zero: an orphan isn't automatically wrong the way a dangling link
is, it's a fact to judge, not an error to fix.

Usage:
    python3 audit_links.py --vault /mnt/user-data/uploads/{{NOVEL_TITLE}}
    python3 audit_links.py --vault ... --strict     # exit 1 if anything dangles
    python3 audit_links.py --vault ... --orphans    # also list zero-inbound notes
"""

import argparse
import collections
import os
import re
import sys

SKIP_DIR_NAMES = {".agents", ".claude", ".git", "_to_delete", "reviews", "templates"}


def prune_skipped_dirs(dirs):
    """Prevent os.walk from entering non-vault-note and placeholder trees."""
    dirs[:] = [d for d in dirs if d not in SKIP_DIR_NAMES]


def frontmatter_aliases(text):
    if not text.startswith("---"):
        return []
    end = text.find("\n---", 3)
    if end == -1:
        return []
    m = re.search(r"^aliases:(.*?)(?=^\S|\Z)", text[3:end], re.MULTILINE | re.DOTALL)
    if not m:
        return []
    body = m.group(1)
    out = [x.strip().strip("\"'") for x in re.findall(r"-\s*(.+)", body)]
    inline = re.search(r"\[(.*?)\]", body, re.DOTALL)
    if inline:
        out += [p.strip().strip("\"'") for p in inline.group(1).split(",")]
    return [o for o in out if o]


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--vault", required=True)
    ap.add_argument("--strict", action="store_true",
                    help="exit 1 if any link dangles (for a pre-commit check)")
    ap.add_argument("--orphans", action="store_true",
                    help="also report notes with zero inbound wikilinks")
    args = ap.parse_args()
    vault = os.path.abspath(args.vault)

    names, aliases = {}, {}
    all_notes = {}  # lowercased stem -> rel path, for orphan reporting
    for root, dirs, files in os.walk(vault):
        prune_skipped_dirs(dirs)
        for f in files:
            if not f.endswith(".md"):
                continue
            path = os.path.join(root, f)
            names.setdefault(os.path.splitext(f)[0].lower(), path)
            rel = os.path.relpath(path, vault).replace(os.sep, "/")
            all_notes[rel] = path
            try:
                for a in frontmatter_aliases(open(path, encoding="utf-8").read()):
                    aliases.setdefault(a.lower(), path)
            except OSError:
                pass

    folders = set()
    novel = os.path.join(vault, "novel")
    if os.path.isdir(novel):
        for arc in os.listdir(novel):
            arc_path = os.path.join(novel, arc)
            if os.path.isdir(arc_path):
                for n in os.listdir(arc_path):
                    if os.path.isdir(os.path.join(arc_path, n)):
                        folders.add(n.lower())

    dangling = collections.defaultdict(set)
    inbound = collections.defaultdict(set)  # resolved target path -> set of rel sources
    scanned = 0
    for root, dirs, files in os.walk(vault):
        prune_skipped_dirs(dirs)
        for f in files:
            if not f.endswith(".md"):
                continue
            path = os.path.join(root, f)
            rel = os.path.relpath(path, vault).replace(os.sep, "/")
            scanned += 1
            for raw in re.findall(r"\[\[([^\]]+)\]\]",
                                  open(path, encoding="utf-8").read()):
                tgt = raw.split("|")[0].split("#")[0].strip().rstrip("/")
                if not tgt:
                    continue
                low = tgt.lower()
                resolved = names.get(low) or aliases.get(low)
                if resolved:
                    resolved_rel = os.path.relpath(resolved, vault).replace(os.sep, "/")
                    if resolved_rel != rel:  # a note linking itself doesn't count
                        inbound[resolved_rel].add(rel)
                    continue
                if low in folders or low.split("/")[0] in folders:
                    continue
                dangling[tgt].add(rel)

    print("Scanned %d notes — %d names, %d aliases, %d chapter folders."
          % (scanned, len(names), len(aliases), len(folders)))

    if not dangling:
        print("No dangling wikilinks. The review bundle can resolve everything.")
    else:
        print("\n%d dangling link target(s):\n" % len(dangling))
        for tgt in sorted(dangling, key=lambda x: (-len(dangling[x]), x)):
            srcs = sorted(dangling[tgt])
            print("  [[%s]]  — referenced by %d note(s)" % (tgt, len(srcs)))
            for s in srcs[:5]:
                print("        %s" % s)
            if len(srcs) > 5:
                print("        ... +%d more" % (len(srcs) - 5))
        print("\nFix by creating the note, adding the name to an existing note's")
        print("`aliases:` frontmatter, or removing the brackets if it isn't an entity.")

    if args.orphans:
        # Notes with zero inbound wikilinks. Index/template/summary-of-self
        # scaffolding is expected to be link-light, so this is informational,
        # not an error — judge each one rather than "fixing" the count to zero.
        orphans = sorted(rel for rel in all_notes if rel not in inbound)
        print("\n%d note(s) with zero inbound wikilinks:\n" % len(orphans))
        for rel in orphans:
            print("  %s" % rel)
        if orphans:
            print("\nHarmless if these are intentionally archival or are index/root")
            print("files nothing is expected to link back to. Otherwise, consider")
            print("adding an inbound link (e.g. from the arc index) so they're")
            print("reachable from Obsidian's backlink graph, not just by folder.")

    if args.strict and dangling:
        sys.exit(1)


if __name__ == "__main__":
    main()
