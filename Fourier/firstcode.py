'''
https://docs.scipy.org/doc/scipy/reference/tutorial/fftpack.html
'''

import numpy as np
import matplotlib.pyplot as plt
import scipy.fftpack

# Number of samplepoints
N = 1600
# sample spacing
T = 1.0 / 800.0

## np.linspace(start,stop,number)
x = np.linspace(0.0, N*T, N)
y = np.sin(50.0 * 2.0*np.pi*x) + 0.5*np.sin(80.0 * 2.0*np.pi*x)
#y = np.sin(5.0 * 2.0*np.pi*x) + 0.5*np.sin(8.0 * 2.0*np.pi*x)
yf = scipy.fftpack.fft(y)
xf = np.linspace(0.0, 1.0/(2.0*T), N/2)


#fig, ax = plt.subplots()
fig = plt.figure(figsize=(18, 4)) 

plt.subplot(1, 2,1)
plt.plot(x, y)
plt.subplot(1, 2,2)

plt.xlim(0.0, 100.0)
plt.plot(xf, 2.0/N * np.abs(yf[:N//2]))
plt.show()
