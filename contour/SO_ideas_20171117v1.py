import numpy as np
import matplotlib.pyplot as plt
import matplotlib.pyplot as plt
import numpy as np
from numpy import ma
from matplotlib import colors, ticker, cm
from matplotlib.mlab import bivariate_normal
from astropy.io import ascii
from matplotlib.colors import LogNorm



filename_red = 'k2d_output_Red.dat'
red          = ascii.read(filename_red)
sigma_red    = red['col1']
pi_red       = red['col2']
xisp_red     = red['col5']
xisp_ham_red = red['col10']
xisp_ls_red  = red['col11']


x = np.array(sigma_red)
y = np.array(pi_red)
#xx, yy = np.meshgrid(x, y)
z = (np.array(xisp_red)+1)


X = np.array(x).reshape(17, 17).T
Y = np.array(y).reshape(17, 17).T
Z = np.array(z).reshape(17, 17).T

Z = ma.masked_where(Z <= 0, Z)

X = np.log10(X)
Y = np.log10(Y)
#Z = np.log10(Z)

lvls = np.logspace(-4,0,20)

print( '    len , shape(X), type(X) ')
#print('X',  len(X), X.shape(), type(X))
print('X', len(X),  X.shape, type(X))
print('Y', len(Y),  Y.shape, type(Y))
print('Z', len(Z),  Z.shape, type(Z))

fig, ((ax1, ax2), (ax3, ax4)) = plt.subplots(2,2, sharex=True, sharey=True)

fig.subplots_adjust(hspace=0)
fig.subplots_adjust(wspace=0)

CS1 = ax1.contour(X, Y, Z, colors='k')
ax1.clabel(CS1, inline=1, fontsize=10)

CS2 = ax2.contour(X, Y, Z, colors='r')
ax2.clabel(CS2, inline=1, fontsize=10)

CS3 = ax3.contour(X, Y, Z, colors='b')
ax3.clabel(CS1, inline=1, fontsize=10)

CS4 = ax4.contour(X, Y, Z, colors='g')
ax4.clabel(CS4, inline=1, fontsize=10)


#fig, ax = plt.subplots(2,2)
#ax[0].contour( X, Y, Z, cmap=plt.cm.jet, norm = LogNorm())
#ax.contourf(X, Y, Z, cmap=plt.cm.jet, norm = LogNorm())
#ax.contourf(X, Y, Z, cmap=plt.cm.jet, norm = LogNorm())
#ax.colorbar()
plt.show()

#plt.contourf(X, Y, Z, cmap=plt.cm.jet, norm = LogNorm())
#plt.show()

#fig, ax = plt.subplots()
#cs = ax.contourf(X, Y, Z, locator=ticker.LogLocator())
#cbar = fig.colorbar(cs)

#cbar = plt.colorbar(CF, ticks=lvls, format='%.4f')

#plt.contour(xx, yy, z)
#plt.show()

#fig = plt.figure()
#ax = fig.gca(projection='3d')
#ax.plot_surface(X=x,Y=y,Z=z)
#plt.show()
