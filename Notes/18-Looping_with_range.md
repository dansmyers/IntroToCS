# Looping with `range`

## Topics

- One- and two-input forms of `range`
- Loops that select and sum
- Three-input version with a non-unit step size
- Looping backwards

## `range`

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
