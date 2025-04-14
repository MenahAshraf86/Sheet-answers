# -*- coding: utf-8 -*-
"""
Created on Sun Apr 13 21:20:57 2025

@author: menah
"""

class Point3D:
    def __init__(self, x=0, y=0, z=0):
        self.x = x
        self.y = y
        self.z = z

    def __str__(self):
        return f"({self.x}, {self.y}, {self.z})"

    def add(self, p):
        self.x += p.x
        self.y += p.y
        self.z += p.z

    def distance(self, p):
        delta_x = self.x - p.x
        delta_y = self.y - p.y
        delta_z = self.z - p.z
        return (delta_x**2 + delta_y**2 + delta_z**2) ** 0.5
    
    def subtract(self, p):
        self.x -= p.x
        self.y -= p.y
        self.z -= p.z


p1 = Point3D(1, 2, 6)
p2 = Point3D(4, -2, 7)
p2.add(p1)
print(p2)  
p2.subtract(p1)
print(p2)  
print(p1.distance(p2))  