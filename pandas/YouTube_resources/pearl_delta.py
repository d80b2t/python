'''
Just some babay code to see if I can read in some data from Wikipedia about the Pearl Delta
https://en.wikipedia.org/wiki/Pearl_River_Delta
'''
import pandas as pd

data_dir = '/cos_pc19a_npr/data/Wikipedia/'
data_file = 'Pearl_delta.html'
data_path = data_dir+data_file

## http://pandas.pydata.org/pandas-docs/stable/generated/pandas.read_html.html
##
## Read HTML tables into a list of DataFrame objects.
##
df = pd.read_html(data_path)


'''
In [39]: type(df)
Out[39]: list

In [40]: df
Out[40]: 
[                0                   1                  2  \
 0            Name                City               Type   
 1          Baiyun  Guangzhou (Yuexiu)        Subdistrict   
 2         Beijing  Guangzhou (Yuexiu)        Subdistrict   
 3          Dadong  Guangzhou (Yuexiu)        Subdistrict   
 4          Datang  Guangzhou (Yuexiu)        Subdistrict   
 5        Dengfeng  Guangzhou (Yuexiu)        Subdistrict
 ..
 383                  398304      2723.9             146  
 384                  341197      2002.8             170  
 385                  542882      1262.9             429  
 [386 rows x 6 columns]]


In [41]: dff = df[0]

In [42]: dff
Out[42]: 
                0                   1                  2  \
0            Name                City               Type   
1          Baiyun  Guangzhou (Yuexiu)        Subdistrict   
2         Beijing  Guangzhou (Yuexiu)        Subdistrict
384                  341197      2002.8             170  
385                  542882      1262.9             429  

[386 rows x 6 columns]

NPR: Things to note, The starting and ending [] for the df


In [46]: type(df)
Out[46]: list

In [47]: type(df[0])
Out[47]: pandas.core.frame.DataFrame

In [48]: type(dff)
Out[48]: pandas.core.frame.DataFrame

In [49]: dfff = dff[0]

In [50]: type(dfff)
Out[50]: pandas.core.series.Series

In [50]: type(dfff)
Out[50]: pandas.core.series.Series
'''
