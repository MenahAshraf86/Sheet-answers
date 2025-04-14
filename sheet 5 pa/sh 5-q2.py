# -*- coding: utf-8 -*-
"""
Created on Sun Apr 13 20:00:17 2025

@author: menah
"""

x_coor = [1, 2, 3, 4, 5]
y_coor = [2, 4, 6, 8, 10]
z_coor = [0, -1, -2, -3, -4]

points = [(x, y, z) for x, y, z in zip(x_coor, y_coor, z_coor)]
print(points)


"""
The Explaination:
    
1. Takes the first item from each sequence and combines them into a tuple
2. Takes the second item from each sequence and combines them into another tuple
3. Continues this process until any of the sequences is exhausted
"""