---
name: chapter-cycle
description: Draft an {{NOVEL_TITLE}} chapter from its existing Outline.md and then run the full review-and-fix cycle — proofread, prose, pacing and continuity reviewers, their findings applied as exact-match diffs, iterating until no IMPORTANT notes remain — then update Summary.md and the codex. Use when the user asks to write or draft a chapter and review it, to "draft and review" a chapter, or to run the review-and-fix loop on a chapter that already has prose. If the chapter has no Outline.md yet, use add-chapter first.
---

# {{NOVEL_TITLE}} — Draft & Review Cycle

One invocation: outline in, reviewed chapter out. This replaces running
`draft-chapter` and then the four review skills by hand.

The vault is a local folder — this skill operates directly on the files under
it (no bridge or staging step needed when running against a local checkout).

## Why this skill exists

A hand-run version of this loop cost several million tokens on the chapter it
was measured against. The measured breakdown showed the cost is **reviewer
turns × context size** — not report writing (about 1% of a reviewer's cost)
and not redrafting (under 1%). Three rules follow from that, and they are the
point of this skill:

1. Reviewers get a **prebuilt bundle**, so they never explore the vault.
2. Reviewers run at the cheapest effort level that's actually adequate for the
   job (see `references/review-protocol.md`).
3. Fixes are applied as **exact-match diffs**, never by rewriting the file.

Do not skip these to "be thorough." Thoroughness comes from the reviewers'
findings, not from how much they read to produce them.

That said, this scoping is a deliberate tradeoff, not a claim that per-chapter
review catches everything. It cannot see beat-order conflicts against
already-outlined future chapters, drift between `00 Index.md`'s status claims
and the outline files, or backlink orphans — those live outside any one
chapter's bundle by construction. See "Periodic whole-vault audit" at the end
of this file for what covers that instead.

---

## Phase 0 — Set up

Confirm the chapter number (never guess it). Then:

```bash
python3 scripts/build_bundle.py --vault <vault-root> --arc 1 --chapter 7 \
    --out /tmp/chapter-cycle/bundle.md
```

The script needs `novel/arc <N>/Chapter <n> - <Title>/Outline.md` to exist; if
it doesn't, stop and offer `add-chapter`.

The script writes one file containing the outline, the planned summary, the
previous chapter's summary and closing prose, the style and genre rules, and
every codex entry the chapter's frontmatter or outline points at — resolving
wikilinks by filename, by frontmatter `aliases:`, and by chapter folder. Read
that one file. Read `references/house-conventions.md`. That is your whole
research phase — do not open codex files individually.

Check the script's `unresolved` count. Anything listed is either a new entity
this chapter introduces (fine) or a real gap (not fine — track down why the
reference doesn't resolve before continuing).

To check the vault as a whole rather than one chapter:

```bash
python3 scripts/audit_links.py --vault <vault-root>
python3 scripts/audit_links.py --vault <vault-root> --orphans   # also lists
                                                                  # notes with
                                                                  # zero inbound
                                                                  # wikilinks
```

Run that at the end of any session that adds codex entries. A dangling wikilink
is invisible in Obsidian but silently strips context out of every future
bundle. `--orphans` is a softer signal (a resolvable note nothing links to,
like a drafted chapter's `Outline.md`) — informational, not something to
"fix" reflexively, but worth a look if the count keeps growing.

If `Outline.md` has `status: needs-input`, resolve its questions with the user
before writing anything.

Read the outline's `## Sanderson pass` before drafting. It is the chapter's
structural contract: promise, visible progress, POV want, escalation, payoff,
end-state change, and resource/limitation budget. For an older outline without
that section, derive a compact preflight from
`codex/outline/Sanderson Method — {{NOVEL_TITLE}} Working Guide.md` before Phase 1. Do not
add the full guide to the reviewer bundle; the chapter-specific conclusions
belong in the outline. Stop for user input if the planned climax requires an
unseeded ability, unavailable resource, or missing causal setup.

---

## Phase 1 — Draft

Write the chapter to a **local working copy** (e.g. `/tmp/chapter-cycle/chapter.md`), not
straight to the vault file. Everything in the loop operates on the working copy; it
goes to the vault once, at the end.

If the chapter file already holds prose, copy it to `drafts/v<N> - <date>.md` in
the vault before you begin.

Follow the outline's beats in order. You may deepen a beat, add connective
tissue, or find the specific words. You may not drop a beat, add a plot event,
introduce a character the outline doesn't have, or change the ending. If a beat
genuinely doesn't work in prose, say so and get the user's call — don't quietly
rewrite the plan. Respect the outline's **Constraints** section absolutely.

Voice and house rules are in `references/house-conventions.md` — read it in
full, it's written to be filled in for your novel's actual POV/tense/register,
not assumed. If it declares a scene-opening convention (many novels do, e.g.
opening on the POV character's name), that's typically the one that gets
broken most in practice — check it as you write each scene, not after.

Target length per `codex/Writing Style.md` (default to something reasonable
for your genre if it isn't filled in yet — ask the user rather than guessing).

Any number that lands on the page — a percentage, a count, a rank tag — is
canon the moment you write it. Round 1 review and Phase 5's Summary rewrite
both need to quote that exact value, not re-derive it, so keep track of the
load-bearing ones as you draft (see Phase 5's numeric cross-check).

Also track, per scene, the POV goal, resistance/escalation, visible progress
signpost, exit-state change, and finite resources spent or regained. This is a
scratch ledger only. It prevents a planned beat from occurring on paper without
creating a change the reader can feel.

---

## Phase 2 — Review round 1

Run all four reviewers — `proofread`, `pacing-review`, `prose-review`,
`continuity-reviewer` — against the working copy and the bundle. See
`references/review-protocol.md` for the exact prompt template, the
suggested effort level per reviewer, and how to run them in parallel if your
environment supports it (or sequentially if it doesn't — order doesn't
matter, they're independent).

Every reviewer must be told: **report only, never edit**, and every finding needs
an exact quoted string from the chapter plus a drafted replacement, marked
IMPORTANT or MINOR. A finding without a quotable anchor can't become a diff.

Do not add `sanderson-review` as a fifth chapter-cycle reviewer. The structural
work is divided between the existing reviewers: `pacing-review` owns whether
promise/progress/payoff is reader-visible and proportioned; `continuity-reviewer`
owns whether every payoff obeys established capabilities, limitations, and
current resource state. The prompt additions live in
`references/review-protocol.md`.

`continuity-reviewer`'s Cross-Artifact Fact Consistency check needs the
chapter's own `Summary.md` in front of it to do its job — the bundle already
includes it (Phase 0's "Planned summary" section), so nothing extra to add
here, just don't strip it out when adapting the prompt template.

---

## Phase 3 — Apply as diffs

Collect all four reports. Write a single patch file — one pass, all reviewers
together, so conflicting suggestions get resolved once:

```
--- PATCH: short label ---
<<<<<<< OLD
exact text currently in the chapter
=======
replacement text
>>>>>>> NEW
```

Then:

```bash
python3 scripts/apply_patches.py --file /tmp/chapter-cycle/chapter.md --patch /tmp/chapter-cycle/round1.patch
```

The script fails loudly if an OLD string is missing or appears more than once —
that is the guardrail. Never fall back to rewriting the file because a patch
didn't match; fix the patch.

**The one legitimate exception:** a finding that requires rebuilding a whole
scene's sentence architecture (e.g. "this POV's rhythm is wrong throughout") is
not a diff. Rewrite **that scene only**, into the working copy, and note it in
the changelog. Never rewrite the whole chapter for a scene-scoped problem.

Reviewers will disagree. Resolve it yourself, apply one version, and record the
disagreement in the review report for the user to settle later.

If a patch changes a quantitative or categorical fact (a number, a rank, a
placement), note it on a scratch list as you go — Phase 5 needs to re-verify
every one of these against the final `Summary.md`, and it's cheaper to track
them as they happen than to re-diff the whole chapter against the Summary at
the end.

---

## Phase 4 — Regression check, then stop

Round 1 fixes reliably reintroduce round 1's own problems in the new material.
So round 2 is **not** a second full review — it is one cheap, targeted check.
See `references/review-protocol.md` for exactly how to run it (resume the two
structural reviewers if your environment supports resuming a session's
context; otherwise re-run them fresh with the narrower regression-check
prompt).

Ask one question: *did any of these reintroduce a problem, and is anything
IMPORTANT still open?* Apply anything they return as diffs, and add any new
fact-changing patch to the same scratch list from Phase 3.

Also check that the fixes did not erase the chapter's visible progress signpost,
remove the cost that made a payoff earned, or introduce a new capability at the
point of solution.

**Then stop.** Do not run a third round. If a reviewer still reports something
IMPORTANT after round 2, apply it and tell the user rather than opening
another cycle.

---

## Phase 5 — Finish

1. **Proofread pass on the final text only.** The last round of diffs is where
   dangling modifiers and broken parallelism get introduced. One cheap/fast
   pass, working copy only, no bundle.
2. Write the working copy to the vault chapter path. Update the chapter
   frontmatter's `characters:`, `locations:`, and `beats:` to what actually
   appears and actually landed — the outline was a prediction, the prose is
   the fact.
3. Rewrite `Summary.md` as a record of what was written (drop `status: planned`),
   matching `codex/templates/Summary Template.md`— scene by
   scene, plus `**Sets up:**` and any `**Open thread**`. Every quantitative or
   categorical claim in it (a percentage, a count, a rank, a placement) must be
   copied from the final prose, not reconstructed from the outline or from an
   earlier draft round.
4. **Numeric/fact cross-check.** Using the scratch list from Phases 3–4, go
   through each fact that changed during review and confirm the *same* value
   now appears in: the final prose, the just-rewritten `Summary.md`, and any
   codex page (step 6) that also states it. This is the step that was
   previously missing and caused real drift on Chapter 7 — a fix applied to
   the prose but never propagated to the Summary or codex, which then agreed
   with each other and looked confirmed. Do this before writing the changelog,
   not after — the changelog entry in step 5 should already reflect the
   synced state.
5. Write `drafts/Changelog.md` — what each round found and what you did,
   including which non-manuscript files (Summary, codex pages) the numeric
   cross-check touched.
6. Write `reviews/<Chapter> - review-rounds-<date>.md` — what reviewers praised,
   what they disagreed about, any codex expansion the draft forced.
7. Update the codex: `codex/00 Index.md` (status + open threads),
   `novel/arc <N>/00 Arc <N> Index.md`, `codex/outline/Arc <N> — <Title>.md`'s
   "Chapter N Advances" table (what actually landed, not just what was
   planned), the status line in every `codex/outline/Thread <X>` file this
   chapter touched, `codex/outline/00 Outline Index.md`'s drafted/outline-only
   range, `codex/plot/Macro Progression.md`, and
   `codex/plot/Mystery Discovery Tracker.md` only for discoveries that
   actually landed on the page. Run `add-to-codex` for anything genuinely
   new.

Report to the user: word count, scene breakdown, any outline deviation and why,
reviewer disagreements you resolved, any codex conflict the draft forced, and
which files the numeric cross-check (step 4) corrected, if any.

---

## Budget

Watch your own token/cost usage against whatever budget you're working within.
If a run is running far more expensive than expected, something in Phase 0 or 2
is usually the cause — almost always a reviewer exploring the vault instead of
reading the bundle. Check its transcript before adding more rounds.

---

## Periodic whole-vault audit (outside this skill's scope)

This skill is deliberately scoped to one chapter per run, for the cost reasons
above. Beat-order contradictions between a Thread's full beat list and
already-outlined future chapters, `00 Index.md`/outline status drift, and
backlink orphans are real but only show up when comparing files across the
whole vault — no single chapter-cycle run will surface them. Run a dedicated
whole-vault continuity-and-backlink pass periodically (every arc boundary, or
every 3–4 chapters) rather than folding that reasoning into every chapter-cycle
run. `scripts/audit_links.py --orphans` covers the mechanical half (link
resolution and orphan detection); beat-order and status-metadata consistency
still need a reasoning pass over the outline files, similar in shape to
`continuity-reviewer` but scoped to the whole `codex/outline/` tree instead of
one chapter's bundle.
