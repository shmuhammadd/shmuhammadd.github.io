#!/usr/bin/env python3
"""Generate a PDF from the Advanced NLP Part 1 Improved notebook."""

import json
import re
from reportlab.lib.pagesizes import letter
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.colors import HexColor, black, white, Color
from reportlab.lib.units import inch
from reportlab.lib.enums import TA_LEFT, TA_CENTER, TA_JUSTIFY
from reportlab.platypus import (
    SimpleDocTemplate, Paragraph, Spacer, PageBreak,
    Table, TableStyle, Preformatted, KeepTogether,
    HRFlowable, ListFlowable, ListItem
)
from reportlab.lib import colors

# ─── Load notebook ───────────────────────────────────────────────
NB_PATH = "/Users/smuhamma/Documents/Github/shmuhammadd.github.io/.claude/worktrees/objective-black/Advanced_NLP_Part1_Improved.ipynb"
OUT_PATH = "/Users/smuhamma/Downloads/Advanced_NLP_Part1_Improved.pdf"

with open(NB_PATH, "r") as f:
    nb = json.load(f)

# ─── Colour palette ─────────────────────────────────────────────
DARK_BLUE   = HexColor("#1a237e")
MED_BLUE    = HexColor("#1565c0")
LIGHT_BLUE  = HexColor("#e3f2fd")
LIGHT_GREEN = HexColor("#e8f5e9")
LIGHT_AMBER = HexColor("#fff8e1")
LIGHT_GREY  = HexColor("#f5f5f5")
CODE_BG     = HexColor("#f8f9fa")
DARK_GREY   = HexColor("#424242")
ACCENT_GREEN= HexColor("#2e7d32")
ACCENT_ORANGE= HexColor("#e65100")
BORDER_GREY = HexColor("#e0e0e0")

# ─── Custom styles ───────────────────────────────────────────────
styles = getSampleStyleSheet()

styles.add(ParagraphStyle(
    name='NB_Title',
    parent=styles['Title'],
    fontSize=26,
    textColor=DARK_BLUE,
    spaceAfter=6,
    alignment=TA_CENTER,
    fontName='Helvetica-Bold',
))

styles.add(ParagraphStyle(
    name='NB_Subtitle',
    parent=styles['Normal'],
    fontSize=13,
    textColor=MED_BLUE,
    spaceBefore=4,
    spaceAfter=20,
    alignment=TA_CENTER,
    fontName='Helvetica',
))

styles.add(ParagraphStyle(
    name='NB_H1',
    parent=styles['Heading1'],
    fontSize=20,
    textColor=DARK_BLUE,
    spaceBefore=24,
    spaceAfter=10,
    fontName='Helvetica-Bold',
    borderWidth=0,
    borderPadding=0,
))

styles.add(ParagraphStyle(
    name='NB_H2',
    parent=styles['Heading2'],
    fontSize=16,
    textColor=MED_BLUE,
    spaceBefore=18,
    spaceAfter=8,
    fontName='Helvetica-Bold',
))

styles.add(ParagraphStyle(
    name='NB_H3',
    parent=styles['Heading3'],
    fontSize=13,
    textColor=DARK_GREY,
    spaceBefore=14,
    spaceAfter=6,
    fontName='Helvetica-Bold',
))

styles.add(ParagraphStyle(
    name='NB_Body',
    parent=styles['Normal'],
    fontSize=10,
    leading=15,
    textColor=black,
    spaceAfter=6,
    fontName='Helvetica',
    alignment=TA_JUSTIFY,
))

styles.add(ParagraphStyle(
    name='NB_Code',
    parent=styles['Code'],
    fontSize=8.5,
    leading=12,
    fontName='Courier',
    textColor=HexColor("#333333"),
    backColor=CODE_BG,
    borderWidth=0.5,
    borderColor=BORDER_GREY,
    borderPadding=8,
    spaceBefore=6,
    spaceAfter=8,
    leftIndent=10,
    rightIndent=10,
))

styles.add(ParagraphStyle(
    name='NB_Blockquote',
    parent=styles['Normal'],
    fontSize=10,
    leading=14,
    textColor=DARK_GREY,
    leftIndent=20,
    borderWidth=0,
    borderPadding=(8, 8, 8, 12),
    spaceBefore=8,
    spaceAfter=8,
    fontName='Helvetica-Oblique',
    backColor=LIGHT_AMBER,
))

styles.add(ParagraphStyle(
    name='NB_Bullet',
    parent=styles['Normal'],
    fontSize=10,
    leading=14,
    textColor=black,
    leftIndent=25,
    bulletIndent=12,
    spaceBefore=2,
    spaceAfter=2,
    fontName='Helvetica',
))

