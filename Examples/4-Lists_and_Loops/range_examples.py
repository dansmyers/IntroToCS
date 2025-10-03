"""
Show how to use the range function
"""

# Basic form of the range-driven loop

# Takes one argument, n
# Generates the range from 0 to n - 1
# There are n total numbers in the range

# Challenge: the input value n is not included in the range
# You must remember this

# In older versions of Python, range generated a list of values that
# you would then iterate through -- that could use a lot of memory

# Generates an object that can return numbers in the range on demand

for i in range(101):
    print(i)
    
    
# Second version of range: two arguments, starting value and stopping value

# Count from 2 up to 22

for i in range(2, 23):
    print(i)
    
    
# Loop through the numbers from 1 to 100
# Print each number, except for numbers divisible by 7 print BEEP!
#
# Look at Fizzbuzz problem on the program

for i in range(1, 101):
    if i % 7 == 0:
        print('BEEP!')
    else:
        print(i)


# Third form of range lets you specify a step size in addition
# to the starting and stopping values

# Count from 5 to 50 by fives

for k in range(5, 55, 5):
    print(k)
    
# 6 to 96 by 3
for j in range(6, 99, 3):
    print(j)
    
    
# Write a loop that counts down
#
# You can use this to write loops that count down, but
# it gets a little tricky for negative step sizes other than 1
for c in range(20, 0, -1):
    print(c)


# Using a loop to print out a tower of stars
#
# Given height and width, print a field of stars of the given dimensions
#
# Cool feature: string multiplication

height = 12
width = 8

# Write a loop that iterates over the range specified by height
#
# This loop will run height number of times
for h in range(height):
    print('*' * width)
    

# Key ideas:
#
# Three forms of the range loop: single argument that starts at 0, start and stop,
# start and stop plus step size

# Combine for loop with an if statement to pick out certain numbers from a range

# String multiplication to easily duplicate a string and then using a loop to print
# multiple copies of that string
