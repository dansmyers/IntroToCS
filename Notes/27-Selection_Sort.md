# Selection Sort

The selection sort algorithm sorts a list into increasing order by repeatedly finding the smallest remaining unsorted item, then swapping it into its correct position. For example, suppose we have the list
```
[5, 1, 3, 2, 7, 9, 4]
```
The algorithm first scans the entire list to discover that 1 is the smallest item and swaps it into the first position. 1 is now in its correct location and doesn't need to be considered further.
```
[1, 5, 3, 2, 7, 9, 4]
```
The second iteration finds the second smallest remaining item, the 2, and swaps it into the second position. Both 1 and 2 are now in their correct final positions.
```
[1, 2, 3, 5, 7, 9, 4]
```
The third iteration checks the remaining items to identify 3 as the next smallest item and, as it turns out, already in its correct position. Note that even though 3 is in its eventual final position already, the algorithm doesn't have a way to discover that, so the method still has to look through everything.
```
[1, 2, 3, 5, 7, 9, 4]
```
This process continues until the list is completely sorted.

## Implementation

Look at the implementation below. Notice that it uses two loops. The outer `for` loop iterates through the swap destinations--the first position, second position, third position, and so forth--the inner loop finds the smallest remaining item.

Also observe that the method doesn't return anyhing. The list is sorted *in-place* by exchanging its elements, not by making a copy.

```
"""
Selection sort

Repeatedly find the minimum remaining item in the list and swap it into
its correct position
"""

def sort(a):
    """
    Sort the input list a into increasing order

    Doesn't return anything - a is sorted in in-place by rearranging
    the data inside the single list, not by making copies with different items
    """

    # Use two loops

    # Outer loop keeps track of the swap destination position on each iteration
    #
    # Iteration 1: i = 0 and the smallest item swaps into position 0
    # Iteration 2: i = 1 and the second smallest item swaps into position 1
    # etc.
    #
    # The loop ends when there is only one item remaining; it must be the max
    for i in range(0, len(a) - 1):

        # Use an inner loop to find the minimum among the remaining items
        min_value = a[i]
        min_index = i
        for j in range(i + 1, len(a)):
            if a[j] < min_value:
                min_value = a[j]
                min_index = j

        # Swap the minimum item into position i
        temp = a[i]
        a[i] = a[min_index]
        a[min_index] = temp


### Main
example = [5, 1, 3, 2, 7, 9, 4]
sort(example)
print(example)
```

## Passing lists are arguments

The main section of the program makes a list variable named `example`. You can think of the name as a reference to the underlying object in memory.
```
example ---> [5, 1, 3, 2, 7, 9, 4]
```
When you pass `example` into the `sort` function, the input parameter `a` become an *alias* to the same underlying list in memory. That is, passing the list doesn't create a *copy* of its data for the function. Instead, we just pass a *reference* to the underlying list in memory.
```
example -----
            |
            v
            [5, 1, 3, 2, 7, 9, 4]
            ^
            |
a -----------
```
Therefore, changes made through `a` in the function are persisted outside of it. Printing `example` at the end of the program prints the sorted list.

## Calculating the amount of work

Consider the amount of work required by selection sort. If the list has length `n`, then the first iteration requires examining `n` elements to find the minimum. The second iteration examines `n - 1` elements to find the second smallest item and so forth. Therefore, the total number of item examinations is
```
T = n + (n - 1) + (n - 2) + ... + 3 + 2 + 1
```
This is a well-known summation:
```
T = (n / 2)(n + 1)
```
This style of **algorithm analysis** considers how the performance of selection sort changes as its input becomes bigger and bigger, in a way that depends only on the algorithm itself and not on the actual timing of a particular implementation running on a given system.
