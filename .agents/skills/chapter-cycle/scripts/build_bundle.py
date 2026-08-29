#!/usr/bin/env python3
"""Assemble a single self-contained review bundle for one {{NOVEL_TITLE}} chapter.

The point: reviewer subagents should read ONE file, not explore the vault.
On Chapter 7 a reviewer spent 23 Read calls and 48 turns discovering which
codex files mattered; that discovery is deterministic and belongs here.

Usage:
    python3 build_bundle.py --vault /mnt/user-data/uploads/{{NOVEL_TITLE}} \
        --arc 1 --chapter 7 --out /tmp/chapter-cycle/bundle.md
"""

import argparse
import os
import re
import sys

TAIL_WORDS = 900          # closing prose of the previous chapter to include
MAX_CODEX_CHARS = 9000    # per codex entry; the big backstory notes otherwise
                          # swallow the bundle (Jordan.md alone is ~23k chars)


def die(msg):
    sys.stderr.write("ERROR: %s\n" % msg)
    sys.exit(1)


def read(path):
    with open(path, encoding="utf-8") as fh:
        return fh.read()


def find_chapter_dir(vault, arc, chapter):
    arc_dir = os.path.join(vault, "novel", "arc %d" % arc)
    if not os.path.isdir(arc_dir):
        die("no such arc directory: %s" % arc_dir)
    prefix = "Chapter %d - " % chapter
    for name in sorted(os.listdir(arc_dir)):
        if name.startswith(prefix) and os.path.isdir(os.path.join(arc_dir, name)):
            return os.path.join(arc_dir, name)
    die("no folder named '%s...' in %s" % (prefix, arc_dir))


def prev_chapter_dir(vault, arc, chapter):
    """Previous chapter folder, or Chapter 0 - Prologue when chapter == 1."""
    arc_dir = os.path.join(vault, "novel", "arc %d" % arc)
    if chapter <= 1:
        p = os.path.join(arc_dir, "Chapter 0 - Prologue")
        return p if os.path.isdir(p) else None
    prefix = "Chapter %d - " % (chapter - 1)
    for name in sorted(os.listdir(arc_dir)):
        if name.startswith(prefix) and os.path.isdir(os.path.join(arc_dir, name)):
            return os.path.join(arc_dir, name)
    return None


def chapter_prose_path(folder):
    """The chapter file itself — same name as its folder."""
    candidate = os.path.join(folder, os.path.basename(folder) + ".md")
    if os.path.isfile(candidate):
        return candidate
    for name in sorted(os.listdir(folder)):
        if name.endswith(".md") and name not in ("Summary.md", "Outline.md"):
            return os.path.join(folder, name)
    return None


def frontmatter_aliases(text):
    """`aliases:` entries, inline-list or block-list form."""
    if not text.startswith("---"):
        return []
    end = text.find("\n---", 3)
    if end == -1:
        return []
    head = text[3:end]
    m = re.search(r"^aliases:(.*?)(?=^\S|\Z)", head, re.MULTILINE | re.DOTALL)
    if not m:
        return []
    body = m.group(1)
    out = []
    for item in re.findall(r"-\s*(.+)", body):          # block list
        out.append(item.strip().strip("\"'"))
    inline = re.search(r"\[(.*?)\]", body, re.DOTALL)   # inline list
    if inline:
        out.extend(p.strip().strip("\"'") for p in inline.group(1).split(","))
    return [o for o in out if o]


def index_codex(vault):
    """Map lowercased note stem -> path, for every .md under codex/.

    Also indexes each note's frontmatter `aliases:`, so a link like
    [[Riley's Species]] resolves to the note that actually holds it. Real
    filenames always win over an alias.
    """
    idx, alias = {}, {}
    codex = os.path.join(vault, "codex")
    for root, _dirs, files in os.walk(codex):
        for f in files:
            if not f.endswith(".md"):
                continue
            path = os.path.join(root, f)
            idx.setdefault(os.path.splitext(f)[0].lower(), path)
            try:
                for a in frontmatter_aliases(read(path)):
                    alias.setdefault(a.lower(), path)
            except OSError:
                pass
    for key, path in alias.items():
        idx.setdefault(key, path)
    return idx


def wikilinks(text):
    """Ordered, de-duplicated [[targets]], with any |alias and #anchor stripped."""
    out = []
    for raw in re.findall(r"\[\[([^\]]+)\]\]", text):
        target = raw.split("|")[0].split("#")[0].strip()
        target = target.rstrip("/")
        if target and target not in out:
            out.append(target)
    return out


def tail_words(text, n):
    words = text.split()
    return text if len(words) <= n else " ".join(words[-n:])


def frontmatter_entities(text):
    """Wikilinked names out of the chapter frontmatter's pov/characters/locations.

    The outline links chapters and threads, but rarely the characters themselves
    — so relying on outline wikilinks alone silently drops the POV voice files,
    which are the single most important thing a prose reviewer needs.
    """
    if not text.startswith("---"):
        return []
    end = text.find("\n---", 3)
    if end == -1:
        return []
    head = text[3:end]
    names = []
    for key in ("pov", "characters", "locations"):
        for block in re.findall(r"^%s:(.*?)(?=^\S|\Z)" % key, head,
                                re.MULTILINE | re.DOTALL):
            for raw in re.findall(r"\[\[([^\]]+)\]\]", block):
                target = raw.split("|")[0].split("#")[0].strip()
                if target and target not in names:
                    names.append(target)
    return names


