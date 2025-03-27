# -*- coding: utf-8 -*-
"""
Created on Thu Mar 13 03:32:30 2025

@author: menah
"""

sequence = [10, 20, 30, 40, 50, 60]
even_sum = 0
odd_sum = 0
for s in range(len(sequence)):
    if s % 2 == 0 :
        even_sum+= sequence[s]
    else:
        odd_sum += sequence[s]

print(f" The sum of evens is: {even_sum}, and the sum of odds is: {odd_sum} .")