---
name: pacing-review
description: |
  Review chapter/scene-level PACING — the rate tension, information, and story-time are delivered, and whether it matches what each moment needs. Flags DRAGGING (static scenes, redundant introspection, conflict that never escalates, stalled description) and RUSHED (major beats with no reaction, conflict resolved with no resistance, skipped setup, beats crammed together) — every finding includes a drafted Replacement, not just a diagnosis. STRUCTURAL/SCENE-LEVEL pass, distinct from prose-review (sentence rhythm/voice) and continuity-reviewer (facts/timeline). Use when asked to review pacing, check if a chapter drags or feels rushed, wants a pacing report/map, asks "does this move too fast/slow," or wants action-vs-reflection balance feedback. Also use proactively after drafting a new {{NOVEL_TITLE}} chapter, alongside proofread/prose-review/continuity-reviewer, even if the user just says "review this chapter."
---

# Pacing Review for {{NOVEL_TITLE}}

This skill reviews **pacing**: whether the rate a chapter delivers tension, information, and story-time matches what each moment is asking for. It's the level above prose-review's sentence rhythm and below continuity-reviewer's fact-checking — it asks "does this scene earn its length, and does the next one pick up where the tension left off?" rather than "is this sentence built right?" or "does this contradict the codex?"

Require the chapter text. Use beat/timeline frontmatter and `Outline.md` when
available; an outline's `## Sanderson pass` supplies the intended promise,
reader-visible progress, payoff, and end-state change.

## Why this skill exists (read before applying rules)

