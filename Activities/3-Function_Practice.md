# Function Practice

## Overview

The questions below will let you practice writing functions that take inputs and **print** values. After this activity, we'll work on making our functions **return** values that can then be saved into a variable and used in another part of the program.

Some tips:

- Read the problem. It will tell you the required inputs for each function.
- Functions take inputs through their parameters! Don't use `input` to read a value within a function.
- Give each function a docstring that summarizes what it does. This isn't always required if the function is small and self-documenting, but it's a good habit to practice.


## Programs

### `print_area_of_triangle`

Complete the following program with a function that takes an input base and height, then **prints** the area of the corresponding triangle.

```
"""
Write a function that prints the area of a triangle
"""

def print_area_of_triangle(base, height):
    """
    Complete this function docstring
    """
    
    # Calculate the area of the triangle
    
    # Print the result
    

### Main

print_area_of_triangle(10, 5)

print_area_of_triangle(3, 11)

# Add a statement to print the area of a triangle with base 7 and height 17

# Write a statement that calls the function with inputs that will print 99 as the output
```


### Willigrams
After Scott invented the Scottometer, Will needed his own unit of measurement so he created the **Willigram**. The actual magnitude of the Willigram is a bit uncertain (the definition has varied over time), but is currently set at 10000 pounds per Willigram.

Write a program that reads a number of pounds from the user and prints the corresponding number of Willigrams. Use a function called `pounds_to_willigrams` to perform the conversion and print the result. Your function should take one input called `pounds`. 

Make sure that your function has an appropriate docstring.

Notice that the `input` statement is in the main part of the program and the input value is passed to the function to get the result. Don't use `input` in the function itself.

```
"""
Convert pounds to Willigrams
"""

### Write your function definition here
#
# The input argument should be named pounds


### Main

# Read a number of pounds
value = int(input('Enter a number of pounds: '))

# Call the function that performs the conversion and prints the result
pounds_to_willigrams(value)
```


### Crickets

<img src="https://www.liveabout.com/thmb/VL-U6f9b4pDPuedh1OFORBlM0lo=/1500x0/filters:no_upscale():max_bytes(150000):strip_icc()/GettyImages-84892625-5c76ff65c9e77c0001d19c74.jpg" width="300px" />

*Buddy Holly and the Crickets*

Let's return to the cricket protein powder question. Recall that one cricket contains about .3 grams of protein. Complete the program below by writing a function that takes grams of protein as input and **prints** the number of crickets required for that amount.

Tip: Make sure to include a docstring at the start of your function.


```
"""
Convert grams of protein into crickets
"""

### Write your function definition here


### Main

# Read input number of grams of protein
value = float(input('Enter a number of grams of protein: '))

# Call the function to perform the conversion and print the result
grams_of_protein_to_crickets(value)
```
