# Hello, World!

## Writing a program that prints

Go to [trinket.io/python3](https://trinket.io/python3) to access the interactive environment we used in class. Highlight and then delete any pre-existing code in the left pane.

Click in the left pane, then type
```
print('Hello, World!')
```
This is the basic Python command to print a line of text to the output terminal. It has three important parts:

- The command `print`, which is the basic Python command to print output

- A pair of parentheses. Like a mathematical function, `print` takes an *argument*, which is enclosed in parentheses.
  
- The text string `Hello, World!`, which is the text that we want to print. Text strings in Python are enclosed in a pair of *single quotes*, to indicate that this is **literal text** that should be reproduced exactly.

Run the program by clicking the triangular Play button at the top of the editing window, then verify that `Hello, World!` appears in the righthand pane.

### Practice

Change the text enclosed in your quotes, then re-run the program to verify that the output changes.

### What about double quotes?

For now, we'll focus on using single quotes for our Python strings, but it's possible to specify text using double quotes. You can also do things like make quoted strings that contain quote characters. We'll practice doing this in the lab.

### Multiple statements

You can print more text by adding multiple print statements. For example,
```
print('Hello, CMS 120!')
print('Python is a great language.')
print('Goodbye!')
```
Modify you program to have multiple print statements, then run it and check the output.

## Comments

It's desirable to include useful comments in your programs to explain what they do and any special features or unusual techniques that you're using. I always start every program by placing a descriptive header at the top, specifying the purpose of the program.

Python uses the `#` symbol to denote a commment. Everything after the `#` is ignored by the interpreter and treated as descriptive text rather than executable program code. We'll also frequently add comments to our programs to explain the features that we're introducing. The program below includes a header comment and a summary of how the print command works.
```
# Write some print statements to produce output 

# print is the basic output command in Python
# print takes an argument in parentheses
# Literal text strings are enclosed in single quotes

print('Hello, CMS 120!')
print('Python is a great language.')
print('Goodbye!')
```

### Whitespace

Python does not care about blank lines. It's useful to think about each line of code as a sentence, like a single thought, and then group related lines together into blocks, like paragraphs, separated by a blank line. Don't cram all your code together into one unseparated block. This is ugly and hard to read.
```
# Write some print statements to produce output 
# print is the basic output command in Python
# print takes an argument in parentheses
# Literal text strings are enclosed in single quotes
print('Hello, CMS 120!')
print('Python is a great language.')
print('Goodbye!')
```
*Horizontal white space* is very important to Python. For now, all of your statements must be **left aligned** in order for the program to run. If you accidentally place an extra space at the start of a line, Python will give you an error.
```
# Write some print statements to produce output

# print is the basic output command in Python
# print takes an argument in parentheses
# Literal text strings are enclosed in single quotes

print('Hello, CMS 120!')
print('Python is a great language.')
  print('Goodbye!')   # <--- error: remove the leading spaces
```

## Errors

Dealing with errors is a normal part of programming. Rather than trying to write perfect programs every time, it's often better to start with a partially complete program and then progressively debug and improve it until it works perfectly. Don't be discouraged when you see errors in your code!

Here's an example: suppose that you accidentally forget to close one of your text strings.
```
# Write some print statements to produce output 

# print is the basic output command in Python
# print takes an argument in parentheses
# Literal text strings are enclosed in single quotes

print('Hello, CMS 120!)
print('Python is a great language.')
print('Goodbye!')
```
The editor's syntax highlighting may help you spot problems, but often you won't notice anything is wrong until you run the program. Python will produce an error message like the following:
```
  File "/tmp/sessions/ca577f0ec7f002fc/main.py", line 9
    print('Hello, CMS 120!)
          ^
SyntaxError: unterminated string literal (detected at line 9)
```
Start by looking for the line number, 9 in this case, specfying the line where Python encountered the problem. The rest of the error message gives you information on the problem and, in some cases, how to fix it. Here, `SyntaxError` means that there's a problem with the form of the program; specifically, the string on line 9 has not been terminated properly due to the missing closing quote.

### Practice

Experiment with making some more errors. Read the error message for each one and see how it explains the problem with the code.