styles.add(ParagraphStyle(
    name='NB_Practice',
    parent=styles['Normal'],
    fontSize=10,
    leading=14,
    textColor=ACCENT_GREEN,
    leftIndent=15,
    spaceBefore=6,
    spaceAfter=6,
    fontName='Helvetica-Bold',
    backColor=LIGHT_GREEN,
    borderPadding=8,
))

styles.add(ParagraphStyle(
    name='NB_TableCell',
    parent=styles['Normal'],
    fontSize=9,
    leading=12,
    fontName='Helvetica',
    textColor=black,
))

styles.add(ParagraphStyle(
    name='NB_TableHeader',
    parent=styles['Normal'],
    fontSize=9,
    leading=12,
    fontName='Helvetica-Bold',
    textColor=white,
))

# ─── Helpers ─────────────────────────────────────────────────────

def escape_xml(text):
    """Escape characters that are special in ReportLab's XML markup."""
    text = text.replace("&", "&amp;")
    text = text.replace("<", "&lt;")
    text = text.replace(">", "&gt;")
    return text


def md_inline(text):
    """Convert inline markdown to ReportLab XML."""
    # Bold + italic
    text = re.sub(r'\*\*\*(.*?)\*\*\*', r'<b><i>\1</i></b>', text)
    text = re.sub(r'___(.*?)___', r'<b><i>\1</i></b>', text)
    # Bold
    text = re.sub(r'\*\*(.*?)\*\*', r'<b>\1</b>', text)
    text = re.sub(r'__(.*?)__', r'<b>\1</b>', text)
    # Italic
    text = re.sub(r'\*(.*?)\*', r'<i>\1</i>', text)
    text = re.sub(r'(?<!\w)_(.*?)_(?!\w)', r'<i>\1</i>', text)
    # Inline code
    text = re.sub(r'`([^`]+)`', r'<font name="Courier" size="9" color="#c62828">\1</font>', text)
    # Links [text](url) - just show text
    text = re.sub(r'\[([^\]]+)\]\([^)]+\)', r'<u>\1</u>', text)
    return text


def parse_md_table(lines):
    """Parse a markdown table into a list of rows (each row is a list of cell strings)."""
    rows = []
    for line in lines:
        line = line.strip()
        if line.startswith("|") and not re.match(r'^\|[\s\-:|]+\|$', line):
            cells = [c.strip() for c in line.split("|")[1:-1]]
            rows.append(cells)
    return rows


def build_table(rows):
    """Build a ReportLab Table from parsed markdown table rows."""
    if not rows or len(rows) < 1:
        return None

    header = rows[0]
    body = rows[1:]

    # Build table data with Paragraphs
    table_data = []
    header_row = [Paragraph(md_inline(escape_xml(c)), styles['NB_TableHeader']) for c in header]
    table_data.append(header_row)

    for row in body:
        # Pad row if needed
        while len(row) < len(header):
            row.append("")
        data_row = [Paragraph(md_inline(escape_xml(c)), styles['NB_TableCell']) for c in row[:len(header)]]
        table_data.append(data_row)

    ncols = len(header)
    col_width = (6.5 * inch) / ncols
    col_widths = [col_width] * ncols

    t = Table(table_data, colWidths=col_widths, repeatRows=1)
    t.setStyle(TableStyle([
        ('BACKGROUND', (0, 0), (-1, 0), MED_BLUE),
        ('TEXTCOLOR', (0, 0), (-1, 0), white),
        ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
        ('FONTSIZE', (0, 0), (-1, 0), 9),
        ('BOTTOMPADDING', (0, 0), (-1, 0), 8),
        ('TOPPADDING', (0, 0), (-1, 0), 8),
        ('BACKGROUND', (0, 1), (-1, -1), white),
        ('ROWBACKGROUNDS', (0, 1), (-1, -1), [white, LIGHT_GREY]),
        ('GRID', (0, 0), (-1, -1), 0.5, BORDER_GREY),
        ('VALIGN', (0, 0), (-1, -1), 'TOP'),
        ('LEFTPADDING', (0, 0), (-1, -1), 8),
        ('RIGHTPADDING', (0, 0), (-1, -1), 8),
        ('TOPPADDING', (0, 1), (-1, -1), 5),
        ('BOTTOMPADDING', (0, 1), (-1, -1), 5),
    ]))
    return t


