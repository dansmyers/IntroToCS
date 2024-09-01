# Lab 2 &ndash; Variables and Input

## Setup

Open your GitHub Codespace. Look at your path and verify that your shell is in the normal starting home directory, then create a new `Lab_2` directory using
```
mkdir Lab_2
```
Change to the lab directory:
```
cd Lab_2
```
You can then create new files using `touch`. For example, to create a file named `temp.py` for the first problem, use
```
touch temp.py
```


## Problems

### Guidelines

- Put every problem into its own `.py` file

- Start every program with a comment describing what it's supposed to do

- Use `input` to read values from the teminal. Remember that the value returned by `input` is **a string**. You can convert an input value into integer using
```
user_input = input('Enter a number: ')
value = int(user_input)
```


### Temperature Conversion

A classic example.

To convert a temperature of *F* degrees Fahrenheit into Celsius, use

```
C = (F - 32) * (5 / 9)
```

Write a program that can read an **integer** number of degrees Fahrenheit from the terminal and report the corresponding number of degrees Celcius.
Output your results to **one decimal place**.


### Furlongs


A furlong is an archaic unit of length defined to be one-eigth of a mile (660 feet).

Write a program that can read a length in feet and convert it to units of fulongs. Print your results to one decimal place.

You may assume that the user will enter a valid length.

Tip:

Assume that the input may be fractional. To read fractional input, use

```
user_input = input()
feet = float(user_input)
```


### The Magic Computers

<img src="https://miro.medium.com/max/2100/1*8M2JfaTacGjI8YQlO9qF5A.jpeg" width="50%" />

Mad Libs are a word completion game originally invented in 1953 by two New Yorkers, Leonard Stern and Roger Price, who went on to publish a series of best-selling books based on the concept.

Each Mad Lib is an incomplete short story, where some of the words have been replaced by blanks, each labeled with a part of speech. One player asks the others for words to fill in the blanks, then reads the complete story. Hilarity ensues.

Write a program to implement the "Magic Computers" Mad Lib given above. Use the input function to prompt the user to enter words of each type, then combine all of the answers together to print the finished story. Here's a little bit to help you get started:

```

"""
The Magic Computers: a Mad Lib
"""

# Prompt the user to enter all of the required words
noun1 = input('Enter a noun: ')
plural_noun1 = input('Enter a plural noun: ')

# Add more cases for the other blanks...

# Print out the story with the user's words mixed in
# %s is the format specifier for a string variable
# This is an easy way to mix string variables in with other output

print('Today, every student has a computer small enough to fit into his %s.' % noun1)
print('He can solve any math problem by simply pushing the computer\'s little %s.' % plural_noun1)

# Add more print statements for the rest of the story...
```

Tip: The last sentence has multiple blanks. You can print multiple variables in a single statement as follows:

```
print('Others have a/an %s screen that shows all kinds of %s and %s figures.' % (adj1, plural_noun2, adj2))
```

Python puts the first variable (`adj1`) in place of the first `%s`, the second variable (`plural_noun2`) in place of the second `%s`, and so forth.


### The Weight

<img src="https://staticg.sportskeeda.com/wp-content/uploads/2016/08/1-1470306645-800.jpg" width="50%" />

Write a program to read in a weight in kilograms and convert it to pounds. There are about 2.20462 pounds in one kilogram.
Display the result to one decimal place.

The current world record for weight lifted overhead in the clean and jerk is 263.5 kg, held by the vending-machine-sized Iranian superheavy
weightlifter [Hossein Rezazadeh](https://www.youtube.com/watch?v=FOE-PZJq2sk). Use your program to calculate the weight of Rezazadeh's record lift 
in pounds.


### Mystery Operator

Python supports a special operator, `%`, which is called the **modulus operator**.

Run the Python prompt in your terminal by typing `python3` and pressing `ENTER`. Try some calculations using the modulus operator
and see what results you get:

```
7 % 3
12 % 5
19 % 7
2 % 2
```

Can you figure out what the mod operator does? Hint: it has something to do with division.

Press `CTRL + d` to exit the Python prompt and return to your regular terminal.


### Number Fail

Recall that all of the data in our Python programs must ultimately be stored on a real, physical computer. This implies that there must be **limitations** for the range and precision of values that can be represented in code.

Run the `python3` prompt again and output the following calculation. Do you get the right answer?

```
.1 + .2
```

This is an example of **numerical error**: floating point numbers (the `float` type) can only represent some numbers approximately so 
calculations involving fractions may have very small errors.

Find another example using `float` arithmetic that doesn't give the exact result you would expect.


### Comrades

<img src="https://ultra-x.co/wp-content/uploads/2020/01/comrades-marathon-africa-ultra-x.jpg" width="50%" />

Write a program that can read in a number of kilometers as input and print the corresponding number of miles. There are
1.60934 kilometers in one mile.

The Comrades Marathon in South Africa is the world's oldest and largest ultramrathon race, established in 1921. 
It is run between the cities of Durban and Pietermaritzburg in South Africa, a distance of about 87 km. The race was cancelled in 2020, but more than 25000 
people participate during a normal year. The direction alternates every year, with the course beginning in Durban being mostly uphill and the other direction being mostly downhill, so there are actually two records for the course.

What is the length of Comrades Marathon in miles?


### Binet's Formula

Recall the famous Fibonacci sequence, where each term is the sum of the previous two terms.

```
0, 1, 1, 2, 3, 5, 8, 13, 21, ...
```

Suppose you would like to calculate the Nth Fibonacci number. How could you do that? One way is to start at the base case and grind your way up through the sequence until you've calculated N total terms. 

It turns out there is a single formula that will calculate the terms of the Fibonacci sequence. This is weird and suprising, because it seems unlikely that such a highly structured sequence, where each term depends on all the previous terms, could be represented in closed form.

The result is known as Binet's formula and it says that the Nth Fibonacci number `F_n` is

<img src="https://latex.artofproblemsolving.com/8/6/d/86d486c560727727342090b432e23ba85ac098b1.png" width="30%"/>

Gnarly.

The number `(1 + sqrt(5)) / 2` is the famous golden ratio, the most aesthetically pleasing of all proportions. It's sometimes denoted by the Greek letter φ (phi) after the ancient architect and sculptor Phidias, who used it in planning the design of the Parthenon.

<img src="https://lp-cms-production.imgix.net/2019-09/ab57ac3775d90a72da514d158401bd47-parthenon.jpg" width="35%" />

*much columns  such proportions*

Write a program that reads an integer `n` from the user and prints the corresponding term in the Fibonacci sequence. Test your program by inputting values of `n` from 0 up to 10 and verifying that you get the correct Fibonacci numbers.

Tips:

**Use variables to break up the calculation**. Don't try to do everything in one line! I recommend making one variable for each term and calculated value.

You'll need the ability to take square roots and calculate powers. Use the built-in `**` operator to calculate powers. There is a built-in square root function that you can import into your program by adding the following line to the top of your code:

```
from math import sqrt
```

You can then call the functions like so

```
phi = (1 + sqrt(5)) / 2  # sqrt(5) calculates the square root of 5
phi_to_the_n = phi ** n  # Calculate phi to the power n
```