def section(title, body):
    return "\n\n## %s\n\n%s\n" % (title, body.strip())


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--vault", required=True, help="vault root (staged copy)")
    ap.add_argument("--arc", type=int, default=1)
    ap.add_argument("--chapter", type=int, required=True)
    ap.add_argument("--out", required=True)
    args = ap.parse_args()

    vault = os.path.abspath(args.vault)
    folder = find_chapter_dir(vault, args.arc, args.chapter)
    title = os.path.basename(folder)

    outline_path = os.path.join(folder, "Outline.md")
    if not os.path.isfile(outline_path):
        die("no Outline.md in %s — run add-chapter first" % folder)
    outline = read(outline_path)

    parts = [
        "# Review bundle — %s" % title,
        "",
        "Everything a reviewer needs, in one file. Do not open other vault files;",
        "if something you need is missing, say so in your report instead of going",
        "to look for it.",
    ]

    parts.append(section("Outline (the plan — the chapter is judged against this)", outline))

    planned = os.path.join(folder, "Summary.md")
    if os.path.isfile(planned):
        parts.append(section("Planned summary", read(planned)))

    # --- governing project context --------------------------------------
    for rel, label in (("AGENTS.md", "Project instructions (routing and authority)"),
                       ("codex/00 Index.md", "Current manuscript state and open threads"),
                       ("codex/Genre.md", "Genre"),
                       ("codex/Writing Style.md", "Writing Style (book-wide rules)"),
                       ("codex/Editing Workflow.md", "Editing workflow")):
        p = os.path.join(vault, rel)
        if os.path.isfile(p):
            parts.append(section(label, read(p)))

    # --- previous chapter continuity ------------------------------------
    prev = prev_chapter_dir(vault, args.arc, args.chapter)
    if prev:
        prev_name = os.path.basename(prev)
        ps = os.path.join(prev, "Summary.md")
        if os.path.isfile(ps):
            parts.append(section("Previous chapter — %s — summary" % prev_name, read(ps)))
        pp = chapter_prose_path(prev)
        if pp:
            parts.append(section(
                "Previous chapter — %s — closing ~%d words (physical handoff)"
                % (prev_name, TAIL_WORDS),
                tail_words(read(pp), TAIL_WORDS)))

    # --- codex entries referenced by the outline AND the frontmatter -------
    idx = index_codex(vault)
    wanted = []
    chapter_file = chapter_prose_path(folder)
    if chapter_file:
        wanted.extend(frontmatter_entities(read(chapter_file)))
    for name in wikilinks(outline):
        if name not in wanted:
            wanted.append(name)

    # Every referenced character's voice file, whether or not it was linked.
    for name in list(wanted):
        voice = "%s - Voice" % name
        if voice.lower() in idx and voice not in wanted:
            wanted.append(voice)

    # Already their own sections above; don't duplicate them.
    already = {"genre", "writing style", title.lower()}

    included, missing = [], []
    seen_rel = set()
    for name in wanted:
        if name.lower() in already:
            continue
        path = idx.get(name.lower())
        if not path:
            # A [[Chapter N - Title]] link points into novel/, not codex/.
            # Its Summary.md is the useful thing, not a missing codex note.
            summary = os.path.join(vault, "novel", "arc %d" % args.arc, name, "Summary.md")
            if os.path.isfile(summary):
                path = summary
            else:
                missing.append(name)
                continue
        rel = os.path.relpath(path, vault).replace(os.sep, "/")
        if rel in seen_rel:
            continue
        seen_rel.add(rel)
        body = read(path)
        if len(body) > MAX_CODEX_CHARS:
            body = (body[:MAX_CODEX_CHARS]
                    + "\n\n*[truncated at %d chars — flag it in your report if a "
                      "finding depends on the rest]*" % MAX_CODEX_CHARS)
        included.append((rel, body))

    if included:
        chunks = ["### %s\n\n%s" % (rel, body.strip()) for rel, body in included]
        parts.append(section("Codex entries referenced by the outline",
                             "\n\n---\n\n".join(chunks)))

    if missing:
        parts.append(section(
            "Referenced but not available",
            "These were linked but could not be resolved. Either they are entities "
            "this chapter introduces (no note exists yet — expected), or the file "
            "was never staged (a gap: say so in your report rather than guessing).\n\n"
            + "\n".join("- %s" % m for m in missing)))

    os.makedirs(os.path.dirname(os.path.abspath(args.out)) or ".", exist_ok=True)
    text = "\n".join(parts).rstrip() + "\n"
    with open(args.out, "w", encoding="utf-8") as fh:
        fh.write(text)

    print("Bundle written: %s" % args.out)
    print("  chapter folder : %s" % folder)
    print("  codex entries  : %d included, %d unresolved" % (len(included), len(missing)))
    print("  size           : %d chars (~%d tokens)" % (len(text), len(text) // 4))
    if missing:
        print("  unresolved     : %s" % ", ".join(missing))


if __name__ == "__main__":
    main()
