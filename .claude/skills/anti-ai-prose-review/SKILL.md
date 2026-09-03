---
name: anti-ai-prose-review
description: >-
  Review fiction prose for recurring AI-shaped language and "AI slop": stock ChatGPT/Claude sentence frames, canned connectors, contrastive negation, templated emotional beats, vague pseudo-depth, false dramatic endings, uniform cadence, and model-favored phrase clusters. Use when the user asks whether prose sounds AI-written, wants AI-assisted prose cleaned up, asks for an anti-slop or human-voice pass, mentions Claude-isms/ChatGPT-isms, dislikes overly dramatic paragraph or scene endings, or wants a chapter checked for generic chatbot cadence. Produce an actionable markdown review with exact original anchors and voice-matched replacements; do not claim to determine authorship.
reviewer-kind: line
reviewer-scope: chapter
thinking-level: low
complexity: 3
default-in-cycle: true
cycle-order: 4
---

# Anti-AI Prose Review

Review the surface prose for model-shaped repetition and replace generic machinery with scene-specific, character-specific writing. Treat the result as a style diagnosis, never an authorship detector.

## Required reading and tools

1. Read the supplied text in full before flagging anything.
2. Read `references/pattern-catalog.md` before reviewing; it contains the calibrated phrase families, thresholds, and research basis.
3. For a chapter, read `codex/Writing Style.md` and the POV character's voice guide before drafting replacements.
4. When the source is a local file of roughly 500 words or more, run:

   ```text
   python scripts/scan_prose.py <path-to-text-or-markdown>
   ```

   Use `--json` if structured results help. The scan is a candidate finder, not a verdict. Inspect every hit and paragraph-ending candidate in context; ignore quoted examples, system text, frontmatter, and intentional repetition.

## Scope and boundaries

Own these questions:

- Does the prose repeatedly fall into recognizable LLM sentence skeletons?
- Are connectors and emphasis devices doing real logical or dramatic work, or merely simulating it?
- Are emotional and sensory beats concrete to this character and scene, or interchangeable with another story?
- Does the passage preserve the established POV voice, or flatten into polished assistant voice?
- Do sentence and paragraph shapes feel mechanically even or repeatedly "punched up" by the same device?

Do not duplicate other reviewers:

- Let `proofread` own grammar, spelling, and punctuation correctness.
- Let `prose-review` own general deep POV, filter words, sensory range, and sentence craft unless the problem is specifically a model-shaped template or cluster.
- Let `pacing-review` own scene escalation and reaction-beat structure.
- Let `continuity-reviewer` own facts, lore, and timeline.

## Confidence and severity

Never assign an AI probability and never state that a person or model wrote the text. Ordinary human prose contains every individual pattern in this catalog.

Classify the revision need, not presumed provenance:

- **HIGH** — Several independent signal families cluster in one passage, a distinctive corpus-backed phrase repeats, or a model-shaped template noticeably replaces the POV voice across a sustained span.
- **MEDIUM** — A clear stock frame or phrase weakens a specific sentence, or one signal family recurs enough to become audible.
- **LOW** — A single weak or practitioner-observed signal is worth a light nudge because the replacement is materially more specific. Do not report LOW findings that amount only to personal taste.

Raise severity for density, repetition, cross-category clustering, sudden voice shift, and interchangeability. Lower it when the construction is precise, purposeful, rare in the text, or established in the author's baseline voice.

## Signal families

Apply the catalog, grouped into these report categories:

1. **Contrastive scaffolding** — repeated `not X, but Y`, `not just X; Y`, `no X, no Y, just Z`, or similar manufactured contrasts.
2. **Canned connectors and signposts** — essay-like transitions, summary sentences, and emphasis cues that announce importance instead of dramatizing it.
3. **Stock fiction phrasing** — overrepresented dialogue, body-language, silence, breath, heartbeat, gaze, and sensory formulas.
4. **Vague pseudo-specificity** — `something`, `somehow`, `the kind of`, `almost`, and `not quite` constructions that withhold the observation while implying depth.
5. **Hedging and connective filler** — `seemed to`, `appeared to`, `couldn't help but`, `found himself`, `without realizing`, and stage directions used as glue.
6. **Template rhythm** — repeated tricolons, fragment stacks, matched paragraph lengths, repeated sentence openings, and formulaic em-dash punches.
7. **Explained subtext or emotion** — dialogue/action followed by a translation of what it means, or a concrete beat followed by a generic emotional label.
8. **Over-dramatic landing or false closure** — compact epigrams, theatrical tail clauses, moralized summaries, and repeated paragraph endings that manufacture a climax or make several consecutive beats sound final.
9. **Lexical cluster** — several model-favored abstract or inflated words co-occurring. Never flag one vocabulary word by itself.
10. **Voice flattening** — several characters or narrative passages converge on the same polished, cautious, reflective register despite the scene's established voice.

## Workflow

