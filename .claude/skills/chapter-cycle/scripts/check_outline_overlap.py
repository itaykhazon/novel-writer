#!/usr/bin/env python3
"""Report wording the chapter shares with its own outline.

The failure this catches: an outline whose beat lines are written as polished
sentences turns drafting into transcription, and the chapter's quality is
capped at the outline's. The tell is long runs of identical wording between the
two files — and the runs are usually *narration*, which means the best phrasing
in the chapter was chosen at planning time, by someone thinking about structure,
before anyone knew what the scene would feel like.

The outline's job is to lock function and outcome. Sentences are written on the
page. Some wording is meant to land verbatim, though — an oath, an in-fiction
system readout, a recurring line, the exact description of a planted object that
has to match its first appearance. Those go under a `## Verbatim anchors`
heading in the outline, one per line, and are exempted here. Only the anchor's
own span is deducted: a run that merely sits next to an anchor is still judged,
so padding an anchor can't launder the text around it.

This reports evidence, never a verdict. Identical wording is not automatically
bad and the script cannot read context — a proper noun, a stock phrase, or a
beat line that was always going to be the plainest way to say something will all
show up here. Read each hit and decide. What it is good for is the shape of the
result: several long non-anchor runs means the chapter was expanded rather than
written, and the fix is to rewrite those passages from the scene, not to reword
them until this script goes quiet.

Usage:
    python3 check_outline_overlap.py --chapter <path/to/Chapter N - Title.md>
    python3 check_outline_overlap.py --chapter <chapter.md> --outline <Outline.md>
    python3 check_outline_overlap.py --chapter <chapter.md> --min-run 9 --json

Exit codes: 0 = clean (or outline not found); 1 = non-anchor overlap to review.
"""

from __future__ import annotations

import argparse
import json
import os
import re
import sys

DEFAULT_MIN_RUN = 7      # words; below this, English collocations dominate
MAX_REPORTED = 12
CONTEXT_CHARS = 90

FRONTMATTER = re.compile(r"\A---\n.*?\n---\n", re.S)
WORD = re.compile(r"[a-z0-9']+")


def strip_frontmatter(text: str) -> str:
    return FRONTMATTER.sub("", text, count=1)


def tokenize(text: str) -> tuple[list[str], list[int]]:
    """Lowercase word tokens plus each token's character offset in `text`.

    Markdown emphasis, headings and list markers are punctuation to the word
    regex, so they fall out without a separate stripping pass. Curly and
    straight apostrophes are folded so "didn't" matches "didn’t".
    """
    flat = text.replace("’", "'").lower()
    tokens, offsets = [], []
    for match in WORD.finditer(flat):
        tokens.append(match.group(0))
        offsets.append(match.start())
    return tokens, offsets


def read_anchors(outline_text: str) -> list[list[str]]:
    """Token sequences from the outline's `## Verbatim anchors` section."""
    match = re.search(
        r"^#{1,6}\s*Verbatim anchors\s*$(.*?)(?=^#{1,6}\s|\Z)",
        outline_text,
        re.M | re.S,
    )
    if not match:
        return []
    anchors = []
    for line in match.group(1).splitlines():
        line = re.sub(r"^\s*(?:[-*+]|\d+[.)])\s*", "", line).strip().strip('"“”')
        if not line:
            continue
        tokens, _ = tokenize(line)
        if tokens:
            anchors.append(tokens)
    return anchors


def find_sequence(haystack: list[str], needle: list[str]) -> list[tuple[int, int]]:
    """Every [start, end) span where `needle` occurs in `haystack`."""
    spans, n = [], len(needle)
    if not n or n > len(haystack):
        return spans
    for i in range(len(haystack) - n + 1):
        if haystack[i:i + n] == needle:
            spans.append((i, i + n))
    return spans


def shared_runs(prose: list[str], outline: list[str], min_run: int) -> list[tuple[int, int]]:
    """Maximal runs of prose that appear verbatim in the outline.

    Indexes the outline's min_run-grams once, then walks the prose extending
    each hit as far as it goes. Linear in the prose; the greedy extension can't
    miss a longer run because any longer run starts with a matching n-gram.
    """
    if len(outline) < min_run or len(prose) < min_run:
        return []

    index: dict[tuple[str, ...], list[int]] = {}
    for i in range(len(outline) - min_run + 1):
        index.setdefault(tuple(outline[i:i + min_run]), []).append(i)

    runs, i = [], 0
    while i <= len(prose) - min_run:
        starts = index.get(tuple(prose[i:i + min_run]))
        if not starts:
            i += 1
            continue
        best = min_run
        for start in starts:
            length = min_run
            while (
                i + length < len(prose)
                and start + length < len(outline)
                and prose[i + length] == outline[start + length]
            ):
                length += 1
            best = max(best, length)
        runs.append((i, i + best))
        i += best
    return runs


