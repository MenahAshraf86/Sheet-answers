# -*- coding: utf-8 -*-
"""
Created on Thu Mar 27 03:30:33 2025

@author: menah
"""

import random

def generate_password(length, chars):
    password = ''.join(random.choices(chars, k=length))
    return password

print(generate_password(8, "abcde"))