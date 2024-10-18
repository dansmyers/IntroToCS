"""
Searching a list for a value of interest
"""

def search(a, value):
    """
    Return the first index where value occurs in a, or -1
    """

    for i in range(len(a)):
        if a[i] == value:
            return i

    return -1


### Main
print(search([2, 3, 5, 7, 11, 13, 17, 19], 11))
print(search([2, 3, 5, 7, 11, 13, 17, 19], 8))
