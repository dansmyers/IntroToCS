# Writing and Running Programs

<img src="https://media.pitchfork.com/photos/5c37770817eefc510f1b3565/16:9/w_1280,c_limit/David-Bowie.jpg" width="500px" />

*David Bowie using a computer, ca. 1994*

## Overview

This lab will let you practice using the Replit environment.

The lab has two parts:

- Working with files and directories in the Linux terminal
- Writing some practice programs that use printing and calculations in Python

## Grading

Complete the activities below. When you've finished, let me know and I'll take a look at your solutions, then give you credit. Remember: Don't hestitate to ask questions if you get stuck!

- Put each program in its own file. The first questions will show you how to create and name new files. Choose names that make it clear which problem goes with each file.
- Start each program with a descriptive comment.

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

The shell program prints a prompt for your commands, which typically identifies your current working directory. On Replit, my prompt looks like this:

```
~/CMS120$
```
The commands you type will appear to the right of the `$`.

### Paths and directories

The shell program recognizes one *working directory* at any given time. This is the directory that you are currently "in" and all of 
your commands will be executed with respect to it.

Type `pwd` at the prompt and press ENTER to print your **present working directory**.
```
pwd
```
You should see something like the following:
```
/home/runner/CMS120
```
The Linux file system is organized as a tree, similar to the Mac or Windows file system that you may be familiar with.
The leading `/` at the front of your `pwd` output represents the top-level **root directory**. Everything in Linux lives
below the root directory.

Every file and directory on the system has a *path* that describes its place in the file system tree. An *absolute path* gives the 
position of the object relative to the root. For example, the path

```
/home/runner/CMS120/hello.py
```

identifies a file named `hello.py`, which resides in a directory called `CMS120`, which is itself in a directory 
called `runner`. The `runner` directory is located in the `home` directory under the root, `/`. Here's a picture&mdash;I've added a
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
                runner            scott         will     
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

The top-level directories right beneath `/` are fairly standard across systems.


### Creating directories

Let's make a new directory to hold the files for this lab. The `mkdir` command creates a new folder.

```
mkdir Lab_1
```

Note that `mkdir` does not produce any output when it executes: it just creates the new directory, finishes, and then the prompt 
reappears. In the Unix world, *silence is golden*. Programs that run correctly tend to finish and exit without producing unnecessary
output.

To see the results of the command, you can **list** the contents of the current directory. The listing command is `ls`. Type it at the prompt
and see what happens:

```
ls
```

Take a look at the output of `ls` and verify that you now have a `Lab_1` directory. You should also see `Lab_1` appear in your file browsing pane on the left side of your workspace.

### Changing directories

Suppose that we want to work on a file for this lab. The first thing to do is **change the working directory** to the `Lab_1` folder we just created.
Use the `cd` command to change directories:

```
cd Lab_1
```
You can then check your present working directory with `pwd` and see that it has been updated.
```
pwd
```
The output should show that you are now working out of the `Lab_1` directory:
```
/home/runner/CMS120/Lab_1
```

### Moving between directories

Sometimes you need to move around the directory hierarchy. You shouldn't really need to do that for a while in this class, but sometimes you can accidentally `cd` to a directory you don't want to be in.

Use `..` (two dots) to refer to the parent directory; that is, one level up in the hierarchy. You can move up to the parent directory using
```
cd ..
```

Try using `cd` to move up to the parent directory, then use `cd Lab_1` to move back to the `Lab_1` directory.

Another useful shortcut is
```
cd ~
```
which will move you automatically back to your home directory. This is useful if you don't know where you are in the directory hierarchy and need to return back to a known place.

## Problems



### McChocolate Potatoes

The Japanese yen currently trades for about $.0068.

I'm a sucker for regional fast food items. It turns out that you ~can~ could get **chocolate fries** at [McDonald's in Japan](https://www.eater.com/2016/1/19/10790586/mcdonalds-chocolate-fries-japan) (they are officially known
as "McChocolate Potatoes"). Are they any good? Maybe not, but they cost only 330 yen as a side item.

<img src="https://cdn.vox-cdn.com/thumbor/WMJG04bu5nCmDiQ5mh0_chXelTY=/247x0:787x405/1820x1213/filters:focal(247x0:787x405):format(webp)/cdn.vox-cdn.com/uploads/chorus_image/image/48592139/McDonald_s_Chocolate_Fries.0.0.jpg" width="50%" />

What is the cost of a side of chocolate fries in dollars?

Note: 

- Create a new file named `fries.py` to hold your program.
```
touch fries.py
```

- You only need to write one line that uses a `print` statement to display the result of the calculation.
```
# Cost of a side of chocolate fries in dollars

print(330 * .0068)
```

- Run the program by typing
```
python3 fries.py
```
at the shell prompt and pressing ENTER.


### Our Princess is in Another Castle

<img src="https://cdn.mobilesyrup.com/wp-content/uploads/2020/11/super-nintendo-world-scaled.jpg" width="300px" />

*Super Nintendo World Japan. Coming to Universal Orlando in a few years.*

