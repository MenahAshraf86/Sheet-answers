# -*- coding: utf-8 -*-
"""
Created on Thu Mar 27 03:39:43 2025

@author: menah
"""

Names = ["Maryam", "Ashraf", "Amira", "Merna", "Ali"]
S = {letter  for name in Names for letter in name}
print("All letters used in family names is :", S)