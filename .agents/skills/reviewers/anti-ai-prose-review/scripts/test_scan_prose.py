#!/usr/bin/env python3
"""Deterministic tests for the anti-AI prose candidate scanner."""

from __future__ import annotations

import importlib.util
import sys
import unittest
from pathlib import Path


SCRIPT_PATH = Path(__file__).with_name("scan_prose.py")
SPEC = importlib.util.spec_from_file_location("scan_prose", SCRIPT_PATH)
assert SPEC and SPEC.loader
scan_prose = importlib.util.module_from_spec(SPEC)
sys.modules[SPEC.name] = scan_prose
SPEC.loader.exec_module(scan_prose)


class ScannerTests(unittest.TestCase):
    def test_clusters_repetitive_false_landings(self) -> None:
        text = (
            "Mara closed the file.\n\n"
            "That was the truth of it.\n\n"
            "She put the key in her pocket.\n\n"
            "And somehow, that was enough.\n"
        )
        result = scan_prose.analyze(text)
        endings = result["dramatic_paragraph_endings"]
        self.assertEqual(2, len(endings))
        self.assertTrue(all(item["clustered"] for item in endings))
        self.assertEqual(2, result["metrics"]["clustered_dramatic_endings"])

    def test_marks_isolated_candidate_without_calling_it_clustered(self) -> None:
        text = (
            "The latch broke under his thumb.\n\n"
            "Nothing would ever be the same.\n\n"
            "He wrapped the wire around the exposed contact and tested it twice.\n"
        )
        ending = scan_prose.analyze(text)["dramatic_paragraph_endings"][0]
        self.assertFalse(ending["clustered"])
        self.assertEqual(1, ending["nearby_count"])

    def test_does_not_flag_earned_concrete_short_ending(self) -> None:
        text = "The round punched through the neck seam.\n\nThe Striker dropped.\n"
        result = scan_prose.analyze(text)
        self.assertEqual([], result["dramatic_paragraph_endings"])

    def test_masks_frontmatter_and_system_readouts(self) -> None:
        text = (
            "---\nsummary: That was the whole of it.\n---\n\n"
            "**NOTHING WOULD EVER BE THE SAME.**\n\n"
            "The pump restarted.\n"
        )
        result = scan_prose.analyze(text)
        self.assertEqual([], result["dramatic_paragraph_endings"])
        self.assertEqual(0, result["category_counts"].get("dramatic_landing", 0))


if __name__ == "__main__":
    unittest.main()
