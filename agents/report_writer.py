from tools.pdf_generator import create_pdf

def generate_report(ticker, market_data, analysis_data, logs, log):
    # log conversation
    log("Report Writer", "Writing insights to PDF")

    # create PDF (pass logs also if supported)
    pdf_path = create_pdf(
        ticker=ticker,
        market_data=market_data,
        financial_data=analysis_data,
        logs=logs
    )
    log("Report Writer", f"PDF generated at {pdf_path}")
    return pdf_path
