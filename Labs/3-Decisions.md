# Decisions

## Overview

This lab will allow you to practice writing programs that use `if` statements to implement branching.


## Setup

Create a new `Lab_3` directory and then `cd` into it.
```
mkdir Lab_3
```
```
cd Lab_3
```

Put each program into its own `.py` file. You can choose the names for each file.

## Problems

### Even-odd

Recall that Python supports a special operator, `%`, which is called the **modulus operator**. The mod operator calculates the remainder after division. For example,
```
11 % 3  is  2

13 % 4  is  1

8 % 2  is  0 (because 8 is evenly divisible by 2)

17 % 6  is  5
```
The mod operator can be used to check for divisibility. For example, suppose you want to test if an input value `n` is even. A number is even if it's evenly divisible by 2, so
```
if n % 2 == 0:
    # n is even
else:
    # n is odd
```
Write a program that reads an integer from the terminal and prints `Even` if the number is even or `Odd` if it's odd.

### Input validation


### `fortune`

There's a classic UNIX program called `fortune` that prints random messages when you run it. Let's use it as an example for installing new packages in Linux.

First, you need to update the package install, which is called `apt-get`. Run the following command **in your terminal** (not in a Python script):
```
sudo apt-get update
```
You can then install `fortune`. Enter `Y` when you're asked if you want to continue.
```
sudo apt-get install fortune
```
The program is installed into a special directory called `/usr/games`. You can run it in the terminal by typing
```
/usr/games/fortune
```
You can think of this command as telling the shell to run the program named `fortune` that's located in `/usr/games`. Run the program a few times to see a different random output each time.

#### `sudo`

Here's a side point: What is `sudo` doing in the install command? 

Linux systems have the notion of privilege levels and access control. The top level account on any system is the **superuser** or **root** account, which has the ability to make any change to anything. Regular user accounts always run with privileges below that of root. A major goal of a malicious hacker is to perform *privilege escalation* by starting with a regular account and then using exploits to gain root access.

`sudo` is `substitute user do`&mdash;it's a way to run individual commands with superuser-level privileges without actually logging in as the root account.

`apt-get` is a standard command for managing packages and installing programs on many Linux distros. It has to be run as root to make
system changes, so it's prefixed by `sudo`.

![xkcd #149](https://imgs.xkcd.com/comics/sandwich.png)


### `cowsay`

```
 ___________________________________
/ After all, all he did was string  \
| together a lot of old, well-known |
| quotations.                       |
|                                   |
\ -- H. L. Mencken, on Shakespeare  /
 -----------------------------------
        \   ^__^
         \  (oo)\_______
            (__)\       )\/\
                ||----w |
                ||     ||
```

Here's another program to install:
```
sudo apt-get install cowsay
```
Run the program in your terminal:
```
/usr/games/cowsay "Hello, world!"
```
Linux allows you to "pipe" programs together, so that the output of one becomes the input to another. Try the following command and run it multiple times:
```
/usr/games/fortune | /usr/games/cowsay
```

