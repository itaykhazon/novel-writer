---
name: export-novel-pdf
description: Export selected {{NOVEL_TITLE}} manuscript chapters to a polished, phone-friendly PDF with embedded fonts, flush-left prose, preserved italics and bold system readouts, chapter bookmarks, page numbers, and rendered visual verification. Use when the user asks to export, compile, assemble, or send a novel arc or chapter range as a PDF.
---

# Export Novel PDF

Use the bundled `scripts/export_novel_pdf.py` generator for repeatable exports. The skill is project-aware: it reads prose from `novel/arc <N>/Chapter */` and writes final PDFs to `output/pdf/` unless the user gives another output path.

## Workflow

1. Read `codex/00 Index.md` to confirm manuscript order and which chapters are drafted. Read `codex/Editing Workflow.md` before touching manuscript files; exporting does not authorize prose edits.
2. Resolve the requested range explicitly. The Prologue is chapter 0. Do not include outlined or future chapters merely because their folders exist.
3. Before the first PDF create/edit operation, run the PDF skill's required artifact-operation marker with `create` or `edit`, one expected PDF output, and `pdf` as the format.
4. Check that Python has `reportlab` and `pypdf`. If missing, install them only into a temporary PDF workspace or use the PDF skill's documented dependency path.
5. Run the generator from the vault root:

   ```powershell
   python .agents/skills/export-novel-pdf/scripts/export_novel_pdf.py --arc 1 --from-chapter 0 --to-chapter 7
   ```

   Use `--output` for a different filename or folder.
6. Render representative pages with Poppler (`pdftoppm`): title page, first prose page, a page containing system readouts, a chapter transition, and the final page. Inspect the PNGs visually. Fix the generator and rebuild if needed.
7. Verify the final PDF with `pdfinfo` and `pypdf`: page count, A5 portrait page size, metadata, chapter bookmarks, no frontmatter leakage, and expected opening/ending prose. Do not deliver until the latest render is clean.
8. Remove temporary builders, package installs, rendered PNGs, and intermediate PDFs. Keep only the final artifact under `output/pdf/`.

## House layout

- Use A5 portrait for comfortable phone reading, with an asymmetric margin split (17mm left/right, 15mm top, 21mm bottom) rather than even margins — the smaller top / larger bottom follows classical book-page proportion instead of centering the text block.
- Embed a genre-appropriate old-style book serif, matching standard print-fiction typesetting rather than a screen font: try Garamond, then Palatino Linotype, then Georgia under `C:\Windows\Fonts` (native Windows runs), then Liberation Serif, then DejaVu Serif under `/usr/share/fonts` (Linux runs, including the Cowork device-bridge sandbox — this is the pair that actually resolves there instead of silently falling back). Helvetica is the last-resort fallback only if none of those are found; the generator prints which font it embedded.
- Body prose is 11.5pt with 15.3pt leading (~133%, inside the 120–145% range genre fiction uses) — sized for roughly 55–65 characters per line at these margins, up from the previous 10.7pt/15.1pt.
- Keep prose paragraphs flush-left (`firstLineIndent=0`) and separate them with vertical space.
- Preserve Markdown `_italics_`, `*italics*`, and `**bold**`.
- Treat standalone bold dialogue blocks beginning with `**"` or `**“` as prose dialogue, not UI readouts.
- Render two-line location/date openers in centered italic text.
- Render bare `—` scene breaks as centered ochre em dashes with spacing.
- If your novel uses system/UI text (a LitRPG-style stat panel, HUD readout, or similar in-fiction interface block) rendered as an all-bold standalone block, style it as a UI panel rather than a subtle box: a light tinted background, a rounded border, and indented padding, so it reads as an interface element interrupting the prose rather than as narration. Skip this rule entirely if your novel has no such convention.
- Include a restrained title page, a running header built from the book/arc title, page numbers, PDF metadata, and chapter outline bookmarks.
- Credit the author configured for this project (see the project's README/config) on the cover and in PDF metadata by default; accept `--author` when another author is explicitly requested.
- Strip YAML frontmatter. Never include `Summary.md`, `Outline.md`, `Changelog.md`, or files in `drafts/` as manuscript prose.

## Output handoff

Report the exact final PDF path and cite that PDF once with a plain output file citation. If the user needs phone access, explain that a local workspace link may not be reachable from a phone; use a connected Google Drive or other approved cloud app when available rather than uploading manuscript text to an unapproved third-party service.
