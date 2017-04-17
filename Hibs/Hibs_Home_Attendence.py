'''
Data from::
http://www.fitbastats.com/hibs/club_records_league_attendance.php

Code from:
https://matplotlib.org/examples/api/date_demo.html

Inspiration from:
The Chief.

http://space.mit.edu/home/turnerm/python.html

'''
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

## Data in...
data = pd.read_html('/cos_pc19a_npr/data/Hibs/Hibs_Home_Attendences_justNums_wWW2.dat', header=0)[0]
data.head()

#plt.style.use('fivethirtyeight')

#f, ax = plt.subplots()
#plt.figure()

figsize=(12, 6)
fontsize=16.
leg='Average for Home League Games'

data.index.name ='xlabel'
data.plot('Season','Average Attendance',
          figsize=figsize, fontsize=fontsize*0.9, style='go-',
          label=leg, linewidth=4, markersize=14)

plt.xlabel('Season', fontsize=fontsize)
plt.ylabel('Attendance',fontsize=fontsize)
#ax.set_xlabel("Season", fontsize=fontsize)
#ax.set_ylabel("Attendance", fontsize=fontsize)

plt.legend(prop={'size':fontsize*0.8}, markerfirst=False)

plt.gca().invert_xaxis()
plt.show()


