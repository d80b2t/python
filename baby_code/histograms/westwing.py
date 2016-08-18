
"""

Wanting to make histogram plots...

https://stanford.edu/~mwaskom/software/seaborn/tutorial/distributions.html

And since we're using this thing called seaborn, I really can't not 
use a West Wing reference... ;-) 

"""

## %matplotlib inline

import numpy as np
import pandas as pd
from scipy import stats, integrate
import matplotlib.pyplot as plt
import seaborn as sns

sns.set(color_codes=True)

np.random.seed(sum(map(ord, "distributions")))

"""
Plotting univariate distributions

The most convenient way to take a quick look at a univariate distribution in seaborn is the distplot() function. By default, this will draw a histogram and fit a kernel density estimate (KDE).

"""

x = np.random.normal(size=100)
sns.distplot(x);
