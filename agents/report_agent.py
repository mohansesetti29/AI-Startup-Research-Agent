
from reportlab.lib.pagesizes import LETTER
from reportlab.pdfgen import canvas
import textwrap
import os
import datetime

class ReportAgent:
    def __init__(self, output_dir="output/reports"):
        self.output_dir = output_dir
        os.makedirs(output_dir, exist_ok=True)

    def _write_section(self, c, title, lines, y):
        c.setFont("Helvetica-Bold", 12)
        c.drawString(40, y, title)
        y -= 18
        c.setFont("Helvetica", 10)
        for line in lines:
            wrapped = textwrap.wrap(line, 90)
            for w in wrapped:
                c.drawString(50, y, w)
                y -= 14
        return y - 10

    def generate(self, query, exec_summary, summary_dict, sources_dict):
        import datetime
        timestamp = datetime.datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
        filename = f"{self.output_dir}/report_{timestamp}.pdf"
        c = canvas.Canvas(filename, pagesize=LETTER)
        y = 750

        c.setFont("Helvetica-Bold", 16)
        c.drawString(40, y, f"Market Research Report")
        y -= 25
        c.setFont("Helvetica", 10)
        c.drawString(40, y, f"Query: {query}")
        y -= 30

        c.setFont("Helvetica-Bold", 12)
        c.drawString(40, y, "Executive Summary:")
        y -= 18
        c.setFont("Helvetica", 10)
        for line in textwrap.wrap(exec_summary, 90):
            c.drawString(50, y, line)
            y -= 14
        y -= 20


        for section, bullets in summary_dict.items():
            y = self._write_section(c, section.title(), bullets, y)
            if y < 100:
                c.showPage(); y = 750

            # sources
            srcs = sources_dict.get(section, [])
            if srcs:
                y = self._write_section(c, "Sources:", srcs, y)
            if y < 100:
                c.showPage(); y = 750

        c.save()
        return filename
