from astropy.table import Table
from astropy.io import fits
import fitsio
import time
import timeit
import pyfits

## Can also use::
## https://docs.python.org/2/library/timeit.html

start_time = time.time()

##  5.4G  survey-dr3-specObj-dr13.fits
fname_decals = '/cos_pc19a_npr/data/DECaLS/legacysurvey/dr3/external/survey-dr3-specObj-dr13.fits'

columns = ['OBJID']
#timeit.timeit('str = fitsio.read(fname_decals, columns=columns)', number=10)
#timeit.timeit('str = Table.read(fname_decals, columns=columns)', number=10)
#timeit.timeit('fx = pyfits.open(fname_decals, memmap=True)', number=10)

#str = fitsio.read(fname_decals, columns=columns)
#str = Table.read(fname_decals, columns=columns)
str = fits.open(fname_decals,colums=columns)
#str = pyfits.open(fname_decals, memmap=True)

print("--- %s seconds ---" % (time.time() - start_time))

