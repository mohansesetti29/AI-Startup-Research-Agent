
from .base_agent import BaseAgent

class RewriteAgent(BaseAgent):
    def __init__(self):
        super().__init__("RewriteAgent")

    def rewrite_points(self, bullet_points: list[str]):
        rewritten = []
        for point in bullet_points:
            p = point.replace(" - ", "").strip()
            if p.lower().startswith("the"):
                p = p[0].upper() + p[1:]
            rewritten.append(p)
        return rewritten

    def exec_summary(self, summary_dict):
        highlights = []
        for section, bullets in summary_dict.items():
            for b in bullets[:1]:  # pick strongest bullet
                highlights.append(b)
        return " ".join(highlights)
