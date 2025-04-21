# -*- coding: utf-8 -*-
"""
Created on Mon Apr 21 17:25:44 2025

@author: menah
"""

import numpy as np

my_arr = np.arange(100)  
new_shape = my_arr.reshape(4, -1)  
print(new_shape)

print("The new shape of reshaped array is: ", new_shape.shape)