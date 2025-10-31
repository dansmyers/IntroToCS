# Dictionaries

## Topics

- Maps
- Basic dictionary operations
- Counting letters in the word list
- Key ordering


## Maps

Recall that a list is a sequence of data items, where each position in the list is associated with an index.
```
primes = [2, 3, 5, 7, 11, 13, 17, 19]

first_item = primes[0]
second_item = primes[1]

# etc.
```

Suppose you wanted to scan through a large text document and count the occurrences of words. This problem isn't a good fit for a list, because it's not clear how to map  given word to a specific position in the list.

Instead, you want a different data structure: a **map**, also called a **dictionary**.

A dictionary stores a list of <*key*, *value*> pairs. The basic operation on a dictionary is a lookup. Given a particular key, return its associated value. Examples are ubiquitous:

- A physical dictionary maps a word to a list of its definitions
- A thesaurus maps a word to a list of its synonyms
- A serach engine maps a query string to a list of its associated web pages
- A student database maps an ID string to a set of records about that student

In general, maps are a good fit for any problem where the data can be naturally modeled as a *table*. For example, in the word counting problem, you might have the following data for *Moby Dick*:
```
   word     | count
---------------------
whale       |  1000
the         | 15000
matrimonial |     1
dexterity   |     2
```
The "word" column would correspond to the key in the dictionary and the "count" column to the value.


## Dictionary operations

Use curly braces to declare an empty dictionary.
```
counts = {}
```
Once you have a dictionary, use square bracket notation to assign a key-value pair
```
counts['whale'] = 1000
```
Note that keys aren't required to be strings, although that's the most common case. Technnically, any immutable item can serve as a key in a dictionary. We'll see examples of other kinds of keys later.

You can use a dictionary value in expressions, as you would expect, but the mapping must exist.
```
# Increment an existing entry - this is fine
counts['whale'] += 1

# This line would generate KeyError - the mapping doesn't exist
counts['matrimonial'] += 1
```

You can also declare a set of initial entries when you create the dictionary.
```
counts = {'whale':1000, 'the':15000, 'matrimonial':1, 'dexterity':1}
```

## Counting letters

The program below iterates through the word list and counts the occurrence of each letter.
```
"""
Count letters in the word list
"""

# Empty dictionary
counts = {}

with open('words.txt', 'r') as f:
    for line in f:
        line = line.strip()

        # Iterate through the letters
        for letter in line:
            # If this is the first occurrence of a letter, give it a default entry
            if letter not in counts:
                counts[letter] = 0

            counts[letter] += 1

# Print - for loop can iterate through dictionaries
for key in counts:
    print(key, counts[key])
```

## Key ordering

If you run the program, you'll see output like the following:
```
a 68582
h 20200
e 106758
d 34552
i 77412
n 60513
g 27848
s 86547
l 47011
r 64965
v 9186
k 9370
w 8535
o 54542

# etc.
```
Observe that the ordering doesn't follow any obvious ordering. The keys aren't sorted, nor are the entries sorted by value.

It turns out that, in Python, dictionary keys are returned in the order they were inserted. However, in other languages, like Java, there is no guarantee on the ordering of keys in a dictionary. Therefore, a good rule of thumb is never assume any particular ordering on dictionary keys.
