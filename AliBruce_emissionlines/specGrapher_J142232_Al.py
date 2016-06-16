import glob
import numpy as np
import matplotlib
matplotlib.rcParams.update({'text.usetex':True, 'font.family':'serif', 'axes.linewidth': 0.5, 'font.size':8})
from matplotlib import pyplot as plt
from scipy.signal import medfilt

dataPath = '../profileFitter/residuals/'
target = 'J142232_UV_line'
tfiles = glob.glob(dataPath+target+'*')
tfiles.sort()

f, ((ax1, ax2)) = plt.subplots(1, 2, sharey='row', figsize=(3,2))
colours = ['#aaaaff','#8888ff','#6666ff','#4444ff','#2222ff','#0000ff']
kernels = [31]*6
for i in range(len(tfiles)):
	data = np.genfromtxt(tfiles[i])
	ax1.plot(data[:,0], medfilt(data[:,1], kernel_size=kernels[i])/10**-17, linewidth=0.5, color=colours[i])
	ax2.plot(data[:,0], medfilt(data[:,1], kernel_size=kernels[i])/10**-17, linewidth=0.5, color=colours[i])

CIVmid  = 3210
CIIImid = 3960
MgIImid = 5820
ax1.set_xlim(CIIImid-200,CIIImid+200)
ax2.set_xlim(MgIImid-200,MgIImid+200)
ax1.set_ylim(-0.5,5)
ax1.locator_params(axis='x',nbins=6)
ax2.locator_params(axis='x',nbins=6)

f.text(0.46,0.82,'CIII]',ha='right',va='center')
f.text(0.88,0.82,'MgII',ha='right',va='center')
f.text(0.5,0.029,r'$\lambda$ (\AA)',ha='center',va='center')
f.text(0.023,0.5,r'F$_\lambda$ ($\times10^{-17}$\,erg\,s$^{-1}$\,cm$^{-2}$\,\AA$^{-1}$)',ha='center',va='center',rotation='vertical')
f.text(0.5,0.96,'J142232',ha='center',va='center')

plt.tight_layout(pad=1.4,h_pad=0.4)
f.subplots_adjust(hspace=0,wspace=0)
plt.savefig(target+'.eps',dpi=300)
