# Euouae

<img src="https://whitneymedia.org/assets/artwork/34855/2008_339a-x_vw1_cropped.jpeg" width="400px" />

*Kitchen*, Liza Lou (1991-1996), via the [Whitney Museum](https://whitney.org/collection/works/34855)

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

<img src="https://whitneymedia.org/assets/artwork/34855/LMA_LizaLou_0205.jpeg" width="400px" />


### Beep Boop

Write a program that loops through the numbers 7 to 77 and prints each number, except:

- For numbers divisible by 7 print `Beep`
- For numbers divisible by 4 print `Boop`
- For numbers divisible by both 7 and 4 print `BeepBoop`


### Multiplication tables

The program below uses a pair of nested loops to print a 5x5 table of sums.
```
"""
Example of nested loops
"""
for a in range(1, 6):
    for b in range(1, 6):
        print(a + b, end='\t')

    print() # Go to the next line
```
Run this program and observe what it prints out. The statement
```
print(a + b, end='\t')
```
Prints `a + b`, but ends the print statement with a tab character instead of the normal newline.

When working with a pair of `for` loops, remember that the inner loop runs through all of its values for each value of the outer loop. In this case, the outer loop sets `a = 1`, then runs through the entire inner loop for `b`, then sets `a = 2` and runs the entire inner loop a second time, and so forth.

Modify the program to print a 12x12 multiplication table.

### Project Euler #6

The sum of the squares of the first ten natural numbers is,

1<sup>2</sup> + 2<sup>2</sup> + 3<sup>2</sup> + ... + 10<sup>2</sup> = 385

The square of the sum of the first ten natural numbers is,

(1 + 2 + 3 + ... + 10)<sup>2</sup> = 3025

Hence the difference between the sum of the squares of the first ten natural numbers and the square of the sum is

3025 - 385 = 2640.

Find the difference between the sum of the squares of the first one hundred natural numbers and the square of the sum.



### All vowels

<img src="https://upload.wikimedia.org/wikipedia/commons/5/5c/LiberUsualisEuouae.jpg" width="300px" />

*Example of medieval plainchant music showing the euouae mnemonic, from Wikipedia*

<br/>

[The longest all-vowel word](https://www.grammarly.com/blog/14-of-the-longest-words-in-english) in English is *euouae*: a mnemonic which was used in medieval music to denote the sequence of tones in the ending of the Gloria Patri, which ends with the phrase *In saecula saeculorum, Amen*. In Latin psalters and plainchant books, the melodic formula to be sung at the end of every chanted line (called the *differentia*), would be written over the letters EUOUAE, representing the vowels of *saeculorum Amen*.

Write a function called `has_only_vowels` that takes a string named `s` as input and returns `True` if the string contains only vowels letters and `False` if it contains any non-vowel letters. You can assume that `s` contains only lowercase letters.

Tip: you can check if a letter `c` is not in the set of vowels using

```
if c not in 'aeiou':
    # Do something if c is not a vowel
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
Tip: Let the entered height be `n`. Use a loop with `range(n)` to run for `n` total iterations. Print one block on the first line, two blocks on the second, and so forth.

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

Tip-tip: `print` can take a special parameter called `end` that specifies what to put at the end of its output. Normally this is a newline, but you can avoid moving to the next line automatically if you set `end=''`.
```
# Example: print 5 spaces, staying on the same line, then 3 blocks
print(' ' * 5, end='')
print('#' * 3)
```

### Look On my works, ye mighty, and despair!

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


### I'm so fancy

Make one more fancy pyramid that alternates spaces and stars.
```
    *
   * *
  * * *
 * * * *
* * * * *
```
