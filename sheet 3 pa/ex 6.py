# -*- coding: utf-8 -*-
"""
Created on Thu Mar 13 03:38:54 2025

@author: menah
"""

The numbers = {}
while True:
    number_1 = int(input ("Enter a non-positive number " ))
    if number_1 <= 0:
        break
    numbers [number_1] = True
    
unique_numbers_1 = list (numbers_1.keys())
unique_pairs = [(unique_numbers_1 [X] , unique_numbers_1 [y])
               for x in range (len(unique_numbers_1))
               for y in range (x + 1, len (unique_numbers_1))]
print ("unique_numbers_1 is : ", unique_pairs)       