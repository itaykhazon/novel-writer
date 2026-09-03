---
name: populate-project
description: Interview the author (via the grilling skill) about this novel's genre, POV/tense, register, comp titles, and formatting conventions, research those comp titles and genre-reader expectations online, then write the results into this project's reference/data files — never into any skill's SKILL.md. Use once early when setting up a new novel from this boilerplate, or later whenever the declared genre, comps, or conventions change enough that the reference files need refreshing.
---

# Populate Project

This boilerplate's skills (`draft-chapter`, `chapter-cycle`, `prose-review`,
`pacing-review`, `target-audience-readthrough`, and others) are deliberately
written to be genre- and POV-agnostic — none of them assume third person,
past tense, or any particular genre. Instead they read from a small set of
reference/data files for the specifics: `codex/Genre.md`, `codex/Writing
Style.md`, `codex/Craft Influences.md`,
`chapter-cycle/references/house-conventions.md`, and
`target-audience-readthrough/references/audience-model.md`. Fresh off this
export, those files are placeholders — bracketed `<fill in>` prompts, or (for
`audience-model.md`) content still carrying the specific genre of the project
this boilerplate was ported from.

This skill exists to fill those files in properly: by asking the author what
they actually know (genre, POV, comps), and by researching what they may not
have spelled out themselves (what their comp authors' prose actually reads
like, what readers in their genre actually respond to). That second part is
why this is a separate skill from just editing the files by hand — a comp
title is only useful to `prose-review`/`pacing-review` once someone has
actually looked into what that author's prose *does*, not just named it.

## What this skill touches, and what it never touches

**Writes only to reference/data files:**

- `codex/project.json`
- `codex/Genre.md`
- `codex/Writing Style.md`
- `codex/Craft Influences.md`
- `.agents/skills/chapter-cycle/references/house-conventions.md` **and** its
  mirror `.claude/skills/chapter-cycle/references/house-conventions.md`
- `.agents/skills/target-audience-readthrough/references/audience-model.md`
  **and** its mirror
  `.claude/skills/target-audience-readthrough/references/audience-model.md`
  — this one matters most: unfilled, it simulates a reader calibrated to
  nobody, which is worse than not running that skill at all
- Optionally, with the author's explicit go-ahead (see Step 5),
  `codex/00 Braindump.md`

**Never edits any `SKILL.md`, anywhere, for any reason.** The whole design
this skill exists to support is that craft logic stays generic in the skills
and specifics live in the files above. If you find yourself wanting to change
a skill's actual rule logic to fit this novel better, that's a sign the rule
belongs in one of the reference files instead — flag it to the user rather
than editing the skill.

Also never touches manuscript, outline, or other codex entity files — this
skill sets up the project's declared conventions, it doesn't write story
content.

## Step 1 — Orient: see what's already filled in

Read the current state of every file listed above. Some may already be
partially filled in from a previous run of this skill or by hand — note
which sections are still bracketed placeholders versus already-declared
content. Don't silently overwrite anything that's already a real answer
(not a placeholder); if the interview in Step 2 produces an answer that
conflicts with something already declared, surface the conflict and ask
which one wins rather than picking for the author.

## Step 2 — Interview with `grilling`

Run the `grilling` skill (see `.agents/skills/grilling/SKILL.md`) to gather
what only the author knows. Map the dependency tree roughly like this before
asking the first round:

- **Genre** (one line) — usually answerable immediately, no dependency.
- **POV convention and tense** — first/third/omniscient, single or multiple
  POV, past or present. Independent of genre, ask in the same early round.
- **Register and pacing** — brisk and propulsive, slow and literary,
  variable-by-scene, etc. Easier to answer once genre is known, so this can
  ride in round 1 with a genre-informed suggestion or wait for round 2.
