

#u  0.04438   -2.26095  -0.13387   0.27099 
#g -0.01808   -0.13595   0.01941  -0.00183 
#r -0.01836   -0.03577   0.02612  -0.00558
#i  0.01170   -0.00400   0.00066  -0.00058
#z -0.01062   -0.03577   0.02612   0.00890
#y  0.08924   -0.00400   0.00066  -0.02441

import numpy as np

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

y = int(((x_max - x_min)/diff))
m_diff = np.zeros((y,6))

xmin = int(x_min * 100)
xmax = int(x_max * 100)
di   = int(diff  * 100)

for xx in range(xmin, xmax, di):
    x = xx*diff
    m_diff[xx] = a0 + (a1*x) + (a2*x*x) + (a3*x*x*x)


