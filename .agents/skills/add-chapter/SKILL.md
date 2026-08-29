---
name: add-chapter
description: Set up a new chapter in the {{NOVEL_TITLE}} novel manuscript — folder structure, chapter file with frontmatter, drafts/, a planned Summary.md and a beat-by-beat Outline.md — and update the arc index and codex status. This skill plans a chapter; it never writes chapter prose. Use when the user asks to add, set up, plan, or outline a new chapter for {{NOVEL_TITLE}}. To turn a finished outline into actual prose, use draft-chapter instead.
---

# Add an {{NOVEL_TITLE}} Chapter (planning only)

The vault is a local folder (this skill's working directory, or the folder
the user points you at) — read and write its files directly.

## THE HARD RULE

**This skill does not write chapter prose. Ever.**

The chapter `.md` file this skill creates contains frontmatter, a title heading,
and a placeholder line — nothing else. No scenes, no dialogue, no opening
paragraph, not even "just to show the tone." Writing the chapter is a separate,
explicitly-invoked step (`draft-chapter`).

The deliverable here is a **plan the user can read, argue with, and edit** before
a single word of prose exists. If you find yourself writing a sentence that would
appear in the finished book, stop — it belongs in the outline as a beat, not as
prose.

## 1. Get the chapter number — this is required

Before anything else, confirm the chapter number (and arc, if ambiguous). If the
user didn't give one, ask. Don't guess from "the next one" without checking the
arc index — and don't proceed on a number that already exists without confirming
whether they mean to replace, renumber, or restructure.

The title can be provisional; the number can't.

## 2. Find the direction

If the user gave content instructions, those win. Whether they did or not, read
for direction before outlining:

1. `codex/00 Index.md` — manuscript status and, critically, the **open threads**.
   A new chapter should resolve an open thread or knowingly carry it forward.
2. `codex/plot/Macro Progression.md` — the global outline. Find where
   this chapter number sits in the phase sequence, and what that phase says has
   to happen. This is the primary source of direction when the user is vague.
3. `codex/outline/Sanderson Method — {{NOVEL_TITLE}} Working Guide.md` — the project's
   plotting diagnostic. Read it when planning every chapter, but put only the
   chapter-specific conclusions in `Outline.md`; do not copy the guide itself.
4. The previous chapter's `Summary.md` (not the full chapter) for immediate
   continuity — where everyone physically is, what just happened, what was
   promised.
5. `codex/Genre.md` and `codex/Writing Style.md` — always in effect.
6. `codex/plot/Mystery Discovery Tracker.md` if the chapter is anywhere
   near a reveal.

