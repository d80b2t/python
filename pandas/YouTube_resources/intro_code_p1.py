'''
https://pythonprogramming.net/data-analysis-python-pandas-tutorial-introduction/

N.B.
http://pandas.pydata.org/pandas-docs/stable/remote_data.html

You should replace the imports of the following:
  from pandas.io import data, wb
With:
  from pandas_datareader import data, wb
OR THIS::
  import pandas_datareader.data as web

'''

import pandas as pd
import datetime
#import pandas.io.data as web
#from pandas_datareader import data, wb
import pandas_datareader.data as web

import matplotlib.pyplot as plt
from matplotlib import style

style.use('ggplot')

start = datetime.datetime(2010, 1, 1)
end = datetime.datetime(2015, 8, 22)

## df = web.DataReader("XOM", "yahoo", start, end)
## Goes to:
df = web.DataReader("XOM", 'yahoo', start, end)

## Just the first five rows
## Date being treated as an index...
print(df.head())

##                 Open       High        Low      Close    Volume  Adj Close
## Date                                                                       
## 2010-01-04  68.720001  69.260002  68.190002  69.150002  27809100  56.187171
## 2010-01-05  69.190002  69.449997  68.800003  69.419998  30174700  56.406554
## 2010-01-06  69.449997  70.599998  69.339996  70.019997  35044700  56.894077
## 2010-01-07  69.900002  70.059998  69.419998  69.800003  27192100  56.715323
## 2010-01-08  69.690002  69.750000  69.220001  69.519997  24891800  56.487807

df['Adj Close'].plot()

plt.show()