- **Comp titles / influences** — 2–5 specific books or authors this novel
  should read like or be shelved next to. Push for specificity ("N.K.
  Jemisin's *The Fifth Season*", not "epic fantasy") — vague comps give
  Step 3 nothing to research.
- **Formatting conventions** — units, scene-break style, chapter-opener
  convention (if any), whether the novel has any in-fiction system/UI text
  (an in-world letter or report format, a HUD readout, a progression stat panel, etc.)
  and if so its exact rendering, target chapter length. These depend on
  genre/register being roughly known, so they fit round 2.
- **Structural extras** — does this novel need the `species-factions`,
  `systems-mechanics`, or plot mystery-tracker structures `codex/` ships
  with, or should those be trimmed? This can ride in whichever round has
  room; it's independent of the rest.

Follow `grilling`'s own shape guardrails (frontier-only rounds, suggestions
grounded in what's already been said, 2–3 rounds typical). Close the
interview with a one-line summary of what got settled before moving to
research.

## Step 3 — Research

For each comp title/author the author named, and for the declared genre as a
whole, do real web research — don't infer prose style from a title or trust
your own priors about an author you haven't actually looked into for this
purpose. For each comp, look for:

- Characteristic sentence length and rhythm, interiority vs. action-forward
  scenes, dense vs. sparse worldbuilding — reviews, craft essays, interviews
  with the author about their process, or close-reading discussion (r/fantasy,
  r/books, genre-specific subreddits, litfic/genre review outlets) are all
  fair game.
- POV/tense conventions that author is known for, if relevant to why the
  author named them as a comp.

For the genre as a whole, look for what that genre's actual reader community
values and complains about. `target-audience-readthrough/references/audience-model.md`
shows the shape the research should take in its "Research basis" section:
reading-motivation research, readers'-advisory sources, and genre-community
discussion, each cited, with community discussion described as a qualitative
signal rather than a statistic. Genre-specific reader subreddits or
communities, readers'-advisory writeups, and craft-side genre analysis are all
good sources. Cite everything — a claim about what a genre's readers want is
only useful if it's traceable, the same way the original file's citations
are.

Don't fabricate a citation or a research finding. If a comp title turns out
to be hard to find real craft commentary on, say so in the file rather than
inventing a plausible-sounding note — an honest "couldn't verify" beats
confident invention, since these files are load-bearing for other skills'
judgment calls.

## Step 4 — Write the reference files

- **`codex/project.json`** — the book's title and credited author from Step 2.
  This is the one machine-readable file in the vault and the only place the
  title is stored; `export-novel-pdf` reads it for the cover and running
  header. Write it first, since it is the cheapest thing to get right and the
  most annoying to discover missing at export time. If the author hasn't
  settled on a title yet, write the working title and say so — a placeholder
  here is fine, a wrong title baked into sixty files is what the old
  find-and-replace setup used to produce.
- **`codex/Genre.md`** — the one-line genre from Step 2, factual, not
  promotional (per the file's own instruction).
- **`codex/Writing Style.md`** — fill in POV convention, tense, any
  scene/chapter-opening rule, register/pacing line, and the Formatting
  section (units, scene breaks, chapter openers, in-fiction system/UI text
  if any, target chapter length) from the interview answers. Leave
  "Frequently broken continuity" alone — that section fills in from
  experience, not setup.
- **`codex/Craft Influences.md`** — list the comp titles/authors with the
  one-line "why" from the interview, then fill in "What each comp means for
  craft (researched)" from Step 3's actual findings, cited. Write the
  Synthesis paragraph reconciling the comps (say explicitly if they pull in
  different directions and how this novel splits the difference), and the
  one-line Target register summary `prose-review`/`pacing-review` will quote.
- **`chapter-cycle/references/house-conventions.md`** (both copies) — this
  file's Voice/Structural/Continuity sections are already genre-neutral;
  mainly fill in its Formatting section and any strict voice rule to match
  what `Writing Style.md` now says, so the two files agree rather than one
  going stale. Keep the two copies (`.agents/skills/` and `.claude/skills/`)
  identical — write to both, or write one and copy it over the other
  (`sync-skills`'s Job 1 script can confirm zero drift afterward).
- **`target-audience-readthrough/references/audience-model.md`** (both
  copies) — this file needs the most work of the set, and it ships with its
  genre-specific slots empty rather than wrong. Fill in every `<fill in>` from
  Step 3's research: who this reader is, what they read for, what makes them
  put a book down, the genre's conventions and where deviation is forgiven, the
  genre-specific satisfactions under "What to notice naturally", the tone
  section, the tuning axes, and the "Research basis" citations. Leave
  everything not marked `<fill in>` exactly as written — the
  opinion-calibration vocabulary, the general reaction categories, the
  preference-variance rules and the two general citations are genre-agnostic
  and already correct. Remove the file's banner once every slot is filled.

Apply these as you would any vault edit — show the author what changed if
they're present for the session, per `codex/Editing Workflow.md`'s general
spirit, though filling in a still-bracketed placeholder isn't the kind of
manuscript edit that workflow's approval rule is really guarding.

## Step 5 — Optional: seed `00 Braindump.md`

The interview in Step 2 may surface material that belongs in
`codex/00 Braindump.md`'s "Tone and story identity" section (comp titles and
register genuinely belong there too) or elsewhere in that file. This is
author-supplied content, not research, and `00 Braindump.md` is a much bigger
and more personal file than the others — don't touch it without asking first.
Offer to seed the relevant section from what the interview already
established; only write it in if the author says yes.

## When to re-run

Whenever the declared genre, comps, or conventions meaningfully change — a
new comp title the author decides better represents the book, a POV switch
mid-project, a formatting convention that solidified after a few chapters.
Re-running should follow Step 1's rule: read what's there, don't clobber a
real answer without surfacing the conflict first.
