# Novel-writing vault boilerplate

This is a generic, reusable export of an AI-assisted novel-writing workflow, stripped of any one book's story content so it can be dropped into a new novel's own folder. It gives an AI assistant (Codex CLI, Claude Code, or Cowork) a codex-and-skills structure for planning chapters, drafting them in a consistent voice, running a structured review-and-fix cycle, keeping a lore codex in sync with the manuscript, and exporting a finished PDF — without you having to re-explain your process from scratch every session. None of it assumes a particular genre, POV, or tense: the skills are written to read their specifics (genre, first/third/omniscient, past/present, register, comp titles) from a small set of reference files instead of hardcoding any of it.

## What's in here

```
AGENTS.md                    ← routing file: read this first, every session
README.md                    ← this file
LICENSE                      ← MIT, scoped to the boilerplate/tooling — see the note at its top
.gitignore                   ← Obsidian workspace state, OS junk, Python cache, PDF build output
.gitattributes                ← normalizes line endings across Windows/macOS/Linux
.agents/skills/               ← skills for Codex CLI (the agentskills.io standard) — includes
                                 8 "reviewer" skills (proofread, prose-review, etc.), each
                                 identified by frontmatter rather than folder location; see
                                 add-reviewer/references/reviewer-template.md for the contract
.claude/skills/               ← identical mirror, for Claude Code
codex/                        ← your story bible / lore database
  00 Index.md                 ← vault map + current manuscript status — start here
  project.json                ← your book's title/author; the one file scripts read
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

1. **Set your book's title** in `codex/project.json`. That is the only place in the vault it lives — no skill, script, or codex file hardcodes it, so there is no find-and-replace to run and no half-substituted placeholder to hunt down later. `populate-project` (step 3) writes this file for you if you'd rather answer it in the interview.
2. **If you're turning this into its own git repo**, `git init` here and make an initial commit — `.gitignore` and `.gitattributes` are already in place. Decide what to do with `LICENSE` first (see the note at the top of that file): it's scoped to just the boilerplate/tooling, not your manuscript, but replace or remove it if that split doesn't match what you want for your own repo.
3. **Run `populate-project`** — this is the fast path for the rest of this checklist. It interviews you (via the `grilling` skill) about genre, POV/tense, register, comp titles, and formatting conventions, researches your comp titles and genre-reader expectations online, and writes the results into `codex/Genre.md`, `codex/Writing Style.md`, `codex/Craft Influences.md`, `chapter-cycle/references/house-conventions.md`, and `target-audience-readthrough/references/audience-model.md` — the files steps 4, 5, 8, and 10 below otherwise cover by hand. It never edits a `SKILL.md`. You can skip it and fill those files in yourself instead; the steps below describe what to fill in either way.
4. **Fill in `codex/Genre.md`** — one line.
5. **Fill in `codex/Writing Style.md`** and **`codex/Craft Influences.md`** — your POV convention, tense, register, exact formatting rules (units, scene breaks, chapter openers, any in-fiction system/UI text), and your comp titles with what they mean for prose/pacing craft. `Writing Style.md` is the single source of truth other skills quote from; the more precisely both files are filled in, the better `draft-chapter` and the reviewers perform — their rules are written to flex to whatever these files declare rather than assuming any particular genre or POV.
6. **Fill in `codex/00 Braindump.md`** — your story bible: premise, tone, main characters, world, mystery engine (if any), macro progression, motifs, and any guardrails you want an AI to respect while writing your book. This is the highest-value file to get right; everything else derives from it.
7. **Fill in `codex/00 Index.md`**'s "Manuscript status" and "Open threads" sections once you have any chapters planned or drafted — leave them as placeholders until then.
8. **Fill in `.agents/skills/chapter-cycle/references/house-conventions.md`** (and its mirror in `.claude/skills/`) with your novel's specific formatting conventions and the facts your reviewers keep getting wrong. This starts nearly empty by design — it fills in from experience (`populate-project` seeds its Formatting section from Step 3, but "Established facts that get broken" is yours to grow over time).
9. If your novel has species/factions or a systems/mechanics layer, keep those `codex/` subfolders; if not, delete them and remove the reference from `codex/00 Index.md`'s folder map.
10. Optional (skip if you ran `populate-project`): fill in the `<fill in>` slots in `.agents/skills/target-audience-readthrough/references/audience-model.md` (and its `.claude/skills/` mirror) — who your genre's reader is, what makes them stop reading, and the research behind both. Leave the rest of that file alone; it's genre-agnostic as written.

You do not need to create anything under `novel/` by hand — the first time you ask an assistant to plan a chapter, `add-chapter` creates the folder structure for you.

## The workflow, end to end

1. **`add-chapter`** — plans a chapter: folder, frontmatter, a beat-by-beat `Outline.md`, a future-tense `Summary.md`. Writes no prose. Ask for one chapter at a time, with a chapter number.
2. **`draft-chapter`** — writes the actual prose from an existing `Outline.md`, in the voice established by `Writing Style.md` and your character voice notes. It writes sentences and nothing else: no Summary rewrite, no codex updates, no frontmatter reconciliation. That is deliberate — see the design principles below.
3. **`reconcile-chapter`** — the other half of drafting: brings the chapter frontmatter, `Summary.md`, the arc and outline indexes, the thread statuses and the codex in line with the prose that actually landed, and cross-checks that every number appears with the same value everywhere it's stated. Never edits prose.
4. **`chapter-cycle`** — does all of the above and then runs a full review-and-fix loop against a prebuilt context bundle, applies findings as exact-match diffs, and does one regression pass. The reviewer set it runs (currently `proofread`, `prose-review`, `pacing-review`, `continuity-reviewer`, `anti-ai-prose-review`) isn't hardcoded — it's read at run time from whichever skills declare `default-in-cycle: true` in their own frontmatter, in `cycle-order`; see `add-reviewer/references/reviewer-template.md`. This is the "draft and review a chapter" one-shot command; it's the most expensive skill in the set, so it's built to spend its budget on reviewer judgment rather than re-exploring the vault each time. See its `SKILL.md` for why, and `references/review-protocol.md` for the exact reviewer prompts. `sanderson-review`, `target-audience-readthrough`, and `prose-smell-review` (below) ship `default-in-cycle: false` and are not currently part of this bundle — run them separately.
5. **`add-to-codex`** — adds or updates a lore entry (character, location, mechanic, species/faction, plot thread) with correct frontmatter, cross-links, and index updates. Called automatically by the chapter skills when a chapter introduces something new; call it directly for anything else.
6. **`tweak-outline`** — before you commit to a structural change (a new ending, a removed subplot, a retconned reveal), this maps every file across the vault the change would touch, so you can see the blast radius before approving it. Report only, no edits.
7. **`draft-from-review`** — takes any saved review report from any reviewer skill (the ones in `chapter-cycle`'s default set, or any of the opt-in ones — `sanderson-review`, `target-audience-readthrough`, `prose-smell-review`) and applies its approved findings to the manuscript, logging every change to that chapter's `Changelog.md`.
8. **`export-novel-pdf`** — compiles a chapter range into a polished, phone-friendly PDF with your formatting conventions rendered properly.
9. **`sync-skills`** — reconciles `.agents/skills/` and `.claude/skills/` after you edit either one, and (manually) against a Cowork account original if you maintain skills there too.

Supporting skills you'll reach for less often: `populate-project` (interview plus web research to fill in this novel's genre/style/craft reference files — see the setup checklist above), `grilling` (batch-interview the user on several related open decisions at once, instead of guessing or asking one question at a time — wired into `add-chapter`, `add-to-codex`, `populate-project`, and `add-reviewer`), `snippet` (park a spare fragment of prose for later, clearly marked non-canon), `roleplay-character` (talk to one of your characters in voice, then extract anything worth saving back to the codex), `add-reviewer` (scaffold a new reviewer skill, conformant to `add-reviewer/references/reviewer-template.md`, in both `.agents/skills/` and `.claude/skills/` — use it instead of hand-writing a new reviewer's `SKILL.md`), `sanderson-review` (a promise/progress/payoff structural audit using Brandon Sanderson's plotting framework — report only), `target-audience-readthrough` (a simulated cold read from one plausible genre reader), `prose-smell-review` (a blunt, unsparing pass for broad craft smells — vagueness, ready-made phrasing, obscured agency, over-explained emotion, author-driven exposition, artificial withholding, mechanical cadence, static scenes — grounded in Strunk, King, Orwell, Vonnegut, and Le Guin; distinct from `prose-review`'s deep-POV/voice focus and `anti-ai-prose-review`'s model-shaped-language focus, and not currently wired into `chapter-cycle`).

## Design principles worth keeping

- **Plan and prose are separate invocations.** `add-chapter` never writes a sentence of manuscript prose; that's `draft-chapter`'s job alone. This keeps you in the loop on structure before any words are spent.
- **The outline locks function and outcome, not sentences.** An outline whose beats are written as finished prose turns drafting into transcription, and the chapter's quality gets capped at the quality of sentences written under planning constraints, before anyone knew what the scene would feel like. So `add-chapter` names events, costs and reveals and deliberately avoids the good phrasing; `draft-chapter` finds the words in the scene; and `chapter-cycle/scripts/check_outline_overlap.py` reports wording that made the trip anyway. Anything meant to land word-for-word — an oath, a system readout, a planted object's established description — goes under the outline's `## Verbatim anchors` heading and is exempt.
- **Prose and bookkeeping are separate invocations too.** `draft-chapter` writes; `reconcile-chapter` updates the records. They compete for the same attention and prose loses — a pass simultaneously tracking resource budgets, frontmatter accuracy and index status writes competent, characterless sentences. The reviewers downstream can remove what's wrong with a draft; none of them can supply what a draft never had, so the drafting pass is where the attention has to go.
- **The manuscript beats the codex, and the codex beats the braindump.** When they disagree, that's a canon decision for you to make, not something an assistant should silently resolve.
- **Skill logic stays generic; specifics live in reference files.** No `SKILL.md` hardcodes a genre, POV, or tense — `draft-chapter`, `chapter-cycle`, `prose-review`, `pacing-review`, and `target-audience-readthrough` all read `codex/Genre.md`, `codex/Writing Style.md`, and `codex/Craft Influences.md` (or their own `references/` files) for the actual answer, and recalibrate their judgment calls to whatever those declare. `populate-project` exists to fill those files in without ever touching a skill's own logic.
- **Reviewers get a prebuilt context bundle, not vault access.** This is what makes `chapter-cycle` affordable — see its `SKILL.md`'s "Why this skill exists" section for the numbers that motivated it.
- **Every reviewer follows one template, and declares itself in frontmatter, not folder location.** `add-reviewer/references/reviewer-template.md` is the contract (required sections, plus `reviewer-kind`, `reviewer-scope`, `thinking-level`, `complexity`, `default-in-cycle`, `cycle-order`) every reviewer skill satisfies — each one lives as a normal top-level skill like any other, so both Codex CLI and Claude Code discover it directly. `chapter-cycle/scripts/list_reviewers.py` reads that frontmatter to decide which reviewers run automatically and in what order — adding or reordering a reviewer never requires editing `chapter-cycle` itself. `add-reviewer` scaffolds a new one against the same template.
- **Fixes apply as exact-match diffs, never full-file rewrites.** Keeps edits minimal and auditable; every applied change gets logged to a chapter's `Changelog.md`.
- **Nothing gets applied without approval**, except the one explicitly-authorized exception: an explicit request to run `chapter-cycle` authorizes its own one-shot draft/review/fix loop end to end.

