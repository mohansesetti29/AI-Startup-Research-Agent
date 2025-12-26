import streamlit as st
import os
from main import run_multi_agent
from agents.report_agent import ReportAgent
from agents.alert_agent import AlertAgent

# ---- PAGE CONFIG ----
st.set_page_config(page_title="AI Startup Research Agent", layout="wide")

# ---- DARK THEME ----
dark_bg = """
<style>
body {
    background-color: #0d0d0d !important;
}
.report-container {
    padding: 20px;
    border-radius: 10px;
    background: #1a1a1a;
    color: white;
}
.heading {
    font-size: 42px;
    font-weight: 800;
    background: linear-gradient(90deg, #00ffcc, #0077ff);
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
}
.subtext {
    color: #9f9f9f;
    font-size: 16px;
}
.button {
    background: linear-gradient(90deg, #0077ff, #00ccff);
    color: white;
    padding: 12px 20px;
    border-radius: 8px;
}
</style>
"""
st.markdown(dark_bg, unsafe_allow_html=True)

# ---- HEADER ----
st.markdown("<h1 class='heading'>🚀 AI Startup Research Agent</h1>", unsafe_allow_html=True)
st.markdown("<p class='subtext'>Turn any startup idea into a full research report — live market data, competitors, gaps, pricing & more.</p>", unsafe_allow_html=True)

# ---- INPUT ----
query = st.text_input("🔍 Enter Startup Idea / Market Topic", placeholder="ex: AI therapy app India – competitors & TAM")

if st.button("⚡ Generate Research Report", use_container_width=True):
    if not query.strip():
        st.error("Please enter a valid topic.")
        st.stop()

    with st.spinner("⏳ Researching live web data... this may take ~60 seconds"):
        result = run_multi_agent(query)

        # Alerts
        alert = AlertAgent()
        new_links = alert.check_new(result["query"], result["sources"])

        # PDF
        report = ReportAgent()
        file_path = report.generate(result["query"], result["exec_summary"], result["summary"], result["sources"])

    st.success("🎉 Report Ready!")
    st.write("👇 Download Your PDF")

    with open(file_path, "rb") as f:
        st.download_button(
            label="📥 Download PDF",
            data=f,
            file_name=os.path.basename(file_path),
            mime="application/pdf",
            type="primary"
        )

    if new_links:
        st.warning("🆕 New Market Updates Detected!")
        for link in new_links:
            st.write("• ", link)

# ---- HISTORY PANEL ----
with st.expander("📜 View Report History"):
    files = os.listdir("output/reports")
    files = sorted(files, reverse=True)
    for f in files:
        filepath = f"output/reports/{f}"
        st.write(f"📄 {f}")
        with open(filepath, "rb") as data:
            st.download_button("Download", data, file_name=f)
