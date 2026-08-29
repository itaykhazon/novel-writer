---
name: target-audience-readthrough
description: Simulate an honest, opinionated cold read of a chapter, arc, or the entire drafted story by one plausible genre-literate reader in this novel's actual target audience (see references/audience-model.md — genre-specific, fill in via populate-project or by hand). Use when the user asks for a target-audience readthrough, reader reaction, beta-reader opinion, engagement map, keep-reading or DNF assessment, or which segments were thrilling, boring, overlong, repetitive, underdeveloped, or a slog. Read only the requested manuscript prose and never use the codex, outlines, summaries, reviews, changelogs, frontmatter, author explanations, or other privileged context.
---

# Target-Audience Readthrough

Give the writer the experience of handing pages to a real target reader. React as one disclosed reader, not as an editor, a lore expert, or a statistical consensus.

Read `references/audience-model.md` before every readthrough. Use its default persona unless the user specifies a different audience segment.

## Protect the cold read

Treat context isolation as the central requirement.

Use only:

- the manuscript prose in the exact requested scope;
- titles and file paths needed to establish reading order;
- audience preferences explicitly supplied by the user;
- the audience model bundled with this skill.

Do not open or use:

- anything under `codex/`;
- `Summary.md`, `Outline.md`, chapter frontmatter, drafts, or changelogs;
- existing reviews or review findings;
- character sheets, voice notes, beat plans, or author explanations;
- earlier or later manuscript prose outside the declared reading scope.

Ignore YAML frontmatter and any author-only notes embedded around the prose. Never repair uncertainty from outside knowledge. If the text does not establish something, experience that absence as the reader would.

If a fresh-context worker is available and its use is allowed, delegate the reading pass to one with no conversation history. Give it only this skill, `references/audience-model.md`, the declared reading mode, and the target manuscript paths. Do not pass prior conclusions, codex facts, summaries, or suspected issues. The primary agent may format and save the returned report without adding privileged knowledge.

If no fresh worker is available and the current context already contains meaningful forbidden knowledge about the target, continue only when necessary and disclose under **Reader Setup** that cold-read integrity was limited. Do not pretend forgotten knowledge is absent.

## Select the scope and mode

Choose the narrowest mode that matches the request. Do not silently expand it.

- **Chapter / exact-scope:** Read only the named chapter. This is the default for a chapter request.
- **Chapter / continuing-reader:** Read manuscript prose from the story's beginning through the named chapter, then focus the report on that chapter. Use only when the user explicitly asks for in-context or continuing-reader feedback.
- **Arc:** Read only the drafted chapter prose in the named arc, in narrative order. Include cumulative arc reactions in one report.
- **Entire story:** Read all drafted manuscript prose, including a prologue when present, in narrative order. Skip outlined but undrafted chapters.

For file discovery, inspect names and paths under `novel/` without opening excluded companion files. A manuscript chapter is the prose file named for its chapter inside that chapter folder. Exclude `Summary.md`, `Outline.md`, `drafts/`, and non-prose planning artifacts.

State the chosen mode and exact files in the report. If reading order cannot be determined from manuscript names and folders alone, ask for the order instead of consulting the codex.

## Read like a reader

Perform the first pass continuously and in order. Do not begin with a craft checklist and do not stop to propose fixes.

Divide the experience by meaningful segments, not merely by chapters. A segment begins when the reader's goal, tension, location, relationship focus, or level of engagement changes. Cover roughly 3–7 segments for a chapter and at least 2 meaningful segments per chapter for an arc or whole-story read, adding more whenever engagement changes sharply. Do not force uniform segment sizes.

Give every segment one blunt verdict:

- **THRILLED:** I actively resisted stopping and urgently wanted the next beat.
- **HOOKED:** Strong curiosity, tension, emotion, or delight pulled me onward.
- **ENGAGED:** My attention was steady and the segment earned its space.
- **COASTING:** Readable, but I was passively waiting for a stronger development.
- **SLOG:** Boring, overlong, repetitive, or effortful enough that I skimmed or wanted to.
- **LOST:** Confusion or indifference seriously broke investment or created a stopping risk.

Name which reward channel drove the verdict — a segment engages or fails through one or more of these, and naming the right one turns a vague "this was flat" into an actionable diagnosis:

