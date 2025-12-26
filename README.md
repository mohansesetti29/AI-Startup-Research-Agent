
# 🚀 AI Startup Research Agent — Multi-Agent Market Intelligence Tool

Turn any startup idea into a full research report — automatically.  
This project is a **multi-agent AI research system** that searches the web in real-time, extracts relevant information, summarizes market insights, detects new competitor updates, and generates a **downloadable PDF market report** — all from a single query.

Built using:  
🧠 Python + Multi-Agent Architecture  
🌐 Real-time Web Scraping (DuckDuckGo + Requests + BS4)  
🧮 Sentence-Transformer Embeddings (Local — no OpenAI needed)  
📑 ReportLab PDF Generation  
⚡ Streamlit Dark-UI for Demo  
🔔 Alert System to detect NEW market updates

---

## 🎯 What Problem Does It Solve?

Startup founders waste **hours researching**:
- Competitors
- Pricing
- TAM & Market Size
- Trends
- Pain points
- Opportunities

This tool automates that entire workflow.

Example query 👇

"AI smartwatch for seniors India – market competitors & opportunity"


Output PDF includes:
- Competitors
- Pricing tables
- TAM & market size (India + global)
- Adoption trends
- Pain-points
- Market gaps & opportunities
- Executable summary
- Full citation list

---

## 🧩 Architecture — Multi-Agent Flow

User Input
↓
Planner Agent → generates research sub-tasks
↓
Research Agent → web search + scrape + extract text
↓
Embedder → convert text → vectors
↓
Ranker → relevance scoring
↓
Summarizer Agent → extract useful insights
↓
Rewrite Agent → rewrite into clean English
↓
Alert Agent → detect new unseen URLs
↓
Report Agent → generate PDF file


---

## 🖥️ UI Screenshot (Dark Theme)

Run with:

```bash
streamlit run ui.py
```

Features:
- Modern dark-theme dashboard
- Founder-friendly UX
- One-click PDF download
- History panel for past reports
- Alert popup when new competitor data is found

---

## 🛠️ Installation

### 1️⃣ Clone Repo
```bash
git clone https://github.com/mohansesetti29/AI-Startup-Research-Agent.git
cd AI-Startup-Research-Agent


2️⃣ Install Dependencies

pip install -r requirements.txt
First run will auto-download sentence-transformer model (~90MB)

▶️ Run the App
CLI mode :
   python main.py "AI therapy app India – pricing & TAM"

Streamlit mode :
   streamlit run ui.py


📂 Project Structure

.
├─ main.py
├─ ui.py
├─ agents/
│  ├─ planner_agent.py
│  ├─ research_agent.py
│  ├─ summarizer_agent.py
│  ├─ rewrite_agent.py
│  ├─ alert_agent.py
│  ├─ report_agent.py
├─ core/
│  ├─ search.py
│  ├─ scraper.py
│  ├─ chunker.py
│  ├─ embedder.py
│  ├─ ranker.py
├─ output/
│  ├─ reports/
│  ├─ seen_urls.json
├─ requirements.txt
└─ README.md


📑 PDF Output Example Structure

Market Research Report — AI Smartwatch for Seniors (India)

Executive Summary:
 - Seniors market growing 12% CAGR
 - Demand driven by health alerts, fall-detection

Sections:
 ✔ Competitors list
 ✔ Market size + India forecast
 ✔ Pricing
 ✔ Pain Points
 ✔ Gaps + Opportunities
 ✔ Links / Citations


🔔 Alerts — Detect NEW Market Info

Each run compares live-scraped URLs against previous history:

🔔 ALERT — New information detected!
 + https://mordorintelligence.com/...
 + https://navdristi.in/ai-smartwatch...

Seen URLs stored here:

output/seen_urls.json


