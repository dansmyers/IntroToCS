# Euouae

<img src="https://miro.medium.com/v2/resize:fit:1400/format:webp/1*NlSMDSt5QOaGblOH7zU4BA.png" width="750px" />

*Kitchen*, Liza Lou (1991-1996), via the [Whitney Museum](https://whitney.org/collection/works/34855) and [this review article](https://rachelletaj.medium.com/reviewing-liza-lou-the-kitchen-1991-a9b541d18c2f)

> A full-scale and exactingly detailed kitchen encrusted in a rainbow of glistening beads, Liza Lou’s monumental installation took five years to make. After researching kitchen design manuals as well as historical tracts about the lives of nineteenth-century women, Lou made drawings and three-dimensional models to achieve a loose outline of Kitchen’s floor plan. She then fashioned the objects out of paper mâché, painted them, and applied the beads in a mosaic of surface pattern.

## Setup

Create a `Lab_7` directory and `cd` into it:
```
mkdir Lab_7
```
```
cd Lab_7
```

## Loop Practice


### Beep Boop

Write a program that loops through the numbers 7 to 77 and prints each number, except:

- For numbers divisible by 7 print `Beep`
- For numbers divisible by 4 print `Boop`
- For numbers divisible by both 7 and 4 print `BeepBoop`


### Multiplication tables

The program below uses a pair of nested loops to print a 5x5 table of products
```
"""
Example of nested loops
"""
for a in range(1, 6):
    for b in range(1, 6):
        print(a * b, end='\t')

    print() # Go to the next line
```
Run the program and observe what it prints out. The statement
```
print(a + b, end='\t')
```
Prints `a + b`, but ends the output with a tab character, rather than the normal behavior of moving to the next line.

When working with a pair of `for` loops, remember that the inner loop runs through all of its values for each value of the outer loop. In this case, the outer loop sets `a = 1`, then runs through the entire inner loop for `b`, then sets `a = 2` and runs the entire inner loop a second time, and so forth.

Modify the program to print a 12x12 multiplication table.


### All vowels

<img src="https://upload.wikimedia.org/wikipedia/commons/5/5c/LiberUsualisEuouae.jpg" width="300px" />

*Example of medieval plainchant music showing the euouae mnemonic, from Wikipedia*

<br/>

[The longest all-vowel word](https://www.grammarly.com/blog/14-of-the-longest-words-in-english) in English is *euouae*: a mnemonic which was used in medieval music to denote the sequence of tones in the ending of the Gloria Patri, which ends with the phrase *In saecula saeculorum, Amen*. In Latin psalters and plainchant books, the melodic formula to be sung at the end of every chanted line (called the *differentia*), would be written over the letters EUOUAE, representing the vowels of *saeculorum Amen*.

Write a function called `has_only_vowels` that takes a string named `s` as input and returns `True` if the string contains only vowels letters and `False` if it contains any non-vowel letters. You can assume that `s` contains only lowercase letters.

Here is a starting program:
```
"""
Test if a string has only vowels
"""

def has_only_vowels(word):
    # Loop through the letters of word

        # Test if the letter is NOT a vowel
        #
        # If you find a non-vowel, return False immediately

    # If you finish the loop, return True

### Main
test_word = 'euouae'

if has_only_vowels(test_word):
    print(f'{test_word} has only vowels.')
else:
    print(f'{test_word} has non-vowels.')
```

Tip: you can check if a letter `c` is not in the set of vowels using
```
if c not in 'aeiou':
    # Do something if c is not a vowel
```


## List practice


### Filling a list
Write a program that creates an empty list, then uses a loop to fill it with the values from 1 to 100.
```
"""
Filling a list with a loop
"""

# Empty starting list
numbers = []

# Loop through the values 1 to 100 and append each value to numbers


# Print the result
```

### List comprehensions

A *list comprehension* is a convenient way to generate a list in a single line using a loop. The previous question could be answered in a single line using:
```
numbers = [i for i in range(1, 101)]
```
This statement use the `for` loop to iterate through the range of numbers 1 to 100, and collects each value of `i` into a list. The result is a list containing the values `[1, 2, 3, 4, ... , 100]`.

You can use comprehensions to generate different kinds of lists. For example, to generate list of 0/1 coin flips you could write
```
flips = [round(random()) for i in range(100)]
```
The loop runs 100 times. Each iteration generates a random value from 0.0 to 1.0 and then rounds it to either 0 or 1. The result is a list of 100 values that are either 0 or 1. For example, `[0, 0, 1, 0, 1, 1, 1, 0, ...]`.

Write a script that uses list comprehensions to initialize each of the following. Print each list to check your results.

- A list of the numbers  1 to 25
- A list of the numbers -10 to 10
- A list of the even numbers 2, 4, 6, 8, ... 100
- A list of the values .01, .02, .03, .04, ..., .98, .99. Tip: think about looping from 1 to 100 and then dividing each value of `i` by 100.
- A list of 10 boolean values that are all `False`

### Tape

The program below illustrates a few major list methods. Modify it to create your own mixtape. Add additional calls to `remove`, `insert`, and `pop` to practice manipulating the list.
```
"""
Make a mixtape - inspired by a Codecademy's taylor.swift project
"""

def tape():
    print(".------------------------.   ")
    print("|     YACHT ROCK MIX     |   ")
    print("|     __  ______  __     |   ")
    print("|    /  \\|\\.....|/  \\    |")
    print("|    \\__/|/_____|\\__/    | ")
    print("|    ________________    |   ")
    print("|___/_._o________o_._\\___|  ")

    print()
    

### Main

# Totally gratuitous ASCII art
tape()

# Create an empty list to hold the songs
songs = []

# Use the .append method to add an element to the end of the list
#
# Key idea: think of the dot as representing a message or a command
# given to the list of songs
# 
# "songs, I need you to append this new value to yourself!"
songs.append('Toto - Africa')
songs.append('Steely Dan - Peg')
songs.append('Christopher Cross - Sailing')
songs.append('Hall and Oates - I Can\'t Go For That (No Can Do)')
songs.append('Michael McDonald - What a Fool Believes')

# Use the remove method to remove the first item with the given value
songs.remove('Michael McDonald - What a Fool Believes')

# Use insert to put a new item at a given index
#
# Remember: the first position is index 0, the second is index 1, etc.
songs.insert(2, 'Donald Fagen - I.G.Y.')

# Use pop to remove and return the item at a given position
africa = songs.pop(0)

# Final list
print(songs)
```


## Edifice Complex

<img src="https://upload.wikimedia.org/wikipedia/en/1/1c/Iron_Maiden_-_Powerslave.jpg" width="300px" />

<br/>

### Descending a staircase

Write a program named `stairs.py` with a method that prints a descending staircase like the one below. Prompt the user to enter the height of the staircase.

```
#
##
###
####
#####
```
Tip: Let the entered height be `n`. Use a loop with `range(1, n + 1)` to run for `n` total iterations. Print one block on the first line, two blocks on the second, and so forth. Think about how to calculate the number of blocks on each line using the loop counting variable `i`.

Here's some starting code:
```
"""
Staircase
"""

# Prompt the user to enter the height
n = int(input('Enter the height of the staircase: '))

# Loop from 1 to n
for i in range(1, n + 1):

    # Print n total blocks
```

Tip: You can use string multiplication to copy a string multiple times. If `i` is the loop counting variable, you could use:
```
print('#' * i)
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

and so forth. Here is a sketch of the program.
```
"""
Reverse staircase
"""
n = int(input('Enter the height: '))

for i in range(n):
    # TODO: calculate number of spaces and number of blocks on line i using n and i

    # TODO: print spaces and blocks
```

Tip-tip: `print` can take a special parameter called `end` that specifies what to put at the end of its output. Normally this is a newline, but you can avoid moving to the next line automatically if you set `end=''`.
```
# Example: print 5 spaces, staying on the same line, then 3 blocks
print(' ' * 5, end='')
print('#' * 3)
```

### Look on my works, ye mighty, and despair!

<img src="https://upload.wikimedia.org/wikipedia/commons/thumb/2/26/Bent_Pyramid_%E6%9B%B2%E6%8A%98%E9%87%91%E5%AD%97%E5%A1%94_-_panoramio.jpg/1920px-Bent_Pyramid_%E6%9B%B2%E6%8A%98%E9%87%91%E5%AD%97%E5%A1%94_-_panoramio.jpg" width="300px" />

*The "Bent Pyramid" of Sneferu. One of the early pyramids, before the art was perfected. The builders were forced to reduce the slope from 54 degrees to 43 degrees partway through the construction.*

<br/>


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
n = int(input('How high shall the pyramid be, my pharoah?'))

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

Tips: Think about three cases for the first line, the last line, and the middle lines. Use an `if`-`elif`-`else` structure inside your loop and think about how to keep track of the number of interior spaces on the middle lines.

### I'm so fancy

<img src="https://wreg.com/wp-content/uploads/sites/18/2023/08/Skyline-Sunset.jpg?w=900" width="400px" />

*The world's tenth largest pyramid is located in Memphis, TN and contains a Bass Pro Shops. It used to have [crystal skull](https://www.forbes.com/sites/joesills/2020/08/26/the-unbelievable-true-story-of-how-the-memphis-pyramid-became-a-bass-pro-shops/) at the top. During the time the University of Memphis used it as a basketball arena it was nicknamed the "Tomb of Doom". Image from WREG*.

<br/>

Make one more fancy pyramid that alternates spaces and stars.
```
    *
   * *
  * * *
 * * * *
* * * * *
```
