

from astropy.io import fits
from astropy.table import Table

hdulist = fits.open('tractor-0298p005.fits')

data = fits.getdata('tractor-0298p005.fits',1)
T = Table(data)

print(T)
print(T['decam_apflux'])

i = np.argmin(np.hypot(T['ra'] - 29.9901, T['dec'] - 0.5530))
print(T['ra'][i], T['dec'][i])

# We have fluxes in "nanomaggies" -- flux with zeropoint 22.5:
print(T['decam_flux'][i])
print(T['decam_apflux'][i])

# these are arrays, [u,g,r,i,z,Y], where only g,r,z are filled.

# For mags:
print(-2.5 * (np.log10(T['decam_flux'][i]) - 9))
