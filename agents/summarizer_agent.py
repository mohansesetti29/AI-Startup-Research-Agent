
from .base_agent import BaseAgent
import re

class SummarizerAgent(BaseAgent):
    def __init__(self):
        super().__init__("SummarizerAgent")

    def extract_sentences(self, text):
        text = text.replace("\n", " ")
        parts = re.split(r'(?<=[.!?]) +', text)
        return [p.strip() for p in parts if len(p.strip()) > 40]

    def summarize_section(self, section):
        points = []
        for item in section:
            sentences = self.extract_sentences(item["passage"])
            if sentences:
                points.append(f"- {sentences[0]}")
        return points[:3]  # keep top 3 concise bullets
