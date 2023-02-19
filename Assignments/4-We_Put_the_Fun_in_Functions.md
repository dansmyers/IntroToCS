# We Put the Fun in Functions!

## Due Wednesday, March 1

## Overview

This assignment will allow you to practice writing Python functions. All of the problems require you to write code that takes inputs and **returns** results.

Use the Assignment 4 workspace on repl.it. All of the functions you need to complete are in `main.py`. Fill in the body of each function. **Don't write any code outside of any functions**.

The testing for this assignment is slightly different. We're using a new feature called **unit tests** to validate your code. A unit test simply calls a function with specified parameters and then checks that it returns the correct result.

To test your code, click on the check mark in the left side menu. It's labeled "Tests" if you hover over it. You'll see a list of all the unit tests. Click the "Run Tests" button and the testing framework will automatically run your functions and report the number of tests that you passed. If you fail a test, look at the output message, which will show the inputs and expected return value.

In order to pass the tests you must **return** a result from every function. **Do not print anything in your functions** and do not use the `input` command to read values.

## Reading

Complete the participation questions for Chapter 4 in the online ZyBook.

## Problems

### `min`

This is a warmup. I've given you a function that finds the minimum of two numbers, but it's not quite correct. Modify it and make sure you can pass its tests.

### Justify Your Existence

We have seen that you can use `+` to concatenate strings together.

```
name = 'World'
print('Hello, ' + name)  # prints Hello, World
```

You can also use `*` to repeat strings.

```
print('a' * 5)  # prints 'aaaaa'
print('spam' * 4)  # prints 'spamspamspamspam'
```

These two operations can be combined.

```
print(' ' * 5 + 'spam'*2)  # prints '     spamspam' (five spaces followed by two spams)
```

Write a function named `right_justify` that takes a string as input and returns the string padded with enough spaces in front to put its last character in **column 20** of the terminal display.


Tips:

You can use the built-in len function to get the number of characters in a string

```
length = len('spam')  # length is 4
```

If you know the length of the string, you can calculate how many spaces to put in front of it to place the last character column 20.

Remember: do not use the `input` function. The input to `right_justify` is passed as a parameter by each test. Do not print anything. `right_justify` only **returns** the padded string.


### Triple min


Write a function called `triple_min` that takes three integers `a`, `b`, and `c` as input and returns the minimum of all three.

Don't use Python's built-in `min` function. Think about how to solve this using nested if-else statements. Start by comparing `a` to `b` to discover which one is smaller.


### Heron's Formula


**Heron's formula** (named after the Greek mathematician and inventor Hero of Alexandria) is a method of calculating the area of a triangle given the lengths of its three sides. If the three side lengths are *a*, *b*, and *c*, the formula is:

<img src="https://wikimedia.org/api/rest_v1/media/math/render/svg/d138044bb9ed870dd9dc5c7c8a3c07ab1db1705d" width="20%" />


where *s* is the "semi-perimeter":

<img src="https://wikimedia.org/api/rest_v1/media/math/render/svg/08ed8a6e351198e0c4ca8d71fa2e2bc4171e9439" width="10%" />

Write a function called `heron` that takes three inputs `a`, `b`, and `c` and returns the area calculated by Heron's formula.

Remember that you do not need to print anything, take any input, or write any code outside of the function; just return the final calculated value at the end of the function body. You can use `sqrt` from the math package to calculate the square root. Import it at the top of your program.


### Reverse a Number

Here is a trickier question that has shown up on technical interviews for coding jobs.

Write a function called `reverse` that takes a three-digit non-negative integer n as input and returns the number with the digits reversed. For example,

```
reverse_num(123)
```

will return 321.

```
reverse_num(742)
```

will return 247.

Tips:

There are a number of ways to do this question. If you do some Internet research you will find answers that do it by turning the number into a string, then reversing the string. I **don't** want you to use those solutions for this problem (we haven't talked much about strings or list operations yet, which those solutions require).

Reverse the number using arithmetic. To do this, break the three digit value into its hundreds, tens, and ones digits, then reassemble the digits with their order reversed.

You can use `//` for integer division in Python 3:

```
# Isolate the 100's digit
hundreds = n // 100

# Carve off the 100's digit to get the other two digits
rest = n - (hundreds * 100)
```

