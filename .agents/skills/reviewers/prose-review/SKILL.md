---
name: prose-review
description: |
  Review fiction prose for craft-level style issues — narrative distance/filter words, free indirect discourse (how deeply narration sits inside the POV character's voice), sentence and paragraph rhythm, sensory range, concrete grounding of unfamiliar worldbuilding, and over-explained emotion. This is a STYLE/VOICE pass, distinct from proofread (grammar/spelling/punctuation) and continuity-reviewer (facts/lore/timeline). Use whenever the user asks to review, critique, or tighten the prose/voice/POV of a chapter, asks "does this sound too distant/flat," wants a deep-POV or free-indirect-discourse pass, or wants feedback on pacing/rhythm at the sentence level. Also use proactively after drafting a new chapter, alongside proofread and continuity-reviewer, as part of the standard review pass — even if the user only says "review this chapter" without naming prose specifically.
reviewer-kind: line
reviewer-scope: chapter
thinking-level: medium
complexity: 5
default-in-cycle: true
cycle-order: 3
---

# Prose Review

This skill reviews prose craft — not grammar, not continuity, but the level between them: how close the narration sits to the POV character (or narrator), how the sentences and paragraphs move, and whether the voice matches the target style. It outputs a markdown report the writer can work through like a punch list.

## Why this skill exists (read before applying rules)

**Before applying any rule below, read `codex/Writing Style.md` and `codex/Craft Influences.md`** (if `populate-project` has been run, the latter holds this novel's actual comp titles/influences and what they mean for prose craft — research-backed, not guessed). This skill's rules are written to be genre- and POV-agnostic, but their *emphasis* should flex to match what those files actually declare: a novel written in first person present tense, an omniscient narrator, or a slow literary register needs this skill's judgment calls recalibrated accordingly, not applied as if every novel is close-third and fast.

The craft principle every rule below is a variation on: is the narration doing its job invisibly, sitting inside the POV character's (or narrator's) voice — or is it visibly standing between the reader and the character (the thing deep-POV craft calls "narrative distance")? This applies whether the target style is spare and fast or dense and literary; only the *acceptable amount* of distance shifts with the declared style. Keep that frame in mind for edge cases the rules don't cover explicitly.

## Scope and boundaries

This reviewer owns sentence- and paragraph-level craft: narrative distance,
free indirect discourse, rhythm, sensory range, over-explained emotion. Let
`proofread` own mechanical correctness, `continuity-reviewer` own facts and
timeline, `pacing-review` own scene-level structure, `prose-smell-review`
own broader reader-effect heuristics, and `anti-ai-prose-review` own
model-shaped phrase families specifically — a passage can be voice-perfect
and still trip one of those.

## Rules and confidence tiers

Confidence = how central this rule is to your novel's target style (per `codex/Writing Style.md` / `codex/Craft Influences.md`) and to prose craft generally. It sets how hard to push, not whether an instance is "wrong" — a HIGH-confidence rule still has real exceptions; use judgment, don't apply mechanically. If a rule's premise doesn't match your declared style (e.g. rule 6 assumes in-fiction system/UI text, rule 12 assumes a POV-name-opening convention), skip it entirely rather than forcing it — see each rule's own note.

### HIGH confidence — flag these often, with a concrete rewrite

**1. Filter words that add narrator-distance.**
Words like *saw, heard, felt, noticed, realized, watched, knew, wondered, thought* insert a reporting layer between the reader and the character's direct experience. Deep third-limited drops them and states the perception directly.
- `She heard the grinding before she saw it.` → `The grinding started before the shape came into view.` (or similar — cut the filter, keep the perception; swap pronoun/person to match your novel's actual POV)
- Don't over-flag: a filter word earns its place when it's doing comparative, sequencing, or uncertainty work (`heard... before he saw` is legitimate; `He looked down and saw his suit` is not — pick one).

**2. Narration that stays neutral-declarative instead of picking up the POV character's voice (free indirect discourse).**
This is the single biggest lever for closing narrative distance, whatever style you're writing in — a passage should sound like it's filtered through *this* character's specific mind, not any competent narrator's. Look for passages of pure external description or action with zero character-voice coloring — no wry aside, no value judgment, no comparison drawn from that character's own specific vocabulary or worldview — especially outside action peaks, and suggest where the character's voice could bleed into the narration. (If `codex/Craft Influences.md` names a comp known for this move, this is exactly where that comp's influence should show.)
- Weak: plain inventory or description that any narrator could have written.
- Strong (already in the manuscript, use as the target): *"He didn't want to get into the whole post-traumatic, exosuit-has-saved-my-life-more-times-than-I-can-count thing with a literal rock."*
- Rewrite suggestions here should sound like a specific character thinking, not just cut a word — this rule needs actual prose alternatives, not just deletions.

### MEDIUM-HIGH confidence — flag as a pattern across a passage, not per-sentence

**3. Sentence/paragraph rhythm defaulting to fragments instead of varying with tension.**
One-line-paragraph fragments are a legitimate tool in many genres and styles (some comp authors in `codex/Craft Influences.md` may lean on them hard in action beats — check there for whether that's true of this novel) — the problem is only when they become the *default* gear even in low-tension moments, which flattens the tool so it can't accelerate toward a real spike.
- Trigger: roughly 5+ consecutive one-line paragraphs that aren't building toward a specific beat (a hit, a reveal, a decision). Suggest consolidating some into a flowing sentence so the punchy ones stand out more.
- Don't flag fragment runs that are clearly earning their tension (an actual fight, an actual shock reveal) — that's the technique working as intended.

### MEDIUM confidence — flag when clearly present, don't invent instances

**5. Showing an emotion physically, then also stating it.**
Craft shorthand: "giving the punchline, then explaining the joke." If a passage already shows the emotion through body/action, a following sentence that names the emotion is usually redundant — trust the shown beat and cut or fold the naming in.

**9. Repetition / crutch words.**
Same word repeated in close proximity within a paragraph, or a word used unusually often across the chapter. This one is mechanically checkable — do an actual word-frequency pass on the chapter text rather than eyeballing it, and only flag words that clear a real threshold (not "the," "he," etc.) — build the tic list from this specific chapter, don't assume a fixed list.

**11. Description/worldbuilding blocks that stall momentum without earning their length.**
Whether extended texture and worldbuilding digression is welcome at all depends on the target style declared in `codex/Writing Style.md`/`codex/Craft Influences.md` — a slower, texture-forward register may deliberately spend real page-time here, while a lean/fast register may not. Where texture is part of the target style, flag a block only when it adds no new tension, no character read, and no plot-relevant information. Suggest trimming or redistributing, not deleting worldbuilding wholesale.

**13. Abstract worldbuilding introduced without a concrete POV anchor.**
New alien systems, cultures, technologies, and magic-like mechanics become
harder to absorb when the prose explains the category before giving the POV
character something physical to perceive, use, fear, misunderstand, or compare.
Apply the pyramid-of-abstraction principle: establish a concrete sensory detail,
interface behavior, object, action, or consequence first, then widen into the
abstract explanation only as far as the scene needs.
- Do not demand sensory decoration around concepts the reader already knows.
- The replacement must use the actual POV character's vocabulary and preserve
  uncertainty; do not turn a grounding fix into an exposition dump.

### LOW-MEDIUM confidence — nudge, don't demand

**7. Sensory range beyond sight.**
The manuscript already does this well in places (the Ch. 1 zero-g silence passage is a strong model: sound, pressure, heartbeat). Nudge toward more smell/temperature/proprioception in exposition-heavy or transitional passages that default to visual-only description — don't treat visual-only description as inherently wrong.

### LOW confidence — mostly backstops; only flag real violations, don't manufacture findings

**4. Direct emotion-naming with zero physical/behavioral accompaniment** (e.g., "he was scared" with nothing else). The manuscript is already good about pairing emotion with somatic detail — only flag the bare cases.

**6. In-fiction system/UI/readout text** (a stat panel, a HUD line, an in-world document block, etc.) — **only applies if your novel uses this convention at all; see `codex/Writing Style.md`.** Where it applies, it's a strength (hard-tech or magic-system grounding, rendered as part of the story's voice), not a problem — never flag its mere presence as an issue; only note opportunities for more personality in how the POV character reacts to/argues with it. If your novel has no such convention, ignore this rule entirely.

**8. POV discipline** — no head-hopping, no narrator knowledge the POV character doesn't have. Cheap to verify, should be a hard stop if it happens, but don't expect to find it often; continuity-reviewer also checks POV consistency, so don't duplicate its findings, just flag if you see it. Note in the finding that this is structural rather than a line-level fix (see Output Format below).
- When the fix is a genuine POV shift (not a mistake but an intentional dual-POV structure), prefer retiming the shift to land on a natural beat change (a new threat, a new scene) over rewriting the transition sentence in place — pair it with the manuscript's existing scene-break marker (`—`) rather than inventing a new convention. Whatever text ends up as the first line of the new POV's scene must still satisfy rule 12 (opens on the POV character's name) — check that explicitly, since retiming/inserting a break often relocates a line that used to be mid-scene into the opening-line position.

**10. Dialogue tag economy** — tags should stay plain (*said, asked, admitted*) rather than "hissed/quipped/exclaimed." Only flag if an unusual tag actually appears; the manuscript is already correct here.

### HIGH confidence — house style, mechanically checkable

**12. Chapters and scenes open with the POV character's name.**
**Only applies if `codex/Writing Style.md` declares this house rule for your novel — many novels don't use it, and it doesn't apply at all to a single-POV first-person novel where every scene is already "in" the same narrator.** Where it does apply, it's a firm house-style rule, not a craft judgment call: the first word (or opening clause) of every chapter, and of every new scene within it (i.e. right after a scene-break marker, whatever your novel's actual convention is), must be the POV character's name. It grounds the reader in whose head they're in immediately, especially important right after a scene break where the POV may have just shifted. If your novel has no such rule, skip this one.
- Check this mechanically: read the first line after the chapter's opening frontmatter/date-stamp, and the first line after every scene-break marker. If it doesn't open on the POV character's name, flag it — regardless of whether the sentence is otherwise well-written.
- When flagging alongside another fix (e.g. a rule 1 filter-word fix that would naturally displace the name — "Vess heard the grinding before she saw it" → cutting "Vess heard" as the filter fix), the replacement must still open on the name. Solve the underlying issue without losing the naming convention as a side effect (e.g. "Vess's lamp found the grinding before she did" keeps "Vess" first while still cutting the filter construction). The names here are placeholders for whoever your POV character actually is.
- This rule interacts directly with rule 8 (POV discipline/shifts) — see that rule's note below.

## Workflow

1. Read the chapter text in full before flagging anything — rhythm and voice issues only show up across a passage, not in isolated sentences. If reviewing several chapters together for context (e.g. to track a crutch word or rhythm pattern across a run), still read all of them before flagging.
2. Work rule by rule (or read once and tag passages against the rule list) — don't stop at the first few paragraphs.
3. For each finding, decide the confidence tier from the rule (don't invent a new scale) and write an exact **Original** quote and an exact **Replacement** — see Output Format below for what "exact" requires at every tier, including MEDIUM and LOW findings.
4. Order the report HIGH → MEDIUM-HIGH → MEDIUM → LOW-MEDIUM → LOW, and within a tier, by order of appearance in the chapter.
5. **If a single request covers multiple chapters, produce and save one report file per chapter** — each file scoped only to that chapter's findings, with locations/quotes local to that chapter. Don't combine multiple chapters into one file, even though you read them together for context; this keeps each report directly consumable by `draft-from-review` one chapter at a time.
6. Save each report to the vault's top-level `reviews/` folder (a single vault-wide folder, sibling to `codex/` and `novel/` — create it if it doesn't exist yet). Do not save into a chapter's own `drafts/` folder — that's reserved for `Changelog.md` and applied-edit records from `draft-from-review`.
   Name each file `<Chapter Name> - prose-review-<YYYY-MM-DD>.md`, e.g. `Chapter 4 - Title - prose-review-2026-08-14.md`.
7. Close with a short "what's already working" note — name 1-3 specific passages that hit the target style, so the writer isn't only seeing problems. Pull directly from the chapter; don't generate generic praise.

## Output Format

Every finding, at every tier, must give an exact **Original** quote and an exact **Replacement** — never a description-only note like "consider adding more sensory detail here." The report should be directly usable by `draft-from-review` as a find/replace list, without the writer or another skill having to guess what text to change.

Two kinds of findings need two different treatments:

- **Mechanical findings** (most HIGH/MEDIUM-HIGH/MEDIUM/LOW-MEDIUM findings, and most LOW findings): give the exact original text and the exact replacement text, verbatim, quoted in full — the same span, so it can be applied as a straight substitution.
- **Structural findings** (chiefly rule 8, POV discipline, and any rhythm/voice issue that spans a whole scene rather than one passage): a single Original/Replacement pair isn't enough. Instead:
  1. State the transformation rule in plain language (what has to change and why).
  2. Give one worked **Original → Replacement** example for the start of the flagged span, following that rule.
  3. Explicitly instruct that the same rule applies through the rest of the flagged span, and name where that span ends.
  This keeps even a big structural finding actionable rather than just descriptive — `draft-from-review` (or the writer) can apply the stated rule mechanically past the worked example, instead of being left with only a note.

```markdown
# Prose Review: [Chapter Name]

## Summary

| Tier | Count |
|------|-------|
| HIGH | X |
| MEDIUM-HIGH | X |
| MEDIUM | X |
| LOW-MEDIUM | X |
| LOW | X |

## Findings

### [HIGH] Rule 1 — Filter word
**Location:** [paragraph/line reference]

**Original:**
> quoted passage, exact and complete

**Replacement:**
> rewritten passage, exact and complete — a direct drop-in substitution for the Original span

**Why:** one or two sentences tying it back to the rule and, where relevant, the target style (e.g., "this is the move `codex/Craft Influences.md` names for [comp author] — let the voice do the explaining").

---

### [MEDIUM] Rule 9 — Crutch word
**Location:** ... (if a pattern spans several instances, list each instance as its own Original/Replacement pair, numbered, so each can be applied independently)

**Original:** exact quoted instance
**Replacement:** exact fix for that instance
**Pattern note:** e.g. "'shudder(ed)' appears 4 times in this chapter, 2 within the same paragraph (lines X, Y) — see instances 1-4 below."

---

### [LOW] Rule 8 — POV shift (structural)
**Location:** [start of span] through [end of span]

**Transformation rule:** plain-language statement of what has to change across the whole span.

**Original (start of span):**
> quoted passage

**Replacement (worked example):**
> rewritten passage following the transformation rule

**Note:** "Apply the same rule through the rest of the flagged span, ending at [reference]."

---

## What's Already Working

- [specific quoted passage] — [why it hits the target style]

---

*Prose review completed for this novel.*
```

## Applied-status tracking

`prose-review` does not mark findings as applied — it only produces the report. Once `draft-from-review` applies a finding to the manuscript, it writes a `**Status:** Applied <date> — see <chapter>/drafts/Changelog.md` line back into this report immediately below that finding's `**Why:**` (or `**Note:**` for structural findings). If you're revising an existing report (e.g. incorporating author feedback on a finding that was already applied in a prior pass), preserve any existing `**Status:** Applied` line on findings you don't change, and remove it only if the finding's fix is being substantively replaced by a new, not-yet-applied one.

## Key principles

- **This is a style pass, not a correctness pass.** Every finding should be arguable, not a rule violation — phrase the "Why" as "consider" or "this could," not "this is wrong." The Original/Replacement text itself should still be exact and directly usable, even though the underlying judgment is a suggestion.
- **Confidence tier governs how hard to push, not whether to flag, and not whether it gets an exact fix.** A LOW-confidence rule that's genuinely violated still gets flagged, and still gets an exact Original/Replacement (or the structural worked-example treatment) — it just gets a lighter touch in the "Why."
- **Rewrites must sound like the scene's actual POV character, not like generic "better prose."** A rewrite that fixes the filter word but reads like a different author's voice has failed rule 2 while fixing rule 1.
- **Ground rewrites in the POV character's specific vocabulary and worldview, not generic literary imagery.** If a character's established voice notes (`<Name> - Voice.md`) show them thinking in a particular register — mechanical/technical, legalistic, folksy, clinical, whatever's actually established — a rewrite that reaches for a mismatched comparison instead of that working vocabulary is off-voice even if it's well-written on its own terms. Match the register the voice note actually establishes rather than defaulting to a "literary" tone.
- **Favor a rewrite that pulls double duty over one that only fixes the flagged problem.** A line that fixes the filter word *and* sharpens character voice, or a beat that fixes a rhythm issue *and* reveals something, beats a rewrite that's merely correct — a single element doing two jobs (plot and character, action and voice) reads as tighter than either job done alone. Don't force it: a clean single-purpose fix beats a contrived one chasing a second function that isn't actually there.
- **When applying multiple house rules to the same passage, satisfy all of them, not just the one you started with.** A rule 1 (filter word) fix that ends up displacing the POV character's name from the opening position also breaks rule 12; a rule 8 (POV shift) fix that solves the transition but starts the new scene on the wrong word breaks rule 12 too. Re-check the edited passage against the other HIGH rules before finalizing a finding.
- **Don't relitigate continuity or grammar.** If something is a fact/lore/timeline problem, note it exists and point to continuity-reviewer; if it's a typo or grammar slip, point to proofread. Don't duplicate their findings in this report.
- **Protect the parts of the style that are already working** (system/HUD text as voice, somatic emotion, plain dialogue tags) — actively don't invent findings against rules 4, 6, 8, 10 just to have something in every category.
