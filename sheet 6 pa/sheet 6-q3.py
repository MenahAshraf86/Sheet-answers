# -*- coding: utf-8 -*-
"""
Created on Mon Apr 14 23:01:26 2025

@author: menah
"""

file = open("my file.txt", "a")

for x in range(1, 101):
    file.write(f"{x}\n")
    
file.close()