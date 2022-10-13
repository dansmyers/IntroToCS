# Wordplay

## Setup

Begin by downloading the `words.txt` file posted to Canvas.

Open your Mimir IDE, then use `File ---> Upload` to copy `words.txt` up to your Mimir workspace. You can verify that the upload completed by typing the listing command

```
ls
```

and observing the `words.txt` is now in your home directory along with the `CMS_120` directory.

Make a new directory to hold this lab's programs:

```
mkdir CMS_120/Lab_7
```

Now, **move** the words file into the lab directory. The move command is `mv`, which can also be used to rename files. **Double-check the spelling of your destination
directory before you run the command**. If you type the wrong thing, your file might end up in a different location.

```
mv words.txt CMS_120/Lab_7
```

You cam then `cd` to the lab directory and verify that `words.txt` is there.

```
cd CMS_120/Lab_7

ls
```

## Questions

### Print the words

Our first program will simply print all of the words in the wordlist. There are four interesting pieces here:

- The `open` command creates a connection to a file. `open` takes two arguments: The name of the file and a mode, which is `'r'` for reading in this example (if you 
wanted to write to the file the second argument would be `'w'`; there are a few other option).

- Once the file is open, Python returns a **file handle** that we can use to interact with it. Here, variable `f` stores the handle to the open `words.txt` file.

- A file is a sequence of lines, so we can iterate over them with the `for` loop. The loop in the code below steps through each line in the file one at a time. It's possible
to read from files at a more granular level, like one word or one character at a time, but reading entire lines will work for this lab.

- `line = line.strip()` uses the  built-in `strip` function to remove trailing whitespace from the line. This statement removes the trailing newline character that would 
otherwise create an extra blank line between the words.
  
```
"""
Print the words in the list
"""

# Open the file for reading
f = open('words.txt', 'r')

# Iterate through the lines
for line in f:

    # Strip the terminating newline character
    line = line.strip()
   
    print(line)
```

### Starts with `q`

Let's modify the basic word-printing example to print only the words that start with `q`.

```
"""
Words that start with q
"""

def starts_with_q(word):
    return word[0] == 'q'
    

### Main
f = open('words.txt', 'r')

for line in f:

    # Strip the terminating newline character
    line = line.strip()
    
    if starts_with_q(line):
        print(line)
```

**Use this program as a template for all of the following programs**. Each one of your answers to the following questions should have a **function** that implements
whatever tests are required to answer the problem.


### Starts With `q` But Not `qu`

<img src="https://en.numista.com/catalogue/photos/albanie/5eb334f6befca9.58828003-360.jpg" width="30%" />

*A qindar is a subunit of the lek, Albania's unit of currency*.

Print the words that start with `q` but not `qu`.

### Long words

Recall that you can use `len` to get the number of characters in a string, like so

```
num_chars = len(word)
```

Print all of the words with 18 or more characters.

### Ends With `x`

Recall that there are two ways to access the last character of a word:

```
word[len(word) - 1]

word[-1]
```

Print all of the words that end with `x`

### I'm Thinking of a Word

I'm thinking of a word that starts with `he` and ends with `he`. What could it be?

### No Vowels

<img src=https://upload.wikimedia.org/wikipedia/commons/thumb/9/92/Crwth_rem.jpg/800px-Crwth_rem.jpg width="30%" />

*The Welsh Crwth*

<img src=https://upload.wikimedia.org/wikipedia/commons/9/9f/Western_Cwm_and_Lhotse.jpg width="30%" />

*The Western Cwm (a glaciated valley) on Mt. Everest with the Lhotse Face in the background*

Find all of the words that contain no vowels and no `y`.

Tip:

An easy way to test if a letter is vowel or y is

```
# Test if letter is a vowel or y
if letter in 'aeiouy':
    return False
```

Loop over the characters in the word and test each one to see if it's a vowel. If you find a vowel or a `y`, the test method can immediately `return False`. If you make it all the way through the loop and never find a vowel or `y`, `return True`.


### Abecedarian Words

Let's say that a word is *abecedarian* if its letters are in alphabetical order, allowing for repeated letters. For example, *effort*, *ghosty*, and *beefily* are abecedarian words.

Print all the abecedarian words in the list.

Remember that you can compare characters using the standard relational operators `<` and `>`. All of the words in the list are lowercase, so you don't have to worry about any
upper vs. lower case comparison issues.


### TACOCAT is TACOCAT Backwards

<img src="https://images-wixmp-ed30a86b8c4ca887773594c2.wixmp.com/f/cf45aa02-f54d-4cab-a8e8-4e43c0ed6c74/dcn8689-dc15f569-0e2e-4552-b107-12fc38995653.png?token=eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJzdWIiOiJ1cm46YXBwOjdlMGQxODg5ODIyNjQzNzNhNWYwZDQxNWVhMGQyNmUwIiwiaXNzIjoidXJuOmFwcDo3ZTBkMTg4OTgyMjY0MzczYTVmMGQ0MTVlYTBkMjZlMCIsIm9iaiI6W1t7InBhdGgiOiJcL2ZcL2NmNDVhYTAyLWY1NGQtNGNhYi1hOGU4LTRlNDNjMGVkNmM3NFwvZGNuODY4OS1kYzE1ZjU2OS0wZTJlLTQ1NTItYjEwNy0xMmZjMzg5OTU2NTMucG5nIn1dXSwiYXVkIjpbInVybjpzZXJ2aWNlOmZpbGUuZG93bmxvYWQiXX0.UopOXSHXupOZqB0oUtH4dPwiENGDw3zC1nxStTpzhCM" width="30%" />

Find all the palindromes in the word list.

Tip: Use a loop that compares pairs of letters, starting at the outermost letters (indexes 0 and length - 1) and working inwards. If you find a pair that doesn't match, return `False` immediately. If you succeed in checking all pairs, return `True`.

```
# Calculate the index of the middle letter using integer division
middle = len(word) // 2

for i in range(middle):
    # Check if the letter at position i and its opposite letter are the same
    
    # If not, return False immediately

```

The tricky part: How can you determine the index of the letter that is opposite letter `i`? You can do this by subtracting from `len(word)` or by using negative indexing.

### Triple Double Letters

The word `balloon` has two consecutive pairs of double letters.

I'm thinking of a word that has *three* **consecutive** pairs of double letters. What could it be?
