'''
https://stackoverflow.com/questions/32303666/plot-multiple-y-values-against-one-x-values-in-python
'''

from numpy import *
from matplotlib import pyplot as plt

ys = [1.00, 
[(1.99-2.27e-17j),(0.61+9.08e-17j), (0.12-0j)], 
[(1.9+4.54e-17j), (0.61-9.081e-17j), (0.12+4.54e-17j)], 
[(1.99+4.5e-17j), (0.61-9.08e-17j), (0.12+4.54e-17j)], 
[(1.99-2.27e-17j), (0.61+9.0e-17j), (0.12-0j)], 
3.00]

xs = array([ 0. ,  0.2,  0.4,  0.6,  0.8,  1. ])

pxs = []
pys = []
for i, yelems in enumerate(ys):
    x = xs[i]
    try:
        for yelem in yelems:
            pxs.append(x)
            pys.append(yelem.real)
    except TypeError:
        pxs.append(x)
        pys.append(yelems)

plt.plot(pxs, pys)
plt.scatter(pxs, pys)
plt.show()

