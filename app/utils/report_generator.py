from reportlab.platypus import (
    SimpleDocTemplate,
    Paragraph,
    Spacer
)

from reportlab.lib.styles import getSampleStyleSheet


class ReportGenerator:

    @staticmethod
    def generate_report(
        filename,
        similarity_score,
        winnow_score,
        minhash_score,
        risk_level
    ):

        pdf = SimpleDocTemplate(filename)

        styles = getSampleStyleSheet()

        content = []

        title = Paragraph(
            "PlagiarismGuard AI Report",
            styles["Title"]
        )

        content.append(title)

        content.append(Spacer(1, 20))

        content.append(
            Paragraph(
                f"Similarity Score: {similarity_score}%",
                styles["Normal"]
            )
        )

        content.append(
            Paragraph(
                f"Winnowing Score: {winnow_score}%",
                styles["Normal"]
            )
        )

        content.append(
            Paragraph(
                f"MinHash Score: {minhash_score}%",
                styles["Normal"]
            )
        )

        content.append(
            Paragraph(
                f"Risk Level: {risk_level}",
                styles["Normal"]
            )
        )

        pdf.build(content)