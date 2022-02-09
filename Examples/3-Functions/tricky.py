"""
A tricky set of functions using the same variable name in multiple places. What does this code output?
"""

def baz(x):
    x = x * 2
    return x    


def foo(value):
    x = baz(value + 1)
    return x


### Main
x = 1
x = foo(x)
print(x)
