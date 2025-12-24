from agents.market_researcher import run_market_research
from agents.data_analyst import run_data_analysis
from agents.report_writer import generate_report

conversation_logs = []

def log(agent, message):
    conversation_logs.append(f"[{agent}] {message}")


def run_crew(ticker):
    global conversation_logs
    conversation_logs = [] 

    log("System", f"Starting analysis for {ticker}")

    # Market Research Agent
    log("Market Researcher", "Collecting market news & sentiment")
    market_data = run_market_research(ticker, log)

    # Data Analyst Agent
    log("Data Analyst", "Fetching price data & calculating KPIs")
    analysis_data = run_data_analysis(ticker, log)
    
    # Report Writer Agent
    log("Report Writer", "Generating PDF report")
    report_path = generate_report(
    ticker,
    market_data,
    analysis_data,
    conversation_logs,
    log    
    )

    log("System", "Analysis completed")
    return report_path, conversation_logs
