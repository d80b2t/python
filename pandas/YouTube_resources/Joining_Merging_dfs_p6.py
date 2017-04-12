'''
https://www.youtube.com/watch?v=XMjSGGej9y8&list=PLQVvvaa0QuDc-3szzjeP6N6b0aDrrKyL-&index=6

https://pythonprogramming.net/join-merge-data-analysis-python-pandas-tutorial/?completed=/concatenate-append-data-analysis-python-pandas-tutorial/
'''
import pandas as pd

df1 = pd.DataFrame({'HPI':[80,85,88,85],
                    'Int_rate':[2, 3, 2, 2],
                    'US_GDP_Thousands':[50, 55, 65, 55]},
                    index = [2001, 2002, 2003, 2004])
   
df2 = pd.DataFrame({'HPI':[80,85,88,85],
                    'Int_rate':[2, 3, 2, 2],
                    'US_GDP_Thousands':[50, 55, 65, 55]},
                   index = [2005, 2006, 2007, 2008])

df3 = pd.DataFrame({'HPI':[80,85,88,85],
                    'Unemployment':[7, 8, 9, 6],
                    'Low_tier_HPI':[50, 52, 50, 53]},
                   index = [2001, 2002, 2003, 2004])

## Merging
#print(pd.merge(df1,df2, on='HPI'))
## Gives duplicated data...
##print(pd.merge(df1,df2, on=['HPI']))

#print(pd.merge(df1,df2, on=['HPI', 'Int_rate']))

## Joining
df1.set_index('HPI', inplace=True)
df3.set_index('HPI', inplace=True)

joined = df1.join(df3)
#print(joined)
## Still got some data duplication


## Merging...
df1 = pd.DataFrame({
                    'Int_rate':[2, 3, 2, 2],
                    'US_GDP_Thousands':[50, 55, 65, 55],
                    'Year':[2001, 2002, 2003, 2004]
                    })

df3 = pd.DataFrame({
                    'Unemployment':[7, 8, 9, 6],
                    'Low_tier_HPI':[50, 52, 50, 53],
                    'Year':[2001, 2003, 2004, 2005]})

merged = pd.merge(df1,df3, on='Year')
## Only picks out Years in common:: 2001, 2003, 2004
merged.set_index('Year', inplace=True)
#print(merged)

## Four choices for the databases/merging::
## Left, Right, Outer, Inner.
##
## merged = pd.merge(Left, Right)
#merged = pd.merge(df1,df3, on='Year', how='left')
#merged = pd.merge(df1,df3, on='Year', how='right')
#merged.set_index('Year', inplace=True)
#print(merged)

## Outer is a Union of the keys.
merged = pd.merge(df1,df3, on='Year', how='outer')
merged.set_index('Year', inplace=True)
print(merged)

## Inner is the default
merged = pd.merge(df1,df3, on='Year', how='inner')
merged.set_index('Year', inplace=True)
print(merged)

## In summary::
## With Join, index is honoured.
## With Merge (and Cat and Append) index really doesn't come into it.
## The key to Merge is to merge on a common column (name)
