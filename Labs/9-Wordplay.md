## Edifice Complex

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

Tip: Print a number of spaces, then a number of blocks. Think about how many spaces you need as a function of `n` and the loop counter `i`. If `n` is 5, then

- Line 1 has four spaces and one block
- Line 2 has three spaces and two blocks
- Line 3 has two spaces and three blocks

and so forth.

Tip-tip: `print` can take a special parameter called `end` that specifies what to put at the end of its output. Normally, this is a newline, but you can avoid moving to the next line automatically if you set `end=''`.
```
# Print 5 spaces, staying on the same line, then 3 blocks
print(' ' * 5, end='')
print('#' * 3)
```

### Look On My Works, Ye Mighty, and Despair!

<img src="https://upload.wikimedia.org/wikipedia/en/1/1c/Iron_Maiden_-_Powerslave.jpg" width="300px" />

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
