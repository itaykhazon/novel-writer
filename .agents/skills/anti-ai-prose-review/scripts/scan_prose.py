#!/usr/bin/env python3
"""Surface candidate AI-shaped prose patterns without inferring authorship."""

from __future__ import annotations

import argparse
import bisect
import json
import math
import re
import sys
from collections import Counter
from dataclasses import dataclass
from pathlib import Path


@dataclass(frozen=True)
class Pattern:
    category: str
    name: str
    regex: str
    evidence: str


PATTERNS = [
    Pattern("contrastive_scaffolding", "not just/only X but Y", r"\bnot\s+(?:just|only|merely)\b[^.!?\n]{1,140}?\bbut(?:\s+also)?\b", "corpus"),
    Pattern("contrastive_scaffolding", "subject was not X. Subject was Y", r"\b(?:it|this|that|he|she|they)(?:['’]s\s+not|\s+(?:isn['’]t|wasn['’]t|weren['’]t|aren['’]t|is\s+not|was\s+not|were\s+not|are\s+not))\b[^.!?\n]{1,100}?[.!?][ \t]*(?:it|this|that|he|she|they)(?:['’]s|\s+(?:is|was|were|are))\b", "corpus"),
    Pattern("contrastive_scaffolding", "subject was not just X--subject was Y", r"\b(?:it|this|that|he|she|they)(?:['’]s\s+not|\s+(?:isn['’]t|wasn['’]t|weren['’]t|aren['’]t|is\s+not|was\s+not|were\s+not|are\s+not))\s+(?:just|only|merely)\b[^.!?\n]{1,100}?[;:—–-]{1,2}[ \t]*(?:it|this|that|he|she|they)(?:['’]s|\s+(?:is|was|were|are))\b", "corpus"),
    Pattern("contrastive_scaffolding", "no X, no Y, just Z", r"\bno\b[^.!?\n]{1,50}?,\s*no\b[^.!?\n]{1,50}?,\s*just\b", "corpus"),
    Pattern("contrastive_scaffolding", "not because X but because Y", r"\bnot\s+because\b[^.!?\n]{1,120}?\bbut\s+because\b", "field"),
    Pattern("stock_fiction", "voice barely above a whisper", r"\bvoice\s+(?:was\s+)?barely\s+above\s+a\s+whisper\b", "corpus"),
    Pattern("stock_fiction", "eyes never leaving", r"\beyes\s+never\s+leaving\b", "corpus"),
    Pattern("stock_fiction", "heart hammered/pounded against ribs", r"\bheart\s+(?:hammered|pounded|thudded)\b[^.!?\n]{0,35}?\bribs\b", "corpus"),
    Pattern("stock_fiction", "voice trembling slightly", r"\bvoice\s+trembl(?:ed|ing)\s+slightly\b", "corpus"),
    Pattern("stock_fiction", "voice devoid of emotion", r"\bvoice\s+(?:was\s+)?devoid\s+of\b", "corpus"),
    Pattern("stock_fiction", "profound sense", r"\b(?:felt|with)\s+(?:a\s+)?profound\s+sense\s+of\b", "corpus"),
    Pattern("stock_fiction", "something flickered/flashed", r"\bsomething\s+(?:flickered|flashed|shifted|stirred|broke|passed)\b", "field"),
    Pattern("stock_fiction", "emotion crossed features", r"\b(?:a\s+)?flicker\s+of\s+\w+\s+(?:crossed|passed\s+over|flashed\s+across)\b", "field"),
    Pattern("stock_fiction", "breath hitch/unknown held breath", r"\b(?:breath\s+hitched|(?:released|let\s+out)\s+a\s+breath\s+(?:he|she|they)\s+didn['’]t\s+know\s+(?:he|she|they)(?:['’]d|\s+had)\s+been\s+holding)\b", "field"),
    Pattern("stock_fiction", "silence stretched/hung/pressed", r"\b(?:the\s+)?silence\s+(?:stretched|hung|pressed|settled|wrapped|fell)\b", "field"),
    Pattern("stock_fiction", "air crackled", r"\b(?:the\s+)?air\s+crackled\s+with\b", "field"),
    Pattern("stock_fiction", "wave of emotion washed over", r"\ba\s+wave\s+of\s+\w+\s+washed\s+over\b", "field"),
    Pattern("stock_fiction", "weight settled", r"\bthe\s+weight\s+of\b[^.!?\n]{1,60}?\bsettled\b", "field"),
    Pattern("stock_fiction", "world stopped/slowed/fell away", r"\bthe\s+world\s+(?:seemed\s+to\s+)?(?:stop|stopped|slow|slowed|fall|fell)\s*(?:away)?\b", "field"),
    Pattern("vague_pseudo_specificity", "something about/in", r"\bsomething\s+(?:about\s+the\s+way|in\s+(?:his|her|their)\s+(?:voice|expression|gaze|eyes))\b", "field"),
    Pattern("vague_pseudo_specificity", "something could not name", r"\bsomething\s+(?:he|she|they)\s+couldn['’]t\s+name\b", "field"),
    Pattern("vague_pseudo_specificity", "the kind of X that", r"\bthe\s+kind\s+of\b[^.!?\n]{1,70}?\bthat\b", "field"),
    Pattern("vague_pseudo_specificity", "almost/not quite cue", r"\b(?:almost\s+(?:as\s+if|like|a\s+(?:smile|laugh|confession|apology))|not\s+quite\s+(?:a\s+)?(?:smile|laugh|anger|relief|hope|truth))\b", "field"),
    Pattern("vague_pseudo_specificity", "somehow profundity", r"\b(?:and\s+)?somehow(?:,|\s+that\s+(?:was|made\s+it))\b", "field"),
    Pattern("hedging_filler", "seemed/appeared to", r"\b(?:seemed|appeared)\s+to\b", "field"),
    Pattern("hedging_filler", "could not help but", r"\bcouldn['’]t\s+help\s+but\b", "field"),
    Pattern("hedging_filler", "found self", r"\bfound\s+(?:himself|herself|themselves)\b", "field"),
    Pattern("hedging_filler", "without thinking/realizing", r"\bwithout\s+(?:thinking|meaning\s+to|realizing)\b", "field"),
    Pattern("hedging_filler", "began/started to", r"\b(?:began|started)\s+to\b", "field"),
    Pattern("explained_subtext", "what they really meant", r"\bwhat\s+(?:he|she|they)\s+really\s+meant\s+was\b", "field"),
    Pattern("explained_subtext", "they both knew", r"\band\s+they\s+both\s+knew\b", "field"),
    Pattern("explained_subtext", "words hung/landed", r"\bthe\s+words\s+(?:hung|landed|cut)\b", "field"),
    Pattern("canned_signpost", "one thing was clear/certain", r"\bone\s+thing\s+was\s+(?:clear|certain)\b", "field"),
    Pattern("canned_signpost", "and with that", r"\band\s+with\s+that\b", "field"),
    Pattern("canned_signpost", "as if on cue", r"\bas\s+if\s+on\s+cue\b", "field"),
    Pattern("canned_signpost", "served as reminder/testament", r"\bserved\s+as\s+(?:a\s+)?(?:powerful\s+)?(?:reminder|testament)\b", "field"),
    Pattern("canned_signpost", "set the stage", r"\bset(?:ting)?\s+the\s+stage\s+for\b", "field"),
    Pattern("dramatic_landing", "that was the point/difference/enough", r"\b(?:and\s+)?(?:somehow,?\s*)?that\s+was\s+(?:the\s+(?:point|difference|truth(?:\s+of\s+it)?|whole\s+of\s+it)|enough|worse|better|all)\b", "field"),
    Pattern("dramatic_landing", "everything changed/would never be the same", r"\b(?:that\s+was\s+when\s+everything\s+changed|(?:nothing|things?)\s+would\s+(?:ever\s+)?be\s+the\s+same)\b", "field"),
    Pattern("dramatic_landing", "did not know it yet", r"\b(?:he|she|they)\s+(?:didn['’]t|did\s+not)\s+know\s+it\s+yet\b", "field"),
    Pattern("dramatic_landing", "whether they knew it or not", r"\bwhether\s+(?:he|she|they)\s+knew\s+it\s+or\s+not\b", "field"),
    Pattern("dramatic_landing", "that would come later", r"\b(?:but\s+)?that\s+(?:would|could)\s+come\s+later\b", "field"),
    Pattern("dramatic_landing", "only one thing mattered colon reveal", r"\b(?:the\s+truth\s+was\s+simple|only\s+one\s+thing\s+mattered)\s*:", "field"),
    Pattern("dramatic_landing", "future portent", r"\b(?:in\s+ways\s+(?:he|she|they)\s+couldn['’]t\s+yet\s+understand|the\s+(?:real|hardest)\s+[^.!?\n]{1,45}\s+(?:had\s+only\s+begun|was\s+still\s+ahead))\b", "field"),
]

