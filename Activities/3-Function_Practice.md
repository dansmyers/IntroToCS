# Function Writing Practice

This micro-lab will let you practice writing some functions that return results.

## Setup

Create one file named `function_practice.py` in your `Functions` subdirectory:

You can add each function into this file. Write a few lines in the "Main" section to test each new function after you complete it.


## 3d6

Write a function called `three_d6` that returns the sum of three six-sided dice.


## Doge II: Return of Doge

<img src="https://i.redd.it/bkhyosuip8g51.jpg" width="300px" />

*The Doge of Venice. You can also read about the complete insanity involved in [selecting a new doge](https://en.wikipedia.org/wiki/Doge_of_Venice#Selection_of_the_doge)*.


Complete the program below by writing a function called `usd_to_doge` that takes a number of USD as input and converts to the equivalent number of DOGE. The function should **return** the result.

1 dollar is currently worth about 9.17 DOGE.

```
"""
USD to DOGE converter
"""

### Write your function definition here
#
# Remember: don't use input or print inside the function; return the result


### Put these lines in your main section to test the function

# Read a number of dollars
dollars = float(input('Enter a number of dollars: '))

# Call a function that converts to DOGE and then print the result
doge = usd_to_doge(dollars)
print(f'That is {doge: .2f} dogecoins.'
```

## Max of two numbers

Write a function named `max` that takes two input parameters named `a` and `b`. Return the larger of the two input values.

Tip: use an `if-else` block. Each branch will have a return statement.

Tip-tip: Python has a built-in `max` function, but don't use it for this problem.

```
def max(a, b):
    """
    Return the max of a and b
    """

```

Write some test code that calls `max` for various input values and verify that it returns the correct result. For example,

```
### Put this code in main
result = max(77, 13)  # Change these numbers to test different cases
print(result)  # Verify this is the maximum
```


## Even-odd

Write a function named `is_even` that takes an integer `n` as input and returns `True` if `n` is even and `False` if `n` is odd. Use an `if-else` block inside the function that tests `n`.

Add the test code below to your main section.

```
### Main
number = int(input('Enter a number: '))
print(f'Is it even? {is_even(number)}'
```

Tip: Recall that you can use the modulus operator to test for evenness: `n % 2 == 0` is `True` if `n` is even.
