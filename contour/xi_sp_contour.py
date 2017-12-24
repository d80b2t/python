'''
Demonstrate use of a log color scale in contourf
'''

import matplotlib.pyplot as plt
import numpy as np
from numpy import ma
from matplotlib import colors, ticker, cm
from matplotlib.mlab import bivariate_normal
from astropy.io import ascii

#path     = '/cos_pc19a_npr/programs/GZ/OP/Red/'
#inputfile = path+filename


# Red
filename_red = 'k2d_output_Red.dat'
red          = ascii.read(filename_red)
sigma_red    = red['col1']
pi_red       = red['col2']
xisp_red     = red['col5']
xisp_ham_red = red['col10']
xisp_ls_red  = red['col11']

# Blue
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
filename_ET = 'k2d_output_ET.dat'
ET          =  ascii.read(filename_ET)
sigma_ET    = ET['col1']
pi_ET       = ET['col2']
xisp_ET     = ET['col5']
xisp_ham_ET = ET['col10']
xisp_ls_ET  = ET['col11']

xvec = xi_red
yvec = sigma_red
x, y = np.meshgrid(xvec, yvec)
A = np.array(xisp_red)
B = np.reshape(A, (17,17))
Z = B

z = np.meshgrip(xisp_red, xisp_red)

plt.figure()
CS = plt.contour(X, Y, Z)
plt.clabel(CS, inline=1, fontsize=10)
plt.title('Simplest default with labels')

   
#X, Y = np.meshgrid(xi, sigma)

## A low hump with a spike coming out of the top right.
## Needs to have z/colour axis on a log scale so we see both hump and spike.
## linear scale only shows the spike.
#z = (bivariate_normal(X, Y, 0.1, 0.2, 1.0, 1.0)      + 0.1 * bivariate_normal(X, Y, 1.0, 1.0, 0.0, 0.0))

# Put in some negative values (lower left corner) to cause trouble with logs:
#z[:5, :5] = -1

# The following is not strictly essential, but it will eliminate
# a warning.  Comment it out to see the warning.
#z = ma.masked_where(z <= 0, z)


# Automatic selection of levels works; setting the
# log locator tells contourf to use a log scale:
fig, ax = plt.subplots()
f, ax = plt.subplots(2,2, sharex=True, sharey=True)


## https://stackoverflow.com/questions/38747311/how-to-create-a-symmetric-matrix-from-a-numpy-1d-array-the-most-efficient-way
## https://stackoverflow.com/questions/13781025/matplotlib-contour-from-xyz-data-griddata-invalid-index

#fig, ax = plt.subplots(1,2, sharex=True, sharey=True)
#
cs = ax.contourf(X, Y, xisp, locator=ticker.LogLocator(), cmap=cm.PuBu_r)


ax[0].tricontourf(xi_red,  sigma_red,  xisp_red, 20)
ax[1].tricontourf(xi_blue, sigma_blue, xisp_blue, 20)
ax[2].tricontourf(xi_ET,   sigma_ET,   xisp_ET, 20)
ax[3].tricontourf(xi_Sp,   sigma_Sp,   xisp_SP, 20)

# Alternatively, you can manually set the levels
# and the norm:
#lev_exp = np.arange(np.floor(np.log10(z.min())-1),
#                    np.ceil(np.log10(z.max())+1))
#levs = np.power(10, lev_exp)
#cs = P.contourf(X, Y, z, levs, norm=colors.LogNorm())

# The 'extend' kwarg does not work yet with a log scale.

#cbar = fig.colorbar(cs)

plt.show()
