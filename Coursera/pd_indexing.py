"""

http://stackoverflow.com/questions/16683701/in-pandas-how-to-get-its-index-of-a-known-value

"""
import pandas as pd
import numpy as np

fv = pd.DataFrame(np.arange(10).reshape(5,2),columns=['c1','c2'])
fv

print()
print('fv.ix[0,1]', fv.ix[0,1], '\n')
print('fv.c2[0]', fv.c2[0], '\n')
print('fv.c2.ix[0]', fv.c2.ix[0], '\n')
a.c1[a.c1 == 8].index.tolist()


## http://stackoverflow.com/questions/12555323/adding-new-column-to-existing-dataframe-in-python-pandas
df1 = pd.DataFrame(np.random.randn(10, 4), columns=['a', 'b', 'c', 'd'])
mask = df1.applymap(lambda x: x <-0.7)
df1 = df1[-mask.any(axis=1)]
sLength = len(df1['a'])
e = Series(np.random.randn(sLength))
