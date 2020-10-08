# -*- coding: utf-8 -*-
"""
Created on Thu Oct  8 10:30:55 2020

@author: 15025
"""


import matplotlib
import matplotlib.pyplot as plt


class SaveFigureWithoutGui:
    def mainProgram(self):
        # set non-GUI backend
        matplotlib.use('Agg')
        
        # set plot style, if not, everytime it will use random color to show result
        plt.style.use('fivethirtyeight')
        
        # draw figure
        plt.plot([1,2,3])
        
        # save figure, default format is png
        plt.savefig('C:/Users/15025/Desktop/myfig')
        
    
if __name__ == '__main__':
    main = SaveFigureWithoutGui()
    main.mainProgram()