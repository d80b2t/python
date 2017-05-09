from astropy.table import Table
import fitsio
import time
import timeit
import pyfits

## Could also use
https://docs.python.org/2/library/timeit.html

start_time = time.time()

##  5.4G  survey-dr3-specObj-dr13.fits
fname_decals = '/cos_pc19a_npr/data/DECaLS/legacysurvey/dr3/external/survey-dr3-specObj-dr13.fits'


columns = ['OBJID']
timeit.timeit('str = fitsio.read(fname_decals, columns=columns), number=10)
timeit.timeit('str = Table.read('fname_decals', columns=columns), number=10)
timeit.timeit('fx = pyfits.open(fname_decals, memmap=True)', number=10


print("--- %s seconds ---" % (time.time() - start_time))

