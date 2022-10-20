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

print("#" * n)
