---
name: continuity-reviewer
description: Check a manuscript chapter against the codex for continuity errors, including character traits, locations, timelines, plot threads, lore, any stat/progression-system rules, resource budgets, and whether climactic solutions obey established capabilities, limitations, and costs. Use when reviewing or revising a chapter, proofreading for continuity, checking lore consistency, verifying character or item state, ensuring plot beats resolve in order, checking timeline logic, or testing whether a mechanical payoff is earned.
reviewer-kind: line
reviewer-scope: chapter
thinking-level: high
complexity: 8
default-in-cycle: true
cycle-order: 1
---

# Continuity Reviewer for Story Codex

When you review a chapter for continuity, this skill reads the chapter text and cross-references every detail against your story's codex (characters, locations, plot, mechanics, species lore). It returns a structured list of issues: character trait mismatches, timeline breaks, forgotten plot threads, location state inconsistencies, and rule violations — each flagged by severity so you know what to fix first.

## Scope and boundaries

This reviewer owns facts: character/location/item state, timeline,
plot-thread status, mechanical/system rules, and whether a payoff is
factually earned. It does not own mechanical correctness (`proofread`),
sentence-level craft or voice (`prose-review`, `prose-smell-review`), or
model-shaped phrasing (`anti-ai-prose-review`) — a passage can be
continuity-clean and still weak prose, and that's those reviewers' finding
to make, not this one's.

## How to use

You'll need:
1. **The chapter text** — the file itself, in the manuscript folder
2. **Access to your codex** — the skill reads your indexed story bible (characters, locations, plot, species, systems) directly from `codex/` in the vault
3. **Optional context** — if this chapter references prior chapters, mention which ones

## What the skill checks

### Beat Advancement (NEW - Primary Check)

If your outline labels plot threads with numbered beats that each chapter must advance, the skill verifies:

- **Beat presence**: Does the chapter actually show the beats it's supposed to? If Chapter 7 should advance A4 (responsibility), does the POV character make a decision they own?
- **Beat ordering**: Are discoveries happening in the right sequence? (C1 before C2 before C3?)
- **Deferred beats**: If a beat was assigned but didn't land, is it intentionally deferred to a later chapter? (Flag as note, not error)
- **Timeline fit**: Does the chapter's estimated-duration allow time for the beats to develop? (Example: "Thread D beat D6 requires overnight trust-building, but chapter is only 2 hours" → WARNING)

**How to use**: Include the `beats:` field in your chapter frontmatter (e.g., `beats: [A4, B1, C3, E1]`). The skill checks the chapter text against these beats. `codex/templates/Scene Frontmatter Template.md` defines this field (along with `timeline:` and `estimated-duration:`) — if a chapter's frontmatter is missing them, that's a gap in how the chapter was created, not something to infer around. Say so in the report rather than silently working without them (see "Limitations" below).

### Character Consistency
- **Traits & appearance**: Hair color, scars, disabilities, physical state — flagged if a chapter contradicts earlier description
- **Group membership**: Which crew, party, household, unit or faction a character belongs to and their role in it — flagged if contradicted
- **Backstory & knowledge**: What each character knows/has learned — flagged if a character acts on information before learning it
- **Abilities & equipment**: Special gear, powers, skill levels — flagged if used before acquisition or contradicts established state
- **Status**: Injured, dead, missing, unconscious — flagged if status changes without narrative explanation

### Location & World State
- **Descriptions**: Ship layout, building structure, terrain — flagged if contradicted (same location described differently)
- **Occupants**: Who's present, who should be there — flagged if a character appears in two places simultaneously
- **Equipment & tech state**: Does a ship still have working systems? Has a location been damaged or rebuilt? — flagged if state changes without explanation
- **Travel time**: Does travel between locations take a reasonable amount of time given established speeds/distances?
- **Access**: Can characters access a locked location? Do they have the key/password?

