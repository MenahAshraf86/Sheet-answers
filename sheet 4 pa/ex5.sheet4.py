# -*- coding: utf-8 -*-
"""
Created on Thu Mar 27 04:13:00 2025

@author: menah
"""

def substitute(equation, **kwargs):
    for var_name, var_value in kwargs.items():
        equation = equation.replace(var_name, str(var_value))
    return equation

result_equation = substitute("x * 2 + y - z + 1 ", x=2, y=3, z=4)
print(result_equation)