---
name: prose-smell-review
description: >-
  Review fiction for broad prose smells that weaken clarity, specificity,
  agency, reader trust, scene function, or immersion. Use when the user asks
  for a prose-smell, bad-writing, rules-of-thumb, Elements of Style, or Stephen
  King On Writing pass; wants to find vague, over-explained, author-driven,
  static, monotonous, or artificially withheld prose; or wants exact
  voice-matched improvements for those problems. Produces a blunt, unsparing,
  actionable report and never edits manuscript prose.
reviewer-kind: line
reviewer-scope: chapter
thinking-level: medium
complexity: 6
default-in-cycle: false
---

# Prose Smell Review

Review fiction using practical craft heuristics as diagnostic tests, not laws.
Flag a passage only when the suspected smell has an observable cost and a
specific replacement improves it without damaging voice, meaning, rhythm,
ambiguity, or scene purpose.

This is a broad reader-effect pass. It asks whether the prose gives the reader
a precise experience or substitutes explanation, generic language, ornament,
or authorial convenience for that experience.

## Reviewing posture

Be adversarial toward the prose and fair to the author. The reviewer's job is
to find and prosecute weak writing, not to protect the writer from hearing that
a passage fails. The author can defend a choice after seeing the evidence.

- **Lead with the verdict.** Say that a passage is weak, vague, redundant,
  confusing, inert, overwritten, dishonest to the POV, or otherwise failing
  when the evidence supports that judgment. Explain the effect immediately.
- **Do not hedge for politeness.** Avoid `consider`, `perhaps`, `might`, and
  `could` in verdicts and explanations unless uncertainty is genuine and
  specifically identified.
- **Intent is not effect.** A deliberate choice can still fail. Naming a
  passage's intended function does not prove that the function succeeds.
- **House style is not immunity.** `This is the voice`, `the scene is supposed
  to be slow`, `the character is confused`, and similar defenses count only
  when the actual words create a worthwhile effect on the page.
- **No compliment sandwich.** Do not cushion a finding with praise before or
  after it. Report strengths separately and only when the text supplies exact
  evidence.
- **Attack the writing, never the writer.** Brutal means candid and exact, not
  insulting, sarcastic, theatrical, or contemptuous.
- **Do not ration findings to protect morale.** Report every material smell the
  text supports. Prioritize them so the author knows what matters most.

## Required reading

1. Read the supplied prose in full before diagnosing individual lines.
2. Read [references/smell-catalog.md](references/smell-catalog.md) in full. It
   defines the smells, thresholds, exceptions, remedies, and research basis.
3. For a chapter in this project, also read:
   - `codex/Writing Style.md`
   - `codex/Craft Influences.md`
   - the current POV character's `<Name> - Voice.md`
   - `codex/Editing Workflow.md` when saving a report

The manuscript outranks the codex, and this novel's house style outranks a generic
maxim. Surface conflicts; do not rewrite around them silently.

## Scope and boundaries

Own these questions:

- Does each passage earn its reading cost through action, tension, character,
  information, atmosphere, humor, rhythm, emotional pressure, or orientation?
- Is the experience concrete and specific to this POV, place, and moment?
- Does the prose trust evidence and subtext, or explain their meaning again?
- Do grammar and word order make agency, emphasis, and causality easy to
  follow?
- Does description or exposition arrive because the scene needs it now?
- Does withheld information create legitimate uncertainty or false suspense?
- Do dialogue, imagery, and cadence belong to these characters rather than a
  generic narrator?
- Does a scene begin near its meaningful pressure and leave something changed?

Specialist ownership controls depth and repair, not whether this reviewer is
allowed to name a smell:

- `proofread` owns grammar, spelling, punctuation, and capitalization errors.
- `prose-review` owns systematic deep-POV distance, filter words, sensory
  range, and voice calibration.
- `anti-ai-prose-review` owns model-shaped phrase families and claims about
  templated or AI-like texture.
