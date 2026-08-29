---
name: draft-chapter
description: Write the actual prose of an {{NOVEL_TITLE}} chapter from its existing Outline.md, in the established voice, then update Summary.md, the arc index, and the codex to reflect what landed on the page. Use when the user asks to write, draft, or flesh out a chapter that has already been outlined (typically after add-chapter), or to rewrite an existing chapter from its outline. If no outline exists yet, use add-chapter first.
---

# Draft an {{NOVEL_TITLE}} Chapter from its Outline

The vault is a local folder (this skill's working directory, or the folder
the user points you at) — read and write its files directly.

This skill is the second half of the pair. `add-chapter` plans; this one
writes. It assumes the plan is settled — the outline is the brief, not a
suggestion.

## 1. Locate the chapter and its outline

Confirm which chapter (number, and arc if ambiguous). Then read, in this order:

1. `novel/arc <N>/Chapter <n> - <Title>/Outline.md` — **required**. If there is
   no `Outline.md`, stop and offer to run `add-chapter` first. Don't
   improvise a chapter that was never planned.
2. That folder's `Summary.md` (the planned one) for the intended shape.
3. The previous chapter's `Summary.md` for continuity, and the last ~1000 words
   of the previous chapter's actual prose for voice and immediate handoff — if
   this chapter continues directly from a cliffhanger, read enough to match the
   physical situation exactly.
4. `codex/Genre.md` and `codex/Writing Style.md`.
5. Codex entries for every character, mechanic, creature, and location the
   outline lists — abilities and limits have to be right on the page.

If `Outline.md` has `status: needs-input`, resolve its open questions with the
user before writing a word.

Before drafting, read its `## Sanderson pass`. For an older outline that lacks
one, perform the same compact preflight from
`codex/outline/Sanderson Method — {{NOVEL_TITLE}} Working Guide.md` without rewriting the
approved plan: identify the promise, reader-visible progress, POV want,
try–fail/escalation, payoff, end-state change, and resource/limitation budget.
If the climax needs an unestablished ability, unavailable resource, or missing
setup, stop and surface the plan problem before prose makes it canon.

## 2. Voice

`codex/Writing Style.md` is the source of truth for every line you write — read it fully, don't rely on this summary. It's genre- and POV-agnostic by design: your novel might be third-limited or first-person or omniscient, past or present tense, single-POV or multi-POV, lean and fast or dense and literary. Whatever it specifies, in force for every line:

