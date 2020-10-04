# -*- coding: utf-8 -*-
"""
Created on Sun Oct  4 12:27:59 2020

@author: 15025
"""

import matplotlib.pyplot as plt
from matplotlib.collections import PatchCollection
from matplotlib.patches import Circle
from matplotlib.patches import Wedge
from matplotlib.patches import Polygon
from matplotlib.patches import Ellipse


class Patches:
    def extend(lst):
        for i in lst:
            ax.add_artist(i)
        

# background and canvas
color = r"#39CF18"
fig, ax = plt.subplots(figsize=[8, 8])
# do not display ticks of coordinate axis
plt.xticks([])
plt.yticks([])
ax.set_fc(color)
plt.xlim([0, 40])
plt.ylim([0, 40])

es1 = Ellipse([15, 24], width=21, height=18, facecolor="white", zorder=1)
es2 = Ellipse([26, 16], width=18, height=15, facecolor="white", linewidth=5, edgecolor=color, zorder=1)
Patches.extend([es1, es2])

c1 = Circle([11, 27], radius=1.3, facecolor=color, zorder=2)
c2 = Circle([19, 27], radius=1.3, facecolor=color, zorder=2)
c3 = Circle([23, 18], radius=1, facecolor=color, zorder=2)
c4 = Circle([29, 18], radius=1, facecolor=color, zorder=2)
Patches.extend([c1, c2, c3, c4])

w1 = Wedge([8, 13], r=7, theta1=40, theta2=80, facecolor="white", zorder=2)
w2 = Wedge([33.5, 8.5], r=7, theta1=110, theta2=140, facecolor="white", zorder=2)
Patches.extend([w1, w2])