def process_markdown_cell(source, story):
    """Convert a markdown cell to ReportLab flowables and append to story."""
    lines = source.split('\n')
    i = 0

    while i < len(lines):
        line = lines[i]
        stripped = line.strip()

        # Skip empty lines
        if not stripped:
            story.append(Spacer(1, 4))
            i += 1
            continue

        # Skip image references
        if stripped.startswith('!['):
            i += 1
            continue

        # Skip <details> blocks (solutions)
        if '<details>' in stripped:
            while i < len(lines) and '</details>' not in lines[i]:
                i += 1
            i += 1  # skip </details>
            story.append(Paragraph(
                '<font color="#2e7d32"><i>[Solution hidden - try it yourself first!]</i></font>',
                styles['NB_Body']
            ))
            continue

        # Horizontal rules
        if stripped in ('---', '***', '___'):
            story.append(Spacer(1, 6))
            story.append(HRFlowable(width="100%", thickness=1, color=BORDER_GREY))
            story.append(Spacer(1, 6))
            i += 1
            continue

        # Headers
        if stripped.startswith('#'):
            level = len(stripped) - len(stripped.lstrip('#'))
            text = stripped.lstrip('#').strip()
            text = md_inline(escape_xml(text))

            if level == 1:
                story.append(Spacer(1, 10))
                story.append(HRFlowable(width="100%", thickness=2, color=DARK_BLUE))
                story.append(Paragraph(text, styles['NB_H1']))
            elif level == 2:
                story.append(Paragraph(text, styles['NB_H2']))
            elif level >= 3:
                story.append(Paragraph(text, styles['NB_H3']))
            i += 1
            continue

        # Tables: collect consecutive table lines
        if '|' in stripped and re.match(r'^\|.*\|$', stripped):
            table_lines = []
            while i < len(lines) and '|' in lines[i].strip():
                table_lines.append(lines[i])
                i += 1
            rows = parse_md_table(table_lines)
            if rows:
                t = build_table(rows)
                if t:
                    story.append(Spacer(1, 6))
                    story.append(t)
                    story.append(Spacer(1, 6))
            continue

        # Code blocks
        if stripped.startswith('```'):
            code_lines = []
            i += 1
            while i < len(lines) and not lines[i].strip().startswith('```'):
                code_lines.append(lines[i])
                i += 1
            i += 1  # skip closing ```
            code_text = escape_xml('\n'.join(code_lines))
            if code_text.strip():
                story.append(Preformatted(code_text, styles['NB_Code']))
            continue

        # Blockquotes
        if stripped.startswith('>'):
            quote_lines = []
            while i < len(lines) and lines[i].strip().startswith('>'):
                quote_lines.append(lines[i].strip().lstrip('>').strip())
                i += 1
            quote_text = ' '.join(quote_lines)
            quote_text = md_inline(escape_xml(quote_text))
            story.append(Paragraph(quote_text, styles['NB_Blockquote']))
            continue

        # Bullet points
        if stripped.startswith('- ') or stripped.startswith('* '):
            text = stripped[2:]
            text = md_inline(escape_xml(text))
            story.append(Paragraph(f'\u2022  {text}', styles['NB_Bullet']))
            i += 1
            continue

        # Numbered lists
        num_match = re.match(r'^(\d+)\.\s+(.*)', stripped)
        if num_match:
            num = num_match.group(1)
            text = num_match.group(2)
            text = md_inline(escape_xml(text))
            story.append(Paragraph(f'{num}.  {text}', styles['NB_Bullet']))
            i += 1
            continue

        # Regular paragraph - collect consecutive non-special lines
        para_lines = []
        while i < len(lines):
            l = lines[i].strip()
            if (not l or l.startswith('#') or l.startswith('```') or
                l.startswith('>') or l.startswith('- ') or l.startswith('* ') or
                l.startswith('|') or l in ('---', '***', '___') or
                l.startswith('![') or '<details>' in l or
                re.match(r'^\d+\.\s+', l)):
                break
            para_lines.append(l)
            i += 1

        if para_lines:
            text = ' '.join(para_lines)
            text = md_inline(escape_xml(text))
            story.append(Paragraph(text, styles['NB_Body']))


def process_code_cell(source, story):
    """Convert a code cell to a styled code block."""
    if not source.strip():
        return

    code_text = escape_xml(source.rstrip())

    # Add a "Python" label
    story.append(Spacer(1, 4))
    story.append(Paragraph(
        '<font name="Helvetica-Bold" size="8" color="#1565c0">Python</font>',
        styles['NB_Body']
    ))
    story.append(Preformatted(code_text, styles['NB_Code']))


# ─── Build the document ─────────────────────────────────────────

