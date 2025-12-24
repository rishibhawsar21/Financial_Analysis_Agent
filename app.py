import streamlit as st
from orchestration.crew import run_crew
import os

os.environ["STREAMLIT_SERVER_PORT"] = os.getenv("PORT", "8501")
os.environ["STREAMLIT_SERVER_ADDRESS"] = "0.0.0.0"


#PAGE CONFIG
st.set_page_config(
    page_title="Financial Analysis Agent Crew",
    page_icon="📊",
    layout="wide"
)

#CUSTOM CSS
st.markdown("""
<style>
.main {
    background-color: #0e1117;
}
.stButton>button {
    background-color: #4CAF50;
    color: white;
    border-radius: 8px;
    padding: 0.6em 1.2em;
    font-size: 16px;
}
.stButton>button:hover {
    background-color: #45a049;
}
.card {
    background-color: #161b22;
    padding: 20px;
    border-radius: 12px;
    box-shadow: 0px 0px 15px rgba(0,0,0,0.3);
}
.log-box {
    background-color: #0d1117;
    border-left: 4px solid #4CAF50;
    padding: 15px;
    border-radius: 8px;
}
</style>
""", unsafe_allow_html=True)

#HEADER
st.markdown(
    "<h1 style='text-align: center;'>📊 Financial Analysis Agent Crew</h1>",
    unsafe_allow_html=True
)
st.markdown(
    "<p style='text-align: center; color: gray;'>Multi-Agent AI system for stock analysis & automated reporting</p>",
    unsafe_allow_html=True
)

st.divider()

#INPUT SECTION 
with st.container():
    st.markdown("<div class='card'>", unsafe_allow_html=True)

    col1, col2 = st.columns([3, 1])

    with col1:
        ticker = st.text_input(
            "🔎 Enter Stock Ticker",
            value="AAPL",
            help="Example: AAPL, MSFT, NVDA, TSLA"
        )

    with col2:
        generate = st.button("🚀 Generate Report")

    st.markdown("</div>", unsafe_allow_html=True)

# Action
if generate:
    with st.spinner("🤖 AI agents are collaborating..."):
        report_path, logs = run_crew(ticker.upper().strip())

    st.success("✅ Report generated successfully!")

    st.divider()

    #OUTPUT SECTION 
    col_left, col_right = st.columns([2, 3])

    #PDF DOWNLOAD
    with col_left:
        st.markdown("<div class='card'>", unsafe_allow_html=True)
        st.subheader("📄 Download Report")

        with open(report_path, "rb") as f:
            st.download_button(
                label="⬇ Download PDF Report",
                data=f,
                file_name=f"{ticker}_report.pdf",
                mime="application/pdf"
            )

        st.markdown("</div>", unsafe_allow_html=True)

    #AGENT LOGS
    with col_right:
        st.markdown("<div class='card'>", unsafe_allow_html=True)
        st.subheader("🤖 Agent Conversation Logs")

        if logs:
            log_text = "\n".join(logs)
            st.markdown("<div class='log-box'>", unsafe_allow_html=True)
            st.code(log_text, language="text")
            st.markdown("</div>", unsafe_allow_html=True)
        else:
            st.info("No logs available.")

        st.markdown("</div>", unsafe_allow_html=True)

#FOOTER
st.divider()
st.markdown(
    "<p style='text-align: center; color: gray;'>Built with ❤️ using Python, Streamlit & Multi-Agent AI</p>",
    unsafe_allow_html=True
)
