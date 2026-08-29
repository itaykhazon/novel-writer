# Novel manuscript

This folder holds the actual manuscript, organized as `novel/arc <N>/`, one folder per arc.

Inside each arc folder: an `00 Arc <N> Index.md` (see `codex/templates/Arc Index Template.md`), and one subfolder per chapter — `Chapter <n> - <Title>/` — containing:

- `Chapter <n> - <Title>.md` — the chapter itself
- `Outline.md` — the beat-by-beat plan `add-chapter` writes before any prose exists
- `Summary.md` — a factual summary of what's on the page (see `codex/templates/Summary Template.md`)
- `drafts/` — prior versions and `Changelog.md`

Nothing needs to exist here yet — `add-chapter` creates this structure the first time you plan a chapter. This file exists only so the folder is present in a fresh checkout; delete it once your first arc folder exists.
