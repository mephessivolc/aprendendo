from googlefinance.client import get_price_data, get_prices_data, get_prices_time_data
import numpy as np
import pandas as pd
# Dow Jones
param = {
    'q': "IBOV", # Stock symbol (ex: "AAPL")
    'i': "60", # Interval size in seconds ("86400" = 1 day intervals)
    'x': "INDEXBVMF", # Stock exchange symbol on which stock is traded (ex: "NASD")
    'p': "1D" # Period (Ex: "1Y" = 1 year)
}

df = get_price_data(param)
# print(df['Open'].mean())
with open('respostas.txt', 'w') as resp:
    resp.writelines(str(df['Open'].describe()))

# print(df['Open'].loc['2017-08-03 16:00:00':'2017-08-03 17:00:00'].describe())
