# -*- coding: utf-8 -*-
"""
Created on Thu Mar 13 03:27:52 2025

@author: menah
"""

fl_num = 1234.5678
bef_int_num = 2
aft_int_num = 3
num =str(fl_num)
ind=num.index(".")
int_part=num[ind-2:ind]
float_part= num[ind+1:ind+4]
print(int_part+"."+float_part)