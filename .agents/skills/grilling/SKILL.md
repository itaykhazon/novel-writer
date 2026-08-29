---
name: grilling
description: A round-based interview technique for settling several related open questions at once — a new character's motivations and relationships, a new mechanic's rules and costs, a chapter's undecided beats — instead of guessing, free-writing options, or asking one question at a time. Use when add-chapter or add-to-codex hit real open decisions the user hasn't already answered, when several related unknowns need resolving together before writing anything, or when the user asks to be "grilled" on a plan, character, or idea.
---

# Grilling

Adapted from Matt Pocock's `/grilling` primitive (github.com/mattpocock/skills) for
{{NOVEL_TITLE}}'s planning skills. The problem it solves: a normal back-and-forth interview
asks one question, waits, asks the next — slow, and it re-asks things the
answers already implied. Grilling asks a whole batch at once, then only asks
what the last batch actually unlocked.

## When to use this, and when not to

Use it inside `add-chapter` (Step 2, thin or missing direction; Step 5,
real "Open questions") and `add-to-codex` (Step 4, a new character,
mechanic, or system with unresolved fields) whenever more than one or two
related things are genuinely undecided.

Don't use it when the user already gave clear direction — write from what
they said. Don't use it for a single isolated fact ("what's this ship called?"
is one question, just ask it). Don't use it for review skills — those diagnose
existing text; there's nothing to interview.

## The method

**1. Map the open questions as a small dependency tree.** List everything
genuinely undecided for this character/mechanic/chapter. For each, note what
it depends on, if anything (a character's core fear may need their formative
event settled first; a chapter's climax beat may need the mechanic's cost
settled first).

**2. Ask the frontier, not the whole tree.** A question belongs in this round
only if everything it depends on is already known (from the codex, the outline,
or an earlier round's answer). Never ask a question whose prerequisite is
itself unanswered — that's round 2's question, not this one.

**3. Ask the round as one numbered list**, each item short enough to answer by
number:

```
1. **[Short title]** — [one to two sentences of context: what's already
   established, why this needs deciding now]. *Suggestion: [a concrete
   default, grounded in the codex/genre, not a generic placeholder.]*
```

The suggestion matters — it lets the user answer "go with 1, 3, and 5" for
anything they don't feel strongly about, and reserve their attention for the
ones they do. Never send a round with no suggestions; that's just a form.

**4. Fold the answers in, then expand the frontier.** Whatever those answers
unblock becomes the next round. A round that surfaces zero new questions means
you're done — stop, don't invent more to ask.

**5. Close with one line, not a fourth round.** State what's settled and what's
still deliberately open (carried into the outline's "Open questions" or the
codex entry's `status: future intent`, per the calling skill's own rules) —
don't let grilling itself decide to leave something open; that's the calling
skill's call.

## Shape guardrails

- Usually 2–3 rounds. If you're drafting a 4th, the topic is probably bigger
  than one grilling pass — say so and suggest splitting it (a new arc's whole
  architecture, for instance, isn't a grilling pass inside `add-chapter`).
- A round asks *only* the frontier — resist bundling in a question that's
  merely related but not actually unblocked yet.
- Keep suggestions specific to {{NOVEL_TITLE}} (genre, established mechanics, existing
  characters) — a generic suggestion is worse than no suggestion, because it
  invites a reflexive "sure, fine" that settles nothing real.
- Grilling produces answers, not prose. Feed the settled answers back into the
  calling skill's own writing step; don't let the interview itself start
  drafting outline beats or codex sentences.
