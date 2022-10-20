# Assignment 5: Strange Loops

<img src="https://images-na.ssl-images-amazon.com/images/I/515BFnlnNML._AC_UL900_SR615,900_.jpg" width="30%" />

## Due


## Overview


## Grading


## Problems

### Max of a list

Write a function called `list_max` that takes a list named `a` as input and finds and returns its largest element. Don't use the built-in `max` function.

Remember: this problem uses a unit test, so you need to **return** the result. Don't print anything and don't use the `input` function.


### Range of a list

Write a method called `list_range` that takes a list of numbers as input and returns the difference between the largest and smallest elements.

Tips: You need to find the largest and smallest elements in the list. Don't use the built-in `max` or `min` functions.


### Rotate a list

Write a function called `rotate_list` that takes a list and a number as input, then returns the list rotated the specified number of places. A rotation of one place moves the first element to the back of the list. A rotation of two places moves the first element to the back of the list, then the second element to the back of the list, etc.

For example,

```
rotate_list([1, 2, 3, 4], 1)
```

will return
```
[2, 3, 4, 1]
```
and
```
rotate_list([1, 2, 3, 4], 3)
```
will return
```
[4, 1, 2, 3]
```

Tips:

You can use the list's `pop` method to remove an element at a given position and get its value:
```
first_value = a.pop(0)  # remove the element at position 0
```
You can use append to stick a new element onto the end of a list
```
a.append(new_item)
```
Use a loop that combines popping and appending.

What about empty lists? Empty lists automatically evaluate to False, so you can use the following code to return immediately if the list has no elements.

```
# If a is empty there's nothing to rotate
if not a:
    return a
```

### Modified limited Fibonacci sequence

Recall the famous Fibonacci sequence, where every term is the sum of the two previous terms:

```
0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, ...
```

Write a function called `largest_fib_num` that takes a number `n` as input and returns the largest Fibonacci number greater than or equal to `n`. For example,
```
largest_fib_num(10) = 8
largest_fib_num(50) = 34
largest_fib_num(1) = 1
```
You can assume that `n` is greater than or equal to 1.

Tip:

Use a `while` loop and two variables, one to keep track of the current Fibonacci number and one for the previous number. At the beginning of the program, set

```
current = 1
prev = 0
```

then loop as long as `current <= n`. The body of the loop should update the values of `current` and `prev` to advance to the next number in th sequence.

### Primes

Write a function called is_prime that takes an integer `n` as input and returns `True` if the number is prime and `False` otherwise.

Tip

The easiest way to test if a number n is prime is to use a loop over the numbers from 2 to the square root of n. Here's a **pseudocode** example:

```
root = int(n ** .5)

for i in range(2, root + 1):

    if i divides n:
        n is not prime, return False
```

If you complete the loop and never return `False`, then `n` is prime and you can return `True` at the end of the function. Make sure that your code works correctly for 2.

Note: `int(n ** .5)` calculates the square root of n and then truncates it to an integer. `range` won't accept a decimal value as a parameter.


### Day of the year

Write a function called `day_of_the_year` that takes a `month` and `day` as input and returns the associated day of the year. Let the month by a number from 1 (representing January) to 12 (representing December). For example,

```
day_of_the_year(1, 1) = 1
day_of_the_year(2, 1) = 32
day_of_the_year(3, 1) = 60
```

You can ignbore Leap Years and assume that February has 28 days.

Tip:

Make a list with the number of days in each month:

```
days_per_month = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
```

Use a loop to add up the full number of days for all months before the one you're interested in, then add in the remaining days. For example, to find the day of the year for March 5, add up the first two entries in `days_per_month` to get the total number of days in January and February, then add in 5 more days.


### The Doomsday Algorithm

The Doomsday algorithm, developed by John Conway, is a technique for computing the day of the week of any given date.

The method relies on the fact that certain dates in each year are all guaranteed to fall on the same day of the week, which Conway calls the "Doomsday" for that year.  The most important dates that fall on the Doomsday are 4/4, 6/6, 8/8, 10/10, 12/12, and the last day of February.  Monday is the Doomsday for 2022. January 3 falls on the Doomsday in non-leap years.

To find the day of the week associated with a given date, start by finding the Doomsday for the year. Next, determine the number of days separating the date in question from one of the days which is guaranteed to fall on the Doomsday.  The distance in days modulo 7 gives the number of days of the week separating the final answer from the Doomsday.

For example, 4/14 is ten days from 4/4, one of the dates guaranteed to fall on the Doomsday.  Therefore the day of the week of 4/14 is three days from the Doomsday.  The Doomsday for 2013 is Thursday, so 4/14 falls three days after Thursday, which is a Sunday.

Write a function called `doomsday` that takes a `month` and `day` as input and returns the associated day of the week.

- Use the `day_of_the_year` function from the previous problem to convert `month` and `day` into an integer; you can do the same thing with one of the days that are known to be on the Doomsday.

- Take the difference in days modulo 7 and use that to return the correct day.


