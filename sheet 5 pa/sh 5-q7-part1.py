# -*- coding: utf-8 -*-
"""
Created on Sun Apr 13 21:13:22 2025

@author: menah
"""

class Point2D:
    def __init__(self, x=0, y=0):  # Corrected constructor
        self.x = x  # Initialize x coordinate
        self.y = y  # Initialize y coordinate

    def __str__(self):  # Corrected string representation method
        return f"({self.x}, {self.y})"  # Return string representation

    def add(self, p):
        self.x += p.x  # Add p's x to self's x
        self.y += p.y  # Add p's y to self's y

    def distance(self, p):
        delta_x = self.x - p.x  # Calculate x difference
        delta_y = self.y - p.y  # Calculate y difference
        dist = (delta_x ** 2 + delta_y ** 2) ** 0.5  # Pythagorean theorem
        return dist


p1 = Point2D(1, 2)  # Create point at (1,2)
p2 = Point2D(4, -2)  # Create point at (4,-2)

p2.add(p1)  # Move p2 by p1's coordinates

print(p2)  # Print new position of p2
print(p1.distance(p2))  # Print distance between p1 and p2