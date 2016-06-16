import glob
import numpy as np
import matplotlib
matplotlib.rcParams.update({'text.usetex':True, 'font.family':'serif', 'axes.linewidth': 0.5, 'font.size':8})
from matplotlib import pyplot as plt
from scipy.signal import medfilt

dataPath = '../profileFitter/fits/'
target = 'J142232_UV_best'
tfiles = glob.glob(dataPath+target+'*')
tfiles.sort()

f, ((ax1)) = plt.subplots(1, 1, figsize=(3,2))
colours = ['#aaaaff','#8888ff','#6666ff','#4444ff','#2222ff','#0000ff']
kernels = [31]*6
data = np.genfromtxt(tfiles[3])
ax1.plot(data[:,0], data[:,1]/10**-17, linewidth=0.5, color=colours[-1])

CIVmid  = 3210
CIIImid = 3960
MgIImid = 5820
ax1.set_xlim(4250,5950)
ax1.set_ylim(0,5)
ax1.locator_params(axis='x',nbins=6)

ax1.axhline(4, xmin=4500, xmax=5000)
ax1.annotate('MgII', xy=(5193.5,3.2), xytext=(5193.5,4), horizontalalignment='center', arrowprops=dict(shrink=0.12, width=0.1, headwidth=2.5, color='r'), color='r')
ax1.annotate('FeII', xy=(4811,3.2), xytext=(4811,4), horizontalalignment='center', arrowprops=dict(shrink=0.12, width=0.01, headwidth=2.5, color='r'), color='r')
ax1.annotate('FeII', xy=(4391,3.3), xytext=(4391,4), horizontalalignment='center', arrowprops=dict(shrink=0.12, width=0.01, headwidth=2.5, color='r'), color='r')
f.text(0.92,0.82,'MgII',ha='right',va='center', color='b')
f.text(0.5,0.029,r'$\lambda$ (\AA)',ha='center',va='center')
f.text(0.023,0.5,r'F$_\lambda$ ($\times10^{-17}$\,erg\,s$^{-1}$\,cm$^{-2}$\,\AA$^{-1}$)',ha='center',va='center',rotation='vertical')
f.text(0.5,0.96,'J142232',ha='center',va='center')

plt.tight_layout(pad=1.4,h_pad=0.4)
f.subplots_adjust(hspace=0,wspace=0)
plt.savefig(target+'_abs.eps',dpi=300)