LEXICON = {
    "bolster", "bolstered", "crucial", "delve", "delved", "emphasize", "emphasized",
    "enduring", "enhance", "enhanced", "foster", "fostering", "garner", "highlight",
    "highlighted", "interplay", "intricate", "landscape", "meticulous", "pivotal",
    "robust", "showcase", "showcased", "tapestry", "testament", "underscore",
    "underscored", "vibrant", "profound", "visceral", "liminal", "ethereal",
    "poignant", "ineffable", "transcendent", "ephemeral", "gossamer", "luminous",
    "iridescent", "unwavering", "indelible", "shimmer", "shimmered", "glimmer",
    "glimmered", "unfurl", "unfurled", "smolder", "smoldered", "crescendo",
}

PARAGRAPH_ENDING_PATTERNS = [
    (
        "compact verdict",
        re.compile(
            r"^(?:and\s+)?(?:somehow,?\s*)?(?:that|this|it)\s+(?:was|is)\s+"
            r"(?:the\s+(?:point|difference|truth(?:\s+of\s+it)?|whole\s+of\s+it)|enough|worse|better|all|everything)[.!?]?$",
            re.IGNORECASE,
        ),
    ),
    (
        "miniature reveal",
        re.compile(
            r"^(?:and\s+)?that\s+was\s+(?:what\s+(?:did\s+it|mattered|changed)|when\s+everything\s+changed)[.!?]?$",
            re.IGNORECASE,
        ),
    ),
    (
        "staccato verdict",
        re.compile(
            r"^(?:(?:not|never)\s+(?:yet|again|anymore)|(?:a|the)\s+(?:beginning|promise|warning|choice|truth|difference))[.!?]?$",
            re.IGNORECASE,
        ),
    ),
    (
        "future portent",
        re.compile(
            r"^(?:(?:but\s+)?that\s+(?:would|could)\s+come\s+later|"
            r"nothing\s+would\s+(?:ever\s+)?be\s+the\s+same|"
            r"the\s+(?:real|hardest)\s+.{1,60}\s+(?:had\s+only\s+begun|was\s+still\s+ahead))[.!?]?$",
            re.IGNORECASE,
        ),
    ),
    (
        "hindsight tail",
        re.compile(
            r"^.{0,100}\b(?:though\s+(?:he|she|they)\s+(?:didn['’]t|did\s+not)\s+know\s+it\s+yet|"
            r"in\s+ways\s+(?:he|she|they)\s+couldn['’]t\s+yet\s+understand|"
            r"whether\s+(?:he|she|they)\s+knew\s+it\s+or\s+not)[.!?]?$",
            re.IGNORECASE,
        ),
    ),
]


