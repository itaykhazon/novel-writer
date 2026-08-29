# {{NOVEL_TITLE}} — Project Instructions

<fill in — one line describing the book: genre and hook, e.g. "An epic fantasy novel about...">

This is the shared routing file for AI assistants working in this vault.

## Start here

1. Read `codex/00 Index.md` for the vault map, current manuscript state, and open threads.
2. Read `codex/Genre.md` and `codex/Writing Style.md` before outlining, drafting, or reviewing prose.
3. Read `codex/Editing Workflow.md` before changing manuscript, codex, review, summary, outline, or changelog files.
4. Follow any applicable skill under `.agents/skills/`; skill-specific workflow supplements these project documents but does not override them.

## Authority

For story facts, the manuscript beats the codex, and the codex beats `codex/00 Braindump.md`. Braindump material is future intent until it appears on the page. Surface substantive conflicts instead of silently choosing canon.

## Chapter-cycle exception

An explicit request to run `chapter-cycle` authorizes its complete one-shot draft, review, regression-check, and fix-application loop. Other suggested manuscript edits still require the approval described in `codex/Editing Workflow.md`.

## Tool-specific automation

Claude account skills (Cowork) may provide orchestration that Codex does not share — see `.agents/skills/sync-skills/SKILL.md` for how the two local copies (`.agents/skills/` and `.claude/skills/`) and any Cowork-account originals relate. Durable story knowledge and house rules belong in this vault, not exclusively inside an account-level skill.
