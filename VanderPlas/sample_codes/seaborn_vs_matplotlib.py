"""
Python_Data_Science_Handbook
pp. 489,490
"""

import matplotlib.pyplot as plt

import seaborn as sns
import numpy as np
import pandas as pd


sns.set()y

# Create some data
rng = np.random.RandomState(0)
x = np.linspace(0, 10, 500)
y = np.cumsum(rng.randn(500, 6), 0)

plt.plot(x, y)
plt.legend('ABCDEF', ncol=2, loc='upper left');
