

#u  0.04438   -2.26095  -0.13387   0.27099 
#g -0.01808   -0.13595   0.01941  -0.00183 
#r -0.01836   -0.03577   0.02612  -0.00558
#i  0.01170   -0.00400   0.00066  -0.00058
#z -0.01062   -0.03577   0.02612   0.00890
#y  0.08924   -0.00400   0.00066  -0.02441

import numpy as np
import matplotlib.pyplot as plt

a0 = np.array([ 0.04438, -0.01808, -0.01836,  0.01170, -0.01062, -0.01062])
a1 = np.array([-2.26095, -0.13595, -0.03577, -0.00400, -0.03577, -0.00400])
a2 = np.array([-0.13387,  0.01941,  0.02612,  0.00066,  0.02612,  0.00066])
a3 = np.array([ 0.00066, -0.00183, -0.00558, -0.00558,  0.00890,  0.00890])

## x = (g_ps1 - i_ps1)

## They are valid for main-sequence stars with 0.4 < x < 2.7.
## Coefficients are provided for gP1 - usdss and yP1 - zsdss for completeness.
x_max = 2.80
x_min = 0.30
diff  = 0.01


x      = np.arange(x_min,x_max,diff)
xs     = np.power.outer(x,range(4))
coeffs = np.vstack((a0,a1,a2,a3))
curves = np.dot(xs,coeffs)

plt.plot(x,curves)

plt.savefig('BM_plot_temp.png', format='png')
plt.show()


