"""
Calculate the area of a circle using a function
"""

from math import pi

def print_area_of_circle(radius):
    """
    Calculate the area of the circle with the given input radius
    """
    
    area = radius ** 2 * pi
    print(area)
    

### Main

print_area_of_circle(1)

print_area_of_circle(10)

print_area_of_circle(100)

print_area_of_circle(1000)
