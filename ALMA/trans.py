#!/usr/bin/python
import sys
import numpy as np

def find_nearest(array,value):
    idx = (np.abs(array-value)).argmin()
    return idx

if __name__ == "__main__":
	if len(sys.argv)==1:
		print 'sky transmission at ALMA site'
		print
		print 'trans.py 850 microns (or um or micron)'
		print 'trans.py 350 GHz'
		print
		print 'assumes 1mm pwv'
		exit(0)
	w = float(sys.argv[1])
	unit = sys.argv[2]
	lines = open('alma-0-2000-1.dat').readlines()
	nu = np.array([float(l.split()[0]) for l in lines])
	if unit=='GHz': 
		idx = find_nearest(nu,w)
		print 'Transmission at %.3f %s = %s'%(w,unit,lines[idx].split()[1])
	elif (unit=='um' or unit=='micron' or unit=='microns'):
		wl = 3.e14/(1.e9*nu)
		idx = find_nearest(wl,w)
		print 'Transmission at %.3f %s = %s'%(w,unit,lines[idx].split()[1])