- `pacing-review` owns full scene/sequel architecture and tension-rate maps.
- `continuity-reviewer` owns lore, timeline, capabilities, resource accounting,
  and whether a payoff is factually earned.

Flag every smell supported by the text even when a specialist could analyze it
further. State the verdict and reader cost first, then refer the deeper check or
repair; a referral never replaces the finding. Avoid duplicating a specialist's
full technical analysis. If a fix requires a canon decision, a new plot beat,
or a changed capability, say plainly that the prose currently fails and name
the unresolved dependency instead of inventing a solution.

## Rule hierarchy

When two rules conflict, use this order:

1. Canon and factual continuity.
2. Reader comprehension of the intended event.
3. POV knowledge, character voice, and scene purpose.
4. This novel's house style and formatting.
5. General craft maxims.

Never damage a higher level to satisfy a lower one. Passive voice, adverbs,
telling, long sentences, fragments, repetition, and slow passages can all be
correct when they perform a deliberate function successfully. Merely calling a
device intentional, stylistic, atmospheric, or voice-specific does not move it
up this hierarchy.

## Severity

Classify the revision need, not the number of maxim violations:

- **HIGH** — A sustained passage or structural choice obscures agency or
  causality, breaks reader trust, creates false suspense, flattens a scene, or
  substantially weakens immersion.
- **MEDIUM** — A clear local smell or repeated pattern makes the prose less
  precise, less character-specific, or more effortful than necessary.
- **LOW** — A localized refinement with a materially better exact alternative.
  Omit taste-only LOW findings.

Raise severity for repetition, clustering, a sudden voice change, or a smell at
a major emotional or plot turn. Lower it when the device is isolated,
purposeful, voice-specific, or necessary for pace.

## Workflow

1. **Read for experience.** On the first pass, do not mark sentences. Identify
   what the reader should feel, understand, anticipate, and question.
2. **Map function.** For each scene, note the POV want, resistance, information
   delivered, entry state, exit state, and any passage whose primary job is
   atmosphere, humor, reflection, or transition. These are legitimate jobs.
3. **Apply the catalog.** On the second pass, collect candidates by smell ID.
   Record the exact anchor, the suspected reader cost, and the smallest viable
   remedy.
4. **Run false-positive tests.** Before reporting a candidate, ask:
   - **Deletion test:** What specific function disappears if this is cut?
   - **Focus test:** Does passive voice or word order put the correct subject in
     focus?
   - **Knowledge test:** Is information absent because the POV lacks it, or
     because the author is hiding it?
   - **Voice test:** Is this wording generic, or is it established character
     diction?
   - **Pace test:** Is telling compressing an unimportant interval on purpose?
   - **Read-aloud test:** Does the rhythm work better than it looks?
   Do not clear a candidate because the device can serve that function in
   theory. Clear it only when this passage demonstrably earns the exception;
   record the exact evidence that acquits it.
5. **Draft the fix.** Preserve facts, blocking, formatting, uncertainty, and
   voice. Prefer deletion when the passage already works without the suspect
   sentence. Otherwise write the smallest exact replacement that addresses the
   cost.
6. **Cross-check the replacement.** Make sure it does not introduce a new
   smell, POV error, unsupported fact, overwritten subtext, or house-style
   violation.
7. **Order findings** HIGH → MEDIUM → LOW, then by appearance within each
   severity.
8. **Save reports** in the top-level `reviews/` folder as
   `<Chapter Name> - prose-smell-review-<YYYY-MM-DD>.md`. For multiple chapters,
   save one report per chapter. For unnamed pasted prose, respond in chat unless
   the user requests a file.
9. **Report only.** Do not edit manuscript prose. `draft-from-review` applies
   author-approved changes and logs them.

## Replacement requirements

Every finding must be actionable:

- For a line-level or paragraph-level finding, provide verbatim **Original**
  and a complete, drop-in **Replacement** covering the same span.
