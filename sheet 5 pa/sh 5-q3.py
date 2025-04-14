# -*- coding: utf-8 -*-
"""
Created on Sun Apr 13 20:01:27 2025

@author: menah
"""

"""

def apply(lst, fn):
    result = []
    for elem in lst:
        result.append(fn(elem))
    return result

def add_1(num):
    return num + 1

r = apply([1, 2, 3], add_1)
print(r) ,,,, output : [2, 3, 4]

"""

def add_1(num):
    return num + 1

r = list(map(add_1, [1, 2, 3]))  
print(r)

