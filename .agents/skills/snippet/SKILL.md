---
name: snippet
description: Generate a short random {{NOVEL_TITLE}} prose fragment or capture a user-supplied fragment, then save it as a clearly non-canon, indexed snippet note for possible later incorporation. Use when the user invokes /snippet or $snippet, asks for a random {{NOVEL_TITLE}} snippet, wants to park spare prose or dialogue, or says to save a fragment or scene idea for later.
---

# Save an {{NOVEL_TITLE}} Snippet

Create or capture one compact fragment and file it in the codex without treating it as manuscript canon.

## 1. Choose the mode

- If the user supplied fragment text, preserve that text exactly. Do not polish, extend, correct, or add wikilinks inside it unless asked.
- If the user asks for a random snippet or invokes the skill without fragment text, generate one short fragment, normally 80–250 words.
- Honor any seed the user gives: character, setting, mood, image, line, mechanic, or possible chapter.
- If the request has neither text nor permission to generate, ask for the fragment instead of guessing.

## 2. Orient before writing

Read `codex/00 Index.md` and `codex/Editing Workflow.md` before changing the codex.

For a generated snippet, also read:

1. `codex/Genre.md` and `codex/Writing Style.md`.
2. The relevant character, voice, location, and mechanic notes for the chosen focus.
3. Any open thread named in `codex/00 Index.md` that the fragment might touch.

Choose a fresh combination of focus and function, such as a character micro-beat, dialogue exchange, environmental image, mechanic complication, dark-comedy interruption, or foreshadowing seed. Prefer established elements used in a new way over inventing a new species, power, faction, or mystery answer.

Keep generated prose compatible with established limitations and character voice, but do not force it into the current timeline. Never resolve a deliberately unknown mystery or present Braindump intent as fact.

## 3. Create the snippet note

Use `codex/templates/Snippet Template.md`. Save one note per fragment under `codex/snippets/` with this filename pattern:

`YYYY-MM-DD HHmmss - <Short Descriptive Title>.md`

Use local time, remove filename-invalid characters, and add a numeric suffix if a collision remains. Fill every template field:

- `status: unincorporated`
- `canon-status: non-canon`
- `captured:` with an ISO 8601 timestamp
- `source: generated` or `source: user-supplied`
- `related:` with only existing codex wikilinks

Write a specific two-to-seven-word title. Put the fragment under `## Snippet` without codex markup inside the prose. Under `## Incorporation notes`, give concise, practical possibilities rather than declaring where it belongs. Record any continuity dependency or conflict found during orientation.

The invocation authorizes creation of this snippet note and its index line. It does not authorize edits to manuscript prose or established lore.

## 4. Update the snippets index

Add the new note at the top of `## Unincorporated` in `codex/snippets/00 Snippets Index.md`. Replace the `_None yet._` placeholder when adding the first entry. Use this form:

`- [[<filename without extension>|<title>]] — <one factual sentence about the fragment's focus or possible use>.`

Do not update character, mechanic, plot, or manuscript-status notes based only on a snippet. A snippet remains speculative material even when it matches the outline.

## 5. Preserve the lifecycle

Do not incorporate the fragment automatically. When the user later approves its use in manuscript prose, follow `codex/Editing Workflow.md` and the applicable drafting or review-application skill. Only after the prose actually lands on the page:

1. Change `status` to `incorporated` and `canon-status` to `incorporated-as-revised` or `incorporated-verbatim`.
2. Add `incorporated-in: "[[Chapter N - Title]]"` to the snippet frontmatter.
3. Move its index line from `## Unincorporated` to `## Incorporated`, adding the chapter link.

## 6. Report the result

Return the created note's title and clickable path, its generated or user-supplied source, and any conflict that could affect later incorporation. Do not describe the fragment as canon.
