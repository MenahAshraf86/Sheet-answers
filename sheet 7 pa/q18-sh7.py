# -*- coding: utf-8 -*-
"""
Created on Mon Apr 21 17:58:03 2025

@author: menah
"""

import numpy as np

a = np.array([1,2,3]).reshape(3,1)
b = np.array([4,5,6]).reshape(1,3)

print(a + b)

"""
Output:
[[5 6 7]
 [6 7 8]
 [7 8 9]]

"""