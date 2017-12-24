import numpy as np
import matplotlib.pyplot as plt
import matplotlib.pyplot as plt
import numpy as np
from numpy import ma
from matplotlib import colors, ticker, cm
from matplotlib.mlab import bivariate_normal
from astropy.io import ascii
from matplotlib.colors import LogNorm
from matplotlib.colors import BoundaryNorm
from matplotlib.ticker import MaxNLocator


filename_red  = 'k2d_output_Red.dat'
red           = ascii.read(filename_red)
sigma_red     = red['col1']
pi_red        = red['col2']
xisp_red      = red['col5']
xisp_ham_red  = red['col10']
xisp_ls_red   = red['col11']

filename_blue = 'k2d_output_Blue.dat'
blue          = ascii.read(filename_blue)
sigma_blue    = blue['col1']
pi_blue       = blue['col2']
xisp_blue     = blue['col5']
xisp_ham_blue = blue['col10']
xisp_ls_blue  = blue['col11']

# Spirals 
filename_Sp   = 'k2d_output_Sp.dat'
Sp            = ascii.read(filename_Sp)
sigma_Sp      = Sp['col1']
pi_Sp         = Sp['col2']
xisp_Sp       = Sp['col5']
xisp_ham_Sp   = Sp['col10']
xisp_ls_Sp    = Sp['col11']

# Early Types
filename_ET   = 'k2d_output_ET.dat'
ET            = ascii.read(filename_ET)
sigma_ET      = ET['col1']
pi_ET         = ET['col2']
xisp_ET       = ET['col5']
xisp_ham_ET   = ET['col10']
xisp_ls_ET    = ET['col11']

####   R  E  D   ####
sigma_red = np.array(sigma_red)
pi_red = np.array(pi_red)
#xx, yy = np.meshgrid(x, y)
xisp_red = (np.array(xisp_red)+1)

X_red = np.array(sigma_red).reshape(17, 17).T
Y_red = np.array(pi_red).reshape(17, 17).T
Z_red = np.array(xisp_red).reshape(17, 17).T
Z_red = ma.masked_where(Z_red <= 0, Z_red)

X_red = np.log10(X_red)
Y_red = np.log10(Y_red)
#Z_red = np.log10(Z_red)


####   B L U E   ####
sigma_blue = np.array(sigma_blue)
pi_blue = np.array(pi_blue)
#xx, yy = np.meshgrid(x, y)
xisp_blue = (np.array(xisp_blue)+1)

X_blue = np.array(sigma_blue).reshape(17, 17).T
Y_blue = np.array(pi_blue).reshape(17, 17).T
Z_blue = np.array(xisp_blue).reshape(17, 17).T
Z_blue = ma.masked_where(Z_blue <= 0, Z_blue)

X_blue = np.log10(X_blue)
Y_blue = np.log10(Y_blue)
#Z_blue = np.log10(Z_blue)


####  S P I R A L    ####
sigma_Sp = np.array(sigma_Sp)
pi_Sp = np.array(pi_Sp)
#xx, yy = np.meshgrid(x, y)
xisp_Sp = (np.array(xisp_Sp)+1)

X_Sp = np.array(sigma_Sp).reshape(17, 17).T
Y_Sp = np.array(pi_Sp).reshape(17, 17).T
Z_Sp = np.array(xisp_Sp).reshape(17, 17).T
Z_Sp = ma.masked_where(Z_Sp <= 0, Z_Sp)

X_Sp = np.log10(X_Sp)
Y_Sp = np.log10(Y_Sp)
#Z_Sp = np.log10(Z_Sp)


####   E A R L Y     T Y P E    ####
sigma_ET = np.array(sigma_ET)
pi_ET = np.array(pi_ET)
#xx, yy = np.meshgrid(x, y)
xisp_ET = (np.array(xisp_ET)+1)

X_ET = np.array(sigma_ET).reshape(17, 17).T
Y_ET = np.array(pi_ET).reshape(17, 17).T
Z_ET = np.array(xisp_ET).reshape(17, 17).T
Z_ET = ma.masked_where(Z_ET <= 0, Z_ET)

X_ET = np.log10(X_ET)
Y_ET = np.log10(Y_ET)
#Z_ET = np.log10(Z_ET)