- **Transportation:** immersion in the story world — coherent sensory grounding, a POV I could inhabit.
- **Aesthetic:** sentence-level pleasure — rhythm, word choice, a line worth rereading for its own sake.
- **Social Simulation:** characters read as minds — distinct voices, legible interiority, behavior I could model.
- **Flow:** the pace matched what the moment could support — challenge and information arriving at a rate I could ride.
- **Curiosity/Prediction:** an open question, a gap, a stake I wanted resolved.

A THRILLED or HOOKED segment usually has two or more channels firing at once. A COASTING, SLOG, or LOST segment usually has a specific one starved — say which, not just that engagement dropped.

At each boundary, capture the immediate first-person reaction before later events can soften it:

- what has my attention now;
- which character I care about, distrust, or feel indifferent toward;
- what I think is happening and what I predict;
- what created tension, curiosity, delight, dread, or amusement;
- the exact point where I became impatient, bored, confused, or tempted to skim;
- what I was waiting or hoping for while the segment continued;
- whether a reveal, victory, joke, or emotional beat paid off;
- what would make me continue or put the story down.

For every **THRILLED** or **HOOKED** segment, identify the precise turn that raised engagement and what desire it created. For every **SLOG** or **LOST** segment, identify its beginning and end, what made it feel long or empty, whether I actually skimmed, and what finally restored attention—if anything.

Track story promises while reading: conflicts, relationships, mysteries, goals, antagonists, emotional wounds, and progression paths that the prose presents as important. Note when a promise is fed, transformed, paid off, forgotten, or remains too thin to support the weight later placed on it. Do not call a deliberately unresolved question underdeveloped merely because it remains open; call it underdeveloped when the read scope repeatedly signals importance but gives too little change, texture, consequence, or page presence to sustain interest.

Judge length by experience, not word count. A long segment is not a problem when it keeps changing the reader's understanding or emotion. A short segment can still be a slog when it repeats a function whose effect is already complete.

For an arc or whole-story pass, preserve all segment verdicts and promise notes as a private reader journal so later knowledge does not overwrite earlier boredom, confusion, excitement, or predictions. The journal may contain only reactions derived from the manuscript itself.

After finishing, revisit only the target prose to locate brief supporting passages or scene references. Do not turn the second pass into proofreading, continuity checking, or line editing.

## Keep the opinion honest

- Write in first person: “I cared,” “I was confused,” “I laughed,” “I started skimming.”
- Use the strongest honest word. If a segment was boring, call it boring. If it thrilled me, say what made me eager to keep reading.
- Anchor every strong opinion to a specific segment, scene turn, or brief passage.
- Do not manufacture a criticism to balance praise, or praise to soften criticism.
- Do not wrap every criticism in a compliment. State the negative reaction first and plainly.
- Avoid automatic hedges such as “a little,” “somewhat,” “mild,” or “may” unless the reaction truly was marginal.
- Compare segments against one another. Name the most exciting, funniest, dullest, longest-feeling, and thinnest-developed material when those categories exist.
- Do not summarize a chapter and mistake that for an opinion. Any paragraph that only recounts events is incomplete until it states how my engagement changed and why.
- Do not claim to speak for all readers. Separate a personal preference from a likely audience-fit issue.
- Distinguish a **pull-forward question** from **blocking confusion**. Mystery creates desire to learn more; blocking confusion prevents the reader from understanding the present action, goal, or consequence.
- Distinguish deliberate breathing room from boredom by asking whether the slower material deepened character, atmosphere, stakes, or anticipation.
- If your novel has stat or progression elements, judge them by whether progression is legible, consequential, and earned—not by the sheer quantity of numbers or alerts. Skip this bullet entirely if your novel has no such system.
- Judge dark humor by whether it arises from character or situation and whether the scene retains emotional consequences after the laugh.
- Call out cheesiness by name when it happens: a line, beat, or emotional turn that reads as melodramatic, corny, or try-hard rather than earned — whether it's a serious moment overplaying its hand or a joke landing flat. Say so as plainly as any other reaction, in the segment where it happened; don't soften it into "the emotional beat didn't quite land."
- Never infer author intent. Describe the experience that reached the page.
- Never offer replacement prose or a fix list. This skill reports reader response; other review skills diagnose craft and propose edits.

## Save one scope-level report