**Before applying any rule below, read `codex/Genre.md`, `codex/Writing Style.md`, and `codex/Craft Influences.md`** (if `populate-project` has been run, the latter names this novel's actual comp titles and, where researched, how their pacing differs — a slow, texture-forward influence and a lean, propulsive one call for different judgment calls, and most novels blend more than one). Whatever the declared register is, it rarely means a single fixed speed throughout the book — a genre brief that says "fast-paced" is usually describing the book's floor or its action-scene register, not a mandate that literally every scene move at the same clip. Recalibrate everything below to the register your novel's own reference files actually declare, rather than assuming any particular genre.

So "fast" isn't automatically a synonym for "good pacing," and this skill should not push every slower scene toward speed just because part of the genre brief says fast-paced. A story moving at one speed forever is exhausting in the same way a story that never moves is boring. In most genres, the deliberate scenes (politics, worldbuilding, relationship beats, a character actually reckoning with what just happened) are load-bearing, not automatically padding to be trimmed toward the action average — though a genre or house style genuinely built for constant momentum (a thriller, for instance) may legitimately want less of this; that's exactly the kind of call `codex/Writing Style.md`/`Craft Influences.md` should settle. Good pacing is **variable pacing that tracks the story's own tension curve**: scenes tighten as stakes rise, then give the reader (and the characters) a beat to process before the next push, in proportion to what the declared style actually wants. A chapter that's wall-to-wall action reads as noise because nothing had room to matter; a chapter that's wall-to-wall reflection with no forward pressure at all reads as stalled because nothing is actually at risk in the reading present. The judgment call this skill exists to make is which of those two failure modes a given scene is actually in — not "is this scene slow," but "is this scene earning its slowness, for *this* novel's declared style."

The craft frame this skill is built on (Dwight Swain's scene/sequel structure, the standard model behind most modern pacing advice) names the two halves explicitly:

- **Scene** = Goal → Conflict → Disaster. A character wants something concrete, something opposes them and the opposition escalates, and the scene ends on an unanticipated outcome (a flat "no," or a "yes, but" that creates new trouble). This is what makes a scene feel like it's *moving*.
- **Sequel** = Reaction → Dilemma → Decision. The character (and reader) processes what just happened, weighs the bad options left, and picks one — which becomes the next scene's Goal. This is what makes a disaster *matter* instead of just being the next thing that happened.

Most pacing problems are one of these two structural pieces missing or overstaying: a Scene with no Disaster (conflict just... resolves), a Disaster with no Sequel (huge event, zero reaction, next paragraph is already the next thing), or a Sequel with no Decision (the character stews for pages without the stew producing a choice that moves forward). Keep that frame in mind for edge cases the rules below don't name explicitly.

**Division of labor with the other reviewers**, so findings don't duplicate:
- **prose-review** owns sentence/paragraph-level wording — fragment runs, sentence length variation, filter words, voice. If a passage's problem is purely *how a sentence is worded* (not what beats are present or missing), note that pacing-review saw a symptom but let prose-review own the word-level polish.
- **continuity-reviewer** owns whether elapsed time is *factually* plausible (travel times, whether 2 hours is enough for an overnight-feeling beat). Pacing-review owns whether the *narrative weight* given to a beat matches its dramatic importance, regardless of whether the clock math checks out.
- **pacing-review** owns: scene/sequel structure, escalation, reaction-beat presence, information pacing (setup vs. payoff), and the overall tension curve of the chapter — **and it drafts the fix, not just the diagnosis.** Every finding needs a concrete Replacement: an actual reaction beat to insert, actual text to cut, an actual compressed version of a stretch that's dragging. A pacing report is only as useful as its worst finding's fix — "add more reaction here" leaves the writer with the same blank page; a drafted sentence or two of Alex (or the scene's actual POV character) reacting gives them something to react to, edit, or reject. Match the POV character's voice as best you can (see prose-review's rule 2 on free indirect discourse for the target register) — it doesn't need to be publication-final (that's what a follow-up prose-review pass on the applied fix is for), but it must be a real, usable draft, not a placeholder description.

## Rules and issue types

Every finding is one of two directions — **RUSHED** (moving faster than the moment can support) or **DRAGGING** (moving slower than the moment earns) — plus a severity (HIGH / MEDIUM / LOW) for how much it costs the reading experience.

### RUSHED — the story is moving faster than a moment can support

**R1. Disaster with no Sequel (HIGH).** A major event lands — a death, a betrayal, a big reveal, a costly decision — and the very next beat is already the next plot point, with no reaction from the POV character. The reader (and the character) never gets to feel it, which drains the event of weight no matter how well the event itself was written.
- Check: after any beat you'd call "big" if summarized in one line, is there at least a sentence or paragraph of reaction before the story moves on? If the chapter's `beats:` frontmatter or Outline.md is available, treat each listed beat as a candidate for this check.
- Fix: draft the missing reaction beat — a sentence or short paragraph, in the POV character's voice, inserted between the disaster and what currently follows it.

**R2. Conflict resolved without escalation (HIGH).** A Scene's Conflict should get harder before it breaks (Goal → resistance → worse resistance → Disaster). If the opposition appears and is overcome in the same breath — no second attempt, no complication, no cost — the scene reads as a formality rather than something that was actually in doubt.
- Fix: draft one added complication or cost between the opposition appearing and it being overcome — something that makes the win less clean or the attempt take a real try.

**R3. Setup skipped, so a twist or stake doesn't land (MEDIUM-HIGH).** The reader needs to know what's at risk *before* the moment that risks it, or a reveal reads as arbitrary instead of a payoff. If a beat depends on information, a relationship, or a stake the reader hasn't been given yet, the speed itself is the problem — no amount of dramatic writing at the moment of payoff fixes a setup gap.
- Fix: draft a short earlier insertion (a line, a beat) that plants the missing piece before the payoff moment, and name exactly where upstream it should land.

**R4. Multiple major beats crammed into too little chapter-space (MEDIUM).** If several beats that each deserve independent weight (per the outline, or per their own dramatic size) are stacked back-to-back with no breathing room between any of them, the chapter as a whole reads as rushed even if each individual sentence is fine. This is a chapter-shape problem, not a single-passage one — flag it as structural (see Output Format), and draft the specific insertion (usually a short reaction/decision beat between two of the stacked beats) that would give the tightest pair room.

### DRAGGING — the story is moving slower than a moment earns

**D1. Sequel with no Decision (HIGH).** Reaction and dilemma are legitimate, necessary beats — the problem is only when they run past the point of producing a choice. If a character spends an extended stretch processing/deliberating and the scene ends without them deciding anything that turns back into forward motion, the chapter has stalled in place.
- Fix: draft a short decision beat (a line or two) that closes out the deliberation with an actual choice, placed where the drift currently just trails off or restates itself.

**D2. Static scene: no Goal, so nothing is actually in motion (HIGH).** A scene needs a character to want something concrete for conflict to have anything to push against. Extended dialogue, travel, or description with no character goal driving it tends to read as filler, however well-written the individual lines are — check whether you could summarize the scene's point in "X wants Y, and Z gets in the way"; if you can't, that's the diagnosis.
- Fix: name the concrete Goal the scene is missing and draft the line(s) that would establish it early in the scene, so what follows reads as pursuing something rather than just happening.

**D3. Redundant introspection or restated information (MEDIUM-HIGH).** The character (or narration) arrives at a conclusion, then circles back to the same conclusion again a few paragraphs later without new information changing it. Distinct from prose-review's filter-word rule — this is about the *idea* repeating at the scene level, not a sentence-level word choice.
- Fix: draft the trimmed version — cut the repeated instance outright, or replace it with a line that adds a genuinely new complication instead of restating the same one.

**D4. Description or worldbuilding that doesn't move tension, character read, or plot (MEDIUM).** Overlaps with prose-review rule 11 at the sentence level; flag here specifically when an entire beat/paragraph-run is functioning as a pause button — nothing the reader learns here changes what they expect next or how they read the characters. Don't flag texture that's doing double duty (grounding a location *and* building dread, say) — that's earning its place.
- Fix: draft a condensed version of the block that keeps only what's earning its place, or suggest redistributing a sentence or two of it into a nearby action beat instead of cutting it outright.

**D5. Flat conflict — resistance that doesn't escalate within a scene (MEDIUM).** The DRAGGING mirror of R2: conflict is present but static — the same obstacle at the same intensity repeated rather than building — so the scene has motion without acceleration and starts to feel like it's marking time.
- Fix: draft a replacement for the repeated/flat beat that escalates instead of restating — the same obstacle, but harder, changed, or newly costly.

**D6. Invisible progress — an assigned beat occurs but the reader cannot feel a change (MEDIUM-HIGH).** The outline may claim relationship, information, internal, external, or mastery progress while the prose only performs related logistics. A conversation happens without altering behavior; a clue appears without changing a hypothesis; a victory repeats an existing competence; a decision is made but never becomes legible as a decision. Beat presence is a continuity question; **felt movement** is pacing's responsibility.
- Check the outline's `Reader-visible progress` and `End-state change` lines. Identify the exact action, realization, new evidence, changed interaction, or mastery signpost that should make the advance perceptible without reading the outline.
- Fix: draft the smallest insertion or replacement that makes the change visible. Do not add a new plot event; sharpen the consequence, comparison, reaction, choice, or changed behavior already authorized by the outline.

Every rule above ends in a **Fix** because every finding in this skill's report needs a drafted Replacement, not just a diagnosis — see Output Format below for exactly how that gets written up.

## Workflow

1. Read the whole chapter before flagging anything — pacing is a property of the sequence, not any single paragraph. If you have the chapter's `beats:` frontmatter, Outline.md, or Summary.md, read those too; they tell you what the chapter is *supposed* to accomplish, which is the baseline pacing measures against.
2. Break the chapter into scenes (a new scene = new Goal, or a hard cut in place/time/POV-focus). For each scene, identify: the Goal (what the POV character wants right now), how Conflict escalates, the Disaster it lands on, and — if present — the Sequel that follows (Reaction → Dilemma → Decision). Also identify which promise/progress track the scene feeds and what is different at its exit. A scene missing a piece isn't automatically wrong; note it, then judge under the rules above whether the gap is a real pacing problem or a legitimate compressed/transitional beat.
3. Build the **Pacing Map** (see Output Format) from that breakdown before writing prose findings — it's the fastest way to see the chapter's overall shape and where RUSHED/DRAGGING findings will cluster.
4. Apply the rules above scene by scene. Every finding needs a concrete anchor (the exact passage, or the start of a spanning issue) and a drafted Replacement — see Output Format for the two treatments (insertion vs. trim/rewrite) and don't defer the drafting to a later step or to the writer.
5. **If reviewing multiple chapters together**, still produce one report per chapter (see prose-review and continuity-reviewer for why — this keeps each report directly usable by `draft-from-review` on its own chapter). But add a short **Cross-Chapter Pacing Note** section to each affected chapter's report when you see a pattern spanning chapters — e.g., three consecutive chapters that all open with a slow Sequel, or an arc that's all Scene with no processing beats anywhere. Keep this section short; it's context, not a new rule category.
6. Order findings HIGH → MEDIUM-HIGH → MEDIUM → LOW, RUSHED and DRAGGING interleaved by order of appearance in the chapter (not grouped by direction) — pacing findings read best in chapter order since they're about sequence.
7. Save the report to the vault's top-level `reviews/` folder (sibling to `codex/` and `novel/` — create it if it doesn't exist). Do not save into a chapter's own `drafts/` folder. Name it `<Chapter Name> - pacing-review-<YYYY-MM-DD>.md`, e.g. `Chapter 4 - Title - pacing-review-2026-08-14.md`.
8. Close with a short "what's already working" note — 1-3 specific scenes or transitions that hit the target rhythm (a Disaster that lands and gets its beat, an escalation that actually escalates), pulled directly from the chapter.

## Output Format

```markdown
# Pacing Review: [Chapter Name]

## Summary

| Direction | HIGH | MEDIUM-HIGH | MEDIUM | Total |
|-----------|------|--------------|--------|-------|
| RUSHED    | X    | X            | X      | X     |
| DRAGGING  | X    | X            | X      | X     |

## Pacing Map

A scene-by-scene table built from the Workflow step 2 breakdown — this is the chapter's shape at a glance.

| # | Scene (location/POV focus) | Goal | Conflict → Disaster | Sequel? | Promise / progress signpost | End-state change | Read |
|---|----------------------------|------|----------------------|---------|-----------------------------|------------------|------|
| 1 | [where/what, one line] | [character wants X] | [what escalates, what breaks] | Yes / No / Partial | [track + visible marker] | [what is now different] | RUSHED / DRAGGING / ON TARGET |

Keep the "Read" column honest — most scenes in a well-paced chapter should land ON TARGET; if every row says RUSHED or every row says DRAGGING, that's itself the headline finding (a chapter running at one speed throughout), and it should be called out in prose above the Findings section even if no single scene individually crosses a severity threshold.

## Promise–Progress–Payoff Check

- **Promise renewed:** [what expectation remains alive on the page]
- **Progress felt:** [what changed and the exact signpost that communicates it]
- **Payoff / preparation:** [what pays here, or what later payoff receives setup]

If the outline promises movement that the prose does not make perceptible, log
a D6 finding rather than quietly crediting the outline.

## Findings

Every finding needs an exact **Original** quote and a drafted **Replacement** — never leave a finding as description-only ("add more reaction here," "this could be trimmed"). The report should be directly usable by `draft-from-review` as a find/replace list, the same standard prose-review and continuity-reviewer hold themselves to. Two treatments, depending on the finding's shape:

- **Insertion findings** (most RUSHED findings — R1, R3, R4: something is *missing* between two existing passages): quote the **Original** passage showing the gap (the disaster and what currently follows it, with nothing between), then give the **Replacement**: the same passage with the drafted insertion (a reaction beat, a decision, a planted setup line) written in, so it's a direct drop-in.
- **Trim/rewrite findings** (most DRAGGING findings, and RUSHED findings R2/D5 where existing text needs to escalate rather than just be cut): quote the **Original** span and give the **Replacement** as the condensed or escalated version of that same span. For a span longer than a couple of paragraphs, use the worked-example treatment instead of rewriting the whole thing: state the **Transformation rule** in plain language, give one worked **Original → Replacement** example for the start of the span, and instruct that the same rule applies through the rest of the flagged span, naming where it ends (see prose-review's structural-finding format for this pattern) — but the worked example itself must still be real drafted prose, not a placeholder.

Drafted Replacement text doesn't need to be publication-final — it needs to be a real, usable draft in the POV character's voice that the writer can accept, edit, or reject. A follow-up prose-review pass can polish the wording once a fix is applied; this skill's job is to make sure a fix exists to apply.

### [HIGH — RUSHED] R1 — Disaster with no Sequel
**Location:** [scene / paragraph reference]

**Original:**
> exact quoted passage showing the disaster landing and the very next beat starting immediately, with nothing between them

**Replacement:**
> the same passage with a drafted reaction beat inserted between the disaster and what follows — a sentence or short paragraph in the POV character's voice that lets the event register before the story moves on

**Why:** one or two sentences tying it to the scene/sequel frame — what the event costs the reader if it isn't felt.

---

### [MEDIUM — DRAGGING] D3 — Redundant introspection
**Location:** [span reference]

**Transformation rule:** plain-language statement of what should be cut or compressed and why (e.g., "the character reaches the same conclusion about X twice; cut the second instance or replace it with a new complication").

**Original (start of span):**
> quoted passage

**Replacement (worked example):**
> the drafted trimmed/replaced version of that opening passage, following the transformation rule

**Note:** "Apply the same rule through the rest of the flagged span, ending at [reference]."

---

### [MEDIUM — RUSHED] R4 — Beats crammed together (structural, chapter-wide)
**Location:** [start] through [end]

**Transformation rule:** name which beats are competing for space and what would need to expand (a Sequel added, a scene split) to give each room.

**Original (tightest seam):**
> quoted passage showing the two most-crowded beats butting against each other

**Replacement (worked example):**
> the same passage with a drafted short reaction/decision beat inserted at that seam, giving the tightest pair room; note that the same treatment can extend to other seams in the flagged span if more than one is crowded

---

## Cross-Chapter Pacing Note *(only if multiple chapters were reviewed together and a pattern spans them)*

- [pattern] — seen in [chapters], suggest [what to vary]

## What's Already Working

- [specific quoted passage or beat] — [why it hits the target rhythm]

---

*Pacing review completed for {{NOVEL_TITLE}} novel.*
```

## Key principles

- **RUSHED and DRAGGING are both failures of match, not a "faster is better" or "slower is better" bias.** Unless your novel's declared style (`codex/Writing Style.md`/`Craft Influences.md`) is genuinely built for constant momentum throughout, a chapter that never shifts out of action-gear is exactly as broken as one that never shifts into it. Judge each scene against what its own Goal/stakes call for and against the register your novel's own declared comp influences would use for that kind of beat (a quieter, dialogue-driven scene earns different pacing than a set-piece), not against a single fixed target speed.
- **This is a shape pass, not a correctness pass.** Like prose-review, every finding should be arguable — phrase the "Why" as "consider" or "this could," not "this is wrong." The location, quoted anchor, and drafted Replacement should still be exact and real, even though the underlying judgment is a suggestion.
- **Never leave a finding as diagnosis-only.** "This scene needs a reaction beat" or "this could be trimmed" is half a finding. Every RUSHED and DRAGGING finding gets an actual drafted Replacement the writer can drop in, edit, or reject — that's what makes this report something `draft-from-review` can act on directly instead of the writer having to go draft the fix themselves first.
- **Don't re-litigate what another reviewer owns.** If a scene is slow because of long sentences and dense paragraphs (wording), name that it's a symptom and point to prose-review; if a beat happens too fast because the timeline math doesn't work (a fact), point to continuity-reviewer. This skill's own findings should be about structure: what beat is present/missing/misweighted, not how it's worded or whether it's factually consistent.
- **The Pacing Map matters as much as the findings list.** A writer working chapter by chapter often can't see their own chapter's shape — the map is the single most useful thing this skill produces, even before any individual finding.
- **Protect scenes that are intentionally compressed.** A quick transitional scene with no real Conflict isn't a bug if it's doing its job as connective tissue between two heavier scenes — only flag D2 (static scene) when the scene is presented as if it matters but has no actual push behind it.
