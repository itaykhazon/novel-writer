from __future__ import annotations

import argparse
import html
import json
import re
from pathlib import Path

# The title used on the cover page, the running header, and the default output
# filename when --title isn't passed. Read from codex/project.json at run time
# rather than hardcoded, so this script needs no per-project editing; build()
# sets it once from --root before anything renders.
NOVEL_TITLE = "Untitled Novel"


def load_project_title(root: Path) -> str:
    """Return the novel's title from <root>/codex/project.json.

    Missing, unreadable or malformed file is not fatal — an export with a
    placeholder title is more useful than no export, and --title overrides
    this anyway. Warn once so it's visible rather than silently wrong.
    """
    config = Path(root) / "codex" / "project.json"
    try:
        with open(config, encoding="utf-8") as handle:
            title = json.load(handle).get("title", "").strip()
    except FileNotFoundError:
        print(f"warning: {config} not found; using placeholder title")
        return NOVEL_TITLE
    except (json.JSONDecodeError, OSError) as exc:
        print(f"warning: could not read {config} ({exc}); using placeholder title")
        return NOVEL_TITLE
    if not title:
        print(f"warning: {config} has no \"title\"; using placeholder title")
        return NOVEL_TITLE
    return title


def load_dependencies():
    try:
        from reportlab.lib import colors
        from reportlab.lib.enums import TA_CENTER, TA_LEFT
        from reportlab.lib.pagesizes import A5
        from reportlab.lib.styles import ParagraphStyle, getSampleStyleSheet
        from reportlab.lib.units import mm
        from reportlab.pdfbase import pdfmetrics
        from reportlab.pdfbase.ttfonts import TTFont
        from reportlab.platypus import BaseDocTemplate, Frame, KeepTogether, PageBreak, PageTemplate, Paragraph, Spacer
        from pypdf import PdfReader, PdfWriter
    except ImportError as exc:
        raise SystemExit("Missing PDF dependencies. Install reportlab and pypdf, then rerun.") from exc
    return locals()


def register_font(pdfmetrics, TTFont):
    # Priority order follows genre-fiction typesetting convention (an old-style
    # book serif over a screen-optimized one) while staying resilient across
    # the platforms this skill actually runs on: a native Windows shell has
    # Microsoft's Garamond/Palatino Linotype/Georgia under C:\Windows\Fonts;
    # a Linux shell (including the Cowork device bridge's sandbox) instead has
    # Liberation Serif / DejaVu Serif under /usr/share/fonts. Helvetica is the
    # last-resort fallback if none of these are present.
    candidates = [
        ("Garamond", Path(r"C:\Windows\Fonts"), "GARA.TTF", "GARABD.TTF", "GARAIT.TTF", "GARABI.TTF"),
        ("Palatino", Path(r"C:\Windows\Fonts"), "pala.ttf", "palab.ttf", "palai.ttf", "palabi.ttf"),
        ("Georgia", Path(r"C:\Windows\Fonts"), "georgia.ttf", "georgiab.ttf", "georgiai.ttf", "georgiaz.ttf"),
        ("Georgia", Path("/usr/share/fonts/truetype/msttcorefonts"), "Georgia.ttf", "Georgia_Bold.ttf", "Georgia_Italic.ttf", "Georgia_Bold_Italic.ttf"),
        ("Liberation Serif", Path("/usr/share/fonts/truetype/liberation2"), "LiberationSerif-Regular.ttf", "LiberationSerif-Bold.ttf", "LiberationSerif-Italic.ttf", "LiberationSerif-BoldItalic.ttf"),
        ("Liberation Serif", Path("/usr/share/fonts/truetype/liberation"), "LiberationSerif-Regular.ttf", "LiberationSerif-Bold.ttf", "LiberationSerif-Italic.ttf", "LiberationSerif-BoldItalic.ttf"),
        ("DejaVu Serif", Path("/usr/share/fonts/truetype/dejavu"), "DejaVuSerif.ttf", "DejaVuSerif-Bold.ttf", "DejaVuSerif-Italic.ttf", "DejaVuSerif-BoldItalic.ttf"),
    ]
    for family, folder, regular, bold, italic, bold_italic in candidates:
        paths = [folder / name for name in (regular, bold, italic, bold_italic)]
        if all(path.exists() for path in paths):
            pdfmetrics.registerFont(TTFont(family, str(paths[0])))
            pdfmetrics.registerFont(TTFont(f"{family}-Bold", str(paths[1])))
            pdfmetrics.registerFont(TTFont(f"{family}-Italic", str(paths[2])))
            pdfmetrics.registerFont(TTFont(f"{family}-BoldItalic", str(paths[3])))
            pdfmetrics.registerFontFamily(family, normal=family, bold=f"{family}-Bold", italic=f"{family}-Italic", boldItalic=f"{family}-BoldItalic")
            return family
    return "Helvetica"


