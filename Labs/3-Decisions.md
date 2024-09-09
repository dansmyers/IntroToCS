# Decisions

## Overview

This lab will allow you to practice writing programs that use `if` statements to implement branching.


## Setup

Create a new `Lab_3` directory and then `cd` into it.
```
mkdir Lab_3
```
```
cd Lab_3
```

Put each program into its own `.py` file. You can choose the names for each file.

## Problems

### Even-odd

Recall that Python supports a special operator, `%`, which is called the **modulus operator**. The mod operator calculates the remainder after division. For example,
```
11 % 3  is  2

13 % 4  is  1

8 % 2  is  0 (because 8 is evenly divisible by 2)

17 % 6  is  5
```
The mod operator can be used to check for divisibility. For example, suppose you want to test if an input value `n` is even. A number is even if it's evenly divisible by 2, so
```
if n % 2 == 0:
    # n is even
else:
    # n is odd
```
Write a program that reads an integer from the terminal and prints `Even` if the number is even or `Odd` if it's odd.

### Input validation


### `fortune`

There's a classic UNIX program called `fortune` that prints random messages when you run it. Run the following command **in your terminal** (not in a Python script) to install it
```
sudo apt-get install fortune
```



###
