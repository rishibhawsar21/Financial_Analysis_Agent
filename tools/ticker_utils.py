import yfinance as yf
import difflib

POPULAR_TICKERS = [
    "AAPL", "MSFT", "GOOGL", "AMZN", "META",
    "TSLA", "NFLX", "NVDA", "IBM", "INTC"
]

def is_valid_ticker(ticker):
    try:
        df = yf.download(ticker, period="1mo")
        return not df.empty
    except Exception:
        return False

def suggest_ticker(ticker):
    matches = difflib.get_close_matches(
        ticker.upper(),
        POPULAR_TICKERS,
        n=1,
        cutoff=0.6
    )
    return matches[0] if matches else None
