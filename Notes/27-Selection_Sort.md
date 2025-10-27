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
    # on the first iteration, i = 0 and we swap the smallest item into position 0
    # on the second iteration, i = 1 and we swap the second smallest item to position 1
    # etc.
    #
    # When there is one item remaining, it must be the maximum and there's nothing to do
    # so the loop can stop one iteration before the end of the list
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
