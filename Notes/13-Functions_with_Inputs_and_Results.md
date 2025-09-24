# Functions That Take Inputs and Return Results

## Topics

- Functions that take input parameters
- Parameters vs. `input`
- Multiple inputs
- Returning results
- Return vs. `print`

## Input parameters

The program below defines a function name `area_of_circle` with an input named `radius`. It calculates the area of the corresponding circle and **prints** it. The input parameter is specified in the parentheses as part of the function definition.
```
"""
Example of a function with an input parameter
"""

from math import pi

def area_of_circle(radius):
    area = pi * radius ** 2
    print(area)

### Main
area_of_circle(5.0)
```
