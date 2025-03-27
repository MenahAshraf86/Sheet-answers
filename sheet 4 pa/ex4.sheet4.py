# -*- coding: utf-8 -*-
"""
Created on Thu Mar 27 03:56:32 2025

@author: menah
"""

def average(*numbers):
 total = 0.0
 count = 0
 for num in numbers:
        total += num
        count += 1
 return total / count
AVG=average(50, 60, 70)
print( "Average of 50, 60, 70 is: ", AVG)