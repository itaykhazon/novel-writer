#!/usr/bin/env python3
"""
Codex analyzer — indexes and analyzes story codex files for continuity checking.
Extracts entities, traits, timelines, and relationships from markdown codex.
"""

import json
import re
from pathlib import Path
from typing import Dict, List, Any, Tuple

class CodexAnalyzer:
    def __init__(self, codex_path: str):
        self.codex_path = Path(codex_path)
        self.entities = {}  # type: location -> name -> details
        self.characters = {}
        self.locations = {}
        self.plot_threads = {}
        self.mechanics = {}

    def load_codex(self) -> Dict[str, Any]:
        """Load and index all codex files."""

        # Load characters
        char_dir = self.codex_path / "characters"
        if char_dir.exists():
            self._load_character_files(char_dir)

        # Load locations
        loc_dir = self.codex_path / "locations"
        if loc_dir.exists():
            self._load_location_files(loc_dir)

        # Load plot info
        plot_dir = self.codex_path / "plot"
        if plot_dir.exists():
            self._load_plot_files(plot_dir)

        # Load systems/mechanics
        sys_dir = self.codex_path / "systems-mechanics"
        if sys_dir.exists():
            self._load_mechanics_files(sys_dir)

        return {
            "characters": self.characters,
            "locations": self.locations,
            "plot_threads": self.plot_threads,
            "mechanics": self.mechanics,
        }

    def _load_character_files(self, char_dir: Path):
        """Extract character traits and stats."""
        for char_file in char_dir.rglob("*.md"):
            if char_file.name.startswith("00") or char_file.stem.endswith(" - Voice"):
                continue
            char_name = char_file.stem
            content = char_file.read_text(encoding="utf-8")

            # Extract frontmatter and key traits
            self.characters[char_name] = {
                "file": str(char_file),
                "traits": self._extract_traits(content),
                "status": self._extract_field(content, "status"),
                "role": self._extract_field(content, "role"),
                "squad": self._extract_field(content, "squad"),
                "species": self._extract_field(content, "species"),
            }

    def _load_location_files(self, loc_dir: Path):
        """Extract location descriptions and details."""
        for loc_file in loc_dir.rglob("*.md"):
            if loc_file.name.startswith("00"):
                continue
            loc_name = loc_file.stem
            content = loc_file.read_text(encoding="utf-8")

            self.locations[loc_name] = {
                "file": str(loc_file),
                "description": self._extract_description(content),
                "world_kind": self._extract_field(content, "world-kind"),
            }

    def _load_plot_files(self, plot_dir: Path):
        """Extract plot threads and mystery tracker."""
        for plot_file in plot_dir.rglob("*.md"):
            if plot_file.name.startswith("00"):
                continue
            content = plot_file.read_text(encoding="utf-8")
            self.plot_threads[plot_file.stem] = {
                "file": str(plot_file),
                "threads": self._extract_plot_threads(content),
            }

    def _load_mechanics_files(self, sys_dir: Path):
        """Extract system rules and mechanics."""
        for mech_file in sys_dir.rglob("*.md"):
            if mech_file.name.startswith("00"):
                continue
            content = mech_file.read_text(encoding="utf-8")
            self.mechanics[mech_file.stem] = {
                "file": str(mech_file),
                "rules": self._extract_rules(content),
                "compound_descriptor_flags": self._flag_compound_descriptors(content),
            }

    def _flag_compound_descriptors(self, content: str) -> List[str]:
        """Flag lines that describe a recurring item with a slash-joined pair of
        descriptive terms (e.g. "brass/bronze compass"). This pattern often means
        an earlier pass noticed two different chapters using different wording for
        the same object and folded them together in the codex instead of resolving
        which chapter is correct (or updating both to match). It is not itself proof
        the underlying chapters agree — flag it so a human or the continuity-reviewer
        skill checks the cited chapters' actual text.
        """
        flags = []
        # Matches word/word directly before a physical-object noun. The list is
        # deliberately broad and genre-neutral rather than tuned to one book's
        # props; extend it with your own recurring object nouns (a ship class, a
        # garment, an instrument) if this misses drift in your manuscript.
        OBJECT_NOUNS = (
            "item|object|artifact|relic|heirloom|token|tool|weapon|blade|sword|"
            "knife|gun|armor|armour|cloak|coat|robe|mask|ring|pendant|amulet|"
            "compass|lantern|lamp|key|book|letter|map|box|case|vial|flask|"
            "stone|shard|crystal|gem|ore|mineral|vein|fragment|"
            "device|machine|engine|vehicle|ship|boat|cart"
        )
        pattern = r"\b([A-Za-z]+/[A-Za-z]+)\s+(" + OBJECT_NOUNS + r")\b"
        for match in re.finditer(pattern, content, re.IGNORECASE):
            # Grab a bit of surrounding context for the flag
            start = max(0, match.start() - 40)
            end = min(len(content), match.end() + 60)
            snippet = content[start:end].replace("\n", " ").strip()
            flags.append(snippet)
        return flags

    def _extract_field(self, content: str, field_name: str) -> str:
        """Extract a field from frontmatter."""
        pattern = rf"^{re.escape(field_name)}:\s*(.+?)\s*$"
        match = re.search(pattern, content, re.IGNORECASE | re.MULTILINE)
        return match.group(1).strip() if match else None

    def _extract_traits(self, content: str) -> Dict[str, str]:
        """Extract character traits (physical, backstory, abilities)."""
        traits = {}
        # Look for key sections and extract relevant info
        sections = ["appearance", "abilities", "backstory", "physical", "description"]
        for section in sections:
            pattern = rf"##.*{section}.*?\n(.*?)(?=##|\Z)"
            match = re.search(pattern, content, re.IGNORECASE | re.DOTALL)
            if match:
                traits[section] = match.group(1).strip()[:200]
        return traits

    def _extract_description(self, content: str) -> str:
        """Extract location description."""
        # Prefer an explicit Description section, then fall back to the prose
        # between the H1 title and the first H2 section (the location template).
        pattern = r"##.*Description.*?\n(.*?)(?=^##|\Z)"
        match = re.search(pattern, content, re.IGNORECASE | re.DOTALL | re.MULTILINE)
        if not match:
            match = re.search(r"^#\s+.+?\n+(.*?)(?=^##|\Z)", content,
                              re.DOTALL | re.MULTILINE)
        return match.group(1).strip()[:300] if match else ""

    def _extract_plot_threads(self, content: str) -> List[Dict[str, Any]]:
        """Extract plot threads and their revelation status."""
        threads = []
        pattern = r"^\s*[-*]\s*(.+?)(?:revealed|status):\s*(true|false)"
        for match in re.finditer(pattern, content, re.MULTILINE | re.IGNORECASE):
            threads.append({
                "thread": match.group(1).strip(),
                "revealed": match.group(2).lower() == "true"
            })
        return threads

    def _extract_rules(self, content: str) -> List[str]:
        """Extract mechanical rules."""
        rules = []
        # Extract numbered rules or bullet points from mechanics docs
        pattern = r"^\s*\d+\.\s+(.+?)$"
        for match in re.finditer(pattern, content, re.MULTILINE):
            rules.append(match.group(1).strip())
        return rules


def main():
    import sys
    if len(sys.argv) < 2:
        print("Usage: codex_analyzer.py <path-to-codex>")
        sys.exit(1)

    codex_path = sys.argv[1]
    analyzer = CodexAnalyzer(codex_path)
    codex_data = analyzer.load_codex()

    # Surface compound-descriptor flags up front — these are the cheapest signal
    # of a possible cross-chapter item-description mismatch (the "brass/bronze
    # compass" case) and are easy to miss buried in the full JSON dump below.
    any_flags = False
    for mech_name, mech_data in codex_data.get("mechanics", {}).items():
        for flag in mech_data.get("compound_descriptor_flags", []):
            any_flags = True
            print(f"[COMPOUND DESCRIPTOR] {mech_name}: ...{flag}...", file=sys.stderr)
    if any_flags:
        print("^ Check the chapters cited near each flag above — a slash-joined "
              "descriptor in the codex may mean two chapters use different wording "
              "for the same item.\n", file=sys.stderr)

    # Output as JSON for easy consumption
    print(json.dumps(codex_data, indent=2, default=str))


if __name__ == "__main__":
    main()
