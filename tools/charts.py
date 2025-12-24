import os
import matplotlib.pyplot as plt

def generate_charts(df, ticker):
    # ✅ Ensure reports folder exists (IMPORTANT for Render)
    os.makedirs("reports", exist_ok=True)

    path = f"reports/{ticker}_price.png"

    plt.figure(figsize=(10, 5))
    plt.plot(df.index, df["Close"])
    plt.title(f"{ticker} Price Trend")
    plt.xlabel("Date")
    plt.ylabel("Price")
    plt.grid(True)

    plt.savefig(path)
    plt.close()

    return path
