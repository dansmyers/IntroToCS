"""
Write a function that takes a word as input and returns True if all
of the word's letters are in sorted alphabetical order and returns
False otherwise

ghosty
beefily
ant
abs
fly

Goal: write a loop that can compare elements of the same underlying
sequence to each other

Think about our first version of the for loop

for letter in word:
    # Do something with letter
    
We need the range-based version of the loop so that we can use the index
numbers

for i in range(len(word)):
    # Check if word[i] is alphabetically before or after word[i + 1]
    
Key Idea: the range-based version of the loop is useful when you need to compare
elements of the same string or list to each other

use index numbers to facilitate comparisons of different elements

The basic version is useful when you just need to get the values of each elements
and do something with that element directly
"""


def is_alphabetical(word):
    """
    Return True if the letters of word are in alphabetical order, False otherwise
    """
    
    # range(len(word)) generates the range of numbers from 0 to len(word) - 1
    # When i = len(word) - 1 (that is when i corresponds to the last letter)
    # i + 1 will be len(word), which is beyond the last letter
    #
    # If we run this code using range(len(word)) we'll get an out of bounds
    # exception on the last iteration because i + 1 will be beyond the end of
    # the word
    #
    # What to do instead? Use range(len(word) - 1)
    #
    # If you write a loop and you get an out of bounds exception, that almost
    # always means that you've accidentally tried to access a position beyond
    # the end of the string or list
    #
    # Check your range statement and make sure you're not going too far
    for i in range(len(word) - 1):
        
        # Test if the ith letter is greater than the i + 1 st letter
        if word[i] > word[i + 1]:
            
            # If this condition is satisfied, we've found a pair of consecutive
            # letters that are not in alphabetical order
            return False
    
    # Common construction:  use the loop to test all pairs of consecutive letters
    # If we test all pairs but never return False, then all pairs must be in
    # alphabetical order and we can return True
    return True


### Main
is_alphabetical('dog')
