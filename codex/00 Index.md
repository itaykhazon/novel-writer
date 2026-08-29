---
type: index
tags: [index, ai-orientation]
---

# Codex — Start Here

This index exists to orient an AI assistant fast at the start of a writing session — read this file first, before opening anything else. It's a map plus the current manuscript state, not just a list of links.

> **New project setup:** this whole codex is a boilerplate. Before your first real writing session, set your book's title in `codex/project.json` and fill in the sections below marked `<fill in>`. Nothing else in this vault hardcodes the title — `project.json` is the single place it lives, so there is no find-and-replace to do. See the vault-level `README.md` for the full setup checklist, or run `populate-project`, which writes `project.json` and fills in the genre/style/craft reference files via an interview plus web research.

## Manuscript status (keep this current)

<fill in — one paragraph, updated every time a chapter is drafted or restructured>

Which chapters are drafted, which are outlined-but-undrafted, and exactly where the manuscript currently ends: who's where, what just happened, what's still in motion. This is the single most important paragraph in the vault — every skill that plans or drafts a chapter reads it first for continuity. Keep it current or a new chapter will get planned against a stale state.

## Open threads

<fill in>

List the specific unresolved questions the manuscript has raised but not answered — not every mystery in the Braindump, just what's genuinely dangling on the page right now. A new chapter should either resolve one of these or knowingly carry it forward; `add-chapter` reads this list for direction when instructions are thin.

## Before drafting or extending lore, read

1. [[Genre]], [[Writing Style]], and [[Craft Influences]] — genre, voice, prose, formatting, comp-title influences, and frequently broken continuity rules; always in effect. These files are genre- and POV-agnostic on their own — they only become useful once filled in for your actual novel (by hand, or via `populate-project`).
2. [[Editing Workflow]] — approval, changelog, canon-conflict, chapter-creation, and review rules; read before changing vault files.
3. [[00 Braindump]] — future-intent story bible. The manuscript beats the codex, and the codex beats the Braindump; flag substantive conflicts rather than silently choosing canon.
4. The relevant sub-index below for whatever the scene touches.

## Folder map

- [[00 Characters Index]] — one file per character; frontmatter has `role`, `species`, `group`, `status`
- [[00 Species & Factions Index]] — the peoples, cultures, and organizations of your world (rename or drop this folder if your novel doesn't need it)
- [[00 Locations Index]] — every named place worth its own note
- [[00 Systems Index]] — magic systems, tech, progression mechanics, institutional rules — anything your world runs on (optional; drop if not applicable)
- [[00 Plot Index]] — macro outline + mystery discovery tracker, if your story has one
- [[00 Snippets Index]] — non-canon prose fragments parked for possible later incorporation
- `templates/` — frontmatter/section skeletons for each note type; used by `add-to-codex`, `add-chapter`, and `draft-chapter`
- `reviews/` — per-chapter review reports (proofread, prose, pacing, continuity, external)

## Conventions

- Every note has `type:` in its frontmatter (`character`, `location`, `species-faction`, `mechanic`, `plot`, `snippet`, `chapter`, `index`). Grep-friendly — that's the fastest way for an AI to filter this codex without reading everything.
- Wikilinks on entities, kept for the human-facing backlink graph, but don't rely on them alone for machine lookup — the indexes and `type:` frontmatter are the reliable path. Every wikilink should resolve to a real note or an `aliases:` entry; dangling links break the review-bundle builder (`chapter-cycle/scripts/audit_links.py` checks this).
- Anything not yet written into the manuscript is explicitly flagged (`status:`, `manuscript-status:`, or "not yet reached/written" in prose) so it's never mistaken for established fact.
- <fill in any house-wide fact conventions you want enforced vault-wide, e.g. a units convention — the more load-bearing detail belongs in `Writing Style.md`>
- One note per entity. If something in [[00 Braindump]] doesn't have its own note yet, that's a gap — see `add-to-codex`.

## Novel manuscript

`novel/arc 1/` — one folder per chapter, each containing the chapter file itself, a `Summary.md` (read this instead of the full chapter when you just need a refresher), and a `drafts/` folder for prior versions and a `Changelog.md`. See `codex/templates/Arc Index Template.md` and `codex/templates/Summary Template.md` for the exact shape of the arc index and per-chapter summary.