1. Read the whole text without marking it up. Establish its POV voice, tension level, and deliberate recurring devices.
2. Run the scanner when applicable. Record category counts, repeated sentence openings, and clusters of dramatic paragraph endings, but do not copy its output uncritically into the report.
3. Build a short signal map. For each candidate, ask:
   - Would this sentence fit another scene or character with only the names changed?
   - Does the construction add information, or only emphasis and polish?
   - Is it isolated, repeated, or clustered with other signal families?
   - Does it conflict with the author's established voice?
   - Does the paragraph ending arise from a changed fact or image, or merely declare that the beat mattered?
4. Flag only passages that become better when made more direct, concrete, or character-specific. The goal is not to erase all familiar rhetoric.
5. For a suspected false landing, test deletion before rewriting. If the paragraph becomes weaker or loses a real change in stakes, knowledge, relationship, or action, keep the ending.
6. Draft an exact replacement in the actual POV character's diction. Preserve plot facts, blocking, formatting, and intentional rhythm.
7. Do a false-positive pass. Explicitly clear conspicuous scanner hits that are earned, voice-specific, literal, or isolated before assigning severity.
8. Order findings HIGH → MEDIUM → LOW, then by appearance within each tier.
9. If the source is a chapter, save one report per chapter in the top-level `reviews/` folder as `<Chapter Name> - anti-ai-prose-review-<YYYY-MM-DD>.md`. Do not edit manuscript prose and do not save reports in chapter `drafts/` folders.
10. If the user supplied an unnamed pasted passage, return the report in the response unless they asked for a file. Do not invent a chapter name.
11. Close with 1–3 exact examples that already sound specific and resistant to generic model cadence: surprising detail, asymmetric rhythm, real subtext, or unmistakable character voice.
12. Use the project-specific footer only for this novel's material. For unnamed or unrelated prose, use the generic footer shown below.

## Replacement rules

- Replace generic affect with an observable choice, sensory fact, or character judgment already supported by the scene.
- State the real claim directly instead of swapping one rhetorical template for another.
- Prefer the smallest span that removes the tic. Do not rewrite unrelated prose.
- Preserve useful ambiguity. Replace vague wording only when the text is pretending to be specific while making the reader supply the content.
- Do not "humanize" by injecting typos, slang, fragments, profanity, or randomness.
- Do not ban words. A replacement may retain a listed word when it is the most exact word.
- Do not sand away this novel's house style: its established sentence rhythm, POV-specific vocabulary, in-fiction system/UI readouts, character-specific dialogue rendering, and scene-break convention are not AI signals — see `codex/Writing Style.md`.

## Output format

Every finding needs an exact **Original** and **Replacement**. For a repeated structural pattern, give a transformation rule plus at least one worked exact swap and enumerate the remaining anchors. Supply a drop-in replacement for each remaining anchor unless the same mechanical deletion or substitution applies to all of them.

```markdown
# Anti-AI Prose Review: [Chapter or Scope]

## Summary

**Overall texture:** Clean / Light residue / Noticeable templating / Heavy templating

This label describes revision need, not authorship or an AI probability.

| Severity | Count |
|----------|-------|
| HIGH | X |
| MEDIUM | X |
| LOW | X |

## Signal Map

| Signal family | Observed pattern | Occurrences | Read |
|---------------|------------------|-------------|------|
| Contrastive scaffolding | `not X, but Y` variants | X | Isolated / Repeating / Clustered |

## Findings

### [MEDIUM] Stock fiction phrasing — vague expression cue
**Location:** [paragraph/line reference]
**Pattern evidence:** [phrase family, count, and any nearby supporting signals]

**Original:**
> exact passage

**Replacement:**
> exact drop-in replacement

**Why:** Explain what the template is substituting for and why the replacement better fits this scene and POV. Do not speculate about who wrote it.

---

### [HIGH] Template rhythm — repeated contrastive reframes across a span
**Location:** [start] through [end]
**Transformation rule:** State what repeated machinery should change and what direct principle replaces it.

**Original (worked anchor):**
> exact passage

**Replacement (worked example):**
> exact replacement

**Remaining anchors:** List the other exact instances that need the same treatment.

---

## Calibrated Non-Findings

- [Optional: name a conspicuous scanner hit or repeated device intentionally left alone, and explain its dramatic or voice function. Omit this section when nothing needs clarification.]

---

## What Already Sounds Specific

- [exact quoted passage] — [why its detail, rhythm, or voice resists generic model cadence]

---

*Anti-AI prose review completed. This is a style review, not an authorship determination.*
```

For a chapter, change the footer to: `*Anti-AI prose review completed for this novel. This is a style review, not an authorship determination.*`

## Applied-status tracking

This reviewer only reports suggestions. When `draft-from-review` applies a finding, it may add `**Status:** Applied <date> — see <chapter>/drafts/Changelog.md` beneath that finding's **Why** or structural **Note**. Preserve existing status lines when revising a report unless the proposed fix itself changes.

## Hard safeguards

- Never accuse the author of undisclosed AI use.
- Never cite one em dash, connector, cliché, polished sentence, or vocabulary word as evidence by itself.
- Never cite one short or dramatic paragraph ending as evidence by itself.
- Never turn a scanner count into a conclusion without reading the passage.
- Never penalize a repeated phrase inside dialogue or system text when repetition is characterization or interface design.
- Never optimize solely for evading AI detectors. Optimize for specificity, voice, clarity, and dramatic function.
