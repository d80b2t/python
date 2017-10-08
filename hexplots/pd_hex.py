'''
https://pandas.pydata.org/pandas-docs/version/0.18.1/visualization.html
https://pandas.pydata.org/pandas-docs/version/0.20.1/visualization.html
Hexagonal Bin Plot
'''

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd


df = pd.DataFrame(np.random.randn(1000, 2), columns=['a', 'b'])

df['b'] = df['b'] + np.arange(1000)
## This line below is from the above URLs,
## but doesn't make a tonne of sense to me. 
#df['b'] = df['b'] = df['b'] + np.arange(1000)


df['z'] = np.random.uniform(0, 3, 1000)

#df.plot.hexbin(x='a', y='b', gridsize=25)
df.plot.hexbin(x='a', y='b', C='z', reduce_C_function=np.max, gridsize=25)

plt.show()
