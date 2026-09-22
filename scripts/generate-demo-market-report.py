from pathlib import Path

from reportlab.lib import colors
from reportlab.lib.enums import TA_LEFT
from reportlab.lib.pagesizes import A4
from reportlab.lib.styles import ParagraphStyle, getSampleStyleSheet
from reportlab.lib.units import mm
from reportlab.platypus import (
    KeepTogether,
    PageBreak,
    Paragraph,
    SimpleDocTemplate,
    Spacer,
    Table,
    TableStyle,
)


ROOT = Path(__file__).resolve().parents[1]
OUTPUT = ROOT / "apps" / "web" / "public" / "reports" / "solace-skin-au-market-entry-demo.pdf"

PAPER = colors.HexColor("#F2E4D1")
INK = colors.HexColor("#241109")
MUTED = colors.HexColor("#5A4A3C")
ORANGE = colors.HexColor("#E2603D")
LINE = colors.HexColor("#CDBBA6")


def style(name, **kwargs):
    return ParagraphStyle(name, parent=getSampleStyleSheet()["BodyText"], **kwargs)


SMALL = style("Small", fontName="Helvetica", fontSize=7, leading=10, textColor=MUTED)
MONO = style("Mono", fontName="Courier", fontSize=7, leading=9, textColor=ORANGE, tracking=0.5)
BODY = style("Body", fontName="Helvetica", fontSize=9, leading=14, textColor=MUTED)
HEADING = style("Heading", fontName="Helvetica-Bold", fontSize=33, leading=29, textColor=INK, spaceAfter=10)
SUBHEADING = style("Subheading", fontName="Helvetica-Bold", fontSize=20, leading=22, textColor=INK, spaceAfter=8)
CELL_HEAD = style("CellHead", fontName="Courier", fontSize=6.5, leading=9, textColor=ORANGE)
CELL_TITLE = style("CellTitle", fontName="Helvetica-Bold", fontSize=10.5, leading=13, textColor=INK)
CELL_BODY = style("CellBody", fontName="Helvetica", fontSize=7.6, leading=11, textColor=MUTED)


def header(label, page_number):
    return Table(
        [[
            Paragraph("<b>COMMON<br/>GROUND<br/>CREATIVE</b>", style("Brand", fontName="Courier-Bold", fontSize=7, leading=8, textColor=ORANGE)),
            Paragraph(label, style("Header", fontName="Courier", fontSize=7, textColor=MUTED, alignment=TA_LEFT)),
            Paragraph(f"{page_number:02d}", style("Page", fontName="Courier", fontSize=7, textColor=ORANGE, alignment=TA_LEFT)),
        ]],
        colWidths=[36 * mm, 119 * mm, 18 * mm],
        style=TableStyle([("VALIGN", (0, 0), (-1, -1), "TOP")]),
    )


def footer(page_number):
    return Table(
        [[Paragraph(f"SOLACE SKIN DEMO REPORT  /  PAGE {page_number} OF 6", style("Footer", fontName="Courier", fontSize=6.5, textColor=MUTED))]],
        colWidths=[173 * mm],
        style=TableStyle([("LINEABOVE", (0, 0), (-1, 0), 0.5, LINE), ("TOPPADDING", (0, 0), (-1, -1), 8)]),
    )


def section_title(label, title, copy=None):
    items = [Paragraph(label, MONO), Spacer(1, 5), Paragraph(title, SUBHEADING)]
    if copy:
        items.extend([Paragraph(copy, BODY), Spacer(1, 10)])
    return items


def build_pdf():
    OUTPUT.parent.mkdir(parents=True, exist_ok=True)
    doc = SimpleDocTemplate(
        str(OUTPUT),
        pagesize=A4,
        leftMargin=15 * mm,
        rightMargin=15 * mm,
        topMargin=13 * mm,
        bottomMargin=13 * mm,
        title="Solace Skin Australian Market Entry Demo",
        author="Common Ground Creative",
    )
    sections = [
        ("BUSINESS", "Lead with one hero product and use the first 90 days to validate local demand before expanding.", [("The Ordinary", "Clear hero-product focus", "Keep the first offer easy to understand"), ("Aesop", "Premium brand world", "Build trust before broadening the range")]),
        ("MARKET", "Australia is a credible test market for a premium, proof-led offer that earns trust before it scales.", [("Mecca", "Discovery-led retail", "Local education and proof matter"), ("Adore Beauty", "Digital-first comparison", "Make product benefits and price clear")]),
        ("CUSTOMERS", "Prioritise skincare-literate urban professionals who want a simple, credible routine.", [("Go-To Skincare", "Friendly routine language", "Keep the customer promise human and simple"), ("Ultra Violette", "Lifestyle-specific education", "Anchor the message in a clear use case")]),
        ("STRATEGY", "Start DTC with creator proof and paid social, then scale only the messages that show clear response.", [("The Ordinary", "Education-led product story", "Make proof visible early"), ("Aesop", "Selective distribution", "Protect premium positioning")]),
        ("BUDGET", "Keep a focused 90-day test budget across creator seeding, paid social and a conversion-ready landing page.", [("Digital-first challenger", "Small test and fast learning", "Reserve spend for the strongest signal"), ("Established premium brand", "Broad launch investment", "Avoid paying for reach before proof")]),
        ("CAMPAIGN", "Test three creator-led angles, amplify the strongest one, and retarget high-intent visitors with a routine bundle.", [("Go-To Skincare", "Founder-led familiarity", "Use a recognisable voice"), ("Ultra Violette", "Benefit-led creator proof", "Show the product in a real routine")]),
    ]
    story = []
    for page_number, (title, summary, comparisons) in enumerate(sections, start=1):
        story.extend([header(f"{page_number:02d} / {title}", page_number), Spacer(1, 22 * mm)])
        story.append(Paragraph(title, style("SectionTitle", fontName="Helvetica-Bold", fontSize=24, leading=26, textColor=INK)))
        story.append(Spacer(1, 7 * mm))
        story.append(Paragraph(summary, BODY))
        story.append(Spacer(1, 12 * mm))
        table_data = [[Paragraph("BRAND", CELL_HEAD), Paragraph("APPROACH", CELL_HEAD), Paragraph("IMPLICATION", CELL_HEAD)]]
        table_data.extend([[Paragraph(brand, CELL_TITLE), Paragraph(approach, CELL_BODY), Paragraph(implication, CELL_BODY)] for brand, approach, implication in comparisons])
        story.append(Table(table_data, colWidths=[43 * mm, 65 * mm, 65 * mm], style=TableStyle([
            ("GRID", (0, 0), (-1, -1), 0.5, LINE), ("VALIGN", (0, 0), (-1, -1), "TOP"),
            ("TOPPADDING", (0, 0), (-1, -1), 7), ("BOTTOMPADDING", (0, 0), (-1, -1), 7),
            ("LEFTPADDING", (0, 0), (-1, -1), 7), ("RIGHTPADDING", (0, 0), (-1, -1), 7),
        ])))
        story.append(Spacer(1, 145 * mm))
        story.append(footer(page_number))
        if page_number < len(sections):
            story.append(PageBreak())

    doc.build(story)


if __name__ == "__main__":
    build_pdf()
