"""
The basics of lists
"""

# Declare a list of values using square brackets
fruits = ['apple', 'banana', 'cherry', 'durian', 'eggplant', 'fig']


# Printing a list prints all of its values
print(fruits)


# Individual elements are accessed using [ ] and an index value
#
# LIST INDEXING IN PYTHON STARTS FROM ZERO!
#
# The first element has index 0
# The second element has index 1
# The third element has index 2
# And so forth

print(fruits[0])  # prints 'apple'
print(fruits[1])  # prints 'banana'
print(fruits[2])  # prints 'cherry'


# Lists are MUTABLE -  You can reassign list elements using square brackets and indices
fruits[3] = 'dragon fruit'


# Use the built-in len() function to get the lengtg of a list
print(len(fruits))  # Prints 6


# The last item of a list is always at index length - 1
print(fruits[len(fruits) - 1])  # Prints 'fig'


# Special Python trick: negative indexing!
#
# fruits[-1] is the last element in the list
# fruits[-2] is the second to last element
# And so forth
print(fruits[-1])  # Prints 'fig'
