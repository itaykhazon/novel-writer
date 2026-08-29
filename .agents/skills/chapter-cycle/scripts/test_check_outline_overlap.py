#!/usr/bin/env python3
"""Tests for check_outline_overlap.py. Run: python3 -m unittest test_check_outline_overlap -v"""

import unittest

import check_outline_overlap as coo


def runs(prose_text, outline_text, min_run=7):
    prose, _ = coo.tokenize(prose_text)
    outline, _ = coo.tokenize(outline_text)
    exempt = set()
    for anchor in coo.read_anchors(outline_text):
        for start, end in coo.find_sequence(prose, anchor):
            exempt.update(range(start, end))
    out = []
    for run in coo.shared_runs(prose, outline, min_run):
        for start, end in coo.subtract(run, exempt, min_run):
            out.append(" ".join(prose[start:end]))
    return out


class Tokenize(unittest.TestCase):
    def test_strips_markdown_and_folds_apostrophes(self):
        tokens, _ = coo.tokenize("**Beat 3** — she didn’t answer.")
        self.assertEqual(tokens, ["beat", "3", "she", "didn't", "answer"])

    def test_offsets_point_at_the_source(self):
        text = "the lamp guttered"
        tokens, offsets = coo.tokenize(text)
        self.assertEqual(text[offsets[1]:offsets[1] + 4], "lamp")

    def test_frontmatter_removed(self):
        body = coo.strip_frontmatter("---\npov: mara\n---\nShe ran.\n")
        self.assertEqual(body.strip(), "She ran.")


class Overlap(unittest.TestCase):
    def test_no_shared_wording_is_clean(self):
        self.assertEqual(runs("She broke the window and went in through the frame.",
                              "- Beat 1: the protagonist enters the house illegally"), [])

    def test_transcribed_sentence_is_caught(self):
        shared = "she crosses the bridge before the guards change shift"
        self.assertEqual(runs(f"Dawn came. {shared}, and nobody called out.",
                              f"- Beat 2: {shared}."), [shared])

    def test_run_shorter_than_threshold_is_ignored(self):
        self.assertEqual(runs("he opened the heavy door slowly", "- he opened the heavy door slowly"), [])

    def test_threshold_is_inclusive(self):
        seven = "one two three four five six seven"
        self.assertEqual(runs(seven, seven, min_run=7), [seven])
        self.assertEqual(runs(seven, seven, min_run=8), [])

    def test_longest_run_is_reported_not_just_the_ngram(self):
        shared = "the lantern burned green for the length of a held breath tonight"
        found = runs(f"Outside, {shared} and then died.", f"- Beat 4: {shared}.")
        self.assertEqual(found, [shared])


class Anchors(unittest.TestCase):
    OUTLINE = (
        "- Beat 1: she recites the oath at the door\n"
        "\n"
        "## Verbatim anchors\n"
        "- I keep what I am given and I give what I am kept\n"
    )

    def test_declared_anchor_is_exempt(self):
        prose = "She said it flatly: I keep what I am given and I give what I am kept."
        self.assertEqual(runs(prose, self.OUTLINE), [])

    def test_anchor_parsing_strips_list_markers_and_quotes(self):
        self.assertEqual(
            coo.read_anchors('## Verbatim anchors\n1. "hold the line until dawn"\n'),
            [["hold", "the", "line", "until", "dawn"]],
        )

    def test_no_anchor_section_means_no_exemption(self):
        self.assertEqual(coo.read_anchors("- Beat 1: something happens\n"), [])

    def test_text_adjacent_to_an_anchor_is_still_judged(self):
        """Only the anchor's own span is deducted — padding it can't launder neighbours."""
        anchor = "hold the line until dawn"
        neighbour = "and she did not look back at the ruined gate"
        outline = f"- Beat 1: {neighbour}\n\n## Verbatim anchors\n- {anchor}\n"
        found = runs(f"{anchor} {neighbour}.", outline)
        self.assertEqual(found, [neighbour])


class Subtract(unittest.TestCase):
    def test_surviving_pieces_must_clear_the_threshold(self):
        # exempting index 5 splits 0..12 into 0..5 (5 words) and 6..12 (6 words)
        self.assertEqual(coo.subtract((0, 12), {5}, 7), [])
        self.assertEqual(coo.subtract((0, 12), {5}, 5), [(0, 5), (6, 12)])

    def test_nothing_exempt_returns_the_whole_span(self):
        self.assertEqual(coo.subtract((3, 14), set(), 7), [(3, 14)])


if __name__ == "__main__":
    unittest.main()
