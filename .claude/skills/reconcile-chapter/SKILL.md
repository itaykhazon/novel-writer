---
name: reconcile-chapter
description: Bring a chapter's records in line with the prose that actually landed — chapter frontmatter, Summary.md, the arc index, the outline and thread files, the codex, and a numeric cross-check that the same value appears everywhere it is stated. Use after draft-chapter, after applying review fixes, or any time a chapter's prose has changed and the vault's records still describe the plan. This skill never writes or edits manuscript prose.
---

# Reconcile a Chapter's Records

The vault is a local folder (this skill's working directory, or the folder
the user points you at) — read and write its files directly.

`draft-chapter` writes prose and deliberately leaves every record stale. This
skill closes that gap. It is the accounting half of drafting, split out so that
neither job is done while distracted by the other.

**This skill never edits manuscript prose.** If reconciling surfaces a problem
that can only be fixed in the prose — a contradiction with established canon, a
number that cannot be made consistent — report it and stop. Prose fixes go
through `draft-from-review` or `chapter-cycle`, with the user's approval.

## 1. Read the finished prose

Read the chapter file itself, in full. Everything below is derived from what is
on the page, not from `Outline.md` and not from the planned `Summary.md` — those
are predictions, and the point of this skill is to replace predictions with
facts.

As you read, build one working list: every **quantitative or categorical claim**
the chapter makes — percentages, counts, ranks, tiers, placements, distances,
elapsed time, resource levels. Note the value and where it appears. This list is
the input to step 5 and it is much cheaper to build now, in one read, than to
reconstruct later.

Also note: who actually appears (versus who the outline predicted), where the
chapter actually goes, which planned beats actually landed, and anything the
chapter introduced that has no codex entry.

## 2. Chapter frontmatter

Update `characters:` and `locations:` to who and what actually appears. Fill in
`beats:` with the beat codes that actually landed — not what the outline
planned. If a beat was deferred or didn't land as written, the frontmatter
should say what is true now. Confirm `status: draft`.

## 3. `Summary.md`

Rewrite the planned summary as a record of the finished chapter, matching
`codex/templates/Summary Template.md`: scene-by-scene where the chapter has
distinct scenes, plus `**Sets up:**` and, where relevant, `**Open thread —
resolve in a future chapter:**`. Drop `status: planned` from the frontmatter.

Every quantitative or categorical claim here must be **copied from your step 1
list**, not reconstructed from memory or from the outline's plan — those two
routinely differ once a beat has been deepened in the writing. If a value isn't
on your list, go re-read that passage rather than approximating.

Dense and factual. This file exists so a future session can skip the prose.

Leave `Outline.md` in place as the record of the plan.

## 4. The codex and the indexes

- `codex/00 Index.md` — move the chapter from "outlined" into the written list;
  update story position; update open threads (resolve what this chapter
  resolved, add what it opened, carry the rest forward).
- `novel/arc <N>/00 Arc <N> Index.md` — status `outlined` → `draft`.
- `codex/outline/Arc <N> — <Title>.md` — update this chapter's row in the
  "Chapter N Advances" table to what actually landed, and mark any assigned
  beat that didn't land as deferred rather than leaving it claiming an advance
  that didn't happen.
- `codex/outline/Thread <X> — <Title>.md` for every thread this chapter
  touched — update its status line to the chapter's real state. This file (not
  just the arc table) is what a later `add-chapter` run checks before assigning
  that thread's next beat, so a stale status here propagates straight into the
  next chapter's plan.
- `codex/outline/00 Outline Index.md` — update the drafted/outline-only chapter
  range if this chapter changes it.
- `codex/plot/Mystery Discovery Tracker.md` — flip `revealed:` to `true` only
  for discoveries that actually landed on the page.
- `codex/plot/Macro Progression.md` — update `manuscript-status`, and the phase
  itself if the story has moved into a new one.
- Any character, creature, location, or mechanic appearing for the first time
  needs a codex entry — run `add-to-codex` for each. A chapter that introduces
  something new isn't done until that something is findable later. Where such an
  entry states a percentage, count, rank, or other fact this chapter
  established, copy it from your step 1 list so a third independently-worded
  version doesn't get created here.

## 5. Numeric cross-check

Walk your step 1 list. For each load-bearing value, confirm the **same** value
appears, unchanged, in all three places that state it: the prose, the rewritten
`Summary.md`, and any codex page you just touched.

This is the check most likely to be skipped and most likely to drift silently,
because the failure mode is invisible from inside any one file: a value gets
corrected in the prose during review, the Summary keeps the pre-fix number, the
codex agrees with the Summary, and the two of them look mutually confirmed. See
`continuity-reviewer`'s Cross-Artifact Fact Consistency check for why this earns
being a separate mandatory step rather than folded into "read it again."

## 6. Consistency report

Report to the user — **do not fix these yourself**:

- Anything in the prose that contradicts the codex: an ability's limits, a
  location's geography, an established world or institutional rule. Name both
  sides; don't silently override either. The manuscript beats the codex, but
  which one is *wrong* is the author's call.
- Whether the opening lines up physically with the end of the previous chapter.
- Any beat from `Outline.md` that is not on the page.
- Whether the outline's promised progress is reader-visible, and whether the
  chapter's final state is meaningfully different from its opening state.
- Whether every payoff uses a capability the reader was prepared to accept, with
  the outline's limitations and resource costs still enforced.
- Any POV line the POV character couldn't have perceived.
- Which records you changed, and any value the step 5 cross-check corrected.
