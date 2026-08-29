---
name: draft-chapter
description: Write the actual prose of a chapter from its existing Outline.md, in the established voice. This skill writes sentences and nothing else — it does not update Summary.md, the codex, or any index. Use when the user asks to write, draft, or flesh out a chapter that has already been outlined (typically after add-chapter), or to rewrite an existing chapter from its outline. Follow it with reconcile-chapter to bring the vault's records in line with what landed. If no outline exists yet, use add-chapter first.
---

# Draft a Chapter from its Outline

The vault is a local folder (this skill's working directory, or the folder
the user points you at) — read and write its files directly.

This skill has exactly one job: **put the best possible sentences on the
page.** It does not maintain the vault. Summary rewrites, codex updates, index
status, frontmatter reconciliation and numeric cross-checks all belong to
`reconcile-chapter`, which runs after this one.

That split is deliberate. Bookkeeping and prose compete for the same attention,
and prose loses — a pass that is simultaneously tracking resource budgets,
frontmatter accuracy and index status writes competent, characterless
sentences. Do not "save a step" by folding the reconcile work back in here.

## 1. Locate the chapter and read in

Confirm which chapter (number, and arc if ambiguous). Then read, in this order:

1. `novel/arc <N>/Chapter <n> - <Title>/Outline.md` — **required**. If there is
   no `Outline.md`, stop and offer to run `add-chapter` first. Don't
   improvise a chapter that was never planned.
2. That folder's `Summary.md` (the planned one) for the intended shape.
3. The previous chapter's `Summary.md` for continuity, and the last ~1000 words
   of the previous chapter's actual prose for voice and immediate handoff — if
   this chapter continues directly from a cliffhanger, read enough to match the
   physical situation exactly.
4. `codex/Genre.md`, `codex/Writing Style.md`, and `codex/Craft Influences.md`.
5. Codex entries for every character, mechanic, creature, and location the
   outline lists — abilities and limits have to be right on the page.

If `Outline.md` has `status: needs-input`, resolve its open questions with the
user before writing a word.

Read the outline's `## Sanderson pass` — the chapter's structural contract:
promise, reader-visible progress, POV want, try–fail/escalation, payoff,
end-state change, and resource/limitation budget. For an older outline that
lacks one, derive the same compact preflight from
`codex/outline/Sanderson Method — Working Guide.md` without rewriting the
approved plan. If the climax needs an unestablished ability, unavailable
resource, or missing setup, stop and surface the plan problem before prose
makes it canon.

## 2. Voice

`codex/Writing Style.md` is the source of truth for every line you write — read
it fully, don't rely on this summary. It's genre- and POV-agnostic by design:
your novel might be third-limited or first-person or omniscient, past or
present tense, single-POV or multi-POV, lean and fast or dense and literary.
Whatever it specifies, in force for every line:

- Hold the POV/narrative-distance convention it specifies exactly — if it's
  close POV (first person, third-limited), never include an observation that
  POV character couldn't make; if it's omniscient, hold whatever discipline the
  file specifies for that instead.
