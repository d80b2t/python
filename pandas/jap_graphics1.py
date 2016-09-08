import matplotlib.pyplot as plt

plt.rcParams['font.size'] = 12
plt.rcParams['axes.titlesize'] = 'medium'
plt.rcParams['axes.linewidth'] = 1.25
plt.rcParams['lines.linewidth'] = 1.25
#plt.rcParams['font.family'] = 'serif'



#Make axial ratios 1.23 : 1
plt.subplots_adjust(
left  = 0.22,  # the left side of the subplots of the figure
right = 0.78,    # the right side of the subplots of the figure
bottom = 0.2,   # the bottom of the subplots of the figure
top = 0.8,      # the top of the subplots of the figure
)

def jap_label(xlabel,ylabel,title):
    plt.xlabel(xlabel,labelpad=12)
    plt.ylabel(ylabel,labelpad=4)
    plt.title(title,y=1.03)

def jap_savefig(plotname):
    plt.savefig(plotname,bbox_inches='tight',pad_inches=0.1)
#    plt.clf()
