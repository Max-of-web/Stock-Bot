import yfinance as yf
import pandas as pd
import datetime as dt
from pandas_datareader import data as pdr
import matplotlib.pyplot as plt

start = dt.datetime(2019, 2, 23)
now = dt.datetime.now()

stock = input("Enter ticker: ")

df = pdr.get_data_yahoo(stock, start, now)

df["High"].plot(Label="high")

plt.show()
