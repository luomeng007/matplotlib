# -*- coding: utf-8 -*-
"""
Created on Sat Sep  5 18:05:11 2020

@author: 15025

draw three figures with one common colorbar
"""

import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.axes_grid1 import ImageGrid


class Visualazation:
    def mainProgram(self):
        # Set up figure and image grid
        fig = plt.figure(figsize=(8, 4))
        
        grid = ImageGrid(fig, 111,
                          nrows_ncols=(1,3),
                          axes_pad=0.15,
                          share_all=True,
                          cbar_location="right",
                          cbar_mode="single",
                          cbar_size="7%",
                          cbar_pad=0.15,
                         )
        
        # Add data to image grid
        for ax in grid:
            im = ax.imshow(np.random.random((10,10)), vmin=0, vmax=1)
        
        # Colorbar
        ax.cax.colorbar(im)
        ax.cax.toggle_label(True)
        
        plt.show()
        

if __name__ == "__main__":
    main = Visualazation()
    main.mainProgram()