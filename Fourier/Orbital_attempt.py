'''
Originally from:: 
/cos_pc19a_npr/data/Orbital_npr/Having_Another_Go.ipynb

Having another go at the Orbital Insight Data Challenge... 
https://machinelearningmastery.com/make-sample-forecasts-arima-python/
http://www.seanabu.com/2016/03/22/time-series-seasonal-ARIMA-model-in-python/
'''

import numpy as np
import pandas as pd
import scipy.fftpack
import matplotlib.pyplot as plt
import datetime

from dateutil.relativedelta import relativedelta

from pandas import read_csv
#from pandas import datetime
#from pandas import DataFrame
from pandas import Series

import statsmodels.api as sm  
from statsmodels.tsa.stattools import acf  
from statsmodels.tsa.stattools import pacf
from statsmodels.tsa.seasonal import seasonal_decompose

infile='data_2use.csv'
df = pd.read_csv(infile, parse_dates=True)
df.head()

print(df['date'].head())
print(type(df['date']))
df['car.count'].head()


df_cloudy = df[df['cloud.indicator'] == 'cloudy']
df_clear = df[df['cloud.indicator'] == 'clear']
print(len(df_cloudy))
print(len(df_clear))
print(len(df))

## Some initial plotting
fig, ax = plt.subplots()
ax.plot_date(df['date'],        df['car.count'], fmt='.', color='k')
ax.plot_date(df_clear['date'], df_clear['car.count'], fmt='.', color='b')
ax.plot_date(df_cloudy['date'], df_cloudy['car.count'], fmt='.', color='r')

fig.autofmt_xdate()
plt.xlabel('Date')
plt.ylabel('Counts')
plt.show()

## Getting things ready for the FFT
start = pd.Timestamp(df['date'].min())
end = pd.Timestamp(df['date'].max())
print(start,end)
num = (len(df['date']))

t = np.linspace(start.value, end.value, num)
print(t, t.min(), t.max())
t = (t- t.min())/8.64000000e+13
print(t, t.min(), t.max())

count_fft = scipy.fftpack.fft(df['car.count'])
cloudy_fft = scipy.fftpack.fft(df_cloudy['car.count'])
clear_fft = scipy.fftpack.fft(df_clear['car.count'])
print(count_fft[:6])
print(cloudy_fft[:6])
print(clear_fft[:6])

fig = plt.figure(figsize=(18, 4)) 
plt.xlim(-0.1, 10.0)
plt.plot(count_fft)
plt.plot(cloudy_fft)
plt.plot(clear_fft)