def mask_non_prose(text: str) -> str:
    """Blank frontmatter, fenced code, and bold all-caps readouts while retaining line offsets."""
    lines = text.splitlines(keepends=True)
    in_frontmatter = bool(lines and lines[0].strip() == "---")
    in_fence = False
    result: list[str] = []
    for index, line in enumerate(lines):
        stripped = line.strip()
        masked = False
        if index == 0 and in_frontmatter:
            masked = True
        elif in_frontmatter:
            masked = True
            if stripped == "---":
                in_frontmatter = False
        elif stripped.startswith("```"):
            masked = True
            in_fence = not in_fence
        elif in_fence:
            masked = True
        elif re.fullmatch(r"\*\*[A-Z0-9 .:%'’/-]+\*\*\s*", stripped):
            masked = True
        if masked:
            body = " " * len(line.rstrip("\r\n"))
            result.append(body + ("\n" if line.endswith("\n") else ""))
        else:
            result.append(line)
    return "".join(result)


def line_starts(text: str) -> list[int]:
    starts = [0]
    starts.extend(match.end() for match in re.finditer("\n", text))
    return starts


def line_number(starts: list[int], offset: int) -> int:
    return bisect.bisect_right(starts, offset)


def standard_deviation(values: list[int]) -> float:
    if len(values) < 2:
        return 0.0
    mean = sum(values) / len(values)
    return math.sqrt(sum((value - mean) ** 2 for value in values) / len(values))


