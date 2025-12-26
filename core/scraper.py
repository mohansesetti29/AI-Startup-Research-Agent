
import requests
from bs4 import BeautifulSoup

def fetch_text(url, timeout=10):
    headers = {"User-Agent": "Mozilla/5.0 (auto-research-agent)"}
    try:
        r = requests.get(url, timeout=timeout, headers=headers)
        if r.status_code != 200:
            return ""
        soup = BeautifulSoup(r.text, "html.parser")

        for t in soup(["script", "style", "noscript", "svg", "iframe", "header", "footer", "nav"]):
            t.extract()

        paragraphs = [p.get_text(" ", strip=True) for p in soup.find_all("p")]

        text = " ".join(paragraphs)
        return text
    except:
        return ""