#lvls = np.logspace(-4,0,20)
# x and y are bounds, so z should be the value *inside* those bounds.
# Therefore, remove the last value from the z array.
#z = z[:-1, :-1]
levels_red = MaxNLocator(nbins=15).tick_values(Z_red.min(), Z_red.max())

# pick the desired colormap, sensible levels, and define a normalization
# instance which takes data values and translates those into levels.
cmap = plt.get_cmap('PiYG')
norm = BoundaryNorm(levels_red, ncolors=cmap.N, clip=True)


print( '    len , shape(X), type(X) ')
#print('X',  len(X), X.shape(), type(X))
print('X', len(X_red),  X_red.shape, type(X_red))
print('Y', len(Y_red),  Y_red.shape, type(Y_red))
print('Z', len(Z_red),  Z_red.shape, type(Z_red))

#fig, ((ax1, ax2), (ax3, ax4)) = plt.subplots(2,2, sharex=True, sharey=True)
fig, ((ax1, ax2), (ax3, ax4)) = plt.subplots(2,2)

fig.subplots_adjust(hspace=0)
fig.subplots_adjust(wspace=0)

xmin = -1.1
xmax =  1.30    ## log10(45.)) = 1.65;  log10(30.))=1.477;  log10(20.))=1.301
ymin = -1.1
ymax =  1.30
cmap = 'gist_rainbow'

ll = np.logspace( 0.001,  2.60, 124)
#lll = np.logspace(0.00001, 2.3, 24)
#ll = ['1.00230524', '1.4047531',  '1.96879274',  '2.75930686',    '3.86722998','5.4200089',     '7.59626313',   '10.64633187',   '14.92107111',   '20.9122133', '29.30893245',   '41.07712126',   '57.57049982',   '80.68633704',  '113.08369745', '158.48931925']

#r = np.linspace(0.1, 200, 10)
#s = (r/5.)**(-1.8)
#reversed_s = s[::-1]

n=0.1875
clevels =[n, 2*n, 4*n, 8*n,16*n,32*n, 64*n, 128*n, 256*n]
## Top left
ax1.set_xlim(xmax, xmin)
ax1.set_ylim(ymin, ymax)
CS1 = ax1.contourf(X_red, Y_red, Z_red,         levels=ll,                   cmap=cmap)
CS1 = ax1.contour(X_red, Y_red, Z_red, colors='k',   levels=clevels)
ax1.clabel(CS1, inline=1, fontsize=10)
ax1.spines['bottom'].set_visible(False)
ax1.spines['right'].set_visible(False)
ax1.set_xticklabels([])
ax1.set_xticks([])


## Top right
ax2.set_xlim(xmin, xmax)
ax2.set_ylim(ymin, ymax)
CS2 = ax2.contourf(X_blue, Y_blue, Z_blue, levels=ll,cmap=cmap)
CS2 = ax2.contour(X_blue, Y_blue, Z_blue, colors='k', levels=clevels)
#ax2.clabel(CS2, inline=1, fontsize=10)
ax2.spines['left'].set_visible(False)
ax2.spines['bottom'].set_visible(False)
ax2.set_xticklabels([])
ax2.set_yticklabels([])
ax2.set_xticks([])
ax2.set_yticks([])
ax2.set_yticklabels([])


## bottom left
ax3.set_xlim( xmax, xmin)
ax3.set_ylim( ymax, ymin)
CS3 = ax3.contourf(X_Sp, Y_Sp, Z_Sp, levels=ll, cmap=cmap)
CS3 = ax3.contour(X_Sp, Y_Sp, Z_Sp, colors='k', levels=clevels)
#ax3.clabel(CS3, inline=1, fontsize=10)
ax3.spines['right'].set_visible(False)
ax3.spines['top'].set_visible(False)


## bottom, right
ax4.set_xlim( xmin,xmax)
ax4.set_ylim( ymax, ymin)
CS4 = ax4.contourf(X_ET, Y_ET, Z_ET, levels=ll, cmap=cmap)
CS4 = ax4.contour(X_ET, Y_ET, Z_ET, colors='k', levels=clevels)
#ax2.clabel(CS2, inline=1, fontsize=10)
ax4.spines['left'].set_visible(False)
ax4.spines['top'].set_visible(False)
#ax4.set_xticklabels([])
#ax4.set_xticks([])
ax4.set_yticks([])
ax4.set_yticklabels([])



plt.show()
