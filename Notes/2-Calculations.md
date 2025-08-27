# Calculations

## Topics

- Basic arithmetic operators
- Numerical precision
- Order of operations and parentheses
- Exponents

## Arithmetic

Python uses the four basic arithmetic operators that are likely familiar to you from handheld calculators.

- `+` for addition
- `-` for subtraction
- `*` for multiplication
- `/` for division

If you print an arithmetic expression, Python will calculate it and output the answer
```
# Prints the answer 10
print(2 * 3 + 4)
```

Note that this is *not* the same as printing a string!
```
# Prints the literal string '2 * 3 + 4', not the calculated result
print('2 * 3 + 4')
```

## Numerical precision
Sometimes, you need to do a calculation that produces a repeating decimal answer
```
# 8.666666...
print(20 / 3 + 2)
```
If you execute that statement, you'll see that the output is `8.666666666666668`. What's that 8 doing at the end?

Computers are **finite machines** that exist in the real world. Therefore, they have *limits* on the data they represent and store. The standard methods of storing numbers in a computer don't allow more than about 15 digits of precision after a decimal point. You should always be aware that calculations on a real computer may produce very, very small numerical errors due to the lack of precision in representing tiny fractional quantities. This won't be a problem for us, but it does matter for applications like physics, simulations, and machine learning that need to perform precise, high-repetition calculations.


## Order of operations

Python respects the standard order of operations. You can use parentheses to indicate priority.
```
print((2 + 3) * 4)
```

Don't overly parenthesize expressions! Avoid cluttering expressions with parentheses that simply copy the already-existing order of operations. It's okay to chain multiple operations together sequentially.
```
# Inner parentheses are unnecessary
print(((3 * 4) * 5) * 6)

# This is equivalent and cleaner
print(3 * 4 * 5 * 6)
```

## Style

Place a single space between each operator and its operands to make your expressions easy to read.
```
# Bad: looks like a serial bomber wrote it
print((2+3)*4)

# Good: whitespace communicates openness and confidence
print((2 + 3) * 4)
```
This style is preferred by most professional coding guides.

## Exponents
Python uses `**` for exponentiation. Don't use `^`, which you may have seen on calculators.
```
# Square root of 25 = 5
print(25 ** .5)
```

For example, to calculate the area of a circle with radius 5.0 (using 3.14 as a temporary approximation for pi):
```
print(3.14 * 5.0 ** 2)
```
The exponent has higher priority than multiplication, so parentheses are unnecessary.

## Practice

Complete the questions in Activites/1-Calculation.md.

