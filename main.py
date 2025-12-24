from tools.ticker_utils import is_valid_ticker, suggest_ticker

ticker = input("Enter stock ticker: ").upper().strip()

if not is_valid_ticker(ticker):
    suggestion = suggest_ticker(ticker)
    if suggestion:
        print(f"❓ Invalid ticker. Did you mean {suggestion}? Using {suggestion}.")
        ticker = suggestion
    else:
        print("❌ Invalid ticker. No suggestion found.")
