# Linux and Mimir

## Overview

This lab will let you practice using the Mimir environment.

The lab has three parts:

- Working with files and directories

- Installing and running some new programs on Linux

- Writing programs and executing them in the terminal


## The Terminal and the Shell

If all of your previous experience has been on Windows or Mac OS, a Linux system may feel odd at first.

The most obvious point of departure is the *terminal*, the place where you type commands for the system to execute. Windows and Mac 
systems do have built-in terminals&mdash;it's called the Command Prompt in Windows&mdash;but they favor graphical user interfaces
(GUIs) for most tasks.

Linux systems are pretty much the opposite: most modern distributions support GUIs, but it's traditional for all serious work to be 
done in the terminal environment. Many configuration and maintenance tasks (common in the server realm) are actually easier to handle 
with typed commands than they would be with graphical menus.

The program that receives your commands, interprets them, and launches new programs is called the *shell*. The default shell program 
on most Linux systems is called `bash`.

The shell program prints a prompt for your commands, which typically identifies your username and the current working directory. On
Mimir, my prompt looks like this:

```
user@mimir: ~ > 
```

For clarity, I will just use

```
>
```

when I need to indicate a command prompt. The commands you type will appear to the right of the `>`.

## Paths and Directories

The shell program recognizes one *working directory* at any given time. This is the directory that you are currently "in" and all of 
your commands will be executed with respect to it.

Type `pwd` at the prompt to print your **present working directory**.
```
> pwd
/home/dan
```
Your output should show `/home` followed by the name you gave when you signed up for Mimir.

The Linux file system is organized as a tree, similar to the Mac or Windows file system that you're probably familiar with.
The leading `/` at the front of your `pwd` output represents the top-level **root directory**. Everything in Linux lives
below the root directory.

Every file and directory on the system has a *path* that describes its place in the file system tree. An *absolute path* gives the 
position of the object relative to the root. For example, the path

```
/home/dan/CMS_120/hello.py
```

identifies a file named `hello.py`, which resides in a directory called `CMS_120`, which is itself in a directory 
called `dan`. The `dmyers` directory is located in the `home` directory under the root, `/`. Here's a picture&mdash;I've added a
few more directories at each level to illustrate the tree structure:

```                          
                          / (the root dir)
                             |
                             |
              -----------------------------------
              |     |      |       |      |     |
              |     |      |       |      |     |
             bin   lib    home  include  etc   usr
                           |
                           |
                  ---------------------------------
                  |                 |             |
                  |                 |             |
                 dan              scott         will     
                  |
                  |
           -------------------------
           |            |          |
           |            |          |
        CMS_120       CMS_380    CMS_460
           |
           |
        hello.py
```

The top-level directories right beneath `/` are fairly standard across systems. `home` contains a series of *home directories* for
each system account. The example shows three home directories for three different users. `bin` is short for *binaries* and stores 
common executable programs.


## Creating Directories

Let's make a new directory to hold the files for this class. The `mkdir` command creates a new folder.

```
> mkdir CMS_120
```

Note that `mkdir` does not produce any output when it executes: it just creates the new directory, finishes, and then the prompt 
reappears. In the Unix world, *silence is golden*. Programs that run correctly tend to finish and exit without producing unnecessary
output.

To see the results of the command, you can **list** the contents of the current directory. The listing command is `ls`. Type it at the prompt
and see what happens:

```
> ls
```

## Change Directories

Suppose that we want to work on a file for CMS_120. The first thing to do is **change the working directory** to the `CMS_120` folder we just created.
Use the `cd` command to change directories:

```
> cd CMS_120
```

You can then check your present working directory with `pwd` and see that it has been updated.

```
> pwd
/home/dan/CMS_120
```

Let's create one more new directory to hold files for this lab and then change to it.

```
> mkdir Lab_1
> cd Lab_1
```

Again, use `pwd` to verify that your working directory is now `/home/YOURNAME/CMS_120/Lab_1`.


## Fun with Programs

### Cowsay?

Let's install a new program. **Type this command in the terminal window of your Mimir IDE**.
```
sudo apt-get install cowsay
```

Linux systems have the notion of privilege levels and access control. The top level account on any system is the **superuser** or **root** account, which has the ability to make any change to anything. Regular user accounts always run with privileges below that of root.

`sudo` is `substitute user do`&mdash;it's a way to run individual commands with superuser-level privileges without actually logging in as the root account.

`apt-get` is a standard command for managing packages and installing programs on many Linux distros. It has to be run as root to make
system changes, so it's prefixed by `sudo`.