Then state, in one or two sentences to the user, the direction you derived and
where it came from ("Phase Two says the formal the team assignment is still
unwritten, and Ch6 left the Scout's scream unresolved — so this chapter is X").
If the codex and macro outline genuinely don't point anywhere for this slot, ask
the user rather than inventing a direction. If more than one or two related
things are undecided at once (the chapter's purpose *and* its ending beat *and*
who it's meant to spotlight, say), don't ask them one at a time — run the
`grilling` skill to settle the batch together.

## 3. Create the folder structure

Under `novel/arc <N>/`:

```
novel/arc <N>/Chapter <n> - <Title>/
  Chapter <n> - <Title>.md   ← frontmatter + placeholder only at this stage
  Outline.md                 ← the beat sheet; this is the main output
  Summary.md                 ← planned summary (status: planned)
  drafts/                    ← prior versions, once there are any
```

The Prologue uses the folder name `Chapter 0 - Prologue`. Create `drafts/` with a
plain `mkdir`.

**If restructuring an existing chapter that already has prose:** copy the current
file into `drafts/` with a dated name (`v1 - 2026-08-14.md`) *before* touching
the live file.

## 4. The chapter file

**Open `codex/templates/Scene Frontmatter Template.md` and copy its frontmatter
verbatim** — don't retype it from memory or from this document. The template is
the source of truth for which fields a chapter needs; an inline example here
would just be a second copy that can silently drift out of sync with the
template the way it previously did (the template already defines `beats:`,
`timeline:`, `time-of-day-start:`, `time-of-day-end:`, and `estimated-duration:`,
and every one of them needs to actually land in the chapter file, not just
exist in the template unused). Fill in every field the template defines:

- `beats:` — the beat codes this chapter is meant to advance, taken from step 5
  below (e.g. `beats: [A4, B1, C3, E1]`). Leaving this empty defeats
  `continuity-reviewer`'s beat-advancement check, which depends on it.
- `timeline:` and `estimated-duration:` — even a rough estimate ("same day as
  Ch 6, evening" / "under 3 hours") is enough for `continuity-reviewer` to
  sanity-check whether the beats you're assigning can plausibly fit.
- `status: outlined` — the pre-prose state. (If the template's own status
  comment doesn't list `outlined` as an option, that's the template lagging
  behind actual usage — `draft-chapter` flips this to `draft` later, and
  every existing outlined-but-undrafted chapter already uses this value, so
  don't invent a different word for it.)

Then:

```markdown
# Chapter <n> — <Title>

*Not drafted yet. See [[Outline]] in this folder. Run `draft-chapter` to write it.*
```

Characters and locations come from the planned outline — use exact note
names from `codex/characters/00 Characters Index.md` and
`codex/locations/00 Locations Index.md`. If something in the plan has no codex
entry, note it for the user; creating it can wait until it actually lands on the
page, but a genuinely new named character or location is worth running
`add-to-codex` for now.

## 5. Write `Outline.md` — the real work

This is what the user reviews. Make it specific enough that drafting is
execution, not invention, and short enough to read in a minute.

```yaml
---
type: outline
chapter-file: "[[Chapter <n> - <Title>]]"
status: draft-ready | needs-input
---
```

Then:

- **Purpose** — one line: what this chapter does for the book. Which thread it
  resolves, advances, or opens.
- **Continuity in** — where each character physically and emotionally is at the
  first line, carried from the previous `Summary.md`.
- **Foreshadowed payoffs** — if this chapter is meant to pay off something planted
  in an earlier chapter (an item, ability, mechanic, or detail flagged
  `do not know what it does yet` or similar, per `codex/00 Index.md` open threads
  or the source chapter's own text), quote its established description *verbatim*
  from the chapter that introduced it — the exact color, material, or phrasing
  used on the page, not a paraphrase. Drafting must reuse that description rather
  than inventing a new one. If the codex's own note already blends two different
  descriptions together (a slash-compound like "gold/metallic fragment" is the
  tell), that means the earlier chapters may already disagree — resolve which
  description is correct with the user before outlining the payoff, rather than
  letting a third version get invented at draft time.
- **Beats** — numbered, scene-grouped. Each beat is one line of *what happens*
  and, where it matters, *what it costs or reveals*. Include the intended
  chapter-ending note (cliffhanger, quiet beat, hard cut).

  **Before assigning a beat number, check it forward, not just backward.** Read
  the *full* `codex/outline/Thread <X> — <Title>.md` file for every thread a
  beat touches — not only which beats earlier chapters already claimed, but
  which beats **already-outlined future chapters** claim, and in what order.
  Assigning, say, B4 in this chapter is only safe if no later chapter's
  existing `Outline.md` or arc table already assumed B2/B3 would happen
  *first*. If this chapter's beats would land out of the order a later,
  already-planned chapter assumes, that's a real conflict — surface it to the
  user and resolve the thread's intended order before finishing this outline,
  rather than leaving two outlines that silently disagree about sequence for a
  future audit to find. (This is exactly the failure mode the 2026-08-15
  Story So Far audit found: Chapters 8–9 assigned B4/B5 while Chapters 10–13's
  existing outlines and Arc 2's outline still treated B2/B3/B5 as happening in
  the original order.)
- **On the page for the first time** — any character, creature, location, or
  mechanic that debuts here, with a `[[link]]` and a flag if it has no codex
  entry yet.
- **Constraints** — codex facts the prose must not violate (an ability's
  limits, a distance, an established world/institutional rule), and anything the user explicitly asked for.
- **Sanderson pass** — a compact structural contract for the drafter and
  reviewers. Include each line below; answer `none intentionally` rather than
  omitting a category that does not move in this chapter:

  ```markdown
  ## Sanderson pass

  - **Promise renewed:** [reader expectation this chapter keeps alive]
  - **Reader-visible progress:** [external / information / relationship / internal / mastery change, plus how the reader notices]
  - **Small payoff:** [what pays here, or none intentionally]
  - **Larger payoff prepared:** [future result this sets up]
  - **POV want and value:** [immediate goal; value shaping the method]
  - **Try–fail / escalation:** [attempt, resistance, complication or cost, changed approach]
  - **Existing element deepened:** [mechanic, culture, relationship, location, or System rule]
  - **Resource and limitation budget:** [heat, ammunition, mass, injury, time, knowledge, authority]
  - **End-state change:** [what cannot be reset to the chapter's opening state]
  - **LitRPG progression:** [level/rank/tier/debt/equipment/team mastery, or none intentionally]
  ```

  A beat code is not itself reader-visible progress. Name the action,
  realization, changed behavior, evidence, or mastery signpost that makes the
  advance perceptible without consulting the outline.
- **Open questions** — decisions you did not make. If there's just one, put it
  to the user directly. If there are several and they're related (a payoff's
  exact cost, who pays it, and how it changes the ending all hang together, for
  instance), run the `grilling` skill on them as a batch before finalizing the
  outline, rather than dumping an unsorted list. Whatever's still genuinely
  open after that, set `status: needs-input` and list it here rather than
  picking silently.

Set `status: needs-input` when a major payoff depends on an ability or resource
that has not been established or earned, when the chapter's claimed progress
has no reader-visible signpost, when a major choice has no meaningful
alternative or cost, or when the chapter repeats the previous chapter's
dramatic function without transforming it.

Beats describe events. If a beat contains quotable dialogue or a rendered image,
it's drifted into prose — cut it back.

## 6. Write `Summary.md` (planned)

Same shape as the existing summaries (see `novel/arc 1/Chapter 6 - The
Shooter/Summary.md`), written in the future-facing register of a plan, with
`status: planned` so nobody mistakes it for a record of written prose:

```yaml
---
type: summary
chapter-file: "[[Chapter <n> - <Title>]]"
status: planned
---
```

Keep the `**Sets up:**` and `**Open thread:**` callouts — dense and factual, not
evocative. `draft-chapter` rewrites this from the finished prose and drops
`status: planned`.

## 7. Update the indexes

- `novel/arc <N>/00 Arc <N> Index.md` — add the row with status `outlined`.
  Create the index using `codex/templates/Arc Index Template.md` if the arc is new.
- `codex/00 Index.md` — add the chapter to manuscript status marked **outlined,
  not yet written**, and note which open thread it's aimed at. Do not mark a
  thread resolved and do not flip anything in
  `codex/plot/Mystery Discovery Tracker.md` — a discovery is only revealed
  once it's on the page, which hasn't happened yet.
- `codex/plot/Macro Progression.md` — only update `manuscript-status`
  if the *plan* changes what's true about the manuscript; the phase itself moves
  when prose does.
- `codex/outline/Arc <N> — <Title>.md`'s "Chapter N Advances" table and the
  relevant `codex/outline/Thread <X>` status line — add this chapter's planned
  beats here too, at plan time, not just after drafting. This is the file the
  forward-order check in step 5 reads, and it needs to already reflect this
  chapter's plan for the *next* chapter's outline to check against correctly.

## 8. Consistency check, then stop

Does the outline contradict anything in the codex — a stated ability, a
geography, a rule? Flag it to the user rather than silently overriding either
side. Include foreshadowed payoffs in this check: if "Foreshadowed payoffs"
above cited a source chapter, confirm the description you quoted into the
outline is the one actually on the page there, not the codex's summary of it —
codex bullets sometimes already paraphrase or blend multiple chapters' wording
(see `continuity-reviewer`'s item-consistency check for what that looks like).

Also confirm the forward-order beat check from step 5 didn't turn up an
unresolved conflict — don't finish with a known thread-order contradiction
left silent.

Finally, verify the Sanderson pass against the actual beats: the promised
progress must be visible in an event or choice; the end-state must genuinely
differ; and any climactic solution must obey the stated resource/limitation
budget. Do not solve a weak outline by inventing an unseeded ability.

Then finish. Report: the folder created, the direction you derived and its
source, and any open questions. End by telling the user to review `Outline.md`
and run `draft-chapter` when they're happy with it.

Do not offer to "go ahead and write it now." The separation is the point.
