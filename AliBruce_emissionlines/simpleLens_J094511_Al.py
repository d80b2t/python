import numpy as np
import matplotlib
matplotlib.rcParams.update({'text.usetex':True, 'font.family':'serif', 'axes.linewidth': 0.5, 'font.size':8})
from matplotlib import pyplot as plt

# values from Chelsea's IDL script
D_s = 1521.3120 #Source angular diameter distance for z=0.758 (J094511) (Mpc)
D_d = 799.94244 #Lens angular diameter distance for z=0.25 (Mpc)
D_ds = 954.66823 #Source-lens angular diameter distance for z=0.758,0.25 (J094511) (Mpc)
M_l = 0.4 #Lens mass (solar masses)
v_T = 400 #Transverse velocity (km s^-1)
y_0 = 0.05 #Minimum source position in units of the Einstein radius

G = 6.674*10**-11 #m^3 kg^-1 s^-2
c = 2.998*10**8 #m s^-1
Mpc = 3.08568*10**22 #m
M_sun = 1.989*10**30 #kg

E = np.sqrt( ( 4*G*M_l*M_sun*D_ds )/( c**2*D_d*D_s*Mpc ) )
t_E = (D_d*Mpc*E)/(v_T*1000)

print 't_E:', np.round(t_E/3600/24/365.25,1), 'yrs'
print 'theta_E:', np.round((E*D_s*Mpc)/c/3600/24,1), 'light-days at source'

zero = 23.2 #22.251(J094511 SDSS)

t_0 = 55900
t = np.arange(t_0-3000,t_0+2000,10)
y_t = np.sqrt( y_0**2 + ((t-t_0)/(t_E/3600/24))**2 )
mu_t = (y_t**2+2)/(y_t*np.sqrt(y_t**2+4))
mu_t_mag = -2.5*np.log10(mu_t)+23.2

f, ((ax1)) = plt.subplots(1, 1, figsize=(3,2))

data = np.genfromtxt('./LTfiles/J094511/lc4_crts.txt')
ax1.errorbar(data[:,1], data[:,2]+0.3, data[:,3], color='#aaaaaa', linestyle='none', fmt='.', elinewidth=0.5, capsize=1, markersize=2)
ax1.plot(t, mu_t_mag, 'r', linewidth=0.5)
#data = np.genfromtxt('./LTfiles/J094511/lc4_dvo.txt')
#ax1.errorbar(data[:,1], data[:,2], data[:,3], color='c', linestyle='none', fmt='.', elinewidth=0.5, capsize=1, markersize=2)
data = np.genfromtxt('./LTfiles/J094511/lc4_fgss.txt')
ax1.errorbar(data[:,1], data[:,2], data[:,3], color='m', linestyle='none', fmt='.', elinewidth=0.5, capsize=1, markersize=2)
data = np.genfromtxt('./LTfiles/J094511/lc4_sdr9.txt')
ax1.errorbar(data[1], data[2], data[3], color='k', linestyle='none', fmt='.', elinewidth=0.5, capsize=1, markersize=2)
data = np.genfromtxt('./LTfiles/J094511/lc4.txt')
ax1.errorbar(data[:,1], data[:,2], data[:,3], color='b', linestyle='none', fmt='.', elinewidth=0.5, capsize=1, markersize=2)
ax1.invert_yaxis()
ax1.set_ylim(22.6,19.5)
ax1.set_xlim(53200,57400)
ax1.axhline(23.2, linestyle='dotted',linewidth=0.5, color='r')
f.text(0.5,0.3,'$t_E=$ '+str(np.round(t_E/3600/24/365.25,1))+' yr',ha='left',va='center')
f.text(0.5,0.029,'MJD',ha='center',va='center')
f.text(0.023,0.5,'g mag',ha='center',va='center',rotation='vertical')
f.text(0.5,0.96,'J094511',ha='center',va='center')
ax1.locator_params(axis='x',nbins=6)
plt.tight_layout(pad=1.4,h_pad=0.4)
f.subplots_adjust(hspace=0,wspace=0)
plt.savefig('J094511_mulens.eps',dpi=300)