- For a pure deletion, use `[Delete.]` as the Replacement; do not disguise a
  deletion as a rewrite.
- For a structural finding, state the transformation rule, give one exact
  worked Original → Replacement at the first anchor, list the remaining exact
  anchors, and name where the affected span ends.
- If a valid remedy requires story invention or a canon choice, do not draft it
  as though authorized. State the dependency and refer it to the appropriate
  reviewer or the author.

The replacement is a proposal, not permission to apply it. Match the actual
POV character's diction; do not translate everything into generic spare prose.

## Output format

```markdown
# Prose Smell Review: [Chapter or Scope]

## Summary

**Overall verdict:** Clean / Mostly sound / Clearly flawed / Fundamentally weak

| Severity | Count |
|----------|-------|
| HIGH | X |
| MEDIUM | X |
| LOW | X |

**Main verdict:** [two to four direct sentences naming the dominant failures,
their severity, and the reading experience they damage]

## Smell Map

| Smell | Pattern | Occurrences | Read |
|-------|---------|-------------|------|
| S6 — Explained effect | [specific pattern] | X | Isolated / Repeating / Clustered |

## Findings

### [MEDIUM] S6 — Evidence followed by explanation
**Location:** [scene / paragraph / unique anchor]
**Verdict:** [direct statement of what fails here]
**Observed cost:** [what becomes weaker, redundant, vague, or mistrusted]

**Original:**
> exact passage

**Replacement:**
> exact drop-in replacement, or `[Delete.]`

**Why it fails:** [one or two sentences connecting the judgment to reader
effect and the actual scene, not merely naming a rule]

---

### [HIGH] S12 — Scene exits unchanged (structural)
**Location:** [start] through [end]

**Transformation rule:** [what needs to become perceptibly different without
inventing an unauthorized plot event]

**Original (worked anchor):**
> exact passage

**Replacement (worked example):**
> exact revised passage

**Remaining anchors:** [exact anchors needing the same treatment]
**Span ends:** [unique reference]

---

## Defensible Exceptions *(only when genuinely tested)*

- [Exact passage] — [the concrete effect proving why a likely smell succeeds
  here. Never cite house style or authorial intent by itself.]

## Proven Strengths *(optional; evidence only)*

- [Exact passage] — [the specific function it performs well]

---

*Prose-smell review completed.*
```

Omit **Defensible Exceptions** when no likely false positive needs explanation.
Omit **Proven Strengths** when nothing merits a specific callout; there is no
praise quota. Never use either section to soften the summary or findings. Use a
generic footer for prose from outside this project (add ": for this novel" to the closing line when reviewing a chapter here).

## Applied-status tracking

This reviewer only reports suggestions. When `draft-from-review` applies a
finding, it may add `**Status:** Applied <date> — see
<chapter>/drafts/Changelog.md` beneath that finding's **Why it fails** or structural
note. Preserve existing status lines when revising a report unless the proposed
fix itself changes.

## Hard safeguards

- Never report a maxim by itself as proof of bad writing.
- Never soften a supported verdict to spare the author's feelings.
- Never treat `it's the writing style` as a defense without exact evidence that
  the passage's effect succeeds.
- Never confuse a possible function with a successfully executed function.
- Never bury the verdict after caveats, praise, or a specialist referral.
- Never impose brevity where atmosphere, reflection, humor, or worldbuilding is
  earning its length.
- Never ban passive voice, adverbs, telling, fragments, long sentences,
  figurative language, or repetition.
- Never erase useful ambiguity or make subtext explicit in the replacement.
- Never withhold established information merely to create suspense.
- Never rewrite a character into the reviewer's preferred voice.
- Never insult the author or substitute aggression for analysis.
- Never turn this into an AI-authorship judgment; use
  `anti-ai-prose-review` for model-shaped prose concerns.
- Never modify manuscript files during the review.