For example, if `n` is 123, then `n // 100` is 1 and `rest` is 23. Think about continuing this strategy to carve off the tens and then ones digits and then reassemble them to return the result.

Make sure that you return the result as a **number**, not as a string. As in the other problems, don't print anything and don't read any input, just write the function that takes `n` as input and returns the result.


### The 1089 Trick

Amaze your friends and befuddle your adversaries!

1. Start with any three digit number that has its digits in strictly decreasing order.
2. Reverse your number.
3. Subtract the reversed number from the starting number to obtain a new number.
4. Add this new number from step 3 to its reversed version.
5. The result will always be 1089.

For example,

- Start with 753
- Reverse it to get 357
- Subtract to get 753 - 357 = 396
- Reverse 396 to get 693.
- Add to get 396 + 693 = 1089

Write a function called `magic_trick` that implements the 1089 trick given a number `n` as input.

Tips:

**NO YOU CAN'T JUST RETURN 1089 WITHOUT DOING ANY WORK**. Implement the calculations and return the final result.

It sure would be helpful if you had another function that takes a three-digit number as input and returns its reverse, wouldn't it? Why don't you call the `reverse` function you wrote in the previous problem and use it to help you solve this one?


### Leap Years

Write a function called `is_leap_year` that takes a year (expressed as an integer number) as input and returns `True` if that year is a leap year and `False` otherwise. A year is a leap year if it's divisible by 4, except for years divisible by 100, which are not leap years. Years divisible by 400 are an exception and are still leap years.

For example, 2020 was a leap year, because it was divisible by 4. 1900 was not a leap year, even though it's divisible by 4, because it's divisible by 100. 2000 was a leap year, because it's divisible by 400.

*Continue reading for fascinating background information on the history of calendars*.

Our system of leap years was originally introduced by the Julian Calendar, instituted by Julius Casesar in 46 BC, which subsequently became the dominant calendar system for the Western world until 17th and 18th Centuries. The Julian calendar recognizes that the true solar year (the time it takes the Earth to make one revolution around the Sun) is about 365.25 days.

Adding an extra day to the calendar every fourth year accounts for the additional quarter of a day and keeps the calendar aligned with the true solar year. If we did not add leap days, then the dates of the calendar would gradually drift out of alignment with the seasons.

The older Roman calendar that Caesar replaced used a basic year of 355 days. The extra days were accounted for by adding an extra "intercalary" month of 23 days in the middle of February. Yes, that's correct: They added an entire extra month in the middle of February. This system could actually have worked well, if the intercalary months were scheduled on a regular cycle. In practice, though, the addition of the extra month to a year was determined by the Pontifex, the Roman religious leader, and its scheduling was chaotic and often motivated by political factors, like extending the years in which the Pontifex's allies held important offices.

The Julian calendar worked well for many centuries, but it also contained an error: The true solar year is closer to 365.2425 days than to 365.25 days. Over time, that extra fractional .075 of a day (about 11 minutes) added up, and by the 1500's the calendar had drifted ahead by ten days.

The current calendar that we use is called the Gregorian calendar, named after Pope Gregory, who decreed its introduction in 1582. The primary motivation for reform was the belief that the date of Easter had shifted too late relative to the true spring equinox. Unlike the Jewish Passover, the timing of Easter is not based on the real lunar cycle, but rather on an algorithm (the "computus", Latin for "computation") that approximates the lunar calendar and uses the fixed date of March 21 as an estimate of the true spring equinox. By the time of Gregory, the observance of Easter had shifted about ten days later than the correct date based on the observed equinox.

The Gregorian calendar introduced the system of leap years described above, which results in an average year of 364.2425 days and 97 leap years every 400 years. The new system was quickly adopted by Catholic countries in continental Europe, but Protestant countries were holdouts. Britain and its colonies did not adopt the new calendar until 1752, which required the deletion of ten days from that year in order to bring the old-style calendar in line with the Georgian one. The Eastern Orthodox churches continue to use the Julian calendar for the timing of religious holidays, so their celebration of Easter (called Pascha in Greek) occurs later than that of the Western churches.

The Gregorian system is still not perfect: It accumulates about one day of error every 7000 years.
