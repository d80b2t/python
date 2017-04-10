'''
https://pythonprogramming.net/data-analysis-python-pandas-tutorial-introduction/

N.B.
http://pandas.pydata.org/pandas-docs/stable/remote_data.html
You should replace the imports of the following:
from pandas.io import data, wb
With:
from pandas_datareader import data, wb


'''

import pandas as pd
import datetime
#import pandas.io.data as web
from pandas_datareader import data, wb

import matplotlib.pyplot as py
from matplotlib import style

style.use('ggplot')

start = datetime.datetime(2010, 1, 1)
end = datetime.datetime(2015, 8, 22)

df = web.DataReader("XOM", "yahoo", start, end)

print(df.head())

df['Adj Close'].plot()

plt.show()

