# -*- coding: utf-8 -*-
"""
Created on Thu Mar 27 03:33:39 2025

@author: menah
"""

Chars = ''.join([chr(s) for s in range(97, 123)]+  
                     [ chr(s) for s in range(48, 58)]+ 
                    [ chr(s) for s in range(65, 91)])

print(Chars)

for x in Chars:
    print(f"{x} ==> {ord(x)}")