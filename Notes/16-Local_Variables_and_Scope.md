# Local Variables and Scope

## Topics

- Variables declared inside a function have local scope
- Global variables (are usually bad idea)
- Stack diagrams


## Local scope

Variables declared inside a function are said to be *local variables*. You can only use and interact with a local variable during the time that its function is executing. When a function returns, its local variables go *out of scope* and can't be read or interacted with by other parts of the program.

For example, the following program attempts to print the value of a local variable outside of its function. It will give a `NameError` if you run it.
```
"""
Local variables and scope
"""

from math import pi

def circle_area(r):
    a = pi * r ** 2
    return a

### Main
radius = float(input('Enter a radius: '))
area = circle_area(radius)

# Try to print local variable a - gives NameError: a is not defined
print(a)
```

## Global variables

Variables declared outside of any function have *global* visibility. They can be read and used inside any function. In the example below, the function has no local variable named `radius`, so Python will look to the global scope and use the value of `radius` defined there, in the main part of the program.
```
"""
Accessing a global variable from within a function
"""

from math import pi

def circle_area():
    a = pi * radius ** 2  # Use value of radius from Main
    return a

### Main
radius = float(input('Enter a radius: '))
area = circle_area()
print(area)
```

In general, ***global variables are a bad idea***. Recall that one benefit of functions is *hiding complexity*, so we like for our functions to be nice, self-contained units that take input parameters and return results using the `return` keyword. Making a function that depends on reading global variables is a bad way to share information between parts of the program because it's hard to reason about and tends to lead to conflicts where changes in one part of the code cause unpredictable problems elsewhere.

It is technically possible to change the value of a global variable within a function. You can read about the `global` keyword if you want to, but I'm not going to teach it because writing to a global variable is even worse than just reading one. Functions should, in general, take inputs through their paramters and return results using `return`, not through unpredictable global interactions.

The one reasonable exception to this guideline is a constant that's set one time at the beginning of the program and doesn't change. It's okay to have a program that uses constants, like `pi`, inside of functions.


## Stack diagrams

The **stack** is the special region of memory where the system keeps track of local variables. Every time you call into a function, Python allocates a new region of memory called a *stack frame* to hold the parameters and local variables for that function.

Consider the following example:
```
"""
Using a stack frame to understand local variables
"""

def rect_area(length, width):
    area = length * width
    return area

### Main
length = float(input('Enter a length: '))
width = float(input('Enter a width: '))
area = rect_area(length, width)
print(area)
```

At the beginning of the program, Python allocates a stack frame for the main region, which holds the storage space for all variables declared outside of any function. That includes the `length` and `width` variables on the first two lines of the main section. Suppose the user enters 7 for the length and 5 for the width, then the stack frame after reading those two inputs will look like the following:
```
  -----------
 | length: 7 |
 | width: 5  |  main
 |           |
---------------
    stack
```
The next line allocates a new variable named `area`. To find its value on the right-hand side of the assignment, call `rect_area`, passing in `length` and `width` as arguments. Calling the function allocates a **new stack frame** to hold *its* local variables. Each new frame is allocated on top of the previous frames, like a stack of pancakes, so the stack is also keeping the history of the sequence of function calls the program has made up to this point.
```
  -----------
 |           |
 |           |  rect_area
 |           |
  -----------
 | length: 7 |
 | width: 5  |  main
 | area: ?   |
---------------
    stack
```
The input parameters of `rect_area` are named `length` and `width`, but there **are not the same** as the length and width defined in the main section. Instead, these new local variables are allocated inside the stack frame for `rect_area`.
```
  -----------
 | length: 7 |
 | width: 5  |  rect_area
 |           |
  -----------
 | length: 7 |
 | width: 5  |  main
 | area: ?   |
---------------
    stack
```
The stack explains how local variables in different parts of the program can have the same name, but map to different underlying values: the different `length` and `width` variables are literally stored at differeing underlying locations in the computer's memory.

The next line calculates `area`, which is also a local variable inside the `rect_area` frame.
```
  -----------
 | length: 7 |
 | width: 5  |  rect_area
 | area: 35  |
  -----------
 | length: 7 |
 | width: 5  |  main
 | area: ?   |
---------------
    stack
```
Returning from a function "pops" its frame from the top of the stack and deallocates all of its associated memory. Any variables defined in the frame go out of scope and the function returns the specified value, which is assigned to `area` in the main stack frame.
```
  -----------
 | length: 7 |
 | width: 5  |  main
 | area: 35  |
---------------
    stack
```
Look at the `tricky.py` example in the `Examples/3-Functions` directory for a more complex problem that uses a function calling a function.
