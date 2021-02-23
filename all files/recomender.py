import investpy
import pandas as pd
# import json
# import random
import yfinance as yf

ticker = input("Enter ticker: ")

#Get Yahoo! Finance Big Firm Recommendations
yticker = yf.Ticker(ticker)
ytickerRecommendations = yticker.recommendations

#Take only the last 12 recommendations
lastRecommendations = ytickerRecommendations.iloc[-12:]
lastRecommendations = lastRecommendations.sort_index(ascending=False)
lastRecommendations = lastRecommendations.reset_index()

#Get Investing.com Technical Analysis Data
interval = input("Technical An. Interval (5mins, 15mins, 30mins, 1hour, 5hours, daily, weekly and monthly): ")
idata1 = investpy.technical_indicators(name=ticker, country='united states', product_type='stock', interval=interval)

#Add ticker column to Investing.com data
idata1.insert(0, "Ticker", ticker)

resultData = pd.concat([idata1,lastRecommendations], axis=1)

#Summary Row Title
summaryTitle = {'Ticker': ['Summary']}
summaryRow = pd.DataFrame(summaryTitle)

#Create analysis summary and combine data from Investing.com and Yahoo! Finance
isummary1 = idata1.groupby(['signal'])[['value']].count()
ysummary1 = lastRecommendations.groupby(['To Grade'])[['From Grade']].count()

isummary1 = isummary1.reset_index()
ysummary1 = ysummary1.reset_index()

#Add first and last dates of the Firms Recommendations
fromDate = lastRecommendations['Date'].iloc[0] # first element 
toDate = lastRecommendations['Date'].iloc[-1] # last element 

ftDates = {'Date': [fromDate,toDate]}
summaryDates = pd.DataFrame(ftDates)

summary1 = pd.concat([isummary1,ysummary1,summaryDates], axis=1)
summary1.insert(0, "Ticker", ticker) 

#Combine datasets
resultData = pd.concat([resultData,summaryRow,summary1])

df = pd.DataFrame(resultData)
fileName = ticker + ' ' + interval + '.csv'
df.to_csv(path_or_buf=fileName,index=True)


print(resultData)
print('Analysis file - ' + ticker + ' ' + interval + '.csv generated') 
