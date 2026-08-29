# Review protocol

## Model / effort assignment

If your environment lets you choose a model or effort level per review pass,
match it to how hard the job actually is — on the original run of this
pipeline, using the same (expensive) setting for every reviewer by default
was the single largest waste in the whole cycle.

| Reviewer | Suggested effort | Reasoning |
|---|---|---|
| `proofread` | cheapest/fastest available | Spelling, punctuation, agreement — pattern-matching against a fixed rulebook |
| `pacing-review` | mid-tier | Structural judgment, but bounded by the outline's beat list |
| `prose-review` | mid-tier | Craft judgment, bounded by the voice files in the bundle |
| `anti-ai-prose-review` | cheapest/fastest available | `scan_prose.py` does the counting; the reviewer only judges which candidates cost the prose something |
| `continuity-reviewer` | your best-reasoning tier | Cross-references many facts, including the chapter's own Summary and codex pages for numeric/tag drift (Cross-Artifact Fact Consistency) — the only one with a real reasoning load |

Escalate one reviewer to your top tier only if a specific chapter has an unusual
demand (a new POV character, a mechanic being rewritten) — and say why in the
changelog.

## Running the five reviewers

Run `proofread`, `pacing-review`, `prose-review`, `continuity-reviewer`, and
`anti-ai-prose-review` against the drafted chapter. If your environment supports running multiple
independent passes concurrently (parallel agent/session invocations), run all
four at once — they're independent of each other and don't need to see one
another's output. If it doesn't, run them one after another in any order;
there's no dependency between them.

For each reviewer, give it exactly two things and nothing else: the chapter
working copy, and the context bundle built in Phase 0. `anti-ai-prose-review`
gets a third: run its `scan_prose.py` over the working copy first and paste the
output into its prompt. The script computes densities and baselines exactly;
asking the model to estimate them instead wastes the pass and gets worse
numbers. Below is the prompt
template to adapt — substitute the bracketed parts, keep the rest close to
verbatim, since the constraints are what stop the reviewer from wandering off
and re-exploring the vault:

> Run the `<SKILL NAME>` skill and apply it to a newly drafted novel chapter.
>
> **Chapter to review:** `/tmp/chapter-cycle/chapter.md`
> **Context bundle:** `/tmp/chapter-cycle/bundle.md` — the outline, style rules, previous
> chapter handoff, and every relevant codex entry, already assembled for you.
>
> Read exactly those two files. Do **not** search the vault or open other files;
> everything you need has been collected. If something you need is genuinely
> missing, say so in your report rather than going to look for it.
>
> [ONE OR TWO SENTENCES: what is distinctive about this chapter — new POV, first
> appearance of a mechanic, direct continuation of a cliffhanger.]
>
> Also verify the house rule: the chapter AND every scene (the line right after
> each `—` scene-break marker) must open with the POV character's name as the
> literal first word or opening clause.
>
> For `pacing-review` specifically: use the outline's "Sanderson pass" as the
> chapter's structural contract. Verify that its promised progress is visible
> to a reader, its small payoff/setup receives proportionate page weight, and
> every scene produces a meaningful change or deliberately earns its stillness.
>
> For `anti-ai-prose-review` specifically: the scan output above is candidates,
> not findings. Judge each in context and report only the ones that cost the
> prose something — a device the reader will start anticipating, a cadence that
> has become a loop, a reaction beat doing no work. Do not report a pattern
> merely because it is present, do not treat the scan as an authorship
> determination, and do not propose mechanical rewrites that drive a count to
> zero at the expense of the sentence.
>
> For `continuity-reviewer` specifically: the bundle's "Planned summary" section
> is the chapter's current `Summary.md` — cross-check every percentage, count,
> rank or classification tag, and placement in the chapter against what that section (and any
> codex mechanics page in the bundle) claims for the same fact, and flag a
> disagreement even if the Summary and codex already agree with each other.
> Also verify payoff legality: any capability that solves a problem must have
> been established early enough for the reader to understand it, the character
> must possess the required resource/knowledge/equipment at that exact point,
> and the documented limitation or cost must remain active.
>
> **Report only — do not edit any file.**
>
> Return findings as your final message, ordered most-severe first. Every finding
> must have:
> - the **exact quoted text** from the chapter (long enough to be unique in the file)
> - the problem, in one sentence
> - a **drafted replacement**
> - severity: **IMPORTANT** (a reader would notice) or **MINOR** (polish)
>
> A finding without a uniquely quotable anchor cannot be applied — either anchor
> it or describe it as a general note in a separate section at the end. No
> preamble; if you find nothing, say so plainly.

## Round 2 — regression check only

Do not re-run the full review. If your environment supports resuming a prior
review pass with its context intact (rather than starting a fresh one), resume
`prose-review` and `continuity-reviewer` that way — starting fresh discards
their context and they'd have to re-read everything. Send only:

> The chapter has been revised at the same path. These passages changed:
>
> [QUOTE EACH CHANGED PASSAGE, with one line on what it was meant to fix]
>
> Two questions: did any of these reintroduce a problem you flagged earlier, and
> is anything IMPORTANT still open? Same format as before. Report only.

Then stop. Resume a review pass at most once — its needed context grows every
turn, so whatever you saved by keeping it alive is spent by roughly the third
exchange. If your environment can't resume a prior pass at all, just re-run
`prose-review` and `continuity-reviewer` fresh with the same message above plus
the working copy and bundle — it costs more, but the regression-only scope
still keeps it far cheaper than a full round 2.

## Known regression patterns

New material written to satisfy round-1 findings tends to smuggle back the exact
habits round 1 removed. Check for these before the regression round:

- **Overhead rosters** — a four-item list narrating everyone's position at once,
  with the POV character described from outside their own body.
- **Flash-forwards** — "the part he'd look at later, if there was a later" —
  stepping out of the moment mid-fight.
- **Filters inside direct thought** — `*Stop,* she thought` when the italics are
  already doing that work.
- **Statement → explanation → aphorism** — the same realization delivered three
  times. Keep two movements, drop the middle.
- **Invented numbers** — counts of opponents, rounds, supplies or distances that don't match
  what's actually on the page. Every number added in a fix needs checking against
  the scene.
- **Orphaned Summary/codex values** — a round-1 or round-2 fix that changes a
  number, rank, or placement in the prose but leaves the pre-fix value standing
  in `Summary.md` or a codex mechanics page. This doesn't show up by re-reading
  the chapter alone — it only shows up by diffing the changed fact against the
  Summary and codex, which is why Phase 5's numeric cross-check is a separate,
  mandatory step rather than folded into "read it again."
- **Erased progress signposts** — a trim removes the action, realization, or
  changed behavior that made an assigned beat perceptible, leaving the event
  technically present but structurally invisible.
- **Costless repaired payoffs** — a replacement makes a climax cleaner by
  deleting the energy/supply/mass/injury/time cost that made the solution
  obey its established limitations.

## Final pass

After the last diff round, run one cheap/fast proofread pass on the working copy
alone — no bundle. The final round of edits is where dangling modifiers, broken
parallelism and ambiguous antecedents get introduced, because replacement text
was written to fit a quote rather than its new sentence.
