
import yfinance as yf
from tools.sentiment import analyze_sentiment

def run_market_research(ticker, log):
    log("Market Researcher", "Downloading latest headlines")
    stock = yf.Ticker(ticker)
    news = stock.news[:5] if stock.news else []
    headlines = [n.get("title", "") for n in news]
    sentiment = analyze_sentiment(" ".join(headlines))
    log("Market Researcher", "Sentiment analysis completed")
    return {
        "headlines": headlines,
        "sentiment": sentiment
    }