- Hold the POV/narrative-distance convention it specifies exactly — if it's close POV (first person, third-limited), never include an observation that POV character couldn't make; if it's omniscient, hold whatever discipline the file specifies for that instead.
- **If `codex/Writing Style.md` specifies a scene/chapter-opening convention (e.g. opening on the POV character's name), treat it as a firm house rule, not a stylistic nudge, and check it on every line you write.** If the file specifies no such convention, don't invent one.
- No clichés. If a phrase feels available, it's probably worn.
- Varied sentence length; pacing and rhythm matched to what `codex/Writing Style.md`/`codex/Craft Influences.md` (if populated) actually establish as this novel's target — don't assume "fast" or "cinematic" unless that's what's actually declared.
- Sharp dialogue that does work — characterization, information, or pressure.
  Cut lines that only fill air.
- Render scenes the way `codex/Writing Style.md`'s register calls for — that may mean cinematic and action-forward, or it may mean something slower and more interior. Follow what's actually declared rather than a default assumption.
- Follow the genre and tone recorded in `codex/Genre.md` and `codex/Writing
  Style.md` — including any in-fiction system/UI text format, if your novel
  uses one — matching the format already used in earlier chapters rather than
  reinventing it per chapter.

Match the existing chapters' scale: roughly 3,000–5,000 words, scene-broken the
way earlier chapters break.

## 3. Write it

Preserve prior work first: if the chapter file already contains prose, copy it
into `drafts/` as `v<N> - <YYYY-MM-DD>.md` before overwriting.

Write the full chapter into `novel/arc <N>/Chapter <n> - <Title>/Chapter <n> -
<Title>.md`, keeping the frontmatter and setting `status: draft`. Update
`characters:` and `locations:` to who and what actually appears — the outline was
a prediction; the prose is the fact. Fill in `beats:` with the beat codes that
actually landed on the page (not just what the outline planned — if a beat was
deferred or didn't land as written, the frontmatter should say what's true now).

Build the file across a few passes rather than one enormous write: structure and
scene breaks, then prose scene by scene. For a long chapter, write scenes in
order so continuity holds.

While drafting, keep a short scratch ledger for each scene: POV goal,
resistance/escalation, reader-visible progress signpost, exit-state change, and
any finite resource spent or regained. This is working memory, not a new vault
artifact. A beat does not land merely because the planned event occurred; the
reader must be able to perceive what changed.

Follow the outline's beats in order. You may deepen a beat, add connective
tissue, or find the specific words for a moment. You may not drop a beat, add a
new plot event, introduce a character the outline doesn't have, or change the
ending. If a beat turns out not to work in prose — the physical logistics don't
hold, two beats collapse into one, the ending lands flat — say so and get the
user's call rather than quietly rewriting the plan.

Respect the outline's **Constraints** section absolutely.

Any number that ends up on the page — a percentage, a count, a rank — is the
canonical value the moment you write it. Note it in your own head (or a scratch
list) as you go, so step 4's Summary rewrite quotes the same values instead of
independently re-deriving or rounding them.

## 4. Update `Summary.md` from what you actually wrote

Rewrite the planned summary as a record of the finished chapter, matching the
structure of `codex/templates/Summary Template.md`: scene-by-scene
where the chapter has distinct scenes, plus `**Sets up:**` and, where relevant,
`**Open thread — resolve in a future chapter:**`.

Every quantitative or categorical claim in the Summary (a percentage, a count,
a rank tag, a placement) must be copied from what the prose actually says at
that point, not reconstructed from memory or from the outline's plan — those
two can differ once you've deepened a beat in the writing. If you can't quickly
verify a number against the prose while rewriting the Summary, that's a sign to
go re-read that passage, not to approximate.

Drop `status: planned` from the frontmatter. Dense and factual — this file exists
so a future session can skip the prose.

Leave `Outline.md` in place as the record of the plan.

## 5. Update the codex — the chapter isn't finished until this is done

- `codex/00 Index.md` — move the chapter from "outlined" into the written list;
  update story position, and update the open threads: resolve what this chapter
  resolved, add what it opened, carry the rest forward.
- `novel/arc <N>/00 Arc <N> Index.md` — status `outlined` → `draft`.
- `codex/outline/Arc <N> — <Title>.md` — update this chapter's row in the
  "Chapter N Advances" table to what actually landed (not what was planned),
  and mark any assigned beat that didn't land as deferred rather than leaving
  it claiming an advance that didn't happen.
- `codex/outline/Thread <X> — <Title>.md` for every thread this chapter
  touched — update its status line to the chapter's real state. This file
  (not just the arc table) is what a later `add-chapter` run checks
  before assigning that thread's next beat, so a stale status here propagates
  into the next chapter's plan.
- `codex/outline/00 Outline Index.md` — update the drafted/outline-only chapter
  range if this chapter changes it (e.g. "Chapters 8–64 are outline only"
  needs to become "9–64" once Chapter 8 is drafted).
- `codex/plot/Mystery Discovery Tracker.md` — now you may flip `revealed:`
  to `true`, but only for discoveries that actually landed on the page.
- `codex/plot/Macro Progression.md` — update `manuscript-status`, and
  the phase itself if the story has moved into a new one.
- Any character, creature, location, or mechanic that appeared for the first time
  needs a codex entry — run `add-to-codex` for each. A chapter that
  introduces something new isn't done until that something is findable later.
  If that codex entry states a percentage, count, rank, or other fact this
  chapter established, copy it from the same verified value used in step 4 —
  don't let a third, independently-worded version get created here.

## 6. Consistency check before finishing

- Does the prose contradict anything established in the codex — an ability's
  limits, a location's geography, an established world/institutional rule? Flag it to the user; don't
  silently override either the codex or the draft.
- Does the opening line up physically with the end of the previous chapter?
- Is every beat from `Outline.md` on the page?
- Is the outline's promised progress reader-visible, and is the chapter's final
  state meaningfully different from its opening state?
- Does every payoff use a capability the reader has been prepared to accept,
  with the outline's limitations and resource costs still enforced?
- POV discipline: any line the POV character couldn't have perceived?
- **Numeric/fact spot-check:** pick two or three of the chapter's most
  load-bearing quantitative facts (a percentage sequence, an ammo count, a
  creature's rank tag) and confirm the same value appears, unchanged, in the
  prose, the rewritten `Summary.md`, and any codex page you just updated for
  them. This is the check that's easiest to skip under time pressure and the
  one most likely to silently drift — see `continuity-reviewer`'s
  Cross-Artifact Fact Consistency check for why it matters even when this
  chapter's own review pass looks clean.

Report: word count, scene breakdown, anything you deviated from in the outline
(and why), any codex conflicts, and any new entities that still need codex
entries. Offer to run the `proofread` skill on the finished chapter.
