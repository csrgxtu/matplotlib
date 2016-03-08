#!/usr/bin/env python

from pylab import *
import matplotlib.gridspec as gridspec
import matplotlib.image as mpimg

G = gridspec.GridSpec(1, 3)
# figure(figsize=(1,1))

# axes_1 = subplot(G[0, :])
# xticks([]), yticks([])
# text(0.5,0.5, 'Axes 1',ha='center',va='center',size=24,alpha=.5)
#
# axes_2 = subplot(G[1,:-1])
# xticks([]), yticks([])
# text(0.5,0.5, 'Axes 2',ha='center',va='center',size=24,alpha=.5)

# axes_3 = subplot(G[1:, -1])
# xticks([]), yticks([])
# text(0.5,0.5, 'Axes 3',ha='center',va='center',size=24,alpha=.5)

axes_4 = subplot(G[-1,0])
# xticks([]), yticks([])
# text(0.5,0.5, 'Axes 4',ha='center',va='center',size=24,alpha=.5)
img=mpimg.imread('test.png')
plt.axis("off")
plt.imshow(img)

axes_5 = subplot(G[-1,-2])
# xticks([]), yticks([])
img=mpimg.imread('test1.png')
plt.axis("off")
plt.imshow(img)
# text(0.5,0.5, 'Axes 5',ha='center',va='center',size=24,alpha=.5)

axes_6 = subplot(G[-1,-1])
# xticks([]), yticks([])
img=mpimg.imread('test2.png')
plt.axis("off")
plt.imshow(img)
# text(0.5,0.5, 'Axes 6',ha='center',va='center',size=24,alpha=.5)



#plt.savefig('../figures/gridspec.png', dpi=64)
show()
