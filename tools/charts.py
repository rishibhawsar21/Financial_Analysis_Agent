
import matplotlib.pyplot as plt

def generate_charts(df, ticker):
    path = f"reports/{ticker}_price.png"
    plt.figure()
    plt.plot(df.index, df["Close"])
    plt.title(f"{ticker} Price Trend")
    plt.savefig(path)
    plt.close()
    return path
