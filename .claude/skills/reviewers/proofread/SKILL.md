---
name: proofread
description: |
  Proofread fiction and novel chapters for grammar, spelling, and punctuation errors. Use whenever the user provides text that needs error-checking or asks to proofread, edit, check for typos, or review a chapter from their novel. Focus on mechanical errors (spelling, grammar, punctuation) while respecting intentional stylistic choices common in fiction. Outputs a markdown report with suggestions for the writer to review.
reviewer-kind: line
reviewer-scope: chapter
thinking-level: very-low
complexity: 1
default-in-cycle: true
cycle-order: 5
---

# Proofreading Skill for Fiction

When asked to proofread text, follow this workflow and output a **markdown file** with the findings.

## What to Check

Focus on these core error categories:

1. **Spelling & Typos** — misspelled words, typos, autocorrect errors, repeated words
2. **Grammar** — subject-verb agreement, verb tense consistency, run-on sentences, misplaced modifiers, pronoun-antecedent agreement, unclosed quotation marks
3. **Punctuation** — missing or incorrect commas in compound sentences, unclosed quotes, apostrophe errors (contractions/possessives), incorrect dialogue punctuation
4. **Capitalization** — improper capitalization of proper nouns, obvious errors

## Do NOT Flag

- Deliberate sentence fragments or short sentences (stylistic in fiction)
- Creative capitalization or punctuation for voice/effect
- Formatting (italics, bold, spacing, indentation)
- In-fiction interface text, alerts or technical readouts in all caps, where the novel uses that convention
- Scene-setting text in italics
- Stylistic dialogue punctuation or dialect/accent writing
- Factual accuracy, worldbuilding, continuity, or continuity issues
- Word choice, tone, or narrative voice

## Scope and boundaries

This reviewer owns mechanical correctness only: spelling, grammar,
punctuation, capitalization. Everything else is a sibling reviewer's job —
`prose-review` owns sentence-craft and voice, `prose-smell-review` owns
broader craft heuristics (vagueness, over-explaining, static scenes),
`anti-ai-prose-review` owns model-shaped phrasing, `pacing-review` owns
scene-level structure, and `continuity-reviewer` owns facts, lore, and
timeline. If a passage is grammatically correct but reads flat, generic, or
factually wrong, that is not this reviewer's finding to make.

## Where to Save

Save the report as a markdown file in the vault's top-level `reviews/`
folder (a single vault-wide folder, sibling to `codex/` and `novel/` —
create it if it doesn't exist yet). Do not save reports into a chapter's
own `drafts/` folder — that folder is reserved for `Changelog.md` and
applied-edit records written by the `draft-from-review` skill, not for
review reports themselves.

Name the file `<Chapter or Scope Name> - proofread-review-<YYYY-MM-DD>.md`,
e.g. `Chapter 3 - Repurposed - proofread-review-2026-08-14.md`.

If a single request covers multiple chapters, save one file per chapter
(each containing only that chapter's findings, with location references
local to that chapter) rather than one combined file — this lets
`draft-from-review` process each chapter independently and keeps the
vault-wide `reviews/` folder scannable by chapter.

## Output Format

Create a markdown file with this structure. Every single error, in every
category, must include the exact original text and the exact suggested
fix — never a description-only note. This makes the report directly
consumable by `draft-from-review` as a straight find/replace.

```markdown
# Proofreading Report: [Chapter/Section Name]

## Summary

**Total errors found: X**

| Category | Count |
|----------|-------|
| Spelling/Typos | X |
| Grammar | X |
| Punctuation | X |
| Capitalization | X |

## Errors

### Error 1: [Category]
**Location:** [Paragraph or section reference]

**Original text:**
> original passage here

**Suggested fix:**
> corrected passage here

**Why:** Brief explanation of the grammar rule or error type.

---

### Error 2: [Category]
...

## Notes

- Any patterns observed (e.g., "Recurring its/it's confusion")
- Sections that are particularly strong
- Any areas of uncertainty or subjective calls

---

*Proofreading completed for this novel.*
```

## Workflow

1. Read the provided text carefully, in full
2. Look for errors in the four categories above
3. For each error, note:
   - The exact location/context
   - Original text (quoted exactly, verbatim)
   - Suggested correction (quoted exactly, verbatim — never paraphrased or left as a description)
   - Why it's an error (the rule or reason)
4. Order errors by appearance in the text
5. Generate the markdown report and save it to the vault-wide `reviews/`
   folder using the filename pattern above (one file per chapter covered)
6. Make the report actionable: writer should be able to quickly scan it and decide whether to accept each suggestion

## Key Principles

- **Respect authorial voice:** Fiction writers use fragments, creative punctuation, and unconventional capitalization intentionally. If it looks purposeful, don't flag it.
- **Focus on clarity:** Only flag errors that genuinely confuse meaning or violate grammar rules.
- **Be precise:** Show exact text and exact correction; don't paraphrase.
- **Be concise:** One sentence max per explanation.
- **Consistency matters:** If the same error appears multiple times (e.g., its/it's confusion), note the pattern and list each instance — each instance still gets its own exact original/fix pair.
