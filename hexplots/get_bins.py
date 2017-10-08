
import numpy as np
import math
import matplotlib.pyplot as plt

def generate_data(n):
    """Make random, correlated x & y arrays"""
    points = np.random.multivariate_normal(mean=(0,0),
        cov=[[0.4,9],[9,10]],size=int(n))
    return points

if __name__ =='__main__':

    color_map = plt.cm.Spectral_r
    n = 1e4
    points = generate_data(n)

    xbnds = np.array([-20.0,20.0])
    ybnds = np.array([-20.0,20.0])
    extent = [xbnds[0],xbnds[1],ybnds[0],ybnds[1]]

    fig=plt.figure(figsize=(10,9))
    ax = fig.add_subplot(111)
    x, y = points.T
    # Set gridsize just to make them visually large
    image = plt.hexbin(x,y,cmap=color_map,
                       gridsize=20,extent=extent,mincnt=1,bins='log')
    # Note that mincnt=1 adds 1 to each count
    counts = image.get_array()
    ncnts = np.count_nonzero(np.power(10,counts))
    verts = image.get_offsets()
    for offc in range(verts.shape[0]):
        binx,biny = verts[offc][0],verts[offc][1]
        if counts[offc]:
            plt.plot(binx,biny,'k.',zorder=100)
    ax.set_xlim(xbnds)
    ax.set_ylim(ybnds)
    plt.grid(True)
    cb = plt.colorbar(image,spacing='uniform',extend='max')
    plt.show()
