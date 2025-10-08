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

A list is a sequence and each item in the list is associated with an **index number** indicating its position. You can interact with individual items in a list 
