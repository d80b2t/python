'''
https://pythonprogramming.net/data-analysis-python-pandas-tutorial-introduction/

Pandas Basics - p.2 Data Analysis with Python and Pandas Tutorial
https://www.youtube.com/watch?v=0UA49Ds1XXo&index=2&list=PLQVvvaa0QuDc-3szzjeP6N6b0aDrrKyL-
'''

import pandas as pd
import matplotlib.pyplot as plt
from matplotlib import style
style.use('ggplot')

web_stats = {'Day':[1,2,3,4,5,6],
             'Visitors':[43,34,65,56,29,76],
             'Bounce_Rate':[65,67,78,65,45,52]}

## Converting the web_stats dict(ionary) to a DataFrame:: 
df = pd.DataFrame(web_stats)

## prints whole DataFrame
print(df)

## prints first five rows
#print(df.head())
## prints last five rows
#print(df.tail())
## prints last two rows
#print(df.tail(2))


## setting *The* Index...
#df.set_index('Day')
#print(df.set_index('Day'))
## Here, you are returned *a new* dataframe!!
#      Bounce_Rate  Visitors
# Day                      
# 1          65        43
# 2          67        34
# 3          78        65
# 4          65        56
# 5          45        29
# 6          52        76

#df.set_index('Day', inplace=True)
## will make sure that the Index gets reduxed. 
#df

## Print/reference a column... 
#print(df['Visitors'])

## or could have done::
# print(df['Bounce Rate'])
## if there was a gap above -- very often there will be!!!

## or...
#print(df.Visitors)
## but NOT::
# print(df.Bounce Rate) #when no underscore.

## Referencing several columns...
#print(df[['','']])
print(df[['Bounce_Rate','Visitors']])

## convert this to a list...
print(df.Visitors.tolist)
##Name: Visitors, dtype: int64>
print(df.Visitors.tolist())
#[43, 34, 65, 56, 29, 76]






