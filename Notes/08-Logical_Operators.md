# Logical Operators

## Topics

- `and`, `or`, and `not`
- Writing more complex conditions
- Using truth tables to show equivalent between logical expressions

## `and`

The `and` operator takes two boolean expressions on its left and right sides and combines their results to produce a boolean output. The `and` of two booleans is `True` if both of its inputs are `True` and `False` otherwise.

```
# Sum of two six-sided dice
roll = randint(1, 6) + randint(1, 6)
print(roll)

# This condition is True if the roll is both even and less than 10
if roll % 2 == 0 and roll < 10:
    print('Even and less than 10')
```

You can express the behavior of a logical expression using a **truth table**:
```
 a  b  |  a and b
------------------
 F  F  |     F
 F  T  |     F
 T  F  |     F
 T  T  |     T
```

## `or`

The `or` operator is similar to the `and` operator: it combines the results of two boolean expressions. The `or` operator evaluates to `True` if *at least one* of its inputs is `True` and `False` if both are `False`.

```
 a  b  |  a or b
------------------
 F  F  |     F
 F  T  |     T
 T  F  |     T
 T  T  |     T
```

```
# Require a choice value in the range 1-4
if choice < 1 or choice > 4:
    print('You must enter 1 to 4.')
    quit()
```

A common error is try using `or` with multiple values on the right side of a comparison. For example,
```
# Try to reject values outside the range 1-4 (this doesn't work)
if choice != 1 or 2 or 3 or 4:
    print('You must enter 1 to 4.')
    quit()   
```
This won't work the way you expect. Always use logical operators to combine **boolean expressions**. You can't use them to test against multiple values on one side of an relational comparison.

## `not`

`not` is the *logical inversion* operator. It takes a boolean result and switches it to the opposite value. Sometimes this is useful for simplifying expressions.
```
# Another way of testing for invalid input
if not (choice == 1 or choice == 2):
    print('You must enter 1 or 2.')
    quit()  
```
Notice that the parentheses *are* required in this case to make the `not` operator apply to the entire inner expression.

`not` is the trickiest operator to use correctly. If you want to use it, just think carefully about your expression and make sure it's doing what you want.

## Truth tables

You can use a truth table to test if two expressions are logically equivalent. If they have the same truth table, then they express the same logical operation.

One of the most useful results in logic is **De Morgen's Law**, which states that
```
not (a and b) == (not) or (not b)
```
You can show this equivalence by constructing the relevant truth table columns
```
 a  b  |  not (a and b)  |  (not a) or (not b)
-------------------------|---------------------
 F  F  |       T         |          T
 F  T  |       T         |          T
 T  F  |       T         |          T
 T  T  |       F         |          F
```
Try using truth tables to show the other case of De Morgen's Law:
```
not (a or b) == (not a) and (not b)
```
