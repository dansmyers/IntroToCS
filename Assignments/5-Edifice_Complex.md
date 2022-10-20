# Assignment 5: Edifice Complex

## Due


## Overview


## Grading


## Problems

### Max of a list

Write a function called `list_max` that takes a list named `a` as input and finds and returns its largest element. Don't use the built-in `max` function.

Remember: this problem uses a unit test, so you need to **return** the result. Don't print anything and don't use the `input` function.


### Range of a list

Write a method called `list_range` that takes a list of numbers as input and returns the difference between the largest and smallest elements.

Tips: You need to find the largest and smallest elements in the list. Don't use the built-in `max` or `min` functions.


### Rotate a list

Write a function called `rotate_list` that takes a list and a number as input, then returns the list rotated the specified number of places. A rotation of one place moves the first element to the back of the list. A rotation of two places moves the first element to the back of the list, then the second element to the back of the list, etc.

For example,

```
rotate_list([1, 2, 3, 4], 1)
```

will return
```
[2, 3, 4, 1]
```
and
```
rotate_list([1, 2, 3, 4], 3)
```
will return
```
[4, 1, 2, 3]
```

Tips:

You can use the list's `pop` method to remove an element at a given position and get its value:
```
first_value = a.pop(0)  # remove the element at position 0
```
You can use append to stick a new element onto the end of a list
```
a.append(new_item)
```
Use a loop that combines popping and appending.

What about empty lists? Empty lists automatically evaluate to False, so you can use the following code to return immediately if the list has no elements.

```
# If a is empty there's nothing to rotate
if not a:
    return a
```
