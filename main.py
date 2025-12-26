from agents.planner_agent import PlannerAgent
from agents.summarizer_agent import SummarizerAgent
from agents.report_agent import ReportAgent
from agents.rewrite_agent import RewriteAgent
from core.search import search_web
from core.scraper import fetch_text
from core.chunker import chunk_passages
from core.embedder import Embedder
from core.ranker import rank_passages
import time
import sys
from agents.alert_agent import AlertAgent

if len(sys.argv) > 1 and sys.argv[1] == "history":
    import os
    files = os.listdir("output/reports")
    print("\n📜 Research History:")
    for f in files:
        print(" -", f)
    sys.exit()


PASSAGES_PER_URL = 3

def simple_research(query):
    urls = search_web(query)
    docs = []
    for u in urls:
        text = fetch_text(u)
        if not text:
            continue
        chunks = chunk_passages(text)
        docs += [{"url": u, "text": c} for c in chunks[:PASSAGES_PER_URL]]
    return docs

def run_multi_agent(query):
    start = time.time()
    planner = PlannerAgent()
    summarizer = SummarizerAgent()
    rewriter = RewriteAgent()

    plan = planner.plan(query)
    print("\n🧩 Research Plan:", plan, "\n")

    embedder = Embedder()
    final_summary = {}
    final_sources = {}

    for task in plan["tasks"]:
        docs = simple_research(task)
        if not docs:
            continue

        texts = [d["text"] for d in docs]
        emb = embedder.encode(texts)
        q_emb = embedder.encode([task])[0]

        ranked = rank_passages(texts, emb, q_emb, top_k=2)
        bullet_points = []

        for text, score in ranked:
            src = [d["url"] for d in docs if d["text"] == text][0]
            bullet_points.extend(summarizer.summarize_section([{"passage": text}]))

            if task not in final_sources:
                final_sources[task] = []
            final_sources[task].append(src)

        final_summary[task] = bullet_points

    elapsed = round(time.time() - start, 2)
    clean_summary = {}
    for section, bullets in final_summary.items():
           clean_summary[section] = rewriter.rewrite_points(bullets)

    exec_summary = rewriter.exec_summary(clean_summary)

    return {"query": query, "summary": final_summary,"exec_summary": exec_summary, "sources": final_sources, "time": elapsed}


if __name__ == "__main__":
    query = sys.argv[1] if len(sys.argv) > 1 else input("\n🔍 Enter research topic: ")
    out = run_multi_agent(query)
    print("\n📌 Final Structured Summary:\n", out["summary"])
    print("\n🔗 Sources:\n", out["sources"])
    print("\n⏱ Time:", out["time"], "s")

    alert = AlertAgent()
    new_links = alert.check_new(out["query"], out["sources"])

    if new_links:
        print("\n🔔 ALERT — New information detected!")
        for link in new_links:
            print(" +", link)
    else:
        print("\nℹ No new updates detected.")

    report = ReportAgent()
    file_path = report.generate(out["query"], out["exec_summary"], out["summary"], out["sources"])
    print("\n📁 PDF Report Generated:", file_path)
