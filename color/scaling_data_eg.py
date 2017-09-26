'''
http://research.endlessfernweh.com/colormaps/
"Scaling your data (rather than scaling the colormap)"

'''
from matplotlib import colors, cm, pyplot as plt
 
import numpy as np
 
y,x=np.mgrid[0:1,0:10:0.1]
z=x**(7)
zscale=z**(1/7.)
#For z=x^beta: beta=logz/logx.  Take the last data point for a quick & dirty estimate of beta.
#beta=np.log10(z[-1])/np.log10(x[-1])
 
plt.rc('text',usetex=True)
 
fig=plt.figure(1)
ax1=fig.add_subplot(2,1,1)
plt.imshow(z,cmap='jet')
plt.title('Original Data: z = x$^{\\beta}$')
ax1.axes.get_xaxis().set_visible(False); ax1.axes.get_yaxis().set_visible(False)
 
ax2=fig.add_subplot(2,1,2)
plt.imshow(zscale,cmap='jet')
plt.title('Scaled Data: $\\textrm{z}^{1/ \\beta} = {\\left( \\textrm{x}^{\\beta} \\right) }^{1/\\beta} $')
ax2.axes.get_xaxis().set_visible(False); ax2.axes.get_yaxis().set_visible(False)
 
plt.subplots_adjust(hspace=-.75)
plt.savefig('cmap_powerscaledata.png',bbox_inches='tight')
plt.show()
