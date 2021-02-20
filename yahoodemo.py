import yfinance as yf
'''
# show analysts recommendations
msft.recommendations

# get stock info
msft.info

msft = yf.Ticker("MSFT")
msftt = msft.cashflow
rows = msftt.iloc[-10:]
print(msftt)

data = yf.download("SPY AAPL MSFT", start="2017-01-01", end="2017-04-30")
print(data)
'''
bidu = yf.Ticker("BIDU")
biduu = bidu.recommendations
rows = biduu.iloc[-10:]
x = "BIDU"
print(yf.Ticker(x).recommendations)

