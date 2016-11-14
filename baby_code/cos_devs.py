import numpy as np
from matplotlib import pyplot as plt
from scipy import stats
# We'll use this to make some random distributions for examples


x = np.linspace(-2*np.pi,2*np.pi,500)
signal = np.cos(x)
noise = stats.norm().rvs(signal.shape)
# Gets random deviates with a Gaussian distribution


plt.plot(x,signal,label='cos(x)',linewidth=2)
# Setting the linewidth as well as the label

plt.scatter(x,signal+noise,label='random deviates',c=np.abs(noise),alpha=0.5)
# Setting color and transparency

plt.colorbar(label='residual')
plt.ylim(-5,5)
plt.legend()