![xkcd #149](https://imgs.xkcd.com/comics/sandwich.png)

Run the program:

```
cowsay "Hello, Friend!"
```

Make the cow say a few different things.

### The Man Pages (Not a Dating Site)

To get more information on a system command, consult its manual page using the `man` command.
```
man cowsay
```    
This brings up a description of the `cowsay` command, including discussion of its optional flags and arguments.

Use the arrow keys to scroll and **press `q` to quit the viewer**.

`cowsay` can take on several optional arguments, which are called **flags**. For example, to make a dead cow, supply the `-d` flag:

```
cowsay -d "Hello, Friend!"
 _______________
< Hello, Friend >
 ---------------
        \   ^__^
         \  (xx)\_______
            (__)\       )\/\
             U  ||----w |
                ||     ||
```
    
You can also use a different image file with the `-f` flag:

```
cowsay -f dragon "Extra crispy!"
```

### Fortunate Cows

Install another silly program:
```
sudo apt-get install fortune
```
`fortune` prints sayings&mdash;some profound, some not&mdash;to the console. You can have some fun by **piping** the output of `fortune` to the input of `cowsay`.

```
fortune | cowsay
```

A **pipe** is a connection between two processes. The output of one end of the pipe becomes the input to the other end. In this example, the output of `fortune`, which would ordinarily go to the console, is redirected to the `cowsay` program instead, which then uses it as input and prints an oracular cow.

Pipes are a common tool in the Unix world: they allow you to chain small, simple programs together to accomplish complex feats of text processing.

## Let's Write Some Code

The final part of this lab will show you to create and run programs in the Mimir terminal.

The easiest way to create a file is to `touch` it. Suppose we want to create a new Python script named `hello.py`:

```
> touch hello.py
```

You can then **open** the file for editing using the `open` command:

```
> open hello.py
```

The command will bring up a blank window, which represents the brand-new `hello.py` file. Type some print statements into the file:

```
# A short script to print output

print('Hello, friends.')
print('I am so happy to meet you.')
```

**Save your program**. The easiest way to save is by pressing `CTRL + s` (or `Command + s` on Mac). Look at the `hello.py` tab at the top of your Mimir window. If you have
**unsaved changes** the tab will show an orange circle. Save the file and the circle will disappear. **Forgetting to save is a common mistake**, but one that's easy to 
fix: Just go back in the editor, save your program, and then run it again.

Let's run the program at the command prompt. Use `python3` to run a `.py` script:

```
> python3 hello.py
```

You should see the print statements you wrote in the script output to the terminal window. Take a few minutes and experiment with printing some different strings and
arithmetic expressions. Re-run the program each time and see that your results are reflected in the output.

When you're ready, try writing new scripts that answer the following questions.

## Practice Questions

### McChocolate Potatoes

The Japanese yen currently trades for about $.0097.

I'm a sucker for regional fast food items. It turns out that you ~can~ could get **chocolate fries** at [McDonald's in Japan](https://www.eater.com/2016/1/19/10790586/mcdonalds-chocolate-fries-japan) (they are officially known
as "McChocolate Potatoes"). Are they any good? Maybe not, but they cost only 330 yen as a side item.

<img src="https://cdn.vox-cdn.com/thumbor/WMJG04bu5nCmDiQ5mh0_chXelTY=/247x0:787x405/1820x1213/filters:focal(247x0:787x405):format(webp)/cdn.vox-cdn.com/uploads/chorus_image/image/48592139/McDonald_s_Chocolate_Fries.0.0.jpg" width="50%" />

What is the cost of a side of chocolate fries in dollars?

Note: 

- Create a new file named `fries.py` to hold your program.

```
> touch fries.py
> open fries.py
```

- You only need to write one line that uses a `print` statement to display the result of the calculation.

```
# Cost of a side of chocolate fries in dollars

print(330 * .0097)
```

### Pool Party

I love problems that ask you to convert normal units into ridiculous units.

The world's largest swimming pool is at the San Alfonso del Mar resort in Chile. It measures 3323 feet long, covers 20 acres, and contains about 66 million US gallons of water.

<img src="https://twistedsifter.files.wordpress.com/2012/05/san-alfonso-del-mar-aerial-satellite-from-above-algarrobo-chile-5.jpg" width="50%" />

A **firkin** is an old unit sometimes used to measure beer and ale in Britain. The British Imperial beer firkin is defined to be equal to 10.8 US gallons. 
Suppose we wanted to fill the San Alfonso del Mar pool with beer, ***because reasons***. How many firkins of beer would be required to accomplish this feat?
Write a program to calculate and print the answer.

Tips:

- Put your solution in a file named `pool.py`

- To enter 66 million into a program, use `66000000`. Python doesn't want commas in large numbers.

- You have a number of gallons and need to convert to firkins. In this case, you need to **divide** 66 million by 10.8. Use `/` for the division operator.

### Smoots

Use all of your powers to answer the following question.

Oliver R. Smoot is an MIT graduate and former head of the American National Standards Institute (ANSI) and the International Organization for Standards (ISO).

In 1958, as part of his initiation into ΛXA, Smoot and his brothers measured the entire length of Harvard Bridge over the Charles River in Cambridge, MA, using Smoot’s body as the ruler. He was at the time 170 cm tall (5 feet, 7 inches), and the bridge was declared to be 364.4 Smoots, "plus or minus one ear" (about 2035 feet or 650.7 meters). Since that time, the measurement of Harvard Bridge has always been denominated in Smoots, with the markings repainted each year by the incoming ΛXA pledge class at MIT. The Cambridge police use the Smoot markings to identify the location of accidents on the bridge.

<img src="https://alum.mit.edu/sites/default/files/styles/article_desktop/public/images/SMOOT.jpg?itok=jMC7rC_T" width="50%" />

The Lake Pontchartrain Causeway, which connects Metairie, a suburb of New Orleans, to Mandeville, LA, is 23.83 miles long. It holds the record for being the longest continuous bridge over water (there are longer bridges, but they are not built in one continuous span).

What is the length of the Lake Pontchartrain Causeway in Smoots?

Tip: one Smoot is about 5.5833 feet and there are 5280 feet in a mile.


## One More Thing...
Telnet is a program for establishing a remote connection to another server.

```
sudo apt-get install telnet
telnet towel.blinkenlights.nl
```

Close the terminal window to quit.
