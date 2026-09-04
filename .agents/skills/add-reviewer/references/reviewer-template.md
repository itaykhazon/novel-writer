# Reviewer skill template

This file lives as a reference inside `add-reviewer` rather than as its own
skill — it has no `name`/`description` frontmatter and neither Codex nor
Claude Code will list it as invocable. It is the contract every reviewer
skill is expected to satisfy, and what `add-reviewer` scaffolds from when
you create a new one.

A "reviewer" in this vault is any skill whose job is to read manuscript
prose (or, for the two whole-story reviewers, a run of chapters) and produce
a **report** — it never edits manuscript prose itself. Reviewers aren't
grouped into their own subfolder; each lives directly alongside every other
skill (`.agents/skills/<name>/` and `.claude/skills/<name>/`), the same as
`add-chapter` or `chapter-cycle`, so both tools discover and can invoke them
individually by name. What makes a skill a reviewer is its frontmatter, not
its location: `chapter-cycle` discovers the default set by scanning every
sibling skill's `SKILL.md` for the block below and keeping the ones that
declare `reviewer-kind`; `draft-from-review` applies any reviewer's saved
report to the manuscript afterward, whether or not it's in that default
set.

## Required frontmatter

Every reviewer's `SKILL.md` starts with the normal `name:` and
`description:` fields, plus this block:

```yaml
reviewer-kind: line              # line | structural | reader-simulation
reviewer-scope: chapter          # chapter | arc | book
thinking-level: medium           # very-low | low | medium | high
complexity: 5                    # 1-10, relative reasoning/cost load
default-in-cycle: true           # does chapter-cycle run this automatically?
cycle-order: 3                   # only present when default-in-cycle: true
```

- **`reviewer-kind`** — `line`: reads one chapter's prose against a
  fact/craft standard and returns line-anchored findings (the shape
  `draft-from-review` turns into diffs). `structural`: audits architecture
  (plot promise/payoff, arc shape) rather than sentences — still returns
  findings, but they're often not a clean text swap. `reader-simulation`:
  produces a subjective first-read reaction rather than rule-checked
  findings.
- **`reviewer-scope`** — the largest unit the reviewer is designed to read
  in one run. `chapter`: one chapter plus its prebuilt context bundle.
  `arc`: a chapter range or a whole arc's outline/plan. `book`: the entire
  drafted manuscript, or as much of it as the user selects.
- **`thinking-level`** — the recommended reasoning effort for whatever
  model/subagent runs this reviewer, from `very-low` (pattern-matching
  against a fixed rulebook) to `high` (cross-references many facts or
  synthesizes a lot of context with real judgment calls). This is a
  recommendation to whoever invokes the skill, not an enforced setting —
  environments that can't tune effort per-call should ignore it.
- **`complexity`** — a 1–10 gut-check of cost/difficulty, mostly useful for
  comparing reviewers at a glance and for `chapter-cycle` to warn if a
  chapter's review round is about to get unusually expensive (e.g. a
  `default-in-cycle: false` reviewer with `complexity: 9` getting run
  ad hoc against a whole arc).
- **`default-in-cycle`** — whether `chapter-cycle` includes this reviewer in
  its automatic Phase 2 round without being asked. Adding a new reviewer
  never silently makes every `chapter-cycle` run more expensive — it ships
  `false` until someone deliberately flips it on. A reviewer whose
  `reviewer-scope` isn't `chapter` should almost always stay `false`, since
  `chapter-cycle` only ever hands it one chapter's bundle.
- **`cycle-order`** — where this reviewer runs relative to the other
  `default-in-cycle: true` reviewers, lower runs first. Only meaningful (and
  only present) on reviewers that are actually in the cycle. The vault's
  standing order runs structural/factual checks before craft/style checks
  before mechanical checks, on the theory that a chapter likely to need a
  scene-level rewrite from `continuity-reviewer` shouldn't first burn a
  `prose-review` pass on sentences that might not survive — see
  `chapter-cycle/references/review-protocol.md` for the current sequence and
  the reasoning per reviewer.

## Required body sections

A reviewer's prose logic should stay in whatever voice fits the problem it
solves — this vault doesn't want eight reviewers that read like they were
generated from one mold. But every reviewer needs a section that does each
of these jobs, in roughly this order, under a heading close to the name
shown (exact wording can flex to the reviewer's own voice):

1. **Opening paragraph(s)** (no heading) — one or two sentences on what this
   reviewer is for and what it hands back.
2. **`## Required reading`** — what to read before reviewing: reference
   files bundled with the skill, `codex/` files, a POV voice guide, a
   bundled analysis script to run first. Say explicitly what NOT to do here
   too, if the reviewer is meant to work from a prebuilt bundle rather than
   exploring the vault.
3. **`## Scope and boundaries`** — what this reviewer owns, and an explicit
   list of sibling reviewers it defers to for anything adjacent, by name.
   This is the mechanism that keeps eight reviewers from duplicating each
   other's findings on the same passage — skipping it is how that drifts.
4. **`## Severity`** (or `## Confidence and severity`) — the scale this
   reviewer's findings are labeled with (this vault has both a
   HIGH/MEDIUM/LOW and a CRITICAL/WARNING/NOTE convention in use; either is
   fine, but say which one and define each tier).
5. **`## Workflow`** — the numbered steps from "read the input" to
   "return/save the report."
6. **`## Output format`** — the exact report template, including where
   (and under what filename) it gets saved, and what happens for
   input that isn't a saved chapter (an unnamed pasted passage).
7. **`## Hard safeguards`** (or `## Limitations`) — the explicit do-not-do
   list: never edit manuscript prose, never overreach into a sibling
   reviewer's territory, whatever failure modes are specific to this
   reviewer's judgment call.

A reviewer can have more sections than this (worked examples, a pattern
catalog, edge cases, pro tips are all fair game and several existing
reviewers have them) — this is a floor, not a ceiling.

## What lives beside SKILL.md

Optional, add only what the reviewer actually needs:

- `references/` — a catalog, checklist, or framework doc too long to keep
  inline in `SKILL.md` (the ideal is `SKILL.md` stays readable end to end;
  push anything reference-shaped out here and point to it from `## Required
  reading`).
- `scripts/` — a bundled analysis script (a pattern scanner, a codex
  indexer) that does deterministic work cheaper and more reliably than
  asking the model to estimate it. If you add one, say in `## Required
  reading` exactly when to run it and how its output feeds the review.
- `agents/openai.yaml` — Codex-CLI-specific interface metadata
  (`display_name`, `short_description`, `default_prompt`). Optional; only
  add it if you want a nicer Codex-side presentation than the bare skill
  name.

## Keep both trees identical

Every reviewer folder must be byte-identical between `.agents/skills/<name>/`
and `.claude/skills/<name>/` — write to one and copy over the other, then
confirm with `sync-skills`, either for just this reviewer:

```bash
python3 .agents/skills/sync-skills/scripts/diff_skill_dirs.py \
    --a .agents/skills/<name> --b .claude/skills/<name> --single
```

or for the whole tree at once (catches drift anywhere, not just in the
reviewer you just touched):

```bash
python3 .agents/skills/sync-skills/scripts/diff_skill_dirs.py \
    --a .agents/skills --b .claude/skills
```