At the end of each level of the original *Super Mario Bros.*, Mario jumps up a staircase like the following:

```
     ##
    ###
   ####
  #####
 ######
#######
```

The staircase has six levels. The bottom level has seven blocks and the top level has five spaces and two blocks.
Write a program that uses six print statements to print this staircase.

Tip: Make a new file called `mario.py` using the same steps as the previous problem.

### Haiku

<img src="https://upload.wikimedia.org/wikipedia/commons/b/bd/Kobayashi_Issa-Portrait.jpg" width="300px" />

Write a program to print the following haiku by the poet Kobayashi Issa, famous for his works focusing on insects and other small creatures.

```
O snail
Climb Mount Fuji,
But slowly, slowly!
```

Use three print statements, one for each line.

Tips:

- Match the format of the poem exactly.
- Put your code in a file named `haiku.py`


### Pool Party

<img src="https://twistedsifter.files.wordpress.com/2012/05/san-alfonso-del-mar-aerial-satellite-from-above-algarrobo-chile-5.jpg" width="300px" />


I love problems that ask you to convert normal units into ridiculous units.

The world's largest swimming pool is at the San Alfonso del Mar resort in Chile. It measures 3323 feet long, covers 20 acres, and contains about 66 million US gallons of water.

A **firkin** is an old unit sometimes used to measure beer and ale in Britain. The British Imperial beer firkin is defined to be equal to 10.8 US gallons. 
Suppose we wanted to fill the San Alfonso del Mar pool with beer, ***because reasons***. How many firkins of beer would be required to accomplish this feat?
Write a program to calculate and print the answer.

Tips:

- Put your solution in a file named `pool.py`
- To enter 66 million into a program, use `66000000`. Python doesn't want commas in large numbers.
- You have a number of gallons and need to convert to firkins. In this case, you need to **divide** 66 million by 10.8. Use `/` for the division operator.

### Smoots

<img src="https://alum.mit.edu/sites/default/files/styles/article_desktop/public/images/SMOOT.jpg?itok=jMC7rC_T" width="300px" />

Use all of your powers to answer the following question.

Oliver R. Smoot is an MIT graduate and former head of the American National Standards Institute (ANSI) and the International Organization for Standards (ISO).

In 1958, as part of his initiation into ΛXA, Smoot and his brothers measured the entire length of Harvard Bridge over the Charles River in Cambridge, MA, using Smoot’s body as the ruler. He was at the time 170 cm tall (5 feet, 7 inches), and the bridge was declared to be 364.4 Smoots, "plus or minus one ear" (about 2035 feet or 650.7 meters). Since that time, the measurement of Harvard Bridge has always been denominated in Smoots, with the markings repainted each year by the incoming ΛXA pledge class at MIT. The Cambridge police use the Smoot markings to identify the location of accidents on the bridge.

The Lake Pontchartrain Causeway, which connects Metairie, a suburb of New Orleans, to Mandeville, LA, is 23.83 miles long. It holds the record for being the longest continuous bridge over water (there are longer bridges, but they are not built in one continuous span).

What is the length of the Lake Pontchartrain Causeway in Smoots?

Tips:

- Do the entire calculation in one expression. Use two multiplications.
- One Smoot is about 5.5833 feet and there are 5280 feet in a mile.
- Put your answer in a file named `smoots.py`. Keep making new files for each of the remaining problems.

### Cricket Protein Powder

<img src="https://cdn.shopify.com/s/files/1/0904/3248/products/chocolate_front_1408x1408.jpg?v=1566244530" width="300px" />

Entomophagy is the wave of the future. Crickets are a naturally renewable (albeit noisy) resource and contain proportionally more protein than chicken or beef.

Through a totally unscientific research process, I have learned that the average cricket weighs .50 grams and consists of about 60% protein.

Consider an iron-slinging bodybuilder who wants to consume 200 grams of protein per day in order to get huge. How many crickets are required to produce that amount?


### Beards

<img src="https://upload.wikimedia.org/wikipedia/commons/8/81/Hans_Langseth.jpg" width="300px" />

The beard-second is an incredibly scientific unit of length defined as the distance an average beard grows in 1 second. Google defines the beard-second as 5 nanometers and will perform conversions between beard-seconds and other lengths (try typing “1 foot in beard-seconds” into Google). Using this definition, it would take an average beard 58.8 days to grow 1 inch.

The longest beard in the world is 17 feet long and is housed in the Smithsonian institution. In life, it belonged to Hans Langseth, who immigrated to the U.S. from Norway in 1864; he died in North Dakota in 1927. He would wrap his beard around a corncob and carry it in his pocket.


Under the (completely unrealistic) assumption that Hans Langseth grew his entire beard at the average rate of 1 inch every 58.8 days, how many days would it have taken to him to get 17 feet of facial hair? Write a Python program that **calculates and prints** the answer.


### 1 Barnum = 1 Sucker / Minute

<img src="https://petapixel.com/assets/uploads/2022/01/jonathan-the-190-year-old-tortoise-with-1886-photo.jpg" width="300px" />

