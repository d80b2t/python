
import numpy as np
import matplotlib.pyplot as plt

#from jap_graphics1_square import *
from jap_graphics1 import *

x = np.zeros(99)
y = np.zeros(99)
z = np.zeros(99)

# Open file
f = open('pay.dat', 'r')

# Loop over lines and extract variables of interest
n=0
for line in f:
    n=n+1
    line = line.strip()
    columns = line.split()
    a=float(columns[0])/1000.
    b=float(columns[1])/1000.
    y[n-1]=n
    x[n-1]=a*1.03


f.close()

plt.plot(x, y, 'bo')
plt.plot(x, y, 'b-')
jap_label('Gross annual income in kGBP','percentage point','2014-2015')

#jap_savefig('money.pdf')
plt.show()

for i in range(98):
    z[i]=np.log(x[i+1]/x[i])
#    x[i]=np.log10(x[i])
    y[i]=0.01/z[i]
#    print i, x[i], y[i], z[i]

xx=x[:-1]
yy=y[:-1]
zz=z[:-1]

plt.xlim(3.,300.)
plt.semilogx(xx, yy, 'bo')
plt.semilogx(xx, yy, 'b-')
jap_label('Gross annual income in kGBP','dp/d ln(income)','2014-2015')

#jap_savefig('money.pdf')                                                                                              
plt.show()

sum=0.
for i in range(98):
    rate=0.1/(1+(50./x[i])**2)
    sum=sum+x[i]*rate*0.01
    z[i]=sum

x[98]=200
z[98]=z[97]+1*rate

# 38 million working population. Scale to billions

z=z*38

plt.xlim(3.,300.)
plt.semilogx(x, z, 'bo')
plt.semilogx(x, z, 'b-')
jap_label('Gross annual income in kGBP','cumulative tax in Billion GBP','2014-2015')

#jap_savefig('money.pdf')                                                                                              
plt.show()


