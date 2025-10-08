# List Basics

## Topics

- Declaring lists
- List indexing
- List methods
- Looping over lists

## Declaring a list

A list is a sequence of items associated with a single variable name. Use square brackets to declare a list with the items separated by commas.
```
primes = [2, 3, 5, 7, 11, 13, 17, 19]
```
A list can contain items of any type.
```
fruits = ['apple', 'banana', 'cherry', 'durian', 'eggplant', 'fig']
```
Items don't have to be in sorted increasing or decreasing order.
```
data = [1.5, 2.25, .75, 9.99, .50, 4.44, .25, 3.33]
```
It's unusual, but Python allows heterogeneous lists that mix different types of data.
```
mixed_list = [1, 3.14, 'Hello', True]
```
It's also possible to create a list of lists; we'll see examples of that later.

## List indexing

A list is a sequence and each item in the list is associated with an **index number** indicating its position. You can interact with individual items in a list using square brackets and the index number.

***The first item in the list has index 0***.

- `primes[0]` is the first item, 2 in this case
- `primes[1]` is the second item, 3
- `primes[2]` is the third item, 5
- and so forth

Trying to access a position beyond the end of the list results in an `IndexError`.
```
print(primes[8])  # IndexError: list index out of bounds
```

### Length
The built-in `len` function returns the length of a list, which is the number of items it contains. `len(primes)`, in our example, is 8.

The final item in the list is always at position length - 1.
```
final_item = primes[len(primes) - 1]  ## 19
```

### Negative indexing

Python allows you to use negative index values to interact with the end of the list.

- `primes[-1]` is the last item, the 19
- `primes[-2]`, is the next to last item, 17
- and so forth

Note that this is a feature of Python, but not other languages.

## List methods

Lists support several built-in methods that you can invoke to perform operations on a list's data.

The `append` method adds a new item to the end of the list.
```
fruits.append('guava')
print(fruits)

# Prints ['apple', 'banana', 'cherry', 'durian', 'eggplant', 'fig', 'guava']
```

The `pop` method removes and returns the item at a given position.
```
# Remove the first item, 'apple', and assign it to variable f
f = fruits.pop(0)
```

The `remove` method takes a specific value and finds and removes it from the list if it's present.
```
fruits.remove('eggplant')
```

We'll practice other list methods in the lab.


## Looping over lists

A list is a sequence, so the `for` loop iterates through list items in the same as our other looping examples.
```
# Print items in the data list
for x in data:
    print(x)
```

Summing up the values in a numberic list is a common calculation. The easiest way is to use the built-in `sum` function:
```
total = sum(data)
```
You can achieve the same result with a loop and an accumulator variable.
```
# Sum the items in the data list
total = 0
for x in data:
    total += x

print(total)
```

The built-in `min` and `max` functions return the minimum and maximum valued items in a list, respectively. Here's a loop-based implementation of `min`:
```
# Find the min of the data list
min_value = data[0]
for x in data:
    if x < min_value:
        min_value = x
```
The code fragment uses `min_value` to keep track of the smallest item found in the list at each point in the loop. Initially, `min_value` is set to the first item, which avoids the challenge of picking an arbitrary starting value that's guaranteed to be larger than the true minimum. The loop iterates through the items one at a time and compares each to `min_value`. If the given item is smaller, `min_value` is updated.
