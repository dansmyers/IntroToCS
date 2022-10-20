# Edifice Complex

## Descending a Staircase

Write a program with a method that prints a descending staircase like the one below. Prompt the user to enter the height of the staircase.

```
#
##
###
####
#####
```

Use a counting loop for the number of lines. Inside that loop, print the appropriate number of blocks for the line. If you start counting at 1, line `n` has `n` blocks.

Here's a complete output example:

```
Enter height:
5
#
##
###
####
#####
```

Tip

Remember that you can use string multiplication to concatenate multiple copies of a string together. For example, to print a pound character n times on one line, you could use

```
print("#" * n)
```


## Look On My Works, Ye Mighty, and Despair!

<img src="https://upload.wikimedia.org/wikipedia/en/1/1c/Iron_Maiden_-_Powerslave.jpg" width="30%" />

https://www.poetryfoundation.org/poems/46565/ozymandias

Write a program that can print pyramids of stars like the following:

```
    *
   ***
  *****
 *******
*********
```

Use the `input` function to read the height of the pyramid.

Tip: the first level has `height - 1` spaces and 1 star. The second has `height - 2` spaces and 3 stars. In general, line `i` has

```
height - i spaces
2 * i - 1 stars
```

Use a loop over the levels of the pyramid, then use string multiplication to print the appropriate numbers of spaces and stars on each line.

To print the spaces without moving to the next line you can use

```
print(' ' * num_spaces, end='')   # assume num_spaces is the number you want to print
```

## Hoard

Of course, my pyramid must be hollow inside to hold all of the precious objects that will accompany me to the Afterlife.

```
    *
   * *
  *   *
 *     *
*********
```

Modify your previous program to print hollow pyramids.