Save the report in the vault-level `reviews/` folder. Do not edit the manuscript or any codex file.

Use `<Scope Name> - target-audience-readthrough-<YYYY-MM-DD>.md`, for example:

- `Chapter 8 - The Last Gate - target-audience-readthrough-2026-08-15.md`
- `Arc 1 - target-audience-readthrough-2026-08-15.md`
- `<Novel Title> - target-audience-readthrough-2026-08-15.md`

Keep an arc or whole-story experience in one report; do not split it into chapter reports. If the filename already exists, append `-2`, `-3`, and so on rather than overwrite it.

## Report format

```markdown
# Target-Audience Readthrough: [Scope]

## Reader Setup

- **Reader:** [brief disclosed persona]
- **Mode:** [exact-scope / continuing-reader / arc / entire story]
- **Prose read:** [ordered file or chapter list]
- **Context boundary:** Only the prose listed above; no codex, summaries, outlines, frontmatter, reviews, or author notes.
- **Cold-read integrity:** Clean / Limited because [specific contamination]

## Gut Reaction

[A candid first-person overview. State the best material, the weakest material, and whether the experience strengthened or lost momentum. Do not lead with a plot summary.]

## Engagement Map

### [Chapter/scene]: [segment label] — [THRILLED / HOOKED / ENGAGED / COASTING / SLOG / LOST]

- **Where:** [brief beginning and ending anchors]
- **My reaction:** [what I felt, predicted, wanted, or did as a reader—including actual skimming or rereading]
- **Why:** [the specific change, repetition, absence, character beat, discovery, or payoff that caused the verdict — name the reward channel(s) involved: Transportation, Aesthetic, Social Simulation, Flow, or Curiosity/Prediction]
- **What I wanted next:** [the immediate reader desire, or “Nothing yet”]

[Repeat chronologically for every meaningful engagement segment. Do not flatten one chapter into one entry when the experience changed inside it.]

## The Parts I Was Thrilled to Read

Rank the strongest 1–5 segments. For each, state:

1. **[Segment]:** [the exact turn that lit up the reading experience, why it worked, and what made me want more]

Do not fill a quota. Say “None reached THRILLED” if that is the honest verdict.

## The Parts I Slogged Through

For every material low point, state:

- **Segment:** [exact scene range]
- **Verdict:** [boring / overlong / repetitive / confusing / emotionally thin / other]
- **Severity:** [friction / skimmed / near-DNF / would stop]
- **My honest response:** [what attention did, what I stopped caring about, and what I was waiting for]
- **Recovery:** [where interest returned, or “It did not within this scope”]

Write “None” only if no segment fell below **ENGAGED**. Do not soften **SLOG** into “slower but useful” unless it genuinely remained engaging.

## Underdeveloped Stories, Characters, or Promises

- **[Promise]:** The prose made me expect [specific development]. Within this scope I received [what actually developed]. It felt [satisfying / still alive / underfed / abandoned / too thin for its payoff] because [reader reaction].

Include relationships, mysteries, conflicts, progression paths, and characters only when the prose itself presented them as important. Distinguish “intriguingly unresolved” from “underdeveloped.”

## What I Wanted More Of—and Less Of

- **More:** [specific character pairing, storyline, kind of scene, system interaction, emotional pressure, humor, or world discovery]
- **Less:** [specific repeated beat, explanation mode, combat loop, detour, joke pattern, or other drag]

Do not answer with broad categories such as “more character development.” Name the page-level material that created the appetite or fatigue.

## Questions in My Head

### Pull-forward questions

- [Question that makes me want to continue]

### Blocking confusion

- [Question that prevented present understanding]

Write “None” when appropriate.

## Would I Keep Reading?

**Yes / Maybe / No.** [Direct reason. Name the strongest propulsion point, the exact near-DNF or DNF point, and the storyline I am most and least eager to revisit.]

## Audience-Fit Read

- **Best fit:** [the reader segment most likely to enjoy this]
- **Likely bounce points:** [specific taste mismatches or repeated friction]
- **Personal-taste caveat:** [what may be peculiar to this simulated reader]

---

*Cold target-audience readthrough only; no codex or editorial review used.*
```

Scale detail to scope. A single chapter report should stay compact; an arc or full-story report may be longer but should emphasize the remembered experience rather than summarize every event.