def header_footer(canvas, doc):
    """Draw header and footer on each page."""
    canvas.saveState()

    # Header line
    canvas.setStrokeColor(DARK_BLUE)
    canvas.setLineWidth(1.5)
    canvas.line(72, letter[1] - 50, letter[0] - 72, letter[1] - 50)

    # Header text
    canvas.setFont('Helvetica', 8)
    canvas.setFillColor(MED_BLUE)
    canvas.drawString(72, letter[1] - 45, "Advanced NLP Part 1 - Basics")
    canvas.drawRightString(letter[0] - 72, letter[1] - 45, "Lecture Notes")

    # Footer
    canvas.setStrokeColor(BORDER_GREY)
    canvas.setLineWidth(0.5)
    canvas.line(72, 50, letter[0] - 72, 50)

    canvas.setFont('Helvetica', 8)
    canvas.setFillColor(DARK_GREY)
    canvas.drawCentredString(letter[0] / 2, 36, f"Page {doc.page}")

    canvas.restoreState()


def first_page(canvas, doc):
    """Draw the first page (title page)."""
    canvas.saveState()

    # Blue banner at top
    canvas.setFillColor(DARK_BLUE)
    canvas.rect(0, letter[1] - 180, letter[0], 180, fill=True, stroke=False)

    # Title text
    canvas.setFont('Helvetica-Bold', 32)
    canvas.setFillColor(white)
    canvas.drawCentredString(letter[0] / 2, letter[1] - 90, "Advanced NLP")
    canvas.setFont('Helvetica-Bold', 28)
    canvas.drawCentredString(letter[0] / 2, letter[1] - 125, "Part 1 - Basics")

    # Subtitle
    canvas.setFont('Helvetica', 14)
    canvas.setFillColor(HexColor("#90caf9"))
    canvas.drawCentredString(letter[0] / 2, letter[1] - 160, "Comprehensive Lecture Notes with Practice Exercises")

    # Footer
    canvas.setFont('Helvetica', 9)
    canvas.setFillColor(DARK_GREY)
    canvas.drawCentredString(letter[0] / 2, 50, "Week 5 Lecture - Practical Session")

    canvas.restoreState()


# Build the PDF
doc = SimpleDocTemplate(
    OUT_PATH,
    pagesize=letter,
    topMargin=70,
    bottomMargin=65,
    leftMargin=72,
    rightMargin=72,
    title="Advanced NLP Part 1 - Basics",
    author="Course Instructor",
)

story = []

# Title page content (after the canvas-drawn banner)
story.append(Spacer(1, 140))  # Space for the banner

story.append(Paragraph(
    "Course Overview",
    styles['NB_H2']
))
story.append(Spacer(1, 8))

overview_text = (
    "This lecture covers fundamental Natural Language Processing (NLP) techniques "
    "including POS Tagging, Shallow Parsing, Dependency Parsing, Named Entity Recognition, "
    "and Topic Modeling. Each section includes detailed explanations, code examples, "
    "and practice exercises."
)
story.append(Paragraph(overview_text, styles['NB_Body']))
story.append(Spacer(1, 16))

# Table of contents
toc_data = [
    ["Part", "Topic", "Key Concepts"],
    ["1", "POS Tagging", "SpaCy, NLTK, N-gram taggers, Classifiers"],
    ["2", "Shallow Parsing", "Chunking, Chinking, Regex grammars, IOB tags"],
    ["3", "Dependency Parsing", "Grammatical relations, Tree visualization"],
    ["4", "Named Entity Recognition", "Entity types, SpaCy NER, Entity extraction"],
    ["5", "Topic Modeling", "NMF, SVD, LDA, Time analysis"],
]
toc_table = build_table(toc_data)
if toc_table:
    story.append(toc_table)

story.append(PageBreak())

# ─── Process each cell ───────────────────────────────────────────
cells = nb.get("cells", [])
skip_first_title = True  # Skip the first markdown cell (duplicate of title page)

for cell in cells:
    cell_type = cell.get("cell_type", "")
    source = "".join(cell.get("source", []))

    if not source.strip():
        continue

    if cell_type == "markdown":
        # Skip the very first title cell since we have a custom title page
        if skip_first_title and source.strip().startswith("# Advanced NLP Part 1"):
            skip_first_title = False
            # But still process the content after the title
            # Remove just the title line
            lines = source.split('\n')
            rest = '\n'.join(lines[1:])
            if rest.strip():
                process_markdown_cell(rest, story)
            continue
        skip_first_title = False
        process_markdown_cell(source, story)

    elif cell_type == "code":
        process_code_cell(source, story)

# ─── Final summary page ─────────────────────────────────────────
story.append(Spacer(1, 30))
story.append(HRFlowable(width="100%", thickness=2, color=DARK_BLUE))
story.append(Spacer(1, 10))
story.append(Paragraph("End of Lecture Notes", styles['NB_H2']))
story.append(Paragraph(
    "Practice the exercises, experiment with your own text data, "
    "and explore the referenced libraries for deeper understanding.",
    styles['NB_Body']
))

# Build
doc.build(story, onFirstPage=first_page, onLaterPages=header_footer)
print(f"PDF generated successfully: {OUT_PATH}")
