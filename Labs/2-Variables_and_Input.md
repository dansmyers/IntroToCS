# Variables and Input

<img src="https://preview.redd.it/remote-login-is-a-lot-like-astral-projection-v0-qhyr8o9bgq191.png?width=1080&crop=smart&auto=webp&s=2b4aa5c4a9236864f3450ec31d338f45b2322294" width="400px" />

*The Internet Guide for New Users*, Daniel P. Dern (1994)


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

- Put every problem into its own `.py` file.

- Start every program with a docstring comment in triple quotes describing what it's supposed to do. Use regular single-line comments in your code to explain what each line or small group of lines is doing.

- Use `input` to read values from the teminal. Remember that the value returned by `input` is **a string**. You can convert an input value into a float using
```
user_input = input('Enter a number: ')
value = float(user_input)
```


### Temperature Conversion

A classic example. To convert a temperature of *F* degrees Fahrenheit into Celsius, use

```
temp_in_c = (temp_in_f - 32) * (5 / 9)
```

Write a program that can read a decimal number of degrees Fahrenheit from the terminal and report the corresponding number of degrees Celcius.
Output your results to **one decimal place**.

Tip:

Here's a template to help you get started. Use this as a model for the rest of the programs.

```
"""
Convert temperature from degrees Fahrenheit to degrees Celsius
"""

# Read a temp in degrees Fahrenheit using input()


# Convert the input string to a float using float()


# Perform the calculation


# Print the output using .1f as the format
```


### Furlongs


A furlong is an archaic unit of length defined to be one-eigth of a mile (660 feet), still sometimes used for horse racing. Write a program that can read a length in feet and convert it to units of fulongs. Print your results to one decimal place. You may assume that the user will enter a valid length.

Tip: Use the same basic approach as the previous problem.



### The Weight

<img src="https://upload.wikimedia.org/wikipedia/commons/thumb/1/1d/Weightlifting_at_the_2020_Summer_Olympics_%E2%80%93_Men%27s_%2B109_kg_%2810%29.jpg/620px-Weightlifting_at_the_2020_Summer_Olympics_%E2%80%93_Men%27s_%2B109_kg_%2810%29.jpg" width="300px" />

Write a program to read in a weight in kilograms and convert it to pounds. There are about 2.20462 pounds in one kilogram.
Display the result to one decimal place.

