---
name: add-reviewer
description: |
  Scaffold a new reviewer skill under reviewers/ — a skill that reads manuscript prose (or a run of chapters) and produces a report — conformant to reviewers/TEMPLATE.md, in both .agents/skills and .claude/skills. Interviews the user for what the reviewer checks and where it fits (reviewer-kind, scope, thinking-level, complexity, whether chapter-cycle should run it automatically and in what order), scaffolds the frontmatter and section skeleton, then writes the reviewing logic itself. Use when the user asks to add a new reviewer, a new review skill, or a new craft/continuity/structural/audience check to the review pipeline.
---

# Add a Reviewer

This skill exists so a ninth (or twelfth) reviewer costs one careful pass
through this file instead of someone improvising a `SKILL.md` that's missing
the section `chapter-cycle` or `draft-from-review` silently depends on.
Everything under `reviewers/` — the eight that ship with this vault and
whatever gets added after — has to satisfy the same contract for those two
skills to keep working without special-casing anything.

## 0. Read the template first

Read `reviewers/TEMPLATE.md` in full before anything else. It's the contract
this skill scaffolds against and the source of truth for every "required"
below — this file summarizes it, TEMPLATE.md is authoritative if the two ever
disagree.

## 1. Establish what this reviewer actually owns

Ask the user, in plain language if they haven't already said it: what should
this reviewer catch that nothing under `reviewers/` already catches?

Then check that it's actually new territory. Run
`python3 chapter-cycle/scripts/list_reviewers.py --all` to see every existing
reviewer's kind and scope, and read the "Scope and boundaries" section of any
that sound adjacent to the new idea. If what's being proposed is really a
corner of an existing reviewer's job, say so and suggest expanding that
reviewer's scope instead of creating a new one — a ninth reviewer only earns
its cost (a whole extra pass over the chapter, every time it runs) if it owns
something none of the other eight do. This isn't a formality to rush past;
it's the check that keeps the set from bloating into overlapping reviewers
that all flag the same sentence for slightly different stated reasons.

## 2. Grill the open decisions

Use `grilling` to settle these as one batch — they're independent of each
other and none of them depends on anything not already known from step 1, so
this is a single round, not a multi-round dependency tree:

1. **Name** — kebab-case, e.g. `dialogue-tag-review`. Suggest one derived from
   what step 1 established.
2. **`reviewer-kind`** — `line` | `structural` | `reader-simulation`. Suggest
   based on what step 1 established (see `reviewers/TEMPLATE.md` for what each
   means).
3. **`reviewer-scope`** — `chapter` | `arc` | `book`. Suggest based on the
   largest unit the reviewer actually needs to read to do its job.
4. **`thinking-level`** — `very-low` | `low` | `medium` | `high`. Calibrate the
   suggestion against the existing eight: pattern-matching against a fixed
   rulebook (`proofread`) is `very-low`; cross-referencing many facts or a real
   judgment call (`continuity-reviewer`) is `high`.
5. **`complexity`** — 1–10. Same calibration; the current default set runs
   from 1 (`proofread`) to 8 (`continuity-reviewer`, `sanderson-review`).
6. **`default-in-cycle`** — `true` | `false`. Suggest `false` unless the user
   is confident this should run on *every* `chapter-cycle` invocation from now
   on. It's cheap to flip on later once the reviewer's proven itself standalone
   a few times; it's an unwelcome surprise to discover an expensive reviewer
   quietly running on every chapter because it defaulted to `true`.

If `default-in-cycle` comes back `true`, run one more short round: show the
current order (`python3 chapter-cycle/scripts/list_reviewers.py`) and ask
where the new reviewer slots in. Suggest a position using the standing rule
from `chapter-cycle/references/review-protocol.md` and
`reviewers/TEMPLATE.md`'s `cycle-order` section — structural/factual checks
before craft/style checks before mechanical ones — as the default, but the
user's call wins.

## 3. Scaffold the files

Run the bundled script with what step 2 settled:

```bash
python3 add-reviewer/scripts/scaffold_reviewer.py \
    --name <name> \
    --description "<the frontmatter description: what it checks, when to use it>" \
    --reviewer-kind <line|structural|reader-simulation> \
    --reviewer-scope <chapter|arc|book> \
    --thinking-level <very-low|low|medium|high> \
    --complexity <1-10> \
    --default-in-cycle <true|false> \
    [--cycle-order <n>]   # required iff --default-in-cycle true
```

It refuses if the name already exists in either tree. It writes
byte-identical skeleton `SKILL.md` files to both
`.agents/skills/reviewers/<name>/` and `.claude/skills/reviewers/<name>/` —
frontmatter filled in, every required `reviewers/TEMPLATE.md` section stubbed
with an HTML comment describing what belongs there. If the reviewer is
entering the cycle, it also shifts every existing default-in-cycle reviewer at
or after that slot down by one, in both trees, so `cycle-order` stays a clean
sequence without any hand-renumbering.

## 4. Write the review logic

This is the part scaffolding can't do — delete each stub comment as you
replace it with real content:

- **Required reading** — what this reviewer reads before judging anything:
  bundled `references/`, relevant `codex/` files, a bundled analysis script to
  run first. If it's meant to work from a prebuilt bundle (like the
  `chapter-cycle` default set does) rather than exploring the vault, say that
  explicitly.
- **Scope and boundaries** — write down what step 1's overlap check found, so
  the boundary doesn't drift back into a sibling's territory the next time
  someone reads this file. If the new reviewer takes something a sibling used
  to implicitly cover, add a mirroring note to *that* sibling's own "Scope and
  boundaries" section too — otherwise the two will start duplicating findings
  on the same passage, which is exactly what this section exists to prevent.
- **Severity** — pick HIGH/MEDIUM/LOW or CRITICAL/WARNING/NOTE, whichever
  fits this reviewer's own judgment calls better, and define each tier.
- **Workflow** and **Output format** — follow the existing reviewers' pattern
  (see `proofread`'s or `pacing-review`'s `## Where to Save` / output section)
  so the report lands in `reviews/` under a name `draft-from-review` can find
  and apply the same way it does for every other reviewer.
- **Hard safeguards** — at minimum, state that this reviewer reports only and
  never edits manuscript prose; every existing reviewer says this, and this
  one should too.

Write the content once and copy it over the other tree rather than retyping it
by hand a second time — that's how the two trees drift.

## 5. Verify and report

```bash
python3 .agents/skills/sync-skills/scripts/diff_skill_dirs.py \
    --a .agents/skills/reviewers --b .claude/skills/reviewers
```

If `default-in-cycle: true`, also run
`python3 chapter-cycle/scripts/list_reviewers.py` (either tree — they agree)
to confirm the new reviewer appears in the intended slot and nothing else's
`cycle-order` collided with it.

If the new reviewer is `default-in-cycle: true`, also update `README.md`: the
`chapter-cycle` bullet under "The workflow, end to end" names the current
default set, and that line needs the new reviewer added. If it's opt-in,
add it to the "Supporting skills" paragraph instead, the same way the existing
opt-in reviewers (`sanderson-review`, `target-audience-readthrough`,
`prose-smell-review`) are described there.

Tell the user: the reviewer's name, whether it's in the default cycle and at
what position (or, if not, how to run it standalone — hand it the chapter/arc
and the relevant context, the same as `chapter-cycle` does for the ones it
runs automatically), and which sibling reviewer's "Scope and boundaries" you
updated, if any, per step 4.

## What NOT to do

- Don't set `default-in-cycle: true` without the user explicitly confirming
  it — see step 2.
- Don't invent a reviewer's checks from nothing. If step 1 didn't produce a
  clear "this is the gap none of the other eight cover," say so and ask,
  rather than padding a thin idea out into all seven required sections.
- Don't skip reading `reviewers/TEMPLATE.md`, even for a reviewer that feels
  similar to an existing one — the required sections (especially "Scope and
  boundaries") are the mechanism that keeps a new reviewer from silently
  duplicating an existing one's findings.
- Don't hand-edit `cycle-order` on other reviewers when inserting a new one
  into the cycle — `scaffold_reviewer.py` does that shift for you, correctly,
  in both trees at once. Hand-editing it risks leaving the two trees out of
  sync with each other.
