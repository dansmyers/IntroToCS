# The `for` Loop

## Topics

- Types of loops in Python
- Looping over a string
- The selector pattern
- The accumulator pattern

## Types of loops

Python has two looping keywords: `for` and `while`.

The `for` loop is used to iterate over **sequences**. The following are all examples of sequences in Python:

- The characters in a string
- A range of numbers
- The lines of file
- The values in a list

A `for` loop runs for a fixed number of iterations determined by the length of its sequence.

The `while` loop is controlled by a **boolean condition** and runs as long as its condition is `True`. It's often used for interactive programs that want to repeatedly prompt the user for input and then do something; a chatbot is a good example. The `while` loop can run for an unlimited number of iterations, as long as its condition remains `True`.

We'll start with the `for` loop and then look at the `while` loop after the Midterm exam.

## Looping over a string

A string is a sequence of characters. That is, there is a first character, a second character, and so forth. The following code assigns a string to a variable `s` and then prints out its characters one at a time.
```
s = 'queueing'

for ch in s:
    print(ch)
```
The `for` loop has the following elements:

1. The `for` keyword

2. A *loop variable*, which is used to step through the items of the sequence one at a time. Here, the loop variable is named `ch`, short for "character", but any name could be used. It's common, but not required, to use short names for loop variables. This is a case where single letter names are common.

3. The keyword `in`

4. An expression giving the sequence you want to loop over, which is the variable `s` in this case

5. A colon

6. The indented code block that is the body of the loop

The execution of the program proceeds as follows:
- On the first iteration of the loop, the loop variable `ch` is assigned the first character of `s`, which is `'q'`
- Execute the body of the loop which prints `'q'`
- Python then checks if there are more characters remaining in `s`
- There are, so we return back to the top of the loop and assign the second character, `'u'`, to `ch`
- Execute the body of the loop a second time to print `'u'`
- We then return back to the top for the third iteration, which prints `'e'`
- This process continues until all characters of `s` have been processed, at which point the loop ends and we continue with the rest of the program

The final output of this program is
```
q
u
e
u
e
i
n
g
```

## The selector pattern

A standard operation is to loop through a sequence and select out the items that have some property of interest. The example below prints the letters of `s` that are vowels.
```
s = 'queueing'

for letter in s:
    if letter in 'aeiou':
        print(letter)
```

Here, we've used `letter` as the loop variable name; remember that it can use any variable name we want. The `if` statement tests if the current value of `letter` is any of the characters a, e, i, o, or u. It's equivalent to:
```
if letter == 'a' or letter == 'e' or letter == 'i' or letter == 'o' or letter == 'u':
    print(letter)
```
The loop behaves the same as before. The first iteration assigns `letter` to be `'q'`, which is not a vowel, so it isn't printed. The second iteration assigns `letter` to `'u'`, which is vowel, and so forth. The output of the program is
```
u
e
u
e
i
```

What if we wanted to print *non-vowel* characters?  The following statement uses `not in`:
```
s = 'queueing'

for letter in s:
    if letter not in 'aeiou':
        print(letter)
```

## The accumulator pattern
A second common looping pattern is counting the number of items that have a certain property. This is common in analytics tasks.

This program uses a variable `count` to add up the number of vowels in the string. Notice that `count` is initialize to 0, **before** the loop begins.
```
s = 'queueing'

count = 0
for ch in s:
    if ch in 'aeiou':
        count += 1

print(count)
```

The first letter of `s` is `'q'`, which is not a vowel, so `count` remains 0 during the first iteration. The second iteration sets `ch` to `'u'`, which is a vowel, so count is incremented to 1. The third iteration, `ch = 'e'` is also a vowel, so count is increased to 2, and so forth. The final output is 5.

Recall that `count += 1` is short for
```
count = count + 1
```

