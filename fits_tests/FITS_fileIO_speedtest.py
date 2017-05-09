from astropy.table import Table
import fitsio
import time
import pyfits

start_time = time.time()

##  5.4G  survey-dr3-specObj-dr13.fits
fname_decals = '/cos_pc19a_npr/data/DECaLS/legacysurvey/dr3/external/survey-dr3-specObj-dr13.fits'


columns = ['OBJID']
#str = fitsio.read(fname_decals, columns=columns)
#str = Table.read('fname_decals', columns=columns)
fx = pyfits.open(fname_decals, memmap=True)


print("--- %s seconds ---" % (time.time() - start_time))

