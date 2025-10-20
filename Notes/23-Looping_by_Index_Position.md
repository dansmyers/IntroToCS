# Looping by Index Position

## Sequencing note

Lecture 19 was the last regular class before the midterm. This note picks up after midterm, fall break, and the review day after we returned from the break.

## Topics

- Using `range` and `len` for list loops
- Checking if a list is sorted
-  `break`
- Linear search

## Using `range` and `len`

So far, we've seen several examples of looping through the data items in a list; for exampple, summing the values to calculate an average or finding the maximum item.

Sometimes, it's useful to iterate through a list by **index position** rather than through the items directly. The following code declares a list and then steps through its items one at a time using the index values 0 to 7.
```
"""
Looping by index position
"""

primes = [2, 3, 5, 7, 11, 13, 17, 19]

# Loop through the index positions 0 to 7
for index in range(8):
    print(primes[index])
```
The loop variables `index` starts at 0, so the first iteration prints `primes[0]`, which is 2. The second iteration prints `primes[1]` and so forth up to `primes[7]`, the 19.

Recall that the index of the last item is always given by the length minus 1. A standard technique combines `range` and `len` to generate the index values from 0 to the last index, without the need to hardcode any specific length:
```
# Generate list indices from 0 to length - 1
for index in range(len(primes)):
    print(primes[index])
```

## Checking if a list is sorted

Index-based looping is useful for problems that require comparing items in the list to each other. For example, suppose we want to check if a list is in sorted increasing order.

The basic strategy is to compare pairs of consecutive items and check if they're sorted or not. Suppose we have the list `[2, 3, 5, 1, 7, 9]`

- The first iteration compares 2 and 3 and finds they are sorted
- The second iteration compares 3 and 5, they are again sorted
- The third iteration compares 5 and 1 and discovers they are out of order, so the list can't be in sorted order

The basic for loop can't do this, because we need not just the individual data items, but the ability to compare an item to its neighbor.

The code below implements the sorted check. It uses an `is_sorted` variable to keep track of the answer. The variable is set to `True` at the start of the loop, which is equivalent to assuming that the list is sorted unless we find a counterexample otherwise.
```
"""
Testing is a list is sorted
"""

data = [2, 3, 5, 1, 7, 9]

# Assume the list is sorted unless we find a counterexample
is_sorted = True

for i in range(1, len(data)):

    # Compare item i to its predecessor
    if data[i] < data[i - 1]:
        is_sorted = False


if is_sorted:
    print('The list is sorted.')
else:
    print('The list is not sorted.')
```
Notice the `range` statement. We've chosen to write this loop in a way that compares each item to its *predecessor*. The loop begins at index 1, so that the first iteration compares `data[1]` against `data[0]`.
```
data = [2, 3, 5, 1, 7, 9]
           ^
           |
         i = 1
```
The second iteration compare `data[2]` again `data[1]`, and so forth.

## `break`

Observe that the loop above doesn't stop when it finds a counterexample. It will continue to check all pairs of items in the list even though only one out-of-order pair is enough to determine the list isn't sorted.

The `break` command **ends a loop immediately**. When Python encounters `break`, it immediately stops the current loop and proceeds to the code after the loop.
```
"""
Sort-checking fragment with break statement
"""

data = [2, 3, 5, 1, 7, 9]
is_sorted = True

for i in range(1, len(data)):
    if data[i] < data[i - 1]:
        is_sorted = False

        # The answer has been found - end the loop immediately
        break

if is_sorted:
    print('The list is sorted.')
else:
    print('The list is not sorted.')
```
`break` is useful in situations like this, where you need to answer a question about a list and can then stop once you've discovered the answer.

In general, though, be careful about overusing `break`. Most loops need to run over the whole list; in that case, there's no need for `break`. Also, a question like `is_sorted` is ideal for moving into a function that takes a list as input. In that case, the `break` statement could be turned into a `return`.

## Linear search

Here's another standard problem:
> You're given a list and a search value of interest. Examine the list and return the *index* where the value occurs or -1 if it isn't present.

The basic algorithm for this problem is **linear search**: examine each item one at a time until you either find the value of interest or check the entire list. The program below defines a `search` function.
```
"""
Linear search
"""

def search(a, value):
    """
    Search the list a for the given value

    Returns the first index where value occurs or -1 if value isn't found
    """

    # Loop over the index positions of a
    for i in range(len(a)):
        if a[i] == value:
            return i  # Found value at index i

    return -1  # Failure


### Main
data = [2, 3, 5, 1, 7, 9]

location = search(data, 7)
print(location)
```
