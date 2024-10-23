# Wordplay

<img src="https://www.artic.edu/iiif/2/e966799b-97ee-1cc6-bd2f-a94b4b8bb8f9/full/843,/0/default.jpg" width="400px" />

*Starry Night and the Astronauts*, Alma Thomas (1972), via the [Art Institute of Chicago](https://www.artic.edu/artworks/129884/starry-night-and-the-astronauts)

<br/>

This activity is adapted from Allen Downey's [*Think Python*](https://greenteapress.com/thinkpython2/html/thinkpython2010.html).

## Setup

Create a `Lab_9` directory and `cd` into it.

Go onto Canvas and download the `words.txt` file. This is a *large* list of words collected by Grady Smith as part of the Moby lexicon project, an open-source initiative to collect large free datasets for text analysis. Upload the file into your `Lab_9` directory.



## Words

### Print the words

Our first program will simply print all of the words in the wordlist. Put the code below in a file named `print_words.py` and run the program.
```
"""
Print the words in the list
"""

# Open the file for reading
with open('words.txt', 'r') as f:

    # Iterate through the lines
    for line in f:

        # Strip the terminating newline character
        line = line.strip()
   
        print(line)
```
There are four interesting pieces here:

- The `open` command creates a connection to a file. `open` takes two arguments: The name of the file and a mode, which is `'r'` for reading in this example.

- Once the file is open, Python returns a **file handle** that we can use to interact with it. Here, variable `f` stores the handle to the underlying open file.

- The `with` statement wraps the file opening operation. It ensures that the file gets closed cleanly regardless of how the inner code block terminates. If an exception or return occurs, `with` will still close the file before the program terminates.

- A file is a sequence of lines, so we can iterate over them with the `for` loop. The loop in the code below steps through each line in the file one at a time. It's possible to read from files at a more granular level, like one word or one character at a time, but reading entire lines will work for this lab.

- `line = line.strip()` uses the  built-in `strip` function to remove trailing whitespace from the line. This statement removes the trailing newline character that would otherwise create an extra blank line between the words.
  


### Starts with `q`

Let's modify the basic word-printing example to print only the words that start with `q`. Put this code in a file named `starts_with_q.py`.
```
"""
Words that start with q
"""

def starts_with_q(word):
    """
    Returns True if the given word starts with q and False otherwise
    """
    return word[0] == 'q'
    

### Main
with open('words.txt', 'r') as f:
    for line in f:
        line = line.strip()
    
        if starts_with_q(line):
            print(line)
```

**Use this program as a template for all of the following programs**. Each one of your answers to the following questions should have a **function** that implements whatever tests are required to answer the problem.


### Starts with `q` but not `qu`

<img src="https://en.numista.com/catalogue/photos/albanie/5eb334f6befca9.58828003-360.jpg" width="100px" />

*A qindar is a subunit of the lek, Albania's unit of currency*.

<br/>

Print the words that start with `q` but not `qu`.

### Long words

Recall that you can use `len` to get the number of characters in a string, like so

```
num_chars = len(word)
```

Print all of the words with 18 or more characters.

### Ends with `x`

Recall that there are two ways to access the last character of a word:

```
word[len(word) - 1]

word[-1]
```

Print all of the words that end with `x`

### I'm thinking of a word

I'm thinking of a word that starts with `he` and ends with `he`. What could it be?

### Slicing

**Slicing** is a way to pull out a piece of a string (or list) as a substring (or sublist). To take a slice, use a colon in square brackets and specify the range of index positions you want to slice out.
```
# Slice out the characters from index 1, up to BUT NOT INCLUDING index 5
subword = word[1:5]
```
Slicing works similar to `range`: it starts at the beginning index and goes up to, *but doesn't include* the stopping index. In the example above, if the word is `acidic`, the subword would be `cidi`, formed from the characters at positions 1 to 4.

If you slice from the beginning of the string, you don't have to specify 0 as the starting index:
```
# Slice the first two characters
first_two_letters = word[:2]
```
Similarly, you can automatically slice to the end of the string if you don't specify the ending index:
```
last_two_letters = word[len(word) - 2:]
```

Repeat the previous problem, but use slicing to isolate substrings from the beginning and end of the word, then test if both substrings are equal to `'he'`

### No vowels

<img src=https://upload.wikimedia.org/wikipedia/commons/thumb/9/92/Crwth_rem.jpg/800px-Crwth_rem.jpg width="200px" />

*The Welsh crwth*

<img src=https://upload.wikimedia.org/wikipedia/commons/9/9f/Western_Cwm_and_Lhotse.jpg width="300px" />

*The Western Cwm (a glaciated valley) on Mt. Everest with the Lhotse Face in the background*

<br/>

Find all of the words that contain no vowels and no `y`.

Tip: An easy way to test if a letter is vowel or y is
```
# Test if letter is a vowel or y
if letter in 'aeiouy':
    return False
```
Loop over the characters in the word and test each one to see if it's a vowel. If you find a vowel or a `y`, the test method can immediately `return False`. If you make it all the way through the loop and never find a vowel or `y`, `return True`.


### Abecedarian words

Let's say that a word is *abecedarian* if its letters are in alphabetical order, allowing for repeated letters. For example, *effort*, *ghosty*, and *beefily* are abecedarian words. Print all the abecedarian words in the list.

Remember that you can compare characters using the standard relational operators `<` and `>`. All of the words in the list are lowercase, so you don't have to worry about any upper vs. lower case comparison issues.


### TACOCAT is TACOCAT backwards

<img src="https://images-wixmp-ed30a86b8c4ca887773594c2.wixmp.com/f/cf45aa02-f54d-4cab-a8e8-4e43c0ed6c74/dcn8689-dc15f569-0e2e-4552-b107-12fc38995653.png?token=eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJzdWIiOiJ1cm46YXBwOjdlMGQxODg5ODIyNjQzNzNhNWYwZDQxNWVhMGQyNmUwIiwiaXNzIjoidXJuOmFwcDo3ZTBkMTg4OTgyMjY0MzczYTVmMGQ0MTVlYTBkMjZlMCIsIm9iaiI6W1t7InBhdGgiOiJcL2ZcL2NmNDVhYTAyLWY1NGQtNGNhYi1hOGU4LTRlNDNjMGVkNmM3NFwvZGNuODY4OS1kYzE1ZjU2OS0wZTJlLTQ1NTItYjEwNy0xMmZjMzg5OTU2NTMucG5nIn1dXSwiYXVkIjpbInVybjpzZXJ2aWNlOmZpbGUuZG93bmxvYWQiXX0.UopOXSHXupOZqB0oUtH4dPwiENGDw3zC1nxStTpzhCM" width="30%" />

Find all the palindromes in the word list. Use a function called `is_palindrome` that takes `word` as input and returns `True` if it is a palindrome. Don't use any function that reverses the word.

Tip: Use a loop that compares pairs of letters, starting at the outermost letters (indexes 0 and `len(word) - 1`) and working inwards. If you find a pair that doesn't match, return `False` immediately. If you succeed in checking all pairs, return `True`.

```
# Calculate the index of the middle letter using integer division
middle = len(word) // 2

for i in range(middle):
    # Check if the letter at position i and its opposite letter are the same
    
    # If not, return False immediately

```
The tricky part: How can you determine the index of the letter that is opposite letter `i`? Think about subtracting from `len(word)` or by using negative indexing.

### Triple double letters

The word `balloon` has two consecutive pairs of double letters.

I'm thinking of a word that has *three* **consecutive** pairs of double letters. What could it be?


### Vowels in order

The word `specious` contains all of `e`, `i`, `o`, and `u` in that order.

Find a word that contains the letters `a`, `e`, `i`, `o`, and `u` *in that order*. The letters may not be consecutive.

Tip: There is a built-in method called `index` that you can use to find the index position of a particular value in a sequence. Look it up and think about how you could use it to test for the presence of every vowel and how to verify that they're in order.



## Edifice Complex

<img src="https://upload.wikimedia.org/wikipedia/en/1/1c/Iron_Maiden_-_Powerslave.jpg" width="300px" />

<br/>

### Descending a Staircase

Write a program named `stairs.py` with a method that prints a descending staircase like the one below. Prompt the user to enter the height of the staircase.

```
#
##
###
####
#####
```
Tip: Let the entered height be `n`. Use a loop with `range(n)` to run for `n` total iterations. Print 1 block on the first line, two blocks on the second, and so forth.

You can use string multiplication to copy a string multiple times. If `i` is the loop counting variable, you could use:
```
print('#' * (i + 1))
```


### Reverse staircase

Modify your previous program to reverse the stairs.
```
    #
   ##
  ###
 ####
#####
```

Tip: Print a number of spaces, then a number of blocks. Think about how many spaces and blocks you need as a function of `n` and the loop counter `i`. For example, if `n` is 5, then

- Line 1 has four spaces and one block
- Line 2 has three spaces and two blocks
- Line 3 has two spaces and three blocks

and so forth.

Tip-tip: `print` can take a special parameter called `end` that specifies what to put at the end of its output. Normally, this is a newline, but you can avoid moving to the next line automatically if you set `end=''`.
```
# Example: print 5 spaces, staying on the same line, then 3 blocks
print(' ' * 5, end='')
print('#' * 3)
```

### Look On My Works, Ye Mighty, and Despair!


Write a program named `pyramid.py` that can print pyramids of stars like the following:
```
    *
   ***
  *****
 *******
*********
```
Prompt the user to enter the height of the pyramid.

Tip: Use variables to keep track of the number of spaces and number of stars you need to print on each line. After you print, decrease spaces by one and increase stars by two.
```
n = input('How high shall the pyramid be, my pharoah?')

# TODO: determine the number of stars and spaces on the first level as a function of n
spaces =
stars =

# Loop for n levels
for i in range(n):
    # Print spaces and stars for line i

    # Update spaces and stars for the next line
    spaces -= 1
    stars += 2

```

### Hoard

Of course, my pyramid must be hollow inside to hold all of the precious objects that will accompany me to the Afterlife.

```
    *
   * *
  *   *
 *     *
*********
```
Modify your previous program to print hollow pyramids. Put your solution in a file named `hollow.py`.

Think: Think about how many spaces you need to print on each line. You may want to treat the last line as a special case with an `if` statement.


### Fancy pyramid

Make one more pyramid that alternates spaces and stars.
```
    *
   * *
  * * *
 * * * *
* * * * *
```
