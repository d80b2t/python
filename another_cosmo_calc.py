#!/usr/bin/env python

"""
http://code.google.com/p/esutil/
"""

import esutil
c=esutil.cosmology.Cosmo()

# comoving distance to z=0.5
print c.Dc(0.0, 0.5) 

# angular diameter distance between z=0.5 and z=0.9
c.Da(0.5, 0.9)

# luminosity distance between z=0.2 and a sequence of redshifts
c.Dl(0.2, [0.3, 0.4, 0.5])

# new cosmology
#c=cosmology.Cosmo(H0=70.0, omega_m=0.25)
c=esutil.cosmology.Cosmo(H0=70.0, omega_m=0.25)

# inverse critical density for lensing, lens at 0.2 and
# source at 0.3
c.sigmacritinv(0.2, 0.3)

"""
import cosmology
cosmology.test()
"""
    