def subtract(span: tuple[int, int], exempt: set[int], min_run: int) -> list[tuple[int, int]]:
    """Split a run around exempt indices, keeping surviving pieces >= min_run."""
    pieces, start = [], None
    for i in range(span[0], span[1]):
        if i in exempt:
            if start is not None and i - start >= min_run:
                pieces.append((start, i))
            start = None
        elif start is None:
            start = i
    if start is not None and span[1] - start >= min_run:
        pieces.append((start, span[1]))
    return pieces


def locate(text: str, offset: int) -> int:
    return text.count("\n", 0, offset) + 1


def find_outline(chapter_path: str) -> str | None:
    candidate = os.path.join(os.path.dirname(chapter_path), "Outline.md")
    return candidate if os.path.isfile(candidate) else None


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__.split("\n\n")[0])
    parser.add_argument("--chapter", required=True)
    parser.add_argument("--outline", help="defaults to Outline.md beside the chapter")
    parser.add_argument("--min-run", type=int, default=DEFAULT_MIN_RUN)
    parser.add_argument("--json", action="store_true")
    args = parser.parse_args()

    if args.min_run < 3:
        sys.stderr.write("--min-run below 3 reports noise, not overlap\n")
        return 2

    try:
        with open(args.chapter, encoding="utf-8") as handle:
            chapter_raw = handle.read()
    except OSError as exc:
        sys.stderr.write(f"ERROR: {exc}\n")
        return 2

    outline_path = args.outline or find_outline(args.chapter)
    if not outline_path or not os.path.isfile(outline_path):
        # Not an error: a chapter can legitimately have no outline beside it.
        # Say so rather than exiting 0 silently, which reads as "checked, clean".
        print("no outline found beside the chapter — nothing to compare")
        return 0

    with open(outline_path, encoding="utf-8") as handle:
        outline_raw = handle.read()

    chapter_body = strip_frontmatter(chapter_raw)
    # Line numbers must address the real file, not the frontmatter-stripped body,
    # or every reported line is off by the length of the frontmatter block.
    frontmatter_lines = chapter_raw[:len(chapter_raw) - len(chapter_body)].count("\n")
    prose, prose_offsets = tokenize(chapter_body)
    outline_tokens, _ = tokenize(strip_frontmatter(outline_raw))

    exempt: set[int] = set()
    anchors = read_anchors(outline_raw)
    for anchor in anchors:
        for start, end in find_sequence(prose, anchor):
            exempt.update(range(start, end))

    findings = []
    for run in shared_runs(prose, outline_tokens, args.min_run):
        for start, end in subtract(run, exempt, args.min_run):
            offset = prose_offsets[start]
            findings.append({
                "words": end - start,
                "line": locate(chapter_body, offset) + frontmatter_lines,
                "text": " ".join(prose[start:end]),
                "context": chapter_body[max(0, offset - 20):offset + CONTEXT_CHARS].replace("\n", " ").strip(),
            })
    findings.sort(key=lambda f: -f["words"])

    overlapped = sum(f["words"] for f in findings)
    summary = {
        "chapter_words": len(prose),
        "anchors_declared": len(anchors),
        "anchor_words_exempted": len(exempt),
        "overlap_runs": len(findings),
        "overlap_words": overlapped,
        "overlap_pct": round(overlapped * 100 / len(prose), 2) if prose else 0.0,
        "longest_run": findings[0]["words"] if findings else 0,
        "min_run": args.min_run,
    }

    if args.json:
        print(json.dumps({"summary": summary, "findings": findings}, indent=2))
        return 1 if findings else 0

    if not findings:
        print(
            f"clean — no non-anchor run of {args.min_run}+ words shared with the outline "
            f"({summary['anchors_declared']} anchors declared, "
            f"{summary['anchor_words_exempted']} words exempted)"
        )
        return 0

    print(
        f"{len(findings)} shared run(s) with {os.path.basename(outline_path)} — "
        f"{overlapped} words, {summary['overlap_pct']}% of the chapter, "
        f"longest {summary['longest_run']}\n"
    )
    for finding in findings[:MAX_REPORTED]:
        print(f"  line {finding['line']}  ({finding['words']} words)")
        print(f"    …{finding['context']}…\n")
    if len(findings) > MAX_REPORTED:
        print(f"  … and {len(findings) - MAX_REPORTED} more\n")
    print(
        "Read each in context. A proper noun or the plainest available phrasing is\n"
        "fine; narration reused wholesale is the chapter being transcribed. Rewrite\n"
        "those passages from the scene — don't reword them until this goes quiet.\n"
        "Wording that must land verbatim belongs under the outline's\n"
        "`## Verbatim anchors` heading."
    )
    return 1


if __name__ == "__main__":
    sys.exit(main())
