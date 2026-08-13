from reportlab.lib.pagesizes import A4
from reportlab.platypus import (
    SimpleDocTemplate,
    Paragraph,
    Spacer
)
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.lib.units import inch


def create_pdf_report(
    total_questions,
    average_score,
    performance,
    history,
    ai_report
):

    filename = "AI_Interview_Report.pdf"

    document = SimpleDocTemplate(
        filename,
        pagesize=A4
    )

    styles = getSampleStyleSheet()

    elements = []


    # Title
    elements.append(
        Paragraph(
            "AI Interview Bot - Final Report",
            styles["Title"]
        )
    )

    elements.append(
        Spacer(1, 0.3 * inch)
    )


    # Summary
    elements.append(
        Paragraph(
            f"Questions Attempted: {total_questions}",
            styles["Heading2"]
        )
    )

    elements.append(
        Paragraph(
            f"Average Score: {average_score:.1f}/10",
            styles["Heading2"]
        )
    )

    elements.append(
        Paragraph(
            f"Overall Performance: {performance}",
            styles["Heading2"]
        )
    )

    elements.append(
        Spacer(1, 0.3 * inch)
    )


    # Interview History
    elements.append(
        Paragraph(
            "Interview History",
            styles["Heading1"]
        )
    )


    for i, item in enumerate(history):

        elements.append(
            Paragraph(
                f"Question {i + 1}: {item['question']}",
                styles["Heading3"]
            )
        )

        elements.append(
            Paragraph(
                f"Your Answer: {item['answer']}",
                styles["BodyText"]
            )
        )

        elements.append(
            Paragraph(
                f"Score: {item['score']}/10",
                styles["BodyText"]
            )
        )

        elements.append(
            Spacer(1, 0.2 * inch)
        )


    # AI Performance Analysis
    if ai_report:

        elements.append(
            Paragraph(
                "AI Performance Analysis",
                styles["Heading1"]
            )
        )

        elements.append(
            Paragraph(
                ai_report.replace("\n", "<br/>"),
                styles["BodyText"]
            )
        )


    # Build PDF
    document.build(elements)

    return filename