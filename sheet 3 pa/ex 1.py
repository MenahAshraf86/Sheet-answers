# -*- coding: utf-8 -*-
"""
Created on Thu Mar 13 03:22:49 2025

@author: menah
"""

number_of_runs = 0
total_time = 0

while True:
    S = input("Enter 10 km run time: ")
    
    if S == "" or S == "0":
        break
    
        run_time = float(S)
        total_time += run_time
        number_of_runs += 1
average = total_time / number_of_runs
print(f"Average of {average}, over {number_of_runs} runs")