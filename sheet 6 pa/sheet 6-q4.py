# -*- coding: utf-8 -*-
"""
Created on Mon Apr 14 23:04:01 2025

@author: menah
"""

file = open("my file.txt", "r")

s = file.readlines()  

file.close()

for r in s[49:60]:  
    print(r.strip())  