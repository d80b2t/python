'''
https://www.youtube.com/watch?v=p_Fn_BksF9k&list=PLQVvvaa0QuDc-3szzjeP6N6b0aDrrKyL-&index=9
https://pythonprogramming.net/resample-data-analysis-python-pandas-tutorial/?completed=/percent-change-correlation-data-analysis-python-pandas-tutorial/

Useful URLs:
http://pandas.pydata.org/pandas-docs/stable/timeseries.html#offset-aliases
http://pandas.pydata.org/pandas-docs/stable/api.html#resampling
'''
import quandl
import pandas as pd
import pickle
import matplotlib.pyplot as plt
from matplotlib import style

style.use('fivethirtyeight')

api_key='xTrUFEADji37fXJVMPxM'

## Read in the data...
HPI_data = pd.read_pickle('fiddy_states3.pickle')


## Just picking out e.g., Texas... :-)
#TX1yr = HPI_data['TX'].resample('A', how='mean') ## is outta date...
## http://pandas.pydata.org/pandas-docs/stable/api.html#resampling
#TX1yr_mean = HPI_data['TX'].resample('A').mean()
TX1yr_mean = HPI_data['TX'].resample('AS').mean()

TX1yr_std = HPI_data['TX'].resample('A').std() 

TX1yr_upper = TX1yr_mean + (TX1yr_std * 2.)
TX1yr_lower = TX1yr_mean - (TX1yr_std * 2.)

## Plotting
fig = plt.figure()
ax1 = plt.subplot2grid((1,1), (0,0))

#HPI_data.plot(ax=ax1, linewidth=2) ## plots all 50 States
HPI_data['TX'].plot(ax=ax1, linewidth=2) ## plots all 50 States
TX1yr_mean.plot(ax=ax1, linewidth=2)
#TX1yr_std.plot(ax=ax1, linewidth=2)

#TX1yr_upper.plot(ax=ax1, linewidth=2)
#TX1yr_lower.plot(ax=ax1, linewidth=2)


plt.legend().remove()
plt.show()