- **If `codex/Writing Style.md` specifies a scene/chapter-opening convention
  (e.g. opening on the POV character's name), treat it as a firm house rule,
  not a stylistic nudge, and check it on every line you write.** If the file
  specifies no such convention, don't invent one.
- Varied sentence length; pacing and rhythm matched to what
  `codex/Writing Style.md` and `codex/Craft Influences.md` actually establish as
  this novel's target — don't assume "fast" or "cinematic" unless that's what's
  declared.
- Sharp dialogue that does work — characterization, information, or pressure.
  Cut lines that only fill air.
- Follow the genre and tone recorded in `codex/Genre.md` and
  `codex/Writing Style.md` — including any in-fiction system/UI text format, if
  your novel uses one — matching the format already used in earlier chapters
  rather than reinventing it per chapter.

Note what these rules are and are not. "No clichés", "varied sentence length"
and "sharp dialogue" are *floors*. Clearing them produces prose that is not bad,
which is not the same as prose that is good. What makes a page read as authored
is section 3's specificity requirement, and it is not something a rule can be
written for — it has to be found in the scene.

Match the existing chapters' scale: roughly 3,000–5,000 words, scene-broken the
way earlier chapters break.

## 3. Write it

Preserve prior work first: if the chapter file already contains prose, copy it
into `drafts/` as `v<N> - <YYYY-MM-DD>.md` before overwriting.

Write the full chapter into `novel/arc <N>/Chapter <n> - <Title>/Chapter <n> -
<Title>.md`, keeping the frontmatter and setting `status: draft`. Leave the rest
of the frontmatter alone — `reconcile-chapter` corrects it against what actually
landed.

### The outline locks function and outcome. It does not lock sentences.

This is the rule that decides whether the chapter reads as written or as
expanded, so it comes before everything else in this section.

`Outline.md` is a list of things that must be true by the end of the chapter. It
is not a draft. Its sentences were written to be *scanned by you and the author
in a minute* — they are summary-shaped by construction, and summary-shaped
sentences stay summary-shaped when you inflate them. If a beat line reads
well, that is a warning rather than a gift: it means the best phrasing in that
moment was chosen under planning constraints, by someone thinking about
structure, before anyone knew what the scene would feel like.

So:

- **Never carry a phrase from the outline into the prose.** Not a clause, not an
  image, not a verb chosen for its rightness. Find the words at the keyboard,
  in the scene, with the character in the room.
- The exception is deliberate verbatim material — an oath, an in-fiction system
  readout, a line of dialogue meant to recur exactly, a quoted description of a
  planted object that must match its first appearance. The outline marks these
  under `## Verbatim anchors`. Those land word-for-word by design; everything
  else is written fresh.
- `scripts/check_outline_overlap.py` (in `chapter-cycle/scripts/`) reports runs
  of shared wording between the outline and the prose. Run it when you finish.
  It is evidence, not a verdict — read each hit in context — but a chapter with
  several long non-anchor runs has been transcribed rather than written, and
  the fix is to rewrite those passages from the scene, not to reword them until
  the script goes quiet.

### Compose scene by scene

Write scenes in order, finishing each before starting the next — voice
consistency degrades across a long single generation, and continuity is easier
to hold when the previous scene is actually on the page rather than in the plan.

Before each scene, settle five things in your head: the POV character's goal,
what resists it, the reader-visible signpost that progress happened, how the
exit state differs from the entry state, and any finite resource spent or
regained. Thirty seconds of this, not a written artifact. A beat does not land
because the planned event occurred; it lands because the reader can perceive
what changed.

### Write the turning scenes twice

Identify the two or three scenes the chapter actually turns on. For each, write
the opening 150–250 words **twice**, with genuinely different attacks — enter at
a different moment, lead with a different sensory channel, sit at a different
distance from the character, start on dialogue instead of action. Then pick the
better one, continue from it, and discard the other.

This is the only point in the whole pipeline where prose gets *chosen* rather
than corrected. Everything downstream — the reviewers, the diffs — can remove
what is wrong with a draft; none of it can supply what a draft never had. Two
takes on a chapter's three most important openings is cheap next to a single
review round.

### The specificity floor

Every scene needs at least one concrete observation that **only this POV
character, in this situation, could have made** — a noticing shaped by what they
want, what they fear, what their history makes salient, or what their expertise
lets them see. Not a decorated description; a perception another character
standing in the same room would not have had.

A chapter that clears every rule in section 2 and fails this one is exactly the
draft that reads as competent and unauthored. If you cannot find the observation
for a scene, that scene is not understood yet — go back to what the character
wants in it.

### Fidelity to the plan

Follow the outline's beats in order. You may deepen a beat, reorder sentences
within it, or discover that a moment needs more room than the plan gave it. You
may not drop a beat, add a new plot event, introduce a character the outline
doesn't have, or change the ending. If a beat turns out not to work in prose —
the physical logistics don't hold, two beats collapse into one, the ending lands
flat — say so and get the user's call rather than quietly rewriting the plan.

Respect the outline's **Constraints** section absolutely.

Any number that ends up on the page — a percentage, a count, a rank — is the
canonical value the moment you write it. You don't need to track these;
`reconcile-chapter` reads them back off the finished prose, which is more
reliable than remembering them while writing.

## 4. Hand off

Run the overlap check and report:

```bash
python3 <vault>/.claude/skills/chapter-cycle/scripts/check_outline_overlap.py \
    --chapter "novel/arc <N>/Chapter <n> - <Title>/Chapter <n> - <Title>.md"
```

Then report to the user: word count, scene breakdown, anything you deviated
from in the outline (and why), any point where the codex and the scene
disagreed, any new character/location/mechanic the chapter introduced that has
no codex entry yet, and the overlap check's findings with your read on each.

**The chapter's records are now stale** — the frontmatter, `Summary.md`, the arc
index, the outline files and the codex all still describe the plan, not the
page. Say so, and offer to run `reconcile-chapter`. Do not do that work here.
