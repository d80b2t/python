'''
https://www.youtube.com/watch?v=ylIRlTFt_Fk&index=5&list=PLQVvvaa0QuDc-3szzjeP6N6b0aDrrKyL-
https://pythonprogramming.net/concatenate-append-data-analysis-python-pandas-tutorial/?completed=/dataset-data-analysis-python-pandas-tutorial/
'''

import pandas as pd

## Note, df1 and df3 have the same index, but not the same columns
## df2 and df3 have different indexes (and different columns).
## 
df1 = pd.DataFrame({'HPI':[80,85,88,85],
                    'Int_rate':[2, 3, 2, 2],
                    'US_GDP_Thousands':[50, 55, 65, 55]},
                   index = [2001, 2002, 2003, 2004])

df2 = pd.DataFrame({'HPI':[80,85,88,85],
                    'Int_rate':[2, 3, 2, 2],
                    'US_GDP_Thousands':[50, 55, 65, 55]},
                   index = [2005, 2006, 2007, 2008])

df3 = pd.DataFrame({'HPI':[80,85,88,85],
                    'Int_rate':[2, 3, 2, 2],
                    'Low_tier_HPI':[50, 52, 50, 53]},
                   index = [2001, 2002, 2003, 2004])

## This is fine, since they have the same columns
## becomes a single DataFrame
#concat = pd.concat([df1,df2])
#print(concat)

## Try with df3, and get some NaNs...
concat = pd.concat([df1,df2, df3])
#print(concat)

df4 = df1.append(df2)
#print(df4)

## Note, DataFrames are not really meant to be updated...
## meant to be manipulated, analysed, just not really changed...

df5 = df1.append(df3)
#print(df5)

s = pd.Series([80,2,50])
df6 = df1.append(s, ignore_index=True)
#print(df6)

s = pd.Series([80,2,50], index=['HPI', 'Int_rate', 'US_GDP_Thousands'])
df6 = df1.append(s, ignore_index=True)
print(df6)
## 0   80         2                50
## 1   85         3                55
## 2   88         2                65
## 3   85         2                55
##
## is df1
##
## 4   80         2                50
## is the series s
