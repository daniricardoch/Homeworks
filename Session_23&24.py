# Sessions 23&24
# Download data for 2-3 companies that are related. For example: Nike and Adidas, Honda and Toyota, etc
# Plot their stock graph on the same figure over the same period of time
# Do you observe any correlation?
# You can use yahoo finance to get the data in .csv format
# https://finance.yahoo.com/quote/NKE/history?p=NKE
#
# * This code allows you to customize the time frames.
# *It also pulls the data directly from the site, no need to download.


import datetime as dt
import matplotlib.pyplot as plt
from matplotlib import style
import pandas as pd
import pandas_datareader.data as web

style.use('ggplot')

start = dt.datetime(2018,11,1)
end = dt.datetime(2018,11,30)

df1 = web.DataReader('AAPL', 'yahoo', start, end)
df2 = web.DataReader('TSLA', 'yahoo', start, end)
df3 = web.DataReader('GOOG', 'yahoo', start, end)

# this part of the code is an attempt to divide all values of a certain stock by a particular number
# hopefully this would've reduced the difference in price from one stock and another
# this would have made the graphs more clear

# new_df1=[]
# for i in df1['Close']:
#     i = i/10
#     new_df1.append(i)
#
#
# print(new_df1)
#
# new_df1.plot()

print(df1, "\n", "\n", df2,"\n", "\n", df3)

df1['Close'].plot()
df2['Close'].plot()
df3['Close'].plot()

plt.show()
