---
name: tweak-outline
description: Analyze a proposed change to this novel's existing outline and produce a detailed, source-backed impact map across written canon, chapter plans, arc outlines, plot threads, macro progression, mystery tracking, character/location/mechanic lore, summaries, indexes, and status metadata. Use when the user wants to tweak, restructure, replace, move, add, or remove an outline beat; change a chapter, arc, progression system, mystery sequence, or ending; incorporate structural feedback into the plan; retcon a planned or drafted event; or understand every story and codex consequence before approving edits. Produce a report only; do not edit manuscript, outline, summary, or codex source files.
---

# Tweak an Outline

Turn a proposed story change into a complete implementation map. Reconstruct the current causal chain, design the smallest coherent revised chain, and identify every artifact that must change or be verified. Do not apply the change.

## Hard boundary

- Produce analysis and a change map only. Do not edit manuscript prose, chapter outlines, summaries, arc/thread files, codex notes, discovery flags, indexes, frontmatter, or the Braindump.
- Treat the user's suggestion as proposed intent until they approve an implementation pass.
- Follow `codex/Editing Workflow.md`: manuscript fact outranks codex, codex outranks `codex/00 Braindump.md`, and a contradiction between written chapters requires an explicit canon decision.
- Do not fold unrelated improvements into the map. Record pre-existing drift only when it obstructs or intersects the requested change.
- Do not draft finished prose. Outline-level replacement beats and short worked examples are allowed when needed to make a structural change unambiguous.

## 1. Normalize the requested change

Write a private change brief before searching:

- **Current version:** what the outline or manuscript presently says.
- **Proposed version:** what the user wants instead.
- **Required outcome:** the story function, emotion, rule, or payoff the change must preserve or create.
- **Fixed constraints:** explicit user decisions that are not open for redesign.
- **Open design questions:** choices the request leaves unresolved.
- **Scale:** scene/chapter, arc, multi-arc thread, system rule, or book ending.

When the suggestion came from a review, another task, or pasted discussion, extract the latest user-approved direction rather than treating every brainstorming option as part of the request. Treat those sources as proposal context, not current canon or outline authority. If the referenced conversation is available, read it; otherwise work from the provided change and state the missing context as a limitation.

## 2. Reconstruct the current authority stack

Always read completely:

1. `codex/00 Index.md`
2. `codex/Genre.md`
3. `codex/Writing Style.md`
4. `codex/Editing Workflow.md`
5. `codex/outline/00 Outline Index.md`
6. `codex/plot/00 Plot Index.md`
7. `codex/plot/Macro Progression.md`

Then read the smallest complete dependency set:

- every affected `codex/outline/Arc ...` file;
- every thread file named by affected beat codes, plus adjacent beats whose order or payoff may change;
- any review or saved proposal the user explicitly asks to incorporate;
- the affected chapter's `Outline.md`, `Summary.md`, and manuscript when it exists;
- the preceding summary and the next planned summary/arc entry for entry and exit continuity;
- `codex/plot/Mystery Discovery Tracker.md` (if your story has a mystery thread) for any clue, reveal, or major worldbuilding-truth change;
- linked character, voice, location, faction, mechanic, equipment, and motif notes needed to test the proposal;
- targeted passages from `codex/00 Braindump.md` when future intent is implicated.

For a multi-arc change, ending revision, new central antagonist, new progression spine, or altered climax, also read all arc files, all affected main/subplot threads, and `codex/outline/Sanderson Method — Working Guide.md` completely.

Search the whole vault for:

- exact names, terms, titles, UI labels, and quoted rules being changed;
- conceptual synonyms and consequences, not only the user's wording;
- affected beat codes in arc files, chapter frontmatter, outlines, and summaries;
- wikilinks to entities that may be promoted, renamed, removed, or split;
- manuscript statements that turn an apparently future-only tweak into a retcon.

Do not use summaries as proof of written fact. Verify a numeric, categorical, mechanical, physical-state, dialogue, or rule claim against the manuscript passage itself.

## 3. Classify every relevant claim

Build a compact authority ledger:

| Class | Meaning | Treatment |
|---|---|---|
| **LANDED CANON** | Appears in drafted manuscript | Preserve, or label the change `RETCON / DECISION NEEDED` with exact chapter evidence |
| **DERIVED RECORD** | Drafted `Summary.md`, current-status index text, codex "confirmed" claim | Resync to manuscript; never use it to overrule the page |
| **PLANNED INTENT** | Chapter outline, arc file, thread beat, macro future phase | Freely revisable after tracing prerequisites and payoffs |
| **TRACKER STATE** | Discovery `revealed` flags, manuscript-status fields, index status | Reflect what has landed; never advance merely because a plan changed |
| **FUTURE LORE** | Unrevealed codex or Braindump material | May be redesigned, but keep it visibly future/unrevealed |
| **DELIBERATE GAP** | Fact intentionally left unknown | Require an author decision; do not fill it for convenience |
| **PROPOSAL CONTEXT** | Review, past-task output, or brainstorming alternative | Use for rationale and options only; include only the latest direction the user adopts |

Surface substantive conflicts rather than averaging them together. Distinguish a conflict created by the proposed change from pre-existing drift.

## 4. Trace the dependency graph in both directions

Start at the changed beat and trace:

### Backward: what makes it possible

- promises and expectations that introduce it;
- clues, relationships, resources, permissions, rules, and character motives it requires;
- earlier chapters that state the old rule or prepare the old payoff;
- old terminology, progression measures, or antagonist behavior that must be retired.

### At the change: what exactly happens differently

- the revised event, decision, cause, cost, and exit state;
- whose agency causes it;
- which existing beat codes are transformed, moved, split, merged, retired, or replaced;
- whether the change needs a new recurring thread rather than being buried in one arc summary.

Create a new thread recommendation when the material has its own evolving question, crosses multiple arcs, needs repeated progress signposts, and produces a distinct payoff. Do not create a thread for a one-chapter tactic or a single supporting beat.

### Forward: what the new version changes

- later reactions, injuries, knowledge, resources, relationships, and choices;
- arc endings, chapter purposes, thread payoffs, climax logic, sequel hook, and title/number references;
- mechanics, factions, locations, characters, or motifs that become newly important;
- promises or beats that become orphaned when the old version is removed.

### Crosswise: what must remain synchronized

- chapter `Advances` / frontmatter beat lists and thread ordering;
- arc chapter ranges, endpoint descriptions, questions, and status tables;
- macro phases and the Outline Index's one-line arc endpoints;
- discovery sequence versus actual `revealed` state;
- character/voice, location, faction, mechanic, motif, and equipment notes;
- `00` indexes, Supporting Cast promotion, aliases, backlinks, and manuscript-status wording;
- Braindump passages that would otherwise keep regenerating the rejected plan.

For a new named entity, apply the `add-to-codex` thresholds in the map: keep a minor one-off in Supporting Cast; recommend a dedicated character folder once the entity is plot-relevant; recommend a standalone faction/mechanic/location note only when it recurs or needs independent rules.

## 5. Design the revised causal spine

Recommend one coherent integration when the evidence supports it. Use alternatives only for a genuine author choice that materially changes the book.

State the revised chain from setup to payoff in 5–15 numbered steps. Each step must identify:

- the arc/chapter window;
- the event or information change;
- the character or faction causing it;
- the thread/beat function it serves;
- what new state it creates for the next step.

Test the chain for:

- promise → visible progress → payoff → consequence;
- character agency and credible opposition;
- resource, injury, information, authority, and mechanical legality;
- mystery ordering and knowledge limits;
- causal coupling between plot, character, and setting;
- an ending earned by earlier choices rather than a last-minute exception.

Do not let a new helper, a faction that appears on cue, a newly granted permission, a rule exception, or unexplained technology solve the climax unless its limitation, cost, access path, and earlier setup are included in the map.

## 6. Write the impact map

Save the report to:

`reviews/<Change Name> - outline-change-map-<YYYY-MM-DD>.md`

Use this structure:

```markdown
# Outline Change Map: <Change Name>

## Change brief
- Current version:
- Proposed version:
- Required outcome:
- Scope:

## Authority and conflicts
| Claim | Status | Source | Consequence |

## Recommended revised spine
1. ...

## File-by-file impact map
| Priority | File | Section / anchor | Action | Current claim | Required revision | Why / dependency |

## New, promoted, or retired artifacts
| Artifact | Action | Trigger / placement | Required links or status |

## Decisions needed
1. ...

## Application order
1. ...

## Verification checklist
- ...

## Explicitly unchanged
- ...
```

Use these action labels consistently:

- `RETCON / DECISION NEEDED` — conflicts with landed manuscript.
- `REPLACE` — old planned material is superseded.
- `ADD` — new setup, beat, note, or linkage is required.
- `MOVE` — an existing beat changes location without changing function.
- `SPLIT / MERGE` — beat or chapter structure changes.
- `RETIRE` — old term, promise, beat, or artifact must stop propagating.
- `SYNC` — derived/status/index material must match a changed source.
- `VERIFY` — likely dependency requiring confirmation during application.
- `OPTIONAL` — improves delivery but is not necessary to make the requested change coherent.

Every `RETCON`, `REPLACE`, `ADD`, `MOVE`, `SPLIT / MERGE`, or `RETIRE` row must name a precise file and section/anchor. Quote the current claim briefly when precision matters; paraphrase long passages.

The map must cover, when relevant:

1. written manuscript and its changelog requirement;
2. chapter outlines and planned summaries;
3. arc files and thread beat definitions/order;
4. Outline Index and Macro Progression;
5. discovery tracker without prematurely flipping `revealed`;
6. characters/voice, locations, species/factions, systems/mechanics, and motifs;
7. root/sub-index and frontmatter/status synchronization;
8. Braindump future intent;
9. new/promoted/retired artifacts and links;
10. verification searches and audits after eventual application.

List structurally adjacent material under **Explicitly unchanged** when that boundary prevents accidental scope creep.

## 7. Build an executable application order

Order future edits by dependency, not by folder:

1. resolve landed-canon and deliberate-gap decisions;
2. revise the macro premise/end state;
3. revise or add plot threads and beat definitions;
4. revise arc/chapter assignments and chapter purposes;
5. revise planned chapter outlines/summaries;
6. revise future lore/mechanics/entities;
7. apply any separately approved manuscript retcons and append chapter changelogs;
8. sync indexes, frontmatter, statuses, and Braindump intent;
9. run stale-term, beat-coverage, backlink, and continuity checks.

Keep tracker flags tied to what has actually landed on the page even if their planned descriptions change.

## 8. Final verification

Before delivering the map, confirm:

- every changed/retired beat has all occurrences accounted for;
- no beat is orphaned and no chapter claims a beat whose prerequisite now occurs later;
- chapter ranges, totals, arc endpoints, phase labels, and titles remain consistent;
- every written contradiction is labeled as a decision rather than silently overwritten;
- every new climax capability has setup, access, limitation, cost, and an owner;
- character knowledge does not arrive before its source;
- discovery descriptions may change, but `revealed` flags do not change during planning;
- every promoted/new entity has a likely codex destination and index path;
- rejected terms and old plan language have explicit search targets;
- the report is the only file created or changed.

End by summarizing the recommended integration, the number of required source files, the highest-risk decisions, and the next approval boundary. Do not offer to apply the edits as though approval were already given.

## Calibration examples

- **Drafted chapter tactic changes:** expect a manuscript retcon decision, chapter changelog, `Outline.md`, `Summary.md`, relevant voice/mechanic notes, and the next chapter's resource/physical entry state. Do not rewrite an entire arc when the exit state stays unchanged.
- **Replacing one of the world's own rules with another** (a deadline structure swapped for a public-exposure structure, say): trace the drafted rule statement, any established institutional or Braindump rules it touches, the progression promise, affected chapter titles and difficulty beats, the replacement mechanic, any recurring character whose role depends on the old rule, downstream reputation or consequence effects, and how the finale uses the new mechanic.
- **Replacing a passive end-of-book choice with an escape/infiltration:** rebuild the ending backward—destination access, credential or means, opposition response, ally contribution, mystery discoveries that supply each prerequisite, new multi-arc pressure thread, and the revised sequel hook—while preserving any deliberate worldbuilding gaps unless the user decides them.