def sentence_data(text: str) -> tuple[list[str], list[int], Counter[str]]:
    parts = re.split(r"(?<=[.!?])(?:[\"'’”)]*)\s+|\n{2,}", text)
    sentences = [part.strip() for part in parts if part.strip()]
    lengths = [len(re.findall(r"\b[\w'’]+\b", sentence)) for sentence in sentences]
    openings: Counter[str] = Counter()
    for sentence in sentences:
        words = re.findall(r"\b[\w'’]+\b", sentence.lower())
        if len(words) >= 2:
            openings[" ".join(words[:2])] += 1
    return sentences, lengths, openings


def paragraph_spans(text: str) -> list[tuple[int, int, str]]:
    """Return nonblank paragraph spans with source offsets preserved."""
    spans: list[tuple[int, int, str]] = []
    start: int | None = None
    offset = 0
    for line in text.splitlines(keepends=True):
        if line.strip():
            if start is None:
                start = offset
        elif start is not None:
            spans.append((start, offset, text[start:offset].strip()))
            start = None
        offset += len(line)
    if start is not None:
        spans.append((start, len(text), text[start:].strip()))
    return spans


def last_sentence(paragraph: str) -> tuple[int, str]:
    """Return the paragraph-relative offset and text of its last sentence."""
    matches = list(re.finditer(r"[^.!?]+(?:[.!?]+[\"'’”)]*)?|[^.!?]+$", paragraph))
    if not matches:
        return 0, paragraph.strip()
    match = matches[-1]
    return match.start(), match.group(0).strip()


def dramatic_paragraph_endings(text: str, starts: list[int]) -> list[dict]:
    """Surface known landing shapes and mark nearby repetitions."""
    candidates: list[dict] = []
    prose_index = 0
    for start, _end, paragraph in paragraph_spans(text):
        if paragraph in {"—", "–"} or paragraph.startswith("#"):
            continue
        prose_index += 1
        relative, ending = last_sentence(paragraph)
        normalized = ending.strip().strip("*_`“”\"'’ ")
        word_count = len(re.findall(r"\b[\w'’]+\b", normalized))
        if not 1 <= word_count <= 18:
            continue
        for name, regex in PARAGRAPH_ENDING_PATTERNS:
            if regex.fullmatch(normalized):
                candidates.append({
                    "paragraph": prose_index,
                    "line": line_number(starts, start + relative),
                    "pattern": name,
                    "ending": ending,
                    "nearby_count": 1,
                    "clustered": False,
                })
                break

    for candidate in candidates:
        nearby = sum(
            1 for other in candidates
            if abs(other["paragraph"] - candidate["paragraph"]) <= 5
        )
        candidate["nearby_count"] = nearby
        candidate["clustered"] = nearby >= 2
    return candidates


