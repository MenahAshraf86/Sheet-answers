# -*- coding: utf-8 -*-
"""
Created on Sun Apr 13 20:09:47 2025

@author: menah
"""

def modlist(lst):
    for i in range(len(lst)):
        lst[i] = 10 * lst[i]

def modvar(num):
    num += 10

lst = [1, 2, 3]
modlist(lst)
print(lst)

x = 0
modvar(x) 
print(x)