## A note on genre-specific content

This boilerplate was ported from a sci-fi/progression project, but nothing in it now assumes that genre. POV, tense, register and pacing judgment calls are deferred to `codex/Writing Style.md` and `codex/Craft Influences.md`, which ship blank. Worked examples in the reviewer skills use a deliberately neutral placeholder cast and a placeholder mechanic, labelled as illustrative — they show the shape of a finding, not anyone's story. One file ships with its genre-specific content empty rather than filled in with the wrong genre:

- `.agents/skills/target-audience-readthrough/references/audience-model.md` (and its `.claude/skills/` mirror) has `<fill in>` slots for who your reader is, what makes them stop reading, and the research behind both. Run `populate-project` to have that researched and written, or do it by hand. Unfilled, that skill simulates a reader calibrated to nobody — which is worse than not running it.

One structural assumption remains, and it's about plot shape rather than genre: `codex/plot/Mystery Discovery Tracker.md` and the outline's thread/beat-code structure assume your book has a plotted mystery or multi-thread structure worth tracking that granularly — delete or simplify if your book is more straightforward.

A few skills mention progression systems, stat panels or in-fiction interface text as one example among several of a mechanical-consistency check — these are marked optional/conditional throughout; ignore them entirely if your novel has no such system.

Everything else — the chapter-planning/drafting split, the review cycle, the codex structure, the editing-workflow rules, and every skill's actual craft logic — is genre-, POV-, and tense-agnostic by design and should work for any novel.