def analyze(text: str) -> dict:
    masked = mask_non_prose(text)
    starts = line_starts(masked)
    source_lines = text.splitlines()
    hits: list[dict] = []
    by_category: Counter[str] = Counter()

    for pattern in PATTERNS:
        for match in re.finditer(pattern.regex, masked, flags=re.IGNORECASE | re.MULTILINE):
            line = line_number(starts, match.start())
            hits.append({
                "category": pattern.category,
                "pattern": pattern.name,
                "evidence": pattern.evidence,
                "line": line,
                "match": match.group(0),
                "context": source_lines[line - 1].strip()[:240] if source_lines else "",
            })
            by_category[pattern.category] += 1

    connector_regex = re.compile(r"(?im)(?:^|(?<=[.!?])\s+)(Additionally|Moreover|Furthermore|Consequently|Nevertheless|Notably|Indeed|Ultimately|However|Still|Yet)\b")
    connector_hits = [
        {"connector": match.group(1).lower(), "line": line_number(starts, match.start(1))}
        for match in connector_regex.finditer(masked)
    ]
    if connector_hits:
        by_category["canned_connectors"] += len(connector_hits)

    words = re.findall(r"\b[\w'’]+\b", masked.lower())
    lexical_counts = Counter(word for word in words if word in LEXICON)
    lexical_total = sum(lexical_counts.values())
    if len(lexical_counts) >= 3 or lexical_total >= 5:
        by_category["lexical_cluster"] = lexical_total

    sentences, sentence_lengths, openings = sentence_data(masked)
    ending_candidates = dramatic_paragraph_endings(masked, starts)
    paragraphs = [part.strip() for part in re.split(r"\n\s*\n", masked) if part.strip()]
    paragraph_lengths = [len(re.findall(r"\b[\w'’]+\b", paragraph)) for paragraph in paragraphs]
    repeated_openings = {opening: count for opening, count in openings.most_common() if count >= 3}
    word_count = len(words)
    scene_breaks = sum(1 for line in masked.splitlines() if line.strip() in {"—", "–"})
    em_dash_count = max(0, masked.count("—") + masked.count("–") - scene_breaks)

    return {
        "disclaimer": "Candidate surface patterns only; this output cannot determine authorship.",
        "metrics": {
            "words": word_count,
            "sentences": len(sentences),
            "paragraphs": len(paragraphs),
            "sentence_length_mean": round(sum(sentence_lengths) / len(sentence_lengths), 2) if sentence_lengths else 0.0,
            "sentence_length_stdev": round(standard_deviation(sentence_lengths), 2),
            "paragraph_length_stdev": round(standard_deviation(paragraph_lengths), 2),
            "em_dashes": em_dash_count,
            "em_dashes_per_1000_words": round((em_dash_count * 1000 / word_count), 2) if word_count else 0.0,
            "dramatic_paragraph_endings": len(ending_candidates),
            "clustered_dramatic_endings": sum(1 for item in ending_candidates if item["clustered"]),
        },
        "category_counts": dict(by_category),
        "hits": sorted(hits, key=lambda hit: (hit["line"], hit["category"], hit["pattern"])),
        "connectors": connector_hits,
        "lexical_candidates": dict(lexical_counts.most_common()),
        "repeated_sentence_openings": repeated_openings,
        "dramatic_paragraph_endings": ending_candidates,
    }


