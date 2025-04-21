# -*- coding: utf-8 -*-
"""
Created on Mon Apr 21 17:47:15 2025

@author: menah
"""

import numpy as np

# 14. Basic operations
a = np.arange(100).reshape(-1, 10)
print(a + 1)
print(a - 1)
print(a * 2)
print(a / 2)
print(a ** 2)

print("\n" + "="*45 + "\n")

# 15. Comparisons
print(a > 50)
print(a < 50)
print(a >= 50)

print("\n" + "="*45 + "\n")

# 16. Array operations
a = np.array([1, 2, 3])
b = np.array([4, 5, 6])
print(a + b)
print(a - b)
print(a * b)
print(a / b)

print("\n" + "="*45 + "\n")

# 17. Array comparisons
print(a > b)
print(a < b)
print(a >= b)