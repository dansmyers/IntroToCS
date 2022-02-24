# Challenge Project #2: Project Euler

## Overview

In this challenge project, you'll complete some problems from [Project Euler](http://projecteuler.net), a site that hosts a lot of interesting mathematical programming challenges. The project is straightforward: Solve the five Project Euler problems described below. The questions will give you the chance to practice the features from the first 
half of the class, including loops, conditionals, arithmetic, and functions.
 
## Grading

There are no automated tests for this project. To get credit, submit your code to the assignment I'll create on Canvas.

## Problems

### Sum Square Difference (Problem 6)

The sum of the squares of the first ten natural numbers is,

1<sup>2</sup> + 2<sup>2</sup> + ...+ 10<sup>2</sup> = 385

The square of the sum of the first ten natural numbers is,

(1 + 2 + ... + 10)<sup>2</sup> = 55<sup>2</sup> = 3025

Hence the difference between the sum of the squares of the first ten natural numbers and the square of the sum is

3025 − 385 = 2640.

Find the difference between the sum of the squares of the first one hundred natural numbers and the square of the sum.


### Smallest Multiple (Problem 5)

2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.

What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?

Tips:

- Use `while` loop that begins at 20 and counts up by 20 on each iteration (the solution must be a multiple of 20).

- Write a function called `is_divisible_by_1_to_20(n)` that uses a `for` loop to check if `n` is divisible by the numbers from 1 to 20.


### 10001st Prime (Problem 7)

By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see that the 6th prime is 13.

What is the 10 001st prime number?

Tips:

The basic strategy is something like this:

```
n = 2;
numPrimes = 0;

while (True):
    if (isPrime(n)):
        numPrimes += 1
    
    if (numPrimes == 10001):
        print(n)
        break
    else:
        n += 1
```

Think about how to test if a number is prime. The straightforward way, which you implemented on Assignment 5, is to test for divisibility by any numbers between 2 and sqrt(n). This could be slow though,
because you'll spend a lot of time grinding through numbers.

A faster way is to use a list to keep track of the primes you find. It's then sufficient to test for divisibility by the **primes** 
that are less than sqrt(n).

Try the straightforward solution first. If it runs for more than, say, a minute, try implementing the faster solution.

### Special Pythagorean Triplet (Problem 9)

A Pythagorean triplet is a set of three natural numbers, *a* < *b* < *c*, for which,

*a*<sup>2</sup> + *b*<sup>2</sup> = *c*<sup>2</sup>

For example, 3<sup>2</sup> + 4<sup>2</sup> = 9 + 16 = 25 = 5<sup>2</sup>.

There exists exactly one Pythagorean triplet for which *a* + *b* + *c* = 1000. Find the product *abc*.

Tips:

A straightforward way to attack the problem is this:

```
for a in range(1, 1000):
    for b in range(1, 1000):
        for c in range(1, 1000):
            
            # Test if a + b + c == 1000 and the three numbers are a Pythagorean triple

            # If they are, output them and the product abc and then end the program
 
```

This could work, but is inefficient because it has to evaluate 1000 * 1000 * 1000 combinations. It also wastes time evaluating combinations that can't possible by correct, like 1-1-1, and evaluates the same combinations of `a` and `b` multiple times.

Can you simplify the loops? Maybe you don't need a dedicated loop for `c`?


### Largest Palindromic Number (Problem 4)

A palindromic number reads the same both ways. The largest palindrome made from the product of two 2-digit numbers is 9009 = 91 × 99.

Find the largest palindrome made from the product of two three-digit numbers.

Tips:

- Use two `for` loops to iterate through the combinations of three-digit numbers. For each product, test if it's a palindrome and keep track of the
largest palindrome value you find.

- You probably want an `is_palindrome(n)` function to test if a number `n` is palindromic. Maybe you could use the `str` function to turn `n` into a string
to make the palindrome test easier?