def markdown_report(result: dict) -> str:
    metrics = result["metrics"]
    lines = [
        "# Anti-AI Prose Candidate Scan", "", f"> {result['disclaimer']}", "",
        "## Surface metrics", "", "| Metric | Value |", "|--------|------:|",
        f"| Words | {metrics['words']} |",
        f"| Sentences | {metrics['sentences']} |",
        f"| Sentence length mean | {metrics['sentence_length_mean']} |",
        f"| Sentence length standard deviation | {metrics['sentence_length_stdev']} |",
        f"| Paragraph length standard deviation | {metrics['paragraph_length_stdev']} |",
        f"| Em dashes (scene breaks excluded) | {metrics['em_dashes']} |",
        f"| Em dashes per 1,000 words | {metrics['em_dashes_per_1000_words']} |",
        f"| Dramatic paragraph-ending candidates | {metrics['dramatic_paragraph_endings']} |",
        f"| Candidates in a five-paragraph cluster | {metrics['clustered_dramatic_endings']} |",
        "", "## Candidate categories", "",
    ]
    if result["category_counts"]:
        lines.extend(["| Category | Hits |", "|----------|-----:|"])
        lines.extend(f"| {category} | {count} |" for category, count in sorted(result["category_counts"].items()))
    else:
        lines.append("No catalog patterns found.")

    lines.extend(["", "## Exact hits", ""])
    if result["hits"]:
        lines.extend(["| Line | Evidence | Category | Pattern | Match |", "|-----:|----------|----------|---------|-------|"])
        for hit in result["hits"]:
            match = hit["match"].replace("|", "\\|").replace("\n", " ")
            lines.append(f"| {hit['line']} | {hit['evidence']} | {hit['category']} | {hit['pattern']} | `{match}` |")
    else:
        lines.append("No exact phrase-family hits found.")

    lines.extend(["", "## Sentence-opening connectors", ""])
    if result["connectors"]:
        counts = Counter(item["connector"] for item in result["connectors"])
        lines.append(", ".join(f"`{word}` x {count}" for word, count in counts.most_common()))
    else:
        lines.append("None found.")

    lines.extend(["", "## Lexical candidates", ""])
    if result["lexical_candidates"]:
        lines.append(", ".join(f"`{word}` x {count}" for word, count in result["lexical_candidates"].items()))
    else:
        lines.append("None found.")

    lines.extend(["", "## Repeated two-word sentence openings", ""])
    if result["repeated_sentence_openings"]:
        lines.append(", ".join(f"`{opening}` x {count}" for opening, count in result["repeated_sentence_openings"].items()))
    else:
        lines.append("None occurred three or more times.")

    lines.extend(["", "## Dramatic paragraph-ending candidates", ""])
    if result["dramatic_paragraph_endings"]:
        lines.extend([
            "| Line | Paragraph | Pattern | Nearby | Ending |",
            "|-----:|----------:|---------|-------:|--------|",
        ])
        for item in result["dramatic_paragraph_endings"]:
            ending = item["ending"].replace("|", "\\|").replace("\n", " ")
            lines.append(
                f"| {item['line']} | {item['paragraph']} | {item['pattern']} | "
                f"{item['nearby_count']} | `{ending}` |"
            )
    else:
        lines.append("None found.")

    lines.extend(["", "Inspect every candidate in context. Density and craft cost matter more than presence."])
    return "\n".join(lines)


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("path", nargs="?", default="-", help="UTF-8 text/Markdown file, or - for stdin")
    parser.add_argument("--json", action="store_true", help="Emit JSON instead of Markdown")
    return parser.parse_args()


def main() -> int:
    args = parse_args()
    try:
        text = sys.stdin.read() if args.path == "-" else Path(args.path).read_text(encoding="utf-8-sig")
    except (OSError, UnicodeError) as exc:
        print(f"scan_prose.py: {exc}", file=sys.stderr)
        return 2

    result = analyze(text)
    print(json.dumps(result, indent=2, ensure_ascii=False) if args.json else markdown_report(result))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
