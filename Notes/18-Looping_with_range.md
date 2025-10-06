# Looping with `range`

## Topics

- One- and two-input forms of `range`
- Loops that select and sum
- Three-input version with a non-unit step size
- Looping backwards

## Single-input `range`

The built-in `range` function is our basic tool for looping over **sequences of numbers**. The basic form of `range` takes one input:
```
# Single-input range
for i in range(10):
    print(i)
```
Single-letter variable names like `i`, `j`, and `k` are traditional for numeric loops. In particular, most programmers use `i` as their default loop variable name when writing a numeric `for` loop.

If you run this program, you'll see the following output values:
```
0
1
2
3
4
5
6
7
8
9
```
The single-input `range` starts at ***zero*** and goes ***up to but does not include*** the given stopping number.

For example, the loop below iterates from 0 to 99, but does not include 100.
```
for j in range(100):
    print(j)
```

## Two-input `range`

The two-input `range` specifies the starting and stopping values of the loop. The stopping behavior is the same as the one-input version: go up to ***but not including*** the given ending value. For example, the loop below would iterate from 1 to ***19***:
```
# Loop from 1 to 19
for j in range(1, 20):
    print(j)
```

Recall, from the last class, the *selector pattern* that combined a `for` loop with an `if` statement to select certain values of interest from the sequence. The loop below prints the numbers from 1 to 30 that are divisible by 3. Notice that the second input to `range` is 31, so that 30 is included in the loop.
```
# Numbers 1 to 30 divisible by 3
for n in range(1, 31):
    if n % 3 == 0:
        print(n)
```

A second common loop pattern is the *accumulator pattern*, which uses a variable declared before the loop to sum up values of interest. [Project Euler](https://projecteuler.net/) is a site with fun mathematical problems. Problem #1 says,
>If we list all the natural numbers below that are multiples of 3 or 5, we get 3, 5, 6, and 9. The sum of these multiples is 23.
>
> Find the sum of all the multiples of 3 or 5 below 1000.
```

```