The current all-time world record for weight lifted overhead in the clean and jerk is 267 kg (589 pounds), held by the vending-machine-sized (6' 6" and 403 pounds) Georgian superheavy weightlifter Lasha Talakhadze. Use your program to calculate the weight of Talakhadze's record lift  in pounds.


### Fake Internet Meme Money

<img src="https://external-preview.redd.it/3_iVT6i7dReTdMXS-bNiIS0U9p2QTsfq6BUDC57b8tc.jpg?auto=webp&s=5943d7cf04be56a4de8cf045667e41631c02a90e" width="35%" />

Dogecoins, the favored cryptocurrency of shiba inus everywhere, currently trades for about .33 USD per DOGE.

Write a program that reads a number of DOGE as input, then prints the corresponding amount of USD to two decimal places. Think about the conversion and whether you need to multiple or divide.

Tip:

When working with constants such as a conversion factor, it's common to write the name in `ALL_CAPS`, to indicate that the variable is a constant that shouldn't be reassigned later in the program.

```
"""
Convert DOGE to USD
"""

# Define conversion factor as a constant
USD_PER_DOGE = .33

# Read input number of DOGE

# Convert input string to a number

# Calculate USD using conversion factor constant

# Print to two decimal places

```


### The Magic Computers

<img src="https://miro.medium.com/max/2100/1*8M2JfaTacGjI8YQlO9qF5A.jpeg" width="50%" />

Mad Libs are a word completion game originally invented in 1953 by two New Yorkers, Leonard Stern and Roger Price, who went on to publish a series of best-selling books based on the concept. Each Mad Lib is an incomplete short story, where some of the words have been replaced by blanks, each labeled with a part of speech. One player asks the others for words to fill in the blanks, then reads the complete story. Hilarity ensues.

Write a program to implement the "Magic Computers" Mad Lib given above. Use the input function to prompt the user to enter words of each type, then combine all of the answers together to print the finished story. Here's a little bit to help you get started:

```
"""
The Magic Computers: a Mad Lib
"""

# Prompt the user to enter all of the required words
noun1 = input('Enter a noun: ')
plural_noun1 = input('Enter a plural noun: ')

# Add more cases for the other blanks...


print(f'Today, every student has a computer small enough to fit into his {noun1}.')
print(f'He can solve any math problem by simply pushing the computer\'s little {plural_noun1}.')

# Add more print statements for the rest of the story...
```

Tip: the last sentence has multiple blanks. You can use a formatted print string with multiple variable names, each enclosed in curly braces:
```
print(f'Others have a/an {adj1} screen that shows all kinds of {plural_noun2} and {adj2} figures.')
```

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

When you're done, use `CTRL + d` to exit the Python prompt and return back to the regular terminal.


### Comrades

<img src="https://ultra-x.co/wp-content/uploads/2020/01/comrades-marathon-africa-ultra-x.jpg" width="50%" />

Write a program that can read in a number of kilometers as input and print the corresponding number of miles. There are
1.60934 kilometers in one mile. Use a constant conversion factor named `KM_PER_MILE`:
```
# Constant conversion factor of kilometers per mile
KM_PER_MILE = 1.60934
```

The Comrades Marathon in South Africa is the world's oldest and largest ultramrathon race, established in 1921. 
It is run between the cities of Durban and Pietermaritzburg in South Africa, a distance of about 87 km. The race typically attracts more than 25000 partcipants. The direction alternates every year, with the course beginning in Durban being mostly uphill and the other direction being mostly downhill, so there are actually two records for the course.

Use your program to calculate the length of the Comrades marathon in miles.


### Heron's Formula


**Heron's formula** (named after the Greek mathematician and inventor Hero of Alexandria) is a method of calculating the area of a triangle given the lengths of its three sides. If the three side lengths are *a*, *b*, and *c*, the formula is:

<img src="https://wikimedia.org/api/rest_v1/media/math/render/svg/d138044bb9ed870dd9dc5c7c8a3c07ab1db1705d" width="20%" />

where *s* is the "semi-perimeter":

<img src="https://wikimedia.org/api/rest_v1/media/math/render/svg/08ed8a6e351198e0c4ca8d71fa2e2bc4171e9439" width="10%" />

Write a program named `heron.py` that prompts for three float inputs. Save the three inputs to variables named `a`, `b`, and `c`, then calculate and print the area determined by Heron's formula. Simple math formulas are one case where single-letter variable names are appropriate.

The `math` package has a `sqrt` function. Import it at the top of your program (right after the initial docstring comment) using
```
from math import sqrt
```


### Binet's Formula

<img src="https://lp-cms-production.imgix.net/2019-09/ab57ac3775d90a72da514d158401bd47-parthenon.jpg" width="35%" />

*much columns  such proportions*


Recall the famous Fibonacci sequence, where each term is the sum of the previous two terms.
```
0, 1, 1, 2, 3, 5, 8, 13, 21, ...
```
Suppose you would like to calculate the Nth Fibonacci number. How could you do that? One way is to start at the base case and grind your way up through the sequence until you've calculated N total terms. 

It turns out there is a single formula that will calculate the terms of the Fibonacci sequence. This is weird and suprising, because it seems unlikely that such a highly structured sequence, where each term depends on all the previous terms, could be represented in closed form. The result is known as Binet's formula and it says that the Nth Fibonacci number `F_n` is

<img src="https://latex.artofproblemsolving.com/8/6/d/86d486c560727727342090b432e23ba85ac098b1.png" width="30%"/>

The number `(1 + sqrt(5)) / 2` is the famous **golden ratio**, the most aesthetically pleasing of all proportions. It's sometimes denoted by the Greek letter φ (phi) after the ancient architect and sculptor Phidias, who used it in planning the design of the Parthenon.

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

### Personal Mad Lib

Repeat the Mad Lib program, but write our own story. It can be as long as you want, but make it at least four sentences. Make at least once sentence that includes multiple variables, as in the last sentence of "The Magic Computers".
