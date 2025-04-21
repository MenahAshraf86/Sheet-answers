# -*- coding: utf-8 -*-
"""
Created on Mon Apr 21 17:21:05 2025

@author: menah
"""

import numpy as np
# Q6
my_arr_2d = np.arange(1, 10).reshape(3, 3)
print(my_arr_2d)

print("\n" + "="*45 + "\n")

# Q7
my_arr_1d = my_arr_2d.flatten()  
print(my_arr_1d)