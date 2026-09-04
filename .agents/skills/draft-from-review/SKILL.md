---
name: draft-from-review
description: Apply a manuscript reviewer's findings to the actual chapter file(s), then log the change as a new entry in that chapter's Changelog.md inside its drafts folder. Use when the user has a review report (proofreading, continuity, developmental, line-edit, or any other reviewer's output) and wants the fixes actually applied to the manuscript, not just described. Works with any report format — not tied to a specific reviewer's output structure.
---

# Draft From Review

Turns a reviewer's findings into an applied edit, with a paper trail. This
skill does not care which reviewer produced the report — proofreading,
continuity, developmental notes, a beta reader's comments pasted in chat,
or a human editor's markup all work the same way, as long as the report
identifies specific problems in specific places.

## When to use this

The user has (or asks you to run) some kind of review of one or more
manuscript chapters, and now wants the fixes actually written into the
chapter files — not just a list they have to apply by hand.

Do NOT assume the report looks like the `proofread` skill's output
(numbered "Error N" entries with Original/Suggested/Why fields). Reports
can also be:
- A continuity-reviewer style list of inconsistencies.
- Free-form prose notes ("the pacing drags in the middle, the POV character's line on
  page 3 doesn't match his established voice, there's a typo in
  paragraph 2").
- A pasted list of beta-reader comments.
- A human's inline markup or bullet list of complaints.

Read whatever's given and extract concrete, actionable fixes from it —
don't require a particular structure.

If the user doesn't hand you the report directly, saved reports from
`proofread`, `continuity-reviewer`, and `prose-review` live in the vault's
top-level `reviews/` folder (sibling to `codex/` and `novel/`), one file
per chapter, named `<Chapter Name> - <type>-review-<YYYY-MM-DD>.md`. Look
there first. This skill's own output (diffs and changelog entries) still
belongs in each chapter's own `drafts/Changelog.md`, per step 5 below —
`reviews/` is only where the source reports are read from, never where
this skill writes.

## Workflow

1. **Identify the target file(s).** The report should name or clearly
   imply which chapter(s) it covers. If it's ambiguous which file a
   finding applies to, ask rather than guess. Locate each chapter's main
   manuscript file (e.g. `Chapter 3 - Repurposed/Chapter 3 - Repurposed.md`)
   and confirm it has (or create) a `drafts/` subfolder alongside it.

2. **Stage a working copy.** Copy the current chapter file to a scratch
   location and keep an untouched copy of the original alongside it —
   you'll diff the two later.

3. **Triage the findings before touching anything.** Not every review
   comment is a direct, unambiguous text swap. Sort findings into:
   - **Direct fixes** — the report gives (or clearly implies) exact
     original text and a specific replacement. Apply these directly.
   - **Described-but-not-dictated fixes** — the report describes a
     problem ("this line reads awkwardly," "the injury is described on
     the left side here but the codex says right") without prescribing
     exact replacement text. Draft a minimal, in-voice fix consistent
     with the finding and the surrounding prose. Prefer the smallest
     change that resolves the issue — this is a correction pass, not a
     rewrite.
   - **Subjective or open-ended notes** — pacing complaints, "consider
     cutting this scene," tone preferences, anything requiring a
     judgment call about the story itself rather than a fixable defect.
     Do not resolve these unilaterally. Leave them out of the applied
     edit and call them out to the user afterward as skipped/needs-input.
   - **Continuity findings that touch canon** — if a finding implies a
     codex or outline is wrong rather than the prose (e.g. the reviewer
     flags a contradiction and it's ambiguous which side is the error),
     don't silently pick a side. Ask, or apply the fix that changes only
     the chapter text and note the possible codex implication for the
     user to check.
   - **Cross-artifact fact findings** — if a finding is (or amounts to) a
     `continuity-reviewer` Cross-Artifact Fact Consistency issue — the
     same number, tag, or placement stated differently in the prose vs.
     that chapter's `Summary.md` vs. a codex mechanics page — treat the
     prose as the fact once you've applied the prose-side fix, and see
     step 6a below. Don't treat this as "just" a prose edit; the Summary
     and codex sides need the same correction or the drift just moves
     one artifact over instead of closing.

4. **Apply the direct and described-but-not-dictated fixes** to the
   working copy using targeted edits (smallest possible diff per fix —
   don't reformat or rewrite untouched surrounding text). Preserve the
   file's existing frontmatter, voice, and formatting conventions exactly.
   If a finding turns out to belong to a different chapter than the report
   implied (cross-check the actual text, don't trust the report's chapter
   label blindly), apply it to the correct file and note the correction
   in that chapter's changelog entry.

5. **Diff, then log to the chapter's changelog — not a bare `.diff` file.**
   Generate a unified diff (`diff -u original edited`) between the
   untouched original and the edited working copy. This manuscript lives
   in Obsidian, which only renders `.md` files — a standalone `.diff` file
   is invisible in the vault, so don't rely on one as the primary record.

   Instead, open (or create) `Changelog.md` inside that chapter's
   `drafts/` folder and **append** a new dated section — never overwrite
   or replace earlier entries, this file accumulates across every review
   pass over the chapter's life. Format each entry as:

   ```markdown
   ## <YYYY-MM-DD> — <reviewer or report name>

   <One- or two-sentence plain-language summary of what changed and why —
   readable without opening the diff.>

   ```diff
   <the unified diff for this pass, exactly as produced by `diff -u`>
   ```
   ```

   If `Changelog.md` doesn't exist yet for that chapter, create it with a
   one-line title (`# <Chapter Name> — Draft Changelog`) and a short note
   that entries are newest-at-bottom, generated by this skill, before the
   first dated section.

   Infer `<reviewer or report name>` from the report itself (its filename,
   its title, or which skill/tool produced it — "proofread",
   "continuity-review", "beta-reader-notes", etc.). If nothing sensible is
   available, use "review".

6. **Write the edited file back** to the chapter's main manuscript path,
   overwriting the original (the changelog is the record of what changed
   — the manuscript itself should always reflect the latest accepted
   edits).

6a. **Re-sync any fact you just changed that's also recorded elsewhere.**
   This step exists because it was previously skipped and caused real
   drift: after step 6, check whether the fix you applied changed a
   quantitative or categorical fact (a percentage, a count, a rank/tag, a
   placement, which hand or side something is on) that this chapter's
   `Summary.md` or a codex page (typically under `codex/systems-mechanics/`
   or the relevant character/creature note) *also* states.

   - If the Summary or codex value now disagrees with the corrected prose,
     update it there too, in the same pass — not as a follow-up task, and
     not only when explicitly asked. A prose fix that leaves a stale
     Summary or codex value behind doesn't close the continuity gap, it
     just relocates it, and the next continuity review will find the
     Summary and codex "agreeing" with each other and miss that both are
     wrong.
   - Note every file you touched this way in the same changelog entry
     (step 5) — e.g. "Also corrected the matching charge value in
     `Summary.md` and the mechanic's page under
     `codex/systems-mechanics/`, which still cited the pre-fix number."
   - If you're not sure whether a Summary/codex value is meant to track
     this exact fact (as opposed to a deliberately different, later
     state), don't silently overwrite it — flag it to the user the same
     way you'd flag an ambiguous canon conflict (see step 3's
     "Continuity findings that touch canon").
   - This step applies whether the fix came from a `continuity-reviewer`
     Cross-Artifact Fact Consistency finding specifically, or from any
     other reviewer's finding that happened to touch a fact duplicated
     elsewhere (a proofreading fix that corrects a number is still a fact
     correction).

7. **House-style check before finalizing.** If any applied fix touched a
   chapter's opening line, inserted or moved a scene-break marker (`—`),
   or converted a passage from one POV character to another, re-read the
   resulting opening line of the chapter and of every scene that starts
   or now starts after a break — it must open on the POV character's
   name (per `codex/Writing Style.md` and `prose-review` rule 12). This is
   easy to violate as a side effect of an unrelated fix (e.g. a filter-word
   cut, or retiming a POV shift to a new scene break) — check it
   explicitly rather than assuming the original wording still applies. If
   it's violated, fix it as part of the same pass and note it in the
   changelog entry.

8. **Write the applied status back to the source report, if there is one.**
   If the fixes came from a saved report in `reviews/` (rather than notes
   pasted directly in chat), open that report file and, immediately below
   each applied finding's `**Why:**` (or `**Note:**` for structural
   findings), add a line: `**Status:** Applied <YYYY-MM-DD> — see
   <chapter>/drafts/Changelog.md`. This lets the report double as a status
   tracker instead of going stale the moment fixes are applied. Skip this
   step only if there's no saved report to update (e.g. the findings were
   ad hoc chat notes).

9. **Report back concisely.** Tell the user: how many findings were
   applied, how many were skipped and why (with enough detail to act on
   them), which files besides the manuscript chapter were touched by the
   step 6a re-sync (name them — don't just say "and related files"), and
   confirm the changelog entry was appended (name the file:
   `<chapter>/drafts/Changelog.md`) and, if applicable, that the source
   report's statuses were updated. Don't re-paste the full diff in chat
   unless asked — the changelog entry is the deliverable.

## Multiple chapters in one report

If a single review report covers several chapters, repeat steps 2–8 per
chapter independently — each gets its own appended entry in its own
`drafts/Changelog.md`. Don't merge chapters into one changelog file.

## What NOT to do

- Don't apply fixes for findings you're not confident you understood
  correctly — skip and flag instead of guessing.
- Don't "improve while you're in there" — only touch what the review
  actually flagged. Scope creep here makes the changelog entry misleading.
- Don't overwrite a chapter file without also logging the change — the
  changelog is the whole point of this skill (it's what makes the edit
  visible in Obsidian, reviewable, and revertible).
- Don't fix the manuscript and leave a duplicated fact stale in `Summary.md`
  or a codex page — that's not a smaller version of the fix, it's a
  different bug (a cross-artifact contradiction) replacing the one you just
  closed. See step 6a.
- Don't overwrite `Changelog.md` itself — always append. Read the current
  file first (if it exists) and write back the full content with the new
  section added.
- Don't produce a bare `.diff` file as the deliverable — embed the diff
  inside the changelog entry's fenced code block instead, so it's visible
  in Obsidian without leaving the app.
- Don't assume the report's own formatting (headers, tables, error
  numbering) — extract substance, not structure.

## Don't apply without a go-ahead, and iterate first

The author iterates on suggested rewrites before approving them — presenting
a rewrite is not permission to write it. Wait for an explicit go-ahead
("make that swap," "make the replacement") before touching the manuscript
file, even when a review report already contains a fully drafted
Replacement. Expect pushback on specific words or lines across a few
rounds before a fix is approved.

If a finding reveals a cross-chapter continuity conflict (a detail
described two different ways in two chapters), don't silently pick a
side — surface both established versions with citations and ask which one
is canon. Once decided, apply the fix to every affected chapter with a
matching, cross-linked Changelog entry in each.

If an edit changes an established voice trait or a recurring detail (not
just a one-off line), check whether that fact also lives in the codex
(the character's `Voice.md`, or `codex/plot/Motifs.md` for a vault-wide
recurring detail) and update it there too, alongside the manuscript and
changelog.