### Items, Props & Recurring Objects
- **Physical description**: Color, material, texture, size, distinguishing marks on any recurring non-character, non-location object — a weapon, an heirloom, a tool, a vehicle, a document — flagged if the same object is described differently across mentions with no in-story reason (an item that's "brass" when introduced and "bronze" three chapters later, with nothing on the page explaining the change, is exactly this category).
- **Check across every mention in the manuscript itself, not just the codex's summary of it.** A codex "Confirmed on the page" bullet is a compressed record, not the ground truth — always trace back to the actual chapter text for each cited chapter before confirming a match.
- **Compound descriptors are a red flag, not a resolution.** If a codex entry describes a recurring item with a slash-joined pair of terms (e.g. "brass/bronze compass," "grey/green cloak") — treat that as a sign the underlying chapters may use inconsistent language, not as evidence they already agree. Open the cited chapters and check whether the manuscript text itself actually uses matching description, not just whether the codex's paraphrase covers both.
- **State changes**: Is the item damaged, consumed, transformed, lost, upgraded, or moved to a new owner — flagged if it's used in a state the manuscript hasn't shown it reaching yet.
- **Ownership & location**: Who's holding it and where it physically is — flagged if it's used from the wrong hands or the wrong place without an on-page transfer.

### Cross-Artifact Fact Consistency (NEW)

Every chapter has at least three artifacts that can independently claim the same fact: the manuscript prose, that chapter's `Summary.md`, and any codex page (usually under `systems-mechanics/`) that documents the mechanic or item involved. These are supposed to agree because `Summary.md` is meant to be *derived from* the final prose — but revision rounds routinely change a detail in the prose (a percentage, a supply count, a rank tag, where on a body something landed) without anyone going back to update the Summary or the codex page that was written from an earlier draft. When that happens, the Summary and codex still agree with *each other* — because both trace back to the same stale draft — which makes the pair look like confirmation instead of the drift it actually is. This is the same trap as the compound-descriptor case above, one level up: two sources agreeing is not evidence they're both right if they share a common (outdated) origin.

**Check every fact of this shape against the actual final prose, not against the Summary or the codex first:**
- Any percentage or numeric readout (a device's remaining charge, a stat value, a damage number)
- Counts (supplies or ammunition remaining, opponents present, days elapsed)
- Rank, level, or classification tags (`Level 3, Uncommon` vs. `Level 3, Common`)
- Physical placement or location of an effect, wound, or item (which limb, which side, which body part)
- Which hand/side/arm a piece of equipment is used from

**Treat the prose as ground truth when it disagrees with the Summary or the codex.** If the chapter's `Summary.md` states a value, don't accept that as confirmation — open the actual chapter text at the cited location and verify the number is really there. A discrepancy here is a **WARNING at minimum** (**CRITICAL** if it's the kind of fact — like which hand a piece of gear is on, or a creature's rank — that determines what happens next in the story or contradicts several other chapters at once). Don't downgrade a numeric mismatch just because it "looks like" a typo; report it with both values and let `draft-from-review` (or the writer) decide, per its own re-sync step, which artifacts need correcting.

### Plot & Timeline
- **Event sequence**: Did events happen in the order described? Would characters have enough time to react/travel between scenes?
- **Open threads**: Are unresolved plot threads from earlier chapters addressed or intentionally left hanging? (Flagged as *note* if left intentionally)
- **Mystery discovery**: If your story has a mystery tracker, are clues revealed in order? Is information hidden until the right moment?
- **Character arcs**: Do character actions align with their known goals and arc progression?

### Mechanical & System Consistency
- **Stat/progression rules** (if applicable): Do stat increases, skill unlocks, and leveling follow established mechanics?
- **World rules**: Do contest, combat, or magic-system outcomes respect your story's established rules (an accord, tournament structure, magic law, etc.)?
- **Special mechanics**: Signature gear, artifact effects, faction abilities — do they work as documented?

### Mechanic & Payoff Legality

For every ability, item, rule, discovery, or resource that solves a meaningful
problem, verify all four conditions:

1. **Understanding:** The capability was established early and clearly enough
   for the reader to accept it as a solution. A new rule introduced at the
   moment it wins is a continuity/setup failure even if the codex contains
   future intent for it.
2. **Possession and state:** The character has the required equipment,
   knowledge, position, injury capacity, and current resource at that exact
   moment.
3. **Limitation and cost:** Fuel or charge, supplies, mass, time, reagent, physical
   strain, risk, authority, or another documented constraint remains active.
   Do not let a climax quietly waive the rule that made the power interesting.
4. **Expansion rather than rescue:** The solution recombines or deepens an
   established element. If it adds a new material, mode, upgrade, world rule,
   or exception, confirm it was introduced before the payoff and did not exist
   only to unlock this obstacle.

Trace finite resources across the scene, not only at isolated lines: opening
state → gains/reloads/recovery → spending → closing state. Flag an impossible
budget even when each individual readout looks plausible by itself. If a
project progression ledger exists, cross-check the chapter against its current
stage as another claim subordinate to the final prose.

### Lore & Species Consistency
- **Species/culture behavior**: Do characters from different species, cultures, or factions behave consistently with their established culture and biology?
- **Faction dynamics**: Relationships between factions — flagged if a character does something that contradicts known faction standings
- **Magic/tech systems**: If your world has established technical or magical rules, do characters use them correctly?

## What you'll get back

A structured report with issues organized by severity and type. The example
below uses a placeholder cast and mechanic — it shows the *shape* of a report,
not anything about your novel:

```
BEAT ADVANCEMENT
✓ A4 — Vess demonstrates responsibility in the route decision
✓ B1 — the party shows mutual respect under pressure
⚠ C3 — pursuers shown breaking off, but didn't explicitly show the "they do not return" rule
✓ E1 — Corin joins the group without asking permission

CRITICAL (stop the presses)
- Character trait mismatch: Vess's hand
  Line 242: "Vess flexed both hands" contradicts 00 Index: Vess lost her left hand in Ch 3

WARNING (fix before publishing)
- Timeline issue: Travel time implausible
  Lines 105-110: Character travels 500 km in described time — conflicts with the established travel speed
- Beat timing issue: Thread D beat D6 requires overnight bonding, but chapter estimated-duration is 2 hours
- Item description drift: the compass described as "brass" in Ch 4 and Ch 6, but "bronze" in this chapter with no on-page explanation — codex smooths this over as "brass/bronze," which is not itself confirmation the chapters agree
- Cross-artifact fact mismatch: this chapter's prose shows CHARGE readouts of 18% / 30% / 17%, but the chapter's own Summary.md and the mechanic's codex page both cite 14% / 26% / 4% / 17% — the Summary and codex agree with each other but not with the actual page

NOTE (consider for polish)
- Open thread status
  Ch 5 opened: "What did the watcher on the ridge signal?" — left unresolved through Ch 6 (intentional? flag for next chapter)
- Deferred beat: A5 assigned but deferred to Chapter 9 (noted in Summary)
```

Each issue includes:
- **Type**: What kind of continuity problem (beat, character, timeline, location, item, cross-artifact fact, plot, system, lore)
- **Severity**: CRITICAL / WARNING / NOTE
- **Location**: Line numbers in the chapter
- **Issue detail**: What's wrong and why
- **Codex source**: Which codex file contradicts this (so you can review the source)
- **Suggestion**: How to fix it — see **Output Format & Where to Save** below for exactly what this needs to contain

## Output Format & Where to Save

The illustrative block above is a quick-scan summary — the actual deliverable
is a **markdown file**, structured per-issue as below, so it's directly
usable by `draft-from-review`:

```markdown
# Continuity Review: [Chapter Name]

## Summary

| Severity | Count |
|----------|-------|
| CRITICAL | X |
| WARNING  | X |
| NOTE     | X |

## Beat Advancement

✓ A4 — Vess demonstrates responsibility in the route decision
⚠ C3 — pursuers shown breaking off, but didn't explicitly show the "they do not return" rule

## Issues

### [CRITICAL] Character trait mismatch — Vess's hand
**Location:** Line 242
**Codex source:** `codex/characters/Vess.md` — Vess lost her left hand in Ch 3

**Original:**
> Vess flexed both hands.

**Fix:** one of the two forms below, depending on what the issue actually needs:
- **Replacement** (use when the fix is a direct text swap — a description, a stat, a name, a line of dialogue that contradicts the codex):
  > exact corrected text, quoted in full, ready to substitute for Original
- **Guidance + worked example** (use when the fix isn't a clean swap — it touches plot logic, needs a scene-level change, or it's ambiguous whether the *chapter* or the *codex* is actually wrong): state the change needed in plain language, then show one worked example of the pattern so `draft-from-review` can apply it consistently instead of being left with only a description. If the codex itself might be the thing that's outdated, say so explicitly here rather than picking a side.

**Why:** one or two sentences.

---
```

For a **Cross-Artifact Fact Consistency** finding specifically, always name all
disagreeing artifacts (prose location, `Summary.md` line, codex file and line)
in the same issue rather than only citing one — that's what lets
`draft-from-review` update every affected file in one pass instead of fixing
the prose and leaving the Summary or codex silently wrong.

Give every issue an exact **Original** quote from the chapter text. Never
leave a finding as a bare description ("Vess's hand is
inconsistent") without also giving the exact contradicting text and one of
the two Fix forms above — that's what makes the report something
`draft-from-review` (or the writer) can act on directly rather than having
to re-derive the fix from a summary.

Save the finished report to the vault's top-level `reviews/` folder (a
single vault-wide folder, sibling to `codex/` and `novel/` — create it if
it doesn't exist yet). Do not save into a chapter's own `drafts/` folder
— that's reserved for `Changelog.md` and applied-edit records written by
`draft-from-review`, not for review reports.

Name the file `<Chapter Name> - continuity-review-<YYYY-MM-DD>.md`, e.g.
`Chapter 3 - Repurposed - continuity-review-2026-08-14.md`. If a single
run covers multiple chapters, save one file per chapter rather than
combining them, so each can be applied independently.

## How the skill works

1. Read the chapter text (from its file in the manuscript folder)
2. Read the codex: character files, location files, plot tracker, systems docs, etc.
3. Read the chapter's own `Summary.md`, if one exists — not just as background, but as a second claim to check the prose against (see Cross-Artifact Fact Consistency)
4. Scan the chapter text for references to entities (characters, locations, abilities, plot elements)
5. For each reference, check against the codex:
   - Do character descriptions match?
   - Do timeline references make sense?
   - Are plot threads addressed?
   - Do mechanical/system interactions follow the rules?
6. For every quantitative or categorical fact in the chapter (a number, a rank, a placement), check the same fact wherever `Summary.md` or a codex mechanics page also states it — flag any disagreement even if the non-prose sources agree with each other
7. Return issues grouped by severity and type — CRITICAL issues first

A bundled helper script, `scripts/codex_analyzer.py`, indexes the codex's
characters/locations/plot/mechanics folders into structured JSON and
surfaces compound-descriptor flags (see the Items/Props section above) up
front on stderr. Run it as `python3 scripts/codex_analyzer.py <path-to-codex>`
to get a quick structured index before reading the raw files, especially
useful on a large codex.

## Pro tips

- **Use the outline arc file**: Copy beats directly from `codex/outline/Arc <N> — <Title>.md` for your chapter. Don't guess.
- **Add timeline metadata**: `timeline: "same day as Ch 6, evening"` and `estimated-duration: "4 hours"` help the skill verify that your pacing matches beat requirements (e.g., "Does 2 hours allow time for Character D's arc moment?")
- **Provide summaries**: If you have chapter summaries (like `Summary.md` files), read those along with the full chapter. The "Beats Accomplished" section in the Summary makes verification instant — but remember a Summary is a claim to *check*, not a shortcut that lets you skip reading the actual prose for the facts it restates.
- **Flag deferred beats**: If you intentionally move a beat to a later chapter, note it in your Summary: "A5 — deferred to Ch 9". The skill will mark it as intentional, not an error.
- **Check the codex for gaps**: If your codex is missing a character or location document, the skill will note that it can't verify certain details. Use the `add-to-codex` skill to fill gaps.
- **Review context**: Read the codex source the skill cites — sometimes "contradictions" are actually valid plot developments the codex hasn't caught up to yet.
- **Use continuity-reviewer after drafting, and again after any round of applied fixes**: Run this skill on every new chapter before calling it done — and re-run it (or at least the Cross-Artifact Fact Consistency check) after `draft-from-review` applies edits, since that's exactly when a prose fix and its Summary/codex counterpart are most likely to drift apart. It's your final structural check, not just a one-time gate.
- **Audit for compound descriptors**: Periodically grep the `codex/` folder for slash-joined pairs ("X/Y compass," "X/Y cloak," etc.) in "Confirmed on the page" or similar bullets. Each one is a candidate cross-chapter description mismatch that was smoothed over instead of resolved — worth a quick check against the cited chapters even outside a full review pass.
- **This skill is scoped to one chapter on purpose, for cost reasons — it will not catch cross-chapter/whole-vault problems.** Beat-order contradictions between Thread files and already-outlined *future* chapters, Phase/status metadata drifting out of sync across `00 Index.md` and the outline files, and backlink orphans are all real categories of continuity problem, but they live outside any single chapter's bundle. Don't try to make this skill catch them by feeding it the whole vault — that reintroduces the cost problem `review-loop.md` measured. Instead, run a separate whole-vault audit periodically (every arc boundary, or every 3–4 chapters) — see `codex-structure` / project notes for the cadence, and `scripts/audit_links.py --orphans` in `chapter-cycle` for the mechanical half of it.

## Edge cases

- **New character introduction**: When a new character first appears, the skill won't flag trait issues if there's no codex entry yet (use `add-to-codex` to document them)
- **Intentional retcons**: If you're intentionally changing something in the codex, update that file first, then run continuity review
- **POV-limited information**: If a character doesn't know something yet, it's OK if the reader doesn't either — the skill will note this as context, not an error
- **Pre-written backstory vs. manuscript**: The codex may contain pre-established character info that hasn't been written into the manuscript yet. The skill prioritizes what's *on the page* — flag conflicts between manuscript and codex separately

## Limitations

The skill works best when:
- Your codex is up to date (if you haven't added a new character to the codex yet, the skill can't verify details about them)
- Traits and stats are documented in the codex (subtle inconsistencies in voice or tone are harder to catch than trait mismatches)
- Timeline logic is explicit (if you haven't documented travel times or character locations, the skill may miss timeline issues)
- Recurring items/props are checked against the actual chapter text, not just the codex's paraphrase of them — a codex bullet that already blends two chapters' wording into one compound description will read as "consistent" unless you open the source chapters yourself
- Chapter frontmatter actually carries `beats:`, `timeline:`, and `estimated-duration:` — if a chapter's frontmatter is missing these (check `codex/templates/Scene Frontmatter Template.md` for what should be there), say so explicitly in the report rather than silently inferring assignments; a missing field is itself a finding, not just an obstacle to work around

The skill will flag unclear references: if a chapter says "the ship" but the codex has three ships, the skill will ask for clarification rather than guessing.
