"""
Demonstrate looping over strings
"""

# Strings in Python are considered to be a sequence of characters

# You can access individual characters in a string using [ ] and index numbers
# just like a list

word = 'queueing'

# Can you test if a word starts with q but not qu?

if word[0] == 'q' and word[1] != 'u':
    print("starts with q but not qu")
else:
    print('does not satisfy the quality of being a word that starts with q but not qu')
    
# Use the for loop to iterate over the characters in a string

s = 'Hello, World!'

for ch in s:
    print(ch)
