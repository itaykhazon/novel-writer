# Novel-writing vault boilerplate

This is a generic export of the AI-assisted novel-writing workflow originally built for the **Afela** project, stripped of that book's specific story content so it can be dropped into a new novel's own folder. It gives an AI assistant (Codex CLI, Claude Code, or Cowork) a codex-and-skills structure for planning chapters, drafting them in a consistent voice, running a structured review-and-fix cycle, keeping a lore codex in sync with the manuscript, and exporting a finished PDF — without you having to re-explain your process from scratch every session. None of it assumes a particular genre, POV, or tense: the skills are written to read their specifics (genre, first/third/omniscient, past/present, register, comp titles) from a small set of reference files instead of hardcoding any of it.

## What's in here

```
AGENTS.md                    ← routing file: read this first, every session
README.md                    ← this file
LICENSE                      ← MIT, scoped to the boilerplate/tooling — see the note at its top
.gitignore                   ← Obsidian workspace state, OS junk, Python cache, PDF build output
.gitattributes                ← normalizes line endings across Windows/macOS/Linux
.agents/skills/               ← skills for Codex CLI (the agentskills.io standard)
.claude/skills/               ← identical mirror, for Claude Code
codex/                        ← your story bible / lore database
  00 Index.md                 ← vault map + current manuscript status — start here
  Genre.md                    ← one line: your genre
  Writing Style.md             ← POV, tense, voice, formatting rules — always in effect
  Craft Influences.md          ← your comp titles/authors + researched craft implications
  Editing Workflow.md          ← approval rules, changelog discipline, canon-conflict handling
  00 Braindump.md              ← your full story bible (future intent, not yet-canon)
  characters/ locations/ plot/ species-factions/ systems-mechanics/ snippets/
                                ← one folder per entity type, each with an 00-index
  outline/                     ← thread + arc templates for chapter-level plotting
  templates/                   ← frontmatter/section skeletons every "add" skill uses
novel/                        ← the manuscript itself (empty until you plan a chapter)
reviews/                      ← saved review reports, one per chapter
```

## Setup checklist for a new novel

1. **Find-and-replace `{{NOVEL_TITLE}}`** across the whole vault with your book's actual title. It appears in `AGENTS.md`, throughout `codex/`, and in skill descriptions/scripts under `.agents/skills/` and `.claude/skills/` (both copies — keep them identical).
2. **If you're turning this into its own git repo**, `git init` here and make an initial commit — `.gitignore` and `.gitattributes` are already in place. Decide what to do with `LICENSE` first (see the note at the top of that file): it's scoped to just the boilerplate/tooling, not your manuscript, but replace or remove it if that split doesn't match what you want for your own repo.
3. **Run `populate-project`** — this is the fast path for the rest of this checklist. It interviews you (via the `grilling` skill) about genre, POV/tense, register, comp titles, and formatting conventions, researches your comp titles and genre-reader expectations online, and writes the results into `codex/Genre.md`, `codex/Writing Style.md`, `codex/Craft Influences.md`, `chapter-cycle/references/house-conventions.md`, and `target-audience-readthrough/references/audience-model.md` — the files steps 4, 5, 8, and 10 below otherwise cover by hand. It never edits a `SKILL.md`. You can skip it and fill those files in yourself instead; the steps below describe what to fill in either way.
4. **Fill in `codex/Genre.md`** — one line.
5. **Fill in `codex/Writing Style.md`** and **`codex/Craft Influences.md`** — your POV convention, tense, register, exact formatting rules (units, scene breaks, chapter openers, any in-fiction system/UI text), and your comp titles with what they mean for prose/pacing craft. `Writing Style.md` is the single source of truth other skills quote from; the more precisely both files are filled in, the better `draft-chapter` and the reviewers perform — their rules are written to flex to whatever these files declare rather than assuming any particular genre or POV.
6. **Fill in `codex/00 Braindump.md`** — your story bible: premise, tone, main characters, world, mystery engine (if any), macro progression, motifs, and any guardrails you want an AI to respect while writing your book. This is the highest-value file to get right; everything else derives from it.
7. **Fill in `codex/00 Index.md`**'s "Manuscript status" and "Open threads" sections once you have any chapters planned or drafted — leave them as placeholders until then.
8. **Fill in `.agents/skills/chapter-cycle/references/house-conventions.md`** (and its mirror in `.claude/skills/`) with your novel's specific formatting conventions and the facts your reviewers keep getting wrong. This starts nearly empty by design — it fills in from experience (`populate-project` seeds its Formatting section from Step 3, but "Established facts that get broken" is yours to grow over time).
9. If your novel has species/factions or a systems/mechanics layer, keep those `codex/` subfolders; if not, delete them and remove the reference from `codex/00 Index.md`'s folder map.
10. Optional (skip if you ran `populate-project`): read `.agents/skills/target-audience-readthrough/references/audience-model.md` and rewrite its reader profile and research citations for your actual genre — the copy in this export still carries the epic sci-fi/LitRPG/dark-comedy genre it was ported from, flagged at the top of the file.

You do not need to create anything under `novel/` by hand — the first time you ask an assistant to plan a chapter, `add-chapter` creates the folder structure for you.

## The workflow, end to end

