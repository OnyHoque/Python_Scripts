import yfinance as yf

ticker = 'TSLA'
ticker_yahoo = yf.Ticker(ticker)
data = ticker_yahoo.history()
last_quote = data['Close'].iloc[-1]
print(last_quote)
if last_quote > 100 :
    print("high")