# -*- coding: utf-8 -*-
"""
Created on Tue Feb 15 11:14:53 2022

@author: rdepa
"""

import csv
import matplotlib


def readEnvironment():
    environment = []
    with open('raster_grid.txt', newline='') as f:
        csv_reader = csv.reader(f, quoting=csv.QUOTE_NONNUMERIC)
        for row in csv_reader:
            rowlist = []
            for value in row:
                rowlist.append(value)
                #print(value) 
            environment.append(rowlist)
    return environment
        
#     matplotlib.pyplot.imshow(environment)
#     matplotlib.pyplot.show()
# readEnvironment()

