# Relational Operators and the `if` Statement

## Topics

- The six relational operators
- Testing for divisibility using the modulus operator
- Introduction to the `if` statement
- Indentation and logical structure

## Relational operators

The six relational operators are our primary tool for making comparisons between values. Each operator takes two expressions, one on its left and one on its right, and asks a question about their relationship. The output of a relational comparison is always boolean `True` or `False`.

For example, to test if a variable `x` is strictly greater than 10:
```
x > 10
```
This expression compares the value of x to 10 and evaluates to `True` if `x` is in fact greater than 10 and `False` otherwise.

Like the `=` operator, remember that a relational operator is not the same as a mathematical inequality. Think of it as a question - "Is the value of `x` greater than 10?" - to which the answer is `True` or `False`.

## The six operators

- `>`: strictly greater than
- `<`: strictly less than
- `>=`: greater than or equal
- `<=`: less than or equal
- `==`: equal (true if both sides have equal values)
- `!=`: not equal (true if both sides have different values)

Most of these are straightforward. Try testing some examples in the interactive Python prompt.

It's easy to accidentally type `=` when you meant to type `==`. For example, you meant to test if `x` is equal to 0:
```
x == 0
```
But you typed
```
x = 0
```
This would have the effect of replacing the old value of `x` with 0, which is almost certainly not what you want.

Python is usually forgiving of this error. The language won't allow you to use assignment in places where a test for equality might be expected. Other languages, notably C, are not so merciful however, and you can accidentally end up overwriting variables if you forget the second `=`. Always be aware that this is an easy typo to make.

Aside: The Pascal language dealt with this by using `=` for equality, `:=` for assignment, and `<>` for inequality.

## More on inequality

`!` in programming is often used to indicate an inversion or logical NOT operator. It's often spoken as "bang" instead of "exclamation point".

Inequality is the trickiest operator to get correct, because it requires you to reason about the inversion. It's fine to use, just spend a moment thinking and make sure that your test is doing what you really want.

## Testing for divisibility

`%` is the **modulus operator**, which returns the remainder after division. You can use it to test for divisibility, which is an important building block of many algorithms, games, and simulations.

Consider the remainder after dividing by 2:
```
x % 2
```
There are only two possible results, 0 and 1. If the remainder is 0, then `x` was evenly divided; if it's 1, then `x` must be odd. Therefore, you can test for evenness using:
```
x % 2 == 0
```
If you want to test for oddness, you have a couple of options:
```
x % 2 == 1
x % 2 != 0
```
Similar expressions can be used to test for divisibility by other numbers:
```
# True if x is divisible by 3
x % 3 == 0
```

## The `if` statement

The `if` statement is our main tool for adding **conditional branching** to a program. An `if` statement makes a block of code conditional on the result of a boolean expression.

- If the expression evaluates to `True`, the conditional block is executed, then the program continues
- If the expression is `False`, the block is *skipped*, and then the program continues

Here's an example that reads an input `int` and tests if it's even.
```
"""
Read an int and test if it's even
"""

# Read input value
x = int(input('Enter a positive integer: '))

# Test if x is even and if so print 'Even'
if x % 2 == 0:
    print('Even')

# Code after the if statement
print('Done')
```

When Python encounters the `if` statement, it evaluates `x % 2 == 0`.

- If the result is `True`, it executes the conditional code block, which prints `Even`, then continues to the last line to print `Done`
  
- If the result is `False`, it *skips* the conditional code and proceeds immediately to the last line to print `Done`

## Details of the `if` statement

An `if` statement needs four things.

1. The `if` keyword

2. A boolean expression; that is, an expression that evaluates to `True` or `False`

3. A colon, which Python uses to indicate the opening of a new block

4. The conditional code block. In our example, this is only the single `print` statement, but the block can in general be of any length and contain any combination of statements, including nested `if` statements.

Notice that the conditional block is **indented** with respect to `if`. This is *required*. **Python uses indentation to show the structure of the program**, so every code block must be indented to show that it "belongs" to the previous `if` statement.

Even if it wasn't required, we'd still want to indent because it makes the visual organization of the program match its logical structure.

Python doesn't care how much indentation you use as long as it's consistent within the same block.
```
# This is allowed
if x % 2 == 0:
                print('Even')

# So is this
if x % 2 == 0:
 print('Even')
```
In practice, indenting by **four spaces** is common and easy to read. The editor will help you by automatically indenting when you open a new block with a colon.
