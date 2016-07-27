
'''
Date: Wed, 27 Jul 2016 02:00:59 -0700
From: "John K. Parejko" <parejkoj@uw.edu>
To: Astronomical Python mailing list <astropy@scipy.org>
Subject: [AstroPy] matplotlib histograms and astropy quantites
'''

import numpy as np
from astropy import units as u
import matplotlib.pyplot as plt

range1 = (-3, 3)
range2 = range1*u.arcsecond
np.random.seed(100)
data = np.random.normal(scale=3e-6, size=100)*u.radian
plt.figure()

# Not well centered and wrong X scale.
plt.hist(data)
# Works: I guess I shouldn't be surprised that I have to extract a value here.
plt.axvline(x=data[0].value, color='red')
plt.figure()
# Wanted the range in arcseconds, so this isn't right!
plt.hist(data, range=range1)
# Dimensionalizing it seems to work correctly.
plt.axvline(x=data[0]/u.arcsecond, color='red')
plt.figure()
# UnitsError: Can only apply 'less_equal' function to dimensionless quantities...
plt.hist(data, range=range2)
# UnitsError: Can only apply 'greater' function to dimensionless quantities...
plt.axvline(x=data[0])