P.T. Barnum was a 19th Century showman, promoter, and politician, founder of the Barnum and Bailey Circus. He’s credited with coining the saying, “There’s a sucker born every minute,” although there’s no evidence he actually said this.

Jonathan the tortoise is the oldest known living terrestrial animal. He was hatched in the Seychelles, then transported to the island of Saint Helena in the South Atlantic Ocean in 1882, where he still resides. Measurements show that he was at least 50 years old when he arrived on Saint Helena, so he must have hatched no later than 1832, giving him an estimated age of over 190 years old.

If Barnum’s alleged saying is true, how many suckers have been born during Jonathan’s life? Let’s assume that Jonathan is exactly 190 years old and that each year has 365 days (ignoring leap years). Write a Python program that calculates and prints the answer

### That's So Raven

<img src="https://upload.wikimedia.org/wikipedia/commons/6/62/Paul_Gustave_Dore_Raven14.jpg" width="300px" />

*Illustration by Gustave Doré (1884)*

Python quotes can be delimited using either double quotes, `" "`, or single quotes, `' '`. What if you want to put a literal quote inside a string? There are two ways.

First, you can use single quotes to mark the outside of the string, and use double quotes inside it, or vice-versa, depending on what kind of quote you need. For example,

```
print('Quoth the Raven "Nevermore."')
```

A second approach is to use a special character sequence, `\"`. When Python encounters the `\"` sequence in a string, it will replace it with the regular double quote, `"`.

Think of the `\` as being an "escape" character: it indicates that the following quote character should be treated differently from a regular double quote used to mark the end of a string. For example, the print statement

```
print("Quoth the Raven \"Nevermore.\"");
```

will print

```
Quoth the Raven "Nevermore."
```

Use five print statements and `\"` characters to print the *The Raven* as a limerick:

```
There once was a girl named Lenore
And a bird, and a bust, and a door
And a guy with depression
And a whole lot of questions
And the bird always says "Nevermore"
```

### String addition

Python supports the `+` and `*` operators for strings. Experiment and see what they do. For example,
```
# Adding two strings
print('hello' + 'world')

# String multiplication
print('hello' * 5)
```

### More Smoots

<img src="https://upload.wikimedia.org/wikipedia/en/thumb/9/93/Burj_Khalifa.jpg/800px-Burj_Khalifa.jpg" width="300px" />

Recall the story of Oliver R. Smoot. The Harvard Bridge (2035 feet in length) was measured to be 364.4 Smoots, "plus or minus one ear". One Smoot is about 5.5833 feet.

The Burj Khalifa in Dubai is the tallest tower in the world, measuring 2722 feet to its top spire. What is the height of the Burj Khalifa in Smoots? Add the string "plus or minus one ear" to your output, so that it looks like this:

```
X plus or minus one ear
```

where `X` is the calculated answer value.

You can use the `+` operator to combine a calculation with a string, but you have to first turn the numeric result to a string using the `str` function. For example, the Harvard Bridge calculation could look like the following:

```
# Print the length of the Harvard Bridge in Smoots, plus the additional string
print(str(2035 / 5.5833) + ' plus or minus one ear')
```

Modify this example to print the height of the Burj Khalifa in Smoots.

### Warhols

<img src="https://www.moma.org/d/assets/W1siZiIsIjIwMTUvMTAvMjEvOTY0aWFsdm96Yl9zb3VwY2FuLmpwZyJdLFsicCIsImNvbnZlcnQiLCItcXVhbGl0eSA5MCAtcmVzaXplIDIwMDB4MjAwMFx1MDAzZSJdXQ/soupcan.jpg?sha=9a38fb887eb28928" width="300px" />

The pop artist Andy Warhol said, "In the future, everyone will be world-famous for 15 minutes." Therefore, define one Warhol to be the unit for 15 minutes of world-fame.

The late Queen Elizabeth II of the United Kingdom was a very famous person. Let's suppose she became world-famous in 1936, when her father George VI ascended the throne, following the abdication of his older brother Edward VIII, who gave up being king to marry the divorced American socialite Wallis Simpson. If Queen Elizabeth was world famous for exactly 86.5 years until her death in 2022 (assuming each year has 365.25 days), how many Warhols of fame did she enjoy?

Tip: Write one expression that calculates the number of Warhols in a year times 86.5 years.


### [in Just-]

Another useful special character is `\n`, which makes the printed output move to the next line. Use `\t` to insert a tab character into a line. For example, the statement:

```
print('This is\n\ta test.');
```

will print

```
This is
    a test
```

Notice that you don't need to put spaces around the special characters.

Use multiple print statements and `\t` to print this excerpt from e.e. cummings' poem [in Just-]:

```
it's
spring
and

        the

                  goat-footed

balloonMan        whistles
far
and
wee
```

Tips:

- Use one `print` per line.
- Start by printing the first three lines, testing, then adding a little more. Develop incrementally!
- You can print a blank line using an empty print statement: `print()`
- The line with `the` has two tabs. Use `print('\t\tthe')`
- There are two tabs before `the` and four before `goat-footed`. There are two tabs between `balloonMan` and `whistles`.

