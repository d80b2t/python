#!/usr/bin/env python

"""
 http://oneau.wordpress.com/2011/02/28/simple-statistics-with-scipy/
 
 http://stackoverflow.com/questions/11725115/p-value-from-chi-sq-test-statistic-in-python
 http://stackoverflow.com/questions/9330114/chi-squared-test-in-python

 http://oneau.wordpress.com/2011/02/28/simple-statistics-with-scipy/
 
""" 

import numpy as np
import scipy as sp
from scipy import stats
from matplotlib import pyplot as plt
from scipy import interpolate

chisq_value = 1.
print "chi sq value", chisq_value

print chisq_value

"""
Basically, the 1.-stats.chi2.sf(chi2,nu) value is the confidence level.
e.g.: 1.-stats.chi2.sf(1.00, 1)
0.68268949213708596
"""

"""
http://en.wikipedia.org/wiki/Standard_deviation
z-sigma	Percentage within CI 	Percentage outside CI 	Fraction outside CI
1-sigma 	68.2689492% 	31.7310508% 	1 / 3.1514872
2-sigma 	95.4499736% 	4.5500264% 	1 / 21.977895
3-sigma 	99.7300204% 	0.2699796% 	1 / 370.398
4-sigma 	99.993666% 	0.006334% 	1 / 15,787
5-sigma 	99.9999426697% 	0.0000573303% 	1 / 1,744,278
"""

print "stats.chi2.sf(3.84, 1) ", stats.chi2.sf(3.84, 1)
print
print "stats.chi2.sf(181.4, 81) ", stats.chi2.sf(181.4, 81)
print "stats.chi2.sf(152.1, 72) ", stats.chi2.sf(152.1, 72)