def inline_markup(text):
    escaped = html.escape(text, quote=False)
    escaped = re.sub(r"\*\*(.+?)\*\*", r"<b>\1</b>", escaped)
    escaped = re.sub(r"(?<!\*)\*(?!\*)(.+?)(?<!\*)\*(?!\*)", r"<i>\1</i>", escaped)
    escaped = re.sub(r"(?<![\w])_(.+?)_(?![\w])", r"<i>\1</i>", escaped)
    return escaped


def prose_blocks(path):
    raw = path.read_text(encoding="utf-8").replace("\r\n", "\n")
    if raw.startswith("---\n"):
        _, _, raw = raw.partition("\n---\n")
    blocks, current = [], []
    for line in raw.splitlines():
        if not line.strip():
            if current:
                blocks.append(current)
                current = []
        else:
            current.append(line)
    if current:
        blocks.append(current)
    return blocks


def chapter_files(root, arc, start, end):
    found = []
    for folder in (root / f"novel/arc {arc}").glob("Chapter *"):
        match = re.match(r"Chapter (\d+) - (.+)$", folder.name)
        if not match:
            continue
        number = int(match.group(1))
        if number < start or number > end:
            continue
        candidates = [p for p in folder.glob("*.md") if p.name not in {"Summary.md", "Outline.md"} and "drafts" not in p.parts]
        if not candidates:
            continue
        path = next((p for p in candidates if p.stem == folder.name), candidates[0])
        if "status: outlined" in path.read_text(encoding="utf-8")[:2000]:
            continue
        display_title = "Prologue" if number == 0 else f"Chapter {number} - {match.group(2)}"
        found.append((number, display_title, path))
    return sorted(found)


def block_markup(lines):
    stripped = [line.strip() for line in lines]
    if len(lines) == 1 and stripped[0] == "—":
        return None, "scene"
    if all(re.match(r'^\*\*["“]', line) for line in stripped):
        return " ".join(inline_markup(line) for line in lines), "prose"
    if all(line.startswith("**") and line.endswith("**") for line in stripped):
        return "<br/>".join(inline_markup(line) for line in stripped), "system"
    if all(line.startswith("_") and line.endswith("_") for line in stripped):
        return "<br/>".join("<i>" + inline_markup(line[1:-1]) + "</i>" for line in stripped), "location"
    if any(line.endswith("  ") for line in lines):
        return "<br/>".join(inline_markup(line.rstrip()) for line in lines), "prose"
    return " ".join(inline_markup(line.strip()) for line in lines), "prose"


