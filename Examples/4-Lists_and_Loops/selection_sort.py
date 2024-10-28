"""
Example of sorting a list using selection sort
"""

def sort(a):
    """
    Sort the list a

    Returns nothing because the items in a are rearranged in-place
    """

    # Outer loop: finds the smallest remaining item and swaps into each
    # position i
    #
    # Loop stops one position before the last item, because the last
    # item must automatically be the largest in the list
    for i in range(len(a) - 1):

        # Scan through the items from position i up to the end
        # to identify the minimum
        min_value = a[i]
        min_index = i

        for j in range(i + 1, len(a)):
            if a[j] < min_value:
                min_value = a[j]
                min_index = j

        # Swap the minimum into position i
        temp = a[i]
        a[i] = a[min_index]
        a[min_index] = temp


### Main
values = [3, 2, 1, 7, 5, 11, 9]
sort(values)
print(values)
