import os
from fpdf import FPDF

def add_warning(pdf, message):
    pdf.set_text_color(255, 0, 0)
    pdf.set_font("Arial", "B", 12)
    pdf.multi_cell(0, 8, f"⚠ {message}")
    pdf.ln(3)
    pdf.set_text_color(0, 0, 0)


def clean_text(text):
    """Remove unsupported unicode characters for FPDF"""
    if not text:
        return ""
    return text.encode("latin-1", "ignore").decode("latin-1")


def create_pdf(ticker, market_data, financial_data, logs=None):
    pdf = FPDF()
    pdf.set_auto_page_break(auto=True, margin=15)
    pdf.add_page()
    pdf.set_left_margin(15)
    pdf.set_right_margin(15)

    pdf.set_font("Arial", size=12)

    # ===== TITLE =====
    pdf.cell(0, 10, clean_text(f"Financial Report: {ticker}"), ln=True)
    pdf.ln(3)

    # ===== PARTIAL DATA WARNINGS =====
    if financial_data.get("error"):
        add_warning(pdf, "Price data unavailable. Report generated with partial data.")

    if market_data.get("error"):
        add_warning(pdf, "Market data unavailable. Sentiment may be incomplete.")

    # ===== MARKET SENTIMENT =====
    pdf.cell(
        0,
        10,
        clean_text(f"Market Sentiment: {market_data.get('sentiment', 'N/A')}"),
        ln=True,
    )
    pdf.ln(3)

    # ===== HEADLINES =====
    pdf.set_font("Arial", "B", 12)
    pdf.cell(0, 10, "Recent Headlines:", ln=True)
    pdf.set_font("Arial", size=11)

    headlines = market_data.get("headlines", [])
    if not headlines:
        pdf.multi_cell(180, 8, "- No headlines available")
    else:
        for h in headlines:
            pdf.multi_cell(180, 8, clean_text(f"- {h}"))
            pdf.ln(1)

    pdf.ln(5)

    # ===== FINANCIAL METRICS =====
    pdf.set_font("Arial", "B", 12)
    pdf.cell(0, 10, "Financial Metrics:", ln=True)
    pdf.set_font("Arial", size=11)

    pdf.cell(0, 8, f"Volatility: {financial_data.get('volatility', 'N/A')}", ln=True)
    pdf.cell(
        0,
        8,
        f"Average Return: {financial_data.get('average_return', 'N/A')}",
        ln=True,
    )

    pdf.ln(5)

    # ===== CHART IMAGE =====
    chart_path = financial_data.get("charts")
    if chart_path and os.path.exists(chart_path):
        pdf.set_font("Arial", "B", 12)
        pdf.cell(0, 10, "Price Trend Chart:", ln=True)
        pdf.image(chart_path, x=15, y=pdf.get_y(), w=180)

    # ===== AGENT CONVERSATION LOGS =====
    if logs:
        pdf.add_page()
        pdf.set_font("Arial", "B", 14)
        pdf.cell(0, 10, "Agent Conversation Logs", ln=True)
        pdf.ln(3)

        pdf.set_font("Arial", size=10)
        for line in logs:
            pdf.multi_cell(0, 6, clean_text(line))

    # ===== SAVE PDF =====
    os.makedirs("reports", exist_ok=True)
    output = f"reports/{ticker}_report.pdf"
    pdf.output(output)

    return output
