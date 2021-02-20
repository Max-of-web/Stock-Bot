import investpy
import pandas as pd
import json 
import random

from pprint import pprint

# Once we select an equity, we can get its recent historical data or specify a range of 
# time to retrieve historical data from using the following functions respectively. In this
# case we will be retrieving the information as a pandas.DataFrame, but we can also retrieve
# it as a json file, for more information type in terminal: help(get_recent_data) or
# help(get_historical_data)

# Retrieved values are displayed in Euros (€) as it is the currency used in Spain
'''
df = investpy.get_stock_recent_data(stock='msft',
                                   country='united states')
print(df.head())


stocks_list = investpy.get_stocks_list(country='united states')
print(stocks_list)
'''
'''
investpy.technical.technical_indicators(name, country, product_type, interval='daily')
This function retrieves the technical indicators values calculated by Investing.com for every financial product available (stocks, funds, etfs, indices, currency crosses, bonds, certificates and commodities) for different time intervals. So on, the user must provide the product_type name and the name of the product (unless product_type is ‘stock’ which name value will be the stock’s symbol) and the country if required (mandatory unless product_type is either ‘currency_cross’ or ‘commodity’, where it must be None). Additionally, the interval can be specified which defines the update frequency of the calculations of the technical indicators (mainly momentum indicators).

Parameters:	
name (str) – name of the product to retrieve the technical indicators table from (if product_type is stock, its value must be the stock’s symbol not the name).
country (str) – country name of the introduced product if applicable (if product_type is either currency_cross or commodity this parameter should be None, unless it can be specified just for commodity product_type).
product_type (str) – identifier of the introduced product, available ones are: stock, fund, etf, index, currency_cross, bond, certificate and commodity.
interval (str) – time interval of the resulting calculations, available values are: 5mins, 15mins, 30mins, 1hour, 5hours, daily, weekly and monthly.
Returns:	
The resulting pandas.DataFrame contains the table with the results of the calculation of the technical indicators made by Investing.com for the introduced financial product. So on, if the retrieval process succeed its result will look like:

 technical_indicator | value | signal
---------------------|-------|--------
 xxxxxxxxxxxxxxxxxxx | xxxxx | xxxxxx
Return type:	
pandas.DataFrame - technical_indicators

Raises:	
ValueError – raised if any of the introduced parameters is not valid or errored.
ConnectionError – raised if the connection to Investing.com errored or could not be established.
Examples

>>> data = investpy.technical_indicators(name='bbva', country='spain', product_type='stock', interval='daily')
>>> data.head()


print(stocks)



stocks = investpy.stocks.get_stocks_overview('united states', as_json=True, n_results=100)


  

# Serializing json  
json_object = json.dumps(stocks, indent = 4)  
  
# Writing to sample.json 
with open("sample.json", "w") as outfile: 
    outfile.write(json_object) 


fruits = ["apple", "banana", "cherry"]
for x in fruits:
  print(x)
'''
data1 = investpy.technical_indicators(name='bidu', country='united states', product_type='stock', interval='daily')
data2 = investpy.technical_indicators(name='msft', country='united states', product_type='stock', interval='daily')
title = {'title': ['bidu']}

df = pd.DataFrame(data=title)

data = pd.concat([data1,df, data2])

df = pd.DataFrame(data.head())
df.to_csv(path_or_buf= 'out.csv',index=False)


print(data)

#Just a test comment for Github









