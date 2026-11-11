"""
Find the anagrams in the word list

Demonstrates using tuples of sorted letters as keys in a dictionary
"""

# Open the words.txt file
f = open('../4-Loops/words.txt', 'r')

# Declare an empty anagrams dictionary
anagrams = {}

# Loop through the line
for line in f:
    line = line.strip()

    # Break the current line into characters and sort them
    letters = list(line)
    letters.sort()

    # Turn the sorted letter into a tuple key
    key = tuple(letters)

    # If anagrams doesn't contain an entry for this letter sequence
    # then initialize one
    if key not in anagrams:
        anagrams[key] = []

    # Add the current word to its entry in the anagrams dict
    anagrams[key].append(line)


for key in anagrams:
    if len(anagrams[key]) > 1:
        print(key, anagrams[key])
