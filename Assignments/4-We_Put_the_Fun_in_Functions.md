# We Put the Fun in Functions!

## Overview

This assignment will allow you to practice writing Python functions. All of the problems require you to write code that takes inputs and **returns** results.

Use the Assignment 4 workspace on repl.it. All of the functions you need to complete are in `main.py`. Fill in the body of each function. **Don't write any code outside of any functions**.

The testing for this assignment is slightly different. We're using a new feature called **unit tests** to validate your code. A unit test simply calls a function with specified parameters and then checks that it returns the correct result.

To test your code, click on the check mark in the left side menu. It's labeled "Tests" if you hover over it. You'll see a list of all the unit tests. Click the "Run Tests" button and the testing framework will automatically run your functions and report the number of tests that you passed. If you fail a test, look at the output message, which will show the inputs and expected return value.

In order to pass the tests you must **return** a result from every function. **Do not print anything in your functions** and do not use the `input` command to read values.

## Problems

### `min`

This is a warmup. I've given you a function that finds the minimum of two numbers, but it's not quite correct. Modify it and make sure you can pass its tests.

### Justify Your Existence

We have seen that you can use `+` to concatenate strings together.

```
name = 'World'
print('Hello, ' + name)  # prints Hello, World
```

You can also use `*` to repeat strings.

```
print('a' * 5)  # prints 'aaaaa'
print('spam' * 4)  # prints 'spamspamspamspam'
```

These two operations can be combined.

```
print(' ' * 5 + 'spam'*2)  # prints '     spamspam' (five spaces followed by two spams)
```

Write a function named `right_justify` that takes a string as input and returns the string padded with enough spaces in front to put its last character in **column 20** of the terminal display.


Tips:

You can use the built-in len function to get the number of characters in a string

```
length = len('spam')  # length is 4
```

If you know the length of the string, you can calculate how many spaces to put in front of it to place the last character column 20.

Remember: do not use the `input` function. The input to `right_justify` is passed as a parameter by each test. Do not print anything. `right_justify` only **returns** the padded string.


### Triple min


Write a function called `triple_min` that takes three integers `a`, `b`, and `c` as input and returns the minimum of all three.

Don't use Python's built-in `min` function. Think about how to solve this using nested if-else statements. Start by comparing `a` to `b` to discover which one is smaller.


### Heron's Formula


**Heron's formula** (named after the Greek mathematician and inventor Hero of Alexandria) is a method of calculating the area of a triangle given the lengths of its three sides. If the three side lengths are *a*, *b*, and *c*, the formula is:

<img src="https://wikimedia.org/api/rest_v1/media/math/render/svg/d138044bb9ed870dd9dc5c7c8a3c07ab1db1705d" width="20%" />


where s is the "semi-perimeter":

<img src="https://wikimedia.org/api/rest_v1/media/math/render/svg/08ed8a6e351198e0c4ca8d71fa2e2bc4171e9439" width="10%" />

Write a function called `heron` that takes three inputs `a`, `b`, and `c` and returns the area calculated by Heron's formula.

Remember that you do not need to print anything, take any input, or write any code outside of the function; just return the final calculated value at the end of the function body. You can use `sqrt` from the math package to calculate the square root. Import it at the top of your program.


