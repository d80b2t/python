"""

http://manishamde.github.io/blog/2013/03/07/pandas-and-python-top-10/

"""

import pandas as pd
import numpy as np
from pandas import DataFrame, Series

df = DataFrame({'int_col' : [1,2,6,8,-1], 'float_col' : [0.1, 0.2,0.2,10.1,None], 'str_col' : ['a','b',None,'c','a']})

## At this point, if you do:
##
## In [6]: type(df)
## Out[6]: pandas.core.frame.DataFrame
##

##
##  1.   I N D E X I N G
##
## Selecting a subset of columns
##
## It is one of the simplest features but was surprisingly difficult
## to find. The ix method works elegantly for this purpose. Suppose
## you wanted to index only using columns int_col and string_col, you
## would use the advanced indexing ix method as shown below.

df.ix[:,['float_col','int_col']]

## Or... :-)
df[['float_col','int_col']]


## Conditional indexing
df[df['float_col'] > 0.15]

df[df['float_col'] == 0.1]


## Boolean/Conditional indexing
## & for and, | for or,  ~ for not
##
df[(df['float_col'] > 0.1) & (df['int_col']>2)]
df[(df['float_col'] > 0.1) | (df['int_col']>2)]

df[~(df['float_col'] > 0.1)]

## In [16]: type(df[(df['float_col'] > 0.1) & (df['int_col']>2)])
## Out[16]: pandas.core.frame.DataFrame






##
##  9.   P L O T S
##
##
plot_df = DataFrame(np.random.randn(1000,2),columns=['x','y'])

