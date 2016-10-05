

from astropy.io import fits
from astropy.table import Table
from astropy.coordinates import SkyCoord
from astropy import units as u

from astropy.io import fits as pyfits


hdulist = fits.open('tractor-0298p005.fits')

data = fits.getdata('tractor-0298p005.fits',1)
T = Table(data)

print(T)
print(T['decam_apflux'])

i = np.argmin(np.hypot(T['ra'] - 29.9901, T['dec'] - 0.5530))
print(T['ra'][i], T['dec'][i])


c = SkyCoord(ra=T['ra'][i]*u.degree, dec=T['dec'][i]*u.degree)
print(c.to_string('hmsdms'))



## We have fluxes in "nanomaggies" -- flux with zeropoint 22.5:
print(T['decam_flux'][i])
print(T['decam_apflux'][i])

## these are arrays, [u,g,r,i,z,Y], where only g,r,z are filled.
## For mags:
print(-2.5 * (np.log10(T['decam_flux'][i]) - 9))


## Yeah, so we do have WISE_LC_FLUX, which are WISE light curves -- we made coadds of the ~10 exposures per visit to each part of the sky, roughly one visit per six months.  These are only for the WISE W1 and W2 bands, because they're the only ones still active.
#T['wise_lc_flux'][i,:,:]
T['wise_lc_flux'][i]

print(-2.5 * (np.log10(T['wise_lc_flux'][i]) - 9))


## Inverse variances...
T['wise_lc_flux_ivar'][i]

## The standard deviation is the square root of the variance.
## sigma is Std dev; sigma^2 is variance.
1./((T['wise_lc_flux_ivar'][i])*2)

