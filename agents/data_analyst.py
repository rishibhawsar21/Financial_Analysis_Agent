
import yfinance as yf
import pandas as pd
from tools.charts import generate_charts

def run_data_analysis(ticker, log):
    log("Data Analyst", "Downloading historical price data")
    df = yf.download(ticker, period="6mo")
    df["Return"] = df["Close"].pct_change()
    volatility = df["Return"].std()
    avg_return = df["Return"].mean()
    charts = generate_charts(df, ticker)
    log("Data Analyst", "KPI calculation completed")
    return {
        "volatility": round(volatility, 4),
        "average_return": round(avg_return, 4),
        "charts": charts
    }