1. **`add-chapter`** — plans a chapter: folder, frontmatter, a beat-by-beat `Outline.md`, a future-tense `Summary.md`. Writes no prose. Ask for one chapter at a time, with a chapter number.
2. **`draft-chapter`** — writes the actual prose from an existing `Outline.md`, in the voice established by `Writing Style.md` and your character voice notes.
3. **`chapter-cycle`** — does both of the above and then runs a full review-and-fix loop (`proofread`, `prose-review`, `pacing-review`, `continuity-reviewer`) against a prebuilt context bundle, applies findings as exact-match diffs, and does one regression pass. This is the "draft and review a chapter" one-shot command; it's the most expensive skill in the set, so it's built to spend its budget on reviewer judgment rather than re-exploring the vault each time. See its `SKILL.md` for why, and `references/review-protocol.md` for the exact reviewer prompts.
4. **`add-to-codex`** — adds or updates a lore entry (character, location, mechanic, species/faction, plot thread) with correct frontmatter, cross-links, and index updates. Called automatically by the chapter skills when a chapter introduces something new; call it directly for anything else.
5. **`tweak-outline`** — before you commit to a structural change (a new ending, a removed subplot, a retconned reveal), this maps every file across the vault the change would touch, so you can see the blast radius before approving it. Report only, no edits.
6. **`draft-from-review`** — takes any saved review report (from the four cycle reviewers, `sanderson-review`, `anti-ai-prose-review`, or `target-audience-readthrough`) and applies its approved findings to the manuscript, logging every change to that chapter's `Changelog.md`.
7. **`export-novel-pdf`** — compiles a chapter range into a polished, phone-friendly PDF with your formatting conventions rendered properly.
8. **`sync-skills`** — reconciles `.agents/skills/` and `.claude/skills/` after you edit either one, and (manually) against a Cowork account original if you maintain skills there too.

Supporting skills you'll reach for less often: `populate-project` (interview plus web research to fill in this novel's genre/style/craft reference files — see the setup checklist above), `grilling` (batch-interview the user on several related open decisions at once, instead of guessing or asking one question at a time — wired into `add-chapter`, `add-to-codex`, and `populate-project`), `snippet` (park a spare fragment of prose for later, clearly marked non-canon), `roleplay-character` (talk to one of your characters in voice, then extract anything worth saving back to the codex), `sanderson-review` (a promise/progress/payoff structural audit using Brandon Sanderson's plotting framework — report only), `target-audience-readthrough` (a simulated cold read from one plausible genre reader).

## Design principles worth keeping

- **Plan and prose are separate invocations.** `add-chapter` never writes a sentence of manuscript prose; that's `draft-chapter`'s job alone. This keeps you in the loop on structure before any words are spent.
- **The manuscript beats the codex, and the codex beats the braindump.** When they disagree, that's a canon decision for you to make, not something an assistant should silently resolve.
- **Skill logic stays generic; specifics live in reference files.** No `SKILL.md` hardcodes a genre, POV, or tense — `draft-chapter`, `chapter-cycle`, `prose-review`, `pacing-review`, and `target-audience-readthrough` all read `codex/Genre.md`, `codex/Writing Style.md`, and `codex/Craft Influences.md` (or their own `references/` files) for the actual answer, and recalibrate their judgment calls to whatever those declare. `populate-project` exists to fill those files in without ever touching a skill's own logic.
- **Reviewers get a prebuilt context bundle, not vault access.** This is what makes `chapter-cycle` affordable — see its `SKILL.md`'s "Why this skill exists" section for the numbers that motivated it.
- **Fixes apply as exact-match diffs, never full-file rewrites.** Keeps edits minimal and auditable; every applied change gets logged to a chapter's `Changelog.md`.
- **Nothing gets applied without approval**, except the one explicitly-authorized exception: an explicit request to run `chapter-cycle` authorizes its own one-shot draft/review/fix loop end to end.

## A note on genre-specific content

This boilerplate was ported from a sci-fi/LitRPG project. The skill logic itself doesn't assume that genre — POV, tense, register, and pacing judgment calls are all deferred to `codex/Writing Style.md` and `codex/Craft Influences.md`, which ship as blank fill-in-the-blank files, not sci-fi/LitRPG defaults. Two things still carry the original project's fingerprints because they're genuinely genre-specific data rather than generic logic:

- `.agents/skills/target-audience-readthrough/references/audience-model.md` (and its `.claude/skills/` mirror) assumes an epic sci-fi/LitRPG/dark-comedy reader until you rewrite it — run `populate-project` to have it researched and rewritten for your actual genre, or do it by hand (it says so at the top of the file).
- `codex/plot/Mystery Discovery Tracker.md` and the outline's thread/beat-code structure assume your book has a plotted mystery or multi-thread structure worth tracking that granularly — delete or simplify if your book is more straightforward.

A few skills also mention "LitRPG rules," "stat/progression systems," or similar as one example among several of a mechanical-consistency check — these are marked optional/conditional throughout; ignore them entirely if your novel has no such system.

Everything else — the chapter-planning/drafting split, the review cycle, the codex structure, the editing-workflow rules, and every skill's actual craft logic — is genre-, POV-, and tense-agnostic by design and should work for any novel.
