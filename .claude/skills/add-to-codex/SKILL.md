---
name: add-to-codex
description: Add or update a lore entry (character, location, species/faction, mechanic, or plot thread) in the {{NOVEL_TITLE}} novel's Obsidian codex, at the correct path, with the correct frontmatter, cross-links, and index updates. Use when the user asks to add something to the {{NOVEL_TITLE}} codex, capture new worldbuilding/lore, or when drafting an {{NOVEL_TITLE}} chapter introduces a character, location, creature, or mechanic that doesn't have a codex entry yet.
---

# Add to the {{NOVEL_TITLE}} Codex

This skill exists so the codex stays usable as an AI-facing knowledge base, not a
human scrapbook. The whole point is that a future session (you, with no memory of
this one) can find any fact in one or two reads instead of grepping the entire
vault. Every step below serves that goal — don't skip the index update or the
frontmatter even if the note content itself is small.

The vault is a local folder (this skill's working directory, or the folder the
user points you at) — read and write its files directly. If you can't reach it,
tell the user you need the vault path, or ask them to paste the relevant
existing note so you can hand back updated content for them to save.

## 0. Orient yourself first

Read `codex/00 Index.md` before doing anything else. It has the current
manuscript status, the folder map, and the conventions below in condensed form.
If it's out of sync with what you're about to add, you'll fix that in step 5.

For a new or substantially expanded mechanic, species/faction, location system,
or plot element, also read the relevant sections of
`codex/outline/Sanderson Method — {{NOVEL_TITLE}} Working Guide.md`. Skip that extra read
for a small factual correction or supporting-cast update.

Before creating a new entity, run the expand-before-add check:

1. Can an established mechanic, culture, faction, location, or relationship do
   this through a deeper implication?
2. Does the addition affect plot, character, or setting rather than only making
   the codex denser?
3. What limitation, weakness, cost, social consequence, or uncertainty keeps
   it from becoming a convenient answer?
4. Is the detail needed for the current manuscript, or should it remain marked
   future intent?

The user's explicit worldbuilding decision wins. This check prevents accidental
proliferation; it does not veto a deliberate new idea.

If the entity clears this check but leaves several related things genuinely
undecided — a new character's core want, fear, and one key relationship; a new
mechanic's behavior, limitation, and cost — don't invent them solo and don't
interrogate the user one question at a time. Run the `grilling` skill on the
batch, then write the entry from what actually got settled.

## 1. Decide the type and the folder

| type value | folder | frontmatter fields beyond `type` and `tags` |
|---|---|---|
| `character` | `codex/characters/<Name>/` — **its own folder**, one per character | `role`, `species`, `squad`, `status`, `aliases` |
| `location` | `codex/locations/` | `world-kind`, `persistent`, `first-appearance` |
| `species-faction` | `codex/species-factions/` | `status` (revealed / partially revealed / mostly unrevealed) |
| `mechanic` | `codex/systems-mechanics/` | `owner` (omit if not character-specific) |
| `plot` | `codex/plot/` | whatever the specific tracker needs (see existing files for the pattern) |

**Characters are the one type that gets a folder, not a flat file.** A new
character entry is `codex/characters/<Name>/<Name>.md` — create the `<Name>/`
folder alongside the existing character folders (`Alex/`, `Sam/`,
`Jordan/`, `Riley/`, `Eve Voss/`, `Voreline/`, `Supporting Cast/`). If this
character is or may become a POV character, also add `codex/characters/<Name>/
<Name> - Voice.md` in the same folder (see `codex/templates/Character
Template.md`'s **Voice** section and `codex/characters/Alex/Alex
Mercer - Voice.md` for the format). `[[Wikilink]]`s resolve by filename
regardless of folder, so moving or nesting a character file never breaks
existing links — but always keep the file inside its own folder rather than
loose in `codex/characters/`.

Squad-member-specific species/cultures (e.g. Jordan's people) live inside that
character's own note, not as a separate species-faction file — only split out a
species/faction note if it's broader than one character or recurs independently.

Minor one-off named characters who don't need a full note go into
`codex/characters/Supporting Cast/Supporting Cast.md` as a subsection, not a new
file. Promote them to their own folder the moment they become plot-relevant.

## 2. Check it doesn't already exist

Read the relevant `00 ... Index.md` for that folder (and `characters/00
Characters Index.md` if there's any chance it's a person). Check aliases, not
just the title — e.g. "Sam" vs "Valexia". If it exists, you're updating that
file, not creating a new one.

## 3. Use the matching template

Copy the shape from `codex/templates/` (`Character Template.md`, `Location
Template.md`, `Species-Faction Template.md`, or `Mechanic Template.md`). Keep
the frontmatter fields exactly as named there — that consistency is what makes
the whole codex greppable by `type:` later. For a character, `Character
Template.md` also documents the per-character folder layout and the optional
`Voice.md` companion file — follow it rather than improvising a flat file.

## 4. Write the content with these rules

- **One note per entity.** Don't fold two characters or two mechanics into one
  file because they're related — link them instead.
- **Separate established fact from future intent.** Anything drawn from
  `codex/00 Braindump.md` that hasn't actually happened in a written chapter yet
  must be visibly flagged — a `status:` or `manuscript-status:` frontmatter
  field, or plain text like "not yet reached in the manuscript" / "future
  material — not yet written." Look at `codex/systems-mechanics/Sam's Arm.md`
  for the pattern. This is the single most important rule: a future session
  must never mistake Braindump intent for something that already happened on
  the page.
- **Cite chapters for anything confirmed.** `[[Chapter 4 - Riley]]` style
  links, not vague "established earlier."
- **`[[Wikilink]]` every entity mention** on first use in the note — this
  builds Obsidian's backlink graph for the human user, even though a future
  AI session should rely on the indexes and `type:` frontmatter for its own
  lookup, not backlinks.
- **If the Braindump and the manuscript disagree, the manuscript wins.** Note
  the discrepancy in the entry rather than silently picking one (see how
  `codex/plot/Macro Progression.md` flags this for Phase One).
- **Mechanic entries must expose their story constraints.** For a new or
  substantially changed mechanic, include clearly findable sections or bullets
  for: reader-understood behavior, limitations, costs, current on-page state,
  and planned expansions marked future. State how the element connects to at
  least two of plot, character, and setting when that connection exists. If
  several of these (behavior, limitation, cost) are still open, that's exactly
  the batch to run through `grilling` before writing the entry — a mechanic
  with an invented-solo cost is the kind of "convenient answer" step 0's
  expand-before-add check exists to catch.
- **Codex depth is not permission for an exposition dump.** Preserve complete
  planning knowledge here while distinguishing which details are revealed,
  inferable, and still below the manuscript's iceberg.

## 5. Update the index — do not skip this

Add a one-line, fact-bearing entry (not just a bare link) to the relevant `00
... Index.md`. A future session should be able to read only the index and know
this entity exists and roughly what it is, without opening the file.

If what you added changes the current story state — a new discovery revealed, a
new open thread, a character now on-page who wasn't before — also update
`codex/00 Index.md`'s "Manuscript status" section and, if relevant,
`codex/plot/Mystery Discovery Tracker.md`'s `revealed:` flags.

## 6. Don't invent what's flagged as deliberately unknown

Some notes — a rival faction's page, a deliberately mysterious tech/magic
system, a species page seen only through one character's limited knowledge —
are intentionally incomplete, either because the mystery hasn't been revealed
yet, or because a character's own ignorance is the point (a character
genuinely doesn't know the full truth about something outside their culture).
Don't fill these gaps in in service of a "complete" codex. Expand them only when
the manuscript itself reveals the missing piece.