def build(args):
    global NOVEL_TITLE
    NOVEL_TITLE = load_project_title(args.root)
    deps = load_dependencies()
    colors = deps["colors"]
    TA_CENTER, TA_LEFT = deps["TA_CENTER"], deps["TA_LEFT"]
    A5, mm = deps["A5"], deps["mm"]
    ParagraphStyle, getSampleStyleSheet = deps["ParagraphStyle"], deps["getSampleStyleSheet"]
    BaseDocTemplate, Frame, KeepTogether = deps["BaseDocTemplate"], deps["Frame"], deps["KeepTogether"]
    PageBreak, PageTemplate, Paragraph, Spacer = deps["PageBreak"], deps["PageTemplate"], deps["Paragraph"], deps["Spacer"]
    PdfReader, PdfWriter = deps["PdfReader"], deps["PdfWriter"]
    font = register_font(deps["pdfmetrics"], deps["TTFont"])
    print(f"font {font}")
    chapters = chapter_files(args.root, args.arc, args.from_chapter, args.to_chapter)
    if not chapters:
        raise SystemExit("No drafted chapter files found in the requested range.")
    title = args.title or f"{NOVEL_TITLE} - Arc {args.arc}"
    arc_label = "ONE" if args.arc == 1 else str(args.arc)
    output = Path(args.output) if args.output else args.root / "output" / "pdf" / f"{title}.pdf"
    output.parent.mkdir(parents=True, exist_ok=True)
    temp_output = output.with_suffix(".building.pdf")

    # Body type follows genre-fiction print convention: an 11-12pt old-style
    # serif (the font candidates above target Garamond/Palatino/a Times-class
    # serif) at ~120-145% leading, laid out for ~55-65 characters per line.
    styles = getSampleStyleSheet()
    styles.add(ParagraphStyle(name="Novel", parent=styles["BodyText"], fontName=font, fontSize=11.5, leading=15.3, textColor=colors.HexColor("#20252B"), alignment=TA_LEFT, spaceAfter=7.6, firstLineIndent=0, allowWidows=0, allowOrphans=0))
    styles.add(ParagraphStyle(name="Location", parent=styles["Novel"], fontName=font, fontSize=9.8, leading=13, textColor=colors.HexColor("#536675"), alignment=TA_CENTER, firstLineIndent=0, spaceAfter=2))
    styles.add(ParagraphStyle(name="System", parent=styles["Novel"], fontName=font, fontSize=10.3, leading=13.9, textColor=colors.HexColor("#1B3040"), leftIndent=8 * mm, rightIndent=6 * mm, firstLineIndent=0, spaceBefore=4, spaceAfter=9, backColor=colors.HexColor("#EBF2F6"), borderColor=colors.HexColor("#8FB4CA"), borderWidth=0.8, borderPadding=6, borderRadius=3))
    styles.add(ParagraphStyle(name="Kicker", parent=styles["Normal"], fontName=font, fontSize=9, leading=11.5, textColor=colors.HexColor("#8A5A35"), alignment=TA_CENTER, spaceAfter=7))
    styles.add(ParagraphStyle(name="ChapterTitle", parent=styles["Title"], fontName=font, fontSize=23, leading=29, textColor=colors.HexColor("#20252B"), alignment=TA_CENTER, spaceAfter=19))
    styles.add(ParagraphStyle(name="TitleMain", parent=styles["Title"], fontName=font, fontSize=32, leading=37, textColor=colors.HexColor("#20252B"), alignment=TA_CENTER, spaceAfter=10))
    styles.add(ParagraphStyle(name="TitleSub", parent=styles["Normal"], fontName=font, fontSize=11.5, leading=16.5, textColor=colors.HexColor("#66717D"), alignment=TA_CENTER))
    styles.add(ParagraphStyle(name="Included", parent=styles["Normal"], fontName=font, fontSize=10, leading=14.5, textColor=colors.HexColor("#536675"), alignment=TA_CENTER))

    # Margins: a touch tighter left/right than before to keep line length in
    # the ~55-65 character sweet spot at the larger body size, and a
    # classical top-smaller/bottom-larger split (instead of the previous
    # top-heaviest layout) so the page doesn't feel top-weighted.
    doc = BaseDocTemplate(str(temp_output), pagesize=A5, leftMargin=17 * mm, rightMargin=17 * mm, topMargin=15 * mm, bottomMargin=21 * mm, title=title, author=args.author, subject=f"Chapters {args.from_chapter} through {args.to_chapter}")
    frame = Frame(doc.leftMargin, doc.bottomMargin, doc.width, doc.height, id="novel")

    def draw_page(canvas, document):
        page = canvas.getPageNumber()
        width, height = A5
        canvas.saveState()
        if page > 1:
            canvas.setStrokeColor(colors.HexColor("#D6DCE2"))
            canvas.setLineWidth(0.4)
            canvas.line(document.leftMargin, height - 9 * mm, width - document.rightMargin, height - 9 * mm)
            canvas.setFont(font, 7.5)
            canvas.setFillColor(colors.HexColor("#66717D"))
            canvas.drawString(document.leftMargin, height - 6 * mm, f"{NOVEL_TITLE.upper()}  ·  ARC {arc_label}")
        canvas.setFont(font, 8)
        canvas.setFillColor(colors.HexColor("#66717D"))
        canvas.drawCentredString(width / 2, 10 * mm, str(page))
        canvas.restoreState()

    doc.addPageTemplates([PageTemplate(id="all", frames=[frame], onPage=draw_page)])
    included = " · ".join("Prologue" if number == 0 else chapter_title.split(" - ", 1)[1] for number, chapter_title, _ in chapters)
    range_label = f"Prologue through Chapter {args.to_chapter}" if args.from_chapter == 0 else f"Chapters {args.from_chapter} through {args.to_chapter}"
    story = [Spacer(1, 48 * mm), Paragraph(html.escape(NOVEL_TITLE.upper()), styles["TitleMain"]), Paragraph(f"ARC {arc_label}", styles["Kicker"]), Spacer(1, 7 * mm), Paragraph(range_label, styles["TitleSub"]), Spacer(1, 5 * mm), Paragraph(html.escape(args.author), styles["TitleSub"]), Spacer(1, 25 * mm), Paragraph("Included chapters", styles["Kicker"]), Paragraph(included, styles["Included"]), PageBreak()]
    for index, (_, chapter_title, path) in enumerate(chapters):
        if index:
            story.append(PageBreak())
        story.extend([Spacer(1, 35 * mm), Paragraph(f"ARC {args.arc}", styles["Kicker"]), Paragraph(inline_markup(chapter_title), styles["ChapterTitle"]), Spacer(1, 7 * mm)])
        content = []
        for lines in prose_blocks(path):
            markup, kind = block_markup(lines)
            if kind == "scene":
                scene_style = ParagraphStyle(name=f"Scene{index}", parent=styles["Novel"], alignment=TA_CENTER, firstLineIndent=0, fontSize=11, leading=14, textColor=colors.HexColor("#8A5A35"), spaceBefore=3, spaceAfter=9)
                content.extend([Spacer(1, 8), Paragraph("—", scene_style)])
            elif kind == "location":
                content.append(Paragraph(markup, styles["Location"]))
            elif kind == "system":
                content.append(Paragraph(markup, styles["System"]))
            else:
                content.append(Paragraph(markup, styles["Novel"]))
        story.append(KeepTogether(content[:2]))
        story.extend(content[2:])
    doc.build(story)

    reader = PdfReader(str(temp_output))
    writer = PdfWriter()
    writer.clone_document_from_reader(reader)
    writer.add_metadata({"/Title": title, "/Author": args.author, "/Subject": f"Chapters {args.from_chapter} through {args.to_chapter}"})
    writer.add_outline_item(title, 0)
    for number, chapter_title, _ in chapters:
        marker = "Prologue" if number == 0 else f"Chapter {number} -"
        page_index = 1 if number == 0 else next(page_index for page_index, page in enumerate(reader.pages) if marker in (page.extract_text() or ""))
        writer.add_outline_item(chapter_title, page_index)
    with output.open("wb") as handle:
        writer.write(handle)
    temp_output.unlink(missing_ok=True)
    print(f"created {output}")
    print(f"pages {len(reader.pages)}")


def parse_args():
    parser = argparse.ArgumentParser(description="Export a drafted chapter range as a phone-friendly PDF.")
    parser.add_argument("--root", type=Path, default=Path.cwd())
    parser.add_argument("--arc", type=int, required=True)
    parser.add_argument("--from-chapter", type=int, required=True)
    parser.add_argument("--to-chapter", type=int, required=True)
    parser.add_argument("--output", type=Path)
    parser.add_argument("--title")
    parser.add_argument("--author", default="Your Name", help="Credited author; override with --author when exporting for real.")
    return parser.parse_args()


if __name__ == "__main__":
    build(parse_args())
