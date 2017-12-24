import numpy as np
import matplotlib.pyplot as plt
import matplotlib.pyplot as plt
import numpy as np
from numpy import ma
from matplotlib import colors, ticker, cm
from matplotlib.mlab import bivariate_normal
from astropy.io import ascii

filename_red = 'k2d_output_Red.dat'
red          = ascii.read(filename_red)
sigma_red    = red['col1']
pi_red       = red['col2']
xisp_red     = red['col5']
xisp_ham_red = red['col10']
xisp_ls_red  = red['col11']


x = np.array(sigma_red)
y = np.array(pi_red)
xx, yy = np.meshgrid(x, y)

plt.contour(xx, yy, z)
plt.show()
